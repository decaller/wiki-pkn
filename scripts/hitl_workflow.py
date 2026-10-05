#!/usr/bin/env python3
"""Local, human-operated low/medium review ledger. Never publishes content."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
from datetime import datetime, timezone
from uuid import uuid4

from hybrid_quality_scorer import HybridQualityScorer

CONTENT = Path(__file__).resolve().parents[1] / "content"


class WorkflowError(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def outside_content(path):
    resolved = Path(path).expanduser().resolve()
    if resolved.is_relative_to(CONTENT.resolve()):
        raise WorkflowError("Artifact directories must be outside content, including symlink targets")
    return resolved


def save(path, state):
    path = outside_content(path)
    temporary = outside_content(path.with_name(path.name + ".tmp"))
    temporary.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def persist(run, state):
    save(run / "manifest.json", state)
    save(run / "revisions" / str(state["revision"]) / "manifest.json", state)


def read_input(path):
    path = Path(path).expanduser().absolute()
    data = path.read_bytes()
    if not data.strip():
        raise WorkflowError(f"Required input is empty: {path}")
    data.decode("utf-8")
    return {"path": str(path), "sha256": digest(data)}, data


def load(run):
    run = outside_content(run)
    state = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
    if state["risk"] not in ("low", "medium"):
        raise WorkflowError("High-risk automation is unsupported")
    return run, state


def stale(run, state, reason):
    state["status"] = "STALE"
    state["invalidation"] = {"at": now(), "reason": reason}
    for decision in state["decisions"]:
        decision["valid"] = False
    persist(run, state)


def check_bytes(run, state):
    if state["status"] == "STALE":
        return False
    records = state["inputs"] + [state["draft_snapshot"]]
    if state.get("handoff_path"):
        records.append({"path": state["handoff_path"], "sha256": state["draft_snapshot"]["sha256"]})
    for record in records:
        try:
            if state.get("handoff_path") == record["path"]:
                outside_content(record["path"])
        except WorkflowError as error:
            stale(run, state, str(error))
            return False
        try:
            matches = digest(Path(record["path"]).read_bytes()) == record["sha256"]
        except OSError:
            matches = False
        if not matches:
            stale(run, state, f"Missing or changed bytes: {record['path']}")
            return False
    return True


def new_revision(run, draft, context, sources, risk, previous=None):
    # Read every required input before creating a run or revising its ledger.
    if not sources:
        raise WorkflowError("At least one source path is required")
    inputs = []
    for kind, path in [("draft", draft), ("context", context)] + [("source", source) for source in sources]:
        record, data = read_input(path)
        record["kind"] = kind
        inputs.append(record)
        if kind == "draft":
            draft_bytes = data
    revision = previous["revision"] + 1 if previous else 1
    folder = outside_content(run / "revisions" / str(revision))
    if folder.exists():
        raise WorkflowError("Revision directory already exists; refusing overwrite")
    report = HybridQualityScorer().evaluate_document(draft_bytes.decode("utf-8"), str(draft))
    passed = report["status"] == "APPROVED"
    state = {
        "schema_version": 1, "run_id": previous["run_id"] if previous else uuid4().hex,
        "revision": revision, "risk": risk, "created_at": now(),
        "status": "HUMAN_PENDING" if passed else "PREFLIGHT_FAILED",
        "required_roles": ["editorial", "source"] if risk == "medium" else ["editorial_or_source"],
        "inputs": inputs,
        "draft_snapshot": {"path": str(folder / "draft.md"), "sha256": digest(draft_bytes)},
        "preflight": {"passed": passed, "human_approval": False, "report": report},
        "decisions": [], "handoff_path": None,
        "publication": "No publish or deploy; local handoff only",
        "identity_policy": "Local trusted operator assertions; identities are not authenticated",
    }
    folder.mkdir(parents=True)
    outside_content(folder / "draft.md").write_bytes(draft_bytes)
    save(folder / "preflight.json", state["preflight"])
    persist(run, state)
    return state


def decision(run, state, choice, reviewer, role, reason):
    if not check_bytes(run, state):
        raise WorkflowError("Approval invalidated: inputs are stale; create a fresh revision")
    if not reviewer.strip() or not reason.strip():
        raise WorkflowError("Reviewer identity and reason must be nonempty")
    if state["status"] != "HUMAN_PENDING":
        raise WorkflowError("Only a preflight-passed pending revision accepts decisions")
    if role not in ("editorial", "source"):
        raise WorkflowError("Reviewer role must be editorial or source")
    if choice == "approve" and state["risk"] == "medium":
        approvals = [item for item in state["decisions"] if item["decision"] == "approve" and item["valid"]]
        if any(item["role"] == role or item["reviewer"] == reviewer.strip() for item in approvals):
            raise WorkflowError("Medium risk requires distinct humans and one signoff per required role")
    state["decisions"].append({
        "decision": choice, "reviewer": reviewer.strip(), "role": role, "reason": reason.strip(),
        "at": now(), "revision": state["revision"], "inputs": state["inputs"],
        "draft_sha256": state["draft_snapshot"]["sha256"], "valid": True,
    })
    if choice != "approve":
        state["status"] = "REJECTED" if choice == "reject" else "NEEDS_REVISION"
    else:
        roles = {item["role"] for item in state["decisions"] if item["decision"] == "approve" and item["valid"]}
        if state["risk"] == "low" or roles == {"editorial", "source"}:
            state["status"] = "HUMAN_APPROVED"
    persist(run, state)
    return state


def resume(run, state, output):
    if not check_bytes(run, state):
        raise WorkflowError("Approval invalidated: inputs or handoff are stale")
    if state["status"] != "HUMAN_APPROVED" or not state["preflight"]["passed"]:
        raise WorkflowError("Resume requires exact-version human approval and successful preflight")
    directory = outside_content(output) if output else outside_content(run / "handoff")
    if state.get("handoff_path"):
        outside_content(state["handoff_path"])
        if output and directory != Path(state["handoff_path"]).parent:
            raise WorkflowError("Already resumed; handoff destination is fixed")
        return state
    destination = outside_content(directory / f"{state['run_id']}-r{state['revision']}-approved.md")
    receipt = outside_content(directory / (destination.stem + ".json"))
    protected = {Path(item["path"]).resolve() for item in state["inputs"] + [state["draft_snapshot"]]}
    protected.add((run / "manifest.json").resolve())
    if destination in protected or receipt in protected or destination.exists() or receipt.exists():
        raise WorkflowError("Handoff destination overlaps existing artifacts or inputs; refusing overwrite")
    directory.mkdir(parents=True, exist_ok=True)
    data = Path(state["draft_snapshot"]["path"]).read_bytes()
    with destination.open("xb") as stream:
        stream.write(data)
    state["handoff_path"] = str(destination)
    state["resumed_at"] = now()
    persist(run, state)
    save(receipt, state)
    return state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("create", "revise", "status", "decide", "resume"):
        command = commands.add_parser(name)
        command.add_argument("--run-dir", required=True)
        if name in ("create", "revise"):
            command.add_argument("--draft", required=True)
            command.add_argument("--context-file", required=True)
            command.add_argument("--source", action="append", required=True)
        if name == "create":
            command.add_argument("--risk", choices=("low", "medium"), required=True)
        if name == "decide":
            command.add_argument("--decision", choices=("approve", "reject", "needs-revision"), required=True)
            command.add_argument("--reviewer", required=True)
            command.add_argument("--role", choices=("editorial", "source"), required=True)
            command.add_argument("--reason", required=True)
        if name == "resume":
            command.add_argument("--output-dir")
    args = parser.parse_args()
    try:
        run = outside_content(args.run_dir)
        if args.command == "create":
            if run.exists():
                raise WorkflowError("Run directory already exists; use revise or a new directory")
            state = new_revision(run, args.draft, args.context_file, args.source, args.risk)
        else:
            run, state = load(run)
            if args.command == "revise":
                check_bytes(run, state)
                state = new_revision(run, args.draft, args.context_file, args.source, state["risk"], state)
            elif args.command == "status":
                check_bytes(run, state)
            elif args.command == "decide":
                state = decision(run, state, args.decision, args.reviewer, args.role, args.reason)
            elif args.command == "resume":
                state = resume(run, state, args.output_dir)
        print(json.dumps(state, ensure_ascii=False))
    except (WorkflowError, OSError, UnicodeError, KeyError, json.JSONDecodeError) as error:
        print(f"HITL blocked: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

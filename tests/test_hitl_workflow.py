"""Consumer-visible HITL lifecycle regressions; all artifacts use isolated directories."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts/hitl_workflow.py"
GOOD = "# Panduan\n\n> [!SUMMARY]\n> Orang tua membantu anak belajar melalui teladan.\n\n## Langkah\n\n- Dengarkan anak.\n- Berikan teladan.\n- Catat hasil belajar.\n"


def call(*args, ok=True):
    result = subprocess.run([sys.executable, str(CLI), *map(str, args)], capture_output=True, text=True)
    if ok:
        assert result.returncode == 0, result.stderr
        return json.loads(result.stdout)
    assert result.returncode != 0, result.stdout
    return result


def create(inputs, risk="low"):
    run, draft, context, source = inputs
    return call("create", "--run-dir", run, "--draft", draft, "--context-file", context, "--source", source, "--risk", risk)


def decide(run, decision="approve", role="editorial", reviewer="human-1"):
    return call("decide", "--run-dir", run, "--decision", decision, "--reviewer", reviewer, "--role", role, "--reason", "Checked exact draft and source")


class TestHitlWorkflow(unittest.TestCase):
    def setUp(self):
        self._temp_dir = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self._temp_dir.name)
        draft = self.tmp_path / "input.md"
        context = self.tmp_path / "context.md"
        source = self.tmp_path / "source.md"
        draft.write_text(GOOD)
        context.write_text("Sumber pendidikan; gunakan teladan, bukan hukuman.")
        source.write_text("Catatan sumber asli untuk pemeriksaan manusia.")
        self.inputs = (self.tmp_path / "run", draft, context, source)

    def tearDown(self):
        self._temp_dir.cleanup()

    def test_low_lifecycle_and_idempotent_handoff(self):
        run, draft, _, _ = self.inputs
        state = create(self.inputs)
        self.assertEqual(state["status"], "HUMAN_PENDING")
        self.assertTrue(state["preflight"]["passed"])
        call("resume", "--run-dir", run, ok=False)
        state = decide(run)
        self.assertEqual(state["status"], "HUMAN_APPROVED")
        first = call("resume", "--run-dir", run)
        handoff = Path(first["handoff_path"])
        self.assertEqual(handoff.read_bytes(), draft.read_bytes())
        before = handoff.stat().st_mtime_ns
        self.assertEqual(call("resume", "--run-dir", run)["handoff_path"], str(handoff))
        self.assertEqual(handoff.stat().st_mtime_ns, before)
        self.assertFalse(handoff.is_relative_to(ROOT / "content"))

    def test_medium_requires_both_explicit_roles(self):
        run = self.inputs[0]
        self.assertEqual(create(self.inputs, "medium")["required_roles"], ["editorial", "source"])
        self.assertEqual(decide(run)["status"], "HUMAN_PENDING")
        call("resume", "--run-dir", run, ok=False)
        self.assertEqual(decide(run, role="source", reviewer="human-2")["status"], "HUMAN_APPROVED")
        call("resume", "--run-dir", run)

    def test_negative_decision_requires_fresh_revision(self):
        for decision, status in [("reject", "REJECTED"), ("needs-revision", "NEEDS_REVISION")]:
            with self.subTest(decision=decision, status=status):
                sub_temp = tempfile.TemporaryDirectory()
                sub_path = Path(sub_temp.name)
                draft = sub_path / "input.md"
                context = sub_path / "context.md"
                source = sub_path / "source.md"
                draft.write_text(GOOD)
                context.write_text("Context")
                source.write_text("Source")
                sub_inputs = (sub_path / "run", draft, context, source)
                run = sub_inputs[0]

                create(sub_inputs)
                self.assertEqual(decide(run, decision)["status"], status)
                call("resume", "--run-dir", run, ok=False)
                call("decide", "--run-dir", run, "--decision", "approve", "--reviewer", "other", "--role", "editorial", "--reason", "Override", ok=False)
                draft.write_text(GOOD + "\n## Pemeriksaan\n\n- Diskusikan hasil.\n")
                state = call("revise", "--run-dir", run, "--draft", draft, "--context-file", context, "--source", source)
                self.assertEqual(state["revision"], 2)
                self.assertEqual(state["status"], "HUMAN_PENDING")
                self.assertEqual(state["decisions"], [])
                self.assertTrue((run / "revisions/1/manifest.json").exists())
                decide(run)
                call("resume", "--run-dir", run)
                sub_temp.cleanup()

    def test_stale_or_missing_bytes_durably_invalidate(self):
        for which in ["draft", "source", "context", "snapshot"]:
            for missing in [False, True]:
                with self.subTest(which=which, missing=missing):
                    sub_temp = tempfile.TemporaryDirectory()
                    sub_path = Path(sub_temp.name)
                    draft = sub_path / "input.md"
                    context = sub_path / "context.md"
                    source = sub_path / "source.md"
                    draft.write_text(GOOD)
                    context.write_text("Context")
                    source.write_text("Source")
                    sub_inputs = (sub_path / "run", draft, context, source)
                    run = sub_inputs[0]

                    create(sub_inputs)
                    decide(run)
                    path = {"draft": draft, "source": source, "context": context, "snapshot": run / "revisions/1/draft.md"}[which]
                    if missing:
                        path.unlink()
                    else:
                        path.write_text("changed bytes")
                    call("resume", "--run-dir", run, ok=False)
                    persisted = json.loads((run / "manifest.json").read_text())
                    self.assertEqual(persisted["status"], "STALE")
                    self.assertFalse(persisted["decisions"][0]["valid"])
                    self.assertEqual(call("status", "--run-dir", run)["status"], "STALE")
                    sub_temp.cleanup()

    def test_decision_detects_stale_sources(self):
        run, _, _, source = self.inputs
        create(self.inputs)
        source.write_text("changed")
        call("decide", "--run-dir", run, "--decision", "approve", "--reviewer", "human", "--role", "editorial", "--reason", "Reviewed", ok=False)
        self.assertEqual(call("status", "--run-dir", run)["status"], "STALE")

    def test_failed_preflight_is_not_human_approval(self):
        run, draft, _, _ = self.inputs
        draft.write_text("Di era modern ini " + "kata " * 400 + ".\n\n" + "\n".join([
            "etape archetype arketype behavioral conditioning cliftonstrengths punishment parenting permisif parenting otoriter tabula rasa."
        ] * 3))
        self.assertEqual(create(self.inputs)["status"], "PREFLIGHT_FAILED")
        call("decide", "--run-dir", run, "--decision", "approve", "--reviewer", "human", "--role", "editorial", "--reason", "Reviewed", ok=False)
        call("resume", "--run-dir", run, ok=False)

    def test_required_inputs_and_reviewer_metadata(self):
        run, draft, context, source = self.inputs
        call("create", "--run-dir", run, "--draft", draft, "--risk", "low", ok=False)
        source.unlink()
        call("create", "--run-dir", run, "--draft", draft, "--context-file", context, "--source", source, "--risk", "low", ok=False)
        self.assertFalse((run / "manifest.json").exists())
        source.write_text("source")
        create(self.inputs)
        call("decide", "--run-dir", run, "--decision", "approve", "--reviewer", " ", "--role", "editorial", "--reason", " ", ok=False)
        call("create", "--run-dir", run.parent / "high", "--draft", draft, "--context-file", context, "--source", source, "--risk", "high", ok=False)

    def test_run_and_output_path_safety_including_symlinks(self):
        run, draft, context, source = self.inputs
        alias = self.tmp_path / "corpus-link"
        alias.symlink_to(ROOT / "content", target_is_directory=True)
        for target in (ROOT / "content/hitl-forbidden", alias / "hitl-forbidden"):
            call("create", "--run-dir", target, "--draft", draft, "--context-file", context, "--source", source, "--risk", "low", ok=False)
            self.assertFalse(target.exists())
        create(self.inputs)
        decide(run)
        call("resume", "--run-dir", run, "--output-dir", alias / "hitl-forbidden", ok=False)
        self.assertFalse((alias / "hitl-forbidden").exists())

    def test_handoff_tampering_fails_closed(self):
        run = self.inputs[0]
        create(self.inputs)
        decide(run)
        result = call("resume", "--run-dir", run)
        Path(result["handoff_path"]).write_text("tampered")
        call("resume", "--run-dir", run, ok=False)
        self.assertEqual(call("status", "--run-dir", run)["status"], "STALE")

    def test_medium_cannot_self_sign_both_roles(self):
        run = self.inputs[0]
        create(self.inputs, "medium")
        decide(run)
        call("decide", "--run-dir", run, "--decision", "approve", "--reviewer", "human-1", "--role", "source", "--reason", "Reviewed", ok=False)
        self.assertEqual(call("status", "--run-dir", run)["status"], "HUMAN_PENDING")

    def test_council_output_is_explicitly_unapproved_simulation(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/llm_council.py"), "--topic", "Review simulation", "--offline"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("SIMULASI OFFLINE — BELUM DISETUJUI MANUSIA", result.stdout)

    def test_medium_revision_preserves_risk_and_old_handoff(self):
        run, draft, context, source = self.inputs
        create(self.inputs, "medium")
        decide(run)
        decide(run, role="source", reviewer="human-2")
        old = Path(call("resume", "--run-dir", run)["handoff_path"])
        old_bytes = old.read_bytes()
        revised = call("revise", "--run-dir", run, "--draft", draft, "--context-file", context, "--source", source)
        self.assertEqual(revised["risk"], "medium")
        self.assertEqual(revised["required_roles"], ["editorial", "source"])
        self.assertIsNone(revised["handoff_path"])
        self.assertEqual(old.read_bytes(), old_bytes)
        self.assertEqual(json.loads((run / "revisions/1/manifest.json").read_text())["status"], "HUMAN_APPROVED")

    def test_handoff_never_overwrites_existing_source(self):
        run, _, _, source = self.inputs
        state = create(self.inputs)
        decide(run)
        output = source.parent / "output"
        output.mkdir()
        destination = output / f"{state['run_id']}-r1-approved.md"
        destination.symlink_to(source)
        original = source.read_bytes()
        call("resume", "--run-dir", run, "--output-dir", output, ok=False)
        self.assertEqual(source.read_bytes(), original)

    def test_status_detects_stale_before_resume(self):
        run, draft, _, _ = self.inputs
        create(self.inputs)
        decide(run)
        draft.unlink()
        self.assertEqual(call("status", "--run-dir", run)["status"], "STALE")

    def test_empty_inputs_fail_closed(self):
        self.inputs[2].write_text(" ")
        call("create", "--run-dir", self.inputs[0], "--draft", self.inputs[1], "--context-file", self.inputs[2], "--source", self.inputs[3], "--risk", "low", ok=False)
        self.assertFalse(self.inputs[0].exists())


if __name__ == "__main__":
    unittest.main()

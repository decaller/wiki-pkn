#!/usr/bin/env python3
"""Refresh only the managed Obsidian navigation outline in the existing peta.

The editor must provide exactly one BEGIN_OBSIDIAN_NAVIGATION /
END_OBSIDIAN_NAVIGATION comment pair outside COMPLETE_CONTENT_INDEX.
Source paths identify articles; canonical slugs come from the installed Quartz
utility, not from labels. Editorial content and the complete index stay intact.
"""

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
NAV_STRUCTURE_FILE = ROOT / "nav_structure.json"
OUTPUT_FILE = CONTENT_DIR / "Peta Navigasi Wiki PKN.md"
START = "<!-- BEGIN_OBSIDIAN_NAVIGATION -->"
END = "<!-- END_OBSIDIAN_NAVIGATION -->"


def get_all_markdown_metadata(content_dir):
    """Return a deterministic registry keyed by full content-relative .md path."""
    content_dir = Path(content_dir)
    registry = {}
    for path in sorted(content_dir.rglob("*.md"), key=lambda p: p.relative_to(content_dir).as_posix()):
        if not path.is_file():
            continue
        rel_path = path.relative_to(content_dir).as_posix()
        text = path.read_text(encoding="utf-8")
        frontmatter_text = ""
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
        if match:
            frontmatter_text = match.group(1)
        registry[rel_path] = {
            "stem": path.stem,
            "frontmatter": frontmatter_text,
            "rel_path": rel_path,
        }

    # Batch all paths through the real utility once. Failure is fatal: a Python
    # approximation would silently introduce a second canonical slug contract.
    result = subprocess.run(
        ["node", "--input-type=module", "-e", """
import { slugifyFilePath } from '@quartz-community/utils/path';
import { parse } from 'yaml';
let input = '';
for await (const chunk of process.stdin) input += chunk;
const rows = JSON.parse(input).map(([path, text]) => ({
  slug: slugifyFilePath(path), frontmatter: parse(text) || {}
}));
process.stdout.write(JSON.stringify(rows));
"""],
        input=json.dumps([[path, metadata["frontmatter"]] for path, metadata in registry.items()]),
        text=True, capture_output=True,
        check=True, cwd=ROOT,
    )
    for metadata, row in zip(registry.values(), json.loads(result.stdout), strict=True):
        metadata["slug"] = row["slug"]
        frontmatter = row["frontmatter"]
        metadata["title"] = frontmatter.get("title") or metadata["stem"]
        aliases = frontmatter.get("aliases") or []
        metadata["aliases"] = [aliases] if isinstance(aliases, str) else aliases
        del metadata["frontmatter"]
    return registry


def find_matching_file(title_or_slug, md_registry):
    """Resolve exact title, alias, or basename only when the identity is unique."""
    key = title_or_slug.strip().casefold()
    if key in {"home", "beranda", "beranda utama"}:
        return md_registry.get("index.md")
    matches = {
        path for path, metadata in md_registry.items()
        if key in {name.strip().casefold() for name in
                   [metadata["stem"], metadata["title"], *metadata["aliases"]]}
    }
    if len(matches) > 1:
        raise ValueError(f"Ambiguous navigation label {title_or_slug!r}: {', '.join(sorted(matches))}")
    return md_registry[next(iter(matches))] if matches else None


def build_tree_markdown(items, md_registry, indent=0):
    """Render every link with its source path; reject invalid/ambiguous targets."""
    lines = []
    prefix = "  " * indent
    for item in items:
        title = item.get("title", "")
        children = item.get("children", [])
        if "slug" in item:
            slug = item["slug"]
            matches = [metadata for metadata in md_registry.values() if metadata["slug"] == slug]
            if not isinstance(slug, str) or not slug or not matches:
                raise ValueError(f"Invalid explicit slug {slug!r} for {title!r}")
            if len(matches) != 1:
                paths = ', '.join(sorted(metadata["rel_path"] for metadata in matches))
                raise ValueError(f"Ambiguous explicit slug {slug!r}: {paths}")
            matched = matches[0]
        elif item.get("kind") == "group":
            matched = None
        else:
            matched = find_matching_file(title, md_registry)
            if matched is None and (item.get("kind") == "link" or not children):
                raise ValueError(f"Unresolved navigation label {title!r}; supply an exact canonical slug")
        if matched:
            target = matched["rel_path"][:-3]
            lines.append(f"{prefix}- [[{target}|{title}]]")
        else:
            lines.append(f"{prefix}- **{title}**")
        if children:
            lines.extend(build_tree_markdown(children, md_registry, indent + 1))
    return lines


def render_navigation(nav_structure, md_registry):
    """Render all collections in manifest order, including structural groups."""
    sections = []
    for collection_id, collection in nav_structure.items():
        name = collection.get("name") or (collection.get("collection", {}).get("name") if isinstance(collection.get("collection"), dict) else None) or collection_id
        lines = build_tree_markdown(collection.get("structure", []), md_registry)
        sections.append(f"## {name}\n\n" + "\n".join(lines))
    return "\n\n".join(sections)


def generate_navigation_page():
    page = Path(OUTPUT_FILE)
    # Bytes avoid newline normalization outside the managed range.
    text = page.read_bytes().decode("utf-8")
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("Expected exactly one navigation marker pair; no content was written")
    start = text.index(START)
    end = text.index(END)
    if start >= end:
        raise ValueError("Navigation markers are reversed; no content was written")
    complete_start = "<!-- BEGIN_COMPLETE_CONTENT_INDEX -->"
    complete_end = "<!-- END_COMPLETE_CONTENT_INDEX -->"
    if (complete_start in text[start:end] or complete_end in text[start:end]
            or text.rfind(complete_start, 0, start) > text.rfind(complete_end, 0, start)):
        raise ValueError("Navigation markers overlap COMPLETE_CONTENT_INDEX; no content was written")
    with Path(NAV_STRUCTURE_FILE).open(encoding="utf-8") as manifest:
        nav_structure = json.load(manifest)
    registry = get_all_markdown_metadata(CONTENT_DIR)
    outline = render_navigation(nav_structure, registry)
    updated = text[:start + len(START)] + "\n" + outline + "\n" + text[end:]
    if updated != text:
        page.write_bytes(updated.encode("utf-8"))
    print(f"Updated managed navigation in {page}")


if __name__ == "__main__":
    generate_navigation_page()

#!/usr/bin/env python3
"""Refresh the complete, path-keyed index in the existing navigation hub.

Run after adding, renaming, or removing published content:
    python3 scripts/update_content_index.py
The thematic/editorial sections outside the managed block are preserved.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
PAGE = CONTENT / "Peta Navigasi Wiki PKN.md"
START = "<!-- BEGIN_COMPLETE_CONTENT_INDEX -->"
END = "<!-- END_COMPLETE_CONTENT_INDEX -->"
EXTENSIONS = {".md": "Artikel", ".canvas": "Canvas", ".base": "Bases"}


def label(path):
    title = path.stem
    if path.suffix == ".md":
        text = path.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            frontmatter = text.split("---", 2)[1]
            match = re.search(r"^title:\s*(.+)$", frontmatter, re.MULTILINE)
            if match:
                title = match.group(1).strip().strip("\"'")
    return title.replace("|", "—").replace("[", "(").replace("]", ")").replace("\n", " ")


def render():
    files = sorted((p for p in CONTENT.rglob("*") if p.is_file() and p.suffix in EXTENSIONS),
                   key=lambda p: p.relative_to(CONTENT).as_posix().casefold())
    tree = {}
    for path in files:
        node = tree
        for folder in path.relative_to(CONTENT).parts[:-1]:
            node = node.setdefault(folder, {})
        node[path.name] = path
    counts = {ext: sum(p.suffix == ext for p in files) for ext in EXTENSIONS}
    lines = [START, "## Indeks Lengkap Seluruh Konten", "",
             f"**{counts['.md']} halaman Markdown**, **{counts['.canvas']} canvas**, dan **{counts['.base']} Bases** berdasarkan berkas di `content/`.", "",
             "Susunan mengikuti folder sumber. Setiap berkas memiliki satu tautan dengan jalur lengkap, termasuk halaman indeks folder. Gunakan daftar isi halaman untuk melompat antarbagian. Gambar, audio, PDF, dan lampiran lainnya diakses melalui artikel terkait; berkas tersebut bukan halaman artikel.", "",
             "Indeks ini diperbarui dengan `python3 scripts/update_content_index.py` setelah penambahan, pemindahan, atau penghapusan konten. Bagian tematik di atas tetap menjadi panduan membaca, bukan inventaris lengkap.", ""]

    def walk(node, depth=0):
        for name, value in sorted(node.items(), key=lambda item: (isinstance(item[1], dict), item[0].casefold())):
            if isinstance(value, dict):
                if depth == 0:
                    lines.extend(["", f"### {name}", ""])
                    walk(value, 0 + 1)
                else:
                    lines.append("  " * (depth - 1) + f"- **{name}**")
                    walk(value, depth + 1)
            else:
                relative = value.relative_to(CONTENT).as_posix()
                target = relative[:-3] if value.suffix == ".md" else relative
                suffix = " — " + EXTENSIONS[value.suffix] if value.suffix != ".md" else ""
                lines.append("  " * max(0, depth - 1) + f"- [[{target}|{label(value)}]]{suffix}")
    walk(tree)
    lines.extend(["", END])
    return "\n".join(lines), len(files)


def main():
    text = PAGE.read_text(encoding="utf-8")
    block, count = render()
    if START in text:
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        text = before + block + after
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    PAGE.write_text(text, encoding="utf-8")
    print(f"Indexed {count} content pages in {PAGE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

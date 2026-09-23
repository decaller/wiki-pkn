import json
import os
import re
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT_DIR / "content"

class TestNavStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_files = []
        for root, _, files in os.walk(CONTENT_DIR):
            for f in sorted(files):
                if f.endswith(".md"):
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, CONTENT_DIR)
                    slug = rel[:-3]
                    title = ""
                    aliases = []
                    with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                        txt = fh.read()
                        m = re.search(r"^title:\s*[\"']?(.*?)[\"']?$", txt, re.M)
                        if m:
                            title = m.group(1).strip()
                        m_al = re.search(r"^aliases:\s*\n((?:\s*-\s*.*\n)+)", txt, re.M)
                        if m_al:
                            for line in m_al.group(1).splitlines():
                                line = line.strip()
                                if line.startswith("-"):
                                    aliases.append(line[1:].strip().strip("\"'"))
                    cls.all_files.append({"slug": slug, "title": title, "aliases": aliases, "rel": rel})

        cls.slug_map = {}
        for f in cls.all_files:
            if f["title"]:
                cls.slug_map[f["title"].lower().strip()] = f["slug"]
            for al in f["aliases"]:
                cls.slug_map[al.lower().strip()] = f["slug"]
            parts = f["slug"].split("/")
            last = parts[-1]
            cls.slug_map[last.lower()] = f["slug"]
            if last == "index" and len(parts) > 1:
                cls.slug_map[parts[-2].lower()] = f["slug"]

    @staticmethod
    def slugify(s):
        s = s.lower().strip()
        s = re.sub(r"[^\w\s-]", "", s)
        s = re.sub(r"[\s_-]+", "-", s)
        s = re.sub(r"^-+|-+$", "", s)
        return s

    def resolve(self, title):
        t_low = title.lower().strip()
        if t_low in ["home", "beranda", "beranda utama"]:
            return "index"
        if t_low in self.slug_map:
            return self.slug_map[t_low]
        tb = re.match(r"^0?(\d{1,2})[\.\s\-]", title)
        if tb:
            num = tb.group(1).zfill(2)
            for f in self.all_files:
                last = f["slug"].split("/")[-1]
                if last.startswith(f"{num}-") and "tb40" in f["slug"].lower():
                    return f["slug"]
        st = self.slugify(title)
        if st in self.slug_map:
            return self.slug_map[st]
        for f in self.all_files:
            parts = f["slug"].split("/")
            last = parts[-1]
            prev = parts[-2] if len(parts) > 1 else ""
            if last == st or last == st + "-pkn" or (last == "index" and prev == st):
                return f["slug"]
        for f in self.all_files:
            f_title = f["title"].lower().strip()
            if f_title and t_low in f_title:
                return f["slug"]
            if st in f["slug"]:
                return f["slug"]
        return None

    def test_nav_structure_integrity(self):
        nav_file = ROOT_DIR / "nav_structure.json"
        self.assertTrue(nav_file.exists(), "nav_structure.json must exist")

        with open(nav_file, "r", encoding="utf-8") as fh:
            nav = json.load(fh)

        root_key = list(nav.keys())[0]
        structure = nav[root_key]["structure"]

        def traverse(items, path=""):
            nodes = []
            for it in items:
                cur_path = f"{path} > {it['title']}" if path else it["title"]
                slug = self.resolve(it["title"])
                is_leaf = not bool(it.get("children"))
                nodes.append({
                    "path": cur_path,
                    "title": it["title"],
                    "slug": slug,
                    "is_leaf": is_leaf
                })
                if it.get("children"):
                    nodes.extend(traverse(it["children"], cur_path))
            return nodes

        all_nodes = traverse(structure)
        leaves = [n for n in all_nodes if n["is_leaf"]]
        unlinked_leaves = [n for n in leaves if not n["slug"]]
        unresolved_all = [n for n in all_nodes if not n["slug"]]

        # Assertions
        self.assertEqual(len(all_nodes), 143, f"Expected 143 total nodes, got {len(all_nodes)}")
        self.assertEqual(len(leaves), 116, f"Expected 116 leaf nodes, got {len(leaves)}")
        self.assertEqual(len(unlinked_leaves), 0, f"Unlinked leaves found: {unlinked_leaves}")
        self.assertEqual(len(unresolved_all), 0, f"Unresolved nodes found: {unresolved_all}")

        # Verify physical markdown files exist
        missing_physical = []
        for n in all_nodes:
            slug = n["slug"]
            md_file = CONTENT_DIR / f"{slug}.md"
            idx_file = CONTENT_DIR / slug / "index.md"
            if not md_file.exists() and not idx_file.exists():
                missing_physical.append((n["path"], slug))

        self.assertEqual(len(missing_physical), 0, f"Missing physical files for nodes: {missing_physical}")

if __name__ == "__main__":
    unittest.main()

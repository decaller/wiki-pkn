import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import generate_obsidian_navigation as nav


class TestNavStructure(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.content = Path(self.temp.name)

    def article(self, path, text=""):
        file = self.content / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding="utf-8")

    def registry(self):
        return nav.get_all_markdown_metadata(self.content)

    def test_home_and_nested_indexes_keep_separate_identities(self):
        for path in ("index.md", "A/index.md", "B/index.md"):
            self.article(path)
        registry = self.registry()
        self.assertEqual(set(registry), {"index.md", "A/index.md", "B/index.md"})
        self.assertEqual(nav.find_matching_file("Home", registry)["rel_path"], "index.md")
        lines = nav.build_tree_markdown([
            {"title": "Home"},
            {"title": "A", "slug": "a/index"},
            {"title": "B", "slug": "b/index"},
        ], registry)
        self.assertEqual(lines, ["- [[index|Home]]", "- [[A/index|A]]", "- [[B/index|B]]"])

    def test_title_and_alias_are_frontmatter_only(self):
        self.article("Folder/Source.md", '---\ntitle: "Judul: tepat"\naliases: [Nama, "Nama lain"]\n---\ntitle: Bukan metadata\n')
        registry = self.registry()
        for label in ("Judul: tepat", "Nama", "Nama lain", "Source"):
            self.assertEqual(nav.find_matching_file(label, registry)["rel_path"], "Folder/Source.md")
        self.assertIsNone(nav.find_matching_file("Bukan metadata", registry))
        self.assertIsNone(nav.find_matching_file("Judul", registry))

    def test_ambiguous_alias_title_and_basename_never_choose_first(self):
        self.article("A/Same.md", "---\ntitle: Shared\naliases:\n  - Collision\n---\n")
        self.article("B/Same.md", "---\ntitle: Collision\naliases: [Shared]\n---\n")
        registry = self.registry()
        for label in ("Collision", "Shared", "Same"):
            for ordered in (registry, dict(reversed(list(registry.items())))):
                with self.subTest(label=label), self.assertRaisesRegex(ValueError, "Ambiguous"):
                    nav.find_matching_file(label, ordered)
        self.assertIsNone(nav.find_matching_file("Sam", registry))
        with self.assertRaisesRegex(ValueError, "Unresolved"):
            nav.build_tree_markdown([{"title": "Sam"}], registry)

    def test_explicit_slug_is_exact_and_overrides_label(self):
        self.article("A/First.md", "---\ntitle: Same\n---\n")
        self.article("B/Second.md", "---\ntitle: Same\n---\n")
        registry = self.registry()
        self.assertEqual(nav.build_tree_markdown([{"title": "Same", "slug": "b/second"}], registry),
                         ["- [[B/Second|Same]]"])
        for slug in ("B/Second", "b/second.md", "b/second/", "missing", "", None):
            with self.subTest(slug=slug), self.assertRaisesRegex(ValueError, "Invalid explicit slug"):
                nav.build_tree_markdown([{"title": "First", "slug": slug}], registry)

    def test_canonical_slug_uses_source_path_not_title_slugify(self):
        self.article("Arsitektur PKN/00 - Master & Fitrah (Anak).md", "---\ntitle: Label berbeda\n---\n")
        self.article("Folder/Folder.md")
        self.article("Folder/_index.md")
        registry = self.registry()
        slug = "arsitektur-pkn/00---master--and--fitrah-(anak)"
        self.assertEqual(nav.build_tree_markdown([{"title": "Label", "slug": slug}], registry),
                         ["- [[Arsitektur PKN/00 - Master & Fitrah (Anak)|Label]]"])
        # Quartz maps both folder/name and _index to index; neither may win.
        with self.assertRaisesRegex(ValueError, "Ambiguous explicit slug"):
            nav.build_tree_markdown([{"title": "Folder", "slug": "folder/index"}], registry)

    def test_all_collections_and_groups_render_in_manifest_order(self):
        self.article("A/One.md")
        self.article("B/Two.md")
        self.article("Section.md")
        structure = {
            "first": {"name": "Pertama", "structure": [{"title": "One", "slug": "a/one"}]},
            "second": {"name": "Kedua", "structure": [
                {"title": "Section", "kind": "group", "children": [{"title": "Two", "slug": "b/two"}]},
            ]},
        }
        self.assertEqual(nav.render_navigation(structure, self.registry()),
                         "## Pertama\n\n- [[A/One|One]]\n\n## Kedua\n\n- **Section**\n  - [[B/Two|Two]]")

    def test_writer_preserves_editorial_and_complete_index_and_is_idempotent(self):
        self.article("index.md")
        page = self.content / "Peta.md"
        before = "---\ntitle: Editorial\n---\n\nPengantar manual\n"
        after = "\nCatatan manual\n<!-- BEGIN_COMPLETE_CONTENT_INDEX -->\n[[A/index|Indeks]]\n<!-- END_COMPLETE_CONTENT_INDEX -->\n"
        page.write_text(before + nav.START + "\nLama\n" + nav.END + after, encoding="utf-8")
        manifest = self.content / "nav.json"
        manifest.write_text(json.dumps({"main": {"name": "Utama", "structure": [{"title": "Home"}]}}), encoding="utf-8")
        with patch.object(nav, "CONTENT_DIR", self.content), patch.object(nav, "NAV_STRUCTURE_FILE", manifest), patch.object(nav, "OUTPUT_FILE", page):
            nav.generate_navigation_page()
            expected = before + nav.START + "\n## Utama\n\n- [[index|Home]]\n" + nav.END + after
            self.assertEqual(page.read_text(encoding="utf-8"), expected)
            nav.generate_navigation_page()
            self.assertEqual(page.read_text(encoding="utf-8"), expected)

    def test_missing_duplicate_reversed_or_overlapping_markers_reject_without_write(self):
        self.article("index.md")
        manifest = self.content / "nav.json"
        manifest.write_text(json.dumps({"main": {"structure": [{"title": "Home"}]}}), encoding="utf-8")
        page = self.content / "Peta.md"
        for text in ("Editorial only", nav.END + nav.START, nav.START + nav.START + nav.END,
                     nav.START + nav.END + nav.END,
                     "<!-- BEGIN_COMPLETE_CONTENT_INDEX -->" + nav.START + nav.END + "<!-- END_COMPLETE_CONTENT_INDEX -->",
                     nav.START + "<!-- BEGIN_COMPLETE_CONTENT_INDEX -->x<!-- END_COMPLETE_CONTENT_INDEX -->" + nav.END):
            page.write_text(text, encoding="utf-8")
            with self.subTest(text=text), patch.object(nav, "CONTENT_DIR", self.content), patch.object(nav, "NAV_STRUCTURE_FILE", manifest), patch.object(nav, "OUTPUT_FILE", page):
                with self.assertRaisesRegex(ValueError, "marker|overlap"):
                    nav.generate_navigation_page()
                self.assertEqual(page.read_text(encoding="utf-8"), text)

    def test_invalid_explicit_slug_does_not_modify_page(self):
        self.article("index.md")
        page = self.content / "Peta.md"
        original = nav.START + "\nEditorial\n" + nav.END
        page.write_text(original, encoding="utf-8")
        manifest = self.content / "nav.json"
        manifest.write_text(json.dumps({"main": {"structure": [{"title": "Home", "slug": "missing"}]}}), encoding="utf-8")
        with patch.object(nav, "CONTENT_DIR", self.content), patch.object(nav, "NAV_STRUCTURE_FILE", manifest), patch.object(nav, "OUTPUT_FILE", page):
            with self.assertRaisesRegex(ValueError, "Invalid explicit slug"):
                nav.generate_navigation_page()
        self.assertEqual(page.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()

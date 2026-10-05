import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = ROOT / "public"
HEAD_TSX = ROOT / "quartz/components/Head.tsx"


class TestCanonicalAndSitemap(unittest.TestCase):
    def test_head_tsx_uses_simplify_slug(self):
        """Ensure Head.tsx uses simplifySlug to avoid /index canonical mismatches."""
        content = HEAD_TSX.read_text(encoding="utf-8")
        self.assertIn("simplifySlug", content)
        self.assertRegex(content, r"simplifySlug\s*\(\s*fileData\.slug")

    def test_canonical_and_sitemap_root_consistency(self):
        """Ensure public/index.html canonical matches sitemap.xml root loc."""
        index_html = PUBLIC_DIR / "index.html"
        sitemap_xml = PUBLIC_DIR / "sitemap.xml"

        if not index_html.exists() or not sitemap_xml.exists():
            self.skipTest("Quartz build output not present, skipping build artifact test.")

        index_content = index_html.read_text(encoding="utf-8")
        sitemap_content = sitemap_xml.read_text(encoding="utf-8")

        # Canonical tag in index.html
        canonical_match = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', index_content)
        self.assertIsNotNone(canonical_match, "index.html must have a canonical link")
        canonical_url = canonical_match.group(1)

        # Must not end with /index
        self.assertFalse(canonical_url.endswith("/index"), f"Canonical URL should not end with /index: {canonical_url}")
        self.assertTrue(canonical_url.endswith("/"), f"Root canonical URL should end with /: {canonical_url}")

        # Sitemap must contain this exact canonical URL
        expected_sitemap_loc = f"<loc>{canonical_url}</loc>"
        self.assertIn(expected_sitemap_loc, sitemap_content, f"Sitemap must contain {expected_sitemap_loc}")

    def test_no_lingering_slash_index_canonical_in_public(self):
        """Ensure no html file in public contains href=.../index as canonical."""
        if not PUBLIC_DIR.exists():
            self.skipTest("Public dir not present.")

        erroneous_files = []
        for html_file in PUBLIC_DIR.rglob("*.html"):
            # Skip 404
            if html_file.name == "404.html":
                continue
            text = html_file.read_text(encoding="utf-8", errors="ignore")
            if re.search(r'<link\s+rel="canonical"\s+href="[^"]+/index"', text):
                erroneous_files.append(str(html_file.relative_to(PUBLIC_DIR)))

        self.assertEqual(len(erroneous_files), 0, f"Found files with /index canonical: {erroneous_files[:5]}")


if __name__ == "__main__":
    unittest.main()

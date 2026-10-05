import os
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONNAIRE_PATH = ROOT / "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md"
TB40_DIR = ROOT / "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/TB40"


class TestTB40QuestionnaireMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assertTrue(QUESTIONNAIRE_PATH.exists(), f"File not found: {QUESTIONNAIRE_PATH}")
        cls.content = QUESTIONNAIRE_PATH.read_text(encoding="utf-8")

    def test_section_2_contains_40_alphabetical_items(self):
        """Verify Section 2 has 40 numbered items from 1 to 40."""
        # Match table rows: | **1** | **‘Adaalah / ...** | ...
        row_pattern = re.compile(r"^\|\s*\*\*(\d{1,2})\*\*\s*\|\s*\*\*([^\*\|]+)\*\*\s*\|", re.MULTILINE)
        matches = row_pattern.findall(self.content)
        self.assertGreaterEqual(len(matches), 40, f"Expected at least 40 items, found {len(matches)}")
        
        # Take first 40 matches from section 2
        items = {}
        for num_str, name in matches[:40]:
            num = int(num_str)
            items[num] = name.strip()

        self.assertEqual(len(items), 40, "Should have exactly 40 unique numbered items")
        self.assertEqual(set(items.keys()), set(range(1, 41)), "Numbers should be 1 to 40")
        
        # Check specific critical items found during persona audit
        self.assertIn("rahmah", items[29].lower(), "Item 29 must be Rahmah")
        self.assertIn("syajaa", items[35].lower(), "Item 35 must be Syajaa'ah")
        self.assertIn("munaafasah", items[22].lower(), "Item 22 must be Munaafasah")
        self.assertIn("juud", items[19].lower(), "Item 19 must be Juud")

    def test_section_3_scoring_matrix_complete_and_accurate(self):
        """Verify Section 3 maps all 40 items to the 6 Rumpun Bakat without collision."""
        # Find all occurrences of Butir X in the scoring tables
        butir_pattern = re.compile(r"\|\s*Butir\s*(\d{1,2})\s*\|")
        found_butir = [int(m) for m in butir_pattern.findall(self.content)]
        
        self.assertEqual(len(found_butir), 40, f"Section 3 must contain exactly 40 Butir mappings, found {len(found_butir)}")
        self.assertEqual(set(found_butir), set(range(1, 41)), "All numbers 1..40 must be mapped uniquely")

    def test_tb40_article_links_exist(self):
        """Verify all TB40 markdown articles linked in the scoring table exist."""
        link_pattern = re.compile(r"\[\[(\d{2}-[a-z\-]+)\|")
        links = link_pattern.findall(self.content)
        self.assertEqual(len(links), 40, f"Expected 40 TB40 article links, found {len(links)}")
        
        for slug in links:
            file_path = TB40_DIR / f"{slug}.md"
            self.assertTrue(file_path.exists(), f"Target TB40 article does not exist: {file_path}")

    def test_no_deprecated_bakat_names_in_scoring(self):
        """Ensure no obsolete non-canonical bakat names (Hirmaan, Ziyaadah, Hamaasah, etc.) exist in Section 3."""
        deprecated = ["Hirmaan", "Ziyaadah", "Hamaasah", "Iqnaa'", "Hifzh", "Tatsabbut", "Ta'ammul", "Ta'alluf", "Tasyji'", "Shulh", "Karam"]
        
        sec3_start = self.content.find("## 3. Matriks Pengelompokan 6 Rumpun Bakat")
        sec4_start = self.content.find("## 4. Analisis Profil & Interpretasi Hasil")
        self.assertNotEqual(sec3_start, -1)
        self.assertNotEqual(sec4_start, -1)
        sec3_text = self.content[sec3_start:sec4_start]
        
        for dep in deprecated:
            self.assertNotIn(dep, sec3_text, f"Deprecated bakat name '{dep}' should not be in Section 3")


if __name__ == "__main__":
    unittest.main()

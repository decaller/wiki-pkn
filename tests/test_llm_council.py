import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPT = ROOT_DIR / "scripts" / "llm_council.py"

sys.path.insert(0, str(ROOT_DIR / "scripts"))
from llm_council import (
    ADVISOR_PROFILES,
    LLMCouncilEngine,
    format_markdown_verdict
)


class TestLLMCouncilEngine(unittest.TestCase):
    def setUp(self):
        self.engine = LLMCouncilEngine(offline_mode=True)

    def test_five_advisor_profiles_exist(self):
        self.assertEqual(len(ADVISOR_PROFILES), 5)
        expected_keys = [
            "The Contrarian (Faqih Manhaj)",
            "The First Principles Thinker (Filosof Fitrah)",
            "The Expansionist (Arsitek Peradaban)",
            "The Outsider (Pembaca Awam & Santri)",
            "The Executor (Praktisi KBM & Guru)"
        ]
        for key in expected_keys:
            self.assertIn(key, ADVISOR_PROFILES)
            self.assertIn("lens", ADVISOR_PROFILES[key])
            self.assertIn("description", ADVISOR_PROFILES[key])

    def test_stage_1_generates_five_perspectives(self):
        topic = "Batas Usia Penerapan Disiplin Shalat"
        perspectives = self.engine._generate_perspectives(topic, "")
        self.assertEqual(len(perspectives), 5)
        for name, text in perspectives.items():
            self.assertTrue(len(text) > 50, f"Perspective for {name} too short")

    def test_stage_2_anonymizes_and_creates_reviews(self):
        topic = "SOP Asrama Pesantren"
        perspectives = self.engine._generate_perspectives(topic, "")
        anonymized, mapping, reviews = self.engine._run_peer_reviews(topic, perspectives)

        # Check anonymization
        self.assertEqual(len(anonymized), 5)
        self.assertEqual(set(anonymized.keys()), {"Response A", "Response B", "Response C", "Response D", "Response E"})
        self.assertEqual(len(mapping), 5)
        self.assertEqual(len(reviews), 5)

        for rev in reviews:
            self.assertIn("reviewer", rev)
            self.assertIn("strongest_response", rev)
            self.assertIn("biggest_blind_spot", rev)
            self.assertIn("missed_by_all", rev)

    def test_stage_3_synthesizes_structured_verdict(self):
        topic = "Penyelarasan Kurikulum KOSP dengan Adab"
        res = self.engine.run_council(topic)

        verdict = res["stage_3_verdict"]
        self.assertIn("where_council_agrees", verdict)
        self.assertIn("where_council_clashes", verdict)
        self.assertIn("blind_spots_caught", verdict)
        self.assertIn("recommendation", verdict)
        self.assertIn("the_one_thing_to_do_first", verdict)

        self.assertTrue(len(verdict["where_council_agrees"]) > 0)
        self.assertTrue(len(verdict["where_council_clashes"]) > 0)
        self.assertTrue(len(verdict["blind_spots_caught"]) > 0)

    def test_markdown_formatter(self):
        topic = "Uji Karakter Santri"
        res = self.engine.run_council(topic)
        md = format_markdown_verdict(res)
        self.assertIn("Risalah Ketetapan Dewan Syura", md)
        self.assertIn("Where the Council Agrees", md)
        self.assertIn("Where the Council Clashes", md)
        self.assertIn("The Recommendation", md)
        self.assertIn("The One Thing to Do First", md)

    def test_cli_execution(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--topic", "Tes Topik Strategis", "--offline"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Risalah Ketetapan Dewan Syura", result.stdout)
        self.assertIn("Tes Topik Strategis", result.stdout)


if __name__ == "__main__":
    unittest.main()

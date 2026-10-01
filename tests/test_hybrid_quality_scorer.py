import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPT = ROOT_DIR / "scripts" / "hybrid_quality_scorer.py"

sys.path.insert(0, str(ROOT_DIR / "scripts"))
from hybrid_quality_scorer import (
    RuleBasedLinter,
    SystemOneDecisionHead,
    HybridQualityScorer,
    strip_markdown,
    extract_sentences
)


class TestRuleBasedLinter(unittest.TestCase):
    def setUp(self):
        self.linter = RuleBasedLinter(max_sentence_words=25)

    def test_clean_short_sentences(self):
        text = "Ini adalah kalimat pertama yang ringkas. Kalimat kedua juga sangat teratur dan mudah dipahami."
        res = self.linter.evaluate(text)
        self.assertEqual(res["score"], 100.0)
        self.assertEqual(len(res["violations"]), 0)

    def test_detects_prohibited_vocabulary(self):
        text = "Guru harus memahami etape perkembangan dan menerapkan reward and punishment pada santri."
        res = self.linter.evaluate(text)
        rules = [v["rule"] for v in res["violations"]]
        self.assertIn("prohibited_manhaj_vocabulary", rules)
        self.assertLess(res["score"], 100.0)

    def test_detects_overly_long_sentences(self):
        # Sentence with > 25 words
        long_sentence = " ".join(["kata"] * 30) + "."
        res = self.linter.evaluate(long_sentence)
        rules = [v["rule"] for v in res["violations"]]
        self.assertIn("sentence_length_max_25", rules)
        self.assertEqual(res["metrics"]["long_sentence_count"], 1)


class TestSystemOneDecisionHead(unittest.TestCase):
    def setUp(self):
        self.head = SystemOneDecisionHead()

    def test_inverted_pyramid_detected_with_summary_callout(self):
        content = """# Fase Tamyiz

> [!SUMMARY] Esensi 1 Menit
> Fase Tamyiz dimulai saat anak berusia tujuh tahun.

## Panduan Penerapan
Langkah pertama adalah mengajarkan shalat tanpa paksaan.
"""
        res = self.head.evaluate(content)
        self.assertEqual(res["decisions"]["inverted_pyramid"], "Yes")
        self.assertEqual(res["decisions"]["zero_fluff"], "Clean")
        self.assertEqual(res["decisions"]["scannability"], "Optimized")
        self.assertGreaterEqual(res["score"], 90.0)

    def test_zero_fluff_catches_cliche_openers(self):
        content = """# Pendidikan Karakter

Di era modern yang serba cepat dan penuh dengan godaan teknologi ini, orang tua harus waspada.
Seperti yang telah kita ketahui bersama, zaman sekarang ini sangat menantang.
"""
        res = self.head.evaluate(content)
        self.assertIn(res["decisions"]["zero_fluff"], ["Moderate Fluff", "Heavy Fluff"])
        self.assertLess(res["score"], 80.0)

    def test_scannability_catches_unchunked_walls_of_text(self):
        wall_of_text = "Ini adalah paragraf panjang tanpa jeda. " * 30
        res = self.head.evaluate(wall_of_text)
        self.assertEqual(res["decisions"]["scannability"], "Cluttered")


class TestHybridAggregator(unittest.TestCase):
    def setUp(self):
        self.scorer = HybridQualityScorer(w1=0.4, w2=0.6, pass_threshold=70.0)

    def test_well_structured_page_is_approved(self):
        content = """---
title: Panduan Adab Shalat
---

# Panduan Adab Shalat

> [!SUMMARY] Ringkasan Eksekutif
> Menumbuhkan kecintaan shalat pada anak usia tamyiz dilakukan melalui pembiasaan gembira.

## Langkah Pembiasaan
1. Ajak anak wudhu bersama dengan riang.
2. Berikan pujian tulus saat anak hadir ke masjid.

| 🔴 Kebiasaan Umum | ✅ Pendekatan PKN |
|---|---|
| Membentak saat anak terlambat | Menjadi teladan wudhu tepat waktu |
"""
        res = self.scorer.evaluate_document(content, file_path="test_page.md")
        self.assertEqual(res["status"], "APPROVED")
        self.assertGreaterEqual(res["overall_score"], 70.0)
        self.assertLess(res["execution_time_ms"], 200.0)

    def test_fluffy_long_text_needs_revision(self):
        bad_content = """# Konsep Pendidikan

Di era globalisasi yang serba canggih dan tak terbendung ini, kita harus menyadari pentingnya etape kehidupan manusia.
""" + ("Kalimat ini sangat panjang sekali dan tidak pernah berhenti sehingga melebihi batas kata yang wajar dalam sebuah paragraf yang rapi dan tertata dengan baik dalam sistem wiki. " * 5)
        res = self.scorer.evaluate_document(bad_content, file_path="bad_page.md")
        self.assertEqual(res["status"], "NEEDS_REVISION")
        self.assertLess(res["overall_score"], 70.0)
        self.assertTrue(len(res["actionable_feedback"]) > 0)

    def test_cli_execution(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--text", "# Definisi\n\n> [!SUMMARY]\n> Definisi singkat.\n\n## Sub\n- Butir 1"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("HYBRID QUALITY SCORER", result.stdout)
        self.assertIn("APPROVED", result.stdout)


if __name__ == "__main__":
    unittest.main()

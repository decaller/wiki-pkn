import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "wiki_corpus_linter.py"


class CorpusQualityGateTests(unittest.TestCase):
    def run_linter(self, pages, *flags):
        with tempfile.TemporaryDirectory() as tmp:
            content = Path(tmp) / "content"
            content.mkdir()
            for name, text in pages.items():
                destination = content / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(text, encoding="utf-8")
            report = Path(tmp) / "report.json"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--content-dir", str(content),
                 "--json-out", str(report), *flags], capture_output=True, text=True
            )
            return result.returncode, json.loads(report.read_text(encoding="utf-8"))

    def test_report_timestamp_is_current_and_timezone_aware(self):
        before = datetime.now(timezone.utc)
        status, report = self.run_linter({"index.md": "Kalimat singkat.\n"}, "--check-links")
        after = datetime.now(timezone.utc)
        self.assertEqual(status, 0)
        self.assertLessEqual(before, datetime.fromisoformat(report["timestamp"]).astimezone(timezone.utc))
        self.assertLessEqual(datetime.fromisoformat(report["timestamp"]).astimezone(timezone.utc), after)

    def test_unlinked_new_page_fails_link_gate(self):
        status, report = self.run_linter({"index.md": "Beranda.", "lepas.md": "Artikel mandiri."}, "--check-links")
        self.assertEqual(status, 1)
        self.assertEqual(report["link_integrity"]["orphan_pages"], ["lepas.md"])
        self.assertIn("orphan_pages", report["gate_failures"])

    def test_named_catalog_orphan_is_allowed(self):
        status, report = self.run_linter(
            {"index.md": "Beranda.", "Referensi/Tokoh & Pemikiran/index.md": "Katalog."},
            "--check-links",
        )
        self.assertEqual(status, 0)
        self.assertEqual(report["link_integrity"]["unexpected_orphans"], [])

    def test_short_weak_page_fails_clarity_gate_even_when_average_passes(self):
        clear = "Ini kalimat pendek. " * 40
        difficult = " ".join(["pengembangan"] * 45) + ". "
        pages = {"index.md": clear + "[[buruk]].", "buruk.md": difficult}
        status, report = self.run_linter(pages, "--check-clarity")
        self.assertEqual(status, 1)
        self.assertGreaterEqual(report["indonesian_clarity"]["average_clarity"], 60)
        self.assertIn("clarity_page_floor", report["gate_failures"])

    def test_unstyled_new_article_fails_style_gate(self):
        status, report = self.run_linter({"index.md": "Konten biasa."}, "--check-style")
        self.assertEqual(status, 1)
        self.assertIn("style_page_floor", report["gate_failures"])

    def test_known_weak_page_cannot_regress_below_baseline(self):
        status, report = self.run_linter({"Materi SOTAB.md": " ".join(["pengembangan"] * 50) + "."}, "--check-clarity")
        self.assertEqual(status, 1)
        self.assertIn("clarity_page_floor", report["gate_failures"])

    def test_scoped_links_do_not_imply_missing_style_or_clarity_failures(self):
        status, report = self.run_linter({"index.md": "[[artikel]]", "artikel.md": "Konten biasa."}, "--check-links")
        self.assertEqual(status, 0)
        self.assertEqual(report["gate_failures"], [])


if __name__ == "__main__":
    unittest.main()

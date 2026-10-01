#!/usr/bin/env python3
"""
tests/test_adversarial_content_verification.py

Empirical Challenger Test Suite for Wiki PKN Content, Links, and Vocabulary.
Authored by challenger_o5_1.

Scope:
1. Target Files Link Integrity:
   - Exhaustively extract and resolve every [[WikiLink]] across target files
     in `content/Paradigma - Implementasi PKN/` and `content/Toolkit KBM/`.
   - Ensure 0 broken links against Quartz shortest-path resolution and aliases.
2. Forbidden Vocabulary Guard:
   - Adversarial scan for prohibited terms (etape, archetype, behavioral conditioning,
     cliftonstrengths, punishment, tabula rasa, parenting permisif/otoriter, etc.).
   - Distinguish non-source usage from approved refutation context.
3. LLM Tell Pattern Detection:
   - Scan for robotic meta-announcements, fluffy adjectives, and labeled conclusions.
4. HTML/CSS Leak & Callout Syntax Audit:
   - Check for raw #hex colors in inline style attributes.
   - Check for unclosed/malformed HTML tags.
   - Check for broken callout syntax (> [!info], missing blockquote prefixes in tables).
5. R2, R3, R4 Milestone Deliverables Compliance:
   - R2: Callout contrast table format (🔴 Kebiasaan Umum vs. ✅ Pendekatan PKN)
     with >= 3 pairs per target article.
   - R3: Bank Cerita Sirah dan Apersepsi KBM 4-zone structure, 4 themes, takhrij.
   - R4: Infografis Ringkasan Materi PKN 10-concept cards in mobile-friendly WAG format.
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path
from typing import Dict, List, Set, Tuple

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.wiki_corpus_linter import (
    QuartzLinkResolver,
    VocabularyGuard,
    LLM_TELLS,
)

TARGET_PARADIGMA_FILES = [
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight/SOTABH.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tazkiyatun Nafs.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Belajar.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/Tangki Cinta.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/index.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Tujuan Hidup Manusia.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Bank Studi Kasus.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Imunitas Sosial.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md",
]

TARGET_TOOLKIT_FILES = [
    "content/Toolkit KBM/Bank Cerita Sirah dan Apersepsi KBM.md",
    "content/Toolkit KBM/Infografis Ringkasan Materi PKN Siap Sebar.md",
]

ALL_TARGET_FILES = TARGET_PARADIGMA_FILES + TARGET_TOOLKIT_FILES

R2_RETROFIT_ARTICLES = [
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Tujuan Hidup Manusia.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Belajar.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/Tangki Cinta.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Imunitas Sosial.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tazkiyatun Nafs.md",
]


class TestAdversarialContentVerification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content_dir = PROJECT_ROOT / "content"
        cls.resolver = QuartzLinkResolver(str(cls.content_dir))
        cls.vocab_guard = VocabularyGuard(str(cls.content_dir))

    def test_01_wikilinks_integrity_target_files(self):
        """Adversarially verify all internal [[WikiLinks]] in target files (0 broken links)."""
        wikilink_pattern = re.compile(r"\[\[([^\]\n]+)\]\]")
        broken_links = []
        total_links_verified = 0

        for file_rel in ALL_TARGET_FILES:
            target_path = PROJECT_ROOT / file_rel
            self.assertTrue(target_path.exists(), f"Target file must exist: {file_rel}")

            content = target_path.read_text(encoding="utf-8")
            lines = content.splitlines()

            for line_idx, line in enumerate(lines, start=1):
                # Ignore code blocks
                if line.strip().startswith("```"):
                    continue

                for match in wikilink_pattern.finditer(line):
                    total_links_verified += 1
                    raw_link = match.group(1).strip()

                    resolved = self.resolver.resolve_target(raw_link)
                    if resolved is None:
                        broken_links.append({
                            "file": file_rel,
                            "line": line_idx,
                            "raw_link": raw_link,
                        })

        print(f"\n[Test 01] Total WikiLinks verified across target files: {total_links_verified}")
        if broken_links:
            msg = f"Found {len(broken_links)} broken WikiLinks:\n"
            for b in broken_links:
                msg += f"  - {b['file']}:{b['line']} -> [[{b['raw_link']}]]\n"
            self.fail(msg)

    def test_02_forbidden_vocabulary_guard(self):
        """Adversarially scan for forbidden terms across all new/edited files."""
        scan_res = self.vocab_guard.scan_corpus()
        prohibited_terms = scan_res["prohibited_terms"]

        violations = []
        for file_rel in ALL_TARGET_FILES:
            # find matching entries in prohibited_terms
            for flagged_path, hits in prohibited_terms.items():
                if file_rel.endswith(flagged_path):
                    for h in hits:
                        violations.append({
                            "file": file_rel,
                            "line": h["line"],
                            "term": h["term"],
                            "rule": h["rule"],
                            "cluster": h["cluster"],
                            "snippet": h["snippet"],
                        })

        print(f"\n[Test 02] Prohibited vocabulary scan completed across {len(ALL_TARGET_FILES)} files.")
        if violations:
            msg = f"Found {len(violations)} prohibited vocabulary violations:\n"
            for v in violations:
                msg += f"  - {v['file']}:{v['line']} [{v['rule']}] (matched '{v['term']}'): {v['snippet']}\n"
            self.fail(msg)

    def test_03_llm_tell_patterns(self):
        """Adversarially scan for LLM tell patterns (meta-announcements, fluffy adjectives, labeled conclusions)."""
        scan_res = self.vocab_guard.scan_corpus()
        llm_tells = scan_res["llm_tells"]

        violations = []
        for file_rel in ALL_TARGET_FILES:
            for flagged_path, hits in llm_tells.items():
                if file_rel.endswith(flagged_path):
                    for h in hits:
                        violations.append({
                            "file": file_rel,
                            "line": h["line"],
                            "term": h["term"],
                            "snippet": h.get("snippet", ""),
                        })

        print(f"\n[Test 03] LLM Tell scan completed across {len(ALL_TARGET_FILES)} files.")
        if violations:
            msg = f"Found {len(violations)} LLM tell violations:\n"
            for v in violations:
                msg += f"  - {v['file']}:{v['line']} '{v['term']}': {v['snippet']}\n"
            self.fail(msg)

    def test_04_html_css_leaks_and_callout_syntax(self):
        """Adversarially audit for raw #hex colors, malformed HTML tags, and broken callouts."""
        leaks = []

        hex_in_style_pattern = re.compile(r'style="[^"]*#[0-9a-fA-F]{3,8}[^"]*"')
        unspaced_callout = re.compile(r'^>\[!')

        for file_rel in ALL_TARGET_FILES:
            target_path = PROJECT_ROOT / file_rel
            content = target_path.read_text(encoding="utf-8")
            lines = content.splitlines()

            # 1. Raw #hex in style attribute
            for line_idx, line in enumerate(lines, start=1):
                m_hex = hex_in_style_pattern.search(line)
                if m_hex:
                    leaks.append({
                        "file": file_rel,
                        "line": line_idx,
                        "type": "Raw #hex in style attribute",
                        "content": m_hex.group(0),
                    })

                # 2. Unspaced callout '> [!' instead of '> [!'
                if unspaced_callout.search(line):
                    leaks.append({
                        "file": file_rel,
                        "line": line_idx,
                        "type": "Unspaced callout syntax (> [! is required)",
                        "content": line.strip()[:80],
                    })

            # 3. HTML tag balancing check for <div>, <span>, <table>, <tr>, <td>
            for tag in ["div", "span", "table", "tr", "td", "details", "summary"]:
                open_tags = len(re.findall(rf'<{tag}\b[^>]*>', content, re.IGNORECASE))
                close_tags = len(re.findall(rf'</{tag}>', content, re.IGNORECASE))
                if open_tags != close_tags:
                    leaks.append({
                        "file": file_rel,
                        "line": 0,
                        "type": f"Mismatched <{tag}> tags",
                        "content": f"open: {open_tags}, close: {close_tags}",
                    })

        print(f"\n[Test 04] HTML/CSS and callout syntax audit completed across {len(ALL_TARGET_FILES)} files.")
        if leaks:
            msg = f"Found {len(leaks)} HTML/CSS/Callout syntax leaks:\n"
            for leak in leaks:
                msg += f"  - {leak['file']}:{leak['line']} [{leak['type']}]: {leak['content']}\n"
            self.fail(msg)

    def test_05_r2_callout_contrast_compliance(self):
        """Adversarially verify R2 callout contrast table in target Paradigma files."""
        failures = []
        for file_rel in R2_RETROFIT_ARTICLES:
            target_path = PROJECT_ROOT / file_rel
            self.assertTrue(target_path.exists(), f"File {file_rel} must exist")
            content = target_path.read_text(encoding="utf-8")

            # Check presence of callout header
            if "Refleksi Harian: Kebiasaan Umum vs. Pendekatan PKN" not in content:
                failures.append(f"{file_rel}: Missing callout 'Refleksi Harian: Kebiasaan Umum vs. Pendekatan PKN'")
                continue

            # Check table headers
            if "🔴 Kebiasaan Umum" not in content or "✅ Pendekatan PKN" not in content:
                failures.append(f"{file_rel}: Table missing contrast columns '🔴 Kebiasaan Umum' or '✅ Pendekatan PKN'")
                continue

            # Extract table rows
            table_rows = [
                line for line in content.splitlines()
                if line.strip().startswith("> |") and not line.strip().startswith("> | :---") and "🔴 Kebiasaan Umum" not in line
            ]

            if len(table_rows) < 3:
                failures.append(f"{file_rel}: Expected >= 3 contrast pairs, found {len(table_rows)}")
                continue

            # Verify no empty or dummy placeholder text
            for idx, row in enumerate(table_rows, start=1):
                cols = [c.strip() for c in row.strip("> |").split("|")]
                if len(cols) < 2:
                    failures.append(f"{file_rel}: Row {idx} has fewer than 2 columns: {row}")
                for col in cols:
                    if len(col) < 15 or "TODO" in col or "TBD" in col or "lorem ipsum" in col.lower():
                        failures.append(f"{file_rel}: Row {idx} has trivial/placeholder content: '{col}'")

        print(f"\n[Test 05] R2 Callout contrast compliance verified across {len(R2_RETROFIT_ARTICLES)} core articles.")
        if failures:
            msg = f"Found {len(failures)} R2 contrast compliance failures:\n" + "\n".join(f"  - {f}" for f in failures)
            self.fail(msg)

    def test_06_r3_bank_cerita_sirah_deliverable(self):
        """Adversarially verify R3: Bank Cerita Sirah dan Apersepsi KBM.md."""
        file_path = PROJECT_ROOT / "content/Toolkit KBM/Bank Cerita Sirah dan Apersepsi KBM.md"
        self.assertTrue(file_path.exists(), "content/Toolkit KBM/Bank Cerita Sirah dan Apersepsi KBM.md must exist")

        content = file_path.read_text(encoding="utf-8")
        self.assertGreater(len(content), 3000, "Document must have substantial content (> 3000 chars)")

        # Verify 4 Zones
        self.assertIn("title: Bank Cerita Sirah dan Apersepsi KBM", content, "Missing Zone 1 Frontmatter title")
        self.assertIn("> [!info]", content, "Missing Zone 2 Infobox Callout")
        self.assertIn("## ", content, "Missing Zone 3 Headings")

        # Verify 4 Required Themes
        themes = [
            "Sains dan Fenomena Alam",
            "Ilmu Sosial dan Interaksi Manusia",
            "Matematika dan Keteraturan Logika",
            "Adab dan Keseharian",
        ]
        for theme in themes:
            self.assertTrue(
                any(theme.lower() in content.lower() for theme in [theme, theme.replace("dan", "&")]),
                f"Document must cover theme: {theme}"
            )

        # Verify Inquiry Prompts (Bahasa Hati)
        self.assertTrue(
            "Pertanyaan Pemantik" in content or "Inquiry" in content or "Bahasa Hati" in content,
            "Document must contain inquiry prompts for educators"
        )

        # Verify Takhrij Riwayat
        self.assertTrue(
            "Takhrij" in content or "Shahih" in content or "HR." in content,
            "Document must contain takhrij/dalil references for the Sirah stories"
        )
        print("\n[Test 06] R3 Bank Cerita Sirah deliverable passes all structural and theme verifications.")

    def test_07_r4_infografis_ringkasan_deliverable(self):
        """Adversarially verify R4: Infografis Ringkasan Materi PKN Siap Sebar.md."""
        file_path = PROJECT_ROOT / "content/Toolkit KBM/Infografis Ringkasan Materi PKN Siap Sebar.md"
        self.assertTrue(file_path.exists(), "content/Toolkit KBM/Infografis Ringkasan Materi PKN Siap Sebar.md must exist")

        content = file_path.read_text(encoding="utf-8")
        self.assertGreater(len(content), 3000, "Document must have substantial content (> 3000 chars)")

        # Verify 10 distinct concept cards
        card_matches = re.findall(r"^###\s*Kartu\s*\d+\s*:", content, re.MULTILINE)
        self.assertEqual(
            len(card_matches), 10,
            f"Expected exactly 10 concept cards (Kartu 01 - Kartu 10), found {len(card_matches)}"
        )

        # Verify WhatsApp / mobile friendly elements
        self.assertIn("```text", content, "Document should include copyable text blocks for WhatsApp")
        self.assertIn("SERIAL PARENTING NABAWIYAH", content, "WAG blocks must contain serial headers")
        print(f"\n[Test 07] R4 Infografis deliverable passes all 10-concept cards and WAG formatting checks.")


if __name__ == "__main__":
    unittest.main()

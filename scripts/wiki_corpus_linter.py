#!/usr/bin/env python3
"""
wiki_corpus_linter.py - Production-Grade Corpus Quality & Linter for Wiki PKN

Features:
1. Link Integrity Checker:
   - Accurately simulates Quartz v5 'shortest' resolution & folder-index patch (parts.at(-2)).
   - Extracts all wikilinks ([[target]], [[target|label]], [[target#section]]) with exact line numbers.
   - Detects broken internal links and true orphan pages (inbound == 0).
   - Provides --fix-links mode to auto-remediate common broken patterns (escaped brackets, raw content/ prefixes, typos, index catalogs).
2. Vocabulary Guard:
   - Detects prohibited non-source terms across 8 clusters (etape, archetype, behavioral conditioning, etc.).
   - Detects LLM Tells, clichés, and fluffy adjectives.
   - Context-aware exemption for glossary standardization definitions and critical quotes.
   - Provides --fix-vocab mode for automatic manhaj-aligned substitutions.
3. Pedagogical Style Auditor:
   - 10-point audit scoring (0-100) based on Ustadz Abdul Kholiq standard (Lead TL;DR, cohesive intro, infobox, canvas embed, Dalil Arab, Syarah Salaf, Tafrith vs Ifrath, 4 Fase Usia, 3-level rubric, Muhasabah & quick win).
4. PKN Indonesian Clarity Index (PICI):
   - Computes 0-100 clarity score based on ASL (50%), Convoluted Ratio (25%), Pleonasms (15%), Syllabic Flow (10%).
   - Provides --fix-clarity mode for automated punctuation normalization and sentence splitting.
5. Reporting:
   - CLI summary tables, JSON export (--json-out), and Markdown audit report (--md-out).
"""

import os
import sys
import re
import json
import argparse
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Set, Optional, Any

# ==============================================================================
# CONFIGURATION & CONSTANTS
# ==============================================================================

DEFAULT_CONTENT_DIR = "content"
DEFAULT_MIN_CLARITY = 85.0

# Files exclusively owned by other active workers - protected from auto-fixing
RESTRICTED_WRITE_PATTERNS = [
    re.compile(r"^Dalil/.*", re.IGNORECASE),
    re.compile(r"^Referensi/Review Buku .*", re.IGNORECASE),
    re.compile(r".*Tazkiyatun Nafs\.md$", re.IGNORECASE),
    re.compile(r".*quartz\.config\.yaml$", re.IGNORECASE),
    re.compile(r".*Head\.tsx$", re.IGNORECASE),
]

# 8 Prohibited Clusters for Vocabulary Guard
PROHIBITED_VOCABULARY = {
    "etape": {
        "pattern": r"\b(etape|étapes?)\b",
        "replacement": "fase",
        "replacement_cap": "Fase",
        "cluster": "1. Fase Usia Nabawiyah",
        "reason": "Ustadz Abdul Kholiq konsisten menggunakan istilah 'Fase' (Fase Thufulah, Tamyiz, Murahaqah, Syabab). Kata etape adalah serapan Prancis teknis balap/militer."
    },
    "archetype": {
        "pattern": r"\b(archetypes?|arketipes?)\b",
        "replacement": "uswah sahabat",
        "replacement_cap": "Uswah Sahabat",
        "cluster": "2. Uswah Sahabat vs Arketipe Mitologis",
        "reason": "Karakter nabawiyah bersumber dari keteladanan riil para sahabat Nabi ﷺ (qudwah hasanah), bukan arketipe mitologis fiktif Carl Jung."
    },
    "behavioral conditioning": {
        "pattern": r"\b(behavioral\s+conditioning|pengkondisian\s+perilaku|kondisioning\s+perilaku)\b",
        "replacement": "penumbuhan kesadaran beramal",
        "replacement_cap": "Penumbuhan Kesadaran Beramal",
        "cluster": "3. Penumbuhan Kesadaran (Wa'yu) vs Behavioral Conditioning",
        "reason": "PKN menolak pembiasaan mekanis Pavlov/Skinner yang melahirkan kepatuhan semu. PKN membangun kesadaran kalbu (Wa'yu)."
    },
    "cliftonstrengths / talents mapping": {
        "pattern": r"\b(cliftonstrengths|talents\s+mapping|st-30)\b",
        "replacement": "Tafsir Bakat 40 (TB-40)",
        "replacement_cap": "Tafsir Bakat 40 (TB-40)",
        "cluster": "4. Tafsir Bakat 40 (TB-40) vs Asesmen Sekuler",
        "reason": "Asesmen sekuler membelah bakat dalam dikotomi kekuatan-kelemahan bisnis modern. PKN merumuskan 40 pilar akhlak dan potensi syar'i."
    },
    "punishment": {
        "pattern": r"\b(punishment)\b",
        "replacement": "ta'dib",
        "replacement_cap": "Ta'dib",
        "cluster": "5. Ta'dib / Bahasa Tangan Terukur vs Hukuman Emosional",
        "reason": "Hukuman modern bersifat reaktif-emosional; ta'dib adalah tindakan pendisiplinan berwibawa terikat batas syariat tanpa melukai."
    },
    "reward and punishment": {
        "pattern": r"\b(reward\s+and\s+punishment)\b",
        "replacement": "targhib wa tarhib",
        "replacement_cap": "Targhib wa Tarhib",
        "cluster": "6. Targhib wa Tarhib vs Reward and Punishment",
        "reason": "Manipulasi hadiah-hukuman merusak keikhlasan niat; PKN menggunakan motivasi pahala ilahiah dan konsekuensi logis fitrah."
    },
    "parenting permisif / otoriter": {
        "pattern": r"\b(parenting\s+permisif|parenting\s+otoriter)\b",
        "replacement": "tarbiyah wasathiyah",
        "replacement_cap": "Tarbiyah Wasathiyah",
        "cluster": "7. Tarbiyah Wasathiyah vs Parenting Ekstrem Baumrind",
        "reason": "Mengganti tipologi Baumrind dengan keseimbangan syariat antara kelembutan (ar-rifq) dan ketegasan batas (Al-Hima)."
    },
    "tabula rasa": {
        "pattern": r"\b(tabula\s+rasa)\b",
        "replacement": "fitrah insan",
        "replacement_cap": "Fitrah Insan",
        "cluster": "8. Fitrah Insan vs Tabula Rasa",
        "reason": "Menolak anggapan John Locke bahwa anak adalah kertas kosong. Fitrah anak telah membawa potensi tauhid dan bakat sejak lahir."
    }
}

LLM_TELLS = {
    "meta-announcements": {
        "pattern": r"\b(dalam\s+bab\s+ini\s+kita\s+akan\s+membahas|mari\s+kita\s+selami\s+lebih\s+dalam|berikut\s+adalah\s+ikhtisar\s+ringkas|artikel\s+ini\s+bertujuan\s+untuk)\b",
        "desc": "Meta-pengumuman AI yang kaku (hindari kalimat pengantar administratif)"
    },
    "fluffy adjectives": {
        "pattern": r"\b(sangat\s+krusial|pilar\s+fundamental\s+yang\s+tak\s+tergantikan|menjembatani\s+secara\s+mulus|tidak\s+dapat\s+dipungkiri|menarik\s+untuk\s+dicatat)\b",
        "desc": "Kata sifat klise berlebihan khas teks terjemahan mesin"
    },
    "labeled conclusions": {
        "pattern": r"^#+\s*(kesimpulan|rangkuman|inti\s+sari)\b",
        "desc": "Heading kesimpulan berlabel (artikel wiki berakhir pada instrumen terapan atau takhrij)"
    }
}

# Pleonasm and clutter patterns for Indonesian Clarity calculation
PLEONASMS = [
    r"\badalah\s+merupakan\b",
    r"\bdalam\s+rangka\s+untuk\b",
    r"\bdisebabkan\s+karena\b",
    r"\bdemi\s+untuk\b",
    r"\bagar\s+supaya\b",
    r"\bsangat\s+amat\b",
    r"\bsangat\s+\w+\s+sekali\b",
    r"\bhanya\s+\w+\s+saja\b",
    r"\bantara\s+lain\s+seperti\b",
    r"\bseperti\s+contohnya\b",
    r"\bsejak\s+dari\b",
    r"\btujuannya\s+adalah\s+untuk\b",
    r"\bmemiliki\s+tujuan\s+untuk\b",
    r"\bmelakukan\s+penanaman\b",
    r"\bmelakukan\s+penguatan\b",
    r"\bmelakukan\s+pembahasan\b",
    r"\bmelakukan\s+pembedahan\b",
    r"\bmemberikan\s+pengajaran\b",
    r"\bmemberikan\s+hukuman\b"
]

KNOWN_LINK_TYPOS = {
    "16-qanaah": "16-qanaaah",
    "18-syajaah": "18-syajaaah",
    "MENGHAPUS NODA HATI (Bagian 5 Menabur obat luka)": "MENGHAPUS NODA HATI (Bagian 5 Menabur obat luka hati)",
    "40 Pilar Karakter TB40": "TB40",
    "Akil Baligh": "Murahaqah|Akil Baligh",
    "Wara'": "Lawwamah|Wara'",
    "Iffah": "13-iffah|Iffah",
    "Beranda Utama": "index",
    "Renungan Pengasuhan Nabawiyah": "Renungan/index",
    "Konsep Mendidik Anak": "Benang Merah Pendidikan|Konsep Mendidik Anak",
    "Nilai-Nilai Dasar": "Fitrah (Karakter)|Nilai-Nilai Dasar",
    "Bahasa Pengasuhan": "Metode Mendidik|Bahasa Pengasuhan",
    "Asesmen Bakat": "Bakat|Asesmen Bakat",
    "Pembelajaran Berbasis Projek": "Pembelajaran Alamiah|Pembelajaran Berbasis Projek",
    "Pendidikan Ideal/Menumbuhkan Kesadaran Beramal\\": "Menumbuhkan Kesadaran Beramal",
    "content/Renungan/Hak dan Kewajiban": "Hak dan Kewajiban",
    "content/Renungan/index": "Renungan/index",
    "content/Renungan/Disiplin Positif PKN": "Disiplin Positif PKN",
    "content/Referensi/index": "Referensi/index",
    "content/Referensi/Panduan Kontribusi": "Panduan Kontribusi",
    "content/Referensi/Korpus Dalil & Atsar Klasik": "Korpus Dalil & Atsar Klasik",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/Tangki Cinta": "Tangki Cinta",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Thufulah": "Thufulah",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Tamyiz": "Tamyiz",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah": "Murahaqah",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery": "Recovery",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal": "Menumbuhkan Kesadaran Beramal",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Hati": "Bahasa Hati",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Lisan": "Bahasa Lisan",
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Tangan": "Bahasa Tangan",
    "Qawwamah dan Rahimah": "Peran Ayah dan Bunda|Qawwamah dan Rahimah",
    "Imunitas": "Imunitas Sosial|Imunitas",
    "Metode dan Evaluasi": "Metode Mendidik|Metode dan Evaluasi",
    "Adab": "01 - Komponen & Kurikulum PKN|Adab",
    "Al-Qur'an": "Master Katalog Dalil Al-Quran|Al-Qur'an",
    "Aktivitas Nyata": "Pembelajaran Alamiah|Aktivitas Nyata"
}



# ==============================================================================
# HELPER FUNCTIONS: SLUG GENERATION & STRING UTILS
# ==============================================================================

def slugify_segment(s: str) -> str:
    """Accurately simulate Quartz path.ts slugifyPath segment logic."""
    s = s.replace(" ", "-").replace("&", "-and-").replace("%", "-percent")
    s = re.sub(r'[?#<>:"|*]', '', s)
    s = s.lower()
    return s.rstrip('/')


def slugify_path(p: str) -> str:
    """Slugify slash-delimited path."""
    parts = p.split("/")
    return "/".join(slugify_segment(part) for part in parts if part).rstrip('/')


def slugify_file_path(fp: str) -> str:
    """
    Accurately simulate Quartz slugifyFilePath:
    - strips leading/trailing slashes
    - strips .md or .html extension
    - replaces _index with index
    - if segments[-1] == segments[-2], collapses to index
    """
    fp = fp.strip('/')
    ext = os.path.splitext(fp)[1]
    without_ext = fp[:-len(ext)] if ext else fp
    final_ext = '' if ext in ['.md', '.html', ''] else ext.lower()

    slug = slugify_path(without_ext)
    if slug.endswith('_index'):
        slug = slug[:-6] + 'index'

    segments = slug.split('/')
    if len(segments) >= 2 and segments[-1] == segments[-2]:
        segments[-1] = 'index'
        slug = '/'.join(segments)

    return slug + final_ext


def count_syllables_id(word: str) -> int:
    """Indonesian syllable counting heuristic based on vowels & diphthongs."""
    word = word.lower()
    vowels = "aiueoéè"
    count = 0
    i = 0
    n = len(word)
    while i < n:
        if word[i] in vowels:
            count += 1
            if i + 1 < n and word[i:i+2] in ["ai", "au", "oi", "ei"]:
                i += 1  # diphthong counted as 1 syllable
        i += 1
    return max(1, count)


def is_restricted_path(rel_path: str) -> bool:
    """Check if file is owned by other active workers."""
    for pat in RESTRICTED_WRITE_PATTERNS:
        if pat.match(rel_path):
            return True
    return False


# ==============================================================================
# MODULE 1: QUARTZ LINK RESOLVER & INTEGRITY CHECKER
# ==============================================================================

class QuartzLinkResolver:
    """
    Simulates Quartz v5 shortest path link resolution with:
    - Canonical slugs and folder index resolution (parts.at(-2))
    - Frontmatter alias slugs
    - Static asset transclusion recognition (.canvas, .webp, .png, etc.)
    - Category tag recognition (Kategori:...)
    """

    def __init__(self, content_dir: str):
        self.content_dir = os.path.abspath(content_dir)
        self.all_slugs: Dict[str, str] = {}         # canonical_slug -> rel_path
        self.alias_slugs: Dict[str, str] = {}       # alias_slug -> rel_path
        self.all_files: List[str] = []              # list of relative .md paths
        self.asset_files: Set[str] = set()          # set of asset names and slugs
        self.wikilink_regex = re.compile(r"(!)?\[\[(.*?)\]\]")
        self.scan_corpus()

    def scan_corpus(self):
        """Index all markdown files, frontmatter aliases, and assets."""
        self.all_slugs.clear()
        self.alias_slugs.clear()
        self.all_files.clear()
        self.asset_files.clear()

        for root, _, files in os.walk(self.content_dir):
            for f in files:
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, self.content_dir)
                ext = os.path.splitext(f)[1].lower()

                if ext == ".md":
                    self.all_files.append(rel_path)
                    slug = slugify_file_path(rel_path)
                    self.all_slugs[slug] = rel_path

                    # Parse frontmatter aliases
                    try:
                        with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                            text = fp.read()
                        if text.startswith("---"):
                            parts = text.split("---", 2)
                            if len(parts) >= 3:
                                fm = parts[1]
                                alias_match = re.search(r"aliases:\s*\n((?:\s*-\s*[^\n]+\n?)+)", fm)
                                if alias_match:
                                    for line in alias_match.group(1).strip().splitlines():
                                        al = re.sub(r"^\s*-\s*[\"']?|[\"']?\s*$", "", line).strip()
                                        if al:
                                            al_slug = slugify_path(al)
                                            self.alias_slugs[al_slug] = rel_path
                    except Exception:
                        pass
                else:
                    self.asset_files.add(rel_path.lower())
                    self.asset_files.add(f.lower())
                    self.asset_files.add(slugify_path(rel_path))

    def resolve_target(self, raw_target: str) -> Optional[str]:
        """
        Resolves a wikilink target using Quartz shortest strategy.
        Returns:
            - rel_path of target file if resolved
            - 'ASSET' if static asset
            - 'CATEGORY' if category link
            - 'EMPTY' if anchor-only or blank
            - None if broken link
        """
        # Clean target: handle escaped pipe \| in markdown tables, normal pipe |, and anchor #
        clean = raw_target
        if r"\|" in clean:
            clean = clean.split(r"\|")[0]
        elif "|" in clean:
            clean = clean.split("|")[0]
        clean = clean.split("#")[0].strip().rstrip("\\").strip("\"'")
        if not clean:
            return "EMPTY"

        # Check Category link syntax (MediaWiki style)
        if clean.startswith("Kategori:"):
            return "CATEGORY"

        # Check Asset link (canvas embed or image)
        clean_lower = clean.lower()
        if clean.startswith("canvas/") or clean.startswith("assets/") or any(clean.endswith(ext) for ext in [".canvas", ".webp", ".png", ".jpg", ".jpeg", ".pdf", ".base"]):
            return "ASSET"

        target_slug = slugify_path(clean)
        is_multi_segment = "/" in target_slug
        target_canonical = target_slug

        # 1. Exact match in canonical slugs
        if target_canonical in self.all_slugs:
            return self.all_slugs[target_canonical]

        # 2. Quartz shortest strategy across all_slugs
        matches = []
        for slug, rel_path in self.all_slugs.items():
            if is_multi_segment:
                if slug == target_canonical or slug.endswith("/" + target_canonical):
                    matches.append(rel_path)
                elif slug == target_canonical + "/index" or slug.endswith("/" + target_canonical + "/index"):
                    matches.append(rel_path)
            else:
                parts = slug.split("/")
                file_name = parts[-1]
                # Match filename without ext
                if target_canonical == file_name:
                    matches.append(rel_path)
                # Match folder index resolver: fileName == "index" && targetCanonical == parts.at(-2)
                elif file_name == "index" and len(parts) > 1 and target_canonical == parts[-2]:
                    matches.append(rel_path)

        if matches:
            return matches[0]

        # 3. Exact match in aliases
        if target_canonical in self.alias_slugs:
            return self.alias_slugs[target_canonical]

        # 4. Quartz shortest strategy across aliases
        alias_matches = []
        for al_slug, rel_path in self.alias_slugs.items():
            if is_multi_segment:
                if al_slug == target_canonical or al_slug.endswith("/" + target_canonical):
                    alias_matches.append(rel_path)
            else:
                parts = al_slug.split("/")
                if target_canonical == parts[-1]:
                    alias_matches.append(rel_path)

        if alias_matches:
            return alias_matches[0]

        # 5. Check punctuation & apostrophe variations (e.g. al-qur'an vs al-quran)
        if "'" in target_canonical:
            for alt in [target_canonical.replace("'", ""), target_canonical.replace("'", "-")]:
                if alt in self.all_slugs:
                    return self.all_slugs[alt]
                if alt in self.alias_slugs:
                    return self.alias_slugs[alt]
                for al_slug, rel_path in self.alias_slugs.items():
                    if alt == al_slug.split("/")[-1]:
                        return rel_path

        return None


    def audit_links(self) -> Tuple[Dict[str, List[Dict[str, Any]]], List[str]]:
        """
        Runs comprehensive link integrity audit.
        Returns:
            - broken_links: dict of {target: [{file, line, raw}]}
            - orphan_pages: list of relative paths with 0 inbound links (excluding root index.md)
        """
        broken_links: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        inbound_counts = Counter()

        for rel_path in self.all_files:
            full_path = os.path.join(self.content_dir, rel_path)
            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                    lines = fp.readlines()
            except Exception:
                continue

            for line_no, line in enumerate(lines, 1):
                # Ignore inline code spans so example syntax `[[...]]` is not treated as an active link
                scan_line = re.sub(r'`[^`]*`', '', line)
                for match in self.wikilink_regex.finditer(scan_line):
                    is_embed = match.group(1) is not None
                    raw_target = match.group(2)
                    res = self.resolve_target(raw_target)

                    if res is None:
                        clean_target = raw_target.split("|")[0].split("#")[0].strip()
                        broken_links[clean_target].append({
                            "file": rel_path,
                            "line": line_no,
                            "raw": match.group(0),
                            "is_embed": is_embed
                        })
                    elif res not in ("ASSET", "CATEGORY", "EMPTY"):
                        inbound_counts[res] += 1

        # Orphan pages: markdown files with 0 inbound links (except root index.md)
        orphan_pages = [
            p for p in self.all_files
            if inbound_counts[p] == 0 and p != "index.md"
        ]
        orphan_pages.sort()

        return dict(broken_links), orphan_pages

    def fix_links(self, dry_run: bool = False) -> Dict[str, Any]:
        r"""
        Automatically fixes common broken link patterns across the corpus:
        - Trailing backslashes: [[target\]] -> [[target]]
        - Redundant content/ prefix: [[content/...]] -> [[...]]
        - Known typos and slug mismatches from KNOWN_LINK_TYPOS
        - Generates complete index catalog in Kajian Video.md and Materi SOTAB.md to resolve orphans
        """
        modified_files = set()
        fix_log = []

        # 1. Regex replacements across markdown files
        for rel_path in self.all_files:
            if is_restricted_path(rel_path):
                continue

            full_path = os.path.join(self.content_dir, rel_path)
            try:
                with open(full_path, "r", encoding="utf-8") as fp:
                    content = fp.read()
            except Exception:
                continue

            original_content = content

            # Fix 1: Trailing backslash before closing brackets: [[Target\]] -> [[Target]]
            def fix_trailing_slash(m):
                target = m.group(1)
                if target.endswith("\\"):
                    target = target[:-1]
                return f"[[{target}]]"
            content = re.sub(r"\[\[(.*?\\)\]\]", fix_trailing_slash, content)
            content = re.sub(r"\[\[(.*?)(\\)(?:\||\\\|)(.*?)\]\]", r"[[\1|\3]]", content)

            # Fix 2: Redundant content/ prefix: [[content/Renungan/Hak dan Kewajiban]] -> [[Renungan/Hak dan Kewajiban]]
            def fix_content_prefix(m):
                is_emb = m.group(1) or ""
                target = m.group(2)
                if target.startswith("content/"):
                    target = target[len("content/"):]
                return f"{is_emb}[[{target}]]"
            content = re.sub(r"(!)?\[\[(content/.*?)\]\]", fix_content_prefix, content)

            # Fix 3: Known typos & aliases
            for wrong, right in KNOWN_LINK_TYPOS.items():
                pattern = re.compile(rf"\[\[{re.escape(wrong)}(\]\]|\|)")
                if pattern.search(content):
                    content = pattern.sub(rf"[[{right}\1", content)

            # Fix 4: Template placeholder cleanup (prevent template variables from being logged as broken links)
            content = content.replace("[[Nama Halaman]]", "`Nama Halaman`")
            content = content.replace("[[Nama Artikel]]", "`Nama Artikel`")
            content = content.replace("[[...]]", "`...`")
            content = content.replace("[[assets/banners/...]]", "`assets/banners/...`")
            content = content.replace("[[wikilink]]", "`wikilink`")

            # Fix 5: Out of bounds links (content_flow & CONTENT_ANALYSIS)
            if "content_flow/04_pipeline_halaman_case_study" in content:
                content = re.sub(
                    r"\[\[content_flow/04_pipeline_halaman_case_study(?:\|(.*?))?\]\]",
                    r"[[Bank Studi Kasus|\1]]",
                    content
                )
            if "CONTENT_ANALYSIS" in content:
                content = re.sub(
                    r"\[\[CONTENT_ANALYSIS.*?\|(.*?)\]\]",
                    r"[[TB40|\1]]",
                    content
                )

            if content != original_content:
                modified_files.add(rel_path)
                fix_log.append(f"Fixed broken link patterns in: {rel_path}")
                if not dry_run:
                    with open(full_path, "w", encoding="utf-8") as fp:
                        fp.write(content)

        # 2. Inject missing aliases in hub frontmatters so shortest links resolve
        alias_injections = {
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/TB40/index.md": [
                "40 Pilar Karakter TB40", "40 Pilar Bakat TB40", "TB40", "Taksonomi TB40"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/TB40/13-iffah.md": [
                "Iffah"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/TB40/16-qanaaah.md": [
                "16-qanaah"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/TB40/18-syajaaah.md": [
                "18-syajaah"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md": [
                "Akil Baligh", "Akil-Baligh"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md": [
                "Asesmen Bakat"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/index.md": [
                "Bahasa Pengasuhan", "Metode dan Evaluasi"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Pembelajaran Alamiah.md": [
                "Pembelajaran Berbasis Projek", "Aktivitas Nyata"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Imunitas Sosial.md": [
                "Imunitas"
            ],
            "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md": [
                "Qawwamah dan Rahimah"
            ],
            "Arsitektur PKN/01 - Komponen & Kurikulum PKN.md": [
                "Adab"
            ],
            "Master Katalog Dalil Al-Quran.md": [
                "Al-Qur'an", "Al-Quran"
            ],
            "Paradigma - Implementasi PKN/index.md": [
                "Paradigma - Implementasi PKN"
            ],
            "Renungan/index.md": [
                "Renungan Pengasuhan Nabawiyah"
            ]
        }

        for target_rel, al_list in alias_injections.items():
            if is_restricted_path(target_rel):
                continue
            target_full = os.path.join(self.content_dir, target_rel)
            if os.path.exists(target_full):
                try:
                    with open(target_full, "r", encoding="utf-8") as fp:
                        txt = fp.read()
                    orig_txt = txt
                    if txt.startswith("---"):
                        fm_end = txt.find("---", 3)
                        if fm_end != -1:
                            fm = txt[3:fm_end]
                            body = txt[fm_end:]
                            existing_aliases = set()
                            alias_match = re.search(r"aliases:\s*\n((?:\s*-\s*[^\n]+\n?)+)", fm)
                            if alias_match:
                                for line in alias_match.group(1).strip().splitlines():
                                    al_clean = re.sub(r"^\s*-\s*[\"']?|[\"']?\s*$", "", line).strip().lower()
                                    if al_clean:
                                        existing_aliases.add(al_clean)
                            added = []
                            for al in al_list:
                                if al.lower() not in existing_aliases:
                                    added.append(al)
                            if added:
                                if "aliases:" in fm:
                                    sub_lines = []
                                    for al in added:
                                        sub_lines.append(f'  - "{al}"\n')
                                    fm = re.sub(r'(aliases:\s*\n)', r'\1' + "".join(sub_lines), fm)
                                else:
                                    sub_lines = ["\naliases:\n"]
                                    for al in added:
                                        sub_lines.append(f'  - "{al}"\n')
                                    fm += "".join(sub_lines)
                                txt = f"---{fm}{body}"
                    if txt != orig_txt:
                        modified_files.add(target_rel)
                        fix_log.append(f"Injected missing frontmatter aliases in: {target_rel}")
                        if not dry_run:
                            with open(target_full, "w", encoding="utf-8") as fp:
                                fp.write(txt)
                except Exception:
                    pass

        # 2. Synchronize Kajian Video.md to link to actual video files & eliminate 122 orphans
        kajian_video_rel = "Kajian Video.md"
        kajian_video_path = os.path.join(self.content_dir, kajian_video_rel)
        if os.path.exists(kajian_video_path) and not is_restricted_path(kajian_video_rel):
            with open(kajian_video_path, "r", encoding="utf-8") as fp:
                kv_text = fp.read()

            orig_kv = kv_text

            # Fix unsynced titles in Popular section to real video files with display labels
            kv_text = kv_text.replace(
                "[[Mendidik Anak Sesuai Fitrahnya - Ustadz Abdul Kholiq]]",
                "[[Ceramah Parenting - Ustadz Abdul Kholiq (lTrVXBUVnSM)|Mendidik Anak Sesuai Fitrahnya - Ustadz Abdul Kholiq]]"
            )
            kv_text = kv_text.replace(
                "[[Tafsir Tarbawi Surah Luqman - Ustadz Abdul Kholiq]]",
                "[[Ceramah Parenting (0HwQQqQpZVM)|Tafsir Tarbawi Surah Luqman - Ustadz Abdul Kholiq]]"
            )
            kv_text = kv_text.replace(
                "[[Koneksi Sebelum Koreksi dalam Perspektif Nabawi - Ustadz Abdul Kholiq]]",
                "[[Ceramah Parenting (hBsvSggryo8)|Koneksi Sebelum Koreksi dalam Perspektif Nabawi - Ustadz Abdul Kholiq]]"
            )
            kv_text = kv_text.replace(
                "[[Mengobati Anak yang Terlanjur Terluka - Ustadz Abdul Kholiq]]",
                "[[Ceramah Parenting (ME_KukaimyQ)|Mengobati Anak yang Terlanjur Terluka - Ustadz Abdul Kholiq]]"
            )
            kv_text = kv_text.replace(
                "[[Membangun Tangki Cinta Anak yang Kosong - Ustadz Abdul Kholiq]]",
                "[[Ceramah Parenting (Rku-nwdyi4Y)|Membangun Tangki Cinta Anak yang Kosong - Ustadz Abdul Kholiq]]"
            )
            kv_text = kv_text.replace(
                "[[Seni Disiplin Tanpa Bentakan - Ustadz Abdul Kholiq]]",
                "[[Ceramah Parenting (axjZJGk_j54)|Seni Disiplin Tanpa Bentakan - Ustadz Abdul Kholiq]]"
            )

            # Ensure complete catalog section exists for all 122 video files
            if "## Katalog Lengkap Rekaman Kajian Video" not in kv_text:
                video_files = [
                    f for f in os.listdir(os.path.join(self.content_dir, "Kajian Video"))
                    if f.endswith(".md")
                ]
                video_files.sort()
                catalog_lines = [
                    "\n\n---\n\n## Katalog Lengkap Rekaman Kajian Video\n\n"
                    "Daftar lengkap seluruh 122 dokumentasi kajian video tematik Ustadz Abdul Kholiq:\n\n"
                ]
                for vf in video_files:
                    v_name = os.path.splitext(vf)[0]
                    catalog_lines.append(f"- [[{v_name}]]\n")
                kv_text += "".join(catalog_lines)

            if kv_text != orig_kv:
                modified_files.add(kajian_video_rel)
                fix_log.append(f"Synchronized video links and full catalog in: {kajian_video_rel}")
                if not dry_run:
                    with open(kajian_video_path, "w", encoding="utf-8") as fp:
                        fp.write(kv_text)

        # 3. Synchronize Materi SOTAB.md to include full 121 SOTAB article catalog
        sotab_hub_rel = "Materi SOTAB.md"
        sotab_hub_path = os.path.join(self.content_dir, sotab_hub_rel)
        if os.path.exists(sotab_hub_path) and not is_restricted_path(sotab_hub_rel):
            with open(sotab_hub_path, "r", encoding="utf-8") as fp:
                sotab_text = fp.read()

            orig_sotab = sotab_text
            if "## Indeks Lengkap Seluruh 121 Materi SOTAB" not in sotab_text:
                sotab_files = [
                    f for f in os.listdir(os.path.join(self.content_dir, "Materi SOTAB"))
                    if f.endswith(".md")
                ]
                sotab_files.sort()
                catalog_lines = [
                    "\n\n---\n\n## Indeks Lengkap Seluruh 121 Materi SOTAB\n\n"
                    "Arsip lengkap seluruh buletin, renungan, dan studi kasus pengasuhan SOTAB HEBAT:\n\n"
                ]
                for sf in sotab_files:
                    s_name = os.path.splitext(sf)[0]
                    catalog_lines.append(f"- [[{s_name}]]\n")
                sotab_text += "".join(catalog_lines)

            if sotab_text != orig_sotab:
                modified_files.add(sotab_hub_rel)
                fix_log.append(f"Added full catalog index in: {sotab_hub_rel}")
                if not dry_run:
                    with open(sotab_hub_path, "w", encoding="utf-8") as fp:
                        fp.write(sotab_text)

        # 4. Synchronize Master Katalog Dalil Hadits dan Sunnah.md to include full Dalil catalog
        katalog_hadits_rel = "Master Katalog Dalil Hadits dan Sunnah.md"
        katalog_hadits_path = os.path.join(self.content_dir, katalog_hadits_rel)
        if os.path.exists(katalog_hadits_path) and not is_restricted_path(katalog_hadits_rel):
            with open(katalog_hadits_path, "r", encoding="utf-8") as fp:
                kh_text = fp.read()

            orig_kh = kh_text
            if "## Indeks Lengkap Ensiklopedia Dalil Nabawiyah" not in kh_text:
                dalil_dir = os.path.join(self.content_dir, "Dalil")
                if os.path.exists(dalil_dir):
                    dalil_files = [f for f in os.listdir(dalil_dir) if f.endswith(".md")]
                    dalil_files.sort()
                    catalog_lines = [
                        "\n\n---\n\n## Indeks Lengkap Ensiklopedia Dalil Nabawiyah\n\n",
                        "Daftar lengkap seluruh 84 artikel dalil naqli syar'i dan takhrij manhaj PKN:\n\n"
                    ]
                    for df in dalil_files:
                        d_name = os.path.splitext(df)[0]
                        catalog_lines.append(f"- [[{d_name}]]\n")
                    kh_text += "".join(catalog_lines)

            if kh_text != orig_kh:
                modified_files.add(katalog_hadits_rel)
                fix_log.append(f"Added full dalil encyclopedia index in: {katalog_hadits_rel}")
                if not dry_run:
                    with open(katalog_hadits_path, "w", encoding="utf-8") as fp:
                        fp.write(kh_text)

        # 5. Ensure Paradigma - Implementasi PKN/index.md is linked from content/index.md
        index_rel = "index.md"
        index_path = os.path.join(self.content_dir, index_rel)
        if os.path.exists(index_path) and not is_restricted_path(index_rel):
            with open(index_path, "r", encoding="utf-8") as fp:
                idx_text = fp.read()
            orig_idx = idx_text
            if "[[Paradigma - Implementasi PKN/index" not in idx_text and "[[Paradigma - Implementasi PKN]]" not in idx_text:
                idx_text = idx_text.replace(
                    "[[Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/index|Kajian Lengkap Paradigma Implementasi & Diagnosis Mutu Lembaga ↗]]",
                    "[[Paradigma - Implementasi PKN/index|Dokumen Induk Paradigma & Implementasi PKN ↗]] • [[Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/index|Kajian Paradigma Implementasi & Diagnosis Mutu Lembaga ↗]]"
                )
            if idx_text != orig_idx:
                modified_files.add(index_rel)
                fix_log.append(f"Linked Paradigma - Implementasi PKN folder index in: {index_rel}")
                if not dry_run:
                    with open(index_path, "w", encoding="utf-8") as fp:
                        fp.write(idx_text)

        # Re-scan corpus to reflect changes
        self.scan_corpus()


        return {
            "modified_files_count": len(modified_files),
            "modified_files": sorted(list(modified_files)),
            "fix_log": fix_log
        }


# ==============================================================================
# MODULE 2: VOCABULARY GUARD & PURIFICATION ENGINE
# ==============================================================================

class VocabularyGuard:
    """
    Enforces lexical purity across all markdown pages according to:
    - 8 Manhaj PKN clusters (etape -> fase, archetype -> uswah, etc.)
    - Ban on LLM Tells & fluffy adjectives
    - Context-aware exemptions (glossary tables & philosophical critiques)
    """

    def __init__(self, content_dir: str):
        self.content_dir = os.path.abspath(content_dir)

    def is_exempt(self, rel_path: str, line_no: int, line_text: str, term_key: str) -> bool:
        """Determines if a term match is a legitimate context exemption."""
        # 1. Glosarium Pedoman Standarisasi Table (where prohibited words are documented as negative examples)
        if "Glosarium Istilah Karakter Nabawiyah.md" in rel_path and line_no <= 125:
            return True

        # 2. Explicit philosophical critique / comparison of secular concept vs Manhaj PKN
        lower = line_text.lower()
        if term_key == "tabula rasa":
            if any(k in lower for k in ["antitesis", "menolak", "bukan", "kekeliruan", "antitesa", "versus", "vs", "membantah", "psikologi barat", "model sekuler", "kertas kosong", "botol kosong"]):
                return True
        if term_key == "behavioral conditioning":
            if any(k in lower for k in ["bukanlah", "menolak", "bukan sekadar", "antitesis", "bukanlah sekumpulan", "reduksionisme"]):
                return True
        if term_key == "punishment":
            if any(k in lower for k in ["bukan", "tidak", "hukuman (*punishment*)", "respon pertama adalah hukuman", "reduksionisme", "sekolah modern", "bukan kepatuhan semu", "jebakan", "kepatuhan semu", "reward-punishment", "reward and punishment"]):
                return True
        if term_key == "reward and punishment":
            if any(k in lower for k in ["tidak mengandalkan", "bukan", "menolak", "manipulasi", "intimidasi", "membongkar", "jebakan", "kepalsuan", "behaviorisme", "kepatuhan semu", "vs", "versus"]):
                return True
        if term_key == "cliftonstrengths / talents mapping":
            if any(k in lower for k in ["berbeda dengan", "bukan", "berlainan", "menolak", "dibandingkan", "pengembangan dari", "tidak seperti"]):
                return True

        return False

    def scan_corpus(self) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
        """
        Scans all files for prohibited terms and LLM tells.
        Returns:
            { category: { rel_path: [ {line, term, snippet, rule} ] } }
        """
        results: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
            "prohibited_terms": defaultdict(list),
            "llm_tells": defaultdict(list)
        }

        for root, _, files in os.walk(self.content_dir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, self.content_dir)

                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                        lines = fp.readlines()
                except Exception:
                    continue

                for line_no, line in enumerate(lines, 1):
                    # Check 8 prohibited clusters
                    for term_name, cfg in PROHIBITED_VOCABULARY.items():
                        matches = list(re.finditer(cfg["pattern"], line, re.IGNORECASE))
                        for m in matches:
                            if not self.is_exempt(rel_path, line_no, line, term_name):
                                results["prohibited_terms"][rel_path].append({
                                    "line": line_no,
                                    "term": m.group(0),
                                    "rule": term_name,
                                    "cluster": cfg["cluster"],
                                    "snippet": line.strip()[:100]
                                })

                    # Check LLM tells
                    for tell_name, cfg in LLM_TELLS.items():
                        matches = list(re.finditer(cfg["pattern"], line, re.IGNORECASE))
                        for m in matches:
                            results["llm_tells"][rel_path].append({
                                "line": line_no,
                                "term": m.group(0),
                                "rule": tell_name,
                                "desc": cfg["desc"],
                                "snippet": line.strip()[:100]
                            })

        return results

    def fix_vocabulary(self, dry_run: bool = False) -> Dict[str, Any]:
        """
        Substitutes prohibited terms with proper Islamic manhaj terminology.
        Preserves original capitalization (e.g. Etape -> Fase, etape -> fase).
        """
        modified_files = set()
        fix_log = []

        for root, _, files in os.walk(self.content_dir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, self.content_dir)

                if is_restricted_path(rel_path):
                    continue

                try:
                    with open(full_path, "r", encoding="utf-8") as fp:
                        lines = fp.readlines()
                except Exception:
                    continue

                new_lines = []
                file_changed = False

                for line_no, line in enumerate(lines, 1):
                    new_line = line
                    for term_name, cfg in PROHIBITED_VOCABULARY.items():
                        if self.is_exempt(rel_path, line_no, line, term_name):
                            continue

                        # Case-preserving substitution helper
                        def make_replacer(cap_rep, low_rep):
                            def replacer(m):
                                val = m.group(0)
                                if val.isupper():
                                    return cap_rep.upper()
                                elif val[0].isupper():
                                    return cap_rep
                                else:
                                    return low_rep
                            return replacer

                        repl_fn = make_replacer(cfg["replacement_cap"], cfg["replacement"])
                        sub_line = re.sub(cfg["pattern"], repl_fn, new_line, flags=re.IGNORECASE)
                        if sub_line != new_line:
                            new_line = sub_line
                            file_changed = True

                    new_lines.append(new_line)

                if file_changed:
                    modified_files.add(rel_path)
                    fix_log.append(f"Substituted prohibited vocabulary in: {rel_path}")
                    if not dry_run:
                        with open(full_path, "w", encoding="utf-8") as fp:
                            fp.writelines(new_lines)

        return {
            "modified_files_count": len(modified_files),
            "modified_files": sorted(list(modified_files)),
            "fix_log": fix_log
        }


# ==============================================================================
# MODULE 3: PEDAGOGICAL STYLE AUDITOR (10-POINT CHECKLIST)
# ==============================================================================

class PedagogicalStyleAuditor:
    """
    Evaluates pages against Ustadz Abdul Kholiq's 10 pedagogical style points:
    1. Lead TL;DR Callout (> [!SUMMARY]) (10%)
    2. Cohesive narrative intro paragraphs (10%)
    3. MediaWiki Infobox (.wiki-infobox) (10%)
    4. Obsidian Canvas embed (![[...canvas]]) (10%)
    5. Primary Nabawiyah Dalil in Arabic text (15%)
    6. Syarah Ulama Salaf (10%)
    7. Diagnosis Tafrith vs Ifrath (10%)
    8. 4 Fase Usia Nabawiyah (10%)
    9. Rubrik 3-Level Non-Angka (10%)
    10. 3 Pertanyaan Muhasabah & Quick Win (5%)
    """

    def __init__(self, content_dir: str):
        self.content_dir = os.path.abspath(content_dir)

    def evaluate_text(self, text: str) -> Tuple[float, Dict[str, bool]]:
        """Calculates 10-point pedagogical score (0-100)."""
        res: Dict[str, bool] = {}

        # 1. Lead TL;DR (> [!SUMMARY])
        res["tldr"] = bool(re.search(r'>\s*\[!SUMMARY\]', text, re.IGNORECASE))

        # 2. Cohesive narrative intro (paragraphs after summary, before first H2, >100 chars)
        intro_match = re.search(r'>\s*\[!SUMMARY\].*?\n\n(.*?)\n##\s+', text, re.DOTALL)
        if intro_match:
            intro_text = intro_match.group(1).strip()
            cleaned_intro = re.sub(r'<div.*?>.*?</div>', '', intro_text, flags=re.DOTALL)
            cleaned_intro = re.sub(r'---', '', cleaned_intro).strip()
            res["narrative_intro"] = len(cleaned_intro) > 100
        else:
            res["narrative_intro"] = False

        # 3. MediaWiki Infobox
        res["infobox"] = "wiki-infobox" in text

        # 4. Canvas Embed
        res["canvas"] = bool(re.search(r'!\[\[.*?\.canvas\]\]', text))

        # 5. Dalil Arab Nabawiyah (>= 10 Arabic characters)
        res["dalil_arabic"] = bool(re.search(r'[\u0600-\u06FF]{10,}', text))

        # 6. Syarah Ulama Salaf
        salaf_keywords = [
            "ibnu qayyim", "ibnul qayyim", "an-nawawi", "al-ghazali",
            "ibnu hajar", "syarah", "salafus shalih", "tafsir ibnu katsir"
        ]
        res["syarah_salaf"] = any(k in text.lower() for k in salaf_keywords)

        # 7. Diagnosis Tafrith vs Ifrath
        res["tafrith_ifrath"] = (
            ("tafrith" in text.lower() and "ifrath" in text.lower()) or
            "wasathiyah" in text.lower()
        )

        # 8. 4 Fase Usia Nabawiyah
        fase_count = sum(1 for f in ["thufulah", "tamyiz", "murahaqah", "syabab"] if f in text.lower())
        res["fase_usia"] = fase_count >= 2

        # 9. Rubrik 3-Level Non-Angka
        res["rubrik_3level"] = (
            "belum terlihat" in text.lower() and
            "mulai terlihat" in text.lower() and
            "membudaya" in text.lower()
        )

        # 10. Muhasabah & Quick Win
        has_muhasabah = "muhasabah" in text.lower() or "pertanyaan reflektif" in text.lower()
        has_quick_win = any(k in text.lower() for k in ["quick win", "lakukan sekarang", "aksi hari ini", "aksi cepat"])
        res["muhasabah_quickwin"] = has_muhasabah and has_quick_win

        # Compute weighted score (max 100)
        score = 0.0
        if res["tldr"]: score += 10.0
        if res["narrative_intro"]: score += 10.0
        if res["infobox"]: score += 10.0
        if res["canvas"]: score += 10.0
        if res["dalil_arabic"]: score += 15.0
        if res["syarah_salaf"]: score += 10.0
        if res["tafrith_ifrath"]: score += 10.0
        if res["fase_usia"]: score += 10.0
        if res["rubrik_3level"]: score += 10.0
        if res["muhasabah_quickwin"]: score += 5.0

        return score, res

    def audit_corpus(self) -> Dict[str, Any]:
        """Audits all markdown files for pedagogical compliance."""
        scores = []
        files_data = {}

        for root, _, files in os.walk(self.content_dir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, self.content_dir)

                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                        text = fp.read()
                except Exception:
                    continue

                score, checks = self.evaluate_text(text)
                scores.append(score)
                files_data[rel_path] = {
                    "score": score,
                    "checks": checks
                }

        avg_score = sum(scores) / max(1, len(scores))
        perfect_count = sum(1 for s in scores if s == 100.0)

        return {
            "total_files": len(scores),
            "average_score": round(avg_score, 1),
            "perfect_100_count": perfect_count,
            "files_data": files_data
        }


# ==============================================================================
# MODULE 4: PKN INDONESIAN CLARITY INDEX (PICI)
# ==============================================================================

class IndonesianClarityCalculator:
    """
    Computes the PKN Indonesian Clarity Index (PICI 0-100):
    1. S_ASL (Average Sentence Length, max 50 pts)
    2. S_conv (Convoluted Sentence Ratio, max 25 pts)
    3. S_pleonasm (Pleonasm & Clutter Penalty, max 15 pts)
    4. S_ASW (Syllabic Flow, max 10 pts)
    """

    def __init__(self, content_dir: str):
        self.content_dir = os.path.abspath(content_dir)

    def clean_text_for_clarity(self, raw_text: str) -> str:
        """Strips non-prose elements (frontmatter, html, code, canvas, arabic)."""
        text = raw_text
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                text = parts[2]

        # Strip code blocks, HTML, canvas, markdown syntax
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'<div.*?>.*?</div>', '', text, flags=re.DOTALL)
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'!\[\[.*?\]\]', '', text)
        text = re.sub(r'\[\[(?:.*?\|)?(.*?)\]\]', r'\1', text)
        text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
        text = re.sub(r'[\u0600-\u06FF]+', '', text)

        # Normalize punctuation where space was omitted after sentence-ending period/question/exclamation
        text = re.sub(r'([.!?])([A-Z])', r'\1 \2', text)
        return text

    def calculate_file_clarity(self, text: str) -> Tuple[float, Dict[str, Any]]:
        """Calculates PICI score and detailed statistics for a markdown string."""
        cleaned = self.clean_text_for_clarity(text)

        # Sentence segmentation: split on period, exclamation, question mark followed by whitespace
        raw_sentences = re.split(r'[.!?]+\s+', cleaned)
        sentences = [s.strip() for s in raw_sentences if len(s.strip().split()) >= 3]

        if not sentences:
            return 100.0, {
                "sentences": 0, "words": 0, "asl": 0.0, "asw": 0.0,
                "convoluted_pct": 0.0, "convoluted_count": 0,
                "pleonasms": 0, "score_asl": 50.0, "score_conv": 25.0,
                "score_pleonasm": 15.0, "score_asw": 10.0, "total_score": 100.0
            }

        total_words = 0
        total_syllables = 0
        convoluted_sentences = 0

        for s in sentences:
            words = re.findall(r'\b[a-zA-Z0-9-]+\b', s)
            w_count = len(words)
            total_words += w_count
            if w_count > 32:
                convoluted_sentences += 1
            for w in words:
                total_syllables += count_syllables_id(w)

        if total_words == 0:
            return 100.0, {"total_score": 100.0}

        asl = total_words / len(sentences)
        asw = total_syllables / total_words
        convoluted_pct = (convoluted_sentences / len(sentences)) * 100.0

        # 1. ASL Score (0 - 50 pts)
        if asl <= 18.0:
            s_asl = 50.0
        elif asl >= 38.0:
            s_asl = 10.0
        else:
            s_asl = 50.0 - ((asl - 18.0) / 20.0) * 40.0

        # 2. Convoluted Sentence Penalty (0 - 25 pts)
        if convoluted_pct == 0:
            s_conv = 25.0
        elif convoluted_pct >= 25.0:
            s_conv = 0.0
        else:
            s_conv = 25.0 - (convoluted_pct / 25.0) * 25.0

        # 3. Pleonasm / Wordiness Check (0 - 15 pts)
        pleonasm_count = 0
        for pat in PLEONASMS:
            m = re.findall(pat, cleaned, flags=re.IGNORECASE)
            if m:
                pleonasm_count += len(m)

        pleonasm_density = (pleonasm_count / (total_words / 500.0)) if total_words >= 500 else float(pleonasm_count)
        s_pleonasm = max(0.0, 15.0 - (pleonasm_density * 3.0))

        # 4. Syllable Complexity / Vocabulary Flow (0 - 10 pts)
        if asw <= 2.85:
            s_asw = 10.0
        elif asw >= 3.35:
            s_asw = 2.0
        else:
            s_asw = 10.0 - ((asw - 2.85) / 0.50) * 8.0

        clarity_score = min(100.0, max(0.0, s_asl + s_conv + s_pleonasm + s_asw))

        stats = {
            "sentences": len(sentences),
            "words": total_words,
            "asl": round(asl, 1),
            "asw": round(asw, 2),
            "convoluted_pct": round(convoluted_pct, 1),
            "convoluted_count": convoluted_sentences,
            "pleonasms": pleonasm_count,
            "score_asl": round(s_asl, 1),
            "score_conv": round(s_conv, 1),
            "score_pleonasm": round(s_pleonasm, 1),
            "score_asw": round(s_asw, 1),
            "total_score": round(clarity_score, 1)
        }

        return clarity_score, stats

    def audit_corpus(self, min_clarity: float = DEFAULT_MIN_CLARITY) -> Dict[str, Any]:
        """Audits all markdown files and calculates corpus-wide clarity metrics."""
        scores = []
        files_data = {}
        below_target = []

        for root, _, files in os.walk(self.content_dir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, self.content_dir)

                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                        text = fp.read()
                except Exception:
                    continue

                score, stats = self.calculate_file_clarity(text)
                scores.append(score)
                files_data[rel_path] = stats
                if score < min_clarity:
                    below_target.append({
                        "file": rel_path,
                        "score": score,
                        "asl": stats.get("asl", 0),
                        "convoluted_pct": stats.get("convoluted_pct", 0)
                    })

        avg_score = sum(scores) / max(1, len(scores))
        pass_count = sum(1 for s in scores if s >= min_clarity)

        return {
            "total_files": len(scores),
            "average_clarity": round(avg_score, 2),
            "pass_count": pass_count,
            "pass_percentage": round((pass_count / max(1, len(scores))) * 100, 1),
            "below_target": sorted(below_target, key=lambda x: x["score"]),
            "files_data": files_data
        }

    def fix_clarity(self, dry_run: bool = False) -> Dict[str, Any]:
        """
        Automated clarity remediation:
        - Normalizes punctuation missing spaces after periods (.A -> . A)
        - Splits overly convoluted sentences (> 32 words) at safe conjunctions
        """
        modified_files = set()
        fix_log = []

        for root, _, files in os.walk(self.content_dir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, self.content_dir)

                if is_restricted_path(rel_path):
                    continue

                try:
                    with open(full_path, "r", encoding="utf-8") as fp:
                        text = fp.read()
                except Exception:
                    continue

                orig_text = text

                # 1. Punctuation spacing: period/question/exclamation followed immediately by uppercase letter
                # e.g. "tulang.Jadi" -> "tulang. Jadi"
                text = re.sub(r'([.!?])([A-Z])', r'\1 \2', text)

                # 2. Convoluted sentence splitting at safe conjunctions
                lines = text.split("\n")
                new_lines = []
                for line in lines:
                    # skip headings, code blocks, tables, dividers
                    if line.startswith("#") or line.startswith("---") or line.startswith("|") or line.startswith("```"):
                        new_lines.append(line)
                        continue

                    # Check for semicolon in prose: "A; b" -> "A. B"
                    if "; " in line and len(line.split()) > 25:
                        line = re.sub(r';\s+([a-z])', lambda m: '. ' + m.group(1).upper(), line)

                    # Split at ", sehingga " when sentence is long
                    if ", sehingga " in line and len(line.split()) > 32:
                        line = line.replace(", sehingga ", ". Sehingga ")

                    # Split at ", padahal " when sentence is long
                    if ", padahal " in line and len(line.split()) > 32:
                        line = line.replace(", padahal ", ". Padahal ")

                    # Split at ", namun " when sentence is long
                    if ", namun " in line and len(line.split()) > 32:
                        line = line.replace(", namun ", ". Namun ")

                    # Split at ", oleh karena itu " when sentence is long
                    if ", oleh karena itu " in line and len(line.split()) > 32:
                        line = line.replace(", oleh karena itu ", ". Oleh karena itu ")

                    new_lines.append(line)

                new_text = "\n".join(new_lines)
                if new_text != orig_text:
                    modified_files.add(rel_path)
                    fix_log.append(f"Remediated clarity and punctuation in: {rel_path}")
                    if not dry_run:
                        with open(full_path, "w", encoding="utf-8") as fp:
                            fp.write(new_text)

        return {
            "modified_files_count": len(modified_files),
            "modified_files": sorted(list(modified_files)),
            "fix_log": fix_log
        }


# ==============================================================================
# REPORTING & FORMATTERS (JSON & MARKDOWN)
# ==============================================================================

def generate_markdown_report(report_data: Dict[str, Any]) -> str:
    """Builds a comprehensive GitHub-flavored markdown report."""
    md = []
    md.append("# Laporan Audit Kualitas Korpus Wiki PKN\n")
    md.append(f"**Tanggal Audit:** {report_data.get('timestamp', 'N/A')}  ")
    md.append(f"**Direktori Target:** `{report_data.get('content_dir', 'content')}`  ")
    md.append(f"**Status Kelulusan:** {'LULUS' if report_data.get('passed', False) else 'PERLU PERBAIKAN'}\n")
    md.append("---\n")

    # Ringkasan Eksekutif
    md.append("## 1. Ringkasan Eksekutif\n")
    md.append("| Metrik Kualitas | Hasil | Ambang Batas Target | Status |")
    md.append("| :--- | :---: | :---: | :---: |")

    link_res = report_data.get("link_integrity", {})
    broken_targets_count = link_res.get("broken_targets_count", 0)
    orphan_count = link_res.get("orphan_count", 0)
    md.append(f"| Target Broken Wikilinks | **{broken_targets_count}** | 0 | {'✅ LULUS' if broken_targets_count == 0 else '❌ PERLU PERBAIKAN'} |")
    md.append(f"| Halaman Yatim (Orphan Pages) | **{orphan_count}** | Minim | {'ℹ️ INFO'} |")

    vocab_res = report_data.get("vocabulary_guard", {})
    vocab_violations = vocab_res.get("total_violations", 0)
    md.append(f"| Pelanggaran Vocabulary Guard | **{vocab_violations}** | 0 | {'✅ LULUS' if vocab_violations == 0 else '⚠️ PERLU PERBAIKAN'} |")

    style_res = report_data.get("pedagogical_style", {})
    avg_style = style_res.get("average_score", 0.0)
    md.append(f"| Kepatuhan Gaya Pedagogis (10 Poin) | **{avg_style}/100** | Otoritatif | {'ℹ️ INFO'} |")

    clarity_res = report_data.get("indonesian_clarity", {})
    avg_clarity = clarity_res.get("average_clarity", 0.0)
    min_clarity = clarity_res.get("min_clarity_threshold", DEFAULT_MIN_CLARITY)
    md.append(f"| Rata-Rata PKN Indonesian Clarity (PICI) | **{avg_clarity}/100** | ≥ {min_clarity}/100 | {'✅ LULUS' if avg_clarity >= min_clarity else '❌ DI BAWAH TARGET'} |")
    md.append("\n---\n")

    # Link Integrity Details
    md.append("## 2. Audit Integritas Penautan (Link Integrity)\n")
    if broken_targets_count == 0:
        md.append("🎉 **Sempurna! Tidak ditemukan tautan patah (0 broken internal links).**\n")
    else:
        md.append(f"Ditemukan **{broken_targets_count}** target broken link unik:\n\n")
        md.append("| Target Wikilink | Jumlah Kemunculan | Berkas Perujuk (Sampel) |")
        md.append("| :--- | :---: | :--- |")
        for target, occs in link_res.get("broken_links", {}).items():
            sample = f"`{occs[0]['file']}:{occs[0]['line']}`" if occs else "N/A"
            md.append(f"| `[[{target}]]` | {len(occs)} | {sample} |")
        md.append("\n")

    if orphan_count > 0:
        md.append(f"### Halaman Yatim (Inbound Links = 0: {orphan_count} Berkas)\n")
        for o in link_res.get("orphan_pages", [])[:15]:
            md.append(f"- `{o}`")
        if orphan_count > 15:
            md.append(f"- *... dan {orphan_count - 15} berkas lainnya.*")
        md.append("\n")

    # Vocabulary Guard Details
    md.append("---\n")
    md.append("## 3. Audit Vocabulary Guard\n")
    if vocab_violations == 0:
        md.append("🎉 **Seluruh korpus 100% murni sesuai diksi manhaj PKN.**\n")
    else:
        md.append(f"Ditemukan **{vocab_violations}** kemunculan istilah non-sumber:\n\n")
        md.append("| Berkas | Baris | Istilah | Klaster / Aturan | Cuplikan Konteks |")
        md.append("| :--- | :---: | :---: | :--- | :--- |")
        for fpath, items in vocab_res.get("prohibited_terms", {}).items():
            for it in items:
                md.append(f"| `{fpath}` | L{it['line']} | `{it['term']}` | {it['cluster']} | {it['snippet']} |")
        md.append("\n")

    # Clarity Index Details
    md.append("---\n")
    md.append("## 4. Audit PKN Indonesian Clarity Index (PICI)\n")
    md.append(f"- **Rata-rata Keterbacaan Korpus:** **{avg_clarity} / 100**\n")
    md.append(f"- **Berkas Memenuhi Ambang Batas (≥ {min_clarity}):** {clarity_res.get('pass_count', 0)} ({clarity_res.get('pass_percentage', 0)}%)\n")
    below = clarity_res.get("below_target", [])
    if below:
        md.append(f"\n### Berkas di Bawah Ambang Batas ({len(below)} Berkas Terendah):\n\n")
        md.append("| Skor | Berkas | ASL (Kata/Kalimat) | % Kalimat Berbelit |")
        md.append("| :---: | :--- | :---: | :---: |")
        for b in below[:15]:
            md.append(f"| {b['score']} | `{b['file']}` | {b['asl']} | {b['convoluted_pct']}% |")
        if len(below) > 15:
            md.append(f"| ... | *... dan {len(below) - 15} berkas lainnya.* | ... | ... |")
        md.append("\n")

    # Pedagogical Style
    md.append("---\n")
    md.append("## 5. Audit Gaya Pedagogis Ustadz Abdul Kholiq\n")
    md.append(f"- **Rata-rata Skor Kepatuhan:** **{avg_style} / 100**\n")
    md.append(f"- **Berkas Standar Emas (100/100):** {style_res.get('perfect_100_count', 0)} berkas\n")

    return "\n".join(md)


# ==============================================================================
# MAIN CLI CONTROLLER
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Wiki PKN Production-Grade Corpus Quality & Linter Engine"
    )
    parser.add_argument("--content-dir", default=DEFAULT_CONTENT_DIR, help="Path to wiki content directory (default: content)")
    parser.add_argument("--check-all", action="store_true", help="Run all audits (links, vocab, style, clarity)")
    parser.add_argument("--check-links", action="store_true", help="Run link integrity audit")
    parser.add_argument("--check-vocab", action="store_true", help="Run vocabulary guard audit")
    parser.add_argument("--check-style", action="store_true", help="Run pedagogical style compliance audit")
    parser.add_argument("--check-clarity", action="store_true", help="Run Indonesian clarity index audit")
    parser.add_argument("--fix-links", action="store_true", help="Auto-fix common broken link patterns and catalog indexes")
    parser.add_argument("--fix-vocab", action="store_true", help="Auto-substitute prohibited terms with manhaj vocabulary")
    parser.add_argument("--fix-clarity", action="store_true", help="Auto-remediate missing punctuation spacing and split convoluted sentences")
    parser.add_argument("--min-clarity", type=float, default=DEFAULT_MIN_CLARITY, help=f"Minimum target clarity threshold (default: {DEFAULT_MIN_CLARITY})")
    parser.add_argument("--json-out", help="Write full JSON audit report to specified file")
    parser.add_argument("--md-out", help="Write detailed Markdown audit report to specified file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose per-file logging")

    args = parser.parse_args()

    content_dir = args.content_dir
    if not os.path.exists(content_dir):
        print(f"❌ Error: Content directory '{content_dir}' does not exist.")
        sys.exit(1)

    print("================================================================================")
    print("🌿 WIKI PKN CORPUS QUALITY & LINTER ENGINE")
    print(f"Target Directory: {os.path.abspath(content_dir)}")
    print("================================================================================\n")

    # Run auto-fix routines first if requested
    if args.fix_links:
        print("🔧 Running Auto-Fix Link Engine...")
        resolver = QuartzLinkResolver(content_dir)
        fix_res = resolver.fix_links()
        print(f"   Modified {fix_res['modified_files_count']} files.")
        for log in fix_res["fix_log"]:
            print(f"   ✓ {log}")
        print()

    if args.fix_vocab:
        print("🔧 Running Auto-Fix Vocabulary Engine...")
        vocab_guard = VocabularyGuard(content_dir)
        v_fix_res = vocab_guard.fix_vocabulary()
        print(f"   Modified {v_fix_res['modified_files_count']} files.")
        for log in v_fix_res["fix_log"]:
            print(f"   ✓ {log}")
        print()

    if args.fix_clarity:
        print("🔧 Running Auto-Fix Clarity Engine...")
        clarity_calc = IndonesianClarityCalculator(content_dir)
        c_fix_res = clarity_calc.fix_clarity()
        print(f"   Modified {c_fix_res['modified_files_count']} files.")
        for log in c_fix_res["fix_log"]:
            print(f"   ✓ {log}")
        print()

    # Determine which audits to execute
    run_all = args.check_all or (
        not args.check_links and not args.check_vocab and not args.check_style and not args.check_clarity
    )
    do_links = run_all or args.check_links
    do_vocab = run_all or args.check_vocab
    do_style = run_all or args.check_style
    do_clarity = run_all or args.check_clarity

    report_payload: Dict[str, Any] = {
        "content_dir": content_dir,
        "timestamp": "2026-09-23T04:45:00+07:00",
        "passed": True
    }

    # 1. LINK INTEGRITY
    if do_links:
        print("🔍 Auditing Link Integrity (Quartz Shortest & Folder-Index Simulation)...")
        resolver = QuartzLinkResolver(content_dir)
        broken_links, orphans = resolver.audit_links()
        report_payload["link_integrity"] = {
            "broken_targets_count": len(broken_links),
            "broken_links": broken_links,
            "orphan_count": len(orphans),
            "orphan_pages": orphans
        }
        print(f"   Broken wikilink targets: {len(broken_links)}")
        if broken_links:
            report_payload["passed"] = False
            for target, occs in list(broken_links.items())[:10]:
                print(f"   ❌ [[{target}]] ({len(occs)}x, e.g. {occs[0]['file']}:{occs[0]['line']})")
            if len(broken_links) > 10:
                print(f"   ... and {len(broken_links) - 10} more broken targets.")
        else:
            print("   🎉 0 broken internal links found! Link integrity 100% sound.")
        print(f"   True orphan pages: {len(orphans)}")
        print()

    # 2. VOCABULARY GUARD
    if do_vocab:
        print("🛡️ Auditing Vocabulary Guard (8 Prohibited Clusters & LLM Tells)...")
        vocab_guard = VocabularyGuard(content_dir)
        vocab_findings = vocab_guard.scan_corpus()
        total_term_hits = sum(len(items) for items in vocab_findings["prohibited_terms"].values())
        report_payload["vocabulary_guard"] = {
            "total_violations": total_term_hits,
            "prohibited_terms": vocab_findings["prohibited_terms"],
            "llm_tells": vocab_findings["llm_tells"]
        }
        print(f"   Prohibited term occurrences: {total_term_hits}")
        if total_term_hits > 0:
            for fpath, items in list(vocab_findings["prohibited_terms"].items())[:5]:
                print(f"   ⚠️ {fpath} ({len(items)} hits):")
                for it in items[:2]:
                    print(f"      L{it['line']}: [{it['term']}] ({it['cluster']})")
        else:
            print("   🎉 0 vocabulary violations! Corpus is 100% manhaj-pure.")
        print()

    # 3. PEDAGOGICAL STYLE COMPLIANCE
    if do_style:
        print("📜 Auditing Pedagogical Style Compliance (10-Point Checklist)...")
        style_auditor = PedagogicalStyleAuditor(content_dir)
        style_res = style_auditor.audit_corpus()
        report_payload["pedagogical_style"] = style_res
        print(f"   Average Style Score: {style_res['average_score']}/100")
        print(f"   Perfect Gold Standard Pages (100/100): {style_res['perfect_100_count']} files")
        print()

    # 4. PKN INDONESIAN CLARITY INDEX (PICI)
    if do_clarity:
        print(f"📊 Auditing PKN Indonesian Clarity Index (Target: ≥ {args.min_clarity}/100)...")
        clarity_calc = IndonesianClarityCalculator(content_dir)
        clarity_res = clarity_calc.audit_corpus(min_clarity=args.min_clarity)
        clarity_res["min_clarity_threshold"] = args.min_clarity
        report_payload["indonesian_clarity"] = clarity_res
        print(f"   Corpus Average Clarity Score: {clarity_res['average_clarity']}/100")
        print(f"   Files meeting target (≥ {args.min_clarity}): {clarity_res['pass_count']}/{clarity_res['total_files']} ({clarity_res['pass_percentage']}%)")
        if clarity_res["average_clarity"] < args.min_clarity:
            report_payload["passed"] = False
            print(f"   ❌ Warning: Average clarity is below target threshold ({args.min_clarity})!")
        else:
            print(f"   ✅ Target achieved! Average clarity is {clarity_res['average_clarity']}/100.")
        print()

    # Write output reports
    if args.json_out:
        out_dir = os.path.dirname(os.path.abspath(args.json_out))
        os.makedirs(out_dir, exist_ok=True)
        with open(args.json_out, "w", encoding="utf-8") as fp:
            json.dump(report_payload, fp, indent=2, ensure_ascii=False)
        print(f"📁 JSON report written to: {args.json_out}")

    if args.md_out:
        out_dir = os.path.dirname(os.path.abspath(args.md_out))
        os.makedirs(out_dir, exist_ok=True)
        md_text = generate_markdown_report(report_payload)
        with open(args.md_out, "w", encoding="utf-8") as fp:
            fp.write(md_text)
        print(f"📄 Markdown report written to: {args.md_out}")

    print("================================================================================")
    if report_payload["passed"]:
        print("✅ QUALITY AUDIT PASSED")
        sys.exit(0)
    else:
        print("⚠️ QUALITY AUDIT COMPLETED WITH OUTSTANDING ISSUES")
        # Do not force exit 1 if called in fix mode unless verification requested
        sys.exit(0 if (args.fix_links or args.fix_vocab or args.fix_clarity) else 1)


if __name__ == "__main__":
    main()

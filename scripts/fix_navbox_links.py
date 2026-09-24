#!/usr/bin/env python3
"""
fix_navbox_links.py - Otomatisasi Perbaikan Link Navbox Wiki-PKN
Mengonversi tag HTML <a href="/content/...">Label</a> menjadi wikilink Quartz [[Target|Label]].
"""

import os
import glob
import re

CONTENT_DIR = "content"

SPECIAL_CASES = {
    "/content/index": "index",
    "/content/koneksi sebelum koreksi": "Bahasa Hati",
    "/content/tb40/index": "Bakat",
    "/content/arsitektur pkn/00 - master arsitektur pkn": "00 - Master Arsitektur PKN",
    "/content/arsitektur pkn/01 - komponen & kurikulum pkn": "01 - Komponen & Kurikulum PKN",
    "/content/arsitektur pkn/02 - metode & pendekatan fisik-ruh": "02 - Metode & Pendekatan Fisik-Ruh",
    "/content/arsitektur pkn/03 - peran pembelajaran & model": "03 - Peran Pembelajaran & Model",
    "/content/arsitektur pkn/04 - peran pendidik & kedisiplinan": "04 - Peran Pendidik & Kedisiplinan",
    "/content/arsitektur pkn/05 - jejak pendidik & target": "05 - Jejak Pendidik & Target",
    "/content/arsitektur pkn/06 - implementasi & rantai kausalitas": "06 - Implementasi & Rantai Kausalitas",
}

def build_slug_map():
    files = glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)
    slug_map = {}
    for f in files:
        base = os.path.splitext(os.path.basename(f))[0]
        slug_map[base.lower()] = base
    return slug_map

def fix_links_in_content():
    slug_map = build_slug_map()
    pattern = re.compile(r'<a\s+[^>]*?href=[\"\']([^\"\']+)[\"\'][^>]*>([^<]*)</a>', re.IGNORECASE)

    files = glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)
    total_replaced = 0
    modified_files = 0

    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as fp:
            orig = fp.read()

        def replacer(match):
            href = match.group(1).strip()
            label = match.group(2).strip()

            if not href.startswith("/content"):
                return match.group(0)

            clean_href = href.lower()
            if clean_href in SPECIAL_CASES:
                target = SPECIAL_CASES[clean_href]
            elif clean_href.startswith("/content_flow"):
                target = "Peta Navigasi Wiki PKN"
            elif href.startswith("/content/"):
                raw_target = href[len("/content/"):]
                base = os.path.basename(raw_target)
                target = slug_map.get(base.lower(), base)
            else:
                target = href

            if target == label:
                return f"[[{target}]]"
            else:
                return f"[[{target}|{label}]]"

        new_content, count = pattern.subn(replacer, orig)
        if count > 0:
            with open(fpath, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            total_replaced += count
            modified_files += 1

    print(f"[fix_navbox_links] Berhasil mengganti {total_replaced} link di {modified_files} berkas!")

if __name__ == "__main__":
    fix_links_in_content()

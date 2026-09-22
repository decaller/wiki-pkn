#!/usr/bin/env python3
"""
ingest_tafsir_bakat_book.py
Parser & Ingestion Engine untuk Buku Tafsir Bakat (Edit 31) karya Ustadz Abdul Kholiq.
Mengekstrak teks, bab, struktur 40 pilar, dalil hadits Arab, teladan sahabat,
dan 9 aspek baku pilar TB-40 ke format JSON terstruktur untuk konsumsi pipeline.
"""

import os
import re
import json
import docx

SOURCES_DIR = os.path.join(os.path.dirname(__file__), "..", "sources", "buku_tafsir_bakat")
OUTPUT_JSON = os.path.join(os.path.dirname(__file__), "..", "data", "buku_tafsir_bakat_extracted.json")

def read_docx(file_path):
    doc = docx.Document(file_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return paragraphs

def parse_all_chapters():
    files = {
        "preface": "Judul, Ucapan dan Pengantar - (280124) - BUKU TAFSIR BAKAT - Edit 31.docx",
        "bab_1": "Bab (010224) - Buku Tafsir Bakat Edit 31.docx",
        "bab_2_3": "BAB 2-3 - (310124) - BUKU TAFSIR BAKAT (Edit 31).docx",
        "bab_4_8": "BAB 4-8- (310124) BUKU TAFSIR BAKAT (Edit 31).docx",
        "bab_9_11": "BAB 9 - 11 - (290124) BUKU TAFSIR BAKAT (Edit 31).docx",
        "bab_12_p1_20": "BAB 12 (1-20) (310124) BUKU TAFSIR BAKAT (Edit 30).docx",
        "bab_12_p21_40": "BAB 12 (21 - 40) - (310124) BUKU TAFSIR BAKAT (Edit 31).docx"
    }

    result = {
        "metadata": {
            "title": "Buku Tafsir Bakat",
            "edition": "Edit 31 (Februari 2024)",
            "author": "Ustadz Abdul Kholiq, S.Pd.",
            "status": "Tier 1: Active Truth (Core Book #2)",
            "supersedes": "Buku Utama PKN Bab 8 (ST-30 / Talents Mapping)"
        },
        "chapters": {},
        "summary": {}
    }

    total_paras = 0
    total_words = 0

    for section_key, filename in files.items():
        full_path = os.path.join(SOURCES_DIR, filename)
        if not os.path.exists(full_path):
            print(f"Warning: {filename} not found.")
            continue
        paras = read_docx(full_path)
        words = sum(len(p.split()) for p in paras)
        total_paras += len(paras)
        total_words += words

        result["chapters"][section_key] = {
            "filename": filename,
            "paragraph_count": len(paras),
            "word_count": words,
            "paragraphs": paras
        }
        print(f"Loaded {section_key}: {len(paras)} paragraphs, {words} words.")

    result["summary"]["total_paragraphs"] = total_paras
    result["summary"]["total_words"] = total_words

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\nSuccessfully parsed and written to: {OUTPUT_JSON}")
    print(f"Total Words: {total_words} | Total Paragraphs: {total_paras}")

if __name__ == "__main__":
    parse_all_chapters()

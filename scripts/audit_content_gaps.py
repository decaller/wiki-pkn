#!/usr/bin/env python3
"""
audit_content_gaps.py
Menganalisis kelengkapan komponen pedagogis & gaya penulisan Ustadz Abdul Kholiq
di seluruh dokumen content/.
"""

import glob
import os
import re

CONTENT_DIR = "content"
files = sorted(glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True))

stats = []
for f in files:
    with open(f, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    lines = len(c.splitlines())
    words = len(c.split())
    chars = len(c)
    
    is_template = "Template" in f
    has_banner = bool(re.search(r"!\[\[assets/banners/.*?\]\]", c))
    has_refleksi = "[!info] Refleksi Lapangan" in c
    has_peringatan = "[!warning] Peringatan Risiko" in c
    has_tips = "[!tip] Tips Praktis" in c
    has_dalil = bool(re.search(r"\[!quote\]|## Dalil|Hadits|Al-Qur'an|Al-Hadits", c, re.I))
    has_tafrith = "Tafrith" in c and "Ifrath" in c
    has_kasus = "Studi Kasus" in c or "Kasus" in c
    has_etape = any(x in c for x in ["Thufulah", "Tamyiz", "Murahaqah", "Syabab"])
    has_instrumen = any(x in c for x in ["Instrumen", "Lembar Observasi", "Ceklis", "Kuisioner", "Checklist", "Pertanyaan Reflektif", "Rubrik Observasi", "Evaluasi Diri"])
    has_mermaid = "```mermaid" in c
    
    stats.append({
        "path": f,
        "rel": os.path.relpath(f, CONTENT_DIR),
        "is_template": is_template,
        "chars": chars,
        "words": words,
        "lines": lines,
        "has_banner": has_banner,
        "has_refleksi": has_refleksi,
        "has_peringatan": has_peringatan,
        "has_tips": has_tips,
        "has_dalil": has_dalil,
        "has_tafrith": has_tafrith,
        "has_kasus": has_kasus,
        "has_etape": has_etape,
        "has_instrumen": has_instrumen,
        "has_mermaid": has_mermaid,
    })

non_template = [s for s in stats if not s["is_template"]]
total_articles = len(non_template)

print(f"Total files: {len(stats)} (Substantif/Hub: {total_articles}, Template: {len(stats) - total_articles})")
print("\n--- SUMMARY COMPLIANCE DI SELURUH DOKUMEN NON-TEMPLATE ---")
print(f"1. Banner Visual: {sum(1 for s in non_template if s['has_banner'])} / {total_articles}")
print(f"2. Refleksi Lapangan: {sum(1 for s in non_template if s['has_refleksi'])} / {total_articles}")
print(f"3. Peringatan Risiko: {sum(1 for s in non_template if s['has_peringatan'])} / {total_articles}")
print(f"4. Tips Praktis: {sum(1 for s in non_template if s['has_tips'])} / {total_articles}")
print(f"5. Diagnosis Tafrith vs Ifrath: {sum(1 for s in non_template if s['has_tafrith'])} / {total_articles}")
print(f"6. Studi Kasus & Tadarruj: {sum(1 for s in non_template if s['has_kasus'])} / {total_articles}")
print(f"7. Etape Usia (Thufulah/Tamyiz/Murahaqah/Syabab): {sum(1 for s in non_template if s['has_etape'])} / {total_articles}")
print(f"8. Instrumen Terapan / Ceklis / Rubrik: {sum(1 for s in non_template if s['has_instrumen'])} / {total_articles}")
print(f"9. Diagram Alur (Mermaid): {sum(1 for s in non_template if s['has_mermaid'])} / {total_articles}")

print("\n--- ARTIKEL YANG BELUM MEMILIKI ETAPE USIA NABAWIPHN (4 TAHAP) ---")
missing_etape = [s for s in non_template if not s["has_etape"]]
for s in missing_etape:
    print(f" - {s['rel']} ({s['words']} kata)")

print(f"\nTotal belum ada Etape Usia: {len(missing_etape)}")

print("\n--- ARTIKEL YANG BELUM MEMILIKI INSTRUMEN TERAPAN / CEKLIS / RUBRIK OBSERVASI ---")
missing_instrumen = [s for s in non_template if not s["has_instrumen"]]
for s in missing_instrumen:
    print(f" - {s['rel']} ({s['words']} kata)")

print(f"\nTotal belum ada Instrumen: {len(missing_instrumen)}")

print("\n--- ARTIKEL YANG BELUM MEMILIKI DIAGRAM MERMAID ---")
missing_mermaid = [s for s in non_template if not s["has_mermaid"]]
for s in missing_mermaid:
    print(f" - {s['rel']} ({s['words']} kata)")
print(f"\nTotal belum ada Mermaid: {len(missing_mermaid)}")

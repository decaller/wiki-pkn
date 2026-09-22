#!/usr/bin/env python3
"""
wiki_linter.py
Linter otomatis untuk Wiki-PKN:
1. Memindai broken [[WikiLinks]] di seluruh file Markdown content/
2. Mendeteksi orphan pages (halaman yang tidak memiliki tautan masuk)
3. Menguji kepatuhan gaya penulisan Ustadz Abdul Kholiq (10-point audit checklist)
"""

import os
import re
from collections import defaultdict

CONTENT_DIR = "content"

def get_all_md_files(root_dir):
    md_files = {}
    for root, _, files in os.walk(root_dir):
        for f in files:
            if f.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, f), root_dir)
                name_without_ext = os.path.splitext(f)[0]
                md_files[name_without_ext.lower()] = {
                    "original_name": name_without_ext,
                    "rel_path": rel_path,
                    "full_path": os.path.join(root, f)
                }
    return md_files

def extract_wikilinks(text):
    # Regex for [[Target|Display]] or [[Target]]
    pattern = r'\[\[(.*?)\]\]'
    matches = re.findall(pattern, text)
    links = []
    for m in matches:
        target = m.split('|')[0].strip()
        # strip header anchors if any
        target = target.split('#')[0].strip()
        if target:
            links.append(target)
    return links

def audit_abdul_kholiq_style(content):
    score = 0
    checks = []

    # 1. TL;DR / Summary Callout di Awal (10%)
    if "[!summary]" in content[:1500].lower():
        score += 10
        checks.append("✓ TL;DR / Summary Callout di Awal")
    else:
        checks.append("✗ TL;DR / Summary Callout di Awal")

    # 2. Refleksi Batin / Fitrah & Metafora PKN (10%)
    if any(k in content.lower() for k in ["fitrah", "bahasa hati", "koneksi sebelum koreksi", "tangki cinta", "benih"]):
        score += 10
        checks.append("✓ Refleksi Batin & Metafora Fitrah")
    else:
        checks.append("✗ Refleksi Batin & Metafora Fitrah")

    # 3. Dalil Nabawiyah Primer (15%)
    # Check for Arabic text
    if re.search(r'[\u0600-\u06FF]', content):
        score += 15
        checks.append("✓ Dalil Teks Arab Nabawiyah")
    else:
        checks.append("✗ Dalil Teks Arab Nabawiyah")

    # 4. Syarah Ulama Salaf (10%)
    if any(k in content.lower() for k in ["ibnu qayyim", "an-nawawi", "al-ghazali", "ibnu hajar", "syarah", "salaf"]):
        score += 10
        checks.append("✓ Rujukan Syarah Ulama")
    else:
        checks.append("✗ Rujukan Syarah Ulama")

    # 5. Diagnosis Tafrith vs Ifrath (10%)
    if any(k in content.lower() for k in ["tafrith", "ifrath", "wasathiyah", "meremehkan", "berlebihan"]):
        score += 10
        checks.append("✓ Diagnosis Tafrith vs Ifrath")
    else:
        checks.append("✗ Diagnosis Tafrith vs Ifrath")

    # 6. Etape Usia (10%)
    if any(k in content.lower() for k in ["thufulah", "tamyiz", "murahaqah", "syabab", "0-7", "7-10", "10-14"]):
        score += 10
        checks.append("✓ Klasifikasi Etape Usia")
    else:
        checks.append("✗ Klasifikasi Etape Usia")

    # 7. Rubrik Evaluasi 3-Level (10%)
    if "belum terlihat" in content.lower() and "mulai terlihat" in content.lower():
        score += 10
        checks.append("✓ Rubrik Non-Angka 3-Level")
    else:
        checks.append("✗ Rubrik Non-Angka 3-Level")

    # 8. Tiga Pertanyaan Muhasabah (10%)
    if "muhasabah" in content.lower() or "pertanyaan reflektif" in content.lower():
        score += 10
        checks.append("✓ 3 Pertanyaan Muhasabah")
    else:
        checks.append("✗ 3 Pertanyaan Muhasabah")

    # 9. Quick Win Aksi Hari Ini (5%)
    if "quick win" in content.lower() or "aksi hari ini" in content.lower() or "lakukan sekarang" in content.lower():
        score += 5
        checks.append("✓ Quick Win Aksi Hari Ini")
    else:
        checks.append("✗ Quick Win Aksi Hari Ini")

    # 10. Visualisasi Bagan Obsidian Canvas (10%)
    if re.search(r'!\[\[canvas/.*?\.canvas\]\]', content):
        score += 10
        checks.append("✓ Bagan Konsep Obsidian Canvas (.canvas)")
    else:
        checks.append("✗ Bagan Konsep Obsidian Canvas (.canvas)")

    # 11. Zona 2 Infobox Standar Wiki (Bonus/Check)
    if "wiki-infobox" in content:
        checks.append("✓ Infobox Standar MediaWiki (.wiki-infobox)")
    else:
        checks.append("✗ Infobox Standar MediaWiki (.wiki-infobox)")

    # 12. Zona 4 Navbox Horizontal (Bonus/Check)
    if "wiki-navbox" in content:
        checks.append("✓ Navbox Kluster (.wiki-navbox)")
    else:
        checks.append("✗ Navbox Kluster (.wiki-navbox)")

    return score, checks

def main():
    files = get_all_md_files(CONTENT_DIR)
    print(f"=== WIKI-PKN LINTER REPORT ===")
    print(f"Total Markdown Files in '{CONTENT_DIR}': {len(files)}\n")

    inbound_links = defaultdict(int)
    broken_links = defaultdict(list)

    for key, f_meta in files.items():
        with open(f_meta["full_path"], "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
        links = extract_wikilinks(text)
        for target in links:
            target_key = target.lower()
            if target_key in files:
                inbound_links[target_key] += 1
            else:
                broken_links[target].append(f_meta["rel_path"])

    # 1. Broken Links
    print("--------------------------------------------------")
    print(f"1. BROKEN WIKILINKS AUDIT (Total Broken Targets: {len(broken_links)})")
    print("--------------------------------------------------")
    if broken_links:
        # Show top 15 most frequent broken targets
        sorted_broken = sorted(broken_links.items(), key=lambda x: len(x[1]), reverse=True)
        for target, referrers in sorted_broken[:15]:
            print(f"  ❌ [[{target}]] (referenced {len(referrers)}x, e.g. in {referrers[0]})")
    else:
        print("  🎉 No broken wikilinks found!")

    # 2. Orphan Pages
    orphans = [f_meta["rel_path"] for k, f_meta in files.items() if inbound_links[k] == 0 and not f_meta["rel_path"].startswith("index")]
    print("\n--------------------------------------------------")
    print(f"2. ORPHAN PAGES AUDIT (Total Inbound = 0: {len(orphans)})")
    print("--------------------------------------------------")
    print(f"  Found {len(orphans)} pages without inbound wikilinks.")
    for o in orphans[:10]:
        print(f"  ⚠️ {o}")
    if len(orphans) > 10:
        print(f"  ... and {len(orphans) - 10} more.")

    # 3. Sample Style Compliance Audit on Core Concept
    print("\n--------------------------------------------------")
    print("3. USTADZ ABDUL KHOLIQ STYLE COMPLIANCE SAMPLE AUDIT")
    print("--------------------------------------------------")
    sample_files = [
        "Pendidikan Karakter Nabawiyah.md",
        "Koneksi Sebelum Koreksi.md",
        "Materi SOTAB/ANAK PATUH ATAU ANAK SADAR.md",
        "Materi SOTAB/PENERIMAAN MENDAHULUI PERTUMBUHAN.md"
    ]
    for sf in sample_files:
        full_p = os.path.join(CONTENT_DIR, sf)
        if os.path.exists(full_p):
            with open(full_p, "r", encoding="utf-8") as f:
                c = f.read()
            sc, chk = audit_abdul_kholiq_style(c)
            print(f"File: {sf} | Style Score: {sc}/100")
            for item in chk[:5]:
                print(f"   {item}")

if __name__ == "__main__":
    main()

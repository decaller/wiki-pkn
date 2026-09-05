#!/usr/bin/env python3
"""
enrich_with_qaf.py
Mengintegrasikan hasil riset Qaf AI (maraji' turats) ke dalam artikel Wiki PKN:
1. Menambahkan Penerapan 4 Etape Usia Nabawiyah pada 16 artikel.
2. Menambahkan Instrumen Observasi & Evaluasi Diri Terapan pada 34 artikel.
3. Menambahkan Diagram Mermaid Konseptual (sanitized) pada 14 artikel.
Strict rule: ZERO DELETION (Hanya menambahkan sebelum ## Tautan atau di akhir).
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
QAF_DATA_FILE = ROOT / "data" / "qaf_insights.json"

qaf_data = {}
if QAF_DATA_FILE.exists():
    qaf_data = json.loads(QAF_DATA_FILE.read_text(encoding="utf-8"))

def insert_before_links(content, new_section):
    """Menyisipkan subbab baru sebelum '## Tautan' atau '## Tinjauan' atau di akhir."""
    patterns = [
        r"(##\s+(?:[0-9]+\.\s+)?Tautan[^\n]*)",
        r"(##\s+(?:[0-9]+\.\s+)?Peta Konsep[^\n]*)",
        r"(##\s+(?:[0-9]+\.\s+)?Referensi[^\n]*)",
    ]
    for pat in patterns:
        m = re.search(pat, content, re.IGNORECASE)
        if m:
            idx = m.start()
            return content[:idx] + new_section.strip() + "\n\n---\n\n" + content[idx:]
    
    # Jika tidak ditemukan heading tautan, taruh di paling akhir
    return content.rstrip() + "\n\n---\n\n" + new_section.strip() + "\n"

print("Memulai integrasi hasil riset Qaf AI...")

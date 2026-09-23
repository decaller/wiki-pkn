import os
import re

books_info = {
    "Review Buku Pendidikan Karakter Nabawiyah.md": {
        "url": "https://karakternabawiyah.com/buku-pendidikan-karakter-nabawiyah/",
        "canvas": "canvas/Review Buku/Peta Bab - Pendidikan Karakter Nabawiyah.canvas",
        "title": "Pendidikan Karakter Nabawiyah"
    },
    "Review Buku Tafsir Bakat.md": {
        "url": "https://karakternabawiyah.com/buku-tafsir-bakat-1/",
        "canvas": "canvas/Review Buku/Peta Bab - Tafsir Bakat.canvas",
        "title": "Tafsir Bakat 40 (TB-40)"
    },
    "Review Buku Menumbuhkan Kesadaran Beramal.md": {
        "url": "https://karakternabawiyah.com/buku-menumbuhkan-kesadaran-beramal/",
        "canvas": "canvas/Review Buku/Peta Bab - Menumbuhkan Kesadaran Beramal.canvas",
        "title": "Menumbuhkan Kesadaran Beramal"
    },
    "Review Buku Recovery Berbasis Fitrah.md": {
        "url": "https://karakternabawiyah.com/buku-recovery-berbasis-fitrah/",
        "canvas": "canvas/Review Buku/Peta Bab - Recovery Berbasis Fitrah.canvas",
        "title": "Recovery Berbasis Fitrah"
    },
    "Review Buku Kurikulum Sekolah Karakter Islam.md": {
        "url": "https://karakternabawiyah.com/buku-kurikulum-sekolah-karakter-islam/",
        "canvas": "canvas/Review Buku/Peta Bab - Kurikulum Sekolah Karakter Islam.canvas",
        "title": "Kurikulum Sekolah Karakter Islam"
    },
    "Review Buku Panduan Implementasi Standar PKN.md": {
        "url": "https://karakternabawiyah.com/panduan-implementasi-standar/",
        "canvas": "canvas/Review Buku/Peta Bab - Panduan Implementasi Standar PKN.canvas",
        "title": "Panduan Implementasi Standar PKN"
    },
    "Review Buku Panduan Kurikulum PAUD-TK Karakter Islam.md": {
        "url": "https://karakternabawiyah.com/buku-pendidikan-karakter-nabawiyah/",
        "canvas": "canvas/Review Buku/Peta Bab - Panduan Kurikulum PAUD-TK Karakter Islam.canvas",
        "title": "Panduan Kurikulum PAUD/TK Karakter Islam"
    },
    "Review Buku Bukanlah Sekejap.md": {
        "url": "https://karakternabawiyah.com/buku-menumbuhkan-kesadaran-beramal/",
        "canvas": "canvas/Review Buku/Peta Bab - Bukanlah Sekejap.canvas",
        "title": "Bukanlah Sekejap"
    }
}

for fname, bmeta in books_info.items():
    fpath = f"content/Referensi/{fname}"
    if not os.path.exists(fpath):
        print(f"Skipping {fname} (not found)")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Action bar anchor fix
    text = text.replace("#zone-1-header-action-bar--infobox-bibliografi", "#intisari-eksekutif--gagasan-utama")
    
    # 2. Zone headers replacement
    text = re.sub(r"^# ZONE 1:[^\n]*\n+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^# ZONE 2:[^\n]*", "## Intisari Eksekutif & Gagasan Utama", text, flags=re.MULTILINE)
    text = re.sub(r"^# ZONE 3:[^\n]*", "## Analisis Mendalam & Struktur Pembahasan", text, flags=re.MULTILINE)
    text = re.sub(r"^# ZONE 4:[^\n]*", "## Refleksi Penerapan & Takhrij Rujukan", text, flags=re.MULTILINE)

    # 3. Replace ASCII code block under "## 1. Peta Konsep Bab per Bab"
    pattern_ascii = re.compile(r"(## 1\. Peta Konsep Bab per Bab[\s\S]*?)```[\s\S]*?```", re.IGNORECASE)
    canvas_embed = f"![[{bmeta['canvas']}]]\n\n*Bagan Interaktif: Peta Alur Bab per Bab {bmeta['title']} (Gunakan zoom dan geser kursor untuk eksplorasi bagan interaktif).* \n"
    
    def repl_ascii(m):
        prefix = m.group(1)
        return prefix + canvas_embed
    
    text = pattern_ascii.sub(repl_ascii, text)

    # 4. Add prominent Purchase CTA banner if not already added
    cta_banner = f"""<div class="wiki-cta-box" style="margin: 1.5rem 0; padding: 1.25rem 1.5rem; background: linear-gradient(135deg, rgba(16, 185, 129, 0.08), rgba(14, 165, 233, 0.08)); border: 2px solid #10b981; border-radius: 8px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
  <div>
    <div style="font-size: 1.1rem; font-weight: 700; color: #065f46; margin-bottom: 0.25rem;">📖 Dapatkan Edisi Cetak Fisik Asli &amp; Lengkap</div>
    <div style="font-size: 0.9rem; color: var(--text-color);">Dukung dakwah manhaj PKN dengan memiliki buku fisik resmi karya Ustadz Abdul Kholiq langsung dari penerbit Yayasan Bina Insan Taqwa.</div>
  </div>
  <a href="{bmeta['url']}" target="_blank" rel="noopener noreferrer" style="display: inline-block; padding: 0.65rem 1.25rem; background: #059669; color: white; font-weight: 700; border-radius: 6px; text-decoration: none; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">🛒 Pesan Buku Resmi di KarakterNabawiyah.com ↗</a>
</div>"""

    if "wiki-cta-box" not in text:
        split_marker = "## Intisari Eksekutif & Gagasan Utama"
        if split_marker in text:
            parts = text.split(split_marker, 1)
            text = parts[0] + "\n" + cta_banner + "\n\n---\n\n" + split_marker + parts[1]
        
        nav_marker = '<div class="wiki-navbox">'
        if nav_marker in text:
            parts = text.split(nav_marker, 1)
            text = parts[0] + "\n" + cta_banner + "\n\n" + nav_marker + parts[1]

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Refactored {fname} successfully!")

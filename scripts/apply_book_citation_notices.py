import os, glob, re

# Define mapping rules for the 4 canonical books
rules = [
    {
        "name": "Buku Utama PKN",
        "review_link": "[[Review Buku Pendidikan Karakter Nabawiyah|Ulasan Lengkap & Pemesanan Buku Pendidikan Karakter Nabawiyah ↗]]",
        "book_title": "Pendidikan Karakter Nabawiyah",
        "patterns": [
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/**/*.md",
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/**/*.md",
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/**/*.md",
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/*.md"
        ],
        "notice": """> [!NOTE] Intisari & Kutipan Resmi Literatur
> Halaman ini merupakan ringkasan intisari dan kutipan resmi dari buku rujukan induk **Pendidikan Karakter Nabawiyah** karya Ustadz Abdul Kholiq (Yayasan Bina Insan Taqwa). Naskah disajikan secara padat sebagai panduan praktis dan tidak menggantikan kedalaman naskah buku aslinya.
> 📖 *Untuk telaah komprehensif, struktur bab, dan pemesanan buku fisik resmi, baca:* **[[Review Buku Pendidikan Karakter Nabawiyah|Ulasan Lengkap & Pemesanan Buku Pendidikan Karakter Nabawiyah ↗]]**."""
    },
    {
        "name": "Tafsir Bakat",
        "review_link": "[[Review Buku Tafsir Bakat|Ulasan Lengkap & Pemesanan Buku Tafsir Bakat ↗]]",
        "book_title": "Tafsir Bakat 40 (TB-40)",
        "patterns": [
            "content/Bakat/**/*.md",
            "content/Bakat/*.md"
        ],
        "notice": """> [!NOTE] Intisari & Kutipan Resmi Literatur
> Uraian pilar bakat ini merupakan intisari konseptual dan kutipan resmi dari buku **Tafsir Bakat 40 (TB-40)** karya Ustadz Abdul Kholiq (Yayasan Bina Insan Taqwa). Naskah disajikan secara ringkas untuk rujukan edukatif pendidik dan orang tua.
> 📖 *Untuk pemetaan 40 pilar lengkap, metodologi asesmen, dan pemesanan edisi cetak asli, baca:* **[[Review Buku Tafsir Bakat|Ulasan Lengkap & Pemesanan Buku Tafsir Bakat ↗]]**."""
    },
    {
        "name": "Menumbuhkan Kesadaran Beramal",
        "review_link": "[[Review Buku Menumbuhkan Kesadaran Beramal|Ulasan Lengkap & Pemesanan Buku Menumbuhkan Kesadaran Beramal ↗]]",
        "book_title": "Menumbuhkan Kesadaran Beramal",
        "patterns": [
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md",
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Benang Merah Pendidikan.md",
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md"
        ],
        "notice": """> [!NOTE] Intisari & Kutipan Resmi Literatur
> Halaman ini merupakan ringkasan intisari dan kutipan resmi dari buku **Menumbuhkan Kesadaran Beramal** karya Ustadz Abdul Kholiq (Yayasan Bina Insan Taqwa). Disajikan secara padat sebagai rujukan pedagogis penumbuhan motivasi intrinsik santri.
> 📖 *Untuk telaah mendalam, dinamika hati, dan pemesanan edisi fisik resmi, baca:* **[[Review Buku Menumbuhkan Kesadaran Beramal|Ulasan Lengkap & Pemesanan Buku Menumbuhkan Kesadaran Beramal ↗]]**."""
    },
    {
        "name": "Standar Implementasi",
        "review_link": "[[Review Buku Panduan Implementasi Standar PKN|Ulasan Lengkap & Pemesanan Buku Panduan Implementasi Standar PKN ↗]]",
        "book_title": "Panduan Implementasi Standar PKN",
        "patterns": [
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md",
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md",
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md",
            "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Program dan Kegiatan Pendidikan Karakter Nabawiyah.md"
        ],
        "notice": """> [!NOTE] Intisari & Kutipan Resmi Literatur
> Dokumen standarisasi ini merupakan ringkasan intisari dan kutipan resmi dari buku **Panduan Implementasi Standar PKN** karya Ustadz Abdul Kholiq (Yayasan Bina Insan Taqwa). Naskah disajikan dalam bentuk poin-poin standar kelembagaan siap pakai.
> 📖 *Untuk pedoman teknis lengkap, instrumen akreditasi, dan pemesanan buku fisik resmi, baca:* **[[Review Buku Panduan Implementasi Standar PKN|Ulasan Lengkap & Pemesanan Buku Panduan Implementasi Standar PKN ↗]]**."""
    }
]

total_updated = 0
for rule in rules:
    matched_files = set()
    for pat in rule["patterns"]:
        for f in glob.glob(pat, recursive=True):
            matched_files.add(f)
            
    for fpath in matched_files:
        if not os.path.isfile(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "Intisari & Kutipan Resmi Literatur" in content:
            continue
            
        # Place notice right after frontmatter or after the lead summary
        notice_block = rule["notice"] + "\n\n"
        
        # Check if there is a lead summary block `> [!SUMMARY]`
        summary_pos = content.find("> [!SUMMARY]")
        if summary_pos == -1:
            summary_pos = content.find("> [!summary]")
            
        if summary_pos != -1:
            # Find end of callout block (first line starting with non-quote after callout)
            lines = content.split("\n")
            insert_idx = -1
            in_summary = False
            for idx, line in enumerate(lines):
                if "> [!summary]" in line.lower():
                    in_summary = True
                elif in_summary and not line.startswith(">"):
                    insert_idx = idx
                    break
            if insert_idx != -1:
                lines.insert(insert_idx, "\n" + rule["notice"] + "\n")
                new_content = "\n".join(lines)
            else:
                new_content = content + "\n\n" + rule["notice"]
        else:
            # Insert after frontmatter
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    new_content = f"---{parts[1]}---\n\n{rule['notice']}\n{parts[2]}"
                else:
                    new_content = rule["notice"] + "\n\n" + content
            else:
                new_content = rule["notice"] + "\n\n" + content
                
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        total_updated += 1
        print(f"Applied citation notice: {fpath}")

print(f"Total updated files with citation notice: {total_updated}")

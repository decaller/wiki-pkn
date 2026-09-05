#!/usr/bin/env python3
"""
inject_images_to_articles.py
Menyisipkan horizontal banner (1050x350) di bagian atas setiap artikel wiki
dan menyematkan slide presentasi diagram rujukan resmi di sub-bab yang relevan.
Idempotent: aman dijalankan berulang kali tanpa duplikasi.
"""

import os
import re
import glob

CONTENT_DIR = "content"
BANNER_DIR = "content/assets/banners"
SLIDE_DIR = "content/assets/slides"

# Pemetaan spesifik banner tematik per folder/tema
BANNER_ASSIGNMENTS = {
    # Beranda & Dokumen Khusus
    "content/index.md": "banner-01.webp",
    "content/Master Katalog Dalil Al-Qur'an.md": "banner-02.webp",
    "content/Master Katalog Dalil Hadits dan Sunnah.md": "banner-03.webp",
    "content/Renungan/Hak dan Kewajiban.md": "banner-04.webp",
    "content/Renungan/index.md": "banner-04.webp",

    # Direktori Insan & Jiwa
    "Insan/index.md": "banner-05.webp",
    "Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md": "banner-06.webp",
    "Insan/Tujuan Hidup Manusia.md": "banner-07.webp",
    "Pembagian Jiwa/index.md": "banner-08.webp",
    "Pembagian Jiwa/Muthmainnah.md": "banner-09.webp",
    "Pembagian Jiwa/Lawwamah.md": "banner-10.webp",
    "Pembagian Jiwa/Ammarah.md": "banner-11.webp",

    # Fitrah & Bakat
    "Fitrah (Karakter)/index.md": "banner-12.webp",
    "Fitrah (Karakter)/Belajar.md": "banner-13.webp",
    "Fitrah (Karakter)/Iman/index.md": "banner-14.webp",
    "Fitrah (Karakter)/Iman/Tangki Cinta.md": "banner-15.webp",
    "Fitrah (Karakter)/Bakat/index.md": "banner-16.webp",
    "Fitrah (Karakter)/Bakat/Bekerja Keras.md": "banner-17.webp",
    "Fitrah (Karakter)/Bakat/Berpikir.md": "banner-18.webp",
    "Fitrah (Karakter)/Bakat/Berperasaan.md": "banner-19.webp",
    "Fitrah (Karakter)/Bakat/Memerintah.md": "banner-20.webp",
    "Fitrah (Karakter)/Bakat/Bekerja Sama.md": "banner-21.webp",
    "Fitrah (Karakter)/Bakat/Melayani.md": "banner-22.webp",
    "Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40.md": "banner-23.webp",
    "Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md": "banner-24.webp",

    # Etape Perkembangan
    "Fitrah (Karakter)/Perkembangan/index.md": "banner-25.webp",
    "Fitrah (Karakter)/Perkembangan/Thufulah.md": "banner-26.webp",
    "Fitrah (Karakter)/Perkembangan/Tamyiz.md": "banner-27.webp",
    "Fitrah (Karakter)/Perkembangan/Murahaqah.md": "banner-28.webp",
    "Fitrah (Karakter)/Perkembangan/Syabab.md": "banner-29.webp",

    # Pendidikan Ideal & Metode Mendidik
    "Pendidikan Ideal/index.md": "banner-30.webp",
    "Pendidikan Ideal/Benang Merah Pendidikan.md": "banner-31.webp",
    "Pendidikan Ideal/Pembelajaran Alamiah.md": "banner-32.webp",
    "Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md": "banner-33.webp",
    "Pendidikan Ideal/Bank Studi Kasus.md": "banner-34.webp",
    "Pendidikan Ideal/Batas Toleransi.md": "banner-35.webp",
    "Pendidikan Ideal/Imunitas Sosial.md": "banner-36.webp",
    "Pendidikan Ideal/Metode Mendidik/index.md": "banner-37.webp",
    "Pendidikan Ideal/Metode Mendidik/Bahasa Hati.md": "banner-38.webp",
    "Pendidikan Ideal/Metode Mendidik/Bahasa Lisan.md": "banner-39.webp",
    "Pendidikan Ideal/Metode Mendidik/Bahasa Tangan.md": "banner-40.webp",
    "Pendidikan Ideal/Luka dan Hutang Pengasuhan/index.md": "banner-08.webp",
    "Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md": "banner-09.webp",
    "Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md": "banner-10.webp",

    # Implementasi & Lembaga
    "Implementasi/index.md": "banner-34.webp",
    "Kaidah & Elemen/index.md": "banner-35.webp",
    "Kaidah & Elemen/8 Standar Implementasi PKN.md": "banner-36.webp",
    "Kaidah & Elemen/4 Elemen Implementasi.md": "banner-37.webp",
    "Kaidah & Elemen/4 Kaidah Implementasi.md": "banner-38.webp",
    "Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md": "banner-39.webp",
    "Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md": "banner-40.webp",
    "Peran & Tanggung Jawab/index.md": "banner-01.webp",
    "Peran & Tanggung Jawab/Peran Ayah dan Bunda.md": "banner-02.webp",
    "Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md": "banner-03.webp",
    "Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md": "banner-04.webp",
}

# Pemetaan penyematan slide diagram spesifik ke artikel
SLIDE_INJECTIONS = [
    # Piramida Pendidikan
    {
        "file_patterns": ["content/index.md", "Pendidikan Ideal/index.md"],
        "slide": "slide-piramida-pendidikan.webp",
        "caption": "Piramida Fondasi Pendidikan Karakter: Fondasi Aqidah & Karakter Sebelum Bangunan Ilmu dan Amal",
        "anchor": "## 1."
    },
    # 3 Kondisi Jiwa
    {
        "file_patterns": ["Pembagian Jiwa/index.md", "Bersatunya Ruh dan Jasad Membentuk Jiwa.md"],
        "slide": "slide-tiga-kondisi-jiwa.webp",
        "caption": "Tabel Tiga Tingkatan Nafsu Jiwa (Muthmainnah, Lawwamah, Ammarah)",
        "anchor": "## 1."
    },
    # Sistem Berpikir Jiwa
    {
        "file_patterns": ["Insan/index.md"],
        "slide": "slide-sistem-berpikir-jiwa.webp",
        "caption": "Sistem Berpikir Jiwa: Kesadaran Atas Sadar vs Dorongan Bawah Sadar",
        "anchor": "## 2."
    },
    # Sholat Barometer Jiwa
    {
        "file_patterns": ["content/index.md", "Pembagian Jiwa/Muthmainnah.md"],
        "slide": "slide-sholat-barometer.webp",
        "caption": "Kondisi Jiwa dalam Sholat: Sholat Sebagai Barometer Kematangan Batin Anak",
        "anchor": "Dalil Perintah Sholat"
    },
    # Metode Mendidik Tiga Jiwa
    {
        "file_patterns": ["Pendidikan Ideal/Metode Mendidik/index.md"],
        "slide": "slide-metode-mendidik-jiwa.webp",
        "caption": "Metode Mendidik Tiga Karakteristik Jiwa Anak",
        "anchor": "## 2."
    },
    # Prioritas Iman Sebelum Quran
    {
        "file_patterns": ["Fitrah (Karakter)/Iman/index.md", "Pendidikan Ideal/index.md"],
        "slide": "slide-prioritas-iman-quran.webp",
        "caption": "Prioritas Pendidikan Nabawiyah: Menanamkan Iman Sebelum Al-Qur'an (Atsar Jundub bin Abdillah)",
        "anchor": "## 2."
    },
    # Golden Age Pertumbuhan
    {
        "file_patterns": ["Fitrah (Karakter)/Perkembangan/index.md"],
        "slide": "slide-golden-age-pertumbuhan.webp",
        "caption": "Masa Emas Pertumbuhan Fitrah Anak (0-7 th, 7-10 th, 10-14 th, 15+ th)",
        "anchor": "## 1."
    },
    # Akhlak Tercela & Hutang Pengasuhan
    {
        "file_patterns": ["Luka dan Hutang Pengasuhan/index.md", "Luka dan Hutang Pengasuhan/Recovery.md"],
        "slide": "slide-akhlak-tercela-hutang.webp",
        "caption": "Akar Akhlak Tercela dari Luka dan Hutang Pengasuhan Masa Lalu",
        "anchor": "## 2."
    },
    # ABK
    {
        "file_patterns": ["Luka dan Hutang Pengasuhan/Euforia.md"],
        "slide": "slide-anak-kehebatan-khusus.webp",
        "caption": "Paradigma Anak Berkehebatan Khusus (ABK): Energi Bakat Ekstrem yang Membutuhkan Kanal Ma'ruf",
        "anchor": "## 2."
    },
    # Makna Al-Mauhibah
    {
        "file_patterns": ["Fitrah (Karakter)/Bakat/index.md"],
        "slide": "slide-makna-al-mauhibah.webp",
        "caption": "Makna Hakiki Al-Mauhibah (Bakat): Karunia Allah yang Melekat Kuat",
        "anchor": "## 1. Definisi"
    },
    # Syarat Dawam Bakat
    {
        "file_patterns": ["Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40.md"],
        "slide": "slide-syarat-dawam-bakat.webp",
        "caption": "Syarat Bakat Sejati: Konsistensi Tanpa Lelah (Dawam)",
        "anchor": "## 2."
    },
    # Rukun 3A
    {
        "file_patterns": ["Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md", "Fitrah (Karakter)/Bakat/index.md"],
        "slide": "slide-rukun-3a-bakat.webp",
        "caption": "Formula Rukun 3A Pengembangan Bakat (Alami, Acuhkan Kelemahan Minor, Asah Kekuatan Dominan)",
        "anchor": "Rukun"
    },
    # Reframing Kenakalan
    {
        "file_patterns": ["Fitrah (Karakter)/Bakat/index.md"],
        "slide": "slide-reframing-kenakalan-1.webp",
        "caption": "Kaidah Reframing: Ada Potensi Bakat Tersembunyi di Balik Kenakalan Anak",
        "anchor": "## 3. Paradigma Reframing"
    },
    # 40 Pilar Karakter
    {
        "file_patterns": ["Fitrah (Karakter)/index.md"],
        "slide": "slide-40-pilar-karakter.webp",
        "caption": "Taksonomi 40 Pilar Karakter Nabawiyah (Akhlaq Mulia Rasulullah ﷺ)",
        "anchor": "## 2."
    },
    # Matriks Polarisasi Bakat
    {
        "file_patterns": ["Bakat/Bekerja Keras.md", "Bakat/Memerintah.md"],
        "slide": "slide-matriks-polarisasi-bakat.webp",
        "caption": "Matriks Silsilah 6 Rumpun Bakat: Introvert (Sirr) vs Extrovert ('Alaniyah)",
        "anchor": "## 1."
    },
    # Peta Struktur TB40
    {
        "file_patterns": ["Bakat/Berpikir.md", "Bakat/Bekerja Sama.md", "Bakat/Melayani.md", "Bakat/Berperasaan.md"],
        "slide": "slide-peta-struktur-tb40.webp",
        "caption": "Peta Utuh Struktur & Silsilah Tafsir Bakat TB-40",
        "anchor": "## 1."
    },
    # Mendidik Seperti Bertani
    {
        "file_patterns": ["Pendidikan Ideal/Benang Merah Pendidikan.md"],
        "slide": "slide-mendidik-seperti-bertani.webp",
        "caption": "Filosofi Pendidikan Karakter: Mendidik Anak Seperti Bertani Merawat Benih Fitrah",
        "anchor": "## 1."
    },
    # Kertas Kosong vs Fitrah
    {
        "file_patterns": ["Pendidikan Ideal/Pembelajaran Alamiah.md"],
        "slide": "slide-kertas-kosong-vs-fitrah.webp",
        "caption": "Perbandingan Paradigma: Kertas Kosong (Tabula Rasa) vs Fitrah Qur'ani",
        "anchor": "## 1."
    },
    # Bahasa Hati 0-7 Tahun
    {
        "file_patterns": ["Metode Mendidik/Bahasa Hati.md", "Perkembangan/Thufulah.md", "Iman/Tangki Cinta.md"],
        "slide": "slide-bahasa-hati-0-7.webp",
        "caption": "Metode Pendidikan Usia 0–7 Tahun: Pengisian Penuh Bahasa Hati",
        "anchor": "## 1."
    },
    # Bahasa Lisan 7-10 Tahun
    {
        "file_patterns": ["Metode Mendidik/Bahasa Lisan.md", "Perkembangan/Tamyiz.md"],
        "slide": "slide-bahasa-lisan-7-10.webp",
        "caption": "Metode Pendidikan Usia 7–10 Tahun: Dialog Nalar & Bahasa Lisan Hikmah",
        "anchor": "## 1."
    },
    # Gaya Belajar Qurani
    {
        "file_patterns": ["Fitrah (Karakter)/Belajar.md"],
        "slide": "slide-gaya-belajar-qurani.webp",
        "caption": "Tiga Modalitas Gaya Belajar Qur'ani: As-Sam'u, Al-Bashar, Al-Fu'ad",
        "anchor": "## 1."
    },
    # Bahasa Tangan 10-Baligh
    {
        "file_patterns": ["Metode Mendidik/Bahasa Tangan.md", "Perkembangan/Murahaqah.md", "Pendidikan Ideal/Batas Toleransi.md", "Pendidikan Ideal/Imunitas Sosial.md"],
        "slide": "slide-bahasa-tangan-10-baligh.webp",
        "caption": "Metode Pendidikan Usia 10–Baligh: Ketegasan Bahasa Tangan & Batas Toleransi",
        "anchor": "## 1."
    },
    # Pembelajaran Berbasis Projek & Peristiwa
    {
        "file_patterns": ["Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md"],
        "slide": "slide-alur-kegiatan-projek.webp",
        "caption": "Alur Pembelajaran Berbasis Kegiatan Nyata (Project-Based Learning)",
        "anchor": "## 1."
    },
    {
        "file_patterns": ["Pendidikan Ideal/Bank Studi Kasus.md"],
        "slide": "slide-mengurai-kegiatan-karakter.webp",
        "caption": "Teknik Mengurai Kegiatan Lapangan ke Dalam 40 Pilar Karakter Nabawiyah",
        "anchor": "## 1."
    },
    # Etape Perkembangan Usia
    {
        "file_patterns": ["Insan/Tujuan Hidup Manusia.md", "Perkembangan/Syabab.md"],
        "slide": "slide-fase-perkembangan-tujuan.webp",
        "caption": "Akan Dijadikan Apa Anak Kita? Pendidikan Sesuai Maksud Penciptaannya",
        "anchor": "## 1."
    },
    {
        "file_patterns": ["Peran & Tanggung Jawab/Peran Ayah dan Bunda.md"],
        "slide": "slide-analogi-bertani-fase.webp",
        "caption": "Penerapan Analogi Bertani dalam Siklus Etape Usia Anak",
        "anchor": "## 1."
    },
    # Implementasi Persekolahan
    {
        "file_patterns": ["Kaidah & Elemen/8 Standar Implementasi PKN.md", "Kaidah & Elemen/4 Elemen Implementasi.md", "Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md"],
        "slide": "slide-implementasi-persekolahan.webp",
        "caption": "Rancang Bangun Implementasi Kurikulum PKN pada Lembaga Persekolahan",
        "anchor": "## 1."
    }
]

def get_banner_for_file(filepath):
    # Check explicit assignments
    for key, banner in BANNER_ASSIGNMENTS.items():
        if filepath.endswith(key) or key in filepath:
            return banner
    # Default cyclic banner based on path hash
    h = abs(hash(filepath)) % 40 + 1
    return f"banner-{h:02d}.webp"

def inject_banner(content, banner_file, filepath):
    # Check if banner already present
    if "assets/banners/" in content:
        return content, False

    banner_tag = f"\n![Banner Ilustrasi](/assets/banners/{banner_file})\n"

    # Insert right after the disclaimer callout:
    # Look for the end of "> [!note] Catatan Metodologi ..." callout
    disclaimer_match = re.search(r'(> \[!note\] Catatan Metodologi[\s\S]*?>.*?Tim SOTAB HEBAT.*?\n)', content)
    if disclaimer_match:
        end_pos = disclaimer_match.end()
        new_content = content[:end_pos] + banner_tag + content[end_pos:]
        return new_content, True

    # Otherwise, insert after H1
    h1_match = re.search(r'^(# [^\n]+)', content, re.MULTILINE)
    if h1_match:
        end_pos = h1_match.end()
        new_content = content[:end_pos] + "\n" + banner_tag + content[end_pos:]
        return new_content, True

    return banner_tag + "\n" + content, True

def inject_slide(content, slide_file, caption, anchor):
    # Check if slide already present
    if slide_file in content:
        return content, False

    slide_block = (
        f"\n\n![{caption}](/assets/slides/{slide_file})\n"
        f"*{caption}*\n\n"
    )

    # Try to find anchor heading
    pos = content.find(anchor)
    if pos != -1:
        # Find newline after anchor
        newline_pos = content.find("\n", pos)
        if newline_pos != -1:
            new_content = content[:newline_pos+1] + slide_block + content[newline_pos+1:]
            return new_content, True

    # If anchor not found, try inserting before the presentation citation callout or at bottom
    cit_pos = content.find("> [!quote] Dokumen & Slide Presentasi")
    if cit_pos != -1:
        new_content = content[:cit_pos] + slide_block + content[cit_pos:]
        return new_content, True

    return content + slide_block, True

def main():
    md_files = glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)
    print(f"[*] Processing {len(md_files)} markdown files in {CONTENT_DIR}...")

    banners_injected = 0
    slides_injected = 0

    for filepath in sorted(md_files):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # 1. Inject Banner
        banner_file = get_banner_for_file(filepath)
        content, b_added = inject_banner(content, banner_file, filepath)
        if b_added:
            banners_injected += 1

        # 2. Inject Slides
        for rule in SLIDE_INJECTIONS:
            matches = any(pattern in filepath for pattern in rule["file_patterns"])
            if matches:
                content, s_added = inject_slide(
                    content,
                    rule["slide"],
                    rule["caption"],
                    rule["anchor"]
                )
                if s_added:
                    slides_injected += 1

        # Write back if modified
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"\n[✓] Injected {banners_injected} horizontal banners across articles.")
    print(f"[✓] Injected {slides_injected} presentation slide diagrams across relevant sections.")

if __name__ == "__main__":
    main()

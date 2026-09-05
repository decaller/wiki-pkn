#!/usr/bin/env python3
"""
export_presentation_slides.py
Mengekspor halaman slide diagram kunci dari berbagai PDF resmi di old_backup/
menjadi berkas gambar WebP berkualitas tinggi di content/assets/slides/.
"""

import os
import sys
import subprocess
from PIL import Image

OUTPUT_DIR = "content/assets/slides"
TEMP_DIR = "/tmp/wiki_pkn_slides_temp"
DPI = 150
QUALITY = 88

SLIDE_DEFINITIONS = [
    # Piramida Fondasi Pendidikan
    {
        "pdf": "old_backup/Campur/PIRAMIDA PENDIDIKAN ANAK.pdf",
        "page": 1,
        "filename": "slide-piramida-pendidikan.webp",
        "title": "Piramida Fondasi Pendidikan Anak (Iman, Adab, Ilmu, Amal)"
    },
    # Kondisi 3 Jiwa & Barometer Sholat (Seminar 1)
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 1_ Kondisi Jiwa Anak.pdf",
        "page": 17,
        "filename": "slide-tiga-kondisi-jiwa.webp",
        "title": "Tabel Tiga Tingkatan Nafsu Jiwa (Muthmainnah, Lawwamah, Ammarah)"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 1_ Kondisi Jiwa Anak.pdf",
        "page": 20,
        "filename": "slide-sistem-berpikir-jiwa.webp",
        "title": "Sistem Berpikir Jiwa: Kesadaran Atas Sadar vs Dorongan Bawah Sadar"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 1_ Kondisi Jiwa Anak.pdf",
        "page": 29,
        "filename": "slide-sholat-barometer.webp",
        "title": "Kondisi Jiwa dalam Sholat sebagai Barometer Kematangan Batin"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 1_ Kondisi Jiwa Anak.pdf",
        "page": 35,
        "filename": "slide-metode-mendidik-jiwa.webp",
        "title": "Metode Mendidik Tiga Karakteristik Jiwa Anak"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 1_ Kondisi Jiwa Anak.pdf",
        "page": 43,
        "filename": "slide-prioritas-iman-quran.webp",
        "title": "Prioritas Pendidikan Nabawiyah: Menanamkan Iman Sebelum Al-Qur'an"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 1_ Kondisi Jiwa Anak.pdf",
        "page": 44,
        "filename": "slide-golden-age-pertumbuhan.webp",
        "title": "Masa Emas Pertumbuhan Fitrah Anak (0-7 th, 7-10 th, 10-14 th, 15+ th)"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 1_ Kondisi Jiwa Anak.pdf",
        "page": 55,
        "filename": "slide-akhlak-tercela-hutang.webp",
        "title": "Akar Akhlak Tercela dari Luka dan Hutang Pengasuhan Masa Lalu"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 1_ Kondisi Jiwa Anak.pdf",
        "page": 95,
        "filename": "slide-anak-kehebatan-khusus.webp",
        "title": "Paradigma Anak Berkehebatan Khusus (ABK): Energi Bakat Ekstrem"
    },
    # Bakat TB-40, Syarat, Rukun 3A, Reframing (Seminar 2)
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 2_ Tafsir Bakat  TB - 40.pdf",
        "page": 36,
        "filename": "slide-makna-al-mauhibah.webp",
        "title": "Makna Hakiki Al-Mauhibah (Bakat): Karunia Allah yang Melekat Kuat"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 2_ Tafsir Bakat  TB - 40.pdf",
        "page": 38,
        "filename": "slide-syarat-dawam-bakat.webp",
        "title": "Syarat Bakat Sejati: Konsistensi Tanpa Lelah (Dawam)"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 2_ Tafsir Bakat  TB - 40.pdf",
        "page": 39,
        "filename": "slide-rukun-3a-bakat.webp",
        "title": "Formula Rukun 3A Pengembangan Bakat (Alami, Acuhkan, Asah)"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 2_ Tafsir Bakat  TB - 40.pdf",
        "page": 54,
        "filename": "slide-reframing-kenakalan-1.webp",
        "title": "Kaidah Reframing: Ada Potensi Bakat Tersembunyi di Balik Kenakalan Anak"
    },
    {
        "pdf": "old_backup/Materi Seminar & Workshop PKN (Kupas Tuntas Tafsir Bakat)/Materi Seminar 2_ Tafsir Bakat  TB - 40.pdf",
        "page": 55,
        "filename": "slide-reframing-kenakalan-2.webp",
        "title": "Prinsip PKN: Tidak Ada Anak yang Nakal, Hanya Energi yang Belum Teredukasi"
    },
    # Peta 40 Pilar & Matriks Polarisasi (Akademi Guru Batch 3 - 2. BAKAT)
    {
        "pdf": "old_backup/Akademi Guru Batch 3/2. BAKAT - TB - 40.pdf",
        "page": 45,
        "filename": "slide-40-pilar-karakter.webp",
        "title": "Taksonomi 40 Pilar Karakter Nabawiyah (Akhlaq Mulia Rasulullah ﷺ)"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/2. BAKAT - TB - 40.pdf",
        "page": 74,
        "filename": "slide-matriks-polarisasi-bakat.webp",
        "title": "Matriks Silsilah 6 Rumpun Bakat: Introvert (Sirr) vs Extrovert ('Alaniyah)"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/2. BAKAT - TB - 40.pdf",
        "page": 96,
        "filename": "slide-peta-struktur-tb40.webp",
        "title": "Peta Utuh Struktur & Silsilah Tafsir Bakat TB-40"
    },
    # Metode Pendidikan Karakter Nabawiyah (3 Bahasa)
    {
        "pdf": "old_backup/Akademi Guru Batch 3/4. METODE PENDIDIKAN KARAKTER NABAWIYAH.pdf",
        "page": 12,
        "filename": "slide-mendidik-seperti-bertani.webp",
        "title": "Filosofi Pendidikan Karakter: Mendidik Anak Seperti Bertani Merawat Benih"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/4. METODE PENDIDIKAN KARAKTER NABAWIYAH.pdf",
        "page": 17,
        "filename": "slide-kertas-kosong-vs-fitrah.webp",
        "title": "Perbandingan Paradigma: Kertas Kosong (Tabula Rasa) vs Fitrah Qur'ani"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/4. METODE PENDIDIKAN KARAKTER NABAWIYAH.pdf",
        "page": 64,
        "filename": "slide-bahasa-hati-0-7.webp",
        "title": "Metode Pendidikan Usia 0–7 Tahun: Pengisian Penuh Bahasa Hati"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/4. METODE PENDIDIKAN KARAKTER NABAWIYAH.pdf",
        "page": 74,
        "filename": "slide-bahasa-lisan-7-10.webp",
        "title": "Metode Pendidikan Usia 7–10 Tahun: Dialog Nalar & Bahasa Lisan Hikmah"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/4. METODE PENDIDIKAN KARAKTER NABAWIYAH.pdf",
        "page": 75,
        "filename": "slide-gaya-belajar-qurani.webp",
        "title": "Tiga Modalitas Gaya Belajar Qur'ani: As-Sam'u, Al-Bashar, Al-Fu'ad"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/4. METODE PENDIDIKAN KARAKTER NABAWIYAH.pdf",
        "page": 88,
        "filename": "slide-bahasa-tangan-10-baligh.webp",
        "title": "Metode Pendidikan Usia 10–Baligh: Ketegasan Bahasa Tangan & Batas Toleransi"
    },
    # Pembelajaran Berbasis Projek
    {
        "pdf": "old_backup/Akademi Guru Batch 3/3. PEMBELAJARAN BERBASIS PROJEK.pdf",
        "page": 5,
        "filename": "slide-alur-kegiatan-projek.webp",
        "title": "Alur Pembelajaran Berbasis Kegiatan Nyata (Project-Based Learning)"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/3. PEMBELAJARAN BERBASIS PROJEK.pdf",
        "page": 6,
        "filename": "slide-peristiwa-moment.webp",
        "title": "Pemanfaatan Momentum Peristiwa Alamiah Sebagai Media Pendidikan Jiwa"
    },
    {
        "pdf": "old_backup/Akademi Guru Batch 3/3. PEMBELAJARAN BERBASIS PROJEK.pdf",
        "page": 7,
        "filename": "slide-mengurai-kegiatan-karakter.webp",
        "title": "Teknik Mengurai Kegiatan Lapangan ke Dalam 40 Pilar Karakter Nabawiyah"
    },
    # Penahapan Fase Usia (Temu Lembaga 6)
    {
        "pdf": "old_backup/Temu Lembaga 6/2. Mendidik Sesuai Fase Perkembangan Anak.pdf",
        "page": 2,
        "filename": "slide-fase-perkembangan-tujuan.webp",
        "title": "Akan Dijadikan Apa Anak Kita? Pendidikan Sesuai Maksud Penciptaannya"
    },
    {
        "pdf": "old_backup/Temu Lembaga 6/2. Mendidik Sesuai Fase Perkembangan Anak.pdf",
        "page": 60,
        "filename": "slide-analogi-bertani-fase.webp",
        "title": "Penerapan Analogi Bertani dalam Siklus Etape Usia Anak"
    },
    # Implementasi Persekolahan
    {
        "pdf": "old_backup/Akademi Guru Batch 3/6. Implementasi Kurikulum PKN Pada  Persekolahan.pdf",
        "page": 1,
        "filename": "slide-implementasi-persekolahan.webp",
        "title": "Rancang Bangun Implementasi Kurikulum PKN pada Lembaga Persekolahan"
    }
]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)
    
    print(f"[*] Exporting {len(SLIDE_DEFINITIONS)} key presentation slides to {OUTPUT_DIR}...")
    success_count = 0
    
    for item in SLIDE_DEFINITIONS:
        pdf_path = item["pdf"]
        page_num = item["page"]
        out_filename = item["filename"]
        out_path = os.path.join(OUTPUT_DIR, out_filename)
        
        if not os.path.exists(pdf_path):
            print(f"  [!] Missing PDF: {pdf_path}", file=sys.stderr)
            continue
            
        temp_prefix = os.path.join(TEMP_DIR, f"temp_{page_num}")
        cmd = [
            "pdftoppm",
            "-png",
            "-r", str(DPI),
            "-f", str(page_num),
            "-l", str(page_num),
            pdf_path,
            temp_prefix
        ]
        
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Find generated PNG
            temp_files = [f for f in os.listdir(TEMP_DIR) if f.startswith(f"temp_{page_num}") and f.endswith(".png")]
            if not temp_files:
                print(f"  [!] Failed to generate PNG for {pdf_path} p.{page_num}", file=sys.stderr)
                continue
                
            temp_png = os.path.join(TEMP_DIR, temp_files[0])
            with Image.open(temp_png) as im:
                im = im.convert("RGB")
                # Optimize to webp
                im.save(out_path, "WEBP", quality=QUALITY, method=6)
                
            # Cleanup temp file
            os.remove(temp_png)
            
            size_kb = os.path.getsize(out_path) / 1024
            print(f"  [+] p.{page_num:03d} -> {out_filename:36} | {size_kb:.1f} KB | {item['title'][:55]}")
            success_count += 1
            
        except Exception as e:
            print(f"  [!] Error on {pdf_path} p.{page_num}: {e}", file=sys.stderr)
            
    # Cleanup temp dir
    try:
        for f in os.listdir(TEMP_DIR):
            os.remove(os.path.join(TEMP_DIR, f))
        os.rmdir(TEMP_DIR)
    except Exception:
        pass
        
    print(f"\n[✓] Completed: {success_count}/{len(SLIDE_DEFINITIONS)} presentation slides exported.")

if __name__ == "__main__":
    main()

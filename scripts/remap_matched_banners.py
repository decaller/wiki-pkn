#!/usr/bin/env python3
"""
remap_matched_banners.py
Mencocokkan banner foto berdasarkan hasil analisis vision OMP di data/gambar_properties.json.
- Membersihkan banner lama yang dipasang secara acak/tidak cocok
- Hanya menyematkan banner foto pada artikel yang BENAR-BENAR COCOK dengan konteks gambar
- Menambahkan alt-text semantik sesuai hasil deteksi OMP
"""

import os
import re
import json
import glob

PROPERTIES_FILE = "data/gambar_properties.json"
CONTENT_DIR = "content"

# Peta kecocokan presisi 1-to-1 berbasis hasil analisis OMP
MATCHED_BANNERS = {
    # x1: Timbangan keadilan & palu hakim -> Hak dan Kewajiban & Tanggung Jawab Pendidikan
    "content/Renungan/Hak dan Kewajiban.md": {
        "banner": "banner-01.webp",
        "alt": "Timbangan Keadilan dan Penegakan Hak Syariat"
    },
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md": {
        "banner": "banner-01.webp",
        "alt": "Amanah Keadilan dan Tanggung Jawab Pendidikan"
    },

    # x5: Pelayan menyajikan hidangan dengan adab -> Pilar Melayani
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Melayani.md": {
        "banner": "banner-05.webp",
        "alt": "Karakter Khidmah: Adab dan Keikhlasan dalam Melayani"
    },

    # x6: Anak laki-laki fokus menulis tekun -> Fitrah Belajar & Fase Tamyiz
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Belajar.md": {
        "banner": "banner-06.webp",
        "alt": "Fitrah Belajar Anak: Ketekunan Menuntut Ilmu"
    },
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Tamyiz.md": {
        "banner": "banner-06.webp",
        "alt": "Fase Tamyiz: Semangat Belajar dan Pembiasaan Amal"
    },

    # x8: Pemuda merenung di bangku kayu -> Pilar Berpikir / Tafakkur
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Berpikir.md": {
        "banner": "banner-08.webp",
        "alt": "Tafakkur dan Tadabbur: Merenungi Tanda Kekuasaan Allah"
    },

    # x9: Tangan mengepal erat menahan gejolak amarah -> Jiwa Ammarah & Manajemen Emosi
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Ammarah.md": {
        "banner": "banner-09.webp",
        "alt": "Pengendalian Hawa Nafsu: Menjinakkan Gejolak Nafsu Ammarah"
    },

    # x10: Anak kecil tersenyum polos di balik jendela -> Fase Thufulah (0-7 th) & Fitrah
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Thufulah.md": {
        "banner": "banner-10.webp",
        "alt": "Fase Thufulah: Menjaga Kemurnian Senyum dan Fitrah Anak Usia Dini"
    },

    # x11: Pria menganalisis papan strategi -> Panduan Asesmen TB40 / Kurikulum
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40.md": {
        "banner": "banner-11.webp",
        "alt": "Pemetaan Sistematis dan Analisis Karakter Bakat TB-40"
    },

    # x12: Tangan bertautan erat berdoa & muhasabah batin -> Jiwa Lawwamah
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Lawwamah.md": {
        "banner": "banner-12.webp",
        "alt": "Nafsul Lawwamah: Introspeksi, Muhasabah, dan Penyesalan Hati"
    },

    # x14: Dua orang berdialog hikmah di luar ruangan -> Metode Bahasa Lisan
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Lisan.md": {
        "banner": "banner-14.webp",
        "alt": "Komunikasi Hikmah: Bahasa Lisan Dialogis Penuh Adab"
    },

    # x15: Lansia merenung dalam proses pemulihan -> Pemulihan Luka Pengasuhan (Recovery)
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md": {
        "banner": "banner-15.webp",
        "alt": "Protokol Pemulihan Hati: Menyembuhkan Luka dan Hutang Pengasuhan"
    },
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/index.md": {
        "banner": "banner-15.webp",
        "alt": "Refleksi Mendalam Luka dan Hutang Pengasuhan"
    },

    # x16: Koki fokus memotong bahan dengan ketelitian tinggi -> Pilar Bekerja Keras & Ihsan
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Bekerja Keras.md": {
        "banner": "banner-16.webp",
        "alt": "Etos Kerja Keras dan Ketelitian (Itqan) Menuju Ihsan"
    },

    # x18: Menahan dan melerai konflik -> Batas Toleransi & Imunitas Sosial
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md": {
        "banner": "banner-18.webp",
        "alt": "Ketegasan Sikap dan Pengendalian Diri dalam Menegakkan Batas Toleransi"
    },
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Imunitas Sosial.md": {
        "banner": "banner-18.webp",
        "alt": "Membangun Imunitas Sosial Menghadapi Tekanan Lingkungan"
    },

    # x19: Relawan berbagi makanan dan empati sosial -> Menumbuhkan Kesadaran Beramal
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md": {
        "banner": "banner-19.webp",
        "alt": "Kesadaran Beramal Nyata: Berbagi Kemanfaatan bagi Umat"
    },

    # x20: Menjaga lisan dengan tenang -> Pilar Berperasaan & Shamt (Diam)
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Berperasaan.md": {
        "banner": "banner-20.webp",
        "alt": "Kepekaan Jiwa Berperasaan dan Adab Menjaga Lisan"
    },

    # x21: Kehangatan interaksi dan senyum tulus -> Metode Bahasa Hati
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Hati.md": {
        "banner": "banner-21.webp",
        "alt": "Bahasa Hati: Membangun Kelekatan Jiwa dan Kehangatan Cinta"
    },

    # x22: Duel atlet basket di udara -> Fase Murahaqah (10-15 th) & Energi Fisik
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md": {
        "banner": "banner-22.webp",
        "alt": "Fase Murahaqah: Penyaluran Energi Kepemudaan dan Ketangkasan Fisik"
    },

    # x23: Anak membaca bersama di alam rumput terbuka -> Pembelajaran Alamiah
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Pembelajaran Alamiah.md": {
        "banner": "banner-23.webp",
        "alt": "Pembelajaran Alamiah: Menimba Hikmah di Alam Terbuka Bebas Sekat"
    },

    # x24: Kerjasama sinergis atlet bertumpuk tangan -> Pilar Bekerja Sama
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Bekerja Sama.md": {
        "banner": "banner-24.webp",
        "alt": "Karakter Ta'aawun: Membangun Sinergi dan Kerjasama Umat"
    },

    # x26: Pria bersyukur dan damai menatap langit -> Jiwa Muthmainnah
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Muthmainnah.md": {
        "banner": "banner-26.webp",
        "alt": "Nafsul Muthmainnah: Jiwa yang Tenang dalam Naungan Ridha Ilahi"
    },

    # x27: Jabat tangan kemitraan profesional -> Peran Guru & Sinergi Lembaga
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md": {
        "banner": "banner-27.webp",
        "alt": "Sinergi Kemitraan: Kolaborasi Amanah antara Rumah dan Sekolah"
    },

    # x29: Petani memikul beban hasil panen -> Benang Merah Pendidikan (Analogi Bertani)
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Benang Merah Pendidikan.md": {
        "banner": "banner-29.webp",
        "alt": "Analogi Bertani: Kesabaran Merawat Benih Fitrah Hingga Menuai Hasil"
    },

    # x30: Membelai kucing dengan penuh kelembutan -> Tangki Cinta & Rahmah
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/Tangki Cinta.md": {
        "banner": "banner-30.webp",
        "alt": "Pengisian Tangki Cinta: Menumbuhkan Belas Kasih dan Kelembutan Fitrah"
    },

    # x31: Berdiri di tepi tebing memandang cakrawala luas -> Tujuan Hidup Manusia
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Tujuan Hidup Manusia.md": {
        "banner": "banner-31.webp",
        "alt": "Tujuan Hidup Manusia: Memikul Mandat Khilafah dan 'Ibadurrahman"
    },

    # x33: Pelatihan dan workshop pendidikan komprehensif -> Kaidah di Berbagai Lembaga
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md": {
        "banner": "banner-33.webp",
        "alt": "Standardisasi dan Pelatihan Implementasi PKN di Berbagai Lembaga"
    },

    # x34: Diskusi matang berdua di meja -> Peran Ayah dan Bunda
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md": {
        "banner": "banner-34.webp",
        "alt": "Nakhoda Keluarga: Musyawarah dan Penyelarasan Peran Ayah Bunda"
    },

    # x35: Pembicara di podium kepemimpinan -> Pilar Memerintah / Al-Qiyadah
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Memerintah.md": {
        "banner": "banner-35.webp",
        "alt": "Karakter Al-Qiyadah: Kepemimpinan Nabawiyah dan Pengaruh Peradaban"
    },

    # x36: Pemuda saling merangkul di senja hari -> Fase Syabab (Akil Baligh Mandiri)
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Syabab.md": {
        "banner": "banner-36.webp",
        "alt": "Fase Syabab: Kemandirian Pemuda Akil Baligh Pembawa Risalah"
    },

    # x40: Atlet berpelukan tulus saling menguatkan -> Fitrah Iman & Mahabbah
    "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/index.md": {
        "banner": "banner-40.webp",
        "alt": "Fitrah Iman: Tali Persaudaraan Batin dan Cinta Karena Allah"
    },
}

def clean_old_banners(content):
    # Regex to remove any existing banner markdown line
    cleaned = re.sub(r'\n*!\[Banner[^\]]*\]\(/assets/banners/[^)]+\)\n*', '\n\n', content)
    return cleaned

def inject_matched_banner(content, banner_info):
    banner_file = banner_info["banner"]
    alt_text = banner_info["alt"]
    banner_tag = f"\n![{alt_text}](/assets/banners/{banner_file})\n"

    # Insert right after disclaimer callout if present
    disclaimer_match = re.search(r'(> \[!note\] Catatan Metodologi[\s\S]*?>.*?Tim SOTAB HEBAT.*?\n)', content)
    if disclaimer_match:
        end_pos = disclaimer_match.end()
        return content[:end_pos] + banner_tag + content[end_pos:]

    # Else insert right after H1
    h1_match = re.search(r'^(# [^\n]+)', content, re.MULTILINE)
    if h1_match:
        end_pos = h1_match.end()
        return content[:end_pos] + "\n" + banner_tag + content[end_pos:]

    return banner_tag + "\n" + content

def main():
    md_files = glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)
    print(f"[*] Processing {len(md_files)} markdown files...")

    cleaned_count = 0
    injected_count = 0

    for filepath in sorted(md_files):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # 1. Clean all existing banner lines
        content = clean_old_banners(content)

        # 2. Check if this file has a genuine contextual match
        matched = False
        for path_key, banner_info in MATCHED_BANNERS.items():
            if filepath == path_key or filepath.endswith(path_key):
                content = inject_matched_banner(content, banner_info)
                matched = True
                injected_count += 1
                print(f"  [+] Matched: {os.path.basename(filepath):35} -> {banner_info['banner']} ({banner_info['alt']})")
                break

        if not matched:
            cleaned_count += 1

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"\n[✓] Finished!")
    print(f"    - Only {injected_count} articles with genuine contextual matches now have banners.")
    print(f"    - {cleaned_count} articles have been cleaned of random/unmatched banners.")

if __name__ == "__main__":
    main()

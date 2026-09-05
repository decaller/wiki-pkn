#!/usr/bin/env python3
"""
Script to prepare and isolate the latest unique PPTX presentations into a dedicated folder
(presentations/) for uploading to OneDrive via Rclone and embedding in Wiki PKN.
"""

import os
import glob
import re
import shutil
import json
import hashlib
from datetime import datetime

# 39 Canonical presentation topics & clean URL-safe filenames
CANONICAL_TOPICS = {
    'konsep_umum_pkn': {
        'clean_name': '00-konsep-umum-pkn.pptx',
        'title': 'Konsep Umum PKN (Materi 0)',
        'targets': [
            'content/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/index.md'
        ]
    },
    'mengembalikan_pendidikan_ke_asalnya': {
        'clean_name': '01-mengembalikan-pendidikan-ke-asalnya.pptx',
        'title': '1. Mengembalikan Pendidikan ke Asalnya',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Tujuan Hidup Manusia.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Benang Merah Pendidikan.md'
        ]
    },
    'pendidikan_akhlaq_materi_1': {
        'clean_name': '02-pendidikan-akhlaq-materi-1.pptx',
        'title': '1. Pendidikan Akhlaq (Materi 1)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Belajar.md'
        ]
    },
    'jiwa_dan_metode_mendidiknya': {
        'clean_name': '03-jiwa-dan-metode-mendidiknya.pptx',
        'title': '1. Jiwa dan Metode Mendidiknya',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Ammarah.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Lawwamah.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Muthmainnah.md'
        ]
    },
    'mendidik_sesuai_fase_perkembangan_anak': {
        'clean_name': '04-mendidik-sesuai-fase-perkembangan.pptx',
        'title': '2. Mendidik Sesuai Fase Perkembangan Anak',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Thufulah.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Tamyiz.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Syabab.md'
        ]
    },
    'menangani_anak_yang_bermasalah': {
        'clean_name': '05-menangani-anak-bermasalah.pptx',
        'title': '2. Menangani Anak yang Bermasalah',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Bank Studi Kasus.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md'
        ]
    },
    'bullying': {
        'clean_name': '06-bullying-kipmi.pptx',
        'title': 'Penanganan Bullying (KIPMI)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Bank Studi Kasus.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Imunitas Sosial.md'
        ]
    },
    'pemulihan_karakter_materi_3': {
        'clean_name': '07-pemulihan-karakter-materi-3.pptx',
        'title': '3. Pemulihan Karakter (Materi 3)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md'
        ]
    },
    'recovery_kesadaran': {
        'clean_name': '08-recovery-kesadaran.pptx',
        'title': 'Recovery Kesadaran Fitrah',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md'
        ]
    },
    'metode_pkn': {
        'clean_name': '09-metode-pendidikan-karakter-nabawiyah.pptx',
        'title': '4. Metode Pendidikan Karakter Nabawiyah',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Hati.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Lisan.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Tangan.md'
        ]
    },
    'piramida_pendidikan_anak': {
        'clean_name': '10-piramida-pendidikan-anak.pptx',
        'title': 'Piramida Pendidikan Anak (3 Bahasa)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md'
        ]
    },
    'pembelajaran_alamiah': {
        'clean_name': '11-pembelajaran-alamiah.pptx',
        'title': '4. Pembelajaran Alamiah',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Pembelajaran Alamiah.md'
        ]
    },
    'tambal_sulam': {
        'clean_name': '12-tambal-sulam-pembelajaran.pptx',
        'title': '6. Tambal Sulam Pembelajaran',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Pembelajaran Alamiah.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Belajar.md'
        ]
    },
    'bakat_tb40': {
        'clean_name': '13-tafsir-bakat-tb40.pptx',
        'title': '3. Tafsir Bakat TB-40',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/TB40/index.md'
        ]
    },
    'bedah_buku_tafsir_bakat_2024': {
        'clean_name': '14-bedah-buku-tafsir-bakat-2024.pptx',
        'title': 'Bedah Buku Tafsir Bakat (2024)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md'
        ]
    },
    'bakat_dalam_pendidikan_islam_2023': {
        'clean_name': '15-bakat-dalam-pendidikan-islam.pptx',
        'title': 'Bakat dalam Pendidikan Islam (2023)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md'
        ]
    },
    '40_pilar_karakter': {
        'clean_name': '16-40-pilar-karakter-kurikulum.pptx',
        'title': '1. 40 Pilar Karakter diurai dalam Kurikulum',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Memerintah.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Berpikir.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Berperasaan.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Melayani.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Bekerja Keras.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Bekerja Sama.md'
        ]
    },
    'pendidikan_bakat_materi_2': {
        'clean_name': '17-pendidikan-bakat-materi-2.pptx',
        'title': '2. Pendidikan Bakat (Materi 2)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md'
        ]
    },
    'pembelajaran_berbasis_projek': {
        'clean_name': '18-pembelajaran-berbasis-projek.pptx',
        'title': '3. Pembelajaran Berbasis Projek',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md'
        ]
    },
    'implementasi_kurikulum_persekolahan': {
        'clean_name': '19-implementasi-kurikulum-persekolahan.pptx',
        'title': '6. Implementasi Kurikulum PKN pada Persekolahan',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md'
        ]
    },
    'panduan_implementasi_standar_pkn': {
        'clean_name': '20-panduan-implementasi-standar-pkn.pptx',
        'title': 'Panduan Implementasi Standar PKN',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md'
        ]
    },
    'evaluasi_pkn': {
        'clean_name': '21-evaluasi-pkn.pptx',
        'title': '7. Evaluasi Pendidikan Karakter Nabawiyah',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md'
        ]
    },
    'menyibak_pondasi': {
        'clean_name': '22-menyibak-pondasi-pendidikan.pptx',
        'title': '5. Menyibak Pondasi Pendidikan yang Tak Tersentuh',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/index.md'
        ]
    },
    'pendidikan_karakter_nabawiyah_2023': {
        'clean_name': '23-pendidikan-karakter-nabawiyah-2023.pptx',
        'title': 'Pendidikan Karakter Nabawiyah (Materi 2023)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/index.md'
        ]
    },
    '10_masalah_pendidikan': {
        'clean_name': '24-10-masalah-pendidikan.pptx',
        'title': '10 Masalah Pendidikan Generasi',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/index.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/FAQ Ringkas.md'
        ]
    },
    'all_about_puberty': {
        'clean_name': '25-all-about-puberty.pptx',
        'title': 'All About Puberty (Karima)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md'
        ]
    },
    'asyiknya_menjadi_diri_sendiri': {
        'clean_name': '26-asyiknya-menjadi-diri-sendiri.pptx',
        'title': 'Asyiknya Menjadi Diri Sendiri (Kelas 6)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Syabab.md'
        ]
    },
    'pemetaan_siswa_x_smkn_4_2024': {
        'clean_name': '27-pemetaan-siswa-smkn4.pptx',
        'title': 'Pemetaan Siswa X SMKN 4 (2024)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Syabab.md'
        ]
    },
    'mendidik_generasi_alfa_2': {
        'clean_name': '28-mendidik-generasi-alfa.pptx',
        'title': 'Mendidik Generasi Alfa 2',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md'
        ]
    },
    'setiap_anak_hebat': {
        'clean_name': '29-setiap-anak-adalah-hebat.pptx',
        'title': 'Setiap Anak Adalah Hebat (2024)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md'
        ]
    },
    'setiap_anak_hebat_walisantri': {
        'clean_name': '30-setiap-anak-hebat-walisantri.pptx',
        'title': 'Setiap Anak Adalah Hebat (Walisantri 2024)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md'
        ]
    },
    'pemetaan_gaya_anak': {
        'clean_name': '31-pemetaan-gaya-anak.pptx',
        'title': 'Pemetaan Gaya Anak',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Belajar.md'
        ]
    },
    'menumbuhkan_kesadaran': {
        'clean_name': '32-menumbuhkan-kesadaran-2025.pptx',
        'title': 'Menumbuhkan Kesadaran (2025)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md',
            'content/index.md'
        ]
    },
    'mozaik_implementasi': {
        'clean_name': '33-mozaik-implementasi-fitrah.pptx',
        'title': 'Mozaik Implementasi Pendidikan Fitrah',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Arahan Teknis Implementasi.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight/SOTABH.md'
        ]
    },
    'penerapan_pkn_materi_4': {
        'clean_name': '34-penerapan-pkn-materi-4.pptx',
        'title': '4. Penerapan PKN (Materi 4)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Arahan Teknis Implementasi.md'
        ]
    },
    'rumusan_hasil_share': {
        'clean_name': '35-rumusan-hasil-share-diskusi.pptx',
        'title': 'Rumusan Hasil Share dan Diskusi PKN',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Arahan Teknis Implementasi.md'
        ]
    },
    'pembekalan_musyrif': {
        'clean_name': '36-pembekalan-musyrif.pptx',
        'title': 'Pembekalan Musyrif',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md',
            'content/Renungan/Hak dan Kewajiban.md'
        ]
    },
    'talent_camp_2025': {
        'clean_name': '37-talent-camp-2025.pptx',
        'title': 'Talent Camp (2025)',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Imunitas Sosial.md',
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md'
        ]
    },
    'beda_adab_&_akhlaq_+_kualitas_hidup': {
        'clean_name': '38-beda-adab-akhlaq-kualitas-hidup.pptx',
        'title': 'Beda Adab & Akhlaq + Kualitas Hidup',
        'targets': [
            'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/index.md'
        ]
    }
}

def get_canonical_key(name):
    n = re.sub(r'^\d+[\.\_]\s*', '', name)
    n = re.sub(r'\[\d+\]', '', n)
    n = n.replace('.pptx', '').strip().lower()
    n = re.sub(r'[\s\-_]+', '_', n)
    if 'bakat_tb_40' in n or 'bakat_tb40' in n or 'tafsir_bakat_tb_40' in n or n == 'bakat':
        return 'bakat_tb40'
    if '40_pilar_karakter' in n:
        return '40_pilar_karakter'
    if 'pembelajaran_berbasis_projek' in n:
        return 'pembelajaran_berbasis_projek'
    if 'metode_pendidikan_karakter_nabawiyah' in n:
        return 'metode_pkn'
    if 'menyibak_pondasi' in n:
        return 'menyibak_pondasi'
    if 'implementasi_kurikulum_pkn' in n:
        return 'implementasi_kurikulum_persekolahan'
    if 'evaluasi_pendidikan_karakter_nabawiyah' in n:
        return 'evaluasi_pkn'
    if 'pembelajaran_alamiah' in n or 'pembelajaran_alamiyah' in n:
        return 'pembelajaran_alamiah'
    if 'konsep_pkn' in n or 'konsep_umum_pkn' in n:
        return 'konsep_umum_pkn'
    if 'tambal_sulam' in n:
        return 'tambal_sulam'
    if 'menumbuhkan_kesadaran' in n:
        return 'menumbuhkan_kesadaran'
    if 'mozaik_implementasi' in n:
        return 'mozaik_implementasi'
    if 'asyiknya_menjadi_diri_sendiri' in n:
        return 'asyiknya_menjadi_diri_sendiri'
    if 'all_about_puberty' in n:
        return 'all_about_puberty'
    if 'bullying' in n:
        return 'bullying'
    if 'setiap_anak_adalah_hebat' in n and 'walisantri' not in n:
        return 'setiap_anak_hebat'
    if 'setiap_anak_adalah_hebat' in n and 'walisantri' in n:
        return 'setiap_anak_hebat_walisantri'
    if 'rumusan_hasil_share' in n:
        return 'rumusan_hasil_share'
    if 'panduan_implementasi_standar_pkn' in n:
        return 'panduan_implementasi_standar_pkn'
    return n

def main():
    print("=== Scanning all PPTX files in old_backup/ ===")
    pptx_files = []
    for root, dirs, files in os.walk('old_backup'):
        for f in files:
            if f.lower().endswith('.pptx'):
                full_path = os.path.join(root, f)
                stat = os.stat(full_path)
                pptx_files.append({
                    'path': full_path,
                    'name': f,
                    'size': stat.st_size,
                    'size_mb': round(stat.st_size / (1024*1024), 2),
                    'mtime': stat.st_mtime,
                    'mtime_str': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M')
                })

    print(f"Total PPTX found: {len(pptx_files)}")

    grouped = {}
    for p in pptx_files:
        ck = get_canonical_key(p['name'])
        grouped.setdefault(ck, []).append(p)

    out_dir = 'presentations'
    os.makedirs(out_dir, exist_ok=True)

    manifest = []
    total_copied_bytes = 0

    print("\n=== Selecting latest version and copying to presentations/ ===")
    for ck, info in sorted(CANONICAL_TOPICS.items()):
        files = grouped.get(ck)
        if not files:
            print(f"WARNING: No files found for canonical key {ck}")
            continue

        # Sort by mtime (newest first), then by size
        latest = sorted(files, key=lambda x: (x['mtime'], x['size']), reverse=True)[0]
        clean_name = info['clean_name']
        dest_path = os.path.join(out_dir, clean_name)

        print(f"[{clean_name}] <- {latest['path']} ({latest['size_mb']} MB, {latest['mtime_str']})")
        shutil.copy2(latest['path'], dest_path)
        total_copied_bytes += latest['size']

        # Calculate sha256
        with open(dest_path, 'rb') as f:
            h = hashlib.sha256(f.read()).hexdigest()

        manifest.append({
            'canonical_key': ck,
            'clean_name': clean_name,
            'title': info['title'],
            'original_filename': latest['name'],
            'original_source': latest['path'],
            'size_mb': latest['size_mb'],
            'size_bytes': latest['size'],
            'mtime': latest['mtime'],
            'mtime_str': latest['mtime_str'],
            'sha256': h,
            'target_articles': info['targets']
        })

    # Save manifest.json
    manifest_path = os.path.join(out_dir, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"\nManifest written to: {manifest_path}")

    # Generate README.md in presentations/
    readme_path = os.path.join(out_dir, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# Pangkalan Data Berkas Presentasi PPTX Resmi PKN\n\n")
        f.write("Folder ini berisi **39 berkas presentasi PPTX kanonikal terbaru** materi Pendidikan Karakter Nabawiyah (PKN) karya Ustadz Abdul Kholiq dan Tim Standarisasi PKN.\n\n")
        f.write(f"- **Total Berkas:** {len(manifest)} berkas\n")
        f.write(f"- **Total Ukuran:** {total_copied_bytes / (1024*1024):.2f} MB (~{total_copied_bytes / (1024*1024*1024):.2f} GB)\n")
        f.write(f"- **Tanggal Kompilasi:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## Tabel Katalog & Pemetaan Artikel Wiki PKN\n\n")
        f.write("| No | Nama Berkas Publik | Judul Materi | Ukuran | Sumber Asal | Halaman Terkait |\n")
        f.write("| :- | :--- | :--- | :--- | :--- | :--- |\n")
        for i, m in enumerate(manifest, 1):
            targets_str = "<br>".join([f"`{os.path.basename(t)}`" for t in m['target_articles']])
            f.write(f"| {i} | `{m['clean_name']}` | **{m['title']}** | {m['size_mb']} MB | `{m['original_source']}` | {targets_str} |\n")

    print(f"README written to: {readme_path}")
    print(f"\nSUCCESS: Prepared {len(manifest)} presentations ({total_copied_bytes / (1024*1024):.2f} MB) in {out_dir}/")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
pipeline_runner_dalil.py
Prototipe Pipeline 07 (Halaman Dalil Mandiri):
Membangun halaman mandiri dalil syar'i Al-Qur'an dan Hadits Nabawi bersanad lengkap
dengan teks Arab berharakat, terjemahan, takhrij, syarah ulama salaf, dan relasi pedagogis PKN
sesuai standar 4 Lapisan Progressive Disclosure Quartz v5.
"""

import os
import re

OUTPUT_DIR = "content/Dalil"

CORE_DALIL = [
    {
        "slug": "dalil-fitrah-kesucian-anak",
        "title": "Hadits Fitrah Setiap Anak Terlahir Di Atas Kesucian",
        "reference": "HR. Bukhari No. 1385 & Muslim No. 2658",
        "perawi": "Abu Hurairah radhiyallahu 'anhu",
        "arabic": "مَا مِنْ مَوْلُودٍ إِلَّا يُولَدُ عَلَى الْفِطْرَةِ، فَأَبَوَاهُ يُهَوِّدَانِهِ أَوْ يُنَصِّرَانِهِ أَوْ يُمَجِّسَانِهِ",
        "translation": "Tidak ada seorang anak pun yang terlahir melainkan ia dilahirkan di atas fitrah (kesucian). Maka kedua orang tuanyalah yang menjadikannya Yahudi, Nasrani, atau Majusi.",
        "syarah": "Imam An-Nawawi rahimahullah dalam Syarah Shahih Muslim menjelaskan bahwa makna fitrah adalah ketetapan asal penciptaan manusia yang condong kepada tauhid dan siap menerima kebenaran. Orang tua memegang peranan pengubah dan pembentuk lingkungan (*external nurturing*). Ibnu Qayyim menambahkan bahwa anak itu ibarat tanah subur; apa yang disemaikan orang tua itulah yang akan tumbuh.",
        "pilar_pkn": "Pondasi Fitrah Karakter & Tanggung Jawab Orang Tua",
        "etape_usia": "0–7 Tahun (Thufulah) & Fase Pembentukan Awal",
        "relevansi_kbm": "Pendidik tidak boleh memperlakukan anak sebagai 'kertas kosong' atau 'batu bata keras' yang harus dipaksa. Anak lahir membawa benih kebaikan. Tugas sekolah dan rumah adalah menjaga benteng fitrah agar tidak terkontaminasi oleh polusi pergaulan dan penyimpangan pengasuhan."
    },
    {
        "slug": "dalil-perintah-shalat-usia-7-dan-10",
        "title": "Hadits Perintah Shalat Bertahap Usia 7 dan 10 Tahun",
        "reference": "HR. Abu Dawud No. 495 & Ahmad No. 6689 (Hasan Shahih)",
        "perawi": "Amr bin Syu'aib dari ayahnya dari kakeknya",
        "arabic": "مُرُوا أَوْلَادَكُمْ بِالصَّلَاةِ وَهُمْ أَبْنَاءُ سَبْعِ سِنِينَ، وَاضْرِبُوهُمْ عَلَيْهَا وَهُمْ أَبْنَاءُ عَشْرِ سِنِينَ، وَفَرِّقُوا بَيْنَهُمْ فِي الْمَضَاجِعِ",
        "translation": "Perintahkan anak-anak kalian untuk menunaikan shalat ketika mereka berusia tujuh tahun, dan pukullah mereka (dengan pukulan mendidik tanpa melukai) jika meninggalkannya ketika berusia sepuluh tahun, serta pisahkan tempat tidur di antara mereka.",
        "syarah": "Para ulama tarbiyah menjelaskan rahasia pedagogis hadits ini: ada rentang 3 tahun penuh (sekitar 1.095 hari atau lebih dari 5.000 kali shalat) proses pembiasaan dengan kelembutan Bahasa Hati dan Bahasa Lisan sebelum adanya sanksi tegas Bahasa Tangan di usia 10 tahun. Pemisahan tempat tidur di usia 10 tahun juga merupakan tonggak edukasi seksualitas dan batasan aurat menjelang baligh.",
        "pilar_pkn": "Manhaj Tadarruj (Bertahap) & Disiplin Nabawiyah",
        "etape_usia": "7–10 Tahun (Tamyiz) transisi menuju 10–14 Tahun (Murahaqah)",
        "relevansi_kbm": "Larangan keras melakukan hukuman fisik atau bentakan sebelum anak genap berusia 10 tahun dan sebelum melewati proses pembiasaan 3 tahun penuh. Sekolah wajib menyelaraskan mutaba'ah shalat dengan pendekatan kelembutan di kelas rendah."
    },
    {
        "slug": "dalil-kasih-sayang-mencium-anak",
        "title": "Hadits Kasih Sayang Fisik dan Mencium Anak",
        "reference": "HR. Bukhari No. 5997 & Muslim No. 2318",
        "perawi": "Aisyah dan Abu Hurairah radhiyallahu 'anhuma",
        "arabic": "مَنْ لَا يَرْحَمْ لَا يُرْحَمْ",
        "translation": "Barangsiapa yang tidak menyayangi, maka dia tidak akan disayangi.",
        "syarah": "Konteks hadits ini terjadi ketika seorang Arab badui (Al-Aqra' bin Habis) heran melihat Rasulullah ﷺ mencium cucunya Hasan bin Ali. Beliau menegaskan bahwa mencium, memeluk, dan interaksi fisik hangat dengan anak adalah bukti rahmat yang Allah semaikan di dalam dada. Menahan kasih sayang fisik adalah tanda hati yang kering dan keras.",
        "pilar_pkn": "Pengisian Tangki Cinta & Bahasa Tubuh Nabawiyah",
        "etape_usia": "Seluruh Etape, terutama 0–7 Tahun (Thufulah)",
        "relevansi_kbm": "Guru dan orang tua wajib memulai hari dengan senyuman, tatapan penuh kasih, dan sentuhan lembut (menepuk pundak, mengusap kepala) sebelum menyampaikan instruksi akademik. 'Koneksi Sebelum Koreksi' bersandar langsung pada sunnah amaliyah ini."
    },
    {
        "slug": "dalil-penerimaan-sebelum-pertumbuhan-maryam",
        "title": "Ayat Penerimaan Mendahului Pertumbuhan (Kisah Maryam)",
        "reference": "QS. Ali 'Imran: 37",
        "perawi": "Kalamullah Ta'ala",
        "arabic": "فَتَقَبَّلَهَا رَبُّهَا بِقَبُولٍ حَسَنٍ وَأَنْبَتَهَا نَبَاتًا حَسَنًا",
        "translation": "Maka Tuhannya menerimanya dengan penerimaan yang baik dan menumbuhkannya dengan pertumbuhan yang baik.",
        "syarah": "Tafsir Ath-Thabari dan Ibnu Katsir menjelaskan bahwa ibunda Maryam bernazar menyerahkan anaknya untuk berkhidmat di Baitul Maqdis. Allah menerima penyerahan itu dengan keridhaan sempurna (Qabul Hasan), lalu menumbuhkan Maryam dengan penjagaan, kesucian, dan kemuliaan adab di bawah asuhan Nabi Zakariya. Kata 'Rabbuha' menunjukkan sifat rububiyah yang merawat sedikit demi sedikit.",
        "pilar_pkn": "Penerimaan Fitrah Mendahului Tuntutan Pertumbuhan",
        "etape_usia": "Sejak Dalam Kandungan hingga Dewasa",
        "relevansi_kbm": "Orang tua dan guru dilarang menuntut hasil instan sebelum selesai menerima keunikan potensi dan keterbatasan anak. Penerimaan tanpa syarat adalah tanah subur tempat tumbuhnya fitrah kebaikan."
    }
]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Generating {len(CORE_DALIL)} prototype Dalil pages in '{OUTPUT_DIR}'...")

    for item in CORE_DALIL:
        slug = item["slug"]
        title = item["title"]
        ref = item["reference"]
        arabic = item["arabic"]
        translation = item["translation"]
        syarah = item["syarah"]
        pilar = item["pilar_pkn"]
        etape = item["etape_usia"]
        kbm = item["relevansi_kbm"]

        md_content = f"""---
title: "{title}"
tags:
  - DalilSyar'i
  - HaditsNabawi
  - Takhrij
  - SyarahSalaf
  - PendidikanKarakterNabawiyah
sources:
  - reference: "{ref}"
    authority: 1.0
    verification: "Shamela 11M / Kutubut Tis'ah Verified"
---

> [!abstract] Hook & Ringkasan Dalil (Layer 1)
> **Nas / Rujukan:** {ref}
> **Fokus Karakter:** {pilar}
> **Etape Usia Target:** {etape}

---

## Teks Takhrij Matan Dalil (Layer 2)

<div style="font-family: 'Amiri', 'Scheherazade New', serif; font-size: 1.65rem; line-height: 2.8rem; text-align: right; direction: rtl; padding: 1.25rem; background: var(--highlight); border-radius: 8px; border-right: 4px solid var(--secondary);">
{arabic}
</div>

> **Terjemahan:**
> *"{translation}"*
>
> *(Perawi / Sumber: {ref})*

---

## Analisis Pedagogis & Syarah Ulama (Layer 3)

### 1. Syarah & Atsar Ulama Mu'tabar
{syarah}

### 2. Integrasi Manhaj Pendidikan Karakter Nabawiyah
Dalam kerangka PKN, dalil ini menjadi rujukan baku untuk pilar **{pilar}**. Hal ini menegaskan bahwa:
- Tumbuh kembang karakter anak terikat dengan sunnatullah bertahap (*tadarruj*).
- Pendekatan pengasuhan tidak boleh mendahului atau menyalahi tahapan usia nabawiyah.

### 3. Panduan Operasional & KBM di Sekolah / Rumah
{kbm}

---

## Matriks Panduan Amaliah & Evaluasi (Layer 4)

| Fase Usia | Pendekatan Bahasa | Respon Nabawiyah yang Dianjurkan | Tindakan yang Dilarang (Patologi) |
|:---|:---|:---|:---|
| **0–7 Tahun** | Bahasa Hati | Mengisi tangki cinta, pelukan fisik, teladan amalan. | Menuntut shalat dengan bentakan atau sanksi fisik. |
| **7–10 Tahun** | Bahasa Lisan | Memerintahkan shalat dengan lembut, mengajarkan adab & wudhu. | Membiarkan tanpa pengawasan (meremehkan/Tafrith). |
| **10–14 Tahun** | Bahasa Tangan | Disiplin tegas terukur, pisahkan ranjang tidur, dialog pra-baligh. | Sanksi fisik melukai wajah / emosi amarah tak terkontrol. |

---

## Penautan Navigasi & Konsep
- Kembali ke: [[Indeks Utama]] | [[Kajian Video]] | [[Materi SOTAB]]
- Konsep Terkait: [[4 Etape Usia Nabawiyah]] | [[Koneksi Sebelum Koreksi]] | [[40 Pilar Karakter TB40]]
"""
        filepath = os.path.join(OUTPUT_DIR, f"{slug}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"  ✓ Created: {filepath}")

    print("Prototype Dalil runner completed successfully!")

if __name__ == "__main__":
    main()

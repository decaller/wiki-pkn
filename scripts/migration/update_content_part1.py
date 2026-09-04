"""
Script to enrich content/ markdown files with authentic PKN documentation
extracted and synthesized from old_backup/random/.
"""

import os
import re

CONTENT_BASE = "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi"

def write_file(rel_path, title, content):
    full_path = os.path.join(CONTENT_BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    # Ensure clean YAML frontmatter
    doc = f"""---
title: "{title}"
---

{content.strip()}
"""
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Updated: {full_path}")

# ==============================================================================
# 1. INSAN & PEMBAGIAN JIWA
# ==============================================================================

INSAN_CONTENT = """# Paradigma Insan

Paradigma Insan dalam Pendidikan Karakter Nabawiyah (PKN) meletakkan pemahaman utuh mengenai hakikat penciptaan manusia sebagai makhluk dwidimensi: perpaduan antara jasad biologis dari tanah dan ruh suci ciptaan Ilahi. Persatuan keduanya melahirkan entitas yang disebut jiwa (*nafs*).

Pendidikan karakter bukanlah proses pengisian wadah kosong atau penempaan mekanis dari luar, melainkan ikhtiar pemuliaan fitrah dan penyucian jiwa (*tazkiyatun nafs*) agar manusia mampu menunaikan dua mandat agungnya di muka bumi: sebagai hamba Allah (*'Abdullah*) yang taat beribadah dan sebagai pengelola bumi (*Khalifah fil Ardh*) yang menebar maslahat.

## Arsitektur Manusia dalam PKN

1. **Jasad (Dimensi Fisik):** Unsur biologis yang condong pada kebutuhan hewani (*hayawaniyah*), kenikmatan sesaat, dan membutuhkan pembiasaan gerak serta kedisiplinan fisik.
2. **Ruh (Dimensi Ilahi):** Tiupan langsung dari Allah yang merindukan transendensi, kebenaran mutlak, ketundukan tauhid, dan menjadi sumber nurani.
3. **Nafs (Dimensi Jiwa):** Medan perjumpaan antara dorongan jasad dan bisikan ruh yang melahirkan tiga kondisi jiwa: *Nafsul Muthmainnah* (condong ke ruh), *Nafsul Lawwamah* (pertengahan/akal), dan *Nafsul Ammarah* (condong ke jasad).

## Topik Pembahasan Utama

* [[Tujuan Hidup Manusia]] — Mandat agung 'Abdullah dan Khalifah fil Ardh.
* [[Bersatunya Ruh dan Jasad Membentuk Jiwa]] — Dinamika perjumpaan materi dan immateri.
* [[Pembagian Jiwa]] — Tiga tingkatan nafs: Ammarah, Lawwamah, dan Muthmainnah.
* [[Fitrah (Karakter)]] — Potensi bawaan lahir (Iman, Belajar, Bakat, dan Perkembangan).
"""

RUH_JASAD_CONTENT = """# Bersatunya Ruh dan Jasad Membentuk Jiwa

Manusia bukanlah jasad semata, bukan pula malaikat yang murni tersusun dari cahaya ruh. Allah menciptakan manusia melalui tahapan pembentukan jasad materi dari tanah, kemudian meniupkan ruh ciptaan-Nya ke dalam jasad tersebut. Dari perjumpaan sakral inilah lahir entitas yang disebut **Jiwa (*Nafs*)**.

> *"Dan (ingatlah) ketika Tuhanmu berfirman kepada para malaikat: Sesungguhnya Aku akan menciptakan seorang manusia dari tanah liat kering yang berasal dari lumpur hitam yang diberi bentuk. Maka apabila Aku telah menyempurnakan kejadiannya, dan telah meniupkan ke dalamnya ruh (ciptaan)-Ku, maka tunduklah kamu kepadanya dengan bersujud."* (QS. Al-Hijr: 28-29)

## Dinamika Dua Kutub Manusia

* **Kutub Jasad (Bumi):** Menarik manusia ke bawah menuju kenyamanan materi, makan, istirahat, pelestarian jenis (syahwat), dan kepuasan indrawi. Jika jasad mendominasi tanpa kendali ruh, manusia terdegradasi ke derajat terendah (*asfala safilin*).
* **Kutub Ruh (Langit):** Menarik manusia ke atas menuju kemuliaan akhlak, ketenangan zikir, kerinduan pada Allah, dan pengorbanan demi kebaikan sesama.
* **Peran Nafs (Jiwa):** Jiwa adalah arena pertarungan antara kedua kutub ini. Pendidikan Karakter Nabawiyah (PKN) berfungsi menuntun jiwa agar condong kepada ruh, mengarahkan dorongan fisik menjadi amal sholeh, bukan mematikan jasad melainkan mendisiplinkannya di bawah pimpinan iman.
"""

PEMBAGIAN_JIWA_CONTENT = """# Pembagian Jiwa

Dalam Pendidikan Karakter Nabawiyah (PKN), manusia dipetakan secara utuh melalui tiga dimensi jiwa (*trilogi nafs*) yang saling berkaitan: **Nafsul Muthmainnah (Hati/Perasaan)**, **Nafsul Lawwamah (Akal/Pikiran)**, dan **Nafsul Ammarah (Fisik/Kemauan)**.

Setiap dimensi jiwa ini memiliki hak perkembangan unik yang wajib ditunaikan oleh orang tua dan pendidik agar anak tumbuh seimbang dan siap memikul tanggung jawab syariat (*mukallaf*) secara sadar setelah melewati pintu gerbang baligh.

## Tiga Dimensi Jiwa dalam PKN

| Dimensi Jiwa | Organ / Lokasi | Sifat Kecondongan | Dimensi Karakter | Metode Pendidikan |
|---|---|---|---|---|
| **Nafsul Muthmainnah** | Batin / Qalbu | Ruh / Ketaatan Ilahi | Karakter Iman | Bahasa Hati (Edukasi Rasa) |
| **Nafsul Lawwamah** | Otak / Nalar | Seimbang (Evaluatif) | Karakter Belajar | Bahasa Lisan (Edukasi Logika) |
| **Nafsul Ammarah** | Jasad / Fisik | Materi / Hayawaniyah | Karakter Bakat & Gerak | Bahasa Tangan (Edukasi Aksi) |

## Prinsip Penunaian Hak Jiwa

Penunaian hak pada ketiga dimensi jiwa ini secara bertahap merupakan prasyarat mutlak agar anak tumbuh matang secara mental (*Akil*) bersamaan dengan kedatangan tanda kedewasaan fisiknya (*Baligh*). Memaksa anak memikul beban tanpa memenuhi hak jiwanya di usia dini hanya akan melahirkan kepatuhan semu dan luka pengasuhan.

* [[Ammarah]] — Dimensi fisik, kemauan gerak, dorongan eksekusi, dan bakat jasad.
* [[Lawwamah]] — Dimensi nalar, akal evaluatif, rasa ingin tahu, dan adab ilmu.
* [[Muthmainnah]] — Dimensi hati, kecintaan tauhid, kelapangan dada, dan keikhlasan batin.
"""

AMMARAH_CONTENT = """# Jiwa Ammarah

Jiwa Ammarah adalah unsur jiwa yang memiliki kecondongan kuat terhadap kebutuhan dan dorongan jasad. Jiwa ini menjadi sumber energi vital, keberanian, kemauan (*al-hawa*), dan dorongan untuk segera bergerak serta mengeksekusi tindakan nyata di dunia fisik.

## Sifat Dasar

| Aspek | Nilai Karakteristik | Penjelasan |
|---|---|---|
| **Sifat Umum** | **Condong ke hayawaniyah** | Mengutamakan kebutuhan fisik, indrawi, dan kenyamanan raga |
| **Ego** | **Tinggi** | Memiliki dorongan kuat untuk segera dipenuhi dan diakui |
| **Organ Dominan** | **Jasad** | Berkaitan erat dengan kekuatan fisik, metabolisme, dan motorik |
| **Tipe Kesadaran** | **Bawah Sadar (Refleks)** | Bertindak spontan berbasis kebiasaan dan naluri raga |
| **Pilar Karakter** | **Bakat & Gerak** | Landasan pengembangan daya juang (*grit*) dan eksekusi bakat |

## Pendekatan Pendidikan

| Indikator | Ketentuan | Keterangan |
|---|---|---|
| **Gaya Belajar** | **Bergerak (Kinestetik)** | Menyukai aktivitas luar ruangan, proyek langsung, dan keterlibatan fisik |
| **Golden Age** | **Fase Murahaqah (10 th - Baligh)** | Masa emas melatih kemandirian dan kedisiplinan menjelang baligh |
| **Metode Utama** | **Bahasa Tangan (Ketegasan)** | Pendisiplinan berbasis aturan yang jelas dan konsekuensi nyata |
| **Orientasi Implementasi** | **Amal & Karya** | Menilai proses dan hasil karya nyata yang memberi manfaat |

## Tipologi Bakat Terkait

* **Introvert (Bekerja Keras):** Ketahanan fisik dan mental untuk fokus menuntaskan pekerjaan berat secara tekun (*grit*).
* **Ekstrovert (Memerintah):** Energi kepemimpinan alami yang menggerakkan dan mengorganisasi orang lain menuju suatu tujuan.

## Kondisi Ekstrim & Penyeimbang

* **Mufrith (Kekurangan Energi):** Menghasilkan kemalasan, pasif, dan ketidakmampuan membela diri.
* **Ifroth (Kelebihan Energi):** Menghasilkan agresivitas, arogansi, memaksakan kehendak, dan tunduk mutlak pada hawa nafsu.
* **Solusi Nabawiyah:** Bukan mematikan hasrat jiwa ammarah, melainkan menyalurkannya ke dalam amalan fisik yang bermanfaat, olahraga sunnah, pemagangan karya nyata, dan pendisiplinan ibadah shalat secara konsisten.
"""

LAWWAMAH_CONTENT = """# Jiwa Lawwamah

Jiwa Lawwamah adalah pusat nalar, daya kritis, dan pertimbangan logis (*cognitive quotient*) yang bertempat di otak. Jiwa ini bertindak sebagai hakim internal yang senantiasa mencela dan mengevaluasi diri saat berbuat salah serta memikirkan konsekuensi atas setiap pilihan.

## Sifat Dasar

| Aspek | Nilai Karakteristik | Penjelasan |
|---|---|---|
| **Sifat Umum** | **Seimbang (Akal Evaluatif)** | Menimbang antara dorongan jasad dan tuntunan ruh secara rasional |
| **Ego** | **Sedang** | Terbuka pada dialog, penjelasan logis, dan pembuktian empiris |
| **Organ Dominan** | **Otak / Akal** | Mengolah informasi, hubungan sebab-akibat, dan kausalitas |
| **Tipe Kesadaran** | **Sadar Penuh** | Memerlukan perenungan, pemahaman konsep, dan daya analisis |
| **Pilar Karakter** | **Karakter Belajar** | Landasan penumbuhan kecerdasan, rasa ingin tahu, dan adab menuntut ilmu |

## Pendekatan Pendidikan

| Indikator | Ketentuan | Keterangan |
|---|---|---|
| **Gaya Belajar** | **Eksploratif & Dialogis** | Belajar melalui uji coba (*trial and error*), diskusi, dan pertanyaan |
| **Golden Age** | **Fase Tamyiz (7 - 10 Tahun)** | Masa keemasan penumbuhan nalar kritis dan pemahaman sebab-akibat |
| **Metode Utama** | **Bahasa Lisan (Argumentasi Lembut)** | Komunikasi logis dua arah tanpa amarah atau ancaman fisik |
| **Orientasi Implementasi** | **Ilmu Fungsional** | Memahami ilmu dasar (*Fardhu 'Ain*) yang langsung relevan dengan ibadah dan kehidupan |

## Tipologi Bakat Terkait

* **Introvert (Berpikir):** Ketajaman menganalisis, merancang strategi, membaca pola, dan merumuskan gagasan mendalam.
* **Ekstrovert (Bekerja Sama):** Kemampuan berkomunikasi, berdiplomasi, membangun kemitraan, dan menyatukan sudut pandang.

## Kondisi Ekstrim & Penyeimbang

* **Mufrith (Kekurangan Nalar):** Melahirkan kebodohan, mudah tertipu, taklid buta, dan kerancuan berpikir.
* **Ifroth (Kelebihan Nalar):** Menghasilkan pemujaan logika (*Ahlur Ra'yi*), meragukan kebenaran wahyu, suka mendebat tanpa adab, dan skeptisisme yang melumpuhkan aksi.
* **Solusi Nabawiyah:** Menundukkan akal di bawah wahyu, membimbing rasa ingin tahu dengan adab menuntut ilmu, dan mengimbangi logika dengan ketundukan iman (*Muthmainnah*).
"""

MUTHMAINNAH_CONTENT = """# Jiwa Muthmainnah

Jiwa Muthmainnah adalah puncak kedamaian spiritual, pusat rasa batin (*affective quotient*), dan sumber ketenangan tauhid yang bersemayam di dalam kalbu (*qalb*). Jiwa inilah yang diseru oleh Allah dengan penuh keridhaan di akhir hayat.

> *"Wahai jiwa yang tenang! Kembalilah kepada Tuhanmu dengan hati yang ridha lagi diridhai-Nya. Maka masuklah ke dalam golongan hamba-hamba-Ku, dan masuklah ke dalam surga-Ku."* (QS. Al-Fajr: 27-30)

## Sifat Dasar

| Aspek | Nilai Karakteristik | Penjelasan |
|---|---|---|
| **Sifat Umum** | **Condong ke Ilahiyyah** | Merindukan kedekatan dengan Allah, ketenangan zikir, dan kesucian batin |
| **Ego** | **Rendah / Tunduk** | Lapang dada, ikhlas menerima ketetapan syariat, dan pemaaf |
| **Organ Dominan** | **Qalbu / Hati Nurani** | Merasakan getaran keimanan, empati sosial, dan cinta murni |
| **Tipe Kesadaran** | **Super Sadar (Muraqabah)** | Merasa senantiasa diawasi oleh Allah dalam kesunyian maupun keramaian |
| **Pilar Karakter** | **Karakter Iman** | Fondasi seluruh integritas moral, kejujuran (*shidq*), dan ketulusan |

## Pendekatan Pendidikan

| Indikator | Ketentuan | Keterangan |
|---|---|---|
| **Gaya Belajar** | **Meniru & Merasakan** | Menyerap getaran keshalihan, keteladanan visual, dan suasana penuh kasih |
| **Golden Age** | **Fase Thufulah (0 - 7 Tahun)** | Masa emas penanaman persepsi positif tentang Allah, Rasul, dan kebaikan |
| **Metode Utama** | **Bahasa Hati (Edukasi Rasa)** | Pemenuhan 5 Bahasa Cinta, doa tulus pendidik, dan keteladanan tanpa paksaan |
| **Orientasi Implementasi** | **Koneksi Sebelum Koreksi** | Memastikan tangki cinta terisi penuh sebelum menuntut kepatuhan syariat |

## Tipologi Bakat Terkait

* **Introvert (Berperasaan):** Sensitivitas empati batin yang mendalam, kelembutan rasa, dan kepekaan nurani terhadap sesama.
* **Ekstrovert (Melayani):** Kedermawanan aktif, kerelaan menolong, mengutamakan orang lain (*itsar*), dan keramahan tulus.

## Penjagaan Kemurnian Qalbu

Jiwa Muthmainnah dijaga melalui pemenuhan "Tangki Cinta" di masa kecil dan proses *Tazkiyatun Nafs* yang konsisten. Hati yang telah mencicipi manisnya iman (*Halawatul Iman*) akan memandu akal dan jasad untuk taat secara sukarela, bukan karena keterpaksaan atau ancaman hukuman.
"""

print("Writing Insan & Jiwa files...")
write_file("Insan.md", "Insan", INSAN_CONTENT)
write_file("Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md", "Bersatunya Ruh dan Jasad Membentuk Jiwa", RUH_JASAD_CONTENT)
write_file("Insan/Pembagian Jiwa.md", "Pembagian Jiwa", PEMBAGIAN_JIWA_CONTENT)
write_file("Insan/Pembagian Jiwa/Ammarah.md", "Ammarah", AMMARAH_CONTENT)
write_file("Insan/Pembagian Jiwa/Lawwamah.md", "Lawwamah", LAWWAMAH_CONTENT)
write_file("Insan/Pembagian Jiwa/Muthmainnah.md", "Muthmainnah", MUTHMAINNAH_CONTENT)

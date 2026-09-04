#!/usr/bin/env python3
"""
Sprint 3 Content Generator: Landing Pages, Navigation Nodes, and Templates for Wiki PKN
Elevates all 14 Sprint 3 files into rich, comprehensive, authoritative markdown documents
with Mermaid diagrams, authentic dalil, cross-links, and pedagogical rubrics.
"""

import os
from pathlib import Path

CONTENT_DIR = Path("/home/abuhafi/Project/wiki-pkn/content")

FILES_CONTENT = {
    # 1. index.md (Beranda Utama)
    CONTENT_DIR / "index.md": """---
title: Beranda Utama
---

# Wiki Pendidikan Karakter Nabawiyah (PKN)

Selamat datang di basis pengetahuan digital **Pendidikan Karakter Nabawiyah (PKN)**—sebuah ensiklopedia rujukan komprehensif yang merekonstruksi paradigma, kurikulum, metodologi, dan implementasi pengasuhan generasi Islam berdasarkan sunnah Rasulullah ﷺ, atsar para sahabat, serta pandangan para ulama mu'tabar (*Ibnul Qayyim, Al-Ghazali, Ibnu Sahnun, An-Nawawi, Ibnu Khaldun, Asy-Syathibi*).

> [!quote] Dalil & Rujukan Nabawiyah: Fondasi Pohon Karakter
> **Teks Al-Qur'an:**  
> « أَلَمْ تَرَ كَيْفَ ضَرَبَ اللَّهُ مَثَلًا كَلِمَةً طَيِّبَةً كَشَجَرَةٍ طَيِّبَةٍ أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِي السَّمَاءِ ۝ تُؤْتِي أُكُلَهَا كُلَّ حِينٍ بِإِذْنِ رَبِّهَا »
> 
> *"Tidakkah kamu perhatikan bagaimana Allah telah membuat perumpamaan kalimat yang baik seperti pohon yang baik, akarnya teguh dan cabangnya (menjulang) ke langit, pohon itu menghasilkan buahnya pada setiap waktu dengan seizin Tuhannya..."*  
> — **QS. Ibrahim: 24–25**
> 
> 💡 **Relevansi PKN:** Fondasi metafora arsitektur peradaban: Tauhid dan iman adalah akar yang menghujam ke relung kalbu, adab belajar adalah batang yang kokoh, 40 pilar bakat unik anak adalah cabang yang menjulang, dan buahnya adalah amal peradaban yang bermanfaat bagi semesta.

---

## 1. Peta Konsep Arsitektur Pendidikan Karakter Nabawiyah

Pendidikan Karakter Nabawiyah memandang manusia sebagai kesatuan utuh (*insan kamil*) yang bertumbuh secara organik melalui integrasi tiga pilar agung:

```mermaid
graph TD
    subgraph AKAR["🌱 PONDASI INSAN (AKAR TAUHID)"]
        Tujuan["[[Tujuan Hidup Manusia]]<br/>Ibadah & Khilafah"]
        RuhJasad["[[Bersatunya Ruh dan Jasad Membentuk Jiwa]]<br/>Tiupan Ruh & Tanah"]
        Trilogi["[[Pembagian Jiwa]]<br/>Muthmainnah • Lawwamah • Ammarah"]
        Fitrah["[[Fitrah (Karakter)]]<br/>Cetak Biru Suci Lahiriah"]
    end

    subgraph BATANG["🌳 PENDIDIKAN IDEAL (BATANG ADAB & METODOLOGI)"]
        Benang["[[Benang Merah Pendidikan]]<br/>Wasathiyah: Anti-Tafrith & Ifrath"]
        TigaBahasa["[[Metode Mendidik]]<br/>[[Bahasa Hati]] • [[Bahasa Lisan]] • [[Bahasa Tangan]]"]
        Fase["[[Perkembangan]]<br/>[[Thufulah]] (0-7) • [[Tamyiz]] (7-10) • [[Murahaqah]] (10-15) • [[Syabab]] (15+)"]
        Proteksi["[[Batas Toleransi]] • [[Imunitas Sosial]] • [[Recovery]]"]
    end

    subgraph RANTING["🍃 FITRAH BAKAT (40 PILAR TB40)"]
        BakatUmum["[[Bakat]] (Syakilah Unik)"]
        Sub1["[[Bekerja Keras]] (Al-Hammasah)"]
        Sub2["[[Berpikir]] (Al-Fikrah)"]
        Sub3["[[Berperasaan]] (Al-Wijdaniyyah)"]
        Sub4["[[Memerintah]] (At-Ta'tsir)"]
        Sub5["[[Bekerja Sama]] (At-Ta'amul)"]
        Sub6["[[Melayani]] (Al-Khidmah)"]
    end

    subgraph BUAH["🍎 IMPLEMENTASI & KARYA PERADABAN"]
        Kaidah["[[4 Kaidah Implementasi]]<br/>Taisir • Qudwah • Rahmah • Tadarruj"]
        Elemen["[[4 Elemen Implementasi]]<br/>Ghayah • Manhaj • Uslub • Taqyim"]
        Sinergi["[[Tanggung Jawab Pendidikan]]<br/>[[Peran Ayah dan Bunda]] • [[Peran Guru dan Lembaga Pendidikan]]"]
        Output["Kematangan Akil-Baligh & Khairu Ummah"]
    end

    AKAR --> BATANG
    BATANG --> RANTING
    RANTING --> BUAH
```

---

## 2. Tiga Jalur Belajar Berdasarkan Peran Pengguna

Untuk memudahkan penelusuran dokumen wiki yang berjumlah 61 halaman, silakan pilih jalur membaca yang paling relevan dengan amanah Anda:

### 🧭 Jalur 1: Untuk Ayah (Nakhoda Visi & Ketegasan Syariat)
Sebagai nakhoda keluarga yang memegang amanah *qawwamah* (QS. An-Nisa: 34), Ayah bertugas menetapkan arah peradaban rumah tangga dan menegakkan batas-batas syariat:
1. Pahami tujuan tertinggi penciptaan dalam [[Tujuan Hidup Manusia]] dan [[Tanggung Jawab Pendidikan]].
2. Tegakkan batas perlindungan keluarga dari pengaruh destruktif melalui [[Batas Toleransi]] dan [[Imunitas Sosial]].
3. Pelajari kaidah ketegasan mendidik tanpa kekerasan dalam [[Bahasa Tangan]] dan pendisiplinan fase [[Murahaqah]].
4. Sinergikan pembagian peran pengasuhan dengan istri melalui [[Peran Ayah dan Bunda]].

### 🌸 Jalur 2: Untuk Bunda (Madrasah Cinta & Pengisian Tangki Jiwa)
Sebagai *rahimah* dan madrasah pertama anak, Bunda bertugas menghidupkan suasana kasih sayang dan mengawal kelekatan fitrah:
1. Mulai dari pemenuhan hak batin anak usia dini dalam [[Tangki Cinta]] dan fase [[Thufulah]] (0–7 tahun).
2. Kuasai seni komunikasi kelembutan batiniah dalam [[Bahasa Hati]] dan dialog empatik [[Bahasa Lisan]].
3. Kenali dinamika batiniah anak agar tidak cemas berlebihan melalui [[Pembagian Jiwa]], [[Muthmainnah]], dan [[Lawwamah]].
4. Temukan ketenangan batin dalam mendampingi anak melalui [[Tazkiyatun Nafs]] serta [[Tawakkal dan Doa]].

### 🎓 Jalur 3: Untuk Guru & Pengelola Lembaga Pendidikan
Sebagai mitra pengembang amanah orang tua (*Waratsatul Anbiya'*), pendidik formal dan non-formal bertugas memfasilitasi fitrah unik setiap murid:
1. Pahami kedudukan institusi dan adab guru dalam [[Peran Guru dan Lembaga Pendidikan]].
2. Pelajari kaidah operasional kurikulum berbasis fitrah dalam [[4 Kaidah Implementasi]] dan [[4 Elemen Implementasi]].
3. Terapkan prinsip pembelajaran dunia nyata tanpa sekat kaku kelas melalui [[Pembelajaran Alamiah]].
4. Lakukan pemetaan dan observasi 40 bakat anak menggunakan instrumen Rukun 3A di [[Bakat]], [[Bekerja Keras]], [[Berpikir]], [[Berperasaan]], [[Memerintah]], [[Bekerja Sama]], dan [[Melayani]].

---

## 3. Peta Navigasi Cepat Topik-Topik Kunci

| Kluster Pembahasan | Halaman Kunci yang Wajib Dibaca | Fokus Utama Kajian |
| :--- | :--- | :--- |
| **Pondasi Insan** | [[Insan]], [[Tujuan Hidup Manusia]], [[Bersatunya Ruh dan Jasad Membentuk Jiwa]] | Hakikat penciptaan manusia, pertemuan tanah dan tiupan ruh, serta taksonomi trilogi jiwa. |
| **Trilogi Jiwa (Nafs)** | [[Pembagian Jiwa]], [[Ammarah]], [[Lawwamah]], [[Muthmainnah]] | Memahami pertarungan dorongan fisik (Ammarah), nalar kritis (Lawwamah), dan spiritualitas hati (Muthmainnah). |
| **Fitrah & Belajar** | [[Fitrah (Karakter)]], [[Iman]], [[Tangki Cinta]], [[Belajar]] | Menjaga kesucian fitrah lahiriah, menumbuhkan cinta sebelum hukum, dan fitrah belajar alamiah anak. |
| **Fase Usia Perkembangan** | [[Perkembangan]], [[Thufulah]], [[Tamyiz]], [[Murahaqah]], [[Syabab]] | Panduan mendidik bertahap dari usia 0–7 tahun (bermain), 7–10 tahun (adab shalat), 10–15 tahun (disiplin & karya), hingga 15+ tahun (akil-baligh mandiri). |
| **Metodologi Pengasuhan** | [[Metode Mendidik]], [[Bahasa Hati]], [[Bahasa Lisan]], [[Bahasa Tangan]] | Hirarki tiga bahasa tarbiyah: kehangatan batin, 6 kaidah komunikasi Al-Qur'an, dan ta'dib ketegasan terukur. |
| **Penyembuhan & Proteksi** | [[Luka dan Hutang Pengasuhan]], [[Recovery]], [[Euforia]], [[Batas Toleransi]], [[Imunitas Sosial]] | Memulihkan fitrah anak yang terluka, mengatasi sindrom euforia sesaat, serta benteng proteksi pergaulan. |
| **40 Pilar Bakat (TB40)** | [[Bakat]], [[Bekerja Keras]], [[Berpikir]], [[Berperasaan]], [[Memerintah]], [[Bekerja Sama]], [[Melayani]] | Pemetaan bakat nabawiyah terinspirasi figur sahabat Nabi ﷺ, rubrik observasi 3A, dan pencegahan tafrith-ifrath. |
| **Implementasi Lapangan** | [[Implementasi]], [[4 Kaidah Implementasi]], [[4 Elemen Implementasi]], [[Tanggung Jawab Pendidikan]] | Standar operasional eksekusi kurikulum keluarga, fardhu 'ain orang tua, dan sinergi segitiga emas pendidikan. |

---

## 4. Master Rujukan Dalil & Video Database

Wiki PKN terintegrasi penuh dengan dua basis data ilmiah pelengkap:
* 📖 **[Master Katalog Dalil Al-Qur'an](file:///home/abuhafi/Project/wiki-pkn/QURAN_DALIL_CATALOG.md):** Memuat lebih dari 110 ayat Al-Qur'an berharakat lengkap, terjemahan resmi, takhrij surah/ayat, serta syarah klasik dari **Tafsir Ibnu Katsir** melalui korpus **OpenBayan**.
* 📜 **[Master Katalog Dalil Hadits & Sunnah](file:///home/abuhafi/Project/wiki-pkn/DALIL_MAPPING.md):** Memuat hadits-hadits shahih dari Kutubus Sunnah (*Shahih Bukhari, Shahih Muslim, Riyadush Shalihin, dll.*) yang menjadi pijakan setiap topik.
* 🎥 **[[Referensi Kajian Video]]:** Indeks komprehensif berisi 122 judul rekaman kajian dan 1.159 bab transkrip pembahasan video Ustadz Abdul Kholiq untuk pendalaman materi audio-visual.
* ❓ **[[FAQ Ringkas]]:** Jawaban otoritatif atas pertanyaan-pertanyaan praktis yang sering dihadapi para orang tua dan pendidik.

Gunakan bilah pencarian di bagian atas atau panel navigasi di sebelah kiri untuk mulai menelusuri materi. Semoga Allah Ta'ala menjadikan wiki ini sebagai wasilah kebaikan dalam melahirkan generasi *qurrata a'yun* pembangun peradaban Islam.
""",

    # 2. Dokumen Pendidikan Karakter Nabawiyah.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah.md": """---
title: Dokumen Pendidikan Karakter Nabawiyah
---

# Dokumen Master Pendidikan Karakter Nabawiyah

Dokumen ini merupakan cetak biru (*grand design*) dan arsitektur induk sistem **Pendidikan Karakter Nabawiyah (PKN)**. Dokumen ini merangkum sintesis holistik antara dalil-dalil Al-Qur'an, as-Sunnah ash-Shahihah, khazanah tarbiyah ulama salafush shalih, serta aplikasi empiris pengasuhan berbasis fitrah di era kontemporer.

> [!quote] Dalil & Rujukan Nabawiyah: Petunjuk yang Paripurna
> **Teks Al-Qur'an:**  
> « إِنَّ هَٰذَا الْقُرْآنَ يَهْدِي لِلَّتِي هِيَ أَقْوَمُ وَيُبَشِّرُ الْمُؤْمِنِينَ الَّذِينَ يَعْمَلُونَ الصَّالِحَاتِ أَنَّ لَهُمْ أَجْرًا كَبِيرًا »
> 
> *"Sesungguhnya Al Quran ini memberikan petunjuk kepada (jalan) yang lebih lurus dan memberi kabar gembira kepada orang-orang mukmin yang mengerjakan amal saleh bahwa bagi mereka ada pahala yang besar."*  
> — **QS. Al-Isra': 9**
> 
> 📚 **Rujukan Tafsir OpenBayan:** *Tafsir Ibnu Katsir* menegaskan bahwa petunjuk Al-Qur'an adalah jalan yang paling tegak, paling adil, paling lurus (*aqwam*), dan tidak ada kebengkokan di dalamnya.  
> 💡 **Relevansi PKN:** PKN meletakkan wahyu Ilahi sebagai rujukan mutlak di atas seluruh teori psikologi manusia yang rentan berubah dan terbatas pandangannya.

---

## 1. Visi, Misi, dan Epistemologi PKN

Pendidikan Karakter Nabawiyah hadir sebagai jawaban atas kegagalan sistem pendidikan modern (adopsi model pabrik Prusia) yang mereduksi hakikat manusia menjadi sekadar angka ujian, menstandarisasi potensi unik anak secara seragam, memisahkan perkembangan fisik (*baligh*) dari kematangan nalar dan tanggung jawab (*akil*), serta menyingkirkan dimensi tauhid dari proses belajar.

### Matriks Komparasi: Paradigma Sekuler vs Paradigma Nabawiyah

| Dimensi Evaluasi | Paradigma Pendidikan Sekuler Modern | Paradigma Pendidikan Karakter Nabawiyah (PKN) |
| :--- | :--- | :--- |
| **Hakikat Anak** | Kertas putih kosong (*tabula rasa*) yang harus diisi dan dibentuk oleh lingkungan luar. | Makhluk mulia yang telah membawa cetak biru suci (*fitrah*) dan potensi ketauhidan sejak lahir. |
| **Peran Orang Tua** | Konsumen pendidikan; mendelegasikan tanggung jawab pengasuhan penuh kepada sekolah formal. | Penanggung jawab utama dan pertama di hadapan Allah (*fardhu 'ain*); sekolah hanya mitra pendukung. |
| **Metode Belajar** | Penyeragaman kurikulum massal (*one size fits all*), drill hafalan teks, dan kompetisi ranking. | Personalisasi (*satu anak satu kurikulum*), eksplorasi alamiah, dan mentoring berbasis bakat unik (TB40). |
| **Fokus Usia Dini** | Calistung dini, ujian kognitif formal, dan pengekangan ruang gerak fisik anak di kelas. | Penuntasan tangki cinta tanpa syarat, bermain aktif, keteladanan visual, dan penanaman rasa cinta iman. |
| **Target Akhir** | Ijazah formal, kesiapan menjadi tenaga kerja pasar, dan kepatuhan mekanis industri. | Mencetak pribadi Mukallaf yang Akil-Baligh, berjiwa *khairu ummah*, mandiri, dan beramal peradaban. |

---

## 2. Struktur Pembagian Dokumen Wiki PKN

Arsitektur dokumen Wiki PKN terbagi ke dalam dua divisi utama yang saling menopang secara sistemik:

### Bagian I: [[Paradigma & Implementasi]]
Bagian ini membedah pondasi konseptual filosofis dan rancang bangun metodologis yang wajib dikuasai oleh setiap pendidik:
1. **[[Insan]]:** Membahas tuntas siapa manusia yang dididik, meliputi [[Tujuan Hidup Manusia]], pertemuan [[Bersatunya Ruh dan Jasad Membentuk Jiwa]], taksonomi [[Pembagian Jiwa]] (*Muthmainnah, Lawwamah, Ammarah*), konsepsi [[Fitrah (Karakter)]], pengisian [[Tangki Cinta]], fitrah [[Belajar]], dan 40 ragam [[Bakat]].
2. **[[Pendidikan Ideal]]:** Membahas prinsip dasar tarbiyah lurus dalam [[Benang Merah Pendidikan]], metodologi pengasuhan bertahap dalam [[Metode Mendidik]] (*Bahasa Hati, Bahasa Lisan, Bahasa Tangan*), konsep [[Pembelajaran Alamiah]], benteng [[Imunitas Sosial]], penjagaan [[Batas Toleransi]], serta kurasi solusi dalam [[Bank Studi Kasus]].
3. **[[Implementasi]]:** Membahas panduan praktis eksekusi di dunia nyata melalui [[4 Kaidah Implementasi]], [[4 Elemen Implementasi]], pensucian jiwa dalam [[Tazkiyatun Nafs]], kekuatan [[Tawakkal dan Doa]], serta sinergi segitiga emas dalam [[Tanggung Jawab Pendidikan]], [[Peran Ayah dan Bunda]], dan [[Peran Guru dan Lembaga Pendidikan]].

### Bagian II: [[Insight & Teknis]]
Bagian ini memuat kompilasi catatan lapangan, studi kasus empiris, dan arahan prosedural teknis dari para asatidzah dan praktisi PKN:
1. **[[Insight]]:** Renungan mendalam mengenai dinamika jiwa anak, problematika *fatherless*, bahaya kecanduan digital, dan pemulihan luka pengasuhan.
2. **[[Arahan Teknis Implementasi]]:** Standar operasional prosedur (SOP) harian keluarga, instrumen observasi bakat, checklist adab per fase usia, dan panduan dialog ayah-anak.
3. **[[SOTABH]]:** Panduan kurikulum Sekolah Orang Tua Berbasis Hadits sebagai sarana upgrading berkala kapasitas pengasuhan ayah dan bunda.

---

## 3. Peta Alur Membaca & Verifikasi Dokumen

```mermaid
graph LR
    Doc["Master Dokumen PKN"] --> P1["1. Pelajari Paradigma Insan<br/>(Kenali Karakteristik Anak)"]
    P1 --> P2["2. Kuasai Metode Mendidik<br/>(Bahasa Hati, Lisan, Tangan)"]
    P2 --> P3["3. Pantau Fase Perkembangan<br/>(Thufulah s/d Syabab)"]
    P3 --> P4["4. Petakan Bakat Unik TB40<br/>(Rukun 3A: Suka, Bisa, Berguna)"]
    P4 --> P5["5. Eksekusi Kaidah Lapangan<br/>(Sinergi Ayah, Bunda & Guru)"]
```

### Panduan Aksi Pengguna:
* Ingin membaca ringkasan jawaban cepat atas masalah pengasuhan nyata? Buka [[FAQ Ringkas]].
* Ingin mengetahui cara mendiagnosis penyimpangan anak? Buka bab Tafrith vs Ifrath di setiap berkas bakat.
* Ingin melihat dalil shahih pendukung setiap materi? Telusuri [QURAN_DALIL_CATALOG.md](file:///home/abuhafi/Project/wiki-pkn/QURAN_DALIL_CATALOG.md) dan [DALIL_MAPPING.md](file:///home/abuhafi/Project/wiki-pkn/DALIL_MAPPING.md).
* Ingin mengkaji rekaman audio-visual penjelas? Buka [[Referensi Kajian Video]].
""",

    # 3. FAQ Ringkas.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/FAQ Ringkas.md": """---
title: FAQ Ringkas
---

# FAQ Ringkas: Tanya Jawab Pendidikan Karakter Nabawiyah

Dokumen ini memuat rangkuman jawaban otoritatif atas berbagai pertanyaan mendasar, keraguan teknis, serta dilema praktis yang kerap dihadapi oleh para orang tua dan pendidik saat mengkaji dan menerapkan metode **Pendidikan Karakter Nabawiyah (PKN)**.

> [!quote] Dalil & Rujukan Nabawiyah: Agama adalah Nasihat yang Tulus
> **Naskah Hadits:**  
> « الدِّينُ النَّصِيحَةُ، قُلْنَا: لِمَنْ؟ قَالَ: لِلَّهِ، وَلِكِتَابِهِ، وَلِرَسُولِهِ، وَلِأَئِمَّةِ الْمُسْلِمِينَ وَعَامَّتِهِمْ »
> 
> *"Agama itu adalah nasihat (ketulusan). Kami bertanya: 'Untuk siapa wahai Rasulullah?' Beliau menjawab: 'Untuk Allah, Kitab-Nya, Rasul-Nya, para pemimpin kaum muslimin, dan orang-orang awam di antara mereka.'"*  
> — **HR. Muslim (No. 55) & HR. Bukhari**
> 
> 💡 **Relevansi PKN:** Wiki PKN dan lembar FAQ ini disusun sebagai bentuk nasihat tulus sesama kaum muslimin demi membentengi keluarga dan fitrah anak-anak kita di tengah gelombang fitnah akhir zaman.

---

## 1. Pertanyaan Fondasional: Konsep & Keunggulan PKN

### Q1: Apa perbedaan mendasar antara PKN dan metode parenting barat/konvensional?
**Jawaban:**  
Perbedaan mendasar terletak pada landasan ontologis dan tujuannya:
1. **Landasan Hakikat Manusia:** Psikologi barat umumnya memandang anak sebagai kertas kosong (*tabula rasa*) atau produk evolusi biologis semata. PKN memandang anak sebagai hamba Allah yang terlahir dengan **[[Fitrah (Karakter)]]** bertauhid yang suci dan cetak biru bawaan yang sempurna (*ahsan taqwim*).
2. **Orientasi Akhir:** Parenting modern berfokus pada kesuksesan duniawi materialistis (skor akademik, karier prestisius, kepatuhan sosial semu). PKN berorientasi pada kemaslahatan akhirat: mencetak pribadi yang selamat di hadapan mahkamah Allah, mandiri secara syariat (*mukallaf*), dan memberi manfaat nyata bagi umat (*khairu ummah*).
3. **Metodologi Pembinaan:** PKN tidak mengandalkan intimidasi hukuman atau manipulasi imbalan (*reward & punishment mekanistik*), melainkan mengutamakan keteladanan batin (*qudwah*), pemenuhan tangki cinta (*rahmah*), dialog nalar sehat (*hikmah*), dan ketegasan berbatas syariat (*ta'dib*).

---

### Q2: Mengapa PKN melarang membebani anak usia dini (0–7 tahun) dengan target calistung dan hafalan kaku?
**Jawaban:**  
Berdasarkan sunnatullah perkembangan usia nabawiyah (fase **[[Thufulah]]**), usia 0–7 tahun adalah masa emas pemenuhan hak jiwa muthmainnah melalui penumbuhan cinta, eksplorasi bermain aktif, dan kelekatan emosional dengan orang tua:
* Memaksa anak duduk diam berjam-jam untuk drilling calistung formal merampas hak perkembangan fisiknya (*jiwa ammarah* yang butuh bergerak) dan menekan nalar sebelum waktunya.
* Riwayat shahabat menunjukkan penanaman iman mendahului pengajaran teks: *Jundub bin Abdillah RA* meriwayatkan: *“Kami belajar iman sebelum belajar Al-Qur'an, barulah ketika kami belajar Al-Qur'an bertambahlah iman kami”* (HR. Ibnu Majah No. 61).
* Anak yang tangki cintanya penuh di usia 0–7 tahun akan memasuki fase **[[Tamyiz]]** (7–10 tahun) dengan nalar yang haus ilmu, hati yang tenang, dan kepatuhan sukarela tanpa paksaan.

---

### Q3: Apa yang dimaksud dengan konsep "Akil-Baligh" dan mengapa masyarakat modern memisahkannya?
**Jawaban:**  
Dalam peradaban Islam, kedewasaan adalah satu kesatuan utuh: **Baligh** (tanda kematangan biologis jasad) berjalan seiring dengan **Akil** (kematangan nalar, adab, kemandirian finansial, dan kesiapan memikul beban syariat).
* Pada masa Rasulullah ﷺ, anak-anak usia 15 tahun seperti *Ibnu Umar*, *Zaid bin Tsabit*, dan *Usamah bin Zaid* telah diakui sebagai mukallaf dewasa yang memimpin pasukan dan mengurus urusan umat.
* Sistem sosial modern menciptakan fenomena *adolescence* (remaja galau semu) yang menunda kedewasaan: fisik anak sudah baligh di usia 12–13 tahun, namun mentalnya sengaja dikerdilkan hingga usia 20-an tahun karena dianggap belum mampu bertanggung jawab. PKN berikhtiar merekonstruksi keserentakan Akil dan Baligh melalui pemagangan dan tanggung jawab bertahap di fase **[[Murahaqah]]**.

---

## 2. Pertanyaan Metodologis: Tiga Bahasa & Penerapan di Rumah

### Q4: Bagaimana urutan penerapan Tiga Bahasa Pendidikan Nabawiyah?
**Jawaban:**  
Penerapan tiga bahasa harus mengikuti hirarki yang ketat dan tidak boleh dibalik:
1. **[[Bahasa Hati]] (Edukasi Rasa - Prioritas Utama & Terus Menerus):** Keteladanan akhlak pendidik, limpahan doa di sepertiga malam, pelukan, tatapan mata penuh kasih sayang, dan pengisian tangki cinta tanpa syarat.
2. **[[Bahasa Lisan]] (Edukasi Logika - Digunakan Saat Hati Anak Terhubung):** Dialog dua arah yang lembut, penjelasan sebab-akibat (*qaulan sadida & qaulan layyina*), diskusi nalar yang rasional, dan arahan adab tanpa bentakan.
3. **[[Bahasa Tangan]] (Edukasi Ketegasan - Digunakan Sebagai Benteng Terakhir):** Penegakan konsekuensi logis yang tegas, pembatasan hak, atau ta'dib simbolik yang tidak menyakiti fisik dan batin, hanya setelah Bahasa Hati dan Bahasa Lisan ditunaikan secara maksimal.

> [!warning] Kaidah Emas PKN
> Jika Bahasa Tangan terpaksa digunakan, pastikan amarah orang tua sudah reda sepenuhnya. Bahasa tangan yang keluar dari luapan amarah bukanlah pendidikan nabawiyah, melainkan pelampiasan dendam nafsu ammarah orang tua.

---

### Q5: Bagaimana cara menyeimbangkan peran Ayah dan Bunda dalam pengasuhan sehari-hari?
**Jawaban:**  
Sesuai rancangan syariat dalam **[[Peran Ayah dan Bunda]]**:
* **Ayah memegang mandat Qawwamah (Nakhoda Visi):** Menetapkan visi peradaban keluarga, menjadi penegak hukum dan batasan syariat (*hima*), pelindung dari api neraka (QS. At-Tahrim: 6), serta figur teladan kedisiplinan dan keberanian luar rumah.
* **Bunda memegang mandat Rahimah (Madrasah Cinta):** Pengelola iklim emosional rumah tangga, pendengar setia keluh kesah anak, penuntun adab keseharian, serta penyiram tangki kasih sayang yang mengalirkan ketentraman batin.
* **Sinergi Tanpa Saling Melemahkan:** Ayah tidak boleh meremehkan kelelahan bunda, dan bunda tidak boleh meruntuhkan wibawa ketegasan ayah di depan anak.

---

### Q6: Bagaimana mendidik anak yang menunjukkan tanda-tanda kecanduan gawai (gadget) dan games?
**Jawaban:**  
PKN memandang kecanduan gawai bukan semata masalah teknologi, melainkan gejala **keringnya tangki cinta** dan **tersumbatnya energi bakat jasad**:
1. **Evaluasi Tangki Cinta:** Anak yang haus validasi dan kesepian di rumah akan mencari pelarian dopamin instan di dunia virtual. Penuhi kehadiran jiwa orang tua terlebih dahulu.
2. **Tegakkan [[Batas Toleransi]] (Zonasi Batas):** Buat kesepakatan tegas tanpa negosiasi mengenai waktu dan tempat bebas gawai (*device-free zone* di meja makan dan kamar tidur).
3. **Substitusi dengan Karya Nyata:** Salurkan energi dorongan gerak anak ke aktivitas fisik yang menantang: olahraga memanah/berkuda/berenang, pertukangan kayu, pemagangan proyek, atau eksplorasi [[Pembelajaran Alamiah]].

---

## 3. Pertanyaan Khusus: Bakat, Pemulihan, & Lingkungan

### Q7: Apakah setiap anak pasti memiliki bakat unik dalam PKN? Bagaimana cara menemukannya?
**Jawaban:**  
Ya, mutlak pasti. Allah berfirman: *“Katakanlah: Tiap-tiap orang berbuat menurut keadaannya (bakat bawaannya) masing-masing”* (QS. Al-Isra: 84). Dalam PKN, bakat dipetakan ke dalam **40 Pilar Bakat Nabawiyah (TB40)** di bawah 6 kluster utama:
* Observasi dilakukan menggunakan **Rukun 3A:**
  1. **Suka (*Al-Hirsh*):** Anak melakukan aktivitas tersebut secara spontan dan antusias tanpa disuruh.
  2. **Bisa (*Al-Maqdari*):** Anak cepat menguasai dan menunjukkan kemudahan luar biasa dibanding teman sebayanya.
  3. **Bermanfaat (*Al-Mufid*):** Karya tersebut memberi nilai tambah kebaikan bagi keluarga, masyarakat, dan agama.
* Penajaman bakat dimulai secara serius pada fase **[[Murahaqah]]** melalui magang kerja nyata (*project-based learning*).

---

### Q8: Apa itu sindrom 'Euforia' dan bagaimana mencegahnya agar pengasuhan tidak kandas di tengah jalan?
**Jawaban:**  
Sebagaimana diuraikan dalam **[[Euforia]]**, sindrom ini terjadi ketika orang tua yang baru hijrah parenting merasa sangat antusias, lalu secara tergesa-gesa memaksakan perubahan drastis 180 derajat pada anak dalam semalam (misal: menyita seluruh mainan, mewajibkan hafalan puluhan juz secara mendadak).
* **Akibat:** Anak kaget, tertekan, memberontak, dan orang tua mengalami kejenuhan (*fatrah*) lalu menyerah.
* **Solusi Nabawiyah:** Terapkan kaidah bertahap (**At-Tadarruj**). Perbaiki diri orang tua terlebih dahulu (*tazkiyatun nafs*), basahi rumah dengan kelembutan, dan ubah kebiasaan buruk keluarga satu per satu secara konsisten (*adwamuha wa in qalla* - HR. Bukhari No. 6464).

---

### Q9: Jika orang tua merasa telah melakukan banyak kesalahan fatal di masa lalu, apakah masih bisa diperbaiki?
**Jawaban:**  
Pintu perbaikan tidak pernah tertutup. Allah Maha Pengampun lagi Maha Penyayang (QS. Az-Zumar: 53). Bab **[[Recovery]]** memandu proses pemulihan fitrah melalui 4 langkah terstruktur:
1. **Taubat Nasuha Orang Tua:** Menyesali kelalaian di hadapan Allah dan memohon ampunan-Nya di sepertiga malam.
2. **Rekonsiliasi Rendah Hati:** Meminta maaf secara tulus kepada anak atas luka kata-kata kasar atau penelantaran masa lalu tanpa mencari pembenaran diri.
3. **Pengisian Ulang Tangki Cinta:** Menghabiskan waktu berkualitas berdua tanpa distraksi hingga batin anak mencair.
4. **Restorasi Adab Bertahap:** Menata ulang kesepakatan keluarga baru berlandaskan rasa saling percaya dan kasih sayang.

---

### Q10: Apakah PKN hanya bisa diterapkan oleh keluarga yang homeschooling?
**Jawaban:**  
Tidak. PKN adalah **paradigma cara pandang manusia**, bukan semata format teknis persekolahan. 
* Keluarga yang menyekolahkan anaknya di sekolah formal tetap wajib menerapkan PKN karena mandat utama pendidikan berada di pundak orang tua di rumah (QS. At-Tahrim: 6).
* Orang tua berperan menyaring pengaruh negatif sekolah, mengimbangi kelelahan akademik anak dengan kehangatan rumah, dan membangun **[[Imunitas Sosial]]** agar anak kokoh di tengah pergaulan majemuk.
* Bagi pengelola sekolah, prinsip-prinsip PKN dapat diintegrasikan sebagai ruh budaya madrasah melalui panduan **[[Peran Guru dan Lembaga Pendidikan]]**.
""",

    # 4. Insight & Teknis.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis.md": """---
title: Insight & Teknis
---

# Insight & Teknis Pendidikan Karakter Nabawiyah

Bagian **Insight & Teknis** merupakan jembatan emas yang menghubungkan antara wawasan filosofis (*insight batiniah*) dengan pedoman operasional lapangan (*panduan teknis empiris*) dalam ekosistem **Pendidikan Karakter Nabawiyah (PKN)**. 

> [!quote] Dalil & Rujukan Nabawiyah: Menyatukan Iman dan Aksi Nyata
> **Teks Al-Qur'an:**  
> « فَمَن كَانَ يَرْجُو لِقَاءَ رَبِّهِ فَلْيَعْمَلْ عَمَلًا صَالِحًا وَلَا يُشْرِكْ بِعِبَادَةِ رَبِّهِ أَحَدًا »
> 
> *"Barangsiapa mengharap perjumpaan dengan Tuhannya, maka hendaklah ia mengerjakan amal yang saleh dan janganlah ia mempersekutukan seorangpun dalam beribadah kepada Tuhannya."*  
> — **QS. Al-Kahfi: 110**
> 
> 💡 **Relevansi PKN:** Menegaskan bahwa pemahaman mendalam tentang fitrah anak (insight) harus bermuara pada amal kebaikan terstruktur yang membumi dalam kehidupan sehari-hari (teknis lapangan).

---

## 1. Arsitektur Divisi Insight & Teknis

Divisi ini memuat catatan refleksi, hasil kajian video, serta instrumen terapan yang dirancang untuk memperkaya keterampilan pengasuhan ayah, bunda, dan para guru:

```mermaid
graph TD
    IT["Insight & Teknis PKN"] --> INS["💡 [[Insight]]<br/>(Wawasan Filosofis & Catatan Kritis)"]
    IT --> TEK["🛠️ [[Arahan Teknis Implementasi]]<br/>(SOP Operasional & Panduan Harian)"]
    IT --> SOT["🏫 [[SOTABH]]<br/>(Sekolah Orang Tua Berbasis Hadits)"]
    IT --> VID["🎥 [[Referensi Kajian Video]]<br/>(122 Judul & 1.159 Bab Kajian Transkrip)"]

    INS --> Harmon["Penyelarasan Mindset Pendidik"]
    TEK --> Harmon
    SOT --> Harmon
    VID --> Harmon
```

---

## 2. Peta Sub-Dokumen Utama

### 💡 1. [[Insight]]
Kompilasi artikel pemikiran mendalam dari para asatidzah perintis PKN yang membedah akar permasalahan krisis keluarga modern:
* Mengapa anak kehilangan adab di era informasi berlimpah?
* Fenomena *father hunger* (kelaparan figur ayah) dan dampaknya terhadap orientasi seksual serta kepemimpinan generasi.
* Bagaimana membebaskan diri dari kecemasan berlebihan (*parenting anxiety*) menuju ketenangan tawakkal.

### 🛠️ 2. [[Arahan Teknis Implementasi]]
Buku panduan teknis yang memuat instrumen terapan siap pakai bagi keluarga dan sekolah:
* Standar Operasional Prosedur (SOP) pembiasaan shalat 7–10 tahun dan penegakan konsekuensi 10+ tahun.
* Matriks Observasi Bakat Rukun 3A (*Suka, Bisa, Bermanfaat*) untuk memetakan 40 potensi fitrah anak.
* Format lembar evaluasi pekanan keluarga (*usrah mubarakah*).

### 🏫 3. [[SOTABH]] (Sekolah Orang Tua Berbasis Hadits)
Arsitektur program pelatihan dan kaderisasi orang tua berbasis kajian hadits-hadits tarbiyah:
* Tahapan kurikulum pembelajaran bertingkat (*Mustawa Ula, Wustha, dan 'Ulya*).
* Metodologi bedah hadits tematik untuk diaplikasikan ke dalam studi kasus nyata pengasuhan rumah tangga.
* Pembentukan komunitas pendukung (*peer group*) yang melestarikan iklim keshalihan keluarga.

---

## 3. Kaidah Menggunakan Panduan Teknis

Dalam mengimplementasikan arahan teknis PKN, pendidik wajib memegang teguh kaidah berikut:
1. **Fleksibilitas (*Murunah*):** Setiap keluarga memiliki keunikan kondisi, keterbatasan finansial, dan dinamika jumlah anak. Arahan teknis adalah panduan arah, bukan cetakan kaku yang menuntut keseragaman mutlak.
2. **Prioritaskan Hati Sebelum Aturan:** Jangan pernah menegakkan SOP kedisiplinan teknis jika jembatan cinta batiniah (*Bahasa Hati*) antara anak dan orang tua sedang terputus.
3. **Konsistensi Jangka Panjang:** Perubahan karakter membutuhkan waktu bertahun-tahun; ketekunan mengawal kebiasaan kecil harian jauh lebih berharga daripada gebrakan besar sesaat.
""",

    # 5. Insight.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight.md": """---
title: Insight Wawasan PKN
---

# Insight: Wawasan & Refleksi Kritis Pendidikan Karakter Nabawiyah

Halaman **Insight** menghimpun intisari wawasan filosofis, refleksi kritis, dan catatan lapangan dari para asatidzah serta praktisi **Pendidikan Karakter Nabawiyah (PKN)**. Bagian ini bertujuan mendekonstruksi kekeliruan mindset pengasuhan modern dan mengembalikannya ke rel keautentikan fitrah nubuwah.

> [!quote] Dalil & Rujukan Nabawiyah: Berpijak di Atas Ilmu yang Shahih
> **Teks Al-Qur'an:**  
> « وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِ عِلْمٌ ۚ إِنَّ السَّمْعَ وَالْبَصَرَ وَالْفُؤَادَ كُلُّ أُولَٰئِكَ كَانَ عَنْهُ مَسْئُولًا »
> 
> *"Dan janganlah kamu mengikuti apa yang kamu tidak mempunyai pengetahuan tentangnya. Sesungguhnya pendengaran, penglihatan dan hati, semuanya itu akan diminta pertanggungan jawabnya."*  
> — **QS. Al-Isra': 36**
> 
> 💡 **Relevansi PKN:** Setiap insight tarbiyah harus berakar dari dalil syar'i dan pemahaman mendalam tentang fitrah, bukan sekadar mengikuti opini populer media sosial yang tidak dapat dipertanggungjawabkan di akhirat.

---

## 1. Pokok-Pokok Wawasan Filosofis Pengasuhan

### 🌿 Insight 1: Anak Bukan Miniatur Orang Dewasa
Kesalahan terbesar sistem pendidikan sekuler adalah memperlakukan anak-anak sebagai orang dewasa mini yang dipaksa berpikir abstrak dan memikul target kognitif kompleks sebelum kematangan biologisnya tiba.
* Dalam PKN, anak memiliki dunianya sendiri yang suci: fase **[[Thufulah]]** adalah hak mutlak untuk bergerak, merasakan limpahan cinta, dan meniru keteladanan nyata orang tua.
* Memaksa anak melompati tahapan fitrahnya hanya akan melahirkan kepatuhan semu di luar dan pemberontakan batiniah di kemudian hari.

### 🛡️ Insight 2: Krisis Ayah (*Fatherless*) Adalah Induk Kerusakan Karakter
Ketiadaan kehadiran jiwa ayah (*absent father*) di dalam rumah tangga—meskipun hadir secara fisik—merupakan penyebab utama kerapuhan mental generasi:
* Anak yang kehilangan sentuhan wibawa dan arah dari ayahnya rentan mengalami disorientasi identitas gender, krisis kepercayaan diri, dan kebingungan menentukan prinsip hidup.
* Melalui rekonstruksi **[[Peran Ayah dan Bunda]]**, ayah dipanggil kembali untuk menunaikan mandat *qawwamah*: duduk bersama anak, mengajak berdialog di sepertiga malam, dan memandu visi akhirat keluarga.

### 💧 Insight 3: Tangki Cinta Kosong Adalah Sumber Kenakalan
Perilaku menyimpang anak (kecanduan gawai, berkata kasar, membangkang, hingga pergaulan bebas) hampir selalu bermuara pada **tangki cinta yang bocor atau kering**:
* Hukuman fisik dan bentakan lisan tidak akan pernah mampu menyembuhkan anak yang dahaga kasih sayang; tindakan keras justru memperlebar jurang pemisah.
* Kunci pemulihan adalah membasahi kembali batin anak dengan **[[Bahasa Hati]]** dan penerimaan tanpa syarat (*unconditional love*).

---

## 2. Matriks Transformasi Mindset Pendidik

| Mindset Pengasuhan Lama (Keliru) | Mindset Pengasuhan Nabawiyah (PKN) |
| :--- | :--- |
| Fokus pada hasil nilai rapor dan ranking angka. | Fokus pada kematangan proses adab, integritas, dan kecintaan belajar. |
| Menuntut anak berubah tanpa orang tua mau berkaca. | Memulai perbaikan dari penyucian jiwa (*tazkiyatun nafs*) kedua orang tua. |
| Menganggap kenakalan anak sebagai aib yang harus dimarahi. | Memandang kenakalan sebagai sinyal adanya kebutuhan jiwa/bakat yang belum tersalurkan. |
| Mendidik dengan ancaman, perbandingan sosial, dan rasa bersalah. | Mendidik dengan keteladanan hidup, doa penuh harap, dan dialog rasional. |
| Khawatir berlebihan terhadap masa depan finansial anak. | Menanamkan tauhid dan tawakkal bahwa rezeki telah dijamin Allah SWT. |

---

## 3. Rekomendasi Penelusuran Dokumen Lanjutan

Untuk memperdalam wawasan yang dibahas dalam halaman ini, lanjutkan penelusuran ke materi pendukung berikut:
* Pahami akar trauma dan pemulihannya dalam [[Luka dan Hutang Pengasuhan]] serta [[Recovery]].
* Pelajari bahaya antusiasme sesaat dalam [[Euforia]].
* Tinjau panduan implementasi terapan dalam [[Arahan Teknis Implementasi]] dan kurikulum [[SOTABH]].
""",

    # 6. Arahan Teknis Implementasi.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Arahan Teknis Implementasi.md": """---
title: Arahan Teknis Implementasi
---

# Arahan Teknis Implementasi: Pedoman Operasional Pengasuhan Nabawiyah

Dokumen ini memuat prosedur standar operasional (SOP), checklist harian, instrumen observasi, serta langkah-langkah terapan untuk mengeksekusi prinsip **Pendidikan Karakter Nabawiyah (PKN)** dalam rutinitas keluarga dan lingkungan sekolah.

> [!quote] Dalil & Rujukan Nabawiyah: Ketekunan Beramal Nyata
> **Teks Al-Qur'an:**  
> « فَإِذَا قُضِيَتِ الصَّلَاةُ فَانتَشِرُوا فِي الْأَرْضِ وَابْتَغُوا مِن فَضْلِ اللَّهِ وَاذْكُرُوا اللَّهَ كَثِيرًا لَّعَلَّكُمْ تُفْلِحُونَ »
> 
> *"Apabila telah ditunaikan shalat, maka bertebaranlah kamu di muka bumi; dan carilah karunia Allah dan ingatlah Allah banyak-banyak supaya kamu beruntung."*  
> — **QS. Al-Jumu'ah: 10**
> 
> 💡 **Relevansi PKN:** Keseimbangan antara ibadah ritual spiritual dengan keteraturan aksi teknis di lapangan menjadi kunci keberhasilan mencetak generasi produktif yang diridhai Allah SWT.

---

## 1. Siklus Rutinitas Harian Keluarga Nabawiyah

Penerapan PKN di rumah dibangun di atas ritme sunnah yang teratur, berporos pada 5 waktu shalat fardhu:

```mermaid
graph TD
    Subuh["🌅 WAKTU SUBUH & PAGI<br/>• Shalat Berjamaah di Masjid (Ayah & Anak Laki-laki)<br/>• Dzikir Pagi & Tadabbur 1 Ayat Bersama Bunda<br/>• Pelukan Kehangatan Pengisi Tangki Cinta"] --> Siang["☀️ WAKTU SIANG & SORE<br/>• Eksplorasi Pembelajaran Alamiah / Sekolah<br/>• Makan Siang Beradab & Istirahat Qailulah<br/>• Penyaluran Gerak Fisik & Mengasah 40 Bakat (TB40)"]
    Siang --> Maghrib["🌇 WAKTU MAGHRIB & ISYA<br/>• Shalat Berjamaah & Tilawah Al-Qur'an Bersama<br/>• Evaluasi Pekanan / Dialog Nalar Kasih Sayang<br/>• Menutup Akses Seluruh Gawai (Digital Curfew)"]
    Maghrib --> Malam["🌙 WAKTU MALAM SEBELUM TIDUR<br/>• Adab Wudhu & Membaca Doa/Dzikir Tidur<br/>• Kisah Sirah Shahabat Pengantar Tidur (Bahasa Hati)<br/>• Qiyamul Lail & Doa Mustajab Orang Tua"]
```

---

## 2. Checklist Adab & Tugas Berdasarkan Fase Usia

### 👶 Fase 1: Usia 0–7 Tahun ([[Thufulah]]) — Fokus: Rasa & Fisik
- [ ] Berikan minimal 10 kali pelukan dan ciuman kasih sayang setiap hari kepada ananda.
- [ ] Ajak bermain aktif di luar ruangan (tanah, rumput, air) minimal 1–2 jam sehari tanpa sekat gawai.
- [ ] Dengar tuntas celoteh dan pertanyaan anak dengan kontak mata penuh (*active listening*).
- [ ] Perdengarkan lantunan Al-Qur'an dan kisah kebaikan tanpa memaksakan target hafalan kaku.
- [ ] Tunjukkan keteladanan shalat dan adab nyata di depan mata anak tanpa intimidasi perintah.

### 👦 Fase 2: Usia 7–10 Tahun ([[Tamyiz]]) — Fokus: Nalar & Adab Shalat
- [ ] Perintahkan dan dampingi shalat 5 waktu secara konsisten dan lemah lembut (*amr bil-ma'ruf*).
- [ ] Ajarkan adab privasi syariat: meminta izin masuk kamar orang tua di 3 waktu aurat (QS. An-Nur: 58).
- [ ] Buka sesi dialog nalar sebab-akibat setiap kali anak melakukan kesalahan (*qaulan sadida*).
- [ ] Libatkan anak dalam tugas kerumahtanggaan ringan (merapikan kasur, mencuci piring sendiri).
- [ ] Mulai lakukan observasi kecenderungan bakat unik anak melalui rubrik **Rukun 3A**.

### 🧑 Fase 3: Usia 10–15 Tahun ([[Murahaqah]]) — Fokus: Disiplin & Pra-Baligh
- [ ] Tegakkan konsekuensi tegas jika anak sengaja melalaikan shalat fardhu (sesuai kaidah *ta'dib* nabawiyah).
- [ ] Pisahkan tempat tidur anak laki-laki dan anak perempuan secara ketat.
- [ ] Ajarkan fiqh pubertas: mandi wajib, tanda-tanda baligh, dan penjagaan pandangan (*ghaddhul bashar*).
- [ ] Ajak anak magang proyek nyata atau kerja lapangan bersama ayah/pakar untuk mengasah bakat spesifiknya.
- [ ] Latih kemandirian finansial: mengelola uang saku pribadi dan membiasakan sedekah harian.

---

## 3. Rubrik Observasi Bakat Rukun 3A di Rumah dan Sekolah

Gunakan instrumen sederhana berikut untuk mencatat potensi bawaan lahir anak:

| Parameter Observasi | Pertanyaan Pemandu Pengamatan | Indikator Skor Rendah (1-2) | Indikator Skor Tinggi (4-5) |
| :--- | :--- | :--- | :--- |
| **Suka (*Al-Hirsh*)** | Apakah anak menikmati aktivitas ini secara spontan tanpa harus disuruh atau diiming-imingi hadiah? | Mengerjakan dengan malas, terpaksa, dan mudah bosan. | Mata berbinar, antusias tinggi, dan lupa waktu saat asyik berkarya. |
| **Bisa (*Al-Maqdari*)** | Seberapa cepat anak menguasai keterampilan ini dibanding teman sebayanya? | Membutuhkan bimbingan berulang-ulang dan hasilnya kaku. | Belajar secara intuitif (*otodidak*), cepat mahir, dan memiliki teknik orisinil. |
| **Bermanfaat (*Al-Mufid*)** | Apakah hasil dari aktivitas ini memberi solusi nyata dan kebaikan bagi orang lain? | Hanya dinikmati sendiri dan berpotensi memicu kesombongan. | Membantu meringankan beban keluarga, memecahkan masalah teman, atau bernilai dakwah. |

---

## 4. Tautan Penting Pendukung Arahan Teknis

* Tinjau kaidah filosofis implementasi dalam [[4 Kaidah Implementasi]] dan [[4 Elemen Implementasi]].
* Pelajari panduan penegakan disiplin dalam [[Bahasa Tangan]] dan [[Batas Toleransi]].
* Pelajari kurikulum pelatihan orang tua dalam [[SOTABH]].
""",

    # 7. Paradigma & Implementasi.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi.md": """---
title: Paradigma & Implementasi
---

# Paradigma & Implementasi: Gerbang Arsitektur Utama PKN

Halaman ini merupakan simpul pintu gerbang (*master landing node*) yang memetakan seluruh bangunan teori dan aplikasi praktis **Pendidikan Karakter Nabawiyah (PKN)**. Bagian ini menguraikan dua pilar penyangga utama: **Paradigma Konseptual** (memahami hakikat manusia dan fitrah) serta **Implementasi Operasional** (mengeksekusinya di dunia nyata).

> [!quote] Dalil & Rujukan Nabawiyah: Petunjuk Penjelas Segala Sesuatu
> **Teks Al-Qur'an:**  
> « وَنَزَّلْنَا عَلَيْكَ الْكِتَابَ تِبْيَانًا لِّكُلِّ شَيْءٍ وَهُدًى وَرَحْمَةً وَبُشْرَىٰ لِلْمُسْلِمِينَ »
> 
> *"Dan Kami turunkan kepadamu Al Kitab (Al Quran) untuk menjelaskan segala sesuatu dan petunjuk serta rahmat dan kabar gembira bagi orang-orang yang berserah diri."*  
> — **QS. An-Nahl: 89**
> 
> 💡 **Relevansi PKN:** Al-Qur'an dan Sunnah adalah pedoman paripurna (*tibyanan likulli syai'*) yang menyediakan arsitektur utuh dalam memahami fitrah manusia dan cara mendidiknya.

---

## 1. Struktur Peta Arsitektur Tiga Tingkat

Bangunan dokumen di bawah direktori ini disusun secara logis bertingkat:

```mermaid
graph TD
    Root["Paradigma & Implementasi PKN"] --> P1["1. [[Insan]]<br/>(Pondasi Hakikat Manusia)"]
    Root --> P2["2. [[Pendidikan Ideal]]<br/>(Metodologi & Benang Merah)"]
    Root --> P3["3. [[Implementasi]]<br/>(Kaidah, Elemen & Tanggung Jawab)"]

    P1 --> C1["• [[Tujuan Hidup Manusia]]<br/>• [[Bersatunya Ruh dan Jasad Membentuk Jiwa]]<br/>• [[Pembagian Jiwa]] (Muthmainnah, Lawwamah, Ammarah)<br/>• [[Fitrah (Karakter)]] (Iman, Belajar, Bakat)<br/>• [[Perkembangan]] (Thufulah s/d Syabab)"]
    P2 --> C2["• [[Benang Merah Pendidikan]] (Wasathiyah)<br/>• [[Metode Mendidik]] (Bahasa Hati, Lisan, Tangan)<br/>• [[Pembelajaran Alamiah]]<br/>• [[Batas Toleransi]] & [[Imunitas Sosial]]<br/>• [[Luka dan Hutang Pengasuhan]] & [[Recovery]]"]
    P3 --> C3["• [[4 Kaidah Implementasi]] (Taisir, Qudwah, Rahmah, Tadarruj)<br/>• [[4 Elemen Implementasi]] (Ghayah, Manhaj, Uslub, Taqyim)<br/>• [[Tazkiyatun Nafs]] & [[Tawakkal dan Doa]]<br/>• [[Tanggung Jawab Pendidikan]]<br/>• [[Peran Ayah dan Bunda]] & [[Peran Guru dan Lembaga Pendidikan]]"]
```

---

## 2. Intisari Tiga Pilar Utama

### 🧬 Pilar I: [[Insan]] (Siapa yang Kita Didik?)
Pendidikan tidak akan pernah berhasil jika pendidik keliru memahami objek yang dididiknya. Pilar Insan memetakan manusia secara utuh:
* Manusia diciptakan untuk mengabdi kepada Allah dan memimpin peradaban bumi ([[Tujuan Hidup Manusia]]).
* Manusia adalah perpaduan antara tanah (jasad) dan tiupan ruh Ilahi yang melahirkan entitas jiwa dinamis ([[Bersatunya Ruh dan Jasad Membentuk Jiwa]]).
* Dinamika jiwa bertingkat tiga: nafsu **[[Ammarah]]** (jasad/kemauan), nafsu **[[Lawwamah]]** (akal/nalar), dan nafsu **[[Muthmainnah]]** (hati/iman).
* Setiap anak membawa cetak biru fitrah ketauhidan suci sejak lahir ([[Fitrah (Karakter)]]) dan anugerah 40 potensi bakat unik ([[Bakat]]).
* Pertumbuhan anak melintasi 4 siklus sunnatullah: [[Thufulah]] (0–7 th), [[Tamyiz]] (7–10 th), [[Murahaqah]] (10–15 th), dan [[Syabab]] (15+ th).

### 🎯 Pilar II: [[Pendidikan Ideal]] (Bagaimana Cara Mendidiknya?)
Membahas prinsip-prinsip pedagogis murni warisan Rasulullah ﷺ:
* Berjalan di atas garis lurus jalan tengah (*wasathiyah*) menghindari sikap meremehkan (*tafrith*) maupun memaksa melampaui batas (*ifrath*) dalam [[Benang Merah Pendidikan]].
* Memadukan hirarki tiga bahasa tarbiyah nabawiyah: kehangatan batin dalam [[Bahasa Hati]], dialog logis santun dalam [[Bahasa Lisan]], dan ketegasan berbatas syariat dalam [[Bahasa Tangan]].
* Membebaskan anak dari penjara kelas formal melalui [[Pembelajaran Alamiah]].
* Membangun ketahanan moral anak melalui [[Batas Toleransi]] dan [[Imunitas Sosial]] di tengah fitnah digital.
* Menyembuhkan trauma pengasuhan masa lalu secara sistematis dalam [[Luka dan Hutang Pengasuhan]] dan [[Recovery]].

### ⚙️ Pilar III: [[Implementasi]] (Bagaimana Mengeksekusinya di Lapangan?)
Membahas kaidah praktis eksekusi di lingkungan keluarga dan sekolah:
* Memegang teguh [[4 Kaidah Implementasi]]: Bertahap (*Tadarruj*), Keteladanan (*Qudwah*), Kasih Sayang (*Rahmah*), dan Menjaga Fitrah.
* Mengintegrasikan [[4 Elemen Implementasi]]: Tujuan (*Ghayah*), Kurikulum (*Manhaj*), Metode (*Uslub*), dan Evaluasi (*Taqyim*).
* Menjadikan pensucian jiwa pendidik ([[Tazkiyatun Nafs]]) serta kepasrahan doa ([[Tawakkal dan Doa]]) sebagai poros utama.
* Menegakkan mandat fardhu 'ain pengasuhan dalam [[Tanggung Jawab Pendidikan]], serta membagi peran seimbang antara ayah, bunda, dan sekolah ([[Peran Ayah dan Bunda]], [[Peran Guru dan Lembaga Pendidikan]]).

---

## 3. Langkah Lanjutan

Silakan buka masing-masing pilar di atas untuk menelaah naskah lengkapnya, atau rujuk [QURAN_DALIL_CATALOG.md](file:///home/abuhafi/Project/wiki-pkn/QURAN_DALIL_CATALOG.md) untuk mempelajari ratusan dalil Al-Qur'an yang mendasari setiap bab ini.
""",

    # 8. Kaidah & Elemen.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Kaidah & Elemen.md": """---
title: Kaidah & Elemen Implementasi
---

# Kaidah & Elemen Implementasi Pendidikan Karakter Nabawiyah

Halaman ini merupakan sintesis induk yang merangkum kaidah operasional dan komponen arsitektur dalam mengeksekusi kurikulum **Pendidikan Karakter Nabawiyah (PKN)** di lingkungan keluarga, sekolah, maupun komunitas dakwah.

> [!quote] Dalil & Rujukan Nabawiyah: Fondasi Kebajikan yang Menyeluruh
> **Teks Al-Qur'an:**  
> « لَّيْسَ الْبِرَّ أَن تُوَلُّوا وُجُوهَكُمْ قِبَلَ الْمَشْرِقِ وَالْمَغْرِبِ وَلَٰكِنَّ الْبِرَّ مَنْ آمَنَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ وَالْمَلَائِكَةِ وَالْكِتَابِ وَالنَّبِيِّينَ وَآتَى الْمَالَ عَلَىٰ حُبِّهِ ذَوِي الْقُرْبَىٰ وَالْيَتَامَىٰ وَالْمَسَاكِينَ... »
> 
> *"Bukanlah menghadapkan wajahmu ke arah timur dan barat itu suatu kebajikan, akan tetapi sesungguhnya kebajikan itu ialah beriman kepada Allah, hari kemudian, malaikat-malaikat, kitab-kitab, nabi-nabi dan memberikan harta yang dicintainya kepada kerabatnya, anak-anak yatim, orang-orang miskin..."*  
> — **QS. Al-Baqarah: 177**
> 
> 💡 **Relevansi PKN:** Implementasi pendidikan bukanlah formalitas ritual lahiriah atau penyeragaman mekanis, melainkan keterpaduan utuh antara iman yang menghujam di batin dan amal kebajikan terukur yang dirasakan manfaatnya oleh sesama.

---

## 1. Matriks Sinergi: 4 Kaidah Emas x 4 Elemen Operasional

Keberhasilan implementasi PKN ditentukan oleh bertemunya **4 Kaidah Emas** (nilai-nilai penuntun) dengan **4 Elemen Operasional** (instrumen teknis):

| Elemen Operasional (Al-Arkan) | Kaidah 1: Kemudahan (*At-Taisir*) | Kaidah 2: Keteladanan (*Al-Qudwah*) | Kaidah 3: Kasih Sayang (*Ar-Rahmah*) | Kaidah 4: Bertahap (*At-Tadarruj*) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Tujuan (*Al-Ghayah*)** | Menetapkan target ibadah yang realistis dan membahagiakan anak. | Pendidik mencontohkan orientasi akhirat dalam keseharian nyata. | Menjadikan ridha Allah dan cinta keluarga sebagai motivasi utama. | Target kematangan disesuaikan dengan kesiapan fase usia anak. |
| **2. Kurikulum (*Al-Manhaj*)** | Materi aplikatif, fungsional, dan tidak membebani nalar berlebih. | Kurikulum adab diajarkan melalui praktik hidup orang tua di rumah. | Kurikulum memprioritaskan penuntasan tangki cinta sebelum hukum. | Materi disusun terstruktur: Adab ➡️ Iman ➡️ Al-Qur'an ➡️ Keahlian. |
| **3. Metode (*Al-Uslub*)** | Menggunakan sarana bermain, visual, dan dialog santun yang menyenangkan. | Guru/orang tua menjadi figur hidup (*living curriculum*) yang ditiru. | Menghindari bentakan, celaan, dan kekerasan fisik dalam mengajar. | Hirarki metode: Bahasa Hati ➡️ Bahasa Lisan ➡️ Bahasa Tangan. |
| **4. Evaluasi (*At-Taqyim*)** | Menilai proses dan daya juang, bukan sekadar skor angka ujian formal. | Evaluasi dimulai dari muhasabah diri pendidik sebelum menilai anak. | Memberikan apresiasi tulus atas setiap kemajuan kecil anak. | Evaluasi kualitatif jangka panjang menuju kematangan Akil-Baligh. |

---

## 2. Penjelasan Rinci Sub-Dokumen

### 📜 1. [[4 Kaidah Implementasi]]
Membedah empat pilar metodologis yang menjadi pagar pengaman tarbiyah:
1. **At-Taisir (Prinsip Kemudahan):** *“Yassiru wa la tu'assiru”*—agama disajikan secara menggembirakan tanpa mempersulit.
2. **Al-Qudwah (Prinsip Keteladanan):** Anak adalah cermin; keshalihan orang tua adalah kurikulum paling berpengaruh.
3. **Ar-Rahmah (Prinsip Kasih Sayang):** Kasih sayang tanpa syarat menjadi prasyarat diterimanya nasihat.
4. **At-Tadarruj (Prinsip Bertahap):** Pendidikan mengikuti sunnatullah pertumbuhan biologis dan kesiapan mental.

### ⚙️ 2. [[4 Elemen Implementasi]]
Membedah empat instrumen operasional peradaban:
1. **Al-Ghayah (Tujuan Tertinggi):** Menghamba kepada Allah dan memakmurkan bumi (*ibadah & khilafah*).
2. **Al-Manhaj (Rancang Bangun Jalur):** Kurikulum terintegrasi yang mengharmoniskan fardhu 'ain dan fardhu kifayah.
3. **Al-Uslub (Metodologi Terapan):** Fleksibilitas metode mengajar sesuai karakteristik gaya belajar anak.
4. **At-Taqyim (Monitoring & Evaluasi):** Pengukuran berkelanjutan menggunakan instrumen observasi autentik Rukun 3A.

---

## 3. Checklist Audit Implementasi untuk Lembaga & Keluarga

Gunakan checklist berkala ini untuk memastikan program pendidikan tidak menyimpang dari rel PKN:
- [ ] Apakah anak-anak merasa bahagia, aman, dan dicintai di lingkungan belajarnya?
- [ ] Apakah orang tua dan guru sudah mempraktikkan adab yang dituntut dari anak-anak?
- [ ] Apakah target belajar sudah disesuaikan dengan kapasitas fase usia (*Thufulah, Tamyiz, Murahaqah*)?
- [ ] Apakah evaluasi belajar sudah menghargai keberagaman potensi unik 40 bakat anak tanpa penyeragaman kaku?
""",

    # 9. Internal & Eksternal.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Internal & Eksternal.md": """---
title: Internal & Eksternal
---

# Faktor Internal & Eksternal dalam Pendidikan Karakter Nabawiyah

Keberhasilan pembentukan karakter anak adalah hasil harmonisasi antara **Faktor Internal** (kesucian batiniah dan kualitas spiritual pendidik) dengan **Faktor Eksternal** (ikhtiar nyata, doa, dan proteksi lingkungan pergaulan).

> [!quote] Dalil & Rujukan Nabawiyah: Perubahan Bermula dari Dalam Jiwa
> **Teks Al-Qur'an:**  
> « إِنَّ اللَّهَ لَا يُغَيِّرُ مَا بِقَوْمٍ حَتَّىٰ يُغَيِّرُوا مَا بِأَنفُسِهِمْ »
> 
> *"Sesungguhnya Allah tidak mengubah keadaan suatu kaum sehingga mereka mengubah keadaan yang ada pada diri mereka sendiri..."*  
> — **QS. Ar-Ra'd: 11**
> 
> 💡 **Relevansi PKN:** Transformasi karakter anak bermula dari perbaikan internal jiwa kedua orang tuanya; iklim batin rumah tangga yang bersih akan memancarkan energi kebaikan yang menyerap ke sanubari generasi.

---

## 1. Peta Sinergi Faktor Internal dan Eksternal

```mermaid
graph LR
    subgraph INTERNAL["💎 FAKTOR INTERNAL (JIWA PENDIDIK)"]
        Tazkiyah["[[Tazkiyatun Nafs]]<br/>• Pembersihan Syirik & Hasad<br/>• Keikhlasan Niat Lillahi Ta'ala<br/>• Ketenangan Batin Orang Tua"]
        Qudwah["Keteladanan Autentik<br/>• Keselarasan Kata dan Perbuatan<br/>• Qalbun Salim di Dalam Rumah"]
    end

    subgraph EKSTERNAL["🛡️ FAKTOR EKSTERNAL (IKHTIAR & BENTENG)"]
        Doa["[[Tawakkal dan Doa]]<br/>• Doa Sepertiga Malam Terakhir<br/>• Penyerahan Hasil Mutlak ke Allah"]
        Hima["[[Batas Toleransi]]<br/>• Proteksi Gawai & Pornografi<br/>• Aturan Privasi & Aurat Syariat"]
        Bi'ah["[[Imunitas Sosial]]<br/>• Komunitas & Sahabat Shalih<br/>• Filter Ekosistem Masyarakat"]
    end

    INTERNAL --> Output["Pembentukan Karakter Mukallaf Akil-Baligh"]
    EKSTERNAL --> Output
```

---

## 2. Uraian Pokok Dua Dimensi Penunjang

### 💎 1. Dimensi Internal: [[Tazkiyatun Nafs]]
* **Penyucian Jiwa Orang Tua Adalah Kunci:** Anak adalah spons spiritual yang menyerap energi batin orang tuanya. Jika hati orang tua dipenuhi kemarahan, kecemasan, atau riya, anak akan merespon dengan kegelisahan dan pembangkangan.
* **Takhalliyah & Tahalliyah:** Membersihkan batin dari penyakit hati (*hasad, ujub, takabbur*) dan menghiasinya dengan kesabaran, syukur, serta prasangka baik (*husnuzhan*).

### 🛡️ 2. Dimensi Eksternal: [[Tawakkal dan Doa]]
* **Ikhtiar Maksimal Diiringi Tawakkal Total:** Mendidik dengan teknik terbaik, namun meyakini bahwa hidayah taufiq mutlak berada di tangan Allah SWT.
* **Kekuatan Doa Penembus Langit:** Meneladani doa para nabi (Nabi Ibrahim AS dan Luqman AS) yang secara konsisten memohon anak keturunan penyejuk hati (*qurrata a'yun*) dan penjaga shalat.
* **Sinergi dengan Proteksi Nyata:** Doa harus dibarengi dengan penjagaan batasan syariat ([[Batas Toleransi]]) dan pengkondisian lingkungan yang kondusif ([[Imunitas Sosial]]).

---

## 3. Rekomendasi Kajian Lanjutan

* Pelajari metode pembersihan hati secara mendalam di [[Tazkiyatun Nafs]].
* Pelajari adab memanjatkan doa mustajab untuk anak di [[Tawakkal dan Doa]].
* Pelajari benteng proteksi pergaulan anak di [[Imunitas Sosial]] dan [[Batas Toleransi]].
""",

    # 10. Peran & Tanggung Jawab.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran & Tanggung Jawab.md": """---
title: Peran & Tanggung Jawab
---

# Peran & Tanggung Jawab dalam Pendidikan Karakter Nabawiyah

Halaman ini membedah arsitektur akuntabilitas dan pembagian peran para pemangku kepentingan (*stakeholders*) dalam ekosistem **Pendidikan Karakter Nabawiyah (PKN)**. Bagian ini menegaskan batas tanggung jawab syar'i antara orang tua, guru, lembaga pendidikan, dan masyarakat luas.

> [!quote] Dalil & Rujukan Nabawiyah: Pertanggungjawaban Mutlak Setiap Pemimpin
> **Naskah Hadits:**  
> « كُلُّكُمْ رَاعٍ وَكُلُّكُمْ مَسْئُولٌ عَنْ رَعِيَّتِهِ، فَالْإِمَامُ رَاعٍ وَمَسْئُولٌ عَنْ رَعِيَّتِهِ، وَالرَّجُلُ رَاعٍ فِي أَهْلِهِ وَهُوَ مَسْئُولٌ عَنْ رَعِيَّتِهِ، وَالْمَرْأَةُ رَاعِيَةٌ فِي بَيْتِ زَوْجِهَا وَمَسْئُولَةٌ عَنْ رَعِيَّتِهَا »
> 
> *"Setiap kalian adalah pemimpin dan setiap kalian akan dimintai pertanggungjawaban atas kepemimpinannya. Seorang imam adalah pemimpin dan bertanggung jawab atas rakyatnya. Seorang laki-laki (ayah) adalah pemimpin dalam keluarganya dan bertanggung jawab atas mereka. Dan seorang wanita (ibu) adalah pemimpin di rumah suaminya dan bertanggung jawab atas urusannya..."*  
> — **HR. Bukhari (No. 893) & HR. Muslim (No. 1829)**
> 
> 💡 **Relevansi PKN:** Menetapkan garis batas hukum syariat bahwa tanggung jawab pendidikan generasi berada di pundak keluarga; sekolah dan masyarakat hanyalah mitra penopang.

---

## 1. Segitiga Emas Ekosistem Pendidikan Nabawiyah

```mermaid
graph TD
    Keluarga["🏠 KELUARGA (PENANGGUNG JAWAB UTAMA - FARDHU 'AIN)<br/>• [[Peran Ayah dan Bunda]]: Qawwamah & Rahimah<br/>• [[Tanggung Jawab Pendidikan]]: Perlindungan Api Neraka"]
    Sekolah["🏫 SEKOLAH / GURU (MITRA PENOPANG - WARATSATUL ANBIYA')<br/>• [[Peran Guru dan Lembaga Pendidikan]]: Transfer Adab & Keahlian<br/>• Fasilitasi 40 Bakat Unik Murid Tanpa Penyeragaman Kaku"]
    Masyarakat["🌍 MASYARAKAT / LINGKUNGAN (BENTENG BUDAYA)<br/>• Kontrol Sosial Amar Ma'ruf Nahi Munkar<br/>• Penyediaan Ekosistem Shalih Penumbuh [[Imunitas Sosial]]"]

    Keluarga <-->|Amanah & Delegasi Terbatas| Sekolah
    Sekolah <-->|Kiprah & Pengabdian Nyata| Masyarakat
    Masyarakat <-->|Benteng Budaya Bersama| Keluarga
```

---

## 2. Rincian Tiga Pilar Tanggung Jawab

### 🏠 1. [[Tanggung Jawab Pendidikan]] & [[Peran Ayah dan Bunda]]
* **Mandat Fardhu 'Ain yang Tidak Bisa Dialihkan:** Perintah menjaga keluarga dari api neraka (QS. At-Tahrim: 6) dialamatkan langsung kepada orang tua, bukan kepada menteri pendidikan atau kepala sekolah.
* **Peran Qawwamah Ayah:** Menentukan arah visi akhirat, memimpin musyawarah keluarga, menjadi teladan ketegasan hukum, dan mencari rezeki halal.
* **Peran Rahimah Bunda:** Menjadi madrasah cinta pertama, menjaga kehangatan emosional rumah, membiasakan adab harian, dan mengisi penuh tangki kasih sayang anak.

### 🏫 2. [[Peran Guru dan Lembaga Pendidikan]]
* **Kedudukan Guru Sebagai Pewaris Nabi:** Guru memegang tugas mulia meneruskan risalah kenabian: membacakan ayat (*tilawah*), menyucikan jiwa murid (*tazkiyah*), dan mengajarkan hikmah (*ta'lim*).
* **Bukan Pabrik Penyeragaman:** Lembaga pendidikan PKN menolak perlakuan murid seperti botol kosong yang diisi secara seragam; guru bertindak sebagai fasilitator yang mengasah keunikan 40 bakat bawaan masing-masing anak.

### 🌍 3. Hak dan Kewajiban Timbal Balik
Sebagaimana dibahas dalam **[[Hak dan Kewajiban]]**, keadilan syariat mengharuskan terpenuhinya hak anak di masa kecil (hak hidup, hak bermain, hak disayangi, hak mengenal tauhid) agar kelak menghasilkan generasi yang berbakti (*birrul walidain*) dan bertanggung jawab memajukan peradaban umat.

---

## 3. Peta Penelusuran Dokumen Terkait

* Pahami landasan kewajiban orang tua di [[Tanggung Jawab Pendidikan]].
* Pahami rincian dwi-tunggal pengasuhan di [[Peran Ayah dan Bunda]].
* Pahami etika kemitraan sekolah di [[Peran Guru dan Lembaga Pendidikan]].
* Pahami timbal balik hak anak dan orang tua di [[Hak dan Kewajiban]].
""",

    # 11. Template.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Template.md": """---
title: Standar Template Wiki PKN
---

# Panduan Kontributor & Standar Dokumentasi Wiki PKN

Halaman ini merupakan pedoman standarisasi penulisan, format struktur, dan kriteria penilaian mutu artikel bagi seluruh kontributor yang menyusun konten di dalam **Wiki Pendidikan Karakter Nabawiyah (PKN)**.

> [!quote] Dalil & Rujukan Nabawiyah: Bekerja dengan Kualitas Tertinggi (Itqan)
> **Naskah Hadits:**  
> « إِنَّ اللَّهَ يُحِبُّ إِذَا عَمِلَ أَحَدُكُمْ عَمَلًا أَنْ يُتْقِنَهُ »
> 
> *"Sesungguhnya Allah mencintai seseorang di antara kalian yang apabila melakukan suatu pekerjaan, ia mengerjakannya dengan tekun, cermat, dan berkualitas tinggi (itqan)."*  
> — **HR. Al-Baihaqi (Syu'abul Iman No. 4930)**
> 
> 💡 **Relevansi PKN:** Menulis dan mendokumentasikan ilmu tarbiyah nabawiyah adalah amal jariyah yang menuntut kesungguhan ilmiah (*itqan*), kejelasan takhrij dalil, kerapian tipografi, dan kelengkapan materi.

---

## 1. Ambang Batas Kualitas Artikel Wiki PKN (Standar Emas)

Setiap artikel substantif di Wiki PKN wajib memenuhi ambang batas kualitas berikut:
1. **Panjang Karakter:** Minimal **5.000 karakter** (sekitar 750–1.200 kata) konten akademik berbobot tanpa pengulangan kata kosong (*filler*).
2. **Keaslian Dalil:** Memuat setidaknya **1 dalil Al-Qur'an** dan **1 hadits shahih** berharakat lengkap, terjemahan resmi bahasa Indonesia, dan takhrij kitab induk dari korpus **OpenBayan** (`data/shamela_corpus.db`).
3. **Kutipan Ulama Klasik:** Mengintegrasikan penjelasan (*syarah*) dari ulama mu'tabar seperti *Ibnul Qayyim, Imam Al-Ghazali, Ibnu Katsir, Ibnu Hajar, An-Nawawi, Ibnu Khaldun, atau Asy-Syathibi*.
4. **Keteladanan Shahabat Nabi ﷺ:** Menyertakan kisah nyata interaksi tarbiyah Rasulullah ﷺ dengan para sahabat (dewasa maupun anak-anak).
5. **Kesesuaian Format Quartz:** Menggunakan frontmatter YAML yang valid, callout Obsidian (`[!quote]`, `[!warning]`, `[!info]`, `[!tip]`), serta tautan silang (*wikilinks* `[[...]]`).

---

## 2. Anatomi Baku 8 Bagian Artikel Ilmiah PKN

Setiap penulisan artikel tema pokok wajib mengikuti kerangka 8 bagian terstruktur:

```markdown
---
title: "Judul Artikel"
---

# Judul Artikel

> [!quote] Dalil & Rujukan Nabawiyah
> **Naskah Ayat / Hadits:**  
> « (Teks Arab Berharakat Lengkap) »
> 
> *"(Terjemahan Resmi Bahasa Indonesia)"*
> 
> 📚 **Sumber Rujukan OpenBayan:** (Nama Kitab, Nomor Hadits / Juz & Halaman)  
> 💡 **Relevansi Pedagogis PKN:** (Penjelasan kedudukan dalil dalam pengasuhan)

## 1. Definisi & Konsep Fondasional
- Makna etimologi (bahasa) dan terminologi syariat.
- Kedudukan konsep dalam arsitektur Pendidikan Karakter Nabawiyah.

## 2. Relevansi Pedagogis & Syarah Ulama Klasik
- Penjelasan syarah hadits/tafsir dari ulama mu'tabar.
- Contoh interaksi nyata Rasulullah ﷺ dengan para sahabat.

## 3. Taksonomi & Komponen Esensial
- Pembagian pilar/elemen pembentuk karakter.
- Matriks karakteristik dan indikator perilaku terukur.

## 4. Diagnosis Penyimpangan: Tafrith vs Ifrath
- **Tafrith (Meremehkan / Lalai):** Gejala, akar masalah, dan dampak buruk.
- **Ifrath (Berlebihan / Memaksa):** Gejala over-demanding dan trauma fitrah.
- **Al-Wasathiyah (Jalan Tengah Nabawiyah):** Titik keseimbangan ideal.

## 5. Panduan Praktis untuk Orang Tua & Pendidik
- Rubrik Observasi (Rukun 3A: Suka, Bisa, Bermanfaat).
- Fasilitasi lingkungan rumah dan sekolah.

## 6. Penerapan Berdasarkan Fase Perkembangan Usia
- Penerapan bertahap pada fase Thufulah (0–7 th), Tamyiz (7–10 th), Murahaqah (10–15 th), dan Syabab (15+ th).

## 7. Studi Kasus Nyata & Solusi Kuratif
- Skenario masalah nyata dalam pengasuhan modern dan tahapan solusinya.

## 8. Tautan Relevan & Peta Konsep
- Tautan silang ke halaman wiki terkait menggunakan format [[Nama Halaman]].
```

---

## 3. Daftar Template Khusus yang Tersedia

Silakan gunakan master template berikut sesuai jenis dokumen yang hendak ditulis:
* **[[Template Tema]]:** Format baku untuk artikel tema pokok, filosofis, dan bab materi utama.
* **[[Template Elemen Karakteristik]]:** Format baku untuk merinci sifat, bakat, dan profil karakter anak.
* **[[Template Elemen Refleksi, Implementas, Risiko, dan Tautan]]:** Format baku untuk callout studi kasus lapangan, analisis risiko pengasuhan, dan tautan silang.
""",

    # 12. Template Tema.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Template/Template Tema.md": """---
title: Template Tema
---

# Template Penulisan Tema Pokok PKN

Gunakan template ini untuk menulis atau mengembangkan artikel tema materi pokok dalam Wiki Pendidikan Karakter Nabawiyah. Setiap bagian dirancang untuk memastikan kedalaman materi akademik, keotentikan dalil syariat, dan aplikabilitas praktis bagi orang tua.

---

## Contoh Struktur Kode Markdown Template:

```markdown
---
title: "Nama Tema Pokok"
---

# [Nama Tema Pokok]

(Paragraf pengantar: 2-3 paragraf komprehensif yang menguraikan latar belakang masalah, urgensi tema dalam peradaban Islam, dan kedudukannya dalam arsitektur Pendidikan Karakter Nabawiyah.)

> [!quote] Dalil & Rujukan Nabawiyah
> **Naskah Ayat / Hadits:**  
> « (Teks Arab berharakat lengkap disalin dari katalog dalil OpenBayan) »
> 
> *"(Terjemahan resmi bahasa Indonesia yang shahih dan mudah dipahami)"*
> 
> 📚 **Sumber Rujukan OpenBayan:** (Contoh: Shahih al-Bukhari No. XXXX / Tafsir Ibnu Katsir Juz X Hal. Y)  
> 💡 **Relevansi Pedagogis PKN:** (Penjelasan 2-3 kalimat mengenai relevansi dalil dengan pengasuhan anak)

---

## 1. Definisi & Konsep Fondasional
- **Makna Bahasa (Etimologi):** Akar kata bahasa Arab dan asal-usul istilah.
- **Makna Syar'i (Terminologi):** Batasan makna menurut para ulama mu'tabar.
- **Urgensi Fitrah:** Mengapa aspek ini menjadi pilar pembentukan kepribadian mukallaf yang kokoh.

## 2. Relevansi Pedagogis & Syarah Ulama Klasik
- Syarah mendalam dari kitab klasik (*Madarijus Salikin Ibnul Qayyim, Ihya Ulumiddin Al-Ghazali, Fathul Bari Ibnu Hajar, dll.*).
- Teladan interaksi tarbiyah Rasulullah ﷺ dengan para sahabat besar dan anak-anak kecil (*Hasan, Husain, Anas bin Malik, Ibnu Abbas, Usamah bin Zaid, dll.*).

## 3. Komponen & Taksonomi Karakter
- Rincian pilar-pilar pembentuk (misal: pilar bakat, dimensi batin, atau instrumen adab).
- Matriks karakteristik perilaku yang dapat diamati sehari-hari.

## 4. Diagnosis Penyimpangan: Tafrith vs Ifrath
- **Tafrith (Meremehkan / Melalaikan):** Gejala pengabaian hak anak, dampak kejiwaan, dan penyebab kesalahan pola asuh.
- **Ifrath (Melampaui Batas / Memaksa):** Gejala penekanan kaku, pemaksaan kurikulum sebelum waktunya, dan luka batin yang ditimbulkan.
- **Wasathiyah (Jalan Tengah Nabawiyah):** Posisi keseimbangan ideal yang dicontohkan Rasulullah ﷺ.

## 5. Panduan Praktis untuk Ayah, Bunda & Guru
- Langkah konkret penerapan di rumah dan ruang kelas.
- Rubrik Observasi Rukun 3A (*Suka, Bisa, Bermanfaat*).
- Penyelarasan doa dan kebersihan batin (*tazkiyatun nafs*) pendidik sebelum mendidik anak.

## 6. Penerapan Berdasarkan Fase Perkembangan Usia
- **Fase Thufulah (0–7 Tahun):** Pendekatan bermain aktif, keteladanan visual, dan limpahan kasih sayang tanpa syarat.
- **Fase Tamyiz (7–10 Tahun):** Pembiasaan adab shalat, latihan tanggung jawab terstruktur, dan dialog nalar dua arah.
- **Fase Murahaqah (10–15 Tahun):** Penegakan disiplin tegas berbatas syariat, mentoring bakat, dan pemagangan proyek nyata.
- **Fase Syabab (15+ Tahun):** Kemitraan dewasa, kemandirian finansial dan sosial, serta karya peradaban penegak ummah.

## 7. Studi Kasus Nyata & Solusi Kuratif
- Paparan kasus nyata problematika anak kontemporer (misal: kecanduan gawai, mogok belajar, tantrum, krisis identitas).
- Tahapan solusi kuratif langkah-demi-langkah berlandaskan kaidah PKN.

## 8. Tautan Relevan & Peta Konsep
- Tautan silang ke halaman pendukung: [[Insan]], [[Metode Mendidik]], [[Batas Toleransi]], dll.
```
""",

    # 13. Template Elemen Karakteristik.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Template/Template Elemen Karakteristik.md": """---
title: Template Elemen Karakteristik
---

# Template Deskripsi Karakteristik & Bakat Anak

Gunakan template ini khusus untuk mendeskripsikan elemen karakteristik personal, sifat kepribadian, atau turunan **40 Pilar Bakat Nabawiyah (TB40)** di bawah 6 sub-bakat utama.

---

## Contoh Format Standar Penulisan:

```markdown
---
title: "Nama Karakteristik / Bakat"
---

# [Nama Karakteristik / Bakat] (Istilah Arab)

(Paragraf pembuka: Definisi ringkas karakteristik bakat, letak energinya dalam trilogi jiwa—apakah dominan di Jiwa Muthmainnah/Rasa, Lawwamah/Cipta, atau Ammarah/Karsa—serta orientasi introversi/ekstroversinya.)

> [!quote] Dalil & Figur Keteladanan Shahabat Nabi ﷺ
> **Figur Teladan:** (Nama Sahabat, misal: Khalid bin Walid, Abu Dzar Al-Ghifari, Zaid bin Tsabit)  
> **Kutipan Dalil / Hadits:**  
> « (Teks hadits sanjungan atau penugasan Nabi ﷺ kepada sahabat tersebut) »  
> *"(Terjemahan hadits)"*  
> 💡 **Hikmah Bakat:** Mengapa Rasulullah ﷺ menempatkan sahabat ini pada pos peran peradaban tersebut sesuai potensi bawaannya.

---

## 1. Indikator Perilaku Alami (Natural Traits)
Ciri-ciri spontan yang tampak pada anak yang memiliki karakteristik ini:
* **Bahasa Tubuh & Gestur:** Cepat bergerak / gemar mengamati / tenang menyimak.
* **Respon Emosional:** Spontan empati / analitis kritis / berani mengambil risiko.
* **Kegiatan Favorit:** Membongkar benda / memimpin kawan / melayani kebutuhan orang lain.

## 2. Rubrik Evaluasi Rukun 3A
| Dimensi Rukun 3A | Gejala yang Teramati pada Anak |
| :--- | :--- |
| **Suka (*Al-Hirsh*)** | Anak menekuni aktivitas ini berjam-jam tanpa rasa lelah dan selalu bersemangat memulainya kembali. |
| **Bisa (*Al-Maqdari*)** | Menunjukkan kecepatan belajar luar biasa, memiliki ketajaman insting alami, dan hasilnya di atas rata-rata. |
| **Bermanfaat (*Al-Mufid*)** | Karya atau tindakannya menghasilkan solusi nyata, meringankan beban sesama, dan bernilai dakwah. |

## 3. Matriks Tafrith vs Ifrath pada Bakat Ini
* **Tafrith (Bakat Disia-siakan / Ditindas):** Gejala anak menjadi pemurung, frustrasi, atau melampiaskan energinya ke perilaku destruktif karena potensinya tidak difasilitasi.
* **Ifrath (Bakat Dibiarkan Tanpa Adab Syariat):** Bakat memimpin berubah menjadi tiran sombong; bakat bicara berubah menjadi suka berdebat dan mencela; bakat analitis berubah menjadi peragu iman.
* **Wasathiyah:** Bakat diasah optimal dan dibingkai dengan adab islami serta rasa takut kepada Allah (*khasy-yah*).

## 4. Panduan Stimulasi Berdasarkan Usia
* **Usia 0–7 Tahun (Thufulah):** Diberikan kebebasan bereksplorasi secara alami melalui permainan sensorik dan motorik.
* **Usia 7–10 Tahun (Tamyiz):** Mulai diarahkan pada pembiasaan adab penggunaan bakat dan tanggung jawab harian di rumah.
* **Usia 10–15 Tahun (Murahaqah):** Dimagangkan pada mentor profesional atau proyek nyata yang menguji kehandalan karyanya.
* **Usia 15+ Tahun (Syabab):** Dilepas mandiri untuk menghasilkan karya peradaban yang bermanfaat bagi umat.

## 5. Tautan Induk Terkait
* Kembali ke kategori induk: [[Bakat]]
* Tautan sub-bakat terkait: [[Bekerja Keras]], [[Berpikir]], [[Berperasaan]], [[Memerintah]], [[Bekerja Sama]], [[Melayani]]
```
""",

    # 14. Template Elemen Refleksi, Implementas, Risiko, dan Tautan.md
    CONTENT_DIR / "Paradigma - Implementasi PKN/Template/Template Elemen Refleksi, Implementas, Risiko, dan Tautan.md": """---
title: Template Komponen Refleksi, Implementasi & Risiko
---

# Template Komponen Refleksi Lapangan, Risiko & Tautan

Dokumen ini memuat format standar blok *callout* pendukung yang dapat disisipkan ke dalam artikel-artikel materi wiki untuk memperkaya pembahasan dengan pengalaman empiris, peringatan risiko pengasuhan, dan panduan teknis aplikatif.

---

## 1. Blok Callout Refleksi Lapangan (`[!info]`)

Gunakan blok ini untuk mendokumentasikan temuan nyata, studi kasus empiris, atau observasi perilaku anak di rumah dan sekolah:

```markdown
> [!info] Refleksi Lapangan: [Judul Fenomena Pengasuhan]
> **Kondisi Faktual yang Ditemukan:**  
> (Uraikan fenomena nyata yang kerap terjadi, misal: anak usia 8 tahun yang mendadak enggan shalat berjamaah atau anak remaja yang menarik diri dari komunikasi keluarga.)
> 
> **Akar Masalah Berdasarkan Analisis PKN:**  
> (Jelaskan penyebab di balik perilaku tersebut, misal: keringnya tangki cinta karena ayah terlalu sibuk, bentakan lisan yang melukai jiwa lawwamah, atau penegakan aturan tanpa dialog.)
> 
> **Langkah Penanganan Nabawiyah:**  
> 1. Redakan ketegangan dan pulihkan jembatan batiniah melalui [[Bahasa Hati]].
> 2. Lakukan dialog empatik dua arah tanpa menghakimi melalui [[Bahasa Lisan]].
> 3. Tinjau kembali beban harian anak agar tidak melampaui kapasitas fitrah usianya.
```

---

## 2. Blok Callout Peringatan Risiko Pengasuhan (`[!warning]`)

Gunakan blok ini untuk memberi peringatan tegas atas kesalahan fatal orang tua yang dapat merusak fitrah anak:

```markdown
> [!warning] Peringatan Risiko: Bahaya [Nama Tindakan Fatal]
> * **Bentuk Kesalahan:** Membanding-bandingkan pencapaian anak dengan saudara kandung atau teman sebayanya (*social comparison*).
> * **Dampak Terhadap Jiwa:** Menimbulkan luka pengasuhan menahun, mematikan rasa percaya diri fitrah bakat, dan menyemai benih hasad serta kedengkian antarsaudara (sebagaimana kisah saudara-saudara Nabi Yusuf AS).
> * **Pencegahan Nabawiyah:** Yakini prinsip [[Bakat]]: setiap anak diciptakan unik di atas *syakilah*-nya masing-masing. Fokuslah mengasah keunikan potensi ananda, bukan memaksakannya menjadi fotokopi orang lain.
```

---

## 3. Blok Callout Rekomendasi Solusi Praktis (`[!tip]`)

Gunakan blok ini untuk memberikan tips cepat dan ringkas yang dapat langsung dipraktikkan hari ini oleh ayah dan bunda:

```markdown
> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Luangkan waktu 15 menit sebelum tidur malam untuk memeluk anak dan menanyakan: *"Apa hal paling membahagiakan dan paling menyedihkan yang ananda alami hari ini?"*
> * **Tujuan:** Mengalirkan nutrisi ke dalam [[Tangki Cinta]] dan membuka gerbang kejujuran jiwa [[Lawwamah]] anak tanpa rasa takut disalahkan.
```

---

## 4. Format Penulisan Tautan Silang (*Wikilinks*) Dua Arah

Agar seluruh 61 halaman Wiki PKN saling terhubung dengan rapi tanpa ada halaman buntu (*orphan pages*), patuhi kaidah penulisan tautan berikut:
* Gunakan nama file persis di dalam tanda kurung siku ganda: `[[Nama Halaman]]` (contoh: `[[Thufulah]]`, `[[Bahasa Hati]]`).
* Jika ingin menampilkan teks alternatif yang lebih luwes dalam kalimat, gunakan pipa: `[[Nama Halaman|Teks Tampilan]]` (contoh: `[[Thufulah|masa kanak-kanak dini (0-7 tahun)]]`).
* Setiap artikel baru wajib menautkan minimal ke:
  1. Halaman konsep payung di atasnya (misal: sub-bakat menautkan ke [[Bakat]]).
  2. Halaman fase usia terkait (misal: [[Tamyiz]] atau [[Murahaqah]]).
  3. Halaman metode tarbiyah pendukung (misal: [[Metode Mendidik]] atau [[Bahasa Lisan]]).
"""
}

def main():
    print("Executing Sprint 3: Writing 14 comprehensive landing, navigation, and template files...")
    for file_path, content in FILES_CONTENT.items():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        clean_content = content.strip() + "\n"
        with open(file_path, "w", encoding="utf-8") as fp:
            fp.write(clean_content)
        chars = len(clean_content)
        lines = len(clean_content.splitlines())
        print(f"✅ Written: {file_path.name:<45} | {chars:6,d} chars | {lines:4d} lines")

    print("\nAll 14 Sprint 3 files successfully generated!")

if __name__ == "__main__":
    main()

---
title: "PKN Blueprint: Arsitektur Sistem Pendidikan Karakter Nabawiyah"
tags:
  - blueprint
  - arsitektur
  - sistem
  - peta-konsep
  - visualisasi
  - official-docs
description: "Master blueprint dan peta arsitektur sistem utuh Pendidikan Karakter Nabawiyah (PKN), mengintegrasikan dimensi Jiwa Pendidik, Peran Pendidik, Metode, Materi Kurikulum, hingga 4 Langkah Implementasi Lapangan."
---

# PKN Blueprint: Arsitektur Sistem Pendidikan Karakter Nabawiyah


> **Amal** (What?) ← **Ilmu** (How?) ← **Iman** (Why?)

Kerangka pendidikan karakter berbasis Nabawiyah yang mengintegrasikan
**Jiwa Pendidik → Peran Pendidik → Metode Mendidik → Materi Pendidikan → Implementasi**.

---

## Navigasi Utama

```mermaid
flowchart LR
    IMAN["Iman (Why?)"]
    ILMU["Ilmu (How?)"]
    AMAL["Amal (What?)"]

    IMAN -->|"<<"| ILMU -->|"<<"| AMAL

    JIWA["Jiwa Pendidik"]
    PERAN["Peran Pendidik"]
    METODE["Metode Mendidik"]
    MATERI["Materi Pendidikan"]
    IMPL["Implementasi"]

    JIWA -->|">>"| PERAN -->|">>"| METODE -->|">>"| MATERI -->|">>"| IMPL
```

---

## 1. Materi / Kompetensi

### 1.1 Tujuan Penciptaan Manusia

```mermaid
flowchart TD
    TPC["Tujuan Penciptaan Manusia"]

    TPC --> SHOLIH["Sholih"]
    TPC --> MUSLIH["Muslih"]

    subgraph SHOLIH_BLOCK["Sholih — Hasil Karakter"]
        SHOLIH --> S1["Iman - karakter Iman"]
        SHOLIH --> S2["Ilmu - karakter Belajar"]
        SHOLIH --> S3["Amal - karakter Bakat"]
    end

    subgraph MUSLIH_BLOCK["Muslih — Peran Sosial"]
        MUSLIH --> M1["Imunitas Sosial - 8 lebih dari 88"]
        MUSLIH --> M2["Peran / Profesi - 8 ke 88"]
        M1 --> STD["Syariat, Masyarakat Sekitar, Pribadi"]
        M2 --> STD
    end
```

### 1.2 8 Kompetensi & Standar

| Kompetensi        | Jiwa         | Standar |
|-------------------|--------------|---------|
| Aqidah            | Iman (Hijau) | Individu |
| Ibadah            | Iman (Hijau) | Individu |
| Kemandirian       | Iman (Hijau) | Kelompok |
| Inisiatif         | Ilmu (Kuning)| Kelompok |
| Ketekunan         | Ilmu (Kuning)| Kelompok |
| Keunikan          | Amal (Merah) | Personal |
| Rela Berkorban    | Amal (Merah) | Personal |
| Kebermanfaatan    | Amal (Merah) | Personal |

> **Kesadaran akhir:** LD beretika dengan target akhirat

### 1.3 Maqasid Syariah dan Materi Kurikulum

| Maqasid       | Bidang      | Kurikulum         |
|---------------|-------------|-------------------|
| Agama (Hijau) | —           | —                 |
| Jiwa (Merah)  | Kesehatan   | Jasmani / P3K     |
| Akal (Kuning) | STEM        | Sains & Teknologi |
| Kehormatan    | Adab        | Adab & Akhlak     |
| Harta (Merah) | Fiqh        | Fiqh Muamalah     |

### 1.4 Penguasaan Skill — Skala

| Sumber       | Profil Sosial             | Level Jiwa |
|--------------|---------------------------|------------|
| cukup        | Individu/Publik           | Amal       |
| cukup        | Kolaborasi                | Ilmu       |
| cukup        | Emosi/Ibadah              | Iman       |

**Legend:** Cukup = baseline | Sesuai Bakat = optimal per jiwa

---

## 2. Metode & Perkembangan

### 2.1 Paradigma — 'Fitrah' sebagai Referensi

Analogi alam: Kucing mencari susu induk dan berlatih memburu secara alami.
Serangga langsung mencari makan dan berkembang biak tanpa diajarkan.

```mermaid
flowchart TD
    SF["Sumber Fitrah"]

    SF --> JASAD["Jasad"]
    SF --> RUH["Ruh"]

    subgraph JASAD_PATH["Jalur Jasad — Hayawaniyah"]
        direction LR
        JASAD --> HAY["Hayawaniyah"]
        HAY --> AMM["Ammarah"]
        AMM --> BAKAT["Bakat"]
        BAKAT --> MUR["Murahaqah 10-Baligh"]
    end

    subgraph AKAL_PATH["Jalur Akal — Lawwamah"]
        direction LR
        BIMBANG["Kebimbangan"] --> LAW["Lawwamah"]
        LAW --> BELAJAR["Belajar"]
        BELAJAR --> TAM["Tamyiz 7-10 tahun"]
    end

    subgraph RUH_PATH["Jalur Ruh — Muthmainnah"]
        direction LR
        RUH --> RUBU["Rububiyyah"]
        RUBU --> MUT["Muthmainnah"]
        MUT --> IMAN2["Iman"]
        IMAN2 --> THU["Thufulah 0-7 Tahun"]
    end
```

### 2.2 Tabel Perkembangan 3 Fase

| Fase | Kondisi | Pondasi | Aktivitas Utama | Jika Salah | Hasil |
|------|---------|---------|-----------------|------------|-------|
| **Murahaqah** (10–Baligh) | Jasad+++ Akal+++ Ruh+++ | Khouf / Ketegasan | Ta'dib → Beramal → Proyek | Dihukum | Berguna → Bakat → Amal |
| **Tamyiz** (7–10 thn)     | Jasad+ Akal++ Ruh++     | Roja' / Harapan   | Ta'allum → Pengajaran → Trial & Error | Dilatih | Bisa → Belajar → Ilmu |
| **Thufulah** (0–7 thn)    | Jasad+ Akal+ Ruh+       | Hub / Cinta       | Tazkiyyah → Membuat Kagum → Bermain | Ditoleransi | Suka → Iman → Iman |

### 2.3 Bobot Bahasa & Bobot Kesalahan per Fase

| Fase | Bobot Bahasa | Bobot Kesalahan |
|------|-------------|-----------------|
| Murahaqah (Baligh+) | **Tangan** (aksi langsung) | Harus Benar (tanggung jawab penuh) |
| Tamyiz (10 thn)     | **Lisan** (penjelasan) | Transisi — dilatih |
| Thufulah (7 thn)    | **Hati** (rasa & cinta) | **Boleh Salah** (toleransi luas) |

---

## 3. Personal — Gaya Belajar & Fitrah Bakat

### 3.1 Gaya Belajar per Jiwa

| Jiwa | Gaya Belajar | Cara Belajar | Ide Teknik |
|------|-------------|--------------|-----------|
| Ammarah | Kinestetik | Praktek / Proyek | Bergerak, Tantangan, Kedisiplinan |
| Lawwamah | Visual | Menonton / Diskusi | Media, Struktur, Reward |
| Muthmainnah | Auditori | Bercerita | Intonasi, Kelembutan, Mirroring |

### 3.2 Fitrah Bakat & Fitnah (Bahaya)

| Jiwa | Ego | Introvert | Ekstrovert | Fitnah |
|------|-----|-----------|------------|--------|
| Ammarah | Tinggi | Bekerja keras | Memerintah | Syahwat Tahta |
| Lawwamah | Sedang | Berpikir | Bekerjasama | Syubhat Harta |
| Muthmainnah | Rendah | Berperasaan | Melayani | Syahwat Pasangan |

---

## 4. Peran Pendidik & Disiplin

### 4.1 Tingkat Kesadaran & Alat Mendidik

```mermaid
flowchart LR
    subgraph AMM_PATH["Ammarah — Bawah Sadar (Refleks)"]
        direction LR
        A1["Bawah Sadar refleks"] --> A2["Memori"]
        A2 --> A3["Riyadah"] --> A4["Beramal"]
    end

    subgraph LAW_PATH["Lawwamah — Sadar (Conscious)"]
        direction LR
        B1["Sadar conscious"] --> B2["Nalar"]
        B2 --> B3["Mawizah"] --> B4["Berilmu"]
    end

    subgraph MUT_PATH["Muthmainnah — Atas Sadar (Rasa)"]
        direction LR
        C1["Atas Sadar rasa"] --> C2["Emosi"]
        C2 --> C3["Qudwah"] --> C4["Dicintai"]
    end
```

### 4.2 Tipe Pembelajaran

#### Tidak Terencana (contoh: Sholat)

| Level | Tahap | Contoh Sholat | Kepada Orang Lain |
|-------|-------|--------------|-------------------|
| Amal | Beramal → Meniru | Membaguskan Sholat | Mengajak dalam kebaikan |
| Ilmu | Berilmu → Meniru | Inisiatif Mengikuti | Mau / Semangat menerima nasihat |
| Iman | Niat → Teladan → Kagum | Menunjukkan bagusnya sholat | Terdepan dalam kebaikan |

#### Terencana (contoh: Olahraga — Fisika Memanah)

| Level | Tahap | Contoh Memanah |
|-------|-------|----------------|
| Amal | Ujian | Membuat panah → Ujian memanah |
| Ilmu Teori | Cara memanah | Fisika: parabola, aerodinamika |
| Ilmu Praktek | Memegang → Mencoba → Membongkar panah | — |
| Iman | Inspirasi | Perang Rasul, sejarah memanah, teknologi, mentor |

### 4.3 Disiplin

| Aspek | Kondisi |
|-------|---------|
| Amal / Fisik | Mengikuti secara kondisional |
| Ilmu / Akal | Belajar ketika tidak tahu |
| Iman / Hati | Selalu dalam keadaan beriman |

### 4.4 Penyesuaian Perkembangan — Kedekatan & Peran

| Fase | Kedekatan Perempuan | Kedekatan Laki-laki | Pondasi | Peran |
|------|---------------------|---------------------|---------|-------|
| Murahaqah (10–Baligh) | Ayah | Ibu | Khouf / Ketegasan | Raja Tega |
| Tamyiz (7–10 thn) | Ibu | Ayah | Roja' / Harapan | Pengajar |
| Thufulah (0–7 thn) | Ibu (0-2) lalu Ibu & Ayah (2-7) | — | Hub / Cinta | Penyayang |

### 4.5 Personalisasi — Peran Ayah & Ibu

| Jiwa | Ego Pendidik | Membuat Kagum | Bahasa Cinta | Peran | Sifat | Jika Marah |
|------|-------------|---------------|--------------|-------|-------|-----------|
| Ammarah | Rendah | Dilayani | Pujian, Hadiah | **Ayah** → Pembersih Luka | Penyabar | Sekali marah — anak trauma |
| Lawwamah | Sedang | Diskusi (negosiasi) | Sentuhan, Kebersamaan | **Guru** | Pelaksana | — |
| Muthmainnah | Tinggi | Dimotivasi & dilindungi | Pemaafan, Pengorbanan | **Ibu** → Pelatih | Disiplin | Berkali-kali marah — anak tidak terluka |

> **Kepala Sekolah** = Konseptor (posisi strategis, bukan operasional)

---

## 5. Jiwa Pendidik & Implementasi

### 5.1 Arsitektur Tangki Cinta

```mermaid
flowchart TD
    PENDIDIK["Pendidik (sebelum baligh)"]
    ALLAH["Allah Jalla Jalaluh tidak terbatas (setelah baligh)"]
    TANK["Tangki Cinta Pendidik"]
    RECOVERY["Self Recovery: istirahat, hobi, variasi aktivitas"]
    TANK_ANAK["Tangki Cinta Anak"]

    PENDIDIK -->|"masuk"| TANK
    ALLAH -->|"masuk"| TANK
    RECOVERY -->|"masuk dari bawah"| TANK
    TANK -->|"keluar"| TANK_ANAK
```

### 5.2 Tazkiyyatun Nafs — Penyucian Jiwa Pendidik

| Jiwa | Kebutuhan | Dipenuhi Dengan | Amalan Hati | Praktik |
|------|-----------|-----------------|-------------|---------|
| Ammarah | Jasmani | Harta Halal | Khouf | Mujahadah, Riyadhah, Ibadah Sunnah |
| Lawwamah | Nalar | Menuntut Ilmu | Roja' | Belajar, Muraqabah |
| Muthmainnah | Ruhani | Muhasabah | Hub | Tadabbur, Tafakkur, Taubat, Berdoa |

> **Muara akhir:** Menikmati Ibadah

### 5.3 Implementasi — 4 Langkah Berurutan

```mermaid
flowchart TD
    START(["Mulai Implementasi PKN"])

    L1["Langkah 1: Mulai dari Diri Personal\nJiwa: Muthmainnah"]
    L2["Langkah 2: Dari yang Mudah / Tidak Ideal\nJiwa: Lawwamah — Kaizen 1persen per hari"]
    L3["Langkah 3: Utamakan Menghindari Mudharat\nJiwa: Ammarah"]
    L4["Langkah 4: Sesuaikan Ekspektasi dengan Fitrah\nJiwa: Lawwamah"]

    START --> L1 --> L2 --> L3 --> L4

    NOTE1["Praktik: pembiasaan kecil sholat tepat waktu, senyum salam sapa"]
    NOTE2["Prioritas: lindungi dari pornografi, gadget tak terbatas, bullying"]
    NOTE3["Mindset: garis finish adalah Keridhaan Allah dan keselamatan akhirat"]

    L1 -.->|"praktik"| NOTE1
    L3 -.->|"prioritas"| NOTE2
    L4 -.->|"mindset"| NOTE3
```

#### Detail 4 Langkah Implementasi

| # | Langkah | Jiwa | Prinsip Utama |
|---|---------|------|---------------|
| 1 | Mulai dari Diri Personal | Muthmainnah | Perbaiki diri sendiri dahulu sebelum mendidik |
| 2 | Dari yang Mudah / Tidak Ideal | Lawwamah | Kaizen: perbaikan 1% konsisten lebih baik dari rencana besar tanpa aksi |
| 3 | Utamakan Menghindari Mudharat | Ammarah | Dar'ul mafaasid muqaddam 'ala jalbil mashalih (mencegah kerusakan didahulukan) |
| 4 | Sesuaikan Ekspektasi dengan Fitrah | Lawwamah | Tidak membanding-bandingkan anak; setiap anak unik dengan takdirnya |

---

## Checklist Audit Implementasi PKN

- [ ] Apakah guru mengajar dengan **kasih sayang** atau paksaan amarah?
- [ ] Apakah orang tua **hadir** mengisi tangki cinta anak setiap hari minimal 15–30 menit interaksi berkualitas tanpa distraksi gadget?
- [ ] Apakah penilaian karakter sudah berbasis **observasi perilaku nyata** (bukan sekadar hafalan teori ujian tertulis)?
- [ ] Apakah fase usia anak sudah diperlakukan sesuai kaidah:
  - **0–7 th** — dimanjakan cinta
  - **7–10 th** — dilatih nalar
  - **10–Baligh** — ditegakkan tanggung jawab

---

## Ringkasan Sistem PKN

```mermaid
mindmap
  root(PKN Blueprint)
    Materi
      Tujuan Penciptaan Manusia
        Sholih
        Muslih
      8 Kompetensi
        Aqidah
        Ibadah
        Kemandirian
        Inisiatif
        Ketekunan
        Keunikan
        Rela Berkorban
        Kebermanfaatan
      Maqasid Syariah
        Agama
        Jiwa ke Kesehatan
        Akal ke STEM
        Kehormatan ke Adab
        Harta ke Fiqh
    Metode
      Fitrah Paradigma
        Jasad ke Hayawaniyah ke Ammarah
        Ruh ke Rububiyyah ke Muthmainnah
      3 Fase Perkembangan
        Thufulah 0-7
        Tamyiz 7-10
        Murahaqah 10-Baligh
    Personal
      Gaya Belajar
        Kinestetik Ammarah
        Visual Lawwamah
        Auditori Muthmainnah
      Fitrah Bakat
        Introvert vs Ekstrovert
    Peran Pendidik
      Tingkat Kesadaran
        Bawah Sadar Refleks
        Sadar Conscious
        Atas Sadar Rasa
      Personalisasi
        Ayah vs Ibu
        Kepala Sekolah
    Jiwa Pendidik
      Tangki Cinta
      Tazkiyyatun Nafs
      Implementasi 4 Langkah
```

---

## Legenda Jiwa

| Jiwa | Nama | Aspek | Domain |
|------|------|-------|--------|
| Merah | Ammarah | Fisik, Amal, Tindakan, Jasad | Ta'dib (hukum & disiplin) |
| Kuning | Lawwamah | Akal, Ilmu, Nalar, Belajar | Ta'allum (belajar & nalar) |
| Hijau | Muthmainnah | Ruh, Iman, Cinta, Ketenangan | Tazkiyyah (penyucian hati) |
| Ungu | Khusus | Peran Profesi, Tangki Cinta, Jiwa Pendidik | Implementasi |
| Biru | Sosial | Imunitas Sosial | Interaksi Kemasyarakatan |


---

## Tautan Navigasi Terkait

* [[index|Paradigma & Implementasi: Indeks Utama]]
* [[Pendidikan Ideal/Menumbuhkan Kesadaran Beramal|Menumbuhkan Kesadaran Beramal]]
* [[Insan/Tujuan Hidup Manusia|Tujuan Hidup Manusia: Sholih & Muslih]]
* [[Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN|8 Standar Implementasi PKN]]
* [[Insan/Fitrah (Karakter)/Perkembangan/Thufulah|Fase Perkembangan: Thufulah (0–7 Tahun)]]
* [[Insan/Fitrah (Karakter)/Perkembangan/Tamyiz|Fase Perkembangan: Tamyiz (7–10 Tahun)]]
* [[Insan/Fitrah (Karakter)/Perkembangan/Murahaqah|Fase Perkembangan: Murahaqah (10–Baligh)]]
* [[Insan/Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40|Panduan Asesmen dan Observasi TB40]]
* [[Insan/Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah|Kuisioner Asesmen 40 Bakat Nabawiyah]]
* [[Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda|Peran Ayah dan Bunda]]
* [[Implementasi/Internal & Eksternal/Tazkiyatun Nafs|Tazkiyatun Nafs Pendidik]]
* [[Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery|Panduan Recovery dan Penanganan Hutang Pengasuhan]]

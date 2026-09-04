# Project Handoff: Wiki PKN (Pendidikan Karakter Nabawiyah)

Dokumen ini merangkum arsitektur teknis, riwayat pengembangan, integrasi data **Tafsir Bakat 40 (TB40)**, dan panduan pemeliharaan sistem basis pengetahuan **Wiki PKN** berbasis Quartz v5.

---

## 1. Ikhtisar Proyek & Milestone Utama

Proyek ini bertujuan mempublikasikan basis pengetahuan terstruktur **Pendidikan Karakter Nabawiyah (PKN)** dari berkas ekspor Outline ke dalam platform static site generator **Quartz v5** dengan navigasi sidebar kustom yang presisi dan konten yang kaya.

### Milestone yang Telah Diselesaikan:
1. **Navigasi Kustom `OutlineNav`**: Menggantikan komponen default Quartz `Explorer` dengan plugin `./plugins/outline-nav` yang membaca hierarki `nav_structure.json`.
2. **Fitur Inside Scrolling & State Persistence**:
   - Menerapkan tata letak flexbox dan internal scrolling (`overflow-y: auto; overscroll-behavior: contain; max-height: calc(100vh - 12rem);`) dengan scrollbar ramping.
   - Deteksi tautan aktif (`a.internal.active`) dengan pembukaan otomatis folder induk (*auto-expand parent*).
   - Pemeliharaan posisi scroll antar-halaman (*PJAX*) melalui `sessionStorage` (`outlineNavScrollTop`).
   - Pengingat status lipatan (*collapse/expand*) per folder melalui `localStorage`.
3. **Konfigurasi Resmi Quartz**: Membuat `quartz.config.yaml` dengan `pageTitle: "Wiki PKN"`, `locale: "id-ID"`, dan penonaktifan total `@quartz-community/explorer`.
4. **Pengayaan Konten Otentik (39 Berkas)**: Mentransformasi 39 berkas kerangka kosong di `content/` menjadi naskah komprehensif berbasis data `old_backup/random/`.
5. **100% Resolusi Tautan Navigasi (49 Simpul)**: Seluruh 49 simpul pada `nav_structure.json` memiliki berkas `.md` fisik yang valid (0 *unlinked leaf labels*).
6. **Ekstraksi Data TB40**: Memetakan struktur lengkap taksonomi **Tafsir Bakat 40 (TB40)** dari repositori API observasi karakter (`/home/deck/Projects/observasi-karakter-api/api-tb40-explore/api/`).
7. **Penerbitan Bank Studi Kasus Kurikulum Berbasis Peristiwa**: Menyusun dan merapikan naskah panduan restorasi karakter dengan metode 4-langkah (Tangki Cinta → Bahasa Hati → Bahasa Lisan → Bahasa Tangan) di `content/.../Pendidikan Ideal/Bank Studi Kasus.md`.
8. **Integrasi Basis Data Video Ceramah PKN (`pkn.db`)**: Mengintegrasikan repositori `sqlite-vector-video-db` (122 video ceramah Ustadz Abdul Kholiq, 1.159 bab terindeks dengan timestamp YouTube) ke dalam `old_backup/`, menghasilkan halaman `content/.../Referensi Kajian Video.md`, serta menyediakan skrip utilitas pencarian CLI `scripts/search_pkn_video.py`.
9. **Pengarsipan 117 Artikel SOTAB HEBAT (`old_backup/sotabh/`)**: Mengunduh dan mengonversi seluruh 117 artikel dari situs resmi `sotabh.com/artikel/` ke format Markdown lengkap dengan metadata frontmatter, indeks master kronologis (`old_backup/sotabh/README.md`), basis data terstruktur mentah (`articles.json`), serta skrip sinkronisasi otomatis `scripts/fetch_sotabh_articles.py`.
10. **Ekspansi Konten Berbasis Video Ceramah & Artikel SOTAB**: Memperluas secara mendalam halaman-halaman kunci wiki (`SOTABH.md`, `Luka dan Hutang Pengasuhan.md`, `Recovery.md`, `Peran Ayah dan Bunda.md`, `Perkembangan.md`, `Pembelajaran Alamiah.md`, `Bakat.md`) dengan mengintegrasikan konsep-konsep emas seperti *Pesantren sebagai SMK Jurusan Agama*, *Kemunduran 3 Tahun Anak Modern*, *Protokol 9 Tahap Menghapus Noda Hati*, *Satu Anak Satu Kurikulum*, *Prinsip Naik Turun Gas*, dan rujukan video YouTube terverifikasi.
11. **Audit Menyeluruh Kematangan 61 Berkas Konten**: Melakukan audit lengkap terhadap seluruh 61 berkas Markdown di `content/`, mengklasifikasikan ke dalam 5 kategori kematangan (5 berkas landing node kosong, 3 berkas template acuan, 21 berkas ringkas/draft, 17 berkas sedang, dan 15 berkas mendalam/komprehensif) serta merumuskan panduan prompt pengayaan konten pada `CONTENT_ANALYSIS.md`.
12. **Validasi & Verifikasi Penuh Quartz v5**: Memastikan seluruh 61 berkas Markdown lolos verifikasi sintaks dan tautan dengan hasil kompilasi bersih (`npx quartz build` sukses menghasilkan 272 berkas web ke `public/`).

---

## 2. Arsitektur Data TB40 (Tafsir Bakat 40)

Data model TB40 diekstraksi dari spesifikasi OpenAPI dan berkas kalkulasi engine di `/home/deck/Projects/observasi-karakter-api/api-tb40-explore/api/` (`v0.1/tb40/calculation.json` dan `v0.3/tb40/result.json`). Sistem ini memiliki hierarki bertingkat 5 level:

```mermaid
graph TD
    L2["Level 2: 2 Kutub Sosial (Sirr & 'Alaniyah)"] --> L6
    L3["Level 3: 3 Dimensi Jiwa (Karsa, Cipta, Rasa)"] --> L6
    L6["Level 6: 6 Kategori Bakat Utama"] --> L18["Level 18: 18 Sub-Kelompok Bakat"]
    L18 --> L40["Level 40: 40 Pilar Karakter Nabawiyah"]
```

### A. Level 2 — Kutub Sosial (Energi Interaksi)
* **1. Introvert (*As-Sirr*):** Energi batin, fokus ke dalam, tidak mengutamakan keramaian.
* **2. Extrovert (*Al-'Alaniyah*):** Energi luar, ekspresif, senang berinteraksi sosial.

### B. Level 3 — Dimensi Kemanusiaan & Trilogi Jiwa
1. **Karsa (*Al-Hawa* / Jiwa Ammarah):**
   - Karakteristik: Bergerak, bersemangat, dorongan fisik.
   - Gaya Belajar: **Al-Fuad / Kinestetik** (bergerak, menyentuh, praktik lapangan).
   - Bahasa Hati Utama: **Bahasa Pelayanan (*Acts of Service*)**.
2. **Cipta (*Al-'Aql* / Jiwa Lawwamah):**
   - Karakteristik: Berpikir, nalar evaluatif, menimbang baik-buruk.
   - Gaya Belajar: **Al-Bashar / Visual** (membaca, melihat bagan/diagram, ruangan terang).
   - Bahasa Hati Utama: **Bahasa Kebersamaan (*Quality Time*)**.
3. **Rasa (*Al-Qalb* / Jiwa Muthmainnah):**
   - Karakteristik: Berperasaan, kepekaan nurani, spiritualitas batin.
   - Gaya Belajar: **As-Sam'u / Auditori** (mendengarkan nasihat, berdiskusi, suasana hening).
   - Bahasa Hati Utama: **Bahasa Perlindungan / Hadiah (*Receiving Gifts / Protection*)**.

### C. Level 6 — Matriks 6 Kategori Bakat Utama
Persilangan antara Level 2 (Kutub Sosial) dan Level 3 (Dimensi Jiwa) menghasilkan 6 kategori bakat pokok:
1. **Bekerja Keras (الحَمَاسَة - *Al-Hamasah*):** Introvert + Karsa (Ammarah)
2. **Berpikir / Cerdas (التَّفْكِيْر - *At-Tafkir*):** Introvert + Cipta (Lawwamah)
3. **Berperasaan (الشُعُوْر - *Asy-Syu'ur*):** Introvert + Rasa (Muthmainnah)
4. **Mempengaruhi / Memerintah (التَّأْثِيْر - *At-Ta'tsir*):** Extrovert + Karsa (Ammarah)
5. **Bekerjasama (التَّعَامُل - *At-Ta'amul*):** Extrovert + Cipta (Lawwamah)
6. **Melayani (الخِدْمَة - *Al-Khidmah*):** Extrovert + Rasa (Muthmainnah)

### D. Level 18 — 18 Sub-Kelompok Bakat
* **Bekerja Keras:** Berambisi, Berwibawa, Giat bekerja.
* **Berpikir:** Suka berpikir imajinatif, Suka berpikir positif, Suka berpikir analitis.
* **Berperasaan:** Suka apa adanya, Pendiam, Suka merendah.
* **Mempengaruhi:** Suka menguasai, Suka memotivasi, Suka menolong.
* **Bekerjasama:** Suka menggunakan hubungan yang ada, Suka membuat hubungan baru, Suka mengeratkan hubungan yang ada.
* **Melayani:** Suka melayani dengan cara memberi, Suka melayani dengan cara menjaga, Suka melayani dengan cara mengalah.

### E. Level 40 — 40 Pilar Karakter Nabawiyah
Daftar lengkap 40 pilar dengan nama Arab, nomor urut, dan garis silsilahnya:
* **Grup Bekerja Keras (1-6):** #1 *Himmah* (الهِمَّة), #2 *Ihsaan* (الاِحْسَان), #3 *‘Izzah* (العِزَّة), #4 *Waqaar* (الوَقَار), #5 *‘Aziimah* (العَزِيمَة), #6 *Nasyaath* (النَّشَاط).
* **Grup Berpikir (7-11):** #7 *Firaasah* (الفِرَاسَة), #8 *Nubl* (النُّبْل), #9 *Husnuzhan* (حُسْنُ الظَّن), #10 *Dzakaa’* (الذَّكَاء), #11 *Hikmah* (الحِكْمَة).
* **Grup Berperasaan (12-17):** #12 *Shidq* (الصِّدْق), #13 *‘Iffah* (العِفَّة), #14 *Shamt* (الصَّمْت), #15 *Hayaa’* (الحَيَاء), #16 *Qanaa'ah* (القَنَاعَة), #17 *Tawaadhu'* (التَّوَاضُع).
* **Grup Mempengaruhi (18-24):** #18 *Syajaa’ah* (الشَّجَاعَة), #19 *Ghairah* (الغَيْرَة), #20 *Munaafasah* (المُنَافَسَة), #21 *Nashiihah* (النَّصِيْحَة), #22 *Fashaahah* (الفَصَاحَة), #23 *Nushrah* (النُّصْرَة), #24 *Juud* (الجُوْد).
* **Grup Bekerjasama (25-32):** #25 *Ta'aawun* (التَّعَاوُن), #26 *Ulfah* (الاُلْفَة), #27 *‘Adaalah* (العَدَالَة), #28 *Wafaa'* (الوَفَاء), #29 *Muzaah* (المُزَاح), #30 *Basyaasyah* (البَشَاشَة), #31 *Rifq* (الرِّفْق), #32 *Mahabbah* (المَحَبَّة).
* **Grup Melayani (33-40):** #33 *Rahmah* (الرَّحْمَة), #34 *Itsaar* (الاِيْثَار), #35 *Kitmaanus sirr* (كِتْمَانُ السِّرِّ), #36 *Satr* (السَّتْر), #37 *Amaanah* (الاَمَانَة), #38 *Anaah* (الاَنَاة), #39 *Hilm* (الحِلْم), #40 *Shabr* (الصَّبْر).

### F. Matriks Kondisi Ekstrim (*Tafrith* vs *Ifrath*) & Solusi Kuratif
Setiap sifat mulia berada di antara dua jurang ekstrem (*tafrith* / lalai dan *ifrath* / berlebih):
* **Bekerja Keras:**
  - *Lalai:* **Kasal (Malas)** $\rightarrow$ Solusi: Kuatkan *‘Aziimah* dan *Amaanah*.
  - *Lebih:* **Thama' (Serakah/Ambisi Buta)** $\rightarrow$ Solusi: Kuatkan *Qanaa'ah* dan *Tawaadhu'*.
* **Berpikir:**
  - *Lalai:* **Jahl (Kebodohan / Abaikan Nalar)** $\rightarrow$ Solusi: Kuatkan *Dzakaa'* dan *Hikmah*.
  - *Lebih:* **Ahlu Ra'yi (Pemuja Akal / Rasionalisme Kering)** $\rightarrow$ Solusi: Kuatkan *Hikmah*, *Tawaadhu'*, dan *Hayaa'*.
* **Berperasaan:**
  - *Lalai:* **Kibr / Kasar** $\rightarrow$ Solusi: Kuatkan kepekaan hati dan *Tawaadhu'*.
  - *Lebih:* **Minder (Rendah Diri) & Hazan (Sedih Berlarut)** $\rightarrow$ Solusi: Kuatkan *Syajaa'ah*, *Ghairah*, dan *Nasyaath*.
* **Mempengaruhi:**
  - *Lalai:* **Jubn (Penakut)** $\rightarrow$ Solusi: Kuatkan *Syajaa'ah*, *Ghairah*, dan *Munaafasah*.
  - *Lebih:* **Tahawwur (Ceroboh / Otoriter)** $\rightarrow$ Solusi: Kuatkan *Shabr*, *Hilm*, dan *Anaah*.
* **Bekerjasama:**
  - *Lalai:* **‘Udwaan (Bermusuhan / Menutup Diri)** $\rightarrow$ Solusi: Kuatkan *Ta'aawun*, *Ulfah*, dan *‘Adaalah*.
  - *Lebih:* **Dzull / Bimbang Mengambil Keputusan** $\rightarrow$ Solusi: Kuatkan *Syajaa'ah* dan *Ghairah*.
* **Melayani:**
  - *Lalai:* **Ghilzhah (Kasar / Tidak Peduli)** $\rightarrow$ Solusi: Kuatkan *Rahmah*, *Itsaar*, dan *Hilm*.
  - *Lebih:* **Taqliid (Kepatuhan Buta) / Takut Berlebih** $\rightarrow$ Solusi: Kuatkan *‘Izzah* dan *Waqaar*.

### G. Spesifikasi Teknis Engine API TB40
Sumber data berada di `/home/deck/Projects/observasi-karakter-api/api-tb40-explore/api/`:
* **Struktur Versi:**
  - `v0.1`: Single-pass calculation engine (`calculation.json`), generator pelaporan visual (`tb40.svg`, `tb40byRank.svg`), dan kuesioner flat 40 butir pertanyaan (`questions.json`).
  - `v0.2`: Pengenalan segmentasi pertanyaan bertingkat (*tiered questionnaire*).
  - `v0.3`: OpenAPI 3.0 penuh (`swagger.yaml`) dengan alur **Asesmen Adaptif 4-Tier**:
    - **Tier 1 (Energi Sosial - 1Q):** Menentukan Kutub Introvert vs Extrovert.
    - **Tier 2 (Orientasi Jiwa - 1Q):** Menentukan Trilogi Jiwa (Karsa / Cipta / Rasa) $\rightarrow$ menghasilkan kluster Level 6.
    - **Tier 3 (Pendalaman 18 Sub-Kelompok - 18Q):** Memetakan kekuatan spesifik pada 18 sub-kelompok.
    - **Tier 4 (Presisi 40 Pilar - 40Q):** Pengukuran mendalam terhadap seluruh 40 pilar karakter nabawiyah.
  - **Dua Varian Instrumen:**
    - `tb40Dewasa`: Kuesioner refleksi diri mandiri (40 butir pertanyaan terstandar).
    - `tb40Anak`: Kuesioner observasi anak berbasis studi kasus aktivitas bermain dan keseharian (bahasa ramah anak / observasi orang tua).
  - **Fitur API v0.3:** *Continuous scoring*, *Halfway reporting* (laporan parsial saat baru menyelesaikan Tier 2/3), integrasi peringatan dini (*ego warning*, *lalai warnings*, *lebih warnings*), serta rekomendasi profil karir (`recommended_profesi`) dan rumpun ilmu (`recommended_jurusan`).

---

## 3. Struktur Berkas & Komponen Utama

```
wiki-pkn/
├── content/                                # Naskah Markdown (61 berkas halaman wiki)
│   ├── index.md                            # Beranda Wiki PKN
│   ├── Renungan/                           # Catatan renungan orang tua
│   └── Paradigma - Implementasi PKN/       # Konten utama kurikulum PKN
│       └── Dokumen Pendidikan Karakter Nabawiyah/
│           ├── FAQ Ringkas.md
│           ├── Referensi Kajian Video.md   # Indeks master video ceramah Ustadz Abdul Kholiq
│           └── Paradigma & Implementasi/
│               ├── Insan/                  # Jiwa, Fitrah, 6 Bakat, 4 Fase Usia
│               ├── Pendidikan Ideal/       # Metode Mendidik, 3 Bahasa, Bank Studi Kasus, Pemulihan
│               └── Implementasi/           # Kaidah, Elemen, Peran Ayah/Bunda/Guru
├── old_backup/                             # Sumber data & arsip referensi
│   ├── random/                             # Naskah mentah ekspor Outline & Bank Studi Kasus
│   ├── sotabh/                             # 117 naskah artikel SOTAB HEBAT + articles.json
│   └── sqlite-vector-video-db/             # Basis data pkn.db (122 video, 1.159 bab)
├── plugins/
│   └── outline-nav/                        # Plugin Quartz untuk Navigasi Outline
│       ├── package.json
│       ├── tsup.config.ts
│       └── src/components/OutlineNav.tsx   # Komponen utama sidebar & script
├── scripts/
│   ├── fetch_sotabh_articles.py            # Skrip sinkronisasi 117 artikel SOTAB
│   ├── generate_video_reference.py         # Skrip pembuatan halaman Referensi Kajian Video
│   ├── search_pkn_video.py                 # Utilitas CLI pencarian timestamp video pkn.db
│   └── migration/                          # Skrip migrasi dan pengayaan arsip
├── nav_structure.json                      # Sumber kebenaran struktur navigasi (49 simpul)
├── quartz.config.yaml                      # Konfigurasi aktif Quartz v5
├── CONTENT_ANALYSIS.md                     # Analisis celah konten, master TB40 & audit 61 berkas
└── HANDOFF.md                              # Dokumen serah terima ini
```

---

## 4. Alur Kerja Pengembangan (Workflow)

### Mengedit Plugin `OutlineNav`:
1. Ubah berkas `plugins/outline-nav/src/components/OutlineNav.tsx`.
2. Kompilasi ulang plugin:
   ```bash
   cd plugins/outline-nav
   npm run build
   cd ../..
   ```
3. Restart server Quartz jika sedang berjalan:
   ```bash
   npx quartz build --serve --port 8888
   ```

### Menambahkan atau Mengubah Konten:
1. Pastikan setiap berkas `.md` memiliki metadata `title` pada frontmatter:
   ```yaml
   ---
   title: "Judul Halaman"
   ---
   ```
2. Jika ingin halaman tersebut muncul di sidebar navigasi, daftarkan judulnya ke dalam `nav_structure.json`.

---

## 5. Rencana Pengembangan Selanjutnya (Next Steps)

1. **Pengayaan 21 Berkas Ringkas (Kategori 3) & 5 Landing Node (Kategori 1)**:
   - Manfaatkan skrip `python3 scripts/search_pkn_video.py "<keyword>"` dan arsip artikel di `old_backup/sotabh/`.
   - Prioritaskan pengayaan 6 sub-bakat (`Bekerja Sama.md`, `Melayani.md`, `Berpikir.md`, `Berperasaan.md`, `Memerintah.md`, `Bekerja Keras.md`) dengan memasukkan matriks pilar TB40.
   - Perkaya metode 3 bahasa dan kaidah implementasi dengan studi kasus praktis.
2. **Pembuatan Halaman Profil 40 Pilar**:
   - Mengembangkan sub-direktori `Pilar Karakter/` di dalam `content/.../Insan/` untuk mendokumentasikan ke-40 pilar secara individual berdasarkan taksonomi TB40.
3. **Templat Piagam Akil Baligh & Lembar Observasi Bakat**:
   - Menyediakan berkas instrumen siap unduh/cetak untuk perjanjian kemandirian ananda pasca-baligh dan lembar pengamatan rukun 3A (Suka, Bisa, Berguna).
4. **Diagram Visual & Infografis**:
   - Mengintegrasikan visualisasi `tb40.svg` atau diagram Mermaid interaktif ke halaman payung (*Insan*, *Bakat*, *Pendidikan Ideal*).


---
title: Pengembangan Software dan Ekosistem Digital PKN
description: "Katalog komprehensif arsitektur teknologi, repositori open source, dan peta pengembangan aktif ekosistem perangkat lunak Manhaj Pendidikan Karakter Nabawiyah (TB40, OpenBayan, Rapor Karakter, Mading Digital, dan Quran Sekejap)."
aliases:
  - Pengembangan Software PKN
  - Ekosistem Software PKN
  - Software PKN
  - Teknologi dan Software PKN
  - Ekosistem Digital PKN
  - Edutech PKN
tags:
  - referensi
  - software
  - open-source
  - teknologi
  - github
  - tb40
  - openbayan
  - edutech
---

![[assets/banners/banner_blueprint_arsitektur.webp]]
*Gambar: Arsitektur Rekayasa Perangkat Lunak dan Ekosistem Digital Manhaj Pendidikan Karakter Nabawiyah*

# Pengembangan Software dan Ekosistem Digital PKN

> [!note] Catatan Metodologi & Sumber Penyusunan Dokumen
> Dokumen ini disusun sebagai dokumentasi resmi pemetaan arsitektur teknologi, repositori kode sumber terbuka (*open-source*), dan sistem perangkat lunak yang dikembangkan secara aktif dalam ekosistem **Yayasan Bina Insan Mustaqbal** ([github.com/Yayasan-Bina-Insan-Mustaqbal](https://github.com/Yayasan-Bina-Insan-Mustaqbal)) dan portofolio rekayasa pengembang utama manhaj, **Harridi Ilman Tovid (decaller)** ([github.com/decaller](https://github.com/decaller)).
> 
> Naskah ini menguraikan integrasi antara prinsip tarbiyah fitrah nabawiyah dengan teknologi modern mutakhir: *Knowledge Graph* korpus hadits klasik, asesmen bakat digital (TB-40), pelaporan rapor karakter berbasis kualitatif, majalah dinding digital santri, hingga infrastruktur GitOps otomatis.

---

> [!quote] Dalil & Pijakan Syariat: Teknologi Sebagai Wasilah Khidmah Peradaban
> **Teks Al-Qur'an:**  
> « وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ وَمَنَافِعُ لِلنَّاسِ وَلِيَعْلَمَ اللَّهُ مَن يَنصُرُهُ وَرُسُلَهُ بِالْغَيْبِ ۚ إِنَّ اللَّهَ قَوِيٌّ عَزِيزٌ »
> 
> *"Dan Kami ciptakan besi yang padanya terdapat kekuatan yang hebat dan berbagai manfaat bagi manusia, (supaya mereka mempergunakan besi itu) dan supaya Allah mengetahui siapa yang menolong (agama)-Nya dan rasul-rasul-Nya padahal Allah tidak dilihatnya. Sesungguhnya Allah Maha Kuat lagi Maha Perkasa."*  
> — **QS. Al-Hadid: 25**
> 
> **Atsar & Kaidah Hikmah:**  
> « الْكَلِمَةُ الْحِكْمَةُ ضَالَّةُ الْمُؤْمِنِ، فَحَيْثُ وَجَدَهَا فَهُوَ أَحَقُّ بِهَا »  
> *"Kalimat hikmah (ilmu dan teknologi yang bermanfaat) adalah barang hilang milik orang mukmin. Di mana pun ia menemukannya, maka dialah yang paling berhak mengambilnya."*  
> — **HR. Tirmidzi (No. 2687) & Ibnu Majah (No. 4169)**
> 
> 💡 **Relevansi Manhaj:** Dalam paradigma PKN, perangkat lunak (*software*) bukanlah berhala modern yang diagungkan tanpa adab, melainkan instrumen khidmah (*wasilah peradaban*) untuk mempermudah umat mendalami Al-Qur'an, mengenali potensi fitrah bakat unik, mengelola madrasah berbasis adab, dan mendistribusikan ilmu secara adil tanpa komersialisasi berlebihan.
> 🔍 **Telusuri di OpenBayan:** [🔍 Telusuri di OpenBayan ↗](https://openbayan.insanmustaqbal.or.id/search?q=%D9%88%D9%8E%D8%A3%D9%8E%D9%86%D8%B2%D9%8E%D9%84%D9%92%D9%86%D9%8E%D8%A7%20%D8%A7%D9%84%D9%92%D8%AD%D9%8E%D8%AF%D9%90%D9%8A%D8%AF%D9%8E%20%D9%81%D9%90%D9%8A%D9%87%D9%90%20%D8%A8%D9%8E%D8%A3%D9%92%D8%B3%D9%8C%20%D8%B4%D9%8E%D8%AF%D9%90%D9%8A%D8%AF%D9%8C%20%D9%88%D9%8E%D9%85%D9%8E%D9%86%D9%8E%D8%A7%D9%81%D9%90%D8%B9%D9%8F%20%D9%84%D9%90%D9%84%D9%86%D9%8E%D9%91%D8%A7%D8%B3%D9%90%20%D9%88%D9%8E%D9%84%D9%90%D9%8A%D9%8E%D8%B9%D9%92%D9%84%D9%8E%D9%85%D9%8E&lang=id)

---

## 1. Visi Digitalisasi Berbingkai Fitrah

Banyak institusi pendidikan modern terjebak dalam dua kutub ekstrem terkait teknologi:
1. **Teknofobia / Luddite Extreem:** Mengharamkan atau memusuhi teknologi sama sekali, sehingga anak-anak gagap peradaban saat berhadapan dengan dunia nyata.
2. **Teknokrasi Sekuler / Screen Addiction:** Menyerahkan anak sepenuhnya kepada gawai (*gadget*), aplikasi komersial candu, dan algoritma media sosial yang merusak konsentrasi, merampas jam tidur, dan melukai fitrah interaksi fisik.

Manhaj PKN mengambil jalan tengah kenabian (**Al-Wasathiyah**): **Menundukkan teknologi di bawah bimbingan wahyu dan kematangan akil baligh**. Ekosistem software PKN dirancang dengan kriteria etis yang ketat:
* **Bebas Distraksi & Iklan Riba/Maksiat:** Tidak ada iklan pihak ketiga yang mengeksploitasi privasi santri.
* **Open Source & Berdaulat:** Kode sumber transparan, dapat diaudit komunitas, dan mandiri tanpa ketergantungan pada vendor asing tertutup.
* **Fungsional & Humanis:** Membantu mempermudah interaksi *Bahasa Hati* dan *Bahasa Lisan* antar-manusia, bukan menggantikan kehadiran figur pendidik.

```
                           ┌────────────────────────────────────────────────────────┐
                           │      ARSITEKTUR EKOSISTEM DIGITAL MANHAJ PKN           │
                           └────────────────────────────────────────────────────────┘
                                                       │
        ┌───────────────────────────┬──────────────────┴─────────────────┬───────────────────────────┐
        ▼                           ▼                                    ▼                           ▼
┌──────────────────┐       ┌──────────────────┐                 ┌──────────────────┐        ┌──────────────────┐
│ KORPUS & RISET   │       │  ASESMEN BAKAT   │                 │ EDUTECH SEKOLAH  │        │ MEDIA INTERAKTIF │
│   OPENBAYAN      │       │     (TB-40)      │                 │  RAPOR KARAKTER  │        │ QURAN & DISPLAY  │
├──────────────────┤       ├──────────────────┤                 ├──────────────────┤        ├──────────────────┤
│• OpenBayan Core  │       │• tafsirbakat.com │                 │• rapor-karakter  │        │• mading-digital  │
│• OpenBayanNext   │       │• tb40-fe (App)   │                 │• rapor-sd-drive  │        │• modulSekejap    │
│• Hadith-Data-Sets│       │• tb40-analytics  │                 │• observasi-api   │        │• cursorQuran     │
│• PKN-videoDB     │       │• api-tb40-explore│                 │• surveyReportPKN │        │• Dzikr-Dua App   │
│• Vector Search   │       │• pub.insantaqwa  │                 │• hermesDIL       │        │• factory-blockly │
└──────────────────┘       └──────────────────┘                 └──────────────────┘        └──────────────────┘
```

---

## 2. Kluster 1: Mesin Korpus Hadits, Dalil & AI Knowledge Graph

Fondasi seluruh modul kurikulum PKN berdiri di atas otentisitas dalil Al-Qur'an dan Sunnah. Kluster ini mengembangkan infrastruktur data berskala besar untuk pencarian semantik dan verifikasi sanad:

### A. OpenBayan: The Islamic Knowledge Graph
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/OpenBayan](https://github.com/Yayasan-Bina-Insan-Mustaqbal/OpenBayan)
* **Kategori:** *Knowledge Graph & Multi-Model Classical Search Engine*
* **Teknologi:** Python, FastAPI, Graph Database, HTML/CSS
* **Ruang Lingkup & Kemampuan:**
  * Membangun jejaring graf pengetahuan Islam (*Islamic Knowledge Graph*) yang menghubungkan ayat Al-Qur'an dengan hadits nabawiyah dan kitab syarah klasik.
  * **Cakupan Data Aktif:**
    * **Korpus Al-Qur'an:** 6.236 Ayat teks rasm Utsmani lengkap beserta tafsir mu'tabar (Ibnu Katsir, Ath-Thabari, Al-Qurthubi).
    * **Koleksi Hadits:** Lebih dari 88.690 matan hadits dari Kutubus Sittah dan Kutubut Tis'ah yang telah diperkaya takhrij derajat sanad.
    * **Kitab Turats:** Penyerapan (*ingestion*) ribuan kitab literatur Maktabah Syamilah ke dalam kluster data semantik.

### B. OpenBayanNext: Generasi Penerus Pencarian Semantik
* **Repositori:** [decaller/OpenBayanNext](https://github.com/decaller/OpenBayanNext)
* **Kategori:** *High-Throughput Classical Arabic Information Retrieval (IR)*
* **Teknologi:** Python, Vector Embeddings, LLM Orchestration, Classical Arabic NLP
* **Keunggulan:** Dirancang khusus untuk memproses bahasa Arab klasik tingkat tinggi, menelusuri leksikon akar kata (*isytiqaq*), mencari sinonim makna ruhani, dan menyintesis tema tarbiyah secara otomatis bagi para peneliti dakwah.

### C. Hadith-Data-Sets: Pangkalan Data Hadits 9 Kitab
* **Repositori:** [decaller/Hadith-Data-Sets](https://github.com/decaller/Hadith-Data-Sets)
* **Kategori:** *Open Corpus Dataset*
* **Isi:** Koleksi komprehensif **62.169 Hadits** dari sembilan kitab induk (*Kutubut Tis'ah*) dalam dua varian: dengan tanda baca lengkap (*tashkil*) dan teks gundul untuk efisiensi indexing NLP.

### D. PKN-videoDB & SQLite Vector Search
* **Repositori:** [decaller/PKN-videoDB](https://github.com/decaller/PKN-videoDB) • [decaller/sqlite-vector-video-db](https://github.com/decaller/sqlite-vector-video-db)
* **Kategori:** *Video Caption Pipeline & Vector Database*
* **Teknologi:** Turso SQLite, Vector Search, GitHub Pages, YouTube Transcript API
* **Fungsi:** Mengotomatiskan transkripsi dan ekstraksi teks dari ratusan jam rekaman kajian parenting Ustadz Abdul Kholiq di YouTube, memungkinkannya dicari per detik pembahasan (*deep video search*).

---

## 3. Kluster 2: Ekosistem Digital Asesmen Bakat (TB-40 Ecosystem)

Untuk mendukung implementasi **Tafsir Bakat 40 (TB-40)** di sekolah, pesantren, dan keluarga, dikembangkan rangkaian aplikasi terintegrasi:

### A. Portal Tes Online Resmi: TafsirBakat.com
* **Alamat Web Publik:** [https://tafsirbakat.com/](https://tafsirbakat.com/)
* **Deskripsi:** Portal pengujian online mandiri 40 pilar bakat nabawiyah resmi. Membimbing pengguna mengisi kuisioner 40 butir pernyataan terstandarisasi skala Likert dan menerbitkan laporan pemetaan 6 rumpun bakat secara instan.

### B. TB40 Front-End (Next-Gen Web App)
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/tb40-fe](https://github.com/Yayasan-Bina-Insan-Mustaqbal/tb40-fe)
* **Alamat Deployment (Tahap Pengembangan):** [https://tb40.insanmustaqbal.or.id/](https://tb40.insanmustaqbal.or.id/)
* **Teknologi:** TanStack Start (SSR), React, TypeScript, TailwindCSS, shadcn/ui
* **Fitur Utama:** Antarmuka responsif ultra-ringan, transisi halus, pengalaman pengguna modern, dan dukungan pengisian asesmen berbasis multi-perangkat.

### C. TB40 Analytics API
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/tb40-analytics-api](https://github.com/Yayasan-Bina-Insan-Mustaqbal/tb40-analytics-api)
* **Kategori:** *Backend Analytics Server*
* **Teknologi:** Node.js, Express, SQLite, RESTful API
* **Kapabilitas:**
  * Penyimpanan jawaban santri secara *auto-save* tanpa risiko kehilangan data di tengah pengisian.
  * Mesin kalkulasi bobot skor 40 pilar dan 6 rumpun (*Bekerja Keras, Berpikir, Berperasaan, Memerintah, Bekerja Sama, Melayani*).
  * Penyediaan endpoint analitik untuk dashboard sekolah dan komite pendidikan.

### D. API TB40 Explore & Peta Bakat Visual
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/api-tb40-explore](https://github.com/Yayasan-Bina-Insan-Mustaqbal/api-tb40-explore) • [decaller/pub.insantaqwa.org](https://github.com/decaller/pub.insantaqwa.org)
* **Alamat Web Visual:** [https://pub.insantaqwa.org/bakat/](https://pub.insantaqwa.org/bakat/)
* **Fungsi:** Menyajikan visualisasi graf jejaring sifat insan, memudahkan pendidik memahami pasangan pengimbang pilar bakat serta arketipe sahabat Nabi ﷺ.

---

## 4. Kluster 3: Sistem Rapor Karakter, Observasi & Manajemen Lembaga

Penilaian dalam Manhaj PKN menolak perankingan numerik yang menzholimi potensi unik anak. Oleh karena itu, dibangun perangkat lunak khusus untuk evaluasi naratif berbasis adab:

### A. Rapor Karakter (Builder & Runner Monorepo)
* **Repositori:** [decaller/rapor-karakter](https://github.com/decaller/rapor-karakter)
* **Teknologi:** TypeScript, Vue/React, SurveyJS, TailwindCSS
* **Struktur Arsitektur:**
  1. `builder/`: Panel administrasi guru untuk merancang formulir observasi adab dan templat cetak rapor kualitatif secara *drag-and-drop*.
  2. `runner/`: Antarmuka santri dan wali murid untuk mengisi refleksi diri, mencatat capaian amal harian, dan melihat visualisasi pertumbuhan karakter.

### B. Rapor SD Google Drive Aggregator
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/rapor-sd-frontend-backend](https://github.com/Yayasan-Bina-Insan-Mustaqbal/rapor-sd-frontend-backend)
* **Teknologi:** JavaScript, SQLite, Caddy Web Server, Google Drive API, LibreOffice/ODS Backup
* **Fungsi:** Mengagregasi ratusan lembar kerja Google Sheets guru kelas secara otomatis, menyimpannya ke basis data lokal terenkripsi, membackup ke format open-standard `.ods`, dan menampilkannya dalam portal web terpadu bagi orang tua.

### C. Observasi Karakter API & Survey Report PKN
* **Repositori:** [decaller/observasi-karakter-api](https://github.com/decaller/observasi-karakter-api) • [Yayasan-Bina-Insan-Mustaqbal/surveyReportPKN](https://github.com/Yayasan-Bina-Insan-Mustaqbal/surveyReportPKN)
* **Teknologi:** Node.js, Python Data Analytics
* **Tujuan:** API pencatatan mutaba'ah harian adab shalat, ketertiban, dan kemandirian santri yang menghasilkan laporan berkala bagi wali murid tanpa stigma angka rapor merah.

### D. HermesDIL: Kolaborasi Dokumen Lembaga
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/hermesDIL](https://github.com/Yayasan-Bina-Insan-Mustaqbal/hermesDIL) • [decaller/hermes-collabora-extension](https://github.com/decaller/hermes-collabora-extension)
* **Teknologi:** Collabora Online Integration, JavaScript
* **Fungsi:** Sistem tata persuratan dan penyusunan modul kurikulum internal yayasan berbasis dokumen open source mandiri tanpa ketergantungan Google Workspace/Microsoft 365.

---

## 5. Kluster 4: Media Display Santri, Edukasi Quran & Mobile Apps

### A. Mading Digital: Smart TV Digital Signage System
* **Repositori:** [decaller/mading-digital](https://github.com/decaller/mading-digital)
* **Teknologi:** TanStack Start, TanStack Router, React, TypeScript, Shadcn UI
* **Sasaran Perangkat:** Smart TV Android / Google TV di koridor sekolah dan masjid pesantren.
* **Keunggulan Teknis:**
  * **Zero-Stutter Pure Crossfade:** Transisi gambar antar-slide 1.000 ms tanpa kedipan layar hitam (*no black flash*).
  * **5-Minute Auto-Sync:** Polling otomatis konfigurasi slide JSON dari server setiap 5 menit tanpa perlu restart TV.
  * **Screen Wake Lock:** Memastikan layar TV tetap menyala prima sepanjang jam operasional madrasah.

### B. Modul Quran Sekejap & Cursor Quran
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/modulSekejap](https://github.com/Yayasan-Bina-Insan-Mustaqbal/modulSekejap) • [Yayasan-Bina-Insan-Mustaqbal/cursorQuranSekejap](https://github.com/Yayasan-Bina-Insan-Mustaqbal/cursorQuranSekejap)
* **Teknologi:** Python, TypeScript, Interactive UI
* **Tujuan:** Digitalisasi metode pengajaran terjemah Al-Qur'an perkata sistematis karya perumus SOTAB agar santri usia tamyiz dapat memahami makna bacaan shalat dalam tempo singkat.

### C. Dzikr & Dua Mobile and Web
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/Dzikr-DuaWeb](https://github.com/Yayasan-Bina-Insan-Mustaqbal/Dzikr-DuaWeb) • [decaller/DzikrAndDuaMobile](https://github.com/decaller/DzikrAndDuaMobile)
* **Teknologi:** Kotlin (Android Native), TypeScript (Web Responsive)
* **Fungsi:** Aplikasi panduan doa dan dzikir pagi-petang ma'tsur dengan teks Arab berharakat tajwid, audio pelafalan, dan transliterasi resmi.

### D. Factory Blockly: Stimulasi Nalar Cipta Santri
* **Repositori:** [Yayasan-Bina-Insan-Mustaqbal/factory-blockly](https://github.com/Yayasan-Bina-Insan-Mustaqbal/factory-blockly)
* **Teknologi:** Google Blockly, JavaScript
* **Fungsi:** Sarana edukasi algoritma dan logika pemrograman visual ramah anak tanpa paparan kode teks rumit, menumbuhkan fitrah berpikir kritis (*syakilah cipta*).

### E. PosterMaker & LayoutTK: Otomasi Grafis & Tipografi
* **Repositori:** [decaller/posterMaker](https://github.com/decaller/posterMaker) • [decaller/layoutTK](https://github.com/decaller/layoutTK)
* **Teknologi:** Typst Modern Typesetting, Python
* **Tujuan:** Mesin otomatis pencetak poster adab, pamflet tarbiyah, dan penataan halaman buku materi PAUD/TK berkualitas tinggi dengan standarisasi estetika islami.

---

## 6. Kluster 5: Wiki PKN & Infrastruktur Terbuka (GitOps & Portainer)

Repositori tempat Anda membaca dokumentasi ini merupakan salah satu simpul penting dalam ekosistem digital:

### A. Repositori Wiki-PKN
* **Repositori:** [decaller/wiki-pkn](https://github.com/decaller/wiki-pkn)
* **Domain Produksi:** [https://wikipkn.insanmustaqbal.or.id/](https://wikipkn.insanmustaqbal.or.id/)
* **Mesin Generator:** Quartz v5.0.0 (Fast SPA, Content Indexing, RSS, Full-Text Search, Mermaid Diagram, Obsidian Canvas Page)
* **Keunikan:**
  * Memadukan teks markdown murni dengan 96+ diagram Obsidian Canvas interaktif.
  * Terintegrasi dengan Microsoft Office Web Apps Viewer untuk 39 slide materi asli PPTX.
  * Pangkalan Data TB-40 Bases dan katalog dalil turats OpenBayan (terintegrasi penuh dengan seluruh dataset Maktabah Syamilah).

### B. Deployment GitOps Portainer & Docker
* **Infrastruktur:** Docker Compose, Portainer CE (Stack ID 25, Endpoint ID 3)
* **Otomasi:** Setiap pembaruan kode di branch `main` GitHub otomatis memicu penarikan kode (*git pull*), kompilasi internal container, dan hot-reload server produksi port 4040.

---

## 7. Matriks Komprehensif Ekosistem Software PKN

Berikut adalah ikhtisar lengkap seluruh perangkat lunak yang dikembangkan dalam ekosistem Manhaj PKN:

| No | Nama Software / Proyek | Organisasi / Pengembang | Peran & Domain Utama | Stack Teknologi Kunci | Tautan Repositori |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Wiki PKN** | decaller / YBIM | Pusat Dokumentasi Ensiklopedia Manhaj PKN | Quartz v5, TS, Canvas, Python | [decaller/wiki-pkn](https://github.com/decaller/wiki-pkn) |
| **2** | **OpenBayan Core** | Yayasan-Bina-Insan-Mustaqbal | The Islamic Knowledge Graph (Quran & Hadits) | Python, FastAPI, GraphDB, HTML | [YBIM/OpenBayan](https://github.com/Yayasan-Bina-Insan-Mustaqbal/OpenBayan) |
| **3** | **OpenBayanNext** | decaller | Semantic Search Mesin Riset Bahasa Arab Klasik | Python, Vector IR, NLP, Embeddings | [decaller/OpenBayanNext](https://github.com/decaller/OpenBayanNext) |
| **4** | **Hadith-Data-Sets** | decaller | Basis Data 62.169 Hadits 9 Kitab Shahih | Raw Dataset (Tashkil & Non-Tashkil) | [decaller/Hadith-Data-Sets](https://github.com/decaller/Hadith-Data-Sets) |
| **5** | **PKN-videoDB** | decaller | Saluran Transkrip & Vector Search Video Kajian | Turso SQLite, Vector DB, GitHub Pages | [decaller/PKN-videoDB](https://github.com/decaller/PKN-videoDB) |
| **6** | **TafsirBakat.com** | PKN / Jejaring Lembaga | Portal Resmi Tes Online Asesmen 40 Bakat | Web App, Form Engine, Scoring System | [tafsirbakat.com](https://tafsirbakat.com/) |
| **7** | **TB40 Front-End** | Yayasan-Bina-Insan-Mustaqbal | Web App Asesmen TB40 Insan Mustaqbal (Dev) | TanStack Start, React, TS, shadcn/ui | [YBIM/tb40-fe](https://github.com/Yayasan-Bina-Insan-Mustaqbal/tb40-fe) |
| **8** | **TB40 Analytics API** | Yayasan-Bina-Insan-Mustaqbal | Backend Server Analisis & Skor Tes TB40 | Node.js, SQLite, REST API | [YBIM/tb40-analytics-api](https://github.com/Yayasan-Bina-Insan-Mustaqbal/tb40-analytics-api) |
| **9** | **API TB40 Explore** | Yayasan-Bina-Insan-Mustaqbal | Layanan Eksplorasi Hubungan Sifat & Bakat | Microservice API | [YBIM/api-tb40-explore](https://github.com/Yayasan-Bina-Insan-Mustaqbal/api-tb40-explore) |
| **10** | **Pub Insan Taqwa Bakat** | decaller / Insan Taqwa | Visualisasi Peta Sifat & 40 Pilar Bakat | HTML, D3/Canvas Graph, Interactive JS | [decaller/pub.insantaqwa.org](https://github.com/decaller/pub.insantaqwa.org) |
| **11** | **Rapor Karakter** | decaller | Builder & Runner Rapor Kualitatif Santri | TypeScript, SurveyJS, Web Runner | [decaller/rapor-karakter](https://github.com/decaller/rapor-karakter) |
| **12** | **Rapor SD Drive** | Yayasan-Bina-Insan-Mustaqbal | Agregator Rapor Siswa dari Google Drive | JavaScript, SQLite, Caddy, ODS | [YBIM/rapor-sd-...](https://github.com/Yayasan-Bina-Insan-Mustaqbal/rapor-sd-frontend-backend) |
| **13** | **Observasi Karakter API**| decaller | API Mutaba'ah & Pencatatan Adab Santri | Node.js, Express, REST API | [decaller/observasi-karakter-api](https://github.com/decaller/observasi-karakter-api) |
| **14** | **Survey Report PKN** | Yayasan-Bina-Insan-Mustaqbal | Generator Laporan Survei Karakter Santri | Python Data Script | [YBIM/surveyReportPKN](https://github.com/Yayasan-Bina-Insan-Mustaqbal/surveyReportPKN) |
| **15** | **Mading Digital** | decaller | Signage TV Smart Display Layar Santri | TanStack Start, React, Screen WakeLock | [decaller/mading-digital](https://github.com/decaller/mading-digital) |
| **16** | **Modul Quran Sekejap** | Yayasan-Bina-Insan-Mustaqbal | Media Pembelajaran Al-Qur'an Cepat SOTAB | Python, Data Pipeline | [YBIM/modulSekejap](https://github.com/Yayasan-Bina-Insan-Mustaqbal/modulSekejap) |
| **17** | **Cursor Quran Sekejap** | Yayasan-Bina-Insan-Mustaqbal | Aplikasi Interaktif Belajar Baca & Terjemah | TypeScript, Interactive Web | [YBIM/cursorQuranSekejap](https://github.com/Yayasan-Bina-Insan-Mustaqbal/cursorQuranSekejap) |
| **18** | **Dzikr & Dua App** | YBIM / decaller | Aplikasi Wirid & Doa Harian Santri | Kotlin (Android), TypeScript (Web) | [YBIM/Dzikr-DuaWeb](https://github.com/Yayasan-Bina-Insan-Mustaqbal/Dzikr-DuaWeb) |
| **19** | **Factory Blockly** | Yayasan-Bina-Insan-Mustaqbal | Stimulasi Fitrah Berpikir & Logika Visual | Google Blockly, JavaScript | [YBIM/factory-blockly](https://github.com/Yayasan-Bina-Insan-Mustaqbal/factory-blockly) |
| **20** | **HermesDIL Collabora** | Yayasan-Bina-Insan-Mustaqbal | Tata Dokumen Persuratan Mandiri Yayasan | Collabora Integration, JavaScript | [YBIM/hermesDIL](https://github.com/Yayasan-Bina-Insan-Mustaqbal/hermesDIL) |
| **21** | **PosterMaker & LayoutTK**| decaller | Otomasi Tipografi Modul & Poster Sekolah | Typst, Python Automation | [decaller/posterMaker](https://github.com/decaller/posterMaker) |
| **22** | **Kutubio & IslamResearch**| YBIM / decaller | Riset Pustaka Kitab Klasik & Leksikografi | PHP, Web Database | [YBIM/kutubio](https://github.com/Yayasan-Bina-Insan-Mustaqbal/kutubio) |

---

## 8. Panduan Kontribusi Pengembang (Developer Guide)

Bagi para insinyur perangkat lunak (*software engineers*), pengembang web, data scientist, dan pegiat teknologi Muslim yang ingin mewakafkan keahlian koding untuk kemaslahatan dakwah pendidikan:

### A. Prinsip Etika Koding Berbingkai Syariah
1. **Ikhlas & Anti-Komersialisasi Data:** Seluruh data pribadi santri, rekam jejak ibadah, dan asesmen psikologis wajib dilindungi (*data privacy*), tidak boleh dijual atau diserahkan ke broker data pihak ketiga.
2. **Kualitas Itqan (High Craftsmanship):** Meneladani sabda Rasulullah ﷺ: *"Sesungguhnya Allah mencintai seorang hamba yang apabila melakukan suatu pekerjaan, ia melakukannya dengan itqan (profesional dan sempurna)"* (HR. Al-Baihaqi). Tulis kode yang bersih, terdokumentasi, dan bebas celah keamanan.
3. **Standar Open-Source:** Gunakan lisensi bersahabat (seperti MIT, AGPL, atau Apache-2.0) yang mengizinkan pemanfaatan seluas-luasnya bagi madrasah dan pondok pesantren di pelosok nusantara.

### B. Prosedur Berpartisipasi
1. Kunjungi organisasi GitHub: [github.com/Yayasan-Bina-Insan-Mustaqbal](https://github.com/Yayasan-Bina-Insan-Mustaqbal) atau profil [github.com/decaller](https://github.com/decaller).
2. Pilih proyek yang sesuai dengan keahlian Anda (Front-End React/TanStack, Back-End Node.js/FastAPI, Data Engineering Python, Mobile Android/Kotlin, atau UI/UX).
3. Ajukan perbaikan fitur atau laporkan kutu (*bug*) melalui laman *Issues* dan *Pull Request*.
4. Panduan kontribusi naskah ensiklopedia wiki dapat dipelajari di: [[Panduan Kontribusi]].

---

## 9. Refleksi Lapangan, Peringatan Risiko, dan Tips Praktis

> [!info] Refleksi Lapangan: Teknologi Membantu Menstandarkan, Bukan Menggantikan Keteladanan
> Berdasarkan pengalaman penerapan software di puluhan sekolah mitra PKN, keberadaan aplikasi asesmen bakat online atau sistem rapor karakter otomatis sangat meringankan beban administratif para asatidz. Guru tidak lagi disibukkan dengan rumus Excel berhari-hari.  
> 
> Namun, software tidak akan pernah bisa menggantikan pelukan hangat seorang guru, tatapan kasih sayang saat santri menangis, atau doa tulus di sepertiga malam. Software adalah instrumen efisiensi; ruh pendidikan tetap berada pada keteladanan insan (*Al-Qudwah*).

> [!warning] Peringatan Risiko: Jebakan Teknokrasi dan Digital Obsession
> * **Bentuk Kesalahan:** Menganggap sekolah sudah "berkarakter nabawiyah" hanya karena telah menginstal aplikasi TB40 atau mading digital canggih, sementara adab harian guru dan santri masih diabaikan.
> * **Dampak Terhadap Jiwa:** Timbulnya kesombongan modernitas (*digital pride*), santri kecanduan menatap layar (*screen-time berlebih*), dan hilangnya kepekaan sosial terhadap sesama.
> * **Pencegahan Nabawiyah:** Batasi interaksi santri dengan gawai sesuai etape usia (*belum diizinkan gawai pribadi sebelum usia aqil baligh 15 tahun*); prioritaskan interaksi alam terbuka dan khidmah fisik.

> [!tip] Tips Praktis bagi Pengelola Sekolah & Pengembang Hari Ini
> * **Aksi Sederhana:** Jika Anda seorang pimpinan lembaga, mulailah memanfaatkan **[tafsirbakat.com](https://tafsirbakat.com/)** atau **[tb40.insanmustaqbal.or.id](https://tb40.insanmustaqbal.or.id/)** untuk asesmen berkala santri usia tamyiz akhir.  
> * **Bagi Pengembang:** Fork salah satu repositori terbuka di atas, jalankan secara lokal, dan bantu selesaikan satu issue kecil untuk menjadi amal jariyah keilmuan Anda.

---

## 10. Rujukan Repositori & Tautan Terkait

- **Organisasi GitHub Yayasan:** [Yayasan-Bina-Insan-Mustaqbal](https://github.com/Yayasan-Bina-Insan-Mustaqbal)
- **Profil GitHub Pengembang:** [decaller (Harridi Ilman Tovid)](https://github.com/decaller)
- **Aplikasi Web Terkait:**
  - [Tes Online Tafsir Bakat](https://tafsirbakat.com/)
  - [Aplikasi Asesmen TB40 Insan Mustaqbal](https://tb40.insanmustaqbal.or.id/)
  - [Peta Visual Bakat Insan Taqwa](https://pub.insantaqwa.org/bakat/)
  - [Portal Wiki PKN](https://wikipkn.insanmustaqbal.or.id/)
- **Dokumen Terkait di Wiki PKN:**
  - [[content/Referensi/index|Pusat Referensi & Sumber Rujukan]]
  - [[content/Referensi/Panduan Kontribusi|Panduan Kontribusi Wiki PKN]]
  - [[content/Referensi/Korpus Dalil & Atsar Klasik|Korpus Dalil & Atsar Klasik OpenBayan]]
  - [[Bakat]]
  - [[Panduan Asesmen dan Observasi TB40]]
  - [[Kuisioner Asesmen 40 Bakat Nabawiyah]]
  - [[Program dan Kegiatan Pendidikan Karakter Nabawiyah]]

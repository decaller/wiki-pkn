---
title: "Catatan Rilis dan Pembaruan Sistem"
description: "Dokumentasi riwayat pembaruan sistem dan evolusi platform Wiki Pendidikan Karakter Nabawiyah (PKN) dari Milestone 1 hingga Milestone 60 (v1.0.0 s/d v2.5.0)."
aliases:
  - "/changelog"
  - "changelog"
  - "Catatan Rilis"
  - "Changelog"
  - "Release Notes"
  - "Riwayat Versi"
tags:
  - changelog
  - catatan-rilis
  - pembaruan-sistem
  - rilis-publik
---

<!-- ========================================================================== -->
<!-- ZONA 1: HEADER, ACTION BAR & METADATA                                      -->
<!-- ========================================================================== -->

# 🚀 Catatan Rilis & Pembaruan Sistem Wiki PKN

<div class="wiki-action-bar">
  <span class="wiki-action-item active">📖 Baca</span>
  <a href="https://github.com/decaller/wiki-pkn/releases" class="wiki-action-item" target="_blank" rel="noopener">🏷️ GitHub Releases</a>
  <a href="https://github.com/decaller/wiki-pkn/commits/main" class="wiki-action-item" target="_blank" rel="noopener">📜 Riwayat Komit</a>
  <a href="https://github.com/decaller/wiki-pkn/discussions" class="wiki-action-item" target="_blank" rel="noopener">💬 Diskusi</a>
  <span class="wiki-action-meta">Tier 1: System Release Notes • Produksi Aktif</span>
</div>

<!-- ========================================================================== -->
<!-- ZONA 2: INFOBOX, LEAD SECTION & CANVAS EMBED                               -->
<!-- ========================================================================== -->

<div class="wiki-infobox">
  <div class="wiki-infobox-header">
    <div class="wiki-infobox-title">Ringkasan Sistem Wiki PKN</div>
    <div class="wiki-infobox-subtitle">Spesifikasi Arsitektur & Status Rilis</div>
  </div>
  <table class="wiki-infobox-table">
    <tr>
      <th>Platform</th>
      <td>Wiki Pendidikan Karakter Nabawiyah</td>
    </tr>
    <tr>
      <th>Versi Stabil Terkini</th>
      <td><strong>v2.5.0 Production</strong></td>
    </tr>
    <tr>
      <th>Tanggal Rilis</th>
      <td>September 2026</td>
    </tr>
    <tr>
      <th>Mesin SSG</th>
      <td>Quartz v5.0.0 (Node.js / TypeScript)</td>
    </tr>
    <tr>
      <th>Total Berkas Korpus</th>
      <td>471+ Berkas Markdown</td>
    </tr>
    <tr>
      <th>Integritas Tautan</th>
      <td>🟢 100% Sound (0 Broken Wikilinks)</td>
    </tr>
    <tr>
      <th>Purifikasi Kosakata</th>
      <td>🟢 100% Murni (0 Kata Terlarang)</td>
    </tr>
    <tr>
      <th>Indeks Keterbacaan</th>
      <td>🟢 86.23 / 100 (Target PICI ≥ 85.0)</td>
    </tr>
    <tr>
      <th>Server Produksi</th>
      <td>Portainer Endpoint 3 (Stack ID 25)</td>
    </tr>
    <tr>
      <th>Domain Publik</th>
      <td><code>https://wikipkn.insanmustaqbal.or.id</code></td>
    </tr>
    <tr>
      <th>Lisensi & Otoritas</th>
      <td>Manhaj Ustadz Abdul Kholiq / Yayasan Bina Insan Taqwa</td>
    </tr>
  </table>
</div>

> [!summary] ⚡ Ringkasan Evolusi Wiki PKN: Dari Catatan Lepas Menuju Ensiklopedia Peradaban
> 
> Basis pengetahuan digital **Wiki Pendidikan Karakter Nabawiyah (PKN)** telah berevolusi melalui **60 Milestone terencana** yang terbagi dalam lima generasi rilis utama:
> 1. **v2.5.0 (September 2026):** Penerbitan 80+ halaman mandiri Dalil Al-Qur'an dan Hadits bersanad Maktabah Syamilah / OpenBayan, 8 ulasan ensiklopedis buku kanonikal PKN, mesin linter korpus otomatis (`wiki_corpus_linter.py`), dan analitik mandiri Umami.
> 2. **v2.4.0 (September 2026):** Penerbitan Glosarium Istilah resmi PKN dan purifikasi menyeluruh diksi non-sumber (*fase*, *uswah sahabat*, *kesadaran beramal*).
> 3. **v2.3.0 (September 2026):** Master Blueprint Arsitektur PKN (Sektor 00 s/d 06), kodifikasi 40 pilar bakat fitrah TB-40 dari naskah master Buku Tafsir Bakat, dan standarisasi 100% repositori ke MediaWiki 4-Zone.
> 4. **v2.2.0 (September 2026):** Ingestion 121 materi buletin SOTAB HEBAT, 122 halaman rekaman kajian video (1.159 bab transkrip), dan 106 flowchart alur belajar visual.
> 5. **v2.0.0 (September 2026):** Migrasi arsitektur ke Quartz v5, sidebar kustom `OutlineNav` dengan state persistence, pangkalan data TB-40 Bases, dan standar emas konten 0 defisit.

![[canvas/Beranda - Peta Konsep Arsitektur Pendidikan Karakter Nabawiyah.canvas]]
*Gambar: Arsitektur Ekosistem Digital Manhaj Pendidikan Karakter Nabawiyah (PKN)*

---

<!-- ========================================================================== -->
<!-- ZONA 3: RIWAYAT DETAIL MILISTONE & PEMBARUAN VERSI                          -->
<!-- ========================================================================== -->

## 📦 Riwayat Rilis Versi & Milestone

### 🏷️ Versi 2.5.0 — *Ekspansi Dalil Bersanad, Review 8 Buku, Linter Kualitas & Umami Analytics*
**Tanggal Rilis:** 23 September 2026 | **Cakupan Milestone:** Milestone 60 | **Status:** Rilis Produksi Aktif

Versi 2.5.0 merupakan tonggak ekspansi ilmiah dan infrastruktur terbesar, mengukuhkan otoritas sanad keilmuan Wiki PKN melalui korpus wahyu dan kitab turats klasik:

* 📖 **Basis Data Dalil Mandiri (`content/Dalil/` — 84 Berkas):**
  - Menerbitkan halaman ensiklopedis mandiri berformat MediaWiki 4-Zone untuk setiap dalil Al-Qur'an dan Hadits shahih bersanad.
  - Setiap berkas memuat teks Arab berharakat lengkap, takhrij Maktabah Syamilah / OpenBayan ID Shamela, terjemahan resmi Kemenag RI, serta syarah ulama mu'tabar (*Tafsir Ibnu Katsir*, *Syarah Shahih Muslim An-Nawawi*, *Fathul Bari Ibnu Hajar*).
  - Melengkapi 11 dalil naqli khusus pensucian jiwa (*Tazkiyatun Nafs*: Takhalli dan Tahalli) serta pemutakhiran artikel induk `Tazkiyatun Nafs.md`.
* 📚 **Penerbitan 8 Review Buku Kanonikal PKN (`content/Referensi/`):**
  - Menerbitkan 8 artikel review ensiklopedis komprehensif karya Ustadz Abdul Kholiq: *Pendidikan Karakter Nabawiyah*, *Tafsir Bakat*, *Menumbuhkan Kesadaran Beramal*, *Recovery Berbasis Fitrah*, *Kurikulum Sekolah Karakter Islam*, *Panduan Implementasi Standar PKN*, *Panduan Kurikulum PAUD-TK Karakter Islam*, dan *Bukanlah Sekejap*.
  - Dilengkapi Infobox Bibliografi, Peta Konsep Bab, Relevansi Kurikulum, Matriks Pembaca, dan Kutipan Emas (*Golden Quotes*).
* 🛡️ **Mesin Linter Korpus Otomatis (`scripts/wiki_corpus_linter.py`):**
  - Mengembangkan engine linter produksi (1.484 baris kode) untuk menjaga mutu naskah:
    - **Link Integrity:** 0 broken wikilink targets dan 0 orphan pages di seluruh 471 berkas.
    - **Vocabulary Guard:** Penegakan larangan istilah asing pada 8 klaster terlarang (*zero foreign terms*).
    - **Pedagogical Style Auditor:** Penilaian kepatuhan 10 poin pedagogis Ustadz Abdul Kholiq.
    - **PKN Indonesian Clarity Index (PICI):** Algoritma keterbacaan bahasa dengan capaian rata-rata korpus **86.23/100** (target $\ge 85.0$).
* 📊 **Deployment Umami Analytics & Optimasi SEO:**
  - Deployment stack Docker mandiri Umami Analytics + PostgreSQL 15 di Portainer Endpoint 3 (Stack ID 27, port 3008).
  - Konfigurasi parameter analitik Umami pada `quartz.config.yaml` dan meta tag SEO komprehensif (Open Graph dinamis, canonical URL, XML sitemap) pada `quartz/components/Head.tsx`.

---

### 🏷️ Versi 2.4.0 — *Glosarium Resmi PKN & Purifikasi Kosakata Autentik Sumber*
**Tanggal Rilis:** 23 September 2026 | **Cakupan Milestone:** Milestone 59

Fokus utama versi 2.4.0 adalah standardisasi leksikal dan purifikasi terminologi agar selaras dengan bahasa sumber nabawi:

* 📖 **Penerbitan Glosarium Master PKN (`content/Glosarium Istilah Karakter Nabawiyah.md`):**
  - Menerbitkan kamus rujukan alfabetis resmi (A–Z) yang memuat definisi syar'i, filosofis, pedagogis, serta panduan purifikasi diksi.
  - Memetakan istilah ke dalam 6 klaster tematik: Epistemologi Insan, Dinamika Nafs, Metode Mendidik, Fase Usia, 40 Pilar Bakat TB-40, dan Tata Kelola Kelembagaan.
* 🧹 **Purifikasi Kosakata Autentik Sumber:**
  - Melakukan refaktorisasi 630+ kemunculan kosakata asing non-sumber di seluruh repositori:
    * Mengganti istilah serapan non-sumber secara konsisten menjadi **fase** / **tahapan** (termasuk menamai ulang berkas kanvas: *Fase Thufulah*, *Fase Tamyiz*, *Fase Murahaqah*, dan *Dua Fase Tazkiyatun Nafs*).
    * Mengganti istilah mitologis non-sumber secara konsisten menjadi **uswah sahabat** / **figur teladan**.
    * Mengganti istilah reduksionisme perilaku mekanis secara konsisten menjadi **penumbuhan kesadaran beramal**.
  - Menetapkan alias kanonikal `4 Fase Usia Nabawiyah` dengan mempertahankan kompatibilitas tautan lama.

---

### 🏷️ Versi 2.3.0 — *Master Blueprint Arsitektur PKN & Transformasi 4-Zone Repositori*
**Tanggal Rilis:** 22 September 2026 | **Cakupan Milestone:** Milestone 55 s/d 58

Versi 2.3.0 menandai transformasi arsitektur informasi wiki menjadi taman digital berstandar industri:

* 🏛️ **Master Blueprint Arsitektur PKN (`content/Arsitektur PKN/` — 7 Berkas Master):**
  - Kodifikasi makro 6 sektor sistem tarbiyah nabawiyah:
    * `00 - Master Arsitektur PKN.md` $\leftrightarrow$ Master Hub navigasi sistem.
    * `01 - Komponen & Kurikulum PKN.md` $\leftrightarrow$ Sektor 1 (Epistemologi, 5 Pilar Tarbiyah, Maqashid).
    * `02 - Metode & Pendekatan Fisik-Ruh.md` $\leftrightarrow$ Sektor 2 (Hierarki Insan, Tadarruj, 4 Luaran, 4 Kurva Dinamika).
    * `03 - Peran Pembelajaran & Model.md` $\leftrightarrow$ Sektor 3 (Cara Belajar Fitrah, QS. An-Nahl 78, Lab Alamiah).
    * `04 - Peran Pendidik & Kedisiplinan.md` $\leftrightarrow$ Sektor 4 (Piramida Usia, 3 Bahasa, Zonasi Al-Hima).
    * `05 - Jejak Pendidik & Target.md` $\leftrightarrow$ Sektor 5 (Capaian Santri: Shalih & Muslih, Transisi Gender).
    * `06 - Implementasi & Rantai Kausalitas.md` $\leftrightarrow$ Sektor 6 (Rantai Kausalitas 5 Tingkat, 4 Kaidah Emas, 8 Standar Mutu).
* 🎯 **Integrasi Komprehensif 40 Pilar Bakat Fitrah TB-40 (Milestone 57):**
  - Menyerap naskah master *Buku Tafsir Bakat* karya Ustadz Abdul Kholiq Bab 12 ke dalam 40 berkas di `content/Paradigma - Implementasi PKN/.../TB40/`.
  - Menerapkan arsitektur 4-Zone pada setiap pilar: Action Bar, Infobox vertikal, TL;DR intisari, definisi syar'i, uswah sahabat, matriks tafrith-wasathiyah-ifrath, rubrik 3-level, 3 pertanyaan muhasabah, dan aksi quick win.
* 🌐 **Transformasi Komprehensif 100% Repositori ke 4-Zone MediaWiki (Milestone 58):**
  - Meningkatkan 382 berkas Markdown (Core Manhaj, Materi SOTAB, Kajian Video) ke arsitektur 4-Zone dengan progressive disclosure.

---

### 🏷️ Versi 2.2.0 — *Ingestion 121 Materi SOTAB & 122 Video Ceramah Kajian*
**Tanggal Rilis:** 21 September 2026 | **Cakupan Milestone:** Milestone 51 s/d 54

Fokus pada pengayaan khazanah lapangan dan media audio-visual:

* 📰 **Ingestion 121 Artikel SOTAB HEBAT (`content/Materi SOTAB/`):**
  - Mengonversi seluruh artikel parenting buletin SOTAB HEBAT ke format Markdown lengkap dengan protokol solusi kuratif EMISOL (Empati, Imajinasi, Solusi).
* 🎥 **Indeks 122 Halaman Kajian Video (`content/Kajian Video/`):**
  - Mengindeks 122 rekaman ceramah Ustadz Abdul Kholiq dengan 1.159 bab transkrip lengkap bertaut timestamp YouTube.
* 📊 **106 Visual Flowchart Alur Materi (`content_flow/`):**
  - Menyusun 106 diagram alur berpikir Mermaid untuk visualisasi reading path bertahap antar topik.
* 📋 **Standardisasi 8 Templat Halaman Khusus Non-Penjelasan:**
  - Menetapkan struktur MediaWiki namespaces untuk halaman portal, navigasi, dan indeks.

---

### 🏷️ Versi 2.0.0 — *Fondasi Arsitektur Digital Garden Wiki PKN & Migrasi Quartz v5*
**Tanggal Rilis:** 15–20 September 2026 | **Cakupan Milestone:** Milestone 1 s/d 50

Peletakan pondasi awal platform static site generator modern:

* 🧭 **Navigasi Kustom `OutlineNav`:**
  - Mengembangkan komponen sidebar khusus `./plugins/outline-nav` yang membaca hierarki `nav_structure.json` dengan inside scrolling, active link auto-expand, dan state persistence (`sessionStorage` dan `localStorage`).
* 🎨 **Peralihan ke Obsidian Canvas:**
  - Mengonversi 100% diagram Mermaid lama menjadi berkas kanvas resmi (`content/canvas/*.canvas`) dengan interaksi pan, zoom, dan fullscreen.
* 📊 **Pangkalan Data TB-40 Bases:**
  - Membangun database `TB40.base` berbasis Obsidian Bases (tampilan Tabel, Kartu, dan Kanban 6 rumpun bakat).
* 📽️ **Office Web Apps Viewer PPTX:**
  - Mengintegrasikan penampil slide interaktif Microsoft PowerPoint Online untuk 39 presentasi kanonikal.
* 🔍 **Integrasi Korpus Hadits OpenBayan Awal:**
  - Menghubungkan basis data SQLite `shamela_corpus.db` dengan normalisasi teks Arab FTS5.
* 🚢 **Deployment Produksi Awal:**
  - Otomasi GitOps di Portainer Endpoint 3 melayani situs `https://wikipkn.insanmustaqbal.or.id`.

---

## 📊 Matriks Ringkasan Evolusi Antar-Versi

| Parameter Metrik | Versi 1.0 (Awal) | Versi 2.0 (Fondasi) | Versi 2.2 (Media) | Versi 2.3 (Arsitektur) | Versi 2.4 (Glosarium) | Versi 2.5 (Terkini) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Total Berkas MD** | 39 | 67 | 310 | 382 | 383 | **471+** |
| **Simpul Navigasi** | 49 | 49 | 94 | 118 | 118 | **143** |
| **Standar Format** | Markdown Dasar | Outline MOC | Namespace Khusus | 4-Zone MediaWiki | 4-Zone MediaWiki | **4-Zone MediaWiki** |
| **Halaman Dalil** | 0 | 4 (Prototipe) | 4 | 4 | 4 | **84 Mandiri** |
| **Review Buku** | 0 | 1 (Daftar) | 1 (Daftar) | 1 (Daftar) | 1 (Daftar) | **8 Ensiklopedis** |
| **Glosarium A–Z** | Belum Ada | Belum Ada | Belum Ada | Belum Ada | 1 Berkas Master | **1 Berkas Master** |
| **Toolkit KBM** | Parsial | 1 Panduan | 1 Panduan | 1 Panduan | 1 Panduan | **Hub + 5 Dokumen** |
| **Engine Linter** | Belum Ada | Manual | Skrip Dasar | Skrip Dasar | Purifikasi Regex | **wiki_corpus_linter** |
| **Skor Clarity** | Tidak Terukur | ~70.0 | ~76.5 | ~81.2 | ~83.4 | **86.23 / 100** |
| **Analitik Web** | Belum Ada | Belum Ada | Belum Ada | Belum Ada | Belum Ada | **Umami Analytics** |

---

<!-- ========================================================================== -->
<!-- ZONA 4: CROSS-LINKS, NAVBOX & ROADMAP MASA DEPAN                           -->
<!-- ========================================================================== -->

## 🗺️ Roadmap Pengembangan Sistem Wiki PKN

* **v2.6.0 (Direncanakan):**
  - Implementasi *Local RAG Search Agent* berbasis model semantik ringkas untuk tanya-jawab kurikulum PKN secara cerdas.
  - Modul digital Rapor Karakter Santri interaktif berbasis instrumen kualitatif non-angka 19 butir.
  - Fitur Progressive Web App (PWA) offline-first untuk akses mudah pendidik di daerah minim sinyal internet.

---

<div class="wiki-navbox">
  <div class="wiki-navbox-title">Navigasi Utama Sistem & Khazanah Manhaj Wiki PKN</div>
  <div class="wiki-navbox-content">
    <div class="wiki-navbox-group">
      <span class="wiki-navbox-group-title">Gerbang & Arsitektur</span>
      <span class="wiki-navbox-links">[[index|Beranda Utama]] • [[00 - Master Arsitektur PKN|Master Hub Arsitektur PKN]] • [[PKN Blueprint Arsitektur Sistem|Blueprint Sistem]] • [[Glosarium Istilah Karakter Nabawiyah|Glosarium Resmi]]</span>
    </div>
    <div class="wiki-navbox-group">
      <span class="wiki-navbox-group-title">Rujukan Otoritatif</span>
      <span class="wiki-navbox-links">[[Master Katalog Dalil Al-Quran|Katalog Al-Qur'an]] • [[Master Katalog Dalil Hadits dan Sunnah|Katalog Sunnah]] • [[Korpus Dalil & Atsar Klasik|Korpus Turats]] • [[Referensi Tambahan Buku Cetak|8 Buku Utama PKN]]</span>
    </div>
    <div class="wiki-navbox-group">
      <span class="wiki-navbox-group-title">Praktek & Perangkat</span>
      <span class="wiki-navbox-links">[[Toolkit KBM/index|Template & Toolkit KBM Pendidik]] • [[Panduan RPP dan Observasi Lapangan]] • [[Bank Studi Kasus]] • [[FAQ Ringkas]]</span>
    </div>
    <div class="wiki-navbox-group">
      <span class="wiki-navbox-group-title">Sistem & Tata Kelola</span>
      <span class="wiki-navbox-links">[[Catatan Rilis dan Pembaruan Sistem|Catatan Rilis (Changelog)]] • [[Tentang Aplikasi Wiki PKN]] • [[Panduan Kontribusi]]</span>
    </div>
  </div>
</div>

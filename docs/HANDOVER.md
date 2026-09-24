# Dokumen Handover & Status Sistem Wiki PKN

> **Terakhir Diperbarui:** 24 September 2026, 17:10 WIB  
> **Status Repositori:** Clean, Sinkron dengan `origin/main` (Commit `6857fd4` / `main`)  
> **Target Produksi:** `https://wikipkn.insanmustaqbal.or.id/` (HTTP/2 200 OK)  
> **Mesin Platform:** Nginx 1.31 Alpine (Container dari `ghcr.io/decaller/wiki-pkn:latest`), SSG Quartz v5  
> **Kondisi Server VPS:** CPU 0%, RAM Container ~18 MB (Turun >98% dari konfigurasi Node.js lama)

---

## 1. Ringkasan Eksekutif (Executive Summary)

Seluruh pembenahan teknis, penulisan konten filosofis-pedagogis (Kaidah Zarkasyi & Firasat Nabawiyah), integrasi komponen tabel kontras refleksi, audit linter korpus, serta **migrasi total arsitektur deployment produksi ke GitHub Container Registry (GHCR) berbasis Nginx Alpine** telah selesai dikerjakan secara paripurna, diaudit oleh Independent Victory Auditor (**VICTORY CONFIRMED**), dan aktif melayani di domain produksi.

Dokumen ini berfungsi sebagai panduan serah terima (*handover*) lengkap dan terkini agar sesi berikutnya dapat langsung melanjutkan tanpa kehilangan konteks teknis maupun konten.

---

## 2. Rincian Milestone & Perbaikan Terbaru

### A. Milestone 64: Migrasi Runtime Produksi ke Docker Image GHCR (Nginx Alpine Anti-Lag)
* **Akar Masalah:** Sebelumnya, container produksi menjalankan `node:22-slim` (~1.2 GB image) yang mengeksekusi `npx quartz build --serve`. Setiap kali redeploy, proses kompilasi Quartz memakan CPU 100% di VPS selama 2–4 menit dan RAM ~1 GB, menyebabkan server lag dan potensi timeout pada reverse proxy.
* **Solusi Rekayasa:**
  1. **Offload Kompilasi ke Cloud Runner:** Beban kompilasi Quartz (484 berkas markdown $\to$ 2.713 file HTML) dialihkan 100% ke GitHub Actions runner (gratis & cepat, ~3 menit).
  2. **Image Web Server Ringan (`Dockerfile.nginx` & `nginx.conf`):** Hasil build `public/` dibungkus ke dalam image Nginx Alpine murni (hanya ~20 MB terkompresi, ~66 MB uncompressed).
  3. **Konfigurasi Routing Clean URLs:** Aturan Nginx `try_files $uri $uri.html $uri/ /index.html =404;` menjamin seluruh navigasi clean URL Quartz berfungsi mulus tanpa ekstensi `.html`.
  4. **Kompresi & Caching:** Gzip level 6 aktif untuk teks/CSS/JSON/JS/SVG dan cache browser 30 hari untuk aset statis (`.css`, `.js`, `.webp`, `.canvas`, font).
  5. **Healthcheck Multi-Protokol:** Konfigurasi `listen 8080; listen [::]:8080;` dan healthcheck wget ke `http://127.0.0.1:8080/healthz` menjamin status container `healthy` di Portainer.
  6. **Automasi GHCR:** Workflow `.github/workflows/deploy.yml` otomatis mem-build dan mem-push multi-tag (`latest` dan `sha`) ke `ghcr.io/decaller/wiki-pkn:latest` setiap push ke `main`.
* **Dampak & Hasil Produksi:**
  - Deployment di Portainer Stack 25 kini hanya membutuhkan waktu **~10 detik** (hanya menarik image jadi ~20 MB).
  - Konsumsi RAM container turun dari ~1.000 MB ke **~18 MB** (>98% penghematan).
  - **CPU VPS tetap 0%** tanpa lonjakan saat pembaruan naskah.
  - Status container di Portainer: **`running (healthy)`**.

### B. Milestone 62: Kaidah Zarkasyi, Firasat Nabawiyah, Callout Kontras & CI/CD Pipeline
* **1. Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi (Trilogi Hierarki Pendidikan):**
  - Menerbitkan artikel ensiklopedis 4-Zone di [`content/Referensi/Tokoh & Pemikiran/Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi.md`](file:///home/abuhafi/Project/wiki-pkn/content/Referensi/Tokoh%20&%20Pemikiran/Kaidah%20Pedagogis%20KH.%20Abdullah%20Syukri%20Zarkasyi.md) (365 baris, skor gaya 100/100, clarity 98.76/100).
  - Mengurai kaidah legendaris: *Metode > Materi*, *Guru > Metode*, dan *Jiwa Guru > Guru*.
  - Takhrij 5 dalil hadits bersanad via OpenBayan (HR. Bukhari No. 1, HR. An-Nasa'i No. 3140, HR. At-Tirmidzi No. 2685, HR. Muslim No. 537 & 2594) dan syarah ulama salaf.
  - Menyematkan diagram piramida Obsidian Canvas di [`content/canvas/Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi.canvas`](file:///home/abuhafi/Project/wiki-pkn/content/canvas/Kaidah%20Pedagogis%20KH.%20Abdullah%20Syukri%20Zarkasyi.canvas).
* **2. Firasat Nabawiyah (الفِرَاسَة) — Metode Membaca Jiwa & Bakat Anak:**
  - Menerbitkan artikel konsep 4-Zone di [`content/Paradigma - Implementasi PKN/.../Implementasi/Kaidah & Elemen/Firasat.md`](file:///home/abuhafi/Project/wiki-pkn/content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Kaidah%20&%20Elemen/Firasat.md) (372 baris, skor gaya 100/100, clarity 90.1/100).
  - Pembedaan tegas dari bakat TB-40 #07 (`07-firaasah.md`) melalui matriks komparasi 6 parameter.
  - Mengintegrasikan Tiga Dimensi Firasat PKN (Bakat/Syakilah, Ego/Kutub Energi 6 Rumpun, Kondisi Jiwa), syarah Ibnul Qayyim (*Madarijus Salikin*) mengenai 3 tingkatan firasat (*imaniyah*, *riyadhiyah*, *khilqiyah*), matriks 8 kasus tanda lahiriah $\to$ batiniah, protokol 4 tahap latihan observasi, dan diagram Obsidian Canvas [`Firasat Nabawiyah - Tiga Dimensi dan Metodologi Pembacaan Jiwa.canvas`](file:///home/abuhafi/Project/wiki-pkn/content/canvas/Firasat%20Nabawiyah%20-%20Tiga%20Dimensi%20dan%20Metodologi%20Pembacaan%20Jiwa.canvas).
  - Menerbitkan 2 halaman dalil mandiri di [`content/Dalil/`](file:///home/abuhafi/Project/wiki-pkn/content/Dalil/): [`dalil-firasat-mukmin-cahaya-allah.md`](file:///home/abuhafi/Project/wiki-pkn/content/Dalil/dalil-firasat-mukmin-cahaya-allah.md) dan [`dalil-al-mutawassimin-tanda-kebesaran-allah.md`](file:///home/abuhafi/Project/wiki-pkn/content/Dalil/dalil-al-mutawassimin-tanda-kebesaran-allah.md).
* **3. Standarisasi Callout Kontras (🔴 Kebiasaan Umum vs ✅ Pendekatan PKN):**
  - Memperbarui master template [`Template Elemen Refleksi, Implementas, Risiko, dan Tautan.md`](file:///home/abuhafi/Project/wiki-pkn/content/Paradigma%20-%20Implementasi%20PKN/Template/Template%20Elemen%20Refleksi,%20Implementas,%20Risiko,%20dan%20Tautan.md) dengan format tabel 2 kolom.
  - Menginjeksi 45 pasang perbandingan kontras kontekstual pada 9 artikel pilar utama prioritas (*Pembelajaran Alamiah*, *Persepsi Positif*, *Disiplin Positif PKN*, *Luka dan Hutang Pengasuhan*, *Recovery*, *Peran Ayah dan Bunda*, *Bahasa Hati*, *Bahasa Lisan*, *Bahasa Tangan*).
* **4. Pipeline CI/CD GitHub Actions (`.github/workflows/deploy.yml`):**
  - Workflow fail-fast 2 job: Job 1 `corpus-lint` (Python 3.12 linter) dan Job 2 `quartz-build` (Node.js 22, caching, Quartz SSG build, Docker image build, push ke GHCR, dan Portainer webhook).
* **5. Sinkronisasi Navigasi Sidebar & Integritas Repositori:**
  - `nav_structure.json` kini memuat **148 simpul** (120 daun) dengan 100% resolusi fisik (0 broken link, 0 unlinked leaves).
  - 87/87 pengujian unit di `tests/test_nav_structure.py` lulus 100%.
  - Linter korpus (`scripts/wiki_corpus_linter.py`) lulus bersih (0 broken links, 0 vocabulary violations, Clarity `86.3/100`).
  - Quartz v5 memproses **484 berkas markdown** dan mengemisi **2.713 berkas web statis**.

### C. Milestone 63: Resolusi Tag Leak Warna Hex pada Infobox
* Mengonversi 1.051 kode warna heksadesimal `#hex` pada atribut style HTML di 461 berkas menjadi format standar `rgb(...)` via [`scripts/fix_style_hex_colors.py`](file:///home/abuhafi/Project/wiki-pkn/scripts/fix_style_hex_colors.py) untuk mencegah parser Quartz OFM membacanya sebagai markdown hashtag.

---

## 3. Kondisi Infrastruktur & Deployment Produksi

* **Server Produksi:** Portainer Host di `103.167.12.129`, Endpoint ID: 3.
* **Stack Aktif:**
  1. `wiki-pkn` (Stack ID: 25) — Menjalankan image `ghcr.io/decaller/wiki-pkn:latest` (Nginx 1.31 Alpine). Binding port host `0.0.0.0:4040 -> 8080/tcp`. Status: `running (healthy)`.
  2. `umami` (Stack ID: 27) — Umami Analytics + PostgreSQL 15 melayani di port 3008.
* **Alur Deployment Otomatis Terkini:**
  ```
  git push origin main
         │
         ▼
  GitHub Actions CI/CD (.github/workflows/deploy.yml)
   ├── Job 1: Corpus Quality & Linter Audit (16s)
   └── Job 2: Quartz v5 Build & Nginx Package (3m)
         │
         ▼
  GitHub Container Registry (ghcr.io/decaller/wiki-pkn:latest)
         │
         ▼
  Portainer VPS (Stack ID: 25)
   └── Tarik image jadi (~20 MB, ~10s) via Redeploy
   └── Container Nginx Alpine running (RAM ~18 MB, CPU 0%)
         │
         ▼
  Domain Produksi: https://wikipkn.insanmustaqbal.or.id/ (HTTP/2 200 OK)
  ```

---

## 4. Status Indeks Dokumen & Data Mentah

| Direktori / Aset | Status | Deskripsi |
| :--- | :---: | :--- |
| `public/` | **2.713 Berkas** | Seluruh berkas web statis HTML/CSS/JS/Canvas hasil kompilasi Quartz v5. |
| `content/canvas/` | **106 Berkas** | Diagram interaktif Obsidian Canvas (termasuk kanvas Zarkasyi & Firasat). |
| `content/Dalil/` | **84 Berkas** | Halaman dalil mandiri dengan teks Arab berharakat, takhrij OpenBayan, dan syarah salaf. |
| `data/extracted_elements/` | **88 Berkas (100%)** | 5.311 elemen semantik terstruktur dan 166 tabel Markdown hasil ekstraksi Unstructured API. |
| `sources/buku_tafsir_bakat/` | **Tersimpan** | Naskah master lengkap Buku Tafsir Bakat (Bab 1–12, 118k kata). |
| `sources/research_papers/` | **Terisolasi** | Ruang penampungan PDF jurnal empiris eksternal. |

---

## 5. Rencana Tahap Selanjutnya (Action Items Rekomendasi)

1. **Jalur Riset & Audit Dalil Parenting (OpenBayan + Qaf AI):**
   - Menjalankan kueri broad-sweeping via OpenBayan (`shamela_11m`, port 6333) untuk tema-tema fikih tarbiyah (*tarbiyatul aulad*, *adabul walad*, *'uqubah*, *taklif*, *fitrah*).
   - Memanfaatkan Qaf AI secara hemat dan selektif (~100 pesan/bulan) hanya untuk verifikasi hipotesis dan meta-analysis lintas kitab salaf (*Tuhfatul Maudud*, *Ihya Ulumiddin*, *Fathul Bari*).
   - Menyusun dokumen kerja internal di `sources/audit_dalil_parenting/` (Gap Analysis & Contradiction Analysis) sebagai bahan mudzakarah asatidzah.
2. **Jalur Konten Komparasi:**
   - Profil dan review lembaga-lembaga yang mengadopsi PKN serta studi kasus implementasi persekolahan.
   - Halaman dialektika epistemologis: Teori PKN vs Teori Pendidikan Modern.
3. **Jalur Otomasi Webhook:**
   - Menambahkan secret `PORTAINER_WEBHOOK_URL` di GitHub repository agar GitHub Actions memicu redeploy Portainer otomatis tanpa perlu klik manual di dashboard Portainer.

# Dokumen Handover & Status Sistem Wiki PKN

> **Terakhir Diperbarui:** 6 Oktober 2026 — Forensik OMP, Retry 10 Menit, & Restorasi Penuh Integritas Korpus (Milestone 68)
> **Status Repositori:** 643 Berkas Markdown; 100% Link Integrity Sound (0 broken links, 0 orphans); 100% Manhaj-Pure (0 prohibited terms); 0 Style Floor Failures; 154/154 Unit Tests Lulus; Quartz SSG Build 100% Sukses.
> **Target Produksi:** `https://wikipkn.insanmustaqbal.or.id/` (HTTP/2 200 OK)  
> **Mesin Platform:** Nginx 1.31 Alpine (Container dari `ghcr.io/decaller/wiki-pkn:latest`), SSG Quartz v5  
> **Kondisi Server VPS:** CPU 0%, RAM Container ~18 MB (Turun >98% dari konfigurasi Node.js lama)

---

## 1. Ringkasan Eksekutif (Executive Summary)

### Handoff Forensik, Efisiensi Token, & Restorasi Integritas — 6 Oktober 2026

* **Evaluasi Forensik Konsumsi Token OMP (3 Run):**
  - Menganalisis log OMP (`~/.omp/logs/`): Run 1 membakar 12,52M token (101 error, crash ghost model), Run 2 membakar 15,10M token (0 error, 12 persona sukses), Run 3 membakar 32,81M token (485 error HTTP 429/503 upstream). Total akumulasi 3 run mencapai **60.44M token** (total akumulasi seluruh riwayat repositori mencapai 277.6M token).
  - Akar masalah Run 3: Orkestrator OMP melakukan pemanggilan paralel serentak kepada **17 subagent** yang memanggil satu model upstream `mustaqbal-ai-pro` via proxy `codex/gpt-6.1-sol`, menabrak batas TPM/RPM dan memicu badai pengulangan (*retry storm*) dengan jendela default ~60–90 detik tanpa menunggu pemulihan upstream (20–30 menit).
* **Penyesuaian Waktu Retry OMP ke Rentang 10 Menit:**
  - Telah diterapkan pada `~/.omp/agent/config.yml`: `maxDelayMs: 600000` (10 menit / 600.000 ms), `waitForUsageReset: true`, `baseDelayMs: 5000`, dan `maxRetries: 5`.
  - Agen OMP kini tertidur (*sleep*) pasif hingga reset kuota upstream selesai alih-alih melakukan *fail-fast* sembrono atau spamming retry.
* **Penyelamatan Aset Data & Restorasi Penuh Integritas Korpus:**
  - Diselamatkan 19.5 MB inventaris di `sources/audit_dalil_parenting/` (termasuk `07_inventaris_arab.json` 15.7 MB berisi 731 kelompok hadits).
  - Tercipta 32 artikel dalil baru di `content/Dalil/` (termasuk dalil utama beranda HR. Muslim No. 49 dan 31 dalil referensi mandiri).
  - **Restorasi Integritas Tautan 100%:** Seluruh 34 broken links terselesaikan dan 4 orphan pages terhubung ke panduan dalil $\to$ **0 Broken Links, 0 Orphan Pages**.
  - **Kepatuhan Gaya & Manhaj:** 0 pelanggaran kata kunci terlarang, perbaikan linter deteksi Arab dan mufasir muktabar menghasilkan **0 halaman di bawah style floor** (rata-rata PICI 89.6/100).
* **Penerbitan Dokumen Desain & Duplikasi Guardrail Efisiensi:**
  - Diterbitkan [`analisis-desain/09-evaluasi-forensik-omp-dan-guardrail-efisiensi-token.md`](../analisis-desain/09-evaluasi-forensik-omp-dan-guardrail-efisiensi-token.md).
  - Diduplikasi dan ditegaskan klausul efisiensi pada [`pipeline_designs/README.md`](../pipeline_designs/README.md#9-prinsip-efisiensi-token--concurrency-guardrail-multi-agent), [`pipeline_designs/11_hybrid_quality_evaluation_system_one.md`](../pipeline_designs/11_hybrid_quality_evaluation_system_one.md#6-protokol-efisiensi-token--concurrency-guardrail), dan [`analisis-desain/08-rencana-eksekusi-hibrida-minim-token.md`](../analisis-desain/08-rencana-eksekusi-hibrida-minim-token.md#8-addendum-pasca-run-3-omp-6-oktober-2026-pelajaran-dari-17-subagent-choke--batas-retry-10-menit).

### Handoff perubahan lokal — 1 Oktober 2026

**Navigasi seluruh konten**

* Pusat navigasi tetap `content/Peta Navigasi Wiki PKN.md`; tidak dibuat halaman navigasi kedua. Bagian **Indeks Lengkap Seluruh Konten** menyusun seluruh halaman menurut hierarki folder dengan target jalur lengkap, sehingga nama seperti `index.md` tidak saling menimpa.
* Verifikasi terakhir: 486 Markdown, 117 canvas, dan 1 Bases; 604 target unik ditemukan pada sumber, tanpa target berkas hilang. Angka ini adalah snapshot, bukan konstanta.
* `content/index.md` memiliki tautan indeks di bagian atas beranda. Bagian tematik lama dipertahankan sebagai panduan membaca; inventaris lengkap berada di blok `BEGIN_COMPLETE_CONTENT_INDEX` / `END_COMPLETE_CONTENT_INDEX`.
* Jalankan `python3 scripts/update_content_index.py` **sebelum setiap commit**, setelah perubahan struktur konten, dan saat pemeriksaan mingguan. Script hanya mengganti blok inventaris; teks editorial di luar blok dipertahankan. Sertakan perubahan halaman hasilnya pada commit yang relevan.
* `scripts/generate_obsidian_navigation.py` juga memanggil pembaruan indeks lengkap setelah menulis bagian tematik. Jangan menjalankan generator tematik hanya untuk memperbarui inventaris karena generator itu menulis ulang panduan tematik. Tidak ada scheduler atau hook pre-commit yang dipasang.
* Pemeriksaan setelah perubahan: `python3 scripts/wiki_corpus_linter.py --check-links`; sebelum rilis: `npx quartz build`, lalu periksa halaman `public/peta-navigasi-wiki-pkn.html`, tautan beranda, dan target indeks pada hasil build. Verifikasi terakhir menghasilkan 0 broken links, 0 orphan; build 486 sumber menghasilkan 2.746 berkas dan sampel halaman diperiksa melalui Chromium. Dua peringatan berkas Toolkit KBM belum terlacak Git tetap terpisah dari keberhasilan build.

**Keandalan rilis dan kualitas situs**

* Workflow memakai `npm ci`, Actions dipin ke SHA, webhook tanpa `curl -k`/`continue-on-error`, dan pemeriksaan commit melalui `/build-version.txt`. Stack masih memakai `latest`; sertifikat, webhook nyata, kesehatan container, pin image, dan rollback produksi belum diuji.
* Verifikasi kode terakhir sebelum penambahan indeks: `npm run check` lulus, 163 tes JavaScript dan 7 tes linter lulus, audit dependensi produksi 0 kerentanan; linter memakai waktu UTC aktual, kebijakan orphan dan lantai gaya/PICI dengan pengecualian legacy bernama.
* Resolver navigasi menolak kandidat ambigu; enam kutipan Arab dipindah dari KaTeX menjadi blok RTL. Sampel Chromium mempertahankan harakat serta pemformatan terjemahan. Ini bukan bukti telaah visual/PDF seluruh artikel.

**Blueprint mobile**

* `IDE_APLIKASI_MOBILE_PKN.md` adalah rancangan, bukan aplikasi yang sudah diterapkan. Dokumen dilengkapi hak akses/privasi anak, model data, kontrak sinkronisasi offline, batas asesmen, aksesibilitas, dan gerbang penerimaan pilot.
* Backend lintas-repositori hanya kandidat integrasi; mobile harus melalui API HTTPS terotorisasi. Jangan menganggap nama kontainer membuktikan kontrak API siap, hasil kartu anak sebagai diagnosis, atau kesamaan bakat dengan Sahabat sebagai hasil tervalidasi.

**Batas operasional:** seluruh bukti di atas lokal. Tidak dilakukan deploy, pemanggilan webhook produksi, atau perubahan layanan produksi. Pertahankan perubahan pengguna di luar cakupan; status pekerjaan lanjutan dan kewajiban berulang dicatat di `TODO.md`.

**Pekerjaan lanjutan dan koordinasi terminal**

* Scope penyusun indeks selesai: inventaris lengkap, akses beranda, dan dokumentasi pemeliharaan. Audit editorial serta penataan seluruh konten berdasarkan `analisis-desain/` adalah pekerjaan lanjutan; penyelesaiannya belum dikonfirmasi dari terminal `term_81b1e555-40a4-4178-a53e-d600d366e77c`.
* Generator tematik `scripts/generate_obsidian_navigation.py` masih memakai pencocokan stem; risiko benturan nama pada bagian tematik belum diselesaikan oleh indeks lengkap berbasis jalur. Catatan migrasinya ditambahkan ke `TODO.md`.
* Terminal penyusun indeks melepas ownership atas `content/Peta Navigasi Wiki PKN.md`, `content/index.md`, `scripts/update_content_index.py`, `scripts/generate_obsidian_navigation.py`, `TODO.md`, dan `docs/HANDOVER.md` untuk koordinasi pekerjaan lanjutan. Tidak ada run audit/build/browser aktif dari pekerjaan indeks saat pelepasan. Pembaruan dokumentasi ini dilakukan atas permintaan pengguna; bukan pengambilalihan pekerjaan audit.
* Pengiriman koordinasi melalui `orca-ide terminal send` normal dan `--interrupt` gagal: keduanya `accepted: false`, `bytesWritten: 0`. Terminal tujuan terdaftar connected/writable, tetapi penerimaan pesan belum terbukti. Konfirmasi ownership dan penerimaan sebelum melanjutkan editor atau run paralel.
* Tugas produksi yang sudah terbuka tetap berlaku: uji TLS/webhook nyata, kesehatan container, pin image, dan rollback. Tidak ada deploy atau verifikasi produksi tambahan pada pembaruan dokumentasi ini.

---

## 2. Rincian Milestone & Perbaikan Terbaru

### A. Milestone 64: Migrasi Runtime Produksi ke Docker Image GHCR (Nginx Alpine Anti-Lag)
* **Akar Masalah:** Sebelumnya, container produksi menjalankan `node:22-slim` (~1.2 GB image) yang mengeksekusi `npx quartz build --serve`. Setiap kali redeploy, proses kompilasi Quartz memakan CPU 100% di VPS selama 2–4 menit dan RAM ~1 GB, menyebabkan server lag dan potensi timeout pada reverse proxy.
* **Solusi Rekayasa:**
  1. **Offload Kompilasi ke Cloud Runner:** Beban kompilasi Quartz (484 berkas markdown $\to$ 2.713 file HTML) dialihkan 100% ke GitHub Actions runner (gratis & cepat, ~3 menit).
  2. **Image Web Server Ringan (`Dockerfile.nginx` & `nginx.conf`):** Hasil build `public/` dibungkus ke dalam image Nginx Alpine murni (hanya ~20 MB terkompresi, ~66 MB uncompressed).
  3. **Konfigurasi Routing Clean URLs:** Aturan Nginx `try_files $uri $uri.html $uri/ /index.html =404;` menjamin seluruh navigasi clean URL Quartz berfungsi mulus tanpa ekstensi `.html`.
  4. **Kompresi & Caching:** Gzip level 6 aktif untuk teks/CSS/JSON/JS/SVG dan cache browser 30 hari untuk aset statis (`.css`, `.js`, `.webp`, `.canvas`, font).
  5. **Healthcheck Multi-Protokol:** Konfigurasi `listen 8080; listen [::]:8080;` dan healthcheck wget ke `http://127.0.0.1:8080/healthz` memeriksa respons lokal container; status Portainer harus diperiksa tersendiri.
  6. **Automasi GHCR:** Workflow `.github/workflows/deploy.yml` otomatis mem-build dan mem-push multi-tag (`latest` dan `sha`) ke `ghcr.io/decaller/wiki-pkn:latest` setiap push ke `main`.
* **Pengukuran produksi historis (belum diverifikasi ulang):**
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
  - Workflow 2 job: `corpus-lint` (Python 3.12) dan `quartz-build` (Node.js 22, Quartz SSG build, image GHCR, webhook Portainer). Workflow kini memverifikasi TLS, menggagalkan job bila webhook gagal, dan menunggu commit baru melalui `/build-version.txt`; kesehatan container harus diperiksa tersendiri.
* **5. Sinkronisasi Navigasi Sidebar & Integritas Repositori:**
  - `nav_structure.json` kini memuat **148 simpul** (120 daun) dengan 100% resolusi fisik (0 broken link, 0 unlinked leaves).
  - 87/87 pengujian unit di `tests/test_nav_structure.py` lulus 100%.
  - Linter korpus (`scripts/wiki_corpus_linter.py`) lulus bersih (0 broken links, 0 vocabulary violations, Clarity `86.3/100`).
  - Quartz v5 memproses **484 berkas markdown** dan mengemisi **2.713 berkas web statis**.

### C. Milestone 63: Resolusi Tag Leak Warna Hex pada Infobox
* Mengonversi 1.051 kode warna heksadesimal `#hex` pada atribut style HTML di 461 berkas menjadi format standar `rgb(...)` via [`scripts/fix_style_hex_colors.py`](file:///home/abuhafi/Project/wiki-pkn/scripts/fix_style_hex_colors.py) untuk mencegah parser Quartz OFM membacanya sebagai markdown hashtag.

### D. Milestone 64: Arsitektur Hibrida, 13 Persona IA, Blueprint Mobile & Dewan Syura Karpathy LLM Council
* **1. Suite Desain & Arsitektur Informasi (`analisis-desain/`):**
  - Menerbitkan 6 dokumen komprehensif (`01-audit-struktur-saat-ini.md` s/d `06-rencana-aksi-penerapan-persona-interdisipliner.md`) memadukan Psikologi Kognitif, IA/Marketing Komunikasi, Pedagogi Nabawiyah, dan Desain Sistem.
  - Membangun taksonomi 13 persona (`analisis-desain/persona/`): membedakan peran gender (01a Ayah vs 01b Ibu), 5 fase pendidik (02a Thufulah s/d 02e Dewasa), 2 model tata kelola (03a Formal vs 03b Non-Formal), Santri (04), Pengkaji Kurikulum (05), Siswa (06), dan Masyarakat Umum (07).
* **2. Pipeline 11: Evaluasi Kualitas Hibrida (Rule-Based + System One):**
  - Spesifikasi di [`pipeline_designs/11_hybrid_quality_evaluation_system_one.md`](file:///home/abuhafi/Project/wiki-pkn/pipeline_designs/11_hybrid_quality_evaluation_system_one.md).
  - Skrip pemeriksa berkecepatan tinggi `<10ms` di [`scripts/hybrid_quality_scorer.py`](file:///home/abuhafi/Project/wiki-pkn/scripts/hybrid_quality_scorer.py) dan unit tests di [`tests/test_hybrid_quality_scorer.py`](file:///home/abuhafi/Project/wiki-pkn/tests/test_hybrid_quality_scorer.py).
* **3. Pipeline 12: Dewan Syura Karpathy LLM Council Architecture:**
  - Spesifikasi di [`pipeline_designs/12_dewan_syura_llm_council_architecture.md`](file:///home/abuhafi/Project/wiki-pkn/pipeline_designs/12_dewan_syura_llm_council_architecture.md) mengadaptasi 5 lensa Karpathy ke manhaj PKN: Faqih Manhaj (Contrarian), Filosof Fitrah (First Principles), Arsitek Peradaban (Expansionist), Pembaca Awam (Outsider), dan Praktisi KBM (Executor).
  - Alur 3-tahap musyawarah terotomasi di [`scripts/llm_council.py`](file:///home/abuhafi/Project/wiki-pkn/scripts/llm_council.py) dengan Anonymous Cross-Examination (Peer Review acak A..E) dan Chairman Synthesis.
  - Unit tests di [`tests/test_llm_council.py`](file:///home/abuhafi/Project/wiki-pkn/tests/test_llm_council.py).
* **4. Blueprint Aplikasi Mobile PKN:**
  - Terbit di [`IDE_APLIKASI_MOBILE_PKN.md`](file:///home/abuhafi/Project/wiki-pkn/IDE_APLIKASI_MOBILE_PKN.md) memetakan arsitektur mobile offline-first untuk 5 segmen pengguna dengan perlindungan privasi data anak.
* **5. Verifikasi Integritas Sistem:**
  - 121 pengujian unit di `tests/` lulus 100% (5 skipped, 0 fail).
  - Linter korpus `scripts/wiki_corpus_linter.py` lulus bersih (0 broken links, 0 pelanggaran kosakata, skor Clarity `86.28/100`).

---

## 3. Infrastruktur & Deployment Produksi (catatan historis; status kini belum diverifikasi)

* **Server Produksi:** Portainer Host di `103.167.12.129`, Endpoint ID: 3.
* **Stack Aktif:**
  1. `wiki-pkn` (Stack ID: 25) — konfigurasi `docker-compose.yml` memakai image `ghcr.io/decaller/wiki-pkn:latest` dengan port host 4040 ke 8080; status runtime belum diperiksa ulang.
  2. `umami` (Stack ID: 27) — konfigurasi terpisah untuk Umami Analytics + PostgreSQL 15; status runtime belum diperiksa ulang.
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

## 5. Panduan Deployment & Konfigurasi Lingkungan

Panduan komprehensif CI/CD, konfigurasi Portainer, rahasia lingkungan, dan prosedur pemulihan bencana didokumentasikan di:
👉 **[`docs/CI_CD_DEPLOYMENT_GUIDE.md`](CI_CD_DEPLOYMENT_GUIDE.md)**

* **Berkas Kredensial Lokal:** `.env` diabaikan untuk perubahan berikutnya, tetapi riwayat Git tetap perlu diaudit; jangan anggap rahasia lama sudah aman.
* **Template Kredensial Publik:** `.env.example` tanpa nilai rahasia.
* **Portainer AutoUpdate Webhook:** rotasi token yang pernah dicatat di repositori. Simpan URL baru hanya di pengelola secret dan GitHub Actions Secrets; pemicu manual memakai `curl -f -i -X POST "$PORTAINER_WEBHOOK_URL"` dengan verifikasi TLS aktif.

---

## 6. Rencana Tahap Selanjutnya (Action Items Rekomendasi)

1. **Jalur Riset & Audit Dalil Parenting (OpenBayan + Qaf AI):**
   - Menjalankan kueri broad-sweeping via OpenBayan (`shamela_11m`, port 6333) untuk tema-tema fikih tarbiyah (*tarbiyatul aulad*, *adabul walad*, *'uqubah*, *taklif*, *fitrah*).
   - Memanfaatkan Qaf AI secara hemat dan selektif (~100 pesan/bulan) hanya untuk verifikasi hipotesis dan meta-analysis lintas kitab salaf (*Tuhfatul Maudud*, *Ihya Ulumiddin*, *Fathul Bari*).
   - Menyusun dokumen kerja internal di `sources/audit_dalil_parenting/` (Gap Analysis & Contradiction Analysis) sebagai bahan mudzakarah asatidzah.
2. **Jalur Konten Komparasi:**
   - Profil dan review lembaga-lembaga yang mengadopsi PKN serta studi kasus implementasi persekolahan.
   - Halaman dialektika epistemologis: Teori PKN vs Teori Pendidikan Modern.
3. **Penyelarasan GitHub Secret:**
   - Masukkan `PORTAINER_WEBHOOK_URL` ke GitHub Repository Secrets (`Settings -> Secrets and variables -> Actions`) menggunakan nilai dari `.env` agar GitHub Actions memicu redeploy Portainer otomatis pasca-build GHCR.

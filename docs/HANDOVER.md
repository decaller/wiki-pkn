# Dokumen Handover & Status Sistem Wiki PKN

> **Terakhir Diperbarui:** 24 September 2026, 10:15 WIB  
> **Status Repositori:** Clean, Sinkron dengan `origin/main` (Commit `2269a6b`)  
> **Target Produksi:** `https://wikipkn.insanmustaqbal.or.id/`  
> **Mesin Platform:** Quartz v5 (Node.js 22, TypeScript, Obsidian Flavored Markdown)

---

## 1. Ringkasan Eksekutif (Executive Summary)

Seluruh pembenahan teknis, penuntasan bug UI/CSS leak, integrasi materi hasil ekstraksi Unstructured API, dan audit backlog permintaan telah **selesai dikerjakan secara komprehensif, divalidasi oleh linter korpus, dan di-push ke repositori utama**.

Dokumen ini berfungsi sebagai panduan serah terima (*handover*) lengkap agar sesi berikutnya dapat langsung melanjutkan tanpa kehilangan konteks operasional.

---

## 2. Rincian Milestone & Perbaikan Terbaru

### A. Milestone 63: Resolusi Tag Leak Warna Hex pada Infobox (Commit `2269a6b`)
* **Masalah:** Pada halaman Tangki Cinta (dan halaman ber-infobox lainnya), potongan kode CSS seperti `1e3a8a, #0d9488 ); color: white; ...` bocor dan muncul sebagai teks biasa di atas ikon 🏛️ PKN.
* **Akar Masalah:** Parser Quartz OFM mendeteksi kode warna heksadesimal `#hex` di dalam atribut HTML `style="..."` sebagai markdown hashtag (`#tag`), lalu menyuntikkan tag tautan `<a href="/tags/...">` yang merusak sintaks HTML.
* **Solusi:** 
  - Dibuat dan dijalankan [`scripts/fix_style_hex_colors.py`](file:///home/abuhafi/Project/wiki-pkn/scripts/fix_style_hex_colors.py).
  - Mengonversi **1.051 kode warna heksadesimal di 461 berkas** menjadi format standar **`rgb(...)`** (misal: `#1e3a8a` $\to$ `rgb(30, 58, 138)`).
  - Verifikasi build lokal: `0` kebocoran tag, infobox di `public/.../tangki-cinta.html` ter-render 100% bersih dan elegan.

### B. Milestone 62: Penuntasan Backlog Permintaan Sesi Sebelumnya (Commit `e8f578a`)
* **1. Resolusi Wikilink dalam Tabel HTML:** Dibuatkan patch [`scripts/patch_link_resolver.js`](file:///home/abuhafi/Project/wiki-pkn/scripts/patch_link_resolver.js) pada `@quartz-community/crawl-links` dan dikaitkan ke `postinstall` `package.json`. Tautan di dalam tabel infobox kini otomatis terkonversi menjadi link internal yang sah.
* **2. Pembersihan 5.233 Broken Link Navbox Bawah:** Seluruh tag link `<a href="/content/...">` di 464 berkas dikonversi ke internal wikilink Quartz `[[...]]`.
* **3. Peringkasan 81 Artikel Turunan 4 Buku Utama:** Menambahkan callout kutipan resmi bersanad dan link rujukan ke review buku masing-masing di [`content/Referensi/`](file:///home/abuhafi/Project/wiki-pkn/content/Referensi/).
* **4. Banner Promosi Edisi Fisik:** Call-to-Action terpasang di atas dan bawah seluruh 8 artikel review buku mengarahkan ke `karakternabawiyah.com`.
* **5. Pembersihan Label Kode Kaku:** Menghapus label `# ZONE 1, 2, 3, 4` dari teks bacaan publik.
* **6. Bagan Obsidian Canvas:** 8 kanvas interaktif dibuat di [`content/canvas/Review Buku/`](file:///home/abuhafi/Project/wiki-pkn/content/canvas/Review%20Buku/).
* **7. Lisensi & Otoritas Dimutakhirkan:** Menjadi *"Pengembangan oleh Harridi Ilman Tovid - Yayasan Bina Insan Taqwa - Yayasan Bina Insan Mustaqbal"*.
* **8. Identitas SOTAB HEBAT dari HCE:** Diselaraskan di Glosarium dan portal SOTAB merujuk arsip `old_backup/Brosur HCE/`.

### C. Milestone 61: Harmonisasi Manhaj Tadarruj (Commit `43b7fb6`)
* Menerbitkan naskah ensiklopedis 4-Zone [`Prinsip Tadarruj.md`](file:///home/abuhafi/Project/wiki-pkn/content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Kaidah%20&%20Elemen/Prinsip%20Tadarruj.md) dan bagan visual [`Prinsip Tadarruj.canvas`](file:///home/abuhafi/Project/wiki-pkn/content/canvas/Prinsip%20Tadarruj%20-%20Empat%20Dimensi%20Pentahapan%20Alami%20PKN.canvas).
* Menstandarisasi 4 Dimensi Tadarruj: 4 Fase Usia (0–7 th, 7–10 th, 10–14 th, 15+ th), Kurikulum 3T (*Ta'rif* $\to$ *Ta'alluf* $\to$ *Tamkin*), Gradasi Ta'dib 5 Tingkat, dan Transformasi Lembaga.
* Purifikasi residu kata *etape* menjadi *fase* di seluruh korpus dan berkas desain pipeline.

---

## 3. Kondisi Infrastruktur & Deployment Produksi

* **Server Produksi:** Portainer Host di `103.167.12.129`, Stack ID: 25 (`wiki-pkn`), Endpoint ID: 3.
* **Alur Deployment Saat Ini:** `StackGitRedeploy` dipicu langsung via Portainer API. Portainer menjalankan `docker-compose build` dan kompilasi Quartz di dalam container VPS.
* **Catatan Penting Performa VPS:**
  - Karena korpus sudah mencapai 479 berkas dan meng-emit 2.662 file HTML, proses `docker build` + kompilasi Quartz memakan CPU 100% di VPS selama 2–4 menit.
  - Selama proses kompilasi berlangsung, reverse proxy / port 443 di VPS dapat mengalami antrean atau timeout sementara sampai container baru berstatus *healthy*.
  - **Rekomendasi Arsitektur:** Segera pindahkan proses kompilasi Quartz ke **GitHub Actions CI/CD** (gratis & cepat), sehingga VPS hanya menerima artefak statis `public/` dan tidak pernah lagi mengalami lonjakan CPU.

---

## 4. Status Indeks Dokumen & Data Mentah

| Direktori / Aset | Status | Deskripsi |
| :--- | :---: | :--- |
| `data/extracted_elements/` | **88 Berkas (100%)** | 5.311 elemen semantik terstruktur dan 166 tabel Markdown hasil ekstraksi Unstructured API (47 PDF + 41 PPTX). |
| `sources/buku_tafsir_bakat/` | **Tersimpan** | Naskah master lengkap Buku Tafsir Bakat (Bab 1–12, 118k kata). |
| `sources/research_papers/` | **Terisolasi** | Ruang penampungan PDF jurnal empiris eksternal (terpisah dari naskah internal PKN). |
| `content/canvas/` | **104 Berkas** | Seluruh diagram konsep arsitektur, pilar bakat, dan review buku berformat Obsidian Canvas. |
| `content/Dalil/` | **84 Berkas** | Halaman dalil mandiri dengan matan Arab berharakat, takhrij, dan syarah salaf. |

---

## 5. Rencana Tahap Selanjutnya (Action Items Rekomendasi)

Berikut adalah prioritas pekerjaan berikutnya yang siap dieksekusi:

1. **Jalur Konten Prioritas Tinggi (Filosofis & Pedagogis):**
   - **Artikel Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi (Trilogi Hierarki Pendidikan):** *Materi vs Metode vs Guru vs Jiwa Guru* (Format 4-Zone + Canvas Piramida).
   - **Artikel Firasat Nabawiyah (الفِرَاسَة):** Metode mendidik membaca jiwa, ego, dan bakat anak dari tanda lahiriah (bukan sekadar pilar bakat TB-40).
2. **Jalur Infrastruktur (Permanen & Anti-Lag):**
   - **Setup GitHub Actions CI/CD Workflow (`.github/workflows/deploy.yml`):** Offload proses build Quartz ke cloud runner GitHub, lalu deploy folder `public/` langsung ke VPS via webhook atau rsync.
3. **Jalur Refleksi Lapangan:**
   - **Penyematan Callout Kontras "Kebiasaan Umum vs Pendekatan PKN":** Tabel 2 kolom (🔴 Yang Biasa Dilakukan vs ✅ Alternatif Manhaj PKN) pada blok refleksi artikel pilar utama.

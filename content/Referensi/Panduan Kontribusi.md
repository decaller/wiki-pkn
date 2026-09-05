---
title: "Panduan Kontribusi"
description: "Panduan lengkap kontribusi pengembangan Wiki PKN: kloning repositori GitHub, pengelolaan naskah menggunakan Obsidian, standar dalil, dan tata cara membuat Pull Request (PR)."
aliases:
  - Kontribusi
  - Cara Kontribusi
  - Panduan Kontributor
tags:
  - panduan
  - kontribusi
  - github
  - obsidian
  - pedoman-penulisan
---

![[assets/banners/banner_panduan_rpp_observasi.webp]]
*Gambar: Kolaborasi Terbuka Membangun Khazanah Pendidikan Karakter Nabawiyah*

> [!info] Semangat Gotong Royong Amal Jariyah
> *"Sebaik-baik manusia adalah yang paling bermanfaat bagi sesamanya."* (HR. Ahmad dan Ath-Thabrani)  
> Wiki Pendidikan Karakter Nabawiyah (PKN) dikelola sebagai proyek berbasis pengetahuan terbuka (*open knowledge base*). Setiap asatidz, pendidik, orang tua, peneliti, dan pengembang diundang untuk bersama-sama menyempurnakan, merapikan, dan memperkaya basis data ini demi kemaslahatan umat.

---

# Panduan Lengkap Kontribusi Wiki PKN

Dokumen ini memandu Anda langkah demi langkah untuk berpartisipasi dalam pengembangan materi Wiki PKN—mulai dari persiapan alat, penyuntingan lokal dengan Obsidian, hingga pengajuan revisi melalui GitHub.

---

## 🛠️ 1. Prasyarat & Persiapan Alat

Sebelum memulai, pastikan perangkat komputer Anda telah terpasang:

1. **Git:** Perangkat lunak kendali versi (*version control*). [Unduh Git](https://git-scm.com/).
2. **Akun GitHub:** Akun terdaftar di [GitHub](https://github.com/) untuk mengajukan kontribusi (*Pull Request*).
3. **Obsidian (Sangat Disarankan):** Aplikasi catatan berbasis Markdown lokal yang kaya fitur dan terintegrasi mulus dengan struktur berkas Wiki PKN. [Unduh Obsidian](https://obsidian.md/).
4. **Node.js LTS (Opsional):** Jika Anda ingin menjalankan server pratinjau Quartz secara lokal di komputer Anda. [Unduh Node.js](https://nodejs.org/).

---

## 📥 2. Mengklona Repositori (Clone Repository)

Wiki PKN di-hosting di GitHub pada repositori publik: `https://github.com/decaller/wiki-pkn`.

### Langkah-langkah Kloning:

1. Buka terminal (Linux/macOS) atau Git Bash / PowerShell (Windows).
2. Pilihlah direktori tempat Anda biasa menyimpan proyek, lalu jalankan perintah klon:

```bash
git clone https://github.com/decaller/wiki-pkn.git
cd wiki-pkn
```

3. Periksa status berkas untuk memastikan repositori berada dalam kondisi bersih (*clean working tree*):

```bash
git status
```

---

## 💎 3. Menggunakan Obsidian untuk Menulis & Mengedit

Seluruh naskah materi berada di dalam folder `content/`. Struktur folder ini dirancang untuk bekerja secara instan sebagai sebuah **Obsidian Vault**.

### Langkah Membuka di Obsidian:

1. Buka aplikasi **Obsidian**.
2. Pada layar pembuka, pilih **"Open folder as vault"** (Buka folder sebagai brankas).
3. Arahkan dan pilih folder root repositori Anda (`wiki-pkn`).
4. Obsidian akan membaca seluruh struktur folder, artikel markdown, dan lampiran visual di `assets/`.

### Rekomendasi Konfigurasi Obsidian:

* **Format Tautan Internal (Internal Link Format):**
  Masuk ke menu *Settings -> Files and links -> New link format*, pilih **Wikilink (Shortest path when possible)**. Ini memastikan format tautan `[[Nama Artikel]]` bekerja presisi di Quartz.
* **Folder Lampiran (Attachment Folder Path):**
  Pastikan folder lampiran mengarah ke `assets/` agar berkas gambar/banner tersimpan seragam.
* **Canvas Interaktif (.canvas):**
  Anda dapat membuat peta konsep baru atau membuka kanvas yang sudah ada di folder `content/canvas/` untuk memvisualisasikan keterkaitan antar konsep secara spasial.

---

## ⚖️ 4. Standar Penulisan & Kaidah Ilmiah PKN

Agar kualitas naskah tetap terjaga dan selaras dengan manhaj, setiap kontributor diharapkan mematuhi panduan berikut:

### A. Kaidah Non-Destruktif (*Zero Deletion*)
> [!warning] Kaidah Keutuhan Data
> **Jangan pernah menghapus materi lama yang valid!**  
> Prinsip kontribusi Wiki PKN adalah melengkapi, memperjelas, menyusun ulang (*restructure*), memutakhirkan dalil, atau menambahkan studi kasus. Jika ada bagian yang kurang tepat, diskusikan melalui GitHub Issues sebelum menghapus narasi yang sudah ada.

### B. Otentisitas Dalil & Sanad
* **Al-Qur'an:** Tuliskan lafaz Arab berharakat lengkap (Rasm Utsmani), terjemahan resmi bahasa Indonesia, dan keterangan nama surat serta nomor ayat: *(QS. Al-Baqarah [2]: 155)*.
* **Hadits:** Sebutkan rawi hadits (HR. Bukhari, Muslim, Abu Dawud, dll), nomor hadits, serta derajat keshahihannya berdasarkan pentahqiq mu'tabar.

### C. Anatomi Standar Artikel
Setiap artikel materi sebaiknya memiliki elemen:
1. **Frontmatter YAML:**
   ```yaml
   ---
   title: Judul Artikel Bersih
   description: Ringkasan 1-2 kalimat mengenai fokus materi.
   tags:
     - tag-tema-1
     - tag-tema-2
   ---
   ```
2. **Banner Ilustrasi:** Disematkan di awal artikel: `![[assets/banners/nama_banner.webp]]`.
3. **Isi Pembahasan Utama:** Terstruktur dengan heading `##`, `###`, poin teratur, dan bagan/tabel jika diperlukan.
4. **Callout Refleksi & Mitigasi:** Diletakkan di bagian akhir konten artikel (sebelum materi presentasi / PPT):
   - `> [!info] Refleksi Lapangan: Realitas Penerapan ...`
   - `> [!warning] Peringatan Risiko: Jebakan Formalitas ...`
   - `> [!tip] Tips Praktis Pengasuhan ...`
5. **Media Presentasi & Slide Interaktif (PPTX):** Disematkan di bagian penutup artikel.

---

## 🚀 5. Alur Pengajuan Revisi: Branch & Pull Request (PR)

Setelah Anda selesai melakukan perubahan atau penambahan materi di komputer lokal, ikuti alur Git berikut untuk mengajukan kontribusi ke repositori utama:

### Langkah 1: Buat Cabang Kerja (*Branch*) Baru
Jangan melakukan perubahan langsung di cabang `main`. Buat branch deskriptif:

```bash
git checkout -b konten/tambah-studi-kasus-tamyiz
```

### Langkah 2: Periksa dan Commit Perubahan
Periksa berkas mana saja yang Anda ubah dengan `git status` dan `git diff`:

```bash
git status
git add content/
git commit -m "feat(konten): menambahkan studi kasus pengasuhan fase tamyiz"
```

*Gunakan format commit konvensional:*
- `feat(konten): ...` untuk penambahan materi/artikel baru.
- `fix(dalil): ...` untuk perbaikan kutipan ayat/hadits/salah ketik.
- `docs(navigasi): ...` untuk perbaikan daftar indeks atau tautan.

### Langkah 3: Push ke GitHub Anda & Buat Pull Request
1. Unggah cabang baru ke repositori Anda:
   ```bash
   git push origin konten/tambah-studi-kasus-tamyiz
   ```
2. Buka halaman repositori di peramban: [https://github.com/decaller/wiki-pkn](https://github.com/decaller/wiki-pkn).
3. Anda akan melihat notifikasi berwarna kuning: **"Compare & pull request"**. Klik tombol tersebut.
4. Tuliskan deskripsi ringkas mengenai apa yang Anda tambahkan/perbaiki, alasan perubahan, dan sumber rujukan yang digunakan.
5. Klik **"Create Pull Request"**.

---

## 🔍 6. Proses Tinjauan (*Review & Merge*)

Setelah Pull Request diajukan:
1. Sistem CI/CD otomatis akan menguji build Quartz untuk memastikan tidak ada kesalahan sintaksis atau broken links.
2. Tim kurator dan asatidz akan meninjau substansi materi dan memberikan masukan bila diperlukan.
3. Setelah disetujui (*approved*), perubahan akan digabungkan (*merged*) ke cabang `main` dan otomatis terbit ke situs web resmi **wikipkn.insanmustaqbal.or.id**.

*Jazakumullahu khairan atas partisipasi Anda dalam membangun peradaban generasi Nabawiyah!*

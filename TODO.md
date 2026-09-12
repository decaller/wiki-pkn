# Roadmap & TODO List Wiki-PKN (Pendidikan Karakter Nabawiyah)

Dokumen ini melacak daftar rencana pengembangan konten, pembenahan teknis/UI, editorial, serta perangkat pendukung implementasi Wiki PKN.

---

## Ringkasan Status

- **Status Umum:** Dalam Pengembangan Aktif
- **Target Utama:** Optimalisasi UX mobile, pengayaan database materi/template, peningkatan readability, dan integrasi analitik/SEO.

---

## 1. UI / UX & Tampilan Frontend
Fokus pada perbaikan responsivitas perangkat bergerak dan visualisasi informasi.

- [ ] **Perbaikan layout kotak di mobile yang teksnya terpotong**
  - *Deskripsi:* Fix overflow/wrapping teks pada komponen box/callout/card saat dibuka di viewport mobile (layar sempit).
  - *Prioritas:* Tinggi (Bug UX)
- [x] **Pembuatan alur materi visual (folder `content_flow/`)** `[SELESAI]`
  - *Deskripsi:* Menyediakan replika korpus direktori materi PKN di folder `content_flow/` (106 berkas) berisi diagram alur materi terstruktur (Mermaid `flowchart TD`) tanpa konten teks panjang.
- [ ] **Pembuatan mind map untuk tiap halaman**
  - *Deskripsi:* Menyediakan visualisasi mind map / grafik relasi konsep pada setiap halaman materi untuk mempermudah navigasi mental pembaca.
- [ ] **Pembuatan flow pengolahan**
  - *Deskripsi:* Membuat visualisasi diagram alur proses/workflow pengolahan (mulai dari input materi, kurasi, verifikasi dalil, hingga publikasi).

---

## 2. Teknis, SEO & Analitik
Fokus pada visibilitas mesin pencari, pelacakan audiens, dan riwayat pembaruan sistem.

- [ ] **Peningkatan SEO (Search Engine Optimization)**
  - *Deskripsi:* Optimasi meta description, Open Graph tags, canonical URL, sitemap XML, dan struktur heading untuk indexing optimal di search engine. (Lihat catatan detail audit: [SEO_IMPLEMENTATION.md](file:///home/abuhafi/Project/wiki-pkn/SEO_IMPLEMENTATION.md))
- [ ] **Integrasi Page Analytics**
  - *Deskripsi:* Pemasangan analitik halaman (misal: Google Analytics, Cabin, Tinylytics, Matomo, PostHog, atau Clarity). (Lihat catatan detail implementasi: [PAGE_ANALYTICS.md](file:///home/abuhafi/Project/wiki-pkn/PAGE_ANALYTICS.md))
- [ ] **Pembuatan Halaman Rilis (Changelog / Release Notes)**
  - *Deskripsi:* Menyediakan halaman khusus yang mencatat pembaruan versi, konten baru yang ditambahkan, dan log perbaikan fitur wiki.

---

## 3. Standarisasi Bahasa, Editorial & Kualitas Penulisan
Fokus pada kejelasan kalimat, pemahaman pembaca umum, dan standardisasi istilah.

- [ ] **Pengecekan tulisan menggunakan skill Clarity ([clarity.addy.ie](https://clarity.addy.ie/))**
  - *Deskripsi:* Audit keterbacaan artikel, perbaikan kalimat berbelit (readability score), dan eliminasi ambiguitas tata bahasa.
- [ ] **Penyusunan Glosarium (Glossary) & Minimalisasi Istilah Sulit**
  - *Deskripsi:* Membuat kamus istilah khas PKN dan mengganti/menyederhanakan diksi rumit agar mudah dipahami oleh guru dan orang tua awam.

---

## 4. Pengumpulan & Kurasi Konten Inti PKN
Fokus pada pemindahan khazanah materi narasumber dan konsep-konsep pokok ke dalam wiki.

- [ ] **Kurasi materi tulisan Ustadz Bayu di grup**
  - *Deskripsi:* Mengumpulkan, menyeleksi, dan menyusun arsip materi yang pernah ditulis Ustadz Bayu di grup diskusi ke format markdown wiki yang terstruktur.
- [ ] **Penyusunan Materi Tazkiyatun Nafs**
  - *Deskripsi:* Dokumentasi konsep, tahapan, dan implementasi Tazkiyatun Nafs dalam kerangka pendidikan karakter nabawiyah.
- [ ] **Konsep Pembelajaran Alamiah**
  - *Deskripsi:* Perumusan prinsip pembelajaran alamiah berbasis fitrah belajar dan sunnatullah tumbuh kembang anak.
- [ ] **Tabel TB40**
  - *Deskripsi:* Pembuatan dan penyusunan tabel indikator/materi TB40 sebagai matriks rujukan evaluasi dan capaian.

---

## 5. Kajian Komparasi, Profil & Review Lembaga
Fokus pada telaah kritis literatur dan pemetaan ekosistem implementasi.

- [ ] **Review masing-masing buku**
  - *Deskripsi:* Ulasan mendalam, ringkasan bab, dan relevansi masing-masing buku referensi PKN/tarbiyah islamiyah.
- [ ] **Profil dan review masing-masing kegiatan**
  - *Deskripsi:* Dokumentasi format kegiatan, profil aktivitas, tujuan karakter, dan evaluasi efektivitasnya di lapangan.
- [ ] **Tabel dan profil lembaga-lembaga**
  - *Deskripsi:* Database lembaga/sekolah/pesantren yang menerapkan atau mengadopsi PKN beserta model implementasinya.
- [ ] **Contoh implementasi tiap sekolah (Studi Kasus)**
  - *Deskripsi:* Dokumentasi studi kasus dan *best practices* implementasi nyata PKN di masing-masing sekolah/madrasah (adaptasi kurikulum, pembiasaan adab, manajemen kelas, dan tantangan di lapangan).
- [ ] **Kumpulan perbandingan dan review berbagai konsep**
  - *Deskripsi:* Matriks perbandingan antara konsep PKN dengan konsep-konsep pendidikan lain (konvensional, montessori, fitrah based education, dll.).

---

## 6. Template Siap Pakai & Toolkit KBM
Fokus pada operasional praktis bagi pendidik dan praktisi harian.

- [ ] **Daftar dokumen bantuan dan review masing-masing dokumen**
  - *Deskripsi:* Inventarisasi dokumen panduan/petunjuk teknis pembantu serta telaah kegunaannya.
- [ ] **Kumpulan dokumen template siap pakai**
  - *Deskripsi:* Bank dokumen siap pakai (template RPP, lembar observasi, instrumen penilaian karakter, surat, dan format laporan).
- [ ] **Prompt AI dan template pembuatan dokumen KBM**
  - *Deskripsi:* Penyusunan sistem prompt AI siap pakai bagi guru untuk mengenerate modul ajar, rencana pembelajaran, dan studi kasus berbasis PKN.
- [ ] **Kumpulan tips and trik problematika harian**
  - *Deskripsi:* FAQ dan panduan solusi praktis atas kendala harian guru/orang tua dalam menghadapi dinamika perilaku anak.

---

## 7. Ide dari AI (Usulan Pengembangan Tambahan)
Kumpulan ide dan usulan eksplorasi fitur, konten, serta teknis yang dapat dipertimbangkan untuk pengembangan wiki di masa mendatang.

### A. Pengayaan Konsep & Matriks Tumbuh Kembang
- [ ] **Matriks Karakter Berdasarkan Tahapan Usia (7 Tahun Pertama, Mumayyiz, Baligh)**
  - *Deskripsi:* Panduan target adab dan pendekatan komunikasi sesuai fase usia anak (sunnatullah tumbuh kembang).
- [ ] **Ensiklopedia Karakter Pokok & Karakter Turunan**
  - *Deskripsi:* Direktori karakter (*Shidq*, *Amanah*, *Iffah*, *Syaja'ah*, dll.) lengkap dengan dalil, indikator perilaku nyata, dan antitesisnya.
- [ ] **Modul Sinkronisasi Sekolah & Rumah (Parenting Nabawiyah)**
  - *Deskripsi:* Panduan pendampingan orang tua di rumah untuk melanjutkan pembiasaan adab dari sekolah tanpa dikotomi nilai.

### B. Instrumen Evaluasi & Asesmen Guru
- [ ] **Rubrik & Format Observasi Karakter Tanpa Angka**
  - *Deskripsi:* Evaluasi karakter berbasis narasi perkembangan dan pengamatan perilaku nyata, bukan sekadar skor angka ujian.
- [ ] **Bank Cerita Sirah & Apersepsi KBM**
  - *Deskripsi:* Kumpulan kisah Rasulullah ﷺ dan para sahabat yang dipetakan ke tema-tema pelajaran sains/sosial/matematika untuk apersepsi KBM.
- [ ] **Panduan Penanganan Kasus Khusus (Adiksi Gadget, Bullying, Tantrum)**
  - *Deskripsi:* SOP islami dan pendekatan nabawi dalam menangani pelanggaran adab atau trauma psikologis anak di lingkungan sekolah.

### C. Navigasi & Pengalaman Membaca (Knowledge Graph & UX)
- [ ] **Jalur Belajar / Reading Path untuk Pemula ("Mulai Dari Sini")**
  - *Deskripsi:* Urutan baca terkurasi bagi guru atau orang tua baru agar tidak kebingungan menjelajahi khazanah wiki.
- [ ] **Integrasi Obsidian Canvas (`.canvas`) ke Tampilan Web Interaktif**
  - *Deskripsi:* Memvisualisasikan file `.canvas` di browser secara interaktif untuk mempermudah pemahaman keterkaitan antar konsep PKN.
- [ ] **Optimasi Tipografi Teks Arab & Terjemahan**
  - *Deskripsi:* Penerapan font naskh khusus web (Amiri / Scheherazade New) dan layout dwibahasa yang nyaman dibaca di layar mobile.

### D. Fitur Teknis Platform & Distribusi
- [ ] **Fitur Ekspor PDF Rapi Siap Cetak (Print Stylesheet)**
  - *Deskripsi:* Cetak halaman materi / RPP / modul dalam format A4 bersih tanpa elemen navigasi website.
- [ ] **Dukungan Akses Offline / PWA (Progressive Web App)**
  - *Deskripsi:* Memungkinkan wiki diakses tanpa koneksi internet stabil bagi sekolah/guru di daerah minim sinyal.
- [ ] **Taksonomi & Filter Tag Khusus Dalil**
  - *Deskripsi:* Pencarian dan pemfilteran dalil berdasarkan surah, topik adab, kualitas/sanad hadits, atau kata kunci tematik.

### E. Kolaborasi & Tata Kelola Komunitas
- [ ] **Pedoman Kontributor (Style Guide Penulisan Wiki)**
  - *Deskripsi:* Standarisasi format penulisan, sitasi dalil, dan struktur markdown bagi asatidzah/guru yang menyumbang materi.
- [ ] **Direktori Narasumber & Trainer PKN**
  - *Deskripsi:* Daftar kontak atau lembaga penyedia workshop, sertifikasi, dan pelatihan implementasi PKN untuk sekolah.

### F. Integrasi Multimedia & Perpustakaan Digital
- [ ] **Audio Player Kajian Tersemat (Embedded Audio)**
  - *Deskripsi:* Pemutar audio ringkas pada halaman materi agar pembaca bisa mendengarkan rekaman kajian Ustadz Bayu / narasumber sembari membaca transkrip.
- [ ] **Viewer Presentasi Interaktif di Web (Slide Deck Viewer)**
  - *Deskripsi:* Konversi materi presentasi di folder `presentations/` menjadi slide web interaktif (Reveal.js) siap tampil untuk media ajar kelas.
- [ ] **PDF Deep-Linking (Tautan Langsung ke Halaman Dokumen/Kitab)**
  - *Deskripsi:* Integrasi pipeline OCR `searchable_pdfs` agar kutipan langsung membuka halaman buku atau kitab rujukan asli.

### G. AI & Otomasi Pipeline Konten
- [ ] **Asisten Tanya Jawab PKN (Chatbot RAG Khusus)**
  - *Deskripsi:* Fitur AI pintar pencari solusi yang menjawab pertanyaan seputar PKN berbasis dokumen dan dalil di wiki ini (*grounded QA*).
- [ ] **Otomasi Transkripsi Kajian Suara (Speech-to-Text Pipeline)**
  - *Deskripsi:* Pipeline AI (Whisper) untuk transkripsi otomatis rekaman audio kajian/halaqah menjadi draf tulisan terstruktur.
- [ ] **Skrip Validasi Takhrij & Nomor Dalil Otomatis**
  - *Deskripsi:* Pengecekan otomatis (CI/hook) untuk validasi format nomor surah:ayat dan periwayat hadits saat artikel baru ditambahkan.

### H. Program Pembiasaan Santri & Kemitraan Wali Murid
- [ ] **Format Jurnal Mutaba'ah Yaumiyah (Buku Amalan Harian Terintegrasi)**
  - *Deskripsi:* Template jurnal harian santri (shalat berjamaah, dzikir, tilawah, adab, birrul walidain) yang terhubung ke indikator PKN.
- [ ] **Program "Tantangan Karakter Pekanan" (Weekly Character Campaign)**
  - *Deskripsi:* Panduan program tematik mingguan di sekolah dan rumah (contoh: Pekan Menjaga Lisan, Pekan Kejujuran, Pekan Berbagi).
- [ ] **Kartu Kasus Lapangan & Diskusi Guru (Teacher Case Study Cards)**
  - *Deskripsi:* Kartu simulasi studi kasus harian untuk bahan *morning briefing* guru dalam menyikapi dinamika adab santri.

### I. Visualisasi Media & Aksesibilitas Pembaca
- [ ] **Infografis Ringkasan Siap Sebar (Format WhatsApp/Media Sosial)**
  - *Deskripsi:* Desain ringkasan 1 lembar visual (1080x1080 / PDF 1 halaman) materi pokok untuk memudahkan guru menyebarkannya ke WAG wali murid.
- [ ] **Peta Pohon Sanad & Silsilah Manhaj PKN**
  - *Deskripsi:* Diagram visual silsilah rujukan ilmiah dari Salafus Shalih, kitab-kitab induk tarbiyah, hingga praktisi kontemporer.
- [ ] **Fitur "Dengarkan Artikel" (Text-to-Speech) & Mode Fokus**
  - *Deskripsi:* Tombol narasi audio artikel untuk dibaca saat santai serta mode tampilan minim distraksi (fokus membaca dalil).



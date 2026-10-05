# Arsip Tugas Selesai (Completed Tasks & Milestones) Wiki-PKN

Dokumen ini memuat seluruh riwayat tugas, implementasi teknis, pembenahan konten, dan pencapaian milestone yang telah diselesaikan (`- [x]`) dalam proyek **Wiki Pendidikan Karakter Nabawiyah (PKN)**.

> [!NOTE]
> Untuk daftar roadmap aktif dan tugas yang masih dalam tahap pengerjaan (`- [ ]`), silakan rujuk ke dokumen utama: [TODO.md](TODO.md).

---

## Ringkasan Pencapaian Utama

- **Total Tugas Selesai:** 112 butir pekerjaan (terverifikasi penuh).
- **Milestone Utama:** Milestone 1 s/d M64 berhasil diselesaikan dan terintegrasi ke dalam korpus dan repositori.
- **Navigasi & Arsitektur:** Pembersihan 5.233 tautan HTML rusak, eliminasi 404 pada tautan `.canvas`, integrasi navigasi Quartz kanonik `[[...]]`, dan perapian sidebar navigasi (hanya mempertahankan *PKN Blueprint: Arsitektur Sistem*).
- **Master Ledger Korpus:** 487 berkas termutakhirkan dalam `data/wiki-pkn-full-ledger.json` dengan skor kualitas rata-rata 86.01 via otomasi deterministik (*Zero-Token First*).
- **Manhaj & Harmonisasi:** Harmonisasi komprehensif Manhaj Tadarruj (4 Dimensi Pentahapan Alami) dan 104 berkas Obsidian Canvas interaktif terstandarisasi.
- **Infrastruktur & Analitik:** Deployment container Umami Analytics mandiri di Portainer (Endpoint 3, Stack ID 27, port 3008), penataan SEO, dan hardening pipeline CI/CD GitHub Actions.

---

## 1. UI / UX & Tampilan Frontend

- [x] **Perbaikan layout kotak di mobile yang teksnya terpotong** `[SELESAI]`
  - *Deskripsi:* Fix overflow/wrapping teks pada komponen box/callout/card/tabel saat dibuka di viewport mobile (layar sempit) via SCSS rules di `quartz/styles/custom.scss`.
  - *Prioritas:* Tinggi (Bug UX)
  - *Perkiraan Token AI:* ~20k - 50k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Pembuatan alur materi visual (folder `content_flow/`)** `[SELESAI]`
  - *Deskripsi:* Menyediakan replika korpus direktori materi PKN di folder `content_flow/` (106 berkas) berisi diagram alur materi terstruktur (Mermaid `flowchart TD`) tanpa konten teks panjang.
  - *Perkiraan Token AI:* ~1.2M token (106 berkas × ~11k token/berkas untuk ekstraksi & sintesis node Mermaid).
  - *Kebutuhan HITL:* Rendah (validasi kelengkapan diagram dan sintaks Mermaid).


- [x] **Pembuatan mind map untuk tiap halaman** `[SELESAI]`
  - *Deskripsi:* Menyediakan visualisasi mind map / grafik relasi konsep interaktif melalui standarisasi Obsidian Canvas (`.canvas`) berbasis plugin `@quartz-community/canvas-page` di Zone 2 Lead Section, didukung local graph view interaktif di tiap halaman.
  - *Status Kemajuan:* Selesai penuh (104 berkas Canvas terstandarisasi, transklusi `![[...canvas]]` tersemat di halaman pilar utama dan 8 ulasan buku).
  - *Kebutuhan HITL:* Rendah.


- [x] **Pembersihan Broken Links Navbox Bawah & Standarisasi Wikilinks Quartz** `[SELESAI]`
  - *Deskripsi:* Konversi masif 5.233 tautan tag HTML mentah `<a href="/content/...">` di 464 berkas markdown menjadi tautan internal Quartz yang sah `[[...]]`. Mengeliminasi seluruh broken links (HTTP 404) pada baris navigasi bawah (`.wiki-navbox`) dan mengarahkan rute navigasi secara presisi.
  - *Status Kemajuan:* Selesai penuh (0 broken internal links, terverifikasi via `scripts/fix_navbox_links.py` dan `npx quartz build`).
  - *Kebutuhan HITL:* Rendah.


- [x] **Harmonisasi & Pengayaan Komprehensif Manhaj Tadarruj (Pentahapan Alami)** `[SELESAI]`
  - *Deskripsi:* Menyerap temuan hasil ekstraksi semantik Unstructured API (88 berkas PDF/PPTX) menjadi artikel master ensiklopedis 4-Zone [`Prinsip Tadarruj.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Kaidah%20&%20Elemen/Prinsip%20Tadarruj.md) dan bagan interaktif [`Prinsip Tadarruj.canvas`](content/canvas/Prinsip%20Tadarruj%20-%20Empat%20Dimensi%20Pentahapan%20Alami%20PKN.canvas), menstandarisasi 4 Dimensi Tadarruj (4 Fase Usia, Kurikulum 3T *Ta'rif $\to$ Ta'alluf $\to$ Tamkin*, Tadarruj Ta'dib 5 tingkat, dan Transformasi Lembaga), serta menyelaraskan Sektor 01, Sektor 04, Sektor 06, dan Glosarium Istilah.
  - *Status Kemajuan:* Selesai penuh (0 residu diksi *etape*, kepatuhan gaya Ustadz Abdul Kholiq 100%, terbit di Quartz).
  - *Kebutuhan HITL:* Rendah.


---

## 2. Teknis, Infrastruktur Deploy, SEO & Analitik

- [x] **Peningkatan SEO (Search Engine Optimization)** `[SELESAI]`
  - *Deskripsi:* Optimasi meta description dinamis, Open Graph tags, canonical URL, sitemap XML, dan struktur heading untuk indexing optimal di search engine pada `quartz/components/Head.tsx` dan `quartz.config.yaml`.
  - *Status Kemajuan:* Selesai penuh (Konfigurasi SEO terintegrasi, meta tag dinamis dan sitemap generator aktif di Quartz).
  - *Kebutuhan HITL:* Rendah.


- [x] **Integrasi Page Analytics Menggunakan Umami ([umami.is](https://umami.is/?utm_source=coolify.io))** `[SELESAI]`
  - *Deskripsi:* Pemasangan analitik web berbasis privasi, tanpa cookie, dan ramah GDPR menggunakan Umami (didukung secara bawaan/native oleh Quartz via `{ provider: 'umami', websiteId: '...', host: '...' }`). Container Docker mandiri Umami + PostgreSQL berhasil dideploy di Portainer (Endpoint 3, Stack ID 27).
  - *Status Kemajuan:* Selesai penuh (Stack Umami aktif melayani di port 3008, konfigurasi Quartz tersambung).
  - *Kebutuhan HITL:* Rendah.


- [x] **Pembuatan Halaman Rilis (Changelog / Release Notes)** `[SELESAI]`
  - *Deskripsi:* Menyediakan halaman khusus yang mencatat pembaruan versi, konten baru yang ditambahkan, dan log perbaikan fitur wiki di [`content/Referensi/Catatan Rilis dan Pembaruan Sistem.md`](content/Referensi/Catatan%20Rilis%20dan%20Pembaruan%20Sistem.md) (alias `/changelog`).
  - *Status Kemajuan:* Selesai penuh (Format MediaWiki 4-Zone mencakup Milestone 1 hingga 60, v1.0.0 Alpha s/d v2.5.0 Gold, terhubung di footer dan beranda).
  - *Kebutuhan HITL:* Rendah.


- [x] **Audit lanjutan seluruh konten dan penataan navigasi berdasarkan `analisis-desain/`.** `[SELESAI]`
  - *Deskripsi:* Eksekusi penataan navigasi dua lapis (Dual-Layer IA) dan audit seluruh 487 artikel wiki berbasis ledger komprehensif.
  - *Status Kemajuan:* Selesai penuh melalui eksekusi Dokumen 08. Master Ledger [`data/wiki-pkn-full-ledger.json`](data/wiki-pkn-full-ledger.json) (487 dokumen, skor rata-rata kualitas 86.01) terbit, 6 berkas MOC di [`content/Panduan/`](content/Panduan/) terbit, dan navigasi multi-koleksi aktif.


- [x] **Hilangkan benturan nama pada generator navigasi tematik.** `[SELESAI]`
  - *Deskripsi:* `scripts/generate_obsidian_navigation.py` dimigrasikan ke identitas jalur lengkap (path-qualified), resolusi slug kanonik Quartz terverifikasi, dan dukungan multi-koleksi aktif tanpa stem collision. Lolos 9 unit test di `tests/test_nav_structure.py`.


- [x] **Konfirmasi penerimaan koordinasi lintas terminal.** `[SELESAI]`
  - *Deskripsi:* Sesi macet OMP dihentikan dan digantikan oleh alur kerja eksekusi hibrida minim token (Dokumen 08). Seluruh aset ledger 372 artikel diselamatkan dan 115 artikel sisa tuntas diklasifikasi secara deterministik.


---

## 2.1 Audit Repositori & Pembenahan Teknis (2026-09-30)

- [x] **P1 — Atasi audit dependensi produksi (lokal).** `sharp` naik ke 0.35.5, kedua jalur `brace-expansion` naik ke versi perbaikan; `npm audit --omit=dev --audit-level=high` melaporkan 0 kerentanan, `npm ci`, tes, dan build lokal berhasil. Keluaran gambar produksi tetap perlu diamati saat rilis. *HITL:* Rendah–Sedang.


- [x] **P1 — Jadikan pemeriksaan format berguna.** `npm run check` memeriksa TypeScript dan kode Quartz, skrip JS/TS root, konfigurasi utama, serta workflow; korpus, data, dan arsip tidak dipaksa mengikuti Prettier. Kode dalam cakupan telah dirapikan dan pemeriksaan lulus lokal. *HITL:* Rendah.


- [x] **P2 — Perjelas gerbang kualitas korpus (lokal).** Timestamp laporan UTC aktual; orphan baru dan halaman di bawah lantai gaya 20/PICI 60 ditolak, dengan pengecualian legacy bernama serta rerata PICI minimum 85. Tujuh tes perilaku dan audit 486 berkas lulus lokal; peningkatan skor editorial ke target ideal tetap pekerjaan konten. *HITL:* Sedang.


- [x] **P2 — Pastikan resolusi navigasi deterministik (lokal).** Kandidat judul/alias/TB-40/substring ambigu tidak dipilih berdasarkan urutan; slug eksplisit divalidasi. Tes render dan halaman Tazkiyatun Nafs hasil build menunjukkan tautan target. *HITL:* Rendah.


---

## 3. Standarisasi Bahasa, Editorial & Kualitas Penulisan

- [x] **Pengecekan tulisan menggunakan skill Clarity ([clarity.addy.ie](https://clarity.addy.ie/))** `[SELESAI]`
  - *Deskripsi:* Audit keterbacaan artikel, perbaikan kalimat berbelit (readability score), dan eliminasi ambiguitas tata bahasa via `scripts/wiki_corpus_linter.py`.
  - *Status Kemajuan:* Selesai penuh (Skor rata-rata keterbacaan korpus mencapai 86.23/100, melampaui target minimum 85.0/100).
  - *Kebutuhan HITL:* Rendah.


- [x] **Penyusunan Glosarium (Glossary) & Minimalisasi Istilah Sulit** `[SELESAI]`
  - *Deskripsi:* Membuat kamus istilah khas PKN ([`content/Glosarium Istilah Karakter Nabawiyah.md`](content/Glosarium%20Istilah%20Karakter%20Nabawiyah.md)) dengan indeks A–Z, matriks tematik, definisi syar'i-pedagogis, serta melakukan purifikasi kosakata di seluruh repositori (mengganti *etape* menjadi *fase*, *archetype* menjadi *uswah sahabat*, dll.).
  - *Status Kemajuan:* Selesai penuh (383 berkas terverifikasi, seluruh rujukan 'etape' diubah menjadi 'fase', tautan navigasi diperbarui).
  - *Kebutuhan HITL:* Rendah (telah diverifikasi sesuai diksi asli buku Ustadz Abdul Kholiq).


- [x] **Standarisasi Progressive Disclosure & Framework Diátaxis pada Generator Konten** `[SELESAI]`
  - *Deskripsi:* Menerapkan pedoman [`pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md`](pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md) pada seluruh naskah dan generator AI dengan penekanan khusus pada **Pengalaman Membaca (*Reader's Journey*) & Narasi Kohesif**.
  - *Status Kemajuan:* Selesai penuh (Struktur MediaWiki 4-Zone, Lead TL;DR `> [!SUMMARY]`, Canvas embed, dan Collapsible Raw Data tervalidasi).
  - *Kebutuhan HITL:* Rendah.


- [x] **Validasi Kepatuhan Gaya Penulisan Ustadz Abdul Kholiq (Style Compliance Audit)** `[SELESAI]`
  - *Deskripsi:* Mengimplementasikan validator otomatis pada [`scripts/wiki_corpus_linter.py`](scripts/wiki_corpus_linter.py) berbasis panduan [`pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md`](pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md) untuk memastikan kepatuhan 10 pilar pedagogis: TL;DR di awal, pengantar naratif global, bagan visual Obsidian Canvas, dalil teks Arab bersanad, syarah ulama salaf mengalir, diagnosis Tafrith vs Ifrath, pembagian 4 fase usia, protokol manhaj tadarruj, rubrik 3-level, serta muhasabah 3 pertanyaan.
  - *Status Kemajuan:* Selesai penuh (Audit linter otomatis terintegrasi dengan 0 broken link dan 0 vocabulary violation).
  - *Kebutuhan HITL:* Rendah.


    - [x] Dokumen spesifikasi aturan & matriks penempatan di [`pipeline_designs/CONTENT_PLACEMENT_AND_NAVIGATION_RULES.md`](pipeline_designs/CONTENT_PLACEMENT_AND_NAVIGATION_RULES.md) `[SELESAI]`


    - [x] Penambahan `JourneyAuditor` persona pada Dewan Musyawarah Redaksi AI & `ContentPlacementAuditorNode` di [`pipeline_designs/01_pipeline_halaman_utama.md`](pipeline_designs/01_pipeline_halaman_utama.md) `[SELESAI]`


    - [x] Pembersihan & relokasi rubrik evaluasi dari Beranda ke [`content/Paradigma - Implementasi PKN/Template/Instrumen Evaluasi Kesiapan Transformasi.md`](content/Paradigma%20-%20Implementasi%20PKN/Template/Instrumen%20Evaluasi%20Kesiapan%20Transformasi.md) `[SELESAI]`


- [x] **Penambahan Komponen Callout "Kebiasaan Umum vs. Pendekatan PKN" pada Blok Refleksi Harian (Fase 1: Template Master & 9 Artikel Prioritas)** `[SELESAI]`
  - *Deskripsi:* Memperkaya komponen `[!info] Refleksi Lapangan` yang ada di [`Template Elemen Refleksi, Implementas, Risiko, dan Tautan`](content/Paradigma%20-%20Implementasi%20PKN/Template/Template%20Elemen%20Refleksi,%20Implementas,%20Risiko,%20dan%20Tautan.md) dengan menambahkan — atau menjadikan sub-bagian khusus — berupa **tabel kontras dua kolom** yang membandingkan kebiasaan/respons spontan yang lazim dilakukan kebanyakan orang (pendidik, orang tua, atau guru konvensional) dengan pendekatan yang ditawarkan manhaj PKN.
  - *Status Kemajuan:* Selesai penuh untuk Fase 1 (Master template diperbarui + 45 pasang kontras operasional diimplementasikan pada 9 artikel pilar prioritas: Pembelajaran Alamiah, Persepsi Positif, Disiplin Positif PKN, Luka dan Hutang Pengasuhan, Recovery, Peran Ayah dan Bunda, Bahasa Hati, Bahasa Lisan, dan Bahasa Tangan).
  - *Cakupan Implementasi:*
    1. **Pembaruan Template Master:** Menambah blok callout baru ini sebagai elemen ke-1 di [`Template Elemen Refleksi, Implementas, Risiko, dan Tautan.md`](content/Paradigma%20-%20Implementasi%20PKN/Template/Template%20Elemen%20Refleksi,%20Implementas,%20Risiko,%20dan%20Tautan.md).
    2. **Standarisasi Pipeline Generator:** Format tabel kontras diselaraskan untuk pembuatan halaman baru.
    3. **Pengayaan Artikel Prioritas:** 9 artikel prioritas terbit dan lolos linter 100%.
  - *Kebutuhan HITL:* Rendah (telah diverifikasi sesuai manhaj PKN).


- [x] **Panduan & Walkthrough Naratif Belajar PKN Bertahap** `[SELESAI]`
  - *Deskripsi:* Menyusun panduan belajar dan walkthrough khusus PKN dalam alur naratif yang dimulai dari konsep paling penting dan sederhana, berkembang bertahap menuju materi yang lebih sulit, lalu berakhir pada pemahaman konseptual.
  - *Status Kemajuan:* Selesai penuh melalui penerbitan [`content/Panduan/mulai-di-sini.md`](content/Panduan/mulai-di-sini.md) yang menyediakan 3 lintasan aksi cepat (Pahami Dasar, Lakukan Hari Ini, Periksa Sumber), pemetaan 13 subpersona, matriks 4 kuadran Diátaxis, serta 6 pintu masuk MOC.
  - *Kebutuhan HITL:* Rendah.


---

## 4. Pengumpulan & Kurasi Konten Inti PKN

- [x] **[🔴 PRIORITAS TINGGI] Artikel: Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi — Trilogi Hierarki Pendidikan** `[SELESAI]`
  - *Deskripsi:* Menyusun artikel ensiklopedis mandiri berstandar 4-Zone MediaWiki tentang tiga kaidah pedagogis masyhur dari KH. Abdullah Syukri Zarkasyi (Pimpinan Pondok Modern Darussalam Gontor) yang menguraikan hierarki prioritas dalam pendidikan secara bertingkat:
    1. **Kaidah I — Materi vs. Metode:**
       > الْمَادَّةُ مُهِمَّةٌ وَلَكِنَّ الطَّرِيقَةَ أَهَمُّ مِنَ الْمَادَّةِ
       > *"Materi Pembelajaran adalah sesuatu yang penting, tetapi metode pembelajaran jauh lebih penting daripada materi pembelajaran."*
    2. **Kaidah II — Metode vs. Guru:**
       > الطَّرِيقَةُ مُهِمَّةٌ وَلَكِنَّ الْمُدَرِّسَ أَهَمُّ مِنَ الطَّرِيقَةِ
       > *"Metode pembelajaran adalah sesuatu yang penting, tetapi guru jauh lebih penting daripada metode pembelajaran."*
    3. **Kaidah III — Guru vs. Jiwa Guru:**
       > الْمُدَرِّسُ مُهِمٌّ وَلَكِنَّ رُوحَ الْمُدَرِّسِ أَهَمُّ مِنَ الْمُدَرِّسِ
       > *"Guru adalah sesuatu yang penting, tetapi jiwa guru jauh lebih penting dari seorang guru itu sendiri."*
  - *Status Kemajuan:* Selesai penuh pada Milestone 62 (Naskah ensiklopedis 365 baris 4-Zone di `content/Referensi/Tokoh & Pemikiran/Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi.md`, matriks hierarki 4 tingkat operasional, Canvas interaktif piramida hierarki di `content/canvas/`, dan takhrij 5 dalil bersanad).
  - *Konten Artikel yang Diusulkan:*
    - **Zone 1:** Lead TL;DR berisi intisari tiga kaidah dalam satu paragraf padat, Infobox profil singkat KH. Abdullah Syukri Zarkasyi (lahir 1942, Pimpinan Gontor ke-3, konteks historis kaidah).
    - **Zone 2:** Syarah mendalam per kaidah — uraian filosofis-pedagogis, relevansi dalam manhaj PKN, korelasi dengan konsep *ruh al-mu'allim* (jiwa pendidik) dalam tradisi ulama salaf, dan penyambungan ke prinsip *uswah hasanah* Rasulullah ﷺ sebagai puncak trilogi.
    - **Zone 2:** Tabel matriks hierarki 4 tingkat (*Materi → Metode → Guru → Jiwa Guru*) dengan indikator operasional masing-masing level di kelas/pesantren.
    - **Zone 2:** Embed Obsidian Canvas visualisasi piramida hierarki pedagogis.
    - **Zone 3:** Dalil pendukung (hadits tentang niat, ikhlas, dan keteladanan guru), takhrij Shamela, serta pranala ke halaman [`Pembelajaran Alamiah`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20%26%20Implementasi/Pendidikan%20Ideal/Pembelajaran%20Alamiah.md) dan [`Tazkiyatun Nafs`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20%26%20Implementasi/Implementasi/Internal%20%26%20Eksternal/Tazkiyatun%20Nafs.md).
    - **Zone 4:** Navbox, kategori `[[Kategori:Tokoh Pendidikan Islam]]`, `[[Kategori:Kaidah Pedagogis]]`, `[[Kategori:Gontor]]`.
  - *Target Path:* `content/Referensi/Tokoh & Pemikiran/Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi.md`
  - *Perkiraan Token AI:* ~80k - 150k token (riset biografi, penyusunan syarah kaidah, perakitan artikel 4-Zone, pembuatan canvas, dan verifikasi takhrij dalil pendukung).
  - *Kebutuhan HITL:* **Tinggi** (verifikasi otentisitas dan sanad atribusi kaidah kepada KH. Abdullah Syukri Zarkasyi, review kesesuaian syarah oleh asatidzah/alumni Gontor, serta validasi kontekstualisasi ke manhaj PKN oleh kurator).


- [x] **Artikel: Firasat (الفِرَاسَة) — Metode Nabawi Membaca Jiwa & Mengenali Bakat Anak** `[SELESAI]`
  - *Deskripsi:* Menyusun halaman konsep mandiri berstandar 4-Zone MediaWiki tentang **firasat** sebagai *metode pedagogis inti* dalam manhaj PKN — yaitu kemampuan menyimpulkan hal-hal batin (karakter, bakat, kondisi jiwa) dari tanda-tanda lahir yang tampak (gestur tubuh, ekspresi, perilaku spontan). Halaman ini berbeda dan lebih luas dari entri bakat TB-40 Pilar #7 ([`07-firaasah.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20%26%20Implementasi/Insan/Fitrah%20%28Karakter%29/Bakat/TB40/07-firaasah.md)) yang sudah ada — fokusnya bukan pada *memiliki bakat firasat*, melainkan pada *firasat sebagai alat/metode* yang bisa diasah oleh setiap orang tua dan guru.
  - *Status Kemajuan:* Selesai penuh pada Milestone 62 (Naskah 436 baris 4-Zone di `content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Firasat.md`, Canvas 3 dimensi firasat di `content/canvas/`, matriks 8 kasus tanda lahiriah ke batiniah, protokol latihan observasi, serta penerbitan 2 halaman dalil mandiri di `content/Dalil/`: `dalil-firasat-mukmin-cahaya-allah.md` dan `dalil-al-mutawassimin-tanda-kebesaran-allah.md`).
  - *Konten Artikel yang Diusulkan:*
    - **Zone 1:** Lead TL;DR — definisi firasat dalam Islam (*menyimpulkan hal batiniah dari tanda yang tampak*), posisinya sebagai metode Rasulullah ﷺ dalam mengenali dan menempatkan sahabat, serta relevansinya sebagai metode pemetaan bakat anak yang lebih akurat daripada asesmen tertulis.
    - **Zone 2 — Fondasi Syar'i:** Dalil Al-Qur'an (QS. Al-Hijr: 75 *"Inna fī dzālika la-āyātin lil-mutawassimīn"* — tanda bagi yang tajam firasat) dan hadits tentang ketajaman firasat mukmin (*"Ittaqū firāsatal mu'min fa-innahū yanẓuru bi nūrillāh"*). Takhrij Shamela dan syarah Ibnul Qayyim dalam *Madarijus Salikin* tentang tiga tingkatan firasat: firasat imaniyah, firasat riyādhiyah, dan firasat khilqiyah.
    - **Zone 2 — Tiga Dimensi Firasat dalam Konteks PKN:**
      1. **Firasat Bakat (*Syakilah*):** Membaca potensi dominan anak dari gestur, pola respons, dan kegiatan favorit — lebih valid dari tes psikologi/asesmen karena bersifat longitudinal dan berbasis observasi harian.
      2. **Firasat Ego/Kutub Energi:** Membedakan ego tinggi (introvert-dominan, bertenaga dari dalam), ego sedang (analitis-kolaboratif), dan ego rendah (ekstrover-pelayan) dari cara anak berinteraksi dengan lingkungan dan respons spontan terhadap tekanan.
      3. **Firasat Kondisi Jiwa:** Mendeteksi tanda-tanda hutang pengasuhan, luka batin, atau potensi menyimpang sejak dini dari perubahan perilaku, pola emosi, dan bahasa tubuh anak.
    - **Zone 2 — Cara Mengasah Firasat (Protokol Latihan):** Panduan bertahap melatih kemampuan firasat — mulai dari observasi video anak usia 2–5 tahun, latihan pembacaan gestur langsung, hingga tradisi majelis *syura* guru yang saling berbagi pengamatan firasat tentang santri.
    - **Zone 2 — Tabel Matriks:** Tanda lahir → Kesimpulan batin (ego, bakat rumpun, kondisi jiwa) dengan contoh konkret dari kajian Ustadz Abdul Kholiq.
    - **Zone 2 — Uswah Sahabat:** Kisah Umar bin Khattab (ketajaman firasat ego tinggi), Imam Syafi'i (firasat khilqiyah), dan kasus Rasulullah ﷺ menempatkan sahabat pada posisi peran yang sesuai firasat beliau.
    - **Zone 2 — Batasan & Adab Firasat:** Firasat bukan ramalan, bukan penghakiman permanen — penjelasan tentang bahaya *overthinking* firasat dan kaidah *"al-umūru bi maqāshidihā"* agar firasat tetap berlandaskan niat mendidik, bukan memvonis.
    - **Zone 3:** Pranala silang ke [`07-firaasah.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20%26%20Implementasi/Insan/Fitrah%20%28Karakter%29/Bakat/TB40/07-firaasah.md) (bakat firaasah TB-40), [`Bakat/index.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20%26%20Implementasi/Insan/Fitrah%20%28Karakter%29/Bakat/index.md), kajian video terkait firasat (SQrC2H38EV4, Fti1kjBgBjA, lTrVXBUVnSM, 6H-qENwmmcw).
    - **Zone 4:** Navbox, kategori `[[Kategori:Metode Pedagogis Nabawi]]`, `[[Kategori:Pemetaan Bakat]]`, `[[Kategori:Fitrah Karakter]]`.
  - *Target Path:* `content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Firasat.md`
  - *Perkiraan Token AI:* ~100k - 180k token (riset dalil dan syarah ulama, penyusunan protokol latihan firasat, perakitan artikel 4-Zone, dan pembuatan canvas visualisasi tiga dimensi firasat).
  - *Kebutuhan HITL:* **Tinggi** (verifikasi takhrij hadits firasat mukmin, review syarah Ibnul Qayyim tentang tingkatan firasat, serta validasi kesesuaian tabel matriks tanda-batin dengan pengamatan lapangan oleh asatidzah/guru praktisi PKN).


- [x] **Penyusunan Materi Tazkiyatun Nafs** `[SELESAI]`
  - *Deskripsi:* Dokumentasi konsep, tahapan, dan implementasi Tazkiyatun Nafs dalam kerangka pendidikan karakter nabawiyah ([`content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tazkiyatun Nafs.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Internal%20&%20Eksternal/Tazkiyatun%20Nafs.md)).
  - *Status Kemajuan:* Selesai penuh (Format 4-Zone, Lead TL;DR, Rubrik 3-Level, Muhasabah, dan embed Obsidian Canvas dua fase *Takhalli* dan *Tahalli*).
  - *Kebutuhan HITL:* Rendah.


- [x] **Konsep Pembelajaran Alamiah** `[SELESAI]`
  - *Deskripsi:* Perumusan prinsip pembelajaran alamiah berbasis fitrah belajar dan sunnatullah tumbuh kembang anak ([`content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Pembelajaran Alamiah.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Pendidikan%20Ideal/Pembelajaran%20Alamiah.md)).
  - *Status Kemajuan:* Selesai penuh (538 baris naskah terperinci, integrasi QS. An-Nahl: 78, instrumen Peristiwa vs Proyek, Rukun 3A, dan embed kanvas). Telah disematkan di Beranda Utama ([`content/index.md`](content/index.md)).
  - *Kebutuhan HITL:* Rendah.


- [x] **Tabel & Taksonomi Tafsir Bakat TB-40 (Pengganti Bab 8 Buku Utama)** `[SELESAI]`
  - *Deskripsi:* Menyusun tabel indikator, matriks karakter, dan rukun 3A Tafsir Bakat (TB-40) sebagai pengganti resmi Bab 8 Buku Utama PKN lama (menggantikan ST-30/Talents Mapping yang usang).
  - *Status Kemajuan:* Selesai penuh (40 pilar bakat di [`content/Paradigma - Implementasi PKN/.../TB40/`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Bakat/TB40/) menyerap 100% naskah Bab 12 Buku Tafsir Bakat ke format 4-Zone, serta matriks uswah sahabat di [`Bakat/index.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Bakat/index.md)).
  - *Kebutuhan HITL:* Rendah.


- [x] **Pembuatan Halaman Khusus untuk Setiap Dalil** `[SELESAI]`
  - *Deskripsi:* Membuat halaman mandiri untuk setiap dalil (Al-Qur'an dan Hadits shahih) yang memuat teks dalil Arab berharakat, nomor surah:ayat atau hadits, takhrij Maktabah Syamilah/OpenBayan, syarah ulama mu'tabar (Tafsir Ibnu Katsir, Syarah Muslim An-Nawawi, Fathul Bari Ibnu Hajar), pengayaan dalil Tazkiyatun Nafs (*Takhalli* dan *Tahalli*), serta wikilinks konsep manhaj PKN.
  - *Status Kemajuan:* Selesai penuh (80+ halaman dalil mandiri terbit di [`content/Dalil/`](content/Dalil/) dengan Action Bar, Infobox, dan Navbox terstandar).
  - *Kebutuhan HITL:* Rendah (telah divalidasi sanad dan syarah salaf-nya).


- [x] **Pembuatan Halaman Khusus untuk Setiap Video Kajian Ustadz Abdul Khaliq** `[SELESAI]`
  - *Deskripsi:* Membuat halaman mandiri untuk setiap video kajian dan ceramah Ustadz Abdul Khaliq (122 rekaman ceramah berdasarkan basis data `pkn.db` / `PKN-videoDB`), memuat embed pemutar video YouTube, daftar bab pembahasan terindeks dengan timestamp interaktif ke detik spesifik (1.159 bab), ringkasan poin inti per segmen, transkrip tematik collapsible, serta penautan silang (*cross-link*) ke konsep materi PKN di folder `content/Kajian Video/`.
  - *Status Kemajuan:*


    - [x] Skrip generator [`scripts/generate_video_pages.py`](scripts/generate_video_pages.py) `[SELESAI]`


    - [x] Terbit 122 berkas halaman video + hub portal [`content/Kajian Video.md`](content/Kajian Video.md) `[SELESAI]`
  - *Perkiraan Token AI:* ~1.5M - 2.5M token.
  - *Kebutuhan HITL:* Sedang.


- [x] **Ingestion Seluruh Artikel Resmi SOTAB HEBAT (Karya Ustadz Abdul Kholik)** `[SELESAI]`
  - *Deskripsi:* Mengunduh dan mengompilasi seluruh 121 artikel resmi Sekolah Orangtua Ayah Bunda Hebat Indonesia (SOTAB) dari WordPress REST API ke format Markdown Quartz v5 di folder `content/Materi SOTAB/` lengkap dengan Progressive Disclosure, metadata sumber, dan portal pengindeksan [`content/Materi SOTAB.md`](content/Materi SOTAB.md).
  - *Status Kemajuan:*


    - [x] Skrip pengunduh & konverter [`scripts/ingest_sotab_articles.py`](scripts/ingest_sotab_articles.py) `[SELESAI]`


    - [x] Terbit 121 berkas materi SOTAB berstandar Quartz `[SELESAI]`
  - *Perkiraan Token AI:* ~800k - 1.2M token.
  - *Kebutuhan HITL:* Rendah - Sedang.


---

## 5. Kajian Komparasi, Profil & Review Lembaga

- [x] **Review masing-masing buku & Standarisasi Kutipan 4 Buku Utama** `[SELESAI]`
  - *Deskripsi:* Ulasan mendalam, ringkasan bab, dan relevansi masing-masing buku referensi kanonikal PKN karya Ustadz Abdul Kholiq.
  - *Status Kemajuan:* Selesai penuh (Milestone 60 & 62):


    - [x] Terbit 8 halaman ensiklopedis mandiri di [`content/Referensi/`](content/Referensi/): *Pendidikan Karakter Nabawiyah*, *Tafsir Bakat*, *Menumbuhkan Kesadaran Beramal*, *Recovery Berbasis Fitrah*, *Kurikulum Sekolah Karakter Islam*, *Panduan Implementasi Standar PKN*, *Panduan Kurikulum PAUD-TK Karakter Islam*, dan *Bukanlah Sekejap*.


    - [x] Pembersihan label kode teknis (`# ZONE 1, 2, 3, 4`) menjadi judul naratif elegan.


    - [x] Konversi peta konsep bab dari ASCII/code block menjadi 8 bagan interaktif Obsidian Canvas (`content/canvas/Review Buku/`).


    - [x] Penyematan kartu Call-to-Action (CTA) pembelian edisi cetak fisik resmi di `karakternabawiyah.com`.


    - [x] Peringkasan naskah turunan 4 buku (*Buku Utama PKN*, *Tafsir Bakat*, *Kesadaran Beramal*, *Standar Implementasi*) pada 81 berkas korpus dengan penyematan banner intisari & kutipan resmi bersanad yang menautkan ke halaman review buku.


    - [x] Resolusi tautan otomatis dalam blok HTML mentah (Infobox table & Navbox) via patch Quartz OFM regex & CrawlLinks AST visitor.


    - [x] Pembaruan atribusi hak cipta menjadi *"Pengembangan oleh Harridi Ilman Tovid - Yayasan Bina Insan Taqwa - Yayasan Bina Insan Mustaqbal"* dan identitas SOTAB HEBAT sebagai *"Sekolah Orang Tua HEBAT dari HCE (Home Character Education)"*.
  - *Kebutuhan HITL:* Rendah.


    - [x] Direktori terisolasi `sources/research_papers/` dan `data/extracted_elements/external_research/` `[SELESAI]`


    - [x] Berkas deployment kontainer terisolasi [`docker-compose.qdrant-research.yml`](docker-compose.qdrant-research.yml) (Port 6335, batas RAM 1GB) `[SELESAI]`


    - [x] Skrip batch runner & pre-flight inspector [`scripts/ingest_research_papers.py`](scripts/ingest_research_papers.py) (PyMuPDF + Unstructured + OpenAlex/Semantic Scholar) `[SELESAI]`


    - [x] Pemasangan pustaka riset & alat skrining di `.venv`: `asreview` (v3.0.8 machine learning screening), `habanero` (Crossref/Retraksi), `arxiv`, `qdrant-client`, `beautifulsoup4`, `requests` `[SELESAI]`


    - [x] Skrip pencari literatur multi-mesin [`scripts/search_academic_papers.py`](scripts/search_academic_papers.py) (OpenAlex, Semantic Scholar, arXiv dengan opsi auto-download PDF) `[SELESAI]`


- [x] **[🔴 PRIORITAS TINGGI] Riset Khazanah Turats: Audit Dalil & Pendapat Ulama tentang Parenting via OpenBayan & Qaf — Temuan Gap & Kontradiksi dengan PKN** `[FASE 1 SELESAI]`
  - *Deskripsi:* Menjalankan proyek riset syar'i mendalam dan sistematis menggunakan **OpenBayan** (Qdrant `shamela_11m` — 11 juta matan Maktabah Syamilah) sebagai mesin sweep utama, dan **Qaf AI** (`qaf_wrapper` — 320+ kitab klasik) secara **terbatas dan strategis** untuk mengumpulkan dalil Al-Qur'an, Hadits, dan pendapat/komentar ulama yang berkaitan dengan tema-tema inti parenting/tarbiyatul aulad, lalu melakukan analisis kritis: **(1) Apa yang belum disebutkan dalam PKN?** dan **(2) Apakah ada yang berpotensi bertentangan atau perlu klarifikasi?**
  - *Status Kemajuan:* Fase 1 (Sweeping & Gap Analysis via OpenBayan) selesai penuh pada Milestone 63. Telah diterbitkan 4 berkas riset internal berbobot ~80 KB di `sources/audit_dalil_parenting/`:
    1. `00_README_dan_Metodologi.md` (Alur riset, arsitektur dual-engine FTS5 + Qdrant, taksonomi 7 klaster tematik, batasan syar'i).
    2. `01_sweeping_hadits_tarbiyah.md` (22 entri hadits/atsar lengkap dengan matan Arab berharakat, perawi, nomor, takhrij, derajat sanad, terjemahan resmi, dan kutipan syarah ulama salaf).
    3. `04_gap_analysis_belum_disebutkan.md` (Komparasi 86 file fisik di `content/Dalil/` dan pembongkaran 6 gap kunci dalil tarbiyah).
    4. `06_rekomendasi_pengayaan_konten.md` (Blueprint penerbitan 6 dalil mandiri baru dan matriks pengayaan 10 artikel pilar inti).
  - **Sifat Output: Dokumen Kerja Internal** — Hasil analisis ini **tidak langsung diterbitkan** di Quartz sebagai halaman publik, melainkan disimpan sebagai kumpulan dokumen riset internal di direktori `sources/audit_dalil_parenting/` untuk kemudian menjadi bahan review, koreksi, dan pengayaan naskah PKN oleh tim asatidzah/kurator.
  - > ⚠️ **Batasan Kuota Qaf AI:** Qaf AI memiliki kuota terbatas **~100 pesan per bulan**. Penggunaannya **WAJIB dihemat** — jangan dipakai untuk sweeping massal atau kueri eksplorasi acak. Qaf **hanya boleh dipanggil** untuk: (a) **verifikasi hipotesis** yang sudah dirumuskan dari hasil sweep OpenBayan, dan (b) **meta-analysis tingkat tinggi** — yaitu ketika sudah ada temuan spesifik yang perlu dikonfirmasi atau dikontekstualisasikan dengan komentar ulama dari kitab tertentu. Seluruh eksplorasi awal dan broad scanning dilakukan via OpenBayan.
  - *Tahapan Kerja:*
    1. **Tahap 1 — Pemetaan Tema & Query Design:** Menyusun daftar lengkap tema-tema inti parenting dalam PKN yang akan diaudit (misal: *tarbiyatul aulad*, *adabul walad*, *haq al-walad*, *'uqubah al-walad*, *mahabbah al-walad*, *taklif*, *mumayyiz*, *bait*, *fitrah*, *'aqiqah*, *ta'lim*, *tahfizh*, *riyadhah*, dll.) dan merancang kueri Arab presisi untuk setiap tema. Tahap ini menghasilkan **daftar hipotesis awal** yang akan diuji di tahap berikutnya.
    2. **Tahap 2 — Sweeping Massal OpenBayan (`shamela_11m`) [Mesin Utama]:** Menjalankan kueri BM25 full-text dan dense vector search ke Qdrant port 6333 untuk **semua tema** secara batch — ini adalah operasi tidak terbatas yang bisa diulang bebas. Ekstrak semua matan hadits yang relevan beserta nomor, kitab, dan derajat shahih/hasan/dha'if-nya. Target: menemukan hadits-hadits yang *belum* dirujuk dalam korpus dalil PKN saat ini (`content/Dalil/`). **Gunakan OpenBayan untuk semua eksplorasi awal, bukan Qaf.**
    3. **Tahap 3 — Qaf AI: Verifikasi Hipotesis & Meta-Analysis [Kuota Terbatas, Maks ~100 Pesan/Bulan]:**
       - **Strategi hemat kuota:** Sebelum memanggil Qaf, rumuskan dahulu **hipotesis spesifik** berdasarkan hasil Tahap 2. Contoh: *"Apakah Ibnul Qayyim dalam Tuhfatul Maudud memiliki pendapat tentang usia anak pertama kali dihukum ta'zir?"* — bukan kueri umum seperti *"cari semua tentang mendidik anak"*.
       - **Kapan boleh memanggil Qaf:** (a) Saat ditemukan hadits ambigu dari OpenBayan yang butuh konteks syarah ulama spesifik; (b) Saat ada temuan Divergent yang perlu dikonfirmasi dari kitab primer (*Tuhfatul Maudud*, *Ihya Ulumiddin*, *Fathul Bari*, dll.); (c) Untuk meta-analysis — merangkum posisi lintas ulama terhadap satu isu kritis (*ikhtilaf ulama* tentang tema tertentu).
       - **Kapan TIDAK boleh memanggil Qaf:** Eksplorasi broad, kueri berulang dengan variasi minor, sweeping tema baru yang belum dianalisis di OpenBayan, atau kueri yang jawabannya bisa ditemukan lewat OpenBayan.
       - **Alokasi kuota yang disarankan:** ~20 pesan untuk konfirmasi temuan Gap, ~30 pesan untuk analisis temuan Divergent, ~30 pesan untuk meta-analysis lintas kitab, ~20 pesan cadangan.
    4. **Tahap 4 — Gap Analysis (Belum Disebutkan):** Membandingkan hasil sweeping dengan korpus dalil PKN yang sudah ada, mengidentifikasi:
       - Hadits-hadits shahih tematik parenting yang *belum* muncul di PKN
       - Pendapat ulama yang *belum* dikutip tapi relevan memperkuat atau memperkaya manhaj PKN
       - Tema-tema fiqh tarbiyah yang *sama sekali belum disinggung* dalam konten PKN
    5. **Tahap 5 — Contradiction Analysis (Potensi Bertentangan):** Mengidentifikasi secara jujur dan akademis dalil atau pendapat ulama yang *secara zahir* berpotensi bertentangan dengan prinsip-prinsip PKN, mencakup:
       - Perbedaan pendapat ulama tentang *hukum ta'dib/ta'zir* anak (batas mana yang dibolehkan)
       - Hadits-hadits tentang tegas/keras dalam mendidik vs prinsip *lembut dan kasih sayang* yang ditekankan PKN
       - Perbedaan ulama tentang usia baligh, batas taklif, dan protokol pendisiplinan
       - Ijtihad kontemporer yang berbeda dengan pendekatan PKN
    6. **Tahap 6 — Sintesis & Klasifikasi Temuan:** Mengklasifikasikan seluruh temuan ke dalam tiga kategori:
       - 🟢 **Convergent (Menguatkan PKN):** Dalil/pendapat ulama yang selaras dengan PKN dan bisa langsung dijadikan penguat
       - 🟡 **Gap (Belum Ada di PKN):** Dalil/pendapat yang relevan tapi belum dirujuk — kandidat pengayaan
       - 🔴 **Divergent (Perlu Klarifikasi):** Dalil/pendapat yang zahirnya berseberangan — perlu jawaban dan tahqiq mendalam oleh asatidzah sebelum disikapi
  - *Struktur Output Dokumen Kerja Internal:*
    ```
    sources/audit_dalil_parenting/
    ├── 00_README_dan_Metodologi.md          # Panduan penggunaan dokumen audit ini
    ├── 01_sweeping_hadits_tarbiyah.md       # Hasil raw sweep OpenBayan per tema
    ├── 02_hipotesis_untuk_qaf.md            # Daftar hipotesis terstruktur siap diverifikasi ke Qaf
    ├── 03_hasil_verifikasi_qaf.md           # Hasil pemanggilan Qaf (dicatat hemat, per hipotesis)
    ├── 04_gap_analysis_belum_disebutkan.md  # Temuan dalil & pendapat yang belum ada di PKN
    ├── 05_contradiction_analysis.md         # Temuan yang berpotensi bertentangan + analisis
    ├── 06_rekomendasi_pengayaan_konten.md   # Daftar artikel/dalil yang direkomendasikan untuk ditambahkan
    └── 07_pertanyaan_terbuka_untuk_asatidzah.md  # Daftar pertanyaan yang membutuhkan ijtihad ulama
    ```
  - *Perkiraan Token AI:* ~1.5M - 3M token (kueri Arab multi-tema ke OpenBayan, perumusan hipotesis terstruktur, pemanggilan Qaf terbatas untuk meta-analysis, ekstraksi dan klasifikasi temuan, serta penulisan laporan sintesis per tema).
  - *Kebutuhan HITL:* **Sangat Tinggi** — Dokumen ini pada dasarnya adalah bahan mudzakarah ilmiah yang *wajib* di-review oleh asatidzah sebelum dijadikan dasar perubahan konten PKN. Khususnya untuk temuan kategori 🔴 Divergent, tidak boleh ada kesimpulan atau respons yang diterbitkan tanpa otorisasi kurator/ustadz.


---

## 6. Template Siap Pakai & Toolkit KBM

- [x] **Daftar dokumen bantuan dan review masing-masing dokumen** `[SELESAI]`
  - *Deskripsi:* Inventarisasi dokumen panduan/petunjuk teknis pembantu serta telaah kegunaannya di [`content/Toolkit KBM/index.md`](content/Toolkit%20KBM/index.md).
  - *Status Kemajuan:* Selesai penuh (Portal induk mengindeks seluruh instrumen, alur kerja 4 tahap, dan panduan pengisian).
  - *Kebutuhan HITL:* Rendah.


- [x] **Kumpulan dokumen template siap pakai** `[SELESAI]`
  - *Deskripsi:* Bank dokumen siap pakai operasional KBM di [`content/Toolkit KBM/`](content/Toolkit%20KBM/):
    1. [`Template RPP Karakter Nabawiyah 1 Lembar.md`](content/Toolkit%20KBM/Template%20RPP%20Karakter%20Nabawiyah%201%20Lembar.md) (Iman, Adab, Ilmu & 3 Bahasa).
    2. [`Instrumen Observasi Pertumbuhan Karakter 19 Butir.md`](content/Toolkit%20KBM/Instrumen%20Observasi%20Pertumbuhan%20Karakter%2019%20Butir.md) (Rubrik non-angka BT, MT, BK, MM).
    3. [`Formulir Desain Proyek Pembelajaran Alamiah.md`](content/Toolkit%20KBM/Formulir%20Desain%20Proyek%20Pembelajaran%20Alamiah.md) (Sains & Adab Berbasis Peristiwa).
    4. [`Lembar Dialog Evaluasi Hati Guru-Santri.md`](content/Toolkit%20KBM/Lembar%20Dialog%20Evaluasi%20Hati%20Guru-Santri.md) (Protokol 4 Langkah Pemulihan Adab).
  - *Status Kemajuan:* Selesai penuh (Format markdown bersih siap salin/cetak, bebas angka mati pada adab).
  - *Kebutuhan HITL:* Rendah.


- [x] **Prompt AI dan template pembuatan dokumen KBM** `[SELESAI]`
  - *Deskripsi:* Penyusunan sistem prompt AI siap pakai bagi guru di [`content/Toolkit KBM/Bank Prompt AI Guru KBM.md`](content/Toolkit%20KBM/Bank%20Prompt%20AI%20Guru%20KBM.md) memuat 5 paket prompt XML tags (`<role>`, `<context>`, `<rules>`, `<output_format>`) untuk sirah nabawiyah, proyek fitrah, lembar muhasabah, dan studi kasus.
  - *Status Kemajuan:* Selesai penuh (Dilengkapi few-shot examples dan tips kalibrasi guru).
  - *Kebutuhan HITL:* Rendah.


- [x] **Kumpulan tips and trik problematika harian** `[SELESAI]`
  - *Deskripsi:* Panduan solusi praktis atas kendala harian guru/orang tua dalam menghadapi dinamika perilaku santri via protokol rekonsiliasi hati dan penanganan krisis adab di [`content/Toolkit KBM/Lembar Dialog Evaluasi Hati Guru-Santri.md`](content/Toolkit%20KBM/Lembar%20Dialog%20Evaluasi%20Hati%20Guru-Santri.md).
  - *Status Kemajuan:* Selesai penuh (Protokol 4 langkah tanpa kekerasan verbal/fisik, menjaga fitrah kemuliaan anak).
  - *Kebutuhan HITL:* Rendah.


---

## 7. Transisi & Peluncuran Production

- [x] **Automasi Pipeline CI/CD Build & Deploy ke Server Production** `[SELESAI]`
  - *Deskripsi:* Menghubungkan webhook repositori GitHub ke runner deployment (Coolify / GitHub Actions) agar setiap perubahan naskah yang disetujui di Alexandrie atau commit pengembang otomatis memicu build Quartz dan terbit ke `wiki.karakternabawiyah.com` tanpa intervensi manual.
  - *Status Kemajuan:* Selesai penuh (Penerbitan `.github/workflows/deploy.yml` dengan arsitektur fail-fast 2 job: `corpus-lint` Python 3.12 dan `quartz-build` Node.js 22, caching npm/plugins, patch resolver link, upload artifact `quartz-build-output`, dan webhook Portainer).
  - *Perkiraan Token AI:* ~40k - 80k token.
  - *Kebutuhan HITL:* Rendah.


---

## 8.1 Pengayaan Konsep & Matriks Tumbuh Kembang

- [x] **Matriks Karakter Berdasarkan Tahapan Usia (7 Tahun Pertama, Mumayyiz, Baligh)** `[SELESAI]`
  - *Deskripsi:* Panduan target adab dan pendekatan komunikasi sesuai fase usia anak (sunnatullah tumbuh kembang).
  - *Status Kemajuan:* Selesai penuh melalui penerbitan [`content/Panduan/fase-usia.md`](content/Panduan/fase-usia.md) yang merangkum matriks komparatif 4 rentang usia (Thufulah 0–7, Tamyiz 7–10, Murahaqah 10–15, Syabab 15+), kaidah 5.000 kali pengulangan shalat, dan pendekatan tiga bahasa mendidik.
  - *Kebutuhan HITL:* Rendah.


---

## 8.2 Instrumen Evaluasi & Asesmen Guru

- [x] **Bank Cerita Sirah & Apersepsi KBM** `[SELESAI]`
  - *Deskripsi:* Kumpulan kisah Rasulullah ﷺ dan para sahabat yang dipetakan ke tema-tema pelajaran sains/sosial/matematika untuk apersepsi KBM.
  - *Status Kemajuan:* Selesai penuh pada Milestone 63 (Naskah master berstandar MediaWiki 4-Zone di `content/Toolkit KBM/Bank Cerita Sirah dan Apersepsi KBM.md` memuat 12 riwayat shahih/hasan dalam 4 tema kurikulum sains, sosial, matematika, dan adab, inquiry prompts Bahasa Hati 3 tingkat, rubrik evaluasi kualitatif non-angka BT-MT-BK-MM, takhrij dalil berharakat lengkap, dan SOP 5 menit pembuka KBM).
  - *Perkiraan Token AI:* ~1.2M - 2M token (kurasi riwayat sirah shahihah dan pemetaannya ke topik kurikulum umum).
  - *Kebutuhan HITL:* Tinggi (tahqiq keabsahan riwayat sirah agar terhindar dari kisah dha'if/maudhu').


---

## 8.3 Navigasi & Pengalaman Membaca

- [x] **Jalur Belajar / Reading Path untuk Pemula ("Mulai Dari Sini")** `[SELESAI]`
  - *Deskripsi:* Urutan baca terkurasi bagi guru atau orang tua baru agar tidak kebingungan menjelajahi khazanah wiki.
  - *Status Kemajuan:* Selesai penuh melalui penerbitan [`content/Panduan/mulai-di-sini.md`](content/Panduan/mulai-di-sini.md) yang menghubungkan 3 lintasan belajar dan 6 pintu masuk tematik MOC di sidebar.
  - *Kebutuhan HITL:* Rendah.


---

## 8.4 Fitur Teknis Platform & Distribusi

- [x] **Fitur Ekspor PDF Rapi Siap Cetak (Print Stylesheet)** `[SELESAI LOKAL]`
  - *Deskripsi:* CSS cetak A4 untuk materi / RPP / modul menyembunyikan sidebar, breadcrumb, metadata, action bar, dan footer situs; tabel dibungkus sesuai lebar halaman, callout dan baris tabel dijaga agar tidak terbelah bila muat.
  - *Verifikasi:* Build Quartz 484 input berhasil; Chromium menghasilkan PDF RPP dan artikel dalil. Uji peramban selain Chromium tetap disarankan sebelum rilis publik.
  - *Kebutuhan HITL:* Rendah.


---

## 8.5 AI & Otomasi Pipeline Konten

    - [x] Spesifikasi master arsitektur & 10 desain pipeline tematik di [`pipeline_designs/`](pipeline_designs/README.md) `[SELESAI]`


    - [x] Desain siklus multi-agent debate (Drafter, Sharia Auditor, Pedagogy Critic, Clarity Editor, Supervisor) `[SELESAI]`


- [x] **Prototype Runner Pipeline Dalil Mandiri (Pipeline 07 Dalil)** `[SELESAI]`
  - *Deskripsi:* Membangun skrip eksekutor Python pertama ([`scripts/pipeline_runner_dalil.py`](scripts/pipeline_runner_dalil.py)) yang mengimplementasikan 4 Lapisan Progressive Disclosure, takhrij matan teks Arab, terjemahan, syarah ulama mu'tabar, serta matriks operasional KBM di `content/Dalil/`.
  - *Status Kemajuan:*


    - [x] Skrip eksekutor [`scripts/pipeline_runner_dalil.py`](scripts/pipeline_runner_dalil.py) `[SELESAI]`


    - [x] Terbit 4 halaman dalil induk percontohan di `content/Dalil/` `[SELESAI]`
  - *Perkiraan Token AI:* ~50k - 100k token.
  - *Kebutuhan HITL:* Rendah - Sedang.


- [x] **Wiki Linter Agent & Style Auditor (Continuous Maintenance Script)** `[SELESAI]`
  - *Deskripsi:* Membangun alat audit linter offline ([`scripts/wiki_linter.py`](scripts/wiki_linter.py)) untuk memindai broken `[[WikiLinks]]`, mendeteksi halaman orphan (inbound links = 0), dan mengevaluasi kepatuhan naskah terhadap 10 checklist gaya penulisan Ustadz Abdul Kholiq.
  - *Status Kemajuan:*


    - [x] Skrip linter [`scripts/wiki_linter.py`](scripts/wiki_linter.py) `[SELESAI]`
  - *Perkiraan Token AI:* ~40k - 80k token.
  - *Kebutuhan HITL:* Rendah.


    - [x] Rencana implementasi teknis & alokasi port host `8005` (lihat [implementation_plan.md](file:///home/abuhafi/.gemini/antigravity-ide/brain/c5f632a1-642b-45fa-87cc-28e8af74a811/implementation_plan.md)) `[SELESAI]`


    - [x] Berkas deployment [`docker-compose.unstructured.yml`](docker-compose.unstructured.yml) (kompatibel DIUN & healthcheck) `[SELESAI]`


    - [x] Client adapter Python [`scripts/unstructured_adapter.py`](scripts/unstructured_adapter.py) (partisi elemen, tabel ke markdown, LangChain chunking, MD5 caching) `[SELESAI]`


    - [x] Generator Hierarchical Narrative Graph (TOC + prev/next chunk edges) di [`scripts/unstructured_adapter.py`](scripts/unstructured_adapter.py) `[SELESAI]`


    - [x] Skrip uji & validasi [`scripts/benchmark_extraction.py`](scripts/benchmark_extraction.py) (unit test table converter & schema transformer) `[SELESAI]`


    - [x] Isolasi Partisi Data Ekstraksi: Pemisahan direktori input (`sources/research_papers/` vs `searchable_pdfs/`) dan direktori output (`data/extracted_elements/external_research/` vs `data/extracted_elements/pkn_internal/`) `[SELESAI]`


    - [x] Peluncuran container & batch ingestion 88 dokumen PDF/PPTX mentah menggunakan Unstructured API (hi_res & fast fallback) `[SELESAI]`
      - *Hasil Ekstraksi:* 88/88 berkas sukses 100% (47 PDF + 41 PPTX), menghasilkan 5.311 elemen semantik terstruktur dan 166 tabel Markdown rapi di `data/extracted_elements/`.


    - [x] Implementasi lokal `scripts/pkn_retrieval.py`: indeks Qdrant koleksi `pkn_internal`, embedding Ollama `qwen3-embedding:0.6b`, ID titik stabil, sinkronisasi chunk yang berubah, pencarian dengan lokasi halaman, dan tes in-memory di `tests/test_pkn_retrieval.py`. Jalankan `index --input <satu-JSON-ekstraksi> --source-id <ID-registry-yang-sesuai>` setelah memeriksa asal dokumen. Smoke Qdrant persisten memakai berkas sintetis pada koleksi sementara: 2 titik awal, 2 setelah indeks ulang, 1 setelah chunk dihapus, sitasi `/synthetic/lesson.pdf#page=2`; koleksi sementara telah dihapus. Uji dokumen PDF nyata sempat menghasilkan sitasi, tetapi atribusi `PPTX-PRESENTATIONS` keliru dan koleksi uji itu telah dihapus. Indeks produksi, relevansi korpus penuh, dan sitasi halaman asli belum diverifikasi; klien Qdrant 1.19.1 dan server 1.12.0 belum selaras versinya.
  - *Perkiraan Token AI:* ~150k - 300k token (pembuatan adapter API client Python, konfigurasi deployment container, transformasi skema chunking, dan pengujian perbandingan akurasi ekstraksi).
  - *Kebutuhan HITL:* Sedang (evaluasi presisi hasil partisi teks, struktur tabel, dan teks Arab berharakat pada sampel dokumen PDF modul PKN).


---

## 8.6 Analisis Implementasi & Gerbang Kualitas RAG (2026-10-01)

- [x] **Kerangka Presedensi Berjenjang & Peluruhan Waktu (*Tiered Precedence & Decay Framework*)** `[SELESAI]`
  - *Deskripsi:* Membangun mekanisme mitigasi benturan materi antar-dokumen berdasarkan daur hidup, edisi revisi, penulis, dan media:
    1. **Master Sources Registry (`data/sources_registry.csv`):** Menginventarisasi seluruh sumber PKN dengan penugasan Tier (1: Active Truth, 2: Foundational/Legacy, 3: Ephemeral Audio) dan laju peluruhan $\lambda$.
    2. **Kewenangan Penulis (Author Authority):** Menetapkan pengali otoritas penuh ($1.0\times$) untuk Ustadz Abdul Kholiq sebagai perumus utama, dan menyetel bobot lebih rendah ($0.65\times$) untuk penulis lain/eksternal.
    3. **Pengecualian Time-Decay Abadi ($\lambda = 0.0$):** Seluruh dalil Al-Qur'an, Hadits Sunnah Nabawiyah, dan Kitab Turats Ulama Salaf (An-Nawawi, Ibnul Qayyim, Al-Ghazali) dikecualikan mutlak dari peluruhan waktu ($e^0 = 1.0$), sementara tulisan kontemporer yang lebih tua otomatis terdepresiasi seiring berjalannya tahun.
    4. **Perhitungan Time-Decay Dinamis (`scripts/source_precedence.py`):** Menghitung bobot efektif $W_{\text{eff}} = W_{\text{tier}} \times W_{\text{author}} \times e^{-\lambda \cdot \Delta t}$ saat retrieval.
    5. **Relasi Graf *SUPERSEDES* & Penyajian Naskah Quartz:** Menelusuri rantai silsilah revisi (misal: Buku 2024 *supersedes* Diktat 2016). Konsep lama tetap dipertahankan pada blok collapsible `<details><summary>Catatan Sejarah & Evolusi Manhaj</summary></details>` alih-alih dihapus.
  - *Status Kemajuan:*


     - [x] Registry terpusat [`data/sources_registry.csv`](data/sources_registry.csv) `[SELESAI]`


     - [x] Modul kalkulator presedensi [`scripts/source_precedence.py`](scripts/source_precedence.py) `[SELESAI]`


     - [x] Template naskah evolusi di [`pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md`](pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md) `[SELESAI]`
  - *Perkiraan Token AI:* ~50k - 100k token.
  - *Kebutuhan HITL:* Rendah - Sedang.


- [x] **Adopsi Struktur Standar Industri 4 Zona MediaWiki pada Seluruh Template Wiki** `[SELESAI]`
  - *Deskripsi:* Mengintegrasikan 4 zona fungsional standar MediaWiki ke dalam sistem Wiki PKN (Quartz v5):
    1. **Zona 1 (Header dan Kontrol Halaman):** Judul artikel (H1/URL slug), tab aksi dokumen (baca/diskusi Giscus/riwayat Git/edit sumber), dan toolbar (search, reader mode, dark mode).
    2. **Zona 2 (Area Konten Utama & Infobox):** Paragraf pembuka (*Lead Section*) dengan TL;DR `> [!SUMMARY]`, Infobox vertikal kanan (`.wiki-infobox`) untuk parameter cepat, Table of Contents otomatis, dan Batang Tubuh Naratif (H2/H3, Obsidian Canvas, Syarah, Tafrith vs Ifrath, Instrumen Terapan).
    3. **Zona 3 (Lampiran & Verifikasi Sumber):** Sub-bab "Lihat Pula" (internal cross-links), "Referensi dan Catatan Kaki" dengan rujukan superskrip `[^1]` dan takhrij Shamela/OpenBayan, `<details>` collapsible untuk raw data/evolusi manhaj, serta "Bacaan Lanjutan dan Pranala Luar".
    4. **Zona 4 (Metadata & Taksonomi Bawah):** Kotak navigasi horizontal (`.wiki-navbox`), kategori dokumen (`[[Kategori:...]]`), tautan mu'jam istilah Arab, dan footer hak cipta/lisensi terbuka.
    5. **Dukungan SCSS & Linter:** Menambahkan styling CSS responsive `.wiki-infobox` & `.wiki-navbox` pada `quartz/styles/custom.scss` serta rule audit kepatuhan di `scripts/wiki_linter.py`.
  - *Status Kemajuan:*


    - [x] Panduan arsitektur & template master di [`pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md`](pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md) `[SELESAI]`


    - [x] Spesifikasi pipeline fokus tema di [`pipeline_designs/03_pipeline_halaman_fokus_satu_tema.md`](pipeline_designs/03_pipeline_halaman_fokus_satu_tema.md) `[SELESAI]`


    - [x] Parameter audit kepatuhan di [`pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md`](pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md) & [`scripts/wiki_linter.py`](scripts/wiki_linter.py) `[SELESAI]`


    - [x] Styling CSS responsive di [`quartz/styles/custom.scss`](quartz/styles/custom.scss) `[SELESAI]`
  - *Perkiraan Token AI:* ~40k - 80k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Standarisasi Templat Halaman Khusus Non-Penjelasan (MediaWiki Technical Namespaces)** `[SELESAI]`
  - *Deskripsi:* Merancang 8 templat khusus pembeda untuk halaman non-penjelasan sesuai arsitektur MediaWiki:
    1. **Halaman Disambiguasi:** Format pemilah istilah multitafsir berikon `🔀` dengan navigasi pembeda cepat tanpa uraian panjang.
    2. **Halaman Pengalihan (Redirect):** Stub rujukan dan pemetaan `aliases` frontmatter untuk variasi sinonim/ejaan lama.
    3. **Halaman Daftar Terstruktur:** Matriks data padat tabel (TB-40 40 karakter, indeks hadits, direktori sekolah mitra) dengan statistik agregat.
    4. **Portal Tematik:** Hub kurasi modular berbasis grid kartu untuk pintu masuk rumpun keilmuan besar (Insan, Metode, Praktik, Parenting).
    5. **Halaman Proyek & Kebijakan (Namespace `Wiki-PKN:`):** Standar tata kelola, aturan redaksi, konsensus dewan, dan batasan HITL.
    6. **Templat Pemeliharaan (Noticebox):** Box evaluasi modular di atas artikel (butuh takhrij `⚠️`, konsep terdahulu/superseded `🕰️`, artikel rintisan/stub `🌱`).
    7. **Halaman Berkas / Media:** Dokumentasi metadata aset banner, diagram canvas, dan audio rekaman.
    8. **Halaman Profil Pengguna / Kontributor:** Biodata asatidzah/guru praktisi + ruang *sandbox* (bak pasir) draf pribadi.
    9. **Komponen CSS:** Dukungan styling `.wiki-noticebox` dan `.wiki-portal-*` di `quartz/styles/custom.scss`.
  - *Status Kemajuan:*


    - [x] Dokumen spesifikasi di [`pipeline_designs/SPECIAL_PAGE_TEMPLATES.md`](pipeline_designs/SPECIAL_PAGE_TEMPLATES.md) `[SELESAI]`


    - [x] Komponen styling CSS di [`quartz/styles/custom.scss`](quartz/styles/custom.scss) `[SELESAI]`


    - [x] Referensi indeks di [`pipeline_designs/README.md`](pipeline_designs/README.md) `[SELESAI]`
  - *Perkiraan Token AI:* ~35k - 70k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Pengarsipan & Pemosisian Kanonikal Buku Tafsir Bakat Master (Karya Terpenting Kedua)** `[SELESAI]`
  - *Deskripsi:* Mengarsipkan naskah master lengkap *Buku Tafsir Bakat (Edit 31)* karya Ustadz Abdul Kholiq dari `/home/abuhafi/Downloads/` ke `sources/buku_tafsir_bakat/` (118.464 kata, 871.135 karakter, 4.440 paragraf mencakup Bab 1–12 lengkap):
    1. **Penetapan Otoritas Tier 1 (Active Truth):** Diposisikan tepat setelah Buku Utama PKN sebagai buku babon kedua rujukan taksonomi 40 karakter, silsilah akhlak, profesi peradaban, dan terapi ilaj nabawi.
    2. **Penggantian Total (*Full Supersedes*):** Menegaskan status bahwa naskah ini menggantikan secara utuh Bab 8 Buku Utama PKN terdahulu (ST-30 / Talents Mapping) pada `data/sources_registry.csv` dan `pipeline_designs/05_pipeline_halaman_bakat.md`.
    3. **Parser & Ingestion Engine (`scripts/ingest_tafsir_bakat_book.py`):** Mengekstrak seluruh bab dan 40 pilar ke format JSON terstruktur (`data/buku_tafsir_bakat_extracted.json`) siap diproses ke naskah wiki Quartz.
  - *Status Kemajuan:*


    - [x] Berkas arsip di [`sources/buku_tafsir_bakat/`](sources/buku_tafsir_bakat/) `[SELESAI]`


    - [x] Pendaftaran presedensi di [`data/sources_registry.csv`](data/sources_registry.csv) `[SELESAI]`


    - [x] Ingestion parser di [`scripts/ingest_tafsir_bakat_book.py`](scripts/ingest_tafsir_bakat_book.py) `[SELESAI]`


    - [x] Basis data ekstraksi di [`data/buku_tafsir_bakat_extracted.json`](data/buku_tafsir_bakat_extracted.json) `[SELESAI]`
  - *Perkiraan Token AI:* ~40k - 80k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Kodifikasi Penuh Folder 'Arsitektur PKN' & Integrasi 6 Sektor Makro PKN** `[SELESAI]`
  - *Deskripsi:* Menyusun 7 artikel ensiklopedis di `content/Arsitektur PKN/` yang berpasangan 1-to-1 dengan kanvas arsitektur (`00` s.d `06`), menerapkan standar 4-Zone MediaWiki (Action Bar, Infobox, Lead TL;DR, Canvas Embed, Syarah, Navbox, Takhrij), dan lolos audit linter (skor 90/100) serta verifikasi `npx quartz build` exit code 0.
  - *Status Kemajuan:*


    - [x] 7 file Markdown di [`content/Arsitektur PKN/`](content/Arsitektur%20PKN/) `[SELESAI]`


    - [x] Styling Action Bar `.wiki-action-bar` di [`quartz/styles/custom.scss`](quartz/styles/custom.scss) `[SELESAI]`


    - [x] Pemutakhiran [`content/Peta Navigasi Wiki PKN.md`](content/Peta%20Navigasi%20Wiki%20PKN.md) `[SELESAI]`


    - [x] Kompilasi bersih Quartz v5 & sinkronisasi Git `[SELESAI]`
  - *Perkiraan Token AI:* ~60k - 100k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Integrasi Komprehensif 40 Pilar Bakat Fitrah TB-40 dari Buku Tafsir Bakat ke 4-Zone MediaWiki** `[SELESAI]`
  - *Deskripsi:* Mengembangkan engine `scripts/enrich_tb40_with_book.py` untuk menyerap seluruh naskah master *Buku Tafsir Bakat* Bab 12 (40 pilar, 9 aspek komprehensif) ke dalam 40 artikel di `content/Paradigma - Implementasi PKN/.../TB40/`. Seluruh artikel mematuhi arsitektur MediaWiki 4-Zone, Progressive Disclosure, dan mencapai rata-rata skor linter 90.0/100.
  - *Status Kemajuan:*


    - [x] Engine integrasi di [`scripts/enrich_tb40_with_book.py`](scripts/enrich_tb40_with_book.py) `[SELESAI]`


    - [x] 40 file Markdown TB-40 ter-upgrade 100% `[SELESAI]`


    - [x] Verifikasi build Quartz v5 (2.148 files emitted) & sinkronisasi Git `[SELESAI]`
  - *Perkiraan Token AI:* ~80k - 150k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Transformasi Komprehensif Seluruh Konten Repositori ke 4-Zone MediaWiki (382 Berkas)** `[SELESAI]`
  - *Deskripsi:* Menyelesaikan seluruh batch transformasi repositori (71 artikel Core Manhaj Paradigma, 121 artikel buletin parenting Materi SOTAB, dan 122 artikel Kajian Video) ke arsitektur MediaWiki 4-Zone, menambahkan Action Bar, Infobox terstruktur, Lead TL;DR, Canvas Embed, Protokol EMISOL, dan Navbox.
  - *Status Kemajuan:*


    - [x] 71 Berkas Core Manhaj di [`content/Paradigma - Implementasi PKN/`](content/Paradigma%20-%20Implementasi%20PKN/) `[SELESAI]`


    - [x] 121 Berkas Studi Kasus di [`content/Materi SOTAB/`](content/Materi%20SOTAB/) `[SELESAI]`


    - [x] 122 Berkas Media di [`content/Kajian Video/`](content/Kajian%20Video/) `[SELESAI]`


    - [x] Penyelarasan alias kunci & perbaikan index.md `[SELESAI]`


    - [x] Verifikasi build Quartz v5 (2.157 files emitted, exit code 0) & sinkronisasi Git `[SELESAI]`
  - *Perkiraan Token AI:* ~120k - 200k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Glosarium Resmi PKN & Purifikasi Kosakata Autentik Sumber (383 Berkas)** `[SELESAI]`
  - *Deskripsi:* Menerbitkan master Glosarium Istilah Karakter Nabawiyah ([`content/Glosarium Istilah Karakter Nabawiyah.md`](content/Glosarium%20Istilah%20Karakter%20Nabawiyah.md)) dengan indeks A–Z, matriks tematik 6 klaster, definisi syar'i-pedagogis, serta melakukan purifikasi 630+ kemunculan kosakata asing/tidak bersumber di seluruh repositori (mengganti *etape* menjadi *fase*, *archetype* menjadi *uswah sahabat*, dan merename 4 kanvas fase usia).
  - *Status Kemajuan:* Selesai penuh (383 berkas terverifikasi, Quartz build sukses dengan 2.172 file statis, Portainer live HTTP/2 200 OK).


- [x] **Milestone 62: Kaidah Zarkasyi, Firasat Nabawiyah, Callout Kontras, CI/CD Pipeline & Navigasi Sync** `[SELESAI]`
  - *Deskripsi:* Eksekusi empat pilar pengembangan Wiki PKN:
    1. **R1 (Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi):** Naskah 4-Zone lengkap di `content/Referensi/Tokoh & Pemikiran/Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi.md` mengurai Trilogi Hierarki Pendidikan (*Al-Maddah, Ath-Thariqah, Al-Mudarris, Ruhul Mudarris*), takhrij dalil hadits bersanad, syarah ulama salaf, matriks 4 level, dan Obsidian Canvas interaktif piramida hierarki di `content/canvas/`.
    2. **R2 (Firasat Nabawiyah & 2 Dalil Mandiri):** Naskah konsep 4-Zone di `content/.../Kaidah & Elemen/Firasat.md` membedakan metode firasat universal dari bakat TB-40 #07, syarah Ibnul Qayyim 3 tingkatan firasat (*Madarijus Salikin*), matriks 8 kasus tanda lahiriah ke batiniah, protokol latihan observasi, Canvas 3 dimensi di `content/canvas/`, serta penerbitan 2 halaman dalil mandiri di `content/Dalil/` (`dalil-firasat-mukmin-cahaya-allah.md` dan `dalil-al-mutawassimin-tanda-kebesaran-allah.md`).
    3. **R3 (Callout Kontras Dua Kolom & Eliminasi Teks Generik):** Pembaruan master template `Template Elemen Refleksi, Implementas, Risiko, dan Tautan.md` dengan format tabel kontras dua kolom (`🔴 Kebiasaan Umum vs. ✅ Pendekatan PKN`), implementasi 45 pasang butir kontras kontekstual pada 9 artikel pilar prioritas tinggi, dan eliminasi 100% placeholder generik.
    4. **R4 (Pipeline GitHub Actions CI/CD):** Penyusunan `.github/workflows/deploy.yml` dengan arsitektur fail-fast 2 job (`corpus-lint` Python 3.12 dan `quartz-build` Node.js 22), caching npm/plugins, link resolver patch, artifact upload `quartz-build-output`, dan webhook Portainer.
    5. **R5 (Sinkronisasi Navigasi, Linter Korpus & Quartz Build):** Pembaruan `nav_structure.json` mencakup simpul Zarkasyi, Firasat, dan 2 Dalil (total 148 simpul, 120 simpul daun, 0 broken leaf), 87 unit tests lulus 100%, linter korpus `scripts/wiki_corpus_linter.py` lolos bersih (0 broken link, 0 vocabulary violation, skor Clarity 86.3/100), dan kompilasi statis `npx quartz build` sukses memproses 484 berkas (2.713 file statis, exit code 0).
  - *Perkiraan Token AI:* ~180k - 300k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Milestone 63: Sinkronisasi Status, Perluasan Callout Kontras, Bank Cerita Sirah & Apersepsi KBM, Infografis WAG, dan Riset Turats Parenting OpenBayan** `[SELESAI]`
  - *Deskripsi:* Eksekusi komprehensif lima pilar penyempurnaan konten dan riset repositori Wiki PKN:
    1. **R1 (Sinkronisasi Status TODO.md):** Penyelarasan checklist `[x] [SELESAI]` pada `TODO.md` baris 145 (Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi) dan baris 168 (Firasat Nabawiyah beserta 2 dalil mandirinya), memastikan 100% konsistensi dokumentasi terhadap berkas deliverable fisik repositori.
    2. **R2 (Perluasan Retroaktif Callout Kontras Refleksi):** Injeksi komponen callout tabel kontras dua kolom (`> [!info] Refleksi Harian: Kebiasaan Umum vs. Pendekatan PKN`) berisi 5 pasang butir kontras operasional (total 60 pasang kontras baru) pada 12 artikel pilar inti PKN di `content/Paradigma - Implementasi PKN/` (*Hakikat Insan*, *Tujuan Hidup Manusia*, *Fitrah Belajar*, *4 Kaidah Implementasi*, *Batas Toleransi*, *Tangki Cinta*, *Kesadaran Beramal*, *Imunitas Sosial*, *Tazkiyatun Nafs*, *Peran Guru*, *4 Elemen Implementasi*, *8 Standar Implementasi PKN*), serta eliminasi 100% placeholder generik tanpa sisa.
    3. **R3 (Bank Cerita Sirah & Apersepsi KBM):** Penerbitan dokumen master 4-Zone di `content/Toolkit KBM/Bank Cerita Sirah dan Apersepsi KBM.md` (549 baris) memuat 12 riwayat sirah & atsar sahabat shahih/hasan terpetakan dalam 4 tema (Sains, Sosial, Matematika, Adab), *Inquiry Prompts Bahasa Hati* 3 tingkat, *Rubrik Refleksi Adab Non-Angka* (BT, MT, BK, MM), dan SOP KBM 5 menit bagi pendidik.
    4. **R4 (Infografis Ringkasan Materi PKN Siap Sebar):** Penerbitan dokumen 4-Zone di `content/Toolkit KBM/Infografis Ringkasan Materi PKN Siap Sebar.md` (366 baris) dengan 10 kartu konsep pokok PKN dalam format Dual-Layer (tampilan visual responsif web + blok teks raw monospace siap salin WhatsApp berformat `*bold*` dan `_italic_`), serta Kalender Siar 10 Hari bagi kemitraan sekolah dan orang tua.
    5. **R5 (Riset Khazanah Turats Parenting via OpenBayan):** Eksekusi riset internal di `sources/audit_dalil_parenting/` (4 berkas kerja ~80 KB: `00_README_dan_Metodologi.md`, `01_sweeping_hadits_tarbiyah.md` dengan 22 hadits/atsar terstandar, `04_gap_analysis_belum_disebutkan.md` membedah 6 gap kunci terhadap 86 halaman dalil eksisting, dan `06_rekomendasi_pengayaan_konten.md` perumusan 6 dalil mandiri baru serta matriks pengayaan 10 artikel pilar), 100% bebas istilah terlarang.
    6. **Sinkronisasi Navigasi Sidebar & Verifikasi Kualitas:** Pembaruan `nav_structure.json` dengan penambahan simpul Bank Cerita Sirah dan Infografis WAG (total 150 simpul, 122 daun), sinkronisasi assertion `tests/test_nav_structure.py`, kelulusan 87 unit tests (100% pass), linter korpus `scripts/wiki_corpus_linter.py` bersih (0 broken links, 0 prohibited terms, skor Clarity 86.32/100), dan kompilasi statis Quartz v5 sukses memproses 486 berkas markdown (2.746 berkas statis, exit code 0).
  - *Perkiraan Token AI:* ~200k - 350k token.
  - *Kebutuhan HITL:* Rendah.


- [x] **Milestone 64: Arsitektur Hibrida, Taksonomi 13 Persona, Blueprint Mobile & Dewan Syura LLM Council Karpathy** `[SELESAI]`
  - *Deskripsi:* Eksekusi komprehensif Information Architecture interdisipliner, evaluasi kualitas hibrida, blueprint mobile, dan integrasi metodologi Karpathy LLM Council:
    1. **R1 (Arsitektur Informasi & Analisis Desain Interdisipliner):** Penerbitan 6 dokumen komprehensif di `analisis-desain/` (audit kognitif 486 halaman, kerangka 4 pilar psikologi kognitif/IA/pedagogi/desain sistem, taksonomi persona, pemetaan journey, rekomendasi 6 hub MOC, dan rencana aksi bertahap).
    2. **R2 (Taksonomi 13 Persona Pengguna Berstandar Desain):** Penerbitan 13 berkas persona terstandarisasi di `analisis-desain/persona/` membedakan peran gender (01a Ayah/Qawwam vs 01b Ibu/Madrasah Ula), 5 fase pendidik (02a Thufulah 0-6, 02b Tamyiz 7-10, 02c Murahaqah 11-14, 02d Baligh 15-17, 02e Dewasa 18+), 2 jenis tata kelola lembaga (03a Formal vs 03b Non-Formal), Santri (04), Pengkaji Kurikulum (05), serta Siswa/Remaja (06) dan Masyarakat Umum (07) untuk pengembangan diri mandiri.
    3. **R3 (Pipeline 11: Evaluasi Kualitas Hibrida Rule-Based + System One):** Spesifikasi pada `pipeline_designs/11_hybrid_quality_evaluation_system_one.md`, implementasi mesin evaluasi `<10ms` di `scripts/hybrid_quality_scorer.py` menggabungkan linter regex deterministik dengan scoring terbobot (Tata Bahasa, Kognitif, Struktural, Persona Fit) dan typed decisions (`TERIMA_LANGSUNG`, `PERLU_REVISI_RINGAN`, `TOLAK_DRAF`), serta unit tests komprehensif di `tests/test_hybrid_quality_scorer.py`.
    4. **R4 (Pipeline 12: Dewan Syura Karpathy LLM Council Architecture):** Spesifikasi pada `pipeline_designs/12_dewan_syura_llm_council_architecture.md`, pembaruan master table dan Section 5 pada `pipeline_designs/README.md`, implementasi engine musyawarah 3-tahap di `scripts/llm_council.py` (Tahap 1: 5 Lensa Kognitif Mandiri Faqih Manhaj, Filosof Fitrah, Arsitek Peradaban, Pembaca Awam, Praktisi KBM; Tahap 2: Anonymous Cross-Examination / Peer Review acak A..E; Tahap 3: Chairman Synthesis & Ketetapan Syura format standar), serta unit tests di `tests/test_llm_council.py`.
    5. **R5 (Blueprint Aplikasi Mobile PKN & Verifikasi Korpus):** Perumusan arsitektur aplikasi mobile di `IDE_APLIKASI_MOBILE_PKN.md` (5 target segmen pengguna, offline-first sync, batasan observasi, privasi data anak). Verifikasi 121 unit tests lulus 100% (skipped=5, failures=0), linter korpus `scripts/wiki_corpus_linter.py` lolos bersih (0 broken links, 0 prohibited terms, skor Clarity 86.28/100).
  - *Perkiraan Token AI:* ~220k - 380k token.
  - *Kebutuhan HITL:* Rendah.


---

## 8.7 Visualisasi Media & Aksesibilitas Pembaca

- [x] **Infografis Ringkasan Siap Sebar (Format WhatsApp/Media Sosial)** `[SELESAI]`
  - *Deskripsi:* Desain ringkasan 1 lembar visual (1080x1080 / PDF 1 halaman) materi pokok untuk memudahkan guru menyebarkannya ke WAG wali murid.
  - *Status Kemajuan:* Selesai penuh pada Milestone 63 (Naskah berstandar MediaWiki 4-Zone di `content/Toolkit KBM/Infografis Ringkasan Materi PKN Siap Sebar.md` memuat 10 kartu konsep pokok PKN dalam format Dual-Layer: container visual responsif web + blok teks raw monospace siap salin WhatsApp berformat `*bold*` dan `_italic_`, serta panduan kalender siar 10 hari).
  - *Perkiraan Token AI:* ~400k - 800k token (ekstraksi intisari artikel, copywriting ringkas, dan penyusunan prompt instruksi desain visual).
  - *Kebutuhan HITL:* Sedang (review kejelasan pesan visual oleh tim media/komunikasi).


---


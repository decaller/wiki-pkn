# Standar Templat Halaman Khusus Wiki-PKN (Arsitektur Ekosistem MediaWiki)

Dokumen ini mendefinisikan arsitektur, spesifikasi teknis, dan rancangan templat untuk **halaman-halaman khusus selain halaman artikel penjelasan (fokus tema)** di lingkungan **Wiki Pendidikan Karakter Nabawiyah (Wiki-PKN)**.

Dalam arsitektur ensiklopedia modern berbasis ekosistem MediaWiki, halaman diklasifikasikan secara tegas berdasarkan **fungsi operasional** dan **ruang nama teknis (*technical namespaces*)** guna memisahkan antara konten pembelajaran materi dengan tata kelola sistem, navigasi tematik, dan disambiguasi istilah.

---

## 1. Taksonomi Halaman Khusus vs Halaman Penjelasan

| Golongan Halaman | Jenis Halaman MediaWiki | Fungsi Operasional di Wiki-PKN | Pola Output Dokumen |
|:---|:---|:---|:---|
| **Penataan Informasi** | **Halaman Disambiguasi** | Memilah istilah syar'i/PKN yang memiliki multitafsir atau kemiripan kata. | Indeks pemilah cepat + penjelasan pembeda 1 baris. |
| | **Halaman Pengalihan (Redirect)** | Meneruskan variasi ejaan, akronim, atau sinonim langsung ke target resmi. | Frontmatter `aliases` Quartz atau stub tautan balik. |
| | **Halaman Daftar Terstruktur** | Agregasi data tabular/matriks (40 Bakat TB-40, Indeks Dalil, Timeline Sejarah). | Tabel interaktif, filter kolom, dan rekap statistik. |
| **Navigasi & Kurasi** | **Portal Tematik** | *Hub* eksplorasi rumpun keilmuan besar (Insan, Metode, Praktik, Parenting). | Dashboard visual kartu topik + panduan alur baca. |
| | **Halaman Kategori** | Taksonomi direktori otomatis berbasis tag dan relasi ontologi. | Pohon kategori + daftar artikel alfabetis otomatis. |
| **Tata Kelola Sistem** | **Halaman Proyek & Kebijakan** | Standar tata kelola, aturan redaksi, hak cipta, dan pedoman editorial. | Dokumen normatif, SOP kurasi, dan batasan HITL. |
| | **Halaman Pengguna / Kontributor** | Kredensial asatidzah, guru, atau kurator + *sandbox* draf pribadi. | Biodata keilmuan, riwayat kontribusi, dan ruang uji draf. |
| **Metadata Berkas** | **Halaman Berkas / Media** | Dokumentasi aset ilustrasi banner, diagram canvas, audio, atau PDF. | Metadata hak cipta, resolusi asli, dan daftar penggunaan di artikel. |
| **Templat Modular** | **Templat Pemeliharaan (Noticebox)** | Banner evaluasi status artikel (Butuh Takhrij, Revisi Manhaj, Draf). | Callout khusus di atas naskah penanda status audit. |

---

## 2. Templat 1: Halaman Disambiguasi (*Disambiguation Page*)

Halaman disambiguasi digunakan ketika sebuah istilah dalam PKN memiliki beberapa penerapan berbeda (misal: istilah **"Adab"** bisa merujuk pada *Adab kepada Allah*, *Adab kepada Orang Tua*, *Adab Penuntut Ilmu*, atau *Adab Sebelum Ilmu*).

### Karakteristik:
* Menggunakan noticebox pembuka berikon pemilah (`🔀`).
* Tidak memuat uraian dalil panjang, melainkan definisi pembeda ringkas (1–2 kalimat) disertai tautan `[[Nama Artikel Target]]`.
* Tag taksonomi: `jenis/disambiguasi`, `pkn/navigasi`.

```markdown
---
title: "[Nama Istilah] (Disambiguasi)"
description: "Halaman pemilah arti untuk istilah [Nama Istilah] dalam Manhaj Pendidikan Karakter Nabawiyah."
tags:
  - jenis/disambiguasi
  - pkn/navigasi
---

<div class="wiki-noticebox wiki-noticebox-disambig">
  <div class="wiki-noticebox-icon">🔀</div>
  <div class="wiki-noticebox-body">
    <b>Halaman Disambiguasi:</b> Istilah <b>[Nama Istilah]</b> memiliki beberapa pengertian berbeda dalam kurikulum PKN. Silakan pilih konteks halaman yang sesuai dengan kebutuhan telaah Anda di bawah ini.
  </div>
</div>

# [Nama Istilah] (Disambiguasi)

Istilah **[Nama Istilah]** dalam literatur tarbiyah nabawiyah dan modul Pendidikan Karakter Nabawiyah merujuk pada beberapa konsep berikut:

### Konsep Pokok & Filosofis
* **[[[Nama Istilah] (Konsep Teologis)]]** — Pemaknaan istilah ini dalam kerangka tauhid dan pemenuhan hak-hak rububiyah Allah ﷻ.
* **[[[Nama Istilah] (Psikologi Fitrah)]]** — Manifestasi istilah ini dalam struktur jiwa (*Nafs*) dan dorongan potensi bawaan anak.

### Penerapan Lapangan Berdasarkan Fase Usia
* **[[[Nama Istilah] pada Fase Thufulah]]** — Pembiasaan istilah ini untuk anak rentang usia 0–7 tahun berbasis Bahasa Hati.
* **[[[Nama Istilah] pada Fase Tamyiz]]** — Penanaman kesadaran nalar dan perintah shalat berbatas tegas untuk rentang 7–10 tahun.

### Taksonomi Bakat & Asesmen TB-40
* **[[TB40-[Kode]-[Nama Pilar]]]** — Karakter perilaku nomor [X] dalam 40 Karakter Nabawiyah yang berkaitan dengan sifat ini.

---

<div class="wiki-disambig-footer">
  <i>Catatan: Jika Anda tiba di halaman ini melalui tautan internal di sebuah artikel, silakan perbaiki tautan tersebut agar langsung mengarah ke halaman tujuan yang spesifik.</i>
</div>

**Kategori Direktori:** [[Kategori:Halaman Disambiguasi]]
```

---

## 3. Templat 2: Halaman Pengalihan (*Redirect Stub*)

Di Quartz v5, pengalihan diatur terutama via array `aliases:` pada frontmatter artikel target. Namun, jika diperlukan berkas fisik stub (misal untuk mencatat jejak pustaka atau histori URL lama), gunakan templat stub ini.

```markdown
---
title: "[Variasi Ejaan / Istilah Lama / Akronim]"
aliases:
  - "[Slug-Alternatif]"
---

<div class="wiki-noticebox wiki-noticebox-redirect">
  <div class="wiki-noticebox-icon">↪️</div>
  <div class="wiki-noticebox-body">
    <b>Pengalihan Halaman:</b> Halaman ini diteruskan ke artikel rujukan resmi: <b>[[[Nama Artikel Target Resmi]]]</b>.
  </div>
</div>

# Mengalihkan ke [[[Nama Artikel Target Resmi]]]...

Halaman ini merupakan variasi ejaan, istilah bahasa Arab, atau judul terdahulu dari konsep **[[[Nama Artikel Target Resmi]]]**. Pembaca disarankan membaca rujukan baku pada artikel utama.

*Alasan Pengalihan:*
* Standarisasi istilah Manhaj PKN Edisi 2024.
* Pengalihan sinonim mu'jam: *[Istilah Arab]* $\to$ *[Istilah Baku Bahasa Indonesia]*.
```

---

## 4. Templat 3: Halaman Daftar Terstruktur (*Structured List Page*)

Format ini dipakai untuk menginventarisasi kumpulan data kuantitatif/kualitatif dalam skala besar, seperti **Daftar 40 Karakter TB-40**, **Katalog Lengkap Hadits Tarbiyah**, atau **Daftar Lembaga Mitra SKIS**.

### Karakteristik:
* Tidak memuat paragraf naratif emosional Ustadz Abdul Kholiq.
* Fokus pada kepadatan data tabular (*high density table*), ringkasan metrik, dan tombol lompatan cepat.

```markdown
---
title: "Daftar [Entitas / Data Agregat PKN]"
description: "Daftar terstruktur dan indeks lengkap [Entitas] dalam ekosistem Pendidikan Karakter Nabawiyah."
tags:
  - jenis/daftar
  - pkn/inventaris
---

<div class="wiki-infobox">
  <div class="wiki-infobox-header">Metrik Daftar</div>
  <table class="wiki-infobox-table">
    <tr>
      <th>Total Entitas</th>
      <td><b>[40 Pilar / 120 Hadits]</b></td>
    </tr>
    <tr>
      <th>Dasar Rujukan</th>
      <td>[[Sumber Rujukan Resmi]]</td>
    </tr>
    <tr>
      <th>Status Verifikasi</th>
      <td><span style="color: green;"><b>Terverifikasi 100%</b></span></td>
    </tr>
    <tr>
      <th>Terakhir Diperbarui</th>
      <td>2026-09-22</td>
    </tr>
  </table>
</div>

# Daftar [Entitas / Data Agregat PKN]

> [!SUMMARY] Cakupan Data
> Daftar ini menghimpun seluruh [nama entitas] yang menjadi instrumen resmi PKN. Kolom tabel mencakup kode taksonomi, nama pilar syar'i, kutub energi, teladan sahabat Nabi, dan tautan rujukan mendalam.

---

## Ringkasan Agregat & Distribusi

| Kluster Aksi | Jumlah Karakter | Rumpun Jiwa | Keterangan |
|:---|:---:|:---|:---|
| **Bekerja Keras** | 7 Pilar | Karsa (*Al-Hawa*) | Daya juang dan ketahanan fisik |
| **Berpikir** | 8 Pilar | Cipta (*Al-'Aql*) | Analisis nalar dan strategi |
| **Melayani** | 7 Pilar | Rasa (*Al-Qalb*) | Afeksi, empati, dan pengorbanan |

---

## Tabel Indeks Lengkap

| No | Kode Pilar | Nama Karakter (Indonesia & Arab) | Kutub Energi | Sahabat Rujukan | Aksi Kuratif ('Ilaj) | Tautan Detail |
|:-:|:---|:---|:---:|:---|:---|:---:|
| 1 | `TB40-01` | **Himmah** (<span dir="rtl">هِمَّة</span>) | Introvert | Abu Bakar Ash-Shiddiq | [[Tawadhu]] | [[01-himmah\|Buka Artikel]] |
| 2 | `TB40-02` | **Syaja'ah** (<span dir="rtl">شَجَاعَة</span>) | Extrovert | Khalid bin Walid | [[Hilm]] | [[02-syajaah\|Buka Artikel]] |
| 3 | `TB40-03` | **Shidq** (<span dir="rtl">صِدْق</span>) | Introvert | Abdullah bin Mas'ud | [[Luthf]] | [[03-shidq\|Buka Artikel]] |

---

## Lihat Pula
* [[Tafsir Bakat 40]] — Penjelasan filosofis sistem asesmen bakat nabawiyah.
* [[Kuisioner Asesmen 40 Bakat Nabawiyah]] — Instrumen tes tertulis santri dan guru.

**Kategori Direktori:** [[Kategori:Daftar Terstruktur PKN]] • [[Kategori:Taksonomi Bakat TB40]]
```

---

## 5. Templat 4: Portal Tematik (*Thematic Portal*)

Portal tematik berfungsi seperti *majalah dinding digital* atau gerbang masuk (*landing hub*) ke dalam satu rumpun materi besar. 

### Karakteristik:
* Layout berupa kisi-kisi kartu modular (*grid card navigation*).
* Menampilkan *Topik Pilihan Bulan Ini*, *Peta Alur Bacaan Bertingkat (Learning Path)*, dan *Koleksi Template Siap Pakai*.

```markdown
---
title: "Portal: [Nama Rumpun Keilmuan / Misal: Tarbiyah Usia Tamyiz]"
description: "Pusat navigasi dan eksplorasi komprehensif materi [Nama Rumpun Keilmuan]."
tags:
  - jenis/portal
  - portal/[nama-portal]
---

<div class="wiki-portal-banner">
  <div class="wiki-portal-badge">PORTAL TEMATIK RESMI</div>
  <h1>Portal: [Nama Rumpun Keilmuan]</h1>
  <p>Pusat Kurasi, Alur Pembelajaran, dan Lembar Operasional KBM Terpadu</p>
</div>

<div class="wiki-portal-grid">
  <div class="wiki-portal-card">
    <div class="wiki-portal-card-header">📖 Fondasi Konsep</div>
    <div class="wiki-portal-card-body">
      Uraian filosofis, dalil shahih Al-Qur'an dan Sunnah, serta syarah ulama salaf.
      <ul>
        <li>[[Koneksi Sebelum Koreksi]]</li>
        <li>[[Tangki Cinta]]</li>
        <li>[[Tujuan Hidup Manusia]]</li>
      </ul>
    </div>
  </div>

  <div class="wiki-portal-card">
    <div class="wiki-portal-card-header">🧭 Peta Alur Belajar</div>
    <div class="wiki-portal-card-body">
      Tahapan membaca berurutan dari pengenalan awal hingga implementasi mandiri.
      <ul>
        <li><b>Tingkat 1:</b> Orientasi Hati & Pembenahan Orang Tua</li>
        <li><b>Tingkat 2:</b> Pembiasaan Nalar & Perintah Shalat 7 Th</li>
        <li><b>Tingkat 3:</b> Ketegasan Berbatas & Bahasa Tangan 10 Th</li>
      </ul>
    </div>
  </div>

  <div class="wiki-portal-card">
    <div class="wiki-portal-card-header">🛠️ Perangkat Guru & Ortu</div>
    <div class="wiki-portal-card-body">
      Formulir observasi, rubrik 3-level, dan panduan dialog malam hari.
      <ul>
        <li>[[Instrumen Evaluasi Kesiapan Transformasi]]</li>
        <li>[[Form Observasi Bahasa Hati]]</li>
        <li>[[Kumpulan Tips Praktisi Respon Cepat]]</li>
      </ul>
    </div>
  </div>

  <div class="wiki-portal-card">
    <div class="wiki-portal-card-header">🗺️ Visualisasi Makro</div>
    <div class="wiki-portal-card-body">
      Bagan Obsidian Canvas arsitektur manhaj interaktif.
      <ul>
        <li>![[canvas/Trilogi_Jiwa.canvas]]</li>
        <li><a href="/content/Peta Navigasi Wiki PKN">Buka Indeks Peta MOC Lengkap &rarr;</a></li>
      </ul>
    </div>
  </div>
</div>

---

**Kategori Direktori:** [[Kategori:Portal Tematik PKN]]
```

---

## 6. Templat 5: Halaman Proyek & Kebijakan Redaksi (*Project & Policy Page*)

Halaman dalam ruang nama *Wiki-PKN:* (Project Namespace) mengatur standar editorial, metodologi verifikasi syar'i, konsensus dewan perumus, dan panduan bagi para kontributor.

```markdown
---
title: "Wiki-PKN: [Nama Kebijakan / Misal: Pedoman Takhrij Dalil & Hak Cipta]"
description: "Ketentuan resmi dewan redaksi mengenai standar verifikasi dalil, presedensi sumber, dan etika penulisan."
tags:
  - jenis/kebijakan
  - meta/editorial
---

<div class="wiki-noticebox wiki-noticebox-policy">
  <div class="wiki-noticebox-icon">⚖️</div>
  <div class="wiki-noticebox-body">
    <b>Kebijakan Resmi Wiki-PKN:</b> Halaman ini memuat konsensus baku redaksi. Seluruh kontributor, editor, dan pipeline agen AI wajib mematuhi ketentuan yang tercantum di bawah ini.
  </div>
</div>

# Wiki-PKN: [Nama Kebijakan]

## 1. Maksud dan Tujuan
[Penjelasan normatif mengapa kebijakan ini dibuat, apa tujuannya dalam menjaga kemurnian manhaj dan validitas sanad ilmu].

## 2. Ketentuan Baku (Mandatory Guidelines)
1. **Otoritas Sanad Utama:** Setiap pernyataan konsep wajib bersandar pada naskah resmi Ustadz Abdul Kholiq (bobot 1.0x) atau kutipan kitab salaf bersanad.
2. **Pengecualian Peluruhan Waktu:** Dalil Al-Qur'an dan Hadits tidak mengenal masa kadaluarsa ($\lambda = 0.0$).
3. **Penyajian Bertingkat:** Wajib menerapkan 4 Zona MediaWiki dan Progressive Disclosure.

## 3. Prosedur Eskalasi & Konsensus Redaksi
Jika terjadi perbedaan pendapat penafsiran materi di lapangan, mekanisme penyelesaian dilakukan melalui **Dewan Musyawarah Redaksi AI & Asatidzah Penasihat**:
* Tahap 1: Pengecekan silang ke rekaman video/audio kajian primer.
* Tahap 2: Takhrij derajat hadits melalui OpenBayan Qdrant koleksi `shamela_11m`.
* Tahap 3: Keputusan final oleh perumus manhaj.

---

**Kategori Direktori:** [[Kategori:Kebijakan dan Pedoman Wiki-PKN]]
```

---

## 7. Templat 6: Templat Pemeliharaan / Kotak Pemberitahuan (*Maintenance Noticeboxes*)

Templat modular ini disematkan di bagian atas artikel oleh *Linter Agent* atau kurator manusia saat artikel membutuhkan perbaikan mutu:

### Ragam Kotak Pemeliharaan MediaWiki untuk Wiki-PKN:

```html
<!-- 1. PEMBERITAHUAN BUTUH TAKHRIJ / SANAD DALIL -->
<div class="wiki-noticebox wiki-noticebox-warning">
  <div class="wiki-noticebox-icon">⚠️</div>
  <div class="wiki-noticebox-body">
    <b>Memerlukan Verifikasi Dalil:</b> Artikel ini memuat nukilan hadits atau atsar yang belum dilengkapi teks Arab berharakat resmi atau nomor takhrij Maktabah Syamilah. Harap bantu redaksi dengan melengkapi rujukan melalui <a href="/content/Dalil">Pusat Dalil</a>.
  </div>
</div>

<!-- 2. PEMBERITAHUAN KONSEP TELAH DI-SUPERSEDE (CATATAN SEJARAH) -->
<div class="wiki-noticebox wiki-noticebox-legacy">
  <div class="wiki-noticebox-icon">🕰️</div>
  <div class="wiki-noticebox-body">
    <b>Status Konsep: Terdahulu (Superseded):</b> Pendekatan dalam dokumen ini (misal: Talents Mapping / ST-30 Bab 8 lama) telah diperbarui dan digantikan oleh <b>[[Tafsir Bakat 40 (TB-40)]]</b>. Artikel ini dipertahankan sebagai arsip sejarah perkembangan manhaj.
  </div>
</div>

<!-- 3. PEMBERITAHUAN ARTIKEL RINTISAN (STUB) -->
<div class="wiki-noticebox wiki-noticebox-stub">
  <div class="wiki-noticebox-icon">🌱</div>
  <div class="wiki-noticebox-body">
    <b>Artikel Rintisan (Stub):</b> Penjelasan materi ini baru mencakup ringkasan dasar dan bagan konsep. Anda dapat berkontribusi memperluas sub-bab studi kasus lapangan atau syarah ulama salaf.
  </div>
</div>
```

---

## 8. Templat 7: Halaman Dokumentasi Berkas / Media (*File / Media Page*)

Format halaman khusus untuk mengelola aset gambar banner, diagram Obsidian Canvas, rekaman audio, dan berkas PDF:

```markdown
---
title: "Berkas: [Nama Berkas / Misal: Trilogi_Jiwa.canvas]"
description: "Metadata teknis, riwayat versi, lisensi, dan daftar keterpakaian berkas [Nama Berkas]."
tags:
  - jenis/berkas
  - meta/media
---

# Berkas: [Nama Berkas]

![[canvas/[Nama Berkas]]]

## Informasi Berkas & Spesifikasi Teknis
* **Tipe Media:** Obsidian Canvas Diagram (`.canvas`) / WebP Image
* **Resolusi Asli:** 1920 × 1080 px (Rasio 16:9)
* **Ukuran Berkas:** 42 KB
* **Penyusun / Desainer:** Tim Kurasi Visual PKN
* **Lisensi:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

## Penggunaan Berkas di Wiki-PKN
Berkas ini disematkan dan menjadi acuan visual pada halaman-halaman berikut:
1. [[Koneksi Sebelum Koreksi]] — Sebagai Bagan 1.0 Alur Komunikasi Hati.
2. [[Tangki Cinta]] — Sebagai visualisasi cadangan afeksi anak.
3. [[Peta Navigasi Wiki PKN]] — Indeks peta kanvas utama.

---

**Kategori Direktori:** [[Kategori:Berkas Diagram Obsidian Canvas]] • [[Kategori:Media Pembelajaran PKN]]
```

---

## 9. Templat 8: Halaman Profil Pengguna & Bak Pasir (*User Profile & Sandbox Page*)

Untuk para asatidzah, guru, perumus kurikulum, dan kontributor terdaftar yang memiliki ruang kerja (*workspace*) pribadi:

```markdown
---
title: "Pengguna: [Nama Kontributor]"
description: "Profil kontributor, kredensial keilmuan, dan ruang bak pasir (sandbox) perancangan artikel PKN."
tags:
  - jenis/pengguna
  - meta/kontributor
---

<div class="wiki-infobox">
  <div class="wiki-infobox-header">[Nama Kontributor]</div>
  <table class="wiki-infobox-table">
    <tr>
      <th>Peran Redaksi</th>
      <td><b>Kurator Syar'i / Guru Praktisi</b></td>
    </tr>
    <tr>
      <th>Lembaga</th>
      <td>[[Sekolah Karakter Imam Syafi'i (SKIS)]]</td>
    </tr>
    <tr>
      <th>Fokus Telaah</th>
      <td>Tarbiyah Usia [[Tamyiz]] & Kurikulum Adab</td>
    </tr>
    <tr>
      <th>Bergabung Sejak</th>
      <td>2024</td>
    </tr>
  </table>
</div>

# Pengguna: [Nama Kontributor]

Selamat datang di ruang kontributor saya di Wiki Pendidikan Karakter Nabawiyah. Halaman ini memuat fokus riset tarbiyah saya, daftar artikel yang aktif saya rawat, serta tautan ke halaman bak pasir draf.

## Bidang Kontribusi & Riset Lapangan
* Penyusunan panduan komunikasi Bahasa Hati untuk guru SD/Madrasah.
* Validasi rubrik non-angka 3-level ketercapaian adab santri.

## Ruang Bak Pasir Pribadi (Personal Sandbox)
* [[Pengguna:[Nama Kontributor]/Bak Pasir/Draf Modul Adab Makan]] — Eksperimen naskah KBM adab makan sebelum rilis ke repositori resmi.
* [[Pengguna:[Nama Kontributor]/Catatan Lapangan Kasus Gadget]] — Draf penanganan anak kecanduan gawai di asrama.

---

**Kategori Direktori:** [[Kategori:Kontributor Wiki-PKN]]
```

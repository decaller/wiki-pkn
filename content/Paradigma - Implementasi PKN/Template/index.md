---
title: Standar Template Wiki PKN
aliases:
  - "Template"
---

<!-- ========================================================================== -->
<!-- ZONA 1: HEADER, ACTION BAR & METADATA                                      -->
<!-- ========================================================================== -->

# Template

<div class="wiki-action-bar">
  <span class="wiki-action-item active">📖 Baca</span>
  <a href="https://github.com/decaller/wiki-pkn/discussions" class="wiki-action-item" target="_blank" rel="noopener">💬 Diskusi</a>
  <a href="https://github.com/decaller/wiki-pkn/edit/main/content/Paradigma - Implementasi PKN/Template/index.md" class="wiki-action-item" target="_blank" rel="noopener">✏️ Sunting</a>
  <a href="https://github.com/decaller/wiki-pkn/commits/main/content/Paradigma - Implementasi PKN/Template/index.md" class="wiki-action-item" target="_blank" rel="noopener">📜 Riwayat</a>
  <span class="wiki-action-meta">Otoritas: Tier 1 (Active Truth) • [[Paradigma & Implementasi]]</span>
</div>


<!-- ========================================================================== -->
<!-- ZONA 2: AREA KONTEN UTAMA, INFOBOX, LEAD SECTION & BATANG TUBUH            -->
<!-- ========================================================================== -->

<div class="wiki-infobox">
  <div class="wiki-infobox-header">Template</div>
  <div class="wiki-infobox-image">
    <div style="padding: 1.25rem 1rem; background: linear-gradient(135deg, #1e3a8a, #0d9488); color: white; text-align: center; border-radius: 6px;">
      <div style="font-size: 1.8rem; font-weight: 700; margin-bottom: 0.35rem;">🏛️ PKN</div>
      <div style="font-weight: 600; font-size: 0.9rem;">Template</div>
    </div>
    <div class="wiki-infobox-caption">Manhaj Pendidikan Karakter Nabawiyah</div>
  </div>
  <table class="wiki-infobox-table">
    <tr>
      <th>Topik Inti</th>
      <td><b>Template</b></td>
    </tr>
    <tr>
      <th>Tingkat Otoritas</th>
      <td><b>Tier 1: Active Truth</b> (Buku Utama PKN)</td>
    </tr>
    <tr>
      <th>Kluster Manhaj</th>
      <td>[[Paradigma & Implementasi]]</td>
    </tr>
    <tr>
      <th>Bagan Konsep</th>
      <td>[[canvas/Arsitektur PKN/06 - Implementasi & Rantai Kausalitas.canvas]]</td>
    </tr>
    <tr>
      <th>Kaidah Asas</th>
      <td>Koneksi Sebelum Koreksi</td>
    </tr>
  </table>
</div>


> [!SUMMARY] Ringkasan Eksekutif (TL;DR Lead Section)
> **Hakikat Konsep:** **index** adalah pilar fundamental dalam Manhaj Pendidikan Karakter Nabawiyah yang mengarahkan proses tarbiyah dari penegakan tauhid batin menuju pembiasaan amal shalih lahiriah.
> * **Prinsip Utama:** Mengutamakan pengisian tangki cinta (*Koneksi Sebelum Koreksi*) dan menghormati tahapan fitrah anak (*Tadarruj*).
> * **Orientasi Akhir:** Menghantarkan santri menjadi pribadi yang *Sholih* (selamat akidah & ibadahnya) dan *Muslih* (pelopor peradaban yang bermanfaat bagi ummah).



Halaman ini merupakan pedoman standarisasi penulisan, format struktur, dan kriteria penilaian mutu artikel bagi seluruh kontributor yang menyusun konten di dalam **Wiki Pendidikan Karakter Nabawiyah (PKN)**.

> [!quote] Dalil & Rujukan Nabawiyah: Bekerja dengan Kualitas Tertinggi (Itqan)
> **Naskah Hadits:**  
> « إِنَّ اللَّهَ يُحِبُّ إِذَا عَمِلَ أَحَدُكُمْ عَمَلًا أَنْ يُتْقِنَهُ »
> 
> *"Sesungguhnya Allah mencintai seseorang di antara kalian yang apabila melakukan suatu pekerjaan, ia mengerjakannya dengan tekun, cermat, dan berkualitas tinggi (itqan)."*  
> — **HR. Al-Baihaqi (Syu'abul Iman No. 4930)**
> 
> 💡 **Relevansi PKN:** Menulis dan mendokumentasikan ilmu tarbiyah nabawiyah adalah amal jariyah yang menuntut kesungguhan ilmiah (*itqan*), kejelasan takhrij dalil, kerapian tipografi, dan kelengkapan materi.

---

## 1. Ambang Batas Kualitas Artikel Wiki PKN (Standar Emas)

Setiap artikel substantif di Wiki PKN wajib memenuhi ambang batas kualitas berikut:
1. **Panjang Karakter:** Minimal **5.000 karakter** (sekitar 750–1.200 kata) konten akademik berbobot tanpa pengulangan kata kosong (*filler*).
2. **Keaslian Dalil:** Memuat setidaknya **1 dalil Al-Qur'an** dan **1 hadits shahih** berharakat lengkap, terjemahan resmi bahasa Indonesia, dan takhrij kitab induk dari korpus **OpenBayan** (`data/shamela_corpus.db`).
3. **Kutipan Ulama Klasik:** Mengintegrasikan penjelasan (*syarah*) dari ulama mu'tabar seperti *Ibnul Qayyim, Imam Al-Ghazali, Ibnu Katsir, Ibnu Hajar, An-Nawawi, Ibnu Khaldun, atau Asy-Syathibi*.
4. **Keteladanan Shahabat Nabi ﷺ:** Menyertakan kisah nyata interaksi tarbiyah Rasulullah ﷺ dengan para sahabat (dewasa maupun anak-anak).
5. **Kesesuaian Format Quartz:** Menggunakan frontmatter YAML yang valid, callout Obsidian (`[!quote]`, `[!warning]`, `[!info]`, `[!tip]`), serta tautan silang (*wikilinks* ``...``).

---

## 2. Anatomi Baku 9 Lapisan Halaman Wiki PKN

Untuk menciptakan pengalaman membaca yang seragam, elegan, dan teratur di seluruh 120+ halaman Wiki PKN, setiap artikel wajib mengikuti **urutan hierarki 9 lapisan baku** berikut tanpa membolak-balik posisinya:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Frontmatter YAML (title, description, tags, aliases)      │
├─────────────────────────────────────────────────────────────┤
│ 2. Banner Visual Header (!`assets/banners/...`)           │
├─────────────────────────────────────────────────────────────┤
│ 3. Catatan Metodologi & Rekonstruksi AI ([!note])           │
├─────────────────────────────────────────────────────────────┤
│ 4. Judul Artikel (# Judul) & Paragraf Pengantar Konseptual  │
├─────────────────────────────────────────────────────────────┤
│ 5. Dalil Utama & Takhrij Nabawiyah ([!quote])                │
├─────────────────────────────────────────────────────────────┤
│ 6. Batang Tubuh Materi Substantif (## & ### + Tabel + Canvas)│
├─────────────────────────────────────────────────────────────┤
│ 7. Trio Callout Refleksi Akhir Konten:                      │
│    • [!info] Refleksi Lapangan                              │
│    • [!warning] Peringatan Risiko & Tafrith-Ifrath          │
│    • [!tip] Rekomendasi Aksi & Solusi Praktis               │
├─────────────────────────────────────────────────────────────┤
│ 8. Dokumen & Rujukan Resmi ([!quote] / Daftar Pustaka)       │
├─────────────────────────────────────────────────────────────┤
│ 9. Media Presentasi & Slide Interaktif (Office Web Apps)    │
│    ⚠️ MUTLAK DI BAGIAN PALING TERAKHIR HALAMAN               │
└─────────────────────────────────────────────────────────────┘
```

---

### Contoh Kerangka Kode Baku Halaman:

```markdown
---
title: "Judul Bersih Artikel"
description: "Deskripsi ringkas 1-2 kalimat mengenai esensi materi untuk preview SEO dan metadata pencarian."
tags:
  - pendidikan-karakter-nabawiyah
  - tema-spesifik
aliases:
  - "Template"
  - Alias 1
  - Alias 2
---

![[assets/banners/banner_tema_terkait.webp]]
*Gambar: Ilustrasi visual representatif konsep tarbiyah nabawiyah*


---

## 1. Definisi & Konsep Fondasional
- Makna etimologi (bahasa) dari kamus mu'tabar (*Lisanul 'Arab, Al-Mufradat fi Gharibil Qur'an*).
- Makna terminologi syar'i menurut para ulama salaf.
- Kedudukan konsep dalam trilogi jiwa (*Muthmainnah, Lawwamah, Ammarah*).

## 2. Relevansi Pedagogis & Syarah Ulama Klasik
- Syarah mendalam dari karya ulama klasik (*Ibnul Qayyim, Al-Ghazali, Ibnu Katsir, Ibnu Hajar*).
- Keteladanan interaksi nyata Rasulullah ﷺ bersama sahabat dewasa dan anak-anak.

## 3. Taksonomi, Komponen & Matriks Karakteristik
- Pemetaan pilar dalam tabel terstruktur.
- Gunakan diagram visual berbasis **Obsidian Canvas** (`.canvas`) jika memerlukan peta konsep relasional; **dilarang keras menggunakan blok Mermaid** demi kompatibilitas penuh Quartz dan interaktivitas canvas viewer.

## 4. Diagnosis Penyimpangan: Tafrith vs Ifrath
- **Tafrith (Meremehkan / Melalaikan):** Gejala kelalaian, pengabaian fitrah, dan dampak psikososial.
- **Ifrath (Berlebihan / Memaksa):** Gejala pemaksaan target berlebihan, kekerasan verbal/fisik, dan trauma batin.
- **Wasathiyah (Jalan Tengah Nabawiyah):** Titik keseimbangan ideal fitrah.

## 5. Panduan Praktis untuk Orang Tua & Pendidik
- Rubrik Observasi Rukun 3A (*Suka/Al-Hirsh, Bisa/Al-Maqdari, Bermanfaat/Al-Mufid*).
- Formulasi dialog hati dan tindakan penegasan adab.

## 6. Penerapan Berdasarkan 4 Fase Usia Perkembangan
- **Fase Thufulah (0–7 Tahun):** Limpahan kasih sayang, bermain aktif, teladan visual, tanpa tuntutan beban nalar formal.
- **Fase Tamyiz (7–10 Tahun):** Pembiasaan adab shalat, tanggung jawab konkret harian, dialog nalar terpandu.
- **Fase Murahaqah (10–15 Tahun):** Penegakan disiplin tegas berbatas syariat, penugasan proyek, pemagangan bakat.
- **Fase Syabab (15+ Tahun):** Kemitraan dewasa, kemandirian finansial dan sosial, karya nyata peradaban.

## 7. Studi Kasus Nyata & Solusi Kuratif Bertahap
- Skenario nyata problematika pengasuhan era digital.
- Langkah kuratif langkah-demi-langkah berlandaskan kaidah PKN (*Tangki Cinta → Bahasa Hati → Bahasa Lisan → Bahasa Tangan*).

## 8. Tautan Konseptual Terkait
- Tautan silang dua arah menggunakan format ``Nama Halaman``.

---

## 9. Trio Refleksi Lapangan, Risiko & Rekomendasi Solusi

> [!info] Refleksi Lapangan: Realitas Penerapan di Lembaga & Keluarga
> Berdasarkan observasi empiris di berbagai sekolah mitra dan pendampingan keluarga, tantangan terbesar bukanlah ketiadaan materi kurikulum, melainkan konsistensi keteladanan pendidik dan ketersediaan waktu luang ayah dalam membangun koneksi batin dengan anak.

> [!warning] Peringatan Risiko: Bahaya Pendekatan Formalitas & Pemaksaan
> Mengukur keberhasilan tarbiyah semata-mata dari hafalan verbal atau kepatuhan semu karena takut hukuman berisiko tinggi melahirkan luka batin menahun (*hutang pengasuhan*), kemunafikan adab, dan resistensi spiritual saat anak memasuki usia aqil baligh.

> [!tip] Rekomendasi Solusi Praktis
> Mulailah dari langkah mikro yang berkesinambungan: hidupkan *meja makan peradaban* minimal satu kali sehari, dengarkan anak tanpa mencela selama 15 menit, dan fokuslah mengasah potensi terkuat dalam 40 pilar [[Bakat]] agar kelemahan terangkat secara alamiah.

---

> [!quote] Dokumen & Slide Presentasi Rujukan Resmi PKN
> - **Materi Terkait:** Panduan Standar PKN & Kurikulum Lembaga Karakter.
> - **Narasumber:** Ustadz Abdul Kholiq (Penggagas Manhaj Pendidikan Karakter Nabawiyah).
> - **Korpus Dalil:** OpenBayan Hadith Dataset (62.169 riwayat terverifikasi).

---

## Media Presentasi & Slide Interaktif (Office Web Apps)

<!-- START_OFFICE_PPTX_EMBED -->
> [!note] Panduan Penempatan Elemen Media
> **PENTING DITAATI:** Bagian ini **WAJIB SELALU DITEMPATKAN DI AKHIR HALAMAN**. Dilarang menyisipkan pemutar slide di tengah-tengah pembahasan materi agar tidak mengganggu alur membaca naskah ilmiah dan mencegah pergeseran tata letak (*Cumulative Layout Shift*).

<div style="position: relative; width: 100%; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px; border: 1px solid var(--lightgray); margin: 1.5rem 0; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);">
  <iframe 
    src="https://onedrive.live.com/embed?resid=PLACEHOLDER_RESID&authkey=PLACEHOLDER_AUTHKEY&em=2" 
    width="100%" 
    height="100%" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
    frameborder="0" 
    scrolling="no" 
    allowfullscreen="true" 
    mozallowfullscreen="true" 
    webkitallowfullscreen="true">
  </iframe>
</div>

<div style="display: flex; gap: 0.75rem; justify-content: flex-end; margin-top: 0.5rem; flex-wrap: wrap;">
  <a href="https://onedrive.live.com/view.aspx?resid=PLACEHOLDER_RESID" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.4rem 0.8rem; border-radius: 6px; background-color: var(--secondary); color: white; text-decoration: none; font-size: 0.85rem; font-weight: 500;">
    <span>Buka di Tab Baru ↗</span>
  </a>
</div>
<!-- END_OFFICE_PPTX_EMBED -->
```

---

## 3. Daftar Template Khusus yang Tersedia

Silakan gunakan master template berikut sesuai jenis dokumen yang hendak ditulis:
* **[[Template Tema]]:** Format baku untuk artikel tema pokok, filosofis, dan bab materi utama.
* **[[Template Elemen Karakteristik]]:** Format baku untuk merinci sifat, bakat, dan profil karakter anak (TB40).
* **[[Template Elemen Refleksi, Implementas, Risiko, dan Tautan]]:** Format baku untuk blok callout studi kasus lapangan, analisis risiko pengasuhan, dan etika penempatan callout penutup.

---

## 4. Kaidah Penyeragaman Elemen Penting (*Rule of Placement*)

Berdasarkan standarisasi desain dan kenyamanan pembaca di seluruh web Wiki PKN, berikut adalah aturan mutlak penempatan elemen yang tidak boleh diubah:

| Komponen Halaman | Posisi Wajib | Alasan & Kaidah Desain |
| :--- | :--- | :--- |
| **Frontmatter YAML** | Baris paling awal (baris 1) | Memuat metadata judul, deskripsi untuk SEO/Search, dan tag index Quartz. |
| **Banner Ilustrasi** | Tepat di bawah frontmatter | Memberikan jangkar visual pertama yang elegan dan membangun kesan profesional (*wow factor*). |
| **Catatan Metodologi** | Sebelum judul `# Judul` | Menjaga transparansi akademis bahwa artikel adalah hasil kurasi AI atas kajian otentik Ustadz Abdul Kholiq. |
| **Dalil Syar'i Utama** | Tepat di bawah paragraf pembuka | Menegaskan bahwa manhaj PKN berpijak kokoh di atas wahyu Al-Qur'an dan Sunnah sebelum uraian teoritis. |
| **Visualisasi Peta Konsep** | Di dalam isi tubuh (Bagian 3) | **Wajib Obsidian Canvas (`.canvas`)**, dilarang Mermaid untuk memastikan fluiditas tampilan dan mencegah crash parsing Quartz. |
| **Trio Callout Refleksi** | **Akhir Konten Materi** | Menjadi rangkuman praktis penutup sebelum pembaca berpindah ke halaman lain atau melihat media. |
| **Sitasi Rujukan Resmi** | Tepat setelah Trio Callout | Menyebutkan narasumber utama, dokumen acuan, dan korpus hadits pendukung. |
| **Media Presentasi (Office Web Apps)** | **MUTLAK PALING AKHIR HALAMAN** | Mengunci elemen interaktif iframe berbobot berat di dasar halaman agar waktu muat teks instan dan navigasi tidak terdistorsi. |

---

## 5. Checklist Verifikasi Mutu Kontributor (Pre-Publishing Review)

Sebelum mengajukan pull request atau mempublikasikan artikel di Wiki PKN, lakukan verifikasi mandiri menggunakan checklist berikut:
- [ ] **Panjang Karakter:** Apakah artikel telah mencapai minimal **5.000 karakter** konten berbobot tanpa filler?
- [ ] **Posisi Media di Paling Akhir:** Apakah bagian *Media Presentasi & Slide Interaktif* berada di urutan mutlak paling akhir halaman (di bawah trio callout dan sitasi)?
- [ ] **Trio Callout Refleksi:** Apakah terdapat 3 callout penutup lengkap (`[!info]` Refleksi Lapangan, `[!warning]` Peringatan Risiko, `[!tip]` Tips Solusi)?
- [ ] **Bebas Diagram Mermaid:** Apakah seluruh diagram menggunakan Obsidian Canvas (`.canvas`) atau tabel Markdown, dan tidak ada blok ```` ```mermaid ````?
- [ ] **Teks Arab & Harakat:** Apakah seluruh kutipan ayat Al-Qur'an dan hadits shahih telah berharakat lengkap tanpa salah ketik?
- [ ] **Takhrij Sumber:** Apakah nomor hadits, nama rawi, dan rujukan kitab induk klasik tertera dengan jelas (merujuk katalog OpenBayan)?
- [ ] **Integrasi Ulama:** Apakah artikel memuat setidaknya satu kutipan syarah dari ulama mu'tabar (*Ibnul Qayyim, Al-Ghazali, An-Nawawi, Ibnu Katsir, dll.*)?
- [ ] **Matriks Tafrith-Ifrath:** Apakah bahasan memuat diagnosis penyimpangan dan solusi wasathiyah nabawiyah?
- [ ] **Fase Usia:** Apakah artikel menguraikan panduan aplikatif berdasarkan 4 fase perkembangan (*Thufulah, Tamyiz, Murahaqah, Syabab*)?
- [ ] **Wikilinks:** Apakah artikel memuat minimal 3 tautan silang valid menggunakan format ``Nama Halaman``?
- [ ] **Kerapian Quartz:** Apakah frontmatter YAML valid dan tidak memicu warning pada `npx quartz build`?



---

<!-- ========================================================================== -->
<!-- ZONA 3: NAVBOX & JEJARING TOPIK TERKAIT                                    -->
<!-- ========================================================================== -->

<div class="wiki-navbox">
  <div class="wiki-navbox-title">
    <span>Hierarki Manhaj Pendidikan Karakter Nabawiyah</span>
    <span>[ [[Peta Navigasi Wiki PKN|Peta Navigasi]] ]</span>
  </div>
  <div class="wiki-navbox-group">
    <div class="wiki-navbox-label">Fondasi Manhaj</div>
    <div class="wiki-navbox-links">
      [[index|Beranda]] <span class="wiki-navbox-sep">•</span>
      [[00 - Master Arsitektur PKN|Master Arsitektur]] <span class="wiki-navbox-sep">•</span>
      [[Tujuan Hidup Manusia|Tujuan Hidup]] <span class="wiki-navbox-sep">•</span>
      [[Bahasa Hati|Koneksi Sebelum Koreksi]] <span class="wiki-navbox-sep">•</span>
      [[Tangki Cinta]]
    </div>
  </div>
</div>


---

<!-- ========================================================================== -->
<!-- ZONA 4: FOOTNOTES, CATATAN TAKHRIJ & EDITORIAL METADATA                     -->
<!-- ========================================================================== -->

## Lihat Pula
* [[00 - Master Arsitektur PKN]] — Peta makro arsitektur sistem tarbiyah nabawiyah.
* [[Koneksi Sebelum Koreksi]] — Kaidah emas komunikasi hati pendidik.
* [[Tangki Cinta]] — Pemenuhan afeksi jiwa sebelum penegakan taklif syariat.
* [[4 Fase Usia Nabawiyah]] — Pentahapan tarbiyah dari Thufulah hingga Syabab.

---

## Referensi dan Catatan Kaki

[^1]: **Ustadz Abdul Kholiq**, *Buku Utama Pendidikan Karakter Nabawiyah*, SOTAB HEBAT & Himmatul Ummah.
[^2]: Korpus Takhrij Hadits Nabawi & Atsar Salaf, terverifikasi melalui OpenBayan Qdrant ID `shamela_11m`.

---

**Kategori Direktori:** [[Kategori:Manhaj Pendidikan Karakter Nabawiyah]] • [[Kategori:Template]]

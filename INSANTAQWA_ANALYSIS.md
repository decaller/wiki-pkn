# Laporan Analisis Repositori: pub.insantaqwa.org

Dokumen ini merangkum hasil audit teknis dan pemetaan materi dari repositori [`old_backup/pub.insantaqwa.org/`](file:///home/abuhafi/Project/wiki-pkn/old_backup/pub.insantaqwa.org/) yang menyajikan khazanah visualisasi interaktif mandiri untuk pendidikan karakter nabawiyah.

---

## 1. Ikhtisar Arsitektur & Teknologi

Repositori `pub.insantaqwa.org` dibangun sebagai portal publikasi grafis interaktif berbasis peramban (*web-based interactive infographics*) dengan karakteristik:
* **Framework Grafis & Visualisasi:** Memanfaatkan kombinasi **D3.js**, **Chart.js**, dan manipulasi **SVG / Canvas** murni untuk interaktivitas data.
* **Styling & Tata Letak:** Menggunakan **Tailwind CSS** modern untuk tampilan responsif, gelap/terang, dan tata letak modular.
* **Aplikasi Web Mandiri (`bakat/`):** Bundel SPA (Vite + React/Vue) yang memuat peta interaktif 40 pilar bakat berbasis `calculation.json` dan `tb40.svg`.

---

## 2. Inventaris Modul Visualisasi Interaktif

| Nama Berkas | Judul Visualisasi | Teknologi Utama | Deskripsi Fungsional |
| :--- | :--- | :--- | :--- |
| **`3jiwa.html`** | Analisis Karakter: Ruh, Jiwa, Kecerdasan | D3.js, Chart.js, Tailwind | Visualisasi hierarki tiga tingkatan jiwa (*Ammarah, Lawwamah, Muthmainnah*) serta hubungannya dengan kecerdasan ruhaniyah dan jasadiah. |
| **`3d_perkembangan.html`** | 3D Fitrah Development Chart | D3.js, 3D Canvas Projection | Visualisasi kurva perkembangan fitrah multidimensi melintasi 4 etape usia (*Thufulah, Tamyiz, Murahaqah, Syabab*). |
| **`benang_merah.html`** | Alur Metode Mendidik (Story Mode) | Tailwind, Animasi SVG Interaktif | Panduan alur langkah-demi-langkah penerapan kurikulum fitrah nabawiyah dalam format visual *storytelling*. |
| **`imunitas.html`** | Imunitas to Roadmap Animation | SVG Vector, Tailwind | Simulasi grafis daya tahan jiwa (*imunitas sosial*) anak saat berhadapan dengan polusi lingkungan eksternal. |
| **`bakat/`** | Peta Bakat & Sifat Manusia (TB-40) | Vite, React/D3, SVG Explorer | Aplikasi eksplorasi interaktif 40 pilar bakat, rukun 3A, dan kluster sifat manusia. |
| **`tujuan_hidup.html`** | Arsitektur Tujuan Hidup | SVG, CSS Animations | Diagram visual hubungan antara ibadah vertikal (*'Ibadah*) dan peran kekhalifahan (*Khilafah*). |
| **`tanggung_jawab.html`** | Pembagian Peran Pengasuhan | Tailwind, Flex Matrix | Bagan pembagian tanggung jawab antara Ayah, Ibu, dan Lembaga Pendidikan. |
| **`kaidah_implementasi.html`**| 4 Kaidah Emas Implementasi | CSS Grid, Interactive Cards | Matriks interaktif 4 kaidah implementasi PKN. |
| **`pembelajaran_alamiah.html`**| Siklus Belajar Alami | Flowchart SVG | Alur siklus belajar berbasis fitrah nalar dan indera anak. |
| **`euforia.html`** | Anatomi Jebakan Euforia Prestasi | Infografis Kritis | Visualisasi dekonstruksi racun piala dan pujian semu pada anak. |

---

## 3. Pemetaan Integrasi dengan Artikel Wiki PKN

Seluruh modul visualisasi di atas memiliki tautan konseptual 1-ke-1 dengan artikel materi di Wiki PKN:

1. **`3jiwa.html`** $\longleftrightarrow$ [`content/.../Insan/Pembagian Jiwa/`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Pembagian%20Jiwa/index.md)
2. **`3d_perkembangan.html`** $\longleftrightarrow$ [`content/.../Perkembangan/`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Perkembangan/index.md)
3. **`benang_merah.html`** $\longleftrightarrow$ [`content/.../Pendidikan Ideal/Benang Merah Pendidikan.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Pendidikan%20Ideal/Benang%20Merah%20Pendidikan.md)
4. **`imunitas.html`** $\longleftrightarrow$ [`content/.../Pendidikan Ideal/Imunitas Sosial.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Pendidikan%20Ideal/Imunitas%20Sosial.md)
5. **`bakat/`** $\longleftrightarrow$ [`content/.../Bakat/`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Bakat/index.md)
6. **`tujuan_hidup.html`** $\longleftrightarrow$ [`content/.../Insan/Tujuan Hidup Manusia.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Tujuan%20Hidup%20Manusia.md)
7. **`tanggung_jawab.html`** $\longleftrightarrow$ [`content/.../Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Peran%20&%20Tanggung%20Jawab/Tanggung%20Jawab%20Pendidikan.md)
8. **`kaidah_implementasi.html`** $\longleftrightarrow$ [`content/.../Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Kaidah%20&%20Elemen/4%20Kaidah%20Implementasi.md)
9. **`pembelajaran_alamiah.html`** $\longleftrightarrow$ [`content/.../Pendidikan Ideal/Pembelajaran Alamiah.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Pendidikan%20Ideal/Pembelajaran%20Alamiah.md)
10. **`euforia.html`** $\longleftrightarrow$ [`content/.../Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Pendidikan%20Ideal/Luka%20dan%20Hutang%20Pengasuhan/Euforia.md)

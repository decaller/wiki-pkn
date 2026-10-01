# 01 — Audit Struktur dan Susunan Konten Saat Ini
## *(Current State Content Inventory & Friction Analysis)*

**Status:** Dokumen evaluasi analitis. Berpijak pada inventarisasi berkas fisik direktori `content/` (486 berkas Markdown), struktur navigasi `nav_structure.json` (150 simpul, 122 daun), dan catatan masukan pemilik proyek.

---

## 1. Konteks dan Masalah Awal

Pemilik proyek menyampaikan evaluasi awal bahwa:
> *"Susunan konten saat ini terasa kurang rapi, membingungkan pembaca baru, dan menyulitkan pengguna dalam menemukan materi praktis yang mereka butuhkan."*

Audit ini bertujuan membedah **akar penyebab struktural** dari kebingungan tersebut dengan memeriksa organisasi direktori, kedalaman hierarki, dan keterpisahan format materi.

---

## 2. Inventarisasi Makro Direktori Saat Ini

Saat ini repositori `content/` menampung 486 berkas Markdown yang terbagi ke dalam 7 direktori tingkat atas (*top-level directories*):

| Direktori Utama | Jumlah Berkas | Karakteristik Isi | Pola Pengelompokan |
|---|:---:|---|---|
| `Arsitektur PKN/` | 7 | Ringkasan 6 sektor makro arsitektur PKN | Berbasis diagram Canvas (Sektor 00–06) |
| `Paradigma - Implementasi PKN/` | 84 | Dokumen inti manhaj (Insan, Jiwa, Fitrah, 40 Pilar TB-40, Kaidah, Fase Usia, Peran) | Berbasis hierarki konseptual buku |
| `Toolkit KBM/` | 6 | Templat RPP, Lembar Observasi Karakter, Prompt AI, Bank Cerita Sirah, Infografis WAG | Berbasis instrumen praktis sekolah |
| `Dalil/` | 83 | Halaman mandiri dalil ayat Al-Qur'an dan Hadits shahih | Berbasis entitas dalil mandiri |
| `Materi SOTAB/` | 121 | Buletin parenting Sekolah Orang Tua Ayah Bunda | Berbasis arsip kronologis web SOTAB |
| `Kajian Video/` | 122 | Transkrip dan bab ceramah video Ustadz Abdul Kholiq | Berbasis format media (video YouTube) |
| `Referensi/` | 11 | Review 8 buku kanonikal, glosarium istilah, korpus turats, catatan rilis | Berbasis rujukan kepustakaan |

---

## 3. Identifikasi 6 Titik Friksi Struktural (*Core Frictions*)

Dari pemetaan di atas, teridentifikasi 6 masalah struktural mendasar yang menciptakan beban kognitif (*cognitive load*) bagi pembaca:

### Friksi 1: Kedalaman Folder yang Terlalu Ekstrem (*Deep Nested Hierarchy*)
* **Temuan:** Di dalam direktori `Paradigma - Implementasi PKN/`, naskah tertimbun hingga 5–6 lapisan subfolder:
  ```text
  content/
  └── Paradigma - Implementasi PKN/
      └── Dokumen Pendidikan Karakter Nabawiyah/
          └── Paradigma & Implementasi/
              └── Insan/
                  └── Fitrah (Karakter)/
                      └── Bakat/
                          └── TB40/
                              └── 01-himmah.md
  ```
* **Dampak Pengguna:** Jalur remah roti (*breadcrumbs*) menjadi sangat panjang dan terpotong di layar ponsel. Pengguna merasa "tersesat di dalam labirin folder" dan kesulitan melompat kembali ke tema induk.

---

### Friksi 2: Pengelompokan Berbasis Format Asal Dokumen (*Format-Centric Siloing*)
* **Temuan:** Materi dipisahkan berdasarkan wadah atau format medianya, bukan berdasarkan topik masalah yang dicari pengguna:
  - Pembahasan tentang *fase usia anak* tersebar di `Paradigma/.../Perkembangan/`, ada di artikel `Materi SOTAB/`, dan ada di transkrip `Kajian Video/`.
  - Pembahasan tentang *menangani anak tantrum/luka pengasuhan* terpecah antara `Luka dan Hutang Pengasuhan/Recovery.md`, buletin SOTAB, dan video ceramah.
* **Dampak Pengguna:** Pengguna yang mencari topik *"Pendidikan Anak Usia 7 Tahun"* harus membuka tiga folder terpisah dan menebak apakah materi terbaik ada di teks buku, rekaman video, atau buletin parenting.

---

### Friksi 3: Ketiadaan Gerbang Orientasi Pemula (*No Explicit Onboarding Gateway*)
* **Temuan:** Ketika membuka beranda (`content/index.md`), pembaca langsung disajikan matriks 12 sektor konsep yang padat istilah filosofis (*Syakilah, Muthmainnah, Lawwamah, Taisir, Qudwah, Tadarruj*).
* **Dampak Pengguna:** Persona **Orang Tua Pemula** dan **Guru Baru** mengalami *paralysis by analysis* (kebingungan menentukan dari mana harus mulai membaca). Belum ada tombol atau jalur naratif tegas bertuliskan *"Baru Pertama Kali di Sini? Ikuti 4 Langkah Awal Ini"*.

---

### Friksi 4: Fragmentasi Panduan Praktis KBM dan Parenting
* **Temuan:**
  - Guru mencari instrumen kelas: sebagian ada di `Toolkit KBM/`, sebagian ada di `Paradigma/.../Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md`, dan sebagian ada di `content/Templates/`.
  - Orang tua mencari tips respon harian: harus menyusuri artikel SOTAB yang berjumlah 121 judul tanpa indeks masalah tematik (misal: mogok shalat, kecanduan layar, perkelahian saudara).
* **Dampak Pengguna:** Guru dan orang tua yang membutuhkan pertolongan cepat (*just-in-time answers*) menyerah sebelum menemukan lembar kerja yang dicari.

---

### Friksi 5: Ambiguitas Navigasi Bilah Sisi (`OutlineNav`)
* **Temuan:** Pohon navigasi `nav_structure.json` memiliki 150 simpul teknis yang mencerminkan susunan berkas internal pengembang, bukan pola pencarian mental model pengguna (*mental model mismatch*).
* **Dampak Pengguna:** Di layar perangkat bergerak (mobile), daftar 150 simpul mengharuskan scrolling sangat panjang, membuat pengguna kehilangan orientasi konteks saat ini.

---

### Friksi 6: Pemisahan Tajam Antara Teori dan Dalil Mandiri
* **Temuan:** Sebanyak 83 halaman dalil berada di direktori mandiri `content/Dalil/`. Walaupun tautan silang (*wikilinks*) sudah terpasang, pengguna awam sering kali menganggap folder `Dalil/` sebagai glosarium terpisah yang terisolasi dari penjelasan praktis di kelas atau rumah.
* **Dampak Pengguna:** Penelaah sumber merasa nyaman, tetapi orang tua dan guru merasa dalil tersebut berdiri sendiri tanpa jembatan pedagogis langsung ke keseharian anak.

---

## 4. Implikasi Desain untuk Penataan Ulang

1. **Prinsip Non-Destruktif:** Restrukturisasi informasi tidak boleh mematahkan tautan internal `[[WikiLinks]]` eksisting atau merusak slug URL yang telah terindeks oleh mesin pencari.
2. **Pintu Masuk Berorientasi Tugas (*Task-Oriented Top-Level Facets*):** Susunan navigasi utama harus diubah dari *nama folder dokumen* menjadi *tujuan pencarian pengguna*.
3. **Penyatuan Multi-Modal Tematik (*Topic Hubs*):** Menyatukan tautan naskah, video ceramah, kartu WAG, dan instrumen KBM ke dalam satu halaman induk (*Hub / MOC*) per tema pokok.

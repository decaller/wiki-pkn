# 04 — Matriks Tugas Pengguna dan Skenario Navigasi End-to-End
## *(User Task Matrix & Navigation Journey Walkthrough)*

**Status:** Dokumen spesifikasi pengalaman pengguna (*UX specification*). Menguji efektivitas rancangan arsitektur informasi baru terhadap 5 persona pengguna ([`persona/`](persona/README.md)) melalui skenario tugas konkret dan perbandingan jalur klik (*click-path analysis*).

---

## 1. Matriks Pemetaan Persona vs. Pilar Navigasi Baru

Tabel berikut memetakan keterkaitan antara seluruh kelompok persona pengguna dengan 6 pilar pintu masuk baru:

| Kelompok Persona Pengguna | P1: Mulai di Sini | P2: Fase Usia | P3: Bakat TB-40 | P4: Praktik Keluarga | P5: Guru & KBM | P6: Khazanah Dalil |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **01a — Ayah / Bapak (Kepala Keluarga)** | 🟢 **Primer** | 🟢 **Primer** | 🟡 Sekunder | 🟢 **Primer** | ⚪ Aksidental | 🟡 Sekunder |
| **01b — Ibu / Bunda (Madrasah Utama)** | 🟢 **Primer** | 🟢 **Primer** | 🟡 Sekunder | 🟢 **Primer** | ⚪ Aksidental | ⚪ Aksidental |
| **02a — Guru Fase Thufulah (2–7 Tahun)** | 🟡 Sekunder | 🟢 **Primer** | 🟡 Sekunder | ⚪ Aksidental | 🟢 **Primer** | ⚪ Aksidental |
| **02b — Guru Fase Tamyiz (7–10 Tahun)** | 🟡 Sekunder | 🟢 **Primer** | 🟢 **Primer** | ⚪ Aksidental | 🟢 **Primer** | 🟡 Sekunder |
| **02c — Guru Fase Murahaqah (10–14 Tahun)** | 🟡 Sekunder | 🟢 **Primer** | 🟢 **Primer** | ⚪ Aksidental | 🟢 **Primer** | 🟢 **Primer** |
| **02d — Guru Baligh & Syabab (14–18+ Tahun)** | 🟡 Sekunder | 🟢 **Primer** | 🟢 **Primer** | ⚪ Aksidental | 🟢 **Primer** | 🟡 Sekunder |
| **02e — Instruktur / Pembimbing Dewasa** | 🟢 **Primer** | 🟡 Sekunder | 🟢 **Primer** | 🟢 **Primer** | 🟡 Sekunder | 🟢 **Primer** |
| **03a — Pengelola Lembaga Formal** | 🟡 Sekunder | 🟡 Sekunder | 🟡 Sekunder | 🟡 Sekunder | 🟢 **Primer** | 🟢 **Primer** |
| **03b — Pengelola Lembaga Non-Formal** | 🟡 Sekunder | 🟢 **Primer** | 🟡 Sekunder | 🟢 **Primer** | 🟢 **Primer** | 🟢 **Primer** |
| **04 — Fasilitator Kajian & Da'i** | 🟢 **Primer** | 🟢 **Primer** | 🟡 Sekunder | 🟢 **Primer** | 🟡 Sekunder | 🟢 **Primer** |
| **05 — Penelaah Sumber & Peneliti Dalil** | ⚪ Aksidental | ⚪ Aksidental | 🟡 Sekunder | ⚪ Aksidental | ⚪ Aksidental | 🟢 **Primer** |
| **06 — Siswa & Santri (Pelajar Muda)** | 🟡 Sekunder | 🟡 Sekunder | 🟢 **Primer** | ⚪ Aksidental | ⚪ Aksidental | ⚪ Aksidental |
| **07 — Masyarakat Umum (Tazkiyatun Nafs)** | 🟢 **Primer** | ⚪ Aksidental | 🟢 **Primer** | 🟢 **Primer** | ⚪ Aksidental | 🟢 **Primer** |

*Keterangan: 🟢 Primer = Pintu masuk utama harian; 🟡 Sekunder = Rujukan pendukung tugas; ⚪ Aksidental = Jarang diakses langsung.*

---

## 2. Perbandingan Jalur Navigasi: Kondisi Saat Ini vs. Usulan Baru

Berikut adalah 15 skenario tugas riil yang mencakup seluruh spektrum persona, membandingkan jalur saat ini (*Current Path*) dengan jalur yang diusulkan (*Proposed Path*):

---

### Kelompok Persona 01: Orang Tua Pemula

#### Skenario 1.1: Mencari panduan menangani anak usia 4 tahun yang sering melempar barang dan tantrum
* **Niat Pengguna:** Mengetahui respon emosi yang syar'i dan mendidik tanpa membentak atau memukul.
* **Jalur Saat Ini (Friksi Tinggi):**
  1. Buka Beranda $\rightarrow$ Bingung melihat diagram arsitektur Sektor 00–06.
  2. Buka folder `Materi SOTAB/` $\rightarrow$ Melihat daftar 121 judul artikel buletin tanpa pengelompokan usia.
  3. Mencari kata "Tantrum" di bilah pencarian $\rightarrow$ Muncul transkrip video atau naskah teori panjang.
  4. *Estimasi Klik: 5–7 klik, potensi tersesat tinggi.*
* **Jalur Usulan Baru (Mulus & Cepat):**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Fase Tumbuh Kembang]**.
  2. Pilih sub-kluster **[Fase Thufulah (2–7 Tahun)]**.
  3. Di Hub Thufulah, klik kotak *How-To*: **"Menangani Ledakan Emosi dan Tantrum Balita"**.
  4. *Estimasi Klik: 2 klik, langsung tepat sasaran.*
* **Target Berkas Korpus:** `content/Materi SOTAB/...` / `content/Paradigma - Implementasi PKN/.../Thufulah.md`.

#### Skenario 1.2: Memahami mengapa anak di bawah usia 10 tahun tidak boleh dipukul
* **Niat Pengguna:** Mempelajari batasan syar'i tentang hukuman fisik dan konsep 'uqubah nabawiyah.
* **Jalur Saat Ini:**
  1. Masuk ke `Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/.../Batas Toleransi.md` (tersembunyi di subfolder level 4).
  2. *Estimasi Klik: 5 klik menyusuri pohon folder yang dalam.*
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Praktik Keluarga]**.
  2. Pilih menu **[Disiplin Nabawiyah & Batas Toleransi]**.
  3. Membaca rangkuman eksekutif: perlakuan anak usia < 7 tahun, 7–10 tahun, dan > 10 tahun.
  4. *Estimasi Klik: 2 klik.*
* **Target Berkas Korpus:** `content/Paradigma - Implementasi PKN/.../Batas Toleransi.md` & `content/Dalil/Dalil-Hadits-Perintah-Shalat-Anak-Tamyiz.md`.

#### Skenario 1.3: Membagikan lembar panduan ringkas ke grup WhatsApp keluarga besar
* **Niat Pengguna:** Mengirim tips parenting padat 1 halaman yang mudah dibaca di smartphone anggota keluarga.
* **Jalur Saat Ini:**
  1. Berkas infografis baru saja dibuat dan berada di `content/Toolkit KBM/Infografis Ringkasan Materi PKN Siap Sebar.md` (orang tua tidak terpikir mencari di folder KBM guru).
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Praktik Keluarga]** $\rightarrow$ **[Kartu Ringkasan WAG Siap Sebar]**.
  2. Salin teks kartu atau unduh ringkasan 10 konsep pokok PKN.
  3. *Estimasi Klik: 2 klik.*
* **Target Berkas Korpus:** `content/Toolkit KBM/Infografis Ringkasan Materi PKN Siap Sebar.md`.

---

### Kelompok Persona 02: Guru Pelaksana

#### Skenario 2.1: Menyiapkan apersepsi KBM Sains berbasis Sirah Nabawiyah
* **Niat Pengguna:** Guru IPA kelas 4 SD ingin membuka pelajaran tentang peredaran tata surya dengan kisah keteladanan shahabat.
* **Jalur Saat Ini:**
  1. Menyusuri folder `Toolkit KBM/` $\rightarrow$ Menemukan `Bank Cerita Sirah dan Apersepsi KBM.md`.
  2. Melakukan scrolling pada berkas berukuran 56 KB untuk mencari tema alam semesta.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Lembaga & Guru]** $\rightarrow$ **[Bank Cerita Sirah & Apersepsi]**.
  2. Menggunakan filter tematik: *"Sains & Fenomena Alam"* $\rightarrow$ Menemukan kisah Nabi Ibrahim mencari Rabbnya dan ekspedisi gurun shahabat.
  3. *Estimasi Klik: 2 klik.*
* **Target Berkas Korpus:** `content/Toolkit KBM/Bank Cerita Sirah dan Apersepsi KBM.md`.

#### Skenario 2.2: Mengidentifikasi bakat santri yang dominan suka memimpin dan menggerakkan
* **Niat Pengguna:** Guru wali kelas ingin mencocokkan perilaku murid dengan profil Bakat Nabawiyah TB-40.
* **Jalur Saat Ini:**
  1. Harus masuk ke subfolder tingkat 6: `content/Paradigma - Implementasi PKN/.../Bakat/TB40/01-himmah.md`.
  2. Tidak ada halaman matriks penyaring berbasis kluster; harus membuka satu per satu berkas markdown.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Fitrah & Bakat TB-40]**.
  2. Pilih tab filter **[Kluster Karakter Menggerakkan (*Driving Traits*)]**.
  3. Tampil 10 kartu bakat: *Al-Himmah*, *Al-Qiyadah*, *Ash-Shulhu*, dll., lengkap dengan indikator perilaku mudah diamati.
  4. *Estimasi Klik: 2 klik.*
* **Target Berkas Korpus:** `content/Paradigma - Implementasi PKN/.../TB40/` & `content/Paradigma - Implementasi PKN/.../Kuisioner Asesmen 40 Bakat Nabawiyah.md`.

#### Skenario 2.3: Mengunduh templat RPP / Modul Ajar Karakter
* **Niat Pengguna:** Guru membutuhkan kerangka formal RPP adab untuk diserahkan ke kepala sekolah.
* **Jalur Saat Ini:**
  1. Buka `content/Toolkit KBM/Templat RPP Berbasis Adab dan Karakter.md`.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Lembaga & Guru]** $\rightarrow$ Menu Cepat **[Toolkit KBM]** $\rightarrow$ Klik templat modul ajar.
* **Target Berkas Korpus:** `content/Toolkit KBM/Templat RPP Berbasis Adab dan Karakter.md`.

---

### Kelompok Persona 03: Pengelola Lembaga / Kepala Sekolah

#### Skenario 3.1: Merancang program Sekolah Orang Tua Ayah Bunda (SOTAB) di sekolah
* **Niat Pengguna:** Menyelaraskan pola asuh wali murid di rumah dengan program asrama/sekolah.
* **Jalur Saat Ini:**
  1. Menemukan folder `Materi SOTAB/` berisi 121 buletin, tetapi bingung bagaimana menyusunnya menjadi kurikulum pertemuan bulanan wali murid.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Lembaga & Guru]** $\rightarrow$ **[Manajemen SOTAB Lembaga]**.
  2. Tampil usulan silabus 6 modul tahunan untuk orang tua (dari Pondasi Tauhid, Fase Usia, hingga Detoks Layar).
* **Target Berkas Korpus:** `content/Materi SOTAB.md` & `content/Paradigma - Implementasi PKN/.../Peran Ayah dan Bunda.md`.

#### Skenario 3.2: Menyusun SOP penegakan disiplin santri tanpa kekerasan
* **Niat Pengguna:** Membuat aturan ketertiban asrama yang mengadopsi prinsip hukuman mendidik (*'Uqubah*).
* **Jalur Saat Ini:**
  1. Tersebar di catatan riset dalil dan artikel tafrith vs ifrath.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Lembaga & Guru]** $\rightarrow$ **[SOP Budaya Adab & Disiplin Positif]**.
  2. Mempelajari tabel komparasi hakikat hukuman syar'i vs hukuman dendam/emosional.
* **Target Berkas Korpus:** `content/Paradigma - Implementasi PKN/.../Batas Toleransi.md` & `content/Paradigma - Implementasi PKN/.../4 Kaidah Implementasi.md`.

---

### Kelompok Persona 04: Fasilitator Kajian / Da'i

#### Skenario 4.1: Menyiapkan materi daurah "Pendidikan Aqil Baligh di Era Digital"
* **Niat Pengguna:** Menyusun materi presentasi lengkap dengan dalil Al-Qur'an, Hadits, dan transkrip pendalaman.
* **Jalur Saat Ini:**
  1. Mencari di folder `Kajian Video/` (122 file transkrip berurutan nomor video YouTube).
  2. Mencari dalil baligh di folder `Dalil/`.
  3. Melakukan sintesis mandiri antar dokumen yang terpisah.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Fase Tumbuh Kembang]** $\rightarrow$ **[Hub Fase Murahaqah & Aqil Baligh]**.
  2. Halaman MOC menyediakan paket lengkap: Definisi Baligh, Takhrij Dalil Ayat/Hadits, Transkrip Kajian Video Relevan, dan Poin Presentasi Utama.
* **Target Berkas Korpus:** `content/Paradigma - Implementasi PKN/.../Murahaqah.md`, `content/Dalil/...`, `content/Kajian Video/...`.

#### Skenario 4.2: Menemukan glosarium istilah untuk menjawab pertanyaan jamaah kajian
* **Niat Pengguna:** Mencari definisi resmi istilah *"Syakilah"* atau *"Nafs Muthmainnah"*.
* **Jalur Saat Ini:**
  1. `content/Glosarium Istilah Karakter Nabawiyah.md` berada di root content.
* **Jalur Usulan Baru:**
  1. Tautan langsung tersemat di Header Topbar dan di dalam Pilar **[Mulai di Sini]** $\rightarrow$ **[Glosarium Istilah Karakter]**.

---

### Kelompok Persona 05: Penelaah Sumber / Asatidzah

#### Skenario 5.1: Memeriksa takhrij hadits perintah shalat anak usia 7 dan 10 tahun
* **Niat Pengguna:** Memeriksa sanad hadits, riwayat Abu Dawud no. 495, derajad hadits (shahih/hasan), dan syarah salaf.
* **Jalur Saat Ini:**
  1. Buka folder `content/Dalil/` $\rightarrow$ Mencari nama file di antara 86 judul file dalil.
  2. Buka `content/Master Katalog Dalil Hadits dan Sunnah.md`.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Khazanah Dalil & Rujukan]**.
  2. Gunakan kolom saring cepat (*Quick Lookup Dalil*) berdasarkan tema shalat atau perawi hadits.
  3. Klik langsung menuju halaman dalil terverifikasi dengan link ke database OpenBayan.
* **Target Berkas Korpus:** `content/Dalil/Dalil-Hadits-Perintah-Shalat-Anak-Tamyiz.md` & `content/Master Katalog Dalil Hadits dan Sunnah.md`.

#### Skenario 5.2: Menelaah integrasi pemikiran ulama salaf (Ibnu Qayyim) dengan konsep fitrah PKN
* **Niat Pengguna:** Menilai otentisitas konsep fitrah PKN terhadap kitab *Tuhfatul Maudud bi Ahkamil Maulud*.
* **Jalur Saat Ini:**
  1. Buka `content/Referensi/Review Buku/Tuhfatul Maudud.md`.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Khazanah Dalil & Rujukan]** $\rightarrow$ **[Kajian Kitab & Buku Kanonikal]**.
  2. Akses matriks komparasi bab kitab klasik dengan implementasi kurikulum modern PKN.
---

### Kelompok Persona 06: Siswa & Santri (Pelajar Muda & Pembelajar Bakat)

#### Skenario 6.1: Santri kelas 11 SMA mengisi asesmen 40 Bakat Nabawiyah (TB-40) untuk memilih jurusan
* **Niat Pengguna:** Mengetahui kluster bakat dominan (*Driving*, *Thinking*, *Relating*, atau *Executing*) untuk merancang jalan kontribusi peradaban (*syakilah*).
* **Jalur Saat Ini:**
  1. Menyusuri 6 subfolder ke `content/Paradigma - Implementasi PKN/.../Insan/Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md`.
  2. Tampilan teks mentah tanpa panduan interpretasi ramah pelajar muda.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Fitrah & Bakat TB-40]**.
  2. Klik banner **[Asesmen Mandiri Santri & Pemuda]**.
  3. Mengisi kuesioner ringkas dan membaca kartu deskripsi bakat dominan beserta rekomendasi bidang kiprahnya.
  4. *Estimasi Klik: 2 klik.*
* **Target Berkas Korpus:** `content/Paradigma - Implementasi PKN/.../Kuisioner Asesmen 40 Bakat Nabawiyah.md` & `content/Paradigma - Implementasi PKN/.../TB40/`.

#### Skenario 6.2: Pelajar mencari panduan adab menuntut ilmu dan menjaga keberkahan hafalan
* **Niat Pengguna:** Mengetahui etika menghormati guru, adab memegang kitab, dan menjauhi maksiat pengikis hafalan.
* **Jalur Saat Ini:**
  1. Mencari acak di folder `Referensi/` atau transkrip kajian video.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Mulai di Sini]** $\rightarrow$ **[Adab Penuntut Ilmu (Thalabul Ilmi)]**.
  2. *Estimasi Klik: 2 klik.*
* **Target Berkas Korpus:** `content/Paradigma - Implementasi PKN/.../Belajar.md` & `content/Toolkit KBM/Bank Cerita Sirah dan Apersepsi KBM.md`.

---

### Kelompok Persona 07: Masyarakat Umum & Pembelajar Mandiri (Self-Improvement)

#### Skenario 7.1: Menemukan panduan pemulihan luka batin masa lalu (Recovery Luka Pengasuhan)
* **Niat Pengguna:** Memulihkan trauma masa kecil akibat pola asuh orang tua terdahulu yang keras tanpa terjebak psikoanalisis sekuler.
* **Jalur Saat Ini:**
  1. Buka folder `Paradigma - Implementasi PKN/.../Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md` (terkubur 4 level folder).
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Praktik Keluarga]** $\rightarrow$ **[Pemulihan Diri & Recovery Luka Pengasuhan]**.
  2. Membaca 4 tahap rekonsiliasi jiwa: Pengakuan Fakta, Taubat Nasuha, Menghalalkan Hak (*Tahallul*), dan Pengisian Ulang Tangki Cinta.
  3. *Estimasi Klik: 2 klik.*
* **Target Berkas Korpus:** `content/Paradigma - Implementasi PKN/.../Recovery.md`.

#### Skenario 7.2: Mendalami konsep Tiga Lapisan Jiwa untuk manajemen emosi dan pembersihan hati (Tazkiyatun Nafs)
* **Niat Pengguna:** Memahami mengapa diri sering diliputi amarah tak terkendali dan bagaimana melatih jiwa mencapai ketenangan (*Muthmainnah*).
* **Jalur Saat Ini:**
  1. Buka `content/Paradigma - Implementasi PKN/.../Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md`.
* **Jalur Usulan Baru:**
  1. Buka Beranda $\rightarrow$ Klik Pilar **[Mulai di Sini]** (atau **[Khazanah Dalil]**) $\rightarrow$ **[Peta Jiwa & Tazkiyatun Nafs]**.
  2. Mengakses bagan skema jiwa (Ammarah vs Lawwamah vs Muthmainnah) beserta dalil Al-Qur'an dan riwayat Ibnu Qayyim.
  3. *Estimasi Klik: 2 klik.*
* **Target Berkas Korpus:** `content/Paradigma - Implementasi PKN/.../Bersatunya Ruh dan Jasad Membentuk Jiwa.md` & `content/Paradigma - Implementasi PKN/.../Tazkiyatun Nafs.md`.

---

## 3. Ringkasan Pengurangan Beban Kognitif (*UX Gains*)

| Metrik Evaluasi | Struktur Lama (Folder-Centric) | Usulan Baru (6 Pilar Task-Oriented) | Peningkatan |
|---|:---:|:---:|:---:|
| **Kedalaman Klik Maksimal** | 5 – 6 klik | 2 – 3 klik | 🔻 Berkurang 50% |
| **Beban Membaca Daftar Menu** | 150 simpul di sidebar | 6 pilar utama + sub-kluster tematik | 🔻 Reduksi kebingungan visual |
| **Fragmentasi Media** | Teks, video, dalil terpisah di 3 folder | Menyatu di satu halaman *Topic Hub* | 🟢 Relevansi kontekstual tinggi |
| **Jalur Pengguna Baru (Onboarding)** | Tidak ada (langsung diagram arsitektur) | Jalur terpandu 3 langkah pemula | 🟢 Ramah pengguna awam |

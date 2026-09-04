import json

def build_content_analysis():
    api_result_path = '/home/deck/Projects/observasi-karakter-api/api-tb40-explore/api/v0.1/tb40/result.json'
    with open(api_result_path) as f:
        r1 = json.load(f)

    res = r1['parts']['tb40']['tb40Result']
    nodes = {lvl: {item['pillar']['no']: item for item in res[lvl]} for lvl in ['2', '3', '6', '18', '40']}

    # Build 40 pillars rows
    table_rows = []
    for no in range(1, 41):
        found = None
        for p in nodes['40'].values():
            if int(p['data']['pilar40']) == no:
                found = p
                break
        d = found['data']
        l18 = nodes['18'][found['parents'][0]['no']]['name']
        l6 = nodes['6'][nodes['18'][found['parents'][0]['no']]['parents'][0]['no']]['name']
        row = f"| #{no:02d} | **{found['name']}** | {d['arab']} | {l6} | {l18} | {d['label_diri']} | {d['definisi']} | {d['profesi']} | {d['jurusan']} |"
        table_rows.append(row)

    # Build 40 warning rows
    warning_rows = []
    for no in range(1, 41):
        found = None
        for p in nodes['40'].values():
            if int(p['data']['pilar40']) == no:
                found = p
                break
        d = found['data']
        lalai_name = d.get('lalai_nama_lengkap', '-')
        lalai_def = d.get('lalai_definisi', '-')
        lalai_perbaiki = d.get('lalai_perbaiki', '-')
        lebih_name = d.get('lebih_nama_lengkap', '-')
        lebih_def = d.get('lebih_definisi', '-')
        lebih_perbaiki = d.get('lebih_perbaiki', '-')
        w_row = f"| #{no:02d} **{found['name']}** ({d['arab']}) | **{lalai_name}**: {lalai_def}<br><br>*Solusi Kuratif:* {lalai_perbaiki} | **{lebih_name}**: {lebih_def}<br><br>*Solusi Kuratif:* {lebih_perbaiki} |"
        warning_rows.append(w_row)

    pillars_table_md = "\n".join(table_rows)
    warnings_table_md = "\n".join(warning_rows)

    content = f"""# Analisis Konten & Master Taksonomi TB40 Wiki PKN

Dokumen ini menyajikan hasil analisis mendalam terhadap basis pengetahuan **Pendidikan Karakter Nabawiyah (PKN)**, mencakup rekapitulasi pengayaan materi dari naskah arsip (`old_backup/random/`), integrasi data otoritatif **Tafsir Bakat 40 (TB40)** dari API Observasi Karakter, pemetaan celah konten (*content gaps*), serta peta jalan (*roadmap*) pengembangan selanjutnya.

---

## 1. Ringkasan Eksekutif Pembaruan Konten

Sebelum proses pembaruan dan migrasi dilakukan, dari total 59 berkas Markdown di dalam direktori `content/`, terdapat **43 berkas yang berstatus dokumen kerangka/templat kosong** (hanya memuat teks placeholder seperti `Penjelasan singkat mengenai tema...`, `< matan dalil >`, `< Grafik Utama Tema >`, dan `teks narasi`).

Melalui pemindaian, ekstraksi, dan sintesis terhadap 15 naskah komprehensif di direktori `old_backup/random/`:
1. **39 dokumen inti** telah diperkaya dengan materi otentik berbahasa Indonesia yang terstruktur rapi.
2. **100% resolusi navigasi tercapai**: Seluruh 47 simpul daun pada `nav_structure.json` kini memiliki berkas Markdown fisik yang valid dengan frontmatter `title` yang selaras (0 *unlinked leaf labels*).
3. **Data Otoritatif TB40 Berhasil Diekstraksi**: Data taksonomi lengkap 40 pilar karakter dari `/home/deck/Projects/observasi-karakter-api/api-tb40-explore/api/` telah dipetakan secara utuh, menutup kesenjangan konseptual antara teori fitrah bakat dan operasionalisasi 40 pilar karakter.

---

## 2. Pemetaan Materi yang Telah Diperbarui

Tabel berikut merangkum integrasi antara naskah sumber arsip dan halaman dokumentasi aktif di dalam direktori `content/`:

| Kluster Pembahasan | Halaman yang Diperbarui | Sumber Materi (`old_backup/random/`) | Inti Materi yang Diintegrasikan |
|---|---|---|---|
| **Trilogi Jiwa (Insan)** | `Pembagian Jiwa.md`, `Ammarah.md`, `Lawwamah.md`, `Muthmainnah.md`, `Bersatunya Ruh dan Jasad...` | `Trilogi Jiwa dalam Pendidikan Karakter Nabawiyah.md`, `Struktur Komprehensif... Arsitektural` | Struktur tripartit jasad-ruh-nafs, kecondongan 3 nafs, hak & kewajiban tiap jiwa, kondisi ekstrim (*ifroth* & *tafrith*). |
| **Fitrah & Karakter** | `Fitrah (Karakter).md`, `Iman.md`, `Tangki Cinta.md`, `Belajar.md`, `Bakat.md`, serta 6 sub-bakat | `Menuju Paradigma Pendidikan Berbasis Fitrah...`, `Panduan Strategis Menumbuhkan Kesadaran Beramal...` | Dekonstruksi teori *Tabula Rasa*, 4 dimensi karakter, rukun 3A bakat (Suka, Bisa, Berguna), 5 bahasa cinta & prinsip *koneksi sebelum koreksi*. |
| **Fase Perkembangan** | `Perkembangan.md`, `Thufulah.md`, `Tamyiz.md`, `Murahaqah.md`, `Syabab.md` | `Hak dan Kewajiban Anak dalam Pendidikan Karakter Nabawiyah.md` | Hadits pengangkatan pena (*Rufi'al Qalam*), hak bermain bebas usia 0-7, pembiasaan shalat 7-10, kedisiplinan 10-baligh, dan kemandirian mukallaf pasca-baligh. |
| **Pendidikan Ideal** | `Pendidikan Ideal.md`, `Benang Merah Pendidikan.md`, `Metode Mendidik.md`, `Bahasa Hati/Lisan/Tangan` | `Kritik Pendidikan Modern...`, `Pedoman Strategis Bahasa Tangan...`, `Seni Mengambil Hati...` | Kritik pemesinan anak oleh sekolah modern, penjenjangan 3 bahasa pendidik, syarat operasional pukulan edukatif (*ghairu mubarrih*). |
| **Luka & Pemulihan** | `Luka dan Hutang Pengasuhan.md`, `Euforia.md`, `Recovery.md`, `Batas Toleransi.md` | `Menata Fitrah...`, `Strategi Memenangkan Hati Ananda...` | Asal mula *parenting debt*, dinamika ledakan euforia masa remaja, metode pemulihan EMISOL (Empati, Imajinasi, Solusi). |
| **Implementasi & Peran** | `Implementasi.md`, `4 Kaidah...`, `4 Elemen...`, `Tazkiyatun Nafs.md`, `Tawakkal dan Doa.md`, `Peran Ayah/Bunda/Guru` | `Panduan Strategis Implementasi...`, `Struktur Komprehensif... Transformasi Fitrah` | 4 kaidah penumbuhan fitrah, pembersihan hati pendidik, sinergi peran maskulin ayah & feminin bunda, serta reposisi guru sebagai fasilitator fitrah. |

---

## 3. Spesifikasi Lengkap Master Taksonomi TB40 (Tafsir Bakat 40)

Data taksonomi ini diekstraksi secara langsung dari spesifikasi OpenAPI dan engine kalkulasi repositori API Observasi Karakter di `/home/deck/Projects/observasi-karakter-api/api-tb40-explore/api/` (`v0.1/tb40/calculation.json`, `v0.1/tb40/result.json`, dan `v0.3/tb40/result.json`).

### 3.1 Landasan Filosofis & Penyelarasan Nabawiyah
TB40 (Tafsir Bakat 40) adalah metode pemetaan potensi fitrah dan bakat manusia yang diselaraskan dengan **40 sifat karakter mulia (*fadhilah*)** yang bersumber dari keteladanan Rasulullah ﷺ dan para Sahabat. 

Berbeda dengan asesmen kepribadian konvensional Barat (seperti MBTI atau DISC) yang bersifat deskriptif-netral atau sekuler, TB40 mengintegrasikan:
1. **Konsep Trilogi Jiwa Qur'ani**: Membedah fitrah manusia melalui *Al-Hawa* (Ammarah), *Al-'Aql* (Lawwamah), dan *Al-Qalb* (Muthmainnah).
2. **Karakter Bersifat Normatif-Ideal**: Menjadikan akhlak mulia sebagai standar potensi puncak (*ihsan*).
3. **Pendeteksian Dua Sisi Jurang Ekstrim**: Setiap pilar bakat memiliki batas keseimbangan. Jika diabaikan (*tafrith*) menjadi sifat tercela tertentu, dan jika dilampiaskan berlebihan (*ifrath*) juga menjadi sifat tercela lain. Solusi penyembuhannya (*'ilaj*) diambil secara sistemik dari pilar karakter nabawiyah lainnya.

---

### 3.2 Hierarki 5 Tingkat Arsitektur TB40

TB40 dibangun di atas struktur hierarki matematis dan psikologis 5 tingkat (Level 2 → Level 3 → Level 6 → Level 18 → Level 40):

```mermaid
graph TD
    subgraph "Level 2: 2 Kutub Energi Sosial"
        L2_1["1. Introvert (As-Sirr)"]
        L2_2["2. Extrovert (Al-'Alaniyah)"]
    end

    subgraph "Level 3: 3 Dimensi Jiwa & Gaya Belajar"
        L3_1["1. Karsa / Al-Hawa (Kinestetik - Al-Fuad)"]
        L3_2["2. Cipta / Al-'Aql (Visual - Al-Bashar)"]
        L3_3["3. Rasa / Al-Qalb (Auditori - As-Sam'u)"]
    end

    L2_1 & L3_1 --> L6_1["1. Bekerja Keras (الحَمَاسَة)"]
    L2_1 & L3_2 --> L6_2["2. Berpikir (التَّفْكِيْر)"]
    L2_1 & L3_3 --> L6_3["3. Berperasaan (الشُعُوْر)"]
    L2_2 & L3_1 --> L6_4["4. Mempengaruhi (التَّأْثِيْر)"]
    L2_2 & L3_2 --> L6_5["5. Bekerjasama (التَّعَامُل)"]
    L2_2 & L3_3 --> L6_6["6. Melayani (الخِدْمَة)"]

    subgraph "Level 6: 6 Kategori Bakat Utama"
        L6_1
        L6_2
        L6_3
        L6_4
        L6_5
        L6_6
    end

    L6_1 --> L18_G1["Sub 1-3: Berambisi, Berwibawa, Giat Bekerja"]
    L6_2 --> L18_G2["Sub 4-6: Imajinatif, Berpikir Positif, Analitis"]
    L6_3 --> L18_G3["Sub 7-9: Apa Adanya, Pendiam, Suka Merendah"]
    L6_4 --> L18_G4["Sub 10-12: Menguasai, Memotivasi, Menolong"]
    L6_5 --> L18_G5["Sub 13-15: Hubungan Ada, Hubungan Baru, Mengeratkan"]
    L6_6 --> L18_G6["Sub 16-18: Memberi, Menjaga, Mengalah"]

    L18_G1 --> P_1_6["Pilar #01 - #06 (6 Pilar)"]
    L18_G2 --> P_7_11["Pilar #07 - #11 (5 Pilar)"]
    L18_G3 --> P_12_17["Pilar #12 - #17 (6 Pilar)"]
    L18_G4 --> P_18_24["Pilar #18 - #24 (7 Pilar)"]
    L18_G5 --> P_25_32["Pilar #25 - #32 (8 Pilar)"]
    L18_G6 --> P_33_40["Pilar #33 - #40 (8 Pilar)"]
```

---

### 3.3 Tingkat 2 & 3: Dimensi Jiwa, Gaya Belajar, dan Bahasa Hati

Persilangan antara dorongan energi interaksi dan dimensi jiwa manusia menghasilkan orientasi modalitas belajar dan penerimaan kasih sayang yang spesifik:

| Dimensi Jiwa (Level 3) | Aspek Qur'ani | Kutub Jiwa | Gaya Belajar Otentik (*Modalitas*) | Karakteristik Belajar & Lingkungan Ideal | Bahasa Hati Terpilih (*Love Language*) |
|---|---|---|---|---|---|
| **Karsa** | *Al-Hawa* (الهَوَى) | Jiwa *Ammarah* | **Al-Fuad / Kinestetik** (الفُؤَاد - bergerak & menyentuh) | Belajar lewat aktivitas fisik, membongkar sesuatu, peragaan langsung. Nyaman di ruang terbuka, lapangan, bengkel, laboratorium terbuka. | **Bahasa Pelayanan (*Acts of Service*)**: Melayani kemauannya, membantu tugasnya, menjaga rahasia, memaafkan kesalahannya. |
| **Cipta** | *Al-'Aql* (العَقْل) | Jiwa *Lawwamah* | **Al-Bashar / Visual** (البَصَر - melihat & mengamati) | Membaca cepat, menangkap bagan/diagram, menonton demonstrasi. Memerlukan ruangan dengan pencahayaan optimal, tertata rapi, dan kaya visual. | **Bahasa Kebersamaan (*Quality Time*)**: Menemani aktivitasnya, mendengarkan gagasannya, tersenyum tulus, memenuhi janji, menyayangi. |
| **Rasa** | *Al-Qalb* (القَلْب) | Jiwa *Muthmainnah* | **As-Sam'u / Auditori** (السَمْع - mendengar & menirukan) | Menghafal dengan mengeraskan suara, mendengar narasi/murottal, berdiskusi. Memerlukan ruangan hening, tenang, bebas kebisingan liar. | **Bahasa Perlindungan / Hadiah (*Gifts / Protection*)**: Pemberian hadiah bermakna, kata-kata motivasi tulus, melindungi saat kesulitan, membela harga diri. |

---

### 3.4 Tingkat 6 & 18: Matriks 6 Kategori Bakat & 18 Sub-Kelompok

Persilangan Level 2 (Introvert vs Extrovert) $\times$ Level 3 (Karsa, Cipta, Rasa) melahirkan **6 Kategori Bakat Utama**, yang masing-masing diurai menjadi **3 Sub-Kelompok Bakat (Total 18 Sub-Kelompok)**:

| No | Kategori Bakat (L6) | Aksara Arab | Kombinasi Asal | 18 Sub-Kelompok Bakat (L18) | Karakteristik Dominan |
|---|---|---|---|---|---|
| 1 | **Bekerja Keras** | الحَمَاسَة (*Al-Hamasah*) | Introvert + Karsa | 1. Berambisi<br>2. Berwibawa<br>3. Giat bekerja | Berkeinginan tinggi, pantang menyerah, ingin segera menyelesaikan pekerjaan, tidak suka menunda waktu. |
| 2 | **Berpikir** | التَّفْكِيْر (*At-Tafkir*) | Introvert + Cipta | 4. Suka berpikir imajinatif<br>5. Suka berpikir positif<br>6. Suka berpikir analitis | Cerdas, tajam menganalisis masalah, senang menghitung, menghafal, dan menemukan pola solusi. |
| 3 | **Berperasaan** | الشُعُوْر (*Asy-Syu'ur*) | Introvert + Rasa | 7. Suka apa adanya<br>8. Pendiam<br>9. Suka merendah | Suka merenung sendiri, peka perasaan nurani, pemalu, berhati-hati dalam menjaga kesucian diri. |
| 4 | **Mempengaruhi** | التَّأْثِيْر (*At-Ta'tsir*) | Extrovert + Karsa | 10. Suka menguasai<br>11. Suka memotivasi<br>12. Suka menolong | Berani tampil di depan publik, tegas memimpin, mengarahkan orang lain, bersemangat memotivasi dan membela. |
| 5 | **Bekerjasama** | التَّعَامُل (*At-Ta'amul*) | Extrovert + Cipta | 13. Suka menggunakan relasi ada<br>14. Suka membuka relasi baru<br>15. Suka mengeratkan relasi | Suka kerukunan, anti-konflik, senang menjalin persahabatan, adil, hangat, dan pandai mencairkan suasana. |
| 6 | **Melayani** | الخِدْمَة (*Al-Khidmah*) | Extrovert + Rasa | 16. Melayani dengan memberi<br>17. Melayani dengan menjaga<br>18. Melayani dengan mengalah | Mengutamakan orang lain (*itsaar*), penyayang, setia memegang amanah, menjaga rahasia, pemaaf, dan sabar. |

---

### 3.5 Tingkat 40: Katalog Komprehensif 40 Pilar Karakter Nabawiyah

Berikut adalah basis data lengkap 40 pilar karakter nabawiyah hasil ekstraksi dari sistem engine TB40:

| No | Pilar Karakter | Arab | Kategori (L6) | Sub-Kelompok (L18) | Label Diri | Definisi Operasional | Rekomendasi Profesi | Rekomendasi Rumpun Jurusan |
|---|---|---|---|---|---|---|---|---|
{pillars_table_md}

---

### 3.6 Matriks Kondisi Ekstrim (*Tafrith* vs *Ifrath*) & Formula Kuratif

Kaidah mendasar pendidikan fitrah Nabawiyah adalah bahwa **setiap bakat adalah amanah kebajikan (*fadhilah*) yang harus dijaga keseimbangannya**. Kerusakan karakter terjadi dalam dua bentuk:
1. **Lalai (*Tafrith* / Kekurangan):** Meremehkan, mematikan, atau tidak melatih potensi bakat fitrahnya sehingga terjerumus pada kehinaan.
2. **Berlebih (*Ifrath* / Melampaui Batas):** Memperturutkan dorongan bakat tanpa bingkai syariat dan adab, sehingga menjadi bumerang kezaliman bagi diri dan lingkungannya.

Tabel berikut menyajikan pemetaan kondisi ekstrim dan formula penyembuh kuratif (*'ilaj*) untuk ke-40 pilar:

| Pilar Karakter | Kondisi Lalai / Meremehkan (*Tafrith*) & Solusi Kuratif | Kondisi Berlebihan (*Ifrath*) & Solusi Kuratif |
|---|---|---|
{warnings_table_md}

---

### 3.7 Spesifikasi Engine & Instrumen Asesmen API TB40

Repositori `/home/deck/Projects/observasi-karakter-api/api-tb40-explore/api/` mendokumentasikan evolusi teknis platform asesmen karakter:

#### A. Dua Varian Instrumen Asesmen
1. **TB40 Dewasa (`tb40Dewasa`):** 
   - Kuesioner refleksi mandiri (*self-assessment*) 40 butir pertanyaan dengan skala Likert.
   - Contoh butir (#27 ‘Adaalah): *"Ketika menghadapi orang lain, aku tidak berat sebelah dalam bersikap, tidak memihak, bersikap tengah-tengah, adil, dan fair dalam permainan."*
2. **TB40 Anak (`tb40Anak`):** 
   - Kuesioner berbasis observasi orang tua/guru terhadap aktivitas riil keseharian anak usia 10-14 tahun (Fase Murahaqah).
   - Menggunakan bahasa ramah anak dan konteks bermain. Contoh butir (#27 ‘Adaalah): *"Saat bermain dengan teman, aku selalu mengikuti aturan dan tidak mau curang meskipun aku sangat ingin menang."*

#### B. Alur Asesmen Adaptif 4-Tier (API v0.3)
Pada API versi 0.3 (`swagger.yaml`), asesmen dirombak menjadi model adaptif bertingkat (*continuous scoring*):
- **Tier 1 (Energi Sosial - 1 Soal):** Menyaring dominansi energi Introvert vs Extrovert.
- **Tier 2 (Orientasi Jiwa - 1 Soal):** Mengidentifikasi modalitas jiwa Karsa / Cipta / Rasa. Pada akhir Tier 2, engine dapat menghasilkan **Laporan Separuh Jalan (*Halfway Report*)** berupa kluster Level 6.
- **Tier 3 (Pendalaman Sub-Kelompok - 18 Soal):** Menguji kecondongan perilaku pada 18 sub-kelompok bakat.
- **Tier 4 (Presisi 40 Pilar - 40 Soal):** Mengukur derajat intensitas seluruh 40 pilar secara mendalam.

#### C. Algoritma Pendeteksian Peringatan Dini (*Warning Triggers*)
Engine TB40 v0.3 secara otomatis menghitung skor anomali:
- **Ego Warning:** Muncul jika responden memberikan skor maksimal seragam pada seluruh pilar (indikasi *riya'* atau *self-serving bias*).
- **Lalai Warnings:** Mendeteksi kategori bakat yang skornya berada di bawah ambang batas dasar, lalu memberikan peringatan dini perilaku negatif yang mungkin muncul (misal: *Kasal* untuk pekerja keras, *Jubn* untuk mempengaruhi).
- **Lebih Warnings:** Mendeteksi pilar yang mendominasi secara hiperaktif tanpa penyeimbang, lalu memberikan saran rem kuratif (misal: *Thama'* diredam dengan *Qanaa'ah* dan *Tawaadhu'*).

---

## 4. Analisis Kebutuhan Konten Lanjutan (*Content Gaps*)

Dengan tersedianya master taksonomi TB40 yang komprehensif, celah terbesar dalam literatur Wiki PKN kini berpindah dari tataran *teori konseptual* ke tataran *dokumentasi operasional dan instrumen praktis*. 

Berikut adalah 6 celah konten prioritas:

### Gap A. Pembuatan 40 Halaman Profil Pilar Karakter Nabawiyah
* **Urgensi:** SANGAT TINGGI
* **Deskripsi:** Menjadikan data 40 pilar di atas sebagai halaman-halaman profil mandiri di dalam direktori `content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pilar Karakter/`.
* **Struktur Halaman yang Dibutuhkan:**
  1. Frontmatter judul & metadata kategori.
  2. Matan dalil (Ayat Al-Qur'an & Hadits) terkait sifat tersebut.
  3. Definisi operasional & silsilah hierarki (Level 2, 3, 6, 18).
  4. Indikator perilaku positif dalam keseharian anak.
  5. Tanda-tanda bahaya kondisi ekstrim (*Tafrith* vs *Ifrath*) beserta langkah kuratifnya.
  6. Stimulasi pengasuhan berdasarkan 4 fase usia (Thufulah, Tamyiz, Murahaqah, Syabab).
  7. Proyeksi karir & pilihan studi masa depan.

### Gap B. Lembar Observasi & Portofolio Bakat Anak (Rukun 3A)
* **Urgensi:** TINGGI
* **Deskripsi:** Instrumen panduan bagi orang tua untuk mengamati potensi anak tanpa tergesa memberi label (*labeling*).
* **Komponen yang Dibutuhkan:**
  1. Rubrik pemantauan Rukun 3A: **Suka** (*Al-Hawa* / dorongan senang), **Bisa** (*Al-'Aql* / kemudahan belajar), **Berguna** (*Al-Qalb* / kemanfaatan bagi sesama).
  2. Lembar portofolio kegiatan harian/mingguan anak usia 7-14 tahun.
  3. Contoh rancangan Proyek Bakat Mandiri (*Home-Based Project*) untuk 6 kluster bakat utama.

### Gap C. Dokumen "Piagam Akil Baligh" & Protokol Kesiapan Mukallaf
* **Urgensi:** TINGGI
* **Deskripsi:** Naskah perjanjian tertulis antara orang tua dan anak menjelang peralihan status menuju fase Syabab (15 tahun / baligh).
* **Komponen yang Dibutuhkan:**
  1. Templat kontrak legal-syar'i piagam akil baligh (hak kebebasan pengelolaan diri vs kewajiban ibadah mandiri & nafkah pribadi).
  2. Daftar periksa (*checklist*) kesiapan baligh: fiqih thaharah (mandi wajib), batasan aurat, adab pergaulan lawan jenis, serta literasi finansial syariah.

### Gap D. Bank Studi Kasus Kurikulum Berbasis Peristiwa (*Response Tree*)
* **Urgensi:** SEDANG
* **Deskripsi:** Pedoman langkah-demi-langkah bagi orang tua dalam merespons kejadian faktual di rumah sesuai prinsip *koneksi sebelum koreksi*.
* **Komponen yang Dibutuhkan:**
  1. Skenario studi kasus: anak enggan shalat, pertengkaran saudara (*sibling rivalry*), adiksi gawai, dusta spontan (*kadzib*), dan sikap minder.
  2. Pohon respons bertingkat: Langkah 1 (Cek Tangki Cinta) → Langkah 2 (Bahasa Hati) → Langkah 3 (Bahasa Lisan) → Langkah 4 (Bahasa Tangan jika memenuhi syarat).

### Gap E. Integrasi Materi Folder `Insight & Teknis/`
* **Urgensi:** SEDANG
* **Deskripsi:** Menata 3 berkas pendek di folder `content/.../Insight & Teknis/` (`Arahan Teknis Implementasi.md`, `Insight.md`, `SOTABH.md`).
* **Rekomendasi:** Menyempurnakan berkas SOTABH (*State of the Art Belajar Hati*) dan mengaitkannya secara erat ke bab *Bahasa Hati* dan *Metode Mendidik*.

### Gap F. Visualisasi Konseptual & Diagram Interaktif
* **Urgensi:** SEDANG
* **Deskripsi:** Menghadirkan visualisasi grafis untuk tema-tema berbobot tinggi.
* **Komponen yang Dibutuhkan:**
  1. Integrasi peta visual SVG (`tb40.svg`) ke halaman payung `Bakat.md`.
  2. Penambahan diagram alur Mermaid pada halaman `Insan.md` (struktur jasad-ruh-nafs) dan `Recovery.md` (metode pemulihan luka pengasuhan EMISOL).

---

## 5. Rencana Kerja Bertahap (Roadmap)

```mermaid
flowchart TD
    A["Fase 1: Fondasi Konseptual & Ekstraksi Data (SELESAI)"] --> B["Fase 2: Katalogisasi 40 Halaman Profil Pilar TB40"]
    B --> C["Fase 3: Penyusunan Instrumen Operasional (Piagam & Portofolio)"]
    C --> D["Fase 4: Bank Studi Kasus & Integrasi Visual SVG"]

    subgraph "Fase 2 (Prioritas Eksekusi Utama)"
        B1["Penyusunan Skrip Generator Halaman Pilar Karakter"]
        B2["Pembuatan 40 Berkas Profil Pilar di Direktori Insan/Pilar Karakter/"]
        B3["Penyelarasan Indeks Matriks & Tautan Silang Navigasi"]
    end

    subgraph "Fase 3 (Instrumen Lapangan)"
        C1["Templat Piagam Akil Baligh Siap Cetak"]
        C2["Panduan Observasi Bakat Rukun 3A & Portofolio Karya"]
    end
```

### Rekomendasi Langkah Eksekusi Selanjutnya:
1. **Langkah 1:** Menghasilkan 40 berkas Markdown profil pilar karakter di `content/.../Insan/Pilar Karakter/` menggunakan skrip otomasi berdasarkan data master pada dokumen ini.
2. **Langkah 2:** Memperbarui `nav_structure.json` agar memuat folder cabang `40 Pilar Karakter Nabawiyah` yang terkelompok berdasarkan 6 kategori utama.
3. **Langkah 3:** Menulis templat praktis `Piagam Akil Baligh.md` dan `Lembar Observasi Bakat (Rukun 3A).md` untuk melengkapi bab Fase Perkembangan dan Bakat.
"""

    with open('/home/deck/Projects/wiki-pkn/CONTENT_ANALYSIS.md', 'w') as f:
        f.write(content)
    print('CONTENT_ANALYSIS.md successfully updated. Size:', len(content), 'bytes')

if __name__ == '__main__':
    build_content_analysis()

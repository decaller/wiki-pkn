# Wiki Pendidikan Karakter Nabawiyah (PKN)

[![Quartz v5](https://img.shields.io/badge/Platform-Quartz%20v5-blue)](https://quartz.jzhao.xyz/)
[![Total Halaman](https://img.shields.io/badge/Halaman-69%20Berkas-success)](ARTICLE_AUDIT_REPORT.md)
[![Kepatuhan Standar](https://img.shields.io/badge/Standar%20Emas-100%25%20Lulus%20(%E2%89%A55k%20chars)-brightgreen)](ARTICLE_AUDIT_REPORT.md)
[![Total Karakter](https://img.shields.io/badge/Total%20Karakter-891%2C500%20Karakter-orange)](ARTICLE_AUDIT_REPORT.md)
[![Bahasa](https://img.shields.io/badge/Bahasa-Indonesia%20%26%20Arab%20(OpenBayan)-emerald)](DALIL_MAPPING.md)

Basis pengetahuan digital komprehensif **Pendidikan Karakter Nabawiyah (PKN)**—sebuah ensiklopedia rujukan terstruktur yang merekonstruksi paradigma, kurikulum, metodologi, dan tata kelola implementasi pengasuhan generasi Islam berdasarkan sunnah Rasulullah ﷺ, atsar para sahabat, serta pandangan ulama mu'tabar (*Ibnul Qayyim, Al-Ghazali, Ibnu Sahnun, An-Nawawi, Ibnu Khaldun, Asy-Syathibi*).

---

## 1. Peta Konsep Arsitektur Pendidikan Karakter Nabawiyah

Ensiklopedia ini memetakan manusia secara holistik melalui metafora **Pohon Karakter Nabawiyah**:

```mermaid
graph TD
    subgraph AKAR["🌱 PONDASI INSAN (AKAR TAUHID)"]
        Tujuan["[[Tujuan Hidup Manusia]]<br/>Ibadah & Khilafah"]
        RuhJasad["[[Bersatunya Ruh dan Jasad Membentuk Jiwa]]<br/>Tiupan Ruh & Sari Pati Tanah"]
        Trilogi["[[Pembagian Jiwa]]<br/>Muthmainnah • Lawwamah • Ammarah"]
        Fitrah["[[Fitrah (Karakter)]]<br/>Cetak Biru Suci Lahiriah"]
    end

    subgraph BATANG["🌳 PENDIDIKAN IDEAL (BATANG ADAB & METODOLOGI)"]
        Benang["[[Benang Merah Pendidikan]]<br/>Grand Theory 5 Rantai Kausalitas Amal"]
        TigaBahasa["[[Metode Mendidik]]<br/>[[Bahasa Hati]] • [[Bahasa Lisan]] • [[Bahasa Tangan]]"]
        Fase["[[Perkembangan]]<br/>[[Thufulah]] (0-7) • [[Tamyiz]] (7-10) • [[Murahaqah]] (10-15) • [[Syabab]] (15+)"]
        Proteksi["[[Batas Toleransi]] • [[Imunitas Sosial]] • [[Recovery]]"]
    end

    subgraph RANTING["🍃 FITRAH BAKAT (40 PILAR TB40)"]
        BakatUmum["[[Bakat]] (Syakilah Unik)"]
        Sub1["[[Bekerja Keras]] (Al-Hammasah)"]
        Sub2["[[Berpikir]] (Al-Fikrah)"]
        Sub3["[[Berperasaan]] (Al-Wijdaniyyah)"]
        Sub4["[[Memerintah]] (At-Ta'tsir)"]
        Sub5["[[Bekerja Sama]] (At-Ta'amul)"]
        Sub6["[[Melayani]] (Al-Khidmah)"]
    end

    subgraph BUAH["🍎 IMPLEMENTASI & PERADABAN"]
        Kaidah["[[4 Kaidah Implementasi]]<br/>Taisir • Qudwah • Rahmah • Tadarruj"]
        Lembaga["[[Kaidah Implementasi di Berbagai Lembaga]]<br/>5 Kaidah Ushul Fiqih Adopsi Sekolah/Pesantren"]
        Sinergi["[[Peran Ayah dan Bunda]] • [[Peran Guru dan Lembaga Pendidikan]]"]
        Output["Kematangan Akil-Baligh & Khairu Ummah"]
    end

    AKAR --> BATANG
    BATANG --> RANTING
    RANTING --> BUAH
```

---

## 2. Fitur Unggulan Sistem Basis Pengetahuan

1. **100% Berstandar Emas (≥ 5.000 Karakter per Berkas):** Setiap halaman ensiklopedia ditulis secara mendalam, lengkap dengan landasan Al-Qur'an, Hadits shahih, syarah ulama, diagnosis tafrith-ifrath, rubrik evaluasi, dan lembar refleksi orang tua/guru.
2. **Katalog Dalil Terpadu:**
   - **[QURAN_DALIL_CATALOG.md](QURAN_DALIL_CATALOG.md):** Memuat lebih dari 110 ayat Al-Qur'an lengkap teks Arab berharakat, terjemahan Indonesia, dan rujukan Tafsir Ibnu Katsir.
   - **[DALIL_MAPPING.md](DALIL_MAPPING.md):** Memetakan hadits-hadits shahih hasil penelusuran korpus **OpenBayan** (`data/shamela_corpus.db`).
3. **Integrasi Dokumen Resmi Penggagas Manhaj:** Menyerap seluruh naskah otoritatif karya Ustadz Abdul Kholiq dan Bayu Issetyadi:
   - *Panduan Implementasi Standar PKN pada Lembaga Pendidikan Islam (A4)*
   - *Menumbuhkan Kesadaran Beramal (E-book)*
   - *Kaidah Implementasi PKN dalam Berbagai Lembaga*
4. **Navigasi Kustom `OutlineNav`:** Komponen navigasi sidebar khusus yang membaca struktur hierarki `nav_structure.json`, dilengkapi fitur *inside scrolling*, *active link auto-expand*, dan *session scroll state persistence*.
5. **Dukungan Diagram Interaktif Mermaid & Callout Quartz:** Visualisasi psikospiritual dan rubrik aksi yang memikat serta responsif.

---

## 3. Direktori Dokumen Utama di Root

| Dokumen | Deskripsi |
|---|---|
| 📊 **[ARTICLE_AUDIT_REPORT.md](ARTICLE_AUDIT_REPORT.md)** | Laporan audit kuantitatif & kualitatif panjang seluruh 65 artikel (100% kepatuhan standar emas). |
| 📖 **[QURAN_DALIL_CATALOG.md](QURAN_DALIL_CATALOG.md)** | Katalog master dalil Al-Qur'an, teks Arab berharakat, dan takhrij Tafsir Ibnu Katsir. |
| 📜 **[DALIL_MAPPING.md](DALIL_MAPPING.md)** | Katalog master hadits shahih OpenBayan dan relevansinya bagi kurikulum PKN. |
| 🏗️ **[HANDOFF.md](HANDOFF.md)** | Dokumentasi arsitektur teknis sistem, data model TB40, riwayat milestone 1 s/d 19, dan panduan pemeliharaan. |
| 🔍 **[CONTENT_ANALYSIS.md](CONTENT_ANALYSIS.md)** | Analisis konten holistik, pemetaan hierarki TB40, dan metodologi pengayaan materi. |

| 🤝 **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** | Piagam adab dan etika kontributor riset berbasis nilai-nilai Islam nabawiyah. |

---

## 4. Panduan Menjalankan Secara Lokal

### Prasyarat:
- Node.js versi 18.14.0 atau yang lebih baru.
- npm atau npx.

### Langkah Menjalankan:
```bash
# 1. Kloning repositori
git clone https://github.com/decaller/wiki-pkn.git
cd wiki-pkn

# 2. Instal dependensi
npm install

# 3. Bangun situs statis
npx quartz build

# 4. Jalankan development server lokal
npx quartz build --serve --port 8888
```
Buka peramban di `http://localhost:8888/` untuk menelusuri seluruh basis pengetahuan Wiki PKN.

---

## 5. Tim Penyusun & Pengembang

* **Perumus Manhaj PKN:** Ustadz Abdul Kholiq, Bayu Issetyadi, dan Tim SOTAB HEBAT.
* **Penerbit Dokumen Acuan:** Perkumpulan Radio Komunitas Mutiara Qur'an, Sawangan, Depok.
* **Pengembang Basis Pengetahuan & Sistem Quartz:** Tim Relawan Pengembang Digital PKN.

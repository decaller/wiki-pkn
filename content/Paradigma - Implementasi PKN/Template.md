---
title: Standar Template Wiki PKN
---

# Panduan Kontributor & Standar Dokumentasi Wiki PKN

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
5. **Kesesuaian Format Quartz:** Menggunakan frontmatter YAML yang valid, callout Obsidian (`[!quote]`, `[!warning]`, `[!info]`, `[!tip]`), serta tautan silang (*wikilinks* `[[...]]`).

---

## 2. Anatomi Baku 8 Bagian Artikel Ilmiah PKN

Setiap penulisan artikel tema pokok wajib mengikuti kerangka 8 bagian terstruktur:

```markdown
---
title: "Judul Artikel"
---

# Judul Artikel

> [!quote] Dalil & Rujukan Nabawiyah
> **Naskah Ayat / Hadits:**  
> « (Teks Arab Berharakat Lengkap) »
> 
> *"(Terjemahan Resmi Bahasa Indonesia)"*
> 
> 📚 **Sumber Rujukan OpenBayan:** (Nama Kitab, Nomor Hadits / Juz & Halaman)  
> 💡 **Relevansi Pedagogis PKN:** (Penjelasan kedudukan dalil dalam pengasuhan)

## 1. Definisi & Konsep Fondasional
- Makna etimologi (bahasa) dan terminologi syariat.
- Kedudukan konsep dalam arsitektur Pendidikan Karakter Nabawiyah.

## 2. Relevansi Pedagogis & Syarah Ulama Klasik
- Penjelasan syarah hadits/tafsir dari ulama mu'tabar.
- Contoh interaksi nyata Rasulullah ﷺ dengan para sahabat.

## 3. Taksonomi & Komponen Esensial
- Pembagian pilar/elemen pembentuk karakter.
- Matriks karakteristik dan indikator perilaku terukur.

## 4. Diagnosis Penyimpangan: Tafrith vs Ifrath
- **Tafrith (Meremehkan / Lalai):** Gejala, akar masalah, dan dampak buruk.
- **Ifrath (Berlebihan / Memaksa):** Gejala over-demanding dan trauma fitrah.
- **Al-Wasathiyah (Jalan Tengah Nabawiyah):** Titik keseimbangan ideal.

## 5. Panduan Praktis untuk Orang Tua & Pendidik
- Rubrik Observasi (Rukun 3A: Suka, Bisa, Bermanfaat).
- Fasilitasi lingkungan rumah dan sekolah.

## 6. Penerapan Berdasarkan Fase Perkembangan Usia
- Penerapan bertahap pada fase Thufulah (0–7 th), Tamyiz (7–10 th), Murahaqah (10–15 th), dan Syabab (15+ th).

## 7. Studi Kasus Nyata & Solusi Kuratif
- Skenario masalah nyata dalam pengasuhan modern dan tahapan solusinya.

## 8. Tautan Relevan & Peta Konsep
- Tautan silang ke halaman wiki terkait menggunakan format [[Nama Halaman]].
```

---

## 3. Daftar Template Khusus yang Tersedia

Silakan gunakan master template berikut sesuai jenis dokumen yang hendak ditulis:
* **[[Template Tema]]:** Format baku untuk artikel tema pokok, filosofis, dan bab materi utama.
* **[[Template Elemen Karakteristik]]:** Format baku untuk merinci sifat, bakat, dan profil karakter anak.
* **[[Template Elemen Refleksi, Implementas, Risiko, dan Tautan]]:** Format baku untuk callout studi kasus lapangan, analisis risiko pengasuhan, dan tautan silang.
---

## 4. Checklist Verifikasi Mutu Kontributor (Pre-Publishing Review)

Sebelum mempublikasikan atau memperbarui artikel di Wiki PKN, lakukan verifikasi mandiri menggunakan checklist berikut:
- [ ] **Panjang Karakter:** Apakah artikel telah mencapai minimal 5.000 karakter konten berbobot?
- [ ] **Teks Arab & Harakat:** Apakah seluruh kutipan ayat Al-Qur'an dan hadits shahih telah berharakat lengkap tanpa salah ketik?
- [ ] **Takhrij Sumber:** Apakah nomor hadits, nama rawi, dan rujukan kitab induk klasik tertera dengan jelas (merujuk katalog OpenBayan)?
- [ ] **Integrasi Ulama:** Apakah artikel memuat setidaknya satu kutipan syarah dari ulama mu'tabar (*Ibnul Qayyim, Al-Ghazali, An-Nawawi, Ibnu Katsir, dll.*)?
- [ ] **Matriks Tafrith-Ifrath:** Apakah bahasan memuat diagnosis penyimpangan dan solusi wasathiyah nabawiyah?
- [ ] **Fase Usia:** Apakah artikel menguraikan panduan aplikatif berdasarkan 4 fase perkembangan (*Thufulah, Tamyiz, Murahaqah, Syabab*)?
- [ ] **Wikilinks:** Apakah artikel memuat minimal 3 tautan silang valid menggunakan format `[[Nama Halaman]]`?
- [ ] **Kerapian Quartz:** Apakah frontmatter YAML valid dan blok callout Obsidian ditampilkan dengan benar?

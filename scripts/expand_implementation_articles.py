#!/usr/bin/env python3
"""
scripts/expand_implementation_articles.py
Mengembangkan 6 artikel Paradigma, Kaidah, & Implementasi Pendidikan PKN:
1. Pendidikan Ideal.md
2. Benang Merah Pendidikan.md
3. 4 Kaidah Implementasi.md
4. 4 Elemen Implementasi.md
5. Tanggung Jawab Pendidikan.md
6. Peran Guru dan Lembaga Pendidikan.md

Memasukkan secara komprehensif:
- Contoh nyata interaksi dakwah dan tarbiyah Rasulullah ﷺ bersama para sahabat.
- Keterangan dan fatwa para ulama (Ibnu Qayyim, Ibnu Khaldun, Ibnu Hajar, Asy-Syathibi, Ibn Sahnun, Al-Ghazali).
- Dalil hadits Arab berharakat, terjemahan, dan takhrij OpenBayan.
- Kritik mendalam terhadap reduksi schooling modern & formulasi solutif PKN.
"""

import os

BASE_DIR = "/home/abuhafi/Project/wiki-pkn"
CONTENT_DIR = os.path.join(BASE_DIR, "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi")

ARTICLES = {}

# ==============================================================================
# 1. PENDIDIKAN IDEAL.MD
# ==============================================================================
ARTICLES["Pendidikan Ideal.md"] = """---
title: "Pendidikan Ideal"
tags:
  - pkn
  - pendidikan_ideal
  - akil_baligh
  - generasi_peradaban
  - manhaj_nabawi
---

# Pendidikan Ideal Nabawiyah: Menautkan Akil dan Baligh Menuju Generasi Peradaban

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « كُنتُمْ خَيْرَ أُمَّةٍ أُخْرِجَتْ لِلنَّاسِ تَأْمُرُونَ بِالْمَعْرُوفِ وَتَنْهَوْنَ عَنِ الْمُنكَرِ وَتُؤْمِنُونَ بِاللَّهِ »
>
> *"Kalian adalah sebaik-baik umat (khaira ummah) yang dilahirkan untuk manusia; (karena kalian) menyuruh berbuat ma'ruf, mencegah dari kemungkaran, dan beriman kepada Allah..."*
>
> 📚 **Sumber Rujukan OpenBayan:** QS. Ali 'Imran: 110; Tafsir Ibnu Katsir (Juz 2 Hal. 93); Shahih Al-Bukhari No. 4557; Syarah Riyadush Shalihin.  
> 💡 **Relevansi PKN:** Pendidikan Ideal dalam Islam bukanlah pabrikasi ijazah formal atau perlombaan skor akademis semata, melainkan ikhtiar agung mencetak generasi *Khairu Ummah* yang matang akal budinya (*Akil*) beriringan dengan kedewasaan fisiknya (*Baligh*), kokoh tauhidnya, dan berdaya guna membangun peradaban.

---

## 1. Hakikat Pendidikan Ideal: Rekonstruksi Paradigma Akil-Baligh

Pendidikan Ideal dalam Pendidikan Karakter Nabawiyah (PKN) berakar pada satu misi sentral: **Mengantarkan anak mencapai kedewasaan mental, spiritual, dan sosial (*Akil*) tepat bersamaan dengan datangnya kedewasaan biologis (*Baligh*)**.

### Kesenjangan Patologis Peradaban Modern:
Dalam sistem pendidikan modern sekuler, terjadi jurang pemisah yang sangat lebar (*gap*) antara baligh biologis dan kematangan akal:
* **Baligh Dipercepat:** Karena paparan nutrisi hewani modern berhormon dan banjir rangsangan visual digital, anak-anak mengalami pubertas biologis lebih dini (usia 10–12 tahun).
* **Akil Ditunda-tunda:** Di sisi lain, sistem persekolahan formal menunda kedewasaan mental anak hingga usia 22–25 tahun (lulus kuliah). Anak usia 17 tahun yang telah baligh selama bertahun-tahun masih diperlakukan sebagai "anak-anak" yang tidak berdaya, tidak mandiri secara finansial, dan bebas dari tanggung jawab sosial.
* **Ledakan Masalah Remaja:** Jurang pemisah 10–12 tahun antara baligh dan akil ini melahirkan fenomena kebingungan identitas, kecanduan pornografi, pergaulan bebas, apatisme, hingga depresi mental.

```mermaid
graph LR
    subgraph Model_Modern["Pendidikan Sekuler Modern"]
        M1["Baligh Cepat (Usia 10-12)"] -.->|Jurang 10-12 Tahun Labil| M2["Akil Terlambat (Usia 22-25)"]
    end
    subgraph Model_Nabawi["Pendidikan Ideal Nabawiyah"]
        N1["Baligh Biologis (Usia 14-15)"] ===|Tersinkronisasi Sempurna| N2["Akil & Mukallaf Mandiri (Usia 14-15)"]
    end
```

Pendidikan Ideal Nabawiyah menolak pengkastaan generasi "buih" (*ghutsa'*). Anak yang telah baligh adalah orang dewasa penuh (*rijal / nisa'*) yang siap memikul beban hukum syariat (*taklif*) dan memimpin umat.

---

## 2. Teladan Rasulullah ﷺ Membangun Generasi Terbaik

Rasulullah ﷺ diutus kepada bangsa Arab jahiliyah yang terpecah-belah, buta huruf, dan menyembah berhala. Dalam kurun waktu hanya 23 tahun, melalui metode pendidikan berbasis fitrah dan masjid, beliau berhasil mentransformasikan lebih dari 120.000 manusia menjadi generasi paling agung sepanjang sejarah manusia:

### A. Ekosistem Ash-Shuffah: Universitas Karakter Nabawiyah Pertama
Di serambi Masjid Nabawi, Rasulullah ﷺ membina para sahabat di *Ash-Shuffah*—sebuah lingkungan belajar yang menyatukan antara tilawah Al-Qur'an, pembersihan jiwa (*tazkiyah*), kajian fiqih praktis, dan kerja keras fisik. Di sanalah lahir para ulama besar hadits seperti Abu Hurairah radhiyallahu 'anhu yang mencurahkan siang dan malamnya menyerap ilmu langsung dari bibir kenabian.

### B. Mendidik Manusia Sesuai Keunikannya: Tidak Ada Penyeragaman Kaku
Rasulullah ﷺ tidak pernah meratakan para sahabatnya dengan satu kurikulum seragam:
* Kepada **Abu Dzar Al-Ghifari** yang berjiwa zuhud dan perasa, beliau menasihatkan agar tidak memegang jabatan kepemimpinan: *"Wahai Abu Dzar, sesungguhnya engkau lemah, dan sesungguhnya kepemimpinan itu adalah amanah yang bisa menjadi kehinaan dan penyesalan di hari kiamat!"* (HR. Muslim No. 1825).
* Kepada **Khalid bin Al-Walid** yang berjiwa ksatria dan berani memimpin, beliau tidak memaksanya menjadi penghafal hadits, melainkan mengangkatnya menjadi panglima tertinggi: *"Khalid adalah pedang di antara pedang-pedang Allah yang Dia hunus atas orang-orang kafir!"* (HR. Tirmidzi No. 3820).
* Kepada **Zaid bin Tsabit** yang memiliki kecerdasan logika dan ketelitian hafalan, beliau menugaskannya memimpin dewan pencatatan wahyu Al-Qur'an dan menguasai ilmu faraidh.

---

## 3. Keterangan Para Ulama Otoritatif

### 1. Sosiolog Muslim Ibnu Khaldun (Wafat 808 H)
Dalam kitab monumentalnya *Al-Muqaddimah* (Bab 6: Bahaya Kekerasan Guru Terhadap Murid):
> « إِنَّ الإِرْهَافَ فِي التَّعْلِيمِ مُضِرٌّ بِالمُتَعَلِّمِ، سِيَّمَا فِي أَصَاغِرِ الوَلَدِ... وَمَنْ كَانَ مَرْبَاهُ بِالعَسْفِ وَالقَهْرِ مِنَ المُتَعَلِّمِينَ، سَطَا بِهِ القَهْرُ، وَضَيَّقَ عَلَى النَّفْسِ فِي انْبِسَاطِهَا، وَذَهَبَ بِنَشَاطِهَا، وَدَعَاهُ إِلَى الكَسَلِ، وَحَمَلَ عَلَى الكَذِبِ وَالخُبْثِ... فَتَفْسُدُ مَعَانِي الإِنْسَانِيَّةِ الَّتِي فِي فِطْرَتِهِ! »  
> *"Sesungguhnya bersikap keras dan membebani dalam pengajaran sangat berbahaya bagi para penuntut ilmu, terlebih bagi anak-anak kecil... Barangsiapa yang metode pendidikannya didasarkan pada kekerasan, paksaan, dan intimidasi, maka paksaan itu akan menindas jiwanya, menyempitkan kelapangan hatinya, mematikan gairah belajarnya, menyeretnya kepada kemalasan, serta mendorongnya untuk berbohong dan bersikap licik demi menghindari hukuman... Akibatnya, nilai-nilai kemanusiaan luhur yang ada pada fitrah aslinya akan rusak binasa!"*

### 2. Imam Ibnu Qayyim Al-Jauziyyah
Dalam kitab *I'lamul Muwaqqi'in*:
> *"Syariat ini seluruhnya dibangun di atas hikmah dan kemaslahatan bagi para hamba di dunia dan akhirat. Keadilan syariat menuntut bahwa pendidikan anak harus memperhatikan watak bawaan (*syakilah*) dan kesiapan fitrahnya; tidak boleh memaksakan ikan untuk terbang atau memaksa burung untuk menyelam."*

---

## 4. Enam Pilar Ekosistem Pendidikan Ideal PKN

Untuk merealisasikan pendidikan ideal yang memerdekakan fitrah anak, PKN merumuskan **6 Pilar Ekosistem**:

1. **[[Benang Merah Pendidikan]]**: Menghubungkan seluruh cabang ilmu pengetahuan dengan tauhidullah, membongkar sekularisme kurikulum modern.
2. **[[Metode Mendidik]]**: Mengoperasikan Tiga Bahasa Nabawiyah (Bahasa Hati, Bahasa Lisan, Bahasa Tangan) secara berjenjang.
3. **[[Pembelajaran Alamiah]]**: Mengembalikan pembelajaran ke habitat kehidupan nyata (magang, observasi alam bebas, interaksi sosial nyata) tanpa terpenjara di empat dinding kelas.
4. **[[Luka dan Hutang Pengasuhan]]**: Menyediakan protokol pemulihan (*recovery*) bagi fitrah yang terdistorsi oleh kesalahan pola asuh masa lalu.
5. **[[Batas Toleransi]]**: Menentukan titik temu kapan orang tua harus melonggarkan pemaafan dan kapan harus menegakkan ketegasan sanksi syariat per fase usia.
6. **[[Imunitas Sosial]]**: Membangun benteng kekebalan karakter agar generasi muslim mampu menjadi filter mandiri di tengah tsunami informasi dan pergaulan digital.

---

## 5. Tautan Konseptual Terkait
* [[Benang Merah Pendidikan]] — Kritik Arsitektur Pendidikan Modern.
* [[Metode Mendidik]] — Tiga Bahasa Pengasuhan Nabawiyah.
* [[Pembelajaran Alamiah]] — Metode Belajar Berbasis Ekosistem Nyata.
* [[Perkembangan]] — Pentahapan Usia Menuju Akil-Baligh.
* [[Tujuan Hidup Manusia]] — Orientasi Penciptaan Khalifah fil Ardh.
"""

# ==============================================================================
# 2. BENANG MERAH PENDIDIKAN.MD
# ==============================================================================
ARTICLES["Pendidikan Ideal/Benang Merah Pendidikan.md"] = """---
title: "Benang Merah Pendidikan"
tags:
  - pkn
  - benang_merah
  - kritik_schooling
  - fitrah_bakat
  - restorasi_pendidikan
---

# Benang Merah Pendidikan: Kritik Sistem Pabrik Modern & Restorasi Fitrah

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « كُلُّكُمْ يَعْمَلُ عَلَىٰ شَاكِلَتِهِ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًا »
>
> *"Katakanlah: 'Tiap-tiap orang berbuat menurut keadaannya (syakilatihi - cetak biru potensi dan fitrah bawaannya) masing-masing.' Maka Tuhanmu lebih mengetahui siapa yang lebih benar jalannya."*
>
> 📚 **Sumber Rujukan OpenBayan:** QS. Al-Isra': 84; Tafsir Ibnu Katsir (Juz 5 Hal. 112); Shahih Al-Bukhari No. 4949 (Sabda Nabi ﷺ: *"Beramallah kalian, karena setiap orang akan dimudahkan menuju apa yang ia diciptakan untuknya!"*).  
> 💡 **Relevansi PKN:** Ayat dan hadits ini adalah asas "Benang Merah Pendidikan". Allah tidak menciptakan manusia dengan cetakan seragam bagaikan bata merah. Setiap anak memiliki panggilan peran kekhalifahan unik yang wajib ditemukan dan ditumbuhkan, bukan diseragamkan secara paksa oleh kurikulum industri.

---

## 1. Kritik Paradigma Pendidikan Modern Model Pabrik (Prussian Schooling)

Sistem persekolahan massal yang mendominasi dunia hari ini lahir dari revolusi industri abad ke-19 (Model Prusia) yang didesain bukan untuk memuliakan fitrah manusia, melainkan untuk **mencetak pekerja pabrik dan birokrat yang patuh, seragam, dan mudah diatur**:
* **Standarisasi Kaku:** Jam masuk berbunyi lonceng bagaikan pabrik, murid dibagi berdasarkan usia (tahun produksi), dan dinilai dari kepatuhan duduk diam berjam-jam mendengarkan instruksi satu arah.
* **Reduksi Manusia Menjadi Angka Rapor:** Kecerdasan manusia yang mahakaya direduksi hanya pada kemampuan menghafal dan berhitung di atas kertas ujian. Anak yang memiliki kejeniusan sosial, kepemimpinan lapangan, atau keahlian mekanik dicap "kurang pintar" hanya karena nilai matematikanya rendah.
* **Perampasan Hak Fase Emas:** Anak-anak balita di usia 4–6 tahun dipaksa duduk tenang dengan tugas pekerjaan rumah (*PR*) dan drill calistung mekanis, merampas hak bermain merdeka yang dijamin fitrah dan sunnah Nabi ﷺ.

```mermaid
graph TD
    subgraph Sistem_Pabrik["Sistem Pendidikan Pabrik Modern"]
        P1["Keseragaman Massal & Kurikulum Kaku"] --> P2["Menghukum Perbedaan Bakat & Keunikan"]
        P2 --> P3["Melahirkan 'Generasi Buih' yang Seragam tapi Rapuh"]
    end
    subgraph Benang_Merah["Benang Merah Pendidikan Nabawiyah"]
        N1["Observasi Cetak Biru Fitrah (Syakilah)"] --> N2["Fasilitasi Pertumbuhan 40 Pilar Bakat Unik"]
        N2 --> N3["Melahirkan Generasi Muslih Mandiri Sesuai Peran"]
    end
```

---

## 2. Teladan Rasulullah ﷺ: Pemimpin yang Memelihara Keberagaman Potensi

Rasulullah ﷺ adalah pendidik teragung yang tidak pernah memaksakan standarisasi seragam kepada para sahabatnya:

### A. Sabda Nabi ﷺ tentang Kemudahan Sesuai Panggilan Takdir
Ketika para sahabat bertanya tentang takdir dan amal perbuatan, Rasulullah ﷺ bersabda:
> « اعْمَلُوا فَكُلٌّ مُيَسَّرٌ لِمَا خُلِقَ لَهُ، أَمَّا مَنْ كَانَ مِنْ أَهْلِ السَّعَادَةِ فَيُيَسَّرُ لِعَمَلِ أَهْلِ السَّعَادَةِ، وَأَمَّا مَنْ كَانَ مِنْ أَهْلِ الشَّقَاءِ فَيُيَسَّرُ لِعَمَلِ أَهْلِ الشَّقَاوَةِ »  
> *"Beramallah kalian, karena setiap orang akan dimudahkan menuju apa yang ia diciptakan untuknya! Adapun orang yang termasuk golongan yang bahagia, niscaya ia akan dimudahkan untuk melakukan amalan orang-orang yang bahagia; dan orang yang termasuk golongan celaka akan dimudahkan menuju amalan orang-orang yang celaka."*  
> 📚 *(HR. Al-Bukhari No. 4949 & Muslim No. 2647)*

Hadits ini menjadi landasan bahwa setiap anak memiliki **bakat dan kecenderungan amal shalih yang telah diinstal oleh Allah**. Tugas orang tua bukan mendesain anak menjadi fotokopi dirinya, melainkan mengamati ke mana arah kemudahan (*muyassarun*) anak tersebut beramal.

### B. Pos-Pos Peradaban Shahabat yang Beragam
* **Khalid bin Walid** tidak dipaksa duduk menghafal ribuan hadits, melainkan disalurkan memimpin sayap kavaleri perang.
* **Abu Hurairah** tidak dipaksa menjadi saudagar atau komandan perang, melainkan difasilitasi di Ash-Shuffah menghafal dan meriwayatkan hadits.
* **Abdurrahman bin Auf** tidak dipaksa menjadi tentara garis depan permanen, melainkan didorong menguasai pasar Madinah dan mendanai logistik dakwah.
* **Bilal bin Rabah** yang memiliki suara lantang dan dada yang lapang diangkat menjadi muadzin resmi Islam.
Semua sahabat berbeda pos, namun semuanya mulia dan bersinergi membangun tegaknya peradaban Islam!

---

## 3. Keterangan Para Ulama Otoritatif

### 1. Imam Ibnu Qayyim Al-Jauziyyah
Dalam kitab *Tuhfatul Maudud bi Ahkamil Maulud* (Hal. 242):
> « وَمِمَّا يَحْتَاجُ إِلَيْهِ الطِّفْلُ غَايَةَ الِاحْتِيَاجِ: أَنْ يُعْتَنَى بِأَمْرِ خُلُقِهِ، فَإِنَّهُ يَنْشَأُ عَلَى مَا عَوَّدَهُ الْمُرَبِّي فِي صِغَرِهِ... فَإِذَا كَانَ الْوَلَدُ مُسْتَعِدًّا لِفَهْمِ العِلْمِ وَحِفْظِهِ، فَلْيُفَرَّغْ لَهُ، وَإِنْ كَانَ مُسْتَعِدًّا لِلْفُرُوسِيَّةِ وَأَسْبَابِهَا فَلْيُمَكَّنْ مِنْهَا، وَإِنْ كَانَ لَمْ يُخْلَقْ لِذَلِكَ كُلِّهِ، وَخُلِقَ لِصِنَاعَةٍ مِنْ الصَّنَائِعِ فَلْيُمَكَّنْ مِنْهَا بَعْدَ أَنْ يُعَلَّمَ مَا لَا بُدَّ مِنْهُ مِنْ أَمْرِ دِينِهِ! »  
> *"Dan di antara perkara yang sangat dibutuhkan oleh anak: hendaklah diperhatikan betul kecenderungan fitrahnya... Jika anak memiliki kesiapan bakat untuk memahami ilmu dan menghafalnya, maka fokuskanlah ia untuk ilmu. Jika ia memiliki bakat dan kecenderungan dalam keterampilan berkuda/keprajuritan (*al-furusiyyah*), maka fasilitasilah ia di bidang itu. Dan jika ia tidak diciptakan untuk kedua hal tersebut, melainkan berbakat dalam salah satu jenis perniagaan atau keahlian pertukangan (*shina'ah*), maka berikanlah ruang baginya di bidang tersebut—setelah ia terlebih dahulu diajarkan ilmu agama fardhu 'ain yang wajib baginya!"*

### 2. Imam Asy-Syathibi dalam Al-I'tisham
> *"Kesesuaian amal perbuatan dengan fitrah pembawaan adalah rahmat Allah yang memelihara kelangsungan tatanan dunia. Seandainya semua manusia dipaksa menjadi ulama fikih, niscaya runtuhlah perekonomian dan ketahanan pangan; dan seandainya semua manusia dipaksa menjadi petani, niscaya lenyaplah ilmu syariat."*

---

## 4. Benang Merah Kurikulum PKN: Menautkan Tauhid, Adab, dan Karya

PKN mengembalikan pendidikan kepada mata rantai fitrah yang lurus:

```text
[TAUHIDULLAH / IMAN]  --->  Mendasari seluruh niat hidup anak
        ↓
[ADAB & AKHLAK MULIA] --->  Membingkai cara anak berinteraksi
        ↓
[FITRAH BAKAT (TB40)] --->  Menentukan keunikan peran amal shalih
        ↓
[KARYA PERADABAN]     --->  Maslahat nyata bagi umat manusia
```

1. **Rumah Tangga sebagai Inkubator Utama:**
   * Ayah bertindak sebagai Arsitek Visi, penjaga tauhid, dan penegak hukum syariat (*Qowwamah*).
   * Bunda bertindak sebagai Madrasah Utama, sumber curahan kasih sayang, dan pembina adab keseharian (*Rahimah*).
2. **Sekolah sebagai Mitra Komplementer:**
   * Sekolah hadir bukan untuk menggantikan peran keluarga, melainkan sebagai ekosistem laboratorium sosial yang mendukung penumbuhan potensi unik anak.
3. **Bebas dari Penyakit Al-Wahn:**
   * Anak dididik memiliki cita-cita mulia akhirat, tidak takut miskin saat beramal shalih, dan bangga dengan identitas Islam di tengah peradaban global.

---

## 5. Tautan Konseptual Terkait
* [[Pendidikan Ideal]] — Menautkan Akil dan Baligh Menuju Peradaban.
* [[Bakat]] — Pemetaan 40 Sifat Karakter Nabawiyah.
* [[Pembelajaran Alamiah]] — Model Pembelajaran Alami Non-Formal.
* [[Peran Ayah dan Bunda]] — Sinergi Kepemimpinan Pengasuhan Rumah Tangga.
"""

# ==============================================================================
# 3. 4 KAIDAH IMPLEMENTASI.MD
# ==============================================================================
ARTICLES["Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md"] = """---
title: "4 Kaidah Implementasi"
tags:
  - pkn
  - kaidah_implementasi
  - tadarruj
  - qudwah
  - rahmah
---

# 4 Kaidah Emas Implementasi Pendidikan Karakter Nabawiyah

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « يَسِّرُوا وَلَا تُعَسِّرُوا، وَبَشِّرُوا وَلَا تُنَفِّرُوا، وَتَطَاوَعَا وَلَا تَخْتَلِفَا »
>
> *"Permudahlah dan jangan mempersulit, berikanlah kabar gembira dan jangan membuat orang lari menjauh, serta bersatu-padulah kalian dan jangan saling berselisih!"*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Al-Bukhari No. 69 & Muslim No. 1733; Wasiat Rasulullah ﷺ kepada Mu'adz bin Jabal dan Abu Musa Al-Asy'ari saat diutus ke Yaman; Riyadush Shalihin No. 637.  
> 💡 **Relevansi PKN:** Empat Kaidah Implementasi adalah kompas operasional bagi seluruh orang tua, guru, dan pengelola lembaga pendidikan dalam menerapkan PKN secara aplikatif, menggembirakan, dan terbebas dari kekakuan doktrin yang membuat anak lari menjauh dari agama.

---

## 1. Arsitektur Empat Kaidah Emas PKN

Pendidikan Karakter Nabawiyah merumuskan **4 Kaidah Emas Operasional** yang wajib dipegang teguh oleh setiap pendidik:

```mermaid
graph TD
    K["4 Kaidah Emas Implementasi PKN"]
    K --> K1["Kaidah 1: Pentahapan Alami (At-Tadarruj)"]
    K --> K2["Kaidah 2: Koneksi Sebelum Koreksi (Al-Washlu qablal Qath')"]
    K --> K3["Kaidah 3: Keteladanan Sebelum Tuntutan (Al-Qudwah qablad Da'wah)"]
    K --> K4["Kaidah 4: Fokus Kekuatan Bakat (Ta'zizul Quwwah)"]
```

---

## 2. Rincian Kaidah, Dalil OpenBayan, & Contoh Interaksi Shahabat

### Kaidah 1: Pentahapan Alami (At-Tadarruj fi At-Tarbiyah)
* **Makna Kaidah:** Menumbuhkan karakter mengikuti ritme kematangan biologis dan kejiwaan anak, tidak menuntut buah matang sebelum pohon berakar kuat.
* **Teladan Rasulullah ﷺ & Atsar Aisyah radhiyallahu 'anha:**
  Ummul Mukminin Aisyah mengisahkan hikmah agung pentahapan turunnya Al-Qur'an:
  > « إِنَّمَا نَزَلَ أَوَّلَ مَا نَزَلَ مِنْهُ سُورَةٌ مِنَ المُفَصَّلِ، فِيهَا ذِكْرُ الجَنَّةِ وَالنَّارِ، حَتَّى إِذَا ثَابَ النَّاسُ إِلَى الإِسْلاَمِ نَزَلَ الحَلاَلُ وَالحَرَامُ، وَلَوْ نَزَلَ أَوَّلَ شَيْءٍ: لاَ تَشْرَبُوا الخَمْرَ، لَقَالُوا: لاَ نَدَعُ الخَمْرَ أَبَدًا! وَلَوْ نَزَلَ: لاَ تَزْنُوا، لَقَالُوا: لاَ نَدَعُ الزِّنَا أَبَدًا! »  
  > *"Sesungguhnya ayat Al-Qur'an yang mula-mula turun adalah surat-surat Al-Mufashshal yang di dalamnya menceritakan surga dan neraka (menanamkan keimanan). Hingga ketika manusia telah condong dan kokoh dalam Islam, barulah turun ayat-ayat tentang halal dan haram. Seandainya yang pertama kali turun adalah: 'Janganlah kalian minum khamr!', niscaya mereka akan berkata: 'Kami tidak akan meninggalkan khamr selamanya!' Dan seandainya yang pertama kali turun adalah: 'Janganlah kalian berzina!', niscaya mereka akan berkata: 'Kami tidak akan meninggalkan zina selamanya!'"*  
  > 📚 *(HR. Al-Bukhari No. 4993, Kitab Fadha'ilil Qur'an)*
* **Aplikasi Praktis PKN:** Jangan menuntut anak usia 7 tahun khusyuk shalat laksana ulama senior; usia 7–10 tahun adalah masa pembiasaan gerak dan cinta shalat, bukan masa penuntutan kesempurnaan.

---

### Kaidah 2: Koneksi Sebelum Koreksi (Al-Washlu qablal Qath')
* **Makna Kaidah:** Memastikan jalinan kasih sayang, kepercayaan batin, dan tangki cinta anak terisi penuh sebelum melancarkan koreksi atau teguran disiplin.
* **Teladan Rasulullah ﷺ Bersama Orang Arab Badui di Masjid:**
  Anas bin Malik menceritakan seorang Arab Badui yang kencing di sudut Masjid Nabawi:
  > « أَنَّ أَعْرَابِيًّا بَالَ فِي المَسْجِدِ، فَقَامَ إِلَيْهِ بَعْضُ القَوْمِ لِيَقَعُوا بِهِ، فَقَالَ رَسُولُ اللَّهِ ﷺ: دَعُوهُ وَلَا تُزْرِمُوهُ، فَلَمَّا فَرَغَ دَعَا بِذَنُوبٍ مِنْ مَاءٍ فَصُبَّ عَلَيْهِ، ثُمَّ دَعَاهُ فَقَالَ لَهُ: إِنَّ هَذِهِ المَسَاجِدَ لَا تَصْلُحُ لِشَيْءٍ مِنْ هَذَا البَوْلِ وَالقَذَرِ، إِنَّمَا هِيَ لِذِكْرِ اللَّهِ وَالصَّلَاةِ وَقِرَاءَةِ القُرْآنِ »  
  > *"Seorang Badui kencing di dalam masjid, maka sebagian sahabat bangkit hendak memukulnya. Rasulullah ﷺ bersabda: 'Biarkan dia dan jangan putuskan kencingnya!' Ketika orang Badui itu selesai kencing, beliau meminta seember air lalu menyiram bekas kencingnya. Kemudian beliau memanggil orang Badui itu dengan lembut dan bersabda: 'Sesungguhnya masjid-masjid ini tidak layak untuk air kencing dan kotoran sedikit pun; masjid itu hanya dibangun untuk mengingat Allah, mendirikan shalat, dan membaca Al-Qur'an.'"*  
  > 📚 *(HR. Al-Bukhari No. 220 & Muslim No. 285)*
* **Aplikasi Praktis PKN:** Saat anak berbuat salah (menumpahkan susu, memecahkan piring), jangan langsung menghardik. Dekap tubuhnya, tenangkan ketakutannya (*Koneksi*), bersihkan bersama-sama, barulah ajarkan cara memegang gelas yang benar (*Koreksi*).

---

### Kaidah 3: Keteladanan Sebelum Tuntutan (Al-Qudwah qablad Da'wah)
* **Makna Kaidah:** Pendidik wajib menjadi cerminan hidup dari nilai yang diajarkan. Anak adalah peniru ulung; ia mendengar apa yang kita lakukan, bukan apa yang kita ucapkan.
* **Teladan Rasulullah ﷺ pada Perjanjian Hudaibiyah:**
  Saat para sahabat terpukul dan enggan menyembelih hewan qurban tanda tahallul karena kecewa dengan isi perjanjian yang berat sebelah, Rasulullah ﷺ masuk ke tenda Ummu Salamah radhiyallahu 'anha. Ummu Salamah memberikan usulan cerdas: *"Wahai Rasulullah, keluarlah dan jangan berbicara sepatah kata pun kepada mereka sampai engkau menyembelih untamu dan memanggil tukang cukurmu untuk mencukur rambutmu!"* Ketika Rasulullah ﷺ keluar dan mempraktikkannya di depan mata para sahabat tanpa berkata-kata, seketika itu pula seluruh sahabat bangkit berebut menyembelih qurban dan mencukur rambut mereka! *(HR. Al-Bukhari No. 2731).*
* **Aplikasi Praktis PKN:** Orang tua yang ingin anaknya gemar membaca Al-Qur'an dan menjauhi gawai harus meletakkan ponselnya dan membuka mushaf Al-Qur'an setiap hari di ruang tengah keluarga.

---

### Kaidah 4: Fokus pada Kekuatan Bakat (Ta'zizul Quwwah)
* **Makna Kaidah:** Berfokus melejitkan potensi bakat alami anak (*focus on strengths*), bukan membuang energi hidup untuk memaksa memperbaiki kelemahan yang memang bukan bawaan fitrahnya.
* **Keterangan Imam Ibnu Qayyim Al-Jauziyyah:**
  Dalam *Madarijus Salikin*:
  > *"Pintu masuk menuju surga dan keridhaan Allah itu berbilang sesuai dengan ragam potensi manusia: ada yang dibukakan pintu melalui shalat sunnah dan puasa, ada yang melalui jihad dan keberanian, ada yang melalui sedekah dan harta, ada yang melalui ilmu dan tadabbur. Maka orang tua yang bijak mengamati pintu mana yang paling mudah bagi anaknya untuk masuk menuju Allah, lalu ia membimbingnya di jalan tersebut."*
* **Aplikasi Praktis PKN:** Jika anak memiliki bakat kuat dalam komunikasi dan kepemimpinan (*Memerintah*), jangan paksa ia menjadi juara olimpiade sains murni. Fasilitasi kekuatannya agar menjadi juru bicara dakwah yang tangguh.

---

## 3. Tautan Konseptual Terkait
* [[4 Elemen Implementasi]] — Struktur Empat Komponen Ekosistem PKN.
* [[Metode Mendidik]] — Operasionalisasi Tiga Bahasa Nabawiyah.
* [[Pendidikan Ideal]] — Paradigma Akil-Baligh dan Generasi Peradaban.
* [[Bakat]] — Penjabaran 40 Sifat Karakter Nabawiyah.
"""

# ==============================================================================
# 4. 4 ELEMEN IMPLEMENTASI.MD
# ==============================================================================
ARTICLES["Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md"] = """---
title: "4 Elemen Implementasi"
tags:
  - pkn
  - elemen_implementasi
  - arsitektur_pkn
  - kurikulum_fitrah
---

# 4 Elemen Implementasi Pendidikan Karakter Nabawiyah

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « هُوَ الَّذِي بَعَثَ فِي الْأُمِّيِّينَ رَسُولًا مِّنْهُمْ يَتْلُو عَلَيْهِمْ آيَاتِهِ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ الْكِتَابَ وَالْحِكْمَةَ وَإِن كَانُوا مِن قَبْلُ لَفِي ضَلَالٍ مُّبِينٍ »
>
> *"Dialah yang mengutus kepada kaum yang buta huruf seorang Rasul di antara mereka, yang membacakan ayat-ayat-Nya kepada mereka, menyucikan (jiwa) mereka, dan mengajarkan kepada mereka Kitab (Al-Qur'an) dan Hikmah (As-Sunnah). Dan sesungguhnya mereka sebelumnya benar-benar dalam kesesatan yang nyata."*
>
> 📚 **Sumber Rujukan OpenBayan:** QS. Al-Jumu'ah: 2; Tafsir Ibnu Katsir (Juz 8 Hal. 115); Al-Hulal al-Ibriziyyah min Ta'liqat al-Baziyyah ala Shahih al-Bukhari.  
> 💡 **Relevansi PKN:** Ayat ini menguraikan 4 elemen arsitektural risalah kenabian: Pembacaan tanda kebesaran Allah (Elemen Iman), Penyucian jiwa (Elemen Adab/Hati), Pengajaran hukum syariat (Elemen Belajar), dan Kebijaksanaan aplikasi nyata (Elemen Bakat/Peradaban).

---

## 1. Arsitektur Empat Elemen Ekosistem PKN

Agar Pendidikan Karakter Nabawiyah dapat beroperasi secara utuh di rumah dan sekolah, terdapat **4 Elemen Inti** yang harus hadir secara serentak dan saling menopang:

```mermaid
graph TD
    subgraph Ekosistem["4 Elemen Implementasi PKN"]
        E1["1. Elemen Iman (Ghayah/Tujuan)<br>Penanaman Tauhidullah & Muraqabatullah"]
        E2["2. Elemen Adab (Tazkiyah/Penyucian)<br>Pembersihan Hati & Akhlakul Karimah"]
        E3["3. Elemen Belajar (Manhaj/Nalar)<br>Eksplorasi Alam & Fiqih Syariat"]
        E4["4. Elemen Bakat (Khafiyah/Amal Shalih)<br>Aktualisasi 40 Potensi Peradaban"]
    end
    E1 --> E2 --> E3 --> E4
```

---

## 2. Rincian Empat Elemen & Teladan Tarbiyah Nabawiyah

### 1. Elemen Iman (الغَايَة - Al-Ghayah / Tujuan Tertinggi)
* **Hakikat:** Memastikan bahwa seluruh aktivitas pendidikan anak bermuara pada pengenalan (*Ma'rifatullah*), kecintaan (*Mahabbah*), dan ketundukan mutlak kepada Allah SWT.
* **Teladan Rasulullah ﷺ di Darul Arqam:** Selama 13 tahun fase Makkah, Rasulullah ﷺ memfokuskan pembinaan akidah tauhid sebelum hukum-hukum muamalah dan sanksi hudud diturunkan di Madinah. Hasilnya adalah para sahabat memiliki imunitas iman yang kokoh menghadapi siksaan dahsyat kaum musyrikin (seperti Bilal bin Rabah, Khabbab, dan Keluarga Yasir).
* **Aplikasi Keluarga:** Menghidupkan suasana zikir di rumah, mengaitkan seluruh fenomena sains dengan kekuasaan Allah (*"Lihatlah siapa yang menciptakan langit tanpa tiang ini"*).

### 2. Elemen Adab (التَّزْكِيَة - At-Tazkiyah / Penataan Jiwa)
* **Hakikat:** Menanamkan rasa hormat, tata krama, kesucian diri (*'iffah*), dan kerendahan hati sebelum mengajarkan ilmu pengetahuan akademis.
* **Atsar Shahabat & Ulama Salaf:**
  * Abdullah bin Al-Mubarak berkata: *"Kami mempelajari adab selama tiga puluh tahun, dan kami mempelajari ilmu pengetahuan selama dua puluh tahun."*
  * Imam Malik menasihatkan kepada pemuda Quraisy: *"Pelajarilah adab sebelum engkau mempelajari ilmu!"*
* **Aplikasi Keluarga:** Membiasakan adab makan, adab berbicara, adab meminta izin memasuki kamar orang tua (*isti'dzan*), dan adab menghormati orang yang lebih tua.

### 3. Elemen Belajar (المَنْهَج - Al-Manhaj / Logika & Eksplorasi)
* **Hakikat:** Mengasah fitrah ingin tahu alami anak melalui interaksi langsung dengan dunia nyata (*tajribah & mushahadah*), bukan hafalan mekanis di luar konteks.
* **Teladan Rasulullah ﷺ Mengajarkan Fiqih Praktis:** Rasulullah ﷺ tidak hanya berceramah di atas mimbar, melainkan berwudhu di hadapan para sahabat seraya bersabda: *"Barangsiapa berwudhu seperti wudhuku ini..."* (HR. Bukhari No. 159), dan bersabda: *"Shalatlah kalian sebagaimana kalian melihat aku shalat!"* (HR. Bukhari No. 631).
* **Aplikasi Keluarga:** Mengajak anak ke pasar tradisional untuk belajar matematika jual-beli, mengamati semut dan tumbuhan untuk belajar biologi ciptaan Allah.

### 4. Elemen Bakat (العَمَل - Al-'Amal / Aktualisasi Peran Kekhalifahan)
* **Hakikat:** Mengidentifikasi dan memfasilitasi 40 sifat karakter mulia (TB40) anak hingga bermuara pada karya amal shalih yang solutif bagi umat.
* **Teladan Rasulullah ﷺ Membina Potensi Khusus:** Beliau mengarahkan Hassan bin Tsabit bersyair membela Islam, mengutus Mush'ab bin Umair berdiplomasi, dan mengangkat Usamah bin Zaid memimpin ekspedisi militer.
* **Aplikasi Keluarga:** Menggunakan instrumen observasi Rukun 3A (Suka, Bisa, Bermanfaat) untuk menemukan penjurusan profesi anak menjelang usia baligh.

---

## 3. Tautan Konseptual Terkait
* [[4 Kaidah Implementasi]] — Prinsip Operasional Pengasuhan.
* [[Pendidikan Ideal]] — Paradigma Akil-Baligh PKN.
* [[Bakat]] — Katalog 40 Sifat Karakter Nabawiyah.
* [[Tanggung Jawab Pendidikan]] — Peran Asali Orang Tua dalam Pengasuhan.
"""

# ==============================================================================
# 5. TANGGUNG JAWAB PENDIDIKAN.MD
# ==============================================================================
ARTICLES["Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md"] = """---
title: "Tanggung Jawab Pendidikan"
tags:
  - pkn
  - tanggung_jawab
  - amanah_orang_tua
  - fardhu_ain
---

# Tanggung Jawab Asali Pendidikan: Mandat Mutlak di Pundak Orang Tua

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « يَا أَيُّهَا الَّذِينَ آمَنُوا قُوا أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا وَقُودُهَا النَّاسُ وَالْحِجَارَةُ عَلَيْهَا مَلَائِكَةٌ غِلَاظٌ شِدَادٌ »
>
> *"Wahai orang-orang yang beriman, peliharalah dirimu dan keluargamu dari api neraka yang bahan bakarnya adalah manusia dan batu; penjaganya malaikat-malaikat yang kasar dan keras..."*
>
> 📚 **Sumber Rujukan OpenBayan:** QS. At-Tahrim: 6; Tafsir Ibnu Katsir (Juz 8 Hal. 188); Shahih Al-Bukhari No. 893 & Muslim No. 1829 (Hadits Kepemimpinan Keluarga); Riyadush Shalihin No. 115.  
> 💡 **Relevansi PKN:** Ayat ini menegaskan bahwa tanggung jawab pendidikan dan penyelamatan anak dari fitnah dunia dan siksa akhirat adalah mandat fardhu 'ain yang melekat mutlak pada kedua orang tua kandung. Sekolah, guru les, dan pesantren hanyalah mitra pendukung yang tidak menggugurkan hisab orang tua di hadapan Allah.

---

## 1. Hakikat Mandat Pengasuhan dalam Islam

Dalam syariat Islam, anak bukanlah milik negara dan bukan pula hak milik mutlak orang tua, melainkan **Amanah Suci (Wadi'ah Ilahiyyah)** yang dititipkan Allah SWT. 

### Hadits Pokok Kepemimpinan & Pewarnaan Fitrah:
Rasulullah ﷺ meletakkan prinsip pertanggungjawaban personal:
> « كُلُّكُمْ رَاعٍ، وَكُلُّكُمْ مَسْئُولٌ عَنْ رَعِيَّتِهِ: الإِمَامُ رَاعٍ وَمَسْئُولٌ عَنْ رَعِيَّتِهِ، وَالرَّجُلُ رَاعٍ فِي أَهْلِهِ وَهُوَ مَسْئُولٌ عَنْ رَعِيَّتِهِ، وَالمَرْأَةُ رَاعِيَةٌ فِي بَيْتِ زَوْجِهَا وَمَسْئُولَةٌ عَنْ رَعِيَّتِهَا »  
> *"Setiap kalian adalah pemimpin (penggembala), dan setiap kalian akan dimintai pertanggungjawaban atas apa yang dipimpinnya: Seorang kepala negara adalah pemimpin rakyatnya dan akan dimintai pertanggungjawaban atas mereka. Seorang suami adalah pemimpin di tengah keluarganya dan akan dimintai pertanggungjawaban atas asuhannya. Dan seorang istri adalah pemimpin di rumah suaminya dan akan dimintai pertanggungjawaban atas apa yang di bawah asuhannya..."*  
> 📚 *(HR. Al-Bukhari No. 893 & Muslim No. 1829)*

Dan dalam hadits fitrah yang sangat masyhur:
> « مَا مِنْ مَوْلُودٍ إِلَّا يُولَدُ عَلَى الفِطْرَةِ، فَأَبَوَاهُ يُهَوِّدَانِهِ أَوْ يُنَصِّرَانِهِ أَوْ يُمَجِّسَانِهِ »  
> *"Tidak ada seorang bayi pun yang dilahirkan melainkan ia lahir di atas fitrah (kesucian Islam). Maka kedua orang tuanyalah yang menjadikannya beragama Yahudi, atau Nasrani, atau Majusi!"*  
> 📚 *(HR. Al-Bukhari No. 1358 & Muslim No. 2658)*

Perhatikan redaksi sabda Nabi ﷺ: **« فَأَبَوَاهُ » (Maka kedua orang tuanyalah)**—bukan sekolahnya, bukan kurikulum negaranya, bukan gurunya! Orang tualah pemegang pena utama yang melukis dan mewarnai fitrah sang anak.

---

## 2. Fenomena Cuci Tangan Pendidikan Modern

Salah satu bencana terbesar peradaban modern adalah fenomena **cuci tangan pendidikan (*outsourcing parenting*)**:
* **Menitipkan Anak Secara Penuh:** Orang tua merasa kewajiban pendidikannya telah tuntas begitu membayar SPP mahal ke sekolah Islam terpadu, mengirim anak ke asrama sejak usia dini, atau menyewa guru privat.
* **Hancurnya Keterikatan Jiwa (*Attachment Rupture*):** Anak tumbuh tanpa figur ayah dan tanpa pelukan bunda. Akibatnya, rumah tangga hanya menjadi tempat transit tidur dan hotel makan, sementara transfer nilai diambil alih oleh pergaulan sebaya liar dan algoritma media sosial.
* **Penyangkalan Tanggung Jawab Saat Terjadi Masalah:** Ketika anak kecanduan gawai, berkata kasar, atau mogok shalat, orang tua menyalahkan guru dan sekolah, lupa bahwa hisab pertama di hari kiamat ditujukan kepada ayah dan ibu!

---

## 3. Keterangan Para Ulama Otoritatif

### 1. Imam Ibnu Qayyim Al-Jauziyyah
Dalam *Tuhfatul Maudud bi Ahkamil Maulud* (Hal. 229):
> *"Barangsiapa melalaikan pendidikan anaknya terhadap apa yang bermanfaat baginya dan membiarkannya terlantar tanpa bimbingan adab, sungguh ia telah berbuat seburuk-buruk kezaliman kepadanya. Mayoritas kerusakan karakter anak berakar dari kelalaian para ayah yang mengabaikan pengajaran kewajiban syariat dan sunnah nabawiyah kepada anaknya di masa kecil."*

### 2. Sahabat Ali bin Abi Thalib radhiyallahu 'anhu
Saat menafsirkan firman Allah: *« قُوا أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا »* (*"Peliharalah dirimu dan keluargamu dari api neraka"*):
> « عَلِّمُوهُمْ وَأَدِّبُوهُمْ »  
> *"Maknanya adalah: Ajarkanlah ilmu kepada mereka dan didiklah adab bagi mereka!"*  
> 📚 *(Diriwayatkan oleh Al-Hakim dalam Al-Mustadrak No. 3838, dinyatakan Shahih; Tafsir Ath-Thabari 23/491)*

---

## 4. Matriks Sinergi Tanggung Jawab Rumah Tangga

PKN menegaskan pembagian peran kepemimpinan keluarga yang harmonis:

| Dimensi Peran | Tanggung Jawab Utama Ayah (*Qowwam*) | Tanggung Jawab Utama Bunda (*Rahimah*) |
| :--- | :--- | :--- |
| **Visi & Arah** | Menentukan tujuan akhirat keluarga, memilih ekosistem belajar yang amanah. | Mengalirkan visi ayah ke dalam rutinitas keseharian anak di rumah. |
| **Nafkah & Kehalalan** | Memastikan sebutir beras yang masuk ke perut anak 100% halal tanpa syubhat. | Mengolah rezeki halal menjadi hidangan berkah penuh cinta dan doa. |
| **Hukum & Ketegasan** | Penegak aturan (*Bahasa Tangan*), benteng perlindungan aqidah keluarga. | Sumber kehangatan (*Bahasa Hati*), tempat anak mencurahkan keluh kesah. |
| **Evaluasi Karakter** | Memeriksa kematangan nalar dan kesiapan baligh anak secara berkala. | Mengamati detail perubahan perilaku anak dari hari ke hari (*Observasi 3A*). |

---

## 5. Tautan Konseptual Terkait
* [[Peran Ayah dan Bunda]] — Pembagian Mandat Qowwamah dan Rahimah.
* [[Peran Guru dan Lembaga Pendidikan]] — Posisi Sekolah sebagai Mitra Komplementer.
* [[Pendidikan Ideal]] — Paradigma Akil-Baligh Generasi Peradaban.
"""

# ==============================================================================
# 6. PERAN GURU DAN LEMBAGA PENDIDIKAN.MD
# ==============================================================================
ARTICLES["Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md"] = """---
title: "Peran Guru dan Lembaga Pendidikan"
tags:
  - pkn
  - peran_guru
  - lembaga_pendidikan
  - waratsatul_anbiya
  - kuttab
---

# Peran Guru & Lembaga Pendidikan: Pewaris Risalah & Mitra Fitrah Keluarga

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « إِنَّ الْعُلَمَاءَ وَرَثَةُ الْأَنْبِيَاءِ، وَإِنَّ الْأَنْبِيَاءَ لَمْ يُوَرِّثُوا دِينَارًا وَلَا دِرْهَمًا، وَإِنَّمَا وَرَّثُوا الْعِلْمَ، فَمَنْ أَخَذَهُ أَخَذَ بِحَظٍّ وَافِرٍ »
>
> *"Sesungguhnya para ulama (guru dan pendidik) adalah pewaris para nabi. Dan sesungguhnya para nabi tidak mewariskan dinar maupun dirham, melainkan mereka mewariskan ilmu. Maka barangsiapa mengambilnya, sungguh ia telah mengambil bagian keuntungan yang sangat besar."*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Abu Dawud No. 3641 & At-Tirmidzi No. 2682; Kitab Al-Ilm; Dishahihkan oleh Ibnu Hibban dan Al-Albani; Riyadush Shalihin No. 1388.  
> 💡 **Relevansi PKN:** Guru dan lembaga pendidikan dalam PKN memegang status mulia sebagai *Waratsatul Anbiya'* (Pewaris Risalah Kenabian). Mereka hadir bukan sebagai penjual jasa industri komersial, melainkan sebagai murabbi spiritual yang mendampingi dan menyuburkan fitrah unik setiap anak murid.

---

## 1. Hakikat Posisi Guru & Sekolah dalam Perspektif PKN

Dalam arsitektur Pendidikan Karakter Nabawiyah, **Lembaga Pendidikan (Sekolah/Kuttab/Pesantren) berposisi sebagai MITRA KOMPLEMENTER bagi orang tua, BUKAN pengganti fungsi keluarga**:
* **Menolak Korporatisasi Pendidikan:** Sekolah bukan pabrik pencetak nilai ujian dan guru bukan buruh pengajar yang sekadar mentransfer kurikulum demi gaji. Guru adalah *Mu'addib* (pembina adab) dan *Muslih* (perawat jiwa generasi).
* **Menjaga Sinergi Segitiga Emas:** Ekosistem pendidikan hanya akan berhasil melahirkan generasi mukallaf mandiri jika terjalin sinergi seirama antara: **Orang Tua di Rumah ↔ Guru di Sekolah ↔ Lingkungan Masyarakat Shalih**.
* **Menghindari Standarisasi Pembunuh Bakat:** Sekolah PKN menghargai keberagaman fadhilah anak; tidak memaksakan setiap murid memiliki peringkat ranking seragam, melainkan memfasilitasi 40 pilar karakter nabawiyah (TB40).

---

## 2. Teladan Rasulullah ﷺ sebagai Pendidik Teragung (Al-Mu'allim Al-Awwal)

Rasulullah ﷺ menetapkan standar tertinggi bagi siapa saja yang mengemban profesi pendidik:

### A. Wasiat Beliau kepada Mu'adz bin Jabal & Abu Musa Al-Asy'ari
Ketika Rasulullah ﷺ mengutus kedua sahabat agung ini menjadi pendidik dan da'i bagi penduduk Yaman, beliau membekali mereka dengan kaidah pedagogi emas:
> « يَسِّرَا وَلَا تُعَسِّرَا، وَبَشِّرَا وَلَا تُنَفِّرَا، وَتَطَاوَعَا وَلَا تَخْتَلِفَا »  
> *"Permudahlah dan jangan mempersulit, berikanlah kabar gembira dan jangan membuat orang lari menjauh, serta bersatu-padulah kalian berdua dan jangan saling berselisih!"*  
> 📚 *(HR. Al-Bukhari No. 3038 & Muslim No. 1733)*

Guru yang meneladani sunnah nabawiyah adalah sosok yang membuat ilmu terasa memikat dan mudah dipahami, bukan guru yang senang memamerkan kerumitan dan menakut-nakuti murid dengan ancaman nilai jelek.

### B. Memperhatikan Kondisi Psikologis Murid (Tidak Menjemukan)
Abdullah bin Mas'ud radhiyallahu 'anhu mengisahkan bagaimana Rasulullah ﷺ mengatur jadwal ta'lim:
> « كَانَ النَّبِيُّ ﷺ يَتَخَوَّلُنَا بِالْمَوْعِظَةِ فِي الأَيَّامِ، كَرَاهَةَ السَّآمَةِ عَلَيْنَا »  
> *"Adalah Nabi ﷺ senantiasa memilih-milih hari dan waktu yang tepat dalam memberikan nasihat kepada kami, karena beliau khawatir menimbulkan kebosanan pada diri kami."*  
> 📚 *(HR. Al-Bukhari No. 68 & Muslim No. 2821)*

Seorang guru muslim wajib memiliki kepekaan rasa: kapan murid sedang siap menyerap ilmu, dan kapan murid membutuhkan jeda istirahat untuk menyegarkan kembali jiwanya.

---

## 3. Keterangan Para Ulama Klasik tentang Adab Guru

### 1. Ibn Sahnun Al-Qayrawani (Wafat 256 H)
Dalam kitab *Adab al-Mu'allimin*—buku panduan guru pertama dalam sejarah peradaban Islam:
> *"Wajib bagi seorang guru di Kuttab untuk menyamakan perhatiannya kepada seluruh murid; tidak boleh mengutamakan anak orang kaya atas anak orang miskin. Wajib baginya meniatkan pengajarannya ikhlas karena Allah, bersikap sabar menghadapi kelemahan nalar murid, dan melarang keras murid-muridnya saling mengolok-olok atau menindas satu sama lain."*

### 2. Imam Abu Bakar Muhammad bin Al-Husain Al-Ajurri (Wafat 360 H)
Dalam kitab *Akhlaqul Ulama* (Hal. 45):
> *"Ketahuilah bahwa pendidik sejati bukanlah orang yang banyak bicaranya, melainkan orang yang keteladanan akhlaknya mendahului kata-katanya. Murid-murid akan meniru cara gurunya tersenyum, cara gurunya menahan amarah, dan cara gurunya bersujud jauh lebih cepat daripada hafalan bait-bait syair yang didiktekan kepadanya."*

---

## 4. Tiga Peran Pokok Guru dalam Ekosistem PKN

```mermaid
graph LR
    G["Peran Luhur Guru PKN"]
    G --> G1["1. Mu'addib (Penanam Adab Sebelum Ilmu)"]
    G --> G2["2. Rawi Fitrah (Fasilitator Penemu Bakat 3A)"]
    G --> G3["3. Qudwah Hayyah (Model Keteladanan Nyata)"]
```

1. **Sebagai Mu'addib (Penanam Adab Sebelum Ilmu):**
   * Memastikan murid menghormati ilmu, menghargai buku, menyayangi kawan, dan berbakti kepada orang tua sebelum mengajarkan rumus-rumus sains dan matematika.
2. **Sebagai Rawi Fitrah (Fasilitator Penemu Bakat 3A):**
   * Mengamati kecenderungan unik setiap anak melalui instrumen Rukun 3A (Suka, Bisa, Bermanfaat).
   * Melaporkan portofolio kekuatan karakter anak kepada orang tua secara berkala, bukan sekadar membagikan lembaran angka rapor kognitif.
3. **Sebagai Qudwah Hayyah (Cermin Hidup Keteladanan):**
   * Menjadi teladan integritas, kejujuran lisan (*Shidq*), kelemahlembutan (*Rifq*), dan ketepatan waktu shalat berjamaah.

---

## 5. Tautan Konseptual Terkait
* [[Tanggung Jawab Pendidikan]] — Mandat Fardhu 'Ain di Pundak Orang Tua.
* [[Pendidikan Ideal]] — Menautkan Akil dan Baligh Menuju Peradaban.
* [[4 Kaidah Implementasi]] — Prinsip Operasional Pengasuhan Nabawiyah.
* [[Metode Mendidik]] — Tiga Bahasa Pengasuhan Islam.
"""

def main():
    print("Memulai ekspansi 6 artikel Paradigma & Implementasi PKN...")
    for rel_path, content in ARTICLES.items():
        filepath = os.path.join(CONTENT_DIR, rel_path)
        with open(filepath, "w", encoding="utf-8") as fp:
            fp.write(content)
        chars = len(content)
        words = len(content.split())
        lines = len(content.splitlines())
        print(f"  [BERHASIL] {os.path.basename(rel_path):32s} -> {chars:,} karakter | {words:,} kata | {lines} baris")
    print("Semua 6 artikel Paradigma & Implementasi telah berhasil disimpan.")

if __name__ == "__main__":
    main()

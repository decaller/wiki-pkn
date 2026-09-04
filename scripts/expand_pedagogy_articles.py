#!/usr/bin/env python3
"""
scripts/expand_pedagogy_articles.py
Mengembangkan 8 artikel teori pendidikan dan metode PKN:
1. Metode Mendidik.md
2. Bahasa Hati.md
3. Bahasa Lisan.md
4. Bahasa Tangan.md
5. Thufulah.md
6. Tamyiz.md
7. Murahaqah.md
8. Syabab.md

Memasukkan secara komprehensif:
- Contoh nyata interaksi Rasulullah ﷺ dalam berdakwah dan mendidik para sahabat (dewasa maupun cilik).
- Keterangan dan syarah para ulama otoritatif (Ibnu Qayyim, Imam An-Nawawi, Imam Al-Ghazali, Ibn Sahnun, Ibnu Hajar).
- Teks dalil hadits Arab berharakat, terjemahan, dan takhrij OpenBayan.
- Analisis psikopedagogis Nabawiyah & panduan implementasi.
"""

import os

BASE_DIR = "/home/abuhafi/Project/wiki-pkn"
CONTENT_DIR = os.path.join(BASE_DIR, "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi")

ARTICLES = {}

# ==============================================================================
# 1. METODE MENDIDIK.MD
# ==============================================================================
ARTICLES["Pendidikan Ideal/Metode Mendidik.md"] = """---
title: "Metode Mendidik"
tags:
  - pkn
  - metode_mendidik
  - tiga_bahasa
  - tadarruj
  - manhaj_nabawi
---

# Metode Mendidik Nabawiyah: Tiga Bahasa Pengasuhan

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « ادْعُ إِلَىٰ سَبِيلِ رَبِّكَ بِالْحِكْمَةِ وَالْمَوْعِظَةِ الْحَسَنَةِ ۖ وَجَادِلْهُم بِالَّتِي هِيَ أَحْسَنُ »
>
> *"Serulah (manusia) kepada jalan Tuhanmu dengan hikmah (kebijaksanaan mendalam), pengajaran yang baik (mau'izhah hasanah), dan bantahlah mereka dengan cara yang terbaik (mujadalah bil-lati hiya ahsan)..."*
>
> 📚 **Sumber Rujukan OpenBayan:** QS. An-Nahl: 125; Tafsir Ibnu Katsir (Juz 4 Hal. 613); Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 2 Hal. 347).  
> 💡 **Relevansi PKN:** Ayat ini meletakkan tripartite metodologi pengasuhan Islam: *Al-Hikmah* (Bahasa Hati), *Al-Mau'izhah Al-Hasanah* (Bahasa Lisan), dan ketegasan beradab yang proporsional (*Bahasa Tangan*).

---

## 1. Hakikat Metodologi Pendidikan Karakter Nabawiyah

Metode mendidik dalam Pendidikan Karakter Nabawiyah (PKN) bukanlah sekumpulan teknik mekanistis atau rekayasa perilaku (*behavioral conditioning*) seperti dalam psikologi sekuler Barat. Metode Nabawiyah adalah **penyelarasan interaksi pendidik dengan hukum fitrah insani yang telah ditetapkan Allah SWT**. 

Inti dari metodologi ini bersandar pada kaidah agung **At-Tadarruj (Pentahapan Alami)**:
1. **Tidak Melompatkan Tahapan:** Setiap anak melewati etape pembentukan jiwa yang berurutan. Jiwa tidak dapat menerima beban fisik sebelum akalnya paham, dan akal tidak akan menerima pemahaman sebelum hatinya terpaut cinta.
2. **Kesesuaian Instrumen Bahasa:** Menyampaikan nasihat lisan kepada anak usia 2 tahun yang menangis adalah inefisiensi, sebagaimana memukul anak usia 6 tahun karena belum shalat adalah kezaliman yang diharamkan syariat.
3. **Pendidik sebagai Mu'alliman Muyassiran (Pendidik yang Memudahkan):** Rasulullah ﷺ menegaskan misi pengutusannya: *"Sesungguhnya Allah tidak mengutusku sebagai orang yang kaku dan mempersulit, melainkan sebagai pendidik yang memudahkan."* (HR. Muslim No. 1478).

---

## 2. Arsitektur Piramida Tiga Bahasa Pengasuhan

PKN merumuskan instrumen komunikasi pendidikan ke dalam **Tiga Bahasa Nabawiyah** yang diterapkan secara hierarkis:

```mermaid
graph TD
    subgraph Piramida["Piramida Tiga Bahasa Pengasuhan PKN"]
        BT["Puncak: BAHASA TANGAN<br>Usia 10+ Tahun (Fase Murahaqah & Syabab)<br>Disiplin Amal & Penegakan Konsekuensi"]
        BL["Tengah: BAHASA LISAN<br>Usia 7 - 10 Tahun (Fase Tamyiz)<br>Disiplin Ilmu & Dialog Nalar Sebab-Akibat"]
        BH["Pondasi: BAHASA HATI<br>Usia 0 - 7 Tahun (Fase Thufulah)<br>Disiplin Iman & Keteladanan Cinta Tanpa Syarat"]
    end
    BH --> BL --> BT
```

### Matriks Komparasi Tiga Bahasa Pendidikan:
| Aspek Pembeda | [[Bahasa Hati]] | [[Bahasa Lisan]] | [[Bahasa Tangan]] |
| :--- | :--- | :--- | :--- |
| **Fase Usia Dominan** | 0 – 7 Tahun (*Thufulah*) | 7 – 10 Tahun (*Tamyiz*) | 10 Tahun ke atas (*Murahaqah*) |
| **Dimensi Jiwa** | Hati / Rasa (*Al-Qalb* / Muthmainnah) | Akal / Cipta (*Al-'Aql* / Lawwamah) | Fisik / Karsa (*Al-Jasad* / Ammarah) |
| **Karakter Sasaran** | Fitrah Iman (*Mahabbah*) | Fitrah Belajar (*Nalar & Adab*) | Fitrah Bakat (*Tanggung Jawab Amal*) |
| **Bentuk Aksi** | Pelukan, tatapan kasih, teladan visual | Dialog dua arah, tanya jawab, kisah | Penugasan, sanksi tegas, konsekuensi |
| **Toleransi Kesalahan**| Paling Longgar (Dimaafkan penuh) | Menengah (Diberi tahu & dibimbing) | Ketat (Tuntutan tuntas sebelum baligh) |

---

## 3. Teladan Interaksi Dakwah & Tarbiyah Rasulullah ﷺ

Keagungan metode mendidik Rasulullah ﷺ terbukti dari bagaimana beliau memperlakukan para shahabatnya sesuai dengan kesiapan kondisi kejiwaan masing-masing:

### A. Kisah Mu'awiyah bin Al-Hakam As-Sulami: Mendidik Tanpa Menghardik
Ketika Mu'awiyah bin Al-Hakam berbicara di dalam shalat karena mendoakan orang yang bersin, para shahabat memukul paha mereka untuk memperingatkannya. Mu'awiyah merasa tertekan dan ketakutan. Namun perhatikan bagaimana Rasulullah ﷺ memperlakukannya seusai shalat:
> « فَبِأَبِي هُوَ وَأُمِّي، مَا رَأَيْتُ مُعَلِّمًا قَبْلَهُ وَلَا بَعْدَهُ أَحْسَنَ تَعْلِيمًا مِنْهُ، فَوَاللَّهِ مَا كَهَرَنِي، وَلَا ضَرَبَنِي، وَلَا شَتَمَنِي، قَالَ: إِنَّ هَذِهِ الصَّلَاةَ لَا يَصْلُحُ فِيهَا شَيْءٌ مِنْ كَلَامِ النَّاسِ، إِنَّمَا هُوَ التَّسْبِيحُ وَالتَّكْبِيرُ وَقِرَاءَةُ الْقُرْآنِ »  
> *"Demi ayah dan ibuku sebagai tebusannya, aku belum pernah melihat seorang pendidik pun sebelum maupun sesudahnya yang lebih baik cara mendidiknya daripada Rasulullah ﷺ! Demi Allah, beliau tidak membentakku, tidak memukulku, dan tidak mencelaku. Beliau hanya bersabda: 'Sesungguhnya shalat ini tidak boleh ada di dalamnya perkataan manusia biasa; shalat itu hanyalah tasbih, takbir, dan membaca Al-Qur'an.'"*  
> 📚 *(HR. Muslim No. 537, Kitab Al-Masajid wa Mawadhi' Ash-Shalah)*

### B. Kisah Pemuda yang Meminta Izin Berzina: Dialog Mengikis Syahwat
Seorang pemuda mendatangi majelis Nabi ﷺ dengan lancang meminta izin berzina. Para shahabat marah dan hendak memukulnya. Namun Rasulullah ﷺ menahannya dan menerapkan tiga bahasa sekaligus:
1. **Bahasa Hati:** Memanggilnya mendekat (*"Udnih"*), memintanya duduk tepat di hadapan beliau, dan meletakkan tangan mulia beliau di dada pemuda tersebut.
2. **Bahasa Lisan:** Mengajak nalar pemuda itu berdialog: *"Apakah engkau suka jika perzinaan itu terjadi pada ibumu?... putrimu?... saudara perempuanmu?"* Pemuda itu menjawab: *"Demi Allah tidak, wahai Rasulullah!"* Nabi menjawab: *"Demikian pula orang lain tidak menyukainya bagi keluarga mereka."*
3. **Doa Penyucian Jiwa:** Rasulullah ﷺ berdoa: *"Ya Allah, ampunilah dosanya, bersihkanlah hatinya, dan bentengilah kemaluannya!"* Pemuda itu keluar dari majelis sebagai orang yang paling membenci zina seumur hidupnya (HR. Ahmad No. 22211, sanad shahih).

---

## 4. Keterangan & Fatwa Para Ulama Otoritatif

Para ulama salaf dan khalaf telah merumuskan kaidah emas dalam metode mendidik Islam:

### 1. Imam Ibnu Qayyim Al-Jauziyyah (Wafat 751 H)
Dalam kitab monumentalnya *Tuhfatul Maudud bi Ahkamil Maulud* (Hal. 229), beliau menegaskan bahaya kesalahan metode dan kelalaian orang tua:
> « وَكَمْ مِمَّنْ أَشْقَى وَلَدَهُ وَفِلْذَةَ كَبِدِهِ فِي الدُّنْيَا وَالْآخِرَةِ بِإِهْمَالِهِ وَتَرْكِ تَأْدِيبِهِ، وَإِعَانَتِهِ لَهُ عَلَى شَهَوَاتِهِ، وَيَزْعُمُ أَنَّهُ يُكْرِمُهُ وَقَدْ أَهَانَهُ، وَأَنَّهُ يَرْحَمُهُ وَقَدْ ظَلَمَهُ، فَفَاتَهُ انْتِفَاعُهُ بِوَلَدِهِ، وَفَوَّتَ عَلَيْهِ حَظَّهُ فِي الدُّنْيَا وَالْآخِرَةِ. وَإِذَا اعْتَبَرْتَ الْفَسَادَ فِي الْأَوْلَادِ رَأَيْتَ عَامَّتَهُ مِنْ قِبَلِ الْآبَاءِ! »  
> *"Betapa banyak orang yang mencelakakan anaknya—belahan jantungnya sendiri—di dunia dan akhirat karena kelalaiannya, tidak mendidiknya (*tarku ta'dibihi*), serta menuruti hawa nafsunya. Ia menyangka sedang memuliakan anaknya padahal ia sedang menghinakannya; ia mengira sedang menyayanginya padahal ia sedang menzaliminya!... Dan apabila engkau perhatikan kerusakan pada anak-anak, niscaya engkau akan mendapati mayoritasnya bersumber dari kelalaian para ayah!"*

### 2. Imam Al-Ghazali (Wafat 505 H)
Dalam kitab *Ihya' 'Ulumiddin* (Juz 3 Hal. 72), beliau menguraikan fitrah anak yang plastis dan pentingnya keteladanan visual:
> « الصَّبِيُّ أَمَانَةٌ عِنْدَ وَالِدَيْهِ، وَقَلْبُهُ الطَّاهِرُ جَوْهَرَةٌ نَفِيسَةٌ سَاذَجَةٌ خَالِيَةٌ عَنْ كُلِّ نَقْشٍ وَصُورَةٍ، وَهُوَ قَابِلٌ لِكُلِّ مَا نُقِشَ، وَمَائِلٌ إِلَى كُلِّ مَا يُمَالُ بِهِ إِلَيْهِ، فَإِنْ عُوِّدَ الْخَيْرَ وَعُلِّمَهُ نَشَأَ عَلَيْهِ وَسَعِدَ فِي الدُّنْيَا وَالْآخِرَةِ »  
> *"Anak kecil adalah amanah di sisi kedua orang tuanya. Hatinya yang suci laksana permata berharga yang masih polos, bersih dari segala ukiran dan gambar. Ia siap menerima setiap ukiran yang digoreskan dan cenderung kepada arah ke mana saja ia dipalingkan. Jika ia dibiasakan dengan kebaikan dan diajarkan kebajikan, niscaya ia akan tumbuh di atas kebaikan itu dan bahagia di dunia dan akhirat."*

### 3. Al-Qadhi Abu Bakar Ibn Al-Arabi Al-Maliki (Wafat 543 H)
Beliau mengingatkan agar tidak membebani nalar anak secara terburu-buru:
> *"Hendaklah anak tidak dibebani dengan logika abstrak sebelum adab keseharian dan keindahan Al-Qur'an meresap ke dalam sanubarinya, agar ilmu tidak menjadi beban yang dimusuhi oleh jiwanya."*

---

## 5. Bahaya Pelompatan Tahapan (Penyebab Luka Pengasuhan)

Dalam PKN, penyimpangan metodologis akan melahirkan **Hutang Pengasuhan (*Debt of Parenting*)** yang merusak fitrah:

1. **Bahasa Lisan Tanpa Bahasa Hati (Logika Kering Tanpa Cinta):**
   * *Gejala:* Anak dijejali hafalan, target skor akademis, dan doktrin dalil sejak balita tanpa kehangatan pelukan.
   * *Akibat Fatal:* Anak tumbuh cerdas secara hafalan namun memiliki jiwa yang gersang (*nifaq tersembunyi*). Saat beranjak remaja (*syabab*), ia rentan mengalami kegoncangan iman atau menjadi pembangkang intelektual.
2. **Bahasa Tangan Tanpa Bahasa Hati & Lisan (Kekerasan Fisik Otoriter):**
   * *Gejala:* Membentak, memukul, atau menghukum anak di usia dini (0–7 th) atau memukul tanpa terlebih dahulu memahamkan aturan di usia tamyiz.
   * *Akibat Fatal:* Menghancurkan fitrah kemuliaan anak (*'Izzah*), menumbuhkan sifat pengecut, pendendam, atau melahirkan generasi bermuka dua—taat saat di depan orang tua karena takut dihukum, namun berbuat maksiat liar saat di luar pengawasan.

---

## 6. Protokol Pemulihan (Recovery) Metodologis

Bila orang tua menyadari telah terjadi salah asuh (menggunakan bahasa tangan sebelum waktunya atau menelantarkan bahasa hati), lakukan **Langkah Restorasi Fitrah**:
1. **Turunkan Eskalasi ke Bahasa Hati (Re-Parenting):** Hentikan segala bentuk bentakan dan sanksi fisik. Mulai kembali dengan memeluk anak, meminta maaf atas kekhilafan orang tua di masa lalu, dan mendengarkan keluh kesahnya.
2. **Isi Penuh Tangki Cinta:** Luangkan *Quality Time* minimal 15–30 menit sehari tanpa gangguan gawai untuk bermain dan berdialog intim dengan anak.
3. **Longgarkan Toleransi Sambil Membina Nalar:** Berikan kelonggaran batas toleransi dalam perkara non-prinsipil seraya membangun kembali argumentasi nalar (*Bahasa Lisan*) secara sabar.

---

## 7. Tautan Konseptual Terkait
* [[Bahasa Hati]] — Fondasi Cinta dan Keteladanan Usia 0–7 Tahun.
* [[Bahasa Lisan]] — Seni Dialog Dua Arah Usia 7–10 Tahun.
* [[Bahasa Tangan]] — Batasan Syar'i Ketegasan Usia 10 Tahun ke Atas.
* [[Pendidikan Ideal]] — Paradigma Pendidikan Berbasis Ekosistem Nyata.
* [[Luka dan Hutang Pengasuhan]] — Diagnosis Kerusakan Jiwa Akibat Salah Asuh.
"""

# ==============================================================================
# 2. BAHASA HATI.MD
# ==============================================================================
ARTICLES["Pendidikan Ideal/Metode Mendidik/Bahasa Hati.md"] = """---
title: "Bahasa Hati"
tags:
  - pkn
  - bahasa_hati
  - mahabbah
  - thufulah
  - tangki_cinta
---

# Bahasa Hati: Seni Tarbiyah Bil-Qalb & Kelembutan Nabawiyah

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « إِنَّ الرِّفْقَ لَا يَكُونُ فِي شَيْءٍ إِلَّا زَانَهُ، وَلَا يُنْزَعُ مِنْ شَيْءٍ إِلَّا شَانَهُ »
>
> *"Sesungguhnya kelemahlembutan (ar-rifq) tidaklah berada pada sesuatu melainkan ia akan memperindahnya (menjadikannya mulia), dan tidaklah kelemahlembutan itu dicabut dari sesuatu melainkan pasti akan memperburuknya (menjadikannya hina)."*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Muslim No. 2594, Kitab Al-Birr wash-Shilah wal-Adab; Syarah Shahih Muslim Imam An-Nawawi (Juz 16 Hal. 146); Riyadush Shalihin Tahqiq Al-Fahl No. 633.  
> 💡 **Relevansi PKN:** Bahasa Hati adalah pondasi utama dari seluruh bangunan Pendidikan Karakter Nabawiyah. Tanpa getaran cinta batiniah dan kelembutan, seluruh doktrin syariat dan nasihat lisan akan memantul membentur benteng penolakan jiwa anak.

---

## 1. Hakikat Bahasa Hati dalam Arsitektur PKN

Dalam disiplin Pendidikan Karakter Nabawiyah, **Bahasa Hati (*Lughatul Qalb*)** adalah modalitas pengasuhan berbasis getaran rasa (*Al-Qalb* pada jiwa muthmainnah), keteladanan visual tanpa kata-kata (*lisanul hal*), sentuhan fisik penuh kasih, dan doa tulus di keheningan malam.

Bahasa Hati menjadi **instrumen utama pada Fase Thufulah (0–7 Tahun)**, namun tetap menjadi **ruh penyerta** pada seluruh fase usia berikutnya hingga dewasa. 

### Tiga Pilar Fondasi Bahasa Hati:
1. **Penerimaan Tanpa Syarat (*Unconditional Acceptance*):** Anak diyakinkan bahwa dirinya dicintai bukan karena prestasinya, bukan karena ranking kelasnya, melainkan karena ia adalah amanah suci yang dianugerahkan Allah SWT kepada orang tuanya.
2. **Keteladanan Nyata (*Qudwah Hasanah*):** Jiwa anak kecil belajar melalui pantulan cermin visual (*mirror neurons*). Sebelum anak mendengar perintah shalat, matanya harus terlebih dahulu terbiasa melihat punggung ayah dan bundanya bersujud khusyuk.
3. **Pengisian Penuh Tangki Cinta (*The Emotional Tank*):** Jiwa anak yang lapar cinta bagaikan bejana bocor; ia akan mencari pemenuhan cinta dari luar rumah melalui validasi semu media sosial, pergaulan bebas, atau kecanduan digital.

---

## 2. Teladan Kasih Sayang & Interaksi Tarbiyah Rasulullah ﷺ

Rasulullah ﷺ adalah suri teladan agung dalam memenangkan hati para sahabatnya melalui Bahasa Hati yang meluluhkan jiwa:

### A. Kisah Al-Aqra' bin Habis: Hati Kering yang Menolak Mencium Anak
Al-Bukhari meriwayatkan pemandangan agung di kota Madinah:
> « قَبَّلَ رَسُولُ اللَّهِ ﷺ الحَسَنَ بْنَ عَلِيٍّ وَعِنْدَهُ الأَقْرَعُ بْنُ حَابِسٍ التَّمِيمِيُّ جَالِسًا، فَقَالَ الأَقْرَعُ: إِنَّ لِي عَشَرَةً مِنَ الوَلَدِ مَا قَبَّلْتُ مِنْهُمْ أَحَدًا، فَنَظَرَ إِلَيْهِ رَسُولُ اللَّهِ ﷺ ثُمَّ قَالَ: مَنْ لاَ يَرْحَمُ لاَ يُرْحَمُ »  
> *"Rasulullah ﷺ mencium cucu beliau, Al-Hasan bin Ali, sementara di dekat beliau duduk Al-Aqra' bin Habis At-Tamimi. Al-Aqra' berkata dengan nada heran: 'Sesungguhnya aku memiliki sepuluh orang anak, namun tak seorang pun dari mereka yang pernah kucium!' Maka Rasulullah ﷺ memandangnya seraya bersabda: 'Barangsiapa tidak menyayangi, niscaya ia tidak akan disayangi!'"*  
> 📚 *(HR. Al-Bukhari No. 5997 & Muslim No. 2318)*

Dalam riwayat lain, seorang Arab Badui datang dan berkata: *"Apakah kalian menciumi anak-anak kecil kalian? Demi Allah kami tidak pernah mencium mereka!"* Maka Rasulullah ﷺ bersabda:
> « أَوَأَمْلِكُ لَكَ أَنْ نَزَعَ اللَّهُ مِنْ قَلْبِكَ الرَّحْمَةَ! »  
> *"Lalu apa dayaku jika Allah telah mencabut rasa kasih sayang dari dalam hatimu?!"* (HR. Al-Bukhari No. 5998).

### B. Menggandeng Tangan Mu'adz bin Jabal Sebelum Memberikan Nasihat
Perhatikan bagaimana Rasulullah ﷺ membuka pintu hati Mu'adz sebelum membisikkan doa wirid harian:
> « يَا مُعَاذُ، وَاللَّهِ إِنِّي لَأُحِبُّكَ، وَاللَّهِ إِنِّي لَأُحِبُّكَ، فَقَالَ: أُوصِيكَ يَا مُعَاذُ لَا تَدَعَنَّ فِي دُبُرِ كُلِّ صَلَاةٍ تَقُولُ: اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ، وَشُكْرِكَ، وَحُسْنِ عِبَادَتِكَ »  
> *"Wahai Mu'adz, demi Allah sesungguhnya aku benar-benar mencintaimu! Demi Allah sesungguhnya aku benar-benar mencintaimu! Lalu beliau bersabda: Aku wasiatkan kepadamu wahai Mu'adz, jangan sekali-kali engkau tinggalkan di setiap akhir shalatmu untuk membaca: 'Ya Allah, tolonglah aku untuk senantiasa mengingat-Mu, bersyukur kepada-Mu, dan memperbaiki ibadah kepada-Mu!'"*  
> 📚 *(HR. Abu Dawud No. 1522 & An-Nasa'i No. 1303, Shahih)*

Rasulullah ﷺ mengucapkan ikrar cinta dua kali berturut-turut, menggenggam jemari Mu'adz, mengisi tangki cintanya hingga meluap, barulah mengalirkan wasiat syariat. Wasiat ini terukir abadi di jiwa Mu'adz hingga akhir hayatnya.

### C. Anas bin Malik: Sepuluh Tahun dalam Naungan Bahasa Hati
Anas bin Malik radhiyallahu 'anhu mengisahkan pengalamannya melayani Rasulullah ﷺ sejak usia 10 tahun:
> « خَدَمْتُ رَسُولَ اللَّهِ ﷺ عَشْرَ سِنِينَ، فَمَا قَالَ لِي أُفٍّ قَطُّ، وَمَا قَالَ لِشَيْءٍ صَنَعْتُهُ: لِمَ صَنَعْتَهُ؟ وَلَا لِشَيْءٍ تَرَكْتُهُ: لِمَ تَرَكْتَهُ؟ »  
> *"Aku melayani Rasulullah ﷺ selama sepuluh tahun. Demi Allah, beliau tidak pernah sekalipun berkata kepadaku 'Ah/Cih!' dan beliau tidak pernah mencela perbuatanku: 'Mengapa engkau lakukan ini?' atau pada sesuatu yang kutinggalkan: 'Mengapa engkau tidak lakukan ini?'"*  
> 📚 *(HR. Al-Bukhari No. 6038 & Muslim No. 2309)*

---

## 3. Keterangan & Fatwa Para Ulama Rabbani

### 1. Syaikhul Islam Ibnu Qayyim Al-Jauziyyah
Dalam kitab *I'lamul Muwaqqi'in* (Juz 4 Hal. 157) dan *Tuhfatul Maudud*:
> *"Ketahuilah bahwa mendidik hati anak mendahului mendidik lisannya. Jika orang tua mampu menanamkan kecintaan kepada Allah di dalam hati anak melalui perlakuan kasih sayang, niscaya anak akan menjalankan syariat dengan kerinduan batin (*syauq*), bukan dengan keterpaksaan raga (*ikrah*)."*

### 2. Imam An-Nawawi dalam Syarah Shahih Muslim
Mengomentari hadits tentang mencium anak kecil:
> *"Hadits ini merupakan anjuran agung untuk mencium anak-anak kecil, membelai mereka, memangku mereka dengan penuh rahmah dan kelembutan. Sikap keras dan kaku terhadap anak kecil bukanlah tanda ketegasan wibawa, melainkan tanda kekeringan hati dari rahmat Allah."*

### 3. Ibn Sahnun Al-Qayrawani dalam Adab al-Mu'allimin
Beliau menetapkan bahwa seorang guru di Kuttab tidak boleh memulai pengajaran hafalan sebelum murid merasa aman dan nyaman:
> *"Pendidik wajib bersikap adil, sabar menghadapi anak-anak, dan tidak boleh menampakkan kebencian atau muka masam yang membuat hati murid lari dari ilmu."*

---

## 4. Lima Dialek Operasional Bahasa Hati dalam Pengasuhan Keluarga

Bagaimana orang tua membumikan Bahasa Hati setiap hari di rumah tangga? Terapkan **5 Dialek Bahasa Hati PKN**:

1. **Sentuhan Fisik Penuh Berkah (*Physical Touch*):**
   * Memeluk anak minimal 8 kali sehari (sebagaimana sunnah membelai kepala anak yatim dan mencium kening anak).
   * Memegang pundak anak saat berbicara, menatap matanya sejajar dengan ketinggian tubuhnya.
2. **Kata-Kata Afirmasi Iman (*Words of Affirmation*):**
   * Panggilan kesayangan Nabawiyah (seperti panggilan Rasulullah kepada Aisyah: *"Ya 'Aisy"* / *"Ya Humaira"*).
   * Memuji proses dan kesungguhan anak (*"Bunda bangga melihat abang berusaha keras merapikan buku"*), bukan memuji hasil semata.
3. **Waktu Berkualitas Tanpa Gawai (*Quality Time*):**
   * Menyediakan waktu khusus 20 menit sehari mendengarkan celoteh anak tanpa memegang ponsel.
   * Berjalan-jalan melihat ciptaan Allah di alam bebas sambil bercerita tentang kebesaran Allah.
4. **Pelayanan Kasih Sayang (*Acts of Service*):**
   * Menyiapkan makanan favorit anak dengan senyuman tulus.
   * Merawat anak saat sakit dengan membacakan doa ruqyah syar'iyyah seraya membelai keningnya.
5. **Hadiah Kejutan yang Mengikat Hati (*Receiving Gifts*):**
   * Memberikan hadiah kecil tanpa harus menunggu momen ranking sekolah (*"Ini hadiah untuk adik karena adik anak shalih kesayangan ayah"*).
   * Sabda Nabi ﷺ: *« تَهَادَوْا تَحَابُّوا »* (*"Saling memberilah hadiah, niscaya kalian akan saling mencintai!"* HR. Bukhari dalam Al-Adab Al-Mufrad No. 594).

---

## 5. Tanda-Tanda Anak yang Mengalami Kelaparan Bahasa Hati

Orang tua wajib waspada jika mendapati indikator patologis berikut pada diri anak:
* **Tantrum Kronis & Agresif:** Sering memukul adik, membanting mainan, atau berteriak mencari perhatian (*attention seeking*).
* **Minder & Takut Salah:** Tidak berani mencoba hal baru, gemetar saat diajak berbicara orang dewasa karena trauma bentakan masa lalu.
* **Kecanduan Gawai Parah:** Anak melarikan dahaga jiwanya ke dunia virtual karena layar gadget tidak pernah memarahi atau membentaknya.

### Solusi Kuratif Segera:
Hentikan perdebatan lisan. Ambil anak, dekap erat dalam pelukan hangat selama minimal 3 menit, bisikkan kalimat istighfar dan permohonan maaf, lalu penuhi kembali bejana hatinya dengan cinta ilahiah.

---

## 6. Tautan Konseptual Terkait
* [[Metode Mendidik]] — Arsitektur Induk Tiga Bahasa Pengasuhan.
* [[Bahasa Lisan]] — Tahap Lanjutan Pengajaran Nalar Usia 7–10 Tahun.
* [[Thufulah]] — Etape Emas Masa Bermain dan Kasih Sayang.
* [[Tangki Cinta]] — Mekanisme Psikospiritual Ketahanan Jiwa Anak.
"""

# ==============================================================================
# 3. BAHASA LISAN.MD
# ==============================================================================
ARTICLES["Pendidikan Ideal/Metode Mendidik/Bahasa Lisan.md"] = """---
title: "Bahasa Lisan"
tags:
  - pkn
  - bahasa_lisan
  - tamyiz
  - dialog_nabawi
  - qaulan_sadida
---

# Bahasa Lisan: Seni Dialog Dialogis & Pencerahan Nalar Nabawiyah

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ وَقُولُوا قَوْلًا سَدِيدًا ۝ يُصْلِحْ لَكُمْ أَعْمَالَكُمْ وَيَغْفِرْ لَكُمْ ذُنُوبَكُمْ »
>
> *"Wahai orang-orang yang beriman, bertakwalah kalian kepada Allah dan berkatalah dengan perkataan yang benar (sadida - tepat sasaran, objektif, dan lurus). Niscaya Allah akan memperbaiki amalan-amalan kalian dan mengampuni dosa-dosa kalian..."*
>
> 📚 **Sumber Rujukan OpenBayan:** QS. Al-Ahzab: 70–71; Tafsir Ibnu Katsir (Juz 6 Hal. 488); Riyadush Shalihin Tahqiq Al-Fahl No. 42.  
> 💡 **Relevansi PKN:** Bahasa Lisan Nabawiyah bukan omelan searah atau intimidasi verbal, melainkan tutur kata yang memenuhi kriteria *Qaulan Sadida* (jujur dan tepat), *Qaulan Layyina* (lemah lembut), dan *Qaulan Baligha* (mengena tepat ke relung nalar anak).

---

## 1. Hakikat Bahasa Lisan dalam Arsitektur PKN

Dalam disiplin Pendidikan Karakter Nabawiyah, **Bahasa Lisan (*Lughatul Lisan*)** adalah instrumen pengajaran utama pada **Fase Tamyiz (Usia 7–10 Tahun)**. Pada fase ini, anak mulai mengalami kematangan kognitif (*mumayyiz*): ia mulai mampu membedakan baik dan buruk, memahami hubungan sebab-akibat, serta memiliki rasa ingin tahu logis yang sangat besar.

Bahasa Lisan bertugas menumbuhkan **Fitrah Belajar (*Karakter Cipta/Akal*)** melalui metode dialogis dua arah (*Al-Hiwar*). 

### Perbedaan Bahasa Lisan Nabawiyah vs Omelan Konvensional:
| Parameter | Omelan & Doktrin Kaku | Bahasa Lisan Nabawiyah |
| :--- | :--- | :--- |
| **Arah Komunikasi** | Satu arah (monolog menghakimi) | Dua arah (dialog saling mendengarkan) |
| **Fokus Sasaran** | Menyalahkan anak & melampiaskan emosi | Mengoreksi perilaku & memahamkan hikmah |
| **Kondisi Jiwa Anak** | Tertekan, defensif, mencari pembenaran | Terbuka, merasa dihormati, menyadari kesalahan |
| **Dampak Jangka Panjang** | Anak menjadi ahli berbohong | Tumbuh integritas nalar dan kesadaran amal |

---

## 2. Teladan Dialog Dakwah & Tarbiyah Rasulullah ﷺ Bersama Para Sahabat Cilik

Rasulullah ﷺ memperlakukan anak-anak usia tamyiz sebagai mitra dialog yang berakal, bukan sebagai objek yang boleh dibentak seenaknya:

### A. Umar bin Abi Salamah: Koreksi Adab Makan Tanpa Mempermalukan
Umar bin Abi Salamah menceritakan kenangan masa kecilnya saat makan bersama Nabi ﷺ:
> « كُنْتُ غُلَامًا فِي حَجْرِ رَسُولِ اللَّهِ ﷺ، وَكَانَتْ يَدِي تَطِيشُ فِي الصَّحْفَةِ، فَقَالَ لِي رَسُولُ اللَّهِ ﷺ: يَا غُلَامُ، سَمِّ اللَّهَ، وَكُلْ بِيَمِينِكَ، وَكُلْ مِمَّا يَلِيكَ، فَمَا زَالَتْ تِلْكَ طِعْمَتِي بَعْدُ »  
> *"Dahulu aku adalah seorang bocah kecil di bawah asuhan Rasulullah ﷺ. Tanganku bergerak ke sana kemari di nampan makanan (mengambil lauk sembarangan). Maka Rasulullah ﷺ bersabda kepadaku dengan lembut: 'Wahai anakku (ghulam), bacalah bismillah, makanlah dengan tangan kananmu, dan makanlah dari apa yang ada di dekatmu!' Maka sejak saat itu, demikianlah selalu cara makanku."*  
> 📚 *(HR. Al-Bukhari No. 5376 & Muslim No. 2022)*

Perhatikan keindahan pedagogis Nabi ﷺ: beliau tidak membentak: *"Kamu tidak punya sopan santun!"*, melainkan menyapa hangat (*"Ya Ghulam"*), memberikan tiga kaidah ringkas dan jelas, sehingga anak langsung paham dan mengamalkannya seumur hidup.

### B. Abdullah bin Abbas: Pembinaan Aqidah di Atas Punggung Tunggangan
Saat Ibnu Abbas masih berusia sekitar 9–10 tahun dan dibonceng di belakang unta Rasulullah ﷺ, beliau memanfaatkan momen intim tersebut untuk menanamkan pondasi tauhid:
> « يَا غُلَامُ إِنِّي أُعَلِّمُكَ كَلِمَاتٍ: احْفَظِ اللَّهَ يَحْفَظْكَ، احْفَظِ اللَّهَ تَجِدْهُ تُجَاهَكَ، إِذَا سَأَلْتَ فَاسْأَلِ اللَّهَ، وَإِذَا اسْتَعَنْتَ فَاسْتَعِنْ بِاللَّهِ، وَاعْلَمْ أَنَّ الأُمَّةَ لَوْ اجْتَمَعَتْ عَلَى أَنْ يَنْفَعُوكَ بِشَيْءٍ لَمْ يَنْفَعُوكَ إِلَّا بِشَيْءٍ قَدْ كَتَبَهُ اللَّهُ لَكَ، وَلَوْ اجْتَمَعُوا عَلَى أَنْ يَضُرُّوكَ بِشَيْءٍ لَمْ يَضُرُّوكَ إِلَّا بِشَيْءٍ قَدْ كَتَبَهُ اللَّهُ عَلَيْكَ، رُفِعَتِ الأَقْلَامُ وَجَفَّتِ الصُّحُفُ »  
> *"Wahai anakku, sesungguhnya aku ingin mengajarkan kepadamu beberapa untaian kalimat: Jagalah (syariat) Allah niscaya Dia akan menjagamu! Jagalah Allah niscaya engkau mendapati-Nya di hadapanmu! Jika engkau memohon, mohonlah kepada Allah; dan jika engkau meminta pertolongan, mintalah pertolongan kepada Allah!... Ketahuilah bahwa pena-pena takdir telah diangkat dan lembaran-lembaran catatan telah kering."*  
> 📚 *(HR. At-Tirmidzi No. 2516, dinyatakan Hasan Shahih; Riyadush Shalihin No. 62)*

### C. Jundub bin Abdillah: Iman Sebelum Al-Qur'an Melalui Lisan
Jundub bin Abdillah Al-Bajali mengisahkan metodologi lisan para shahabat kecil bersama Nabi ﷺ:
> « كُنَّا مَعَ النَّبِيِّ ﷺ وَنَحْنُ فِتْيَانٌ حَزَاوِرَةٌ، فَتَعَلَّمْنَا الإِيمَانَ قَبْلَ أَنْ نَتَعَلَّمَ الْقُرْآنَ، ثُمَّ تَعَلَّمْنَا الْقُرْآنَ فَازْدَدْنَا بِهِ إِيمَانًا »  
> *"Dahulu kami bersama Nabi ﷺ saat kami adalah anak-anak muda yang menjelang baligh. Kami mempelajari iman terlebih dahulu sebelum kami mempelajari Al-Qur'an, barulah kemudian kami mempelajari Al-Qur'an, sehingga Al-Qur'an itu semakin menambah keimanan kami."*  
> 📚 *(HR. Ibnu Majah No. 61, sanad shahih; Al-Baihaqi dalam Sunan Al-Kubra No. 5373)*

---

## 3. Keterangan Para Ulama Otoritatif

### 1. Al-Hafizh Ibnu Hajar Al-Asqalani (Wafat 852 H)
Dalam kitab monumental *Fathul Bari Syarah Shahih Al-Bukhari* (Juz 9 Hal. 522), saat mensyarah hadits Umar bin Abi Salamah:
> *"Di dalam hadits ini terdapat pelajaran agung tentang etika mendidik anak kecil. Pendidik hendaknya menegur kekhilafan anak secara langsung dengan perkataan yang lembut (*bi luthfin*), tidak mencela kepribadiannya di hadapan orang lain, dan menyajikan alternatif tindakan yang benar secara ringkas dan mudah diingat."*

### 2. Imam Asy-Syathibi (Wafat 790 H)
Dalam kitab *Al-Muwafaqat fi Ushulisy Syari'ah*:
> *"Kalam syariat diturunkan sesuai dengan nalar pendengar (*'ala qadri 'uqulihim*). Maka seorang pendidik yang bijaksana tidak menyampaikan wacana hukum yang tinggi kepada anak tamyiz yang belum mampu memikulnya, agar kalam tersebut tidak menjadi fitnah bagi agamanya."*

### 3. Syaikh Abdullah Nashih 'Ulwan
Dalam *Tarbiyatul Aulad fil Islam* (Juz 2 Hal. 642):
> *"Metode dialog (*At-Tarbiyah bil-Hiwar*) adalah metode yang paling efektif mengikis keraguan syubhat dan menanamkan keyakinan aqidah di usia tamyiz, karena dialog melibatkan akal anak secara aktif dalam menemukan kebenaran."*

---

## 4. Kaidah Emas Berbahasa Lisan kepada Anak Tamyiz (7–10 Tahun)

Pendidik dan orang tua wajib menerapkan rumus komunikasi Nabawiyah berikut:

1. **Jelaskan Sebab dan Akibat (*Cause and Effect*):**
   * Jangan hanya katakan: *"Jangan main game malam-malam!"*
   * Gunakan Bahasa Lisan: *"Abang, kalau tidur larut malam, besok saat shalat shubuh akan mengantuk dan badan letih, sehingga abang tidak bisa konsentrasi belajar. Yuk kita istirahatkan tubuh kita sekarang."*
2. **Gunakan Pertanyaan Pemantik Nalar (*Socratic Method*):**
   * Ketika anak bertengkar memperebutkan mainan, tanyakan: *"Menurut abang, bagaimana perasaan adik saat mainannya direbut tiba-tiba? Bagaimana solusi yang adil agar kalian berdua bisa bermain gembira?"*
3. **Perintahkan Shalat Tanpa Hukuman Fisik:**
   * Sesuai hadits: *"Perintahkan anakmu shalat saat usia 7 tahun..."*
   * Di usia 7–10 tahun, tugas orang tua adalah **mengajak, mencontohkan, dan memahamkan rukun shalat**, bukan menghukum atau mencaci bila anak masih bolong-bolong. Waktu 3 tahun (7 ke 10 th = sekitar 5.000 waktu shalat) adalah masa pembiasaan lisan yang sangat panjang!

---

## 5. Bahaya Racun Lisan (*Verbal Abuse*) dalam Pengasuhan

Banyak orang tua merusak fitrah anak bukan dengan pukulan tangan, melainkan dengan **lidah yang beracun**:
* **Pelabelan Negatif (*Labeling*):** Memanggil anak dengan sebutan *"pemalas"*, *"bodoh"*, *"nakal"*, *"batu"*. Sabda Nabi ﷺ: *"Janganlah kalian mencela anak-anak kalian!"*
* **Sarkasme & Sindiran Tajam:** Merendahkan harga diri anak di depan saudara atau tamunya.
* **Membanding-bandingkan (*Social Comparison*):** *"Lihat tuh anak tetangga sudah hafal 5 juz, kamu main terus!"* Kalimat ini tidak memicu motivasi, melainkan menumbuhkan bibit hasad dan kebencian kepada kawan dan orang tua.

---

## 6. Tautan Konseptual Terkait
* [[Metode Mendidik]] — Arsitektur Induk Tiga Bahasa Nabawiyah.
* [[Bahasa Hati]] — Pondasi Cinta yang Menjiwai Setiap Kata.
* [[Bahasa Tangan]] — Batasan Ketegasan Fisik Menjelang Baligh.
* [[Tamyiz]] — Etape Perkembangan Nalar Kritis Usia 7–10 Tahun.
"""

# ==============================================================================
# 4. BAHASA TANGAN.MD
# ==============================================================================
ARTICLES["Pendidikan Ideal/Metode Mendidik/Bahasa Tangan.md"] = """---
title: "Bahasa Tangan"
tags:
  - pkn
  - bahasa_tangan
  - murahaqah
  - ta'dib
  - disiplin_positif
---

# Bahasa Tangan: Batasan Syar'i Ketegasan & Ta'dib Nabawiyah

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « مُرُوا أَوْلَادَكُمْ بِالصَّلَاةِ وَهُمْ أَبْنَاءُ سَبْعِ سِنِينَ، وَاضْرِبُوهُمْ عَلَيْهَا وَهُمْ أَبْنَاءُ عَشْرِ سِنِينَ، وَفَرِّقُوا بَيْنَهُمْ فِي الْمَضَاجِعِ »
>
> *"Perintahkanlah anak-anak kalian untuk mengerjakan shalat ketika mereka berusia tujuh tahun, dan pukullah mereka (dengan pukulan mendidik jika meninggalkan shalat) ketika mereka berusia sepuluh tahun, serta pisahkanlah tempat tidur mereka!"*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Abu Dawud No. 495 & Ahmad (Juz 2 Hal. 187); Dinyatakan Shahih oleh Syaikh Al-Albani dalam *Shahih Sunan Abi Dawud*; Syarah As-Sunnah Imam Al-Baghawi (Juz 2 Hal. 407).  
> 💡 **Relevansi PKN:** Hadits ini adalah payung hukum syar'i peletakan *Bahasa Tangan* (*At-Ta'dib*). Sanksi fisik hanya dilegalkan pada usia 10 tahun (fase Murahaqah) setelah melewati 3 tahun penuh pembinaan Bahasa Hati dan Bahasa Lisan (sekitar 5.000 kali ajakan shalat tanpa kekerasan).

---

## 1. Hakikat Bahasa Tangan dalam Arsitektur PKN

Dalam disiplin Pendidikan Karakter Nabawiyah, **Bahasa Tangan (*Lughatul Yad / At-Ta'dib*)** adalah instrumen penegakan aturan (*enforcement*), ketegasan disiplin, dan penetapan konsekuensi nyata.

Bahasa Tangan **baru diizinkan penggunaannya pada anak usia 10 tahun ke atas (Fase Murahaqah)** saat anak mulai mendekati pintu taklif baligh. Tujuannya adalah mendisiplinkan **Fitrah Bakat & Tanggung Jawab Fisik (*Dimensi Karsa / Jasad*)** agar anak siap memikul konsekuensi hukum syariat (*mukallaf*) secara mandiri.

> [!CAUTION] Peringatan Keras Syariat
> Menghukum fisik atau memukul anak di bawah usia 10 tahun (fase Thufulah dan awal Tamyiz) adalah **penyimpangan metode dan kezaliman yang diharamkan para ulama**, karena melompati tahapan fitrah yang telah digariskan Rasulullah ﷺ.

---

## 2. Empat Syarat Syar'i Mutlak Penggunaan Bahasa Tangan

Para fukaha dan ulama tarbiyah menetapkan **4 Syarat Ketat** yang tidak boleh dilanggar dalam menjatuhkan sanksi fisik:

```mermaid
graph TD
    BT["Syarat Syar'i Bahasa Tangan"]
    BT --> S1["1. Usia Minimal 10 Tahun & Didahului 3 Tahun Nasihat"]
    BT --> S2["2. Motivasi Rahmah Bukan Luapan Amarah (Ghadhab)"]
    BT --> S3["3. Pukulan Simbolis (Ghairu Mubarrih) & Haram di Wajah"]
    BT --> S4["4. Bersifat Personal Tanpa Mempermalukan Publik"]
```

### 1. Telah Melewati Fase Bahasa Hati (0–7 th) & Lisan (7–10 th)
Sanksi pukulan di usia 10 tahun adalah hak syariat yang sah hanya jika orang tua telah tuntas mengisi tangki cinta anak selama 7 tahun pertama dan telah konsisten mengajak shalat dengan lisan santun selama 3 tahun penuh (usia 7–10 tahun). Jika orang tua tidak pernah mengajari shalat di usia 7 tahun lalu tiba-tiba memukul di usia 10 tahun, maka orang tualah yang berdosa.

### 2. Dilarang Memukul Saat Marah
Rasulullah ﷺ melarang seorang hakim memutuskan perkara saat marah, demikian pula orang tua/pendidik diharamkan mengeksekusi sanksi fisik saat darah mendidih oleh emosi. Sanksi harus dijatuhkan dalam keadaan tenang dengan niat menyelamatkan anak dari adzab akhirat.

### 3. Pukulan Tidak Melukai (*Dharbun Ghairu Mubarrih*) & Haram Menyentuh Wajah
> « إِذَا ضَرَبَ أَحَدُكُمْ فَلْيَجْتَنِبِ الْوَجْهَ »  
> *"Jika salah seorang di antara kalian terpaksa memukul, maka jauhilah memukul wajah!"*  
> 📚 *(HR. Al-Bukhari No. 2559 & Muslim No. 2612)*
Pukulan ta'dib adalah pukulan simbolis ketegasan (misal menggunakan siwak atau kibasan kain pada betis/pantat), tidak boleh mematahkan tulang, tidak meninggalkan lebam merah apalagi luka berdarah, dan diharamkan keras mengenai kepala, wajah, dada, atau kemaluan.

### 4. Tidak Menghukum Secara Kolektif
Hukuman harus bersifat personal kepada anak yang melanggar. Menghukum satu kelas atau seluruh anak di rumah karena kesalahan satu orang adalah bentuk kezaliman (*zhulm*) yang menimbulkan trauma kebencian pada anak-anak yang tidak bersalah.

---

## 3. Teladan Ketegasan & Keadilan Rasulullah ﷺ

### A. Seleksi Ketat Pasukan Uhud: Ketegasan Berbasis Kematangan Fisik
Ketika para pemuda usia 14–15 tahun seperti Rafi' bin Khadij, Samurah bin Jundub, dan Usamah bin Zaid ingin ikut berperang di Uhud, Rasulullah ﷺ tidak berkompromi dalam hal kesiapan taklif. Beliau memeriksa barisan mereka secara langsung:
* Beliau menolak pemuda yang belum genap baligh demi keselamatan mereka.
* Ketika Rafi' bin Khadij diizinkan karena kepandaiannya memanah, Samurah bin Jundub menangis seraya berkata: *"Wahai Rasulullah, engkau mengizinkan Rafi' padahal aku bisa membantingnya dalam gulat!"* Maka Rasulullah ﷺ menyuruh keduanya bergulat di depan beliau. Ketika Samurah berhasil membanting Rafi', beliau pun mengizinkan keduanya ikut (HR. Ath-Thabrani dalam *Al-Kabir* No. 6710; *Fathul Bari* 7/394).
Ketegasan Rasulullah ﷺ adalah ketegasan yang objektif, memberi ruang unjuk kompetensi, bukan kesewenang-wenangan.

### B. Penolakan Syafa'at dalam Hukum Had: Usamah bin Zaid & Wanita Makhzumiyah
Ketika wanita bangsawan dari Bani Makhzum mencuri, para shahabat meminta Usamah bin Zaid (anak kesayangan Rasulullah ﷺ) untuk meminta keringanan hukuman kepada Nabi ﷺ. Perhatikan reaksi tegas Rasulullah ﷺ:
> « أَتَشْفَعُ فِي حَدٍّ مِنْ حُدُودِ اللَّهِ؟! ثُمَّ قَامَ فَاخْتَطَبَ فَقَالَ: إِنَّمَا أَهْلَكَ الَّذِينَ قَبْلَكُمْ أَنَّهُمْ كَانُوا إِذَا سَرَقَ فِيهِمُ الشَّرِيفُ تَرَكُوهُ، وَإِذَا سَرَقَ فِيهِمُ الضَّعِيفُ أَقَامُوا عَلَيْهِ الحَدَّ، وَايْمُ اللَّهِ! لَوْ أَنَّ فَاطِمَةَ بِنْتَ مُحَمَّدٍ سَرَقَتْ لَقَطَعْتُ يَدَهَا »  
> *"Apakah engkau hendak meminta syafa'at (keringanan) dalam penegakan salah satu hukum batas dari batas-batas Allah?! Kemudian beliau berdiri berkhutbah dan bersabda: Sesungguhnya yang membinasakan umat-umat sebelum kalian adalah apabila ada orang terpandang mencuri mereka membiarkannya, namun jika orang lemah mencuri mereka menegakkan hukuman atasnya! Demi Allah, andai Fathimah putri Muhammad mencuri, niscaya aku sendiri yang akan memotong tangannya!"*  
> 📚 *(HR. Al-Bukhari No. 3475 & Muslim No. 1688)*

Ketegasan Bahasa Tangan harus tegak di atas asas keadilan tanpa pandang bulu, bahkan kepada anak kandung sendiri.

---

## 4. Fatwa & Keterangan Para Ulama Otoritatif

### 1. Ibn Sahnun Al-Qayrawani (Wafat 256 H)
Dalam kitab *Adab al-Mu'allimin*—kitab rujukan pedagogi Islam tertua di dunia:
> *"Seorang guru tidak boleh memukul murid lebih dari tiga kali pukulan ringan dalam urusan adab. Jika pelanggaran berkaitan dengan Al-Qur'an dan shalat pada anak usia 10 tahun, maksimal pukulan tidak boleh melebihi sepuluh kali, dan wajib menggunakan alat pemukul yang tidak melukai kulit dan tidak meninggalkan bekas memar."*

### 2. Imam Al-Qabisi (Wafat 403 H)
Dalam kitab *Ar-Risalah Al-Mufashshalah li Ahwal Al-Mu'allimin*:
> *"Hukuman fisik adalah obat terakhir (*ad-dawa'ul akhir*). Apabila pendidik masih bisa mendisiplinkan dengan pandangan mata yang tegas, teguran lisan, atau pembatasan hak main, maka haram baginya beralih ke hukuman fisik."*

### 3. Imam Ibnu Qayyim Al-Jauziyyah
Dalam *Zadul Ma'ad fi Hadyi Khairil 'Ibad* (Juz 4 Hal. 98):
> *"Pukulan yang diizinkan syariat adalah pukulan rahmat dan ta'dib, sebagaimana ayah memukul anaknya yang tergelincir atau dokter membedah bisul yang bernanah; tujuannya menyembuhkan bukan membinasakan."*

---

## 5. Instrumen Konsekuensi Non-Fisik dalam Bahasa Tangan

Bahasa Tangan dalam dunia modern tidak harus selalu bermakna pukulan fisik. Para pendidik PKN merekomendasikan **Hierarki Konsekuensi Tegas Beradab**:

1. **Pemberian Tugas Tambahan Berkelanjutan:**
   * Anak yang melalaikan tugas merapikan rumah diberikan kewajiban membersihkan halaman atau fasilitas masjid.
2. **Pencabutan Hak Sementara (*Deprivation of Privileges*):**
   * Membatasi waktu bermain di luar rumah, menunda pembelian barang yang diinginkan, atau menyita gawai selama sepekan.
3. **Konsekuensi Pemulihan Kerusakan (*Restitusi*):**
   * Jika anak merusak barang milik orang lain atau melukai hati saudaranya, ia wajib memperbaiki barang tersebut dengan uang sakunya sendiri dan mendatangi korban untuk meminta maaf secara langsung.

---

## 6. Tautan Konseptual Terkait
* [[Metode Mendidik]] — Peta Lengkap Tiga Bahasa Pengasuhan.
* [[Murahaqah]] — Etape Usia 10–15 Tahun dan Batas Taklif Baligh.
* [[Batas Toleransi]] — Kapan Toleransi Diberikan dan Kapan Ketegasan Ditegakkan.
* [[Disiplin Positif PKN]] — Arsip Induk Pedoman Disiplin Nabawiyah.
"""

def main():
    print("Memulai ekspansi 4 artikel Metode Mendidik...")
    for rel_path, content in ARTICLES.items():
        filepath = os.path.join(CONTENT_DIR, rel_path)
        with open(filepath, "w", encoding="utf-8") as fp:
            fp.write(content)
        chars = len(content)
        words = len(content.split())
        lines = len(content.splitlines())
        print(f"  [BERHASIL] {os.path.basename(rel_path):22s} -> {chars:,} karakter | {words:,} kata | {lines} baris")
    print("Semua 4 artikel Metode Mendidik telah berhasil disimpan.")

if __name__ == "__main__":
    main()

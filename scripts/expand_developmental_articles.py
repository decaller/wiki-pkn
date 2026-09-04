#!/usr/bin/env python3
"""
scripts/expand_developmental_articles.py
Mengembangkan 4 artikel Fase Perkembangan Usia Nabawiyah:
1. Thufulah.md (0–7 Tahun)
2. Tamyiz.md (7–10 Tahun)
3. Murahaqah.md (10–15 Tahun)
4. Syabab.md (15+ Tahun)

Memasukkan:
- Rangkaian interaksi tarbiyah Rasulullah ﷺ dengan para sahabat di tiap rentang usia.
- Keterangan dan syarah para ulama (Ibnu Qayyim, Ibnu Hajar, An-Nawawi, Al-Ghazali, Ibnu Taimiyyah).
- Teks dalil hadits Arab berharakat, terjemahan, dan takhrij OpenBayan.
- Matriks hak vs kewajiban anak, milestone perkembangan, dan pencegahan luka pengasuhan.
"""

import os

BASE_DIR = "/home/abuhafi/Project/wiki-pkn"
PERKEMBANGAN_DIR = os.path.join(BASE_DIR, "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan")

ARTICLES = {}

# ==============================================================================
# 1. THUFULAH.MD
# ==============================================================================
ARTICLES["Thufulah.md"] = """---
title: "Thufulah"
tags:
  - pkn
  - perkembangan
  - thufulah
  - usia_dini
  - bahasa_hati
  - mahabbah
---

# Fase Thufulah (0 – 7 Tahun): Etape Raja, Bermain, & Limpahan Kasih Sayang

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « قَبَّلَ رَسُولُ اللَّهِ ﷺ الْحَسَنَ بْنَ عَلِيٍّ وَعِنْدَهُ الأَقْرَعُ بْنُ حَابِسٍ التَّمِيمِيُّ جَالِسًا، فَقَالَ الأَقْرَعُ: إِنَّ لِي عَشَرَةً مِنَ الْوَلَدِ مَا قَبَّلْتُ مِنْهُمْ أَحَدًا، فَنَظَرَ إِلَيْهِ رَسُولُ اللَّهِ ﷺ ثُمَّ قَالَ: مَنْ لَا يَرْحَمُ لَا يُرْحَمُ »
>
> *"Rasulullah ﷺ mencium cucu beliau Al-Hasan bin Ali sementara di dekat beliau duduk Al-Aqra' bin Habis At-Tamimi. Al-Aqra' berkata dengan heran: 'Sesungguhnya aku memiliki sepuluh orang anak, namun tak seorang pun dari mereka yang pernah kucium!' Maka Rasulullah ﷺ memandangnya seraya bersabda: 'Barangsiapa tidak menyayangi, niscaya ia tidak akan disayangi!'"*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Al-Bukhari No. 5997 & Muslim No. 2318; Kitab Al-Adab; Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 3 Hal. 106).  
> 💡 **Relevansi PKN:** Fase Thufulah (0–7 tahun) adalah masa emas pemenuhan tangki cinta (*Mahabbah*). Pada fase ini, anak diperlakukan laksana "Raja" yang dilayani, dipeluk, dan dibiarkan bermain merdeka tanpa beban kewajiban syariat kaku atau ancaman hukuman fisik.

---

## 1. Hakikat Fase Thufulah dalam Arsitektur PKN

Fase Thufulah adalah masa pertumbuhan fisik dan sensori-motorik di mana fitrah keimanan anak berada pada kondisi paling murni. Dalam peribahasa hikmah kearifan Islam para salaf disebutkan:
> *"Ajaklah anakmu bermain pada 7 tahun pertama (Thufulah), didiklah ia adab dan aturan pada 7 tahun kedua (Tamyiz), bersahabatlah dengannya pada 7 tahun ketiga (Murahaqah), dan setelah itu lepaskanlah ia memikul urusannya sendiri (Syabab)."*

### Karakteristik Kunci Fase Thufulah:
1. **Egosentrisme Alami:** Anak usia dini memandang dunia berpusat pada dirinya. Sikap belum mau berbagi mainan atau menangis saat keinginannya tertunda bukanlah tanda "anak nakal", melainkan keniscayaan perkembangan jiwa yang sedang membangun rasa aman (*trust vs mistrust*).
2. **Belajar Melalui Peniruan Visual (*Mirroring*):** Akal anak belum mampu mencerna dalil abstrak. Ia merekam jutaan informasi melalui apa yang dilihatnya dari perangai ayah dan bundanya (*Bahasa Hati*).
3. **Batas Toleransi Paling Longgar:** Kesalahan anak di usia 0–7 tahun tidak dicatat sebagai dosa oleh malaikat, sehingga orang tua wajib memberikan pemaafan seluas-luasnya dan tidak menjatuhkan vonis hukuman.

---

## 2. Teladan Interaksi Pengasuhan Rasulullah ﷺ Bersama Anak Usia Dini

Sirah Nabawiyah menyajikan lukisan terindah tentang bagaimana sebaik-baik manusia memperlakukan anak-anak kecil dengan kelembutan yang tiada tara:

### A. Memperpanjang Sujud demi Cucu yang Menunggangi Punggung Beliau
Abdullah bin Syaddad meriwayatkan dari ayahnya tentang shalat jamaah yang diimami oleh Rasulullah ﷺ:
> « خَرَجَ عَلَيْنَا رَسُولُ اللَّهِ ﷺ فِي إِحْدَى صَلَاتَيِ الْعَشِيِّ وَهُوَ حَامِلٌ حَسَنًا أَوْ حُسَيْنًا، فَتَقَدَّمَ رَسُولُ اللَّهِ ﷺ فَوَضَعَهُ، ثُمَّ كَبَّرَ لِلصَّلَاةِ فَصَلَّى، فَسَجَدَ بَيْنَ ظَهْرَانَيْ صَلَاتِهِ سَجْدَةً أَطَالَهَا... فَلَمَّا قَضَى رَسُولُ اللَّهِ ﷺ الصَّلَاةَ قَالَ النَّاسُ: يَا رَسُولَ اللَّهِ، إِنَّكَ سَجَدْتَ بَيْنَ ظَهْرَانَيْ صَلَاتِكَ سَجْدَةً أَطَلْتَهَا حَتَّى ظَنَنَّا أَنَّهُ قَدْ حَدَثَ أَمْرٌ أَوْ أَنَّهُ يُوحَى إِلَيْكَ! قَالَ: كُلُّ ذَلِكَ لَمْ يَكُنْ، وَلَكِنَّ ابْنِي ارْتَحَلَنِي فَكَرِهْتُ أَنْ أُعَجِّلَهُ حَتَّى يَقْضِيَ حَاجَتَهُ »  
> *"Rasulullah ﷺ keluar mengimami kami dalam salah satu shalat petang (Zuhur atau Ashar) sambil menggendong Al-Hasan atau Al-Husain. Beliau maju ke depan lalu meletakkannya, kemudian bertakbir memulai shalat. Di tengah-tengah shalatnya, beliau sujud dengan sujud yang sangat panjang!... Ketika shalat telah usai, para sahabat bertanya: 'Wahai Rasulullah, sesungguhnya engkau bersujud sangat lama hingga kami mengira telah terjadi sesuatu atau wahyu sedang turun kepadamu!' Beliau bersabda: 'Semua itu tidak terjadi, akan tetapi cucuku ini tadi menunggangi punggungku, maka aku tidak suka membuatnya tergesa-gesa sampai ia menuntaskan keinginannya bermain!'"*  
> 📚 *(HR. An-Nasa'i No. 1141 & Ahmad No. 16033, dinyatakan Shahih oleh Al-Albani)*

### B. Menggendong Umamah binti Zainab dalam Shalat Fardhu
Abu Qatadah Al-Anshari meriwayatkan:
> « رَأَيْتُ النَّبِيَّ ﷺ يَؤُمُّ النَّاسَ وَأُمَامَةُ بِنْتُ أَبِي العَاصِ عَلَى عَاتِقِهِ، فَإِذَا رَكَعَ وَضَعَهَا، وَإِذَا رَفَعَ مِنْ السُّجُودِ أَعَادَهَا »  
> *"Aku melihat Nabi ﷺ mengimami shalat bersama orang-orang sementara Umamah binti Abi Al-'Ash berada di atas pundak beliau. Jika beliau ruku' beliau meletakkannya, dan jika beliau bangkit dari sujud beliau menggendongnya kembali."*  
> 📚 *(HR. Al-Bukhari No. 516 & Muslim No. 543)*

Beliau tidak mengurung anak kecil di rumah demi kekhusyukan sepihak, melainkan menghadirkan kehangatan masjid yang ramah anak.

### C. Menghibur Anak Kecil yang Kehilangan Burung Pipit (Abu 'Umair)
Anas bin Malik menceritakan kelembutan Nabi ﷺ saat menyapa adik kecilnya:
> « كَانَ النَّبِيُّ ﷺ أَحْسَنَ النَّاسِ خُلُقًا، وَكَانَ لِي أَخٌ يُقَالُ لَهُ أَبُو عُمَيْرٍ، كَانَ إِذَا جَاءَ قَالَ: يَا أَبَا عُمَيْرٍ، مَا فَعَلَ النُّغَيْرُ؟ »  
> *"Nabi ﷺ adalah manusia yang paling mulia akhlaknya. Aku memiliki seorang adik kecil yang biasa dipanggil Abu 'Umair. Jika Nabi datang, beliau menyapa bercanda: 'Wahai Abu 'Umair, ada apa dengan burung kecilmu (an-nughair)?'"*  
> 📚 *(HR. Al-Bukhari No. 6129 & Muslim No. 2150)*

Nabi agung pemimpin umat meluangkan waktu berjongkok menghibur duka seorang bocah cilik yang burung peliharaannya mati!

---

## 3. Keterangan & Fatwa Para Ulama Otoritatif

### 1. Imam Ibnu Qayyim Al-Jauziyyah
Dalam *Tuhfatul Maudud bi Ahkamil Maulud* (Hal. 241):
> *"Ketahuilah bahwa masa kanak-kanak awal adalah masa pertumbuhan jasmani dan peneguhan fitrah. Memaksa anak usia dini untuk belajar membaca, menghafal secara kaku, atau membebaninya dengan aturan orang dewasa akan mematikan keceriaan jiwanya, menumpulkan akalnya, dan membuatnya benci terhadap majelis ilmu di masa dewasa."*

### 2. Al-Hafizh Ibnu Hajar Al-Asqalani
Dalam *Fathul Bari* (Juz 10 Hal. 584), saat mengomentari hadits Abu 'Umair:
> *"Di dalam hadits ini terkandung puluhan faidah fiqih dan tarbiyah, di antaranya: kebolehan anak kecil bermain dengan burung mubah, anjuran merendahkan diri (*tawadhu'*) bagi para ulama dan pemimpin terhadap anak kecil, menggunakan nama kunyah bagi anak kecil untuk memuliakannya, serta menghibur hati anak yang sedang bersedih."*

### 3. Imam An-Nawawi
Dalam *Syarah Shahih Muslim* (Juz 15 Hal. 76):
> *"Hadits menggendong Umamah saat shalat menunjukkan betapa agungnya rahmah Rasulullah ﷺ kepada anak-anak, dan menjadi dalil bahwa menyayangi dan membawa anak kecil dalam ibadah tidak membatalkan shalat."*

---

## 4. Matriks Hak Pokok Anak vs Pantangan Mutlak Usia 0–7 Tahun

| Hak Pokok Anak Usia Thufulah | Pantangan Mutlak Orang Tua / Pendidik |
| :--- | :--- |
| **1. Hak Bermain Merdeka:** Eksplorasi sensori-motorik (air, tanah, pasir, balok) tanpa ketakutan dimarahi kotor. | **Dilarang Hukuman Fisik & Bentakan:** Mengharamkan pukulan, cubitan, atau kurungan gelap yang menimbulkan trauma saraf. |
| **2. Hak Limpahan Tangki Cinta:** Pelukan, ciuman, belaian kening, dan kata-kata lembut setiap hari. | **Dilarang Target Akademis Memaksa:** Memaksa calistung dini atau menuntut hafalan Al-Qur'an dengan intimidasi. |
| **3. Hak Penuntasan Egosentris:** Diterima emosinya saat menangis/kecewa tanpa dilabeli "cengeng" atau "nakal". | **Dilarang Membanding-bandingkan:** Mengadu kehebatan anak dengan saudara atau anak tetangga. |
| **4. Hak Melihat Keteladanan:** Menikmati suasana rumah yang tenang, harmonis, dan penuh adab islami. | **Dilarang Bertengkar di Depan Anak:** Keributan pasutri di depan balita meruntuhkan rasa aman batinnya. |

---

## 5. Indikator Keberhasilan Fase Thufulah (Checklist Kesiapan Masuk Tamyiz)

Saat anak menginjak usia 7 tahun, pastikan ia memiliki modalitas batiniah berikut:
1. **Mencintai Allah dan Rasul-Nya secara Alamiah:** Wajahnya ceria saat mendengar adzan, suka menirukan gerakan shalat orang tuanya secara sukarela.
2. **Merasa Aman Bersama Orang Tua:** Tidak takut berbicara jujur, selalu mencari perlindungan kepada ayah bundanya saat menghadapi masalah di luar rumah.
3. **Mata Bersinar & Penuh Rasa Ingin Tahu:** Aktif mengeksplorasi lingkungan dan siap menyambut fase belajar nalar di usia Tamyiz.

---

## 6. Tautan Konseptual Terkait
* [[Perkembangan]] — Peta Holistik 4 Tahapan Usia Nabawiyah.
* [[Bahasa Hati]] — Seni Komunikasi Utama Usia 0–7 Tahun.
* [[Tamyiz]] — Etape Berikutnya: Usia 7–10 Tahun.
* [[Tangki Cinta]] — Mekanisme Psikospiritual Ketahanan Diri Anak.
"""

# ==============================================================================
# 2. TAMYIZ.MD
# ==============================================================================
ARTICLES["Tamyiz.md"] = """---
title: "Tamyiz"
tags:
  - pkn
  - perkembangan
  - tamyiz
  - bahasa_lisan
  - fitrah_belajar
---

# Fase Tamyiz (7 – 10 Tahun): Etape Pembantu, Adab, & Pencerahan Nalar

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « مُرُوا أَوْلَادَكُمْ بِالصَّلَاةِ وَهُمْ أَبْنَاءُ سَبْعِ سِنِينَ »
>
> *"Perintahkanlah anak-anak kalian untuk mengerjakan shalat ketika mereka telah berusia tujuh tahun!"*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Abu Dawud No. 495 & Ahmad; Dishahihkan oleh Imam An-Nawawi dalam *Al-Majmu'* (Juz 3 Hal. 11) dan Al-Albani; Syarah Sunan Abi Dawud Ibnu Ruslan (Juz 3 Hal. 351).  
> 💡 **Relevansi PKN:** Usia 7 tahun adalah garis demarkasi fitrah (*Milestone Tamyiz*). Pada fase ini anak mulai diajak memahami aturan syariat melalui *Bahasa Lisan*, dilatih adab berkhidmah laksana "Pembantu" di rumah, dan dibiasakan shalat tanpa ancaman pukulan selama 3 tahun penuh (sekitar 5.000 waktu shalat).

---

## 1. Hakikat Fase Tamyiz dalam Arsitektur PKN

Secara etimologi, **Tamyiz (التَّمْيِيْز)** bermakna kemampuan memilah dan membedakan. Pada usia 7–10 tahun, anak bertransformasi dari masa egosentris balita (*Thufulah*) menuju masa **kemandirian nalar awal**:
* **Kemampuan Kognitif Operasional Konkret:** Anak mulai memahami hubungan sebab-akibat, membedakan mana hak miliknya dan mana hak orang lain, serta memahami konsep pahala dan adab.
* **Fitrah Belajar Mengembang (*Karakter Cipta/Akal*):** Rasa ingin tahunya bergeser dari sekadar melihat objek fisik menuju pencarian alasan di balik aturan: *"Mengapa kita harus wudhu?", "Mengapa babi haram?"*.
* **Status "Pelayan / Pembantu Rumah Tangga" (*Al-Khadim*):** Anak dilatih melayani keluarga—merapikan kasur sendiri, mencuci piring makannya, membantu menyapu lantai, membawakan belanjaan ibu—untuk mengikis bibit kesombongan dan menanamkan kemandirian.

---

## 2. Teladan Interaksi Pengasuhan Rasulullah ﷺ di Usia Tamyiz

Rasulullah ﷺ membimbing para sahabat cilik usia tamyiz dengan dialog cerdas, penugasan yang bermartabat, dan doa yang penuh berkah:

### A. Abdullah bin Abbas: Pembinaan Aqidah & Doa Kefakihan Ilmu
Ibnu Abbas menceritakan bagaimana beliau berkhidmat menyiapkan wudhu bagi Rasulullah ﷺ saat bermalam di rumah bibinya, Maimunah radhiyallahu 'anha:
> « وَضَعْتُ لِلنَّبِيِّ ﷺ وَضُوءًا، فَقَالَ: مَنْ وَضَعَ هَذَا؟ فَأُخْبِرَ، فَقَالَ: اللَّهُمَّ فَقِّهْهُ فِي الدِّينِ، وَعَلِّمْهُ التَّأْوِيلَ »  
> *"Aku meletakkan air wudhu untuk Nabi ﷺ. Beliau bertanya: 'Siapa yang meletakkan air ini?' Lalu diberitahukan kepada beliau bahwa Ibnu Abbas yang menyiapkannya. Maka beliau berdoa: 'Ya Allah, fahamkanlah dia dalam urusan agama dan ajarkanlah kepadanya ilmu takwil (tafsir Al-Qur'an)!'"*  
> 📚 *(HR. Al-Bukhari No. 143 & Muslim No. 2477)*

Perhatikan: inisiatif khidmah anak usia tamyiz diapresiasi dengan doa keilmuan yang melahirkan sosok *Turjumanul Qur'an* (Pakar Tafsir Umat).

### B. Menanamkan Adab Makan: Umar bin Abi Salamah
Saat tangan Umar kecil menyambar makanan sembarangan di nampan bersama, Rasulullah ﷺ tidak mempermalukannya di depan orang lain, melainkan membimbingnya dengan 3 kaidah emas lisan:
> « يَا غُلَامُ، سَمِّ اللَّهَ، وَكُلْ بِيَمِينِكَ، وَكُلْ مِمَّا يَلِيكَ »  
> *"Wahai anakku, sebutlah nama Allah (bismillah), makanlah dengan tangan kananmu, dan makanlah dari hidangan yang berada di dekatmu!"*  
> 📚 *(HR. Al-Bukhari No. 5376 & Muslim No. 2022)*

### C. Melatih Menjaga Rahasia: Anas bin Malik
Anas menceritakan bagaimana Nabi ﷺ memberikan misi rahasia kepadanya saat usia tamyiz:
> « أَتَى عَلَيَّ رَسُولُ اللَّهِ ﷺ وَأَنَا أَلْعَبُ مَعَ الغِلْمَانِ، فَسَلَّمَ عَلَيْنَا، فَبَعَثَنِي فِي حَاجَةٍ، فَأَبْطَأْتُ عَلَى أُمِّي، فَلَمَّا جِئْتُ قَالَتْ: مَا حَبَسَكَ؟ قُلْتُ: بَعَثَنِي رَسُولُ اللَّهِ ﷺ لِحَاجَةٍ، قَالَتْ: مَا حَاجَتُهُ؟ قُلْتُ: إِنَّهَا سِرٌّ، قَالَتْ: لَا تُخْبِرَنَّ بِسِرِّ رَسُولِ اللَّهِ ﷺ أَحَدًا »  
> *"Rasulullah ﷺ mendatangiku saat aku sedang bermain bersama anak-anak sebaya. Beliau mengucapkan salam kepada kami, lalu mengutusku untuk suatu keperluan. Maka aku terlambat pulang ke rumah ibuku. Ketika aku tiba, ibuku (Ummu Sulaim) bertanya: 'Apa yang membuatmu terlambat?' Aku menjawab: 'Rasulullah ﷺ mengutusku untuk suatu keperluan.' Ibuku bertanya: 'Apa keperluannya?' Aku berkata: 'Itu rahasia!' Maka ibuku berkata: 'Bagus, jangan sekali-kali engkau bocorkan rahasia Rasulullah ﷺ kepada siapapun!'"*  
> 📚 *(HR. Muslim No. 2482, Kitab Fadha'il Ash-Shahabah)*

Pendidikan keluarga salaf bersinergi melatih integritas dan amanah sejak usia tamyiz.

---

## 3. Keterangan & Fatwa Para Ulama Otoritatif

### 1. Imam Al-Ghazali dalam Ihya' 'Ulumiddin
Menjelaskan pentingnya menanamkan rasa malu dan adab di usia 7 tahun:
> *"Tanda pertama terbitnya akal tamyiz adalah munculnya rasa malu (*hayaa'*). Apabila anak mulai menampakkan rasa malu dan menahan diri dari sebagian perbuatan, itu adalah kabar gembira bahwa cahaya akalnya telah memancar. Maka jangan sekali-kali orang tua menyepelekan momen ini; mulailah mengajarkannya adab makan, adab berpakaian, adab berbicara, dan membiasakannya shalat."*

### 2. Imam Taqiyuddin As-Subki
Dalam fatwanya mengenai perintah shalat di usia 7 tahun:
> *"Perintah Nabi ﷺ untuk memerintahkan shalat di usia 7 tahun bukanlah beban taklif hukum syar'i, melainkan bentuk latihan (*tamrin*) dan pengenalan adab ibadah. Oleh karena itu, para ulama sepakat anak usia 7 tahun belum boleh dipukul jika meninggalkannya, agar shalat tidak dirasakan sebagai beban siksaan raga."*

---

## 4. Kurikulum Pendidikan Etape Tamyiz (7–10 Tahun)

PKN membagi fokus kurikulum Tamyiz ke dalam **4 Pilar Pembinaan**:

1. **Pembiasaan Shalat Tanpa Hukuman:**
   * Target: Mengenal syarat sah, rukun wudhu, bacaan shalat, dan gerakan tertib.
   * Strategi: Berikan apresiasi saat ia ikut shalat berjamaah; ingatkan dengan lembut saat ia terlupa tanpa memvonisnya berdosa.
2. **Pendidikan Adab Sosial & Aurat:**
   * Memisahkan tempat tidur anak laki-laki dan perempuan saat mendekati usia 10 tahun.
   * Melatih adab meminta izin (*isti'dzan*) di tiga waktu privasi orang tua (sebelum subuh, siang hari, dan setelah isya - QS. An-Nur: 58).
3. **Kemandirian Tugas Domestik (Peran Khadim):**
   * Merapikan pakaian sendiri, mencuci piring makan sendiri, menjaga kebersihan meja belajar.
4. **Pengenalan Konsep Kepemilikan & Keadilan:**
   * Memahamkan hak milik: tidak boleh mengambil uang kembalian tanpa izin, tidak boleh meminjam barang teman tanpa ridha pemiliknya.

---

## 5. Tautan Konseptual Terkait
* [[Perkembangan]] — Matriks 4 Etape Usia Nabawiyah.
* [[Bahasa Lisan]] — Metode Komunikasi Dialogis Usia Tamyiz.
* [[Murahaqah]] — Etape Berikutnya: Usia 10–15 Tahun Menuju Baligh.
* [[Belajar]] — Konsep Fitrah Belajar Alami Anak.
"""

# ==============================================================================
# 3. MURAHAQAH.MD
# ==============================================================================
ARTICLES["Murahaqah.md"] = """---
title: "Murahaqah"
tags:
  - pkn
  - perkembangan
  - murahaqah
  - baligh
  - bahasa_tangan
  - taklif
---

# Fase Murahaqah (10 – 15 Tahun): Etape Menteri, Tanggung Jawab, & Ambang Taklif

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « وَاضْرِبُوهُمْ عَلَيْهَا وَهُمْ أَبْنَاءُ عَشْرٍ، وَفَرِّقُوا بَيْنَهُمْ فِي الْمَضَاجِعِ »
>
> *"Dan pukullah mereka (dengan pukulan mendidik jika meninggalkan shalat) ketika mereka telah berusia sepuluh tahun, serta pisahkanlah tempat tidur di antara mereka!"*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Abu Dawud No. 495 & Ahmad; Syarah Shahih Muslim Imam An-Nawawi; Dinyatakan Shahih oleh para imam hadits.  
> 💡 **Relevansi PKN:** Usia 10 tahun ke atas adalah pintu gerbang *Murahaqah* (menjelang baligh). Anak tidak lagi diperlakukan sebagai anak kecil yang dimanjakan, melainkan diposisikan sebagai "Menteri / Mitra Tanggung Jawab" yang diajak bermusyawarah, ditegaskan batas aturan dengan *Bahasa Tangan*, dan digembleng kesiapan memikul beban syariat (*taklif*).

---

## 1. Hakikat Fase Murahaqah vs Mitos "Adolescence" Modern

Dalam peradaban Barat sekuler, usia 10–18 tahun dikonstruksikan sebagai masa "Adolescence / Remaja"—masa yang dimaklumi untuk labil, memberontak, mencari jati diri liar, dan bebas dari tanggung jawab kedewasaan.

**Islam membantah mitos remaja labil tersebut!** Dalam khazanah Nabawiyah, tidak ada konsep masa remaja yang permisif. Yang ada adalah:
1. **Fase Murahaqah (المُرَاهَقَة):** Berasal dari kata *rahaqa* yang berarti "mendekati"—yaitu fase anak mendekati kematangan akal dan fisik baligh.
2. **Kesiapan Menjadi Mukallaf:** Begitu tanda-tanda baligh muncul (mimpi basah / haidh / genap 15 tahun), pena pencatat amal malaikat langsung aktif. Detik itu juga, anak sah menjadi **orang dewasa penuh (*baligh 'aqil*)** yang menanggung hisab surga dan neraka secara mandiri!
3. **Peran sebagai Menteri (*Al-Wazir*):** Orang tua memperlakukan anak sebagai menteri pendamping: dilibatkan dalam urusan keluarga, dipercaya memegang proyek nyata, dan dimintai pertanggungjawaban atas tugasnya.

---

## 2. Teladan Tarbiyah Rasulullah ﷺ Menggembleng Pemuda Murahaqah

Rasulullah ﷺ tidak pernah memandang remeh kapasitas pemuda usia 10–15 tahun. Beliau menantang mereka dengan amanah peradaban:

### A. Seleksi Ketat Kesiapan Tempur: Samurah bin Jundub & Rafi' bin Khadij
Ketika Perang Uhud berkecamuk, anak-anak muda usia 14–15 tahun berbondong-bondong mendaftarkan diri:
> *"Nabi ﷺ memeriksa barisan anak muda. Beliau menolak mereka yang belum baligh demi keselamatan jiwa mereka. Ketika Rafi' bin Khadij diizinkan karena ia mahir memanah jitu, Samurah bin Jundub menangis seraya berkata kepada ayah tirinya: 'Rasulullah mengizinkan Rafi' dan menolakku, padahal jika aku bergulat dengan Rafi', aku bisa membantingnya!' Kabar ini sampai kepada Nabi ﷺ, maka beliau memanggil keduanya dan bersabda: 'Bergulatlah kalian berdua di depanku!' Samurah pun membanting Rafi', lalu Rasulullah ﷺ mengizinkan keduanya ikut dalam barisan pasukan Uhud!"*  
> 📚 *(HR. Ath-Thabrani dalam Al-Kabir No. 6710; Fathul Bari karya Ibnu Hajar 7/394)*

Nabi ﷺ menghargai gairah kejantanan pemuda dan menguji kompetensi fisik nyata secara objektif.

### B. Abdullah bin Umar: Menghafal & Menguji Batas Baligh Syar'i
Ibnu Umar menceritakan penetapan hukum batas baligh:
> « عُرِضْتُ عَلَى رَسُولِ اللَّهِ ﷺ يَوْمَ أُحُدٍ وَأَنَا ابْنُ أَرْبَعَ عَشْرَةَ سَنَةً فَلَمْ يُجِزْنِي، وَعُرِضْتُ عَلَيْهِ يَوْمَ الخَنْدَقِ وَأَنَا ابْنُ خَمْسَ عَشْرَةَ سَنَةً فَأَجَازَنِي »  
> *"Aku diajukan kepada Rasulullah ﷺ pada Perang Uhud saat aku berusia 14 tahun, dan beliau tidak mengizinkanku berperang. Lalu aku diajukan kepada beliau pada Perang Khandaq saat aku berusia 15 tahun, maka beliau mengizinkanku."*  
> 📚 *(HR. Al-Bukhari No. 2664 & Muslim No. 1868)*

Imam Nafi' menceritakan bahwa ketika Umar bin Abdul Aziz mendengar riwayat ini saat menjabat Khalifah, beliau langsung menetapkan: *"Inilah batas pemisah antara anak kecil dan orang dewasa!"* Lalu beliau menulis instruksi kepada seluruh gubernurnya untuk membagikan tunjangan mujahid bagi pemuda yang mencapai usia 15 tahun.

### C. Dua Pemuda Penumbang Abu Jahal di Perang Badar
Abdurrahman bin Auf mengisahkan pemuda belia Mu'adz bin 'Amr (14 tahun) dan Mu'awwidz bin 'Afra' yang berdiri di sampingnya saat Perang Badar:
> *"Salah seorang dari mereka berbisik kepadaku: 'Wahai paman, tunjukkan kepadaku mana yang bernama Abu Jahal!' Aku bertanya: 'Wahai keponakanku, apa urusanmu dengannya?' Ia menjawab: 'Aku mendengar bahwa dia selalu mencaci maki Rasulullah ﷺ. Demi Dzat yang jiwaku berada di tangan-Nya, jika mataku melihatnya, niscaya pandanganku tidak akan lepas darinya sampai salah satu di antara kita mati terlebih dahulu!'"* Keduanya menyerbu bagaikan elang dan berhasil menumbangkan Abu Jahal! *(HR. Al-Bukhari No. 3988).*

---

## 3. Keterangan Para Ulama Otoritatif

### 1. Al-Hafizh Ibnu Hajar Al-Asqalani dalam Fathul Bari
Saat mensyarah hadits Ibnu Umar:
> *"Hadits ini merupakan dalil ijma' mayoritas ulama (Madzhab Syafi'i, Maliki, Hanbali) bahwa usia 15 tahun qamariyah adalah batas maksimal baligh secara usia bila tanda biologis (ihtilam/haidh) belum tampak. Pada saat itu seluruh beban taklif syariat berlaku secara penuh tanpa ada keringanan lagi."*

### 2. Imam Ibnu Qayyim Al-Jauziyyah
Dalam *Zadul Ma'ad* dan *Madarijus Salikin*:
> *"Kewajiban memisahkan tempat tidur di usia 10 tahun adalah tindakan preventif syariat (*saddudz-dzari'ah*) untuk membentengi naluri biologis anak yang mulai bergolak. Di usia ini, dorongan kejantanan (*ar-rujulah*) harus dialirkan pada olahraga memanah, menunggang kuda, dan memikul tanggung jawab nafkah, bukan dibiarkan larut dalam angan-angan hampa."*

---

## 4. Tiga Tugas Kritis Pengasuhan Fase Murahaqah (10–15 Tahun)

1. **Penegakan Disiplin Ibadah & Bahasa Tangan:**
   * Di usia 10 tahun, shalat 5 waktu tidak boleh ditinggalkan. Konsekuensi tegas dan pengawasan ketat diberlakukan agar tidak ada hutang shalat saat tiba waktu baligh.
2. **Pemisahan Kamar & Pendidikan Thaharah Baligh:**
   * Memisahkan tempat tidur secara mutlak antara anak laki-laki dan perempuan.
   * Mengajarkan tata cara mandi junub, tanda-tanda baligh, dan hukum-hukum thaharah secara gamblang tanpa rasa tabu yang keliru.
3. **Penyaluran Fitrah Bakat ke Karya Nyata:**
   * Mengikutsertakan anak dalam magang kerja nyata, proyek pertukangan, kepanitiaan dakwah, atau perniagaan mandiri.

---

## 5. Tautan Konseptual Terkait
* [[Perkembangan]] — Garis Waktu Perkembangan Karakter Nabawiyah.
* [[Bahasa Tangan]] — Panduan Teknis Sanksi Mendidik Usia 10+ Tahun.
* [[Syabab]] — Gerbang Kedewasaan Penuh Usia 15+ Tahun.
* [[Bakat]] — Penjurusan Potensi Amal Menjelang Baligh.
"""

# ==============================================================================
# 4. SYABAB.MD
# ==============================================================================
ARTICLES["Syabab.md"] = """---
title: "Syabab"
tags:
  - pkn
  - perkembangan
  - syabab
  - mukallaf
  - kemandirian
  - kepemimpinan
---

# Fase Syabab (15+ Tahun / Pasca-Baligh): Etape Sahabat, Mukallaf Mandiri, & Pencetak Peradaban

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « سَبْعَةٌ يُظِلُّهُمُ اللَّهُ فِي ظِلِّهِ يَوْمَ لَا ظِلَّ إِلَّا ظِلُّهُ: ... وَشَابٌّ نَشَأَ فِي عِبَادَةِ رَبِّهِ »
>
> *"Tujuh golongan yang akan dinaungi oleh Allah di bawah naungan 'Arsy-Nya pada hari kiamat di mana tiada naungan selain naungan-Nya: ... dan seorang Pemuda (Syabbun) yang tumbuh besar dalam beribadah kepada Rabbnya..."*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Al-Bukhari No. 660 & Muslim No. 1031; Kitab Al-Adzan & Kitab Az-Zakah; Syarah Shahih Muslim Imam An-Nawawi (Juz 7 Hal. 120).  
> 💡 **Relevansi PKN:** Fase Syabab adalah etape kemandirian mukallaf penuh. Hubungan orang tua dan anak bertransformasi menjadi "Sahabat Seperjuangan". Pemuda muslim tidak lagi menjadi beban tanggungan keluarga, melainkan menjadi penopang dakwah, penggerak ekonomi halal, dan benteng peradaban umat.

---

## 1. Hakikat Fase Syabab dalam Arsitektur PKN

Begitu seorang anak mengalami tanda baligh (mimpi basah bagi laki-laki, haidh bagi perempuan, atau genap usia 15 tahun), status hukumnya dalam syariat Islam berubah secara radikal:
* **Beralih dari 'Ashab (Keluarga) ke Mukallaf Mandiri:** Setiap detik catatan amalnya dipertanggungjawabkan sendiri di hadapan Allah SWT.
* **Transformasi Relasi Menjadi "Sahabat" (*Al-Mushahabah*):** Orang tua tidak lagi mendikte dengan instruksi sepihak, melainkan menjadi penasihat bijak, kawan diskusi, dan mitra dalam memperjuangkan misi dakwah.
* **Tuntutan Tiga Kemandirian Nabawiyah:**
  1. **Kemandirian Aqidah & Ibadah:** Shalat, puasa, dan penjagaan kehormatan ditegakkan atas dasar muraqabatullah batin, bukan karena takut diawasi orang tua.
  2. **Kemandirian Finansial (*Iffah Nafkah*):** Mampu berwirausaha atau bekerja mencari nafkah halal sehingga tidak menjadi beban parasit bagi orang tua.
  3. **Kemandirian Sosial & Peradaban:** Mampu berkontribusi memecahkan masalah umat dan siap membangun mahligai rumah tangga sakinah.

---

## 2. Teladan Kepemimpinan Para Pemuda (Syabab) di Zaman Rasulullah ﷺ

Sejarah peradaban Islam ditopang di atas pundak para pemuda usia belasan tahun yang diamanahi tugas-tugas raksasa kenegaraan:

### A. Mush'ab bin Umair: Duta Diplomatik Peradaban di Usia Muda
Rasulullah ﷺ memilih Mush'ab bin Umair (pemuda berusia awal 20-an) untuk memegang misi paling strategis: menjadi duta diplomatik pertama Islam ke Yatsrib (Madinah). Dengan kefasihan lisan, keanggunan adab, dan keteguhan iman, Mush'ab berhasil mengislamkan para pemimpin suku besar Aus dan Khazraj (seperti Sa'ad bin Mu'adz dan Usaid bin Hudhair), hingga tidak ada satu rumah pun di Madinah melainkan telah dimasuki cahaya Islam sebelum Nabi ﷺ hijrah!

### B. Usamah bin Zaid: Panglima Perang Melawan Imperium Romawi di Usia 18 Tahun
Menjelang wafatnya Rasulullah ﷺ, beliau menunjuk Usamah bin Zaid—pemuda berusia 18 tahun—menjadi Panglima Tertinggi pasukan ekspedisi Syam untuk menghadapi superpower militer Romawi. Pasukan yang dipimpin Usamah beranggotakan para sahabat agung senior seperti Abu Bakar Ash-Shiddiq, Umar bin Al-Khattab, dan Sa'ad bin Abi Waqqash! Ketika sebagian orang meragukan usianya, Rasulullah ﷺ bersabda dengan tegas:
> « إِنْ تَطْعَنُوا فِي إِمَارَتِهِ فَقَدْ كُنْتُمْ تَطْعَنُونَ فِي إِمَارَةِ أَبِيهِ مِنْ قَبْلِهِ، وَايْمُ اللَّهِ إِنْ كَانَ لَخَلِيقًا لِلْإِمَارَةِ، وَإِنْ كَانَ لَمِنْ أَحَبِّ النَّاسِ إِلَيَّ بَعْدَهُ »  
> *"Jika kalian mencela kepemimpinannya, sungguh kalian dahulu telah mencela kepemimpinan ayahnya (Zaid bin Haritsah). Demi Allah, sungguh ayahnya sangat layak memegang kepemimpinan, dan sungguh anak ini (Usamah) adalah termasuk orang yang paling aku cintai setelahnya!"*  
> 📚 *(HR. Al-Bukhari No. 3730 & Muslim No. 2426)*

Khalifah Abu Bakar Ash-Shiddiq kemudian tetap memberangkatkan pasukan Usamah dan berjalan kaki menuntun kuda yang ditunggangi Usamah seraya berkata: *"Demi Allah, jangan engkau turun, dan demi Allah aku tidak akan naik kuda! Mengapa aku tidak boleh mengotori kedua kakiku sejenak di jalan Allah?!"*

### C. Zaid bin Tsabit: Ketua Dewan Kodifikasi Al-Qur'an
Di usia awal 20-an, Zaid bin Tsabit dipilih oleh Khalifah Abu Bakar dan Umar untuk memimpin proyek paling agung bagi peradaban manusia: menghimpun lembaran-lembaran wahyu menjadi satu Mushaf Al-Qur'an. Abu Bakar berkata kepadanya: *"Sesungguhnya engkau adalah pemuda yang cerdas, kami tidak meragukan integritasmu, dan engkau dahulu senantiasa mencatat wahyu untuk Rasulullah ﷺ!"* (HR. Bukhari No. 4986).

---

## 3. Keterangan Para Ulama Otoritatif

### 1. Syaikhul Islam Ibnu Taimiyyah (Wafat 728 H)
Dalam *Majmu' Al-Fatawa* (Juz 15 Hal. 328):
> *"Pemuda yang telah baligh adalah rijal (lelaki sejati) yang wajib memikul tanggung jawab amar ma'ruf nahi munkar. Pemisahan antara kedewasaan biologis dan kedewasaan sosial adalah kebatilan yang diada-adakan oleh orang-orang kafir yang ingin melalaikan generasi muda dari jihad dan penegakan agama."*

### 2. Imam Asy-Syathibi dalam Al-Muwafaqat
> *"Taklif syariat ditujukan kepada orang yang telah baligh berakal untuk menjaga lima kebutuhan pokok peradaban (adh-dharuriyyat al-khams): Agama, Jiwa, Akal, Kehormatan/Keturunan, dan Harta. Maka mendidik pemuda syabab adalah melatih mereka menjadi penjaga kelima benteng peradaban ini."*

---

## 4. Tiga Pilar Kemandirian Pemuda Mukallaf PKN

Keluarga dan sekolah Islam harus mendesain kurikulum Syabab berbasis **Tiga Kesiapan Mukallaf**:

```mermaid
graph TD
    SY["Pemuda Mukallaf Mandiri (Syabab)"]
    SY --> P1["1. Kesiapan Ruhiyah: Istiqamah Ibadah & Muraqabatullah"]
    SY --> P2["2. Kesiapan Kafa'ah Finansial: Menghasilkan Nafkah Halal Sendiri"]
    SY --> P3["3. Kesiapan Ba'ah Pernikahan: Siap Menjadi Qowwamah Keluarga"]
```

1. **Kesiapan Ruhiyah (Ibadah Tanpa Paksaan):**
   * Shalat malam (*qiyamullail*), tilawah harian, shaum sunnah, dan menundukkan pandangan (*ghaddhul bashar*) menjadi kebutuhan batinnya sendiri.
2. **Kesiapan Finansial (*Economic Self-Reliance*):**
   * Pemuda syabab dilatih magang bisnis, bertani, menjadi teknisi, atau membangun usaha rintisan. Rasulullah ﷺ bersabda: *"Sebaik-baik makanan yang dimakan seseorang adalah hasil kerja tangannya sendiri."* (HR. Bukhari No. 2072).
3. **Kesiapan Membangun Rumah Tangga (*Ba'ah Syar'iyyah*):**
   * Mampu memimpin, memiliki kematangan emosi, memahami fiqih munakahat, dan siap menjadi pelindung bagi keluarganya.

---

## 5. Tautan Konseptual Terkait
* [[Perkembangan]] — Rangkaian Lengkap Pentahapan Usia Nabawiyah.
* [[Murahaqah]] — Etape Transisi Menjelang Baligh.
* [[Bakat]] — Aktualisasi 40 Karakter Menjadi Karya Peradaban.
* [[Tujuan Hidup Manusia]] — Menjadi Khalifah fil Ardh yang Bertauhid.
"""

def main():
    print("Memulai ekspansi 4 artikel Fase Perkembangan Usia Nabawiyah...")
    for rel_path, content in ARTICLES.items():
        filepath = os.path.join(PERKEMBANGAN_DIR, rel_path)
        with open(filepath, "w", encoding="utf-8") as fp:
            fp.write(content)
        chars = len(content)
        words = len(content.split())
        lines = len(content.splitlines())
        print(f"  [BERHASIL] {rel_path:20s} -> {chars:,} karakter | {words:,} kata | {lines} baris")
    print("Semua 4 artikel Fase Perkembangan telah berhasil disimpan.")

if __name__ == "__main__":
    main()

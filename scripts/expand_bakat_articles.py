#!/usr/bin/env python3
"""
scripts/expand_bakat_articles.py
Mengembangkan 6 artikel sub-bakat PKN menjadi naskah komprehensif (≥ 5.000 karakter):
1. Bekerja Keras.md (6 pilar TB40)
2. Berpikir.md (5 pilar TB40)
3. Berperasaan.md (6 pilar TB40)
4. Memerintah.md (7 pilar TB40)
5. Bekerja Sama.md (8 pilar TB40)
6. Melayani.md (8 pilar TB40)

Setiap pilar turunan dilengkapi:
- Nama pilar (Arab & Latin) + Sub-kelompok Level 18
- Definisi operasional karakter
- Inspirasi keteladanan Shahabat Nabi radhiyallahu 'anhum (The Companion Archetype)
- Teks Dalil Otentik dari OpenBayan (Bahasa Arab, Terjemahan, Takhrij Kutubus Sunnah)
- Diagnosis Deviasi Karakter (Tafrith vs Ifrath) & Formula Kuratif
- Panduan Observasi Praktis Orang Tua (Rukun 3A: Suka, Bisa, Bermanfaat)
- Rekomendasi Profesi Masa Depan & Rumpun Keilmuan
"""

import os

BASE_DIR = "/home/abuhafi/Project/wiki-pkn"
BAKAT_DIR = os.path.join(BASE_DIR, "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat")

ARTICLES = {}

# ==============================================================================
# 1. BEKERJA KERAS.MD
# ==============================================================================
ARTICLES["Bekerja Keras.md"] = """---
title: "Bekerja Keras"
tags:
  - pkn
  - fitrah_bakat
  - bekerja_keras
  - tb40
  - shahabat
---

# Bakat Bekerja Keras (الحَمَاسَة - Al-Hamasah)

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « إِنَّ اللَّهَ يُحِبُّ إِذَا عَمِلَ أَحَدُكُمْ عَمَلًا أَنْ يُتْقِنَهُ »
>
> *"Sesungguhnya Allah menyukai jika salah seorang di antara kalian melakukan suatu pekerjaan, ia mengerjakannya dengan tekun, teliti, dan berkualitas tinggi (itqan)."*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Al-Baihaqi (Syu'abul Iman No. 4930), dishahihkan oleh Syaikh Al-Albani dalam *Silsilah Ash-Shahihah* No. 1113; Syarah Riyadush Shalihin (Juz 5 Hal. 12).  
> 💡 **Relevansi PKN:** Bakat Bekerja Keras (*Al-Hamasah*) adalah motor penggerak fisik yang merealisasikan cita-cita iman menjadi amal nyata (*amal shalih*). Tanpa daya tahan kerja keras, gagasan besar peradaban hanya akan berhenti pada angan-angan kosong.

---

## 1. Hakikat & Kedudukan Konseptual dalam Arsitektur PKN

Dalam taksonomi Pendidikan Karakter Nabawiyah (PKN), **Bekerja Keras** merupakan persilangan antara **Kutub Introvert** (dorongan energi yang bersumber dari konsentrasi internal mandiri) dan **Dimensi Karsa / Jasad** (*Al-Hawa* yang telah ditundukkan oleh syariat pada jiwa ammarah). 

Anak dengan bakat dominan Bekerja Keras dicirikan oleh:
* **Grit & Stamina Fisik:** Memiliki ketahanan tinggi terhadap keletihan jasmani, mampu fokus berjam-jam menyelesaikan tantangan praktis.
* **Orientasi Ketuntasan (*Closure*):** Merasa sangat terganggu bila melihat pekerjaan terbengkalai setengah jalan; kepuasan batinnya tercapai ketika proyek selesai dengan kokoh.
* **Bukan Sekadar Otot:** Kerja keras dalam Islam bukanlah perbudakan fisik tanpa arah, melainkan **Al-Mujahadah**—pencurahan segenap potensi fisik dan mental untuk menegakkan kalimat Allah dan memberi manfaat luas bagi sesama.

---

## 2. Enam Turunan Pilar Karakter TB40 & Inspirasi Shahabat Nabi ﷺ

Bakat Bekerja Keras membawahi **6 Pilar Karakter Mulia (TB40)** yang terbagi ke dalam 3 sub-kelompok Level 18. Setiap pilar terinspirasi langsung oleh keteladanan para Shahabat Nabi radhiyallahu 'anhum:

```mermaid
graph TD
    BK["Bekerja Keras (Al-Hamasah)"] --> G1["Sub 1: Berambisi"]
    BK --> G2["Sub 2: Berwibawa"]
    BK --> G3["Sub 3: Giat Bekerja"]

    G1 --> P1["#01 Himmah (Cita-cita Tinggi)"]
    G1 --> P2["#02 Ihsaan (Perfeksionis Mutqin)"]
    G2 --> P3["#03 'Izzah (Keteguhan Harga Diri)"]
    G2 --> P4["#04 Waqaar (Ketenangan Berwibawa)"]
    G3 --> P5["#05 'Aziimah (Tekad Memulai)"]
    G3 --> P6["#06 Nasyaath (Semangat Tuntas)"]
```

### Pilar #01: Himmah (الهِمَّة - Cita-cita Luhur)
* **Sub-Kelompok:** Berambisi (Introvert + Karsa)
* **Definisi Karakter:** Memiliki gairah batin dan cita-cita tertinggi yang melampaui batas kenyamanan duniawi, selalu memandang jauh ke depan.
* **Inspirasi Shahabat Nabi ﷺ:** **Usamah bin Zaid radhiyallahu 'anhu**. Di usia yang belum genap 18 tahun, beliau memiliki *himmah* kepemimpinan yang sangat tinggi hingga dipercaya oleh Rasulullah ﷺ menjadi panglima tertinggi memimpin pasukan yang di dalamnya terdapat Abu Bakar dan Umar untuk menghadapi imperium Romawi.
* **Dalil Otentik OpenBayan:**
  > « فَإِذَا سَأَلْتُمُ اللَّهَ فَاسْأَلُوهُ الْفِرْدَوْسَ، فَإِنَّهُ أَوْسَطُ الْجَنَّةِ، وَأَعْلَى الْجَنَّةِ »  
  > *"Jika kalian memohon kepada Allah, mintalah surga Al-Firdaus, karena sesungguhnya ia adalah surga yang paling utama dan paling tinggi."*  
  > 📚 *(HR. Al-Bukhari No. 2790, Kitab Al-Jihad was-Siyar)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Futuur (الفُتُوْر)** — Lemah kemauan, cepat puas, malas berusaha. *Kuratif:* Dikuatkan dengan pilar *'Aziimah* dan *Nasyaath*.
  * *Ifrath (Berlebih):* **Thuulul Amal (طُوْلُ الأَمَلِ)** — Panjang angan-angan tanpa realisasi realistis. *Kuratif:* Diredam dengan pilar *Qanaa'ah*, *Tawaadhu'*, dan *Hayaa'*.

---

### Pilar #02: Ihsaan (الاِحْسَان - Mutqin & Sempurna)
* **Sub-Kelompok:** Berambisi (Introvert + Karsa)
* **Definisi Karakter:** Dorongan kuat untuk selalu memberikan hasil karya terbaik, tidak rela menghasilkan produk yang cacat atau setengah matang.
* **Inspirasi Shahabat Nabi ﷺ:** **Zaid bin Tsabit radhiyallahu 'anhu**. Beliau menunjukkan standar *ihsaan* dan ketelitian tingkat tinggi saat diamanahi membukukan mushaf Al-Qur'an pada masa Khalifah Abu Bakar dan Utsman; beliau tidak menuliskan satu ayat pun kecuali disaksikan oleh dua saksi hafalan dan tulisan asli.
* **Dalil Otentik OpenBayan:**
  > « إِنَّ اللَّهَ كَتَبَ الْإِحْسَانَ عَلَى كُلِّ شَيْءٍ »  
  > *"Sesungguhnya Allah mewajibkan berbuat ihsan (profesional dan beradab) atas segala sesuatu."*  
  > 📚 *(HR. Muslim No. 1955, Kitab Ash-Shaid wadz-Dzaba'ih)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Isaa'ah (الإِسَاءة)** — Bekerja asal jadi, merusak mutu. *Kuratif:* Dilatih dengan penugasan terukur berbasis *Himmah* dan *'Izzah*.
  * *Ifrath (Berlebih):* **Tabdziir (التَّبْذِيْر)** — Perfeksionisme berlebihan hingga membuang waktu dan biaya demi hal minor. *Kuratif:* Dielingkan dengan *Qanaa'ah* dan *Tawaadhu'*.

---

### Pilar #03: 'Izzah (العِزَّة - Kehormatan Diri Beriman)
* **Sub-Kelompok:** Berwibawa (Introvert + Karsa)
* **Definisi Karakter:** Teguh mempertahankan kemuliaan prinsip tauhid dan integritas pribadi, pantang menghinakan diri di hadapan manusia.
* **Inspirasi Shahabat Nabi ﷺ:** **Umar bin Al-Khattab radhiyallahu 'anhu**. Sosok yang sejak keislamannya memancarkan kemuliaan (*'izzah*) bagi kaum muslimin di Makkah.
* **Dalil Otentik OpenBayan:**
  > « إِنَّا كُنَّا أَذَلَّ قَوْمٍ، فَأَعَزَّنَا اللَّهُ بِالإِسْلاَمِ، فَمَهْمَا نَبْتَغِي الْعِزَّةَ بِغَيْرِ مَا أَعَزَّنَا اللَّهُ بِهِ أَذَلَّنَا اللَّهُ »  
  > *"Dahulu kita adalah kaum yang paling hina, lalu Allah muliakan kita dengan Islam. Maka kapan saja kita mencari kemuliaan dengan selain apa yang Allah muliakan kepada kita, niscaya Allah akan menghinakan kita."*  
  > 📚 *(Atsar Shahih Riwayat Al-Hakim dalam Al-Mustadrak No. 207; Siyar A'lam An-Nubala 1/79)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Dzull (الذُّلّ)** — Jiwa lemah, minder, mudah diintimidasi kebatilan. *Kuratif:* Penguatan tauhid rububiyah dan pilar *Syajaa'ah*.
  * *Ifrath (Berlebih):* **Kibr (الكِبْر)** — Angkuh, menolak kebenaran dan merendahkan manusia. *Kuratif:* Diimbangi dengan pilar *Tawaadhu'* dan *Hayaa'*.

---

### Pilar #04: Waqaar (الوَقَار - Wibawa Ketenangan)
* **Sub-Kelompok:** Berwibawa (Introvert + Karsa)
* **Definisi Karakter:** Memiliki ketenangan sikap yang berbobot, tidak grusa-grusu, sedikit bicara namun mendalam dan berwibawa dalam tindakan.
* **Inspirasi Shahabat Nabi ﷺ:** **Utsman bin Affan radhiyallahu 'anhu**. Beliau adalah pribadi yang sangat tenang, menjaga adab kesantunan tingkat tinggi, namun sangat tangguh dalam mengambil keputusan strategis umat.
* **Dalil Otentik OpenBayan:**
  > « إِذَا أُقِيمَتِ الصَّلَاةُ فَلَا تَأْتُوهَا تَسْعَوْنَ، وَأْتُوهَا تَمْشُونَ وَعَلَيْكُمُ السَّكِينَةُ وَالْوَقَارُ »  
  > *"Jika shalat telah diiqamahkan, janganlah kalian mendatanginya dengan berlari tergesa-gesa. Datangilah dengan berjalan tenang, dan hendaklah kalian menjaga ketenangan batin (sakinah) dan kewibawaan lahiriah (waqaar)."*  
  > 📚 *(HR. Al-Bukhari No. 636 & Muslim No. 602)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Thaysy (الطَّيْش)** — Sikap serampangan, banyak bercanda tidak pada tempatnya, hilang wibawa. *Kuratif:* Latihan adab diam (*Shamt*) dan tafakkur.
  * *Ifrath (Berlebih):* **'Ujb (العُجْب)** — Merasa diri paling suci dan menjaga jarak dingin dari orang lain. *Kuratif:* Pelatihan kehangatan (*Basyaasyah*) dan kerendahhatian (*Tawaadhu'*).

---

### Pilar #05: 'Aziimah (العَزِيمَة - Tekad Memulai)
* **Sub-Kelompok:** Giat Bekerja (Introvert + Karsa)
* **Definisi Karakter:** Tekad membaja untuk segera mengambil inisiatif dan memulai langkah pertama tanpa menunda-nunda pekerjaan (*procrastination*).
* **Inspirasi Shahabat Nabi ﷺ:** **Khalid bin Al-Walid radhiyallahu 'anhu**. Pedang Allah yang tidak pernah ragu mengambil keputusan inisiatif di medan laga saat celah kemenangan terbuka.
* **Dalil Otentik OpenBayan:**
  > « احْرِصْ عَلَى مَا يَنْفَعُكَ، وَاسْتَعِنْ بِاللَّهِ وَلَا تَعْجَزْ »  
  > *"Bersemangatlah terhadap apa saja yang bermanfaat bagimu, mohonlah pertolongan kepada Allah, dan jangan sekali-kali merasa lemah/lemah tekad!"*  
  > 📚 *(HR. Muslim No. 2664, Kitab Al-Qadar)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Kasal (الكَسَل)** — Menunda pekerjaan, ragu melangkah, berat memulai. *Kuratif:* Pemecahan tugas besar menjadi modul kecil dan pendampingan *Bahasa Tangan* terstruktur.
  * *Ifrath (Berlebih):* **Tahawwur (التَّهَوُّر)** — Nekat bertindak tanpa perhitungan syariat dan strategi. *Kuratif:* Wajib musyawarah dan penanaman pilar *Anaah* (kehati-hatian).

---

### Pilar #06: Nasyaath (النَّشَاط - Ketekunan Eksekusi)
* **Sub-Kelompok:** Giat Bekerja (Introvert + Karsa)
* **Definisi Karakter:** Daya tahan kerja fisik yang konsisten, berstamina tinggi dalam menyelesaikan pekerjaan rutin hingga tuntas sempurna.
* **Inspirasi Shahabat Nabi ﷺ:** **Abu Hurairah radhiyallahu 'anhu**. Beliau mengikatkan batu di perutnya menahan lapar demi terus aktif (*nasyaath*) menyertai Rasulullah ﷺ mencatat ribuan hadits tanpa terputus.
* **Dalil Otentik OpenBayan:**
  > « اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْعَجْزِ وَالْكَسَلِ، وَالْجُبْنِ وَالْهَرَمِ »  
  > *"Ya Allah, sesungguhnya aku berlindung kepada-Mu dari kelemahan tekad dan kemalasan fisik, dari rasa takut dan kepikunan."*  
  > 📚 *(HR. Al-Bukhari No. 2823 & Muslim No. 2706)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Khumuul (الخُمُوْل)** — Lesu, pasif, lamban dalam bergerak. *Kuratif:* Olahraga sunnah (memanah, berenang, bela diri) untuk memicu adrenalin gerak.
  * *Ifrath (Berlebih):* **Irhāq (الإِرْهَاق)** — *Workaholic*, memforsir tubuh hingga melanggar hak istirahat, hak keluarga, dan hak ibadah. *Kuratif:* Menegakkan hadits Salman Al-Farisi: *"Sesungguhnya tubuhmu memiliki hak atasmu."*

---

## 3. Rubrik Observasi Bakat untuk Orang Tua & Pendidik (Rukun 3A)

Untuk memastikan apakah seorang anak memiliki benih unggul bakat **Bekerja Keras**, gunakan instrumen observasi **Rukun 3A**:

| Rukun Observasi | Indikator Perilaku Otentik Anak | Catatan Guru / Orang Tua |
| :--- | :--- | :--- |
| **1. Suka (*Interest*)** | Anak secara spontan memilih aktivitas fisik menantang (merakit perkakas, berkebun, membersihkan ruangan, membuat karya pertukangan) tanpa disuruh. | Timbul rasa gembira saat keringat mengalir dan tangan kotor oleh pekerjaan nyata. |
| **2. Bisa (*Ability*)** | Belajar keterampilan motorik dan teknis jauh lebih cepat daripada anak seusianya; memiliki koordinasi mata-tangan dan ketelitian luar biasa. | Mampu menyelesaikan proyek konstruksi mini dengan rapi tanpa cepat menyerah. |
| **3. Bermanfaat (*Utility*)** | Hasil kerjanya memberi solusi nyata bagi rumah tangga atau teman sebaya (membantu memperbaiki barang rusak, merapikan fasilitas umum). | Dorongan tenaganya dialirkan menjadi amal shalih yang meringankan beban orang lain. |

---

## 4. Panduan Pendampingan Berdasarkan 4 Fase Usia Nabawiyah

### A. Fase Thufulah (0–7 Tahun: Raja & Eksplorasi Sensori-Motorik)
* Biarkan anak bebas bermain pasir, lumpur, air, dan balok kayu untuk menumbuhkan kekuatan otot (*gross motor skills*).
* Jangan marahi anak saat bajunya kotor karena bereksplorasi fisik; di sinilah benih *nasyaath* bersemi.
* Sambut bantuan fisiknya (misal membawakan sandal ayah) dengan pelukan hangat dan pujian tulus.

### B. Fase Tamyiz (7–10 Tahun: Pembantu & Adab Ketuntasan)
* Libatkan dalam tugas rumah tangga terstruktur: merapikan tempat tidur, mencuci piring sendiri, menyiram tanaman.
* Ajarkan adab *itqan*: periksa bersama apakah pekerjaan sudah bersih dan rapi sesuai standar.
* Hindari memberi upah uang untuk tugas wajib keluarga; tumbuhkan kebanggaan beramal karena Allah.

### C. Fase Murahaqah (10–15 Tahun: Menteri & Magang Proyek Nyata)
* Berikan proyek teknis mandiri: merakit meja, merawat sepeda/motor, membangun instalasi hidroponik.
* Kenalkan dengan sosok pengrajin atau teknisi Muslim yang memiliki etos *'izzah* dan ketelitian tinggi.
* Jika anak lalai dari tanggung jawab yang disepakati, terapkan konsekuensi logis secara tegas tanpa merendahkan martabatnya.

### D. Fase Syabab (15+ Tahun: Kemitraan & Profesionalisme Mandiri)
* Salurkan bakatnya ke dunia vokasi, industri teknik, rekayasa sipil, atau wirausaha mandiri.
* Tegakkan pemahaman bahwa kerja kerasnya adalah sarana menafkahi keluarga secara halal (*iffah*) dan mendanai dakwah.

---

## 5. Pemetaan Rumpun Profesi & Jurusan Masa Depan

Bakat Bekerja Keras yang terdidik secara islami akan melahirkan insan kamil yang mengisi pos-pos vital peradaban:
* **Profesi:** Insinyur Sipil, Arsitek Lapangan, Kontraktor Proyek, Quality Controller (QC), Mekanik Handal, Ahli Robotika & Mesin, Tim SAR & Logistik Kemanusiaan, Entrepreneur Manufaktur.
* **Rumpun Jurusan:** Teknik Sipil, Teknik Mesin, Teknik Elektro, Agroteknologi, Farmasi Industri, Manajemen Operasional, Desain Produk Industri.

---

## 6. Tautan Konseptual Terkait
* [[Bakat]] — Induk Peta 6 Dimensi Karakter Nabawiyah.
* [[Insan]] — Hakikat Manusia, Ruh, Jasad, dan Jiwa.
* [[Pembelajaran Alamiah]] — Metode Belajar Alami Berbasis Ekosistem Nyata.
* [[Perkembangan]] — Pentahapan Usia dari Thufulah Menuju Mukallaf Mandiri.
"""

# ==============================================================================
# 2. BERPIKIR.MD
# ==============================================================================
ARTICLES["Berpikir.md"] = """---
title: "Berpikir"
tags:
  - pkn
  - fitrah_bakat
  - berpikir
  - tb40
  - shahabat
---

# Bakat Berpikir (التَّفْكِيْر - At-Tafkir)

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « أَفَلَا يَتَدَبَّرُونَ الْقُرْآنَ أَمْ عَلَىٰ قُلُوبٍ أَقْفَالُهَا »
>
> *"Maka tidakkah mereka mentadabburi (memikirkan secara mendalam) Al-Qur'an, ataukah hati mereka telah terkunci rapat?"*
>
> 📚 **Sumber Rujukan OpenBayan:** QS. Muhammad: 24; Tafsir Ibnu Katsir (Juz 7 Hal. 312); Shahih Al-Bukhari (Kitab Fadha'ilil Qur'an).  
> 💡 **Relevansi PKN:** Bakat Berpikir (*At-Tafkir*) adalah modalitas akal (*Al-'Aql*) yang ditundukkan untuk menangkap ayat-ayat kauniyah dan qauliyah, menalar sebab-akibat, serta merumuskan strategi peradaban Islam.

---

## 1. Hakikat & Kedudukan Konseptual dalam Arsitektur PKN

Dalam arsitektur Pendidikan Karakter Nabawiyah, **Bakat Berpikir** adalah hasil persilangan antara **Kutub Introvert** (sumber energi dari perenungan batin mandiri) dan **Dimensi Cipta / Akal** (*Al-'Aql* pada jiwa lawwamah).

Anak dengan bakat dominan Berpikir dicirikan oleh:
* **Daya Analitis & Haus Pengetahuan:** Senang bertanya "mengapa" dan "bagaimana", suka mengurai struktur permasalahan, gemar membaca dan menyerap data.
* **Gaya Belajar Visual & Reflektif:** Cepat memahami bagan, diagram, peta konsep, dan memerlukan ruang hening untuk mencerna informasi secara tuntas.
* **Bukan Sekadar Intelektual Kering:** Berpikir dalam Islam bukanlah rasionalisme sekuler yang mendewakan logika (*ahlur ra'yi*), melainkan **Tafakkur & Tadabbur** yang mengantarkan akal pada kekaguman mutlak kepada Sang Pencipta (*Ma'rifatullah*).

---

## 2. Lima Turunan Pilar Karakter TB40 & Inspirasi Shahabat Nabi ﷺ

Bakat Berpikir membawahi **5 Pilar Karakter Mulia (TB40)** yang terbagi ke dalam 3 sub-kelompok Level 18. Masing-masing pilar berakar pada keteladanan agung para Shahabat Nabi radhiyallahu 'anhum:

```mermaid
graph TD
    BP["Berpikir (At-Tafkir)"] --> G1["Sub 4: Imajinatif & Visioner"]
    BP --> G2["Sub 5: Berpikir Positif"]
    BP --> G3["Sub 6: Analitis & Bijaksana"]

    G1 --> P7["#07 Firaasah (Ketajaman Intuisi)"]
    G1 --> P8["#08 Nubl (Banyak Akal Solutif)"]
    G2 --> P9["#09 Husnuzhan (Objektif Positif)"]
    G3 --> P10["#10 Dzakaa' (Cerdas Analitis)"]
    G3 --> P11["#11 Hikmah (Tepat Menempatkan Perkara)"]
```

### Pilar #07: Firaasah (الفِرَاسَة - Ketajaman Firasat Iman)
* **Sub-Kelompok:** Suka Berpikir Imajinatif / Visioner (Introvert + Cipta)
* **Definisi Karakter:** Ketajaman nalar batin yang mampu menangkap hakikat perkara tersembunyi dengan mengamati tanda-tanda lahiriah yang tampak.
* **Inspirasi Shahabat Nabi ﷺ:** **Umar bin Al-Khattab radhiyallahu 'anhu**. Beliau dijuluki sebagai *Al-Muhaddats* (orang yang diberi ilham firasat benar). Firasat pemikirannya berulang kali bertepatan dengan turunnya wahyu ayat Al-Qur'an (*Muwafaqat Umar*), seperti penetapan Maqam Ibrahim sebagai tempat shalat dan hijab bagi ummahatul mukminin.
* **Dalil Otentik OpenBayan:**
  > « إِنَّهُ قَدْ كَانَ فِيمَا مَضَى قَبْلَكُمْ مِنَ الأُمَمِ مُحَدَّثُونَ، وَإِنَّهُ إِنْ كَانَ فِي أُمَّتِي هَذِهِ مِنْهُمْ فَإِنَّهُ عُمَرُ بْنُ الخَطَّابِ »  
  > *"Sesungguhnya pada umat-umat terdahulu sebelum kalian terdapat orang-orang yang diberi ilham kebenaran (muhaddatsun). Dan jika ada seorang di antara umatku ini, maka dialah Umar bin Al-Khattab."*  
  > 📚 *(HR. Al-Bukhari No. 3689 & Muslim No. 2398)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Safah (السَّفَه)** — Kedangkalan berpikir, mudah tertipu oleh bungkus luar. *Kuratif:* Melatih anak mengamati pola sebab-akibat dan memperdalam tadabbur ayat.
  * *Ifrath (Berlebih):* **Kadzib / Khurafat (الكَذِب)** — Mengaku mengetahui hal ghaib tanpa dalil syar'i. *Kuratif:* Mengikat firasat dengan nash shahih dan kaidah *Shidq*.

---

### Pilar #08: Nubl (النُّبْل - Cerdik & Banyak Akal)
* **Sub-Kelompok:** Suka Berpikir Imajinatif / Visioner (Introvert + Cipta)
* **Definisi Karakter:** Cepat memahami situasi kritis dan lihai merumuskan solusi strategis yang keluar dari kelaziman (*out of the box*).
* **Inspirasi Shahabat Nabi ﷺ:** **Salman Al-Farisi radhiyallahu 'anhu**. Ketika 10.000 pasukan sekutu Quraisy mengepung Madinah dalam Perang Ahzab (Khandaq), Salman mengajukan gagasan cerdik menggali parit raksasa di utara Madinah—sebuah strategi pertahanan militer yang belum pernah dikenal oleh bangsa Arab saat itu.
* **Dalil Otentik OpenBayan:**
  > « كَانَ سَلْمَانُ يُشِيرُ عَلَى رَسُولِ اللَّهِ ﷺ بِالْأَمْرِ فَيَأْخُذُ بِهِ »  
  > *"Adalah Salman senantiasa memberikan usulan gagasan cerdik kepada Rasulullah ﷺ dalam berbagai urusan, lalu beliau mengambil dan menerapkannya."*  
  > 📚 *(Siyar A'lam An-Nubala karya Adz-Dzahabi 1/540; Al-Bidayah wan-Nihayah 4/105)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Jahl (الجَهْل)** — Buntu saat menghadapi masalah kecil, panik. *Kuratif:* Dilatih dengan studi kasus pemecahan teka-teki nyata (*problem solving*).
  * *Ifrath (Berlebih):* **Ghisy / Hiyal (الغِشِّ)** — Menggunakan kecerdikan untuk menipu, memanipulasi celah hukum demi keuntungan pribadi. *Kuratif:* Menanamkan pilar *Amaanah* dan *'Adaalah*.

---

### Pilar #09: Husnuzhan (حُسْنُ الظَّن - Kejernihan Nalar Positif)
* **Sub-Kelompok:** Suka Berpikir Positif (Introvert + Cipta)
* **Definisi Karakter:** Senantiasa mengedepankan asas praduga baik, objektif menyaring informasi, dan tidak mudah terprovokasi oleh isu liar.
* **Inspirasi Shahabat Nabi ﷺ:** **Abu Ayyub Al-Anshari & istrinya radhiyallahu 'anhuma**. Saat kota Madinah diguncang fitnah keji terhadap Ummul Mukminin Aisyah (Haditsul Ifk), Ummu Ayyub bertanya kepada suaminya, lalu Abu Ayyub menjawab dengan jernih: *"Demi Allah, aku tidak akan pernah melakukannya, dan Aisyah jauh lebih mulia daripada engkau!"* Mereka menolak mentah-mentah berita hoax tersebut sebelum ada konfirmasi wahyu.
* **Dalil Otentik OpenBayan:**
  > « إِيَّاكُمْ وَالظَّنَّ، فَإِنَّ الظَّنَّ أَكْذَبُ الحَدِيثِ »  
  > *"Jauhilah oleh kalian prasangka buruk (tanpa bukti), karena sesungguhnya prasangka adalah seburuk-buruk perkataan dusta."*  
  > 📚 *(HR. Al-Bukhari No. 5143 & Muslim No. 2563)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Suu'uzhan (سُوْءُ الظَّن)** — Pikiran penuh kecurigaan kronis, meracuni hubungan persaudaraan. *Kuratif:* Membiasakan tabayyun dan berbaik sangka kepada takdir Allah.
  * *Ifrath (Berlebih):* **Taqliid A'ma (التَّقْلِيْد)** — Polos hingga mudah ditipu dan dibodohi musuh. *Kuratif:* Dilengkapi dengan kewaspadaan pilar *Firaasah* dan *Dzakaa'*.

---

### Pilar #10: Dzakaa' (الذَّكَاء - Cerdas & Cepat Menyerap)
* **Sub-Kelompok:** Suka Berpikir Analitis (Introvert + Cipta)
* **Definisi Karakter:** Kecepatan daya tangkap logika, ketajaman hafalan, serta kecerdasan mendalam dalam mengurai data kompleks.
* **Inspirasi Shahabat Nabi ﷺ:** **Zaid bin Tsabit radhiyallahu 'anhu**. Beliau diperintahkan oleh Nabi ﷺ untuk mempelajari bahasa Yahudi (Suryani/Ibrani) demi kepentingan surat-menyurat resmi kenegaraan, dan beliau mampu menguasainya secara fasih hanya dalam tempo 15 hari!
* **Dalil Otentik OpenBayan:**
  > « أَمَرَنِي رَسُولُ اللَّهِ ﷺ أَنْ أَتَعَلَّمَ لَهُ كِتَابَ يَهُودَ، قَالَ: إِنِّي وَاللَّهِ مَا آمَنُ يَهُودَ عَلَى كِتَابٍ، فَتَعَلَّمْتُهُ، فَمَا مَرَّ بِي نِصْفُ شَهْرٍ حَتَّى حَذَقْتُهُ »  
  > *"Rasulullah ﷺ memerintahkanku untuk mempelajari surat orang-orang Yahudi untuk beliau... Maka aku mempelajarinya, dan belum berlalu setengah bulan sampai aku telah mahir menguasainya."*  
  > 📚 *(HR. At-Tirmidzi No. 2715, dinyatakan Hasan Shahih; Al-Bukhari secara mu'allaq)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Balaadah (البَلَادَة)** — Malas mengasah nalar, enggan membaca. *Kuratif:* Latihan menghafal Al-Qur'an dan mutun ilmiah secara bertahap.
  * *Ifrath (Berlebih):* **Ahlur Ra'yi (أَهْلُ الرَّأْيِ)** — Mendewakan logika akal di atas nash wahyu, gemar mendebat perkara agama yang qath'i. *Kuratif:* Tundukkan akal di bawah wibawa wahyu dengan pilar *Tawaadhu'* dan *Ihsan*.

---

### Pilar #11: Hikmah (الحِكْمَة - Kebijaksanaan Menempatkan Perkara)
* **Sub-Kelompok:** Suka Berpikir Analitis (Introvert + Cipta)
* **Definisi Karakter:** Kedalaman ilmu yang mampu menempatkan setiap perkataan, tindakan, dan keputusan pada tempat dan waktu yang paling tepat (*proporsional*).
* **Inspirasi Shahabat Nabi ﷺ:** **Mu'adz bin Jabal radhiyallahu 'anhu**. Sahabat muda yang dipuji Rasulullah ﷺ sebagai sosok yang paling paham tentang halal dan haram, dan diutus ke Yaman sebagai hakim dan mufti rujukan umat.
* **Dalil Otentik OpenBayan:**
  > « يُؤْتِي الْحِكْمَةَ مَن يَشَاءُ ۚ وَمَن يُؤْتَ الْحِكْمَةَ فَقَدْ أُوتِيَ خَيْرًا كَثِيرًا »  
  > *"Allah menganugerahkan al-hikmah (pemahaman mendalam dan tepat) kepada siapa yang Dia kehendaki. Dan barangsiapa dianugerahi al-hikmah, sungguh dia telah dianugerahi kebajikan yang sangat banyak."*  
  > 📚 *(QS. Al-Baqarah: 269; Tafsir Ibnu Katsir 1/702)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Jahl Murakkab (الجَهْلُ المُرَكَّب)** — Merasa tahu padahal tidak paham konteks, asal bicara. *Kuratif:* Duduk di majelis para ulama rabbani dan belajar mendengarkan.
  * *Ifrath (Berlebih):* **Falsafah ‘Aqiimah (الفَلْسَفَة)** — Berputar-putar dalam teori rumit tanpa aksi nyata. *Kuratif:* Salurkan ke penulisan fatwa praktis atau panduan amal nyata.

---

## 3. Rubrik Observasi Bakat untuk Orang Tua & Pendidik (Rukun 3A)

| Rukun Observasi | Indikator Perilaku Otentik Anak | Catatan Guru / Orang Tua |
| :--- | :--- | :--- |
| **1. Suka (*Interest*)** | Gemar membaca buku, membongkar rahasia mesin/permainan, menikmati teka-teki logika, asyik merenung sendiri. | Wajahnya berbinar ketika menemukan jawaban dari misteri yang mengganjal pikirannya. |
| **2. Bisa (*Ability*)** | Mampu mengingat detail peristiwa dengan sangat presisi; cepat menghubungkan fakta yang berserak menjadi kesimpulan utuh. | Memiliki daya nalar kritis di atas rata-rata usia sebayanya. |
| **3. Bermanfaat (*Utility*)** | Mampu memberikan nasihat bijak kepada kawan yang berselisih; menyusun strategi belajar bersama; merangkum materi rumit. | Pemikirannya menjadi penerang jalan keluar bagi orang-orang di sekitarnya. |

---

## 4. Panduan Pendampingan Berdasarkan 4 Fase Usia Nabawiyah

### A. Fase Thufulah (0–7 Tahun: Menjawab Rasa Ingin Tahu dengan Kasih)
* Dengarkan dan jawab setiap pertanyaan anak tanpa membentak atau menyepelekan ("Kenapa langit biru?", "Kenapa semut baris?").
* Ajak mengamati alam terbuka: melihat dedaunan, perbintangan, hewan ternak untuk memicu *tafakkur*.
* Hindari membebani anak dengan hafalan mekanis yang dipaksakan tanpa kecintaan.

### B. Fase Tamyiz (7–10 Tahun: Menata Logika Syariat & Membaca)
* Fasilitasi perpustakaan rumah yang kaya sirah nabawiyah, kisah shahabat, sains alam, dan fiqih dasar.
* Ajak berdiskusi santai di meja makan mengenai hikmah di balik perintah Allah (misal hikmah shalat berjamaah, hikmah puasa).
* Ajarkan metode berpikir kritis Islami: menyaring kabar bohong (*tabayyun*).

### C. Fase Murahaqah (10–15 Tahun: Pelatihan Riset & Problem Solving)
* Berikan tantangan menganalisis masalah nyata keluarga atau masyarakat, lalu minta ia menyusun proposal solusinya.
* Libatkan anak dalam musyawarah keluarga; dengarkan sudut pandang analitisnya secara serius.
* Ajarkan adab ikhtilaf: bagaimana berbeda pandangan ilmiah dengan tetap menjaga kelembutan hati.

### D. Fase Syabab (15+ Tahun: Karya Intelektual & Khidmah Peradaban)
* Dorong anak untuk menulis artikel, karya ilmiah, riset teknologi, atau kajian syariah aplikatif.
* Dampingi agar ilmunya membuahkan *khasy-yah* (rasa takut kepada Allah), bukan kesombongan akademik.

---

## 5. Pemetaan Rumpun Profesi & Jurusan Masa Depan

* **Profesi:** Peneliti Sains, Analis Kebijakan Publik, Arsitek Sistem Software (IT), Konsultan Manajemen, Mufti/Hakim Syariah, Perencana Strategis (Litbang), Penulis Ilmiah.
* **Rumpun Jurusan:** Ilmu Ushuluddin, Fiqih wa Ushuluhu, Ilmu Komputer/Informatika, Matematika Murni, Fisika Teoritik, Hukum Islam & Internasional, Data Science.

---

## 6. Tautan Konseptual Terkait
* [[Bakat]] — Induk Taksonomi 40 Karakter Nabawiyah.
* [[Insan]] — Hakikat Akal, Hati, dan Hawa Nafsu.
* [[Bahasa Lisan]] — Seni Komunikasi Nasihat & Diskusi Intelektual.
* [[Tamyiz]] — Etape Emas Pembentukan Nalar Kritis Anak.
"""

# ==============================================================================
# 3. BERPERASAAN.MD
# ==============================================================================
ARTICLES["Berperasaan.md"] = """---
title: "Berperasaan"
tags:
  - pkn
  - fitrah_bakat
  - berperasaan
  - tb40
  - shahabat
---

# Bakat Berperasaan (الشُعُوْر - Asy-Syu'ur)

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « أَلَا وَإِنَّ فِي الْجَسَدِ مُضْغَةً إِذَا صَلَحَتْ صَلَحَ الْجَسَدُ كُلُّهُ، وَإِذَا فَسَدَتْ فَسَدَ الْجَسَدُ كُلُّهُ، أَلَا وَهِيَ الْقَلْبُ »
>
> *"Ingatlah, sesungguhnya di dalam tubuh terdapat segumpal daging. Jika ia baik, maka baiklah seluruh tubuh itu; dan jika ia rusak, maka rusaklah seluruh tubuh itu. Ingatlah, segumpal daging itu adalah Hati (Al-Qalb)."*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Al-Bukhari No. 52 & Muslim No. 1599; Syarah Shahih Muslim Imam An-Nawawi (Juz 11 Hal. 27); Tafsir Al-Baghawi.  
> 💡 **Relevansi PKN:** Bakat Berperasaan (*Asy-Syu'ur*) adalah radar batiniah jiwa (*Al-Qalb*) yang peka terhadap kesucian nurani, kejujuran batin, rasa malu syar'i, dan qana'ah terhadap karunia Allah.

---

## 1. Hakikat & Kedudukan Konseptual dalam Arsitektur PKN

Dalam kerangka Pendidikan Karakter Nabawiyah, **Bakat Berperasaan** merupakan persilangan antara **Kutub Introvert** (orientasi internal ke dalam diri) dan **Dimensi Rasa / Hati** (*Al-Qalb* pada jiwa muthmainnah).

Anak dengan bakat dominan Berperasaan memiliki ciri:
* **Sensitivitas Nurani yang Tinggi:** Sangat peka terhadap kebohongan, ketidakadilan, atau kepalsuan; hatinya mudah bergetar oleh nasihat iman dan penderitaan orang lain.
* **Cenderung Pendiam & Suka Merenung:** Tidak suka keramaian yang bising, berhati-hati dalam menjaga kesucian diri (*'iffah*), dan memiliki rasa malu (*hayaa'*) yang sangat dominan.
* **Bukan Kelemahan Mental:** Sensitivitas perasaan bukanlah sifat "cengeng" atau rapuh, melainkan **Muraqabatullah**—kesadaran batin yang mendalam bahwa dirinya senantiasa diawasi oleh Allah SWT.

---

## 2. Enam Turunan Pilar Karakter TB40 & Inspirasi Shahabat Nabi ﷺ

Bakat Berperasaan menaungi **6 Pilar Karakter Mulia (TB40)** yang terbagi ke dalam 3 sub-kelompok Level 18:

```mermaid
graph TD
    BPer["Berperasaan (Asy-Syu'ur)"] --> G1["Sub 7: Apa Adanya"]
    BPer --> G2["Sub 8: Pendiam & Menjaga Diri"]
    BPer --> G3["Sub 9: Suka Merendah & Qana'ah"]

    G1 --> P12["#12 Shidq (Jujur Tanpa Rekayasa)"]
    G2 --> P13["#13 'Iffah (Menjaga Kesucian Diri)"]
    G2 --> P14["#14 Shamt (Bijak Mengendalikan Lisan)"]
    G3 --> P15["#15 Hayaa' (Rasa Malu Syar'i)"]
    G3 --> P16["#16 Qanaa'ah (Merasa Cukup)"]
    G3 --> P17["#17 Tawaadhu' (Rendah Hati)"]
```

### Pilar #12: Shidq (الصِّدْق - Jujur & Autentik)
* **Sub-Kelompok:** Suka Apa Adanya (Introvert + Rasa)
* **Definisi Karakter:** Keselarasan mutlak antara apa yang ada di dalam batin dengan ucapan lisan dan tindakan nyata; pantang bermuka dua.
* **Inspirasi Shahabat Nabi ﷺ:** **Abu Bakar Ash-Shiddiq radhiyallahu 'anhu**. Sosok yang meraih gelar *Ash-Shiddiq* karena membenarkan risalah kenabian tanpa keraguan sedikit pun, serta **Ka'ab bin Malik radhiyallahu 'anhu** yang memilih berkata jujur apa adanya saat tertinggal dari Perang Tabuk meskipun menghadapi sanksi pengasingan sosial, hingga Allah menurunkan pengampunan baginya di QS. At-Taubah: 118.
* **Dalil Otentik OpenBayan:**
  > « عَلَيْكُمْ بِالصِّدْقِ، فَإِنَّ الصِّدْقَ يَهْدِي إِلَى البِرِّ، وَإِنَّ البِرَّ يَهْدِي إِلَى الجَنَّةِ »  
  > *"Wajib atas kalian senantiasa bersikap jujur, karena sesungguhnya kejujuran mengantarkan kepada kebajikan, dan kebajikan mengantarkan ke surga."*  
  > 📚 *(HR. Al-Bukhari No. 6094 & Muslim No. 2607)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Kadzib / Nifaq (الكَذِب)** — Dusta, menutupi kesalahan dengan rekayasa. *Kuratif:* Bangun rasa aman di rumah; jangan pernah hukum anak yang telah berani jujur mengakui kesalahan.
  * *Ifrath (Berlebih):* **Ifsyaa'us Sirr (إِفْشَاءُ السِّرّ)** — Berbicara terlalu polos hingga membuka aib keluarga atau rahasia penting. *Kuratif:* Dikuatkan dengan pilar *Kitmaanus Sirr* dan *Satr*.

---

### Pilar #13: 'Iffah (العِفَّة - Menjaga Kesucian Jiwa)
* **Sub-Kelompok:** Pendiam (Introvert + Rasa)
* **Definisi Karakter:** Kemampuan batin menahan diri dari godaan syahwat, harta syubhat, dan perilaku hina yang merendahkan martabat kehambaan.
* **Inspirasi Shahabat Nabi ﷺ:** **Mush'ab bin Umair radhiyallahu 'anhu**. Pemuda bangsawan Makkah yang meninggalkan segala gelimang harta dan kemewahan demi menjaga kesucian iman di jalan dakwah, hingga wafat di Perang Uhud hanya berkafan sehelai kain burdah.
* **Dalil Otentik OpenBayan:**
  > « اللَّهُمَّ إِنِّي أَسْأَلُكَ الْهُدَى وَالتُّقَى وَالْعَفَافَ وَالْغِنَى »  
  > *"Ya Allah, sesungguhnya aku memohon kepada-Mu petunjuk, ketakwaan, kesucian diri ('iffah), dan kekayaan jiwa."*  
  > 📚 *(HR. Muslim No. 2721, Kitadz-Dzikr wad-Du'a)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Fahsy (الفَحْش)** — Terjerumus pada pergaulan bebas, pornografi, atau serakah harta haram. *Kuratif:* Bentengi pandangan mata, fasilitasi pernikahan dini saat usia syabab bila telah mampu.
  * *Ifrath (Berlebih):* **Was-was / Rohbaniyah (الرَّهْبَانِيَّة)** — Mengharamkan hal-hal mubah dan menjauhi interaksi halal kemasyarakatan. *Kuratif:* Tanamkan sunnah Nabi ﷺ dalam berkeluarga dan bermuamalah.

---

### Pilar #14: Shamt (الصَّمْت - Menjaga Lisan)
* **Sub-Kelompok:** Pendiam (Introvert + Rasa)
* **Definisi Karakter:** Kecenderungan menahan diri dari banyak bicara; hanya berbicara bila mengandung kebaikan, ilmu, atau maslahat dakwah.
* **Inspirasi Shahabat Nabi ﷺ:** **Abdullah bin Mas'ud radhiyallahu 'anhu**. Beliau memegang lisannya seraya berkata: *"Wahai lisan, katakanlah yang baik niscaya engkau beruntung, atau diamlah dari keburukan niscaya engkau selamat!"*
* **Dalil Otentik OpenBayan:**
  > « مَنْ كَانَ يُؤْمِنُ بِاللَّهِ وَاليَوْمِ الآخِرِ فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ »  
  > *"Barangsiapa beriman kepada Allah dan hari akhir, hendaklah ia berkata yang baik atau diam."*  
  > 📚 *(HR. Al-Bukhari No. 6018 & Muslim No. 47)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Ghiibah / Namimah (الغِيْبَة)** — Gemar bergosip, mencela, dan menebar fitnah. *Kuratif:* Puasa bicara sia-sia, perbanyak dzikir lisan.
  * *Ifrath (Berlebih):* **Jubn (الجُبْن)** — Takut berbicara kebenaran saat kemungkaran merajalela. *Kuratif:* Dikuatkan dengan pilar *Syajaa'ah* dan *Nashiihah*.

---

### Pilar #15: Hayaa' (الحَيَاء - Malu Syar'i)
* **Sub-Kelompok:** Suka Merendah (Introvert + Rasa)
* **Definisi Karakter:** Perasaan malu hakiki yang mencegah seorang hamba dari melanggar syariat Allah dan menabrak norma adab kesopanan.
* **Inspirasi Shahabat Nabi ﷺ:** **Utsman bin Affan radhiyallahu 'anhu**. Pribadi yang memiliki tingkat rasa malu begitu luhur hingga para malaikat pun merasa segan dan malu kepada beliau.
* **Dalil Otentik OpenBayan:**
  > « أَلَا أَسْتَحِي مِنْ رَجُلٍ تَسْتَحِي مِنْهُ الْمَلَائِكَةُ »  
  > *"Tidakkah aku merasa malu kepada seorang lelaki yang para malaikat pun merasa malu kepadanya?"*  
  > 📚 *(HR. Muslim No. 2401, Bab Keutamaan Utsman bin Affan)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Waqaahah (الوَقَاحَة)** — Muka tebal, tidak punya malu berbuat dosa di ruang publik. *Kuratif:* Tanamkan muraqabatullah sejak usia tamyiz.
  * *Ifrath (Berlebih):* **Duuniyyah (الدُوْنِيَّة)** — Minder patologis, takut tampil, tidak berani menyuarakan hak. *Kuratif:* Penguatan konsep diri beriman melalui pilar *'Izzah*.

---

### Pilar #16: Qanaa'ah (القَنَاعَة - Merasa Cukup)
* **Sub-Kelompok:** Suka Merendah (Introvert + Rasa)
* **Definisi Karakter:** Kelapangan hati menerima karunia rezeki dari Allah SWT tanpa ada rasa dengki terhadap kenikmatan yang diberikan kepada orang lain.
* **Inspirasi Shahabat Nabi ﷺ:** **Abu Dzar Al-Ghifari radhiyallahu 'anhu**. Sahabat yang hidup sangat bersahaja, tidak silau pada gemerlap perbendaharaan dunia, dan merasa cukup dengan bekal seorang musafir.
* **Dalil Otentik OpenBayan:**
  > « قَدْ أَفْلَحَ مَنْ أَسْلَمَ، وَرُزِقَ كَفَافًا، وَقَنَّعَهُ اللَّهُ بِمَا آتَاهُ »  
  > *"Sungguh sangat beruntung orang yang memeluk Islam, dianugerahi rezeki yang cukup, dan Allah karuniakan sifat qana'ah atas apa yang Dia berikan."*  
  > 📚 *(HR. Muslim No. 1054, Kitab Az-Zakah)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Thama' / Hasad (الطَّمَع)** — Serakah, tidak pernah puas, iri melihat rezeki tetangga. *Kuratif:* Melatih anak berinfaq dan melihat orang yang berada di bawahnya dalam urusan duniawi.
  * *Ifrath (Berlebih):* **Tawaakul / Kasal (التَّوَاكُل)** — Pasrah buta tanpa ikhtiar, enggan bekerja mencari nafkah halal. *Kuratif:* Integrasikan dengan pilar *Himmah* dan *'Aziimah*.

---

### Pilar #17: Tawaadhu' (التَّوَاضُع - Kerendahan Hati)
* **Sub-Kelompok:** Suka Merendah (Introvert + Rasa)
* **Definisi Karakter:** Sikap batin yang tidak memandang dirinya lebih mulia daripada orang lain, mudah menerima kebenaran dari siapa pun datangnya.
* **Inspirasi Shahabat Nabi ﷺ:** **Umar bin Al-Khattab radhiyallahu 'anhu**. Sebagai Amirul Mukminin penguasa dua imperium besar, beliau tetap memanggul karung gandum di punggungnya sendiri di kegelapan malam untuk diserahkan kepada janda miskin yang kelaparan.
* **Dalil Otentik OpenBayan:**
  > « وَمَا تَوَاضَعَ أَحَدٌ لِلَّهِ إِلَّا رَفَعَهُ اللَّهُ »  
  > *"Dan tidaklah seseorang bersikap rendah hati (tawadhu') karena Allah, melainkan Allah pasti akan meninggikan derajatnya."*  
  > 📚 *(HR. Muslim No. 2588, Kitab Al-Birr wash-Shilah)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Kibr (الكِبْر)** — Sombong, memandang remeh orang lain, menolak nasihat. *Kuratif:* Ajak anak berkhidmat melayani orang-orang lemah dan berziarah kubur.
  * *Ifrath (Berlebih):* **Mahaanah (المَهَانَة)** — Menghinakan diri di hadapan orang kaya atau pelaku maksiat. *Kuratif:* Kokohkan dengan pilar *'Izzah* Islamiyah.

---

## 3. Rubrik Observasi Bakat untuk Orang Tua & Pendidik (Rukun 3A)

| Rukun Observasi | Indikator Perilaku Otentik Anak | Catatan Guru / Orang Tua |
| :--- | :--- | :--- |
| **1. Suka (*Interest*)** | Menikmati suasana tenang, suka menggambar hening, peka terhadap keindahan adab, tidak tahan melihat orang lain menangis. | Menolak berbohong meskipun dalam situasi terdesak; menghargai barang milik orang lain. |
| **2. Bisa (*Ability*)** | Memiliki empati alami (*emotional intelligence*); mampu membaca suasana hati orang tua lewat ekspresi mikro wajah. | Mampu menahan diri dari amarah dan godaan jajan sembarangan. |
| **3. Bermanfaat (*Utility*)** | Menjadi penenang di rumah saat terjadi ketegangan; menjadi sahabat yang setia menjaga rahasia kawan; menjaga etika kesantunan. | Menjaga nama baik keluarga melalui keanggunan akhlaknya. |

---

## 4. Panduan Pendampingan Berdasarkan 4 Fase Usia Nabawiyah

### A. Fase Thufulah (0–7 Tahun: Mengisi Tangki Cinta Hati)
* Penuhi jiwa anak dengan pelukan, kelembutan, dan sentuhan fisik (*Bahasa Hati*).
* Jangan bentak atau labeli anak pemalu sebagai "penakut"; rasa malunya adalah modalitas fitrah kesucian.
* Jadilah teladan kejujuran: jangan pernah membohongi anak meskipun untuk menenangkannya saat menangis.

### B. Fase Tamyiz (7–10 Tahun: Menjaga Batas Aurat & Kesucian)
* Pisahkan tempat tidur anak laki-laki dan perempuan sesuai petunjuk hadits Nabi ﷺ.
* Ajarkan adab meminta izin (*isti'dzan*) saat memasuki kamar orang tua di tiga waktu aurat.
* Tumbuhkan rasa bangga dengan busana muslimah yang menutup aurat sempurna secara sukarela.

### C. Fase Murahaqah (10–15 Tahun: Menjaga Pandangan & Manajemen Syahwat)
* Berikan pendidikan *tazkiyatun nafs*: bahaya zina mata dan kerusakan pornografi terhadap qalb.
* Arahkan sensitivitas perasaannya ke dunia seni bernilai adab tinggi: kaligrafi, sastra Islam, puisi dakwah, arsitektur masjid.
* Fasilitasi pertemanan shalih yang saling menjaga kesucian adab pergaulan.

### D. Fase Syabab (15+ Tahun: Benteng Kesucian & Integritas Lembaga)
* Jadikan pemuda pemegang amanah kebendaharaan, audit internal, atau pengelola dana sosial umat.
* Dorong untuk segera menggenapkan separuh agama melalui pernikahan yang berkah bila telah memiliki kesiapan.

---

## 5. Pemetaan Rumpun Profesi & Jurusan Masa Depan

* **Profesi:** Pengelola Baitul Mal / Bendahara Amanah, Auditor Keuangan Syariah, Konselor Pernikahan, Sastrawan/Penulis Buku Akhlak, Arsitek Beradab, Kurator Warisan Sejarah Islam.
* **Rumpun Jurusan:** Akuntansi Syariah, Manajemen Keuangan Islam, Sastra Arab & Linguistik, Psikologi Konseling Islam, Ilmu Adab & Sejarah Peradaban Islam.

---

## 6. Tautan Konseptual Terkait
* [[Bakat]] — Taksonomi Lengkap Karakter Nabawiyah.
* [[Insan]] — Anatomi Ruh, Nafs, dan Qalb.
* [[Bahasa Hati]] — Seni Mengisi Tangki Cinta Anak.
* [[Tazkiyatun Nafs]] — Metodologi Pembersihan Jiwa dalam Islam.
"""

# ==============================================================================
# 4. MEMERINTAH.MD
# ==============================================================================
ARTICLES["Memerintah.md"] = """---
title: "Memerintah"
tags:
  - pkn
  - fitrah_bakat
  - memerintah
  - mempengaruhi
  - tb40
  - shahabat
---

# Bakat Memerintah / Mempengaruhi (التَّأْثِيْر - At-Ta'tsir)

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « كُلُّكُمْ رَاعٍ، وَكُلُّكُمْ مَسْئُولٌ عَنْ رَعِيَّتِهِ »
>
> *"Setiap kalian adalah pemimpin (penggembala), dan setiap kalian akan dimintai pertanggungjawaban atas apa yang dipimpinnya."*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Al-Bukhari No. 893 & Muslim No. 1829; Syarah Riyadush Shalihin (Juz 3 Hal. 412); Sunan Abi Dawud.  
> 💡 **Relevansi PKN:** Bakat Memerintah (*At-Ta'tsir*) adalah energi kepemimpinan ekstrovert yang menggerakkan gerbong dakwah, menegakkan amar ma'ruf nahi munkar, membela kaum mustadh'afin, dan mengambil keputusan strategis di garis terdepan.

---

## 1. Hakikat & Kedudukan Konseptual dalam Arsitektur PKN

Dalam sistematika Pendidikan Karakter Nabawiyah, **Bakat Memerintah / Mempengaruhi** lahir dari persilangan antara **Kutub Ekstrovert** (dorongan energi keluar menuju interaksi publik) dan **Dimensi Karsa / Jasad** (*Al-Hawa* yang disublimasikan menjadi ghirah dakwah pada jiwa ammarah).

Karakteristik dominan anak berbakat Memerintah:
* **Keberanian Tampil (*Presence*):** Percaya diri tinggi berbicara di depan orang banyak, berani mengambil risiko, tidak gentar menghadapi konfrontasi terbuka.
* **Naluri Mengatur & Melindungi:** Suka mengorganisir teman bermainnya, membagi tugas, membela kawan yang diintimidasi, dan mengarahkan tujuan kelompok.
* **Bukan Otoriter Diktator:** Kepemimpinan Nabawiyah (*Qiyadah Nabawiyah*) bukan penindasan ego, melainkan **Sayyidul Qaumi Khaadimuhum**—pemimpin sejati adalah pelayan paling depan bagi kaum yang dipimpinnya.

---

## 2. Tujuh Turunan Pilar Karakter TB40 & Inspirasi Shahabat Nabi ﷺ

Bakat Memerintah membawahi **7 Pilar Karakter Mulia (TB40)** yang terbagi ke dalam 3 sub-kelompok Level 18:

```mermaid
graph TD
    BM["Memerintah (At-Ta'tsir)"] --> G1["Sub 10: Suka Menguasai / Menertibkan"]
    BM --> G2["Sub 11: Suka Memotivasi / Mengarahkan"]
    BM --> G3["Sub 12: Suka Menolong & Berkorban"]

    G1 --> P18["#18 Syajaa'ah (Keberanian Ksatria)"]
    G1 --> P19["#19 Ghairah (Cemburu Membela Syariat)"]
    G1 --> P20["#20 Munaafasah (Fastabiqul Khairat)"]
    G2 --> P21["#21 Nashiihah (Tulus Membimbing)"]
    G2 --> P22["#22 Fashaahah (Fasih Artikulatif)"]
    G3 --> P23["#23 Nushrah (Membela Tertindas)"]
    G3 --> P24["#24 Juud (Dermawan Pemimpin)"]
```

### Pilar #18: Syajaa'ah (الشَّجَاعَة - Keberanian Ksatria)
* **Sub-Kelompok:** Suka Menguasai (Ekstrovert + Karsa)
* **Definisi Karakter:** Keteguhan jiwa menghadapi bahaya dan tantangan besar tanpa gentar demi membela kebenaran hakiki.
* **Inspirasi Shahabat Nabi ﷺ:** **Ali bin Abi Thalib radhiyallahu 'anhu**. Pemuda ksatria yang tanpa ragu tidur di ranjang Rasulullah ﷺ menggantikan beliau saat rumah dikepung para algojo Quraisy bersenjata lengkap, serta keberanian beliau meruntuhkan benteng Khaybar.
* **Dalil Otentik OpenBayan:**
  > « الْمُؤْمِنُ الْقَوِيُّ خَيْرٌ وَأَحَبُّ إِلَى اللَّهِ مِنَ الْمُؤْمِنِ الضَّعِيفِ، وَفِي كُلٍّ خَيْرٌ »  
  > *"Mukmin yang kuat lebih baik dan lebih dicintai oleh Allah daripada mukmin yang lemah, meskipun pada masing-masing ada kebaikan."*  
  > 📚 *(HR. Muslim No. 2664, Kitab Al-Qadar)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Jubn (الجُبْن)** — Pengecut, lari dari tanggung jawab. *Kuratif:* Latihan olahraga ketangkasan dan bela diri syar'i.
  * *Ifrath (Berlebih):* **Tahawwur (التَّهَوُّر)** — Nekat ugal-ugalan tanpa perhitungan. *Kuratif:* Wajib tunduk pada pilar *Hikmah* dan *Anaah*.

---

### Pilar #19: Ghairah (الغَيْرَة - Cemburu Membela Kehormatan Syariat)
* **Sub-Kelompok:** Suka Menguasai (Ekstrovert + Karsa)
* **Definisi Karakter:** Kebencian batin yang membuncah ketika aturan syariat Allah dilanggar, aurat keluarga dinistakan, atau martabat Islam direndahkan.
* **Inspirasi Shahabat Nabi ﷺ:** **Sa'ad bin 'Ubadah radhiyallahu 'anhu**. Beliau berkata dengan tegas mengenai pembelaan terhadap kehormatan keluarga, hingga Rasulullah ﷺ bersabda memuji kecemburuannya.
* **Dalil Otentik OpenBayan:**
  > « أَتَعْجَبُونَ مِنْ غَيْرَةِ سَعْدٍ؟ لَأَنَا أَغْيَرُ مِنْهُ، وَاللَّهُ أَغْيَرُ مِنِّي »  
  > *"Apakah kalian merasa heran dengan kecemburuan Sa'ad? Demi Allah, sungguh aku lebih cemburu daripadanya, dan Allah jauh lebih cemburu daripada diriku!"*  
  > 📚 *(HR. Al-Bukhari No. 6846 & Muslim No. 1499)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Diyaatsah (الدِّيَاثَة)** — Permisif, tidak peduli anggota keluarga bermaksiat. *Kuratif:* Tegakkan qowwamah ayah di rumah.
  * *Ifrath (Berlebih):* **Tasyaddud / Tajassus (التَّجَسُّس)** — Curiga berlebihan dan memata-matai privasi orang lain. *Kuratif:* Terapkan kaidah larangan tajassus (QS. Al-Hujurat: 12).

---

### Pilar #20: Munaafasah (المُنَافَسَة - Bersaing dalam Kebaikan)
* **Sub-Kelompok:** Suka Menguasai (Ekstrovert + Karsa)
* **Definisi Karakter:** Ambisi positif untuk menjadi yang terdepan dalam menorehkan amal kebajikan dan prestasi peradaban (*Fastabiqul Khairat*).
* **Inspirasi Shahabat Nabi ﷺ:** **Umar bin Al-Khattab radhiyallahu 'anhu**. Beliau senantiasa berlomba dengan Abu Bakar Ash-Shiddiq dalam berinfaq di jalan dakwah, seperti saat menyumbangkan separuh hartanya dalam Perang Tabuk.
* **Dalil Otentik OpenBayan:**
  > « وَفِي ذَٰلِكَ فَلْيَتَنَافَسِ الْمُتَنَافِسُونَ »  
  > *"Dan untuk yang demikian itu hendaknya orang-orang berlomba-lomba (mencapai surga dan keridhaan Allah)."*  
  > 📚 *(QS. Al-Muthaffifin: 26; Tafsir Ibnu Katsir 8/355)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Dzull / Qunuth (القُنُوْط)** — Patah arang, merasa diri pecundang. *Kuratif:* Berikan target kemenangan-kemenangan kecil (*small wins*).
  * *Ifrath (Berlebih):* **Hasad / Ghill (الحَسَد)** — Dengki, ingin menjatuhkan kawan agar dirinya juara sendiri. *Kuratif:* Didik untuk mendoakan keberkahan kawan (*Ghibthah*).

---

### Pilar #21: Nashiihah (النَّصِيْحَة - Tulus Membimbing)
* **Sub-Kelompok:** Suka Memotivasi (Ekstrovert + Karsa)
* **Definisi Karakter:** Keinginan tulus agar orang lain menjadi lebih baik, gemar memberi bimbingan, arahan, dan teguran yang membangun.
* **Inspirasi Shahabat Nabi ﷺ:** **Jarir bin Abdillah Al-Bajali radhiyallahu 'anhu**. Beliau membai'at Rasulullah ﷺ untuk senantiasa menegakkan shalat, menunaikan zakat, dan bersikap tulus memberi nasihat kepada setiap muslim.
* **Dalil Otentik OpenBayan:**
  > « الدِّينُ النَّصِيحَةُ، قُلْنَا: لِمَنْ؟ قَالَ: لِلَّهِ وَلِكِتَابِهِ وَلِرَسُولِهِ وَلِأَئِمَّةِ الْمُسْلِمِينَ وَعَامَّتِهِمْ »  
  > *"Agama ini adalah nasihat (ketulusan). Kami bertanya: Untuk siapa? Beliau bersabda: Untuk Allah, Kitab-Nya, Rasul-Nya, para pemimpin kaum muslimin, dan masyarakat umum."*  
  > 📚 *(HR. Muslim No. 55, Kitab Al-Iman)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Mudahanah (المُدَاهَنَة)** — Menjilat, mendiamkan kemungkaran demi cari aman. *Kuratif:* Tanamkan amar ma'ruf nahi munkar.
  * *Ifrath (Berlebih):* **Tanfiir / Ta'yir (التَّنْفِير)** — Menasihati di depan umum dengan kasar hingga mempermalukan. *Kuratif:* Nasihati empat mata dengan *Bahasa Hati*.

---

### Pilar #22: Fashaahah (الفَصَاحَة - Fasih Artikulatif)
* **Sub-Kelompok:** Suka Memotivasi (Ekstrovert + Karsa)
* **Definisi Karakter:** Kemampuan merangkai kata dan berorasi secara memikat, menyederhanakan gagasan rumit agar mudah dipahami dan menggerakkan massa.
* **Inspirasi Shahabat Nabi ﷺ:** **Hassan bin Tsabit radhiyallahu 'anhu**. Penyair resmi dakwah Rasulullah ﷺ yang orasi dan syairnya mampu meruntuhkan propaganda kaum musyrikin dengan dukungan Ruhul Qudus (Malaikat Jibril).
* **Dalil Otentik OpenBayan:**
  > « اهْجُهُمْ وَجِبْرِيلُ مَعَكَ »  
  > *"Bantahlah dan balaslah propaganda mereka (melalui syairmu), dan Jibril senantiasa menyertaimu!"*  
  > 📚 *(HR. Al-Bukhari No. 3213 & Muslim No. 2486)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **'Ujmah (العُجْمَة)** — Gagap mengungkapkan isi pikiran, kosa kata miskin. *Kuratif:* Latihan membaca nyaring dan bercerita (*storytelling*).
  * *Ifrath (Berlebih):* **Jidaal ‘Aqiim (الجِدَال)** — Pandai bersilat lidah, suka mendebat kusir demi gengsi. *Kuratif:* Peringatkan dengan hadits ancaman bagi ahli jidal.

---

### Pilar #23: Nushrah (النُّصْرَة - Membela Kaum Tertindas)
* **Sub-Kelompok:** Suka Menolong (Ekstrovert + Karsa)
* **Definisi Karakter:** Keberpihakan tegas dan aksi nyata membela orang yang teraniaya serta menghentikan kezaliman para penindas.
* **Inspirasi Shahabat Nabi ﷺ:** **Sa'ad bin Mu'adz radhiyallahu 'anhu**. Pemimpin kaum Anshar yang menjadi benteng pertahanan dakwah Rasulullah ﷺ di Madinah, hingga 'Arsy Allah berguncang saat beliau wafat.
* **Dalil Otentik OpenBayan:**
  > « انْصُرْ أَخَاكَ ظَالِمًا أَوْ مَظْلُومًا، فَقَالَ رَجُلٌ: يَا رَسُولَ اللَّهِ، أَنْصُرُهُ إِذَا كَانَ مَظْلُومًا، أَفَرَأَيْتَ إِذَا كَانَ ظَالِمًا كَيْفَ أَنْصُرُهُ؟ قَالَ: تَحْجُزُهُ عَنِ الظُّلْمِ فَإِنَّ ذَلِكَ نَصْرُهُ »  
  > *"Tolonglah saudaramu baik dia dalam keadaan berbuat zalim maupun dizalimi! Seorang sahabat bertanya: Bagaimana menolongnya jika dia zalim? Beliau bersabda: Engkau cegah dia dari berbuat zalim, itulah cara menolongnya!"*  
  > 📚 *(HR. Al-Bukhari No. 2444 & 6952)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Khidzlaan (الخِذْلَان)** — Apatis, membiarkan saudara dizalimi di depan mata. *Kuratif:* Tumbuhkan solidaritas ukhuwah Islamiyah.
  * *Ifrath (Berlebih):* **'Ashabiyah (العَصَبِيَّة)** — Membela kelompoknya secara membabi buta meski berada di pihak yang salah. *Kuratif:* Ikat loyalitas hanya kepada kebenaran syariat (*Al-Haqq*).

---

### Pilar #24: Juud (الجُوْد - Kedermawanan Pemimpin)
* **Sub-Kelompok:** Suka Menolong (Ekstrovert + Karsa)
* **Definisi Karakter:** Kelapangan tangan mengorbankan sumber daya, tenaga, dan harta pribadi demi menyukseskan misi kepemimpinan umat.
* **Inspirasi Shahabat Nabi ﷺ:** **Abdurrahman bin Auf radhiyallahu 'anhu**. Pemimpin saudagar muslim yang pernah menyedekahkan 700 unta bermuatan penuh bahan makanan untuk seluruh penduduk Madinah, serta mendanai berbagai ekspedisi jihad.
* **Dalil Otentik OpenBayan:**
  > « مَا نَقَصَتْ صَدَقَةٌ مِنْ مَالٍ، وَمَا زَادَ اللَّهُ عَبْدًا بِعَفْوٍ إِلَّا عِزًّا »  
  > *"Tidaklah sedekah itu mengurangi harta, dan tidaklah Allah menambah bagi seorang hamba yang pemaaf melainkan kemuliaan."*  
  > 📚 *(HR. Muslim No. 2588, Kitab Al-Birr wash-Shilah)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Bukhl (البُخْل)** — Kikir, pelit mengeluarkan modal untuk perjuangan. *Kuratif:* Latihan sedekah harian secara sembunyi-sembunyi.
  * *Ifrath (Berlebih):* **Riya' / Sum'ah (الرِّيَاء)** — Dermawan demi pujian gelar pahlawan atau mencari pengaruh politik kotor. *Kuratif:* Murnikan niat ikhlas lillahi ta'ala.

---

## 3. Rubrik Observasi Bakat untuk Orang Tua & Pendidik (Rukun 3A)

| Rukun Observasi | Indikator Perilaku Otentik Anak | Catatan Guru / Orang Tua |
| :--- | :--- | :--- |
| **1. Suka (*Interest*)** | Secara alami mengambil inisiatif memimpin barisan, mengatur permainan teman-temannya, berani berbicara mewakili kelompok. | Tidak betah menjadi penonton pasif; ingin selalu terlibat di garis depan pergerakan. |
| **2. Bisa (*Ability*)** | Memiliki kharisma yang ditaati kawan-kawannya; mampu menghentikan perselisihan antar teman dengan ketegasannya. | Mampu berbicara runtut, percaya diri, dan memotivasi orang lain. |
| **3. Bermanfaat (*Utility*)** | Menggunakan kekuatannya untuk melindungi anak yang lebih lemah dari perundungan (*bullying*); mengorganisir kegiatan sosial. | Gerak kepemimpinannya membawa ketertiban dan keadilan di lingkungannya. |

---

## 4. Panduan Pendampingan Berdasarkan 4 Fase Usia Nabawiyah

### A. Fase Thufulah (0–7 Tahun: Jangan Patahkan Keberanian Anak)
* Jangan matikan ego kepemimpinannya dengan label negatif ("kamu suka ngatur-ngatur!").
* Berikan peran kecil di rumah: memimpin doa sebelum makan, memanggil adik untuk shalat.
* Tanamkan empati agar kekuatannya tidak melukai kawan sebayanya.

### B. Fase Tamyiz (7–10 Tahun: Kepemimpinan Berbasis Keteladanan Adab)
* Tanamkan bahwa pemimpin sejati adalah yang paling disiplin menaati aturan syariat.
* Jadikan anak ketua regu saat berkemah atau imam shalat di antara kawan sebayanya.
* Latih seni retorika santun: membedakan antara ketegasan (*Syajaa'ah*) dan kekasaran (*Ghilzhah*).

### C. Fase Murahaqah (10–15 Tahun: Mentoring Tanggung Jawab Nyata)
* Libatkan dalam kepanitiaan dakwah remaja masjid atau OSIS sekolah Islam.
* Ajarkan adab syura (musyawarah): mendengarkan masukan anggota sebelum memutuskan.
* Berikan sanksi mendidik jika ia menyalahgunakan kekuasaan untuk menekan rekannya.

### D. Fase Syabab (15+ Tahun: Panglima Muda Peradaban)
* Siapkan menjadi organisator dakwah kampus, pimpinan ekspedisi kemanusiaan, atau politisi muslim berintegritas.
* Dampingi dengan ulama berilmu agar kepemimpinannya selalu berlandaskan fatwa syar'i yang kokoh.

---

## 5. Pemetaan Rumpun Profesi & Jurusan Masa Depan

* **Profesi:** Komandan Militer/Kepolisian, Diplomat/Duta Besar, Advokat/Pengacara Pembela Hak Umat, Eksekutif Perusahaan (CEO), Manajer Kampanye Dakwah, Juru Bicara Publik.
* **Rumpun Jurusan:** Ilmu Hukum & Syariah, Ilmu Pemerintahan & Hubungan Internasional, Manajemen Kepemimpinan, Ilmu Komunikasi & Jurnalistik, Akademi Militer/Kepolisian.

---

## 6. Tautan Konseptual Terkait
* [[Bakat]] — Peta Lengkap Arsitektur Bakat PKN.
* [[Bahasa Tangan]] — Batasan Tegas Penegakan Disiplin Syar'i.
* [[Murahaqah]] — Etape Penggemblengan Tanggung Jawab Taklif.
"""

# ==============================================================================
# 5. BEKERJA SAMA.MD
# ==============================================================================
ARTICLES["Bekerja Sama.md"] = """---
title: "Bekerja Sama"
tags:
  - pkn
  - fitrah_bakat
  - bekerja_sama
  - tb40
  - shahabat
---

# Bakat Bekerja Sama (التَّعَامُل - At-Ta'amul)

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ »
>
> *"Dan tolong-menolonglah kalian dalam (mengerjakan) kebajikan dan takwa, dan jangan tolong-menolong dalam berbuat dosa dan permusuhan."*
>
> 📚 **Sumber Rujukan OpenBayan:** QS. Al-Ma'idah: 2; Tafsir Ibnu Katsir (Juz 3 Hal. 7); Shahih Al-Bukhari No. 481 (Perumpamaan Mukmin Bagaikan Bangunan yang Kokoh).  
> 💡 **Relevansi PKN:** Bakat Bekerja Sama (*At-Ta'amul*) adalah perekat sosial umat (*networking & harmony*) yang menyatukan ragam potensi yang berserak menjadi shaff perjuangan yang kokoh dan harmonis.

---

## 1. Hakikat & Kedudukan Konseptual dalam Arsitektur PKN

Dalam arsitektur Pendidikan Karakter Nabawiyah, **Bakat Bekerja Sama** berakar pada persilangan antara **Kutub Ekstrovert** (terbuka menjalin relasi sosial) dan **Dimensi Cipta / Akal** (*Al-'Aql* pada jiwa lawwamah yang mendambakan harmoni dan keadilan).

Karakteristik dominan anak berbakat Bekerja Sama:
* **Relasional & Supel:** Mudah bergaul dengan orang baru, pandai mencairkan suasana kaku, senang berada dalam kebersamaan kelompok.
* **Anti-Konflik Destruktif & Berorientasi Solusi:** Memiliki radar keadilan (*'adaalah*), menjunjung tinggi sportivitas dan janji (*wafaa'*), serta suka mendamaikan pihak yang berselisih.
* **Bukan Kompromi Murahan:** Sifat kompromi dan kerukunan dalam Islam dibatasi oleh tauhid; tidak boleh berkompromi dalam perkara prinsipil akidah dan keharaman syariat.

---

## 2. Delapan Turunan Pilar Karakter TB40 & Inspirasi Shahabat Nabi ﷺ

Bakat Bekerja Sama membawahi **8 Pilar Karakter Mulia (TB40)** yang terbagi ke dalam 3 sub-kelompok Level 18:

```mermaid
graph TD
    BS["Bekerja Sama (At-Ta'amul)"] --> G1["Sub 13: Menggunakan Relasi yang Ada"]
    BS --> G2["Sub 14: Membuka Relasi Baru"]
    BS --> G3["Sub 15: Mengeratkan Ikatan Kasih"]

    G1 --> P25["#25 Ta'aawun (Sinergi Beramal)"]
    G1 --> P26["#26 Ulfah (Persatuan Hati)"]
    G1 --> P27["#27 'Adaalah (Keadilan Proporsional)"]
    G1 --> P28["#28 Wafaa' (Menepati Janji)"]
    G2 --> P29["#29 Muzaah (Canda Mengakrabkan)"]
    G2 --> P30["#30 Basyaasyah (Wajah Ramah Berseri)"]
    G3 --> P31["#31 Rifq (Lemah Lembut)"]
    G3 --> P32["#32 Mahabbah (Cinta Karena Allah)"]
```

### Pilar #25: Ta'aawun (التَّعَاوُن - Sinergi Kolektif)
* **Sub-Kelompok:** Menggunakan Relasi yang Ada (Ekstrovert + Cipta)
* **Definisi Karakter:** Kemampuan berkolaborasi dan berbagi peran secara sinergis demi mencapai target dakwah bersama.
* **Inspirasi Shahabat Nabi ﷺ:** **Kaum Muhajirin dan Kaum Anshar**. Monumen kolaborasi terbesar sepanjang sejarah saat kaum Anshar menyediakan modal, tanah, dan hunian, sementara kaum Muhajirin menggerakkan keahlian perniagaan dan dakwah di Madinah.
* **Dalil Otentik OpenBayan:**
  > « الْمُؤْمِنُ لِلْمُؤْمِنِ كَالْبُنْيَانِ يَشُدُّ بَعْضُهُ بَعْضًا »  
  > *"Seorang mukmin dengan mukmin lainnya bagaikan satu bangunan yang saling mengokohkan satu sama lain."*  
  > 📚 *(HR. Al-Bukhari No. 481 & Muslim No. 2585)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **'Inaad / Ananiyah (الأَنَانِيَّة)** — Individualis, egois, tidak mau berbagi peran. *Kuratif:* Libatkan dalam proyek kelompok yang mensyaratkan ketergantungan antar anggota.
  * *Ifrath (Berlebih):* **Ittikaaliyah (الاتِّكَالِيَّة)** — Ketergantungan kronis, tidak bisa bekerja mandiri. *Kuratif:* Berikan tugas personal yang menuntut pertanggungjawaban individual.

---

### Pilar #26: Ulfah (الاُلْفَة - Mengharmoniskan Hati)
* **Sub-Kelompok:** Menggunakan Relasi yang Ada (Ekstrovert + Cipta)
* **Definisi Karakter:** Kemampuan merangkul ragam latar belakang manusia dan menyatukan frekuensi hati dalam kebersamaan iman.
* **Inspirasi Shahabat Nabi ﷺ:** **Abdullah bin Salam radhiyallahu 'anhu** (pendeta Yahudi yang masuk Islam dan menjadi jembatan perdamaian) & **Abu Musa Al-Asy'ari radhiyallahu 'anhu**.
* **Dalil Otentik OpenBayan:**
  > « الأَرْوَاحُ جُنُودٌ مُجَنَّدَةٌ، فَمَا تَعَارَفَ مِنْهَا ائْتَلَفَ، وَمَا تَنَاكَرَ مِنْهَا اخْتَلَفَ »  
  > *"Ruh-ruh manusia bagaikan pasukan yang berbaris; yang saling mengenal di antaranya akan merasa cocok dan bersatu (i'talafa), sedangkan yang saling asing akan berselisih."*  
  > 📚 *(HR. Al-Bukhari No. 3336 & Muslim No. 2638)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Namiimah / Furqah (الفُرْقَة)** — Gemar memecah belah dan mengelompokkan kawan (*clique*). *Kuratif:* Ingatkan dengan dosa besar adu domba.
  * *Ifrath (Berlebih):* **Talfiiq / Muhaadanah (المُهَادَنَة)** — Menoleransi kemungkaran demi menjaga keharmonisan semu. *Kuratif:* Tegakkan batas amar ma'ruf nahi munkar.

---

### Pilar #27: 'Adaalah (العَدَالَة - Keadilan Proporsional)
* **Sub-Kelompok:** Menggunakan Relasi yang Ada (Ekstrovert + Cipta)
* **Definisi Karakter:** Sikap tegak lurus menempatkan sesuatu pada tempatnya, tidak berat sebelah karena suka atau benci.
* **Inspirasi Shahabat Nabi ﷺ:** **Umar bin Al-Khattab radhiyallahu 'anhu (Al-Faruq)**. Beliau bahkan menegakkan keadilan hukum kepada anak gubernur Mesir (Amr bin Al-Ash) yang memukul rakyat biasa suku Qibthi.
* **Dalil Otentik OpenBayan:**
  > « إِنَّ الْمُقْسِطِينَ عِنْدَ اللَّهِ عَلَى مَنَابِرَ مِنْ نُورٍ عَنْ يَمِينِ الرَّحْمَنِ »  
  > *"Sesungguhnya orang-orang yang berlaku adil di sisi Allah berada di atas mimbar-mimbar cahaya di sebelah kanan Ar-Rahman."*  
  > 📚 *(HR. Muslim No. 1827, Kitab Al-Imarah)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Zhulm / Haif (الظُّلْم)** — Curang, pilih kasih terhadap kawan dekat. *Kuratif:* Latihan menjadi wasit adil dalam permainan anak.
  * *Ifrath (Berlebih):* **Jumuud (الجُمُوْد)** — Kaku secara hukum tanpa mempertimbangkan aspek rahmah dan maslahat. *Kuratif:* Gabungkan dengan pilar *Rifq* dan *Rahmah*.

---

### Pilar #28: Wafaa' (الوَفَاء - Setia Menepati Janji)
* **Sub-Kelompok:** Menggunakan Relasi yang Ada (Ekstrovert + Cipta)
* **Definisi Karakter:** Keteguhan memegang komitmen, kesepakatan, dan sumpah setia walaupun dalam situasi yang merugikan dirinya.
* **Inspirasi Shahabat Nabi ﷺ:** **Hudzaifah bin Al-Yaman dan ayahnya Al-Yaman radhiyallahu 'anhuma**. Ketika ditawan kaum musyrikin menjelang Perang Badar, mereka berjanji tidak akan ikut berperang bersama Nabi ﷺ jika dibebaskan. Rasulullah ﷺ memerintahkan mereka menepati janji tersebut dan tidak mengizinkan mereka ikut Perang Badar!
* **Dalil Otentik OpenBayan:**
  > « نَفِي لَهُمْ بِعَهْدِهِمْ، وَنَسْتَعِينُ اللَّهَ عَلَيْهِمْ »  
  > *"Kita penuhi janji kita kepada mereka, dan kita memohon pertolongan kepada Allah untuk menghadapi mereka!"*  
  > 📚 *(HR. Muslim No. 1787, Kitab Al-Jihad was-Siyar)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Ghadr / Khiyanah (الغَدْر)** — Ingkar janji, khianat kesepakatan. *Kuratif:* Ajarkan bahwa tanda munafik adalah bila berjanji ia ingkar.
  * *Ifrath (Berlebih):* **Wafaa' fil Ma'shiyah (الوَفَاءُ بِالمَعْصِيَة)** — Setia pada ikrar yang melanggar syariat. *Kuratif:* Tegakkan kaidah: *"Tidak ada ketaatan dalam maksiat kepada Khalik."*

---

### Pilar #29: Muzaah (المُزَاح - Canda Mengakrabkan)
* **Sub-Kelompok:** Membuka Relasi Baru (Ekstrovert + Cipta)
* **Definisi Karakter:** Keluwesan mencairkan suasana dengan canda tawa yang mubah, membahagiakan hati kawan tanpa ada unsur dusta dan penghinaan.
* **Inspirasi Shahabat Nabi ﷺ:** **Nu'aiman bin 'Amr radhiyallahu 'anhu**. Sahabat yang gemar melontarkan lelucon cerdas yang membuat Rasulullah ﷺ dan para shahabat tertawa bahagia hingga tampak gigi geraham beliau.
* **Dalil Otentik OpenBayan:**
  > « قَالُوا: يَا رَسُولَ اللَّهِ، إِنَّكَ تُدَاعِبُنَا! قَالَ: إِنِّي لَا أَقُولُ إِلَّا حَقًّا »  
  > *"Para shahabat berkata: Wahai Rasulullah, sesungguhnya engkau mencandai kami! Beliau bersabda: Sesungguhnya aku tidak mengatakan (dalam bercanda) kecuali kebenaran."*  
  > 📚 *(HR. At-Tirmidzi No. 1990, dinyatakan Shahih; Syarah Asy-Syamail Al-Muhammadiyah)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **'Ubus / Quhuth (العُبُوْس)** — Wajah selalu cemberut, kaku, menakutkan orang lain. *Kuratif:* Latihan tersenyum dan menyapa ramah.
  * *Ifrath (Berlebih):* **Katsratul Dhahik (كَثْرَةُ الضَّحِكِ)** — Terlalu banyak tertawa terbahak-bahak hingga mematikan kepekaan hati (*qaswatul qalb*). *Kuratif:* Puasa tawa dan dzikrul maut.

---

### Pilar #30: Basyaasyah (البَشَاشَة - Wajah Ceria Ramah)
* **Sub-Kelompok:** Membuka Relasi Baru (Ekstrovert + Cipta)
* **Definisi Karakter:** Kehangatan ekspresi wajah yang selalu berseri-seri dan murah senyum saat menyambut kedatangan orang lain.
* **Inspirasi Shahabat Nabi ﷺ:** **Jarir bin Abdillah Al-Bajali radhiyallahu 'anhu**. Beliau mengisahkan kehangatan interaksinya dengan Rasulullah ﷺ yang senantiasa tersenyum setiap kali memandang wajahnya.
* **Dalil Otentik OpenBayan:**
  > « تَبَسُّمُكَ فِي وَجْهِ أَخِيكَ لَكَ صَدَقَةٌ »  
  > *"Senyum manismu di hadapan saudaramu adalah sedekah bagimu."*  
  > 📚 *(HR. At-Tirmidzi No. 1956, dinyatakan Hasan Gharib; Shahih Ibnu Hibban)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Jafaa' (الجَفَاء)** — Sikap dingin, membuang muka saat berpapasan. *Kuratif:* Budayakan salam, senyum, dan sapa di rumah.
  * *Ifrath (Berlebih):* **Riya' / Tasannu' (التَّصَنُّع)** — Senyum palsu diplomatik untuk menutupi kebusukan niat. *Kuratif:* Luruskan keikhlasan batin lillahi ta'ala.

---

### Pilar #31: Rifq (الرِّفْق - Lemah Lembut Pergaulan)
* **Sub-Kelompok:** Mengeratkan Ikatan Kasih (Ekstrovert + Cipta)
* **Definisi Karakter:** Kelembutan dalam tutur kata dan perbuatan, memilih cara yang paling mudah dan tidak menyulitkan orang lain.
* **Inspirasi Shahabat Nabi ﷺ:** **Anas bin Malik radhiyallahu 'anhu**. Beliau menjadi pelayan Rasulullah ﷺ selama 10 tahun dan menyatakan bahwa Rasulullah ﷺ tidak pernah sekalipun membentaknya atau berkata *"mengapa engkau lakukan ini?"*.
* **Dalil Otentik OpenBayan:**
  > « إِنَّ الرِّفْقَ لَا يَكُونُ فِي شَيْءٍ إِلَّا زَانَهُ، وَلَا يُنْزَعُ مِنْ شَيْءٍ إِلَّا شَانَهُ »  
  > *"Sesungguhnya kelembutan tidaklah berada pada sesuatu melainkan pasti akan menghiasinya (membuatnya indah), dan tidaklah kelembutan dicabut dari sesuatu melainkan pasti akan memperburuknya."*  
  > 📚 *(HR. Muslim No. 2594, Kitab Al-Birr wash-Shilah)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Unf / Ghilzhah (العُنْف)** — Kasar, suka membanting barang, membentak. *Kuratif:* Terapi wudhu saat marah dan larangan berbicara saat emosi tinggi.
  * *Ifrath (Berlebih):* **Dhina' / Huun (الهُوْن)** — Terlalu lembek hingga tidak berani menegur kemungkaran fatal. *Kuratif:* Padukan dengan pilar *Ghairah*.

---

### Pilar #32: Mahabbah (المَحَبَّة - Mempererat Cinta Iman)
* **Sub-Kelompok:** Mengeratkan Ikatan Kasih (Ekstrovert + Cipta)
* **Definisi Karakter:** Kemampuan menumbuhkan dan memelihara ikatan cinta persaudaraan yang murni karena Allah (Ukhuwah Fillah).
* **Inspirasi Shahabat Nabi ﷺ:** **Salman Al-Farisi & Abu Ad-Darda' radhiyallahu 'anhuma** yang dipersaudarakan oleh Nabi ﷺ dan saling menasihati dalam kebaikan dengan penuh cinta.
* **Dalil Otentik OpenBayan:**
  > « لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ »  
  > *"Tidak sempurna iman salah seorang di antara kalian sampai ia mencintai bagi saudaranya apa yang ia cintai bagi dirinya sendiri."*  
  > 📚 *(HR. Al-Bukhari No. 13 & Muslim No. 45)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Bughdh / Jafwah (البُغْض)** — Hati penuh dendam dan permusuhan. *Kuratif:* Mendoakan kebaikan bagi saudaranya di belakangnya.
  * *Ifrath (Berlebih):* **'Isyq Muharram (العِشْق)** — Keterikatan emosional buta yang menggeser cinta mutlak kepada Allah. *Kuratif:* Kokohkan tauhid mahabbah hanya kepada Allah.

---

## 3. Rubrik Observasi Bakat untuk Orang Tua & Pendidik (Rukun 3A)

| Rukun Observasi | Indikator Perilaku Otentik Anak | Catatan Guru / Orang Tua |
| :--- | :--- | :--- |
| **1. Suka (*Interest*)** | Sangat bersemangat saat diajak bermain bersama; suka mengajak kawan baru bergabung; tidak betah bermain sendirian. | Ceria membagikan mainan dan makanan kepada kawan-kawannya. |
| **2. Bisa (*Ability*)** | Mampu menjadi mediator alami saat kawan-kawannya berebut mainan; pandai bernegosiasi secara adil. | Disukai oleh teman-teman dari berbagai tingkatan usia. |
| **3. Bermanfaat (*Utility*)** | Menjadi perekat ukhuwah di kelas; mengorganisir bantuan untuk kawan yang sakit; menyemarakkan kegiatan jamaah. | Menghadirkan suasana persaudaraan yang hangat di lingkungannya. |

---

## 4. Panduan Pendampingan Berdasarkan 4 Fase Usia Nabawiyah

### A. Fase Thufulah (0–7 Tahun: Belajar Berbagi Mainan)
* Latih anak berbagi makanan dan mainan tanpa paksaan kasar; jelaskan nikmatnya makan bersama.
* Ajak berinteraksi dengan teman sebaya di taman atau masjid untuk melatih *basyaasyah*.
* Dampingi saat terjadi pertengkaran perebutan mainan; ajarkan meminta maaf dan memaafkan.

### B. Fase Tamyiz (7–10 Tahun: Menjalin Ukhuwah Shalat Berjamaah)
* Biasakan shalat berjamaah di masjid untuk menanamkan filosofi shaff yang lurus dan rapat.
* Kenalkan konsep menepati janji bermain dan adab bertamu ke rumah kawan.
* Ajarkan olahraga beregu (futsal, basket, kasti) untuk melatih sinergi *ta'aawun*.

### C. Fase Murahaqah (10–15 Tahun: Pengelolaan Organisasi Remaja)
* Dorong aktif dalam tim marawis, panitia qurban, atau karang taruna masjid.
* Ajarkan resolusi konflik: bagaimana menengahi dua kawan yang berselisih secara objektif (*'adaalah*).
* Ingatkan bahaya *peer pressure* (tekanan teman sebaya) yang mengarah pada kemaksiatan.

### D. Fase Syabab (15+ Tahun: Pembangun Jaringan Dakwah & Bisnis)
* Kembangkan kemampuannya dalam diplomasi dakwah, public relations, dan jejaring wirausaha kemitraan.
* Bekali dengan pemahaman fiqih muamalah syirkah (musyarakah, mudharabah) agar kerja samanya berkah.

---

## 5. Pemetaan Rumpun Profesi & Jurusan Masa Depan

* **Profesi:** Public Relations (Humas), Mediator/Juru Damai, Manajer Sumber Daya Manusia (HRD), Pengembang Kemitraan Strategis, Event Organizer (EO) Dakwah, Diplomat Hubungan Luar Negeri.
* **Rumpun Jurusan:** Ilmu Komunikasi, Hubungan Internasional, Psikologi Industri & Organisasi, Manajemen Sumber Daya Manusia, Sosiologi Islam.

---

## 6. Tautan Konseptual Terkait
* [[Bakat]] — Taksonomi Lengkap 40 Pilar Karakter.
* [[Bahasa Lisan]] — Komunikasi Nasihat dan Tabayyun.
* [[Imunitas Sosial]] — Membentengi Anak dari Pengaruh Negatif Lingkungan.
"""

# ==============================================================================
# 6. MELAYANI.MD
# ==============================================================================
ARTICLES["Melayani.md"] = """---
title: "Melayani"
tags:
  - pkn
  - fitrah_bakat
  - melayani
  - khidmah
  - tb40
  - shahabat
---

# Bakat Melayani (الخِدْمَة - Al-Khidmah)

> [!quote] Dalil & Rujukan Nabawiyah Utama
> **Naskah:**  
> « سَيِّدُ الْقَوْمِ خَادِمُهُمْ فِي السَّفَرِ »
>
> *"Pemimpin suatu kaum adalah orang yang paling banyak melayani mereka dalam perjalanan."*
>
> 📚 **Sumber Rujukan OpenBayan:** HR. Al-Baihaqi dalam *Syu'abul Iman* No. 8419; Syarah Shahih Muslim Imam An-Nawawi (Juz 12 Hal. 188); Dinyatakan Hasan oleh Syaikh Al-Albani.  
> 💡 **Relevansi PKN:** Bakat Melayani (*Al-Khidmah*) adalah perwujudan tertinggi dari sifat rahmah dan pengorbanan tanpa pamrih (*itsaar*), menjadi benteng penjaga amanah dan perisai kerahasiaan dakwah Islam.

---

## 1. Hakikat & Kedudukan Konseptual dalam Arsitektur PKN

Dalam disiplin Pendidikan Karakter Nabawiyah, **Bakat Melayani** adalah hasil persilangan antara **Kutub Ekstrovert** (fokus aksi tercurah kepada kebutuhan orang lain) dan **Dimensi Rasa / Hati** (*Al-Qalb* pada jiwa muthmainnah yang dipenuhi kasih sayang ilahiah).

Karakteristik khas anak berbakat Melayani:
* **Altruistik & Berjiwa Sosial Tinggi:** Spontan bergerak membantu orang yang kerepotan tanpa diminta, tidak tega melihat penderitaan orang lain.
* **Amanah & Penjaga Rahasia:** Sangat setia memegang amanah, mampu menutupi aib kawan (*satr*), sabar dan teliti dalam tugas-tugas pendampingan.
* **Bukan Berjiwa Budak (*Riqqun*):** Melayani dalam Islam bukanlah kehinaan perbudakan, melainkan **Al-Itsaar & Khidmah Mubarakah**—kemuliaan derajat yang dicontohkan para nabi dan rasul yang melayani umatnya siang dan malam.

---

## 2. Delapan Turunan Pilar Karakter TB40 & Inspirasi Shahabat Nabi ﷺ

Bakat Melayani membawahi **8 Pilar Karakter Mulia (TB40)** yang terbagi ke dalam 3 sub-kelompok Level 18:

```mermaid
graph TD
    BMel["Melayani (Al-Khidmah)"] --> G1["Sub 16: Melayani dengan Memberi"]
    BMel --> G2["Sub 17: Melayani dengan Menjaga"]
    BMel --> G3["Sub 18: Melayani dengan Mengalah & Sabar"]

    G1 --> P33["#33 Rahmah (Belas Kasih Murni)"]
    G1 --> P34["#34 Itsaar (Mendahulukan Saudara)"]
    G2 --> P35["#35 Kitmaanus Sirr (Menjaga Rahasia)"]
    G2 --> P36["#36 Satr (Menutup Aib Sesama)"]
    G3 --> P37["#37 Amaanah (Bertanggung Jawab)"]
    G3 --> P38["#38 Anaah (Tenang & Cermat)"]
    G3 --> P39["#39 Hilm (Pemaaf Lapang Dada)"]
    G3 --> P40["#40 Shabr (Tabah Bertahan)"]
```

### Pilar #33: Rahmah (الرَّحْمَة - Kasih Sayang Murni)
* **Sub-Kelompok:** Melayani dengan Memberi (Ekstrovert + Rasa)
* **Definisi Karakter:** Pancaran belas kasih tulus yang mendorong tindakan nyata untuk menolong kaum dhu'afa, anak yatim, dan orang-orang yang terluka.
* **Inspirasi Shahabat Nabi ﷺ:** **Abu Bakar Ash-Shiddiq radhiyallahu 'anhu**. Beliau dipuji oleh Rasulullah ﷺ sebagai sosok umat yang paling penyayang kepada umat ini (*Arhamu Ummati bi Ummati*), yang memerdekakan budak-budak tertindas seperti Bilal bin Rabah.
* **Dalil Otentik OpenBayan:**
  > « الرَّاحِمُونَ يَرْحَمُهُمُ الرَّحْمَنُ، ارْحَمُوا مَنْ فِي الأَرْضِ يَرْحَمْكُمْ مَنْ فِي السَّمَاءِ »  
  > *"Orang-orang yang penyayang niscaya akan disayangi oleh Dzat Yang Maha Penyayang (Ar-Rahman). Sayangilah siapa saja yang ada di bumi, niscaya Dzat yang ada di langit akan menyayangi kalian!"*  
  > 📚 *(HR. At-Tirmidzi No. 1924, dinyatakan Shahih; Sunan Abi Dawud No. 4941)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Qaswah (القَسْوَة)** — Hati keras membatu, tega melihat penderitaan orang lain. *Kuratif:* Mengusap kepala anak yatim dan memberi makan orang miskin.
  * *Ifrath (Berlebih):* **Khawwar (الخَوَر)** — Lembek hingga tidak tega menegakkan sanksi syariat yang adil. *Kuratif:* Imbangi dengan pilar *'Adaalah* dan *Ghairah*.

---

### Pilar #34: Itsaar (الاِيْثَار - Altruisme Syar'i)
* **Sub-Kelompok:** Melayani dengan Memberi (Ekstrovert + Rasa)
* **Definisi Karakter:** Kerelaan mendahulukan kebutuhan saudara seiman di atas kepentingan diri sendiri, meskipun dirinya sedang dalam kesempitan.
* **Inspirasi Shahabat Nabi ﷺ:** **Abu Thalhah Al-Anshari & istrinya Ummu Sulaim radhiyallahu 'anhuma**. Mereka mematikan lampu dan berpura-pura makan demi membiarkan tamu Rasulullah ﷺ makan hidangan yang hanya tersisa sedikit sampai kenyang, hingga turun ayat pujian dari langit: QS. Al-Hasyr: 9.
* **Dalil Otentik OpenBayan:**
  > « وَيُؤْثِرُونَ عَلَىٰ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌ »  
  > *"Dan mereka lebih mengutamakan (orang-orang Muhajirin) atas diri mereka sendiri, sekalipun mereka sedang berada dalam kesusahan/kekurangan."*  
  > 📚 *(QS. Al-Hasyr: 9; HR. Al-Bukhari No. 3798 & Muslim No. 2054)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Syuhh / Bukhl (الشُّحّ)** — Sangat kikir dan takut miskin. *Kuratif:* Latihan sedekah barang yang paling dicintai.
  * *Ifrath (Berlebih):* **Dhai'atul 'Iyal (ضَيْعَةُ العِيَالِ)** — Berinfaq habis-habisan ke luar hingga menelantarkan nafkah wajib anak dan istri. *Kuratif:* Dahulukan urutan nafkah keluarga sesuai sabda Nabi ﷺ: *"Mulailah dari orang yang menjadi tanggunganmu."*

---

### Pilar #35: Kitmaanus Sirr (كِتْمَانُ السِّرِّ - Menjaga Rahasia)
* **Sub-Kelompok:** Melayani dengan Menjaga (Ekstrovert + Rasa)
* **Definisi Karakter:** Kemampuan luar biasa mengunci informasi rahasia yang diamanahkan kepadanya agar tidak bocor dan menimbulkan madharat.
* **Inspirasi Shahabat Nabi ﷺ:** **Hudzaifah bin Al-Yaman radhiyallahu 'anhu (Shahibu Sirri Rasulillah)**. Beliau dipercaya memegang daftar rahasia nama-nama orang munafik di Madinah, dan sampai akhir hayatnya beliau tidak pernah membocorkannya kepada siapapun, termasuk kepada Khalifah Umar bin Khattab!
* **Dalil Otentik OpenBayan:**
  > « اسْتَعِينُوا عَلَى قَضَاءِ حَوَائِجِكُمْ بِالْكِتْمَانِ، فَإِنَّ كُلَّ ذِي نِعْمَةٍ مَحْسُودٌ »  
  > *"Bantulah kelancaran penyelesaian hajat-hajat kalian dengan menjaga kerahasiaan, karena sesungguhnya setiap orang yang memiliki nikmat itu ada yang mendengkinya."*  
  > 📚 *(HR. Ath-Thabrani dalam Al-Kabir No. 13334; Al-Bani dalam Silsilah Ash-Shahihah No. 1453)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Ifsyaa'us Sirr (إِفْشَاءُ السِّرّ)** — Mulut ember, membocorkan rahasia penting demi sensasi. *Kuratif:* Peringatkan tentang dosa khianat amanah.
  * *Ifrath (Berlebih):* **Kithmanul Haqq (كِتْمَانُ الحَقِّ)** — Menyembunyikan persaksian kebenaran yang wajib diungkap di pengadilan. *Kuratif:* Tegakkan pilar *Shidq*.

---

### Pilar #36: Satr (السَّتْر - Menutup Aib Saudara)
* **Sub-Kelompok:** Melayani dengan Menjaga (Ekstrovert + Rasa)
* **Definisi Karakter:** Menahan diri dari menceritakan atau menyebarkan aib dan kekhilafan saudaranya sesama muslim demi menjaga martabatnya.
* **Inspirasi Shahabat Nabi ﷺ:** **Abu Bakar & Umar radhiyallahu 'anhuma** yang selalu berusaha menasihati secara tertutup dan menutupi aib kaum muslimin dari cemoohan publik.
* **Dalil Otentik OpenBayan:**
  > « وَمَنْ سَتَرَ مُسْلِمًا سَتَرَهُ اللَّهُ فِي الدُّنْيَا وَالآخِرَةِ »  
  > *"Dan barangsiapa menutupi (aib) seorang muslim, niscaya Allah akan menutupi aibnya di dunia dan akhirat."*  
  > 📚 *(HR. Muslim No. 2699, Kitab Adz-Dzikr wad-Du'a)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Fadhihah / Tasy-hir (الفَضِيْحَة)** — Gemar memviralkan aib dan membongkar kesalahan orang lain. *Kuratif:* Renungi hadits ancaman bahwa Allah akan membongkar aibnya di rumahnya sendiri.
  * *Ifrath (Berlebih):* **Iqrārul Munkar (إِقْرَارُ المُنْكَر)** — Melindungi pelaku kriminal berbahaya yang merugikan publik atas nama menutup aib. *Kuratif:* Laporkan kepada pihak berwenang sesuai kaidah hukum syar'i.

---

### Pilar #37: Amaanah (الاَمَانَة - Tanggung Jawab Terpercaya)
* **Sub-Kelompok:** Melayani dengan Mengalah (Ekstrovert + Rasa)
* **Definisi Karakter:** Sikap bertanggung jawab penuh menunaikan setiap tugas, titipan harta, dan janji tanpa pernah berkhianat.
* **Inspirasi Shahabat Nabi ﷺ:** **Abu Ubaidah bin Al-Jarrah radhiyallahu 'anhu (Aminul Ummah)**. Rasulullah ﷺ bersabda di hadapan delegasi Najran bahwa beliau akan mengirimkan seorang yang benar-benar terpercaya, lalu beliau memegang tangan Abu Ubaidah.
* **Dalil Otentik OpenBayan:**
  > « إِنَّ لِكُلِّ أُمَّةٍ أَمِينًا، وَإِنَّ أَمِينَنَا أَيَّتُهَا الأُمَّةُ أَبُو عُبَيْدَةَ بْنُ الجَرَّاحِ »  
  > *"Sesungguhnya setiap umat memiliki orang yang paling terpercaya (amin), dan sesungguhnya orang yang paling terpercaya di kalangan umat kita ini adalah Abu Ubaidah bin Al-Jarrah."*  
  > 📚 *(HR. Al-Bukhari No. 3744 & Muslim No. 2419)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Khiyanah (الخِيَانَة)** — Mengabaikan tugas, korupsi dana titipan. *Kuratif:* Awasi dengan audit ketat dan tanamkan hisab akhirat.
  * *Ifrath (Berlebih):* **Hamlul Ma La Yuthaq (حَمْلُ مَا لَا يُطَاقُ)** — Mengambil semua beban amanah hingga fisik dan mental hancur (*burnout*). *Kuratif:* Pelajari seni delegasi tugas dengan pilar *Ta'aawun*.

---

### Pilar #38: Anaah (الاَنَاة - Ketenangan & Ketelitian)
* **Sub-Kelompok:** Melayani dengan Mengalah (Ekstrovert + Rasa)
* **Definisi Karakter:** Ketenangan sikap yang mendalam, tidak tergesa-gesa dalam mengambil keputusan, menimbang maslahat dan madharat secara matang.
* **Inspirasi Shahabat Nabi ﷺ:** **Al-Asyaj (Ashaj Abdul Qais) radhiyallahu 'anhu**. Ketika rombongannya tiba di Madinah dan langsung berlari menemui Nabi ﷺ, Al-Asyaj dengan tenang merapikan hewan tunggangannya, mandi, mengenakan pakaian terbaiknya, baru kemudian menghadap Rasulullah ﷺ dengan penuh wibawa.
* **Dalil Otentik OpenBayan:**
  > « إِنَّ فِيكَ خَصْلَتَيْنِ يُحِبُّهُمَا اللَّهُ: الْحِلْمُ، وَالأَنَاةُ »  
  > *"Sesungguhnya pada dirimu terdapat dua sifat yang sangat dicintai oleh Allah: Kesantunan (Al-Hilm) dan Ketenangan yang tidak tergesa-gesa (Al-Anaah)."*  
  > 📚 *(HR. Muslim No. 17 & 18, Kitab Al-Iman; Riyadush Shalihin Tahqiq Al-Fahl No. 631)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **'Ajalah (العَجَلَة)** — Grusa-grusu, terburu-buru, ceroboh. *Kuratif:* Hadits: *"Ketergesa-gesaan itu berasal dari setan."*
  * *Ifrath (Berlebih):* **Tawaani / Batha' (التَّوَانِي)** — Lamban berlebihan hingga kehilangan momentum emas. *Kuratif:* Pacu dengan pilar *'Aziimah*.

---

### Pilar #39: Hilm (الحِلْم - Pemaaf Santun Lapang Dada)
* **Sub-Kelompok:** Melayani dengan Mengalah (Ekstrovert + Rasa)
* **Definisi Karakter:** Kemampuan menahan amarah dan tetap bersikap santun serta memaafkan orang yang berbuat kasar kepadanya, padahal ia sanggup membalas.
* **Inspirasi Shahabat Nabi ﷺ:** **Al-Ahnaf bin Qais radhiyallahu 'anhu**. Tokoh tabi'in senior yang menjadi perumpamaan bangsa Arab dalam sifat santun (*Ahlamu minal Ahnaf*); ketika seseorang memaki dan mengikutinya berjam-jam, beliau hanya berkata tenang di dekat gerbang kampungnya: *"Wahai saudaraku, selesaikanlah makianmu di sini, agar orang-orang di kampungku tidak mendengar dan memukulmu!"*
* **Dalil Otentik OpenBayan:**
  > « لَيْسَ الشَّدِيدُ بِالصُّرَعَةِ، إِنَّمَا الشَّدِيدُ الَّذِي يَمْلِكُ نَفْسَهُ عِنْدَ الغَضَبِ »  
  > *"Bukanlah orang kuat itu yang menang dalam bergulat, melainkan orang kuat sejati adalah yang mampu mengendalikan dirinya saat marah."*  
  > 📚 *(HR. Al-Bukhari No. 6114 & Muslim No. 2609)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Hadad / Ghadhab (الغَضَب)** — Cepat naik darah, meledak-ledak, pendendam. *Kuratif:* Ajarkan teknik meredam amarah (duduk, berbaring, wudhu).
  * *Ifrath (Berlebih):* **Dzull (الذُّلّ)** — Membiarkan kemungkaran merajalela karena takut dianggap tidak santun. *Kuratif:* Imbangi dengan ketegasan *Syajaa'ah*.

---

### Pilar #40: Shabr (الصَّبْر - Ketabahan Melayani Umat)
* **Sub-Kelompok:** Melayani dengan Mengalah (Ekstrovert + Rasa)
* **Definisi Karakter:** Daya tahan batin yang kokoh menghadapi keletihan, cercaan, dan hambatan berat dalam melayani kemaslahatan umat manusia.
* **Inspirasi Shahabat Nabi ﷺ:** **Keluarga Yasir (Ammar, Sumayyah, Yasir) radhiyallahu 'anhum & Khabbab bin Al-Aratt**. Ketabahan luar biasa di bawah terik matahari Makkah menanggung siksaan kaum musyrikin demi mempertahankan kalimat Tauhid.
* **Dalil Otentik OpenBayan:**
  > « صَبْرًا يَا آلَ يَاسِرٍ، فَإِنَّ مَوْعِدَكُمُ الْجَنَّةُ »  
  > *"Bersabarlah wahai keluarga Yasir, karena sesungguhnya tempat yang dijanjikan bagi kalian adalah Surga!"*  
  > 📚 *(Al-Mustadrak Al-Hakim No. 5646, dinyatakan Shahih; Fathul Bari karya Ibnu Hajar 7/46)*
* **Diagnosis Deviasi:**
  * *Tafrith (Lalai):* **Jaza' / Taskhuth (الجَزَع)** — Berkeluh kesah, menyalahkan takdir saat tertimpa musibah. *Kuratif:* Tanamkan keimanan pada qadha dan qadar.
  * *Ifrath (Berlebih):* **Istislam lil Batil (الاسْتِسْلَام)** — Pasrah dizalimi musuh tanpa ada ikhtiar melepaskan diri. *Kuratif:* Bangkitkan tekad perlawanan syar'i dengan *Nushrah*.

---

## 3. Rubrik Observasi Bakat untuk Orang Tua & Pendidik (Rukun 3A)

| Rukun Observasi | Indikator Perilaku Otentik Anak | Catatan Guru / Orang Tua |
| :--- | :--- | :--- |
| **1. Suka (*Interest*)** | Secara spontan membantu merapikan piring kotor, membawakan barang belanjaan ibu, melayani minuman untuk tamu. | Merasa sangat bahagia saat melihat orang yang dibantunya tersenyum lega. |
| **2. Bisa (*Ability*)** | Memiliki kesabaran tinggi mendampingi adik kecil atau orang lanjut usia; sangat teliti dan rapi dalam menjaga barang titipan. | Mampu menahan emosi saat temannya berbuat salah kepadanya. |
| **3. Bermanfaat (*Utility*)** | Menjadi andalan keluarga dan sekolah dalam urusan logistik dan pelayanan kemanusiaan; penjaga rahasia yang paling amanah. | Memberikan rasa aman dan ketenangan bagi lingkungannya. |

---

## 4. Panduan Pendampingan Berdasarkan 4 Fase Usia Nabawiyah

### A. Fase Thufulah (0–7 Tahun: Mengasah Naluri Melayani)
* Apresiasi setiap bantuan kecilnya (mengambilkan handuk ayah, membuang sampah ke tempatnya).
* Jangan anggap melayani sebagai hukuman ("karena nakal, kamu bersihkan lantai!"); jadikan melayani sebagai kehormatan beramal shalih.
* Bacakan kisah keteladanan Anas bin Malik melayani Rasulullah ﷺ dengan penuh cinta.

### B. Fase Tamyiz (7–10 Tahun: Khidmah Tamu & Masjid)
* Libatkan dalam memuliakan tamu (*ikramud dhaif*): menyiapkan hidangan dan membukakan pintu dengan senyum.
* Ajarkan adab membersihkan rumah ibadah (menjadi laskar pembersih masjid).
* Latih amanah memegang uang saku titipan belanja secara presisi.

### C. Fase Murahaqah (10–15 Tahun: Pelayanan Sosial & Medis Dasar)
* Ikutkan dalam kegiatan relawan bencana alam, dapur umum qurban, atau palang merah remaja.
* Ajarkan keterampilan pertolongan pertama pada kecelakaan (P3K) dan perawatan orang sakit.
* Tanamkan kedalaman *kitmaanus sirr*: jangan pernah membicarakan masalah pribadi orang yang sedang ditolongnya.

### D. Fase Syabab (15+ Tahun: Pengabdi Umat & Khadimul Ummah)
* Siapkan menjadi pengelola lembaga amil zakat, dokter/paramedis kemanusiaan, atau administrator yayasan sosial.
* Tanamkan prinsip agung: *"Orang yang paling dicintai Allah adalah yang paling bermanfaat bagi manusia."*

---

## 5. Pemetaan Rumpun Profesi & Jurusan Masa Depan

* **Profesi:** Dokter Spesialis / Tenaga Medis Kemanusiaan, Pekerja Sosial / Relawan SAR, Pengelola Lembaga Zakat & Wakaf, Administrator Rahasia Negara / Notaris, Konselor Rehabilitasi Sosial, Manajer Layanan Pelanggan (Customer Service Excellence).
* **Rumpun Jurusan:** Kedokteran & Keperawatan, Ilmu Kesejahteraan Sosial, Manajemen Zakat & Wakaf, Psikologi Klinis, Ilmu Hukum & Kenotariatan, Administrasi Publik.

---

## 6. Tautan Konseptual Terkait
* [[Bakat]] — Induk Peta Bakat 40 Pilar Karakter.
* [[Insan]] — Pembagian Jiwa dan Tujuan Penciptaan Manusia.
* [[Bahasa Hati]] — Pendidikan Cinta dan Ketulusan Melayani.
* [[Bank Studi Kasus]] — Rekam Jejak Kasus Pengasuhan Berbasis Bakat.
"""

def main():
    print("Memulai penulisan 6 artikel sub-bakat PKN...")
    for filename, content in ARTICLES.items():
        filepath = os.path.join(BAKAT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as fp:
            fp.write(content)
        chars = len(content)
        lines = len(content.splitlines())
        words = len(content.split())
        print(f"  [BERHASIL] {filename:18s} -> {chars:,} karakter | {words:,} kata | {lines} baris")
    print("Semua 6 artikel sub-bakat telah diperkaya dan disimpan.")

if __name__ == "__main__":
    main()

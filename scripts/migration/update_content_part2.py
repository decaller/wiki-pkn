"""
Script part 2: Fitrah, Karakter, Bakat, and Perkembangan
"""

import os

CONTENT_BASE = "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi"

def write_file(rel_path, title, content):
    full_path = os.path.join(CONTENT_BASE, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    doc = f"""---
title: "{title}"
---

{content.strip()}
"""
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Updated: {full_path}")

FITRAH_CONTENT = """# Fitrah (Karakter)

Dalam Pendidikan Karakter Nabawiyah (PKN), karakter bukanlah sesuatu yang dicetak secara paksa dari luar (*behavioral conditioning*), melainkan penumbuhan benih fitrah yang telah diinstalasi oleh Allah pada setiap anak manusia sejak di alam rahim.

> *"Maka hadapkanlah wajahmu dengan lurus kepada agama (Islam); (sesuai) fitrah Allah disebabkan Dia telah menciptakan manusia menurut (fitrah) itu. Tidak ada perubahan pada ciptaan Allah. (Itulah) agama yang lurus, tetapi kebanyakan manusia tidak mengetahui."* (QS. Ar-Rum: 30)

## Dekonstruksi Paradigma Kertas Kosong

Pendidikan modern sering bertumpu pada teori *Tabula Rasa* (John Locke), yang memandang anak bagaikan kertas putih kosong yang pasif dan bebas digambari oleh lingkungannya. PKN menolak pandangan ini:

* **Paradigma Kertas Kosong:** Berorientasi pada penjejalkan materi (*stuffing*), penyeragaman kaku, dan pembentukan perilaku mekanis. Berisiko melukai fitrah dan memicu krisis kedewasaan (*Delayed Akil*).
* **Paradigma Fitrah:** Memandang anak sebagai benih super unggul yang membawa cetak biru kebaikan (tauhid, akal, dan potensi peran). Tugas pendidik adalah bertindak sebagai "Petani Fitrah" yang menyiram, memupuk, dan membersihkan gulma agar potensi itu mekar sempurna.

## Empat Dimensi Karakter Utama

1. **[[Iman]]:** Fondasi vertikal yang mengikat hati dengan Allah melalui rasa cinta (*mahabbah*), takut (*khauf*), dan harap (*raja'*).
2. **[[Belajar]]:** Kapasitas nalar dan rasa ingin tahu untuk memahami ayat-ayat kauniyah dan qauliyah melalui adab dan uji coba (*tajribah*).
3. **[[Bakat]]:** Keunikan potensi motorik, kognitif, dan afektif yang dirancang untuk peran kontribusi nyata di masyarakat.
4. **[[Perkembangan]]:** Tahapan pematangan jiwa sesuai ritme usia (Thufulah, Tamyiz, Murahaqah, hingga Syabab/Mukallaf).
"""

IMAN_CONTENT = """# Karakter Iman

Karakter Iman adalah fondasi paling mendasar dalam Pendidikan Karakter Nabawiyah (PKN). Seluruh bangunan ilmu pengetahuan dan keahlian bakat akan menjadi rapuh atau bahkan destruktif jika tidak berdiri di atas kokohnya tauhid dan kecintaan kepada Allah Azza wa Jalla.

> Dari Jundub bin Abdillah radhiyallahu 'anhu, ia berkata:  
> *"Dahulu kami bersama Nabi ﷺ saat kami masih pemuda menjelang baligh (fityan hazawirah). Kami belajar iman sebelum kami belajar Al-Qur'an (ilmu), kemudian kami belajar Al-Qur'an sehingga bertambahlah iman kami dengannya."* (HR. Ibnu Majah & Thabrani)

## Kaidah Penumbuhan Iman Anak

1. **Mendahulukan Iman Sebelum Ilmu:** Membangun kecintaan dan persepsi positif tentang Allah sebelum membebani anak dengan aturan syariat atau hafalan yang berat.
2. **Mengisi [[Tangki Cinta]]:** Anak yang tidak merasakan cinta dari orang tuanya di dunia nyata akan kesulitan memahami konsep kasih sayang (*Rahman & Rahim*) Allah.
3. **Keteladanan Nyata:** Iman diserap melalui atmosfer keshalihan di rumah, kehangatan hubungan suami-istri, dan konsistensi ibadah kedua orang tua.

## Pilar Karakter Iman Utama

* **Mahabbah:** Kecintaan yang mendalam kepada Allah dan Rasul-Nya melebihi segala sesuatu.
* **Shidq (Kejujuran):** Keselarasan antara keyakinan hati, perkataan lisan, dan perbuatan nyata.
* **Tawakkal:** Sandaran mutlak kepada takdir dan pertolongan Allah setelah menuntaskan ikhtiar terbaik.
"""

TANGKI_CINTA_CONTENT = """# Tangki Cinta

Tangki Cinta adalah metafora bagi wadah kebutuhan emosional dan rasa keberhargaan diri yang ada di dalam batin setiap anak. Dalam PKN, tangki cinta yang terisi penuh merupakan bahan bakar utama bagi lahirnya kesadaran beramal secara sukarela tanpa paksaan.

## Prinsip "Koneksi Sebelum Koreksi"

Orang tua tidak berhak menuntut ketaatan dan disiplin sebelum memastikan tangki cinta anak terisi penuh. Mengoreksi anak saat tangki cintanya kosong bagaikan menyalakan mesin kendaraan tanpa bahan bakar—hanya akan menghasilkan gesekan kasar dan kerusakan mesin jiwa.

## 5 Bahasa Cinta untuk Mengisi Tangki

1. **Kata-Kata Apresiasi (*Words of Affirmation*):** Pujian tulus, doa yang dilafazkan di depan anak, dan pengakuan atas usahanya.
2. **Waktu Berkualitas (*Quality Time*):** Kehadiran utuh tanpa distraksi gawai, mendengarkan celoteh anak dengan tatapan mata hangat.
3. **Hadiah Bermakna (*Receiving Gifts*):** Tanda kasih spontan yang tidak dijadikan alat suap atau imbalan bersyarat.
4. **Pelayanan Kasih (*Acts of Service*):** Bantuan tulus saat anak membutuhkan pendampingan, merawat saat sakit.
5. **Sentuhan Fisik (*Physical Touch*):** Pelukan hangat, ciuman di kening, tepukan bahu, dan elusan lembut di kepala.

## Tanda Tangki Cinta Kosong

* Anak mencari perhatian dengan perilaku merusak (*acting out*) atau tantrum berkepanjangan.
* Menarik diri, pemurung, dan enggan diajak berkomunikasi.
* Mudah terpengaruh oleh validasi semu di media sosial atau pergaulan bebas di luar rumah.
"""

BELAJAR_CONTENT = """# Karakter Belajar

Karakter Belajar adalah kapasitas fitrah nalar anak untuk menyerap kebenaran, menumbuhkan rasa ingin tahu (*syaghaf*), dan memahami hukum-hukum Allah di alam semesta (*Sunnatullah*).

## Menghidupkan Budaya Tajribah (Eksperimen)

Pendidikan Nabawiyah tidak mengurung anak di dalam ruang kelas statis untuk sekadar menghafal definisi demi nilai ujian. Masa keemasan karakter belajar berada pada **Fase Tamyiz (7 - 10 Tahun)** di mana anak berhak:

* **Melakukan Uji Coba (*Trial and Error*):** Belajar dari kegagalan tanpa takut dicela atau dimarahi.
* **Mengajukan Pertanyaan Kritis:** Didengarkan dan diajak berdialog menggunakan akal sehat (*Bahasa Lisan*).
* **Mengamati Alam Nyata:** Berinteraksi langsung dengan tanah, tumbuhan, hewan, dan fenomena sosial di sekitarnya.

## Adab Sebelum Ilmu

Karakter belajar menuntut penanaman adab sebelum penguasaan wawasan teknis. Imam Malik menasihatkan: *"Pelajarilah adab sebelum engkau mempelajari suatu ilmu."* Adab menuntun kecerdasan agar tidak berubah menjadi kesombongan intelektual (*Ahlur Ra'yi*).
"""

BAKAT_CONTENT = """# Karakter Bakat

Bakat (*Mauhibah*) dalam Pendidikan Karakter Nabawiyah adalah keunikan potensi bawaan lahir yang dianugerahkan Allah kepada setiap insan sebagai bekal khusus untuk menjalankan peran kekhalifahan di muka bumi.

## Rukun 3A Pemetaan Bakat

Suatu keunikan aktivitas dapat dikatakan sebagai bakat sejati apabila memenuhi tiga rukun fundamental:

1. **Suka (*Al-Hirsh / Enjoy*):** Anak menikmati proses melakukannya dengan antusiasme tinggi tanpa perlu disuruh.
2. **Bisa (*Al-Maqdari / Easy*):** Anak mampu menguasainya dengan cepat dan menunjukkan keunggulan alami dibanding rata-rata anak sebayanya.
3. **Berguna (*Al-Mufid / Excellent & Useful*):** Menghasilkan karya nyata yang memberikan manfaat luas bagi kemaslahatan umat.

## 6 Tipologi Bakat Berdasarkan Struktur Jiwa

* [[Bekerja Keras]] — Daya tahan dan ketangguhan fisik (Jasad Introvert).
* [[Memerintah]] — Kepemimpinan dan penggerak orang banyak (Jasad Ekstrovert).
* [[Berpikir]] — Analisis data, strategi, dan perumusan gagasan (Akal Introvert).
* [[Bekerja Sama]] — Diplomasi, komunikasi, dan kolaborasi tim (Akal Ekstrovert).
* [[Berperasaan]] — Kepekaan empati batin dan nilai moral (Hati Introvert).
* [[Melayani]] — Kedermawanan sosial dan aksi pengabdian (Hati Ekstrovert).
"""

BEKERJA_KERAS = """# Bakat Bekerja Keras

Bakat Bekerja Keras adalah kecondongan alami seseorang untuk mencurahkan energi fisik dan mental secara tekun dalam menuntaskan tugas-tugas berat dan menantang.

* **Sumber Jiwa:** Jiwa Ammarah (Jasad) berkarakter Introvert.
* **Ciri Khas:** Memiliki daya tahan (*grit*) tinggi, menyukai ketuntasan kerja, tidak mudah menyerah oleh keletihan fisik, dan merasa puas saat melihat pekerjaan selesai rapi.
* **Peran Kekhalifahan:** Eksekutor teknis, pembangun infrastruktur, penjaga ketahanan pangan, dan amil yang ulet.
"""

MEMERINTAH = """# Bakat Memerintah

Bakat Memerintah adalah potensi kepemimpinan alami untuk mengambil keputusan, mengarahkan orang lain, dan menegakkan keteraturan demi tercapainya visi bersama.

* **Sumber Jiwa:** Jiwa Ammarah (Jasad) berkarakter Ekstrovert.
* **Ciri Khas:** Memiliki karisma, wibawa (*waqaar*), ketegasan mengambil risiko, dan dorongan naluriah untuk memimpin kelompok.
* **Peran Kekhalifahan:** Panglima, manajer operasional, pemimpin organisasi, dan pengawal penegakan hukum/syariat.
"""

BERPIKIR = """# Bakat Berpikir

Bakat Berpikir adalah ketajaman akal dalam menganalisis data, menemukan benang merah antar gagasan, dan merumuskan solusi konseptual yang mendalam.

* **Sumber Jiwa:** Jiwa Lawwamah (Akal) berkarakter Introvert.
* **Ciri Khas:** Menyukai riset mandiri, membaca, merenung, membedah persoalan rumit, dan tidak mudah puas dengan jawaban dangkal.
* **Peran Kekhalifahan:** Ulama mujtahid, ilmuwan riset, perancang sistem, dan ahli strategi peradaban.
"""

BEKERJA_SAMA = """# Bakat Bekerja Sama

Bakat Bekerja Sama adalah kecakapan komunikasi sosial untuk membangun sinergi, merangkul perbedaan, dan menjaga keharmonisan tim.

* **Sumber Jiwa:** Jiwa Lawwamah (Akal) berkarakter Ekstrovert.
* **Ciri Khas:** Mudah bergaul, luwes berdiplomasi, pendengar yang baik, dan cakap menyelesaikan perselisihan antar pihak.
* **Peran Kekhalifahan:** Diplomat, humas, negosiator perdamaian, dan fasilitator jejaring umat.
"""

BERPERASAAN = """# Bakat Berperasaan

Bakat Berperasaan adalah sensitivitas batin untuk menangkap kondisi emosional orang lain, menjunjung tinggi nilai etika, dan mengekspresikan keindahan rasa.

* **Sumber Jiwa:** Jiwa Muthmainnah (Hati) berkarakter Introvert.
* **Ciri Khas:** Penuh empati, peka terhadap penderitaan sesama, mencintai keteraturan moral, dan memiliki cita rasa estetika tinggi.
* **Peran Kekhalifahan:** Konselor jiwa, pendidik adab, sastrawan hikmah, dan penjaga nilai spiritualitas.
"""

MELAYANI = """# Bakat Melayani

Bakat Melayani adalah kerelaan hati untuk mendedikasikan tenaga dan perhatian demi meringankan beban orang lain tanpa pamrih.

* **Sumber Jiwa:** Jiwa Muthmainnah (Hati) berkarakter Ekstrovert.
* **Ciri Khas:** Hangat, ramah, mengutamakan kebutuhan sesama (*itsar*), dan selalu sigap memberikan bantuan di garis depan.
* **Peran Kekhalifahan:** Relawan kemanusiaan, tenaga medis pengasih, pelayan umat, dan pegiat sosial kemasyarakatan.
"""

# ==============================================================================
# PERKEMBANGAN
# ==============================================================================

PERKEMBANGAN_CONTENT = """# Karakter Perkembangan

Karakter Perkembangan dalam Pendidikan Karakter Nabawiyah (PKN) memetakan evolusi jiwa anak dari lahir hingga mencapai kedewasaan penuh (*Akil Baligh*).

Prinsip dasarnya bersandar pada sabda Rasulullah ﷺ mengenai pengangkatan pena syariat (*Rufi'al Qalam*):
> *"Pena pencatat amal diangkat dari tiga golongan: dari orang tidur sampai ia bangun, dari anak kecil sampai ia baligh, dan dari orang gila sampai ia berakal."* (HR. Abu Dawud, Tirmidzi, dan Ahmad)

## 4 Fase Usia Nabawiyah

| Fase | Usia | Dimensi Utama | Batas Toleransi | Metode Pendidikan | Status Syariat |
|---|---|---|---|---|---|
| **[[Thufulah]]** | 0 - 7 Tahun | Karakter Iman | Paling Longgar | Bahasa Hati | Bebas Taklif (Hak Penuh) |
| **[[Tamyiz]]** | 7 - 10 Tahun | Karakter Belajar | Sedang | Bahasa Lisan | Pembiasaan Adab & Shalat |
| **[[Murahaqah]]** | 10 th - Baligh | Karakter Bakat | Paling Sempit | Bahasa Tangan | Disiplin Tegas Menjelang Baligh |
| **[[Syabab]]** | Pasca-Baligh | Mukallaf Penuh | Hubungan Dewasa | Kemitraan Dialog | Pemikul Beban Syariat Penuh |
"""

THUFULAH_CONTENT = """# Fase Thufulah (0 - 7 Tahun)

Fase Thufulah adalah masa keemasan penumbuhan **Karakter Iman (Mahabbah/Cinta)**. Pada fase ini, batas toleransi pengasuhan berada pada tingkat **paling longgar**.

## Hak-Hak Pokok Anak

1. **Hak Bermain Merdeka:** Anak berhak bermain tanpa dibebani kurikulum akademis kaku atau hafalan paksaan. Rasulullah ﷺ membiarkan cucu beliau menunggangi punggung beliau saat sujud dalam shalat berjamaah.
2. **Hak Penuntasan Egosentris:** Sifat egosentris di usia dini adalah keniscayaan perkembangan. Anak berhak dipenuhi keinginannya dan dimaafkan kesalahannya selama tidak membahayakan keselamatan diri dan orang lain.
3. **Hak Kasih Sayang Tanpa Syarat (Bahasa Hati):** Berhak mendapatkan tangki cinta yang penuh melalui pelukan, pujian, dan pemaafan luas.

## Larangan Mutlak di Usia 0 - 7 Tahun

* **Dilarang Hukuman Fisik:** Memberikan sanksi fisik atau bentakan keras di usia ini akan merusak fitrah dan menanamkan bibit kemunafikan.
* **Dilarang Beban Kewajiban Syariat:** Belum ada kewajiban shalat atau penuntutan adab secara kaku. Seluruh ketaatan dibangun atas dasar keteladanan visual dan cinta.
"""

TAMYIZ_CONTENT = """# Fase Tamyiz (7 - 10 Tahun)

Fase Tamyiz adalah momentum tumbuhnya nalar kritis (*mumayyiz*), di mana anak mulai mampu membedakan hal yang bermanfaat dan berbahaya bagi dirinya. Ini adalah masa keemasan penumbuhan **Karakter Belajar**.

## Hak dan Metode Pengasuhan

1. **Hak Eksplorasi & Trial and Error:** Anak berhak mencoba berbagai hal dan berbuat salah tanpa takut dicap bodoh atau dimarahi.
2. **Hak Edukasi Logika (Bahasa Lisan):** Komunikasi beralih ke dialog sebab-akibat yang masuk akal bagi anak. Hindari perintah sepihak tanpa argumentasi logis.
3. **Perintah Shalat Sebagai Pembiasaan Adab:** Berdasarkan hadits nabi, anak mulai diperintahkan belajar shalat di usia 7 tahun. Namun, perintah ini murni bersifat **pembiasaan**, sehingga anak sama sekali tidak boleh dipukul atau dihukum jika melalaikannya.
"""

MURAHAQAH_CONTENT = """# Fase Murahaqah (10 Tahun - Baligh)

Fase Murahaqah adalah masa transisi terakhir sebelum anak mencapai "Jatuh Tempo" pendidikan saat baligh. Ini adalah masa keemasan penumbuhan **Karakter Bakat & Kemandirian Fisik**. Toleransi pengasuhan berada pada tingkat **paling sempit**.

## Legalitas Disiplin Tegas (Bahasa Tangan)

Rasulullah ﷺ bersabda: *"Perintahkanlah anak-anakmu untuk mendirikan shalat ketika mereka berumur tujuh tahun, dan pukullah mereka karena melalaikannya ketika mereka berumur sepuluh tahun, serta pisahkanlah tempat tidur mereka."* (HR. Abu Dawud)

* **Ketentuan Hukuman:** Pukulan edukatif (*Bahasa Tangan*) hanya diperbolehkan atas dasar kelalaian shalat dan norma berat, tidak boleh mengenai wajah, tidak melukai fisik, dan harus dilandasi motivasi kasih sayang (*rahmah*), bukan kemarahan pribadi.
* **Pemisahan Tempat Tidur:** Menanamkan adab privasi, kesadaran seksualitas syar'i, dan kemandirian raga.
* **Penjurusan Bakat:** Menajamkan keunikan bakat anak melalui proyek nyata (*Project Based Learning*) atau pemagangan magang agar anak memiliki keahlian hidup mandiri.
"""

SYABAB_CONTENT = """# Fase Syabab (Pasca-Baligh / Mukallaf)

Ketika anak mengalami tanda biologis **Baligh** (mimpi basah bagi laki-laki, haid bagi perempuan), masa kanak-kanaknya secara syariat telah **selesai**. Mereka memasuki fase pemuda (*Syabab*) dan berstatus sebagai **Mukallaf** (pemikul beban hukum syariat penuh).

## Pergeseran Hubungan Orang Tua & Anak

1. **Kemitraan Orang Dewasa:** Mereka bukan lagi objek asuhan yang didikte, melainkan sesama mukallaf. Hubungan orang tua-anak beralih menjadi sahabat diskusi dan penasihat bijak.
2. **Pencatatan Amal Penuh:** Pena taklif telah aktif. Ketaatan mendatangkan pahala individu dan kemaksiatan dicatat sebagai dosa pribadi.
3. **Kemandirian Finansial Laki-Laki:** Secara syariat, kewajiban ayah memberi nafkah kepada anak laki-laki gugur saat ia baligh. Anak laki-laki didorong untuk mandiri mencari nafkah halal. Bantuan orang tua setelah baligh berstatus sebagai sedekah sukarela.

## Mencegah Sindrom "Delayed Akil"

Pola asuh modern kerap melakukan kesalahan terbalik: menekan anak secara kaku di masa TK/SD (sehingga hak bermainnya terampas), namun memanjakan anak saat SMA/kuliah sehingga mereka tumbuh menjadi "anak besar yang manja" (*Delayed Akil*). PKN mengembalikan alur ini agar kematangan mental (*Akil*) dicapai beriringan dengan kedewasaan fisik (*Baligh*).
"""

print("Writing Fitrah, Bakat, and Perkembangan files...")
write_file("Insan/Fitrah (Karakter).md", "Fitrah (Karakter)", FITRAH_CONTENT)
write_file("Insan/Fitrah (Karakter)/Iman.md", "Iman", IMAN_CONTENT)
write_file("Insan/Fitrah (Karakter)/Iman/Tangki Cinta.md", "Tangki Cinta", TANGKI_CINTA_CONTENT)
write_file("Insan/Fitrah (Karakter)/Belajar.md", "Belajar", BELAJAR_CONTENT)
write_file("Insan/Fitrah (Karakter)/Bakat.md", "Bakat", BAKAT_CONTENT)
write_file("Insan/Fitrah (Karakter)/Bakat/Bekerja Keras.md", "Bekerja Keras", BEKERJA_KERAS)
write_file("Insan/Fitrah (Karakter)/Bakat/Memerintah.md", "Memerintah", MEMERINTAH)
write_file("Insan/Fitrah (Karakter)/Bakat/Berpikir.md", "Berpikir", BERPIKIR)
write_file("Insan/Fitrah (Karakter)/Bakat/Bekerja Sama.md", "Bekerja Sama", BEKERJA_SAMA)
write_file("Insan/Fitrah (Karakter)/Bakat/Berperasaan.md", "Berperasaan", BERPERASAAN)
write_file("Insan/Fitrah (Karakter)/Bakat/Melayani.md", "Melayani", MELAYANI)

write_file("Insan/Fitrah (Karakter)/Perkembangan.md", "Perkembangan", PERKEMBANGAN_CONTENT)
write_file("Insan/Fitrah (Karakter)/Perkembangan/Thufulah.md", "Thufulah", THUFULAH_CONTENT)
write_file("Insan/Fitrah (Karakter)/Perkembangan/Tamyiz.md", "Tamyiz", TAMYIZ_CONTENT)
write_file("Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md", "Murahaqah", MURAHAQAH_CONTENT)
write_file("Insan/Fitrah (Karakter)/Perkembangan/Syabab.md", "Syabab", SYABAB_CONTENT)

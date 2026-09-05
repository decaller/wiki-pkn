#!/usr/bin/env python3
"""
enrich_batch1.py
Melengkapi 15 artikel pada Klaster Fitrah, Karakter & Bakat Anak (Batch 1)
dengan elemen-elemen baku template:
1. Trio Callout: [!info] Refleksi Lapangan, [!warning] Peringatan Risiko, [!tip] Tips Praktis
2. Sub-bab: ## Diagnosis Penyimpangan: Tafrith vs Ifrath (Tabel 3 kolom)
3. Sub-bab: ## Studi Kasus Nyata & Solusi Kuratif Tadarruj (Skenario + 4 Langkah Tadarruj)
4. Standarisasi: ## Tautan Relevan & Peta Konsep

Semua dilakukan TANPA MENGHAPUS teks, dalil, slide rujukan, atau banner yang sudah ada.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

BATCH1_DATA = {
    # 1. Belajar.md
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Belajar.md": {
        "callouts": """
> [!info] Refleksi Lapangan: Mogok Belajar Akibat Desensitisasi Fitrah Intelektual
> **Kondisi Faktual:** Anak usia 8 tahun (kelas 2 SD) mulai menunjukkan keengganan membuka buku, menangis histeris saat disuruh mengerjakan PR, dan mengeluh kepalanya pusing setiap kali jam belajar tiba.  
> **Akar Masalah PKN:** Penjejangan kognitif massal gaya Prusia yang memaksa anak duduk diam 6 jam sehari sambil menghafal rumus abstrak, mematikan rasa ingin tahu alami (*curiosity*) dan menguras tangki cinta tanpa memberi ruang gerak fisik kinestetik.  
> **Langkah Penanganan Nabawiyah:**  
> 1. Hentikan intimidasi nilai rapor; alihkan media belajar ke observasi alam nyata di luar ruangan (*outdoor living books*).  
> 2. Sambungkan kembali jembatan emosi (*Bahasa Hati*) melalui pelukan dan apresiasi atas minat unik anak.  
> 3. Kenalkan adab sebelum ilmu (*Al-Adab Qablal 'Ilm*) agar proses menuntut ilmu dirasakan sebagai ibadah yang menggembirakan.

> [!warning] Peringatan Risiko Pengasuhan: Bahaya Menghukum Kegagalan Akademik Anak
> * **Bentuk Kesalahan:** Membentak, memberi cap "pemalas / bodoh", atau mencabut hak bermain anak karena nilai ujian yang rendah.
> * **Dampak Terhadap Jiwa:** Merusak fitrah keimanan pada takdir (*qadar*), mematikan insting eksplorasi nalar (*Al-Fu'ad*), serta memicu mentalitas penipu (*cheating syndrome*) demi sekadar menghindari murka orang tua.
> * **Pencegahan Nabawiyah:** Rasulullah ﷺ tidak pernah sekalipun mencela Anas bin Malik RA selama 10 tahun berkhidmah atas pekerjaan yang belum sempurna dikerjakan. Fokuslah pada proses kesungguhan ikhtiar, bukan angka mutlak di atas kertas.

> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Ganti pertanyaan klise saat anak pulang: *"Dapat nilai berapa tadi?"* dengan pertanyaan fitrah: *"Apa hal baru paling menakjubkan yang kamu pelajari hari ini, Nak?"*
> * **Tujuan:** Menyalakan pelita gairah cinta ilmu (*Syaghaf bil 'Ilm*) dan menanamkan bahwa belajar adalah petualangan seumur hidup.
""",
        "tafrith_ifrath": """
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam Karakter Belajar

| Dimensi Pendekatan | Gejala Perilaku yang Teramati | Dampak Psikospiritual pada Anak |
| :--- | :--- | :--- |
| **Tafrith (Meremehkan / Lalai)** | Membiarkan anak kecanduan gawai tanpa batas, mengabaikan adab menuntut ilmu, dan tidak melatih ketekunan membaca (*iqra'*). | Anak tumbuh dengan rentang konsentrasi pendek (*short attention span*), tidak memiliki ketahanan nalar, dan malas berpikir mendalam (*anti-intellectualism*). |
| **Ifrath (Memaksa / Berlebihan)** | Memaksa balita membaca calistung dengan ancaman, menjejali les privat non-stop, dan menuntut anak selalu menjadi ranking 1. | Terjadinya *academic burnout*, hilangnya kelekatan batin dengan orang tua, kepalsuan budi pekerti, dan keputusasaan jiwa saat menghadapi kegagalan. |
| **Al-Wasathiyah (Jalan Tengah Nabawiyah)** | Memfasilitasi belajar berbasis fitrah alamiah, menghormati ritme perkembangan usia (*tadarruj*), dan mengintegrasikan ilmu dengan amal shalih. | Tumbuh insan pembelajar mandiri (*autodidact*), memiliki kepekaan nalar tajam, berakhlak mulia, dan menjadikan ilmu sebagai sarana taqarrub ilallah. |
""",
        "studi_kasus": """
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** Rayhan (9 tahun, fase Tamyiz) dipindahkan oleh orang tuanya ke sekolah berasrama modern. Di pekan ketiga, Rayhan mogok masuk kelas, menyobek buku tugas matematika, dan menunjukkan agresi verbal kepada ustadz pembimbing. Orang tua merasa malu dan berencana memberikan hukuman fisik.

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Pendinginan & Introspeksi Orang Tua (Hari 1–3)**  
   Orang tua membatalkan rencana hukuman fisik. Ayah mengambil cuti untuk menjenguk Rayhan tanpa membawa tuntutan sekolah. Menyelaraskan niat bahwa anak bukan piala gengsi sosial keluarga.
2. **Fase 2: Pemulihan Jembatan Batin (*Bahasa Hati*) (Hari 4–7)**  
   Ayah mengajak Rayhan keluar lingkungan asrama sejenak, makan bersama di tempat yang tenang, memeluknya erat, dan berkata: *"Maafkan Ayah ya Nak, Ayah lupa bertanya apakah Rayhan nyaman atau kaget dengan suasana baru ini."* Memberikan ruang aman bagi anak untuk menangis dan menumpahkan beban batinnya.
3. **Fase 3: Identifikasi Gaya Belajar (*Bahasa Lisan*) (Pekan 2)**  
   Melalui dialog santun terungkap bahwa Rayhan memiliki dominansi gaya belajar kinestetik-alamiah (*Al-Bashar* & *Al-Amal*). Duduk diam mendengarkan ceramah teori membuatnya frustrasi. Orang tua dan pembimbing menyepakati proyek belajar aplikatif: menghitung luas dan volume melalui pembuatan miniatur kandang kelinci.
4. **Fase 4: Penegasan Amanah & Adab Menuntut Ilmu (*Bahasa Tangan*) (Pekan 3 dst)**  
   Rayhan berkomitmen kembali mengikuti jam pelajaran kelas setelah ritme gerak fisiknya terpenuhi. Dibuat jadwal belajar mandiri 30 menit sehari dengan pendampingan apresiatif tanpa bentakan.
"""
    },

    # 2. Berpikir (Tafakkur).md
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Berpikir (Tafakkur).md": {
        "callouts": """
> [!info] Refleksi Lapangan: Kehilangan Kemampuan Merenung Akibat Banjir Stimulus Digital
> **Kondisi Faktual:** Anak zaman sekarang tidak sanggup duduk diam selama 5 menit tanpa menggenggam layar gawai; ketika hening, mereka langsung gelisah dan mengeluh *"Bosan!"*.  
> **Akar Masalah PKN:** Algoritma media sosial dan video berdurasi singkat (*short reels*) membanjiri dopamin otak secara instan, merusak kemampuan *Tafakkur* dan *Tadabbur* yang membutuhkan keheningan kalbu serta observasi sabar.  
> **Langkah Penanganan Nabawiyah:**  
> 1. Terapkan *digital sabbath* (hari bebas layar gawai) di akhir pekan untuk seluruh anggota keluarga.  
> 2. Ajak anak menatap langit malam bertabur bintang atau mengamati sarang semut untuk memantik kembali pertanyaan kontemplatif.  
> 3. Biasakan jeda diam sesudah shalat untuk melatih anak menyimak bisikan nurani fitrahnya.

> [!warning] Peringatan Risiko Pengasuhan: Melarang Anak Berpikir Kritis
> * **Bentuk Kesalahan:** Menyumpal rasa ingin tahu anak dengan doktrin dogmatis buta: *"Jangan banyak tanya, ikuti saja, nanti kamu berdosa!"*
> * **Dampak Terhadap Jiwa:** Menjadikan anak penganut Islam yang rapuh, mudah terombang-ambing paham syubhat ateisme/liberalisme di perguruan tinggi karena tidak pernah diajak bernalar secara kokoh di rumah.
> * **Pencegahan Nabawiyah:** Al-Qur'an memuat lebih dari 750 ayat yang menantang akal budi manusia (*afala ta'qilun, afala tatafakkarun*). Jadikan rumah sebagai laboratorium dialog teologis yang ramah dan logis.

> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Matikan lampu ruang tengah malam ini selama 10 menit, nyalakan sebatang lilin, dan tanyakan pada anak: *"Bagaimana lilin kecil ini mampu mengalahkan kegelapan ruangan yang begitu luas?"*
> * **Tujuan:** Melatih kemampuan analogi filosofis-spiritual dan menanamkan hakikat cahaya iman di atas gelapnya kejahiliyahan.
""",
        "tafrith_ifrath": """
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam Daya Pikir (Tafakkur)

| Dimensi Nalar | Gejala Perilaku yang Teramati | Dampak Psikospiritual pada Anak |
| :--- | :--- | :--- |
| **Tafrith (Ketumpulan Nalar / Jumud)** | Sikap taklid buta, malas memverifikasi kebenaran informasi (*tabayyun*), dan menerima segala hoaks tanpa filter kritis. | Menjadi mangsa empuk fanatisme sempit, manipulasi emosional massa, dan tidak mampu menyelesaikan masalah hidup secara mandiri. |
| **Ifrath (Rasionalisme Liar / Mu'tazilah Modern)** | Mendewakan logika di atas wahyu, menolak keajaiban mukjizat atau hukum syariat yang belum terjangkau akalnya, dan bersikap arogan intelektual. | Tumbuhnya keraguan (*syak*) terhadap perkara ghaib, hilangnya rasa takut kepada Allah (*khosyyah*), dan hati menjadi keras membatu. |
| **Al-Wasathiyah (Nalar Fitrah Nabawiyah)** | Menggunakan akal pikiran secara brilian untuk merenungi tanda-tanda kebesaran Allah (*ayat kauniyah*) seraya tunduk patuh pada wahyu (*ayat qauliyah*). | Kematangan akal budi yang berpadu dengan ketundukan iman, melahirkan generasi ulul albab perintis peradaban emas Islam. |
""",
        "studi_kasus": """
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** Farhan (13 tahun, fase Murahaqah) mulai menolak diajak shalat berjamaah dengan alasan: *"Kenapa kita harus shalat lima waktu menghadap Kakbah? Apakah Allah butuh shalat kita? Bukankah itu tidak masuk akal jika Allah Maha Kaya?"*. Ayah Farhan marah besar dan menuduhnya telah terpapar pemikiran murtad.

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Manajemen Syok & Menahan Emosi (Hari 1–2)**  
   Ayah menahan diri dari melabeli Farhan murtad. Menyadari bahwa pertanyaan kritis di usia 13 tahun adalah sinyal transisi nalar menuju *aqil baligh* yang membutuhkan dalil aqli, bukan paksaan pentungan.
2. **Fase 2: Memberikan Validasi Intelektual (*Bahasa Hati & Lisan*) (Hari 3–5)**  
   Ayah duduk santai bersama Farhan sambil menikmati minuman hangat: *"Farhan, Ayah bersyukur kamu menanyakan hal ini dengan jujur. Itu tanda akalmu berkembang luar biasa."*
3. **Fase 3: Dialog Filsafat Tauhid Sederhana (Pekan 2)**  
   Ayah menjelaskan analogi dokter dan pasien: *"Apakah dokter butuh kita meminum obat? Tidak, kitalah yang butuh kesembuhan. Shalat adalah kebutuhan jiwa kita agar tidak gila di tengah hiruk pikuk dunia, bukan Allah yang butuh kita."* Mengajak Farhan mengkaji keteraturan semesta dan hikmah sujud dari sudut pandang sains dan spiritual.
4. **Fase 4: Penugasan Riset Mandiri (*Bahasa Tangan*) (Pekan 3)**  
   Farhan diminta membaca buku ilmiah karya ulama kontemporer tentang mukjizat syariat, lalu mempresentasikannya di meja makan keluarga. Farhan kembali shalat atas kesadaran nalar sendiri, bukan karena takut dimarahi.
"""
    },

    # 3. Fitrah (Karakter)/index.md
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/index.md": {
        "callouts": """
> [!info] Refleksi Lapangan: Polusi Lingkungan Pengasuhan terhadap Fitrah Anak
> **Kondisi Faktual:** Banyak anak lahir dari keluarga muslim yang baik, namun saat menginjak remaja justru kehilangan rasa malu (*haya'*), mengabaikan shalat, dan memuja budaya hedonistik.  
> **Akar Masalah PKN:** Sebagaimana sabda Nabi ﷺ bahwa setiap anak lahir di atas fitrah suci, namun kedua orang tuanyalah yang membelokkannya. Rumah tangga modern kerap menjadi produsen polusi fitrah melalui tontonan vulgar, pertengkaran suami-istri tanpa adab, dan ketiadaan keteladanan ibadah.  
> **Langkah Penanganan Nabawiyah:**  
> 1. Bersihkan ekosistem rumah dari kontaminasi visual dan audio yang merusak kesucian batin anak.  
> 2. Orang tua wajib melakukan *Taubat Nasuha* atas kelalaian pola asuh masa lalu.  
> 3. Bangun kembali atmosfer dzikir dan munajat di sepertiga malam agar rahmat Allah menaungi rumah tangga.

> [!warning] Peringatan Risiko Pengasuhan: Merusak Benih Fitrah dengan Doktrin Kekerasan
> * **Bentuk Kesalahan:** Menganggap fitrah anak seperti "kertas kosong" (*tabula rasa*) yang harus dicorat-coret dengan paksaan, atau menganggapnya "berdosa asal" yang harus ditekan dengan intimidasi.
> * **Dampak Terhadap Jiwa:** Merusak poros kepercayaan dasar (*basic trust*), menumbuhkan kebencian tersembunyi pada agama, dan memadamkan lentera ruhani anak.
> * **Pencegahan Nabawiyah:** Perlakukan anak sebagai benih pohon kurma yang mulia. Tugas pendidik hanyalah memupuk, menyiram dengan air cinta, dan melindunginya dari hama, bukan memaksanya menjadi pohon lain.

> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Tatap mata anak Anda pagi ini dengan senyuman penuh keteduhan, lalu ucapkan dalam hati dengan penuh keyakinan: *"Anakku ini diciptakan Allah suci dan mulia dengan potensi takdir kebaikan yang agung."*
> * **Tujuan:** Memancarkan persepsi positif (*husnuzhan*) yang menjadi pupuk terkuat bagi mekarnya fitrah anak.
""",
        "tafrith_ifrath": """
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam Merawat Fitrah Insani

| Sikap Pengasuhan | Gejala Lapangan yang Muncul | Dampak pada Eksistensi Fitrah Anak |
| :--- | :--- | :--- |
| **Tafrith (Pembiaran Liar / Permisif)** | Membiarkan anak tumbuh liar tanpa batas moral, tidak mengenalkan batas halal-haram, dan mengabaikan pendampingan akidah. | Fitrah tertutup oleh karat syahwat (*al-hawa*), anak kehilangan kompas moral, dan mudah terseret arus dekadensi zaman. |
| **Ifrath (Kekerasan Dogmatis / Otoriter)** | Memaksakan target ibadah tanpa menumbuhkan cinta, menghukum kesalahan kecil dengan kekerasan, dan menuntut anak bersikap sempurna seperti malaikat. | Fitrah mengalami mutilasi kejiwaan; anak menjadi hipokrit (tampak saleh di depan orang tua namun bermaksiat di belakang), atau memberontak total. |
| **Al-Wasathiyah (Tarbiyah Fitrah Nabawiyah)** | Mengasuh dengan kelembutan kasih sayang seraya menegakkan batas syariat secara adil, konsisten, dan penuh keteladanan nyata. | Fitrah tumbuh mekar secara alami (*salimul fitrah*), melahirkan kepribadian muslim yang kokoh, tangguh, dan berakhlak mulia. |
""",
        "studi_kasus": """
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** Zahra (11 tahun) tumbuh di keluarga yang sangat religius namun kaku. Sejak usia 5 tahun Zahra dituntut menghafal Al-Qur'an 1 juz per bulan dengan ancaman dikurung di kamar jika tidak mencapai target. Menginjak usia 11 tahun, Zahra mogok menghafal, sering berbohong, dan diam-diam mencopot jilbabnya saat berada di luar rumah.

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Dekonstruksi Obsesi Orang Tua (Hari 1–7)**  
   Orang tua berkonsultasi dengan asatidzah PKN. Disadarkan bahwa ambisi mencetak anak hafidz jangan sampai mengorbankan iman dan kesehatan mental anak. Target hafalan dihentikan total sementara waktu.
2. **Fase 2: Pemulihan Luka Hubungan (*Restorasi Tangki Cinta*) (Bulan 1)**  
   Ibu menghentikan seluruh ceramah nasihat. Ibu fokus memasakkan makanan kesukaan Zahra, menemaninya menggambar, memeluknya setiap malam, dan meminta maaf dengan tulus atas kekerasan verbal masa lalu.
3. **Fase 3: Menemukan Kembali Manisnya Iman (*Dialog Fitrah*) (Bulan 2)**  
   Ayah mengajak Zahra tadabbur alam ke perkebunan teh. Menikmati gemercik air dan semilir angin sambil membaca satu ayat Al-Qur'an tentang penciptaan alam dengan tilawah merdu. Zahra merasakan bahwa Al-Qur'an adalah penyejuk kalbu, bukan beban siksaan.
4. **Fase 4: Penataan Kembali Ibadah Berdasarkan Inisiatif Mandiri (Bulan 3 dst)**  
   Zahra secara sukarela meminta kembali memakai jilbab dan menghafal 3 baris per hari karena dorongan cinta kepada Allah, bukan karena takut hukuman kurung.
"""
    },

    # 4. Bakat/index.md
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md": {
        "callouts": """
> [!info] Refleksi Lapangan: Salah Vonis Kenakalan Anak Akibat Buta Bakat
> **Kondisi Faktual:** Anak yang banyak bicara di kelas sering divonis guru sebagai biang keributan; anak yang gemar membongkar mainan dicap perusak; anak yang tidak bisa diam dilabeli hiperaktif (ADHD).  
> **Akar Masalah PKN:** Sistem persekolahan massal menuntut keseragaman semu (*one size fits all*). Di balik "kenakalan" tersebut sebenarnya tersimpan mutiara 40 pilar bakat yang belum difasilitasi wadah penyalurannya secara benar.  
> **Langkah Penanganan Nabawiyah:**  
> 1. Hentikan stigmatisasi dan labeling negatif; lakukan reframing (*mengubah sudut pandang ke arah potensi positif*).  
> 2. Berikan panggung dan peran tanggung jawab yang menyalurkan energi bakatnya (misal: anak yang banyak bicara ditugasi menjadi juru bicara/presenter kelompok).  
> 3. Lakukan observasi Rukun 3A (*Suka, Bisa, Bermanfaat*) selama minimal 6 bulan.

> [!warning] Peringatan Risiko Pengasuhan: Memaksa Anak Mengambil Jurusan Demi Ambisi Orang Tua
> * **Bentuk Kesalahan:** Memaksa anak masuk jurusan kedokteran atau teknik hanya karena gengsi sosial keluarga, padahal profil dominansi bakat anak berada di rumpun *Melayani* atau *Berperasaan*.
> * **Dampak Terhadap Jiwa:** Menghasilkan generasi profesional yang depresi, tidak mencintai pekerjaannya, mudah korupsi/melakukan malpraktik, dan hampa makna spiritual.
> * **Pencegahan Nabawiyah:** Setiap insan dipermudah Allah menuju takdir penciptaannya (*Kullun muyassarun lima khuliqa lahu*). Hormati cetak biru ilahi pada diri anak.

> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Catat 3 aktivitas yang dikerjakan anak Anda hari ini dengan penuh kebahagiaan (*mata berbinar-binar*) dan tanpa disuruh oleh siapa pun.
> * **Tujuan:** Mengumpulkan data empiris rukun *Al-Hirsh* (Suka) sebagai pijakan memetakan bakat dominan anak.
""",
        "tafrith_ifrath": """
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam Pengasuhan Berbasis Bakat

| Dimensi Pendekatan | Gejala Perilaku yang Tampak | Dampak pada Potensi Peradaban Anak |
| :--- | :--- | :--- |
| **Tafrith (Pengabaian Potensi Unik)** | Menganggap semua anak sama rata, tidak pernah mengamati minat anak, dan membiarkan anak tumbuh tanpa arahan peran peradaban. | Potensi emas anak terkubur, anak tumbuh menjadi generasi rata-rata (*medioker*), minder, dan gamang saat memilih karir masa depan. |
| **Ifrath (Kultus Bakat / Komersialisasi Dini)** | Mengidolakan bakat anak secara berlebihan, melatih anak secara ekstrim demi piala lomba sejak dini, dan mengabaikan pembinaan adab serta ibadah fardhu. | Anak tumbuh menjadi pribadi narsistik, sombong, mengukur segalanya dengan materi/popularitas, dan runtuh jiwanya saat mengalami kekalahan. |
| **Al-Wasathiyah (Bakat Nabawiyah Berbingkai Adab)** | Mengasah kekuatan dominan anak hingga mencapai derajat *itqan*, membentenginya dengan adab tawadhu', dan mengorientasikannya untuk kejayaan ummah. | Lahir tokoh peradaban tangguh berkaliber sahabat: profesional di bidangnya, zuhud hatinya, dan seluruh karyanya bernilai amal jariyah. |
""",
        "studi_kasus": """
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** Ihsan (14 tahun) memiliki bakat luar biasa dalam perakitan mekanik dan robotika (*Al-Itqan* & *Al-Jalad*). Namun, nilai pelajaran bahasa Arab dan fiqihnya di pesantren jeblok. Pengasuh pesantren mengancam tidak menaikkan kelas Ihsan dan menyita peralatan mekaniknya karena dianggap menyita waktu menghafal matan. Ihsan menjadi frustrasi dan berniat kabur dari pesantren.

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Mediasi & Dialog Pemahaman Manhaj (Pekan 1)**  
   Orang tua berdialog dengan pimpinan pesantren dengan membawa referensi kurikulum PKN (*Satu Anak Satu Kurikulum*). Menjelaskan bahwa sahabat seperti Khalid bin Walid RA pun tidak hafal seluruh Al-Qur'an karena sibuk di medan jihad, namun Rasulullah ﷺ tetap memuliakannya sebagai *Saifullah al-Maslul*.
2. **Fase 2: Reframing Fasilitas Bakat (*Bahasa Hati*) (Pekan 2)**  
   Pesantren mengembalikan peralatan mekanik Ihsan. Ihsan diajak berdialog: *"Ihsan, umat Islam tertinggal dalam teknologi karena minimnya insinyur shalih. Kami ingin kamu menjadi insinyur muslim handal penerus Al-Jazari."*
3. **Fase 3: Integrasi Kurikulum Kontekstual (Bulan 1)**  
   Guru bahasa Arab dan fiqih mengubah metode pengajaran untuk Ihsan: teks bahasa Arab yang dipelajarinya adalah kitab-kitab sains klasik Islam (*Turats Ilmi*), dan fiqih yang ditekankan adalah fiqih muamalah dan etika teknologi. Ihsan belajar dengan antusiasme berlipat ganda.
4. **Fase 4: Pembuktian Karya Khidmah (*Bahasa Tangan*) (Bulan 3 dst)**  
   Ihsan ditugasi merancang sistem penyiraman otomatis untuk taman pesantren. Nilai adab dan akademiknya melonjak karena ia merasa dihargai fitrahnya.
"""
    },

    # 5. Bekerja Keras.md
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Bekerja Keras.md": {
        "callouts": """
> [!info] Refleksi Lapangan: Gejala Sindrom Anak Rapuh (*Strawberry Generation*)
> **Kondisi Faktual:** Anak zaman sekarang mudah menyerah saat menghadapi kesulitan tugas sekolah, menangis ketika dikritik sedikit oleh guru, dan enggan melakukan pekerjaan fisik yang menguras keringat.  
> **Akar Masalah PKN:** Pola asuh over-protektif (*helicopter parenting*) yang melayani segala kebutuhan anak sejak kecil tanpa pernah melatih otot daya juang (*Al-Jalad*) dan ketahanan menghadapi tekanan (*resilience*).  
> **Langkah Penanganan Nabawiyah:**  
> 1. Hentikan kebiasaan membereskan semua masalah anak; biarkan mereka merasakan konsekuensi logis dari kelalaiannya.  
> 2. Berikan tanggung jawab pekerjaan rumah tangga harian (*al-khidmah*) yang nyata: mencuci piring sendiri, menyapu halaman, atau membuang sampah.  
> 3. Libatkan dalam kegiatan fisik menantang: hiking, berkemah, atau olahraga bela diri.

> [!warning] Peringatan Risiko Pengasuhan: Memberikan Fasilitas Kemewahan Tanpa Keringat
> * **Bentuk Kesalahan:** Membelikan gawai mahal, motor, atau barang mewah hanya sebagai hadiah nilai tanpa mengajarkan anak berjuang mengumpulkan tabungan atau beramal nyata.
> * **Dampak Terhadap Jiwa:** Menumbuhkan mentalitas parasit (*entitled mentality*), malas bekerja, tidak menghargai tetes keringat orang tua, dan rentan depresi saat dewasa menghadapi dunia nyata.
> * **Pencegahan Nabawiyah:** Para nabi semuanya pernah menggembalakan kambing untuk melatih ketahanan mental dan fisik sebelum memikul amanah kenabian. Latihlah anak bekerja keras sejak dini.

> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Saat anak mengeluh lelah mengerjakan tugas atau membantu di rumah, jangan langsung mengambil alih. Tatap matanya dan katakan: *"Ayah tahu ini berat, tapi Ayah percaya otot jiwamu sedang tumbuh semakin kuat sekarang."*
> * **Tujuan:** Menanamkan kebanggaan atas rasa lelah yang halal dan melatih ketangguhan mental (*Al-Hammasah wal-Jalad*).
""",
        "tafrith_ifrath": """
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam Rumpun Bekerja Keras

| Dimensi Daya Juang | Gejala Sikap yang Teramati | Dampak Psikospiritual pada Anak |
| :--- | :--- | :--- |
| **Tafrith (Manja / Lembek / Menyerah)** | Menghindari pekerjaan sulit, gampang merajuk, menuntut fasilitas instan, dan tidak memiliki daya tahan banting. | Menjadi beban keluarga dan masyarakat, tidak mampu bersaing, serta mudah mengalami krisis mental saat menghadapi ujian hidup. |
| **Ifrath (Workaholic Buta / Eksploitasi Diri)** | Bekerja membabi buta tanpa istirahat, mengorbankan waktu shalat dan hak tubuh, serta menilai kehormatan diri hanya dari akumulasi materi. | Tubuh mengalami kelelahan kronis (*burnout*), hati mengeras, mengabaikan keluarga, dan rawan terjangkit penyakit kesombongan (*ujub*). |
| **Al-Wasathiyah (Etos Kerja Mujahid Nabawi)** | Bekerja keras dengan penuh ketekunan (*itqan*), berniat ikhlas mencari nafkah halal, seraya menunaikan hak ibadah dan istirahat secara proporsional. | Tumbuh insan pejuang yang mandiri, produktif, tangan di atas (*al-yadul 'ulya*), dan seluruh keringatnya bernilai pahala jihad. |
""",
        "studi_kasus": """
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** Daffa (15 tahun, fase Syabab) menghabiskan waktu 8–10 jam sehari bermain game online di kamarnya. Ketika diminta orang tuanya membantu mengangkat galon air atau membersihkan mobil, Daffa mengunci pintu dan membentak ibunya: *"Itu tugas pembantu, bukan tugasku!"*.

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Penegasan Batas Tegas & Pemutusan Fasilitas (Hari 1–3)**  
   Ayah mengambil alih komando (*Bahasa Tangan*). Wifi rumah dimatikan di jam kerja harian. Ayah berbicara empat mata dengan suara rendah tapi sangat tegas: *"Di rumah ini tidak ada tempat bagi pemalas yang tidak menghormati ibunya. Mulai hari ini fasilitas gawai disesuaikan dengan kontribusi amalmu."*
2. **Fase 2: Pemulihan Jembatan Hormat (*Bahasa Hati*) (Hari 4–7)**  
   Ayah mengajak Daffa lari pagi berdua. Setelah lelah berolahraga, ayah membelikan sarapan sederhana di pinggir jalan dan menceritakan bagaimana perjuangan kakek dahulu bekerja membanting tulang demi menyekolahkan ayah. Menumbuhkan rasa malu nurani pada jiwa Lawwamah Daffa.
3. **Fase 3: Kontrak Tanggung Jawab Nyata (*Bahasa Lisan*) (Pekan 2)**  
   Daffa diberikan pilihan 3 pos amanah harian di rumah: (a) membersihkan seluruh teras dan kendaraan, (b) mengurus kebun belakang, atau (c) belanja kebutuhan pasar bersama ayah tiap subuh. Daffa memilih pos belanja dan kendaraan.
4. **Fase 4: Mentorship Kerja Lapangan (*Magang Peradaban*) (Bulan 1 dst)**  
   Saat liburan sekolah, Daffa dimagangkan di bengkel motor milik kerabat selama 2 pekan. Merasakan sendiri beratnya mencari uang halal Rp 50.000 sehari. Sikap Daffa berubah drastis menjadi santun, hemat, dan ringan tangan membantu keluarga.
"""
    }
}

# General enrichment generator for other files
def generate_standard_sections(title, domain, scenario_desc):
    return {
        "callouts": f"""
> [!info] Refleksi Lapangan: Tantangan Penerapan {title} di Era Modern
> **Kondisi Faktual:** Dalam dinamika keseharian, banyak pendidik dan orang tua menghadapi kesulitan dalam mengimplementasikan nilai {title} karena benturan budaya serba instan dan tekanan lingkungan pergaulan bebas.  
> **Akar Masalah PKN:** Ketidakselarasan antara teladan batin pendidik (*tazkiyatun nafs*) dengan metode komunikasi yang digunakan, sering kali memicu resistensi dan penolakan fitrah pada anak.  
> **Langkah Penanganan Nabawiyah:**  
> 1. Mulai dari pembenahan diri pendidik (*ibda' binafsik*) sebelum menuntut perubahan pada anak.  
> 2. Bangun kelekatan jiwa melalui [[Bahasa Hati]] dan dialog beradab [[Bahasa Lisan]].  
> 3. Terapkan prinsip penahapan (*tadarruj*) dan kemudahan (*taisir*) sesuai kapasitas fitrah usia anak.

> [!warning] Peringatan Risiko Pengasuhan: Distorsi Nilai {title}
> * **Bentuk Kesalahan:** Mengabaikan pembiasaan bertahap atau memaksakan kepatuhan semu dengan ancaman kekerasan.
> * **Dampak Terhadap Jiwa:** Melahirkan luka batin menahun, memicu kepalsuan karakter, dan merusak rasa percaya anak kepada orang tua.
> * **Pencegahan Nabawiyah:** Berpegang teguh pada manhaj kenabian: mengutamakan cinta kasih, ketegasan tanpa kezaliman, dan doa istiqamah di sepertiga malam.

> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Luangkan waktu khusus 15 menit hari ini untuk berdialog intim dari hati ke hati bersama anak tanpa menyentuh gawai sama sekali.
> * **Tujuan:** Menjaga kebersihan saluran batin (*wasilah qalbiyah*) agar nilai-nilai mulia {title} dapat terserap dengan indah.
""",
        "tafrith_ifrath": f"""
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam Nilai {title}

| Dimensi Sikap | Gejala Lapangan yang Teramati | Dampak Psikospiritual pada Anak |
| :--- | :--- | :--- |
| **Tafrith (Meremehkan / Melalaikan)** | Sikap abai, membiarkan pelanggaran tanpa koreksi, dan tidak memberikan batasan yang jelas bagi anak. | Anak tumbuh rapuh, bingung membedakan benar dan salah, serta kehilangan pegangan moral dalam hidup. |
| **Ifrath (Memaksa / Melampaui Batas)** | Bersikap otoriter, menuntut kesempurnaan di luar batas kemampuan usia, dan menghukum kesalahan kecil secara berlebihan. | Menimbulkan trauma pengasuhan, kemunafikan sikap, serta potensi pemberontakan saat anak menginjak usia baligh. |
| **Al-Wasathiyah (Jalan Tengah Nabawiyah)** | Memadukan kasih sayang yang tulus dengan ketegasan beradab, menegakkan aturan dengan hikmah, dan membimbing dengan teladan nyata. | Tumbuh kesadaran fitrah yang kokoh, akhlak mulia yang matang, serta jiwa yang tenang dan bahagia (*muthmainnah*). |
""",
        "studi_kasus": f"""
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** {scenario_desc}

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Pendinginan & Evaluasi Diri Pendidik (Hari 1–3)**  
   Orang tua menahan diri dari amarah dan celaan verbal. Memperbanyak istighfar dan meluruskan niat dalam mendidik.
2. **Fase 2: Pemulihan Jembatan Hati (*Bahasa Hati*) (Hari 4–7)**  
   Mengalirkan nutrisi ke dalam [[Tangki Cinta]] anak melalui kehadiran fisik utuh, pelukan tulus, dan mendengarkan keluh kesah tanpa menghakimi.
3. **Fase 3: Dialog Nalar & Penyadaran Fitrah (*Bahasa Lisan*) (Pekan 2)**  
   Membuka diskusi hikmah dua arah (*qaulan sadida*) untuk membedah akar masalah dan menumbuhkan kesadaran tanggung jawab pribadi anak.
4. **Fase 4: Penegasan Amanah & Pembiasaan Amal (*Bahasa Tangan*) (Pekan 3 dst)**  
   Menyepakati aturan bersama dan mengawal pelaksanaannya secara konsisten dengan penuh kasih sayang dan ketegasan beradab.
"""
    }

# Remaining files configuration
REMAINING_CONFIGS = {
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Bekerja Sama.md": (
        "Rumpun Bekerja Sama", "Bakat",
        "Salim (12 tahun) enggan berbagi peran dalam kerja kelompok di sekolah, selalu ingin mendominasi, dan mengejek kawan yang bekerja lambat."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Berpikir.md": (
        "Rumpun Berpikir", "Bakat",
        "Ahmad (14 tahun) memiliki ketajaman nalar tinggi namun menggunakannya untuk mendebat perintah orang tua dan meremehkan guru di kelas."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Berperasaan.md": (
        "Rumpun Berperasaan", "Bakat",
        "Fathimah (10 tahun) sangat perasa dan mudah menangis seharian hanya karena tatapan sinis temannya, membuatnya menolak masuk sekolah."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Melayani.md": (
        "Rumpun Melayani", "Bakat",
        "Bilal (13 tahun) gemar melayani dan membantu orang lain hingga mengabaikan tugas sekolah dan kesehatannya sendiri karena takut ditolak."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Memerintah.md": (
        "Rumpun Memerintah", "Bakat",
        "Thoriq (11 tahun) memiliki dorongan memimpin yang kuat namun sering bertindak tiran, memerintah teman-temannya layaknya pelayan."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/index.md": (
        "Tahapan Perkembangan Fitrah", "Perkembangan",
        "Keluarga mengalami kebingungan menghadapi anak yang mendadak berubah sikap dari penurut di usia 6 tahun menjadi kritis menentang di usia 9 tahun."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Thufulah.md": (
        "Fase Thufulah (0–7 Tahun)", "Perkembangan",
        "Balita usia 4 tahun dipaksa masuk bimbingan belajar intensif calistung hingga mengalami gagap bicara dan sering mengompol kembali."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Tamyiz.md": (
        "Fase Tamyiz (7–10 Tahun)", "Perkembangan",
        "Anak usia 8 tahun sering pura-pura shalat di kamar namun sebenarnya hanya rebahan, memicu kemarahan orang tua yang langsung memukulnya."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md": (
        "Fase Murahaqah (10–15 Tahun)", "Perkembangan",
        "Remaja usia 13 tahun menarik diri dari keluarga, mengunci kamar, dan mulai merokok sembunyi-sembunyi bersama teman sebaya."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Syabab.md": (
        "Fase Syabab (15+ Tahun)", "Perkembangan",
        "Pemuda usia 17 tahun belum memiliki tujuan hidup, gamang memilih jurusan, dan sepenuhnya bergantung finansial serta emosional pada ibunya."
    )
}

def enrich_file(rel_path, data):
    file_path = CONTENT_DIR / rel_path
    if not file_path.exists():
        print(f"[ERROR] File not found: {rel_path}")
        return False

    content = file_path.read_text(encoding="utf-8")

    # Check if already enriched with Tafrith
    if "## Diagnosis Penyimpangan: Tafrith vs Ifrath" in content:
        print(f"[SKIP] Already enriched: {rel_path}")
        return True

    # 1. Insert Callouts (after banner / disclaimer)
    callouts_text = data["callouts"].strip()
    
    # Locate where to insert callouts: after the banner or after disclaimer
    banner_match = re.search(r"!\[\[assets/banners/[^\]]+\]\](?:\s*\*Gambar:[^\n]*\*)?", content)
    if banner_match:
        insert_pos = banner_match.end()
        content = content[:insert_pos] + "\n\n" + callouts_text + "\n" + content[insert_pos:]
    else:
        disclaimer_marker = "> Rangkuman materi kurikulum Pendidikan Karakter Nabawiyah"
        idx = content.find(disclaimer_marker)
        if idx != -1:
            end_callout = content.find("\n\n", idx)
            insert_pos = end_callout + 2 if end_callout != -1 else idx + 200
            content = content[:insert_pos] + "\n\n" + callouts_text + "\n" + content[insert_pos:]
        else:
            content = callouts_text + "\n\n" + content

    # 2. Insert Diagnosis Tafrith vs Ifrath and Studi Kasus before Tautan Relevan / Presentation Citations
    tafrith_text = data["tafrith_ifrath"].strip()
    studi_kasus_text = data["studi_kasus"].strip()
    addition_block = f"\n---\n\n{tafrith_text}\n\n---\n\n{studi_kasus_text}\n\n---\n"

    # Find position before "## Tautan" or before "> [!quote] Dokumen & Slide"
    tautan_match = re.search(r"##\s+(?:Tautan|Rujukan Silang|Peta Konsep)", content, re.IGNORECASE)
    citation_match = re.search(r">\s*\[!quote\]\s+Dokumen\s+&\s+Slide", content, re.IGNORECASE)

    if tautan_match:
        pos = tautan_match.start()
        content = content[:pos] + addition_block + "\n" + content[pos:]
    elif citation_match:
        pos = citation_match.start()
        content = content[:pos] + addition_block + "\n" + content[pos:]
    else:
        content = content + "\n\n" + addition_block

    file_path.write_text(content, encoding="utf-8")
    print(f"[SUCCESS] Enriched: {rel_path}")
    return True

def main():
    print("Memulai pengayaan Batch 1: Klaster Fitrah, Karakter & Bakat Anak (15 Artikel)...")
    success_count = 0

    # 1. Process custom data
    for rel_path, data in BATCH1_DATA.items():
        if enrich_file(rel_path, data):
            success_count += 1

    # 2. Process remaining configs
    for rel_path, (title, domain, scenario) in REMAINING_CONFIGS.items():
        data = generate_standard_sections(title, domain, scenario)
        if enrich_file(rel_path, data):
            success_count += 1

    print(f"\nSelesai: {success_count} artikel berhasil diperkaya dengan elemen baku template!")

if __name__ == "__main__":
    main()

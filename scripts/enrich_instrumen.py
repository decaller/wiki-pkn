#!/usr/bin/env python3
"""
enrich_instrumen.py
Menambahkan subbab '## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)'
pada seluruh 34 artikel yang belum memilikinya.
Strict rule: ZERO DELETION (hanya menyisipkan konten baru sebelum ## Tautan atau di akhir).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

INSTRUMEN_SECTIONS = {
    "Bahasa Hati.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Evaluasi Penerapan Bahasa Hati di Rumah
| No | Indikator Bahasa Hati Teramati | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Menatap mata anak dengan senyum tulus sebelum berbicara | [ ] | [ ] | [ ] |
| 2 | Menahan emosi dan tidak berbicara saat dada sedang marah | [ ] | [ ] | [ ] |
| 3 | Memeluk anak minimal 4 kali sehari tanpa alasan tertentu | [ ] | [ ] | [ ] |
| 4 | Mendoakan anak secara spesifik saat mereka tertidur lelap | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Apakah tatapan mata saya kepada anak hari ini memancarkan rasa aman atau justru intimidasi?
2. Kapan terakhir kali saya mendengarkan cerita anak tanpa menyela atau menghakimi?
3. Sudahkah getaran batin saya selaras dengan kata-kata doa yang saya panjatkan untuknya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Peluk anak Anda selama 20 detik tanpa mengucapkan kata instruksi apa pun, lalu bisikkan: *"Ayah/Bunda bersyukur Allah menitipkanmu pada kami."*
""",

    "Bahasa Lisan.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Audit Higienitas Tutur Kata (Lisan Nabawi)
| No | Indikator Kualitas Lisan Pengasuhan | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Bebas dari pelabelan negatif (*bodoh, malas, nakal, cerewet*) | [ ] | [ ] | [ ] |
| 2 | Menggunakan kalimat perintah positif (*"Simpan sepatumu di rak"*) bukan larangan (*"Jangan taruh sembarangan"*) | [ ] | [ ] | [ ] |
| 3 | Berbicara sejajar mata (*eye-level*) dengan merendahkan tubuh | [ ] | [ ] | [ ] |
| 4 | Memulai teguran dengan pujian atas usahanya terlebih dahulu | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Berapa perbandingan kata apresiasi vs kata kritik yang saya lontarkan kepada anak hari ini?
2. Apakah nada bicara saya membuat anak merasa dihargai fitrahnya atau justru dikecilkan hatinya?
3. Sudahkah lisan saya mengalirkan doa thayyibah saat memanggil namanya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Ganti satu kalimat larangan yang biasa Anda ucapkan hari ini dengan kalimat ajakan positif yang menggugah nalar.
""",

    "Tangki Cinta.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Ceklis Level Indikator Tangki Cinta Anak
| No | Parameter Perilaku Teramati | Tangki Kosong (Merah) | Tangki Cukup (Kuning) | Tangki Penuh (Hijau) |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Respon saat dipanggil orang tua | Menghindar / Membantah | Merespon lambat | Datang dengan ceria |
| 2 | Interaksi dengan saudara kandung | Sering bertengkar / Iri hati | Kadang berselisih | Rukun dan mau berbagi |
| 3 | Reaksi saat menghadapi kegagalan kecil | Tantrum / Merajuk lama | Kecewa sebentar | Cepat bangkit kembali |
| 4 | Keterbukaan menceritakan masalah | Menutup diri / Berbohong | Bercerita jika ditanya | Curhat spontan dan jujur |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Apakah perilaku reaktif anak hari ini merupakan sinyal minta perhatian karena tangki cintanya tiris?
2. Sudahkah saya menyisihkan waktu berkualitas 15 menit (*undivided attention*) tanpa memegang gawai?
3. Bahasa cinta mana (*kata penegasan, sentuhan fisik, waktu berkualitas, hadiah, atau pelayanan*) yang paling membuat mata anak berbinar hari ini?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Luangkan 15 menit waktu khusus berdua saja dengan anak sebelum tidur, lakukan aktivitas yang ia pilih sepenuhnya.
""",

    "Bersatunya Ruh dan Jasad Membentuk Jiwa.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Keseimbangan Asupan Jasad dan Ruhaniyah Anak
| No | Dimensi Pemenuhan Kebutuhan Insan | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Jasad: Asupan makanan halal, thayyib, bergizi, dan minim zat kimia sintetis | [ ] | [ ] | [ ] |
| 2 | Jasad: Gerak fisik aktif, paparan sinar matahari pagi, dan tidur tepat waktu | [ ] | [ ] | [ ] |
| 3 | Ruh: Gemar mendengarkan lantunan Al-Qur'an dan kisah orang shalih | [ ] | [ ] | [ ] |
| 4 | Nafs: Kestabilan emosi dan kemampuan menunda kepuasan instan (*delay gratification*) | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Apakah kelesuan ibadah anak disebabkan oleh kelelahan fisik jasadiah ataukah kekeringan nutrisi ruhaniyah?
2. Makanan dan tontonan apa yang masuk ke dalam tubuh dan indera anak saya hari ini?
3. Sudahkah saya merawat ketenangan jiwa saya sendiri sebelum menuntut anak untuk tenang?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Ajak anak berjalan kaki di luar ruangan tanpa alas kaki di atas rumput (*grounding*) sambil merenungkan keagungan ciptaan Allah di langit.
""",

    "Tujuan Hidup Manusia.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Internalisasi Visi Khalifah fil Ardh pada Anak
| No | Indikator Kesadaran Eksistensial | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Mengetahui bahwa dirinya diciptakan semata-mata untuk beribadah kepada Allah | [ ] | [ ] | [ ] |
| 2 | Memiliki cita-cita yang berorientasi kemanfaatan bagi umat, bukan sekadar gaji materi | [ ] | [ ] | [ ] |
| 3 | Menghubungkan setiap ilmu dan keterampilan sekolah dengan bekal dakwah Islam | [ ] | [ ] | [ ] |
| 4 | Merasa gelisah ketika melihat kemungkaran atau kesulitan orang lain di sekitarnya | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Apakah obrolan harian keluarga lebih banyak membahas capaian duniawi atau tujuan akhirat?
2. Bagaimana respon anak ketika ditanya: *"Untuk apa kamu belajar hari ini?"*
3. Sudahkah saya meneladankan gaya hidup seorang hamba yang faqir di hadapan Allah?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Tanyakan kepada anak: *"Menurutmu, kebaikan apa yang paling ingin kamu persembahkan untuk menolong sesama kelak ketika sudah dewasa?"* Dengarkan tanpa mengoreksi.
""",

    "Pembagian Jiwa/Muthmainnah.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Penanaman Ketenangan Jiwa (Nafs Muthmainnah)
| No | Indikator Ketenangan Batin Teramati | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Wajah riang dan tenang saat diajak mendirikan shalat berjamaah | [ ] | [ ] | [ ] |
| 2 | Mampu mengendalikan diri dari rasa panik atau cemas berlebih saat menghadapi ujian | [ ] | [ ] | [ ] |
| 3 | Ridha dan tidak mengeluh berkepanjangan atas ketetapan takdir yang tidak menyenangkan | [ ] | [ ] | [ ] |
| 4 | Merasa tenteram saat berdzikir atau berada di lingkungan majelis ilmu | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Apakah atmosfer rumah saya hari ini memancarkan ketenangan (*sakinah*) atau kepanikan terburu-buru?
2. Seberapa sering dzikirullah terucap di tengah aktivitas keluarga?
3. Sudahkah saya mengajari anak mencari pelarian kepada sajadah saat hatinya sedang sempit?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Matikan seluruh layar digital 30 menit sebelum tidur, bacakan surah Al-Mulk bersama-sama dalam suasana temaram yang tenang.
""",

    "Pembagian Jiwa/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Pemetaan Dinamika Tiga Jiwa (Ammarah, Lawwamah, Muthmainnah)
| No | Sinyal Dominansi Jiwa | Ammarah (Merah) | Lawwamah (Kuning) | Muthmainnah (Hijau) |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Respon terhadap godaan | Larut dan menuruti hawa nafsu | Sempat tergoda lalu menyesal | Teguh menolak dengan tenang |
| 2 | Respon saat ditegur salah | Membela diri dan marah | Menunduk dan meminta maaf | Berterima kasih atas koreksi |
| 3 | Motif dalam beramal | Ingin dipuji / dipandang hebat | Khawatir tidak diterima | Tulus mengharap ridha Allah |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Jiwa mana yang paling mendominasi perilaku anak saya dan respon saya sendiri hari ini?
2. Bagaimana cara saya menyuburkan penyesalan nurani (*Lawwamah*) tanpa membuatnya putus asa?
3. Sudahkah saya mengalirkan asupan dzikir yang memampukan jiwa anak menundukkan syahwatnya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Saat anak melakukan kesalahan kecil, puji keberaniannya untuk jujur mengakui sebelum membahas solusi perbaikannya.
""",

    "Fitrah (Karakter)/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Audit Kemurnian Fitrah Anak
| No | Pilar Fitrah yang Diobservasi | Terdistorsi / Tertekan | Mengembang Alami | Mekar Paripurna |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Fitrah Keimanan: Antusiasme mendengar kisah kebesaran Allah | [ ] | [ ] | [ ] |
| 2 | Fitrah Belajar & Nalar: Rasa ingin tahu tinggi dan banyak bertanya | [ ] | [ ] | [ ] |
| 3 | Fitrah Bakat: Keunikan sifat dan gaya kerja alami yang khas | [ ] | [ ] | [ ] |
| 4 | Fitrah Seksualitas: Kejelasan identitas peran gender (maskulinitas/feminitas) | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Bagian fitrah anak mana yang hari ini paling sering saya interupsi atau saya paksakan?
2. Apakah saya mendidik anak sesuai cetak biru fitrahnya atau sekadar menuruti ambisi pribadi?
3. Sudahkah saya mensyukuri keunikan anak yang berbeda dari saudara-saudaranya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Amati satu rasa ingin tahu anak hari ini, luangkan waktu untuk menjawab pertanyaannya secara ilmiah dan mendalam.
""",

    "4 Kaidah Implementasi.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Kepatuhan Penerapan 4 Kaidah Emas PKN
| No | Kaidah Emas PKN | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Kaidah 1: Menghargai keunikan tiap anak ('satu anak satu kurikulum') | [ ] | [ ] | [ ] |
| 2 | Kaidah 2: Menerapkan penahapan alami tanpa melompati etape (*tadarruj*) | [ ] | [ ] | [ ] |
| 3 | Kaidah 3: Mengedepankan keteladanan visual sebelum instruksi lisan | [ ] | [ ] | [ ] |
| 4 | Kaidah 4: Mengasah bakat dominan dan mengabaikan kelemahan minor | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Kaidah emas mana yang paling sering terlanggar dalam pola asuh saya pekan ini?
2. Apakah saya memperlakukan semua anak dengan tuntutan seragam yang tidak adil?
3. Seberapa sabar saya membiarkan proses tadarruj berjalan tanpa tergesa-gesa memetik hasil?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Hentikan membandingkan capaian satu anak dengan saudaranya atau anak tetangga hari ini.
""",

    "Kaidah Implementasi di Berbagai Lembaga.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Audit Keselarasan Kebijakan Lembaga dengan Fitrah Nabawiyah
| No | Dimensi Kebijakan Lembaga Pendidikan | Bertentangan | Transisi Penyesuaian | Selaras Penuh |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Sistem Penilaian: Meniadakan perangkingan angka yang melukai harga diri santri | [ ] | [ ] | [ ] |
| 2 | Manajemen Disiplin: Menerapkan konsekuensi edukatif tanpa kekerasan verbal/fisik | [ ] | [ ] | [ ] |
| 3 | Fasilitas Bakat: Menyediakan ruang eksplorasi karya nyata di luar kelas | [ ] | [ ] | [ ] |
| 4 | Sinergi Wali Santri: Komunikasi berkala dua arah memetakan perkembangan fitrah | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Lembaga
1. Apakah kurikulum lembaga kita memanusiakan santri atau memperlakukan mereka sebagai produk pabrik?
2. Sudahkah para pengajar dibekali tazkiyatun nafs sebelum memasuki ruang kelas?
3. Bagaimana lembaga memfasilitasi anak-anak dengan bakat unik yang tidak tertampung di ujian konvensional?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Adakan forum dialog santai antara dewan guru dan perwakilan wali santri untuk menyamakan frekuensi bahasa cinta di rumah dan sekolah.
""",

    "Peran Ayah dan Bunda.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Pembagian Peran Pengasuhan Ayah dan Bunda
| No | Indikator Peran Pengasuhan Harmonis | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Ayah: Menjadi teladan visi tauhid dan memimpin ibadah shalat keluarga | [ ] | [ ] | [ ] |
| 2 | Ayah: Berdialog mendalam (*deep talk*) dengan anak minimal 2 kali sepekan | [ ] | [ ] | [ ] |
| 3 | Bunda: Menjaga kehangatan rumah dan menjadi tempat curahan hati yang aman | [ ] | [ ] | [ ] |
| 4 | Ayah & Bunda: Satu suara di depan anak dan tidak berdebat aturan di hadapan mereka | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Malam Hari
1. Apakah ayah hadir secara utuh jiwa dan raga di rumah, bukan sekadar 'mesin ATM pencari nafkah'?
2. Apakah bunda mendapatkan dukungan emosional dari ayah sehingga tidak meluapkan stres kepada anak?
3. Sudahkah kami berdua mendoakan anak bersama-sama setelah shalat berjamaah?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Ayah mengajak anak keluar rumah berdua saja untuk minum teh atau jalan santai selama 20 menit tanpa interupsi pekerjaan.
""",

    "Peran Guru dan Lembaga Pendidikan.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Evaluasi Diri Pendidik Berbasis Fitrah
| No | Indikator Keteladanan Guru di Kelas | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Memulai pembelajaran dengan menyapa ramah dan mendoakan keberkahan murid | [ ] | [ ] | [ ] |
| 2 | Menghargai setiap pendapat murid tanpa menertawakan jawaban yang salah | [ ] | [ ] | [ ] |
| 3 | Menghindari pemberian cap 'bodoh' atau 'nakal' pada santri yang lambat paham | [ ] | [ ] | [ ] |
| 4 | Mengkaitkan materi pelajaran umum dengan tanda-tanda kebesaran Allah | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Pendidik
1. Apakah kehadiran saya di kelas dirindukan oleh murid atau justru membuat mereka tegang tertekan?
2. Seberapa banyak saya mendoakan hidayah bagi murid-murid yang paling sulit diatur?
3. Sudahkah saya membersihkan niat mengajar murni lillahi ta'ala hari ini?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Berikan catatan apresiasi tertulis di buku tugas seorang murid yang paling sering membuat masalah, puji satu kebaikan kecil yang ia lakukan hari ini.
""",

    "Tanggung Jawab Pendidikan.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Audit Tanggung Jawab Pendidikan Keluarga
| No | Pilar Tanggung Jawab Pendidikan | Diabaikan | Dititipkan Penuh ke Sekolah | Dikelola Mandiri Secara Bersama |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Penanaman Aqidah & Tauhid | [ ] | [ ] | [ ] |
| 2 | Pembiasaan Adab & Akhlak Harian | [ ] | [ ] | [ ] |
| 3 | Pengajaran Baca Tulis Al-Qur'an | [ ] | [ ] | [ ] |
| 4 | Penjagaan Kesehatan Jasad & Makanan Halal | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Orang Tua
1. Apakah saya menganggap tanggung jawab mendidik anak selesai begitu uang SPP sekolah dibayar?
2. Bagaimana jika kelak di akhirat Allah menuntut saya atas aqidah anak yang menyimpang?
3. Langkah nyata apa yang sudah saya siapkan untuk memastikan anak kokoh memegang agama sebelum baligh?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Ambil alih satu sesi belajar adab atau mengaji Al-Qur'an anak malam ini langsung oleh ayah atau bunda di rumah.
""",

    "Peran & Tanggung Jawab/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Keselarasan Tripartit (Ayah, Bunda, Guru)
| No | Dimensi Koordinasi Pengasuhan | Retak / Kontradiktif | Kadang Selaras | Terpadu Sempurna |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Kesepakatan batasan penggunaan gawai di rumah dan sekolah | [ ] | [ ] | [ ] |
| 2 | Kesamaan cara merespon pelanggaran adab anak | [ ] | [ ] | [ ] |
| 3 | Keterbukaan informasi mengenai perkembangan emosi dan bakat anak | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah anak melihat adanya perbedaan standar aturan yang membuatnya bingung bersikap?
2. Seberapa solid komunikasi antara wali murid dan wali kelas dalam menangani problem santri?
3. Apakah ego orang tua atau guru pernah menghalangi kemaslahatan terbaik bagi jiwa anak?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Kirimkan pesan singkat ucapan terima kasih dari orang tua kepada guru kelas atas kesabarannya membimbing anak hari ini.
""",

    "Implementasi/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Kesiapan Implementasi Ekosistem PKN
| No | Komponen Ekosistem Belajar | Tahap Awal | Berkembang | Mandiri Berkelanjutan |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Ruang fisik yang ramah gerak fitrah dan eksplorasi alam | [ ] | [ ] | [ ] |
| 2 | Jadwal harian yang lapang dan tidak terburu-buru | [ ] | [ ] | [ ] |
| 3 | Budaya apresiasi proses dan pembiasaan adab salam, senyum, sapa | [ ] | [ ] | [ ] |
| 4 | Bank portofolio bakat dan karya nyata anak | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah implementasi PKN di lingkungan kita sudah menyentuh hati atau baru sebatas jargon di dinding?
2. Hambatan mental apa yang paling menghalangi kita untuk konsisten menerapkan fitrah nabawiyah?
3. Sudahkah seluruh anggota keluarga/pengajar memiliki pemahaman visi yang setara?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Buat papan majalah dinding sederhana di ruang keluarga untuk memajang karya dan apresiasi kebaikan harian anak.
""",

    "Menumbuhkan Kesadaran Beramal.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Pengukuran Motivasi Beramal Anak (Internal vs Eksternal)
| No | Parameter Kesadaran Beramal | Level 1: Imbalan/Hukuman | Level 2: Pujian Sosial | Level 3: Kesadaran Lillahi Ta'ala |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Menunaikan shalat lima waktu | Menunggu diancam/diberi hadiah | Karena malu dilihat orang | Bersegera saat adzan berkumandang |
| 2 | Merapikan tempat tidur dan mainan | Menunggu diteriaki | Ingin dibilang anak pintar | Spontan atas inisiatif mandiri |
| 3 | Menolong teman atau adik | Mengharap balasan setimpal | Agar dipuji guru | Ikhlas karena cinta kebaikan |

### 2. Tiga Pertanyaan Reflektif
1. Seberapa sering saya menyogok anak dengan imbalan materi agar ia mau melakukan ketaatan?
2. Bagaimana cara saya menyadarkan anak bahwa Allah Maha Melihat setiap amal rahasianya?
3. Apakah saya sendiri sudah menikmati manisnya beramal shalih tanpa mengharap balasan manusia?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Ajak anak memasukkan sedekah ke kotak amal secara diam-diam tanpa ada orang lain yang melihat, lalu rasakan kebahagiaannya bersama.
""",

    "Pembelajaran Alamiah.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Pemenuhan Siklus Belajar Alami Anak
| No | Tahapan Belajar Alami | Terbelenggu Ruang Kaku | Cukup Terfasilitasi | Bebas Bereksplorasi |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Mengamati fenomena alam ciptaan Allah secara langsung | [ ] | [ ] | [ ] |
| 2 | Bertanya kritis dan mendiskusikan sebab-akibat | [ ] | [ ] | [ ] |
| 3 | Mencoba langsung lewat tangan dan alat (*hands-on learning*) | [ ] | [ ] | [ ] |
| 4 | Mengambil hikmah dan mensyukuri kebesaran Sang Pencipta | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Berapa jam anak saya menghabiskan waktu di alam terbuka pekan ini dibandingkan di depan layar?
2. Apakah saya terlalu cepat mematikan rasa penasaran anak dengan jawaban singkat yang tidak memancing nalar?
3. Bagaimana kita mengubah lingkungan rumah menjadi laboratorium kehidupan yang menakjubkan?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Bawa sehelai daun atau sebiji batu ke meja makan, amati guratan seratnya bersama anak menggunakan kaca pembesar dan tadabburi keteraturannya.
""",

    "Bank Studi Kasus.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Analisis Kasus Masalah Perilaku Anak
| Tahapan Diagnosis | Pertanyaan Kunci Evaluasi Mandiri | Catatan Kondisi Anak |
| :--- | :--- | :--- |
| **Identifikasi Gejala** | Perilaku tampak apa yang meresahkan (tantrum, membantah, malas)? | |
| **Pemeriksaan Tangki Cinta** | Kapan terakhir kali anak merasa benar-benar dicintai tanpa syarat? | |
| **Deteksi Etape Usia** | Apakah tuntutan kita sudah sesuai dengan kapasitas usianya? | |
| **Pemetaan Bakat Terdistorsi** | Apakah perilaku buruk tersebut sebenarnya luapan energi bakat yang tersumbat? | |

### 2. Tiga Pertanyaan Reflektif
1. Apakah saya melihat masalah anak sebagai aib yang harus ditutupi atau sebagai panggilan untuk memperbaiki diri?
2. Seberapa sering saya terburu-buru menghukum sebelum memahami akar luka di balik perbuatannya?
3. Sudahkah saya memohon petunjuk khusus kepada Allah dalam sujud tahajud mengenai kasus anak ini?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Tuliskan satu kasus perilaku anak yang paling memusingkan Anda hari ini, bedah menggunakan kacamata 'energi bakat yang salah wadah'.
""",

    "Imunitas Sosial.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Ketahanan Benteng Imunitas Sosial Anak
| No | Indikator Imunitas Terhadap Pengaruh Negatif | Rentan Terbawa Arus | Kadang Bimbang | Kokoh Berpendirian |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Menolak ajakan teman untuk berkata kotor atau mengejek orang lain | [ ] | [ ] | [ ] |
| 2 | Tidak minder mengenakan pakaian syar'i di tengah lingkungan heterogen | [ ] | [ ] | [ ] |
| 3 | Mampu membatasi waktu bermain gawai sesuai kesepakatan keluarga | [ ] | [ ] | [ ] |
| 4 | Memilih sahabat karib yang shalih dan saling mengingatkan dalam kebaikan | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah pergaulan anak di luar rumah sudah diimbangi dengan kehangatan obrolan di dalam rumah?
2. Seberapa siap anak saya berani mengatakan *"Tidak, ini haram"* saat sendirian tanpa pengawasan orang tua?
3. Sudahkah kita membekali anak dengan dalil rasional mengapa syariat Islam melindungi dirinya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Diskusikan satu tren media sosial terkini bersama anak remaja Anda, ajak ia membedah dampaknya terhadap kemuliaan akhlak.
""",

    "Luka dan Hutang Pengasuhan/Euforia.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Deteksi Candu Euforia Prestasi Semu
| No | Gejala Jebakan Euforia Prestasi | Nihil | Terindikasi Ringan | Parah / Menjadi Candu |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Anak mogok belajar atau putus asa saat tidak mendapatkan juara satu | [ ] | [ ] | [ ] |
| 2 | Orang tua memamerkan piala anak di media sosial demi menaikkan gengsi keluarga | [ ] | [ ] | [ ] |
| 3 | Hubungan persaudaraan menjadi tegang karena kompetisi prestasi yang tidak sehat | [ ] | [ ] | [ ] |
| 4 | Anak hanya mau berbuat baik jika dijanjikan hadiah atau sanjungan khalayak | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Untuk siapa sebenarnya piala dan sertifikat lomba anak ini diperjuangkan: untuk Allah atau ego orang tua?
2. Kapan terakhir kali saya memuji kebaikan anak yang tidak menghasilkan piagam penghargaan?
3. Apakah saya tetap mencintai anak dengan kadar yang sama ketika ia gagal dalam perlombaan?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Peluk anak Anda dan katakan: *"Bagi Ayah dan Bunda, keikhlasan dan kejujuranmu jauh lebih berharga daripada seribu piala di dunia."*
""",

    "Luka dan Hutang Pengasuhan/Recovery.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Pemantauan Kemajuan Proses Pemulihan (Recovery)
| No | Indikator Kesembuhan Luka Batin Anak | Masih Terluka Dalam | Mulai Membuka Diri | Pulih & Tangguh |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Reaksi fisik saat didekati orang tua (tidak lagi tegang atau menjauh) | [ ] | [ ] | [ ] |
| 2 | Berani menatap mata orang tua saat diajak berbicara | [ ] | [ ] | [ ] |
| 3 | Kemampuan mengekspresikan kesedihan atau kekecewaan tanpa meledak marah | [ ] | [ ] | [ ] |
| 4 | Hilangnya gejala psikosomatis (mual, pusing, mengompol saat cemas) | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Orang Tua
1. Apakah saya sudah tulus meminta maaf kepada anak atas kekasaran lisan atau fisik di masa lalu?
2. Seberapa sabar saya menerima proses pemulihan anak yang mungkin mengalami pasang surut?
3. Sudahkah saya memaafkan diri saya sendiri dan memohon ampun kepada Allah atas kelalaian masa lalu?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Tulis surat pendek berisi permohonan maaf dan ungkapan kasih sayang, selipkan di bawah bantal anak Anda malam ini.
""",

    "Luka dan Hutang Pengasuhan/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Audit Hutang Pengasuhan (*Emotional Debt*)
| No | Bentuk Hutang Pengasuhan Terabaikan | Lunas Terbayar | Terhutang Sebagian | Menumpuk Berat |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Hutang Dekapan & Sentuhan Fisik Hangat di Usia Dini | [ ] | [ ] | [ ] |
| 2 | Hutang Kehadiran Jiwa Ayah (*Father Hunger*) | [ ] | [ ] | [ ] |
| 3 | Hutang Bermain Bersama Tanpa Interupsi Pekerjaan | [ ] | [ ] | [ ] |
| 4 | Hutang Apresiasi dan Pengakuan atas Usaha Kerasnya | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Berapa banyak janji kepada anak yang belum sempat saya tunaikan hingga hari ini?
2. Apakah sikap keras kepala anak hari ini adalah cerminan dari bentakan saya bertahun-tahun yang lalu?
3. Sebelum ajal menjemput, hutang pengasuhan mana yang paling mendesak untuk saya bayar kepada anak?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Lunasi satu janji kecil kepada anak yang pernah tertunda pekan ini tanpa mencari alasan lagi.
""",

    "Internal & Eksternal/Tawakkal dan Doa.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Keseimbangan Ikhtiar dan Tawakkal Pengasuhan
| No | Dimensi Kepasrahan Hati Pendidik | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Memulai setiap rencana mendidik dengan basmalah dan istikharah | [ ] | [ ] | [ ] |
| 2 | Menyerahkan hasil akhir hidayah anak kepada kehendak Allah (*Tawakkal Mutlak*) | [ ] | [ ] | [ ] |
| 3 | Menyisihkan waktu sepertiga malam terakhir khusus menangis mendoakan anak | [ ] | [ ] | [ ] |
| 4 | Tidak membanggakan kehebatan metode atau materi sendiri saat anak berhasil | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah saya lebih percaya pada kehebatan tips parenting modern daripada ketuk pintu langit lewat doa?
2. Bagaimana ketenangan hati saya ketika anak menghadapi jalan terjal yang tidak sesuai rencana saya?
3. Sudahkah air mata taubat saya menetes membasahi sajadah demi keselamatan iman anak saya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Bangun 15 menit sebelum adzan Subuh, dirikan dua rakaat shalat malam dan sebutkan nama anak Anda satu per satu dalam doa qunut atau sujud terakhir.
""",

    "Internal & Eksternal/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Penyelarasan Faktor Internal (Ruhiyah) dan Eksternal (Lingkungan)
| No | Dimensi Ekosistem Tumbuh Kembang | Lemah / Kontradiktif | Cukup Terjaga | Sinergis Paripurna |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Internal: Kekuatan ruhiyah orang tua dan keteraturan ibadah rumah tangga | [ ] | [ ] | [ ] |
| 2 | Eksternal: Lingkungan tetangga dan teman sebaya yang mendukung keshalihan | [ ] | [ ] | [ ] |
| 3 | Eksternal: Kemitraan harmonis dengan lembaga pendidikan formal | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah kita terlalu sibuk membenahi faktor luar sementara ruhiyah internal keluarga keropos?
2. Bagaimana cara kita menyaring polusi lingkungan luar tanpa harus mengurung anak di dalam rumah?
3. Seberapa kokoh benteng keimanan internal anak saat menghadapi badai fitnah pergaulan?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Lakukan evaluasi bersama pasangan mengenai tontonan dan pengaruh lingkungan luar yang paling mendesak untuk dibatasi pekan ini.
""",

    "Insight & Teknis/Insight/SOTABH.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Observasi Rukun 3A SOTAB HEBAT
| Aktivitas Unik Anak | sukA (Al-Hirsh) | bisA (Al-Itqan) | bergunA (Al-Mufid) | Status Validasi Bakat |
| :--- | :-: | :-: | :-: | :--- |
| (Aktivitas 1: .................) | [ ] | [ ] | [ ] | Calon Bakat Kuat / Lemah |
| (Aktivitas 2: .................) | [ ] | [ ] | [ ] | Calon Bakat Kuat / Lemah |
| (Aktivitas 3: .................) | [ ] | [ ] | [ ] | Calon Bakat Kuat / Lemah |

### 2. Tiga Pertanyaan Reflektif
1. Aktivitas apa yang membuat anak saya lupa waktu dan mengerjakannya dengan mata berbinar-binar?
2. Apakah saya mengapresiasi keunikan bakat anak yang berbeda dari bakat saya sendiri?
3. Wadah nyata apa yang sudah saya sediakan untuk menyalurkan energi bakatnya agar bermanfaat bagi orang lain?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Amati dan catat satu aktivitas anak hari ini yang memenuhi ketiga kriteria Rukun 3A secara alami.
""",

    "Insight & Teknis/Insight/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Transformasi Wawasan (Insight) Menjadi Amal Nyata
| No | Tahap Penyerapan Wawasan PKN | Sekadar Wacana Teori | Mulai Diuji Coba | Menjadi Kebiasaan Otomatis |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Memahami kaidah 'satu anak satu kurikulum' | [ ] | [ ] | [ ] |
| 2 | Mengganti bentakan dengan dialog Bahasa Hati | [ ] | [ ] | [ ] |
| 3 | Menghubungkan bakat anak dengan misi peradaban Islam | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Dari sekian banyak materi PKN yang saya baca, berapa persen yang sudah saya praktikkan di rumah?
2. Hambatan psikologis apa yang membuat kita sulit mengubah pola asuh lama yang keliru?
3. Bagaimana cara kita saling mengingatkan antar anggota keluarga saat kembali tergoda menggunakan cara-cara instan?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Pilih satu konsep kecil dari wiki ini hari ini, diskusikan bersama pasangan saat makan malam dan sepakati langkah penerapannya.
""",

    "Insight & Teknis/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Audit Kemandirian Teknis Pengasuhan
| No | Kemampuan Teknis Pendidik | Belum Dikuasai | Sedang Dipelajari | Mahir Mempraktikkan |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Melakukan observasi bakat berbasis Rukun 3A | [ ] | [ ] | [ ] |
| 2 | Mengisi dan menganalisis Kuisioner TB-40 | [ ] | [ ] | [ ] |
| 3 | Merancang Rencana Pelaksanaan Pembelajaran (RPP) berbasis fitrah | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah instrumen teknis yang kita gunakan mempermudah kita mendidik atau justru membebani birokrasi?
2. Bagaimana cara menjaga agar instrumen teknis tidak menghilangkan ruh kasih sayang alami dalam keluarga?
3. Sudahkah data observasi anak didokumentasikan dengan rapi untuk dievaluasi per semester?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Buka satu catatan observasi anak, perbarui catatan perkembangannya berdasarkan pengamatan sepekan terakhir.
""",

    "Pendidikan Ideal/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Standar Emas Lingkungan Pendidikan Ideal
| No | Indikator Sekolah / Rumah Mempesona | Jauh dari Standar | Mendekati Standar | Memenuhi Standar Emas |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Rasa aman fisik dan psikologis bagi seluruh anak | [ ] | [ ] | [ ] |
| 2 | Keterbukaan ruang dialog tanpa rasa takut dihakimi | [ ] | [ ] | [ ] |
| 3 | Fasilitas pengembangan bakat yang beragam dan adil | [ ] | [ ] | [ ] |
| 4 | Keterikatan batin yang hangat antara guru dan murid | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah anak-anak kita merasa bahagia dan bersemangat saat melangkahkan kaki ke tempat belajarnya?
2. Nilai-nilai peradaban apa yang paling kuat tertanam di lingkungan belajar anak kita?
3. Apa kontribusi nyata yang dapat saya berikan untuk mewujudkan iklim pendidikan ideal di sekitar saya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Bersihkan dan tata ulang satu sudut ruang belajar anak di rumah agar lebih nyaman, lapang, dan mengundang inspirasi.
""",

    "Paradigma & Implementasi/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Penyelarasan Paradigma dan Aksi Lapangan
| No | Pilar Paradigma PKN | Paradigma Materialistik Lama | Transisi Kesadaran | Paradigma Nabawiyah Utuh |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Orientasi Sukses Anak | Gaji tinggi dan jabatan duniawi | Sukses dunia dan akhirat | Ridha Allah dan karya peradaban |
| 2 | Cara Memandang Kenakalan | Anak rusak / pembuat onar | Butuh perhatian | Energi bakat yang tersumbat |
| 3 | Metode Memperbaiki Sikap | Hukuman keras dan bentakan | Dialog nalar | Doa, teladan, dan Bahasa Hati |

### 2. Tiga Pertanyaan Reflektif
1. Sejauh mana paradigma berpikir saya sudah berhijrah dari standar pabrik menuju standar kenabian?
2. Ketika anak berbuat salah, apakah respon pertama saya adalah kemarahan ataukah empati mendalam?
3. Siapa figur panutan utama yang saya rujuk dalam menyelesaikan konflik pengasuhan di rumah?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Reframing satu 'kelakuan menjengkelkan' anak hari ini menjadi potensi fitrah yang sedang mencari wadah penyalurannya.
""",

    "FAQ Ringkas.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Ceklist Diagnostik Masalah Parenting Harian
| No | Pertanyaan Diagnostik Cepat | Ya | Ragu-ragu | Tidak |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Apakah saya tahu apa kebutuhan batin anak saat ia sedang rewel? | [ ] | [ ] | [ ] |
| 2 | Apakah aturan di rumah sudah jelas konsekuensi logisnya bagi anak? | [ ] | [ ] | [ ] |
| 3 | Apakah anak memiliki waktu bermain bebas di luar ruangan setiap hari? | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Dari berbagai jawaban di FAQ ini, poin mana yang paling relevan dengan kondisi keluarga saya saat ini?
2. Apakah saya mencari solusi instan ataukah siap menjalani proses kesabaran tarbiyah?
3. Sudahkah saya mendiskusikan FAQ ini bersama pasangan untuk menyamakan langkah?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Pilih satu solusi dari FAQ ini dan terapkan langsung pada situasi konflik anak sore nanti.
""",

    "Referensi Kajian Video.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Rencana Pembelajaran Mandiri Wali Santri (Video Learning Log)
| Judul Kajian Video PKN | Durasi Disimak | Poin Utama yang Menggugah | Aksi Nyata yang Akan Diterapkan |
| :--- | :-: | :--- | :--- |
| (Kajian 1: .................) | ... Menit | ................................... | ................................... |
| (Kajian 2: .................) | ... Menit | ................................... | ................................... |

### 2. Tiga Pertanyaan Reflektif
1. Seberapa rutin saya meluangkan waktu menuntut ilmu pengasuhan nabawi di tengah kesibukan kerja?
2. Apakah ilmu dari rekaman kajian ini sekadar menjadi wawasan atau sudah meresap ke dalam akhlak saya mendidik?
3. Siapa kawan atau kerabat yang paling membutuhkan video kajian ini untuk saling menguatkan dalam kebaikan?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Simak 1 rekaman kajian video PKN pilihan Anda hari ini bersama pasangan selama 15 menit dan tuliskan satu intisarinya.
""",

    "Dokumen PKN/index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Navigasi Pembelajaran Korpus PKN
| No | Klaster Dokumen PKN | Belum Dibaca | Sedang Dipelajari | Telah Diterapkan di Lapangan |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Klaster Fondasi Insan & Jiwa | [ ] | [ ] | [ ] |
| 2 | Klaster Fitrah, Karakter & Bakat | [ ] | [ ] | [ ] |
| 3 | Klaster Metode Mendidik & Pemulihan | [ ] | [ ] | [ ] |
| 4 | Klaster Kaidah & Standar Implementasi | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah saya sudah membaca dokumen ini secara berurutan atau hanya melompat ke topik praktis?
2. Bagaimana pemahaman menyeluruh terhadap korpus ini mengubah cara pandang saya membesarkan generasi?
3. Langkah apa yang saya siapkan untuk membagikan mutiara ilmu ini kepada komunitas di sekitar saya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Tandai satu dokumen tema yang paling menantang bagi Anda, jadwalkan waktu 20 menit besok pagi untuk membacanya tuntas.
""",

    "Renungan/Hak dan Kewajiban.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Penunaian Hak Anak di Rumah
| No | Hak Syar'i Anak yang Wajib Diberikan | Terabaikan | Diberikan Bersyarat | Diberikan Penuh Tanpa Syarat |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Hak Rasa Aman dan Terbebas dari Kekerasan Verbal | [ ] | [ ] | [ ] |
| 2 | Hak Dididik Mengenal Allah dan Rasul-Nya | [ ] | [ ] | [ ] |
| 3 | Hak Diberikan Makanan dari Harta yang Halal | [ ] | [ ] | [ ] |
| 4 | Hak Diperlakukan Adil di Antara Saudara-saudaranya | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif
1. Apakah saya lebih sering menuntut kewajiban anak daripada menunaikan hak-haknya?
2. Bagaimana jika anak kelak menuntut saya di hadapan mahkamah Allah atas haknya yang saya rampas?
3. Sudahkah saya meminta maaf kepada anak atas hak kasih sayangnya yang sering tercuri oleh kesibukan kerja saya?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Tunaikan satu hak anak hari ini: berikan waktu mendengarkan seluruh keluh kesahnya tanpa menyela sedikit pun.
""",

    "index.md": """
## Instrumen Observasi Terapan & Lembar Evaluasi Diri (Self-Assessment)

### 1. Rubrik Ceklist Kesiapan Transformasi Pendidikan Karakter Nabawiyah
| No | Indikator Transformasi Budaya Pengasuhan | Belum Dimulai | Tahap Adaptasi | Membudaya Istiqamah |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Keluarga/Lembaga memiliki visi peradaban akhirat yang jelas dan tertulis | [ ] | [ ] | [ ] |
| 2 | Bahasa Hati dan keteladanan menjadi instrumen utama komunikasi harian | [ ] | [ ] | [ ] |
| 3 | Meniadakan pelabelan negatif dan pemaksaan kurikulum seragam | [ ] | [ ] | [ ] |
| 4 | Menumbuhkan kesadaran beramal shalih atas dorongan cinta kepada Allah | [ ] | [ ] | [ ] |

### 2. Tiga Pertanyaan Reflektif Utama
1. Apakah rumah dan sekolah kita sudah menjadi oasis ketenangan yang merawat fitrah anak-anak kita?
2. Warisan karakter apa yang paling ingin kita tinggalkan dalam jiwa mereka ketika kita telah tiada?
3. Sudahkah kita berpasrah total kepada Allah setelah menyempurnakan seluruh ikhtiar tarbiyah ini?

### 3. Aksi Cepat (*Quick Win*) Hari Ini
* Ambil komitmen satu perubahan kecil hari ini: gantikan satu teriakan marah dengan satu pelukan doa yang tulus bagi anak Anda.
"""
}

def insert_before_links(content, section_text):
    patterns = [
        r"(##\s+(?:[0-9]+\.\s+)?Tautan[^\n]*)",
        r"(##\s+(?:[0-9]+\.\s+)?Peta Konsep[^\n]*)",
        r"(##\s+(?:[0-9]+\.\s+)?Referensi[^\n]*)",
    ]
    for pat in patterns:
        m = re.search(pat, content, re.IGNORECASE)
        if m:
            idx = m.start()
            return content[:idx] + section_text.strip() + "\n\n---\n\n" + content[idx:]
    return content.rstrip() + "\n\n---\n\n" + section_text.strip() + "\n"

def main():
    print("Menambahkan Instrumen Observasi Terapan & Evaluasi Diri pada 34 artikel...")
    count = 0
    for file_key, section_text in INSTRUMEN_SECTIONS.items():
        matched_files = list(CONTENT_DIR.rglob(file_key))
        if not matched_files:
            print(f"[WARN] File tidak ditemukan: {file_key}")
            continue
            
        # Pilih yang bukan Template
        target_file = [f for f in matched_files if "Template" not in str(f)][0]
        content = target_file.read_text(encoding="utf-8")
        
        if "## Instrumen Observasi Terapan" in content:
            print(f"[SKIP] Sudah ada instrumen di {file_key}")
            continue
            
        new_content = insert_before_links(content, section_text)
        target_file.write_text(new_content, encoding="utf-8")
        print(f"[UPDATED] {target_file.relative_to(CONTENT_DIR)} (+Instrumen)")
        count += 1
        
    print(f"\nSelesai: {count} artikel berhasil diperkaya dengan Instrumen Observasi & Evaluasi Diri!")

if __name__ == "__main__":
    main()

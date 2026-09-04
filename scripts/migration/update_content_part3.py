"""
Script part 3: Pendidikan Ideal and Implementasi
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

PENDIDIKAN_IDEAL = """# Pendidikan Ideal

Pendidikan Ideal dalam Pendidikan Karakter Nabawiyah (PKN) adalah sebuah sistem rekonstruksi pengasuhan dan pembelajaran yang bertujuan mengantarkan anak mencapai kedewasaan mental (*Akil*) tepat bersamaan dengan kedatangan kedewasaan biologisnya (*Baligh*).

Pendidikan bukanlah arena perlombaan gelar akademik atau pabrikasi pekerja mekanis, melainkan ikhtiar peradaban untuk membebaskan generasi Muslim dari penyakit *Al-Wahn* (cinta dunia dan takut mati) serta fenomena "Generasi Buih" yang banyak secara kuantitas namun rapuh secara mental dan spiritual.

## Pilar Pembahasan Pendidikan Ideal

* [[Benang Merah Pendidikan]] — Kritik terhadap sistem sekolah modern dan pemulihan jalur fitrah.
* [[Metode Mendidik]] — Tiga bahasa pengasuhan: Bahasa Hati, Bahasa Lisan, dan Bahasa Tangan.
* [[Pembelajaran Alamiah]] — Membedakan antara edukasi momen spontan dan proyek kegiatan terencana.
* [[Luka dan Hutang Pengasuhan]] — Anatomi luka fitrah masa lalu dan metodologi pemulihannya (*Recovery*).
* [[Batas Toleransi]] — Matriks kelonggaran dan ketegasan pengasuhan per fase usia.
* [[Imunitas Sosial]] — Membentengi generasi dari distorsi digital dan arus pergaulan bebas.
"""

BENANG_MERAH = """# Benang Merah Pendidikan

Sistem pendidikan modern warisan revolusi industri telah mereduksi manusia menjadi sekrup dalam mesin ekonomi. Anak-anak diseragamkan dengan standar kaku, dipaksa duduk diam berjam-jam, dan dinilai hanya dari angka ujian kognitif semata.

## Dampak Reduksi Pendidikan Modern

1. **Memesinkan Manusia:** Memaksa anak dengan fitrah bakat yang beragam untuk menguasai hal yang sama, membunuh keunikan potensi bawaan lahir mereka.
2. **Perampasan Hak Fase Emas:** Anak usia TK/SD dirampas hak bermain merdekanya dengan drill calistung dan tugas berlebihan, menyisakan kekosongan emosional.
3. **Lahirnya Hutang Pengasuhan:** Emosi dan fitrah yang tidak tuntas meledak saat usia remaja dalam bentuk disorientasi hidup, apatisme, atau kenakalan remaja.

## Benang Merah Kurikulum Nabawiyah

Pendidikan Nabawiyah mengembalikan kemerdekaan fitrah anak. Rumah tangga diposisikan sebagai inkubator utama karakter, ayah sebagai arsitek visi dan penegak hukum, dan ibu sebagai sumber curahan kasih sayang batin. Sekolah hadir bukan untuk menggantikan keluarga, melainkan bermitra mendukung perkembangan potensi unik anak.
"""

METODE_MENDIDIK = """# Metode Mendidik

Dalam Pendidikan Karakter Nabawiyah (PKN), terdapat tiga instrumen bahasa utama yang digunakan secara berjenjang sesuai dengan kematangan jiwa anak:

1. **[[Bahasa Hati]] (Usia 0 - 7 Tahun):** Komunikasi berbasis getaran rasa kasih sayang, keteladanan visual tanpa kata-kata, pelukan fisik, dan pemenuhan 5 Bahasa Cinta. Digunakan untuk menumbuhkan fitrah iman.
2. **[[Bahasa Lisan]] (Usia 7 - 10 Tahun):** Komunikasi dialogis dua arah, memberikan argumentasi logis sebab-akibat, dan menuntaskan rasa ingin tahu anak tanpa amarah. Digunakan untuk menumbuhkan fitrah belajar.
3. **[[Bahasa Tangan]] (Usia 10 Tahun ke Atas):** Tindakan tegas, penetapan konsekuensi nyata, dan penegakan aturan tanpa menyakiti raga untuk mendisiplinkan amalan wajib menjelang baligh. Digunakan untuk menumbuhkan fitrah bakat dan tanggung jawab.
"""

BAHASA_HATI = """# Bahasa Hati

Bahasa Hati adalah metode pengasuhan utama pada **Fase Thufulah (0 - 7 Tahun)** yang menitikberatkan pada sentuhan rasa, kehangatan batin, dan keteladanan tanpa paksaan.

## Karakteristik Bahasa Hati

* **Tanpa Dikte Verbal:** Anak usia dini adalah peniru ulung. Satu keteladanan nyata orang tua jauh lebih membekas daripada seribu nasihat lisan.
* **Pengisian Penuh Tangki Cinta:** Memberikan rasa aman dan nyaman agar anak meyakini bahwa dirinya dicintai tanpa syarat (*unconditional love*).
* **Membangun Citra Positif tentang Allah:** Menanamkan bahwa Allah Maha Pengasih, Maha Penyayang, dan menyukai keindahan, bukan menakut-nakuti anak kecil dengan siksa neraka.
"""

BAHASA_LISAN = """# Bahasa Lisan

Bahasa Lisan adalah instrumen pengajaran utama pada **Fase Tamyiz (7 - 10 Tahun)** di mana anak mulai mampu diajak berpikir rasional dan memahami hubungan sebab-akibat.

## Karakteristik Bahasa Lisan

* **Dialog Dua Arah:** Meniru metode Nabi Ibrahim saat berdialog dengan Nabi Ismail, mendengarkan argumen anak dan membimbing nalarnya dengan lembut.
* **Bukan Omelan atau Cacian:** Bahasa lisan yang efektif adalah kata-kata yang jernih, tenang, dan objektif, bukan bentakan atau kalimat sarkastis yang meruntuhkan harga diri anak.
* **Memahamkan Konsekuensi:** Membimbing anak memahami mengapa suatu aturan ada dan apa dampak perbuatannya bagi diri sendiri serta lingkungan.
"""

BAHASA_TANGAN = """# Bahasa Tangan

Bahasa Tangan adalah instrumen ketegasan dan penegakan konsekuensi yang mulai dilegalkan penggunaannya pada **Fase Murahaqah (10 Tahun - Baligh)**, khususnya untuk mendisiplinkan ibadah shalat dan pelanggaran norma yang membahayakan.

## Syarat Operasional Bahasa Tangan

1. **Didahului Tuntasnya Bahasa Hati & Lisan:** Jika anak tidak dicintai di usia 0-7 th dan tidak diajarkan shalat di usia 7-10 th, pukulan di usia 10 tahun adalah bentuk kezaliman.
2. **Motivasi Kasih Sayang (*Rahmah*):** Bertujuan mendidik agar anak selamat di akhirat, bukan melampiaskan amarah atau kekesalan orang tua.
3. **Tidak Melukai dan Tidak di Wajah:** Pukulan simbolis yang mendidik (*ghairu mubarrih*), tidak menimbulkan memar fisik, patah tulang, atau luka trauma batin.
4. **Bersifat Personal:** Ditegakkan kepada anak yang bersangkutan, bukan menghukum kelompok secara kolektif yang mencelakakan anak tak bersalah.
"""

PEMBELAJARAN_ALAMIAH = """# Pembelajaran Alamiah

Pembelajaran Alamiah adalah konsep edukasi PKN yang membedakan secara tegas antara dua jenis situasi pendidikan: **Peristiwa (*Moment*)** dan **Kegiatan (*Project*)**.

## 1. Peristiwa (Moment Spontan)

* Terjadi secara insidental dalam kehidupan sehari-hari (misal: anak terjatuh, bertengkar memperebutkan mainan, atau melihat orang kesusahan).
* **Fokus Edukasi:** Penanaman adab, nilai moral, dan penguatan fitrah iman.
* **Prinsip:** Segera dieksekusi saat kejadian hangat agar menjadi hikmah batin yang membekas kuat (*teachable moment*).

## 2. Kegiatan (Project Terencana)

* Dirancang secara terstruktur dan bertahap (misal: proyek berkebun, merakit robot, menyusun buku, atau pemagangan karya).
* **Fokus Edukasi:** Penajaman karakter belajar dan pengasahan keahlian bakat (Rukun 3A: Suka, Bisa, Berguna).
* **Prinsip:** Melibatkan proses eksplorasi mendalam, penetapan target, dan evaluasi proses.
"""

LUKA_HUTANG = """# Luka dan Hutang Pengasuhan

Hutang Pengasuhan (*Parenting Debt*) adalah kondisi ketidaktuntasan pemenuhan hak-hak fitrah anak pada suatu fase perkembangan yang mengakibatkan terganggunya fase-fase berikutnya.

## Mekanisme Terjadinya Hutang

* Jika anak tidak puas bermain dan kurang dicintai di usia 0-7 tahun (Fase Thufulah), ia akan menuntut hak bermain tersebut saat berusia remaja atau dewasa (tumbuh menjadi pribadi kekanak-kanakan).
* Jika nalar anak dibungkam dan dilarang bereksperimen di usia 7-10 tahun (Fase Tamyiz), ia akan tumbuh menjadi pemuda yang ragu-ragu, takut mengambil inisiatif, dan miskin kreativitas.

## Dua Cabang Konsekuensi

* [[Euforia]] — Fase ledakan emosi dan tuntutan kebebasan yang tak terkendali.
* [[Recovery]] — Metodologi pemulihan jiwa (*fitrah restoration*) untuk menuntaskan luka masa lalu.
"""

EUFORIA = """# Fase Euforia

Fase Euforia adalah kondisi psikologis ketika anak yang selama masa kecilnya mengalami penekanan ketat (*excessive pressure*) atau perampasan hak fitrah tiba-tiba mendapatkan kebebasan di usia remaja atau dewasa.

* **Bentuk Manifestasi:** Perilaku memberontak secara ekstrem, kecanduan hiburan/gawai tanpa kendali, pergaulan bebas, dan penolakan total terhadap nasihat orang tua.
* **Sebab Utama:** Ledakan dendam alamiah jiwa (*nafs*) yang menuntut penuntasan hak masa kecil yang dulu dirampas demi kepatuhan instan.
* **Penanganan:** Orang tua tidak boleh membalas dengan kekerasan yang lebih besar. Perlu jeda de-eskalasi, pengakuan kesalahan masa lalu secara jujur, dan pembukaan dialog rekonsiliasi.
"""

RECOVERY = """# Recovery (Pemulihan Fitrah)

Recovery adalah proses terstruktur untuk menyembuhkan luka batin dan menuntaskan hutang pengasuhan anak sebelum mereka melangkah ke fase kedewasaan mandiri.

## Metode EMISOL dalam Recovery

1. **Empati (Edukasi Rasa):** Orang tua mendengarkan keluh kesah dan kemarahan anak tanpa membantah, memvalidasi perasaannya, dan memohon maaf atas kekeliruan pengasuhan masa lalu.
2. **Imajinasi (Edukasi Visi):** Mengajak anak membayangkan masa depan yang mulia, menemukan kembali jati diri dan panggilan hidupnya sebagai hamba Allah.
3. **Solusi (Edukasi Aksi):** Menyusun kesepakatan baru yang adil dan realistis untuk melatih tanggung jawab secara bertahap tanpa paksaan kaku.
"""

BATAS_TOLERANSI = """# Batas Toleransi

Batas Toleransi adalah prinsip graduasi ketegasan orang tua dalam menyikapi pelanggaran anak sesuai dengan fase usianya:

| Rentang Usia | Fase | Tingkat Toleransi | Tindakan Terhadap Pelanggaran |
|---|---|---|---|
| **0 - 7 Tahun** | Thufulah | **Paling Longgar** | Dimaafkan secara luas, dialihkan perhatiannya, dipeluk, dan diberi teladan yang benar. |
| **7 - 10 Tahun** | Tamyiz | **Sedang** | Dinasihati secara logis (*Bahasa Lisan*), diajak merenungkan akibat perbuatannya tanpa sanksi fisik. |
| **10 th - Baligh** | Murahaqah | **Paling Sempit** | Ditegakkan aturan tegas (*Bahasa Tangan* jika lalai shalat), diminta bertanggung jawab atas kerusakan yang dibuat. |
| **Pasca-Baligh** | Syabab | **Nol Toleransi Syariat** | Dosa dan pahala ditanggung sendiri secara mukallaf di hadapan Allah. |
"""

IMUNITAS_SOSIAL = """# Imunitas Sosial

Imunitas Sosial adalah daya tahan batin dan kekebalan mental seorang anak terhadap polusi moral, syubhat pemikiran, dan arus pergaulan negatif di lingkungan sekitarnya.

## Cara Membangun Imunitas

1. **Memperkuat Karakter Iman Sejak Usia Dini:** Anak yang memiliki muraqabah (merasa diawasi Allah) tidak memerlukan pengawasan fisik orang tua selama 24 jam.
2. **Keterbukaan Komunikasi di Rumah:** Menjadikan orang tua sebagai tempat curhat pertama yang aman, sehingga anak tidak mencari pelarian semu di luar rumah.
3. **Menyalurkan Energi Lewat Karya:** Anak yang sibuk menekuni bakatnya yang bermanfaat tidak akan memiliki ruang waktu luang untuk hal-hal yang sia-sia (*laghwu*).
"""

# ==============================================================================
# IMPLEMENTASI
# ==============================================================================

IMPLEMENTASI_CONTENT = """# Paradigma Implementasi

Implementasi Pendidikan Karakter Nabawiyah (PKN) menuntut integrasi harmonis antara kebersihan hati pendidik (*Tazkiyatun Nafs*), pemenuhan 4 elemen karakter, dan pembagian peran yang seimbang antara ayah, ibu, serta lembaga pendidikan.

## Struktur Implementasi PKN

* **[[Kaidah & Elemen]]:**
  * [[4 Kaidah Implementasi]] — Prinsip metodologis penumbuhan fitrah.
  * [[4 Elemen Implementasi]] — Sinergi Iman, Belajar, Bakat, dan Perkembangan.
* **[[Internal & Eksternal]]:**
  * [[Tazkiyatun Nafs]] — Fondasi pembersihan batin pendidik.
  * [[Tawakkal dan Doa]] — Kepasrahan spiritual atas hasil pendidikan.
* **[[Peran & Tanggung Jawab]]:**
  * [[Tanggung Jawab Pendidikan]] — Hakikat amanah orang tua di hadapan Allah.
  * [[Peran Ayah dan Bunda]] — Sinergi kepemimpinan maskulin dan kehangatan feminin.
  * [[Peran Guru dan Lembaga Pendidikan]] — Sekolah sebagai mitra pelengkap rumah.
"""

KAIDAH_4 = """# 4 Kaidah Implementasi

Dalam menjalankan Pendidikan Karakter Nabawiyah, terdapat empat kaidah fundamental yang wajib dijaga oleh para pendidik:

1. **Kaidah Bertahap (*Tadrij*):** Menumbuhkan karakter mengikuti ritme kematangan jiwa anak, tidak melompat langsung menuntut kedewasaan sebelum fase usianya tiba.
2. **Kaidah Koneksi Sebelum Koreksi:** Memastikan jalinan kasih sayang dan tangki cinta anak terisi penuh sebelum menegakkan aturan dan pendisiplinan.
3. **Kaidah Keteladanan Sebelum Tuntutan:** Pendidik wajib menjadi cerminan nyata dari akhlak yang ingin ditanamkan. Anak belajar dari apa yang ia lihat, bukan apa yang ia dengar semata.
4. **Kaidah Kekuatan Menutupi Kelemahan:** Berfokus menumbuhkembangkan potensi bakat unik anak (*focus on strengths*), bukan sibuk meratapi atau memaksa memperbaiki kekurangannya secara kaku.
"""

ELEMEN_4 = """# 4 Elemen Implementasi

Empat elemen pokok yang harus hadir secara serentak dalam ekosistem pendidikan nabawiyah:

1. **Elemen Iman:** Menjaga agar seluruh aktivitas pembelajaran bermuara pada pengenalan dan kecintaan kepada Allah (*Tauhidullah*).
2. **Elemen Belajar:** Mengasah daya nalar kritis dan rasa ingin tahu melalui eksplorasi dunia nyata (*Tajribah*).
3. **Elemen Bakat:** Menemukan dan memfasilitasi panggilan peran spesifik anak melalui rukun Suka, Bisa, dan Berguna.
4. **Elemen Perkembangan:** Menyesuaikan metode pengasuhan (Bahasa Hati, Lisan, atau Tangan) dengan tahapan usia anak.
"""

TAZKIYATUN_NAFS = """# Tazkiyatun Nafs

Tazkiyatun Nafs (penyucian jiwa) adalah faktor internal paling krusial bagi setiap orang tua dan guru dalam Pendidikan Karakter Nabawiyah.

> *"Sungguh beruntung orang yang menyucikan jiwanya, dan sungguh merugi orang yang mengotorinya."* (QS. Asy-Syams: 9-10)

Pendidik yang jiwanya penuh dengan riya', dendam, kesombongan, atau kecintaan berlebih pada dunia (*al-wahn*) tidak akan mampu memancarkan getaran hikmah kepada anak asuhnya. Mendidik adalah proses transfer kesucian batin; jika sumber airnya keruh, air yang mengalir ke hilir pun akan keruh.
"""

TAWAKKAL_DOA = """# Tawakkal dan Doa

Pendidikan Nabawiyah menyadarkan orang tua akan batas kekuasaannya sebagai manusia. Sehebat apa pun metode yang digunakan, hidayah dan taufik berada sepenuhnya di tangan Allah Azza wa Jalla.

* **Ikhtiar Maksimal, Tawakkal Total:** Menjalankan ikhtiar terbaik sesuai sunnatullah pendidikan, lalu menyerahkan hasilnya kepada ketetapan Allah.
* **Kekuatan Doa Orang Tua:** Doa orang tua untuk anaknya adalah salah satu doa mustajab yang menembus langit tanpa hijab. Menyelipkan nama-nama anak dalam setiap sujud dan sepertiga malam terakhir adalah bagian tak terpisahkan dari kurikulum pendidikan nabawiyah.
"""

TANGGUNG_JAWAB = """# Tanggung Jawab Pendidikan

Rasulullah ﷺ bersabda:
> *"Setiap kalian adalah pemimpin, dan setiap kalian akan dimintai pertanggungjawaban atas apa yang dipimpinnya. Seorang laki-laki adalah pemimpin di dalam keluarganya dan akan dimintai pertanggungjawaban atas mereka. Dan seorang wanita adalah pemimpin di rumah suaminya dan akan dimintai pertanggungjawaban atas asuhannya..."* (HR. Bukhari & Muslim)

Pendidikan anak adalah amanah fardhu 'ain yang melekat pada kedua orang tua kandung. Amanah ini tidak dapat dialihkan atau dicuci-tangan sepenuhnya kepada sekolah, pondok pesantren, atau guru les berbayar.
"""

PERAN_AYAH_BUNDA = """# Peran Ayah dan Bunda

Keluarga adalah laboratorium peradaban di mana ayah dan ibu memainkan peran komplementer yang saling melengkapi:

## Peran Ayah (Arsitek Visi & Hukum)
* Menetapkan arah tujuan hidup keluarga dan kurikulum karakter rumah tangga.
* Membawa wibawa (*waqaar*), ketegasan penegakan syariat, dan batasan operasional.
* Mengajarkan kemandirian hidup, keberanian menghadapi tantangan dunia luar, dan pencarian nafkah halal.

## Peran Bunda (Curahan Kasih & Madrasah Pertama)
* Menjadi sumber utama kehangatan batin, curahan kasih sayang, dan pengisian tangki cinta.
* Menanamkan adab keseharian, bahasa tutur kata yang lembut, dan kepekaan nurani.
* Merawat perkembangan fisik dan psikologis anak dari masa buaian hingga mandiri.
"""

PERAN_GURU_SEKOLAH = """# Peran Guru dan Lembaga Pendidikan

Lembaga pendidikan dan para guru dalam perspektif PKN berposisi sebagai **mitra pelengkap orang tua**, bukan pengganti fungsi orang tua.

* **Guru Sebagai Fasilitator Fitrah:** Menemukan keunikan potensi setiap murid, bukan meratakan semua anak dengan kurikulum seragam yang kaku.
* **Membangun Ekosistem Belajar yang Menggairahkan:** Menyediakan fasilitas laboratorium nyata, ruang diskusi nalar yang terbuka, dan suasana yang ramah anak tanpa kekerasan mental.
* **Sinergi dengan Rumah:** Melaporkan perkembangan fitrah anak secara berkala kepada orang tua, bekerja sama menyelaraskan nilai-nilai yang dibangun di sekolah dengan kebiasaan di rumah.
"""

print("Writing Pendidikan Ideal and Implementasi files...")
write_file("Pendidikan Ideal.md", "Pendidikan Ideal", PENDIDIKAN_IDEAL)
write_file("Pendidikan Ideal/Benang Merah Pendidikan.md", "Benang Merah Pendidikan", BENANG_MERAH)
write_file("Pendidikan Ideal/Metode Mendidik.md", "Metode Mendidik", METODE_MENDIDIK)
write_file("Pendidikan Ideal/Metode Mendidik/Bahasa Hati.md", "Bahasa Hati", BAHASA_HATI)
write_file("Pendidikan Ideal/Metode Mendidik/Bahasa Lisan.md", "Bahasa Lisan", BAHASA_LISAN)
write_file("Pendidikan Ideal/Metode Mendidik/Bahasa Tangan.md", "Bahasa Tangan", BAHASA_TANGAN)
write_file("Pendidikan Ideal/Pembelajaran Alamiah.md", "Pembelajaran Alamiah", PEMBELAJARAN_ALAMIAH)
write_file("Pendidikan Ideal/Luka dan Hutang Pengasuhan.md", "Luka dan Hutang Pengasuhan", LUKA_HUTANG)
write_file("Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md", "Euforia", EUFORIA)
write_file("Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md", "Recovery", RECOVERY)
write_file("Pendidikan Ideal/Batas Toleransi.md", "Batas Toleransi", BATAS_TOLERANSI)
write_file("Pendidikan Ideal/Imunitas Sosial.md", "Imunitas Sosial", IMUNITAS_SOSIAL)

write_file("Implementasi.md", "Implementasi", IMPLEMENTASI_CONTENT)
write_file("Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md", "4 Kaidah Implementasi", KAIDAH_4)
write_file("Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md", "4 Elemen Implementasi", ELEMEN_4)
write_file("Implementasi/Internal & Eksternal/Tazkiyatun Nafs.md", "Tazkiyatun Nafs", TAZKIYATUN_NAFS)
write_file("Implementasi/Internal & Eksternal/Tawakkal dan Doa.md", "Tawakkal dan Doa", TAWAKKAL_DOA)
write_file("Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md", "Tanggung Jawab Pendidikan", TANGGUNG_JAWAB)
write_file("Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md", "Peran Ayah dan Bunda", PERAN_AYAH_BUNDA)
write_file("Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md", "Peran Guru dan Lembaga Pendidikan", PERAN_GURU_SEKOLAH)

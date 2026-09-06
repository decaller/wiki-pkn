#!/usr/bin/env python3
"""
scripts/inject_original_source_links.py
Menyematkan tautan langsung ke artikel/naskah sumber asli dari:
1. Sekolah Karakter Imam Syafi'i (sekolahkarakter.com)
2. Portal Resmi Pendidikan Karakter Nabawiyah (karakternabawiyah.com)
3. SOTAB HEBAT (sotabh.com)

pada seluruh artikel wiki terkait di content/.
"""

import os
import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
CONTENT_DIR = BASE_DIR / "content"

# Load metadata
skis = json.load(open(BASE_DIR / "old_backup/skis/articles.json"))
sotab = json.load(open(BASE_DIR / "old_backup/sotabh/articles.json"))
pkn = json.load(open(BASE_DIR / "old_backup/karakternabawiyah/articles.json"))

# Build master database by (source, slug)
source_db = {}
for a in skis:
    source_db[('SKIS', a.get('slug', ''))] = {
        'source': 'SKIS',
        'title': a.get('title', '').strip(),
        'url': a.get('url', '').strip(),
        'site_name': "Sekolah Karakter Imam Syafi'i (SKIS)",
        'badge': '🏫'
    }

for a in sotab:
    t = a.get('title', {})
    title = (t.get('rendered', '') if isinstance(t, dict) else str(t)).strip()
    source_db[('SOTAB', a.get('slug', ''))] = {
        'source': 'SOTAB',
        'title': title,
        'url': a.get('link', '').strip(),
        'site_name': 'SOTAB HEBAT (sotabh.com)',
        'badge': '💡'
    }

for a in pkn:
    source_db[('PKN', a.get('slug', ''))] = {
        'source': 'PKN',
        'title': a.get('title', '').strip(),
        'url': a.get('url', '').strip(),
        'site_name': 'Portal Manhaj Pendidikan Karakter Nabawiyah',
        'badge': '🌐'
    }

# Mapping: Relative file path in content/ -> list of (source, slug, optional note)
ARTICLE_SOURCE_MAP = {
    # ─── Insan: Tujuan & Jiwa ────────────────────────────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Tujuan Hidup Manusia.md': [
        ('PKN', 'termaktub-dalam-salah-satu-lembar-kitabnya', 'Menegaskan orientasi mutlak manusia diciptakan untuk beribadah dan memakmurkan bumi.'),
        ('SOTAB', 'kemerdekaan-sejati-dimulai-dari-hati', 'Kemerdekaan hakiki insan dalam penghambaan total kepada Allah.'),
        ('SKIS', 'surga-dunia-dalam-mendidik-anak', 'Meraih ketenangan batin dalam mendidik anak menuju ridha Allah.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md': [
        ('SKIS', 'kuatkan-akar-pendidikan-pada-anak', 'Mengokohkan akar ruhani dan kesiapan fisik anak sebelum membebaninya.'),
        ('SOTAB', 'kami-ajarkan-huruf-tapi-lupa-menumbuhkan-hati', 'Kritik pendidikan mekanis yang mengabaikan dimensi ruh dan hati.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/index.md': [
        ('SKIS', 'sepasang-sayap-khouf-dan-roja-dalam-mendidik-anak', 'Menjaga keseimbangan jiwa anak antara harap dan takut kepada Allah.'),
        ('SOTAB', 'kemerdekaan-sejati-dimulai-dari-hati', 'Penataan kebebasan dan ketenangan batin pada tingkatan jiwa.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Ammarah.md': [
        ('SKIS', 'mengendalikan-kemarahan-pada-anak', 'Menundukkan letupan emosi nafsu ammarah melalui keteladanan orang tua.'),
        ('SOTAB', 'hukuman-yang-membunuh-karakter', 'Dampak destruktif hukuman emosional terhadap jiwa yang masih labil.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Lawwamah.md': [
        ('SOTAB', 'bukan-jalan-keluar-tapi-cari-jalan-kedalam', 'Muhasabah batin dan penyesalan positif jiwa lawwamah.'),
        ('SKIS', 'meminta-maaf-kepada-anak-bukan-aib', 'Menumbuhkan kesadaran diri dan keberanian mengakui kekhilafan.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Muthmainnah.md': [
        ('SOTAB', 'kemerdekaan-sejati-dimulai-dari-hati', 'Mencapai derajat ketenteraman jiwa muthmainnah melalui tazkiyah.'),
        ('SKIS', 'cara-mendidik-hati-anak-agar-tumbuh-keikhlasan', 'Menanamkan benih keikhlasan murni di lubuk kalbu anak.')
    ],

    # ─── Insan: Fitrah Belajar, Iman, & Tangki Cinta ──────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Belajar.md': [
        ('SKIS', 'karakter-belajar', 'Menumbuhkan gairah fitrah belajar alami anak tanpa paksaan kurikulum kaku.'),
        ('SKIS', 'gaya-belajar', 'Memahami 3 modalitas belajar fitrah Qur\'ani: Al-Fuad, Al-Bashar, dan As-Sam\'u.'),
        ('SKIS', 'cara-mengatasi-anak-yang-susah-belajar', 'Solusi praktis merestorasi semangat belajar melalui pendekatan emosi.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/Tangki Cinta.md': [
        ('SOTAB', 'takaran-cinta', 'Menakar dosis kasih sayang agar tidak berlebih (manja) dan tidak kurang (haus cinta).'),
        ('SOTAB', 'ramuan-cinta', 'Unsur-unsur pembangun kehangatan hubungan batin orang tua dan anak.'),
        ('SOTAB', 'salah-kaprah-meramu-cinta', 'Meluruskan kesalahpahaman antara memfasilitasi materi dan mencurahkan cinta.'),
        ('SKIS', 'bahasa-cinta', 'Risalah komunikasi cinta nabawiyah di lingkungan keluarga.'),
        ('SOTAB', 'cinta-yang-tak-melukai', 'Menjaga kemurnian kasih sayang tanpa menyelipkan luka batin.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/index.md': [
        ('SOTAB', 'jangan-membebani-iman-anak', 'Menjaga kemurnian fitrah tauhid anak tanpa doktrinasi kaku melampaui usianya.'),
        ('SKIS', 'cara-mendidik-hati-anak-agar-tumbuh-keikhlasan', 'Menumbuhkan kecintaan beribadah atas dorongan ikhlas karena Allah.'),
        ('SOTAB', 'cinta-dan-keteladanan', 'Keteladanan nyata orang tua sebagai pintu gerbang keimanan anak.')
    ],

    # ─── Insan: Etape Perkembangan Usia ──────────────────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Thufulah.md': [
        ('SKIS', 'sekilas-pandang-usia-0-7-tahun', 'Prinsip pengasuhan emas usia dini: pemenuhan kasih sayang dan kebebasan bermain.'),
        ('SOTAB', 'anak-anak-tanpa-dosa', 'Memahami kepolosan anak pra-tamyiz yang bebas dari beban hukum taklif.'),
        ('SOTAB', 'anak-terlahir-untuk-dididik', 'Amanah fitrah sejak lahir yang membutuhkan lingkungan subur.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Tamyiz.md': [
        ('SKIS', 'pendidikan-karakter-usia-7-10-tahun', 'Fase tamyiz: pembiasaan shalat 5.000 kali dengan keteladanan tanpa kekerasan.'),
        ('SKIS', 'cara-mendidik-hati-anak-agar-tumbuh-keikhlasan', 'Membimbing nalar anak membedakan benar dan salah secara sukarela.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md': [
        ('SKIS', 'pendidikan-usia-10-14-tahun', 'Fase transisi murahaqah: penegakan disiplin amanah dan pemisahan tempat tidur.'),
        ('SKIS', 'pendidikan-karakter-usia-10-14-tahun', 'Strategi pendampingan menjelang pubertas dan kedewasaan akil baligh.'),
        ('SKIS', 'pendidikan-anak-usia-10-tahun-s-d-baligh', 'Pedoman praktis mendampingi perubahan hormonal dan emosi anak pra-baligh.'),
        ('SKIS', 'ada-apa-dengan-remaja', 'Mendekonstruksi mitos kenakalan remaja melalui kacamata syariat.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Syabab.md': [
        ('SKIS', 'pendidikan-karakter-usia-aqil-baligh', 'Kesiapan memikul beban taklif syar\'i dan kemandirian hidup pemuda pasca-baligh.'),
        ('SKIS', 'teknik-pendidikan-post-aqil-baligh-usia-15-tahun', 'Metode pendampingan pemuda usia 15 tahun ke atas menuju kedewasaan sosial.'),
        ('SKIS', 'konsep-he-post-aqil-baligh-usia-15-tahun', 'Rancang bangun pendidikan mandiri dan penjurusan karir pasca-aqil baligh.'),
        ('SKIS', 'katakan-pemuda-bukan-remaja', 'Menolak glorifikasi status labil remaja demi mencetak pemuda berjiwa kesatria.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/index.md': [
        ('SKIS', 'karakter-perkembangan', 'Peta komprehensif penahapan etape usia fitrah manusia menurut Manhaj Nabawi.'),
        ('SKIS', 'sekilas-pandang-usia-0-7-tahun', 'Etape awal pengisian cinta kasih.'),
        ('SKIS', 'pendidikan-karakter-usia-7-10-tahun', 'Etape pembiasaan disiplin sukarela.'),
        ('SKIS', 'pendidikan-karakter-usia-aqil-baligh', 'Etape penyempurnaan akil baligh.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/index.md': [
        ('SKIS', 'karakteristik', 'Filosofi kurikulum berbasis fitrah dan penguatan pilar karakter nabawiyah.'),
        ('SOTAB', 'anak-itu-benih-bukan-bata', 'Paradigma benih hidup yang tumbuh dari dalam, bukan bata yang dicetak kaku dari luar.'),
        ('SKIS', 'anak-bukanlah-kertas-kosong', 'Menolak teori tabula rasa: setiap anak lahir membawa cetak biru fitrah Ilahi.')
    ],

    # ─── Insan: Bakat & Asesmen TB40 ─────────────────────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md': [
        ('SKIS', 'karakter-bakat', 'Konsep Al-Mauhibah: anugerah potensi unik yang telah diinstal Allah pada setiap anak.'),
        ('SKIS', 'setiap-anak-punya-bakat-unggul', 'Kaidah optimisme fitrah: tidak ada anak bodoh, setiap insan punya keunggulan amal.'),
        ('SOTAB', 'mengenal-bakat-cara-alami', 'Metodologi observasi alamiah mengenali bakat anak melalui Rukun 3A.'),
        ('PKN', 'buku-tafsir-bakat-1', 'Buku resmi Kupas Tuntas Tafsir Bakat TB-40 karya Ustadz Abdul Kholiq.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40.md': [
        ('SOTAB', 'mengenal-bakat-cara-alami', 'Observasi keseharian anak untuk memetakan kekuatan sifat dan minat peran.'),
        ('SKIS', 'kiat-menggali-misteri-bakat', 'Langkah taktis orang tua menemukan panggilan hidup (*calling*) anak.'),
        ('PKN', 'buku-tafsir-bakat-1', 'Instrumen terstandarisasi pengujian bakat nabawiyah.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md': [
        ('PKN', 'buku-tafsir-bakat-1', 'Katalog butir pertanyaan kuisioner asesmen 40 pilar bakat.'),
        ('SOTAB', 'mengenal-bakat-cara-alami', 'Validasi hasil tes tertulis dengan observasi perilaku nyata di lapangan.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Memerintah.md': [
        ('SKIS', 'karakter-bakat', 'Rumpun bakat mempengaruhi dan memimpin (At-Ta\'tsir).'),
        ('SKIS', 'setiap-anak-punya-bakat-unggul', 'Mengasah potensi kepemimpinan anak sejak dini.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Berpikir.md': [
        ('SKIS', 'karakter-bakat', 'Rumpun bakat cerdas dan analitis (At-Tafkir).'),
        ('SKIS', 'kiat-menggali-misteri-bakat', 'Mengasah ketajaman firasat, hikmah, dan inovasi anak.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Berperasaan.md': [
        ('SKIS', 'karakter-bakat', 'Rumpun bakat kepekaan rasa nurani batin (Asy-Syu\'ur).'),
        ('SOTAB', 'mengenal-bakat-cara-alami', 'Mengelola kepekaan empati menjadi kekuatan karya kebaikan.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Melayani.md': [
        ('SKIS', 'karakter-bakat', 'Rumpun bakat pengabdian dan ketulusan khidmah (Al-Khidmah).'),
        ('SOTAB', 'melengkapi-bukan-mengalahkan', 'Menemukan kemuliaan hidup dalam memberi manfaat bagi sesama.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Bekerja Keras.md': [
        ('SKIS', 'karakter-bakat', 'Rumpun bakat ketangguhan fisik dan etos kerja (Al-Hamasah).'),
        ('SKIS', 'setiap-anak-punya-bakat-unggul', 'Menyalurkan energi tinggi anak aktif menuju produktivitas amal shalih.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Bekerja Sama.md': [
        ('SKIS', 'karakter-bakat', 'Rumpun bakat jejaring dan keharmonisan sosial (At-Ta\'amul).'),
        ('SOTAB', 'melengkapi-bukan-mengalahkan', 'Sinergi peradaban: menyatukan keunikan sifat untuk saling melengkapi.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/index.md': [
        ('SKIS', 'karakteristik', 'Fondasi filosofis hakikat manusia seutuhnya dalam manhaj nabawi.'),
        ('SOTAB', 'anak-itu-benih-bukan-bata', 'Menumbuhkan fitrah insani dengan pendekatan organik.'),
        ('PKN', 'meniti-paradigma-pkn', 'Cetak biru rekonstruksi manusia berkarakter khairu ummah.')
    ],

    # ─── Pendidikan Ideal & Metode Mendidik ───────────────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/index.md': [
        ('PKN', 'konsep-ideal-ke-praktik-nyata', 'Menjembatani konsep agung akil baligh ke dalam praktik pengasuhan harian.'),
        ('SKIS', 'menumbuhkan-keikhlasan-pada-anak-bukan-dengan-paksaan-dan-lemah', 'Membangun ketaatan sukarela tanpa ancaman.'),
        ('SKIS', 'memperbaiki-niat-dalam-mendidik-anak', 'Meluruskan orientasi pengasuhan semata mengharap ridha Allah.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Benang Merah Pendidikan.md': [
        ('SOTAB', 'benalu-pendidikan', 'Kritik tajam penyakit kurikulum modern yang menjerat dan melemahkan fitrah anak.'),
        ('SKIS', 'kuatkan-akar-pendidikan-pada-anak', 'Menancapkan akar akidah dan adab sebelum menuntut buah prestasi akademis.'),
        ('SKIS', 'anak-bukanlah-kertas-kosong', 'Penegasan fitrah asali anak dalam pendidikan Islam.'),
        ('SKIS', 'surga-dunia-dalam-mendidik-anak', 'Menemukan kebahagiaan proses tarbiyah di rumah.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Pembelajaran Alamiah.md': [
        ('PKN', 'ga-perlu-membuat-pembelajaran', 'Menjadikan seluruh denyut keseharian hidup sebagai laboratorium belajar alami.'),
        ('PKN', 'pembelajaran-kemandirian', 'Membiasakan anak mengurus diri sendiri dan bertanggung jawab atas amalnya.'),
        ('PKN', 'pembelajaran-agribisnis', 'Menghidupkan jiwa kewirausahaan dan keakraban dengan alam sejak belia.'),
        ('PKN', 'pembelajaran-kepedulian-lingkungan', 'Mendidik santri beradab menjaga kebersihan dan ekosistem bumi.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Kurikulum Kemandirian Berbasis Maqashid Syariah.md': [
        ('PKN', 'pembelajaran-kemandirian', 'Prinsip kemandirian finansial dan sosial pasca-akil baligh.'),
        ('SKIS', 'konsep-he-post-aqil-baligh-usia-15-tahun', 'Rancang bangun kurikulum mandiri bagi santri pasca-15 tahun.'),
        ('SOTAB', 'liburan-bermakna', 'Mengisi masa liburan dengan karya kemandirian dan proyek nyata.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Bank Studi Kasus.md': [
        ('SKIS', 'anak-anak-yang-tersalahkan', 'Membela anak-anak yang terstigma nakal padahal memendam energi bakat besar.'),
        ('SKIS', 'anak-sortiran', 'Mengurai fenomena anak yang tersingkirkan oleh sistem sekolah konvensional.'),
        ('SKIS', 'tidak-mau-sekolah', 'Solusi komprehensif mengurai akar mogok sekolah karena trauma pengasuhan.'),
        ('SOTAB', 'kenakalan-anak-yang-paling-berbahaya', 'Membedah aneka bentuk penyimpangan perilaku dan cara pemulihannya.'),
        ('SKIS', 'menghadapi-sibling-rivalry-anak', 'Panduan menangani persaingan dan pertengkaran antar saudara kandung.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md': [
        ('SKIS', 'disiplin-mesin-hewan-dan-manusia', 'Membedakan penegakan disiplin fitrah manusiawi dengan kepatuhan robotik.'),
        ('SOTAB', 'hukuman-yang-membunuh-karakter', 'Batas ketegasan syar\'i yang tidak melukai harga diri anak.'),
        ('SOTAB', 'ketika-anak-pergi-menjauh', 'Mendeteksi kerenggangan emosi anak saat batasan pengasuhan dilanggar.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Imunitas Sosial.md': [
        ('SKIS', 'berani-tampil-beda', 'Membangun integritas dan ketangguhan moral anak di tengah arus pergaulan bebas.'),
        ('SOTAB', 'kemerdekaan-sejati-dimulai-dari-hati', 'Kekokohan prinsip batin yang tidak mudah terombang-ambing tren peradaban.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md': [
        ('PKN', 'buku-menumbuhkan-kesadaran-beramal', 'Karya monumental Ustadz Abdul Kholiq tentang proses tumbuhnya kesadaran amal.'),
        ('SKIS', 'menumbuhkan-keikhlasan-pada-anak-bukan-dengan-paksaan-dan-lemah', 'Kaidah menumbuhkan niat beramal tanpa represi lahiriah.'),
        ('PKN', 'akses-pikiran-bawah-sadar', 'Menanamkan nilai-nilai kebaikan ke dalam memori bawah sadar anak.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Hati.md': [
        ('PKN', 'bahasa-hati', 'Naskah rujukan resmi PKN mengenai hakikat Bahasa Hati dan getaran rasa cinta.'),
        ('SOTAB', 'bahasa-hati-bukan-pembiaran', 'Meluruskan anggapan keliru: Bahasa Hati bukan membiarkan kesalahan anak.'),
        ('SKIS', 'bahasa-cinta', 'Menghidupkan suasana kasih sayang dan penerimaan tanpa syarat di rumah.'),
        ('SOTAB', 'internet-cinta', 'Menjaga koneksi batin orang tua dan anak agar tidak terputus oleh distraksi gawai.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Lisan.md': [
        ('PKN', 'lebih-dari-sekedar-ungkapan-kata', 'Kekuatan kata-kata hikmah (*qaulan sadida*) yang membekas di jiwa anak.'),
        ('SKIS', 'bahasa-cinta', 'Mengemas nasihat lisan dalam balutan kehangatan kasih sayang.'),
        ('SKIS', 'mengendalikan-kemarahan-pada-anak', 'Menjaga lisan dari kata-kata celaan dan laknat saat menegur anak.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Tangan.md': [
        ('SKIS', 'disiplin-mesin-hewan-dan-manusia', 'Penerapan ketegasan ta\'dib nabawi yang memuliakan martabat manusia.'),
        ('SOTAB', 'hukuman-yang-membunuh-karakter', 'Membedakan hukuman edukatif (*dharbun ghairu mubarrih*) dengan kekerasan fisik.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/index.md': [
        ('PKN', 'bahasa-hati', 'Hierarki Tiga Bahasa Pengasuhan Nabawiyah: Hati, Lisan, dan Tangan.'),
        ('SKIS', 'bahasa-cinta', 'Pondasi awal komunikasi kasih sayang.'),
        ('SKIS', 'disiplin-mesin-hewan-dan-manusia', 'Penegakan aturan syariat secara beradab.')
    ],

    # ─── Luka dan Hutang Pengasuhan / Recovery ───────────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/index.md': [
        ('SKIS', 'recovery-karakter-berbasis-fitrah', 'Konsep pemulihan cedera emosional anak akibat luka dan kekosongan pengasuhan.'),
        ('SOTAB', 'menghapus-noda-hati-bagian-9-pemulihan-luka-hati', 'Protokol 9 tahap menghapus noda dan membalut luka batin anak.'),
        ('SOTAB', 'menghapus-noda-hati-bagian-1-penyebab-luka-hati', 'Menganalisis akar penyebab luka batin dari sikap orang tua.'),
        ('SOTAB', 'anak-digital-kurang-mampu-membasuh-lukanya', 'Kerapuhan emosional generasi digital dalam mengobati lukanya sendiri.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md': [
        ('SKIS', 'recovery-karakter-berbasis-fitrah', 'Manual komprehensif restorasi karakter anak berbasis kemurnian fitrah.'),
        ('SOTAB', 'menghapus-noda-hati-bagian-9-pemulihan-luka-hati', 'Panduan klinis pengasuhan dalam memulihkan luka batin.'),
        ('SOTAB', 'menghapus-noda-hati-bagian-5-menabur-obat-luka', 'Menabur obat penerimaan dan ketulusan untuk menyembuhkan luka hati.'),
        ('PKN', 'buku-recovery-berbasis-fitrah', 'Buku panduan resmi Recovery Berbasis Fitrah karya Ustadz Abdul Kholiq.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md': [
        ('SOTAB', 'gagal-tapi-berhasil', 'Sikap tawadhu menghadapi euforia semu keberhasilan pendidikan.'),
        ('SOTAB', 'maju-kena-mundur-kena', 'Ketenangan batin di tengah ujian dan dinamika tarbiyah anak.'),
        ('SKIS', 'sepasang-sayap-khouf-dan-roja-dalam-mendidik-anak', 'Menjaga keseimbangan antara optimisme dan kewaspadaan diri.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/index.md': [
        ('SKIS', 'recovery-karakter-berbasis-fitrah', 'Pintu gerbang direktori pemulihan luka pengasuhan berbasis fitrah.'),
        ('SOTAB', 'menghapus-noda-hati-bagian-9-pemulihan-luka-hati', 'Siklus restorasi kalbu anak dan orang tua.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/index.md': [
        ('PKN', 'konsep-ideal-ke-praktik-nyata', 'Paradigma kurikulum Pendidikan Ideal Nabawiyah menuju kematangan akil baligh.'),
        ('SKIS', 'kuatkan-akar-pendidikan-pada-anak', 'Pentingnya mengokohkan pondasi adab dan akidah anak.'),
        ('SOTAB', 'anak-itu-benih-bukan-bata', 'Menumbuhkan potensi anak secara alamiah sesuai sunnatullah.')
    ],

    # ─── Implementasi: Peran & Tanggung Jawab ─────────────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md': [
        ('SKIS', 'ayah-bangunlah-dari-tidurmu', 'Seruan menggugah bagi para ayah untuk mengambil alih kepemimpinan pengasuhan di rumah.'),
        ('SKIS', 'orang-tua-mogol-setengah-matang', 'Kritik fenomena orang tua setengah matang yang belum tuntas mendewasakan diri.'),
        ('SKIS', 'orang-tua-pemberani', 'Keberanian orang tua mengambil jalan sunyi mendidik anak di luar arus mayoritas.'),
        ('SKIS', 'anakku-aku-didik-sendiri-di-rumah', 'Inspirasi pendidikan berbasis rumah (*home education*) berlandaskan sunnah.'),
        ('SOTAB', 'jangan-pernah-merasa-berjasa-dalam-mendidik', 'Menjaga keikhlasan orang tua tanpa menuntut balas budi dari anak.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md': [
        ('SOTAB', 'guru-manusia', 'Membangkitkan kembali martabat guru sebagai penumbuh jiwa manusiawi, bukan robot kurikulum.'),
        ('SOTAB', 'guru-robot-bukan-pendidik', 'Kritik mekanisasi peran guru yang hanya bertindak sebagai penyampai materi ujian.'),
        ('SOTAB', 'gurubot', 'Bahaya desensitisasi empati pendidik di era otomasi dan digital.'),
        ('SOTAB', 'andai-sekolah-dibubarkan', 'Refleksi mendalam fungsi hakiki sekolah sebagai mitra pendukung keluarga.'),
        ('PKN', 'testimoni-akademi-guru', 'Kisah transformasi paradigma para guru peserta Akademi Guru PKN se-Indonesia.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md': [
        ('SKIS', 'tanggung-jawab-pendidikan', 'Naskah rujukan SKIS mengenai mandat mutlak pendidikan anak di pundak orang tua.'),
        ('SKIS', 'syarat-utama-mendidik-anak', 'Syarat pokok keberhasilan tarbiyah: kesalehan pribadi orang tua dan keteladanan.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/index.md': [
        ('SKIS', 'tanggung-jawab-pendidikan', 'Arsitektur sinergi tripartit: Orang Tua, Guru, dan Lembaga Pendidikan.'),
        ('SKIS', 'ayah-bangunlah-dari-tidurmu', 'Pentingnya peran kepemimpinan ayah dalam keluarga.'),
        ('SOTAB', 'guru-manusia', 'Memuliakan martabat pendidik sebagai teladan adab.')
    ],

    # ─── Implementasi: Kaidah, Standar & Program Resmi ────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md': [
        ('PKN', 'konsep-ideal-ke-praktik-nyata', 'Empat kaidah operasional pengasuhan: Tadarruj, Taisir, Wasathiyah, dan Qudwah.'),
        ('SKIS', 'karakteristik', 'Penerapan kaidah-kaidah karakter nabawiyah dalam tata kelola harian.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md': [
        ('SKIS', 'karakteristik', 'Empat elemen ekosistem sekolah karakter: Iman, Adab, Belajar, dan Bakat.'),
        ('SKIS', 'sekilas-pandang', 'Gambaran integrasi 4 elemen kurikulum di Sekolah Karakter Imam Syafi\'i.'),
        ('PKN', 'konsep-ideal-ke-praktik-nyata', 'Penyelarasan elemen kurikulum dengan kebutuhan fitrah anak.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md': [
        ('PKN', 'panduan-implementasi-pkn-batch-3', 'Dokumen resmi Panduan Implementasi Standar PKN Batch 3.'),
        ('PKN', 'panduan-implementasi-pkn-batch-4', 'Standarisasi mutu kelembagaan pendidikan karakter nabawiyah Batch 4.'),
        ('PKN', 'panduan-implementasi-standar', 'Manual resmi 8 Standar Mutu Pendidikan Karakter Nabawiyah.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md': [
        ('PKN', 'implementasi-terbaik', 'Best practices penerapan manhaj PKN pada sekolah formal, pesantren, dan madrasah.'),
        ('PKN', 'panduan-implementasi-standar', 'Pedoman adaptasi standar lembaga sesuai kondisi lokal.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md': [
        ('PKN', 'panduan-implementasi-standar', 'Format resmi Rencana Pelaksanaan Pembelajaran (RPP) terpadu karakter fitrah.'),
        ('SOTAB', 'mengenal-bakat-cara-alami', 'Pedoman pengisian lembar observasi harian santri di lapangan.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Program dan Kegiatan Pendidikan Karakter Nabawiyah.md': [
        ('PKN', 'panduan-implementasi-pkn-batch-3', 'Dokumentasi kegiatan Panduan Implementasi Standar PKN Batch 3.'),
        ('PKN', 'panduan-implementasi-pkn-batch-4', 'Dokumentasi standarisasi mutu lembaga Batch 4 di berbagai daerah.'),
        ('PKN', 'event-panduan-implementasi-standar-pendidikan-karakter-nabawiyah', 'Laporan agenda nasional standarisasi sekolah Islam.'),
        ('PKN', 'testimoni-akademi-guru', 'Kumpulan catatan dan evaluasi pelaksanaan Akademi Guru (AKG) 17 batch.'),
        ('PKN', 'profil-ustadz-abdul-kholiq', 'Profil perjalanan dakwah Ustadz Abdul Kholiq membina program-program PKN.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/index.md': [
        ('PKN', 'panduan-implementasi-standar', 'Direktori kaidah operasional dan standar kelembagaan PKN.'),
        ('SKIS', 'karakteristik', 'Standar operasional kurikulum berbasis karakter nabawiyah.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tawakkal dan Doa.md': [
        ('SKIS', 'sepasang-sayap-khouf-dan-roja-dalam-mendidik-anak', 'Menyerahkan hasil akhir pengasuhan sepenuhnya kepada kekuasaan Allah.'),
        ('SOTAB', 'cinta-dan-keteladanan', 'Kekuatan doa dan ketulusan batin orang tua melintasi ruang dan waktu.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tazkiyatun Nafs.md': [
        ('SOTAB', 'menghapus-noda-hati-bagian-9-pemulihan-luka-hati', 'Pembersihan kotoran batin orang tua sebagai syarat mengalirkan berkah pendidikan.'),
        ('SOTAB', 'kemerdekaan-sejati-dimulai-dari-hati', 'Meraih kemerdekaan jiwa melalui penyucian kalbu dari penyakit hati.'),
        ('SKIS', 'cara-mendidik-hati-anak-agar-tumbuh-keikhlasan', 'Menanamkan benih tazkiyah sejak usia dini.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/index.md': [
        ('SOTAB', 'kemerdekaan-sejati-dimulai-dari-hati', 'Penataan faktor internal jiwa pendidik dan proteksi faktor eksternal lingkungan.'),
        ('SKIS', 'kuatkan-akar-pendidikan-pada-anak', 'Membangun benteng pertahanan moral anak dari pengaruh negatif luar.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/index.md': [
        ('PKN', 'implementasi-terbaik', 'Kompilasi panduan praktis implementasi Manhaj PKN di sekolah dan keluarga.'),
        ('PKN', 'panduan-implementasi-standar', 'Standar kelembagaan PKN yang teruji di lapangan.'),
        ('SKIS', 'karakteristik', 'Pengalaman implementasi kurikulum karakter di SKIS Semarang.')
    ],

    # ─── Insight, Teknis, & Arsitektur Sistem ─────────────────────────────────
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight/SOTABH.md': [
        ('SOTAB', 'anak-itu-benih-bukan-bata', 'Paradigma revolusioner Belajar Hati: anak adalah benih hidup yang tumbuh mekar.'),
        ('SOTAB', 'satu-anak-satu-kurikulum', 'Kaidah keadilan tarbiyah: menghargai keunikan rancang bangun fitrah setiap anak.'),
        ('SOTAB', 'kami-ajarkan-huruf-tapi-lupa-menumbuhkan-hati', 'Kritik pedas pengajaran huruf dan teks yang melupakan penanaman adab kalbu.'),
        ('SOTAB', 'mengenal-bakat-cara-alami', 'Metodologi observasi 3A SOTAB HEBAT dalam memvalidasi panggilan bakat anak.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight/index.md': [
        ('SOTAB', 'anak-itu-benih-bukan-bata', 'Khazanah artikel pemikiran mendalam Belajar Hati dan Manhaj PKN.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Arahan Teknis Implementasi.md': [
        ('PKN', 'konsep-ideal-ke-praktik-nyata', 'Petunjuk teknis operasional penataan jadwal harian dan adab santri.'),
        ('PKN', 'panduan-implementasi-standar', 'Checklist teknis kesiapan lembaga mengadopsi manhaj PKN.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/index.md': [
        ('PKN', 'konsep-ideal-ke-praktik-nyata', 'Indeks panduan teknis dan wawasan lapangan implementasi PKN.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/PKN Blueprint Arsitektur Sistem.md': [
        ('PKN', 'meniti-paradigma-pkn', 'Diagram arsitektur utuh sistem pemikiran Pendidikan Karakter Nabawiyah.'),
        ('SKIS', 'karakteristik', 'Cetak biru kurikulum karakter nabawiyah terpadu.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/index.md': [
        ('PKN', 'meniti-paradigma-pkn', 'Peta besar integrasi paradigma dan strategi implementasi Manhaj PKN.'),
        ('SKIS', 'karakteristik', 'Filosofi kurikulum dan pengalaman lapangan SKIS Semarang.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/FAQ Ringkas.md': [
        ('SKIS', 'tanya-jawab-teknik-pendidikan-post-aqil-baligh-usia-15-tahun', 'Tanya jawab seputar pendampingan pemuda pasca-aqil baligh 15 tahun ke atas.'),
        ('SKIS', 'tanya-jawab-konsep-pendidikan-post-aqil-baligh-usia-15-tahun', 'Tanya jawab konsep pendidikan mandiri dan penjurusan bakat.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Referensi Kajian Video.md': [
        ('PKN', 'profil-ustadz-abdul-kholiq', 'Profil Ustadz Abdul Kholiq dan rekaman ceramah kajian tematik PKN.'),
        ('PKN', 'meniti-paradigma-pkn', 'Dokumentasi perjalanan kajian perumusan manhaj PKN.')
    ],
    'Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/index.md': [
        ('PKN', 'meniti-paradigma-pkn', 'Dokumen induk Pendidikan Karakter Nabawiyah.'),
        ('SKIS', 'karakteristik', 'Pedoman karakter dan tata kelola lembaga.')
    ],
    'Paradigma - Implementasi PKN/index.md': [
        ('PKN', 'meniti-paradigma-pkn', 'Gerbang utama Paradigma dan Implementasi PKN.'),
        ('SKIS', 'karakteristik', 'Prinsip-prinsip dasar pendidikan karakter Islam.')
    ],

    # ─── Renungan ────────────────────────────────────────────────────────────
    'Renungan/Hak dan Kewajiban.md': [
        ('SOTAB', 'cinta-dan-keteladanan', 'Keseimbangan adil antara hak anak mendapatkan cinta dan penunaian kewajiban amalnya.'),
        ('SKIS', 'anak-bukanlah-kertas-kosong', 'Memenuhi hak bermain dan hak fitrah anak sebelum menuntut kewajiban syar\'i.')
    ],
    'Renungan/Disiplin Positif PKN.md': [
        ('SKIS', 'disiplin-mesin-hewan-dan-manusia', 'Pembedaan mendasar antara disiplin fitrah nabawiyah dengan kepatuhan mekanis paksaan.'),
        ('SOTAB', 'hukuman-yang-membunuh-karakter', 'Kritik terhadap hukuman fisik dan emosional yang melumpuhkan jiwa anak.'),
        ('SOTAB', 'kekerasan-anak-cermin-kelalaian', 'Refleksi mendalam: kekerasan lahiriah anak adalah cermin kelalaian pengasuhan orang tua.')
    ],
    'Renungan/Persepsi Positif.md': [
        ('PKN', 'persepsi-artikel', 'Naskah rujukan resmi PKN mengenai pembentukan persepsi positif dan siklus amal berulang.'),
        ('PKN', 'akses-pikiran-bawah-sadar', 'Mekanisme persepsi bawah sadar dalam membentuk motivasi ibadah jangka panjang.'),
        ('SOTAB', 'bukan-jalan-keluar-tapi-cari-jalan-kedalam', 'Melihat ke dalam lubuk hati untuk memperbaiki prasangka dan persepsi diri.')
    ],
    'Renungan/index.md': [
        ('SOTAB', 'cinta-dan-keteladanan', 'Kumpulan risalah renungan pengasuhan hati bagi orang tua dan pendidik.'),
        ('SKIS', 'surga-dunia-dalam-mendidik-anak', 'Menemukan kedamaian dan keindahan dalam merawat amanah Ilahi.')
    ],

    # ─── Beranda & Referensi ─────────────────────────────────────────────────
    'index.md': [
        ('PKN', 'beranda-pkn', 'Portal utama pergerakan Manhaj Pendidikan Karakter Nabawiyah (karakternabawiyah.com).'),
        ('SKIS', 'pendidikan', 'Khazanah pemikiran pendidikan berbasis fitrah Sekolah Karakter Imam Syafi\'i Semarang.'),
        ('SKIS', 'karakteristik', 'Filosofi kurikulum dan pilar karakter Sekolah Karakter.'),
        ('SOTAB', 'anak-itu-benih-bukan-bata', 'Paradigma Belajar Hati SOTAB HEBAT: menumbuhkan benih fitrah kehidupan.')
    ],
    'Master Katalog Dalil Al-Quran.md': [
        ('PKN', 'meniti-paradigma-pkn', 'Rujukan ayat-ayat Al-Qur\'an dalam korpus dalil manhaj PKN.')
    ],
    'Master Katalog Dalil Hadits dan Sunnah.md': [
        ('PKN', 'meniti-paradigma-pkn', 'Rujukan hadits-hadits shahih dan sunnah nabawiyah dalam manhaj PKN.')
    ],
    'Referensi/Referensi Tambahan Buku Cetak.md': [
        ('PKN', 'buku-pendidikan-karakter-nabawiyah', 'Buku babon induk Pendidikan Karakter Nabawiyah.'),
        ('PKN', 'buku-menumbuhkan-kesadaran-beramal', 'Buku Menumbuhkan Kesadaran Beramal karya Ustadz Abdul Kholiq.'),
        ('PKN', 'buku-tafsir-bakat-1', 'Buku Kupas Tuntas Tafsir Bakat TB-40.'),
        ('PKN', 'buku-recovery-berbasis-fitrah', 'Buku Recovery Karakter Berbasis Fitrah.'),
        ('PKN', 'buku-kurikulum-sekolah-karakter-islam', 'Buku Kurikulum Sekolah Karakter Islam.')
    ],
    'Referensi/Tentang Aplikasi Wiki PKN.md': [
        ('PKN', 'profil-ustadz-abdul-kholiq', 'Profil narasumber utama dan perumus Manhaj PKN Ustadz Abdul Kholiq.'),
        ('SKIS', 'sekilas-pandang', 'Latar belakang historis kurikulum fitrah di SKIS Semarang.')
    ],
    'Referensi/index.md': [
        ('PKN', 'beranda-pkn', 'Portal induk resmi Pendidikan Karakter Nabawiyah.'),
        ('SKIS', 'sekilas-pandang', 'Arsip resmi Sekolah Karakter Imam Syafi\'i Semarang.')
    ],
    'Referensi/Bahan Tayang & Slide PPTX.md': [
        ('PKN', 'panduan-implementasi-standar', 'Materi tayang presentasi resmi standardisasi lembaga PKN.')
    ],
    'Referensi/Korpus Dalil & Atsar Klasik.md': [
        ('PKN', 'meniti-paradigma-pkn', 'Katalog dalil turats Islam klasik rujukan manhaj PKN.')
    ],
    'Referensi/Panduan Kontribusi.md': [
        ('SKIS', 'karakteristik', 'Pedoman integritas penulisan dan kontribusi kurikulum karakter.')
    ],
    'Referensi/Pengembangan Software dan Ekosistem Digital PKN.md': [
        ('PKN', 'tools-pkn', 'Katalog tools dan aplikasi rekayasa perangkat lunak pendukung manhaj PKN.')
    ]
}

def generate_source_callout(sources_list):
    """Menghasilkan blok callout markdown rujukan sumber asli."""
    lines = [
        "> [!quote] Naskah Sumber Asli & Khazanah Artikel Terkait",
        "> Materi dalam artikel ini memiliki keterkaitan sanad keilmuan dan disintesis dari naskah/tulisan asli narasumber pada situs resmi berikut:"
    ]
    for item in sources_list:
        src_type, slug = item[0], item[1]
        note = item[2] if len(item) > 2 else ""
        data = source_db.get((src_type, slug))
        if not data:
            continue
        badge = data['badge']
        title = data['title']
        url = data['url']
        lines.append(">")
        lines.append(f"> - {badge} **[{data['source']}] {title}**  ")
        lines.append(f">   🔗 Sumber Asli: [{url}]({url})  ")
        if note:
            lines.append(f">   *{note}*  ")
    return "\n".join(lines)

def process_file(rel_path, sources_list):
    file_path = CONTENT_DIR / rel_path
    if not file_path.exists():
        print(f"[WARN] File tidak ditemukan: {rel_path}")
        return False

    content = file_path.read_text(encoding="utf-8")

    # Cek jika callout sumber asli sudah pernah diinjeksi sebelumnya
    if "> [!quote] Naskah Sumber Asli & Khazanah Artikel Terkait" in content:
        # Hapus blok lama untuk digantikan yang terbaru
        content = re.sub(
            r">\s*\[!quote\]\s*Naskah Sumber Asli & Khazanah Artikel Terkait.*?(?=\n---\n|\n<!-- START_OFFICE_PPTX_EMBED -->|\n<!-- END_OFFICE_PPTX_EMBED -->|\Z)",
            "",
            content,
            flags=re.DOTALL
        )
        # Bersihkan sisa newline ganda jika ada
        content = re.sub(r'\n{3,}', '\n\n', content)

    callout_block = generate_source_callout(sources_list)
    callout_with_delimiters = f"\n\n---\n\n{callout_block}\n"

    # Penempatan:
    # 1. Sebelum <!-- START_OFFICE_PPTX_EMBED --> jika ada
    # 2. Atau sebelum > [!quote] Dokumen & Slide Presentasi Rujukan Resmi PKN jika ada
    # 3. Atau di akhir berkas
    if "<!-- START_OFFICE_PPTX_EMBED -->" in content:
        parts = content.split("<!-- START_OFFICE_PPTX_EMBED -->", 1)
        # Cek apakah di akhir parts[0] sudah ada blok PPTX intro
        new_content = parts[0].rstrip() + callout_with_delimiters + "\n<!-- START_OFFICE_PPTX_EMBED -->" + parts[1]
    elif "> [!quote] Dokumen & Slide Presentasi Rujukan Resmi PKN" in content:
        parts = content.split("> [!quote] Dokumen & Slide Presentasi Rujukan Resmi PKN", 1)
        new_content = parts[0].rstrip() + callout_with_delimiters + "\n> [!quote] Dokumen & Slide Presentasi Rujukan Resmi PKN" + parts[1]
    else:
        new_content = content.rstrip() + callout_with_delimiters

    file_path.write_text(new_content, encoding="utf-8")
    return True

def main():
    print(f"Memulai injeksi tautan sumber asli ke {len(ARTICLE_SOURCE_MAP)} artikel wiki...")
    success_count = 0
    total_links_injected = 0

    for rel_path, sources in ARTICLE_SOURCE_MAP.items():
        if process_file(rel_path, sources):
            success_count += 1
            total_links_injected += len(sources)
            print(f"  [OK] {rel_path} (+{len(sources)} link sumber)")

    print("\n" + "=" * 60)
    print(f"SELESAI! Berhasil memproses {success_count} artikel.")
    print(f"Total tautan artikel sumber asli yang disematkan: {total_links_injected}")
    print("=" * 60)

if __name__ == "__main__":
    main()

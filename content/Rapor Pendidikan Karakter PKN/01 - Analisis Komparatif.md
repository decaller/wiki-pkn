---
title: "Analisis Komparatif Rapor Karakter PKN"
description: "Perbandingan panduan rapor awal, dokumen wiki, instrumen eksternal, serta keputusan desain yang masih memerlukan telaah."
tags: [rapor-pkn, draf-riset]
draft: true
status: draf-riset
review_status: pending
---

# Analisis Komparatif Rapor Karakter PKN

> [!WARNING] Draf riset — belum tervalidasi atau disahkan
> **Temuan** melaporkan isi sumber; **interpretasi** menilai hubungan dan risikonya; **usulan** adalah keputusan editorial yang diajukan. Ketiganya bukan pengesahan instrumen. [Indeks paket](index.md).

## 1. Kesimpulan analisis

**Interpretasi:** bahan repo cukup untuk menyusun paket telaah dan draf percakapan pendidikan, tetapi belum cukup untuk menetapkan satu alat ukur karakter yang teruji. Masalah utama bukan kurangnya kolom rapor: konstruk batin bercampur dengan perilaku, versi rubrik tidak selaras, status bukti kosong berbeda, serta dukungan lingkungan belum selalu dipisahkan dari capaian anak.[^riset]

**Usulan:** gunakan laporan naratif yang dapat ditelusuri ke peristiwa dan karya; pertahankan rujukan indikator asal; jelaskan bantuan, kesempatan, batas pengamatan, dan tindakan pendamping. Jangan menghasilkan skor atau kategori gabungan. Pilihan naratif juga perlu diuji: bahasa pujian dapat menyembunyikan bias dan tafsir batin.

## 2. Panduan awal dibandingkan wiki dan riset

Panduan awal yang dikaji adalah `side-project/rapor-pendidikan-karakter/panduan_lengkap_rapor_pendidikan_karakter_nabawiyah.md`, terutama bagian perbandingan konvensional–PKN, tahapan usia, parameter evaluasi, alur kerja, dan contoh rapor. Nomor bagian/heading dipakai karena Markdown tidak mempunyai halaman tetap. Dokumen asal dipertahankan.

| Tema | Temuan panduan awal | Pembanding dan interpretasi | Usulan untuk draf |
|---|---|---|---|
| Tujuan rapor | Menawarkan kolaborasi guru–wali, potensi unik, dan pendampingan | Selaras dengan jurnal dan narasi toolkit, tetapi kolaborasi tidak membuktikan pengukuran akurat.[^toolkit] | Rapor sebagai ringkasan dialog dukungan, bukan sertifikat kesalehan |
| Sistem nasional | Menyajikan nilai 0–100, P5, dan komponen “wajib” tanpa edisi/aturan yang ditunjukkan | Klaim nasional belum terverifikasi; jangan membangun oposisi PKN versus seluruh sistem nasional dari tabel tersebut | Periksa aturan jenjang yang berlaku secara terpisah; jangan menyatakan paket menggantikan rapor formal |
| Iman dan batin | Tangki cinta, mahabbah/raja’/khauf, cinta ibadah, profil jiwa dan ego | Bukan seluruhnya dapat diamati; toolkit bagian 7 membatasi inferensi niat/iman dari kejadian.[^toolkit] | Catat tindakan dan ucapan sukarela; hilangkan kesimpulan batin dari draf laporan |
| Fase | Urutan fase dan usia dipakai untuk arah pendampingan | Perangkat fase mempunyai isi berbeda menurut fase; angka usia dan versi tidak semuanya selaras.[^fase] | Simpan rujukan fase/versi; konteks bantuan bukan vonis keterlambatan, taklif, atau kelulusan |
| Kategori | Belum Tumbuh/Mulai Tumbuh/Tuntas Ma’ruf tanpa deskriptor keputusan memadai | Tidak identik dengan BT/MT/BK/MM toolkit atau skala perangkat lain | Tidak memetakan kategori tersebut ke kategori wiki; keputusan kategori ditunda |
| Bakat dan gaya belajar | TB40, firasat, VAK, jiwa–ego; klaim potensi 170 | Skor ipsatif TB40, skala 0–100, dan klaim 170 tidak dapat dianggap setara; dasar VAK dan pemetaan jiwa belum ditunjukkan.[^asesmen] | Portofolio aktivitas, minat sementara dan kesempatan eksplorasi; profil permanen/jalur otomatis tidak masuk rapor |
| Pengamatan | Microjournaling insidental, termasuk pascapelanggaran | Toolkit memberi catatan anekdot dan jurnal; kejadian menonjol saja berisiko bias negatif/seleksi.[^toolkit] | Pilih juga kegiatan rutin dan konteks berbeda; pisahkan fakta, interpretasi, bantuan dan belum diketahui |
| Visual dan operasi | Cetak grafik TB40 oleh TU dan dialog 15–20 menit | Kecepatan proses/keamanan dan manfaat grafik belum dibuktikan; akses TU ke semua jurnal tidak otomatis diperlukan | Tentukan penerima minimum dan uji beban seluruh proses; durasi bukan janji layanan |
| Contoh rapor | Profil jiwa/VAK/ego dan “Tuntas Ma’ruf” dicontohkan sebagai format siap pakai; ada label dokumen resmi | Contoh tidak menyajikan jejak bukti yang cukup untuk keputusan tersebut | Ganti pada draf baru dengan contoh sintetis berjejak; jangan mengubah sumber asal diam-diam |

**Yang dipertahankan:** hubungan sekolah–rumah, bahasa yang tidak merendahkan anak, perhatian pada kegiatan nyata, dan tindak lanjut konkret. **Yang ditahan:** klaim validitas, klasifikasi batin, penyeragaman fase, angka potensi, serta pengesahan administratif tanpa bukti dan penelaah berwenang.

## 3. Perbandingan riset instrumen eksternal

Inventaris berikut merangkum hasil pengumpulan sebelumnya; **bukan pengunduhan atau validasi baru**. Satu baris basis data dapat berupa identitas atau subitem matriks, bukan satu pertanyaan unik. Sumber, cakupan, bahasa dan pembatasannya tercatat dalam `data/extracted_elements/external_research/education_questionnaires/sources.csv` dan `usage_notes.csv`.[^eksternal]

| Sumber | Cakupan temuan terkumpul | Unit dan fungsi pembanding | Dapat dipelajari / tidak dapat dipindahkan |
|---|---|---|---|
| MPLS 2026 | 342 baris pada `indonesia_questions.csv` | Pengenalan karakteristik dan kebutuhan perkembangan murid, bukan AN/Sulingjar | Pelibatan keluarga dan konteks kebutuhan; bukan rubrik iman atau diagnosis |
| PISA 2022 | 1.023 baris pada `pisa_2022_questions.csv`; templat internasional bahasa Inggris, murid/sekolah dan opsi orang tua | Konteks pengalaman belajar dan lingkungan; bukan adaptasi Indonesia yang telah divalidasi | Pemisahan perspektif/responden dan konteks; bukan skor karakter PKN atau ambang fase |
| TALIS 2024 | 1.268 baris pada `talis_questions.csv`; guru dan dua varian kepala sekolah, butir bersama berulang | Pengalaman/praktik profesional dan lingkungan kerja pendidik | Dukungan dan refleksi pendidik; jangan memindahkannya menjadi capaian anak |
| Sulingjar komunitas | 179 butir terpisah; 148 dengan opsi sumber, 31 opsi tidak diketahui | Arsip pratinjau/blog; semua `authenticity_status` belum terverifikasi | Bahan audit sumber saja; bukan instrumen resmi kementerian atau dasar keputusan anak |
| Sulingjar resmi | FAQ menjelaskan input/proses lingkungan pembelajaran dan hasil satuan pendidikan | Evaluasi lingkungan, bukan hasil individu | Gunakan untuk menanyakan mutu dukungan sekolah; jangan turunkan hasil lembaga menjadi skor seorang anak.[^sulingjar] |
| Rapor Pendidikan Indonesia 2025 | Buku resmi 198 halaman; membahas data 2022–2024 | Publikasi sistem pendidikan, bukan rapor semester individu | Konteks perbaikan layanan; bukan validasi instrumen PKN atau dataset tahun data 2025 yang dirilis 2026.[^rapor] |

Master resmi berisi 2.633 baris MPLS/PISA/TALIS. Salinan Sulingjar komunitas **tidak digabungkan** ke master. Sebagian skala kelompok pada salinan komunitas tidak selaras dengan makna butir; opsi kosong berarti tidak diketahui, bukan otomatis pertanyaan terbuka. Tidak ada dasar untuk mengklaim bahwa seluruh butir Sulingjar bersifat persepsi atau tidak mempunyai jawaban substantif.[^eksternal]

**Interpretasi komparatif:** instrumen eksternal membantu merumuskan pertanyaan tentang pengalaman dan dukungan, bukan meminjam validitasnya. Perubahan bahasa, tujuan, responden, budaya, atau aturan skor memerlukan telaah tersendiri. Publikasi terbuka juga tidak otomatis berarti bebas redistribusi atau penggunaan komersial.

## 4. Lima lapis yang harus dipisahkan

| Lapis | Pertanyaan yang sah | Sumber yang relevan | Kesalahan yang dihindari |
|---|---|---|---|
| Orientasi PKN | Pendidikan hendak mendampingi apa? | Arsitektur PKN; sumber materi/dalil sesuai klaim | Menjadikan tujuan ruhani sebagai variabel batin terukur |
| Observasi anak | Apa yang terjadi, dalam konteks dan bantuan apa? | Toolkit 19 butir, RPP/observasi, perangkat fase, portofolio | Menyamakan tidak dicatat dengan belum berkembang |
| Praktik pendidik | Kesempatan dan umpan balik apa yang diberikan? | RPP, refleksi pendidik, TALIS sebagai pembanding desain | Menimpakan kegagalan dukungan kepada anak |
| Program/lembaga | Apakah layanan aman, inklusif, dan membaik? | Evaluasi program fase, Sulingjar, pustaka akreditasi | Merata-ratakan “iman anak” untuk menyatakan sekolah bermutu |
| Pelaporan | Bukti terpilih apa yang perlu dibicarakan dan ditindaklanjuti? | Rapor naratif fase, jurnal toolkit | Menyalin jurnal lengkap atau profil sensitif ke keluarga lain |

Hubungan sumber dan indikator dijabarkan pada [peta observasi](02%20-%20Peta%20Sumber%20dan%20Poin%20Observasi.md); hubungan mutu lembaga dibatasi pada [kajian akreditasi](04%20-%20Keselarasan%20Akreditasi%20dan%20Evaluasi%20Program.md).

## 5. Keputusan desain yang diajukan

1. **Satu rapor tidak harus mencakup seluruh konstruk.** Nyatakan kegiatan/periode dan rujukan butir yang relevan; jangan mengisi yang belum diamati untuk melengkapi tampilan.
2. **Pertahankan versi.** Penilaian dari 19 butir toolkit, tabel RPP, rubrik tiga tingkat, dan instrumen fase tidak diagregasikan atau dibandingkan sebagai ukuran setara.
3. **Bukti lebih dulu, bahasa kemudian.** Review catatan dan variasi konteks sebelum menyusun narasi; bukan menulis pujian lalu mencari pembenaran.
4. **Dukungan tetap terlihat.** Bantuan komunikasi, alat, istirahat, pendampingan, dan akses bukan pengurang nilai karakter.
5. **Koreksi dua arah.** Anak/wali boleh berbeda pandangan atau tidak menjawab; perbedaan konteks dicatat, bukan dipaksa menjadi kategori tunggal.
6. **Tidak ada penggunaan nyata otomatis.** Selesaikan gerbang sumber, asesmen, inklusi, perlindungan anak, privasi dan keputusan manusia pada [TODO](05%20-%20Bagan%20dan%20TODO%20Pengembangan.md).

[^riset]: `side-project/rapor-pendidikan-karakter/riset/09-sintesis-dan-keputusan.md`, §1–4 dan §7: sintesis riset dokumenter, konflik dan batas hasil; bukan sumber primer validasi.
[^toolkit]: [Instrumen Observasi Pertumbuhan Karakter 19 Butir](../Toolkit%20KBM/Instrumen%20Observasi%20Pertumbuhan%20Karakter%2019%20Butir.md), §3 (indikator), §5–6 (anekdot/narasi), §7.1–7.4 (jurnal editorial, batas bukti dan berbagi). Bagian 7 sendiri menunggu telaah.
[^fase]: `side-project/parameter-penilaian-fase/README.md`, bagian perangkat tiga tier; `parameter_penilaian_fase.typ`, bagian instrumen per fase. Lihat peta sumber paket untuk perbedaan versi.
[^asesmen]: `side-project/rapor-pendidikan-karakter/riset/02-asesmen-dan-rubrik.md`, §5–6, memetakan konflik jumlah butir, ambang, radar dan TB40; keterlacakan riset tidak mengesahkan konversinya.
[^eksternal]: `data/extracted_elements/external_research/education_questionnaires/usage_notes.csv`, topik `counting`, `language`, `coverage_AN`, `pisa_coverage`, `talis_variants`, `verification`, serta `sulingjar_*`; periksa `sources.csv` untuk provenance setiap berkas. Tidak ada jawaban peserta di inventaris ini.
[^sulingjar]: Kemendikdasmen, [Tentang Survei Lingkungan Belajar (Sulingjar) untuk Kepala Satuan Pendidikan dan Guru](https://pusatinformasi.rumahpendidikan.kemendikdasmen.go.id/hc/id/articles/52442458221721-Tentang-Survei-Lingkungan-Belajar-Sulingjar-untuk-Kepala-Satuan-Pendidikan-dan-Guru), penjelasan tujuan dan hasil satuan pendidikan; bukan bank butir resmi yang berhasil diarsipkan.
[^rapor]: PSKP/Kemendikdasmen, [Rapor Pendidikan Indonesia 2025](https://pskp.kemendikdasmen.go.id/file/kebijakan/1768184990_file.pdf), identitas terbitan dan cakupan tahun; salinan lokal `sources/research_papers/rapor_pendidikan/rapor_pendidikan_indonesia_2025.pdf`, metadata `data/extracted_elements/external_research/education_questionnaires/rapor_publications.csv`. Tidak ada klaim hasil indikator numerik buku yang diturunkan di sini.

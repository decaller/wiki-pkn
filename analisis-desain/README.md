# Analisis Desain Wiki PKN

## Tujuan

Menata ulang susunan konten agar pengguna dapat menemukan, memahami, dan menggunakan materi Pendidikan Karakter Nabawiyah sesuai kebutuhannya.

Titik awal: pemilik proyek melaporkan bahwa susunan konten terasa kurang rapi dan menyulitkan pengguna. Ini merupakan masukan pemilik proyek, bukan hasil pengujian pengguna.

## Lingkup tahap pertama

- Membuat persona awal sebagai dasar pembahasan arsitektur informasi.
- Mengidentifikasi tugas, kebutuhan informasi, hambatan potensial, dan skenario pencarian setiap persona.
- Belum memindahkan artikel, mengganti navigasi, mengubah URL, atau menerbitkan desain baru.

## Struktur Dokumen Analisis dan Desain

Berikut adalah rangkaian dokumen evaluasi arsitektur informasi dan desain konten Wiki PKN:

| Berkas | Judul & Fokus Utama | Status & Output |
|---|---|---|
| [**01 — Audit Struktur Saat Ini**](01-audit-struktur-saat-ini.md) | Inventarisasi 482 berkas korpus fisik dan identifikasi 6 titik friksi navigasi (*deep nesting*, siloing format, beban menu). | Evaluasi Analitis (Faktual) |
| [**02 — Audit Model Diátaxis**](02-audit-model-diataxis.md) | Sensus 4 kuadran Diátaxis, temuan defisit tutorial (< 3%) dan dominasi penjelasan (~48%), serta strategi penyeimbangan. | Analisis Arsitektur Konten |
| [**03 — Usulan Arsitektur Informasi**](03-usulan-arsitektur-informasi.md) | Desain taksonomi ganda (*Dual-Layer IA*) dan 6 pilar navigasi berorientasi tugas (*task-oriented*) dengan prinsip *zero-broken-links*. | Cetak Biru Arsitektur (*Blueprint*) |
| [**04 — Matriks Tugas & Skenario Navigasi**](04-matriks-tugas-dan-skenario-navigasi.md) | Pemetaan matriks 5 persona terhadap 15 skenario tugas riil dan perbandingan jalur klik (*click-path* lama vs. baru). | Spesifikasi UX & Skenario |
| [**05 — Rencana Validasi & Pengujian**](05-rencana-validasi-dan-pengujian.md) | Protokol validasi empiris: Card Sorting 50 kartu, Tree Testing 10 tugas, moderasi ketergunaan (SUS $\ge 80$), dan kriteria kelulusan. | Protokol Pengujian Metodologis |
| [**06 — Strategi Konten Interdisipliner & Rencana Aksi**](06-rencana-aksi-penerapan-persona-interdisipliner.md) | Integrasi 4 disiplin ilmu (Psikologi Kognitif, MarKom, Desain Visual, WCAG 2.1) dan alur kerja 5-fase penerapan 13 persona. | Panduan Operasional & Aksi |
| [**Persona Pengguna**](persona/README.md) | Profil 13 persona terperinci dalam 5 ranah: Orang Tua (Ayah vs Bunda), Guru Fase Usia (Thufulah, Tamyiz, Murahaqah, Baligh, Dewasa), Pengelola Lembaga (Formal vs Non-Formal), Penelaah/Fasilitator, serta Siswa & Pengembangan Diri. | Hipotesis Desain (`[INFERENCE]`) |

## Landasan dan batas bukti

- [Beranda wiki](../content/index.md): menyebut kebutuhan orang tua, pendidik, dan lembaga, serta memuat paradigma, implementasi, dan rujukan.
- [Pedoman arsitektur informasi terdahulu](../pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md): membedakan kebutuhan guru, orang tua, dan peneliti; mengusulkan pembelajaran bertahap, panduan tindakan, rujukan, dan penjelasan mendalam.
- [Konteks proyek](../PROJECT.md): wiki ensiklopedis dengan materi dalil dan referensi kanonikal.
- [Registry sumber](../data/sources_registry.csv): buku, slide, artikel, video, instrumen, serta status sumber yang digantikan.

Dokumen persona adalah **hipotesis desain**, bukan hasil wawancara, analitik, atau observasi perilaku. Tidak ada kutipan pengguna, demografi, maupun angka penggunaan yang direkayasa. Kebutuhan yang disebutkan harus diuji sebelum dijadikan keputusan navigasi final.

## Prinsip pembahasan berikutnya

1. Utamakan tugas pengguna, bukan nama folder internal atau format asal dokumen.
2. Pisahkan kebutuhan belajar awal, tindakan praktis, penjelasan konsep, dan pemeriksaan sumber; gunakan kembali prinsip Diátaxis yang sudah ada.
3. Berikan penjelasan istilah dan jalur bacaan lanjutan tanpa menghilangkan kedalaman dalil.
4. Satu artikel dapat mendukung beberapa persona; hindari menyalin konten ke folder terpisah untuk setiap peran.
5. Validasi melalui pencarian tugas dan pengelompokan kartu sebelum menetapkan susunan menu baru.

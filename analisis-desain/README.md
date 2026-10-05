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
| [**01 — Audit Struktur Saat Ini**](01-audit-struktur-saat-ini.md) | Inventaris dan potensi friksi navigasi; baseline terkini486 Markdown termasuk4 Renungan,482 tanpa Renungan. Tabel lama perlu ledger rekonsiliasi. | Audit Struktur; dampak perilaku belum terukur |
| [**02 — Audit Model Diátaxis**](02-audit-model-diataxis.md) | Klasifikasi empat kuadran pada cakupan482; distribusi lama belum didukung ledger per artikel. | Analisis Konten, bukan sensus tervalidasi |
| [**03 — Usulan Arsitektur Informasi**](03-usulan-arsitektur-informasi.md) | Desain taksonomi ganda (*Dual-Layer IA*) dan 6 pilar navigasi berorientasi tugas (*task-oriented*) dengan prinsip *zero-broken-links*. | Cetak Biru Arsitektur (*Blueprint*) |
| [**04 — Matriks Tugas & Skenario Navigasi**](04-matriks-tugas-dan-skenario-navigasi.md) | Baseline13 persona dan16 skenario; traceability tiap subpersona dan perbandingan klik masih memerlukan verifikasi empiris. | Spesifikasi UX, bukan hasil uji |
| [**05 — Rencana Validasi & Pengujian**](05-rencana-validasi-dan-pengujian.md) | Protokol validasi empiris: Card Sorting 50 kartu, Tree Testing 10 tugas, moderasi ketergunaan (SUS $\ge 80$), dan kriteria kelulusan. | Protokol Pengujian Metodologis |
| [**06 — Strategi Konten Interdisipliner & Rencana Aksi**](06-rencana-aksi-penerapan-persona-interdisipliner.md) | Integrasi 4 disiplin ilmu (Psikologi Kognitif, MarKom, Desain Visual, WCAG 2.1) dan alur kerja 5-fase penerapan 13 persona. | Panduan Operasional & Aksi |
| [**07 — Paket Implementasi Agentic Orchestration**](07-paket-implementasi-agentic-orchestration.md) | Kontrak pilot enam MOC, unit task/ownership, dependency waves, review gates, recipe Orca, verifikasi serta rollout/rollback. | Siap persiapan/pilot terotorisasi; bukan produksi |
| [**08 — Rencana Eksekusi Hibrida Minim Token**](08-rencana-eksekusi-hibrida-minim-token.md) | Penyelamatan 372 ledger & audit navigasi OMP, arsitektur hibrida 4-fase (Zero-Token First), dan penuntasan bundling 7 butir tugas TODO. | Rencana Eksekusi Resmi & Bundling TODO |
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

## Tahap persiapan dan pilot

[Paket07](07-paket-implementasi-agentic-orchestration.md) menyintesis audit desain dan teknis pada run `run_f8befa457d4e`. Tahap ini hanya dokumentasi persiapan, belum perubahan situs/korpus/config/kode atau persetujuan deploy.

1. Rekonsiliasi baseline486 Markdown termasuk4 Renungan versus482 tanpa Renungan; petakan13 persona dan16 skenario ke tugas, target kanonik, sumber, accepted destinations dan gap.
2. Tinjau keselamatan/manhaj/otoritas sumber, terutama usia/taklif, perlindungan anak, trauma dan batas klinis. Label usia tetap korpus sampai reviewer menyetujui.
3. Tetapkan manifest satu collection enam MOC `content/Panduan/`, tanpa memindahkan artikel. Metadata baru hanya bila ada consumer nyata; fitur filterTB40/dalil/Sirah/asesmen/ekspor/feedback tetap contract-gated.
4. Setelah izin pilot, fan-out content/UI/generator/CSS/audit dengan kepemilikan eksklusif; coordinator satu owner shared config/nav. Verifikasi dan smoke aktual dilakukan setelah integrasi, bukan selama penyusunan paket.
5. Produksi menunggu card sorting, tree testing, usability/a11y, gerbang keselamatan dan persetujuan rollout/rollback. Angka target pada05 masih provisional; tidak ada klaim UX/test/WCAG lulus.

Smoke baseline yang dilaporkan coordinator: `python3 scripts/wiki_corpus_linter.py --check-links` exit0, Broken wikilink targets0 dan True orphan pages0. Hasil ini bukan bukti build, URL render, aksesibilitas, atau keberhasilan pengguna; penyusunan paket tidak menjalankan ulang lint/build/test/formatter.

### Integrasi pipeline musyawarah

[Paket07, bagian6.1](07-paket-implementasi-agentic-orchestration.md) menambahkan traceability Pipeline11/12, brief M0–M3, state/gates, ownership, dependency DAG dan smoke CLI aman. Sumber nyata: [master pipeline §5](../pipeline_designs/README.md), [arsitektur Dewan Syura](../pipeline_designs/12_dewan_syura_llm_council_architecture.md), dan [engine council](../scripts/llm_council.py).

Engine saat ini memiliki CLI tiga tahap **simulasi offline**; respons/review/verdict berupa template, context belum dipakai untuk sintesis dan live mode masih placeholder. Tidak ada bukti wiring otomatis scorer/council/Quartz atau human approval; skor70, style85%, latency200ms, lima lensa dan shape tests tidak membuktikan keputusan manhaj atau konsensus semantik. Integrasi pilot memakai risalah advisory terlabel dan signoff manusia nyata; adapter/live tetap contract-gated, tidak otomatis publish.

Riset tambahan hanya membaca sumber dan memperbarui07/README. Smoke council yang diusulkan memakai `python3 scripts/llm_council.py --help` dan `--offline`, output stdout atau direktori sementara terisolasi, bukan `content/`; belum dijalankan pada tahap ini. `pipeline_runner_dalil.py` tidak dijadikan smoke karena menulis korpus langsung.

### Transisi Eksekusi Hibrida Minim Token (Dokumen 08)

Upaya orkestrasi serial berbasis agen LLM monolitik pada run `run_0f3cfd37f363` dievaluasi mengalami kebuntuan (*hang*) akibat ledakan konteks (naskah ledger membengkak hingga 91.000 baris / 3.3 MB), model subagent fiktif pada konfigurasi OMP, dan *rate limiting* upstream API (429/503). 

[Dokumen 08](08-rencana-eksekusi-hibrida-minim-token.md) menetapkan arah eksekusi resmi:
1. **Penyelamatan Aset:** Memanfaatkan 372 ledger artikel yang sudah tervalidasi di `/tmp/wiki-pkn-omp-content.json` dan rancangan arsitektur navigasi 100% tuntas di `/tmp/wiki-pkn-omp-nav.md`.
2. **Pola Hibrida Zero-Token:** Audit 115 berkas sisa diselesaikan melalui skrip parser Python deterministik (<2 detik, 0 token) tanpa membebani LLM.
3. **Penerbitan 6 MOC Task-Oriented:** Membangun Presentation Layer di `content/Panduan/` (*Mulai di Sini, Fase Usia, Fitrah & Bakat, Praktik Keluarga, Lembaga & Guru, Dalil & Rujukan*) berbasis 4 kuadran Diátaxis dan 13 persona.
4. **Multi-Task Bundling:** Mengintegrasikan penuntasan 7 butir pekerjaan di `TODO.md` (TODO 66, 67, 68, 139/431, 402, 120, 86, 65) dalam satu siklus implementasi yang rapi dan terukur.

**Status Kemajuan:**
* **Fase 1 (Selesai):** Master Ledger [`data/wiki-pkn-full-ledger.json`](../data/wiki-pkn-full-ledger.json) (487 berkas, 100% tuntas, rata-rata skor kualitas 86.01, waktu proses 1.15 detik, 0 token API) berhasil diterbitkan.
* **Fase 2 (Sedang Berjalan):** Penerbitan 6 berkas MOC di `content/Panduan/`.



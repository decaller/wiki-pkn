# Roadmap & TODO List Wiki-PKN (Pendidikan Karakter Nabawiyah)

Dokumen ini melacak daftar rencana pengembangan aktif Wiki PKN yang disusun secara metodologis mengikuti urutan tahapan dokumen **[Analisis Desain](analisis-desain/README.md)** (dari fondasi keamanan & kepatuhan persona, arsitektur informasi & navigasi kanonikal, standarisasi kognitif & Diátaxis, perangkat kerja operasional 13 persona, studi kasus lembaga, rilis domain produksi, hingga orkestrasi pipeline AI & GraphRAG).

Setiap butir rencana dilengkapi dengan **estimasi penggunaan token AI** serta **tingkat kebutuhan tinjauan manusia (HITL - Human-in-the-Loop)**.

> [!TIP]
> Seluruh tugas yang telah tuntas diselesaikan (112 butir pencapaian, termasuk Milestone 1–64, pembersihan tautan kanonik, harmonisasi manhaj tadarruj, dan integrasi analitik) telah diarsipkan secara terpisah di **[TODO-COMPLETED.md](TODO-COMPLETED.md)**.

---

## Ringkasan Status & Metrik Estimasi

- **Status Umum:** Dalam Pengembangan Aktif (66 Tugas Terbuka Terjadwal).
- **Kerangka Urutan:** Selaras 100% dengan dokumen bertahap di `analisis-desain/` (Fase 1 s/d Fase 7).
- **Audit Pembelajaran 13 Persona (3 Oktober 2026):** Terintegrasi penuh pada Fase 1 (P0: rekonsiliasi kuesioner TB40 & guardrails klinis/KDRT), Fase 2 (P1: tautan internal 8 Standar & canvas), Fase 3 (P1: konsistensi istilah adab vs bakat), Fase 4 (P2: toolkits 13 persona), dan Fase 7 (P2: otomasi runner audit persona).
- **Pedoman Tingkat HITL (Human-in-the-Loop):**
  - `Rendah`: Verifikasi visual layout, pengujian fungsional/otomatis, atau review teknis sederhana.
  - `Sedang`: Pengecekan keterbacaan, validasi format operasional KBM, atau review bahasa oleh tim editor/guru.
  - `Tinggi`: Verifikasi keselarasan konsep filosofis, keabsahan dalil/takhrij, atau otorisasi materi oleh kurator/ustadz.
  - `Sangat Tinggi`: Tahqiq sanad, otentisitas syarah ulama, atau keputusan hukum/fatwa syar'i sensitif.

---

## Fase 1: Keamanan Sistem, Integritas Data & Safety Guardrails (P0 & Audit Keamanan)
*Rujukan Dokumen Analisis: Dokumen [05 — Rencana Validasi & Pengujian](analisis-desain/05-rencana-validasi-dan-pengujian.md), [Temuan Kritis Audit Persona 3 Okt 2026](analisis-desain/audit-persona/run-2026-10-03/HASIL-GABUNGAN.md), dan Temuan Audit Repositori P0.*

Fokus pada mitigasi risiko keselamatan anak/keluarga, koreksi matriks asesmen bakat TB-40 agar tidak menyesatkan pengguna, pengamanan kredensial, dan isolasi jaringan layanan backend.

- [x] **P0 — Rekonsiliasi & Koreksi Total Matriks Kuesioner Asesmen TB-40.** `[SELESAI]`
  - *Status Kemajuan:* Selesai penuh (4 Oktober 2026):
    1. Seluruh 40 nomor butir pernyataan pada Section 3 [`Kuisioner Asesmen 40 Bakat Nabawiyah.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Bakat/Kuisioner%20Asesmen%2040%20Bakat%20Nabawiyah.md) telah direkonsiliasi penuh 1:1 ke 6 Rumpun Bakat mengacu pada 40 berkas kanonikal di folder `TB40/`. Butir 29 (Rahmah) dan Butir 35 (Syajaa'ah) serta Butir 22 (Munaafasah) dan Butir 19 (Juud) kini terpetakan dengan tepat.
    2. Menghilangkan seluruh nama bakat usang/non-standar (*Hirmaan, Ziyaadah, Hamaasah, dll.*) dari tabel penilaian.
    3. Menyelaraskan penjelasan formula seleksi *Top 6 Kekuatan Utama* (formula baku aplikasi) dan *Top 5 Fokus Pendampingan Keluarga*.
    4. Mengintegrasikan automated regression test di [`tests/test_tb40_questionnaire_matrix.py`](tests/test_tb40_questionnaire_matrix.py) (4 tests lulus).
  - *Kebutuhan HITL:* Selesai.


- [x] **P0 — Penguatan Safety Guardrails, Batasan Etis/Klinis & Pengecualian Bahaya Fisik/KDRT pada Panduan Pemulihan (Recovery) & Keluarga.** `[SELESAI]`
  - *Status Kemajuan:* Selesai penuh (4 Oktober 2026):
    1. Menyisipkan kotak peringatan *Safety Guardrail & Demarkasi Klinis* pada [`Recovery.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Pendidikan%20Ideal/Luka%20dan%20Hutang%20Pengasuhan/Recovery.md): menegaskan batas wilayah edukasi fitrah/tazkiyah vs psikoterapi klinis, serta mencantumkan hotline darurat nasional (Kemenkes 119 ext 8, SAPA 129 KemenPPPA, dan PUSPAGA).
    2. Menambahkan klausul *Pengecualian Mutlak Kedaruratan KDRT & Bahaya Fisik* pada [`Peran Ayah dan Bunda.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Peran%20&%20Tanggung%20Jawab/Peran%20Ayah%20dan%20Bunda.md): menegaskan bahwa kaidah "satu suara di depan anak" gugur demi hukum/syariat bila terjadi KDRT atau ancaman keselamatan fisik.
    3. Menambahkan klausul pengecualian keselamatan langsung pada tips jeda teguran 24 jam di `Recovery.md`.
    4. Menyelaraskan redaksi penjelasan amigdala sebagai metafora neuro-edukatif.
  - *Kebutuhan HITL:* Selesai.


- [x] **P0 — Rotasi dan keluarkan kredensial Umami dari Git.** `[SELESAI]`
  - *Status Kemajuan:* Selesai penuh (4 Oktober 2026):
    1. Seluruh nilai kredensial sensitif (`POSTGRES_PASSWORD`, `DATABASE_URL`, dan `APP_SECRET`) pada [`docker-compose.umami.yml`](docker-compose.umami.yml) telah ditarik dan diganti dengan interpolasi variabel lingkungan yang wajib didefinisikan (`${UMAMI_DB_PASSWORD:?...}`, `${UMAMI_APP_SECRET:?...}`).
    2. Port exposure Umami diikat ke loopback lokal `127.0.0.1:${UMAMI_PORT:-3008}:3000`.
    3. Template berkas aman dan panduan rahasia telah dikonsolidasikan pada [`.env.example`](.env.example). Berkas `.env` telah di-untrack dan dilindungi oleh `.gitignore` dan `.dockerignore`.
  - *Kebutuhan HITL:* Selesai untuk kode repositori; rotasi nilai di VPS produksi dapat disinkronkan saat deployment.


- [ ] **P0 — Rotasi webhook Portainer yang pernah tertulis di dokumentasi.** Token telah diredaksi dari `docs/CI_CD_DEPLOYMENT_GUIDE.md` dan `docs/HANDOVER.md`, tetapi riwayat Git dan salinan lama masih dapat memuatnya. Cabut token lama di Portainer, simpan URL baru hanya di secret GitHub, audit riwayat dan koordinasikan pembersihan tanpa mencetak nilainya; uji trigger serta pastikan image baru benar-benar berjalan. *HITL:* Tinggi (akses dan koordinasi produksi).


- [x] **P0 — Batasi akses Qdrant riset.** `[SELESAI]`
  - *Status Kemajuan:* Selesai penuh (4 Oktober 2026): Port HTTP (6333) dan gRPC (6334) pada [`docker-compose.qdrant-research.yml`](docker-compose.qdrant-research.yml) telah diikat secara eksplisit ke antarmuka loopback `127.0.0.1` (`127.0.0.1:${QDRANT_RESEARCH_HTTP_PORT:-6335}:6333` dan `127.0.0.1:${QDRANT_RESEARCH_GRPC_PORT:-6336}:6334`), mencegah akses publik tanpa autentikasi.
  - *Kebutuhan HITL:* Selesai.


- [x] **P0 — Batasi akses Unstructured API.** `[SELESAI]`
  - *Status Kemajuan:* Selesai penuh (4 Oktober 2026): Port parser (8000) pada [`docker-compose.unstructured.yml`](docker-compose.unstructured.yml) telah diikat ke loopback `127.0.0.1:${UNSTRUCTURED_HOST_PORT:-8005}:8000`, mengisolasi layanan ekstraksi dari jaringan publik.
  - *Kebutuhan HITL:* Selesai.


---

## Fase 2: Arsitektur Informasi, Navigasi Kanonikal & Integritas Tautan (P1 & Dokumen 01/03/08)
*Rujukan Dokumen Analisis: Dokumen [01 — Audit Struktur Saat Ini](analisis-desain/01-audit-struktur-saat-ini.md), [03 — Usulan Arsitektur Informasi](analisis-desain/03-usulan-arsitektur-informasi.md), [08 — Rencana Eksekusi Hibrida Minim Token](analisis-desain/08-rencana-eksekusi-hibrida-minim-token.md), dan Temuan Audit Persona P1.*

Fokus pada penegakan Dual-Layer IA, zero-broken-links, koreksi tautan internal 8 Standar, konsistensi canonical beranda dengan sitemap, pruning konten, dan hardening pipeline CI/CD.

- [x] **P1 — Audit & Koreksi Target Tautan Internal (Menu 8 Standar & Tautan Canvas).** `[SELESAI]`
  - *Status Kemajuan:* Selesai penuh (4 Oktober 2026):
    1. Memperbaiki algoritma resolusi tautan pada plugin navigasi [`plugins/outline-nav/src/components/OutlineNav.tsx`](plugins/outline-nav/src/components/OutlineNav.tsx): mengubah urutan pencocokan agar exact title, slug matches, dan filename matches diprioritaskan sebelum heuristik penomoran TB-40. Menambahkan validasi keyword pada deteksi TB-40 sehingga judul seperti "8 Standar Implementasi PKN" tidak lagi salah dipetakan ke berkas bakat `08-nubl`.
    2. Menambahkan alias kanonikal (`8 Standar Implementasi PKN`, `8 Standar Mutu PKN`, `8-standar-implementasi-pkn`) pada [`8 Standar Implementasi PKN.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Kaidah%20&%20Elemen/8%20Standar%20Implementasi%20PKN.md).
    3. Membangun ulang bundle plugin (`npm run build` pada `plugins/outline-nav/`) dan memverifikasi integritas tautan via `wiki_corpus_linter.py --check-links` (0 broken internal links, 0 true orphans).
  - *Kebutuhan HITL:* Selesai.


- [x] **P1 — Cocokkan canonical beranda dengan sitemap dan rute publik.** `[SELESAI]`
  - *Status Kemajuan:* Selesai penuh (4 Oktober 2026):
    1. Memperbaiki pembuatan tag canonical dan open graph pada [`quartz/components/Head.tsx`](quartz/components/Head.tsx) menggunakan fungsi `simplifySlug(fileData.slug!)`.
    2. Menghilangkan anomali canonical `/index` pada halaman utama dan folder index: `public/index.html` kini mengeluarkan canonical kanonik `https://wikipkn.insanmustaqbal.or.id/`, 100% selaras dengan entri sitemap generator (`<loc>https://wikipkn.insanmustaqbal.or.id/</loc>`).
    3. Folder index kini mengeluarkan canonical direktori trailing-slash (misal `/referensi/tokoh--and--pemikiran/`), mengeliminasi redudansi pengindeksan crawler.
    4. Mengintegrasikan automated regression test di [`tests/test_canonical_and_sitemap.py`](tests/test_canonical_and_sitemap.py) (3 tests lulus).
  - *Kebutuhan HITL:* Selesai.


- [ ] **Evaluasi Penempatan, Relokasi & Eliminasi Konten Berbasis User Journey (Placement & Pruning Engine)**
  - *Deskripsi:* Menerapkan filter arsitektur informasi pada pipeline LangGraph (lihat [`pipeline_designs/CONTENT_PLACEMENT_AND_NAVIGATION_RULES.md`](pipeline_designs/CONTENT_PLACEMENT_AND_NAVIGATION_RULES.md)) untuk mengevaluasi kecocokan penempatan materi. Mencegah *cognitive overload* dan salah sasaran audiens dengan memindahkan konten teknis/mikro (seperti tips harian, formulir/rubrik asesmen, dan studi kasus spesifik) dari gerbang makro (Home/Beranda) ke hub yang tepat (`content/Templates/`, `content/Tips/`, atau sub-halaman operasional), serta mengeliminasi konten redundan/basa-basi.
  - *Status Kemajuan:*


    - [ ] Integrasi otomatis validator penempatan konten pada skrip linter dan LangGraph runner
  - *Perkiraan Token AI:* ~150k - 300k token (penyusunan audit rules, evaluasi penempatan, dan migrasi terarah).
  - *Kebutuhan HITL:* Sedang (penyelarasan arsitektur navigasi dan pengalaman membaca).


- [ ] **Pemeliharaan berulang — Perbarui indeks lengkap sebelum setiap commit dan secara berkala.** Jalankan `python3 scripts/update_content_index.py` sebelum setiap commit; jalankan juga setelah menambah, memindahkan, mengganti nama, atau menghapus berkas di `content/`, serta dalam pemeriksaan mingguan. Periksa perubahan `content/Peta Navigasi Wiki PKN.md` dan sertakan pembaruannya dalam commit yang relevan. Setelah perubahan konten, jalankan `python3 scripts/wiki_corpus_linter.py --check-links`; sebelum rilis, build Quartz dan periksa tautan indeks hasil build. Script belum dijadwalkan otomatis dan belum menjadi hook pre-commit; kewajiban ini masih manual. *HITL:* Rendah. *Status:* Tugas berulang, jangan ditutup hanya karena satu kali dijalankan.


- [ ] **P1 — Pulihkan verifikasi TLS webhook Portainer.** Workflow tidak lagi memakai `curl -k` dan gagal jika webhook tidak tersedia/HTTP gagal; sertifikat/CA dan secret di lingkungan produksi belum diuji. *HITL:* Sedang (akses deployment).


- [ ] **P1 — Tegakkan build/deploy yang reproduktif.** `npm ci` menggantikan fallback install; Actions dipin ke SHA dan image memiliki tag `sha-<commit-pendek>`. Stack masih memakai `latest`, sehingga pin commit/digest, uji rollback dan konsistensi Portainer tetap terbuka. *HITL:* Sedang.


- [ ] **P1 — Jadikan kegagalan redeploy terlihat.** Workflow kini gagal bila webhook gagal dan memeriksa `/build-version.txt` sampai commit baru tersaji; uji dengan CI/Portainer dan cek status image/health container nyata masih terbuka. *HITL:* Sedang (akses produksi).


---

## Fase 3: Standarisasi Kognitif, Model Diátaxis, Terminologi & Editorial (P1 & Dokumen 02/06)
*Rujukan Dokumen Analisis: Dokumen [02 — Audit Model Diátaxis](analisis-desain/02-audit-model-diataxis.md), [06 — Strategi Interdisipliner & Rencana Aksi](analisis-desain/06-rencana-aksi-penerapan-persona-interdisipliner.md), dan Temuan Audit Persona P1.*

Fokus pada penertiban konsistensi istilah (nilai adab vs katalog TB-40, rentang usia Murahaqah, klausul pendewasaan), penulisan kepadatan tinggi (*high-density*), standarisasi taksonomi & takhrij dalil, serta tipografi teks Arab.

- [x] **P1 — Penertiban Konsistensi Istilah TB-40, Rentang Usia Murahaqah, dan Klausul Pendewasaan.** `[SELESAI]`
  - *Status Kemajuan:* Selesai penuh (4 Oktober 2026):
    1. Memberi distingsi tegas pada format dan contoh KBM di [`Template RPP Karakter Nabawiyah 1 Lembar.md`](content/Toolkit%20KBM/Template%20RPP%20Karakter%20Nabawiyah%201%20Lembar.md): memisahkan kolom *Nilai Adab & Karakter Umum* (misal: *Syukur*, *Khidmah*) dari *Pilar Bakat Fitrah TB-40 Spesifik* (misal: *Ihsaan #02*, *Anaah #38*, *Itsaar #34*).
    2. Menambahkan *Catatan Terminologi Rentang Usia Murahaqah* pada [`Murahaqah.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Perkembangan/Murahaqah.md) yang mengintegrasikan penjelasan 10–14 tahun (fase transisi biologis pubertas di SMP), 10–15 tahun (batas maksimal usia baligh syar'i), dan 10–Baligh (jembatan pembinaan menuju mukallaf).
    3. Menyelaraskan penomoran klausul pendewasaan pada Section 5 `Murahaqah.md` dari "Klausul 11" menjadi **Klausul 10**, seragam dengan piagam mutu [`8 Standar Implementasi PKN.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Kaidah%20&%20Elemen/8%20Standar%20Implementasi%20PKN.md) dan bab [`Syabab.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Perkembangan/Syabab.md).
  - *Kebutuhan HITL:* Selesai.


- [ ] **Penerapan Mekanisme Penulisan Kepadatan Tinggi & Pembatasan Negatif (*High-Density Prompt Engineering*)**
  - *Deskripsi:* Mencegah naskah wiki terdilusi menjadi rangkuman dangkal atau kehilangan *edge cases* syar'i/teknis akibat basa-basi AI (*LLM tells*), melalui 5 aturan mekanik penulisan:
    1. **Negative Style Constraints:** Larangan mutlak pengumuman meta (*"Dalam bab ini kita akan..."*), eliminasi kata klise/sycophantic (*krusial, vital, seamless, pilar penting yang tak tergantikan*), larangan judul kesimpulan berlabel (*"Kesimpulan/Rangkuman"*), dan penegakan kalimat aktif.
    2. **Pola Scratchpad-Then-Synthesize (`<phase_1_fact_extraction>` $\to$ `<phase_2_wiki_draft>`):** Memaksa model mengekstrak seluruh parameter dalil, batasan usia, dan patologi parenting secara atomik sebelum mulai merangkai naskah artikel, lalu memverifikasi kembali bahwa tidak ada detail yang hilang saat sintesis.
    3. **Enforce High-Density Formats:** Mengganti narasi panjang bersyarat dengan *Condition $\to$ Root Cause $\to$ Exact Remediation Matrix*; menegakkan *Specification Box Rule* (paragraf dengan $\ge 3$ parameter wajib dirender sebagai tabel kunci-nilai atau callout card).
    4. **Multi-Pass "Editor" Chaining (Two-Agent Pipeline):** Memisahkan drafter dan copy-editor dengan checklist retensi fakta/dalil. Hapus repetisi sesuai kebutuhan, bukan kuota pemotongan 25%; panduan kanonis berada di `PANDUAN_PENULISAN_KONTEN.md`.
    5. **Kalibrasi Parameter Inferensi Model:** Menyetel $T \in [0.0, 0.2]$ dan $\text{Top-P} = 0.9$ untuk presisi terminologi syar'i dan mitigasi halusinasi.
  - *Perkiraan Token AI:* ~120k - 250k token (penyusunan prompt template system, testing perbandingan few-shot negatif-positif, dan validasi output).
  - *Kebutuhan HITL:* Rendah - Sedang (evaluasi kepadatan informasi dan eliminasi kalimat bertele-tele pada draf uji coba).
  - *Status implementasi:* Pilot copy-edit `Bank Studi Kasus.md` dan `Pembelajaran Alamiah.md` selesai: lead, repetisi, transisi, dan label ilustrasi diperjelas; kutipan, rujukan, konsep, dan embed dipertahankan. Evaluasi manusia belum selesai. Materi klinis, hukuman fisik, dan syariah lama tidak disahkan oleh perubahan editorial ini.


- [ ] **Ensiklopedia Karakter Pokok & Karakter Turunan**
  - *Deskripsi:* Direktori karakter (*Shidq*, *Amanah*, *Iffah*, *Syaja'ah*, dll.) lengkap dengan dalil, indikator perilaku nyata, dan antitesisnya.
  - *Perkiraan Token AI:* ~1.5M - 2.5M token (penyusunan puluhan entri karakter: takrif, dalil, indikator empiris, dan antitesis).
  - *Kebutuhan HITL:* Tinggi (verifikasi ketepatan klasifikasi karakter dan dalil pendukung).


- [ ] **Pedoman Kontributor (Style Guide Penulisan Wiki)**
  - *Deskripsi:* Standarisasi format penulisan, sitasi dalil, dan struktur markdown bagi asatidzah/guru yang menyumbang materi.
  - *Perkiraan Token AI:* ~80k - 150k token (penulisan dokumen SOP standarisasi markdown, takhrij, dan etika kutipan).
  - *Kebutuhan HITL:* Sedang (persetujuan tim redaksi wiki).
  - *Status implementasi:* Panduan root menjadi kanonis; `pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md` menjadi referensi pendamping. Struktur artikel/MOC/formulir, atribusi, retensi fakta, dan gerbang HITL telah diselaraskan. Review privat: `private/hitl/editorial-batch-2026-10-04/panduan/`; `PREFLIGHT_FAILED` (64,8), tanpa keputusan manusia. Scorer menandai istilah dalam negasi serta struktur Markdown sebagai kalimat panjang; keterbatasan ini bukan alasan mengubah fakta atau menambah pengisi. Persetujuan redaksi tetap tertunda.


- [ ] **Taksonomi & Filter Tag Khusus Dalil**
  - *Deskripsi:* Pencarian dan pemfilteran dalil berdasarkan surah, topik adab, kualitas/sanad hadits, atau kata kunci tematik.
  - *Perkiraan Token AI:* ~300k - 600k token (auto-tagging dalil berdasarkan kategori surah, tema karakter, dan perawi).
  - *Kebutuhan HITL:* Sedang - Tinggi (review akurasi label kategorisasi syar'i).


- [ ] **Skrip Validasi Takhrij & Nomor Dalil Otomatis**
  - *Deskripsi:* Pengecekan otomatis (CI/hook) untuk validasi format nomor surah:ayat dan periwayat hadits saat artikel baru ditambahkan.
  - *Perkiraan Token AI:* ~80k - 150k token (penulisan regex validator, integrasi database surah/hadits, dan setup GitHub Action).
  - *Kebutuhan HITL:* Rendah (pengecekan false positives pada penulisan nama surah dan nomor ayat).


- [ ] **Optimasi Tipografi Teks Arab & Terjemahan**
  - *Deskripsi:* Penerapan font naskh khusus web (Amiri / Scheherazade New) dan layout dwibahasa yang nyaman dibaca di layar mobile.
  - *Perkiraan Token AI:* ~20k - 40k token (tuning CSS webfont, penyesuaian font-size, line-height, dan layout terjemahan).
  - *Kebutuhan HITL:* Sedang (uji kenyamanan membaca teks Arab berharakat oleh asatidzah).


- [ ] **P2 — Audit render Arab dan keluaran situs.** Enam kutipan Arab telah dipindah dari KaTeX ke blok Arab; build lokal 486 berkas selesai tanpa peringatan KaTeX dan sampel DOM mempertahankan harakat. Verifikasi visual/PDF artikel penuh pasca-perubahan, pemeriksaan otomatis canonical/sitemap seluruh situs, dan telaah editorial Arab belum selesai. *HITL:* Sedang.


---

## Fase 4: Perangkat Kerja Operasional 13 Persona & KBM Praktis (P2 & Dokumen 04/Persona)
*Rujukan Dokumen Analisis: Dokumen [04 — Matriks Tugas & Skenario Navigasi](analisis-desain/04-matriks-tugas-dan-skenario-navigasi.md), [Persona Pengguna 13 Ranah](analisis-desain/persona/README.md), dan Temuan Audit Persona P2.*

Fokus pada penyediaan task-based toolkits untuk 13 persona (Ayah, Bunda, Guru Thufulah–Syabab, Lembaga Formal–Nonformal, Penelaah, Pelajar), instrumen asesmen kualitatif tanpa angka, SOP penanganan kasus khusus, serta sinkronisasi rumah-sekolah.

- [ ] **P2 — Pengembangan Alat Kerja Praktis Berorientasi Tugas (Task-Based Toolkits) untuk 13 Persona.**
  - *Akar Masalah:* Artikel wiki sangat kaya materi naratif dan dalil, namun persona praktisi (orang tua sibuk, guru baru, pimpinan lembaga) memerlukan instrumen operasional siap pakai dalam hitungan menit.
  - *Rencana Aksi Berdasarkan Temuan 13 Persona:*
    1. *Persona 01a (Ayah):* Lembar instan *"Kartu Aksi 3 Menit Ayah"* (panduan dialog hati sepulang kerja, pembagian peran qawwamah, dan tips mendengarkan anak).
    2. *Persona 01b (Bunda):* Panduan respons instan pasca-emosi (protokol meminta maaf dan memulihkan batin anak tanpa rasa bersalah berlarut).
    3. *Persona 02a (Guru Thufulah):* Bank ide kegiatan main fitrah berbasis alam dan lembar observasi anak usia 2–6 tahun.
    4. *Persona 02b (Guru Tamyiz):* Contoh RPP tematik terisi lintas mata pelajaran (Matematika, Bahasa, Sosial) dengan integrasi nalar fitrah.
    5. *Persona 02c (Guru Murahaqah):* SOP Pencegahan & Penanganan Kasus Perundungan (Bullying) santri dan panduan adab pergaulan islami.
    6. *Persona 02d (Guru Syabab):* Panduan perancangan proyek magang kemandirian santri dan regulasi perlindungan kerja remaja.
    7. *Persona 02e (Pembimbing Dewasa) & 07 (Pembelajar Mandiri):* Panduan muhasabah mandiri dan rubrik refleksi diri dewasa.
    8. *Persona 03a (Lembaga Formal) & 03b (Lembaga Nonformal):* Matriks keselarasan kurikulum nasional/akreditasi vs 8 Standar PKN, kalender program tahunan ringan, dan draf MoU kemitraan orang tua.
    9. *Persona 04 (Fasilitator/Pengkaji) & 06 (Pelajar):* Jalur belajar bertingkat dengan estimasi waktu baca (15 menit, 1 jam, 1 hari) serta panduan pemetaan bakat penjurusan tanpa labelling kaku.
  - *Target Berkas:* [`content/Toolkit KBM/`](content/Toolkit%20KBM/), [`content/Panduan/`](content/Panduan/).
  - *Prioritas:* P2 (Sedang — Peningkatan Utilitas Lapangan)
  - *Perkiraan Token AI:* ~80k - 160k token.
  - *Kebutuhan HITL:* Sedang - Tinggi (peninjauan kelayakan operasional oleh guru dan praktisi lembaga).


- [ ] **Rubrik & Format Observasi Karakter Tanpa Angka**
  - *Deskripsi:* Evaluasi karakter berbasis narasi perkembangan dan pengamatan perilaku nyata, bukan sekadar skor angka ujian.
  - *Perkiraan Token AI:* ~450k - 800k token (perumusan indikator perilaku deskriptif & rubrik asesmen naratif).
  - *Kebutuhan HITL:* Tinggi (validasi konstruk instrumen penilaian karakter oleh pakar evaluasi pendidikan).


- [ ] **Panduan Penanganan Kasus Khusus (Adiksi Gadget, Bullying, Tantrum)**
  - *Deskripsi:* SOP islami dan pendekatan nabawi dalam menangani pelanggaran adab atau trauma psikologis anak di lingkungan sekolah.
  - *Perkiraan Token AI:* ~400k - 750k token (penyusunan SOP integratif syariat-psikologis untuk krisis perilaku).
  - *Kebutuhan HITL:* Sangat Tinggi (review konselor adab anak, psikolog muslim, dan kepala sekolah).


- [ ] **Modul Sinkronisasi Sekolah & Rumah (Parenting Nabawiyah)**
  - *Deskripsi:* Panduan pendampingan orang tua di rumah untuk melanjutkan pembiasaan adab dari sekolah tanpa dikotomi nilai.
  - *Perkiraan Token AI:* ~500k - 900k token (penyusunan silabus pendampingan keluarga dan lembar checklist adab di rumah).
  - *Kebutuhan HITL:* Sedang (masukan praktis dari perwakilan orang tua santri dan guru pembina).
  - *Status implementasi:* Draf modul, persetujuan, privasi, ritme, tindak lanjut, lembar dua arah, dan contoh sintetis tersedia pada bagian 3 `content/Toolkit KBM/Infografis Ringkasan Materi PKN Siap Sebar.md`. Review privat: `private/hitl/editorial-batch-2026-10-04/sekolah-rumah/`, `HUMAN_PENDING`; masukan guru/wali belum tercatat.


- [ ] **Format Jurnal Mutaba'ah Yaumiyah (Buku Amalan Harian Terintegrasi)**
  - *Deskripsi:* Template jurnal harian santri (shalat berjamaah, dzikir, tilawah, adab, birrul walidain) yang terhubung ke indikator PKN.
  - *Perkiraan Token AI:* ~150k - 300k token (penyusunan tabel amalan harian, checklist adab, dan format evaluasi bersama wali murid).
  - *Kebutuhan HITL:* Sedang (penyelarasan target amalan harian dengan budaya sekolah/pesantren).
  - *Status implementasi:* Jurnal harian/pekanan, refleksi, tindak lanjut, contoh sintetis, dan mutabaah opsional privat tersedia pada bagian 7 `content/Toolkit KBM/Instrumen Observasi Pertumbuhan Karakter 19 Butir.md`. Tanpa skor/target normatif atau perubahan 19 indikator dan BT/MT/BK/MM. Review privat: `private/hitl/editorial-batch-2026-10-04/jurnal/`, `HUMAN_PENDING`; penyesuaian budaya sekolah menunggu manusia.


- [ ] **Program "Tantangan Karakter Pekanan" (Weekly Character Campaign)**
  - *Deskripsi:* Panduan program tematik mingguan di sekolah dan rumah (contoh: Pekan Menjaga Lisan, Pekan Kejujuran, Pekan Berbagi).
  - *Perkiraan Token AI:* ~300k - 600k token (pembuatan silabus aktivitas pekanan, panduan guru, dan kriteria evaluasi anak).
  - *Kebutuhan HITL:* Sedang (penyesuaian dengan kalender kegiatan sekolah dan kesiapan wali murid).
  - *Status implementasi:* Draf empat pekan amanah–ta'awun–perbaikan–khidmah, aksi sekolah/rumah, bahan, waktu fleksibel, keamanan, refleksi, dan lembar reusable tersedia pada bagian 5 `content/Toolkit KBM/Formulir Desain Proyek Pembelajaran Alamiah.md`; ditautkan dari portal Toolkit KBM. Review privat: `private/hitl/editorial-batch-2026-10-04/tantangan-pekanan/`, `HUMAN_PENDING`; kalender dan kesiapan wali belum disetujui.
  - *Verifikasi batch editorial:* `python3 scripts/wiki_corpus_linter.py --check-links` lulus (0 target rusak, 0 orphan); `npx quartz build` memproses 493 berkas dan menghasilkan 2.807 keluaran. Preview browser memeriksa portal, lima anchor paket, tiga halaman toolkit, kedua artikel sampel, dan jurnal pada viewport 390 px tanpa overflow halaman. Alias wikilink dalam tabel portal telah di-escape setelah tampilan awal menunjukkan teks mentah. Server preview Python memerlukan akhiran `.html`; ini bukan uji routing produksi. CLI `resume` untuk review pending ditolak; seluruh ledger tetap tanpa keputusan manusia.


- [ ] **Kartu Kasus Lapangan & Diskusi Guru (Teacher Case Study Cards)**
  - *Deskripsi:* Kartu simulasi studi kasus harian untuk bahan *morning briefing* guru dalam menyikapi dinamika adab santri.
  - *Perkiraan Token AI:* ~350k - 700k token (generasi skenario dinamika santri, pertanyaan pemantik, dan panduan respon nabawiyah).
  - *Kebutuhan HITL:* Tinggi (review kesesuaian solusi tindakan disiplin dengan prinsip kasih sayang nabawiyah).


---

## Fase 5: Kajian Komparatif, Studi Kasus Lembaga & Kurasi Konten Inti
*Rujukan Dokumen Analisis: Dokumen [04 — Matriks Tugas](analisis-desain/04-matriks-tugas-dan-skenario-navigasi.md), [05 — Rencana Validasi](analisis-desain/05-rencana-validasi-dan-pengujian.md), dan [06 — Rencana Aksi Konten](analisis-desain/06-rencana-aksi-penerapan-persona-interdisipliner.md).*

Fokus pada kurasi naskah tulisan asatidzah, sinkronisasi Dropbox PDF/rujukan, profil lembaga mitra/penerap PKN, studi kasus lapangan, komparasi epistemologis PKN vs teori pendidikan Barat, serta integrasi multimedia & PDF deep-linking.

- [ ] **Kurasi materi tulisan Ustadz Bayu di grup**
  - *Deskripsi:* Mengumpulkan, menyeleksi, dan menyusun arsip materi yang pernah ditulis Ustadz Bayu di grup diskusi ke format markdown wiki yang terstruktur.
  - *Perkiraan Token AI:* ~1M - 1.8M token (ekstraksi arsip pesan, clustering tema, restrukturisasi paragraf, dan formatting markdown).
  - *Kebutuhan HITL:* Tinggi (verifikasi dan otorisasi konten langsung oleh Ustadz Bayu / murid senior).


- [ ] **Sinkronisasi & Pengambilan Berkas PDF dari Dropbox Menggunakan Rclone**
  - *Deskripsi:* Mengunduh dan menyinkronkan seluruh arsip dokumen PDF dari remote Dropbox yang telah terkonfigurasi (`dropbox:projects/PKN`) menggunakan utilitas CLI `rclone` yang telah terpasang di sistem (`/usr/bin/rclone`). Dokumen PDF yang diunduh difilter secara selektif (modul pelatihan guru, panduan standar implementasi, materi seminar, buku) untuk kemudian dipetakan ke direktori input yang sesuai (`searchable_pdfs/` untuk materi PKN atau `sources/research_papers/` untuk literatur pembanding) sebelum diproses ke pipeline ekstraksi Unstructured.
  - *Alur Kerja & Spesifikasi Operasional:*
    1. **Inspeksi & Inventarisasi Remote:** Menjalankan `rclone lsf --include "*.pdf" --include "*.PDF" -R dropbox:projects/PKN` untuk mendata seluruh PDF di remote dan mencocokkannya dengan katalog [`dropbox_files.md`](dropbox_files.md).
    2. **Sinkronisasi Terarah (*Targeted Sync*):** Mengunduh folder yang dibutuhkan menggunakan `rclone copy --include "*.pdf" --include "*.PDF" --progress dropbox:projects/PKN/<subfolder> <target_dir>/` dengan preservasi struktur direktori asal.
    3. **Penyaringan & Verifikasi Checksum:** Validasi integritas ukuran file dan hash pasca-unduh agar tidak ada file korup sebelum masuk ke pre-flight inspector PyMuPDF.
  - *Perkiraan Token AI:* ~15k - 30k token (pembuatan skrip pembantu automasi sinkronisasi dan pencatatan log katalog).
  - *Kebutuhan HITL:* Rendah (pemilihan sub-folder prioritas yang ingin diunduh dan verifikasi masa aktif token Dropbox).


- [ ] **Profil dan review masing-masing kegiatan**
  - *Deskripsi:* Dokumentasi format kegiatan, profil aktivitas, tujuan karakter, dan evaluasi efektivitasnya di lapangan.
  - *Perkiraan Token AI:* ~400k - 700k token (analisis dokumen kegiatan, pemetaan indikator adab, dan perumusan evaluasi).
  - *Kebutuhan HITL:* Sedang (validasi data riil aktivitas oleh koordinator lapangan/sekolah).


- [ ] **Tabel dan profil lembaga-lembaga**
  - *Deskripsi:* Database lembaga/sekolah/pesantren yang menerapkan atau mengadopsi PKN beserta model implementasinya.
  - *Perkiraan Token AI:* ~300k - 600k token (strukturisasi profil lembaga, ekstraksi data kontak/program, perancangan tabel matriks).
  - *Kebutuhan HITL:* Sedang (konfirmasi keabsahan profil dan izin publikasi dari lembaga bersangkutan).


- [ ] **Contoh implementasi tiap sekolah (Studi Kasus)**
  - *Deskripsi:* Dokumentasi studi kasus dan *best practices* implementasi nyata PKN di masing-masing sekolah/madrasah (adaptasi kurikulum, pembiasaan adab, manajemen kelas, dan tantangan di lapangan).
  - *Perkiraan Token AI:* ~600k - 1.2M token (pengolahan catatan lapangan/wawancara, sintesis kendala praktis, dan perumusan solusi).
  - *Kebutuhan HITL:* Tinggi (validasi keakuratan fakta lapangan bersama kepala sekolah/guru pendamping).


- [ ] **Kumpulan perbandingan dan review berbagai konsep**
  - *Deskripsi:* Matriks perbandingan antara konsep PKN dengan konsep-konsep pendidikan lain (konvensional, montessori, fitrah based education, dll.).
  - *Perkiraan Token AI:* ~500k - 900k token (analisis komparatif filosofis, kelebihan/kekurangan, dan tinjauan syariat).
  - *Kebutuhan HITL:* Tinggi (telaah kritis keselarasan prinsip syar'i oleh dewan pakar pendidikan).


- [ ] **Pencarian Referensi Riset Ilmiah, Jurnal Empiris & Pembahasan Komparasi Teori PKN**
  - *Deskripsi:* Melakukan penelusuran sistematis literatur riset ilmiah, jurnal peer-reviewed, dan data empiris di internet (neurobiologi, ilmu kognitif, psikologi perkembangan anak, sosiologi pendidikan, dan pedagogi) untuk diverifikasi replikabilitasnya, dibersihkan dari distorsi pop-science, lalu dianalisis dan dikomparasikan secara kritis terhadap teori Pendidikan Karakter Nabawiyah (PKN). **Prinsip Utama:** Dalam PKN, bukti empiris hanyalah instrumen pendukung (*wasilah / syawahid kauniyah*), bukan dan tidak bisa menjadi acuan utama (*al-ashl* adalah wahyu Al-Qur'an dan Sunnah). Mengidentifikasi titik temu (*convergence* - mekanisme fisik selaras syariat) dan titik tolak (*divergence* - reduksionisme materialistik, krisis replikasi, relativisme moral) sesuai panduan teknis pada [`pipeline_designs/EVIDENCE_BASED_RESEARCH_WORKFLOW.md`](pipeline_designs/EVIDENCE_BASED_RESEARCH_WORKFLOW.md).
  - *Arsitektur Isolasi Data Terjaga:*
    - **Direktori Input Terpisah:** Kumpulan berkas PDF riset eksternal ditampung khusus di [`sources/research_papers/`](sources/research_papers/) (terpisah dari modul materi internal PKN di `searchable_pdfs/` dan `presentations/`).
    - **Direktori Output Terpisah:** Hasil ekstraksi semantik dan konversi Markdown disimpan secara terisolasi di [`data/extracted_elements/external_research/`](data/extracted_elements/external_research/) (terpisah dari data ekstraksi modul internal di `data/extracted_elements/pkn_internal/`).
    - **Manajemen Siklus Kontainer On-Demand:** Kontainer Unstructured API dijalankan secara bergantian/on-demand untuk batch parsing guna menjaga ketersediaan RAM sistem.
  - *Status Kesiapan Teknis:*


    - [ ] Uji coba ekstraksi pada sampel berkas PDF riset
  - *Alur Analisis & Perangkat Riset:*
    1. **Discovery & Citation Graph Engines:** Penelusuran jejaring sitasi kronologis & konseptual via OpenAlex, Semantic Scholar (NLP intent), Connected Papers/Litmaps (ko-sitasi), dan Consensus.app (consensus meter).
    2. **Verification, Replicability & Retraction Auditing:** Audit replikabilitas dan integritas publikasi via scite.ai (Smart Citations: mentioning, supporting, contrasting), Retraction Watch Database (audit penarikan paper), dan OSF.io (audit pra-registrasi & mitigasi p-hacking).
    3. **Model Context Protocol (MCP) Academic Servers:** Pemanfaatan MCP server untuk AI agent (PubMed/NCBI, Semantic Scholar, Zotero Local, Markdown Scraper) agar kueri literatur bebas halusinasi.
    4. **Systematic Screening & Extraction:** Skrining terstruktur minim bias seleksi menggunakan ASReview (active learning) dan Rayyan (PRISMA double-blind screening).
    5. **Local Synthesis & Matriks Komparasi 6 Dimensi:** Pencatatan atomik Zotero + Obsidian, pemisahan data mekanistik (*wasilah*) vs asumsi filosofis (*ghayah*), serta perakitan tabel matriks komparasi 6 dimensi ([`pipeline_designs/08_pipeline_halaman_komparasi_konsep.md`](pipeline_designs/08_pipeline_halaman_komparasi_konsep.md)).
  - *Perkiraan Token AI:* ~800k - 1.5M token (kueri literatur, ekstraksi metodologi/sampel, audit replikasi, dan sintesis telaah kritis komparatif).
  - *Kebutuhan HITL:* Tinggi (validasi keabsahan telaah kritis syar'i dan keakuratan penafsiran data empiris oleh dewan pakar/asatidzah).


- [ ] **Pembuatan Halaman Khusus Debat & Dialektika Epistemologis: Teori PKN vs Riset & Teori Pendidikan Modern (Pendukung vs Kontradiktif)**
  - *Deskripsi:* Merancang dan menerbitkan halaman ensiklopedis mandiri berstandar 4-Zone MediaWiki sebagai arena debat komparatif dan dialektika epistemologis tingkat tinggi antara Teori PKN dengan berbagai teori pendidikan serta temuan riset empiris modern—baik yang mendukung/sejalan (*points of convergence*) maupun yang bertolak belakang/kontradiktif (*points of divergence*). Menegakkan aksioma bahwa wahyu adalah fondasi mutlak dan bukti empiris adalah penguat deskriptif sunnatullah.
  - *Struktur & Komponen Gelanggang Debat:*
    1. **Gelanggang Konvergensi (Temuan Riset Pendukung):** Dokumentasi riset empiris yang menguatkan sunnatullah manhaj PKN (misal: stimulasi fitrah belajar multisensori, transmisi adab tatap muka langsung vs kemunduran layar digital, ritme tidur sirkadian/gelombang lambat bagi konsolidasi hafalan Al-Qur'an, dan NEAT berkelanjutan vs kesehatan raga).
    2. **Gelanggang Divergensi (Bantahan Epistemologis & Dekonstruksi Riset Kontradiktif):** Pembongkaran asumsi sekuler teori pembanding (Tabula Rasa John Locke vs Fitrah Tauhid, behaviorisme radikal reward/punishment mekanistik vs keikhlasan niat, degradasi krisis replikasi psikologi sosial seperti Ego Depletion & Power Posing, serta demistifikasi neuromitos otak kiri/kanan).
    3. **Gelanggang Dialektika Terbuka (*Unresolved Empirical Frontiers*):** Analisis fenomena empiris kontemporer (anomali cadangan kognitif/Alzheimer, dinamika media digital/hiperrealitas) dengan metodologi *negative capability* dan pemisahan observasi murni dari narasi pop-science.
    4. **Tabel Matriks Komparasi 6 Dimensi:** Hakikat Insan (*Ontologi*), Tujuan Puncak (*Ghayah*), Peran Pendidik (*Murabbi*), Pendekatan Disiplin (*Adab & 'Uqubah*), Orientasi Hasil (*Najaah*), dan Keterikatan dengan Akhirat & Ridha Allah.
  - *Perkiraan Token AI:* ~600k - 1.2M token (perumusan dialektika, penataan tabel komparatif 6 dimensi, ekstraksi dalil dan syarah pembanding, serta perakitan draf artikel 4-Zone).
  - *Kebutuhan HITL:* Sangat Tinggi (otorisasi dan verifikasi argumen syar'i oleh kurator utama/Dewan Pakar Pendidikan Islam).


- [ ] **Direktori Narasumber & Trainer PKN**
  - *Deskripsi:* Daftar kontak atau lembaga penyedia workshop, sertifikasi, dan pelatihan implementasi PKN untuk sekolah.
  - *Perkiraan Token AI:* ~50k - 100k token (strukturisasi profil narasumber, bidang kepakaran, dan format kontak).
  - *Kebutuhan HITL:* Tinggi (verifikasi data kontak dan izin pencantuman dari narasumber terkait).


- [ ] **Audio Player Kajian Tersemat (Embedded Audio)**
  - *Deskripsi:* Pemutar audio ringkas pada halaman materi agar pembaca bisa mendengarkan rekaman kajian Ustadz Bayu / narasumber sembari membaca transkrip.
  - *Perkiraan Token AI:* ~25k - 50k token (komponen audio player Quartz, linking file audio, dan sinkronisasi bab).
  - *Kebutuhan HITL:* Rendah (pengujian pemutaran audio di perangkat desktop dan mobile).


- [ ] **PDF Deep-Linking (Tautan Langsung ke Halaman Dokumen/Kitab)**
  - *Deskripsi:* Integrasi pipeline OCR `searchable_pdfs` agar kutipan langsung membuka halaman buku atau kitab rujukan asli.
  - *Perkiraan Token AI:* ~200k - 400k token (pemetaan sitasi teks ke koordinat/nomor halaman berkas PDF).
  - *Kebutuhan HITL:* Sedang (uji coba presisi deep link pada sampel kutipan buku).


---

## Fase 6: Infrastruktur Platform, Web Editor & Transisi Domain Resmi
*Rujukan Dokumen Analisis: Dokumen [08 — Rencana Eksekusi Hibrida Minim Token](analisis-desain/08-rencana-eksekusi-hibrida-minim-token.md) dan Cetak Biru Produksi.*

Fokus pada peluncuran domain utama `wiki.karakternabawiyah.com`, mekanisme redirect 301, penyelarasan branding visual, integrasi web editor Git Alexandrie, monitoring DIUN, PWA offline, dan lokalisasi multibahasa.

- [ ] **Konfigurasi Domain Utama & DNS (`wiki.karakternabawiyah.com`)**
  - *Deskripsi:* Pengaturan DNS record (A / CNAME), setup penerbitan sertifikat SSL/TLS otomatis (Let's Encrypt), konfigurasi reverse proxy (Traefik/Caddy via Coolify), dan pembaruan konfigurasi `baseUrl: "wiki.karakternabawiyah.com"` pada Quartz.
  - *Perkiraan Token AI:* ~20k - 40k token (update konfigurasi Quartz `baseUrl`, pembuatan konfigurasi Caddy/Nginx, dan skrip verifikasi SSL/DNS).
  - *Kebutuhan HITL:* Rendah (pointing DNS di registrar domain/Cloudflare dan verifikasi status aktif HTTPS).


- [ ] **Mekanisme Redirect 301 & Penyelarasan Canonical URL**
  - *Deskripsi:* Konfigurasi permanent redirect (HTTP 301) dari URL hosting sementara / domain staging ke `wiki.karakternabawiyah.com`, serta pemastian seluruh canonical URL, sitemap XML, dan Open Graph metadata merujuk ke domain resmi.
  - *Perkiraan Token AI:* ~25k - 50k token (pembuatan rules redirect web server/Cloudflare Page Rules dan audit konsistensi tag canonical).
  - *Kebutuhan HITL:* Rendah (verifikasi uji redirect 301 pada sampel halaman materi penting).


- [ ] **Penyelarasan Branding & Identitas Visual Domain Resmi**
  - *Deskripsi:* Penyesuaian favicon, logo navbar, metadata Open Graph banner, serta footer hak cipta agar mencerminkan identitas resmi Karakter Nabawiyah saat tautan dibagikan ke publik/media sosial.
  - *Perkiraan Token AI:* ~30k - 60k token (standarisasi resolusi aset grafis, penataan metadata social preview, dan pembaruan lisensi/footer).
  - *Kebutuhan HITL:* Sedang (persetujuan visual brand identity oleh pengelola resmi Karakter Nabawiyah).


- [ ] **Integrasi Web Editor Markdown Berbasis Git ([Alexandrie](https://github.com/Smaug6739/Alexandrie))**
  - *Deskripsi:* Deployment dan integrasi Alexandrie sebagai web-based Git CMS / editor markdown yang terhubung langsung ke repositori GitHub Wiki PKN. Memungkinkan tim redaksi, asatidzah, dan guru mengedit naskah, membuat draf materi baru, melihat preview render Quartz secara langsung, serta melakukan submit commit/pull request langsung dari peramban tanpa perlu instalasi lokal (VS Code/Git).
  - *Perkiraan Token AI:* ~80k - 150k token (setup deployment container Alexandrie di Coolify/Docker, konfigurasi OAuth/GitHub App credentials, pemetaan direktori konten Quartz, dan penyusunan panduan editor bagi kontributor).
  - *Kebutuhan HITL:* Sedang (konfigurasi perizinan GitHub App, penentuan hak akses pengguna/role editor, dan pengujian alur kerja penyuntingan via browser).


- [ ] **Instalasi & Deployment DIUN (Docker Image Update Notifier) ([crazymax.dev/diun](https://crazymax.dev/diun/?utm_source=coolify.io))**
  - *Deskripsi:* Instalasi DIUN pada environment deploy server (Coolify / Docker Host) untuk memantau pembaruan image container secara otomatis (seperti container Umami, Unstructured API, reverse proxy, dll.) dan mengirimkan notifikasi instan (via Telegram, Discord, Email, atau Webhook) ketika ada rilis image versi baru di registry Docker Hub / GitHub Container Registry.
  - *Perkiraan Token AI:* ~15k - 30k token (penyusunan konfigurasi `docker-compose.yml` / template Coolify untuk DIUN, pengaturan provider Docker socket, rules filter image, dan template webhook notifikasi).
  - *Kebutuhan HITL:* Rendah (setup kredensial bot/webhook Telegram atau Discord di server Coolify serta verifikasi penangkapan alert image).


- [ ] **Dukungan Akses Offline / PWA (Progressive Web App)**
  - *Deskripsi:* Memungkinkan wiki diakses tanpa koneksi internet stabil bagi sekolah/guru di daerah minim sinyal.
  - *Perkiraan Token AI:* ~40k - 80k token (implementasi service worker, manifest JSON, dan strategi caching aset).
  - *Kebutuhan HITL:* Rendah (pengujian fungsionalitas reload halaman saat koneksi internet offline).


- [ ] **Fitur Multibahasa / i18n Berbasis Mesin Terjemahan Lokal ([Argos Translate](https://github.com/argosopentech/argos-translate))**
  - *Deskripsi:* Implementasi dukungan internasionalisasi (i18n) dan penerjemahan materi wiki ke berbagai bahasa (misal: ID ↔ EN, ID ↔ AR) menggunakan engine *neural machine translation* offline dan open-source dari Argos Translate, dengan preservasi struktur markdown (frontmatter, callout, kode teks Arab berharakat, dan tabel) serta konfigurasi bahasa di Quartz.
  - *Perkiraan Token AI:* ~200k - 400k token (pembuatan skrip integrasi batch `argos-translate`, sistem proteksi sintaks markdown/dalil saat terjemahan, setup routing/switcher bahasa di Quartz).
  - *Kebutuhan HITL:* Tinggi (kurasi editorial oleh penutur bahasa sasaran untuk memastikan ketepatan terjemahan istilah khas adab, fitrah, dan terminologi syar'i).


- [ ] **P2 — Selaraskan dokumentasi dan jalur runtime.** README kini memakai Node `>=22` dan membedakan 484 input build dari audit artikel lama; M5 dinyatakan parsial. `Dockerfile` Node lama masih digunakan oleh dokumentasi Docker nonproduksi, sedangkan deploy memakai `Dockerfile.nginx`; putuskan dukungan lokalnya dan perbarui instruksi yang terdampak sebelum menghapus. *HITL:* Rendah.


- [ ] **P2 — Uji cetak lintas-peramban dan dokumen panjang.** CSS A4 sudah diuji pada RPP dan dalil di Chromium; bandingkan Firefox/WebKit, halaman bertabel panjang dan matan Arab berharakat untuk clipping, pemenggalan, dan fallback font. Jangan samakan nama “RPP 1 Lembar” dengan jumlah halaman artikel lengkap. *HITL:* Rendah–Sedang (tinjauan visual/editorial).


- [ ] **P2 — Pantau analitik dari halaman nyata.** Skrip Umami termuat melalui `postscript` pada build, tetapi permintaan jaringan dan pencatatan kunjungan tidak diuji; validasi pada lingkungan berizin dengan persetujuan privasi dan tanpa membocorkan website ID. *HITL:* Sedang (akses analitik).


---

## Fase 7: Pipeline AI, Otomasi Audit Persona & Continuous Quality Control
*Rujukan Dokumen Analisis: Dokumen [07 — Paket Implementasi Agentic Orchestration](analisis-desain/07-paket-implementasi-agentic-orchestration.md), Master Pipeline §5, [Dewan Syura LLM Council](pipeline_designs/12_dewan_syura_llm_council_architecture.md), dan Arsitektur GraphRAG.*

Fokus pada peningkatan runner audit persona otomatis (RFC robots & multi-turn event logging), Dewan Musyawarah Redaksi AI, orkestrasi LangGraph/Langflow, Unstructured API ingest, Qdrant/GraphRAG, compounding queries, Karpathy Wiki pattern, dan continuous linter agent.

- [ ] **P2 — Peningkatan Engine & Validasi Otomatis Runner Audit Persona (`scripts/run_persona_audit.py`).**
  - *Deskripsi:* Memperkuat infrastruktur pengujian otomatis audit persona agar dapat dijalankan secara berkala pada pipeline CI/CD:
    1. Perbaiki parser `robots.txt` agar patuh standar RFC tanpa memerlukan flag bypass `--allow-invalid-robots`.
    2. Sediakan mekanisme re-crawling selektif untuk memperbarui cache snapshot `pages.json` saat terjadi pembaruan artikel.
    3. Perluas cakupan unit test di `tests/test_persona_audit_runner.py` untuk menguji URL safety, redirect validation, dan skema laporan.
  - *Target Berkas:* [`scripts/run_persona_audit.py`](scripts/run_persona_audit.py), [`tests/test_persona_audit_runner.py`](tests/test_persona_audit_runner.py).
  - *Prioritas:* P2 (Sedang — Pemeliharaan Kualitas Pengujian)
  - *Perkiraan Token AI:* ~20k - 40k token.
  - *Kebutuhan HITL:* Rendah.


- [ ] **Implementasi Dewan Musyawarah Redaksi AI (Multi-Agent Editorial Council & Critique Loop)**
  - *Deskripsi:* Membangun siklus perdebatan dan evaluasi kritis multi-agent berbasis persona pada LangGraph untuk menguji dan memperbaiki naskah secara iteratif sebelum sampai ke meja kurator manusia:
    1. **Drafter:** Merakit draf lengkap berstandar 9 lapisan.
    2. **Sharia Auditor (Faqih):** Audit keabsahan dalil, harakat teks Arab, derajat hadits via Qdrant `shamela_11m`, serta pencegahan takwil serampangan.
    3. **Pedagogical Critic (Guru Praktisi):** Menguji kepraktisan implementasi KBM di kelas/rumah, menuntut contoh konkret, dan validasi formula *'ilaj*.
    4. **Clarity Redactor:** Mengoptimalkan skor keterbacaan, memangkas kalimat berbelit, dan memastikan kepatuhan glosarium PKN.
    5. **Consensus Supervisor:** Mengagregasi feedback, membatasi putaran debat (maksimal 2–3 putaran), dan memicu gerbang persetujuan manusia jika konsensus $\ge 85\%$.
  - *Perkiraan Token AI:* ~200k - 400k token (orkestrasi prompt persona, evaluasi multi-turn reflection, dan pengujian batas konvergensi).
  - *Kebutuhan HITL:* Sedang (kalibrasi prompt persona agen bersama asatidzah dan penentuan ambang batas konsensus).
  - *Status implementasi lokal:* `scripts/hitl_workflow.py` tersedia untuk lifecycle draf Markdown nyata → preflight scorer → review manusia → handoff privat, terbatas risiko rendah–sedang. Keputusan terikat byte draf/konteks/sumber; perubahan atau kehilangan input membatalkan approval persisten. Sedang memerlukan identitas berbeda untuk peran editorial dan source. CLI council dilabeli simulasi offline belum disetujui; bukan review manusia atau provider live.
  - *Status operasional:* Butir utama tetap terbuka: belum ada bukti signoff manusia nyata, otoritas reviewer yang disepakati, integrasi LangGraph/live provider, validasi dalil eksternal, atau publikasi/deploy. Ledger memakai identitas yang dinyatakan operator lokal terpercaya, bukan autentikasi dan bukan manifest tahan modifikasi pemilik filesystem. Regresi consumer-visible ditambahkan di `tests/test_hitl_workflow.py`; verifikasi dijalankan oleh koordinator, bukan klaim pada status ini.
  - *Verifikasi lokal:* 38 pengujian HITL/council/scorer lulus. Smoke CLI risiko sedang membuktikan resume terblokir sebelum dua signoff berbeda, handoff identik byte dan idempoten, serta perubahan sumber menghasilkan `STALE`. Identitas smoke sintetis, bukan signoff operasional.


- [ ] **Pipeline Pemrosesan Dokumen Terorkestrasi (LangChain, LangGraph & LangGraph Flow)**
  - *Deskripsi:* Membangun sistem pipeline pemrosesan dokumen otomatis menggunakan LangChain dan LangGraph (serta visualisasi state graph via LangGraph Flow/Studio) untuk orkestrasi ekstraksi multi-modal (PDF, PPTX, XLSX, transkrip kajian), rekonstruksi materi tematik, verifikasi dalil syar'i via OpenBayan, standardisasi 9 lapisan format, hingga peninjauan *human-in-the-loop*.
  - *Status Kemajuan:*


    - [ ] Implementasi runner State Graph LangGraph & integrasi node Langflow
  - *Perkiraan Token AI:* ~300k - 600k token (pembuatan arsitektur state graph, perancangan prompt per node, dan integrasi API tools).
  - *Kebutuhan HITL:* Tinggi (validasi titik approval intervensi manusia sebelum naskah masuk ke repositori).


- [ ] **Migrasi Pemrosesan Dokumen ke Unstructured API ([unstructured-api](https://github.com/Unstructured-IO/unstructured-api))**
  - *Deskripsi:* Memigrasikan layer ekstraksi dan parsing dokumen multi-modal (PDF, PPTX, XLSX, DOCX, dan scan buku) dari script parser lokal ke Unstructured API (self-hosted Docker / Cloud API) untuk partisi dokumen terstruktur, ekstraksi tabel presisi tinggi, chunking semantik berbasis elemen (Title, Table, NarrativeText), serta integrasi langsung sebagai Document Loader di pipeline LangChain/LangGraph.
  - *Status Kemajuan:*


    - [ ] Penyelarasan materi hasil ekstraksi dan pengindeksan ke koleksi Qdrant **khusus korpus PKN** (bukan `shamela_11m`), dengan ID stabil, metadata sumber/lokasi, pembaruan idempoten, dan penghapusan chunk dokumen yang berubah; verifikasi hasil kueri pada sampel dokumen sebelum menandai selesai.


- [ ] **Arsitektur GraphRAG Heterogen & Bobot Sumber (Unstructured ➔ Schema Extractor ➔ SurrealDB & Qdrant)**
  - *Deskripsi:* Membangun engine GraphRAG terspesialisasi untuk menangani korpus heterogen PKN (Buku rujukan, Slide PPTX, Transkrip audio 122 video di `pkn.db`, Modul PDF, dan data terstruktur JSON):
    1. **Front-Door Ingestion:** Memanfaatkan container `unstructured-api` (port 8005) untuk preservasi tata letak slide presentasi (.pptx), tabel perbandingan, dan hierarki heading buku.
    2. **Hierarki Bobot Otoritas (*Source Weighting*):** Menetapkan bobot ilmiah berjenjang: Kitab Induk/Buku Manhaj (`authority_score = 0.9`), Slide Presentasi (`0.7`), Transkrip Audio Tanya-Jawab (`0.4`), dan JSON terstruktur.
    3. **Pre-cleaning Transkrip & Schema-Constrained Triples:** Pembersihan *conversational filler words* pada 1.159 bab transkrip rekaman video sebelum ekstraksi; membatasi ekstraksi entitas graf menggunakan Pydantic / LlamaIndex `SchemaLLMPathExtractor` yang dikunci ketat pada taksonomi baku PKN (40 Pilar TB-40, 4 Fase Usia Thufulah–Syabab, 3 Dimensi Jiwa, 3 Bahasa Mendidik, Hubungan Dalil).
    4. **Penyimpanan Graph & Hybrid Retrieval (RRF):** Menyimpan simpul dan relasi `RELATE` pada container `open-notebook-surrealdb-1` (port 8000), dipadukan dengan pencarian semantik teks hadits/dalil pada container `local_qdrant` (port 6333, koleksi `shamela_11m`). Memadukan pencarian teks Arab presisi (BM25/Full-text) dan pencarian vektor semantik via Reciprocal Rank Fusion (RRF).
    5. **Hierarchical Tree-of-Content & Sequential Narrative Flow:** Mengintegrasikan model graf dokumen dua lapis: simpul vertikal Daftar Isi (`part_of`) untuk top-down routing bab, dipadu dengan relasi baca horizontal (`next` dan `previous`) antar-chunk untuk memecahkan masalah kata ganti (*coreference*) dan mencegah pemotongan fatwa syar'i secara serampangan.
    6. **Dual-Level GraphRAG (Pola LightRAG) & AutoMergingRetriever (LlamaIndex):**
       - Menerapkan arsitektur dua tingkat: *High-Level Retrieval* untuk ringkasan bab dan manhaj makro, serta *Low-Level Retrieval* untuk dalil spesifik dan indikator karakter mikro.
       - Menerapkan `AutoMergingRetriever`: saat beberapa *leaf chunks* (~150 token) dari sub-bab yang sama terpicu, sistem otomatis menggabungkannya menjadi *parent section* (~1.200 token) untuk LLM.
    7. **Small-to-Big & Contextual Situational Prefix:** Mengindeks *child chunk* (~150 token) untuk presisi pencarian, namun menyuplai *parent section* (~1.200 token) ke LLM; menyematkan awalan situasional 50-token `[Konteks: Dokumen, Bab, Etape Usia]` untuk mengeliminasi kesalahan konteks hukum antar-fase usia anak.
  - *Perkiraan Token AI:* ~450k - 900k token (perumusan ontologi Pydantic, dual-level retrieval runner, integrasi client SurrealDB/Qdrant, dan evaluasi akurasi jawaban).
  - *Kebutuhan HITL:* Tinggi (validasi keabsahan skema relasi karakter dan review hasil jawaban RAG oleh tim asatidzah/kurator).
  - *Kriteria penerimaan:* Jalur dokumen-ke-indeks-ke-kueri dapat dijalankan ulang tanpa duplikasi; setiap hasil menunjuk dokumen, bagian/halaman atau timestamp, dan `source_id`; graf lintas dokumen tidak bentrok ID; evaluasi berlabel membandingkan baseline tanpa graf dengan graf/hybrid dan menunjukkan manfaat terukur sebelum kompleksitas baru dipertahankan.


- [ ] **Kompilasi Wiki Otomatis Pola 3-Pass Map-Reduce (Map-Reduce Wiki Compiler)**
  - *Deskripsi:* Membangun arsitektur 3 lintasan (*three-pass compilation*) untuk mengompilasi korpus multi-modal (8 buku cetak, slide daurah, dan 122 video `pkn.db`) menjadi halaman Quartz v5 berstandar Diátaxis tanpa distorsi fakta:
    1. **Pass 1 (Map / Ingestion):** Parsing via Unstructured, ekstraksi proposisi fakta atomik, dan perakitan pohon Daftar Isi (TOC Tree).
    2. **Pass 2 (Shuffle / Topic Clustering):** Mengelompokkan seluruh proposisi dan kutipan yang merujuk pada topik/entitas tertentu menggunakan algoritma *Louvain Community Detection* (pola `nashsu/llm_wiki`), diurutkan berdasarkan skor otoritas ilmiah (`Buku Manhaj 0.9 > Slide 0.7 > Transkrip Audio 0.4`).
    3. **Pass 3 (Reduce / Wiki Synthesis):** Sintesis naskah 9 lapisan Progressive Disclosure. Friksi/kontradiksi konten diselesaikan dengan mengutamakan sumber berbobot tertinggi dan mencatat perbedaannya pada seksi *Catatan Khilafiyah Lapangan*.
  - *Perkiraan Token AI:* ~250k - 500k token (orkestrasi prompt Map-Reduce, clustering entitas, dan resolusi kontradiksi).
  - *Kebutuhan HITL:* Sedang (inspeksi konsistensi hasil clustering dan validasi aturan resolusi kontradiksi).


- [ ] **Asisten Tanya Jawab PKN (Chatbot RAG Khusus)**
  - *Deskripsi:* Fitur AI pintar pencari solusi yang menjawab pertanyaan seputar PKN berbasis dokumen, graf konsep, dan dalil di wiki ini (*grounded QA* memanfaatkan layer GraphRAG di atas).
  - *Perkiraan Token AI:* ~250k - 500k token (setup chunking, embedding korpus, perumusan system prompt, dan evaluasi retrieval).
  - *Kebutuhan HITL:* Tinggi (evaluasi mitigasi halusinasi terhadap dalil dan panduan adab).
  - *Prasyarat rilis:* Retrieval dan sitasi lolos evaluasi berlabel serta review kurator; jawaban tanpa bukti memadai menyatakan keterbatasan, tidak mengarang dalil atau derajat hadits; antarmuka hanya menampilkan rujukan yang dapat ditelusuri ke sumber asli. UI publik dan kebijakan akses/biaya layanan diputuskan sebelum deployment.


- [ ] **Mekanisme Compounding Queries (Konversi Tanya-Jawab RAG Menjadi Halaman Wiki Permanen)**
  - *Deskripsi:* Menghubungkan chatbot RAG asisten PKN ke siklus akumulasi pengetahuan (*Compounding Knowledge Loop*): saat asisten menghasilkan sintesis jawaban bernilai tinggi atas problematika pengasuhan/KBM yang kompleks, jawaban tersebut tidak hilang di riwayat chat, melainkan otomatis dikompilasi menjadi draf artikel baru di direktori `content/Insight & Teknis/` atau FAQ terindeks via branch staging Git (`ingest/qna-...`), sehingga ilmu terus bertambah (*compounding*) dan siap diretrieve instan pada pencarian berikutnya.
  - *Perkiraan Token AI:* ~200k - 350k token (orkestrasi QnA synthesizer, pemetaan wikilinks, dan pembuatan draf Diátaxis).
  - *Kebutuhan HITL:* Sedang - Tinggi (review kurator/asatidzah sebelum draf jawaban RAG di-merge ke branch `main`).
  - *Kriteria penerimaan:* Jawaban tersimpan sebagai draf dengan tautan sumber dan jejak versi, bukan langsung sebagai fakta publik; kurator menyetujui perubahan sebelum merge, dan indeks hanya memperbarui konten yang telah disetujui agar jawaban sintetis tidak menjadi sumber bagi dirinya sendiri.


- [ ] **Arsitektur Tiga Tingkat "LLM-as-Librarian" & Pembaruan Diferensial (The Karpathy Wiki Pattern)**
  - *Deskripsi:* Menerapkan pemisahan mutlak tiga lapisan sistem:
    1. **Tier 1 (Raw Ingestion / Immutable):** Berkas PDF, PPTX, transkrip rekaman video `pkn.db`, dan JSON (Read-Only bagi LLM).
    2. **Tier 2 (Living Wiki Layer / Mutable Markdown):** Naskah wiki di `content/` yang dikelola LLM melalui pembaruan diferensial (*patching over rewriting* — menghitung delta informasi baru, memperbarui metadata sumber di frontmatter, dan mencatat log di changelog).
    3. **Tier 3 (Schema & Agent Rules):** Panduan Diátaxis, style guide Ustadz Abdul Kholiq, dan aturan penulisan.
    4. **Traceability Back-Pointers (Standar `nashsu/llm_wiki` & `awesome-llm-wiki`):** Setiap proposisi penting memuat blok metadata frontmatter `sources: [{file, pages, timestamp, authority}]` serta catatan kaki tak kasat mata ke berkas sumber mentah di Tier 1 (misal: `[^source-1]: Kajian_2026-03.mp4 @ 14:20`).
  - *Perkiraan Token AI:* ~200k - 400k token (pembuatan diff patcher, pelacakan sitasi presisi, dan skrip update parsial).
  - *Kebutuhan HITL:* Sedang (audit konsistensi perubahan diferensial pada artikel eksisting).


- [ ] **Wiki "Linter" Agent (Continuous Knowledge Maintenance & Audit Kualitas Korpus)**
  - *Deskripsi:* Membangun agen pemeliharaan linter offline terjadwal untuk mengaudit kesehatan struktural repositori wiki:
    1. **Orphan & Broken Link Detection:** Memindai seluruh sintaks `[[WikiLinks]]`, menandai tautan buntu (*broken target*) atau halaman yatim (*orphan page*) yang tidak memiliki rujukan masuk (*zero inbound citations*).
    2. **Contradiction Auditing:** Memindai halaman-halaman yang bertopik sama untuk mendeteksi pernyataan yang bertolak belakang (*mutually exclusive*) dan mengusulkan resolusi berbasis skor otoritas.
    3. **Synthesis Candidate Detection:** Mendeteksi konsep yang saling merujuk silang lebih dari $N$ kali untuk diusulkan pembuatan halaman komparasi/sintesis payung baru.
    4. **Community Topology Inspection:** Visualisasi klaster topik via Louvain algorithm untuk mendeteksi pulau-pulau materi yang terisolasi dari pohon navigasi utama.
  - *Perkiraan Token AI:* ~160k - 320k token (script linter markdown, parsing regex wikilinks, dan prompt deteksi kontradiksi).
  - *Kebutuhan HITL:* Rendah (peninjauan laporan temuan linter berkala).


- [ ] **Otomasi Transkripsi Kajian Suara (Speech-to-Text Pipeline)**
  - *Deskripsi:* Pipeline AI (Whisper) untuk transkripsi otomatis rekaman audio kajian/halaqah menjadi draf tulisan terstruktur.
  - *Perkiraan Token AI:* ~100k - 200k token (coding pipeline Whisper + prompt pembersihan ucapan/filler words bahasa Indonesia & istilah Arab).
  - *Kebutuhan HITL:* Sedang - Tinggi (koreksi istilah-istilah Arab/fikih yang kerap keliru pada transkripsi suara).


- [ ] **Uji Coba Sandbox Alat "Self-Building Wiki" Open-Source (`nashsu/llm_wiki`, `Graphify`, & `synthadoc`)**
  - *Deskripsi:* Menyiapkan lingkungan eksperimen (*pilot testing*) pada subset data uji (misal: 5 PDF materi + 5 transkrip rekaman video `pkn.db`) untuk mengevaluasi efisiensi aplikasi siap pakai versus pipeline kustom kita:
    1. **Uji Coba `nashsu/llm_wiki`:** Menjalankan instance desktop lokal terhadap korpus uji, mengamati ketepatan pembuatan relasi silang otomatis (*cross-links*), klaster komunitas Louvain, dan visualisasi graf Sigma.js.
    2. **Uji Coba `Graphify` & `synthadoc`:** Menilai kualitas konversi multi-format menjadi Open Knowledge Format (OKF) markdown dan ekstraksi subgraf agenik.
    3. **Evaluasi Gap & Benchmarking:** Membandingkan output alat siap pakai vs arsitektur pipeline kustom kita (apakah mampu menjaga standar 4 lapisan Progressive Disclosure, Diátaxis, dan validasi syar'i OpenBayan/Qaf AI).
  - *Perkiraan Token AI:* ~50k - 100k token (eksekusi uji coba inferensi LLM pada batch dokumen kecil dan analisis perbandingan output).
  - *Kebutuhan HITL:* Rendah - Sedang (evaluasi kualitatif terhadap kerapian struktur markdown dan konsistensi kutipan).


- [ ] **Integrasi Model Context Protocol (MCP) Servers untuk Riset Akademik & Verifikasi Ilmiah**
  - *Deskripsi:* Mengonfigurasi dan menghubungkan rangkaian MCP Server akademik ke agen AI dan pipeline riset lokal untuk penelusuran literatur empiris bebas halusinasi (sesuai rincian [`pipeline_designs/EVIDENCE_BASED_RESEARCH_WORKFLOW.md`](pipeline_designs/EVIDENCE_BASED_RESEARCH_WORKFLOW.md)):
    1. **PubMed / NCBI MCP Server:** Akses native ke kueri MeSH MEDLINE/PubMed dan PMC full-text XML untuk verifikasi data fisiologis, tumbuh kembang, dan neurosains anak.
    2. **Semantic Scholar MCP Server:** Pengambilan graf sitasi otomatis, pelacakan *influential citations*, dan ringkasan intensi sitasi berdasarkan DOI.
    3. **Zotero Local MCP Server:** Integrasi LLM langsung ke database SQLite Zotero lokal dan repository PDF riset untuk kueri semantik presisi tinggi.
    4. **Fetch / Puppeteer Markdown Scraper MCP:** Ekstraksi paper preprint (arXiv, bioRxiv) dan basis data terbuka langsung ke Markdown bersih tanpa boilerplate web.
  - *Perkiraan Token AI:* ~60k - 120k token (konfigurasi MCP server configs, pembuatan prompt adapter/tools untuk agen AI, dan pengetesan kueri literatur).
  - *Kebutuhan HITL:* Rendah (pengujian fungsional tool calling dan verifikasi integritas data yang ditarik).


---


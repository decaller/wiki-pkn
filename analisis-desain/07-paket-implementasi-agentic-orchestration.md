# Paket Implementasi Agentic Orchestration Wiki PKN

**Goal:** Menyiapkan pilot navigasi berorientasi tugas yang mempertahankan artikel, URL, kedalaman dalil, dan keselamatan pembaca sebelum keputusan produksi.

**Architecture:** Dual-layer IA memakai enam MOC sebagai jalur tugas di atas korpus kanonik yang tidak dipindahkan. OutlineNav dan indeks Obsidian mengonsumsi satu manifest navigasi; coordinator menjadi satu pemilik konfigurasi bersama. Fan-out hanya sesudah kontrak disetujui, dengan kepemilikan content/UI/generator/CSS/audit terpisah.

**Tech Stack:** Quartz v5.0.0 ESM, Preact ^10.28.2, TypeScript ^5.9.3, esbuild ^0.27.2, unified/remark, YAML, Markdown/WikiLinks, Python unittest; Node >=22 dan npm >=10.9.2; Orca supervised orchestration.

> **Status: siap untuk persiapan dan pilot terotorisasi, bukan produksi.** Dokumen ini adalah paket eksekusi bersyarat, bukan persetujuan mengubah situs. Pekerjaan penyusunan hanya mengubah dokumen07 dan README analisis; tidak menjalankan build/test/lint/formatter, tidak commit, tidak deploy. Worker implementasi kelak membaca skill relevan dan menyelesaikan checkbox sesuai dependency serta review gate.

## 1. Sumber dan batas bukti

Sintesis dua audit read-only pada run `run_f8befa457d4e`: laporan desain (`artifact://16:raw` pada coordinator, message `msg_1fc043cc60e9`) dan teknis (`artifact://23:raw`, message `msg_ca20ca194857`). URI artifact tidak tersedia di konteks worker; coordinator menyediakan delivery lengkap sebagai sumber sementara. Dokumen ini menyimpan kesimpulan yang diperlukan tanpa bergantung pada file sementara itu.

Rujukan lokal: [01 audit struktur](01-audit-struktur-saat-ini.md), [02 Diátaxis](02-audit-model-diataxis.md), [03 blueprint](03-usulan-arsitektur-informasi.md), [04 skenario](04-matriks-tugas-dan-skenario-navigasi.md), [05 protokol](05-rencana-validasi-dan-pengujian.md), [06 aksi](06-rencana-aksi-penerapan-persona-interdisipliner.md), dan [persona](persona/README.md). Angka dan contoh dalam blueprint bukan hasil uji pengguna.

| Kelas bukti | Pernyataan dan keputusan |
|---|---|
| Fakta snapshot coordinator | Baseline **486 Markdown, termasuk 4 Renungan**; 482 adalah cakupan tanpa Renungan, bukan total semua folder. Catat tanggal, aturan include/exclude dan daftar path saat eksekusi; jangan mengubah korpus demi menyamakan angka. |
| Konflik audit lama | 01 menyebut486 tetapi tujuh baris tabel berjumlah434; 02 memakai482 dan kuadran10/75/166/231. Persentase2,1%/47,9% belum didukung ledger klasifikasi per artikel. Jangan menyebutnya sensus isi tervalidasi atau target persentase produksi. |
| Fakta dokumen | Ada **13 persona aktif**, tiga profil umum rujukan, dan baseline terkini **16 skenario**. Klaim5 persona/15 skenario pada header lama dan laporan desain adalah ketertinggalan snapshot; audit desain tetap menemukan gap traceability spesifik tiap subpersona. |
| Masukan pemilik | Susunan terasa kurang rapi dan menyulitkan pengguna; bukan wawancara atau hasil observasi. |
| Hipotesis/estimasi | Enam pilar, pengurangan klik50%, tersesat/menyerah, isolasi dalil, persona primer harian/aksidental, Gen-Z ber-atensi pendek, F/Z-pattern, proporsi ideal Diátaxis dan manfaat intervensi belum terukur. |
| Smoke coordinator yang sudah diamati | `python3 scripts/hybrid_quality_scorer.py --help` dan `python3 scripts/wiki_corpus_linter.py --help` exit0; opsi `--min-score`/`--check-links` tersedia. `python3 scripts/wiki_corpus_linter.py --check-links` exit0: Broken wikilink targets0 dan True orphan pages0. Jangan ulang untuk mengonfirmasi. Ini bukan bukti URL render, build, a11y, UX, atau semua kualitas korpus. |
| Audit runtime | Percobaan codex gagal readiness karena zsh correction; omp mencapai ready dan dua audit succeeded pada `run_f8befa457d4e`. Readiness agen bukan kelulusan situs. Scout audit gagal `No model selected`; laporan diteruskan dengan pembacaan langsung. |

## 2. Kontrak pilot aman

### 2.1 Manifest enam MOC

Tidak memindahkan, mengganti nama, menghapus, menyalin per persona, atau mengubah aliases/anchors artikel lama. Tambahkan **satu collection** `Panduan` dengan **enam node** berikut dalam urutan ini, masing-masing memakai `slug` eksplisit dan `title` yang ditetapkan. Slug adalah path kanonik tanpa `.md`, bukan hasil tebakan judul.

| ID | Label | Target baru yang diotorisasi saat pilot | Slug eksplisit |
|---|---|---|---|
| mulai-di-sini | Mulai di Sini | `content/Panduan/mulai-di-sini.md` | `Panduan/mulai-di-sini` |
| fase-usia | Fase Usia | `content/Panduan/fase-usia.md` | `Panduan/fase-usia` |
| fitrah-dan-bakat | Fitrah dan Bakat | `content/Panduan/fitrah-dan-bakat.md` | `Panduan/fitrah-dan-bakat` |
| praktik-keluarga | Praktik Keluarga | `content/Panduan/praktik-keluarga.md` | `Panduan/praktik-keluarga` |
| lembaga-dan-guru | Lembaga dan Guru | `content/Panduan/lembaga-dan-guru.md` | `Panduan/lembaga-dan-guru` |
| dalil-dan-rujukan | Dalil dan Rujukan | `content/Panduan/dalil-dan-rujukan.md` | `Panduan/dalil-dan-rujukan` |

MOC memiliki lead singkat, tujuan/tugas, empat bagian **Tutorial / How-to / Reference / Explanation**, dan next action. Bagian boleh kosong dengan teks “Gap: belum ada materi yang ditinjau untuk kebutuhan ini”; tidak boleh memakai tautan fiktif atau menjanjikan fitur. Tetapkan kelas editorial MOC ringkas sebagai pengecualian sadar terhadap minimum5000 karakter artikel di `PANDUAN_PENULISAN_KONTEN.md:306–310`; jangan memanjangkan teks demi skor.

Daftar target lama yang telah dipetakan audit, bukan izin mengubah isinya:

- `content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Thufulah.md`
- `content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Tamyiz.md`
- `content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md`
- `content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Syabab.md`
- `content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/TB40/index.md`
- `content/Toolkit KBM/index.md`
- `content/Toolkit KBM/Bank Cerita Sirah dan Apersepsi KBM.md`
- `content/Master Katalog Dalil Al-Quran.md`
- `content/Master Katalog Dalil Hadits dan Sunnah.md`
- `content/Glosarium Istilah Karakter Nabawiyah.md`

Gunakan WikiLinks path-qualified relatif terhadap root content; tampilkan label manusia tanpa mengubah target. Target dewasa/pengembangan diri yang belum ditemukan dicatat gap, bukan disamakan otomatis dengan Syabab atau dijadikan pilar ketujuh. Label fase tetap **0–7,7–10,10–15,15+** sesuai korpus sampai reviewer manhaj menyetujui; blueprint0–2/2–7/7–10/10–14/14+ tidak menjadi aturan baru. Usia saja bukan pengendali taklif atau tindakan.

### 2.2 Metadata dan traceability

Frontmatter existing `title`, `description`, `tags`, `aliases` tetap. Field persona/pilar/fase/Diátaxis **hanya ditambahkan bila consumer nyata yang disetujui membaca field tersebut**; kontrak memuat tipe, vocabulary, null/empty, precedence, sumber, dan fallback konten lama. Jika tidak ada consumer, simpan pemetaan sebagai ledger desain, bukan migrasi metadata seluruh korpus. Jangan klasifikasi berdasarkan nama file saja.

Ledger wajib mencakup13 persona:01a Ayah,01b Ibu,02a Guru Thufulah,02b Guru Tamyiz,02c Guru Murahaqah,02d Guru Baligh/Syabab,02e Pembimbing Dewasa,03a Pengelola Formal,03b Pengelola Nonformal,04 Fasilitator,05 Penelaah,06 Siswa/Santri,07 Pembelajar Mandiri. Profil01/02/03 umum hanya rujukan. Tiap baris: ID/JTBD, tugas prioritas dan satu atau lebih dari16 skenario, target file/slug, tersedia/gap/usulan, accepted destination set, sumber aktif/superseded, indikator pemahaman/batas/sumber, serta representasi rekrutmen. Semua16 skenario harus terpetakan; jumlah skenario tidak membuktikan cakupan13 persona. Penggabungan segmen harus berbukti tugas setara, bukan stereotip gender/perangkat/umur.

## 3. Konflik teknis yang harus ditutup

| Bukti nyata | Keputusan integrasi |
|---|---|
| `quartz/plugins/loader/config-loader.ts:35–38`, `quartz.config.yaml` | Konfigurasi YAML, bukan `quartz.config.ts`. SPA/popovers/Umami/id-ID ada; keberadaan Umami bukan izin feedback/telemetry baru. |
| `quartz.config.yaml:137–164`, `plugins/outline-nav/src/components/OutlineNav.tsx` | OutlineNav left:40 aktif, Explorer nonaktif. Gunakan plugin dan layout deklaratif yang ada, bukan virtual folder/konvensi kedua. |
| `nav_structure.json`, `plugins/outline-nav/src/types.ts:1–21` | Record collection+structure, node title/icon/children/slug. UI merender semua collection; target slug harus ada di allFiles, judul ambigu tidak boleh menjadi tautan salah. |
| `scripts/generate_obsidian_navigation.py:104–143,237–242` | Generator lama hanya collection pertama dan mencocokkan judul/stem; perbaiki dukungan semua collection dan slug eksplisit sebelum menjanjikan parity Obsidian. Generated page overwrite milik generator saja. |
| `scripts/update_content_index.py:31–73` | Pertahankan blok BEGIN/END_COMPLETE_CONTENT_INDEX path-keyed untuk `.md/.canvas/.base` dan bagian tematik. |
| `quartz.config.yaml:78–82,116–122`, `scripts/patch_link_resolver.js` | URL mengikuti jalur fisik, crawl-links shortest/alias-redirects; HTML WikiLinks/backlinks ditangani patch. Preserve URL lama; `public/index.html` hanya artifact lama, bukan build terkini. |
| Output content-page plugin: `article.popover-hint > div.markdown-preview-view.markdown-rendered` | `.article-content` pada blueprint bukan selector nyata. Konfirmasi DOM saat smoke; constrain prose saja, bukan canvas/tabel/matan Arab. |
| `quartz/styles/custom.scss:197–219,321–405,622–658` | Reuse navbox HTML dan CSS print yang ada. Pilih **65ch untuk prose pilot**, line-height1.6; 68ch bukan keputusan paralel. Dua kata pertama heading bold butuh markup dan tidak masuk pilot tanpa kontrak. |
| `OutlineNav.tsx:153–178,270–285` | Toggle SVG/span dan collapse<=800px perlu review button/keyboard/aria/focus/SPA, bukan dianggap aksesibel. |
| `scripts/hybrid_quality_scorer.py:315–365` | Threshold70 heuristik tertimbang; durasi dicatat tetapi bukan gate latensi/WCAG. Linter audits links/vocab/style/clarity, belum gate heading berurutan. Pisahkan hard failure dari advisories, jangan memperlonggar legacy floor. |
| `pipeline_designs/README.md`, `.github/workflows/deploy.yml`, `.github/workflows/ci.yaml` | Spesifikasi11 evaluator/HITL/traceability bukan otomasi terbukti. Deploy CI melakukan linter/build; CI upstream docs bukan situs utama. Tidak otomatis deploy dari paket ini. |

## 4. Fitur contract-gated, tetap dalam backlog

Tidak ada fitur di bawah yang dianggap tersedia hanya karena MOC, Markdown, atau tautan eksternal ada. Tidak dihapus dari kebutuhan pengguna; masing-masing menunggu keputusan produk dan consumer nyata.

| Fitur | Kontrak/keputusan yang belum tersedia sebelum task implementasi |
|---|---|
| Filter TB40 | Vocabulary kluster dan membership40 tervalidasi, data owner, sumber klasifikasi, kombinasi pilihan dan empty-state, deep-link hasil, fallback tanpa JS. |
| Filter dalil | Jenis/tema/status takhrij/sumber, pemisahan nash-terjemahan-sintesis, status aktif/superseded, accepted sources, kombinasi dan kosong. |
| Filter Sirah | Item/anchor kanonik, tema dan sumber; bank existing12 narasi4 tema adalah bahan, bukan filter siap pakai. |
| Asesmen/rekomendasi | Instrumen dan izin/validitas, scoring/cutoff/interpretasi, non-diagnostik, reviewer, consent peserta anak, persistensi/retensi/penghapusan dan privasi. Instrumen19 butir bukan bukti validitas scoring. |
| Ekspor | Cetak atau PDF disepakati, sumber konten, nama file, watermark/atribusi, versi/status sumber, Arab RTL, isi yang boleh diekspor dan data pribadi. CSS print bukan downloader. |
| Feedback/analitik | Kanal/endpoint, data minimum, consent, PII, spam/moderasi, akses/retensi/penghapusan, tujuan metrik dan tanggung jawab pengelola. Jangan otomatis memasukkan feedback footer atau event Umami baru. |
| Silabus/matriks kitab/OpenBayan | Scope penulisan/integrasi, sumber dan otoritas, lisensi, ketersediaan layanan, batas klaim dan pemilik konten; bukan tambahan diam-diam dalam kurasi IA. |

Sesudah kontrak lengkap, coordinator membuat task terpisah per fitur (asesmen dan ekspor boleh dipisah bila owner/data berbeda), menetapkan path plugin baru mengikuti `plugins/outline-nav/package.json:21–35`, data ownership, consumer dan acceptance. Tanpa itu task tetap blocked; jangan membuat stub, fake fallback, hasil scoring rekayasa atau klaim selesai.

## 5. Gerbang empiris dan keselamatan

**G0 persiapan:** ledger baseline486/Renungan4,13 persona/16 skenario, manifest, kelas MOC dan batas scope disetujui coordinator/pemilik. Hasil audit cukup untuk merancang pilot, bukan memilih desain final.

**G1 keselamatan:** reviewer otoritas materi/manhaj dan perlindungan anak meninjau ringkasan usia/taklif/sanksi fisik, trauma dan rekomendasi. Pertahankan konteks hukum, batas penerapan dan bantuan profesional; jangan menjadikan ringkasan instruksi kekerasan atau nasihat klinis. Penelaah sumber memverifikasi nash/terjemahan/sintesis serta registry `data/sources_registry.csv` dan status superseded. Hasil IA tidak membuktikan penyembuhan/perubahan karakter.

**G2 protokol:** peneliti dan pemilik menetapkan baseline nyata, tugas lama/kandidat sebanding, start/end klik, denominator, accepted destinations untuk dual placement, rekrutmen seluruh segmen pemula/berpengalaman, consent dan perlindungan peserta anak. Kartu open sorting tidak menampilkan kelompok jawaban internal; label netral dan urutan acak.

**G3 empiris berurutan:** open/closed card sorting, revisi; tree testing, revisi; prototipe terpisah dan moderated usability/a11y. Agreement>=80%, TCR>=85%, directness>=75%, waktu<60s, SUS>=80, SEQ>=5,8 dari05 adalah **threshold provisional** sampai baseline/sign-off; laporkan per tugas/segmen, pemahaman/sumber/batas dan semua metrik, bukan agreement/TCR saja. Reviewer memutuskan lulus/revisi/ulang; kegagalan keselamatan tidak dapat dikompensasi skor agregat.

**G4 teknis pilot:** snapshot URL/anchors lama, smoke actual surface, keyboard/screen reader/zoom/light-dark/mobile/RTL/print dan seluruh link pilot; standar aksesibilitas serta kriteria severity disepakati. Smoke bukan sertifikat WCAG atau UX lulus. Tabel setiap artikel/F-Z pattern bukan aturan universal.

**G5 produksi:** pemilik menerima hasil G1–G4, gap, kontrak fitur yang benar-benar diotorisasi, serta rollout/rollback. Keputusan publikasi eksplisit; pilot dapat berjalan di lokal/prototipe terisolasi sebelum validasi final, tetapi produksi menunggu seluruh gate. Tidak ada auto-deploy.

## 6. Unit tugas dan waves

Semua worker menahan build/test/lint/formatter selama fan-out; coordinator melakukan verifikasi integrasi satu kali sesudah slice settled. Worker tidak commit, tidak menyentuh owner lain, dan meminta coordinator jika kontrak bergeser. Brief tiap unit di bawah **self-contained**: saat dispatch salin seluruh blok unit, kontrak §2, batas §4–5, dan path dokumen ini; jangan mengandalkan percakapan coordinator.

### P — Persiapan kontrak (wave0)

- [ ] **Target:** `analisis-desain/01-audit-struktur-saat-ini.md`, `02-audit-model-diataxis.md`, `04-matriks-tugas-dan-skenario-navigasi.md`, `05-rencana-validasi-dan-pengujian.md`, `persona/README.md`.
- [ ] **Change:** rekonsiliasi snapshot486/482/Renungan4 dan ledger artikel ber-confidence/multi-intent; traceability13/16 dan protokol G0–G3; identifikasi gap dewasa/self-improvement dan keselamatan.
- [ ] **Constraints:** read-only situs/korpus/kode; klaim lama tidak direpin sebagai hasil empiris; tidak mengarang data pengguna; belum menjalankan validasi.
- [ ] **Ownership:** coordinator atau satu worker dokumen khusus; tidak bersamaan dengan I yang menyentuh dokumen sama.
- [ ] **Observable acceptance:** pemilik dan reviewer menerima ledger, status bukti, recruitment/tasks/threshold provisional, manifest dan batas scope;16 skenario terpetakan dan semua13 persona punya indikator atau gap eksplisit. **Dependencies:** tidak ada. **Gate:** G0–G2 sebelum fan-out.

### C — Content/MOC (wave1, sesudah P)

- [ ] **Target:** `content/index.md` dan enam file `content/Panduan/` pada §2.1.
- [ ] **Change:** buat enam MOC ringkas dengan empat bagian Diátaxis, lead, next action dan link path-qualified ke target nyata §2.1; tambah entrypoint beranda tanpa menghapus akses indeks penuh; pilih source/batas dari review G1.
- [ ] **Constraints:** tidak memindahkan artikel, mengubah aliases/anchors lama, menjanjikan filter/asesmen/ekspor, atau memigrasi metadata tanpa consumer; label usia korpus tetap. Gap berupa teks, bukan link palsu.
- [ ] **Ownership:** eksklusif tujuh file ini; tidak edit nav/config/CSS/generated page.
- [ ] **Observable acceptance:** reviewer memeriksa setiap link/target dan konteks keselamatan, semua enam slug tersedia, empat bagian ada walau gap, semua13 persona punya entrypoint atau gap tercatat. **Gate:** editorial/safety sebelum I dan smoke.

### U — UI OutlineNav (wave1, sesudah P)

- [ ] **Target:** `plugins/outline-nav/src/types.ts`, `plugins/outline-nav/src/components/OutlineNav.tsx`, `plugins/outline-nav/src/components/OutlineNav.test.tsx`.
- [ ] **Change:** konsumsi manifest/slugs dengan resolver ambigu aman; gunakan button toggle dengan aria-expanded/focus; active ancestors, SPA dan mobile collapse benar. Header entrypoints hanya bila kontrak manifest komponen disetujui, bukan UI kedua.
- [ ] **Constraints:** allFiles target slug nyata; fallback konten lama; tidak edit JSON/config/plugin package; tidak klaim WCAG dari test unit. Tests permanen hanya boundary/perilaku consumer, bukan salinan wiring.
- [ ] **Ownership:** eksklusif tiga file; class/DOM contract disampaikan ke S, target slug dari C dibutuhkan saat integrasi, bukan alasan menserialkan pengembangan U.
- [ ] **Observable acceptance:** skenario ambiguous title tidak salah tautan, toggle keyboard/ARIA dan ancestor benar melalui smoke coordinator. **Gate:** technical review sebelum I.

### N — Generator/indeks (wave1, sesudah P)

- [ ] **Target:** `scripts/generate_obsidian_navigation.py`, `scripts/update_content_index.py`, generated `content/Peta Navigasi Wiki PKN.md`.
- [ ] **Change:** semua collection/slug eksplisit didukung; hasil WikiLink path-qualified/ambiguity-safe, indeks lengkap `.md/.canvas/.base` tetap dan blok tematik tidak ditimpa. Generator halaman dijalankan coordinator sesudah C+I agar tidak menulis output dari target belum ada.
- [ ] **Constraints:** tanpa rename korpus/anchors lama; jangan edit file MOC/beranda; jangan hanya special-case satu collection untuk menyembunyikan bug.
- [ ] **Ownership:** eksklusif script dan generated page; writer konten tidak menyentuh generated page.
- [ ] **Observable acceptance:** output menunjuk semua enam target dengan parity UI; fixture multi-collection/duplicate title/explicit slug tidak kehilangan tujuan; anchor indeks lama bertahan. **Gate:** resolver/output review sebelum I.

### S — Presentation (wave1, sesudah P; kontrak DOM U)

- [ ] **Target:** `quartz/styles/custom.scss`.
- [ ] **Change:** prose65ch/line-height1.6 pada selector output nyata, callout light-dark, RTL, overflow tabel, print; reuse navbox style.
- [ ] **Constraints:** tidak constrain canvas/tabel/matan Arab; tidak bold dua kata heading tanpa markup; tidak edit UI/content/config. Jika U mengubah class, sepakati kontrak dulu.
- [ ] **Ownership:** eksklusif CSS ini.
- [ ] **Observable acceptance:** desktop/mobile/200%/light-dark/Arab/print pada surface actual tidak memotong konten atau menghilangkan focus; screenshot/observasi diserahkan coordinator. **Gate:** visual/a11y review, bukan heuristik saja.

### A — Audit (wave1, sesudah P)

- [ ] **Target:** `scripts/wiki_corpus_linter.py`, `scripts/hybrid_quality_scorer.py`, `tests/test_wiki_corpus_linter.py`, `tests/test_hybrid_quality_scorer.py`, `tests/test_nav_structure.py`.
- [ ] **Change:** gate heading hierarchy dengan pengecualian code/callout/HTML yang didefinisikan; hard failures terpisah advisories; sinkronkan nav resolver tests dengan semantics explicit slug/set-based ambiguity UI, bukan raw path/last-match title.
- [ ] **Constraints:** tidak memperlonggar threshold70/legacy untuk meluluskan pilot, tidak menyamakan durasi scorer dengan latency gate, tidak mengklaim linter membuktikan UX/WCAG; hindari test source-text/incidental wording.
- [ ] **Ownership:** eksklusif lima file; U hanya memiliki test TS UI.
- [ ] **Observable acceptance:** kasus heading/slug ambigu/batas consumer menunjukkan failure yang tepat dan tidak memblokir code/callout sah melalui run integrasi coordinator. **Gate:** audit rule review sebelum I.

### I — Integrasi (wave2, sesudah C,U,N,S,A)

- [ ] **Target:** `quartz.config.yaml`, `nav_structure.json`, `plugins/outline-nav/package.json` hanya jika registrasi perlu, `package.json`/`package-lock.json` hanya jika dependency perlu, `PANDUAN_PENULISAN_KONTEN.md`, `analisis-desain/03-usulan-arsitektur-informasi.md`, `06-rencana-aksi-penerapan-persona-interdisipliner.md`, `analisis-desain/README.md`.
- [ ] **Change:** satu collection enam explicit-slug node; pertahankan collection/jalur lama yang masih diperlukan; tutup konflik YAML/Explorer/selector/fase/prose, kelas MOC dan status pilot; catat contract-gated fitur, integrasikan output generator dan verifikasi §7.
- [ ] **Constraints:** satu owner shared config/nav, dependency baru harus dibuktikan perlu; tidak deploy/commit otomatis; tidak mengubah label fase tanpa reviewer.
- [ ] **Ownership:** **coordinator satu pemilik**, tidak ada worker slice menulis file bersama. P harus settled sebelum I menyentuh dokumentasi.
- [ ] **Observable acceptance:** semua slice settled dan reviewed, snapshot URL terjaga, hasil command/smoke dengan status gagal/lulus yang jujur tersedia; produksi tetap blocked sampai G5.

### V — Validasi empiris dan keputusan rollout (wave3, sesudah I untuk prototipe)

- [ ] **Target:** protokol/hasil pada `analisis-desain/05-rencana-validasi-dan-pengujian.md` dan status `analisis-desain/README.md`; prototipe lokal, bukan deploy produksi.
- [ ] **Change:** jalankan G3 berurutan menggunakan baseline sebanding dan accepted destinations; review keselamatan/a11y serta keputusan G5.
- [ ] **Constraints:** hasil nyata saja; gap segmen atau kegagalan gate memerlukan revisi/ulang, tidak diubah menjadi klaim sukses; data peserta minimum/consent/privasi.
- [ ] **Ownership:** peneliti/reviewer hasil; coordinator mengendalikan release dan publikasi.
- [ ] **Observable acceptance:** semua metrik/per-task/per-segmen dan keputusan sign-off tercatat, rollback siap; publikasi hanya dengan otorisasi pemilik.

Fitur §4 adalah wave terpisah setelah kontraknya lengkap; **bukan dependency pilot enam MOC** dan bukan alasan mengklaim fitur telah selesai. Manifest/P adalah prerequisite bersama; C/U/N/S/A adalah fan-out eksklusif, I menunggu semuanya, V mempertahankan urutan card-sort/tree-test/usability yang benar.

## 7. Verifikasi terencana, belum dijalankan worker

Perintah berikut nyata dari audit/package/CLI, **bukan hasil kelulusan**. Coordinator menjalankan setelah izin implementasi dan slice selesai, tanpa `--fix-*`. Catat exit code, output, scope dan temuan; berhenti pada kegagalan kontrak/keselamatan.

```sh
npm run check
npm test
npx tsx --test plugins/outline-nav/src/components/OutlineNav.test.tsx
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/wiki_corpus_linter.py
python3 scripts/hybrid_quality_scorer.py --file content/Panduan/mulai-di-sini.md --min-score 70
python3 scripts/generate_obsidian_navigation.py
python3 scripts/update_content_index.py
```

`npm run check` mencakup typecheck+prettier check; tidak dijalankan pada penyusunan dokumen. Scorer perlu aturan kelas MOC disetujui sebelum skor dijadikan gate; tidak memakai placeholder filename atau menjalankan seluruh korpus tanpa scope. Output generator dihasilkan hanya sesudah manifest/target tersedia dan ditinjau karena overwrite halaman.

```sh
npm ci
node scripts/patch_link_resolver.js
npx quartz build
npx quartz build --serve --port 8888
```

Jika cache plugin belum siap, coordinator memakai `npm run install-plugins` atau `npx quartz plugin install` sesuai pipeline yang dipilih. `npx quartz build` tidak otomatis menjalankan npm prebuild; patch resolver perlu langkah eksplisit seperti CI. Jangan menjalankan workflow deploy sebagai smoke.

**Smoke aktual wajib saat implementasi:** buka server lokal di browser, kunjungi enam MOC dan target kanonik, full index anchor, deep-link URL lama/aliases, search/context/source depth, navbox HTML WikiLink dan backlinks dua arah. Periksa ambiguous title, back/forward SPA, ancestor/active state; tab/Enter/Space/Escape collapse tanpa kehilangan fokus; desktop/mobile<=800px, light-dark, zoom200%, screen reader label/state, Arab RTL, canvas/tabel/print. Simpan URL/screenshot/observasi dan batas bukti; tests saja tidak membuktikan surface. Fitur contract-gated yang nanti diotorisasi memerlukan kombinasi filter/kosong/source, asesmen input/reset/hasil valid, ekspor download+buka+RTL, feedback consent/retensi aktual. Jangan menilai fitur belum diotorisasi sebagai tersedia atau menghapusnya dari catatan gap.

## 8. Recipe Orca: receipt, dependency dan settlement

Recipe untuk coordinator sesudah G0–G2/izin pilot, **tidak dieksekusi pada penyusunan ini**. Gunakan executable yang benar dari skill/session; contoh ini memakai `orca` di terminal Orca. Muat `orca skills get orchestration` dan referensi coordinator-loop untuk DAG lebih luas. Agent `omp` hanya dipakai bila enabled/readiness lokal terkonfirmasi; percobaan codex readiness gagal tidak otomatis diulang atau dipulihkan dengan ID rekaan.

```sh
orca status --json
orca orchestration run-create --objective "Pilot enam MOC Wiki PKN; preserve korpus dan URL; tanpa deploy otomatis" --json
```

Ambil `RUN_ID` dari receipt `run-create`; `SPEC_P`, `SPEC_C`, `SPEC_U`, `SPEC_N`, `SPEC_S`, `SPEC_A`, `SPEC_I`, `SPEC_V` adalah teks lengkap brief unit§6 ditambah kontrak§2/4/5. Variabel bukan task ID statis. Mulai P dan simpan `TASK_P` serta `DISPATCH_P` dari receipt nyata:

```sh
orca orchestration task-create --run "$RUN_ID" --task-title "P kontrak persiapan" --spec "$SPEC_P" --json
orca orchestration worker-start --run "$RUN_ID" --task "$TASK_P" --worktree current --agent omp --json
```

Setelah P settled/accepted dan gerbang review terbuka, buat lima task dengan dependency **TASK_P nyata dari receipt**; salin taskId setiap receipt menjadi `TASK_C/U/N/S/A` masing-masing. Jangan mengisi string `task-1` atau ID contoh.

```sh
orca orchestration task-create --run "$RUN_ID" --task-title "C content" --spec "$SPEC_C" --deps "[\"$TASK_P\"]" --json
orca orchestration task-create --run "$RUN_ID" --task-title "U UI" --spec "$SPEC_U" --deps "[\"$TASK_P\"]" --json
orca orchestration task-create --run "$RUN_ID" --task-title "N generator" --spec "$SPEC_N" --deps "[\"$TASK_P\"]" --json
orca orchestration task-create --run "$RUN_ID" --task-title "S CSS" --spec "$SPEC_S" --deps "[\"$TASK_P\"]" --json
orca orchestration task-create --run "$RUN_ID" --task-title "A audit" --spec "$SPEC_A" --deps "[\"$TASK_P\"]" --json
orca orchestration worker-start --run "$RUN_ID" --task "$TASK_C" --worktree current --agent omp --json
orca orchestration worker-start --run "$RUN_ID" --task "$TASK_U" --worktree current --agent omp --json
orca orchestration worker-start --run "$RUN_ID" --task "$TASK_N" --worktree current --agent omp --json
orca orchestration worker-start --run "$RUN_ID" --task "$TASK_S" --worktree current --agent omp --json
orca orchestration worker-start --run "$RUN_ID" --task "$TASK_A" --worktree current --agent omp --json
orca orchestration check --wait --types "worker_done,escalation,question" --timeout-ms 900000 --json
```

Run hanya namespace, bukan scheduler; deps tidak menggantikan review/launch manual. Wave dibuat seluruhnya sebelum menunggu. Simpan semua receipt Task/Dispatch/terminal dan path evidence. Shared worktree aman hanya dengan batas eksklusif di§6; worker tidak menjalankan generator/build mid-flight. I tetap coordinator-owner: jika dieksekusi melalui worker, satu worker integrasi yang ditunjuk mewakili owner tersebut, tidak editor paralel shared config.

```sh
orca orchestration task-create --run "$RUN_ID" --task-title "I integrasi coordinator" --spec "$SPEC_I" --deps "[\"$TASK_C\",\"$TASK_U\",\"$TASK_N\",\"$TASK_S\",\"$TASK_A\"]" --json
orca orchestration worker-start --run "$RUN_ID" --task "$TASK_I" --worktree current --agent omp --json
orca orchestration task-create --run "$RUN_ID" --task-title "V validasi empiris" --spec "$SPEC_V" --deps "[\"$TASK_I\"]" --json
```

Mulai V hanya sesudah I accepted dan protokol/reviewer siap. Untuk setiap delivery, cocokkan taskId+dispatchId dengan attempt aktif; baca body/evidence, jawab question, terima outcome succeeded/failed secara eksplisit, putuskan reuse/retain/release sebelum ack. Gunakan `MESSAGE_ID`, `DISPATCH_ID`, `DELIVERY_ID` dari receipt/check, bukan fabricated IDs:

```sh
orca orchestration reply --id "$MESSAGE_ID" --body "$ANSWER" --json
orca orchestration worker-release --dispatch "$DISPATCH_ID" --json
orca orchestration check --ack "$DELIVERY_ID" --wait --types "worker_done,escalation,question" --timeout-ms 900000 --json
orca orchestration worker-list --run "$RUN_ID" --terminal-state reclaimable --json
```

Release hanya setelah accepted settlement, bukan timeout atau hilang kontak. Worker mengirim heartbeat setiap5 menit, check pada checkpoint, worker_done sekali dengan ringkasan3 kalimat, taskId/dispatchId, outcome dan path nyata; sesudah itu idle. Worker-start nonzero: baca failedStage/residualResources dan recovery reference, jangan relaunch buta. Setelah tiga wait kosong, enumerasi worker-list/include-remote dan ikuti nextAction receipt; `unverifiable` bukan process death. Jangan menambah task-update completed setelah worker_done. Akhir run harus mencatat semua outcome dan tidak menyisakan terminal reclaimable tanpa keputusan.

## 9. Rollout dan rollback

- [ ] Simpan snapshot konfigurasi/nav/URL/anchors dan sumber konten sebelum pilot; coordinator menjaga change-set per slice agar rollback tidak menghapus perubahan pengguna yang tak terkait.
- [ ] Sajikan pilot lokal atau prototipe terisolasi, tetap memberi akses indeks lengkap; jangan mengganti publik sebelum G5. Catat gap dewasa/self-improvement dan fitur contract-gated pada review.
- [ ] Pemilik menyetujui rollout terbatas dan pengamatan terukur; tidak ada deploy otomatis dari agent. Rollout produksi baru setelah gate empiris/keselamatan/teknis dan persetujuan terpisah.
- [ ] Trigger rollback: URL/anchor/backlink lama rusak, navigasi salah tujuan, regresi keyboard/RTL/print berat, sumber keliru atau risiko keselamatan/privasi. Stop publikasi, kembalikan hanya perubahan pilot/config/nav/CSS/generator yang teridentifikasi, pulihkan beranda/menu lama tanpa menyentuh artikel kanonik atau perubahan unrelated.
- [ ] Setelah rollback, coordinator mengulangi smoke jalur terdampak dan mencatat temuan/revisi; jangan memakai rollback sebagai alasan mengklaim desain lolos.

**Batas selesai paket ini:** rencana, kontrak, ownership, dependencies, gates, recipe dan tautan lokal tersedia. Tidak ada klaim build/test/UX/WCAG lulus atau pilot sudah diimplementasikan; smoke link baseline coordinator adalah satu-satunya bukti runtime situs yang dilaporkan di sini.

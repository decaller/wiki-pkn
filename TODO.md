# Roadmap & TODO List Wiki-PKN (Pendidikan Karakter Nabawiyah)

Dokumen ini melacak daftar rencana pengembangan konten, pembenahan teknis/UI, editorial, serta perangkat pendukung implementasi Wiki PKN. Setiap butir rencana dilengkapi dengan **estimasi penggunaan token AI** serta **tingkat kebutuhan tinjauan manusia (HITL - Human-in-the-Loop)**.

---

## Ringkasan Status & Metrik Estimasi

- **Status Umum:** Dalam Pengembangan Aktif
- **Target Utama:** Transisi & peluncuran ke domain resmi `wiki.karakternabawiyah.com`, integrasi web editor Alexandrie, optimalisasi UX mobile, pengayaan database materi/template, standarisasi dalil syar'i, analitik Umami, dan pipeline pemrosesan dokumen.
- **Pedoman Tingkat HITL (Human-in-the-Loop):**
  - `Rendah`: Verifikasi visual layout, pengujian fungsional/otomatis, atau review teknis sederhana.
  - `Sedang`: Pengecekan keterbacaan, validasi format operasional KBM, atau review bahasa oleh tim editor/guru.
  - `Tinggi`: Verifikasi keselarasan konsep filosofis, keabsahan dalil/takhrij, atau otorisasi materi oleh kurator/ustadz.
  - `Sangat Tinggi`: Tahqiq sanad, otentisitas syarah ulama, atau keputusan hukum/fatwa syar'i sensitif.

---

## 1. UI / UX & Tampilan Frontend
Fokus pada perbaikan responsivitas perangkat bergerak dan visualisasi informasi.

- [x] **Perbaikan layout kotak di mobile yang teksnya terpotong** `[SELESAI]`
  - *Deskripsi:* Fix overflow/wrapping teks pada komponen box/callout/card/tabel saat dibuka di viewport mobile (layar sempit) via SCSS rules di `quartz/styles/custom.scss`.
  - *Prioritas:* Tinggi (Bug UX)
  - *Perkiraan Token AI:* ~20k - 50k token.
  - *Kebutuhan HITL:* Rendah.
- [x] **Pembuatan alur materi visual (folder `content_flow/`)** `[SELESAI]`
  - *Deskripsi:* Menyediakan replika korpus direktori materi PKN di folder `content_flow/` (106 berkas) berisi diagram alur materi terstruktur (Mermaid `flowchart TD`) tanpa konten teks panjang.
  - *Perkiraan Token AI:* ~1.2M token (106 berkas × ~11k token/berkas untuk ekstraksi & sintesis node Mermaid).
  - *Kebutuhan HITL:* Rendah (validasi kelengkapan diagram dan sintaks Mermaid).
- [ ] **Pembuatan mind map untuk tiap halaman**
  - *Deskripsi:* Menyediakan visualisasi mind map / grafik relasi konsep pada setiap halaman materi untuk mempermudah navigasi mental pembaca.
  - *Perkiraan Token AI:* ~1.5M - 2M token (106 halaman × ~15k - 20k token per halaman untuk ekstraksi hierarki konsep).
  - *Kebutuhan HITL:* Sedang (validasi akurasi relasi konsep antarcabang materi oleh guru/praktisi).
- [x] **Pembuatan visualisasi flow pengolahan (arsitektur pipeline dokumen)** `[SELESAI]`
  - *Deskripsi:* Membuat visualisasi diagram alur proses/workflow pengolahan dokumen (memetakan state graph LangGraph & LangGraph Flow mulai dari input materi multi-modal, kurasi, verifikasi dalil, hingga publikasi Quartz). Tersedia lengkap di direktori [`pipeline_designs/`](pipeline_designs/README.md) (1 master README + 10 dokumen spesifikasi pipeline tematik).
  - *Perkiraan Token AI:* ~30k - 60k token (perancangan arsitektur node dan representasi diagram Mermaid/flowchart).
  - *Kebutuhan HITL:* Sedang (penyelarasan urutan langkah kurasi bersama kurator & developer).

---

## 2. Teknis, Infrastruktur Deploy, SEO & Analitik
Fokus pada visibilitas mesin pencari, pelacakan audiens, otomatisasi monitoring container server deploy, dan riwayat pembaruan sistem.

- [ ] **Peningkatan SEO (Search Engine Optimization)**
  - *Deskripsi:* Optimasi meta description, Open Graph tags, canonical URL, sitemap XML, dan struktur heading untuk indexing optimal di search engine. (Lihat catatan detail audit: [SEO_IMPLEMENTATION.md](file:///home/deck/Projects/wiki-pkn/SEO_IMPLEMENTATION.md))
  - *Perkiraan Token AI:* ~500k - 800k token (generasi meta description kontekstual untuk 100+ halaman + konfigurasi sitemap & schema markup).
  - *Kebutuhan HITL:* Rendah - Sedang (review keterbacaan cuplikan hasil pencarian dan audit tools SEO).
- [ ] **Integrasi Page Analytics Menggunakan Umami ([umami.is](https://umami.is/?utm_source=coolify.io))**
  - *Deskripsi:* Pemasangan analitik web berbasis privasi, tanpa cookie, dan ramah GDPR menggunakan Umami (didukung secara bawaan/native oleh Quartz via `{ provider: 'umami', websiteId: '...', host: '...' }`, baik melalui Cloud maupun self-hosted via Coolify). (Lihat catatan detail implementasi: [PAGE_ANALYTICS.md](file:///home/deck/Projects/wiki-pkn/PAGE_ANALYTICS.md))
  - *Perkiraan Token AI:* ~15k - 30k token (konfigurasi parameter analitik Umami pada konfigurasi Quartz dan pengujian tracking transisi SPA).
  - *Kebutuhan HITL:* Rendah (pembuatan Website ID di dashboard Umami / instance Coolify dan verifikasi penerimaan data event).
- [ ] **Instalasi & Deployment DIUN (Docker Image Update Notifier) ([crazymax.dev/diun](https://crazymax.dev/diun/?utm_source=coolify.io))**
  - *Deskripsi:* Instalasi DIUN pada environment deploy server (Coolify / Docker Host) untuk memantau pembaruan image container secara otomatis (seperti container Umami, Unstructured API, reverse proxy, dll.) dan mengirimkan notifikasi instan (via Telegram, Discord, Email, atau Webhook) ketika ada rilis image versi baru di registry Docker Hub / GitHub Container Registry.
  - *Perkiraan Token AI:* ~15k - 30k token (penyusunan konfigurasi `docker-compose.yml` / template Coolify untuk DIUN, pengaturan provider Docker socket, rules filter image, dan template webhook notifikasi).
  - *Kebutuhan HITL:* Rendah (setup kredensial bot/webhook Telegram atau Discord di server Coolify serta verifikasi penangkapan alert image).
- [ ] **Pembuatan Halaman Rilis (Changelog / Release Notes)**
  - *Deskripsi:* Menyediakan halaman khusus yang mencatat pembaruan versi, konten baru yang ditambahkan, dan log perbaikan fitur wiki.
  - *Perkiraan Token AI:* ~40k - 80k token (parsing riwayat git commit & pengelompokan changelog ramah pembaca).
  - *Kebutuhan HITL:* Rendah (kurasi poin rilis utama yang relevan bagi pengguna awam).

---

## 3. Standarisasi Bahasa, Editorial & Kualitas Penulisan
Fokus pada kejelasan kalimat, pemahaman pembaca umum, dan standardisasi istilah.

- [ ] **Pengecekan tulisan menggunakan skill Clarity ([clarity.addy.ie](https://clarity.addy.ie/))**
  - *Deskripsi:* Audit keterbacaan artikel, perbaikan kalimat berbelit (readability score), dan eliminasi ambiguitas tata bahasa.
  - *Perkiraan Token AI:* ~1.8M - 2.5M token (audit keterbacaan dan usulan penyederhanaan kalimat pada 100+ artikel wiki).
  - *Kebutuhan HITL:* Sedang - Tinggi (review tim redaksi agar esensi pesan tarbiyah tidak terdistorsi saat disederhanakan).
- [ ] **Penyusunan Glosarium (Glossary) & Minimalisasi Istilah Sulit**
  - *Deskripsi:* Membuat kamus istilah khas PKN dan mengganti/menyederhanakan diksi rumit agar mudah dipahami oleh guru dan orang tua awam.
  - *Perkiraan Token AI:* ~600k - 1M token (ekstraksi entitas istilah Arab/pedagogis khas PKN dan perumusan definisi kontekstual).
  - *Kebutuhan HITL:* Tinggi (verifikasi ketepatan definisi syar'i dan pedagogis oleh ustadz/ahli).
- [ ] **Standarisasi Progressive Disclosure & Framework Diátaxis pada Generator Konten**
  - *Deskripsi:* Menerapkan pedoman [`pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md`](pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md) pada seluruh naskah dan generator AI. Menata artikel ke dalam 4 lapisan bertingkat (Layer 1: Hook/TL;DR 10 detik, Layer 2: Core Flow Mermaid & Dalil Primer 2 menit, Layer 3: Syarah Salaf & Protokol Aksi KBM 10 menit, Layer 4: Raw Takhrij, Transkrip Video, & Graf Triples dalam `<details>`), serta memisahkan intensi konten berdasarkan 4 kuadran Diátaxis (Tutorials, How-To, Reference, Explanation) untuk mencegah artikel menjadi *flat text dump*.
  - *Status Kemajuan:*
    - [x] Panduan arsitektur informasi & template naskah di [`pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md`](pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md) `[SELESAI]`
    - [ ] Penerapan template prompt pada *Drafter & Clarity Agent* di LangGraph
    - [ ] Retrofit halaman-halaman yang sudah ada dengan summary box & collapsible raw data
  - *Perkiraan Token AI:* ~400k - 800k token (penyusunan prompt generator, retrofit naskah yang ada, dan evaluasi keterbacaan).
  - *Kebutuhan HITL:* Sedang (inspeksi konsistensi format dan keterbacaan artikel oleh tim redaksi).
- [ ] **Validasi Kepatuhan Gaya Penulisan Ustadz Abdul Kholiq (Style Compliance Audit)**
  - *Deskripsi:* Mengimplementasikan validator otomatis pada pipeline LangGraph berbasis panduan [`pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md`](pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md) dan skrip [`scripts/audit_content_gaps.py`](scripts/audit_content_gaps.py) untuk memastikan setiap naskah mematuhi 6 pilar pedagogis khas beliau: metafora fitrah ("Koneksi Sebelum Koreksi"), dalil interaksi fisik nabawiyah, diagnosis Tafrith vs Ifrath, pembagian 4 etape usia (*Thufulah–Syabab*), protokol *manhaj tadarruj*, serta blok instrumen terapan (rubrik 3-level non-angka, 3 pertanyaan reflektif muhasabah malam, dan 1 aksi cepat *Quick Win*).
  - *Status Kemajuan:*
    - [x] Panduan gaya & parameter audit 10 poin di [`pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md`](pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md) `[SELESAI]`
    - [ ] Integrasi node evaluasi gaya ke *Pedagogical Critic Agent* di LangGraph
  - *Perkiraan Token AI:* ~200k - 400k token (evaluasi kepatuhan gaya naskah dan feedback perbaikan draf).
  - *Kebutuhan HITL:* Sedang (kalibrasi sensitivitas deteksi gaya bersama tim asatidzah/kurator).
- [ ] **Penerapan Mekanisme Penulisan Kepadatan Tinggi & Pembatasan Negatif (*High-Density Prompt Engineering*)**
  - *Deskripsi:* Mencegah naskah wiki terdilusi menjadi rangkuman dangkal atau kehilangan *edge cases* syar'i/teknis akibat basa-basi AI (*LLM tells*), melalui 5 aturan mekanik penulisan:
    1. **Negative Style Constraints:** Larangan mutlak pengumuman meta (*"Dalam bab ini kita akan..."*), eliminasi kata klise/sycophantic (*krusial, vital, seamless, pilar penting yang tak tergantikan*), larangan judul kesimpulan berlabel (*"Kesimpulan/Rangkuman"*), dan penegakan kalimat aktif.
    2. **Pola Scratchpad-Then-Synthesize (`<phase_1_fact_extraction>` $\to$ `<phase_2_wiki_draft>`):** Memaksa model mengekstrak seluruh parameter dalil, batasan usia, dan patologi parenting secara atomik sebelum mulai merangkai naskah artikel, lalu memverifikasi kembali bahwa tidak ada detail yang hilang saat sintesis.
    3. **Enforce High-Density Formats:** Mengganti narasi panjang bersyarat dengan *Condition $\to$ Root Cause $\to$ Exact Remediation Matrix*; menegakkan *Specification Box Rule* (paragraf dengan $\ge 3$ parameter wajib dirender sebagai tabel kunci-nilai atau callout card).
    4. **Multi-Pass "Editor" Chaining (Two-Agent Pipeline):** Memisahkan tugas *Agent 1 (Technical Drafter)* yang menjamin 100% kelengkapan fakta/dalil dari *Agent 2 (Ruthless Copy-Editor)* yang memotong 25% kata mubazir dan menegakkan kepadatan informasi maksimal.
    5. **Kalibrasi Parameter Inferensi Model:** Menyetel $T \in [0.0, 0.2]$ dan $\text{Top-P} = 0.9$ untuk presisi terminologi syar'i dan mitigasi halusinasi.
  - *Perkiraan Token AI:* ~120k - 250k token (penyusunan prompt template system, testing perbandingan few-shot negatif-positif, dan validasi output).
  - *Kebutuhan HITL:* Rendah - Sedang (evaluasi kepadatan informasi dan eliminasi kalimat bertele-tele pada draf uji coba).

---

## 4. Pengumpulan & Kurasi Konten Inti PKN
Fokus pada pemindahan khazanah materi narasumber dan konsep-konsep pokok ke dalam wiki.

- [ ] **Kurasi materi tulisan Ustadz Bayu di grup**
  - *Deskripsi:* Mengumpulkan, menyeleksi, dan menyusun arsip materi yang pernah ditulis Ustadz Bayu di grup diskusi ke format markdown wiki yang terstruktur.
  - *Perkiraan Token AI:* ~1M - 1.8M token (ekstraksi arsip pesan, clustering tema, restrukturisasi paragraf, dan formatting markdown).
  - *Kebutuhan HITL:* Tinggi (verifikasi dan otorisasi konten langsung oleh Ustadz Bayu / murid senior).
- [ ] **Penyusunan Materi Tazkiyatun Nafs**
  - *Deskripsi:* Dokumentasi konsep, tahapan, dan implementasi Tazkiyatun Nafs dalam kerangka pendidikan karakter nabawiyah.
  - *Perkiraan Token AI:* ~150k - 300k token (sintesis naskah komprehensif, penyusunan tahapan tazkiyah, dan pemetaan dalil).
  - *Kebutuhan HITL:* Tinggi (verifikasi manhaj tazkiyah dan kesahihan dalil rujukan).
- [ ] **Konsep Pembelajaran Alamiah**
  - *Deskripsi:* Perumusan prinsip pembelajaran alamiah berbasis fitrah belajar dan sunnatullah tumbuh kembang anak.
  - *Perkiraan Token AI:* ~120k - 250k token (perumusan prinsip fitrah, analogi sunnatullah, dan komparasi metode KBM).
  - *Kebutuhan HITL:* Tinggi (penyelarasan konsep filosofis bersama perumus materi PKN).
- [ ] **Tabel & Taksonomi Tafsir Bakat TB-40 (Pengganti Bab 8 Buku Utama)**
  - *Deskripsi:* Menyusun tabel indikator, matriks karakter, dan rukun 3A Tafsir Bakat (TB-40) berbasis API Observasi Karakter (`http://localhost:4040`) sebagai **pengganti resmi Bab 8 Buku Utama PKN lama** (yang sebelumnya menggunakan ST-30 & 34 bakat Talents Mapping yang kini berstatus *superseded*).
  - *Perkiraan Token AI:* ~100k - 200k token (digitalisasi, parsing matriks indikator TB-40, dan perancangan tabel responsif).
  - *Kebutuhan HITL:* Sedang (pengecekan cross-reference indikator TB40 terhadap materi rujukan asli).
- [ ] **Pembuatan Halaman Khusus untuk Setiap Dalil**
  - *Deskripsi:* Membuat halaman mandiri untuk setiap dalil (Al-Qur'an dan Hadits) yang memuat teks dalil beserta terjemahan, referensi dalil terkait, serta syarah/komentar para ulama.
  - *Perkiraan Token AI:* ~2.5M - 4M token (inventarisasi ~150-300 dalil, query teks Arab berharakat, takhrij OpenBayan/Shamela, integrasi syarah ulama mu'tabar, dan dalil terkait).
  - *Kebutuhan HITL:* Sangat Tinggi (tahqiq kesahihan sanad/derajat hadits, akurasi teks Arab berharakat, serta kesesuaian kutipan syarah ulama oleh asatidzah).
- [x] **Pembuatan Halaman Khusus untuk Setiap Video Kajian Ustadz Abdul Khaliq** `[SELESAI]`
  - *Deskripsi:* Membuat halaman mandiri untuk setiap video kajian dan ceramah Ustadz Abdul Khaliq (122 rekaman ceramah berdasarkan basis data `pkn.db` / `PKN-videoDB`), memuat embed pemutar video YouTube, daftar bab pembahasan terindeks dengan timestamp interaktif ke detik spesifik (1.159 bab), ringkasan poin inti per segmen, transkrip tematik collapsible, serta penautan silang (*cross-link*) ke konsep materi PKN di folder `content/Kajian Video/`.
  - *Status Kemajuan:*
    - [x] Skrip generator [`scripts/generate_video_pages.py`](scripts/generate_video_pages.py) `[SELESAI]`
    - [x] Terbit 122 berkas halaman video + hub portal [`content/Kajian Video.md`](content/Kajian Video.md) `[SELESAI]`
  - *Perkiraan Token AI:* ~1.5M - 2.5M token.
  - *Kebutuhan HITL:* Sedang.
- [x] **Ingestion Seluruh Artikel Resmi SOTAB HEBAT (Karya Ustadz Abdul Kholik)** `[SELESAI]`
  - *Deskripsi:* Mengunduh dan mengompilasi seluruh 121 artikel resmi Sekolah Orangtua Ayah Bunda Hebat Indonesia (SOTAB) dari WordPress REST API ke format Markdown Quartz v5 di folder `content/Materi SOTAB/` lengkap dengan Progressive Disclosure, metadata sumber, dan portal pengindeksan [`content/Materi SOTAB.md`](content/Materi SOTAB.md).
  - *Status Kemajuan:*
    - [x] Skrip pengunduh & konverter [`scripts/ingest_sotab_articles.py`](scripts/ingest_sotab_articles.py) `[SELESAI]`
    - [x] Terbit 121 berkas materi SOTAB berstandar Quartz `[SELESAI]`
  - *Perkiraan Token AI:* ~800k - 1.2M token.
  - *Kebutuhan HITL:* Rendah - Sedang.

---

## 5. Kajian Komparasi, Profil & Review Lembaga
Fokus pada telaah kritis literatur dan pemetaan ekosistem implementasi.

- [ ] **Review masing-masing buku**
  - *Deskripsi:* Ulasan mendalam, ringkasan bab, dan relevansi masing-masing buku referensi PKN/tarbiyah islamiyah.
  - *Perkiraan Token AI:* ~800k - 1.5M token (ingestion intisari bab buku rujukan dan perumusan telaah kritis komparatif).
  - *Kebutuhan HITL:* Sedang - Tinggi (review kredibilitas tinjauan dan relevansi penerapannya di PKN).
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

---

## 6. Template Siap Pakai & Toolkit KBM
Fokus pada operasional praktis bagi pendidik dan praktisi harian.

- [ ] **Daftar dokumen bantuan dan review masing-masing dokumen**
  - *Deskripsi:* Inventarisasi dokumen panduan/petunjuk teknis pembantu serta telaah kegunaannya.
  - *Perkiraan Token AI:* ~350k - 600k token (ekstraksi metadata berkas bantuan dan pembuatan panduan penggunaan operasional).
  - *Kebutuhan HITL:* Sedang (pengecekan relevansi dokumen bantuan dengan kebutuhan riil guru).
- [ ] **Kumpulan dokumen template siap pakai**
  - *Deskripsi:* Bank dokumen siap pakai (template RPP, lembar observasi, instrumen penilaian karakter, surat, dan format laporan).
  - *Perkiraan Token AI:* ~800k - 1.5M token (generasi draf format RPP, instrumen evaluasi adab non-angka, dan lembar kerja pendidik).
  - *Kebutuhan HITL:* Sedang - Tinggi (uji coba kelayakan instrumen pada aktivitas kelas nyata).
- [ ] **Prompt AI dan template pembuatan dokumen KBM**
  - *Deskripsi:* Penyusunan sistem prompt AI siap pakai bagi guru untuk mengenerate modul ajar, rencana pembelajaran, dan studi kasus berbasis PKN.
  - *Perkiraan Token AI:* ~250k - 500k token (perancangan prompt few-shot terstruktur, pengujian batas output, dan dokumentasi petunjuk penggunaan).
  - *Kebutuhan HITL:* Sedang (evaluasi kemudahan pakai prompt oleh guru awam teknologi).
- [ ] **Kumpulan tips and trik problematika harian**
  - *Deskripsi:* FAQ dan panduan solusi praktis atas kendala harian guru/orang tua dalam menghadapi dinamika perilaku anak.
  - *Perkiraan Token AI:* ~500k - 900k token (klasifikasi kasus perilaku santri dan formulasi panduan respon nabawiyah).
  - *Kebutuhan HITL:* Tinggi (verifikasi pendekatan adab dan psikologi anak agar selaras dengan sunnah).

---

## 7. Transisi & Peluncuran Production (wiki.karakternabawiyah.com)
Fokus pada migrasi infrastruktur, domain kustom resmi, integrasi web editor untuk kontributor, dan kesiapan rilis publik.

- [ ] **Integrasi Web Editor Markdown Berbasis Git ([Alexandrie](https://github.com/Smaug6739/Alexandrie))**
  - *Deskripsi:* Deployment dan integrasi Alexandrie sebagai web-based Git CMS / editor markdown yang terhubung langsung ke repositori GitHub Wiki PKN. Memungkinkan tim redaksi, asatidzah, dan guru mengedit naskah, membuat draf materi baru, melihat preview render Quartz secara langsung, serta melakukan submit commit/pull request langsung dari peramban tanpa perlu instalasi lokal (VS Code/Git).
  - *Perkiraan Token AI:* ~80k - 150k token (setup deployment container Alexandrie di Coolify/Docker, konfigurasi OAuth/GitHub App credentials, pemetaan direktori konten Quartz, dan penyusunan panduan editor bagi kontributor).
  - *Kebutuhan HITL:* Sedang (konfigurasi perizinan GitHub App, penentuan hak akses pengguna/role editor, dan pengujian alur kerja penyuntingan via browser).
- [ ] **Konfigurasi Domain Utama & DNS (`wiki.karakternabawiyah.com`)**
  - *Deskripsi:* Pengaturan DNS record (A / CNAME), setup penerbitan sertifikat SSL/TLS otomatis (Let's Encrypt), konfigurasi reverse proxy (Traefik/Caddy via Coolify), dan pembaruan konfigurasi `baseUrl: "wiki.karakternabawiyah.com"` pada Quartz.
  - *Perkiraan Token AI:* ~20k - 40k token (update konfigurasi Quartz `baseUrl`, pembuatan konfigurasi Caddy/Nginx, dan skrip verifikasi SSL/DNS).
  - *Kebutuhan HITL:* Rendah (pointing DNS di registrar domain/Cloudflare dan verifikasi status aktif HTTPS).
- [ ] **Mekanisme Redirect 301 & Penyelarasan Canonical URL**
  - *Deskripsi:* Konfigurasi permanent redirect (HTTP 301) dari URL hosting sementara / domain staging ke `wiki.karakternabawiyah.com`, serta pemastian seluruh canonical URL, sitemap XML, dan Open Graph metadata merujuk ke domain resmi.
  - *Perkiraan Token AI:* ~25k - 50k token (pembuatan rules redirect web server/Cloudflare Page Rules dan audit konsistensi tag canonical).
  - *Kebutuhan HITL:* Rendah (verifikasi uji redirect 301 pada sampel halaman materi penting).
- [ ] **Automasi Pipeline CI/CD Build & Deploy ke Server Production**
  - *Deskripsi:* Menghubungkan webhook repositori GitHub ke runner deployment (Coolify / GitHub Actions) agar setiap perubahan naskah yang disetujui di Alexandrie atau commit pengembang otomatis memicu build Quartz dan terbit ke `wiki.karakternabawiyah.com` tanpa intervensi manual.
  - *Perkiraan Token AI:* ~40k - 80k token (penyusunan GitHub Actions workflow / webhook trigger Coolify, strategi caching aset build Quartz, dan skrip rollback).
  - *Kebutuhan HITL:* Rendah (pengujian siklus commit → trigger build otomatis → verifikasi halaman live).
- [ ] **Penyelarasan Branding & Identitas Visual Domain Resmi**
  - *Deskripsi:* Penyesuaian favicon, logo navbar, metadata Open Graph banner, serta footer hak cipta agar mencerminkan identitas resmi Karakter Nabawiyah saat tautan dibagikan ke publik/media sosial.
  - *Perkiraan Token AI:* ~30k - 60k token (standarisasi resolusi aset grafis, penataan metadata social preview, dan pembaruan lisensi/footer).
  - *Kebutuhan HITL:* Sedang (persetujuan visual brand identity oleh pengelola resmi Karakter Nabawiyah).

---

## 8. Ide dari AI (Usulan Pengembangan Tambahan)
Kumpulan ide dan usulan eksplorasi fitur, konten, serta teknis yang dapat dipertimbangkan untuk pengembangan wiki di masa mendatang.

### A. Pengayaan Konsep & Matriks Tumbuh Kembang
- [ ] **Matriks Karakter Berdasarkan Tahapan Usia (7 Tahun Pertama, Mumayyiz, Baligh)**
  - *Deskripsi:* Panduan target adab dan pendekatan komunikasi sesuai fase usia anak (sunnatullah tumbuh kembang).
  - *Perkiraan Token AI:* ~400k - 750k token (pemetaan capaian adab dan strategi komunikasi per rentang usia).
  - *Kebutuhan HITL:* Tinggi (verifikasi keselarasan tahapan tumbuh kembang dengan hadits dan fiqh tarbiyatul aulad).
- [ ] **Ensiklopedia Karakter Pokok & Karakter Turunan**
  - *Deskripsi:* Direktori karakter (*Shidq*, *Amanah*, *Iffah*, *Syaja'ah*, dll.) lengkap dengan dalil, indikator perilaku nyata, dan antitesisnya.
  - *Perkiraan Token AI:* ~1.5M - 2.5M token (penyusunan puluhan entri karakter: takrif, dalil, indikator empiris, dan antitesis).
  - *Kebutuhan HITL:* Tinggi (verifikasi ketepatan klasifikasi karakter dan dalil pendukung).
- [ ] **Modul Sinkronisasi Sekolah & Rumah (Parenting Nabawiyah)**
  - *Deskripsi:* Panduan pendampingan orang tua di rumah untuk melanjutkan pembiasaan adab dari sekolah tanpa dikotomi nilai.
  - *Perkiraan Token AI:* ~500k - 900k token (penyusunan silabus pendampingan keluarga dan lembar checklist adab di rumah).
  - *Kebutuhan HITL:* Sedang (masukan praktis dari perwakilan orang tua santri dan guru pembina).

### B. Instrumen Evaluasi & Asesmen Guru
- [ ] **Rubrik & Format Observasi Karakter Tanpa Angka**
  - *Deskripsi:* Evaluasi karakter berbasis narasi perkembangan dan pengamatan perilaku nyata, bukan sekadar skor angka ujian.
  - *Perkiraan Token AI:* ~450k - 800k token (perumusan indikator perilaku deskriptif & rubrik asesmen naratif).
  - *Kebutuhan HITL:* Tinggi (validasi konstruk instrumen penilaian karakter oleh pakar evaluasi pendidikan).
- [ ] **Bank Cerita Sirah & Apersepsi KBM**
  - *Deskripsi:* Kumpulan kisah Rasulullah ﷺ dan para sahabat yang dipetakan ke tema-tema pelajaran sains/sosial/matematika untuk apersepsi KBM.
  - *Perkiraan Token AI:* ~1.2M - 2M token (kurasi riwayat sirah shahihah dan pemetaannya ke topik kurikulum umum).
  - *Kebutuhan HITL:* Tinggi (tahqiq keabsahan riwayat sirah agar terhindar dari kisah dha'if/maudhu').
- [ ] **Panduan Penanganan Kasus Khusus (Adiksi Gadget, Bullying, Tantrum)**
  - *Deskripsi:* SOP islami dan pendekatan nabawi dalam menangani pelanggaran adab atau trauma psikologis anak di lingkungan sekolah.
  - *Perkiraan Token AI:* ~400k - 750k token (penyusunan SOP integratif syariat-psikologis untuk krisis perilaku).
  - *Kebutuhan HITL:* Sangat Tinggi (review konselor adab anak, psikolog muslim, dan kepala sekolah).

### C. Navigasi & Pengalaman Membaca (Knowledge Graph & UX)
- [ ] **Jalur Belajar / Reading Path untuk Pemula ("Mulai Dari Sini")**
  - *Deskripsi:* Urutan baca terkurasi bagi guru atau orang tua baru agar tidak kebingungan menjelajahi khazanah wiki.
  - *Perkiraan Token AI:* ~100k - 200k token (analisis keterkaitan materi wiki dan penyusunan silabus baca terstruktur).
  - *Kebutuhan HITL:* Sedang (review alur pemahaman oleh pengguna pemula/guru baru).
- [ ] **Optimasi Tipografi Teks Arab & Terjemahan**
  - *Deskripsi:* Penerapan font naskh khusus web (Amiri / Scheherazade New) dan layout dwibahasa yang nyaman dibaca di layar mobile.
  - *Perkiraan Token AI:* ~20k - 40k token (tuning CSS webfont, penyesuaian font-size, line-height, dan layout terjemahan).
  - *Kebutuhan HITL:* Sedang (uji kenyamanan membaca teks Arab berharakat oleh asatidzah).

### D. Fitur Teknis Platform & Distribusi
- [ ] **Fitur Ekspor PDF Rapi Siap Cetak (Print Stylesheet)**
  - *Deskripsi:* Cetak halaman materi / RPP / modul dalam format A4 bersih tanpa elemen navigasi website.
  - *Perkiraan Token AI:* ~30k - 60k token (pembuatan aturan `@media print` CSS, page break, dan header/footer bersih).
  - *Kebutuhan HITL:* Rendah (pengujian print-preview di beberapa peramban).
- [ ] **Dukungan Akses Offline / PWA (Progressive Web App)**
  - *Deskripsi:* Memungkinkan wiki diakses tanpa koneksi internet stabil bagi sekolah/guru di daerah minim sinyal.
  - *Perkiraan Token AI:* ~40k - 80k token (implementasi service worker, manifest JSON, dan strategi caching aset).
  - *Kebutuhan HITL:* Rendah (pengujian fungsionalitas reload halaman saat koneksi internet offline).
- [ ] **Taksonomi & Filter Tag Khusus Dalil**
  - *Deskripsi:* Pencarian dan pemfilteran dalil berdasarkan surah, topik adab, kualitas/sanad hadits, atau kata kunci tematik.
  - *Perkiraan Token AI:* ~300k - 600k token (auto-tagging dalil berdasarkan kategori surah, tema karakter, dan perawi).
  - *Kebutuhan HITL:* Sedang - Tinggi (review akurasi label kategorisasi syar'i).
- [ ] **Fitur Multibahasa / i18n Berbasis Mesin Terjemahan Lokal ([Argos Translate](https://github.com/argosopentech/argos-translate))**
  - *Deskripsi:* Implementasi dukungan internasionalisasi (i18n) dan penerjemahan materi wiki ke berbagai bahasa (misal: ID ↔ EN, ID ↔ AR) menggunakan engine *neural machine translation* offline dan open-source dari Argos Translate, dengan preservasi struktur markdown (frontmatter, callout, kode teks Arab berharakat, dan tabel) serta konfigurasi bahasa di Quartz.
  - *Perkiraan Token AI:* ~200k - 400k token (pembuatan skrip integrasi batch `argos-translate`, sistem proteksi sintaks markdown/dalil saat terjemahan, setup routing/switcher bahasa di Quartz).
  - *Kebutuhan HITL:* Tinggi (kurasi editorial oleh penutur bahasa sasaran untuk memastikan ketepatan terjemahan istilah khas adab, fitrah, dan terminologi syar'i).

### E. Kolaborasi & Tata Kelola Komunitas
- [ ] **Pedoman Kontributor (Style Guide Penulisan Wiki)**
  - *Deskripsi:* Standarisasi format penulisan, sitasi dalil, dan struktur markdown bagi asatidzah/guru yang menyumbang materi.
  - *Perkiraan Token AI:* ~80k - 150k token (penulisan dokumen SOP standarisasi markdown, takhrij, dan etika kutipan).
  - *Kebutuhan HITL:* Sedang (persetujuan tim redaksi wiki).
- [ ] **Direktori Narasumber & Trainer PKN**
  - *Deskripsi:* Daftar kontak atau lembaga penyedia workshop, sertifikasi, dan pelatihan implementasi PKN untuk sekolah.
  - *Perkiraan Token AI:* ~50k - 100k token (strukturisasi profil narasumber, bidang kepakaran, dan format kontak).
  - *Kebutuhan HITL:* Tinggi (verifikasi data kontak dan izin pencantuman dari narasumber terkait).

### F. Integrasi Multimedia & Perpustakaan Digital
- [ ] **Audio Player Kajian Tersemat (Embedded Audio)**
  - *Deskripsi:* Pemutar audio ringkas pada halaman materi agar pembaca bisa mendengarkan rekaman kajian Ustadz Bayu / narasumber sembari membaca transkrip.
  - *Perkiraan Token AI:* ~25k - 50k token (komponen audio player Quartz, linking file audio, dan sinkronisasi bab).
  - *Kebutuhan HITL:* Rendah (pengujian pemutaran audio di perangkat desktop dan mobile).
- [ ] **PDF Deep-Linking (Tautan Langsung ke Halaman Dokumen/Kitab)**
  - *Deskripsi:* Integrasi pipeline OCR `searchable_pdfs` agar kutipan langsung membuka halaman buku atau kitab rujukan asli.
  - *Perkiraan Token AI:* ~200k - 400k token (pemetaan sitasi teks ke koordinat/nomor halaman berkas PDF).
  - *Kebutuhan HITL:* Sedang (uji coba presisi deep link pada sampel kutipan buku).

### G. AI & Otomasi Pipeline Konten
- [ ] **Pipeline Pemrosesan Dokumen Terorkestrasi (LangChain, LangGraph & LangGraph Flow)**
  - *Deskripsi:* Membangun sistem pipeline pemrosesan dokumen otomatis menggunakan LangChain dan LangGraph (serta visualisasi state graph via LangGraph Flow/Studio) untuk orkestrasi ekstraksi multi-modal (PDF, PPTX, XLSX, transkrip kajian), rekonstruksi materi tematik, verifikasi dalil syar'i via OpenBayan, standardisasi 9 lapisan format, hingga peninjauan *human-in-the-loop*.
  - *Status Kemajuan:*
    - [x] Spesifikasi master arsitektur & 10 desain pipeline tematik di [`pipeline_designs/`](pipeline_designs/README.md) `[SELESAI]`
    - [x] Desain siklus multi-agent debate (Drafter, Sharia Auditor, Pedagogy Critic, Clarity Editor, Supervisor) `[SELESAI]`
    - [ ] Implementasi runner State Graph LangGraph & integrasi node Langflow
  - *Perkiraan Token AI:* ~300k - 600k token (pembuatan arsitektur state graph, perancangan prompt per node, dan integrasi API tools).
  - *Kebutuhan HITL:* Tinggi (validasi titik approval intervensi manusia sebelum naskah masuk ke repositori).
- [ ] **Implementasi Dewan Musyawarah Redaksi AI (Multi-Agent Editorial Council & Critique Loop)**
  - *Deskripsi:* Membangun siklus perdebatan dan evaluasi kritis multi-agent berbasis persona pada LangGraph untuk menguji dan memperbaiki naskah secara iteratif sebelum sampai ke meja kurator manusia:
    1. **Drafter:** Merakit draf lengkap berstandar 9 lapisan.
    2. **Sharia Auditor (Faqih):** Audit keabsahan dalil, harakat teks Arab, derajat hadits via Qdrant `shamela_11m`, serta pencegahan takwil serampangan.
    3. **Pedagogical Critic (Guru Praktisi):** Menguji kepraktisan implementasi KBM di kelas/rumah, menuntut contoh konkret, dan validasi formula *'ilaj*.
    4. **Clarity Redactor:** Mengoptimalkan skor keterbacaan, memangkas kalimat berbelit, dan memastikan kepatuhan glosarium PKN.
    5. **Consensus Supervisor:** Mengagregasi feedback, membatasi putaran debat (maksimal 2–3 putaran), dan memicu gerbang persetujuan manusia jika konsensus $\ge 85\%$.
  - *Perkiraan Token AI:* ~200k - 400k token (orkestrasi prompt persona, evaluasi multi-turn reflection, dan pengujian batas konvergensi).
  - *Kebutuhan HITL:* Sedang (kalibrasi prompt persona agen bersama asatidzah dan penentuan ambang batas konsensus).
- [x] **Prototype Runner Pipeline Dalil Mandiri (Pipeline 07 Dalil)** `[SELESAI]`
  - *Deskripsi:* Membangun skrip eksekutor Python pertama ([`scripts/pipeline_runner_dalil.py`](scripts/pipeline_runner_dalil.py)) yang mengimplementasikan 4 Lapisan Progressive Disclosure, takhrij matan teks Arab, terjemahan, syarah ulama mu'tabar, serta matriks operasional KBM di `content/Dalil/`.
  - *Status Kemajuan:*
    - [x] Skrip eksekutor [`scripts/pipeline_runner_dalil.py`](scripts/pipeline_runner_dalil.py) `[SELESAI]`
    - [x] Terbit 4 halaman dalil induk percontohan di `content/Dalil/` `[SELESAI]`
  - *Perkiraan Token AI:* ~50k - 100k token.
  - *Kebutuhan HITL:* Rendah - Sedang.
- [x] **Wiki Linter Agent & Style Auditor (Continuous Maintenance Script)** `[SELESAI]`
  - *Deskripsi:* Membangun alat audit linter offline ([`scripts/wiki_linter.py`](scripts/wiki_linter.py)) untuk memindai broken `[[WikiLinks]]`, mendeteksi halaman orphan (inbound links = 0), dan mengevaluasi kepatuhan naskah terhadap 10 checklist gaya penulisan Ustadz Abdul Kholiq.
  - *Status Kemajuan:*
    - [x] Skrip linter [`scripts/wiki_linter.py`](scripts/wiki_linter.py) `[SELESAI]`
  - *Perkiraan Token AI:* ~40k - 80k token.
  - *Kebutuhan HITL:* Rendah.
- [ ] **Migrasi Pemrosesan Dokumen ke Unstructured API ([unstructured-api](https://github.com/Unstructured-IO/unstructured-api))**
  - *Deskripsi:* Memigrasikan layer ekstraksi dan parsing dokumen multi-modal (PDF, PPTX, XLSX, DOCX, dan scan buku) dari script parser lokal ke Unstructured API (self-hosted Docker / Cloud API) untuk partisi dokumen terstruktur, ekstraksi tabel presisi tinggi, chunking semantik berbasis elemen (Title, Table, NarrativeText), serta integrasi langsung sebagai Document Loader di pipeline LangChain/LangGraph.
  - *Status Kemajuan:*
    - [x] Rencana implementasi teknis & alokasi port host `8005` (lihat [implementation_plan.md](file:///home/abuhafi/.gemini/antigravity-ide/brain/c5f632a1-642b-45fa-87cc-28e8af74a811/implementation_plan.md)) `[SELESAI]`
    - [x] Berkas deployment [`docker-compose.unstructured.yml`](docker-compose.unstructured.yml) (kompatibel DIUN & healthcheck) `[SELESAI]`
    - [x] Client adapter Python [`scripts/unstructured_adapter.py`](scripts/unstructured_adapter.py) (partisi elemen, tabel ke markdown, LangChain chunking, MD5 caching) `[SELESAI]`
    - [x] Generator Hierarchical Narrative Graph (TOC + prev/next chunk edges) di [`scripts/unstructured_adapter.py`](scripts/unstructured_adapter.py) `[SELESAI]`
    - [x] Skrip uji & validasi [`scripts/benchmark_extraction.py`](scripts/benchmark_extraction.py) (unit test table converter & schema transformer) `[SELESAI]`
    - [ ] Peluncuran container & batch ingestion dokumen PDF/PPTX `searchable_pdfs/` ke vector store
  - *Perkiraan Token AI:* ~150k - 300k token (pembuatan adapter API client Python, konfigurasi deployment container, transformasi skema chunking, dan pengujian perbandingan akurasi ekstraksi).
  - *Kebutuhan HITL:* Sedang (evaluasi presisi hasil partisi teks, struktur tabel, dan teks Arab berharakat pada sampel dokumen PDF modul PKN).
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
- [ ] **Mekanisme Compounding Queries (Konversi Tanya-Jawab RAG Menjadi Halaman Wiki Permanen)**
  - *Deskripsi:* Menghubungkan chatbot RAG asisten PKN ke siklus akumulasi pengetahuan (*Compounding Knowledge Loop*): saat asisten menghasilkan sintesis jawaban bernilai tinggi atas problematika pengasuhan/KBM yang kompleks, jawaban tersebut tidak hilang di riwayat chat, melainkan otomatis dikompilasi menjadi draf artikel baru di direktori `content/Insight & Teknis/` atau FAQ terindeks via branch staging Git (`ingest/qna-...`), sehingga ilmu terus bertambah (*compounding*) dan siap diretrieve instan pada pencarian berikutnya.
  - *Perkiraan Token AI:* ~200k - 350k token (orkestrasi QnA synthesizer, pemetaan wikilinks, dan pembuatan draf Diátaxis).
  - *Kebutuhan HITL:* Sedang - Tinggi (review kurator/asatidzah sebelum draf jawaban RAG di-merge ke branch `main`).
- [ ] **Arsitektur Tiga Tingkat "LLM-as-Librarian" & Pembaruan Diferensial (The Karpathy Wiki Pattern)**
  - *Deskripsi:* Menerapkan pemisahan mutlak tiga lapisan sistem:
    1. **Tier 1 (Raw Ingestion / Immutable):** Berkas PDF, PPTX, transkrip rekaman video `pkn.db`, dan JSON (Read-Only bagi LLM).
    2. **Tier 2 (Living Wiki Layer / Mutable Markdown):** Naskah wiki di `content/` yang dikelola LLM melalui pembaruan diferensial (*patching over rewriting* — menghitung delta informasi baru, memperbarui metadata sumber di frontmatter, dan mencatat log di changelog).
    3. **Tier 3 (Schema & Agent Rules):** Panduan Diátaxis, style guide Ustadz Abdul Kholiq, dan aturan penulisan.
    4. **Traceability Back-Pointers (Standar `nashsu/llm_wiki` & `awesome-llm-wiki`):** Setiap proposisi penting memuat blok metadata frontmatter `sources: [{file, pages, timestamp, authority}]` serta catatan kaki tak kasat mata ke berkas sumber mentah di Tier 1 (misal: `[^source-1]: Kajian_2026-03.mp4 @ 14:20`).
  - *Perkiraan Token AI:* ~200k - 400k token (pembuatan diff patcher, pelacakan sitasi presisi, dan skrip update parsial).
  - *Kebutuhan HITL:* Sedang (audit konsistensi perubahan diferensial pada artikel eksisting).
- [x] **Kerangka Presedensi Berjenjang & Peluruhan Waktu (*Tiered Precedence & Decay Framework*)** `[SELESAI]`
  - *Deskripsi:* Membangun mekanisme mitigasi benturan materi antar-dokumen berdasarkan daur hidup, edisi revisi, penulis, dan media:
    1. **Master Sources Registry (`data/sources_registry.csv`):** Menginventarisasi seluruh sumber PKN dengan penugasan Tier (1: Active Truth, 2: Foundational/Legacy, 3: Ephemeral Audio) dan laju peluruhan $\lambda$.
    2. **Kewenangan Penulis (Author Authority):** Menetapkan pengali otoritas penuh ($1.0\times$) untuk Ustadz Abdul Kholiq sebagai perumus utama, dan menyetel bobot lebih rendah ($0.65\times$) untuk penulis lain/eksternal.
    3. **Pengecualian Time-Decay Abadi ($\lambda = 0.0$):** Seluruh dalil Al-Qur'an, Hadits Sunnah Nabawiyah, dan Kitab Turats Ulama Salaf (An-Nawawi, Ibnul Qayyim, Al-Ghazali) dikecualikan mutlak dari peluruhan waktu ($e^0 = 1.0$), sementara tulisan kontemporer yang lebih tua otomatis terdepresiasi seiring berjalannya tahun.
    4. **Perhitungan Time-Decay Dinamis (`scripts/source_precedence.py`):** Menghitung bobot efektif $W_{\text{eff}} = W_{\text{tier}} \times W_{\text{author}} \times e^{-\lambda \cdot \Delta t}$ saat retrieval.
    5. **Relasi Graf *SUPERSEDES* & Penyajian Naskah Quartz:** Menelusuri rantai silsilah revisi (misal: Buku 2024 *supersedes* Diktat 2016). Konsep lama tetap dipertahankan pada blok collapsible `<details><summary>Catatan Sejarah & Evolusi Manhaj</summary></details>` alih-alih dihapus.
  - *Status Kemajuan:*
    - [x] Registry terpusat [`data/sources_registry.csv`](data/sources_registry.csv) `[SELESAI]`
    - [x] Modul kalkulator presedensi [`scripts/source_precedence.py`](scripts/source_precedence.py) `[SELESAI]`
    - [x] Template naskah evolusi di [`pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md`](pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md) `[SELESAI]`
  - *Perkiraan Token AI:* ~50k - 100k token.
  - *Kebutuhan HITL:* Rendah - Sedang.
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
- [ ] **Skrip Validasi Takhrij & Nomor Dalil Otomatis**
  - *Deskripsi:* Pengecekan otomatis (CI/hook) untuk validasi format nomor surah:ayat dan periwayat hadits saat artikel baru ditambahkan.
  - *Perkiraan Token AI:* ~80k - 150k token (penulisan regex validator, integrasi database surah/hadits, dan setup GitHub Action).
  - *Kebutuhan HITL:* Rendah (pengecekan false positives pada penulisan nama surah dan nomor ayat).
- [ ] **Uji Coba Sandbox Alat "Self-Building Wiki" Open-Source (`nashsu/llm_wiki`, `Graphify`, & `synthadoc`)**
  - *Deskripsi:* Menyiapkan lingkungan eksperimen (*pilot testing*) pada subset data uji (misal: 5 PDF materi + 5 transkrip rekaman video `pkn.db`) untuk mengevaluasi efisiensi aplikasi siap pakai versus pipeline kustom kita:
    1. **Uji Coba `nashsu/llm_wiki`:** Menjalankan instance desktop lokal terhadap korpus uji, mengamati ketepatan pembuatan relasi silang otomatis (*cross-links*), klaster komunitas Louvain, dan visualisasi graf Sigma.js.
    2. **Uji Coba `Graphify` & `synthadoc`:** Menilai kualitas konversi multi-format menjadi Open Knowledge Format (OKF) markdown dan ekstraksi subgraf agenik.
    3. **Evaluasi Gap & Benchmarking:** Membandingkan output alat siap pakai vs arsitektur pipeline kustom kita (apakah mampu menjaga standar 4 lapisan Progressive Disclosure, Diátaxis, dan validasi syar'i OpenBayan/Qaf AI).
  - *Perkiraan Token AI:* ~50k - 100k token (eksekusi uji coba inferensi LLM pada batch dokumen kecil dan analisis perbandingan output).
  - *Kebutuhan HITL:* Rendah - Sedang (evaluasi kualitatif terhadap kerapian struktur markdown dan konsistensi kutipan).

### H. Program Pembiasaan Santri & Kemitraan Wali Murid
- [ ] **Format Jurnal Mutaba'ah Yaumiyah (Buku Amalan Harian Terintegrasi)**
  - *Deskripsi:* Template jurnal harian santri (shalat berjamaah, dzikir, tilawah, adab, birrul walidain) yang terhubung ke indikator PKN.
  - *Perkiraan Token AI:* ~150k - 300k token (penyusunan tabel amalan harian, checklist adab, dan format evaluasi bersama wali murid).
  - *Kebutuhan HITL:* Sedang (penyelarasan target amalan harian dengan budaya sekolah/pesantren).
- [ ] **Program "Tantangan Karakter Pekanan" (Weekly Character Campaign)**
  - *Deskripsi:* Panduan program tematik mingguan di sekolah dan rumah (contoh: Pekan Menjaga Lisan, Pekan Kejujuran, Pekan Berbagi).
  - *Perkiraan Token AI:* ~300k - 600k token (pembuatan silabus aktivitas pekanan, panduan guru, dan kriteria evaluasi anak).
  - *Kebutuhan HITL:* Sedang (penyesuaian dengan kalender kegiatan sekolah dan kesiapan wali murid).
- [ ] **Kartu Kasus Lapangan & Diskusi Guru (Teacher Case Study Cards)**
  - *Deskripsi:* Kartu simulasi studi kasus harian untuk bahan *morning briefing* guru dalam menyikapi dinamika adab santri.
  - *Perkiraan Token AI:* ~350k - 700k token (generasi skenario dinamika santri, pertanyaan pemantik, dan panduan respon nabawiyah).
  - *Kebutuhan HITL:* Tinggi (review kesesuaian solusi tindakan disiplin dengan prinsip kasih sayang nabawiyah).

### I. Visualisasi Media & Aksesibilitas Pembaca
- [ ] **Infografis Ringkasan Siap Sebar (Format WhatsApp/Media Sosial)**
  - *Deskripsi:* Desain ringkasan 1 lembar visual (1080x1080 / PDF 1 halaman) materi pokok untuk memudahkan guru menyebarkannya ke WAG wali murid.
  - *Perkiraan Token AI:* ~400k - 800k token (ekstraksi intisari artikel, copywriting ringkas, dan penyusunan prompt instruksi desain visual).
  - *Kebutuhan HITL:* Sedang (review kejelasan pesan visual oleh tim media/komunikasi).


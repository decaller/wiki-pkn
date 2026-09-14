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

- [ ] **Perbaikan layout kotak di mobile yang teksnya terpotong**
  - *Deskripsi:* Fix overflow/wrapping teks pada komponen box/callout/card saat dibuka di viewport mobile (layar sempit).
  - *Prioritas:* Tinggi (Bug UX)
  - *Perkiraan Token AI:* ~20k - 50k token (inspeksi CSS Quartz, penyesuaian media query, dan pengujian rendering).
  - *Kebutuhan HITL:* Rendah (inspeksi visual tampilan pada viewport smartphone).
- [x] **Pembuatan alur materi visual (folder `content_flow/`)** `[SELESAI]`
  - *Deskripsi:* Menyediakan replika korpus direktori materi PKN di folder `content_flow/` (106 berkas) berisi diagram alur materi terstruktur (Mermaid `flowchart TD`) tanpa konten teks panjang.
  - *Perkiraan Token AI:* ~1.2M token (106 berkas × ~11k token/berkas untuk ekstraksi & sintesis node Mermaid).
  - *Kebutuhan HITL:* Rendah (validasi kelengkapan diagram dan sintaks Mermaid).
- [ ] **Pembuatan mind map untuk tiap halaman**
  - *Deskripsi:* Menyediakan visualisasi mind map / grafik relasi konsep pada setiap halaman materi untuk mempermudah navigasi mental pembaca.
  - *Perkiraan Token AI:* ~1.5M - 2M token (106 halaman × ~15k - 20k token per halaman untuk ekstraksi hierarki konsep).
  - *Kebutuhan HITL:* Sedang (validasi akurasi relasi konsep antarcabang materi oleh guru/praktisi).
- [ ] **Pembuatan visualisasi flow pengolahan (arsitektur pipeline dokumen)**
  - *Deskripsi:* Membuat visualisasi diagram alur proses/workflow pengolahan dokumen (memetakan state graph LangGraph & LangGraph Flow mulai dari input materi multi-modal, kurasi, verifikasi dalil, hingga publikasi).
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
- [ ] **Tabel TB40**
  - *Deskripsi:* Pembuatan dan penyusunan tabel indikator/materi TB40 sebagai matriks rujukan evaluasi dan capaian.
  - *Perkiraan Token AI:* ~100k - 200k token (digitalisasi, parsing matriks indikator, dan perancangan tabel responsif).
  - *Kebutuhan HITL:* Sedang (pengecekan cross-reference indikator TB40 terhadap materi rujukan asli).
- [ ] **Pembuatan Halaman Khusus untuk Setiap Dalil**
  - *Deskripsi:* Membuat halaman mandiri untuk setiap dalil (Al-Qur'an dan Hadits) yang memuat teks dalil beserta terjemahan, referensi dalil terkait, serta syarah/komentar para ulama.
  - *Perkiraan Token AI:* ~2.5M - 4M token (inventarisasi ~150-300 dalil, query teks Arab berharakat, takhrij OpenBayan/Shamela, integrasi syarah ulama mu'tabar, dan dalil terkait).
  - *Kebutuhan HITL:* Sangat Tinggi (tahqiq kesahihan sanad/derajat hadits, akurasi teks Arab berharakat, serta kesesuaian kutipan syarah ulama oleh asatidzah).

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
- [ ] **Integrasi Obsidian Canvas (`.canvas`) ke Tampilan Web Interaktif**
  - *Deskripsi:* Memvisualisasikan file `.canvas` di browser secara interaktif untuk mempermudah pemahaman keterkaitan antar konsep PKN.
  - *Perkiraan Token AI:* ~50k - 100k token (coding parser JSON `.canvas` ke komponen canvas interaktif).
  - *Kebutuhan HITL:* Rendah (pengecekan visual rendering dan interaksi zoom/pan di browser).
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
- [ ] **Viewer Presentasi Interaktif di Web (Slide Deck Viewer)**
  - *Deskripsi:* Konversi materi presentasi di folder `presentations/` menjadi slide web interaktif (Reveal.js) siap tampil untuk media ajar kelas.
  - *Perkiraan Token AI:* ~150k - 300k token (konversi struktur slide PPTX ke markdown Reveal.js interaktif).
  - *Kebutuhan HITL:* Sedang (pengecekan visual estetika slide dan keterbacaan materi ajar).
- [ ] **PDF Deep-Linking (Tautan Langsung ke Halaman Dokumen/Kitab)**
  - *Deskripsi:* Integrasi pipeline OCR `searchable_pdfs` agar kutipan langsung membuka halaman buku atau kitab rujukan asli.
  - *Perkiraan Token AI:* ~200k - 400k token (pemetaan sitasi teks ke koordinat/nomor halaman berkas PDF).
  - *Kebutuhan HITL:* Sedang (uji coba presisi deep link pada sampel kutipan buku).

### G. AI & Otomasi Pipeline Konten
- [ ] **Pipeline Pemrosesan Dokumen Terorkestrasi (LangChain, LangGraph & LangGraph Flow)**
  - *Deskripsi:* Membangun sistem pipeline pemrosesan dokumen otomatis menggunakan LangChain dan LangGraph (serta visualisasi state graph via LangGraph Flow/Studio) untuk orkestrasi ekstraksi multi-modal (PDF, PPTX, XLSX, transkrip kajian), rekonstruksi materi tematik, verifikasi dalil syar'i via OpenBayan, standardisasi 9 lapisan format, hingga peninjauan *human-in-the-loop*.
  - *Perkiraan Token AI:* ~300k - 600k token (pembuatan arsitektur state graph, perancangan prompt per node, dan integrasi API tools).
  - *Kebutuhan HITL:* Tinggi (validasi titik approval intervensi manusia sebelum naskah masuk ke repositori).
- [ ] **Migrasi Pemrosesan Dokumen ke Unstructured API ([unstructured-api](https://github.com/Unstructured-IO/unstructured-api))**
  - *Deskripsi:* Memigrasikan layer ekstraksi dan parsing dokumen multi-modal (PDF, PPTX, XLSX, DOCX, dan scan buku) dari script parser lokal ke Unstructured API (self-hosted Docker / Cloud API) untuk partisi dokumen terstruktur, ekstraksi tabel presisi tinggi, chunking semantik berbasis elemen (Title, Table, NarrativeText), serta integrasi langsung sebagai Document Loader di pipeline LangChain/LangGraph.
  - *Perkiraan Token AI:* ~150k - 300k token (pembuatan adapter API client Python, konfigurasi deployment container, transformasi skema chunking, dan pengujian perbandingan akurasi ekstraksi).
  - *Kebutuhan HITL:* Sedang (evaluasi presisi hasil partisi teks, struktur tabel, dan teks Arab berharakat pada sampel dokumen PDF modul PKN).
- [ ] **Asisten Tanya Jawab PKN (Chatbot RAG Khusus)**
  - *Deskripsi:* Fitur AI pintar pencari solusi yang menjawab pertanyaan seputar PKN berbasis dokumen dan dalil di wiki ini (*grounded QA*).
  - *Perkiraan Token AI:* ~250k - 500k token (setup chunking, embedding korpus, perumusan system prompt, dan evaluasi retrieval).
  - *Kebutuhan HITL:* Tinggi (evaluasi mitigasi halusinasi terhadap dalil dan panduan adab).
- [ ] **Otomasi Transkripsi Kajian Suara (Speech-to-Text Pipeline)**
  - *Deskripsi:* Pipeline AI (Whisper) untuk transkripsi otomatis rekaman audio kajian/halaqah menjadi draf tulisan terstruktur.
  - *Perkiraan Token AI:* ~100k - 200k token (coding pipeline Whisper + prompt pembersihan ucapan/filler words bahasa Indonesia & istilah Arab).
  - *Kebutuhan HITL:* Sedang - Tinggi (koreksi istilah-istilah Arab/fikih yang kerap keliru pada transkripsi suara).
- [ ] **Skrip Validasi Takhrij & Nomor Dalil Otomatis**
  - *Deskripsi:* Pengecekan otomatis (CI/hook) untuk validasi format nomor surah:ayat dan periwayat hadits saat artikel baru ditambahkan.
  - *Perkiraan Token AI:* ~80k - 150k token (penulisan regex validator, integrasi database surah/hadits, dan setup GitHub Action).
  - *Kebutuhan HITL:* Rendah (pengecekan false positives pada penulisan nama surah dan nomor ayat).

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
- [ ] **Peta Pohon Sanad & Silsilah Manhaj PKN**
  - *Deskripsi:* Diagram visual silsilah rujukan ilmiah dari Salafus Shalih, kitab-kitab induk tarbiyah, hingga praktisi kontemporer.
  - *Perkiraan Token AI:* ~150k - 300k token (kompilasi data riwayat rujukan keilmuan dan kodefikasi diagram grafis Mermaid/Graphviz).
  - *Kebutuhan HITL:* Sangat Tinggi (tahqiq kesahihan silsilah keilmuan oleh para masyaikh/asatidzah).
- [ ] **Fitur "Dengarkan Artikel" (Text-to-Speech) & Mode Fokus**
  - *Deskripsi:* Tombol narasi audio artikel untuk dibaca saat santai serta mode tampilan minim distraksi (fokus membaca dalil).
  - *Perkiraan Token AI:* ~40k - 80k token (integrasi Web Speech API / TTS provider dan penataan styling CSS mode fokus).
  - *Kebutuhan HITL:* Rendah (pengecekan pelafalan kata bahasa Arab dan Indonesia).

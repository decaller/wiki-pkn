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
- [x] **Pembuatan mind map untuk tiap halaman** `[SELESAI]`
  - *Deskripsi:* Menyediakan visualisasi mind map / grafik relasi konsep interaktif melalui standarisasi Obsidian Canvas (`.canvas`) berbasis plugin `@quartz-community/canvas-page` di Zone 2 Lead Section, didukung local graph view interaktif di tiap halaman.
  - *Status Kemajuan:* Selesai penuh (104 berkas Canvas terstandarisasi, transklusi `![[...canvas]]` tersemat di halaman pilar utama dan 8 ulasan buku).
  - *Kebutuhan HITL:* Rendah.
- [x] **Pembuatan visualisasi flow pengolahan (arsitektur pipeline dokumen)** `[SELESAI]`
  - *Deskripsi:* Membuat visualisasi diagram alur proses/workflow pengolahan dokumen (memetakan state graph LangGraph & LangGraph Flow mulai dari input materi multi-modal, kurasi, verifikasi dalil, hingga publikasi Quartz). Tersedia lengkap di direktori [`pipeline_designs/`](pipeline_designs/README.md) (1 master README + 10 dokumen spesifikasi pipeline tematik).
  - *Perkiraan Token AI:* ~30k - 60k token (perancangan arsitektur node dan representasi diagram Mermaid/flowchart).
  - *Kebutuhan HITL:* Sedang (penyelarasan urutan langkah kurasi bersama kurator & developer).

---

## 2. Teknis, Infrastruktur Deploy, SEO & Analitik
Fokus pada visibilitas mesin pencari, pelacakan audiens, otomatisasi monitoring container server deploy, dan riwayat pembaruan sistem.

- [x] **Peningkatan SEO (Search Engine Optimization)** `[SELESAI]`
  - *Deskripsi:* Optimasi meta description dinamis, Open Graph tags, canonical URL, sitemap XML, dan struktur heading untuk indexing optimal di search engine pada `quartz/components/Head.tsx` dan `quartz.config.yaml`.
  - *Status Kemajuan:* Selesai penuh (Konfigurasi SEO terintegrasi, meta tag dinamis dan sitemap generator aktif di Quartz).
  - *Kebutuhan HITL:* Rendah.
- [x] **Integrasi Page Analytics Menggunakan Umami ([umami.is](https://umami.is/?utm_source=coolify.io))** `[SELESAI]`
  - *Deskripsi:* Pemasangan analitik web berbasis privasi, tanpa cookie, dan ramah GDPR menggunakan Umami (didukung secara bawaan/native oleh Quartz via `{ provider: 'umami', websiteId: '...', host: '...' }`). Container Docker mandiri Umami + PostgreSQL berhasil dideploy di Portainer (Endpoint 3, Stack ID 27).
  - *Status Kemajuan:* Selesai penuh (Stack Umami aktif melayani di port 3008, konfigurasi Quartz tersambung).
  - *Kebutuhan HITL:* Rendah.
- [ ] **Instalasi & Deployment DIUN (Docker Image Update Notifier) ([crazymax.dev/diun](https://crazymax.dev/diun/?utm_source=coolify.io))**
  - *Deskripsi:* Instalasi DIUN pada environment deploy server (Coolify / Docker Host) untuk memantau pembaruan image container secara otomatis (seperti container Umami, Unstructured API, reverse proxy, dll.) dan mengirimkan notifikasi instan (via Telegram, Discord, Email, atau Webhook) ketika ada rilis image versi baru di registry Docker Hub / GitHub Container Registry.
  - *Perkiraan Token AI:* ~15k - 30k token (penyusunan konfigurasi `docker-compose.yml` / template Coolify untuk DIUN, pengaturan provider Docker socket, rules filter image, dan template webhook notifikasi).
  - *Kebutuhan HITL:* Rendah (setup kredensial bot/webhook Telegram atau Discord di server Coolify serta verifikasi penangkapan alert image).
- [x] **Pembuatan Halaman Rilis (Changelog / Release Notes)** `[SELESAI]`
  - *Deskripsi:* Menyediakan halaman khusus yang mencatat pembaruan versi, konten baru yang ditambahkan, dan log perbaikan fitur wiki di [`content/Referensi/Catatan Rilis dan Pembaruan Sistem.md`](content/Referensi/Catatan%20Rilis%20dan%20Pembaruan%20Sistem.md) (alias `/changelog`).
  - *Status Kemajuan:* Selesai penuh (Format MediaWiki 4-Zone mencakup Milestone 1 hingga 60, v1.0.0 Alpha s/d v2.5.0 Gold, terhubung di footer dan beranda).
  - *Kebutuhan HITL:* Rendah.

---

## 3. Standarisasi Bahasa, Editorial & Kualitas Penulisan
Fokus pada kejelasan kalimat, pemahaman pembaca umum, dan standardisasi istilah.

- [x] **Pengecekan tulisan menggunakan skill Clarity ([clarity.addy.ie](https://clarity.addy.ie/))** `[SELESAI]`
  - *Deskripsi:* Audit keterbacaan artikel, perbaikan kalimat berbelit (readability score), dan eliminasi ambiguitas tata bahasa via `scripts/wiki_corpus_linter.py`.
  - *Status Kemajuan:* Selesai penuh (Skor rata-rata keterbacaan korpus mencapai 86.23/100, melampaui target minimum 85.0/100).
  - *Kebutuhan HITL:* Rendah.
- [x] **Penyusunan Glosarium (Glossary) & Minimalisasi Istilah Sulit** `[SELESAI]`
  - *Deskripsi:* Membuat kamus istilah khas PKN ([`content/Glosarium Istilah Karakter Nabawiyah.md`](content/Glosarium%20Istilah%20Karakter%20Nabawiyah.md)) dengan indeks A–Z, matriks tematik, definisi syar'i-pedagogis, serta melakukan purifikasi kosakata di seluruh repositori (mengganti *etape* menjadi *fase*, *archetype* menjadi *uswah sahabat*, dll.).
  - *Status Kemajuan:* Selesai penuh (383 berkas terverifikasi, seluruh rujukan 'etape' diubah menjadi 'fase', tautan navigasi diperbarui).
  - *Kebutuhan HITL:* Rendah (telah diverifikasi sesuai diksi asli buku Ustadz Abdul Kholiq).
- [x] **Standarisasi Progressive Disclosure & Framework Diátaxis pada Generator Konten** `[SELESAI]`
  - *Deskripsi:* Menerapkan pedoman [`pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md`](pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md) pada seluruh naskah dan generator AI dengan penekanan khusus pada **Pengalaman Membaca (*Reader's Journey*) & Narasi Kohesif**.
  - *Status Kemajuan:* Selesai penuh (Struktur MediaWiki 4-Zone, Lead TL;DR `> [!SUMMARY]`, Canvas embed, dan Collapsible Raw Data tervalidasi).
  - *Kebutuhan HITL:* Rendah.
- [x] **Validasi Kepatuhan Gaya Penulisan Ustadz Abdul Kholiq (Style Compliance Audit)** `[SELESAI]`
  - *Deskripsi:* Mengimplementasikan validator otomatis pada [`scripts/wiki_corpus_linter.py`](scripts/wiki_corpus_linter.py) berbasis panduan [`pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md`](pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md) untuk memastikan kepatuhan 10 pilar pedagogis: TL;DR di awal, pengantar naratif global, bagan visual Obsidian Canvas, dalil teks Arab bersanad, syarah ulama salaf mengalir, diagnosis Tafrith vs Ifrath, pembagian 4 fase usia, protokol manhaj tadarruj, rubrik 3-level, serta muhasabah 3 pertanyaan.
  - *Status Kemajuan:* Selesai penuh (Audit linter otomatis terintegrasi dengan 0 broken link dan 0 vocabulary violation).
  - *Kebutuhan HITL:* Rendah.
- [ ] **Penerapan Mekanisme Penulisan Kepadatan Tinggi & Pembatasan Negatif (*High-Density Prompt Engineering*)**
  - *Deskripsi:* Mencegah naskah wiki terdilusi menjadi rangkuman dangkal atau kehilangan *edge cases* syar'i/teknis akibat basa-basi AI (*LLM tells*), melalui 5 aturan mekanik penulisan:
    1. **Negative Style Constraints:** Larangan mutlak pengumuman meta (*"Dalam bab ini kita akan..."*), eliminasi kata klise/sycophantic (*krusial, vital, seamless, pilar penting yang tak tergantikan*), larangan judul kesimpulan berlabel (*"Kesimpulan/Rangkuman"*), dan penegakan kalimat aktif.
    2. **Pola Scratchpad-Then-Synthesize (`<phase_1_fact_extraction>` $\to$ `<phase_2_wiki_draft>`):** Memaksa model mengekstrak seluruh parameter dalil, batasan usia, dan patologi parenting secara atomik sebelum mulai merangkai naskah artikel, lalu memverifikasi kembali bahwa tidak ada detail yang hilang saat sintesis.
    3. **Enforce High-Density Formats:** Mengganti narasi panjang bersyarat dengan *Condition $\to$ Root Cause $\to$ Exact Remediation Matrix*; menegakkan *Specification Box Rule* (paragraf dengan $\ge 3$ parameter wajib dirender sebagai tabel kunci-nilai atau callout card).
    4. **Multi-Pass "Editor" Chaining (Two-Agent Pipeline):** Memisahkan tugas *Agent 1 (Technical Drafter)* yang menjamin 100% kelengkapan fakta/dalil dari *Agent 2 (Ruthless Copy-Editor)* yang memotong 25% kata mubazir dan menegakkan kepadatan informasi maksimal.
    5. **Kalibrasi Parameter Inferensi Model:** Menyetel $T \in [0.0, 0.2]$ dan $\text{Top-P} = 0.9$ untuk presisi terminologi syar'i dan mitigasi halusinasi.
  - *Perkiraan Token AI:* ~120k - 250k token (penyusunan prompt template system, testing perbandingan few-shot negatif-positif, dan validasi output).
  - *Kebutuhan HITL:* Rendah - Sedang (evaluasi kepadatan informasi dan eliminasi kalimat bertele-tele pada draf uji coba).
- [ ] **Evaluasi Penempatan, Relokasi & Eliminasi Konten Berbasis User Journey (Placement & Pruning Engine)**
  - *Deskripsi:* Menerapkan filter arsitektur informasi pada pipeline LangGraph (lihat [`pipeline_designs/CONTENT_PLACEMENT_AND_NAVIGATION_RULES.md`](pipeline_designs/CONTENT_PLACEMENT_AND_NAVIGATION_RULES.md)) untuk mengevaluasi kecocokan penempatan materi. Mencegah *cognitive overload* dan salah sasaran audiens dengan memindahkan konten teknis/mikro (seperti tips harian, formulir/rubrik asesmen, dan studi kasus spesifik) dari gerbang makro (Home/Beranda) ke hub yang tepat (`content/Templates/`, `content/Tips/`, atau sub-halaman operasional), serta mengeliminasi konten redundan/basa-basi.
  - *Status Kemajuan:*
    - [x] Dokumen spesifikasi aturan & matriks penempatan di [`pipeline_designs/CONTENT_PLACEMENT_AND_NAVIGATION_RULES.md`](pipeline_designs/CONTENT_PLACEMENT_AND_NAVIGATION_RULES.md) `[SELESAI]`
    - [x] Penambahan `JourneyAuditor` persona pada Dewan Musyawarah Redaksi AI & `ContentPlacementAuditorNode` di [`pipeline_designs/01_pipeline_halaman_utama.md`](pipeline_designs/01_pipeline_halaman_utama.md) `[SELESAI]`
    - [x] Pembersihan & relokasi rubrik evaluasi dari Beranda ke [`content/Paradigma - Implementasi PKN/Template/Instrumen Evaluasi Kesiapan Transformasi.md`](content/Paradigma%20-%20Implementasi%20PKN/Template/Instrumen%20Evaluasi%20Kesiapan%20Transformasi.md) `[SELESAI]`
    - [ ] Integrasi otomatis validator penempatan konten pada skrip linter dan LangGraph runner
  - *Perkiraan Token AI:* ~150k - 300k token (penyusunan audit rules, evaluasi penempatan, dan migrasi terarah).
  - *Kebutuhan HITL:* Sedang (penyelarasan arsitektur navigasi dan pengalaman membaca).

---

## 4. Pengumpulan & Kurasi Konten Inti PKN
Fokus pada pemindahan khazanah materi narasumber dan konsep-konsep pokok ke dalam wiki.

- [ ] **Kurasi materi tulisan Ustadz Bayu di grup**
  - *Deskripsi:* Mengumpulkan, menyeleksi, dan menyusun arsip materi yang pernah ditulis Ustadz Bayu di grup diskusi ke format markdown wiki yang terstruktur.
  - *Perkiraan Token AI:* ~1M - 1.8M token (ekstraksi arsip pesan, clustering tema, restrukturisasi paragraf, dan formatting markdown).
  - *Kebutuhan HITL:* Tinggi (verifikasi dan otorisasi konten langsung oleh Ustadz Bayu / murid senior).
- [x] **Penyusunan Materi Tazkiyatun Nafs** `[SELESAI]`
  - *Deskripsi:* Dokumentasi konsep, tahapan, dan implementasi Tazkiyatun Nafs dalam kerangka pendidikan karakter nabawiyah ([`content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tazkiyatun Nafs.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Implementasi/Internal%20&%20Eksternal/Tazkiyatun%20Nafs.md)).
  - *Status Kemajuan:* Selesai penuh (Format 4-Zone, Lead TL;DR, Rubrik 3-Level, Muhasabah, dan embed Obsidian Canvas dua fase *Takhalli* dan *Tahalli*).
  - *Kebutuhan HITL:* Rendah.
- [x] **Konsep Pembelajaran Alamiah** `[SELESAI]`
  - *Deskripsi:* Perumusan prinsip pembelajaran alamiah berbasis fitrah belajar dan sunnatullah tumbuh kembang anak ([`content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Pembelajaran Alamiah.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Pendidikan%20Ideal/Pembelajaran%20Alamiah.md)).
  - *Status Kemajuan:* Selesai penuh (538 baris naskah terperinci, integrasi QS. An-Nahl: 78, instrumen Peristiwa vs Proyek, Rukun 3A, dan embed kanvas). Telah disematkan di Beranda Utama ([`content/index.md`](content/index.md)).
  - *Kebutuhan HITL:* Rendah.
- [x] **Tabel & Taksonomi Tafsir Bakat TB-40 (Pengganti Bab 8 Buku Utama)** `[SELESAI]`
  - *Deskripsi:* Menyusun tabel indikator, matriks karakter, dan rukun 3A Tafsir Bakat (TB-40) sebagai pengganti resmi Bab 8 Buku Utama PKN lama (menggantikan ST-30/Talents Mapping yang usang).
  - *Status Kemajuan:* Selesai penuh (40 pilar bakat di [`content/Paradigma - Implementasi PKN/.../TB40/`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Bakat/TB40/) menyerap 100% naskah Bab 12 Buku Tafsir Bakat ke format 4-Zone, serta matriks uswah sahabat di [`Bakat/index.md`](content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20&%20Implementasi/Insan/Fitrah%20(Karakter)/Bakat/index.md)).
  - *Kebutuhan HITL:* Rendah.
- [x] **Pembuatan Halaman Khusus untuk Setiap Dalil** `[SELESAI]`
  - *Deskripsi:* Membuat halaman mandiri untuk setiap dalil (Al-Qur'an dan Hadits shahih) yang memuat teks dalil Arab berharakat, nomor surah:ayat atau hadits, takhrij Maktabah Syamilah/OpenBayan, syarah ulama mu'tabar (Tafsir Ibnu Katsir, Syarah Muslim An-Nawawi, Fathul Bari Ibnu Hajar), pengayaan dalil Tazkiyatun Nafs (*Takhalli* dan *Tahalli*), serta wikilinks konsep manhaj PKN.
  - *Status Kemajuan:* Selesai penuh (80+ halaman dalil mandiri terbit di [`content/Dalil/`](content/Dalil/) dengan Action Bar, Infobox, dan Navbox terstandar).
  - *Kebutuhan HITL:* Rendah (telah divalidasi sanad dan syarah salaf-nya).
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

- [x] **Review masing-masing buku & Standarisasi Kutipan 4 Buku Utama** `[SELESAI]`
  - *Deskripsi:* Ulasan mendalam, ringkasan bab, dan relevansi masing-masing buku referensi kanonikal PKN karya Ustadz Abdul Kholiq.
  - *Status Kemajuan:* Selesai penuh (Milestone 60 & 62):
    - [x] Terbit 8 halaman ensiklopedis mandiri di [`content/Referensi/`](content/Referensi/): *Pendidikan Karakter Nabawiyah*, *Tafsir Bakat*, *Menumbuhkan Kesadaran Beramal*, *Recovery Berbasis Fitrah*, *Kurikulum Sekolah Karakter Islam*, *Panduan Implementasi Standar PKN*, *Panduan Kurikulum PAUD-TK Karakter Islam*, dan *Bukanlah Sekejap*.
    - [x] Pembersihan label kode teknis (`# ZONE 1, 2, 3, 4`) menjadi judul naratif elegan.
    - [x] Konversi peta konsep bab dari ASCII/code block menjadi 8 bagan interaktif Obsidian Canvas (`content/canvas/Review Buku/`).
    - [x] Penyematan kartu Call-to-Action (CTA) pembelian edisi cetak fisik resmi di `karakternabawiyah.com`.
    - [x] Peringkasan naskah turunan 4 buku (*Buku Utama PKN*, *Tafsir Bakat*, *Kesadaran Beramal*, *Standar Implementasi*) pada 81 berkas korpus dengan penyematan banner intisari & kutipan resmi bersanad yang menautkan ke halaman review buku.
    - [x] Resolusi tautan otomatis dalam blok HTML mentah (Infobox table & Navbox) via patch Quartz OFM regex & CrawlLinks AST visitor.
    - [x] Pembaruan atribusi hak cipta menjadi *"Pengembangan oleh Harridi Ilman Tovid - Yayasan Bina Insan Taqwa - Yayasan Bina Insan Mustaqbal"* dan identitas SOTAB HEBAT sebagai *"Sekolah Orang Tua HEBAT dari HCE (Home Character Education)"*.
  - *Kebutuhan HITL:* Rendah.
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

---

## 6. Template Siap Pakai & Toolkit KBM
Fokus pada operasional praktis bagi pendidik dan praktisi harian.

- [x] **Daftar dokumen bantuan dan review masing-masing dokumen** `[SELESAI]`
  - *Deskripsi:* Inventarisasi dokumen panduan/petunjuk teknis pembantu serta telaah kegunaannya di [`content/Toolkit KBM/index.md`](content/Toolkit%20KBM/index.md).
  - *Status Kemajuan:* Selesai penuh (Portal induk mengindeks seluruh instrumen, alur kerja 4 tahap, dan panduan pengisian).
  - *Kebutuhan HITL:* Rendah.
- [x] **Kumpulan dokumen template siap pakai** `[SELESAI]`
  - *Deskripsi:* Bank dokumen siap pakai operasional KBM di [`content/Toolkit KBM/`](content/Toolkit%20KBM/):
    1. [`Template RPP Karakter Nabawiyah 1 Lembar.md`](content/Toolkit%20KBM/Template%20RPP%20Karakter%20Nabawiyah%201%20Lembar.md) (Iman, Adab, Ilmu & 3 Bahasa).
    2. [`Instrumen Observasi Pertumbuhan Karakter 19 Butir.md`](content/Toolkit%20KBM/Instrumen%20Observasi%20Pertumbuhan%20Karakter%2019%20Butir.md) (Rubrik non-angka BT, MT, BK, MM).
    3. [`Formulir Desain Proyek Pembelajaran Alamiah.md`](content/Toolkit%20KBM/Formulir%20Desain%20Proyek%20Pembelajaran%20Alamiah.md) (Sains & Adab Berbasis Peristiwa).
    4. [`Lembar Dialog Evaluasi Hati Guru-Santri.md`](content/Toolkit%20KBM/Lembar%20Dialog%20Evaluasi%20Hati%20Guru-Santri.md) (Protokol 4 Langkah Pemulihan Adab).
  - *Status Kemajuan:* Selesai penuh (Format markdown bersih siap salin/cetak, bebas angka mati pada adab).
  - *Kebutuhan HITL:* Rendah.
- [x] **Prompt AI dan template pembuatan dokumen KBM** `[SELESAI]`
  - *Deskripsi:* Penyusunan sistem prompt AI siap pakai bagi guru di [`content/Toolkit KBM/Bank Prompt AI Guru KBM.md`](content/Toolkit%20KBM/Bank%20Prompt%20AI%20Guru%20KBM.md) memuat 5 paket prompt XML tags (`<role>`, `<context>`, `<rules>`, `<output_format>`) untuk sirah nabawiyah, proyek fitrah, lembar muhasabah, dan studi kasus.
  - *Status Kemajuan:* Selesai penuh (Dilengkapi few-shot examples dan tips kalibrasi guru).
  - *Kebutuhan HITL:* Rendah.
- [x] **Kumpulan tips and trik problematika harian** `[SELESAI]`
  - *Deskripsi:* Panduan solusi praktis atas kendala harian guru/orang tua dalam menghadapi dinamika perilaku santri via protokol rekonsiliasi hati dan penanganan krisis adab di [`content/Toolkit KBM/Lembar Dialog Evaluasi Hati Guru-Santri.md`](content/Toolkit%20KBM/Lembar%20Dialog%20Evaluasi%20Hati%20Guru-Santri.md).
  - *Status Kemajuan:* Selesai penuh (Protokol 4 langkah tanpa kekerasan verbal/fisik, menjaga fitrah kemuliaan anak).
  - *Kebutuhan HITL:* Rendah.

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
- [x] **Adopsi Struktur Standar Industri 4 Zona MediaWiki pada Seluruh Template Wiki** `[SELESAI]`
  - *Deskripsi:* Mengintegrasikan 4 zona fungsional standar MediaWiki ke dalam sistem Wiki PKN (Quartz v5):
    1. **Zona 1 (Header dan Kontrol Halaman):** Judul artikel (H1/URL slug), tab aksi dokumen (baca/diskusi Giscus/riwayat Git/edit sumber), dan toolbar (search, reader mode, dark mode).
    2. **Zona 2 (Area Konten Utama & Infobox):** Paragraf pembuka (*Lead Section*) dengan TL;DR `> [!SUMMARY]`, Infobox vertikal kanan (`.wiki-infobox`) untuk parameter cepat, Table of Contents otomatis, dan Batang Tubuh Naratif (H2/H3, Obsidian Canvas, Syarah, Tafrith vs Ifrath, Instrumen Terapan).
    3. **Zona 3 (Lampiran & Verifikasi Sumber):** Sub-bab "Lihat Pula" (internal cross-links), "Referensi dan Catatan Kaki" dengan rujukan superskrip `[^1]` dan takhrij Shamela/OpenBayan, `<details>` collapsible untuk raw data/evolusi manhaj, serta "Bacaan Lanjutan dan Pranala Luar".
    4. **Zona 4 (Metadata & Taksonomi Bawah):** Kotak navigasi horizontal (`.wiki-navbox`), kategori dokumen (`[[Kategori:...]]`), tautan mu'jam istilah Arab, dan footer hak cipta/lisensi terbuka.
    5. **Dukungan SCSS & Linter:** Menambahkan styling CSS responsive `.wiki-infobox` & `.wiki-navbox` pada `quartz/styles/custom.scss` serta rule audit kepatuhan di `scripts/wiki_linter.py`.
  - *Status Kemajuan:*
    - [x] Panduan arsitektur & template master di [`pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md`](pipeline_designs/DIATAXIS_PROGRESSIVE_DISCLOSURE.md) `[SELESAI]`
    - [x] Spesifikasi pipeline fokus tema di [`pipeline_designs/03_pipeline_halaman_fokus_satu_tema.md`](pipeline_designs/03_pipeline_halaman_fokus_satu_tema.md) `[SELESAI]`
    - [x] Parameter audit kepatuhan di [`pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md`](pipeline_designs/USTADZ_ABDUL_KHOLIQ_STYLE_GUIDE.md) & [`scripts/wiki_linter.py`](scripts/wiki_linter.py) `[SELESAI]`
    - [x] Styling CSS responsive di [`quartz/styles/custom.scss`](quartz/styles/custom.scss) `[SELESAI]`
  - *Perkiraan Token AI:* ~40k - 80k token.
  - *Kebutuhan HITL:* Rendah.
- [x] **Standarisasi Templat Halaman Khusus Non-Penjelasan (MediaWiki Technical Namespaces)** `[SELESAI]`
  - *Deskripsi:* Merancang 8 templat khusus pembeda untuk halaman non-penjelasan sesuai arsitektur MediaWiki:
    1. **Halaman Disambiguasi:** Format pemilah istilah multitafsir berikon `🔀` dengan navigasi pembeda cepat tanpa uraian panjang.
    2. **Halaman Pengalihan (Redirect):** Stub rujukan dan pemetaan `aliases` frontmatter untuk variasi sinonim/ejaan lama.
    3. **Halaman Daftar Terstruktur:** Matriks data padat tabel (TB-40 40 karakter, indeks hadits, direktori sekolah mitra) dengan statistik agregat.
    4. **Portal Tematik:** Hub kurasi modular berbasis grid kartu untuk pintu masuk rumpun keilmuan besar (Insan, Metode, Praktik, Parenting).
    5. **Halaman Proyek & Kebijakan (Namespace `Wiki-PKN:`):** Standar tata kelola, aturan redaksi, konsensus dewan, dan batasan HITL.
    6. **Templat Pemeliharaan (Noticebox):** Box evaluasi modular di atas artikel (butuh takhrij `⚠️`, konsep terdahulu/superseded `🕰️`, artikel rintisan/stub `🌱`).
    7. **Halaman Berkas / Media:** Dokumentasi metadata aset banner, diagram canvas, dan audio rekaman.
    8. **Halaman Profil Pengguna / Kontributor:** Biodata asatidzah/guru praktisi + ruang *sandbox* (bak pasir) draf pribadi.
    9. **Komponen CSS:** Dukungan styling `.wiki-noticebox` dan `.wiki-portal-*` di `quartz/styles/custom.scss`.
  - *Status Kemajuan:*
    - [x] Dokumen spesifikasi di [`pipeline_designs/SPECIAL_PAGE_TEMPLATES.md`](pipeline_designs/SPECIAL_PAGE_TEMPLATES.md) `[SELESAI]`
    - [x] Komponen styling CSS di [`quartz/styles/custom.scss`](quartz/styles/custom.scss) `[SELESAI]`
    - [x] Referensi indeks di [`pipeline_designs/README.md`](pipeline_designs/README.md) `[SELESAI]`
  - *Perkiraan Token AI:* ~35k - 70k token.
  - *Kebutuhan HITL:* Rendah.
- [x] **Pengarsipan & Pemosisian Kanonikal Buku Tafsir Bakat Master (Karya Terpenting Kedua)** `[SELESAI]`
  - *Deskripsi:* Mengarsipkan naskah master lengkap *Buku Tafsir Bakat (Edit 31)* karya Ustadz Abdul Kholiq dari `/home/abuhafi/Downloads/` ke `sources/buku_tafsir_bakat/` (118.464 kata, 871.135 karakter, 4.440 paragraf mencakup Bab 1–12 lengkap):
    1. **Penetapan Otoritas Tier 1 (Active Truth):** Diposisikan tepat setelah Buku Utama PKN sebagai buku babon kedua rujukan taksonomi 40 karakter, silsilah akhlak, profesi peradaban, dan terapi ilaj nabawi.
    2. **Penggantian Total (*Full Supersedes*):** Menegaskan status bahwa naskah ini menggantikan secara utuh Bab 8 Buku Utama PKN terdahulu (ST-30 / Talents Mapping) pada `data/sources_registry.csv` dan `pipeline_designs/05_pipeline_halaman_bakat.md`.
    3. **Parser & Ingestion Engine (`scripts/ingest_tafsir_bakat_book.py`):** Mengekstrak seluruh bab dan 40 pilar ke format JSON terstruktur (`data/buku_tafsir_bakat_extracted.json`) siap diproses ke naskah wiki Quartz.
  - *Status Kemajuan:*
    - [x] Berkas arsip di [`sources/buku_tafsir_bakat/`](sources/buku_tafsir_bakat/) `[SELESAI]`
    - [x] Pendaftaran presedensi di [`data/sources_registry.csv`](data/sources_registry.csv) `[SELESAI]`
    - [x] Ingestion parser di [`scripts/ingest_tafsir_bakat_book.py`](scripts/ingest_tafsir_bakat_book.py) `[SELESAI]`
    - [x] Basis data ekstraksi di [`data/buku_tafsir_bakat_extracted.json`](data/buku_tafsir_bakat_extracted.json) `[SELESAI]`
  - *Perkiraan Token AI:* ~40k - 80k token.
  - *Kebutuhan HITL:* Rendah.
- [x] **Kodifikasi Penuh Folder 'Arsitektur PKN' & Integrasi 6 Sektor Makro PKN** `[SELESAI]`
  - *Deskripsi:* Menyusun 7 artikel ensiklopedis di `content/Arsitektur PKN/` yang berpasangan 1-to-1 dengan kanvas arsitektur (`00` s.d `06`), menerapkan standar 4-Zone MediaWiki (Action Bar, Infobox, Lead TL;DR, Canvas Embed, Syarah, Navbox, Takhrij), dan lolos audit linter (skor 90/100) serta verifikasi `npx quartz build` exit code 0.
  - *Status Kemajuan:*
    - [x] 7 file Markdown di [`content/Arsitektur PKN/`](content/Arsitektur%20PKN/) `[SELESAI]`
    - [x] Styling Action Bar `.wiki-action-bar` di [`quartz/styles/custom.scss`](quartz/styles/custom.scss) `[SELESAI]`
    - [x] Pemutakhiran [`content/Peta Navigasi Wiki PKN.md`](content/Peta%20Navigasi%20Wiki%20PKN.md) `[SELESAI]`
    - [x] Kompilasi bersih Quartz v5 & sinkronisasi Git `[SELESAI]`
  - *Perkiraan Token AI:* ~60k - 100k token.
  - *Kebutuhan HITL:* Rendah.
- [x] **Integrasi Komprehensif 40 Pilar Bakat Fitrah TB-40 dari Buku Tafsir Bakat ke 4-Zone MediaWiki** `[SELESAI]`
  - *Deskripsi:* Mengembangkan engine `scripts/enrich_tb40_with_book.py` untuk menyerap seluruh naskah master *Buku Tafsir Bakat* Bab 12 (40 pilar, 9 aspek komprehensif) ke dalam 40 artikel di `content/Paradigma - Implementasi PKN/.../TB40/`. Seluruh artikel mematuhi arsitektur MediaWiki 4-Zone, Progressive Disclosure, dan mencapai rata-rata skor linter 90.0/100.
  - *Status Kemajuan:*
    - [x] Engine integrasi di [`scripts/enrich_tb40_with_book.py`](scripts/enrich_tb40_with_book.py) `[SELESAI]`
    - [x] 40 file Markdown TB-40 ter-upgrade 100% `[SELESAI]`
    - [x] Verifikasi build Quartz v5 (2.148 files emitted) & sinkronisasi Git `[SELESAI]`
  - *Perkiraan Token AI:* ~80k - 150k token.
  - *Kebutuhan HITL:* Rendah.
- [x] **Transformasi Komprehensif Seluruh Konten Repositori ke 4-Zone MediaWiki (382 Berkas)** `[SELESAI]`
  - *Deskripsi:* Menyelesaikan seluruh batch transformasi repositori (71 artikel Core Manhaj Paradigma, 121 artikel buletin parenting Materi SOTAB, dan 122 artikel Kajian Video) ke arsitektur MediaWiki 4-Zone, menambahkan Action Bar, Infobox terstruktur, Lead TL;DR, Canvas Embed, Protokol EMISOL, dan Navbox.
  - *Status Kemajuan:*
    - [x] 71 Berkas Core Manhaj di [`content/Paradigma - Implementasi PKN/`](content/Paradigma%20-%20Implementasi%20PKN/) `[SELESAI]`
    - [x] 121 Berkas Studi Kasus di [`content/Materi SOTAB/`](content/Materi%20SOTAB/) `[SELESAI]`
    - [x] 122 Berkas Media di [`content/Kajian Video/`](content/Kajian%20Video/) `[SELESAI]`
    - [x] Penyelarasan alias kunci & perbaikan index.md `[SELESAI]`
    - [x] Verifikasi build Quartz v5 (2.157 files emitted, exit code 0) & sinkronisasi Git `[SELESAI]`
  - *Perkiraan Token AI:* ~120k - 200k token.
  - *Kebutuhan HITL:* Rendah.
- [x] **Glosarium Resmi PKN & Purifikasi Kosakata Autentik Sumber (383 Berkas)** `[SELESAI]`
  - *Deskripsi:* Menerbitkan master Glosarium Istilah Karakter Nabawiyah ([`content/Glosarium Istilah Karakter Nabawiyah.md`](content/Glosarium%20Istilah%20Karakter%20Nabawiyah.md)) dengan indeks A–Z, matriks tematik 6 klaster, definisi syar'i-pedagogis, serta melakukan purifikasi 630+ kemunculan kosakata asing/tidak bersumber di seluruh repositori (mengganti *etape* menjadi *fase*, *archetype* menjadi *uswah sahabat*, dan merename 4 kanvas fase usia).
  - *Status Kemajuan:* Selesai penuh (383 berkas terverifikasi, Quartz build sukses dengan 2.172 file statis, Portainer live HTTP/2 200 OK).
  - *Perkiraan Token AI:* ~60k - 100k token.
  - *Kebutuhan HITL:* Rendah.
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
- [ ] **Integrasi Model Context Protocol (MCP) Servers untuk Riset Akademik & Verifikasi Ilmiah**
  - *Deskripsi:* Mengonfigurasi dan menghubungkan rangkaian MCP Server akademik ke agen AI dan pipeline riset lokal untuk penelusuran literatur empiris bebas halusinasi (sesuai rincian [`pipeline_designs/EVIDENCE_BASED_RESEARCH_WORKFLOW.md`](pipeline_designs/EVIDENCE_BASED_RESEARCH_WORKFLOW.md)):
    1. **PubMed / NCBI MCP Server:** Akses native ke kueri MeSH MEDLINE/PubMed dan PMC full-text XML untuk verifikasi data fisiologis, tumbuh kembang, dan neurosains anak.
    2. **Semantic Scholar MCP Server:** Pengambilan graf sitasi otomatis, pelacakan *influential citations*, dan ringkasan intensi sitasi berdasarkan DOI.
    3. **Zotero Local MCP Server:** Integrasi LLM langsung ke database SQLite Zotero lokal dan repository PDF riset untuk kueri semantik presisi tinggi.
    4. **Fetch / Puppeteer Markdown Scraper MCP:** Ekstraksi paper preprint (arXiv, bioRxiv) dan basis data terbuka langsung ke Markdown bersih tanpa boilerplate web.
  - *Perkiraan Token AI:* ~60k - 120k token (konfigurasi MCP server configs, pembuatan prompt adapter/tools untuk agen AI, dan pengetesan kueri literatur).
  - *Kebutuhan HITL:* Rendah (pengujian fungsional tool calling dan verifikasi integritas data yang ditarik).

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


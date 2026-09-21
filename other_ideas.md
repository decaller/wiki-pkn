# Ide-Ide Eksplorasi & Fitur Masa Depan (Other Ideas)

Dokumen ini memuat daftar ide, modul eksplorasi, dan rencana fitur pelengkap yang dipindahkan dari `TODO.md` utama agar fokus pengerjaan saat ini tetap terpusat pada **nilai inti (*core value*) Wiki-PKN**: kompilasi manhaj tarbiyah, pemetaan 4 etape usia nabawiyah, verifikasi dalil shahih, digitalisasi 122 video kajian Ustadz Abdul Kholiq, dan toolkit terapan KBM.

Fitur-fitur di bawah ini tetap didokumentasikan dengan baik dan dapat diaktifkan kembali pada fase pengembangan berikutnya (*Post-Launch / Tahap 2*).

---

## 1. Navigasi & Visualisasi Alternatif

- **Integrasi Obsidian Canvas (`.canvas`) ke Tampilan Web Interaktif**
  - *Deskripsi:* Memvisualisasikan berkas `.canvas` di peramban secara interaktif dengan kemampuan zoom dan panning untuk memetakan keterkaitan konsep PKN.
  - *Catatan Evaluasi:* Saat ini Quartz v5 sudah memiliki *native Graph View* bawaan dan folder `content_flow/` menyediakan diagram alur Mermaid yang jauh lebih ringan, semantik, serta responsif di perangkat mobile.
  - *Estimasi Token AI:* ~50k - 100k token.
  - *Kebutuhan HITL:* Rendah.

---

## 2. Multimedia & Distribusi Tambahan

- **Viewer Presentasi Interaktif di Web (Slide Deck Viewer via Reveal.js)**
  - *Deskripsi:* Mengonversi berkas materi di folder `presentations/` menjadi slide web interaktif berbasis Reveal.js yang dapat dipresentasikan langsung di kelas.
  - *Catatan Evaluasi:* Konversi setiap presentasi menjadi slide web terpisah memecah fokus pembaca wiki. Poin inti presentasi saat ini sudah dipartisi langsung via Unstructured API ke dalam naskah Diátaxis. Kebutuhan guru lebih condong ke format ringkas 1 lembar (Infografis/PDF rangkuman) atau berkas PPTX asli.
  - *Estimasi Token AI:* ~150k - 300k token.
  - *Kebutuhan HITL:* Sedang.

- **Fitur "Dengarkan Artikel" (Text-to-Speech Web) & Mode Fokus**
  - *Deskripsi:* Tombol narasi audio artikel sintetis untuk dibaca saat santai serta mode tampilan minim distraksi (fokus membaca dalil).
  - *Catatan Evaluasi:* Engine TTS browser umum (Web Speech API) kerap salah melafalkan harakat teks Arab dan istilah fiqih tarbiyah. Wiki-PKN sudah memiliki rekaman suara dan video otentik Ustadz Abdul Kholiq (122 video kajian, 1.159 bab di `pkn.db`) yang jauh lebih berwibawa dan menyentuh hati (*lisanul qalb*).
  - *Estimasi Token AI:* ~40k - 80k token.
  - *Kebutuhan HITL:* Rendah.

---

## 3. Riset Historis & Silsilah Manhaj

- **Peta Pohon Sanad & Silsilah Manhaj PKN**
  - *Deskripsi:* Diagram visual silsilah rujukan ilmiah dari Salafus Shalih, kitab-kitab induk tarbiyah (Imam An-Nawawi, Ibnul Qayyim, Al-Ghazali), hingga praktisi kontemporer.
  - *Catatan Evaluasi:* Memerlukan riset turats dan tahqiq sanad keilmuan yang sangat mendalam dari dewan masyaikh/asatidzah senior (HITL: Sangat Tinggi) dan rentan perdebatan metodologis jika tidak divalidasi tuntas. Ditunda hingga buku-buku induk fisik tiba dan diverifikasi langsung oleh asatidzah.
  - *Estimasi Token AI:* ~150k - 300k token.
  - *Kebutuhan HITL:* Sangat Tinggi.

---

## 4. Eksplorasi Alternatif Static Site Generator (SSG)

- **Benchmarking Starlight (Astro) & Material for MkDocs**
  - *Deskripsi:* Pengujian sandbox terhadap rendering direktori `content/` pada engine Starlight (Astro) untuk pencarian Pagefind atau MkDocs Material untuk fitur tab dan callout teknis.
  - *Catatan Evaluasi:* Quartz v5 saat ini sudah sangat stabil, mendukung SPA routing cepat, backlink explorer, popover hover preview, dan native graph view. Mengganti SSG saat ini akan membuang waktu penataan CSS responsif yang sudah berjalan.
  - *Estimasi Token AI:* ~20k - 40k token.
  - *Kebutuhan HITL:* Rendah.

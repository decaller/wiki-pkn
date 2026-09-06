---
title: "Tentang Aplikasi Wiki PKN"
description: "Dokumentasi teknis lengkap platform Wiki Pendidikan Karakter Nabawiyah (wikipkn.insanmustaqbal.or.id): sumber data, metodologi pengolahan, teknologi, plugin navigasi kustom, dan infrastruktur deployment."
aliases:
  - Tentang Wiki
  - About
  - Metodologi
  - Teknologi
tags:
  - referensi
  - metodologi
  - teknologi
  - openbayan
  - quartz
---

![[assets/banners/banner_blueprint_arsitektur.webp]]
*Gambar: Arsitektur Digital & Ekosistem Platform Wiki Pendidikan Karakter Nabawiyah*

# Tentang Aplikasi Wiki PKN

> [!note] Catatan Metodologi & Sumber Penyusunan Dokumen
> Dokumen ini merupakan hasil rangkuman dan rekonstruksi berbantuan kecerdasan buatan (AI) dari berbagai materi presentasi, modul kurikulum, dokumen standar lembaga, dan rekaman kajian **Pendidikan Karakter Nabawiyah (PKN)** yang diampu oleh **Ustadz Abdul Kholiq**.
>
> Naskah ini telah melalui verifikasi dan pengayaan ulang dalil-dalil Al-Qur'an dan Hadits shahih dari korpus **OpenBayan** (seluruh dataset **Maktabah Syamilah**), serta diperkaya dengan sintesis intisari dan masukan berharga dari kawan-kawan **Himmatul Ummah**, **Insan Taqwa / Mustaqbal**, dan **Tim SOTAB HEBAT**.

Halaman ini mendokumentasikan secara teknis dan metodologis **seluruh aspek pembangunan dan pengoperasian** platform basis pengetahuan **Wiki Pendidikan Karakter Nabawiyah** yang dapat diakses publik di:

> 🌐 **[https://wikipkn.insanmustaqbal.or.id](https://wikipkn.insanmustaqbal.or.id)**

---

## 1. Identitas & Tujuan Platform

| Atribut | Detail |
| :--- | :--- |
| **Nama Resmi** | Wiki Pendidikan Karakter Nabawiyah (Wiki PKN) |
| **URL Produksi** | [https://wikipkn.insanmustaqbal.or.id](https://wikipkn.insanmustaqbal.or.id) |
| **Repositori Git** | [github.com/decaller/wiki-pkn](https://github.com/decaller/wiki-pkn) |
| **Platform Dasar** | Quartz v5 (Static Site Generator berbasis Obsidian) |
| **Bahasa Konten** | Bahasa Indonesia + Arab (teks berharakat penuh) |
| **Total Artikel** | 123 berkas Markdown (100% standar emas ≥ 5.000 karakter) |
| **Total Karakter** | > 1.000.000 karakter konten ensiklopedia |
| **Domain Organisasi** | [insanmustaqbal.or.id](https://insanmustaqbal.or.id) — Yayasan Bina Insan Mustaqbal |

**Tujuan utama:** Menjadi basis pengetahuan digital terbuka dan komprehensif yang merekonstruksi paradigma, kurikulum, metodologi, dan tata kelola implementasi pengasuhan generasi Islam berdasarkan sunnah Rasulullah ﷺ dan manhaj Pendidikan Karakter Nabawiyah.

---

## 2. Sumber Data: Dari Mana Konten Diambil

### A. Materi Primer — Karya Resmi Ustadz Abdul Kholiq & Tim

Seluruh konten ensiklopedia bersumber dari karya otoritatif **perumus manhaj PKN**, Ustadz Abdul Kholiq (Yayasan Bina Insan Mustaqbal / SOTAB HEBAT):

| # | Sumber | Jenis | Cakupan |
| :-: | :--- | :--- | :--- |
| 1 | **8 Buku Cetak Resmi** | Buku terbit | Epistemologi PKN, Tafsir Bakat TB40, Recovery, Kurikulum, Implementasi Standar, Maqashid Syariah |
| 2 | **145 Berkas Presentasi** (86 PDF + 59 PPTX) | Slide pelatihan | Semua materi Akademi Guru Batch 3–5, Temu Lembaga Batch 4–6, Seminar Tafsir Bakat |
| 3 | **122 Video Ceramah YouTube** (1.159 bab) | Rekaman kajian | Ceramah Ustadz Abdul Kholiq tersimpan di basis data `pkn.db` (SQLite + vector index) |
| 4 | **Manual Standar Implementasi PKN 11-2024 (81 hal)** | Dokumen resmi | Klausul 5–13, Standar Pendewasaan, Matriks Recovery 4 Kondisi |
| 5 | **9 Spreadsheet Asesmen TB-40** (.xlsx) | Data instrumen | Peta Karir Peradaban 40 Pilar, Form Observasi, Blueprint Rapor Santri SKIS |

### B. Khazanah Web & Artikel Online

| Sumber | Crawler | Jumlah | Isi |
| :--- | :--- | :-: | :--- |
| **SOTAB HEBAT** (`sotabh.com/artikel/`) | `fetch_sotabh_articles.py` | 117 artikel | Esai kurikuler, studi kasus pengasuhan, risalah fitrah |
| **Sekolah Karakter Imam Syafi'i** (`sekolahkarakter.com`) | `fetch_skis_articles.py` | 172 halaman | Artikel blog, profil lembaga, filosofi kurikulum SKIS Semarang |
| **Portal Resmi PKN** (`karakternabawiyah.com`) | `fetch_pkn_portal.py` | 60+ berkas | Artikel ilmiah, katalog event (AKG, PIS, TDK, TC), profil buku |
| **GitHub Repositories** | `crawl_github_repos.py` | 69 repositori | 15 repo Yayasan YBIM + 54 repo decaller (ekosistem digital PKN) |

### C. Korpus Dalil & Turats Islam Klasik

| Sumber | Akses | Cakupan |
| :--- | :--- | :--- |
| **OpenBayan** (seluruh dataset Maktabah Syamilah) | API + portal `openbayan.insanmustaqbal.or.id` | Ribuan kitab turats: Tafsir, Hadits Kutubus Sittah + syarah, Fiqih salaf |
| **Qaf AI SDK** | Python wrapper `qaf_wrapper` | 320+ rujukan maraji' (Ibnul Qayyim, Al-Ghazali, Ibnu Hajar, An-Nawawi) |
| **Kitab Ashabur Rasul SAW** (Syaikh Mahmud Al-Mishri, 543 hal) | PDF `old_backup/Campur/` | Sirah 40 sahabat — Archetype Matrix TB-40 |
| **Seminar 1: Kondisi Jiwa Anak** (119 hal) | PDF `old_backup/` | Psikospiritual jiwa, shalat barometer, bahasa hati vs akal |
| **Seminar 2: Tafsir Bakat TB-40** (196 hal) | PDF `old_backup/` | Teologi bakat, syarat dawam, rukun 3A |
| **Kajian Pendidikan Lestari** Prof. Dr. Iman Harymawan (77 hal) | PDF `old_backup/` | Peran guru nabawiyah, syabab, benang merah pendidikan |

### D. Aset Visual

| Sumber | Proses | Output |
| :--- | :--- | :--- |
| **Foto Dokumentasi PKN** (40 foto, `old_backup/Gambar/`) | Crop 1050×350px WebP via PIL | Banner horizontal artikel |
| **Pexels API** (via MCP Server) | Filter compliance syariat, crop WebP | Banner visual masjid, alam, ilmu |
| **PDF Slide Presentasi Resmi** | `pdftoppm` + PIL export ke WebP | 29 slide diagram berharga di `content/assets/slides/` |
| **Foto Uzungöl Mosque** (Rüveyda Akkaya / Pexels) | Crop 1920×800px WebP | Cover header beranda utama |

---

## 3. Metodologi Pengolahan & Rekonstruksi Konten

### A. Prinsip Rekonstruksi Berbantuan AI

Seluruh naskah wiki dihasilkan melalui **pipeline rekonstruksi berbantuan AI** dengan prinsip:

1. **Ekstraksi Multi-Modal**: Membaca PDF, PPTX, XLSX, audio transkrip, artikel web, dan kitab Arab secara simultan.
2. **Sintesis Tematik**: AI (Gemini 2.5 Flash/Pro + Claude Sonnet) merangkum, menyusun ulang, dan mengintegrasikan materi dari berbagai sumber ke dalam satu naskah kohesif per topik.
3. **Verifikasi Dalil**: Setiap dalil dicocokkan dengan korpus OpenBayan (Maktabah Syamilah) untuk memastikan teks Arab berharakat, takhrij, dan syarah yang akurat.
4. **Zero Deletion**: Setiap iterasi pengayaan bersifat **additive** — tidak ada satu pun teks, dalil, atau konten yang dihapus dari versi sebelumnya.

### B. Pipeline Pemrosesan Data

```
SUMBER DATA (PDF/PPTX/XLSX/Video/Web)
        ↓
 EKSTRAKSI & PARSING
 (Python: pdfplumber, python-pptx, openpyxl,
  BeautifulSoup, yt-dlp/whisper transkrip)
        ↓
 REKONSTRUKSI AI
 (Gemini 2.5 Flash Pro / Claude Sonnet 4.6 via IDE Antigravity)
  → Sintesis konsep, penulisan naskah, struktur tabel
  → Verifikasi dalil dengan OpenBayan API
  → Injeksi dalil Arab berharakat + terjemahan + takhrij
        ↓
 STANDARISASI FORMAT
 (9 Lapisan Anatomi Baku sesuai Template Resmi):
  1. Frontmatter YAML (title, description, tags, aliases)
  2. Banner Visual Header (WebP 1050×350px)
  3. Catatan Metodologi & Rekonstruksi AI ([!note])
  4. Judul Utama (#) & Paragraf Konseptual
  5. Dalil Syar'i Pokok & Takhrij OpenBayan ([!quote])
  6. Batang Tubuh Materi (##, tabel matriks, Obsidian Canvas)
  7. Trio Callout Refleksi ([!info], [!warning], [!tip])
  8. Sitasi Rujukan Resmi ([!quote] Dokumen PPT)
  9. Media Presentasi Office Web Apps (MUTLAK PALING AKHIR)
        ↓
 AUDIT & VALIDASI
 (standar emas ≥ 5.000 karakter, 0 broken links)
        ↓
 BUILD QUARTZ v5
 (npx quartz build → public/ statis)
```

### C. Standar Emas Konten

Setiap artikel harus memenuhi ambang batas kualitas minimum:

| Kriteria | Standar |
| :--- | :--- |
| Panjang minimal | ≥ 5.000 karakter per halaman |
| Teks Arab | Berharakat penuh (*rasm utsmani*) |
| Dalil | Disertai takhrij lengkap (kitab, bab, nomor) |
| Syarah | Merujuk kitab mu'tabar (Fathul Bari, Syarah Muslim) |
| Link OpenBayan | Tombol 🔍 pada setiap callout dalil |
| Visualisasi | Obsidian Canvas (bukan Mermaid) |
| Refleksi | Trio callout lapangan di akhir konten |
| Presentasi | Embed OneDrive Office Web Apps |

---

## 4. Teknologi & Stack Teknis

### A. Platform Utama

| Komponen | Teknologi | Versi/Detail |
| :--- | :--- | :--- |
| **Static Site Generator** | [Quartz v5](https://quartz.jzhao.xyz/) | v5.0.0 — berbasis TypeScript/React |
| **Format Konten** | Markdown + Obsidian Flavored Markdown | WikiLinks `[[...]]`, Callouts, Canvas |
| **Diagram Visual** | Obsidian Canvas (JSON Canvas 1.0) | 96 berkas `.canvas` aktif, 0 Mermaid |
| **Pencarian** | Quartz Full-Text Search (FlexSearch) | Client-side, tanpa backend |
| **Komentar** | Giscus (GitHub Discussions) | Repositori `decaller/wiki-pkn` |
| **Sitasi Akademik** | BibTeX `bibliography.bib` + Quartz Citations | Format APA/IEEE |

### B. Plugin Quartz yang Diaktifkan

```yaml
# quartz.config.yaml — plugin aktif
plugins:
  transformers:
    - ObsidianFlavoredMarkdown    # WikiLinks, Callouts, Canvas
    - GitHubFlavoredMarkdown      # Tables, Strikethrough
    - CrawlLinks                  # resolusi [[wikilink]] ke path
    - Citations                   # BibTeX citation rendering
    - HardLineBreaks
    - TableOfContents             # TOC otomatis
    - Latex                       # LaTeX math rendering

  filters:
    - RemoveDrafts

  emitters:
    - ContentPage                 # halaman artikel HTML
    - FolderPage                  # halaman folder/index
    - TagPage                     # halaman per-tag
    - ContentIndex                # JSON index pencarian
    - AliasRedirects              # alias URL
    - Static                      # aset statis
    - ComponentResources          # CSS/JS komponen
    - CNAME                       # domain custom
    - SitemapPage                 # sitemap.xml SEO
    - RSSFeedPage                 # RSS feed

components:
  # Komponen UI aktif
  - DesktopOnly: OutlineNav      # navigasi sidebar KUSTOM
  - Search                       # pencarian fulltext
  - Darkmode                     # toggle tema gelap/terang
  - TagList                      # daftar tag per artikel
  - Graph                        # knowledge graph interaktif
  - Backlinks                    # backlink antar artikel
  - TableOfContents              # TOC kanan
  - RecentNotes                  # (khusus beranda index)
  - Comments (Giscus)            # komentar GitHub Discussions
  - Footer                       # footer kustom
```

### C. Plugin Navigasi Kustom `OutlineNav`

Komponen utama yang membedakan Wiki PKN dari wiki Quartz biasa adalah plugin sidebar navigasi kustom bernama **`OutlineNav`**, menggantikan komponen default `Explorer` bawaan Quartz.

**Lokasi:** [`plugins/outline-nav/src/components/OutlineNav.tsx`](https://github.com/decaller/wiki-pkn/blob/main/plugins/outline-nav/src/components/OutlineNav.tsx)

**Cara Kerja:**
1. Membaca struktur hierarki navigasi dari [`nav_structure.json`](https://github.com/decaller/wiki-pkn/blob/main/nav_structure.json) (49 simpul navigasi terstruktur).
2. Merender sidebar navigasi sebagai pohon hierarki yang dapat dilipat/dibuka (*collapsible tree*).
3. Mendeteksi halaman aktif secara otomatis berdasarkan URL saat ini.

**Fitur Unggulan:**
| Fitur | Implementasi Teknis |
| :--- | :--- |
| **Inside Scrolling** | `overflow-y: auto; overscroll-behavior: contain; max-height: calc(100vh - 12rem)` |
| **Scrollbar Ramping** | CSS custom scrollbar styling (webkit) |
| **Active Link Detection** | `a.internal.active` — deteksi URL aktif |
| **Auto-Expand Parent** | Buka otomatis folder induk halaman aktif saat navigasi |
| **Scroll State Persistence** | `sessionStorage` — simpan posisi scroll antar-halaman (PJAX) |
| **Collapse/Expand State** | `localStorage` — ingat status lipatan per folder antar-sesi |

**Konfigurasi `nav_structure.json`:**
```json
{
  "label": "Wiki PKN",
  "children": [
    {
      "label": "Insan",
      "path": "/Paradigma - Implementasi PKN/.../Insan/",
      "children": [
        { "label": "Tujuan Hidup Manusia", "path": "..." },
        { "label": "Pembagian Jiwa", "path": "..." }
      ]
    }
  ]
}
```

**Build Plugin:**
```bash
cd plugins/outline-nav
npm run build   # kompilasi TypeScript → JavaScript bundle
cd ../..
npx quartz build
```

### D. Integrasi OpenBayan

Platform **OpenBayan** (terintegrasi penuh dengan seluruh dataset **Maktabah Syamilah**) digunakan dalam dua cara:

1. **Fase Pengembangan** — Verifikasi teks Arab, takhrij hadits, dan pencarian dalil tematik via API OpenBayan selama proses rekonstruksi konten.
2. **Fase Produksi** — Setiap callout dalil dalam wiki memiliki tombol **🔍 Telusuri di OpenBayan** yang diarahkan pada pencarian **tema/topik pembahasan dalam bahasa Arab** (misal: *غاية خلق الإنسان*, *أمر الأولاد بالصلاة*, *مراتب تغيير المنكر*), bukan sekadar mengutip teks dalil mentah:

```
URL Format: https://openbayan.insanmustaqbal.or.id/search?q=<TEMA_BAHASA_ARAB_URL_ENCODED>&lang=id
Contoh: https://openbayan.insanmustaqbal.or.id/search?q=%D8%BA%D8%A7%D9%8A%D8%A9+%D8%AE%D9%84%D9%82+%D8%A7%D9%84%D8%A5%D9%86%D8%B3%D8%A7%D9%86&lang=id (Tema: غاية خلق الإنسان)
```

### E. Integrasi Microsoft PowerPoint Online (OneDrive)

Seluruh 41 materi presentasi resmi PKN ditampilkan sebagai **iframe embed interaktif** menggunakan Microsoft Office Web Apps Viewer, di-host di OneDrive pengguna:

```html
<iframe
  src="https://1drv.ms/p/c/3efe4d3cd3a3788a/IQR...?em=2&wdAr=1.7777777777777777"
  style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;"
  allowfullscreen>
</iframe>
```

Token embed per-file tersimpan di [`data/onedrive_embed_tokens.json`](https://github.com/decaller/wiki-pkn/blob/main/data/onedrive_embed_tokens.json).

---

## 5. Infrastruktur & Deployment

### A. Arsitektur Deployment Produksi

```
GitHub (decaller/wiki-pkn, branch: main)
        ↓  GitOps / Auto Pull
Portainer Stack (Stack ID: 25, Endpoint ID: 3)
        ↓  docker-compose.yml
Docker Container "wiki-pkn"
  ├── Dockerfile: node:22-slim multi-stage build
  ├── Build Stage: npm install + npx quartz build
  └── Runtime: npx quartz serve (port 8080)
        ↓  Port Binding
Host: 0.0.0.0:4040 → container:8080
        ↓  Reverse Proxy
Zoraxy Reverse Proxy → domain routing
        ↓  CDN / SSL
Cloudflare Proxy + SSL/TLS (HTTPS)
        ↓  Pengguna
https://wikipkn.insanmustaqbal.or.id
```

### B. Konfigurasi Docker

**`docker-compose.yml`:**
```yaml
services:
  wiki-pkn:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: wiki-pkn
    restart: unless-stopped
    ports:
      - "${HOST_PORT:-4040}:${PORT:-8080}"
    environment:
      - DOMAIN=${DOMAIN:-localhost}
      - PORT=${PORT:-8080}
      - WS_PORT=${WS_PORT:-3001}
    volumes:
      - ./presentations:/usr/src/app/presentations:ro
    healthcheck:
      test: ["CMD", "node", "-e", "fetch('http://localhost:' + (process.env.PORT || 8080))..."]
      interval: 30s
      retries: 3
```

**`Dockerfile` (multi-stage build):**
- **Stage 1 (builder):** `node:22-slim` + `git` → `npm install` + `npx quartz plugin install`
- **Stage 2 (runtime):** `node:22-slim` + `git` → copy hasil build + `docker-entrypoint.sh`

**Optimasi `.dockerignore`:** Mengecualikan direktori besar yang tidak perlu masuk container:
- `old_backup/` (2,6 GB arsip sumber)
- `searchable_pdfs/` (925 MB)
- `node_modules/`
- `public/` (di-generate ulang saat build)

### C. Environment Variables Produksi

| Variabel | Nilai Produksi | Keterangan |
| :--- | :--- | :--- |
| `DOMAIN` | `wikipkn.insanmustaqbal.or.id` | FQDN untuk canonical URL, OpenGraph, sitemap |
| `BASE_URL` | `wikipkn.insanmustaqbal.or.id` | URL base Quartz |
| `PORT` | `8080` | Port internal container |
| `HOST_PORT` | `4040` | Port host ke reverse proxy |
| `WS_PORT` | `3001` | WebSocket live-reload |
| `GISCUS_REPO` | `decaller/wiki-pkn` | GitHub Discussions komentar |
| `GISCUS_CATEGORY` | `General` | Kategori diskusi |

### D. GitOps & CI/CD

Deployment otomatis via **Portainer GitOps**:
- Setiap `git push` ke branch `main` → Portainer Stack auto-pull & rebuild
- Atau manual via `StackGitRedeploy` (Stack ID: 25, Endpoint ID: 3)
- Webhook URL tersedia untuk integrasi GitHub Actions

### E. DNS & SSL

| Layer | Teknologi | Detail |
| :--- | :--- | :--- |
| **DNS** | Cloudflare | NS records organisasi `insanmustaqbal.or.id` |
| **SSL/TLS** | Cloudflare SSL | Otomatis HTTPS, mode Full (Strict) |
| **CDN** | Cloudflare CDN | Cache aset statis (WebP, JS, CSS) |
| **Reverse Proxy** | Zoraxy | Routing `wikipkn.insanmustaqbal.or.id` → `localhost:4040` |

---

## 6. Desain Visual & Estetika

### A. Palet Warna Nabawiyah

| Mode | Warna | Kode HEX |
| :--- | :--- | :--- |
| **Light — Background** | Parchment | `#fbf8f3` |
| **Light — Teks** | Walnut Brown | `#3d312a` |
| **Light — Aksen** | Emerald | `#2d6a4f` |
| **Dark — Background** | Charcoal Espresso | `#1a1714` |
| **Dark — Teks** | Ivory Linen | `#ded5cb` |
| **Dark — Aksen** | Luminous Mint | `#52b788` |

### B. Aset Visual

- **Header Beranda:** Panorama Masjid Uzungöl & Danau Trabzon (1920×800px WebP, Rüveyda Akkaya / Pexels)
- **Banner Artikel:** 100% artikel memiliki banner horizontal 1050×350px WebP (standar rasio 3:1)
- **Slide Diagram:** 29 slide WebP berkualitas tinggi dari PDF presentasi resmi PKN

### C. Tipografi & Aksesibilitas

- Font: Inter (Google Fonts) — memenuhi standar keterbacaan huruf Arab bersama sistem font Arab bawaan
- Aksesibilitas: Konten dark mode tersedia, kontras warna dioptimalkan
- Responsif: Mobile-first, sidebar `OutlineNav` dioptimalkan untuk layar kecil

---

## 7. Skrip Otomasi & Alat Pengembangan

Seluruh skrip Python tersimpan di direktori [`scripts/`](https://github.com/decaller/wiki-pkn/tree/main/scripts):

| Skrip | Fungsi |
| :--- | :--- |
| `inject_openbayan_links.py` | Injeksi link pencarian OpenBayan ke semua dalil |
| `inject_page_disclaimer.py` | Sematkan banner metodologi AI di semua halaman |
| `inject_presentation_citations.py` | Sisipkan callout sitasi slide PPT |
| `inject_pptx_office_embeds.py` | Embed iframe OneDrive PowerPoint Online |
| `update_onedrive_embeds.py` | Update token embed OneDrive terbaru |
| `generate_horizontal_banners.py` | Crop foto → banner 1050×350px WebP |
| `export_presentation_slides.py` | Ekspor slide PDF → WebP diagram |
| `inject_images_to_articles.py` | Pasang banner & slide ke artikel |
| `analyze_images_omp.py` | Visi AI (Gemini) audit konten foto |
| `remap_matched_banners.py` | Petakan banner ke artikel relevan (semantik) |
| `search_pexels.py` | Cari foto dari Pexels API (compliance syariat) |
| `curate_missing_banners.py` | Kurasi banner untuk artikel tanpa gambar |
| `enrich_batch{1-4}.py` | Pengayaan batch 4 klaster tematik |
| `enrich_etape_usia.py` | Tambah panduan 4 etape usia di semua artikel |
| `enrich_instrumen.py` | Tambah rubrik 3-level + refleksi muhasabah |
| `fetch_sotabh_articles.py` | Crawl 117 artikel SOTAB HEBAT |
| `fetch_skis_articles.py` | Crawl 172 halaman Sekolah Karakter |
| `fetch_pkn_portal.py` | Crawl portal karakternabawiyah.com |
| `crawl_github_repos.py` | Telusuri repo GitHub organisasi & developer |
| `generate_tb40_bases.py` | Generate 40 profil pilar karakter TB40 |
| `convert_all_mermaid_to_canvas.py` | Konversi 94 diagram Mermaid → Obsidian Canvas |
| `search_pkn_video.py` | CLI pencarian timestamp video ceramah pkn.db |
| `search_dalil_openbayan.py` | CLI pencarian dalil di basis data OpenBayan |
| `fix_mermaid_lists.py` | Perbaiki sintaks list Mermaid (error browser) |

---

## 8. Ekosistem Digital Terintegrasi

Wiki PKN bukan berdiri sendiri, melainkan bagian dari **ekosistem digital PKN** yang lebih luas:

| Platform | URL | Fungsi |
| :--- | :--- | :--- |
| **Wiki PKN** (dokumen ini) | [wikipkn.insanmustaqbal.or.id](https://wikipkn.insanmustaqbal.or.id) | Ensiklopedia referensi terbuka |
| **OpenBayan** | [openbayan.insanmustaqbal.or.id](https://openbayan.insanmustaqbal.or.id) | Mesin pencari turats Islam (Maktabah Syamilah) |
| **Tes Online Tafsir Bakat (resmi)** | [tafsirbakat.com](https://tafsirbakat.com) | Asesmen mandiri 40 pilar bakat nabawiyah |
| **TB40 Insan Mustaqbal** | [tb40.insanmustaqbal.or.id](https://tb40.insanmustaqbal.or.id) | Platform asesmen TB40 (pengembangan) |
| **Peta Bakat Visual** | [pub.insantaqwa.org/bakat](https://pub.insantaqwa.org/bakat/) | Visualisasi interaktif polarisasi 40 bakat |
| **Portal Resmi PKN** | [karakternabawiyah.com](https://karakternabawiyah.com) | Informasi program, event, dan buku resmi |
| **SOTAB HEBAT** | [sotabh.com](https://sotabh.com) | Artikel dan produk Tim SOTAB HEBAT |

---

> [!info] Refleksi Lapangan: Mengapa Dokumentasi Teknis Ini Penting
> **Kondisi Faktual:** Sistem basis pengetahuan yang dibangun melalui proses panjang dan berlapis (49 milestone) ini perlu didokumentasikan secara transparan agar dapat direplikasi, dipelihara, dan dikembangkan oleh tim lain.
> **Akar Masalah:** Tanpa dokumentasi metodologi yang jelas, risiko kehilangan pengetahuan teknis (knowledge loss) sangat tinggi jika terjadi pergantian tim pengembang.
> **Langkah Penanganan:** Halaman ini bersama [HANDOFF.md](https://github.com/decaller/wiki-pkn/blob/main/HANDOFF.md) menjadi dokumen resmi serah terima teknis yang harus selalu diperbarui setiap ada milestone baru.

> [!warning] Peringatan Pemeliharaan
> * **Bentuk Kesalahan:** Menjalankan deployment langsung ke Portainer tanpa terlebih dahulu menguji di lokal (`npx quartz build --serve --port 8888`).
> * **Dampak:** Build error atau broken links dapat langsung mempengaruhi pengguna di produksi.
> * **Pencegahan:** Selalu jalankan `npx quartz build` lokal terlebih dahulu, verifikasi via browser, baru push ke `main` dan redeploy.

> [!tip] Cara Berkontribusi ke Wiki PKN
> * **Aksi:** Untuk berkontribusi konten baru, baca panduan lengkap di [[Panduan Kontribusi]] dan pastikan mengikuti 9 Lapisan Anatomi Baku (Frontmatter → Banner → Note AI → Judul → Dalil → Konten → Trio Refleksi → Sitasi → Media PPT).
> * **Tujuan:** Menjaga konsistensi standar emas dan integritas ilmiah seluruh ensiklopedia.

---

---

> [!quote] Naskah Sumber Asli & Khazanah Artikel Terkait
> Materi dalam artikel ini memiliki keterkaitan sanad keilmuan dan disintesis dari naskah/tulisan asli narasumber pada situs resmi berikut:
>
> - 🌐 **[PKN] Profil Ustadz Abdul Kholiq**  
>   🔗 Sumber Asli: [https://karakternabawiyah.com/profil-ustadz-abdul-kholiq/](https://karakternabawiyah.com/profil-ustadz-abdul-kholiq/)  
>   *Profil narasumber utama dan perumus Manhaj PKN Ustadz Abdul Kholiq.*  
>
> - 🏫 **[SKIS] Sekilas Pandang**  
>   🔗 Sumber Asli: [https://sekolahkarakter.com/sekilas-pandang/](https://sekolahkarakter.com/sekilas-pandang/)  
>   *Latar belakang historis kurikulum fitrah di SKIS Semarang.*  

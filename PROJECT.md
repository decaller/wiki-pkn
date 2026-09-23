# Project: Wiki PKN Full-Scale Expansion

## Architecture
Wiki PKN is an encyclopedic knowledge base for Pendidikan Karakter Nabawiyah (PKN) built on Quartz v5 (Node.js/TypeScript static site generator) rendering 383+ Markdown notes into an interconnected digital garden.
The expansion comprises four technical & content tracks plus an automated verification & deployment track:
1. **Dalil & Turats Track (R1)**: High-density Islamic reference base (`content/Dalil/`) with MediaWiki 4-Zone layout, authentic Arabic matan, Kemenag translations, classical syarah, takhrij from Maktabah Syamilah / OpenBayan, and enrichment of `Tazkiyatun Nafs.md`.
2. **Corpus Quality & Linter Track (R2)**: Automated linting via `scripts/wiki_corpus_linter.py` enforcing Link Integrity (0 broken links), Vocabulary Guard (replacing Western pedagogy terms with Islamic/fitrah terminology), 10 Pedagogical Style points of Ustadz Abdul Kholiq, and PKN Indonesian Clarity Index (PICI >= 85/100).
3. **Analytics & SEO Track (R3)**: Self-hosted privacy-friendly Umami Analytics stack (PostgreSQL 15 + Umami) on Portainer Endpoint 3, configured seamlessly in Quartz (`quartz.config.yaml`), alongside comprehensive SEO metadata (canonical URLs, Open Graph, sitemap).
4. **Canonical Reference Track (R4)**: 8 standalone encyclopedic book reviews in MediaWiki 4-Zone (`content/Referensi/`) for the primary PKN canon by Ustadz Abdul Kholiq, interconnected to knowledge hubs.
5. **E2E Verification & Deployment Track**: Automated test/lint run, full Quartz build (`npx quartz build`), and GitOps production deployment on Portainer Endpoint 3 (`https://wikipkn.insanmustaqbal.or.id`).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Dalil 4-Zone MediaWiki Standard | Standardized Zone 1 (Header/Action Bar), Zone 2 (Infobox), Zone 3 (Arabic/Translation/Syarah/4-Fase Matriks), Zone 4 (Cross-links/Navbox) | M1 | Survey R1 |
| 2 | Refactor Existing Dalil Files | Update 4 existing prototype dalil files to full 4-Zone format and fix vocabulary (*etape* -> *fase*) | M1 | Survey R1 |
| 3 | Publish 61+ New Mandiri Dalil Pages | Create >= 50 (target 61+) new encyclopedic dalil files across 8 Manhaj PKN clusters in `content/Dalil/` | M1 | Survey R1 |
| 4 | Enrich Tazkiyatun Nafs Article | Add 8 verified naqli dalils (matan Arab, translation, syarah) for Takhalli and Tahalli to `Tazkiyatun Nafs.md` | M1 | Survey R1 |
| 5 | Master Dalil Cross-Linking | Reciprocal wikilinks between dalils and core Manhaj PKN concepts (4 Fase Usia, Tiga Bahasa, Rukun 3A, TB-40) | M1 | Survey R1 |
| 6 | Horizontal Dalil Navbox | Component-based navigation box connecting dalil topics | M1 | Survey R1 |
| 7 | Wiki Corpus Linter Development | Create standalone, robust `scripts/wiki_corpus_linter.py` with AST/regex parser, JSON/MD reporting | M2 | Survey R2 |
| 8 | Link Integrity Audit & Fix | Detect and resolve 54 broken link targets (118 occurrences) and 248 orphan pages across 383+ md files | M2 | Survey R2 |
| 9 | Vocabulary Guard Enforcement | Programmatic detection and remediation of prohibited foreign words (*etape* -> *fase*, *archetype* -> *uswah*, etc.) | M2 | Survey R2 |
| 10 | Style Compliance & 10 Pedagogical Points | Audit and scoring for UAK pedagogical style (TL;DR callout, canvas embed, 3-level rubric, muhasabah questions) | M2 | Survey R2 |
| 11 | Indonesian Clarity Audit & Tuning | Implement PKN Indonesian Clarity Index (PICI) and optimize essay files to reach average score >= 85/100 | M2 | Survey R2 |
| 12 | Deploy PostgreSQL + Umami Stack | Docker stack deployment on Portainer Endpoint 3 (internal bridge network, host port 3008:3000) | M3 | Survey R3 |
| 13 | Configure Umami in Quartz | Update `quartz.config.yaml` with Umami host and websiteId | M3 | Survey R3 |
| 14 | Canonical URL Tag in Quartz | Add `<link rel="canonical" href={socialUrl} />` to `quartz/components/Head.tsx` | M3 | Survey R3 |
| 15 | SEO Verification (OG, Sitemap) | Validate dynamic Open Graph tags, meta descriptions, and sitemap generation | M3 | Survey R3 |
| 16 | 8 Canonical Book Reviews Publication | Publish 8 4-Zone encyclopedic book reviews in `content/Referensi/` using bibtex & source materials | M4 | Survey R4 |
| 17 | Reference Hub Interlinking | Cross-link all 8 book reviews in `content/Referensi/Referensi Tambahan Buku Cetak.md` and `content/index.md` | M4 | Survey R4 |
| 18 | E2E Quartz Build Verification | Ensure `npx quartz build` completes with exit code 0 | M5 | Delivery Standard |
| 19 | Linter Verification | Verify 0 broken internal links and average clarity >= 85/100 across corpus | M5 | Delivery Standard |
| 20 | Git Commit & Portainer Production Redeploy | Commit all changes to `main` and trigger GitOps redeploy on Portainer Endpoint 3 (`https://wikipkn.insanmustaqbal.or.id`) | M5 | Delivery Standard |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Dalil Database Expansion & Tazkiyatun Nafs | Features 1, 2, 3, 4, 5, 6 | None | DONE |
| M2 | Wiki Corpus Linter & Quality Remediation | Features 7, 8, 9, 10, 11 | M1, M4 (partial) | DONE |
| M3 | Umami Analytics Container & SEO Optimization | Features 12, 13, 14, 15 | None | DONE |
| M4 | 8 Canonical Book Reviews & Reference Hub | Features 16, 17 | None | DONE |
| M5 | E2E Verification & Production Deployment | Features 18, 19, 20 | M1, M2, M3, M4 | PLANNED |

## Interface Contracts
### content/Dalil/ ↔ content/
- Filename pattern: `dalil-[topik-kebab-case].md`
- Wikilink syntax: `[[dalil-[topik-kebab-case]|QS. [Surah]:[Ayat]]` or `[[dalil-[topik-kebab-case]|HR. [Perawi] No. [X]]`
- Format: Zone 1 Header, Zone 2 Infobox Dalil, Zone 3 Matan/Tarjamah/Syarah/Matriks, Zone 4 Cross-links & Navbox

### scripts/wiki_corpus_linter.py ↔ content/
- CLI interface: `python3 scripts/wiki_corpus_linter.py [--check-links] [--check-vocab] [--check-style] [--check-clarity] [--fix] [--json-out report.json]`
- Pass criteria: 0 broken internal links, average clarity >= 85.0

### Portainer Endpoint 3 ↔ Quartz Config
- Umami instance exposed at `http://localhost:3008` (or public URL/reverse proxy)
- `quartz.config.yaml` `analytics.provider`: "umami", `analytics.host`: "...", `analytics.websiteId`: "..."

### content/Referensi/ ↔ content/
- Filename pattern: `Review Buku [Judul Lengkap].md`
- Referenced from `content/index.md` and `content/Referensi/Referensi Tambahan Buku Cetak.md`

## Code Layout
- `content/Dalil/`: All dalil markdown files
- `content/Paradigma - Implementasi PKN/.../Tazkiyatun Nafs.md`: Tazkiyatun Nafs core article
- `content/Referensi/`: Reference materials and 8 canonical book reviews
- `content/index.md`: Main wiki homepage hub
- `scripts/wiki_corpus_linter.py`: Linter and audit script
- `quartz.config.yaml`: Quartz static site generator configuration
- `quartz/components/Head.tsx`: HTML Head component for SEO & canonical tags
- `docker-compose.umami.yml` or Portainer Stack: Umami + PostgreSQL stack definition

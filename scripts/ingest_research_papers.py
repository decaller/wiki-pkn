#!/usr/bin/env python3
"""
Batch Ingestion & Pre-Flight Pipeline for External Research Papers (Wiki-PKN).

Pipeline ini bertugas:
1. Memindai berkas PDF di sources/research_papers/
2. Melakukan pre-flight inspection via PyMuPDF (mendeteksi teks digital vs scan gambar, ekstraksi DOI heuristik)
3. Mengekstrak elemen dokumen via Unstructured API (port 8005) dengan strategi optimal (fast / ocr_only)
4. Melakukan audit dan pengayaan metadata akademik via OpenAlex API & Semantic Scholar API (jika DOI ditemukan)
5. Menghasilkan Catatan Atomik Riset (Atomic Note) berformat Markdown dengan matriks komparasi 6 dimensi PKN
6. Menyimpan hasil secara terisolasi di data/extracted_elements/external_research/
"""

import os
import sys
import json
import re
import time
import hashlib
import argparse
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Import UnstructuredAdapter dari scripts lokal
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from unstructured_adapter import UnstructuredAdapter
except ImportError:
    UnstructuredAdapter = None

# Deteksi ketersediaan PyMuPDF (fitz)
try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False

# Konfigurasi Default
DEFAULT_INPUT_DIR = Path("sources/research_papers")
DEFAULT_OUTPUT_DIR = Path("data/extracted_elements/external_research")
DEFAULT_API_URL = os.getenv("UNSTRUCTURED_API_URL", "http://localhost:8005/general/v0/general")

# Regex pola DOI standar
DOI_PATTERN = re.compile(r'\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)\b')


class PreflightInspector:
    """Melakukan inspeksi awal berkas PDF sebelum dikirim ke mesin ekstraksi."""

    @staticmethod
    def inspect_pdf(pdf_path: Path) -> Dict[str, Any]:
        """Periksa apakah PDF memiliki text-layer digital atau murni scan gambar."""
        info = {
            "path": str(pdf_path),
            "filename": pdf_path.name,
            "size_bytes": pdf_path.stat().st_size,
            "page_count": 0,
            "has_digital_text": False,
            "recommended_strategy": "fast",
            "detected_doi": None,
            "sample_title_hint": None,
            "error": None
        }

        if not HAS_PYMUPDF:
            # Fallback jika PyMuPDF belum aktif di environment ini
            info["recommended_strategy"] = "auto"
            return info

        try:
            doc = fitz.open(pdf_path)
            info["page_count"] = len(doc)

            total_chars = 0
            sample_pages = min(5, len(doc))
            extracted_samples = []

            for i in range(sample_pages):
                page = doc[i]
                text = page.get_text("text")
                total_chars += len(text.strip())
                extracted_samples.append(text)

                # Cari pola DOI pada halaman awal
                if not info["detected_doi"]:
                    match = DOI_PATTERN.search(text)
                    if match:
                        clean_doi = match.group(1).rstrip(".,;")
                        info["detected_doi"] = clean_doi

            # Rata-rata karakter per halaman
            avg_chars = total_chars / max(1, sample_pages)
            if avg_chars > 80:
                info["has_digital_text"] = True
                info["recommended_strategy"] = "fast"
            else:
                info["has_digital_text"] = False
                info["recommended_strategy"] = "ocr_only"

            # Ambil petunjuk judul dari baris teks besar pertama di halaman 1
            if sample_pages > 0 and len(extracted_samples) > 0:
                first_lines = [l.strip() for l in extracted_samples[0].split("\n") if len(l.strip()) > 10]
                if first_lines:
                    info["sample_title_hint"] = first_lines[0][:150]

            doc.close()
        except Exception as e:
            info["error"] = str(e)
            info["recommended_strategy"] = "auto"

        return info


class AcademicMetadataEnricher:
    """Menarik metadata akademik resmi dari OpenAlex dan Semantic Scholar."""

    @staticmethod
    def query_openalex(doi: str) -> Optional[Dict[str, Any]]:
        """Kueri metadata dari OpenAlex API (Gratis, tanpa key)."""
        clean_doi = urllib.parse.quote(doi)
        url = f"https://api.openalex.org/works/https://doi.org/{clean_doi}"
        headers = {"User-Agent": "wiki-pkn-researcher/1.0 (mailto:admin@karakternabawiyah.com)"}

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    authors = [
                        a.get("author", {}).get("display_name", "")
                        for a in data.get("authorships", [])[:5]
                    ]
                    return {
                        "source": "OpenAlex",
                        "title": data.get("title"),
                        "publication_year": data.get("publication_year"),
                        "authors": [a for a in authors if a],
                        "cited_by_count": data.get("cited_by_count", 0),
                        "is_retracted": data.get("is_retracted", False),
                        "open_access": data.get("open_access", {}).get("is_oa", False),
                        "primary_topic": data.get("primary_topic", {}).get("display_name", ""),
                        "landing_page_url": data.get("primary_location", {}).get("landing_page_url", "")
                    }
        except Exception:
            return None
        return None

    @staticmethod
    def query_semantic_scholar(doi: str) -> Optional[Dict[str, Any]]:
        """Kueri metadata dan pengaruh sitasi dari Semantic Scholar API."""
        clean_doi = urllib.parse.quote(doi)
        url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{clean_doi}?fields=title,year,authors,influentialCitationCount,citationStyles"
        headers = {"User-Agent": "wiki-pkn-researcher/1.0"}

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode("utf-8"))
                    authors = [a.get("name", "") for a in data.get("authors", [])[:5]]
                    return {
                        "source": "Semantic Scholar",
                        "title": data.get("title"),
                        "year": data.get("year"),
                        "authors": [a for a in authors if a],
                        "influential_citation_count": data.get("influentialCitationCount", 0)
                    }
        except Exception:
            return None
        return None


class AtomicNoteGenerator:
    """Menyusun catatan atomik Markdown berstandar Progressive Disclosure & PKN Matriks."""

    @staticmethod
    def generate_note(
        pdf_path: Path,
        inspection: Dict[str, Any],
        academic_meta: Optional[Dict[str, Any]],
        markdown_body: str
    ) -> str:
        title = (
            (academic_meta and academic_meta.get("title"))
            or inspection.get("sample_title_hint")
            or pdf_path.stem.replace("_", " ").title()
        )
        authors = (academic_meta and academic_meta.get("authors")) or ["Unknown Author"]
        year = (academic_meta and (academic_meta.get("publication_year") or academic_meta.get("year"))) or "Unknown"
        doi = inspection.get("detected_doi") or "N/A"
        citations = (academic_meta and academic_meta.get("cited_by_count")) or 0
        influential_citations = (academic_meta and academic_meta.get("influential_citation_count")) or 0
        is_retracted = (academic_meta and academic_meta.get("is_retracted")) or False

        # Status Replikasi Heuristik
        repl_status = "Retracted (Ditarik)" if is_retracted else "Perlu Diaudit (Cek scite.ai)"

        frontmatter = f"""---
title: "{title}"
authors: {json.dumps(authors)}
year: {year}
doi: "{doi}"
citation_count: {citations}
influential_citations: {influential_citations}
is_retracted: {str(is_retracted).lower()}
methodology: "Perlu Klasifikasi (RCT / Kohort / Meta-Analisis / Kualitatif)"
sample_size_N: "Belum Diekstrak"
measurement_type: "Perlu Verifikasi (Substrat Fisik vs Konstruk Laten Likert)"
preregistered: "Perlu Cek OSF"
replication_status: "{repl_status}"
pkn_perspective:
  convergence_wasilah: "Mekanisme fisik / biologis sunnatullah yang sejalan dengan fitrah"
  divergence_ghayah: "Bantahan terhadap asumsi reduksionisme materialistik / ketiadaan akhirat"
  matrix_mapping:
    hakikat_insan: "Fitrah Tauhid & Jism-Ruh-Nafs-Aql vs Materi Evolusioner"
    ghayah_tujuan: "Sa'adatud Darain vs Prestasi Duniawi Semata"
    peran_murabbi: "Uswah, Mu'allim & Doa vs Fasilitator Bebas Nilai"
    adab_uqubah: "Tadarrub & Haya' vs Behaviorisme Reward-Punishment Mekanistik"
    najaah_hasil: "Kesadaran Beramal & Integritas vs Angka Skor Kognitif"
    keterikatan_akhirat: "Hisab & Ridha Allah vs Ketiadaan Dimensi Transendental"
---
"""

        body = f"""# {title}

> [!NOTE] Ringkasan Eksekutif & Asal Usul Sumber
> **Penulis:** {', '.join(authors)} ({year})  
> **DOI:** `{doi}` | **Total Sitasi:** {citations} | **Influential Citations:** {influential_citations}  
> **Status Retraksi:** {'⚠️ DITARIK PENERBIT' if is_retracted else '✅ Tidak Terdeteksi Retraksi'}  
> **Berkas Asli:** `{pdf_path.name}` ({inspection.get('page_count', 0)} halaman)

---

## 1. Analisis Metodologis & Kebersihan Kognitif
* **Tipe Objek Kajian:** Apakah meneliti *Natural Kinds* (substrat biologi keras) atau *Latent Construct* (angket perilaku)?
* **Kerapuhan Replikasi:** Apakah metodologi telah dipra-registrasikan di OSF / AsPredicted?
* **Pencegahan Cocoklogi:** Apakah ada indikasi *HARKing* atau *$p$-hacking* pada signifikansi data?

---

## 2. Gelanggang Dialektika: PKN vs Riset Temuan

### A. Titik Temu Sunnatullah (Wasilah / Sarana Fisik)
* Catat di sini mekanisme biologis atau psikofisika yang terbukti valid dan memperkuat sunnatullah tumbuh kembang anak (misal: pentingnya stimulasi multisensori, bahaya stimulasi layar digital berlebih, atau siklus tidur sirkadian).

### B. Titik Tolak Kritis & Dekonstruksi Syar'i (Ghayah / Aksiologi)
* Catat celah filosofis, reduksionisme kimiawi otak, atau relativisme moral yang bertentangan dengan Al-Qur'an dan Sunnah.

---

## 3. Ekstraksi Naskah Dokumen Asli (Unstructured Output)

<details>
<summary><b>Klik untuk Membuka Teks & Tabel Hasil Partisi Dokumen</b></summary>

{markdown_body}

</details>
"""
        return frontmatter + "\n" + body


class ResearchBatchPipeline:
    """Orkestrator batch ekstraksi dokumen riset eksternal."""

    def __init__(
        self,
        input_dir: Path = DEFAULT_INPUT_DIR,
        output_dir: Path = DEFAULT_OUTPUT_DIR,
        api_url: str = DEFAULT_API_URL,
        strategy: str = "auto",
        skip_enrichment: bool = False,
        force: bool = False
    ):
        self.input_dir = Path(input_dir).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.api_url = api_url
        self.strategy = strategy
        self.skip_enrichment = skip_enrichment
        self.force = force

        self.adapter = None
        if UnstructuredAdapter:
            self.adapter = UnstructuredAdapter(api_url=self.api_url)

    def scan_files(self) -> List[Path]:
        """Pindai seluruh berkas PDF di direktori input."""
        if not self.input_dir.exists():
            return []
        files = sorted(list(self.input_dir.glob("**/*.pdf")))
        return files

    def run_preflight_report(self) -> List[Dict[str, Any]]:
        """Jalankan pre-flight inspection untuk seluruh berkas tanpa memanggil Unstructured."""
        files = self.scan_files()
        print(f"\n=======================================================")
        print(f" 🔍 PRE-FLIGHT INSPECTION: {len(files)} BERKAS PDF DITEMUKAN")
        print(f" Direktori Input : {self.input_dir}")
        print(f"=======================================================\n")

        results = []
        for idx, pdf in enumerate(files, 1):
            info = PreflightInspector.inspect_pdf(pdf)
            results.append(info)
            doi_str = f" | DOI: {info['detected_doi']}" if info['detected_doi'] else " | No DOI"
            strat_str = f"Strategi: {info['recommended_strategy'].upper()}"
            print(f"[{idx:02d}/{len(files):02d}] {pdf.name[:45]:<45} ({info['page_count']} hal) -> {strat_str}{doi_str}")

        return results

    def process_file(self, pdf_path: Path) -> Dict[str, Any]:
        """Proses satu berkas PDF secara utuh."""
        print(f"\n[+] Memproses: {pdf_path.name}")
        inspection = PreflightInspector.inspect_pdf(pdf_path)

        chosen_strategy = (
            self.strategy if self.strategy != "auto"
            else inspection.get("recommended_strategy", "fast")
        )
        print(f"    - Strategi Ekstraksi: {chosen_strategy} (Digital Text: {inspection.get('has_digital_text')})")

        # 1. Ekstraksi Unstructured
        markdown_body = ""
        if self.adapter:
            try:
                extraction = self.adapter.process_file_with_cache(
                    file_path=pdf_path,
                    output_dir=self.output_dir,
                    strategy=chosen_strategy,
                    force=self.force
                )
                markdown_body = extraction.get("markdown", "")
                print(f"    - Ekstraksi Berhasil ({extraction.get('element_count', 0)} elemen terpartisi)")
            except Exception as e:
                print(f"    - [ERROR Unstructured]: {e}")
                markdown_body = f"*Ekstraksi dokumen via Unstructured gagal atau tertunda: {e}*"
        else:
            markdown_body = "*UnstructuredAdapter tidak tersedia.*"

        # 2. Pengayaan Metadata Akademik
        academic_meta = None
        detected_doi = inspection.get("detected_doi")
        if detected_doi and not self.skip_enrichment:
            print(f"    - Menghubungi OpenAlex API untuk DOI: {detected_doi}...")
            academic_meta = AcademicMetadataEnricher.query_openalex(detected_doi)
            if not academic_meta:
                print(f"    - Menghubungi Semantic Scholar API...")
                academic_meta = AcademicMetadataEnricher.query_semantic_scholar(detected_doi)

            if academic_meta:
                print(f"    - Metadata Akademik Ditemukan: {academic_meta.get('title')} ({academic_meta.get('publication_year') or academic_meta.get('year')})")
            else:
                print("    - Metadata eksternal tidak ditemukan (menggunakan metadata lokal).")

        # 3. Bentuk Catatan Atomik Markdown
        note_content = AtomicNoteGenerator.generate_note(
            pdf_path=pdf_path,
            inspection=inspection,
            academic_meta=academic_meta,
            markdown_body=markdown_body
        )

        note_file = self.output_dir / f"{pdf_path.stem}_atomic_note.md"
        with open(note_file, "w", encoding="utf-8") as f:
            f.write(note_content)

        print(f"    - Catatan Atomik Terbit: {note_file.name}")
        return {"status": "success", "note_file": str(note_file)}


def main():
    parser = argparse.ArgumentParser(description="Batch Ingest External Research Papers for Wiki-PKN")
    parser.add_argument("--input-dir", type=str, default=str(DEFAULT_INPUT_DIR), help="Direktori input berkas PDF")
    parser.add_argument("--output-dir", type=str, default=str(DEFAULT_OUTPUT_DIR), help="Direktori output hasil")
    parser.add_argument("--api-url", type=str, default=DEFAULT_API_URL, help="URL endpoint Unstructured API")
    parser.add_argument("--strategy", type=str, default="auto", choices=["auto", "fast", "ocr_only", "hi_res"])
    parser.add_argument("--preflight-only", action="store_true", help="Hanya jalankan inspeksi awal tanpa ekstraksi API")
    parser.add_argument("--skip-enrichment", action="store_true", help="Lewati query ke OpenAlex / Semantic Scholar")
    parser.add_argument("--force", action="store_true", help="Paksa ekstrak ulang abaikan cache MD5")
    parser.add_argument("--file", type=str, help="Proses hanya satu file spesifik")

    args = parser.parse_args()

    pipeline = ResearchBatchPipeline(
        input_dir=Path(args.input_dir),
        output_dir=Path(args.output_dir),
        api_url=args.api_url,
        strategy=args.strategy,
        skip_enrichment=args.skip_enrichment,
        force=args.force
    )

    if args.preflight_only:
        pipeline.run_preflight_report()
        return

    if args.file:
        target_file = Path(args.file)
        if target_file.exists():
            pipeline.process_file(target_file)
        else:
            print(f"[ERROR] Berkas tidak ditemukan: {target_file}")
            sys.exit(1)
        return

    files = pipeline.scan_files()
    if not files:
        print(f"\n[INFO] Belum ada berkas PDF di '{args.input_dir}'.")
        print(f"Silakan letakkan berkas PDF riset Anda di direktori tersebut, lalu jalankan kembali skrip ini.")
        return

    print(f"\nMemulai batch ekstraksi untuk {len(files)} berkas PDF...")
    for pdf in files:
        pipeline.process_file(pdf)
        time.sleep(0.5)  # Cooldown rate-limit ramah sistem


if __name__ == "__main__":
    main()

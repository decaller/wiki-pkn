#!/usr/bin/env python3
"""
Academic Paper Search & Discovery CLI for Wiki-PKN.

Alat pencarian literatur riset ilmiah lintas mesin:
- OpenAlex (>250M works, open access filter, citation metrics)
- Semantic Scholar (Influential citations & intent)
- arXiv (Preprint server via python-arxiv)

Mendukung pencarian kata kunci, audit metriks, dan pengunduhan PDF Open-Access
langsung ke folder sources/research_papers/ untuk diproses oleh pipeline Wiki-PKN.
"""

import os
import sys
import json
import time
import argparse
import urllib.parse
from pathlib import Path
from typing import Dict, List, Any, Optional

# Tambahkan venv site-packages jika dijalankan dengan python sistem
VENV_PATH = Path(__file__).resolve().parent.parent / ".venv" / "lib"
if VENV_PATH.exists():
    for p in VENV_PATH.glob("python*/site-packages"):
        sys.path.insert(0, str(p))

import requests

try:
    import arxiv
    HAS_ARXIV = True
except ImportError:
    HAS_ARXIV = False

DEFAULT_DOWNLOAD_DIR = Path("sources/research_papers")


class AcademicSearchEngine:
    """Mesin agregasi pencarian literatur ilmiah terbuka."""

    @staticmethod
    def search_openalex(query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Mencari paper di katalog OpenAlex."""
        encoded_q = urllib.parse.quote(query)
        url = f"https://api.openalex.org/works?search={encoded_q}&sort=cited_by_count:desc&per-page={limit}"
        headers = {"User-Agent": "wiki-pkn-discovery/1.0 (mailto:admin@karakternabawiyah.com)"}

        results = []
        try:
            resp = requests.get(url, headers=headers, timeout=12)
            if resp.status_code == 200:
                data = resp.json()
                for item in data.get("results", []):
                    # Ekstrak data kunci
                    doi_raw = item.get("doi") or ""
                    clean_doi = doi_raw.replace("https://doi.org/", "") if doi_raw else None
                    authors = [
                        a.get("author", {}).get("display_name", "")
                        for a in item.get("authorships", [])[:4]
                    ]
                    
                    # URL PDF Open Access
                    oa_info = item.get("open_access", {})
                    pdf_url = oa_info.get("oa_url")
                    if not pdf_url and item.get("primary_location"):
                        pdf_url = item.get("primary_location", {}).get("pdf_url")

                    results.append({
                        "source": "OpenAlex",
                        "title": item.get("title") or "No Title",
                        "authors": [a for a in authors if a],
                        "year": item.get("publication_year"),
                        "doi": clean_doi,
                        "citation_count": item.get("cited_by_count", 0),
                        "influential_citations": "N/A",
                        "is_retracted": item.get("is_retracted", False),
                        "is_open_access": oa_info.get("is_oa", False),
                        "pdf_url": pdf_url,
                        "landing_url": item.get("primary_location", {}).get("landing_page_url", "")
                    })
        except Exception as e:
            print(f"[!] Warning OpenAlex: {e}", file=sys.stderr)

        return results

    @staticmethod
    def search_semantic_scholar(query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Mencari paper di Semantic Scholar Graph API."""
        encoded_q = urllib.parse.quote(query)
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded_q}&limit={limit}&fields=title,authors,year,citationCount,influentialCitationCount,openAccessPdf"
        headers = {"User-Agent": "wiki-pkn-discovery/1.0"}

        results = []
        try:
            resp = requests.get(url, headers=headers, timeout=12)
            if resp.status_code == 200:
                data = resp.json()
                for item in data.get("data", []):
                    authors = [a.get("name", "") for a in item.get("authors", [])[:4]]
                    oa_pdf = item.get("openAccessPdf") or {}
                    pdf_url = oa_pdf.get("url") if isinstance(oa_pdf, dict) else None

                    results.append({
                        "source": "Semantic Scholar",
                        "title": item.get("title") or "No Title",
                        "authors": [a for a in authors if a],
                        "year": item.get("year"),
                        "doi": item.get("externalIds", {}).get("DOI") if item.get("externalIds") else None,
                        "citation_count": item.get("citationCount", 0),
                        "influential_citations": item.get("influentialCitationCount", 0),
                        "is_retracted": False,
                        "is_open_access": bool(pdf_url),
                        "pdf_url": pdf_url,
                        "landing_url": f"https://www.semanticscholar.org/paper/{item.get('paperId')}"
                    })
        except Exception as e:
            print(f"[!] Warning Semantic Scholar: {e}", file=sys.stderr)

        return results

    @staticmethod
    def search_arxiv(query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Mencari paper di preprint server arXiv."""
        if not HAS_ARXIV:
            return []

        results = []
        try:
            client = arxiv.Client()
            search = arxiv.Search(
                query=query,
                max_results=limit,
                sort_by=arxiv.SortCriterion.Relevance
            )
            for paper in client.results(search):
                authors = [a.name for a in paper.authors[:4]]
                results.append({
                    "source": "arXiv",
                    "title": paper.title,
                    "authors": authors,
                    "year": paper.published.year,
                    "doi": paper.doi,
                    "citation_count": "Preprint",
                    "influential_citations": "Preprint",
                    "is_retracted": False,
                    "is_open_access": True,
                    "pdf_url": paper.pdf_url,
                    "landing_url": paper.entry_id
                })
        except Exception as e:
            print(f"[!] Warning arXiv: {e}", file=sys.stderr)

        return results


def download_pdf(pdf_url: str, output_path: Path) -> bool:
    """Mengunduh berkas PDF dari URL open-access."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        req = requests.get(pdf_url, headers=headers, stream=True, timeout=30)
        if req.status_code == 200:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return True
    except Exception as e:
        print(f"[!] Gagal mengunduh {pdf_url}: {e}", file=sys.stderr)
    return False


def main():
    parser = argparse.ArgumentParser(description="Search Academic Research Papers for Wiki-PKN")
    parser.add_argument("query", type=str, nargs="?", help="Kata kunci pencarian topik riset")
    parser.add_argument("--source", type=str, default="openalex", choices=["all", "openalex", "semanticscholar", "arxiv"])
    parser.add_argument("--limit", type=int, default=5, help="Jumlah hasil per mesin pencari")
    parser.add_argument("--download-oa", action="store_true", help="Otomatis unduh PDF yang berlisensi Open Access ke sources/research_papers/")
    parser.add_argument("--output-json", type=str, help="Simpan hasil pencarian ke file JSON")

    args = parser.parse_args()

    if not args.query:
        print("Silakan masukkan kata kunci pencarian. Contoh:")
        print("  python3 scripts/search_academic_papers.py \"prefrontal cortex executive function children\"")
        print("  python3 scripts/search_academic_papers.py \"screen time cognitive development\" --source all")
        return

    print(f"\n=====================================================================")
    print(f" 🔎 PENCARIAN RISET AKADEMIK: '{args.query}'")
    print(f" Mesin Sumber : {args.source.upper()} | Batas: {args.limit} karya")
    print(f"=====================================================================\n")

    all_results = []

    if args.source in ("all", "openalex"):
        print("-> Mencari di OpenAlex (>250M Catalog)...")
        oa_res = AcademicSearchEngine.search_openalex(args.query, limit=args.limit)
        all_results.extend(oa_res)

    if args.source in ("all", "semanticscholar"):
        print("-> Mencari di Semantic Scholar (Citation Graph)...")
        ss_res = AcademicSearchEngine.search_semantic_scholar(args.query, limit=args.limit)
        all_results.extend(ss_res)

    if args.source in ("all", "arxiv"):
        print("-> Mencari di arXiv (Preprints)...")
        ar_res = AcademicSearchEngine.search_arxiv(args.query, limit=args.limit)
        all_results.extend(ar_res)

    print(f"\n[✓] Ditemukan {len(all_results)} paper ilmiah relevan:\n")

    for idx, paper in enumerate(all_results, 1):
        authors_str = ", ".join(paper["authors"][:3])
        if len(paper["authors"]) > 3:
            authors_str += " et al."
        if not authors_str:
            authors_str = "Unknown"

        retracted_badge = " ⚠️ [RETRACTED!]" if paper.get("is_retracted") else ""
        oa_badge = " [OPEN ACCESS]" if paper.get("is_open_access") else " [PAYWALLED]"
        
        print(f"{idx:02d}. [{paper['source']}]{oa_badge}{retracted_badge}")
        print(f"    Judul    : {paper['title']}")
        print(f"    Penulis  : {authors_str} ({paper['year']})")
        print(f"    Sitasi   : Total {paper['citation_count']} | Berpengaruh: {paper['influential_citations']}")
        if paper.get("doi"):
            print(f"    DOI      : {paper['doi']}")
        if paper.get("pdf_url"):
            print(f"    PDF Link : {paper['pdf_url']}")
        print("-" * 65)

        # Download jika diminta dan ada link PDF
        if args.download_oa and paper.get("pdf_url"):
            safe_name = "".join(c for c in paper['title'][:50] if c.isalnum() or c in " _-").strip()
            out_file = DEFAULT_DOWNLOAD_DIR / f"{paper['year']}_{safe_name}.pdf"
            if not out_file.exists():
                print(f"    >> Mengunduh PDF ke: {out_file}...")
                success = download_pdf(paper['pdf_url'], out_file)
                if success:
                    print(f"    [OK] Unduhan berhasil disimpan!")
                else:
                    print(f"    [FAIL] Tidak dapat mengunduh langsung dari link penerbit.")
            else:
                print(f"    [INFO] Berkas sudah ada di {out_file.name}")

    if args.output_json:
        out_p = Path(args.output_json)
        with open(out_p, "w", encoding="utf-8") as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
        print(f"\n[✓] Hasil pencarian disimpan ke: {out_p}")


if __name__ == "__main__":
    main()

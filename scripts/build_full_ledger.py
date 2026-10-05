#!/usr/bin/env python3
"""
Build Master Ledger with Hybrid Quality Scoring for Wiki PKN.
Merges OMP's 372 reviewed records, deterministically classifies the remaining
115 pending files, and runs the HybridQualityScorer across all 487 documents.

Zero token cost, runs 100% locally in under 3 seconds.
Output: data/wiki-pkn-full-ledger.json
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Import HybridQualityScorer
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.hybrid_quality_scorer import HybridQualityScorer


def compute_sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def extract_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Extract YAML frontmatter if present and return remaining body."""
    if not content.startswith("---"):
        return {}, content
    match = re.match(r"^---\n([\s\S]*?)\n---\n([\s\S]*)$", content)
    if not match:
        return {}, content
    raw_yaml, body = match.group(1), match.group(2)
    # Simple regex yaml parser for string/list fields
    fm: Dict[str, Any] = {}
    for line in raw_yaml.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key, val = key.strip(), val.strip()
            # Clean string quotes
            val = val.strip("'\"")
            if val.startswith("[") and val.endswith("]"):
                items = [x.strip(" '\"") for x in val[1:-1].split(",") if x.strip()]
                fm[key] = items
            else:
                fm[key] = val
    return fm, body


def extract_title(content: str, rel_path: str, fm: Dict[str, Any]) -> str:
    """Extract human-readable title from frontmatter, H1 heading, or filename."""
    if fm.get("title"):
        return str(fm["title"]).strip()

    # Search for first H1: # Title
    h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if h1_match:
        raw_title = h1_match.group(1).strip()
        # Clean markdown links, emojis, and styling
        clean = re.sub(r"\[\[([^\]|]+)\|?([^\]]*)\]\]", r"\2", raw_title)
        clean = re.sub(r"[\*\_]", "", clean)
        clean = re.sub(r"^[^\w\s]+", "", clean).strip()  # strip leading emojis
        if clean:
            return clean

    # Fallback to stem
    stem = Path(rel_path).stem
    return stem


def classify_pending_article(rel_path: str, content: str) -> Dict[str, Any]:
    """
    Deterministic rule-based classifier for the 115 pending files.
    Maps file path & content heuristics to Diataxis, Persona, JTBD, and Pillars.
    """
    path_lower = rel_path.lower()
    
    # 1. Bakat TB-40 Profiles (40+ profiles)
    if "/tb40/" in path_lower or "/bakat/tb40/" in path_lower:
        return {
            "diataxis": {
                "primary": "Reference",
                "secondary": ["Explanation"],
                "rationale": "Profil deskriptif rujukan takrif, ciri khas, dan indikator pilar bakat TB-40."
            },
            "persona": ["01", "02", "03", "05"],
            "jtbd": "Mengenal profil bakat spesifik anak atau santri dan memetakan potensi produktifnya.",
            "pillars": ["fitrah-dan-bakat"],
            "phases": ["0–7", "7–10", "10–15", "15+"]
        }

    # 2. Bakat Rumpun & Kuisioner
    if "/bakat/" in path_lower:
        if "kuisioner" in path_lower or "asesmen" in path_lower or "panduan" in path_lower:
            return {
                "diataxis": {
                    "primary": "How-to",
                    "secondary": ["Reference"],
                    "rationale": "Petunjuk teknis dan instrumen asesmen observasi bakat nabawiyah."
                },
                "persona": ["01", "02", "03a", "03b", "04"],
                "jtbd": "Melakukan asesmen dan observasi minat bakat santri/anak secara terstruktur.",
                "pillars": ["fitrah-dan-bakat", "praktik-keluarga"],
                "phases": ["7–10", "10–15", "15+"]
            }
        else:
            return {
                "diataxis": {
                    "primary": "Explanation",
                    "secondary": ["Reference"],
                    "rationale": "Uraian konseptual rumpun fitrah bakat dan manifestasi amalnya."
                },
                "persona": ["01", "02", "03"],
                "jtbd": "Memahami prinsip dasar fitrah bakat dan membedakannya dari tipologi sekuler.",
                "pillars": ["fitrah-dan-bakat"],
                "phases": ["7–10", "10–15", "15+"]
            }

    # 3. Toolkit KBM & Panduan Guru
    if "toolkit" in path_lower or "kbm" in path_lower:
        return {
            "diataxis": {
                "primary": "How-to",
                "secondary": ["Reference"],
                "rationale": "Instrumen operasional kegiatan belajar mengajar dan rubrik evaluasi guru."
            },
            "persona": ["03a", "03b", "04"],
            "jtbd": "Mengaplikasikan rubrik KBM dan instrumen pengajaran nabawiyah di ruang kelas.",
            "pillars": ["lembaga-dan-guru"],
            "phases": ["7–10", "10–15"]
        }

    # 4. Template Dokumen / RPP
    if "template" in path_lower:
        return {
            "diataxis": {
                "primary": "How-to",
                "secondary": ["Reference"],
                "rationale": "Templat standar penyusunan perencanaan pembelajaran dan tata kelola tarbiyah."
            },
            "persona": ["03a", "03b", "04"],
            "jtbd": "Menyusun dokumen rencana ajar atau modul pengasuhan berbasis format baku PKN.",
            "pillars": ["lembaga-dan-guru"],
            "phases": ["0–7", "7–10", "10–15", "15+"]
        }

    # 5. Referensi, Tokoh, Kitab, Glosarium
    if "referensi" in path_lower or "glosarium" in path_lower or "review buku" in path_lower:
        return {
            "diataxis": {
                "primary": "Reference",
                "secondary": ["Explanation"],
                "rationale": "Dokumentasi rujukan pustaka, kritik literatur, dan ensiklopedia istilah manhaj."
            },
            "persona": ["04", "05"],
            "jtbd": "Memverifikasi sanad literatur, kutipan kitab salaf, atau padanan istilah syar'i.",
            "pillars": ["dalil-dan-rujukan"],
            "phases": ["0–7", "7–10", "10–15", "15+"]
        }

    # 6. Renungan & Refleksi Jiwa
    if "renungan" in path_lower or "pembagian jiwa" in path_lower:
        return {
            "diataxis": {
                "primary": "Explanation",
                "secondary": [],
                "rationale": "Tadabbur filosofis dan penyucian jiwa (*tazkiyatun nafs*) dalam pendidikan."
            },
            "persona": ["01", "02"],
            "jtbd": "Menumbuhkan kedalaman empati jiwa dan kesadaran spiritual orang tua.",
            "pillars": ["praktik-keluarga"],
            "phases": ["0–7", "7–10", "10–15", "15+"]
        }

    # 7. Fase Usia, Tamyiz, Murahaqah, Thufulah
    if any(k in path_lower for k in ["thufulah", "tamyiz", "murahaqah", "fase", "perkembangan"]):
        return {
            "diataxis": {
                "primary": "Explanation",
                "secondary": ["How-to"],
                "rationale": "Pemetaan hukum syar'i dan tahapan psikologis anak sesuai rentang usia nabawiyah."
            },
            "persona": ["01", "02", "03"],
            "jtbd": "Mengetahui tuntutan pendidikan dan metode yang sah sesuai rentang usia anak.",
            "pillars": ["fase-usia"],
            "phases": ["0–7", "7–10", "10–15", "15+"]
        }

    # 8. Default fallback
    return {
        "diataxis": {
            "primary": "Explanation",
            "secondary": [],
            "rationale": "Uraian landasan dan metodologi Pendidikan Karakter Nabawiyah."
        },
        "persona": ["01", "02", "03"],
        "jtbd": "Mempelajari prinsip dan paradigma umum pendidikan karakter nabawiyah.",
        "pillars": ["mulai-di-sini"],
        "phases": ["0–7", "7–10", "10–15", "15+"]
    }


def main():
    parser = argparse.ArgumentParser(description="Build Wiki PKN Master Ledger with Hybrid Quality Scoring")
    parser.add_argument("--omp-cache", default="/tmp/wiki-pkn-omp-content.json", help="Path to OMP cached audit json")
    parser.add_argument("--content-dir", default="content", help="Directory containing markdown files")
    parser.add_argument("--output", default="data/wiki-pkn-full-ledger.json", help="Output JSON path")
    parser.add_argument("--min-score", type=float, default=70.0, help="Approval score threshold")
    args = parser.parse_args()

    t_start = time.perf_counter()

    # Load OMP cache if available
    omp_cache_map: Dict[str, Dict[str, Any]] = {}
    if os.path.exists(args.omp_cache):
        try:
            with open(args.omp_cache, "r", encoding="utf-8") as f:
                omp_raw = json.load(f)
            raw_ledger = omp_raw.get("ledger", [])
            for item in raw_ledger:
                if item.get("review_status") == "reviewed-full":
                    omp_cache_map[item["path"]] = item
            print(f"📦 Loaded {len(omp_cache_map)} fully reviewed records from OMP cache ({args.omp_cache}).")
        except Exception as e:
            print(f"⚠️ Warning: Failed to load OMP cache: {e}. Will classify all deterministically.")

    # Initialize Scorer
    scorer = HybridQualityScorer(pass_threshold=args.min_score)

    # Scan content directory
    content_path = Path(args.content_dir)
    md_files = sorted(list(content_path.rglob("*.md")))
    print(f"📂 Found {len(md_files)} markdown files in '{args.content_dir}/'.")

    ledger_entries: List[Dict[str, Any]] = []
    omp_reused_count = 0
    deterministic_count = 0

    scores_list: List[float] = []
    approved_count = 0
    needs_revision_count = 0

    diataxis_counter: Dict[str, int] = {}
    pillar_counter: Dict[str, int] = {}

    for md_path in md_files:
        rel_path = str(md_path.as_posix())
        try:
            with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Error reading {rel_path}: {e}")
            continue

        fm, body = extract_frontmatter(content)
        title = extract_title(content, rel_path, fm)
        sha256_hash = compute_sha256(content)
        file_bytes = len(content.encode("utf-8"))
        line_count = len(content.splitlines())

        # Determine Classification
        if rel_path in omp_cache_map:
            cached = omp_cache_map[rel_path]
            review_source = "omp_reviewed"
            omp_reused_count += 1
            diataxis = cached.get("diataxis", {})
            persona = cached.get("persona", [])
            jtbd = cached.get("jtbd", "")
            pillars = cached.get("pillars", [])
            phases = cached.get("phases", [])
            sources = cached.get("sources", [])
            evidence = cached.get("evidence", [])
            gaps = cached.get("gaps", [])
        else:
            classified = classify_pending_article(rel_path, content)
            review_source = "deterministic_classified"
            deterministic_count += 1
            diataxis = classified["diataxis"]
            persona = classified["persona"]
            jtbd = classified["jtbd"]
            pillars = classified["pillars"]
            phases = classified["phases"]
            sources = []
            evidence = []
            gaps = []

        # Tally metrics
        prim_diataxis = diataxis.get("primary", "Explanation")
        diataxis_counter[prim_diataxis] = diataxis_counter.get(prim_diataxis, 0) + 1
        for pil in pillars:
            pillar_counter[pil] = pillar_counter.get(pil, 0) + 1

        # Run Hybrid Quality Scorer
        eval_res = scorer.evaluate_document(content, rel_path)
        overall_score = eval_res["overall_score"]
        status = eval_res["status"]

        scores_list.append(overall_score)
        if status == "APPROVED":
            approved_count += 1
        else:
            needs_revision_count += 1

        # Structure final entry
        entry = {
            "path": rel_path,
            "title": title,
            "folder": str(md_path.parent.as_posix()),
            "sha256": sha256_hash,
            "bytes": file_bytes,
            "lines": line_count,
            "review_source": review_source,
            "diataxis": diataxis,
            "persona": persona,
            "jtbd": jtbd,
            "pillars": pillars,
            "phases": phases,
            "sources": sources,
            "evidence": evidence,
            "gaps": gaps,
            "quality": {
                "score": overall_score,
                "status": status,
                "linter_score": eval_res["layers"]["layer_1_linter"]["score"],
                "system_one_score": eval_res["layers"]["layer_2_system_one"]["score"],
                "decisions": eval_res["layers"]["layer_2_system_one"]["decisions"],
                "metrics": eval_res["layers"]["layer_1_linter"]["metrics"],
                "actionable_feedback": eval_res["actionable_feedback"]
            }
        }
        ledger_entries.append(entry)

    duration_total = time.perf_counter() - t_start

    # Build Master Ledger File
    avg_score = round(sum(scores_list) / len(scores_list), 2) if scores_list else 0.0

    master_ledger = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_documents": len(ledger_entries),
            "omp_reviewed_reused": omp_reused_count,
            "deterministic_completed": deterministic_count,
            "execution_duration_sec": round(duration_total, 2),
            "quality_summary": {
                "average_score": avg_score,
                "pass_threshold": args.min_score,
                "approved_count": approved_count,
                "approved_pct": round((approved_count / len(ledger_entries)) * 100, 1) if ledger_entries else 0.0,
                "needs_revision_count": needs_revision_count,
                "needs_revision_pct": round((needs_revision_count / len(ledger_entries)) * 100, 1) if ledger_entries else 0.0
            },
            "diataxis_distribution": diataxis_counter,
            "pillars_distribution": pillar_counter
        },
        "ledger": ledger_entries
    }

    # Ensure output directory exists
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(master_ledger, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 70)
    print("🎯 WIKI PKN MASTER LEDGER GENERATION COMPLETE")
    print("=" * 70)
    print(f"📄 Total Dokumen         : {len(ledger_entries)}")
    print(f"♻️ Reused dari OMP Cache : {omp_reused_count} berkas")
    print(f"⚡ Deterministic Selesai : {deterministic_count} berkas")
    print(f"⏱️ Waktu Eksekusi Total  : {duration_total:.2f} detik (Zero Token API)")
    print("-" * 70)
    print(f"📊 Rata-rata Skor        : {avg_score} / 100.0")
    print(f"✅ APPROVED (>= {args.min_score})   : {approved_count} ({master_ledger['metadata']['quality_summary']['approved_pct']}%)")
    print(f"⚠️ NEEDS_REVISION (< {args.min_score}) : {needs_revision_count} ({master_ledger['metadata']['quality_summary']['needs_revision_pct']}%)")
    print("-" * 70)
    print("📌 Distribusi Diátaxis:")
    for k, v in diataxis_counter.items():
        print(f"   • {k:12}: {v:3} dokumen ({v/len(ledger_entries)*100:.1f}%)")
    print("-" * 70)
    print(f"💾 File tersimpan di     : {out_path.resolve()}")
    print("=" * 70)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Batch Hi-Res Ingestion Worker for Wiki PKN.
Extracts searchable_pdfs/ and presentations/ sequentially using Unstructured API (hi_res),
tracks progress in a JSON log, handles timeouts/errors gracefully, and writes structured Markdown/JSON.
"""

import sys
import os
import time
import json
import logging
from pathlib import Path
from datetime import datetime

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from scripts.unstructured_adapter import UnstructuredAdapter

LOG_FILE = BASE_DIR / "data/batch_hires_progress.json"
OUTPUT_DIR = BASE_DIR / "data/extracted_elements"
LOG_TXT = BASE_DIR / "data/batch_hires.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_TXT, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

def load_progress() -> dict:
    if LOG_FILE.exists():
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logging.warning(f"Failed to read progress file: {e}")
    return {"started_at": datetime.now().isoformat(), "processed": {}, "stats": {"total": 0, "success": 0, "failed": 0, "skipped": 0}}

def save_progress(data: dict):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    adapter = UnstructuredAdapter(timeout=900) # 15 minutes timeout per file for large docs

    progress = load_progress()

    # Collect target files: PDFs first, then PPTXs
    pdf_dir = BASE_DIR / "searchable_pdfs"
    pptx_dir = BASE_DIR / "presentations"

    all_files = []
    if pdf_dir.exists():
        all_files.extend(sorted(list(pdf_dir.rglob("*.pdf"))))
    if pptx_dir.exists():
        all_files.extend(sorted(list(pptx_dir.rglob("*.pptx"))))

    progress["stats"]["total"] = len(all_files)
    save_progress(progress)

    logging.info(f"=== Starting Batch Ingestion (HI_RES Strategy) ===")
    logging.info(f"Total target files discovered: {len(all_files)} (PDFs & PPTXs)")
    logging.info(f"Target Output Directory: {OUTPUT_DIR}")

    success_cnt = progress["stats"].get("success", 0)
    failed_cnt = progress["stats"].get("failed", 0)
    skipped_cnt = progress["stats"].get("skipped", 0)

    for idx, file_path in enumerate(all_files, 1):
        rel_path = str(file_path.relative_to(BASE_DIR))
        file_size_mb = file_path.stat().st_size / (1024 * 1024)

        # Check if already processed
        if rel_path in progress["processed"] and progress["processed"][rel_path].get("status") == "success":
            logging.info(f"[{idx}/{len(all_files)}] SKIPPED (Already done): {rel_path}")
            skipped_cnt += 1
            continue

        logging.info(f"[{idx}/{len(all_files)}] PROCESSING ({file_size_mb:.2f} MB): {rel_path} ...")
        t0 = time.time()

        # Dynamic output subdirectory matching source tree
        sub_rel = file_path.relative_to(BASE_DIR).parent
        file_out_dir = OUTPUT_DIR / sub_rel

        try:
            res = adapter.process_file_with_cache(
                file_path=file_path,
                output_dir=file_out_dir,
                strategy="hi_res",
                force=False
            )
            elapsed = time.time() - t0
            elements_count = res.get("elements_count", 0)
            tables_count = res.get("tables_count", 0)

            logging.info(f"[{idx}/{len(all_files)}] ✓ SUCCESS in {elapsed:.1f}s -> {elements_count} elements, {tables_count} tables")

            progress["processed"][rel_path] = {
                "status": "success",
                "processed_at": datetime.now().isoformat(),
                "duration_seconds": round(elapsed, 2),
                "file_size_mb": round(file_size_mb, 2),
                "elements_count": elements_count,
                "tables_count": tables_count,
                "markdown_path": res.get("markdown_path"),
                "json_path": res.get("json_path")
            }
            success_cnt += 1

        except Exception as e:
            elapsed = time.time() - t0
            logging.error(f"[{idx}/{len(all_files)}] ✗ FAILED after {elapsed:.1f}s: {e}")
            progress["processed"][rel_path] = {
                "status": "failed",
                "attempted_at": datetime.now().isoformat(),
                "duration_seconds": round(elapsed, 2),
                "error": str(e)
            }
            failed_cnt += 1

        # Update stats
        progress["stats"]["success"] = success_cnt
        progress["stats"]["failed"] = failed_cnt
        progress["stats"]["skipped"] = skipped_cnt
        progress["last_updated"] = datetime.now().isoformat()
        save_progress(progress)

    logging.info(f"=== Batch Ingestion Complete ===")
    logging.info(f"Total: {len(all_files)}, Success: {success_cnt}, Failed: {failed_cnt}, Skipped: {skipped_cnt}")

if __name__ == "__main__":
    main()

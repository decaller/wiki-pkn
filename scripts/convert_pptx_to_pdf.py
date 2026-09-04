#!/usr/bin/env python3
import os
import subprocess
import sys

base_dir = os.path.abspath("old_backup")
missing = []

for root, _, files in os.walk(base_dir):
    if "/.git" in root:
        continue
    for f in files:
        if f.lower().endswith(".pptx"):
            base = os.path.splitext(f)[0]
            pdf_path = os.path.join(root, base + ".pdf")
            if not os.path.exists(pdf_path):
                missing.append((os.path.join(root, f), root))

print(f"Total files to convert: {len(missing)}")

for idx, (pptx_path, out_dir) in enumerate(missing, 1):
    print(f"[{idx}/{len(missing)}] Converting: {os.path.basename(pptx_path)}...", flush=True)
    cmd = [
        "flatpak", "run", "--filesystem=host",
        "org.libreoffice.LibreOffice",
        "--headless",
        "--convert-to", "pdf",
        pptx_path,
        "--outdir", out_dir
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error converting {pptx_path}: {res.stderr}", flush=True)
    else:
        print(f"Done: {res.stdout.strip()}", flush=True)

print("Batch conversion completed!", flush=True)

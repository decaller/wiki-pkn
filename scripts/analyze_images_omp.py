#!/usr/bin/env python3
"""
analyze_images_omp.py
Menganalisis seluruh 40 gambar foto di old_backup/Gambar/ menggunakan OMP (Oh My Pi)
dengan model vision (gemini-2.5-flash) untuk mendeteksi objek, aktivitas, tema, dan
relevansi kurikulum PKN, lalu menyimpannya ke data/gambar_properties.json.
"""

import os
import sys
import json
import re
import subprocess

IMAGE_DIR = "old_backup/Gambar"
OUTPUT_JSON = "data/gambar_properties.json"
MODEL = "gemini-2.5-flash"

SYSTEM_PROMPT = """Analisis gambar ini untuk kurikulum Pendidikan Karakter Nabawiyah (PKN).
Identifikasi secara objektif apa yang tampak pada foto:
1. Objek visual utama (orang, anak, ayah, ibu, buku, pemandangan, alat tukang, timbangan, olahraga, dll)
2. Aktivitas atau ekspresi
3. Suasana/konteks (belajar, keluarga, alam bebas, kerja keras, kepemimpinan, hukum/keadilan, refleksi, dll)
4. Relevansi pilar atau topik kurikulum PKN yang paling cocok

Balas HANYA dalam format JSON valid berikut (tanpa markdown tambahan):
{
  "deskripsi": "penjelasan singkat isi gambar 1-2 kalimat",
  "objek": ["daftar", "objek", "terlihat"],
  "aktivitas": "aktivitas yang sedang berlangsung",
  "suasana": "suasana atau mood",
  "kata_kunci": ["keyword1", "keyword2", "keyword3"],
  "topik_pkn": ["topik atau pilar PKN yang cocok"],
  "saran_halaman": ["nama topik/konsep artikel PKN yang paling sesuai"]
}
"""

def extract_json(text):
    text = text.strip()
    if text.startswith("Working..."):
        text = text[len("Working..."):].strip()
    # Try markdown json block
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        text = match.group(1).strip()
    # Find outer curly braces
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1:
        text = text[start:end+1]
    return json.loads(text)

def main():
    properties = {}
    if os.path.exists(OUTPUT_JSON):
        try:
            with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
                properties = json.load(f)
            print(f"[*] Loaded existing cache with {len(properties)} entries.")
        except Exception:
            properties = {}

    files = [f"x{i}.jpg" for i in range(1, 41)]
    print(f"[*] Analyzing {len(files)} images using omp ({MODEL})...")

    for idx, filename in enumerate(files, 1):
        image_path = os.path.join(IMAGE_DIR, filename)
        if not os.path.exists(image_path):
            continue

        key = filename.split(".")[0]
        if key in properties and "deskripsi" in properties[key]:
            print(f"  [{idx:02d}/40] {filename} (Cached): {properties[key]['deskripsi'][:60]}...")
            continue

        print(f"  [{idx:02d}/40] Analyzing {filename}...", end=" ", flush=True)

        cmd = [
            "omp",
            "-p",
            "--model", MODEL,
            SYSTEM_PROMPT,
            f"@{image_path}"
        ]

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            data = extract_json(res.stdout)
            data["id"] = key
            data["file_asli"] = filename
            data["banner_file"] = f"banner-{idx:02d}.webp"
            properties[key] = data

            # Save immediately on each step
            with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
                json.dump(properties, f, indent=2, ensure_ascii=False)

            print(f"✓ {data.get('deskripsi', '')[:50]}...")

        except Exception as e:
            print(f"✗ Error: {e}")

    print(f"\n[✓] Finished! Saved metadata for {len(properties)} images to {OUTPUT_JSON}.")

if __name__ == "__main__":
    main()

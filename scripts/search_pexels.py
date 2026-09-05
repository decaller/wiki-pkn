#!/home/abuhafi/Project/wiki-pkn/pexels-mcp-server/.venv/bin/python3
"""
Pexels Search & Download Utility for Wiki PKN
Includes Islamic Compliance Verification:
- STRICT RULE 1: No women or girls pictured.
- STRICT RULE 2: All human figures must cover aurat (no shirtless, no shorts, modest attire).
- PREFERRED: Architecture (mosques, courtyards, historic cities), nature (mountains, skies, stars, rivers),
             objects (books, Quran, calligraphy, pens, scales, lanterns, tools, maps).
- AI Vision Verification via OMP (gemini-2.5-flash) to automatically audit candidate images before saving.
"""

import os
import sys
import json
import re
import argparse
import subprocess
import tempfile
import requests
from pathlib import Path
from PIL import Image
import io
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
PEXELS_DIR = ROOT / "pexels-mcp-server"

# Load .env from pexels-mcp-server/.env or root .env
load_dotenv(PEXELS_DIR / ".env")
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("PEXELS_API_KEY", "")
BASE_URL = "https://api.pexels.com/v1"
OMP_BIN = "/home/abuhafi/.local/bin/omp"

ISLAMIC_AUDIT_PROMPT = """Analisis gambar ini secara sangat teliti untuk website pendidikan Islam (Wiki PKN) dengan aturan syariat ketat:

KRITERIA WAJIB:
1. TIDAK BOLEH menampilkan wanita atau anak perempuan sama sekali (dewasa maupun anak-anak).
2. TIDAK BOLEH menampilkan aurat manusia (contoh DILARANG: pria tanpa baju/shirtless, celana pendek di atas lutut, pakaian ketat/terbuka, pakaian renang).
3. TIDAK BOLEH mengandung patung makhluk bernyawa, berhala, salib, atau simbol keagamaan non-Islam.
4. GAMBAR YANG DIPERBOLEHKAN:
   - Alam semesta (langit, gunung, bintang, laut, gurun, pohon).
   - Arsitektur (masjid, kubah, menara, pilar, perpustakaan, kota).
   - Objek & alat (buku, mushaf, kaligrafi, pena, timbangan, lentera, kompas, jam).
   - Pria/anak laki-laki yang berpakaian sopan menutup aurat sempurna (baju lengan, celana panjang/gamis).

Balas HANYA format JSON valid berikut tanpa teks tambahan:
{
  "compliant": true,
  "has_women_or_girls": false,
  "has_exposed_aurat": false,
  "reason": "Alasan kepatuhan atau pelanggaran singkat",
  "recommended_pkn_topic": "Topik PKN yang cocok jika compliant"
}
"""

def check_api_key():
    if not API_KEY or API_KEY == "your-api-key-here":
        print("[ERROR] PEXELS_API_KEY is not set or still default.")
        print(f"Please set your PEXELS_API_KEY in {PEXELS_DIR}/.env or export PEXELS_API_KEY='...'")
        print("You can get a free API key instantly at: https://www.pexels.com/api/")
        sys.exit(1)

def extract_json(text):
    text = text.strip()
    if text.startswith("Working..."):
        text = text[len("Working..."):].strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        text = match.group(1).strip()
    try:
        return json.loads(text)
    except Exception:
        first_brace = text.find("{")
        last_brace = text.rfind("}")
        if first_brace != -1 and last_brace != -1:
            try:
                return json.loads(text[first_brace:last_brace+1])
            except Exception:
                pass
    return None

def verify_image_compliance(image_path_or_bytes):
    """Run OMP vision model on the image to ensure Islamic compliance."""
    if not os.path.exists(OMP_BIN):
        print(f"[WARN] OMP not found at {OMP_BIN}. Skipping automated AI vision audit.")
        return {"compliant": True, "reason": "OMP not installed, manual check advised."}

    # Save to temp file if bytes
    temp_file = None
    if isinstance(image_path_or_bytes, bytes):
        temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        temp_file.write(image_path_or_bytes)
        temp_file.close()
        image_path = temp_file.name
    else:
        image_path = str(image_path_or_bytes)

    try:
        cmd = [
            OMP_BIN, "-p",
            "--model", "gemini-2.5-flash",
            ISLAMIC_AUDIT_PROMPT,
            f"@{image_path}"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
        if res.returncode != 0:
            return {"compliant": False, "reason": f"OMP audit error: {res.stderr.strip()}"}

        result = extract_json(res.stdout)
        if result:
            return result
        return {"compliant": False, "reason": f"Could not parse OMP vision output: {res.stdout[:150]}"}
    finally:
        if temp_file and os.path.exists(temp_file.name):
            os.remove(temp_file.name)

def search_photos(query, orientation="landscape", per_page=10, page=1, verify=False):
    check_api_key()
    headers = {"Authorization": API_KEY}
    params = {
        "query": query,
        "orientation": orientation,
        "per_page": per_page,
        "page": page
    }
    resp = requests.get(f"{BASE_URL}/search", headers=headers, params=params, timeout=15)
    if resp.status_code != 200:
        print(f"[ERROR] API returned {resp.status_code}: {resp.text}")
        sys.exit(1)
    return resp.json()

def download_and_crop(photo_url, output_path, target_width=1050, target_height=350, skip_verify=False):
    resp = requests.get(photo_url, timeout=30)
    resp.raise_for_status()
    raw_bytes = resp.content

    if not skip_verify:
        print("[AUDIT] Running Islamic Compliance Vision Audit (OMP gemini-2.5-flash)...")
        audit = verify_image_compliance(raw_bytes)
        if not audit.get("compliant", False):
            print("\n" + "="*60)
            print("[REJECTED] Image DOES NOT comply with Islamic guidelines:")
            print(f"  Reason: {audit.get('reason')}")
            print(f"  Has women/girls: {audit.get('has_women_or_girls')}")
            print(f"  Has exposed aurat: {audit.get('has_exposed_aurat')}")
            print("="*60 + "\n")
            sys.exit(1)
        else:
            print(f"[PASSED] Compliant with Islamic guidelines: {audit.get('reason')}")

    img = Image.open(io.BytesIO(raw_bytes)).convert("RGB")
    src_w, src_h = img.size
    target_ratio = target_width / target_height
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        new_w = int(src_h * target_ratio)
        offset_x = (src_w - new_w) // 2
        crop_box = (offset_x, 0, offset_x + new_w, src_h)
    else:
        new_h = int(src_w / target_ratio)
        offset_y = (src_h - new_h) // 2
        crop_box = (0, offset_y, src_w, offset_y + new_h)

    cropped = img.crop(crop_box)
    resized = cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    resized.save(output_path, "WEBP", quality=85)
    print(f"[OK] Saved cropped banner to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Search and download Pexels photos for Wiki PKN (with Islamic Compliance Rules)")
    subparsers = parser.add_subparsers(dest="command")

    # Search command
    search_p = subparsers.add_parser("search", help="Search photos on Pexels")
    search_p.add_argument("query", help="Search query (e.g., 'islamic library', 'mosque architecture', 'night sky stars')")
    search_p.add_argument("--orientation", default="landscape", choices=["landscape", "portrait", "square"])
    search_p.add_argument("--count", type=int, default=5, help="Number of results to display")
    search_p.add_argument("--verify", action="store_true", help="Audit each search result with AI Vision for Islamic compliance")

    # Download command
    dl_p = subparsers.add_parser("download", help="Download, audit Islamic compliance, and crop photo to 1050x350 WebP")
    dl_p.add_argument("url", help="Direct image URL or Pexels photo ID")
    dl_p.add_argument("output", help="Filename or path relative to content/assets/banners/")
    dl_p.add_argument("--skip-verify", action="store_true", help="Bypass automated Islamic compliance audit")

    # Audit command
    audit_p = subparsers.add_parser("audit", help="Audit an existing local image or URL for Islamic compliance")
    audit_p.add_argument("target", help="File path or URL of image to audit")

    args = parser.parse_args()

    if args.command == "search":
        data = search_photos(args.query, orientation=args.orientation, per_page=args.count)
        print(f"\nFound {data.get('total_results', 0)} photos for '{args.query}':\n")
        for i, photo in enumerate(data.get("photos", []), 1):
            pid = photo["id"]
            photographer = photo["photographer"]
            alt = photo.get("alt", "(No description)")
            preview_url = photo["src"]["medium"]
            large_url = photo["src"]["large2x"]

            verdict = ""
            if args.verify:
                print(f"Auditing [{i}] {pid} with OMP vision...")
                try:
                    resp = requests.get(preview_url, timeout=10)
                    audit = verify_image_compliance(resp.content)
                    if audit.get("compliant", False):
                        verdict = f" -> [PASSED: {audit.get('reason')}]"
                    else:
                        verdict = f" -> [REJECTED: {audit.get('reason')}]"
                except Exception as e:
                    verdict = f" -> [AUDIT ERROR: {e}]"

            print(f"[{i}] ID: {pid} | Photographer: {photographer}{verdict}")
            print(f"    Desc: {alt}")
            print(f"    URL : {large_url}\n")

    elif args.command == "download":
        check_api_key()
        out_path = Path(args.output)
        if not out_path.is_absolute():
            out_path = ROOT / "content" / "assets" / "banners" / args.output
        if not str(out_path).endswith(".webp"):
            out_path = out_path.with_suffix(".webp")
        download_and_crop(args.url, out_path, skip_verify=args.skip_verify)

    elif args.command == "audit":
        if args.target.startswith("http://") or args.target.startswith("https://"):
            resp = requests.get(args.target, timeout=15)
            audit = verify_image_compliance(resp.content)
        else:
            audit = verify_image_compliance(Path(args.target))
        print(json.dumps(audit, indent=2, ensure_ascii=False))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()

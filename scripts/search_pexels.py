#!/usr/bin/env python3
"""
Pexels Search & Download Utility for Wiki PKN
Utilizes pexels-mcp-server environment or PEXELS_API_KEY.
"""

import os
import sys
import argparse
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

def check_api_key():
    if not API_KEY or API_KEY == "your-api-key-here":
        print("[ERROR] PEXELS_API_KEY is not set or still default.")
        print(f"Please set your PEXELS_API_KEY in {PEXELS_DIR}/.env or export PEXELS_API_KEY='...'")
        print("You can get a free API key instantly at: https://www.pexels.com/api/")
        sys.exit(1)

def search_photos(query, orientation="landscape", per_page=10, page=1):
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

def download_and_crop(photo_url, output_path, target_width=1050, target_height=350):
    resp = requests.get(photo_url, timeout=30)
    resp.raise_for_status()
    
    img = Image.open(io.BytesIO(resp.content)).convert("RGB")
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
    parser = argparse.ArgumentParser(description="Search and download Pexels photos for Wiki PKN")
    subparsers = parser.add_subparsers(dest="command")

    # Search command
    search_p = subparsers.add_parser("search", help="Search photos on Pexels")
    search_p.add_argument("query", help="Search query (e.g., 'islamic library', 'father teaching son')")
    search_p.add_argument("--orientation", default="landscape", choices=["landscape", "portrait", "square"])
    search_p.add_argument("--count", type=int, default=5, help="Number of results to display")

    # Download command
    dl_p = subparsers.add_parser("download", help="Download and crop photo to 1050x350 WebP")
    dl_p.add_argument("url", help="Direct image URL or Pexels photo ID")
    dl_p.add_argument("output", help="Filename or path relative to content/assets/banners/")

    args = parser.parse_args()

    if args.command == "search":
        data = search_photos(args.query, orientation=args.orientation, per_page=args.count)
        print(f"\nFound {data.get('total_results', 0)} photos for '{args.query}':\n")
        for i, photo in enumerate(data.get("photos", []), 1):
            pid = photo["id"]
            photographer = photo["photographer"]
            alt = photo.get("alt", "(No description)")
            large_url = photo["src"]["large2x"]
            print(f"[{i}] ID: {pid} | Photographer: {photographer}")
            print(f"    Desc: {alt}")
            print(f"    URL : {large_url}\n")
    elif args.command == "download":
        check_api_key()
        out_path = Path(args.output)
        if not out_path.is_absolute():
            out_path = ROOT / "content" / "assets" / "banners" / args.output
        if not str(out_path).endswith(".webp"):
            out_path = out_path.with_suffix(".webp")
        download_and_crop(args.url, out_path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

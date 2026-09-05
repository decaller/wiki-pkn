#!/usr/bin/env python3
"""
generate_horizontal_banners.py
Memproses 40 foto di old_backup/Gambar/ menjadi horizontal banner 1050x350px (tinggi 350px, rasio 3:1)
dalam format WebP yang ringan dan berkualitas tinggi untuk halaman-halaman Wiki PKN.
"""

import os
import sys
from PIL import Image, ImageOps

INPUT_DIR = "old_backup/Gambar"
OUTPUT_DIR = "content/assets/banners"
TARGET_WIDTH = 1050
TARGET_HEIGHT = 350
QUALITY = 85

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    total_processed = 0
    total_bytes = 0

    print(f"[*] Processing images from {INPUT_DIR} to {OUTPUT_DIR} ({TARGET_WIDTH}x{TARGET_HEIGHT} px)...")

    for i in range(1, 41):
        filename = f"x{i}.jpg"
        input_path = os.path.join(INPUT_DIR, filename)
        if not os.path.exists(input_path):
            continue

        out_name = f"banner-{i:02d}.webp"
        output_path = os.path.join(OUTPUT_DIR, out_name)

        try:
            with Image.open(input_path) as im:
                # Correct orientation if EXIF present
                im = ImageOps.exif_transpose(im)
                
                # Convert to RGB if palette or RGBA
                if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
                    bg = Image.new('RGB', im.size, (255, 255, 255))
                    bg.paste(im, mask=im.split()[-1] if im.mode in ('RGBA', 'LA') else None)
                    im = bg
                elif im.mode != 'RGB':
                    im = im.convert('RGB')

                # Smart center-crop to 1050x350 with upper-center focus (0.5, 0.42) for portraits/landscapes
                banner = ImageOps.fit(
                    im,
                    (TARGET_WIDTH, TARGET_HEIGHT),
                    method=Image.Resampling.LANCZOS,
                    centering=(0.5, 0.42)
                )

                banner.save(output_path, "WEBP", quality=QUALITY, method=6)
                size_kb = os.path.getsize(output_path) / 1024
                total_bytes += os.path.getsize(output_path)
                total_processed += 1
                print(f"  [+] {filename:7} -> {out_name:15} | {banner.size[0]}x{banner.size[1]} | {size_kb:.1f} KB")

        except Exception as e:
            print(f"  [!] Error processing {filename}: {e}", file=sys.stderr)

    print(f"\n[✓] Completed: {total_processed} banners generated in {OUTPUT_DIR} (Total: {total_bytes/1024:.1f} KB).")

if __name__ == "__main__":
    main()

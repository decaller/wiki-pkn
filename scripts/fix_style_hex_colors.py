#!/usr/bin/env python3
"""
fix_style_hex_colors.py - Mengonversi kode warna hex (#hex) di dalam atribut HTML style="..."
menjadi format rgb(...) di seluruh berkas Markdown Wiki-PKN.
Mencegah Quartz micromark OFM parser mengira #hex sebagai markdown tag/hashtag.
"""

import glob
import re
import os

CONTENT_DIR = "content"

def hex_to_rgb(hex_code):
    h = hex_code.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    return f"rgb({r}, {g}, {b})"

def fix_style_attributes_in_content():
    files = glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)
    total_replaced = 0
    modified_files = 0

    # Pattern to find style attributes in HTML tags
    # Matches style="...", style='...'
    style_attr_pattern = re.compile(r'(style\s*=\s*["\'])([^"\']+)(["\'])', re.IGNORECASE)

    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as fp:
            orig = fp.read()

        def style_replacer(match):
            prefix = match.group(1)
            style_content = match.group(2)
            suffix = match.group(3)

            # Replace any #hex color (3 or 6 hex digits) within the style content
            def hex_replacer(h_match):
                nonlocal count_file
                count_file += 1
                return hex_to_rgb(h_match.group(0))

            new_style_content = re.sub(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b', hex_replacer, style_content)
            return f"{prefix}{new_style_content}{suffix}"

        count_file = 0
        new_text = style_attr_pattern.sub(style_replacer, orig)

        if count_file > 0:
            with open(fpath, "w", encoding="utf-8") as fp:
                fp.write(new_text)
            total_replaced += count_file
            modified_files += 1

    print(f"[fix_style_hex_colors] Berhasil mengonversi {total_replaced} kode warna hex di {modified_files} berkas!")

if __name__ == "__main__":
    fix_style_attributes_in_content()

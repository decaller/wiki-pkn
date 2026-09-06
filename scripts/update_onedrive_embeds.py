import os
import glob
import re
import json

with open("data/onedrive_embed_tokens.json", "r", encoding="utf-8") as f:
    tokens = json.load(f)

md_files = glob.glob("content/**/*.md", recursive=True)
updated_files = 0
total_replacements = 0

for filepath in md_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    
    # 1. Update iframe src:
    # Pattern: src="https://view.officeapps.live.com/op/embed.aspx?src=https%3A%2F%2Fwikipkn.insanmustaqbal.or.id%2Fpresentations%2F([^&"]+\.pptx)"
    def replace_iframe(match):
        filename = match.group(1)
        if filename in tokens:
            embed_url = tokens[filename]
            return f'src="{embed_url}?em=2&amp;wdAr=1.7777777777777777"'
        return match.group(0)

    content = re.sub(
        r'src="https://view\.officeapps\.live\.com/op/embed\.aspx\?src=https%3A%2F%2Fwikipkn\.insanmustaqbal\.or\.id%2Fpresentations%2F([^&"]+\.pptx)"',
        replace_iframe,
        content
    )

    # 2. Update Buka Layar Penuh links:
    # Pattern: href="https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fwikipkn.insanmustaqbal.or.id%2Fpresentations%2F([^&"]+\.pptx)"
    def replace_view_link(match):
        filename = match.group(1)
        if filename in tokens:
            embed_url = tokens[filename]
            return f'href="{embed_url}?em=2"'
        return match.group(0)

    content = re.sub(
        r'href="https://view\.officeapps\.live\.com/op/view\.aspx\?src=https%3A%2F%2Fwikipkn\.insanmustaqbal\.or\.id%2Fpresentations%2F([^&"]+\.pptx)"',
        replace_view_link,
        content
    )

    # Label updates: (Office Online) -> (PowerPoint Online)
    content = content.replace("🖥️ Buka di Office Online", "🖥️ Buka di PowerPoint Online")
    content = content.replace("🖥️ Buka Layar Penuh (Office Online)", "🖥️ Buka Layar Penuh (PowerPoint Online)")

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_files += 1
        print(f"Updated: {filepath}")

print(f"\nFinished! Total updated files: {updated_files}")

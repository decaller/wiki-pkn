#!/usr/bin/env python3
"""
ingest_sotab_articles.py
Mengunduh 121 artikel resmi Sekolah Orangtua Ayah Bunda Hebat Indonesia (SOTAB)
karya Ustadz Abdul Kholik dari WordPress REST API dan mengompilasinya ke format Markdown Quartz v5
lengkap dengan Progressive Disclosure, metadata sumber, dan taksonomi PKN.
"""

import os
import json
import re
import urllib.request
from bs4 import BeautifulSoup

SOTAB_API_BASE = "https://sotabh.com/wp-json/wp/v2/posts"
OUTPUT_DIR = "content/Materi SOTAB"

def clean_html_to_markdown(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Remove unwanted tags
    for tag in soup(["script", "style"]):
        tag.decompose()
        
    # Convert blockquotes
    for bq in soup.find_all("blockquote"):
        text = bq.get_text(separator="\n").strip()
        lines = [f"> {line}" for line in text.split("\n")]
        bq.replace_with("\n" + "\n".join(lines) + "\n")
        
    # Convert headings
    for h in soup.find_all(["h1", "h2", "h3", "h4"]):
        level = int(h.name[1])
        text = h.get_text(strip=True)
        h.replace_with(f"\n{'#' * level} {text}\n")
        
    # Convert paragraphs
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        p.replace_with(f"\n\n{text}\n\n")
        
    # Get raw text
    text = soup.get_text()
    # Normalize multiple linebreaks
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text

def sanitize_filename(title):
    title = re.sub(r'[\\/*?:"<>|]', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def fetch_all_posts():
    posts = []
    page = 1
    while True:
        url = f"{SOTAB_API_BASE}?per_page=100&page={page}"
        print(f"Fetching SOTAB posts page {page}...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Wiki-PKN Ingester)"})
            with urllib.request.urlopen(req, timeout=30) as res:
                data = json.loads(res.read().decode("utf-8"))
                if not data:
                    break
                posts.extend(data)
                total_pages = int(res.headers.get("X-WP-TotalPages", 1))
                if page >= total_pages:
                    break
                page += 1
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break
    return posts

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    posts = fetch_all_posts()
    print(f"Total posts fetched: {len(posts)}")
    
    saved_count = 0
    for p in posts:
        post_id = p.get("id")
        title = BeautifulSoup(p.get("title", {}).get("rendered", ""), "html.parser").get_text().strip()
        if not title:
            title = f"Artikel-SOTAB-{post_id}"
            
        slug = p.get("slug", "")
        date = p.get("date", "")
        link = p.get("link", "")
        raw_html = p.get("content", {}).get("rendered", "")
        
        md_body = clean_html_to_markdown(raw_html)
        if not md_body or len(md_body) < 50:
            continue
            
        # Extract first paragraph as summary hook
        paragraphs = [p for p in md_body.split("\n\n") if p.strip() and not p.strip().startswith("#") and not p.strip().startswith(">")]
        hook = paragraphs[0] if paragraphs else "Materi pengasuhan dan pendidikan karakter nabawiyah SOTAB."
        if len(hook) > 280:
            hook = hook[:277] + "..."
            
        filename = f"{sanitize_filename(title)}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Assemble Quartz v5 Progressive Disclosure template
        quartz_md = f"""---
title: "{title}"
date: "{date}"
tags:
  - SOTAB
  - PendidikanKarakterNabawiyah
  - AbdulKholik
  - ParentingNabawiyah
sources:
  - url: "{link}"
    title: "{title}"
    author: "Ustadz Abdul Kholik, S.Pd"
    platform: "SOTAB HEBAT (Sekolah Orangtua Ayah Bunda Hebat Indonesia)"
    authority: 0.85
---

> [!abstract] Intisari & Hook (Layer 1)
> **Pesan Pokok:** {hook}
> **Penulis/Konseptor:** Ustadz Abdul Kholik, S.Pd
> **Sumber Asli:** [SOTAB HEBAT]({link})

## Uraian Materi Lengkap

{md_body}

---

## Hubungan & Penautan Konsep
- Kembali ke: [[Indeks Utama]] | [[Materi SOTAB]]
- Terkait: [[4 Etape Usia Nabawiyah]] | [[Koneksi Sebelum Koreksi]] | [[Tazkiyatun Nafs]]
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(quartz_md)
        saved_count += 1

    print(f"Successfully generated {saved_count} SOTAB article pages in '{OUTPUT_DIR}'!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
scripts/fetch_skis_articles.py
Mengunduh dan mengonversi seluruh artikel dan halaman dari https://sekolahkarakter.com/
ke format Markdown di old_backup/skis/artikel/ dan old_backup/skis/pages/
lengkap dengan metadata frontmatter, articles.json, dan README.md indeks.
"""

import os
import re
import json
import time
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup, NavigableString

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "old_backup", "skis")
ARTIKEL_DIR = os.path.join(OUTPUT_DIR, "artikel")
PAGES_DIR = os.path.join(OUTPUT_DIR, "pages")

os.makedirs(ARTIKEL_DIR, exist_ok=True)
os.makedirs(PAGES_DIR, exist_ok=True)

def fetch_url(url, retries=3, delay=1.0):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                print(f"  [ERROR] Gagal mengunduh {url}: {e}")
                return None

def get_sitemap_urls(sitemap_url):
    xml_content = fetch_url(sitemap_url)
    if not xml_content:
        return []
    soup = BeautifulSoup(xml_content, "xml")
    urls = []
    for loc in soup.find_all("loc"):
        url = loc.text.strip()
        # Filter out images and assets
        if not any(url.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".pdf", ".zip"]):
            urls.append(url)
    return urls

def elem_to_markdown(elem):
    if elem is None:
        return ""
    
    # Remove unwanted elements first
    for unwanted in elem.find_all(["script", "style", "noscript", "form", "iframe"]):
        unwanted.decompose()
    for share in elem.find_all(class_=lambda c: c and any(w in c for w in ["share", "social", "jp-relatedposts", "author-bio", "nav-links", "comments"])):
        share.decompose()
        
    def walk(node):
        if isinstance(node, NavigableString):
            return str(node)
        
        tag = node.name
        if not tag:
            return ""
            
        if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            level = int(tag[1])
            inner = "".join(walk(c) for c in node.children).strip()
            return f"\n\n{'#' * level} {inner}\n\n"
            
        elif tag == "p":
            inner = "".join(walk(c) for c in node.children).strip()
            return f"\n\n{inner}\n\n" if inner else ""
            
        elif tag == "blockquote":
            inner = "".join(walk(c) for c in node.children).strip()
            lines = inner.splitlines()
            quoted = "\n".join(f"> {l}" for l in lines)
            return f"\n\n{quoted}\n\n"
            
        elif tag in ["ul", "ol"]:
            is_ol = (tag == "ol")
            res = ["\n\n"]
            idx = 1
            for li in node.find_all("li", recursive=False):
                li_text = "".join(walk(c) for c in li.children).strip()
                prefix = f"{idx}. " if is_ol else "* "
                res.append(f"{prefix}{li_text}\n")
                idx += 1
            res.append("\n")
            return "".join(res)
            
        elif tag == "li":
            return "".join(walk(c) for c in node.children).strip()
            
        elif tag in ["strong", "b"]:
            inner = "".join(walk(c) for c in node.children).strip()
            return f"**{inner}**" if inner else ""
            
        elif tag in ["em", "i"]:
            inner = "".join(walk(c) for c in node.children).strip()
            return f"*{inner}*" if inner else ""
            
        elif tag == "a":
            href = node.get("href", "")
            inner = "".join(walk(c) for c in node.children).strip()
            if inner and href and not href.startswith("javascript:"):
                return f"[{inner}]({href})"
            return inner
            
        elif tag == "img":
            src = node.get("src", "")
            alt = node.get("alt", "Gambar")
            return f"\n\n![{alt}]({src})\n\n" if src else ""
            
        elif tag == "br":
            return "\n"
            
        elif tag == "hr":
            return "\n\n---\n\n"
            
        elif tag in ["div", "section", "article", "span", "figure"]:
            return "".join(walk(c) for c in node.children)
            
        else:
            return "".join(walk(c) for c in node.children)

    raw_md = walk(elem)
    # Clean multiple empty lines
    cleaned = re.sub(r"\n{3,}", "\n\n", raw_md).strip()
    return cleaned

def parse_post(url, html, is_page=False):
    soup = BeautifulSoup(html, "html.parser")
    
    # Extract Title
    title = ""
    h1 = soup.find("h1")
    if h1:
        title = h1.text.strip()
    elif soup.find("title"):
        title = soup.find("title").text.split("-")[0].strip()
        
    # Extract Dates
    pub_date = ""
    mod_date = ""
    time_pub = soup.find("meta", property="article:published_time")
    if time_pub:
        pub_date = time_pub.get("content", "")
    time_mod = soup.find("meta", property="article:modified_time")
    if time_mod:
        mod_date = time_mod.get("content", "")
    if not pub_date:
        t_tag = soup.find("time")
        if t_tag:
            pub_date = t_tag.text.strip()

    # Extract Author
    author = "Ustadz Abdul Kholiq (SKIS)"
    meta_author = soup.find("meta", attrs={"name": "author"})
    if meta_author:
        author_val = meta_author.get("content", "").strip()
        if author_val and author_val.lower() != "admin":
            author = author_val

    # Extract Categories & Tags
    categories = []
    tags = []
    art_tag = soup.find("article")
    if art_tag:
        classes = art_tag.get("class", [])
        for c in classes:
            if c.startswith("category-"):
                categories.append(c.replace("category-", "").replace("-", " ").title())
            elif c.startswith("tag-"):
                tags.append(c.replace("tag-", "").replace("-", " "))
    
    # Also check rel links
    for a in soup.find_all("a", rel=lambda r: r and "category" in r):
        cat = a.text.strip()
        if cat and cat not in categories:
            categories.append(cat)
    for a in soup.find_all("a", rel=lambda r: r and "tag" in r):
        t = a.text.strip()
        if t and t not in tags:
            tags.append(t)

    # Extract Content
    content_node = None
    if art_tag:
        content_node = art_tag.find(class_=lambda c: c and "entry-content" in c)
        if not content_node:
            content_node = art_tag
    if not content_node:
        content_node = soup.find(class_=lambda c: c and any(w in c for w in ["entry-content", "post-content", "site-content"]))

    body_md = elem_to_markdown(content_node) if content_node else ""
    
    # Generate Slug
    parsed = urlparse(url)
    slug = parsed.path.strip("/").split("/")[-1]
    if not slug:
        slug = "index"

    return {
        "title": title,
        "date": pub_date,
        "modified": mod_date,
        "author": author,
        "categories": categories,
        "tags": tags,
        "url": url,
        "slug": slug,
        "content_length": len(body_md),
        "body_md": body_md,
        "is_page": is_page
    }

def main():
    print("=== CRAWLER SEKOLAH KARAKTER IMAM SYAFI'I (SKIS) ===")
    
    # 1. Dapatkan daftar URL artikel dan halaman
    post_urls = get_sitemap_urls("https://sekolahkarakter.com/post-sitemap.xml")
    page_urls = get_sitemap_urls("https://sekolahkarakter.com/page-sitemap.xml")
    
    # Filter page URLs yang relevan (profil, visi, kurikulum, dsb)
    ignored_slugs = ["hubungi-kami", "privacy-policy", "auto-draft", "footer", "home-extra", "home-2", "coming"]
    filtered_page_urls = [
        u for u in page_urls 
        if not any(ign in u for ign in ignored_slugs) and u.strip("/") != "https://sekolahkarakter.com"
    ]
    
    print(f"Total post URLs: {len(post_urls)}")
    print(f"Total relevant page URLs: {len(filtered_page_urls)}")
    
    all_records = []
    
    # 2. Unduh dan proses semua artikel blog
    print("\n--- Mengunduh dan Memproses Artikel Blog ---")
    for i, url in enumerate(post_urls, 1):
        parsed = urlparse(url)
        slug = parsed.path.strip("/").split("/")[-1]
        out_file = os.path.join(ARTIKEL_DIR, f"{slug}.md")
        
        print(f"[{i}/{len(post_urls)}] {slug} ... ", end="", flush=True)
        html = fetch_url(url)
        if not html:
            continue
            
        data = parse_post(url, html, is_page=False)
        if not data["body_md"]:
            print("KOSONG (Dilewati)")
            continue
            
        # Tulis Markdown
        frontmatter = [
            "---",
            f'title: {json.dumps(data["title"], ensure_ascii=False)}',
            f'date: "{data["date"]}"',
            f'modified: "{data["modified"]}"',
            f'author: "{data["author"]}"',
            f'url: "{data["url"]}"',
            f'slug: "{data["slug"]}"',
            "categories:",
        ]
        for c in (data["categories"] or ["Artikel"]):
            frontmatter.append(f"  - {c}")
        if data["tags"]:
            frontmatter.append("tags:")
            for t in data["tags"]:
                frontmatter.append(f"  - {t}")
        frontmatter.append("---\n")
        
        body = [
            f'# {data["title"]}\n',
            f'*Dipublikasikan pada: {data["date"]} | Penulis: {data["author"]} | Sumber: [{data["url"]}]({data["url"]})*\n',
            "---\n",
            data["body_md"]
        ]
        
        with open(out_file, "w", encoding="utf-8") as fp:
            fp.write("\n".join(frontmatter) + "\n" + "\n".join(body))
            
        all_records.append(data)
        print(f"OK ({data['content_length']} karakter)")
        time.sleep(0.3)
        
    # 3. Unduh dan proses halaman statis penting
    print("\n--- Mengunduh dan Memproses Halaman Statis Profil ---")
    for i, url in enumerate(filtered_page_urls, 1):
        parsed = urlparse(url)
        slug = parsed.path.strip("/").split("/")[-1]
        out_file = os.path.join(PAGES_DIR, f"{slug}.md")
        
        print(f"[{i}/{len(filtered_page_urls)}] {slug} ... ", end="", flush=True)
        html = fetch_url(url)
        if not html:
            continue
            
        data = parse_post(url, html, is_page=True)
        if not data["body_md"]:
            print("KOSONG (Dilewati)")
            continue
            
        frontmatter = [
            "---",
            f'title: {json.dumps(data["title"], ensure_ascii=False)}',
            f'date: "{data["date"]}"',
            f'author: "{data["author"]}"',
            f'url: "{data["url"]}"',
            f'slug: "{data["slug"]}"',
            "type: page",
            "---\n"
        ]
        body = [
            f'# {data["title"]}\n',
            f'*Sumber Halaman Resmi: [{data["url"]}]({data["url"]})*\n',
            "---\n",
            data["body_md"]
        ]
        with open(out_file, "w", encoding="utf-8") as fp:
            fp.write("\n".join(frontmatter) + "\n" + "\n".join(body))
            
        all_records.append(data)
        print(f"OK ({data['content_length']} karakter)")
        time.sleep(0.3)

    # 4. Simpan articles.json
    json_path = os.path.join(OUTPUT_DIR, "articles.json")
    clean_records = []
    for r in all_records:
        r_copy = dict(r)
        del r_copy["body_md"]  # hilangkan body untuk efisiensi json metadata
        clean_records.append(r_copy)
        
    with open(json_path, "w", encoding="utf-8") as fp:
        json.dump(clean_records, fp, ensure_ascii=False, indent=2)
    print(f"\nDisimpan: {json_path} ({len(clean_records)} artikel/halaman)")

    # 5. Bangun README.md Indeks Katalog
    readme_path = os.path.join(OUTPUT_DIR, "README.md")
    readme_lines = [
        "# Khazanah Arsip Artikel & Dokumen Resmi Sekolah Karakter (SKIS Semarang)",
        "",
        "Direktori ini memuat arsip otentik seluruh artikel pemikiran, risalah parenting nabawiyah, kritik sistem pendidikan, dan panduan kurikulum lapangan dari situs resmi **Sekolah Karakter Imam Syafi'i (SKIS Semarang)** (`https://sekolahkarakter.com/`).",
        "",
        f"- **Tanggal Pengarsipan:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **Total Berkas Terarsip:** {len(clean_records)} berkas ({len([r for r in clean_records if not r['is_page']])} artikel blog, {len([r for r in clean_records if r['is_page']])} halaman statis profil)",
        f"- **Basis Data Terstruktur:** [`articles.json`](articles.json)",
        "",
        "---",
        "",
        "## 📑 Indeks Master Artikel SKIS (Berdasarkan Topik & Urutan Kronologis)",
        "",
        "| No | Judul Artikel | Tanggal | Kategori | Berkas Lokal | Tautan Asli |",
        "| :---: | :--- | :---: | :--- | :--- | :--- |"
    ]
    
    # Sort by date descending
    sorted_records = sorted(clean_records, key=lambda x: x["date"] or "", reverse=True)
    for idx, r in enumerate(sorted_records, 1):
        date_display = (r["date"][:10]) if r["date"] else "-"
        cats_display = ", ".join(r["categories"]) if r.get("categories") else "Artikel"
        folder = "pages" if r["is_page"] else "artikel"
        local_link = f"[`{r['slug']}.md`]({folder}/{r['slug']}.md)"
        readme_lines.append(f"| {idx} | **{r['title']}** | {date_display} | {cats_display} | {local_link} | [Kunjungi]({r['url']}) |")

    with open(readme_path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(readme_lines) + "\n")
    print(f"Disimpan: {readme_path}")
    print(f"\nCRAWLING SELESAI DENGAN SUKSES! Total {len(clean_records)} naskah terarsip di old_backup/skis/.")

if __name__ == "__main__":
    main()

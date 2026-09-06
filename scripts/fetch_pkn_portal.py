#!/usr/bin/env python3
"""
scripts/fetch_pkn_portal.py
Mengunduh dan mengonversi seluruh artikel, event pelatihan, dan halaman dari
portal resmi Pendidikan Karakter Nabawiyah: https://karakternabawiyah.com/
ke format Markdown di old_backup/karakternabawiyah/
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
OUTPUT_DIR = os.path.join(BASE_DIR, "old_backup", "karakternabawiyah")
ARTIKEL_DIR = os.path.join(OUTPUT_DIR, "artikel")
EVENTS_DIR = os.path.join(OUTPUT_DIR, "events")
PAGES_DIR = os.path.join(OUTPUT_DIR, "pages")

os.makedirs(ARTIKEL_DIR, exist_ok=True)
os.makedirs(EVENTS_DIR, exist_ok=True)
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
        if not any(url.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".pdf", ".zip", ".svg"]):
            urls.append(url)
    return urls

def elem_to_markdown(elem):
    if elem is None:
        return ""
    
    # Remove unwanted elements first
    for unwanted in elem.find_all(["script", "style", "noscript", "form", "iframe"]):
        unwanted.decompose()
    for share in elem.find_all(class_=lambda c: c and any(w in c for w in ["share", "social", "jp-relatedposts", "author-bio", "nav-links", "comments", "elementskit-menu"])):
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
            return f"\n\n{'#' * level} {inner}\n\n" if inner else ""
            
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
    cleaned = re.sub(r"\n{3,}", "\n\n", raw_md).strip()
    return cleaned

def parse_page(url, html):
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
    time_pub = soup.find("meta", property="article:published_time")
    if time_pub:
        pub_date = time_pub.get("content", "")
    if not pub_date:
        t_tag = soup.find("time")
        if t_tag:
            pub_date = t_tag.text.strip()

    # Extract Content
    # On Elementor pages, .elementor or .entry-content holds the main body
    content_node = None
    for selector in [".entry-content", ".elementor", "article", "#content", "main"]:
        node = soup.select_one(selector)
        if node and len(node.get_text(strip=True)) > 150:
            content_node = node
            break
            
    if not content_node:
        content_node = soup.body

    body_md = elem_to_markdown(content_node) if content_node else ""
    
    # Filter out header/footer boilerplate that might have seeped in
    boilerplate_lines = [
        "Skip to content", "Profil PEMATERI", "Ustadz Abdul Kholiq", 
        "Prof. Iman Harymawan", "Panduan Implementasi Standar", "Akademi Guru PKN"
    ]
    cleaned_lines = []
    for line in body_md.splitlines():
        if line.strip() in boilerplate_lines and len(line.strip()) < 30:
            continue
        cleaned_lines.append(line)
    body_md = "\n".join(cleaned_lines).strip()
    body_md = re.sub(r"\n{3,}", "\n\n", body_md)
    
    parsed = urlparse(url)
    slug = parsed.path.strip("/").split("/")[-1]
    if not slug:
        slug = "beranda-pkn"

    # Classify type
    is_event = any(slug.startswith(p) for p in ["akg-", "pis-", "tdk-", "tc-", "event-", "workshop-", "webinar"])
    is_article = "/termaktub" in url or "/lebih-dari" in url or "/ga-perlu" in url or "/akses-pikiran" in url or "/implementasi-terbaik" in url or "/persepsi-artikel" in url or "/bahasa-hati" in url or "/konsep-ideal" in url

    item_type = "event" if is_event else ("artikel" if is_article else "page")

    return {
        "title": title,
        "date": pub_date,
        "url": url,
        "slug": slug,
        "type": item_type,
        "content_length": len(body_md),
        "body_md": body_md
    }

def main():
    print("=== CRAWLER PORTAL PENDIDIKAN KARAKTER NABAWIYAH (karakternabawiyah.com) ===")
    
    post_urls = get_sitemap_urls("https://karakternabawiyah.com/post-sitemap.xml")
    page_urls = get_sitemap_urls("https://karakternabawiyah.com/page-sitemap.xml")
    
    ignored_slugs = ["sukses-registrasi", "sukses-form-slide", "form-slide"]
    all_urls = []
    seen = set()
    
    for u in post_urls + page_urls:
        if u not in seen and not any(ign in u for ign in ignored_slugs):
            seen.add(u)
            all_urls.append(u)
            
    print(f"Total target URLs to crawl: {len(all_urls)}")
    all_records = []
    
    for i, url in enumerate(all_urls, 1):
        parsed = urlparse(url)
        slug = parsed.path.strip("/").split("/")[-1]
        if not slug:
            slug = "beranda-pkn"
            
        print(f"[{i}/{len(all_urls)}] {slug} ... ", end="", flush=True)
        html = fetch_url(url)
        if not html:
            continue
            
        data = parse_page(url, html)
        if data["content_length"] < 100:
            print(f"Dilewati (konten terlalu pendek: {data['content_length']} karakter)")
            continue
            
        # Tentukan direktori simpan
        if data["type"] == "event":
            dest_dir = EVENTS_DIR
        elif data["type"] == "artikel":
            dest_dir = ARTIKEL_DIR
        else:
            dest_dir = PAGES_DIR
            
        out_file = os.path.join(dest_dir, f"{slug}.md")
        
        frontmatter = [
            "---",
            f'title: {json.dumps(data["title"], ensure_ascii=False)}',
            f'date: "{data["date"]}"',
            f'url: "{data["url"]}"',
            f'slug: "{data["slug"]}"',
            f'type: "{data["type"]}"',
            "---\n"
        ]
        body = [
            f'# {data["title"]}\n',
            f'*Sumber Resmi: [{data["url"]}]({data["url"]})*\n',
            "---\n",
            data["body_md"]
        ]
        
        with open(out_file, "w", encoding="utf-8") as fp:
            fp.write("\n".join(frontmatter) + "\n" + "\n".join(body))
            
        all_records.append(data)
        print(f"OK ({data['content_length']} karakter) -> {data['type']}")
        time.sleep(0.3)
        
    # Simpan articles.json
    json_path = os.path.join(OUTPUT_DIR, "articles.json")
    clean_records = []
    for r in all_records:
        r_copy = dict(r)
        del r_copy["body_md"]
        clean_records.append(r_copy)
        
    with open(json_path, "w", encoding="utf-8") as fp:
        json.dump(clean_records, fp, ensure_ascii=False, indent=2)
        
    # Bangun README.md katalog
    readme_path = os.path.join(OUTPUT_DIR, "README.md")
    readme_lines = [
        "# Khazanah Arsip Portal Resmi Pendidikan Karakter Nabawiyah (PKN)",
        "",
        "Direktori ini memuat arsip otentik artikel, dokumentasi kegiatan pelatihan resmi (**Akademi Guru PKN, Panduan Implementasi Standar, Temu Lembaga, Talent Camp, Workshop Sekolah Tanpa OB**), serta profil perumus manhaj dari portal resmi `https://karakternabawiyah.com/`.",
        "",
        f"- **Tanggal Pengarsipan:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **Total Berkas Terarsip:** {len(clean_records)} berkas",
        f"- **Rincian:** {len([r for r in clean_records if r['type'] == 'event'])} Event & Program Pelatihan, {len([r for r in clean_records if r['type'] == 'artikel'])} Artikel Kajian, {len([r for r in clean_records if r['type'] == 'page'])} Halaman Profil & Kurikulum",
        f"- **Basis Data Terstruktur:** [`articles.json`](articles.json)",
        "",
        "---",
        "",
        "## 🗓️ 1. Katalog Event & Program Kegiatan Pelatihan PKN",
        "",
        "| No | Nama Event / Kegiatan | Kategori | Berkas Lokal | Tautan Asli |",
        "| :---: | :--- | :---: | :--- | :--- |"
    ]
    
    events = [r for r in clean_records if r["type"] == "event"]
    for idx, e in enumerate(events, 1):
        readme_lines.append(f"| {idx} | **{e['title']}** | Program PKN | [`{e['slug']}.md`](events/{e['slug']}.md) | [Kunjungi]({e['url']}) |")
        
    readme_lines.extend([
        "",
        "---",
        "",
        "## 📚 2. Artikel Pemikiran & Halaman Lembaga",
        "",
        "| No | Judul Naskah | Tipe | Berkas Lokal | Tautan Asli |",
        "| :---: | :--- | :---: | :--- | :--- |"
    ])
    
    others = [r for r in clean_records if r["type"] != "event"]
    for idx, o in enumerate(others, 1):
        folder = "artikel" if o["type"] == "artikel" else "pages"
        readme_lines.append(f"| {idx} | **{o['title']}** | {o['type'].title()} | [`{o['slug']}.md`]({folder}/{o['slug']}.md) | [Kunjungi]({o['url']}) |")
        
    with open(readme_path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(readme_lines) + "\n")
        
    print(f"\nDisimpan: {json_path}")
    print(f"Disimpan: {readme_path}")
    print(f"SELESAI! Total {len(clean_records)} berkas berhasil diunduh ke old_backup/karakternabawiyah/.")

if __name__ == "__main__":
    main()

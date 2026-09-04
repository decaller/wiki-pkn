import urllib.request
import json
import os
import re
import html

OUTPUT_DIR = 'old_backup/sotabh/artikel'
INDEX_FILE = 'old_backup/sotabh/README.md'
JSON_FILE = 'old_backup/sotabh/articles.json'

os.makedirs(OUTPUT_DIR, exist_ok=True)

def html_to_markdown(html_text):
    if not html_text:
        return ""
    text = html.unescape(html_text)
    
    # Remove unwanted scripts or styles
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    
    # Headings
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', text, flags=re.DOTALL)
    
    # Formatting
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<i>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)
    
    # Blockquotes
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'\n> \1\n', text, flags=re.DOTALL)
    
    # Lists
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'* \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<\/?(?:ul|ol)[^>]*>', '\n', text)
    
    # Links & Images
    text = re.sub(r'<a\s+(?:[^>]*?\s+)?href=[\"\'](.*?)[\"\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL)
    text = re.sub(r'<img\s+(?:[^>]*?\s+)?src=[\"\'](.*?)[\"\'][^>]*alt=[\"\'](.*?)[\"\'][^>]*>', r'![\2](\1)', text)
    text = re.sub(r'<img\s+(?:[^>]*?\s+)?src=[\"\'](.*?)[\"\'][^>]*>', r'![](\1)', text)
    
    # Paragraphs & line breaks
    text = re.sub(r'</p>\s*<p[^>]*>', '\n\n', text)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<\/?p[^>]*>', '\n\n', text)
    
    # Strip any remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Clean excessive whitespace
    lines = [line.strip() for line in text.splitlines()]
    clean_text = '\n'.join(lines)
    clean_text = re.sub(r'\n{3,}', '\n\n', clean_text)
    
    return clean_text.strip()

def sanitize_filename(name):
    # Keep alphanumeric, spaces, dashes
    clean = re.sub(r'[\\/*?:"<>|]', '', name)
    clean = clean.strip().replace(' ', '-')
    return clean[:100]

def fetch_all_posts():
    all_posts = []
    page = 1
    while True:
        url = f"https://sotabh.com/wp-json/wp/v2/posts?per_page=100&page={page}"
        print(f"Fetching page {page} from {url}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                if not data:
                    break
                all_posts.extend(data)
                total_pages = int(resp.headers.get('X-WP-TotalPages', 1))
                print(f"Page {page} fetched ({len(data)} posts). Total collected: {len(all_posts)} / {resp.headers.get('X-WP-Total')}")
                if page >= total_pages:
                    break
                page += 1
        except Exception as e:
            print(f"Finished or error on page {page}: {e}")
            break
            
    print(f"\nTotal posts collected: {len(all_posts)}")
    return all_posts

def main():
    posts = fetch_all_posts()
    
    # Save raw JSON
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f"Saved raw JSON to {JSON_FILE}")

    index_entries = []
    
    for i, post in enumerate(posts, 1):
        raw_title = post['title']['rendered']
        title = html.unescape(raw_title).strip()
        date = post['date']
        link = post['link']
        slug = post['slug']
        
        content_html = post['content']['rendered']
        content_md = html_to_markdown(content_html)
        
        excerpt_html = post['excerpt']['rendered']
        excerpt_md = html_to_markdown(excerpt_html)
        excerpt_clean = excerpt_md.replace('\n', ' ')[:150] + '...' if len(excerpt_md) > 150 else excerpt_md.replace('\n', ' ')
        
        filename = f"{date[:10]}-{slug}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        file_content = f"""---
title: "{title}"
date: "{date}"
url: "{link}"
slug: "{slug}"
---

# {title}

*Dipublikasikan pada: {date[:10]} | Sumber: [{link}]({link})*

---

{content_md}
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)
            
        index_entries.append((date[:10], title, filename, link, excerpt_clean))

    # Generate README.md index
    readme_content = """# Arsip Artikel SOTAB HEBAT (sotabh.com)

Dokumen ini merupakan arsip referensi lengkap seluruh artikel yang diterbitkan di **[SOTAB HEBAT](https://sotabh.com/artikel/)** (State of the Art Belajar Hati) oleh Ustadz Abdul Kholiq dan tim Pendidikan Karakter Nabawiyah.

Total artikel yang diarsipkan: **""" + str(len(index_entries)) + """ artikel**.

---

## Daftar Lengkap Artikel (Kronologis Terkini)

| No | Tanggal | Judul Artikel | Berkas Lokal | Tautan Asli |
|---|---|---|---|---|
"""
    for idx, (dt, tit, fn, lnk, exc) in enumerate(index_entries, 1):
        clean_tit = tit.replace('|', '-')
        readme_content += f"| {idx} | {dt} | **[{clean_tit}](artikel/{fn})** | `{fn}` | [Web]({lnk}) |\n"

    readme_content += "\n---\n\n## Ringkasan Eksekutif Artikel\n\n"
    for idx, (dt, tit, fn, lnk, exc) in enumerate(index_entries, 1):
        readme_content += f"### {idx}. [{tit}](artikel/{fn})\n"
        readme_content += f"- **Tanggal:** {dt} | **Tautan:** [{lnk}]({lnk})\n"
        readme_content += f"- **Kutipan:** {exc}\n\n"

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(readme_content)
        
    print(f"Generated index at {INDEX_FILE}")
    print(f"All {len(index_entries)} markdown articles written to {OUTPUT_DIR}/")

if __name__ == '__main__':
    main()

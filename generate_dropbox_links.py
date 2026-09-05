#!/usr/bin/env python3
import json
import subprocess
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.parse

print("Fetching file listing from dropbox:projects/PKN...", flush=True)
res = subprocess.run(
    ["rclone", "lsjson", "-R", "--files-only", "dropbox:projects/PKN"],
    capture_output=True,
    text=True
)

if res.returncode != 0:
    print(f"Error fetching files: {res.stderr}", file=sys.stderr)
    sys.exit(1)

all_items = json.loads(res.stdout)

# Filter out .git repository internal files
files = [item for item in all_items if not item["Path"].startswith("wiki/wikiPKN/.git/")]
print(f"Found {len(files)} files to generate direct download links for.", flush=True)

cache_file = "dropbox_links_cache.json"
links_cache = {}
if os.path.exists(cache_file):
    try:
        with open(cache_file, "r") as f:
            links_cache = json.load(f)
    except:
        links_cache = {}

def get_link(item):
    rel_path = item["Path"]
    if rel_path in links_cache:
        return rel_path, links_cache[rel_path], item

    remote_path = f"dropbox:projects/PKN/{rel_path}"
    for attempt in range(3):
        res = subprocess.run(["rclone", "link", remote_path], capture_output=True, text=True)
        if res.returncode == 0 and res.stdout.strip().startswith("http"):
            url = res.stdout.strip()
            # If dl=0, convert or provide direct download url dl=1
            return rel_path, url, item
        time.sleep(1)

    # Fallback to browser home url
    fallback_url = "https://www.dropbox.com/home/" + urllib.parse.quote("projects/PKN/" + rel_path)
    return rel_path, fallback_url, item

results = {}
completed = 0
total = len(files)

print(f"Generating links with 8 parallel workers...", flush=True)
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(get_link, item) for item in files]
    for fut in as_completed(futures):
        rel_path, url, item = fut.result()
        results[rel_path] = {"url": url, "item": item}
        links_cache[rel_path] = url
        completed += 1
        if completed % 25 == 0 or completed == total:
            print(f"Progress: {completed}/{total} links retrieved ({completed/total*100:.1f}%)", flush=True)
            with open(cache_file, "w") as f:
                json.dump(links_cache, f, indent=2)

with open(cache_file, "w") as f:
    json.dump(links_cache, f, indent=2)

def fmt_sz(num_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if num_bytes < 1024.0:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} TB"

# Group by directory
by_folder = {}
for rel_path, data in results.items():
    folder = os.path.dirname(rel_path)
    if not folder:
        folder = "Root (projects/PKN)"
    by_folder.setdefault(folder, []).append((rel_path, data["url"], data["item"]))

# Sort folders and files
output_md = "dropbox_files.md"
with open(output_md, "w", encoding="utf-8") as out:
    out.write("# PKN Dropbox Archive: File Catalog & Download Links\n\n")
    out.write(f"- **Source Directory**: `dropbox:projects/PKN`\n")
    out.write(f"- **Total Files**: {len(files)}\n")
    out.write(f"- **Direct Download (`dl=1`)**: Clicking **[Direct Download]** initiates an immediate file download. **[Open in Dropbox]** views it in the browser.\n\n")
    out.write("---\n\n")
    out.write("## Table of Contents\n\n")
    for folder in sorted(by_folder.keys()):
        anchor = folder.lower().replace(" ", "-").replace("/", "").replace("(", "").replace(")", "").replace(".", "")
        out.write(f"- [{folder}](#{anchor}) ({len(by_folder[folder])} files)\n")
    out.write("\n---\n\n")

    for folder in sorted(by_folder.keys()):
        anchor = folder.lower().replace(" ", "-").replace("/", "").replace("(", "").replace(")", "").replace(".", "")
        out.write(f"## {folder}\n\n")
        out.write("| File Name | Size | Direct Download | View Link |\n")
        out.write("| :--- | :---: | :---: | :---: |\n")
        
        # sort items alphabetically by file name
        items_in_folder = sorted(by_folder[folder], key=lambda x: os.path.basename(x[0]).lower())
        for rel_path, url, item in items_in_folder:
            fn = os.path.basename(rel_path)
            sz = fmt_sz(item.get("Size", 0))
            if "dl=0" in url:
                direct_url = url.replace("dl=0", "dl=1")
            else:
                direct_url = url
            out.write(f"| `{fn}` | {sz} | [Download]({direct_url}) | [Open]({url}) |\n")
        out.write("\n")

print(f"Successfully generated {output_md}!", flush=True)

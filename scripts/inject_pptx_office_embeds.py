#!/usr/bin/env python3
"""
Script to embed official Microsoft Office Web Apps Viewer iframes into Wiki PKN articles.
Uses the manifest generated in presentations/manifest.json.
Follows strict Zero-Deletion rule: preserves all existing content, dalil, and callouts.
"""

import os
import json
import urllib.parse

EMBED_START_TAG = "<!-- START_OFFICE_PPTX_EMBED -->"
EMBED_END_TAG = "<!-- END_OFFICE_PPTX_EMBED -->"

BASE_URL = os.environ.get("DOMAIN", os.environ.get("BASE_URL", "wikipkn.insanmustaqbal.or.id"))
CLEAN_DOMAIN = BASE_URL.replace("https://", "").replace("http://", "").strip("/")

def generate_embed_html(presentation, is_primary=True):
    clean_name = presentation["clean_name"]
    title = presentation["title"]
    size_mb = presentation["size_mb"]
    
    file_public_url = f"https://{CLEAN_DOMAIN}/presentations/{clean_name}"
    encoded_url = urllib.parse.quote(file_public_url, safe="")
    embed_src = f"https://view.officeapps.live.com/op/embed.aspx?src={encoded_url}"
    view_src = f"https://view.officeapps.live.com/op/view.aspx?src={encoded_url}"
    
    large_file_note = ""
    if size_mb > 25:
        large_file_note = f"""  <p style="font-size: 0.85rem; color: var(--gray); margin-top: 0.25rem; font-style: italic;">💡 <strong>Catatan:</strong> Berkas tayang ini berukuran cukup besar ({size_mb} MB). Jika pratinjau Office Online lambat memuat, disarankan mengklik <strong>Unduh Slide PPTX</strong> untuk membuka di aplikasi PowerPoint lokal.</p>"""

    html = f"""<div class="presentation-wrapper" style="margin: 1.5rem 0;">
  <h4 style="margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">📊 Pratinjau Materi Presentasi: {title}</h4>
  <div class="presentation-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border: 1px solid var(--lightgray); background: var(--light);">
    <iframe 
      src="{embed_src}" 
      style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border: 0;" 
      frameborder="0" 
      allowfullscreen="true"
      title="{title}">
    </iframe>
  </div>
  <div class="presentation-actions" style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 0.6rem; margin-bottom: 0.5rem; font-size: 0.85rem;">
    <a href="{file_public_url}" download style="display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.4rem 0.8rem; background: var(--light); border: 1px solid var(--lightgray); border-radius: 6px; text-decoration: none; color: var(--dark); font-weight: 500;">📥 Unduh Slide PPTX ({size_mb} MB)</a>
    <a href="{view_src}" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.4rem 0.8rem; background: var(--light); border: 1px solid var(--lightgray); border-radius: 6px; text-decoration: none; color: var(--dark); font-weight: 500;">🖥️ Buka Layar Penuh (Office Online)</a>
    <a href="https://1drv.ms/f/c/3efe4d3cd3a3788a/IgDcc7tk4xrzRLl5cAMnNZRfAZnQHlpC2x6T2PpXeL_jTzg" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.4rem 0.8rem; background: var(--light); border: 1px solid var(--lightgray); border-radius: 6px; text-decoration: none; color: var(--dark); font-weight: 500;">☁️ Folder OneDrive Resmi</a>
  </div>{large_file_note}
</div>"""
    return html

def main():
    manifest_path = "presentations/manifest.json"
    if not os.path.exists(manifest_path):
        print(f"Error: {manifest_path} not found.")
        return

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # Group presentations by target article
    article_to_pres = {}
    for item in manifest:
        for target in item.get("target_articles", []):
            article_to_pres.setdefault(target, []).append(item)

    print(f"Total articles targeted for embedding: {len(article_to_pres)}")
    
    modified_count = 0
    for target_path, pres_list in sorted(article_to_pres.items()):
        if not os.path.exists(target_path):
            print(f"Skipping missing file: {target_path}")
            continue

        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Remove old embed block if present
        if EMBED_START_TAG in content and EMBED_END_TAG in content:
            start_idx = content.find(EMBED_START_TAG)
            end_idx = content.find(EMBED_END_TAG) + len(EMBED_END_TAG)
            content = content[:start_idx] + content[end_idx:]
            content = content.strip() + "\n"

        # Generate embeds
        embed_blocks = []
        embed_blocks.append(EMBED_START_TAG)
        embed_blocks.append("\n---\n\n### 📽️ Media Presentasi & Slide Interaktif (Office Web Apps)\n")
        embed_blocks.append("> [!info] Pratinjau Interaktif Microsoft Office\n> Anda dapat menavigasi slide secara langsung melalui penampil di bawah ini, atau membuka layar penuh dan mengunduh berkas aslinya.\n")
        
        for idx, pres in enumerate(pres_list):
            embed_blocks.append(generate_embed_html(pres, is_primary=(idx == 0)))

        embed_blocks.append(EMBED_END_TAG)
        full_embed_str = "\n".join(embed_blocks) + "\n"

        # Where to insert?
        # If there's already a "> [!quote] Dokumen & Slide Presentasi Rujukan Resmi PKN",
        # insert right before or after it!
        # Let's insert right before the presentation citation callout or at the end of the file
        citation_marker = "> [!quote] Dokumen & Slide Presentasi Rujukan Resmi PKN"
        if citation_marker in content:
            # Insert right before the citation callout
            content = content.replace(citation_marker, full_embed_str + "\n" + citation_marker)
        else:
            # Append near the end of the document
            content = content.rstrip() + "\n\n" + full_embed_str

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)

        modified_count += 1
        print(f"Embedded {len(pres_list)} presentation(s) in: {target_path}")

    print(f"\nSUCCESS: Embedded Microsoft Office Viewer into {modified_count} articles.")

if __name__ == "__main__":
    main()

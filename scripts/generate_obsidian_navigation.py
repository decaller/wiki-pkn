#!/usr/bin/env python3
"""
generate_obsidian_navigation.py

Generator Halaman Navigasi Cepat (Navigation Hub / MOC) untuk Obsidian:
1. Membaca pohon struktur dari nav_structure.json dan seluruh berkas di content/
2. Memetakan setiap artikel dengan kanvas visual Obsidian (.canvas), status pembacaan, dan relasi folder
3. Menghubungkan nomor dan judul TB-40 ke file markdown fisik
4. Mengelompokkan berdasarkan kluster materi (Insan, Metode, Implementasi, TB40, SOTAB, Video, Dalil, Canvas)
5. Menghasilkan 'content/Peta Navigasi Wiki PKN.md' yang interaktif dan mudah diedit langsung di Obsidian.
"""

import os
import json
import re
from pathlib import Path

CONTENT_DIR = "content"
NAV_STRUCTURE_FILE = "nav_structure.json"
OUTPUT_FILE = os.path.join(CONTENT_DIR, "Peta Navigasi Wiki PKN.md")

def get_all_markdown_metadata(content_dir):
    """Memindai seluruh file Markdown untuk mengambil frontmatter title, aliases, dan relasi canvas."""
    md_registry = {}
    for root, _, files in os.walk(content_dir):
        for f in sorted(files):
            if f.endswith(".md"):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, content_dir)
                stem = Path(f).stem
                
                title = stem
                canvas_links = []
                with open(full_path, "r", encoding="utf-8", errors="ignore") as fh:
                    content = fh.read()
                    m_title = re.search(r"^title:\s*[\"']?(.*?)[\"']?$", content, re.MULTILINE)
                    if m_title:
                        title = m_title.group(1).strip()
                        
                    canvases = re.findall(r'!\[\[(canvas/.*?\.canvas)\]\]', content)
                    canvas_links = canvases

                md_registry[stem.lower()] = {
                    "stem": stem,
                    "title": title,
                    "rel_path": rel_path,
                    "canvas_links": canvas_links
                }
    return md_registry

def get_all_canvas_files(content_dir):
    """Memindai seluruh berkas .canvas di folder content/canvas/."""
    canvas_dir = os.path.join(content_dir, "canvas")
    canvases = []
    if os.path.exists(canvas_dir):
        for root, _, files in os.walk(canvas_dir):
            for f in sorted(files):
                if f.endswith(".canvas"):
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, content_dir)
                    canvases.append(rel_p)
    return sorted(canvases)

def find_matching_file(title_or_slug, md_registry):
    """Mencocokkan judul dari nav_structure ke file markdown fisik secara cerdas."""
    key = title_or_slug.lower().strip()
    
    # Penanganan kasus khusus Home & Blueprint
    if key == "home":
        if "index" in md_registry:
            return md_registry["index"]
    if "pkn blueprint" in key:
        for k, v in md_registry.items():
            if "blueprint" in k:
                return v

    if key in md_registry:
        return md_registry[key]
    
    # Penanganan nomor TB-40 misal: "01. Himmah (Bercita-Cita Tinggi)" -> "01-himmah"
    m_tb = re.match(r'^(\d{2})[\.\s]+([A-Za-z\']+)', title_or_slug)
    if m_tb:
        num = m_tb.group(1)
        name_clean = m_tb.group(2).lower().replace("'", "")
        tb_key = f"{num}-{name_clean}"
        if tb_key in md_registry:
            return md_registry[tb_key]
        for k, v in md_registry.items():
            if k.startswith(f"{num}-"):
                return v

    # Coba bersihkan prefix angka
    cleaned = re.sub(r'^\d+[\.\s]+', '', key)
    name_only = key.split('(')[0].strip()
    cleaned_name_only = cleaned.split('(')[0].strip()

    for k, v in md_registry.items():
        if k == cleaned or k == name_only or k == cleaned_name_only:
            return v
        if key in k or k in key:
            return v
    return None

def build_tree_markdown(items, md_registry, indent=0):
    """Membangun teks navigasi bertingkat dari nav_structure.json."""
    lines = []
    prefix = "  " * indent
    for item in items:
        title = item.get("title", "")
        children = item.get("children", [])
        matched = find_matching_file(title, md_registry)
        
        icon = "📄"
        if children:
            icon = "📂"
            
        if matched:
            target_link = matched["stem"]
            canvas_badge = ""
            if matched["canvas_links"]:
                canvas_name = Path(matched["canvas_links"][0]).stem
                canvas_badge = f" `[🎨 Canvas: {canvas_name[:30]}...]`"
            lines.append(f"{prefix}- {icon} [[{target_link}|{title}]]{canvas_badge}")
        else:
            lines.append(f"{prefix}- {icon} **{title}** *(Folder/Topik)*")
            
        if children:
            lines.extend(build_tree_markdown(children, md_registry, indent + 1))
    return lines

def generate_navigation_page():
    md_registry = get_all_markdown_metadata(CONTENT_DIR)
    canvases = get_all_canvas_files(CONTENT_DIR)
    
    nav_struct = {}
    if os.path.exists(NAV_STRUCTURE_FILE):
        with open(NAV_STRUCTURE_FILE, "r", encoding="utf-8") as f:
            nav_struct = json.load(f)
            
    top_structure = []
    for col_id, col_data in nav_struct.items():
        top_structure = col_data.get("structure", [])
        break

    tree_lines = build_tree_markdown(top_structure, md_registry)
    
    total_md = len(md_registry)
    total_canvases = len(canvases)
    
    sotab_files = [v for v in md_registry.values() if v["rel_path"].startswith("Materi SOTAB/")]
    video_files = [v for v in md_registry.values() if v["rel_path"].startswith("Kajian Video/")]
    dalil_files = [v for v in md_registry.values() if v["rel_path"].startswith("Dalil/")]
    template_files = [v for v in md_registry.values() if "Template" in v["rel_path"]]

    content = f"""---
title: "Peta Navigasi & Map of Content (MOC) Wiki PKN"
description: "Pusat kendali navigasi cepat hierarki materi, tautan kanvas Obsidian, dan status korpus untuk mempermudah penulisan dan penjelajahan di Obsidian."
aliases:
  - MOC
  - Peta Navigasi
  - Navigation Hub
  - Indeks Materi
tags:
  - navigasi
  - moc
  - obsidian-hub
---

# 🧭 Peta Navigasi & Map of Content (MOC) Wiki-PKN

> [!SUMMARY] Ringkasan Eksekutif & Panduan Editor
> **Tujuan Dokumen:** Berfungsi sebagai *Command Center* bagi editor di Obsidian untuk menavigasi, menyunting, dan menautkan halaman secara instan.
> * **Total Halaman Markdown:** {total_md} artikel aktif
> * **Total Bagan Obsidian Canvas:** {total_canvases} bagan visual interaktif
> * **Format Navigasi:** Hierarki pohon terstruktur dilengkapi penanda badge kanvas `[🎨 Canvas]` dan tautan silang dua arah `[[...]]`.

---

## 🏛️ 1. Hierarki Manhaj Utama (Paradigma & Implementasi PKN)

Berikut adalah silsilah topik fondasional PKN yang tersusun dari epistemologi insan, metodologi pendidikan nabawiyah, hingga tata kelola kelembagaan:

{os.linesep.join(tree_lines)}

---

## 🎨 2. Katalog Visual Obsidian Canvas ({len(canvases)} Bagan)

Bagan visual spasial untuk memahami keterhubungan konsep secara global sebelum masuk ke perincian:

<details open>
<summary><b>Lihat Seluruh {len(canvases)} Berkas Obsidian Canvas</b></summary>

| No | Nama Bagan Obsidian Canvas | Tautan Buka di Obsidian |
| :-: | :--- | :--- |
"""

    for idx, c_path in enumerate(canvases, 1):
        canvas_title = Path(c_path).stem
        content += f"| {idx} | **{canvas_title}** | ![[{c_path}]] |\n"

    content += f"""
</details>

---

## 📚 3. Kluster Khazanah Materi Pendukung

### 💡 A. Koleksi Tulisan SOTAB HEBAT ({len(sotab_files)} Artikel)
* **Hub Utama:** [[Materi SOTAB|Portal Direktori Materi SOTAB ↗]]
* Menghimpun seluruh refleksi kelembutan Bahasa Hati, perbaikan luka asuh, dan dialog kelekatan ayah-bunda karya Ustadz Abdul Kholiq.

### 🎥 B. Koleksi Rekaman Kajian Video ({len(video_files)} Rekaman & 1.159 Bab)
* **Hub Utama:** [[Kajian Video|Portal Kajian Video & Indeks Timestamp ↗]]
* Memuat transkrip tematik, pembahasan studi kasus nyata, dan tautan langsung ke menit video YouTube.

### 📜 C. Koleksi Halaman Dalil Mandiri ({len(dalil_files)} Dalil)
* **Pondasi Syar'i:** [[Master Katalog Dalil Al-Quran]], [[Master Katalog Dalil Hadits dan Sunnah]], serta halaman takhrij mandiri di folder `content/Dalil/`.

### 📋 D. Toolkit & Template Operasional KBM ({len(template_files)} Dokumen)
* **Instrumen Lapangan:**
  - [[Instrumen Evaluasi Kesiapan Transformasi|Ceklist Kesiapan Transformasi Pengasuhan]]
  - [[Panduan RPP dan Observasi Lapangan]]
  - [[Kuisioner Asesmen 40 Bakat Nabawiyah]]

---

## 🛠️ 4. Panduan Kerja Cepat Editor di Obsidian

1. **Gunakan Quick Switcher:** Tekan `Ctrl + O` (atau `Cmd + O` di Mac) lalu ketik nama halaman untuk melompat langsung ke artikel target.
2. **Lihat Hubungan di Graph View:** Buka *Local Graph* pada bilah samping (*sidebar*) untuk melihat simpul artikel yang sedang aktif beserta tautan dua arahnya.
3. **Patuhi Aturan Penulisan:** 
   - Awali draf dengan Callout `> [!SUMMARY]` (**TL;DR**).
   - Berikan pengantar global naratif dan sematkan bagan Obsidian Canvas `![[canvas/...canvas]]`.
   - Sambungkan antarpoin dalam narasi bertahap yang mengalir dan kohesif.
"""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"✅ Sukses menghasilkan halaman navigasi di: {OUTPUT_FILE}")
    print(f"   Total berkas markdown terindeks: {total_md}")
    print(f"   Total Obsidian Canvas terindeks: {total_canvases}")

if __name__ == "__main__":
    generate_navigation_page()

#!/usr/bin/env python3
"""
generate_video_pages.py
Mengekstrak 122 video kajian dan 1.159 segmen bab Ustadz Abdul Kholiq dari SQLite pkn.db
menjadi halaman Markdown Quartz v5 terstruktur dengan embed YouTube, tabel timestamp interaktif,
dan transkrip terformat rapi sesuai arsitektur Progressive Disclosure.
"""

import sqlite3
import os
import re

DB_PATH = "../PKN-videoDB/caption-getter/v1/pkn.db"
OUTPUT_DIR = "content/Kajian Video"

def sanitize_filename(title):
    title = re.sub(r'[\\/*?:"<>|]', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title[:120]

def main():
    if not os.path.exists(DB_PATH):
        print(f"Error: Database not found at {DB_PATH}")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Query all videos
    cur.execute("SELECT id, title, url, fetched_at FROM videos ORDER BY id ASC")
    videos = cur.fetchall()
    print(f"Found {len(videos)} videos in {DB_PATH}")

    total_chapters_processed = 0

    for vid_id, vid_title, vid_url, fetched_at in videos:
        # Extract clean youtube ID or link
        clean_title = sanitize_filename(vid_title)
        
        # Query chapters for this video
        cur.execute("""
            SELECT id, start_time, start_seconds, topic, summary, clean_transcript 
            FROM chapters 
            WHERE video_id = ? 
            ORDER BY start_seconds ASC
        """, (vid_id,))
        chapters = cur.fetchall()
        total_chapters_processed += len(chapters)

        # Build Markdown content
        frontmatter = f"""---
title: "{vid_title.replace('"', "'")}"
tags:
  - KajianVideo
  - UstadzAbdulKholiq
  - VideoPKN
  - RekamanKajian
sources:
  - file: "pkn.db/videos/{vid_id}"
    url: "{vid_url}"
    title: "{vid_title.replace('"', "'")}"
    authority: 0.4
---

> [!abstract] Ringkasan Kajian (Layer 1)
> **Judul Rekaman:** {vid_title}
> **Narasumber:** Ustadz Abdul Kholiq, S.Pd (Konseptor Pendidikan Karakter Nabawiyah)
> **Tautan Video:** [Tonton di YouTube]({vid_url})
> **Jumlah Bab Pembahasan:** {len(chapters)} segmen terindeks

## Pemutar Video (Embed)

<iframe class="external-embed youtube" src="https://www.youtube.com/embed/{vid_url.split('v=')[-1].split('&')[0]}" title="{vid_title.replace('"', "'")}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## Daftar Bab & Garis Waktu Pembahasan (Layer 2)

| Waktu Mulai | Topik Pembahasan | Ringkasan Inti |
|:---:|:---|:---|
"""
        table_rows = []
        deep_dives = []

        for ch_id, start_time, start_sec, topic, summary, clean_transcript in chapters:
            yt_link = f"{vid_url}&t={int(start_sec)}s"
            topic_str = topic.replace("|", "/") if topic else "Pembahasan Materi"
            summary_str = summary.replace("|", "/") if summary else "-"
            table_rows.append(f"| [{start_time}]({yt_link}) | **{topic_str}** | {summary_str} |")

            # Section for deep-dive transcript
            transcript_content = clean_transcript.strip() if clean_transcript else "Transkrip belum tersedia."
            deep_dives.append(f"""### ⏱️ [{start_time}]({yt_link}) - {topic_str}

> [!info] Ringkasan Bab
> {summary_str}

<details>
<summary>📜 Buka Transkrip Lengkap Bab Ini</summary>

{transcript_content}

</details>
""")

        body = frontmatter + "\n".join(table_rows) + "\n\n---\n\n## Rincian Bab & Transkrip Tematik (Layer 3 & 4)\n\n" + "\n".join(deep_dives)
        body += f"""
---

## Penautan Materi & Konsep Terkait
- Kembali ke direktori: [[Kajian Video]] | [[Indeks Utama]]
- Topik Manhaj Terkait: [[Pendidikan Karakter Nabawiyah]] | [[4 Etape Usia Nabawiyah]] | [[Koneksi Sebelum Koreksi]]
"""

        filename = f"{clean_title}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(body)

    print(f"Generated {len(videos)} video pages with {total_chapters_processed} indexed chapters in '{OUTPUT_DIR}'!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
CLI Helper to search PKN Video Database (pkn.db)
Usage:
    python3 scripts/search_pkn_video.py "kata kunci" [limit]
"""
import sys
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'old_backup', 'sqlite-vector-video-db', 'pkn.db')

def search_videos(query, limit=10):
    if not os.path.exists(DB_PATH):
        print(f"Error: Database file not found at {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    sql = """
        SELECT v.title, c.start_time, c.topic, c.summary, v.url, c.start_seconds
        FROM chapters c
        JOIN videos v ON c.video_id = v.id
        WHERE c.topic LIKE ? OR c.summary LIKE ?
        LIMIT ?;
    """
    pattern = f"%{query}%"
    c.execute(sql, (pattern, pattern, limit))
    rows = c.fetchall()

    print(f"\n🔍 Hasil pencarian untuk: '{query}' (Ditemukan: {len(rows)})\n" + "="*70)
    for i, r in enumerate(rows, 1):
        url = f"{r[4]}&t={r[5]}s" if 'watch?v=' in r[4] or 'live/' in r[4] else f"{r[4]}?t={r[5]}s"
        print(f"\n{i}. [{r[1]}] {r[2]}")
        print(f"   Video : {r[0]}")
        print(f"   Tautan: {url}")
        print(f"   Ikhtisar: {r[3]}")
    print("\n" + "="*70 + "\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Penggunaan: python3 scripts/search_pkn_video.py <kata_kunci> [jumlah_hasil]")
        sys.exit(1)
    q = sys.argv[1]
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    search_videos(q, lim)

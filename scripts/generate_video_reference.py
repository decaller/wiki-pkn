import sqlite3

conn = sqlite3.connect('old_backup/sqlite-vector-video-db/pkn.db')
c = conn.cursor()

def get_chapters(query, limit=5):
    c.execute("""
        SELECT v.title, c.start_time, c.topic, c.summary, v.url, c.start_seconds
        FROM chapters c
        JOIN videos v ON c.video_id = v.id
        WHERE c.topic LIKE ? OR c.summary LIKE ?
        LIMIT ?;
    """, (f'%{query}%', f'%{query}%', limit))
    return c.fetchall()

def format_section(title, desc, query, limit=5):
    rows = get_chapters(query, limit)
    md = f"### {title}\n\n{desc}\n\n"
    for r in rows:
        url = f"{r[4]}&t={r[5]}s" if 'watch?v=' in r[4] or 'live/' in r[4] else f"{r[4]}?t={r[5]}s"
        md += f"* **[{r[2]}]({url})** (`{r[1]}`)\n"
        md += f"  - *Ringkasan:* {r[3]}\n"
        md += f"  - *Video Sumber:* {r[0]}\n\n"
    return md

content = """---
title: "Referensi Kajian Video"
---

# Indeks Referensi Kajian Video Pendidikan Karakter Nabawiyah

Halaman ini menyajikan katalog terindeks dari rekaman kajian dan ceramah **Ustadz Abdul Kholiq** (perumus materi Pendidikan Karakter Nabawiyah) yang diekstraksi secara otomatis dari basis data `pkn.db` (122 video, 1.159 bab tematik terindeks).

Orang tua dan pendidik dapat langsung mengklik tautan bab untuk menyaksikan penjelasan otentik beserta contoh kasus di kanal YouTube resmi.

---

## 1. Fondasi Fitrah, Insan, & Trilogi Jiwa

"""

content += format_section(
    "Konsep Dasar Fitrah & Egosentris Anak",
    "Penjelasan mengenai struktur fitrah, penuntasan egosentris di usia dini (0–7 tahun), dan bagaimana fitrah iman ditumbuhkan.",
    "egosentris",
    5
)

content += format_section(
    "Trilogi Jiwa & Hakikat Insan",
    "Pembagian jiwa (Ammarah, Lawwamah, Muthmainnah) serta interaksi jasad dan ruh.",
    "jiwa",
    4
)

content += """---

## 2. Tiga Metode Mendidik (Bahasa Hati, Lisan, & Tangan)

"""

content += format_section(
    "Metode Mendidik & Karakteristik 3 Bahasa",
    "Kaidah penggunaan Bahasa Hati (tanpa syarat), Bahasa Lisan (bersyarat), dan Bahasa Tangan (bersyarat ketat).",
    "tiga metode",
    4
)

content += format_section(
    "Bahasa Hati & Pengisian Tangki Cinta",
    "Pentingnya menyentuh pikiran bawah sadar dan mengisi tangki cinta ananda sebelum instruksi.",
    "tangki cinta",
    4
)

content += """---

## 3. Fase Perkembangan Usia & Kesiapan Baligh

"""

content += format_section(
    "Tahapan Usia Perkembangan (0-7, 7-10, 10-14, 15+)",
    "Penahapan pendidikan sesuai perkembangan fitrah dari masa bermain, belajar, berkarya, hingga mandiri.",
    "tahap",
    5
)

content += format_section(
    "Persiapan Menuju Baligh & Kemandirian (Fase Murahaqah & Syabab)",
    "Menghadapi percepatan biologis dan melatih kematangan akal (Aqil-Baligh).",
    "baligh",
    5
)

content += """---

## 4. Luka Pengasuhan, Inner Child, & Recovery

"""

content += format_section(
    "Konsep Hutang Pengasuhan Orang Tua",
    "Memahami asal mula luka masa lalu orang tua dan dampaknya pada anak.",
    "hutang pengasuhan",
    5
)

content += format_section(
    "Metode Recovery EMISOL & Prinsip Naik Turun Gas",
    "Langkah praktis memulihkan ketaatan anak yang terlanjur membangkang atau trauma.",
    "recovery",
    4
)

content += """---

## 5. Fitrah Bakat & Penjurusan (TB40 & Rukun 3A)

"""

content += format_section(
    "Observasi Bakat Berdasarkan Usia Anak",
    "Cara memetakan bakat anak melalui rukun Suka, Bisa, dan Bermanfaat.",
    "bakat",
    5
)

content += """---

## 6. Studi Kasus Harian & Tanya Jawab Pengasuhan

"""

content += format_section(
    "Penanganan Masalah Shalat pada Anak",
    "Strategi menumbuhkan kecintaan shalat dan mendisiplinkan anak tanpa merusak fitrah.",
    "shalat",
    5
)

content += format_section(
    "Mengatasi Gadget & Generasi Digital",
    "Sikap bijak menghadapi layar digital dan melindungi anak dari erosi perhatian.",
    "gadget",
    4
)

content += format_section(
    "Mengatasi Konflik Saudara (Sibling Rivalry)",
    "Menegakkan keadilan dan mendamaikan anak-anak di rumah.",
    "saudara",
    4
)

with open('content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Referensi Kajian Video.md', 'w') as f:
    f.write(content)

print("Referensi Kajian Video.md successfully created. Length:", len(content))

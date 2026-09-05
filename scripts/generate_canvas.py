#!/usr/bin/env python3
"""
generate_canvas.py
Merekonstruksi diagram poster Pendidikan Karakter Nabawiyah_1.pdf
menjadi berkas Obsidian Canvas (.canvas) interaktif berstandar resmi.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_CANVAS = ROOT / "content" / "Pendidikan Karakter Nabawiyah.canvas"

nodes = []
edges = []

# Helper functions
def add_group(id, label, x, y, width, height, color=None):
    g = {
        "id": id,
        "type": "group",
        "label": label,
        "x": x,
        "y": y,
        "width": width,
        "height": height
    }
    if color:
        g["color"] = str(color)
    nodes.append(g)

def add_text_node(id, text, x, y, width, height, color=None):
    n = {
        "id": id,
        "type": "text",
        "text": text,
        "x": x,
        "y": y,
        "width": width,
        "height": height
    }
    if color:
        n["color"] = str(color)
    nodes.append(n)

def add_edge(id, from_node, to_node, from_side="bottom", to_side="top", label=None, color=None):
    e = {
        "id": id,
        "fromNode": from_node,
        "fromSide": from_side,
        "toNode": to_node,
        "toSide": to_side
    }
    if label:
        e["label"] = label
    if color:
        e["color"] = str(color)
    edges.append(e)

# --- 1. HEADER & JUDUL UTAMA ---
add_text_node(
    "header-main",
    "# 🌟 PENDIDIKAN KARAKTER NABAWIYAH (PKN)\n**Peta Arsitektur Komprehensif Manhaj Tarbiyah Berbasis Fitrah & Sunnah**\n*Ustadz Abdul Kholiq • SOTAB HEBAT • Himmatul Ummah*",
    x=-400, y=-600, width=800, height=140, color="1"
)

# --- 2. SEKTOR 1: SUMBER & KOMPONEN KURIKULUM ---
add_group("group-sektor1", "SEKTOR 1: FONDASI, SUMBER & KOMPONEN KURIKULUM", -850, -400, 1700, 480, "4")

add_text_node(
    "node-sumber",
    "### 📖 5 Sumber Otoritatif\n1. **Al-Qur'anul Karim** (Petunjuk Utama)\n2. **As-Sunnah Ash-Shahihah** (Model Teladan)\n3. **As-Sirah An-Nabawiyyah** (Konteks Sejarah)\n4. **Kalam Ulama Salaf** (Syarah & Atsar)\n5. **Ilmu Pengetahuan Objektif** (Ayat Kauniyah)",
    x=-800, y=-340, width=360, height=220, color="4"
)

add_text_node(
    "node-komponen",
    "### ⚖️ 5 Komponen Pokok\n1. **Aqidah & Tauhid** (Pondasi Jiwa)\n2. **Ibadah Mahdhah** (Penghambaan Murni)\n3. **Akhlaq & Adab** (Buah Keimanan)\n4. **Muamalah Sosial** (Keadilan & Rahmah)\n5. **Dakwah & Khilafah** (Peran Peradaban)",
    x=440, y=-340, width=360, height=220, color="4"
)

add_text_node(
    "node-kurikulum-core",
    "## 🏛️ KURIKULUM PENDIDIKAN KARAKTER NABAWIYAH\n**'Satu Anak Satu Kurikulum'**\nMemandu tumbuh kembang fitrah insan secara utuh tanpa penyeragaman kaku model pabrik.",
    x=-240, y=-330, width=480, height=150, color="2"
)

add_text_node(
    "node-sub-kurikulum",
    "### 🧩 Ranting Kurikulum Tematik\n• **Adab & Muru'ah** (Integritas Pribadi)\n• **Ketahanan Jati Diri** (Anti-Perundungan & Syahwat)\n• **Eksplorasi 40 Bakat (TB-40)** (Keunikan Potensi)\n• **Pembelajaran Alamiah** (Tadabbur Alam Semesta)\n• **Keterampilan Hidup & Kepekaan Sosial**",
    x=-320, y=-140, width=640, height=180, color="3"
)

add_edge("e-sum-kur", "node-sumber", "node-kurikulum-core", "right", "left", "Mengalirkan Dalil")
add_edge("e-kom-kur", "node-komponen", "node-kurikulum-core", "left", "right", "Membentuk Struktur")
add_edge("e-kur-sub", "node-kurikulum-core", "node-sub-kurikulum", "bottom", "top")

# --- 3. SEKTOR 2: METODE & DIMENSI INSAN ---
add_group("group-sektor2", "SEKTOR 2: DIMENSI INSAN & METODE PENDEKATAN", -850, 140, 1700, 420, "5")

add_text_node(
    "node-dimensi-insan",
    "### 👤 4 Dimensi Hakikat Insan\n1. **Ruh:** Bernafaskan Asma Allah & Panggilan Fitrah\n2. **Jasad:** Fisik Sehat, Halal Thayyib & Gerak Motorik\n3. **Akal:** Nalar Kritis, Tadabbur & Ilmu Bermanfaat\n4. **Nafs:** Jiwa yang Ditanamkan Taubat & Tazkiyah",
    x=-800, y=200, width=360, height=200, color="5"
)

add_text_node(
    "node-metode-tadarruj",
    "### 🔄 Kaidah Metode Nabawi: Tadarruj\n• **Berorientasi Proses:** Bukan Angka Rapor Semu\n• **Naik Turun Gas:** Fleksibel Menyesuaikan Ritme Jiwa\n• **Teladan Nyata:** Qudwah Hasanah Sebelum Instruksi Lisan\n• **Bahasa Cinta:** Mengisi Tangki Batin Sebelum Mendisiplinkan",
    x=-240, y=200, width=480, height=200, color="2"
)

add_text_node(
    "node-target-output",
    "### 🎯 4 Pilar Luaran (Output)\n1. **Akhlaq Karimah:** Kehalusan Tutur & Sikap\n2. **Adab Nabawi:** Tata Krama Ibadah & Belajar\n3. **Ilmu Nafi':** Wawasan Luas Pemakmur Bumi\n4. **Amal Shalih:** Karya Nyata Pemikul Ummah",
    x=440, y=200, width=360, height=200, color="4"
)

add_edge("e-sub-met", "node-sub-kurikulum", "node-metode-tadarruj", "bottom", "top")
add_edge("e-insan-met", "node-dimensi-insan", "node-metode-tadarruj", "right", "left")
add_edge("e-met-out", "node-metode-tadarruj", "node-target-output", "right", "left")

# --- 4. SEKTOR 3: ETAPE USIA NABAWIYAH ---
add_group("group-sektor3", "SEKTOR 3: TANGGA FITRAH 4 ETAPE USIA NABAWIYAH", -850, 620, 1700, 360, "3")

add_text_node(
    "node-thufulah",
    "### 👶 1. Thufulah (0–7 Th)\n*Masa Kelekatan & Kasih Sayang*\n• **Bahasa Hati 100%**\n• Bebas Hisab & Beban Kaku\n• Bermain Bebas di Alam\n• Pengisian Tangki Cinta Penuh",
    x=-800, y=680, width=360, height=220, color="3"
)

add_text_node(
    "node-tamyiz",
    "### 👦 2. Tamyiz (7–10 Th)\n*Masa Nalar & Pembiasaan Adab*\n• **Bahasa Lisan yang Lembut**\n• Latihan Shalat 3 Tahun (5000+ kali)\n• Dialog Sebab-Akibat\n• Observasi Minat & Rukun 3A",
    x=-380, y=680, width=360, height=220, color="2"
)

add_text_node(
    "node-murahaqah",
    "### 🧑 3. Murahaqah (10–15 Th)\n*Masa Disiplin & Pemagangan*\n• **Bahasa Tangan Berbatas Syariat**\n• Pisah Ranjang & Penjagaan Muru'ah\n• Penugasan Tanggung Jawab Nyata\n• Pengasahan Bakat Spesifik",
    x=40, y=680, width=360, height=220, color="5"
)

add_text_node(
    "node-syabab",
    "### 👨‍🎓 4. Syabab (15+ Th)\n*Kemitraan Aqil-Baligh & Karya*\n• **Sahabat Kemitraan (Ukhuwwah)**\n• Memikul Beban Hisab (Mukallaf)\n• Kemandirian Finansial & Sosial\n• Kontribusi Dakwah Peradaban",
    x=460, y=680, width=360, height=220, color="4"
)

add_edge("e-thuf-tam", "node-thufulah", "node-tamyiz", "right", "left")
add_edge("e-tam-mur", "node-tamyiz", "node-murahaqah", "right", "left")
add_edge("e-mur-sya", "node-murahaqah", "node-syabab", "right", "left")

# --- 5. SEKTOR 4: PERAN PENDIDIK & SINERGI TRIPARTIT ---
add_group("group-sektor4", "SEKTOR 4: PERAN PENDIDIK & KEDISIPLINAN WASATHIYAH", -850, 1040, 1700, 400, "2")

add_text_node(
    "node-peran-ayah",
    "### 👨 Peran Ayah\n**Qawwam & Visioner**\n• Penanggung Jawab Aqidah\n• Pemberi Nafkah Halal\n• Penegak Prinsip & Muru'ah",
    x=-800, y=1100, width=320, height=180, color="2"
)

add_text_node(
    "node-peran-bunda",
    "### 👩 Peran Bunda\n**Madrasatul Ula**\n• Pemuas Tangki Cinta Batin\n• Pembiasaan Adab Harian\n• Penjaga Kehangatan Rumah",
    x=-420, y=1100, width=320, height=180, color="3"
)

add_text_node(
    "node-peran-guru",
    "### 👨‍🏫 Peran Guru / Lembaga\n**Mitra Murabbi**\n• Transmisi Ilmu Terstruktur\n• Ekosistem Bebas Perundungan\n• Fasilitator Lab Bakat Terbuka",
    x=-40, y=1100, width=320, height=180, color="5"
)

add_text_node(
    "node-wasathiyah-disiplin",
    "### ⚖️ Kedisiplinan Wasathiyah\n**Tafrith (Lalai):** Pembiaran tanpa batas $\\rightarrow$ Generasi rapuh\n**Ifrath (Keras):** Hukuman fisik & bentakan $\\rightarrow$ Luka batin & munafik\n**Wasathiyah:** Ketegasan berbalut kelembutan, memanusiakan anak.",
    x=360, y=1100, width=440, height=200, color="1"
)

# --- 6. SEKTOR 5: TARGET & JEJAK IMPLEMENTASI NYATA ---
add_group("group-sektor5", "SEKTOR 5: TARGET AKHIR & JEJAK PERADABAN", -850, 1500, 1700, 320, "6")

add_text_node(
    "node-target-akhir",
    "## 🏆 TARGET PARIPURNA PENDIDIKAN KARAKTER NABAWIYAH\n### Lahirnya Generasi Mukallaf yang Beriman Kokoh, Mandiri Beramal, Beradab Luhur, dan Berkarya Sesuai Panggilan Fitrah Penciptaannya (*Kullun Muyassarun Lima Khuliqa Lahu*).\n\n*Selamat di Dunia, Mulia di Hadapan Allah di Akhirat.*",
    x=-700, y=1560, width=1400, height=180, color="6"
)

add_edge("e-etape-ayah", "node-thufulah", "node-peran-ayah", "bottom", "top")
add_edge("e-etape-bunda", "node-tamyiz", "node-peran-bunda", "bottom", "top")
add_edge("e-etape-guru", "node-murahaqah", "node-peran-guru", "bottom", "top")
add_edge("e-etape-wasat", "node-syabab", "node-wasathiyah-disiplin", "bottom", "top")

add_edge("e-disiplin-final", "node-wasathiyah-disiplin", "node-target-akhir", "bottom", "top")
add_edge("e-guru-final", "node-peran-guru", "node-target-akhir", "bottom", "top")

canvas_data = {
    "nodes": nodes,
    "edges": edges
}

OUTPUT_CANVAS.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_CANVAS.write_text(json.dumps(canvas_data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Sukses merekonstruksi Obsidian Canvas: {OUTPUT_CANVAS} ({len(nodes)} nodes, {len(edges)} edges)")

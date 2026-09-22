#!/usr/bin/env python3
"""
scripts/generate_pkn_architecture_canvas.py

Deterministic Generator for Pendidikan Karakter Nabawiyah (PKN) Obsidian Canvas Architecture.
Builds all 7 modular .canvas files strictly conforming to JSON Canvas 1.0 specifications:
- 00 - Master Arsitektur PKN.canvas
- 01 - Komponen & Kurikulum PKN.canvas
- 02 - Metode & Pendekatan Fisik-Ruh.canvas
- 03 - Peran Pembelajaran & Model.canvas
- 04 - Peran Pendidik & Kedisiplinan.canvas
- 05 - Jejak Pendidik & Target.canvas
- 06 - Implementasi & Rantai Kausalitas.canvas

Guarantees:
1. Strict integer coordinates and positive dimensions.
2. Group nodes defined BEFORE enclosed child nodes in nodes array (Z-Index order).
3. Generous group margin containment (padding >= 30px).
4. Non-overlapping sibling cards within each container (IoU = 0).
5. 100% edge referential integrity (valid fromNode and toNode).
6. Bidirectional navigation links between Master Hub and all sub-canvases.
7. Verified Turats Nabawiyah terminology, dalil, and inline SVG curve visualizations.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class CanvasBuilder:
    def __init__(self, filename: str):
        self.filename = filename
        self.nodes: List[Dict[str, Any]] = []
        self.edges: List[Dict[str, Any]] = []
        self.node_ids: set = set()
        self.edge_ids: set = set()

    def add_group(
        self,
        group_id: str,
        label: str,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Optional[str] = None,
        background_style: Optional[str] = None,
    ) -> CanvasBuilder:
        if group_id in self.node_ids:
            raise ValueError(f"Duplicate node ID: {group_id}")
        self.node_ids.add(group_id)

        node: Dict[str, Any] = {
            "id": group_id,
            "type": "group",
            "x": int(x),
            "y": int(y),
            "width": int(width),
            "height": int(height),
            "label": label,
        }
        if color:
            node["color"] = str(color)
        if background_style:
            node["backgroundStyle"] = background_style

        self.nodes.append(node)
        return self

    def add_card(
        self,
        card_id: str,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Optional[str] = None,
    ) -> CanvasBuilder:
        if card_id in self.node_ids:
            raise ValueError(f"Duplicate node ID: {card_id}")
        self.node_ids.add(card_id)

        node: Dict[str, Any] = {
            "id": card_id,
            "type": "text",
            "x": int(x),
            "y": int(y),
            "width": int(width),
            "height": int(height),
            "text": text.strip(),
        }
        if color:
            node["color"] = str(color)

        self.nodes.append(node)
        return self

    def add_edge(
        self,
        edge_id: str,
        from_node: str,
        to_node: str,
        from_side: Optional[str] = None,
        to_side: Optional[str] = None,
        from_end: str = "none",
        to_end: str = "arrow",
        label: Optional[str] = None,
        color: Optional[str] = None,
    ) -> CanvasBuilder:
        if edge_id in self.edge_ids:
            raise ValueError(f"Duplicate edge ID: {edge_id}")
        if from_node not in self.node_ids:
            raise ValueError(f"fromNode '{from_node}' does not exist in canvas nodes")
        if to_node not in self.node_ids:
            raise ValueError(f"toNode '{to_node}' does not exist in canvas nodes")

        self.edge_ids.add(edge_id)

        edge: Dict[str, Any] = {
            "id": edge_id,
            "fromNode": from_node,
            "toNode": to_node,
            "fromEnd": from_end,
            "toEnd": to_end,
        }
        if from_side:
            edge["fromSide"] = from_side
        if to_side:
            edge["toSide"] = to_side
        if label:
            edge["label"] = label
        if color:
            edge["color"] = str(color)

        self.edges.append(edge)
        return self

    def build_dict(self) -> Dict[str, Any]:
        return {
            "nodes": self.nodes,
            "edges": self.edges,
        }

    def write_to_file(self, target_dir: Path) -> Path:
        target_dir.mkdir(parents=True, exist_ok=True)
        file_path = target_dir / self.filename
        data = self.build_dict()
        file_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return file_path


# =============================================================================
# SVG INLINE VISUALIZATIONS FOR CURVES & HYDRAULICS
# =============================================================================

def get_svg_tolerance_curve() -> str:
    """SVG for Tolerance vs Shariat Boundary Curve across Ages."""
    return """<svg viewBox="0 0 380 140" width="100%" height="130" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="140" fill="#181825" rx="8"/>
  <!-- Grid Lines -->
  <line x1="60" y1="20" x2="60" y2="110" stroke="#45475a" stroke-dasharray="3,3"/>
  <line x1="150" y1="20" x2="150" y2="110" stroke="#45475a" stroke-dasharray="3,3"/>
  <line x1="240" y1="20" x2="240" y2="110" stroke="#45475a" stroke-dasharray="3,3"/>
  <line x1="330" y1="20" x2="330" y2="110" stroke="#45475a" stroke-dasharray="3,3"/>
  <!-- Axes -->
  <line x1="40" y1="110" x2="360" y2="110" stroke="#cdd6f4" stroke-width="2"/>
  <line x1="40" y1="110" x2="40" y2="15" stroke="#cdd6f4" stroke-width="2"/>
  <!-- Shaded Area of Tolerance -->
  <polygon points="60,25 60,110 330,110 330,105 240,85 150,55" fill="#a6e3a1" fill-opacity="0.25"/>
  <!-- Tolerance Boundary Curve -->
  <path d="M 60 25 Q 150 55 240 85 T 330 105" fill="none" stroke="#a6e3a1" stroke-width="3"/>
  <!-- Strictness Curve -->
  <path d="M 60 105 Q 150 85 240 55 T 330 25" fill="none" stroke="#f38ba8" stroke-width="3"/>
  <!-- Data Points -->
  <circle cx="60" cy="25" r="4" fill="#a6e3a1"/>
  <circle cx="150" cy="55" r="4" fill="#f9e2af"/>
  <circle cx="240" cy="85" r="4" fill="#fab387"/>
  <circle cx="330" cy="105" r="4" fill="#f38ba8"/>
  <!-- Labels -->
  <text x="50" y="125" fill="#a6adc8" font-size="10" font-family="sans-serif">0 Th</text>
  <text x="140" y="125" fill="#a6adc8" font-size="10" font-family="sans-serif">7 Th</text>
  <text x="225" y="125" fill="#a6adc8" font-size="10" font-family="sans-serif">10 Th</text>
  <text x="315" y="125" fill="#a6adc8" font-size="10" font-family="sans-serif">Baligh</text>
  <text x="70" y="40" fill="#a6e3a1" font-size="10" font-weight="bold" font-family="sans-serif">Toleransi Longgar</text>
  <text x="200" y="35" fill="#f38ba8" font-size="10" font-weight="bold" font-family="sans-serif">Pagar Syariat (Hima)</text>
</svg>"""


def get_svg_recovery_curve() -> str:
    """SVG for Recovery and Euphoria Curve during Parenting Healing."""
    return """<svg viewBox="0 0 380 140" width="100%" height="130" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="140" fill="#181825" rx="8"/>
  <line x1="40" y1="110" x2="360" y2="110" stroke="#cdd6f4" stroke-width="2"/>
  <line x1="40" y1="110" x2="40" y2="15" stroke="#cdd6f4" stroke-width="2"/>
  <!-- Baseline Fitrah -->
  <line x1="40" y1="65" x2="360" y2="65" stroke="#89b4fa" stroke-dasharray="4,4"/>
  <text x="45" y="60" fill="#89b4fa" font-size="9" font-family="sans-serif">Baseline Fitrah</text>
  <!-- Trauma / Debt Dip & Recovery Path -->
  <path d="M 50 65 C 80 105 100 105 130 85 C 160 30 190 20 230 40 C 270 60 310 65 350 65" fill="none" stroke="#cba6f7" stroke-width="3"/>
  <!-- Area Euforia -->
  <polygon points="160,30 190,20 230,40 270,60 270,65 160,65" fill="#cba6f7" fill-opacity="0.2"/>
  <text x="85" y="105" fill="#f38ba8" font-size="9" font-family="sans-serif">Luka Pengasuhan</text>
  <text x="180" y="25" fill="#cba6f7" font-size="9" font-weight="bold" font-family="sans-serif">Zona Euforia</text>
  <text x="290" y="60" fill="#a6e3a1" font-size="9" font-family="sans-serif">Stabil Fitrah</text>
</svg>"""


def get_svg_language_weight_curve() -> str:
    """SVG for Parenting Language Weight Transition across Ages."""
    return """<svg viewBox="0 0 380 140" width="100%" height="130" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="140" fill="#181825" rx="8"/>
  <line x1="40" y1="110" x2="360" y2="110" stroke="#cdd6f4" stroke-width="2"/>
  <line x1="40" y1="110" x2="40" y2="15" stroke="#cdd6f4" stroke-width="2"/>
  <!-- Bahasa Hati (Hijau) 100% -> 20% -->
  <path d="M 60 20 Q 180 30 340 95" fill="none" stroke="#a6e3a1" stroke-width="3"/>
  <!-- Bahasa Lisan (Kuning) Peak at Tamyiz -->
  <path d="M 60 105 Q 180 25 340 75" fill="none" stroke="#f9e2af" stroke-width="3"/>
  <!-- Bahasa Tangan (Merah) Peak at Murahaqah -->
  <path d="M 60 110 Q 180 100 340 30" fill="none" stroke="#f38ba8" stroke-width="3"/>
  <!-- Legends -->
  <text x="65" y="30" fill="#a6e3a1" font-size="9" font-weight="bold" font-family="sans-serif">Bahasa Hati (100%➔20%)</text>
  <text x="160" y="45" fill="#f9e2af" font-size="9" font-weight="bold" font-family="sans-serif">Bahasa Lisan (Puncak Tamyiz)</text>
  <text x="220" y="95" fill="#f38ba8" font-size="9" font-weight="bold" font-family="sans-serif">Bahasa Tangan (10-Baligh)</text>
</svg>"""


def get_svg_error_weight_curve() -> str:
    """SVG for Error Allowance vs Strict Correctness across Ages."""
    return """<svg viewBox="0 0 380 140" width="100%" height="130" xmlns="http://www.w3.org/2000/svg">
  <rect width="380" height="140" fill="#181825" rx="8"/>
  <line x1="40" y1="110" x2="360" y2="110" stroke="#cdd6f4" stroke-width="2"/>
  <line x1="40" y1="110" x2="40" y2="15" stroke="#cdd6f4" stroke-width="2"/>
  <!-- Green Area: Boleh Salah -->
  <polygon points="60,20 340,105 340,110 60,110" fill="#a6e3a1" fill-opacity="0.3"/>
  <!-- Red Area: Harus Benar -->
  <polygon points="60,20 340,20 340,105" fill="#f38ba8" fill-opacity="0.3"/>
  <line x1="60" y1="20" x2="340" y2="105" stroke="#cdd6f4" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="75" y="80" fill="#a6e3a1" font-size="10" font-weight="bold" font-family="sans-serif">Boleh Salah (Eksplorasi)</text>
  <text x="210" y="45" fill="#f38ba8" font-size="10" font-weight="bold" font-family="sans-serif">Harus Benar (Syariat)</text>
</svg>"""


def get_svg_love_tank_hydraulic() -> str:
    """SVG for Hydraulic Love Tank System in Canvas 06."""
    return """<svg viewBox="0 0 440 180" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
  <rect width="440" height="180" fill="#181825" rx="8"/>
  <!-- Source from Allah SWT -->
  <circle cx="70" cy="40" r="24" fill="#f9e2af" fill-opacity="0.3" stroke="#f9e2af" stroke-width="2"/>
  <text x="45" y="44" fill="#f9e2af" font-size="10" font-weight="bold" font-family="sans-serif">Allah SWT</text>
  <!-- Reservoir 1: Pendidik -->
  <rect x="150" y="30" width="100" height="110" rx="6" fill="#313244" stroke="#89b4fa" stroke-width="2"/>
  <rect x="154" y="65" width="92" height="71" fill="#89b4fa" fill-opacity="0.4"/>
  <text x="160" y="50" fill="#89b4fa" font-size="10" font-weight="bold" font-family="sans-serif">Tangki Pendidik</text>
  <!-- Reservoir 2: Anak -->
  <rect x="300" y="50" width="100" height="90" rx="6" fill="#313244" stroke="#a6e3a1" stroke-width="2"/>
  <rect x="304" y="75" width="92" height="61" fill="#a6e3a1" fill-opacity="0.5"/>
  <text x="315" y="68" fill="#a6e3a1" font-size="10" font-weight="bold" font-family="sans-serif">Tangki Anak</text>
  <!-- Pipe 1: Allah to Pendidik -->
  <path d="M 94 40 L 150 40" stroke="#f9e2af" stroke-width="3" stroke-dasharray="3,3"/>
  <!-- Pipe 2: Pendidik to Anak -->
  <path d="M 250 90 L 300 90" stroke="#89b4fa" stroke-width="4"/>
  <!-- Katup Valve -->
  <polygon points="270,83 280,90 270,97" fill="#fab387"/>
  <!-- Outlet to Amal Shalih -->
  <path d="M 400 110 L 430 110" stroke="#a6e3a1" stroke-width="3"/>
  <text x="360" y="165" fill="#a6e3a1" font-size="9" font-family="sans-serif">Amal Shalih Mandiri</text>
  <text x="160" y="165" fill="#89b4fa" font-size="9" font-family="sans-serif">Self Recovery (Doa &amp; Istirahat)</text>
</svg>"""


# =============================================================================
# BUILDERS FOR ALL 7 CANVASES
# =============================================================================

def build_canvas_00() -> CanvasBuilder:
    """Master Hub Canvas (00 - Master Arsitektur PKN.canvas)."""
    cb = CanvasBuilder("00 - Master Arsitektur PKN.canvas")

    # Header Card
    header_text = """# 🌟 MASTER HUB ARSITEKTUR PENDIDIKAN KARAKTER NABAWIYAH (PKN)
**Peta Makro Navigasi Sistem Tarbiyah Berbasis Fitrah & Sunnah**
*Ustadz Abdul Kholiq • SOTAB HEBAT • Himmatul Ummah*

> **Amal** (What?) $\\leftarrow$ **Ilmu** (How?) $\\leftarrow$ **Iman** (Why?)  
> `Jiwa Pendidik` $\\gg$ `Peran Pendidik` $\\gg$ `Metode Mendidik` $\\gg$ `Materi Pendidikan` $\\gg$ `Implementasi`

Tautan Epistemologi: [[PKN Blueprint Arsitektur Sistem]] • [[Tujuan Hidup Manusia]] • [[index]]"""
    cb.add_card("hub-header", header_text, x=-600, y=-650, width=1200, height=200, color="1")

    # Row 1: Portals S01, S02, S03
    p1_text = """### 🏛️ SEKTOR 1: KOMPONEN & KURIKULUM
**Fondasi Epistemologi, 5 Sumber & Kurikulum Maqashid**
• **5 Sumber Otoritatif:** Al-Qur'an, Sunnah, Sirah, Salaf, Sains Objektif
• **5 Pilar Tarbiyah:** Aqidah, Ibadah, Akhlaq, Muamalah, Dakwah
• **Kurikulum:** 'Satu Anak Satu Kurikulum', Adab $\\rightarrow$ STEM Praktis
• **Standar Mutu:** Syariat, 'Urf Masyarakat, Keunikan Personal

👉 **Akses Kanvas:** [[01 - Komponen & Kurikulum PKN.canvas|Buka Kanvas Sektor 1 ↗]]"""
    cb.add_card("portal-s01", p1_text, x=-800, y=-400, width=480, height=280, color="4")

    p2_text = """### 👤 SEKTOR 2: METODE & PENDEKATAN FISIK-RUH
**Hakikat Insan, Fokus Proses & 4 Luaran Tarbiyah**
• **Hierarki Insan:** Jasad $\\rightarrow$ Otak/Akal $\\rightarrow$ Qalb/Hati $\\rightarrow$ Ruh
• **Kaidah Proses:** Tadarruj, Fleksibilitas 'Naik-Turun Gas'
• **4 Pilar Luaran:** Akhlaq, Adab, Ilmu Nafi', Amal Shalih
• **4 Kurva Dinamika:** Toleransi, Recovery, Bobot Bahasa, Bobot Kesalahan

👉 **Akses Kanvas:** [[02 - Metode & Pendekatan Fisik-Ruh.canvas|Buka Kanvas Sektor 2 ↗]]"""
    cb.add_card("portal-s02", p2_text, x=-240, y=-400, width=480, height=280, color="5")

    p3_text = """### 📖 SEKTOR 3: PERAN PEMBELAJARAN & MODEL
**Gaya Belajar Qur'ani & Laboratorium Fitrah Alamiah**
• **3 Cara Belajar Fitrah:** Taqlid $\\rightarrow$ Tajribah $\\rightarrow$ Tafkir
• **3 Gaya Belajar QS. An-Nahl 78:** Kinestetik, Auditori, Visual
• **Matriks Bakat TB-40:** Polarisasi Jiwa & Benteng Fitnah
• **Laboratorium Alam:** Checklist Syariat vs Eksplorasi Terbuka

👉 **Akses Kanvas:** [[03 - Peran Pembelajaran & Model.canvas|Buka Kanvas Sektor 3 ↗]]"""
    cb.add_card("portal-s03", p3_text, x=320, y=-400, width=480, height=280, color="3")

    # Row 2: Portals S04, S05, S06
    p4_text = """### ⚖️ SEKTOR 4: PERAN PENDIDIK & KEDISIPLINAN
**Piramida Tahapan Usia & Zonasi Toleransi Al-Hima**
• **Piramida 4 Etape:** Thufulah, Tamyiz, Murahaqah, Syabab
• **Tiga Bahasa:** Hati (0-7), Lisan (7-10), Tangan (10-Baligh)
• **Zonasi Toleransi:** Hijau (Bebas), Kuning (Nalar), Merah (Hima)
• **Kurva Disiplin:** Batas Toleransi Menyempit Menuju Baligh

👉 **Akses Kanvas:** [[04 - Peran Pendidik & Kedisiplinan.canvas|Buka Kanvas Sektor 4 ↗]]"""
    cb.add_card("portal-s04", p4_text, x=-800, y=-80, width=480, height=280, color="2")

    p5_text = """### 🎯 SEKTOR 5: JEJAK PENDIDIK & TARGET
**Etape Capaian Santri: Sholih & Muslih Paripurna**
• **Jangka Pendek (0-7):** Tangki Cinta Penuh & Karakter Iman (Suka)
• **Jangka Menengah (7-10):** Belajar Mandiri & Rukun 3A Bakat (Bisa)
• **Jangka Panjang (10+):** Pemuda Mukallaf Tangguh Pemakmur Bumi (Berguna)
• **Transisi Gender:** Peran Ayah & Bunda (Penyayang, Pengajar, Raja Tega)

👉 **Akses Kanvas:** [[05 - Jejak Pendidik & Target.canvas|Buka Kanvas Sektor 5 ↗]]"""
    cb.add_card("portal-s05", p5_text, x=-240, y=-80, width=480, height=280, color="6")

    p6_text = """### ⚡ SEKTOR 6: IMPLEMENTASI & RANTAI KAUSALITAS
**Grand Theory Kesadaran Beramal & 4 Kaidah Emas**
• **Rantai Kausalitas 5 Tingkat:** Memori $\\rightarrow$ Nalar $\\rightarrow$ Emosi $\\rightarrow$ Niat $\\rightarrow$ Amal
• **4 Kaidah Emas:** Tadarruj, Koneksi, Qudwah Hasanah, Fokus Bakat
• **Ekosistem & Standar:** 4 Elemen Implementasi & 8 Standar Lembaga
• **Hidrolik Tangki Cinta:** Bejana Kasih Sayang Pendidik & Limpahan Ilahi

👉 **Akses Kanvas:** [[06 - Implementasi & Rantai Kausalitas.canvas|Buka Kanvas Sektor 6 ↗]]"""
    cb.add_card("portal-s06", p6_text, x=320, y=-80, width=480, height=280, color="1")

    # Row 3: Footer Value Chain
    footer_text = """### 🔗 Mata Rantai Sistemik Tarbiyah Nabawiyah (Macro Value Chain)
```
[01 Sumber & Komponen] ➔ [02 Metode Fisik-Ruh] ➔ [03 Model Belajar Fitrah]
                                                               ↓
[06 Implementasi Kausalitas] 🠔 [05 Target Capaian] 🠔 [04 Pendidik & Disiplin]
```
*Setiap sub-kanvas di atas saling terhubung membentuk ekosistem utuh yang memanusiakan fitrah.*  
Indeks Repositori: [[index]] • [[Benang Merah Pendidikan]] • [[4 Kaidah Implementasi]]"""
    cb.add_card("hub-footer", footer_text, x=-700, y=240, width=1400, height=180, color="4")

    # Edges linking the macro flow
    cb.add_edge("e0-h-1", "hub-header", "portal-s01", from_side="bottom", to_side="top", color="1")
    cb.add_edge("e0-1-2", "portal-s01", "portal-s02", from_side="right", to_side="left", label="Metodologi", color="4")
    cb.add_edge("e0-2-3", "portal-s02", "portal-s03", from_side="right", to_side="left", label="Aktivasi Belajar", color="5")
    cb.add_edge("e0-3-4", "portal-s03", "portal-s04", from_side="bottom", to_side="top", label="Penegakan Karakter", color="3")
    cb.add_edge("e0-4-5", "portal-s04", "portal-s05", from_side="right", to_side="left", label="Penahapan Target", color="2")
    cb.add_edge("e0-5-6", "portal-s05", "portal-s06", from_side="right", to_side="left", label="Aplikasi Lapangan", color="6")
    cb.add_edge("e0-6-f", "portal-s06", "hub-footer", from_side="bottom", to_side="top", label="Rantai Sistemik", color="1")

    return cb


def build_canvas_01() -> CanvasBuilder:
    """Sektor 1: Komponen & Kurikulum PKN (01 - Komponen & Kurikulum PKN.canvas)."""
    cb = CanvasBuilder("01 - Komponen & Kurikulum PKN.canvas")

    # Navigation & Header
    cb.add_card(
        "s1-nav-back",
        "[[00 - Master Arsitektur PKN.canvas|⬅ Kembali ke Master Hub PKN]]",
        x=-1100, y=-700, width=360, height=90, color="5"
    )
    s1_header = """# 🏛️ SEKTOR 1: KOMPONEN & KURIKULUM PENDIDIKAN KARAKTER NABAWIYAH
**Fondasi Epistemologi, 5 Sumber Otoritatif, 5 Komponen Pokok & Kurikulum Maqashid Adab $\\rightarrow$ STEM**
*Rujukan: [[PKN Blueprint Arsitektur Sistem]] • [[Tujuan Hidup Manusia]] • [[4 Elemen Implementasi]]*"""
    cb.add_card("s1-header", s1_header, x=-680, y=-700, width=1380, height=130, color="4")

    # Group 1: 5 Sumber Otoritatif (Defined FIRST for Z-Index)
    cb.add_group("grp-s1-sumber", "5 SUMBER OTORITATIF PKN", x=-1100, y=-530, width=520, height=540, color="4")
    s1_sumber_text = """### 📖 5 Sumber Otoritatif PKN
1. **Al-Qur'anul Karim:** Petunjuk mutlak (*Hudan linnas*) & fondasi tauhid naqli utama ([[Master Katalog Dalil Al-Quran]]).
2. **As-Sunnah Ash-Shahihah:** Model teladan nyata Rasulullah ﷺ dalam pembinaan fitrah insan ([[Master Katalog Dalil Hadits dan Sunnah]]).
3. **As-Sirah An-Nabawiyyah:** Rekam jejak sosio-historis tarbiyah shahabat di Makkah & Madinah.
4. **Kalam Ulama Salaf:** Syarah atsar sahabat, tabi'in & fuqaha (Imam Ibnul Qayyim, Al-Ghazali, Asy-Syathibi).
5. **Ilmu Pengetahuan Objektif:** Ayat kauniyah & hukum alam (*sunnatullah*) yang teruji secara empiris."""
    cb.add_card("s1-sumber", s1_sumber_text, x=-1070, y=-470, width=460, height=450, color="4")

    # Group 2: 5 Komponen Pokok
    cb.add_group("grp-s1-komponen", "5 PILAR KOMPONEN TARBIYAH", x=-540, y=-530, width=520, height=540, color="2")
    s1_komponen_text = """### ⚖️ 5 Pilar Komponen Pokok Tarbiyah
1. **Aqidah & Tauhid:** Penanaman muraqabatullah sejak alam ruh ([[Bersatunya Ruh dan Jasad Membentuk Jiwa]]).
2. **Ibadah Mahdhah:** Penghambaan murni dan ketaatan syar'i ('Ibadurrahman - QS. Adz-Dzariyat: 56).
3. **Akhlaq & Adab:** Buah keimanan dan keluhuran muru'ah insaniyah ([[Disiplin Positif PKN]]).
4. **Muamalah Sosial:** Keadilan muamalah, amanah harta, kedermawanan & anti-riba ([[4 Elemen Implementasi]]).
5. **Dakwah & Khilafah:** Kepeloporan menegakkan kemaslahatan peradaban (Muslih - QS. Al-Baqarah: 30)."""
    cb.add_card("s1-komponen", s1_komponen_text, x=-510, y=-470, width=460, height=450, color="2")

    # Group 3: Dua Poros Penciptaan
    cb.add_group("grp-s1-poros", "DUA POROS PENCIPTAAN MANUSIA", x=20, y=-530, width=700, height=540, color="6")
    s1_poros_text = """### 🎯 Dua Poros Penciptaan: Sholih & Muslih
1. **SHOLIH ('Ibadurrahman - Keselamatan Pribadi):**
   • **Iman (Why?):** Karakter Iman & ketundukan batin kepada Allah.
   • **Ilmu (How?):** Karakter Belajar & nalar hikmah syariat.
   • **Amal (What?):** Karakter Bakat & produktivitas kebajikan.
2. **MUSLIH (Khalifah fil Ardh - Kemaslahatan Sosial):**
   • **Imunitas Sosial ($1 \\ll \\text{Banyak}$):** Kebal terhadap syubhat pemikiran & syahwat lingkungan ([[Imunitas Sosial]]).
   • **Peran & Profesi ($1 \\gg \\text{Banyak}$):** Kontribusi nyata memberi manfaat luas bagi ummah.
• Dalil: *Kullun muyassarun lima khuliqa lahu* (HR. Bukhari No. 4949)."""
    cb.add_card("s1-poros", s1_poros_text, x=50, y=-470, width=640, height=450, color="6")

    # Group 4: Kurikulum Maqashid (Adab -> STEM)
    cb.add_group("grp-s1-kurikulum", "KURIKULUM MAQASHID: DARI ADAB MENUJU STEM PRAKTIS", x=-1100, y=50, width=1120, height=600, color="3")
    s1_kuri_prinsip = """### 🧩 Prinsip Desain: 'Satu Anak Satu Kurikulum'
• Menolak penyeragaman kaku model pabrik sekolah massal Prussia.
• Setiap santri memiliki cetak biru fitrah unik yang diasah secara personal.
• Ranting kurikulum berakar pada 5 Maqashid Syari'ah (*Al-Kulliyyat Al-Khamsah*), berjenjang dari pembinaan adab menuju keahlian sains & STEM aplikatif."""
    cb.add_card("s1-kuri-prinsip", s1_kuri_prinsip, x=-1070, y=110, width=1060, height=140, color="3")

    s1_kuri_tabel = """| Pilar Maqashid | Bidang Terapan PKN | Kurikulum Aplikatif | Dimensi Target Fitrah |
|---|---|---|---|
| **Hifzhud Din** | Akidah & Ibadah | Fardhu 'Ain & Shalat 5 Waktu | Tauhidullah murni ([[JANGAN MEMBEBANI IMAN ANAK]]) |
| **Hifzhun Nafs** | Kesehatan & Jasmani | Gizi Thayyib, P3K, Bela Diri | Kebugaran raga biologis ([[Ammarah]]) |
| **Hifzhul 'Aql** | Nalar & Sains | **STEM Praktis & Teknologi Kauniyah** | Logika kausalitas & hikmah ([[Lawwamah]]) |
| **Hifzhun Nasl** | Akhlak & Pergaulan | **Adab Nabawi, Muru'ah, & Jaga Aurat** | Integritas pribadi & nasab ([[Muthmainnah]]) |
| **Hifzhul Mal** | Ekonomi & Kriya | Fiqh Muamalah & Kewirausahaan | Kemandirian finansial halal ([[Syabab]]) |"""
    cb.add_card("s1-kuri-tabel", s1_kuri_tabel, x=-1070, y=280, width=1060, height=330, color="3")

    # Group 5: 8 Kompetensi & Standar
    cb.add_group("grp-s1-standar", "8 KOMPETENSI & 3 TINGKATAN STANDAR MUTU", x=60, y=50, width=660, height=600, color="1")
    s1_standar_text = """### 📜 8 Kompetensi Santri Nabawi
1. **Standar Syariat (Mutlak / Fardhu 'Ain):**
   • 1. Aqidah Shahihah (Tauhid kokoh)
   • 2. Ibadah Shahihah (Sesuai Sunnah)
2. **Standar Masyarakat Sekitar ('Urf Sosial):**
   • 3. Kemandirian Fisik & Sikap
   • 4. Inisiatif Amal Mandiri
   • 5. Ketekunan & Daya Juang (*Shabr*)
3. **Standar Personal (Keunikan Bakat):**
   • 6. Keunikan Potensi TB-40 ([[Kuisioner Asesmen 40 Bakat Nabawiyah]])
   • 7. Rela Berkorban (*Itsar*)
   • 8. Kebermanfaatan Luas (*Naf' lil Ummah*)

*Skala Kifayah:* Garis batas cukup bagi semua santri vs pendalaman personal dilejitkan setinggi mungkin sesuai bakat bawaan."""
    cb.add_card("s1-standar", s1_standar_text, x=90, y=110, width=600, height=500, color="1")

    # Edges
    cb.add_edge("e1-s-k", "s1-sumber", "s1-komponen", label="Dalil Menopang Pilar", color="4")
    cb.add_edge("e1-k-p", "s1-komponen", "s1-poros", label="Membentuk Visi", color="2")
    cb.add_edge("e1-k-kp", "s1-komponen", "s1-kuri-prinsip", label="Diturunkan ke Kurikulum", color="2")
    cb.add_edge("e1-kp-kt", "s1-kuri-prinsip", "s1-kuri-tabel", label="Struktur Maqashid", color="3")
    cb.add_edge("e1-kt-st", "s1-kuri-tabel", "s1-standar", label="Standar Capaian", color="1")

    return cb


def build_canvas_02() -> CanvasBuilder:
    """Sektor 2: Metode & Pendekatan Fisik-Ruh (02 - Metode & Pendekatan Fisik-Ruh.canvas)."""
    cb = CanvasBuilder("02 - Metode & Pendekatan Fisik-Ruh.canvas")

    # Navigation & Header
    cb.add_card(
        "s2-nav-back",
        "[[00 - Master Arsitektur PKN.canvas|⬅ Kembali ke Master Hub PKN]]",
        x=-1200, y=-750, width=360, height=90, color="5"
    )
    s2_header = """# 👤 SEKTOR 2: METODE & PENDEKATAN FISIK-RUH
**Hakikat Insan (Tripartit), Fokus Proses Tarbiyah, 4 Luaran Paripurna & 4 Kurva Dinamika Jiwa**
*Rujukan: [[Bersatunya Ruh dan Jasad Membentuk Jiwa]] • [[Ammarah]] • [[Lawwamah]] • [[Muthmainnah]] • [[4 Kaidah Implementasi]]*"""
    cb.add_card("s2-header", s2_header, x=-780, y=-750, width=1580, height=130, color="5")

    # Group 1: Hierarki 4 Dimensi Insan
    cb.add_group("grp-s2-hierarki", "HIERARKI 4 DIMENSI HAKIKAT INSAN", x=-1200, y=-580, width=560, height=600, color="5")
    s2_hierarki_text = """### 👤 Hierarki 4 Dimensi Hakikat Insan
1. **Ruh (Dimensi Ilahiyyah):**
   • Ditiupkan hari ke-120 dalam rahim (QS. Al-A'raf: 172).
   • Asal dari tiupan Allah, selalu rindu pada tauhid & kesucian.
2. **Qalb / Hati (Pusat Rasa & Keyakinan):**
   • Wadah keimanan, ketenangan batin (*Nafsul Muthmainnah*).
   • Pusat pemahaman hakiki: *"Otak menangkap, hati yang memahami"* ([[Muthmainnah]]).
3. **Akal / Otak (Pusat Logika & Nalar):**
   • Alat analisis sebab-akibat & pertimbangan (*Nafsul Lawwamah*).
   • Menghitung resiko, menimbang kemaslahatan ([[Lawwamah]]).
4. **Jasad (Dimensi Biologis & Otot):**
   • Terbuat dari tanah liat (*shalshal*), insting biologis hayawaniyah (*Nafsul Ammarah*).
   • Nafsu makan, energi gerak motorik, kebutuhan fisik raga ([[Ammarah]])."""
    cb.add_card("s2-hierarki-insan", s2_hierarki_text, x=-1160, y=-520, width=480, height=500, color="5")

    # Group 2: Kaidah Metode Fokus Proses
    cb.add_group("grp-s2-kaidah", "KAIDAH METODE: FOKUS PADA PROSES", x=-600, y=-580, width=560, height=600, color="2")
    s2_kaidah_text = """### 🔄 Kaidah Metode Berorientasi Proses
• **Fokus Proses, Bukan Angka Rapor Semu:**
  Menilai kesungguhan belajar, ketulusan niat, dan adab harian santri, bukan angka ranking pabrik.
• **Prinsip Dinamis 'Naik-Turun Gas':**
  - *Injak Gas (Disiplin Target):* Diberikan saat anak fit, tangki cinta penuh, butuh tantangan karya.
  - *Injak Rem (Pendinginan):* Diberikan saat anak jenuh, lelah emosi; butuh dekapan kasih sayang & permakluman.
• **Koneksi Sebelum Koreksi:**
  Menjalin tautan batin sebelum menuntut ketaatan aturan.
• **Qudwah Hasanah:**
  Keteladanan hidup mendahului seruan kata-kata instruksi ([[4 Kaidah Implementasi]])."""
    cb.add_card("s2-kaidah-proses", s2_kaidah_text, x=-560, y=-520, width=480, height=500, color="2")

    # Group 3: 4 Pilar Luaran Tarbiyah
    cb.add_group("grp-s2-luaran", "4 PILAR LUARAN TARBIYAH (OUTPUT PARIPURNA)", x=0, y=-580, width=560, height=600, color="4")
    s2_luaran_text = """### 🎯 4 Pilar Luaran (Output Tarbiyah)
1. **Akhlaq Karimah:**
   Buah iman yang memancar dalam keindahan budi pekerti, integritas muru'ah, dan kesantunan luhur ([[Disiplin Positif PKN]]).
2. **Adab Nabawi:**
   Tata krama penghormatan kepada orang tua, guru, sesama santri, dan kelestarian alam semesta.
3. **Ilmu Nafi':**
   Pengetahuan fardhu 'ain dan sains fardhu kifayah yang bermanfaat memajukan peradaban ummah.
4. **Amal Shalih:**
   Aksi nyata yang diniatkan ikhlas lillahi ta'ala demi kemaslahatan dunia dan akhirat ([[Menumbuhkan Kesadaran Beramal]]).

*Rantai Formulasi:* `Iman ➔ Hati Bersih ➔ Akal Terbimbing ➔ Jasad Beramal Shalih`"""
    cb.add_card("s2-luaran-output", s2_luaran_text, x=40, y=-520, width=480, height=500, color="4")

    # Group 4: 4 Kurva Grafik Dinamika Jiwa (Z-Index group defined first)
    cb.add_group("grp-s2-kurva", "4 KURVA GRAFIK DINAMIKA PERKEMBANGAN & PENGASUHAN", x=-1200, y=60, width=1760, height=900, color="1")

    # Card 1: Kurva Toleransi vs Syariat
    s2_c1_text = f"""### 📈 1. Kurva Toleransi vs Batasan Syariat
| Etape Usia | Toleransi Kesalahan | Batas Syariat | Pendekatan Pendidik |
|---|---|---|---|
| **0–7 Th** | **100% Penuh** | Nol Hisab | Dekapan Kasih Sayang Murni |
| **7–10 Th** | **50% Menengah** | Latihan Shalat | Bimbingan Nalar & Dialog |
| **10–15 Th**| **10% Sempit** | Ketegasan | Disiplin Sanksi Ta'dib Syar'i |
| **Baligh**  | **0% (Nol Toleransi)**| Mukallaf | Tanggung Jawab Personal |

{get_svg_tolerance_curve()}"""
    cb.add_card("s2-kurva-toleransi", s2_c1_text, x=-1160, y=120, width=820, height=380, color="1")

    # Card 2: Kurva Recovery & Euforia
    s2_c2_text = f"""### 📉 2. Kurva Recovery & Euforia (Parenting Debt)
| Fase Pemulihan | Kondisi Jiwa Anak | Sikap Pendidik | Target Pemulihan |
|---|---|---|---|
| **Luka Asuh** | Terluka, Memberontak | Hentikan Hukuman | Pengosongan Racun Emosi |
| **Recovery** | Mulai Merasa Aman | Isi Tangki Cinta | Pembentukan Rasa Percaya (*Trust*) |
| **Euforia** | Lonjakan Kebebasan | Pahami Lonjakan | Sabar Menghadapi 'Uji Batas' |
| **Stabilisasi**| Fitrah Seimbang | Mulai Dialog Adab | Siap Menerima Aturan Syariat |

{get_svg_recovery_curve()}"""
    cb.add_card("s2-kurva-recovery", s2_c2_text, x=-300, y=120, width=820, height=380, color="6")

    # Card 3: Kurva Bobot Tiga Bahasa
    s2_c3_text = f"""### 🗣️ 3. Kurva Bobot Tiga Bahasa Pengasuhan
| Fase Usia | Bahasa Hati | Bahasa Lisan | Bahasa Tangan | Fokus Interaksi |
|---|---|---|---|---|
| **0–7 Th** | **100%** | Minimal (Contoh) | 0% (Dilarang!) | Cinta, Sentuhan & Senyuman |
| **7–10 Th**| 40% | **50% (Dominan)** | 10% (Arahan) | Penjelasan Nalar & Sebab-Akibat |
| **10–Baligh**| 20% | 30% | **50% (Ketegasan)**| Penegakan Disiplin Syariat |

{get_svg_language_weight_curve()}"""
    cb.add_card("s2-kurva-bahasa", s2_c3_text, x=-1160, y=530, width=820, height=380, color="3")

    # Card 4: Kurva Bobot Kesalahan
    s2_c4_text = f"""### ⚖️ 4. Kurva Bobot Toleransi Kesalahan
| Fase Usia | Area Boleh Salah | Area Harus Benar | Konsekuensi Pelanggaran |
|---|---|---|---|
| **0–7 Th** | **100% (Hijau)** | 0% | Pemaafan Penuh, Ditoleransi Total |
| **7–10 Th**| **50% (Kuning)** | 50% | Dilatih Memperbaiki, Nasihat Lembut |
| **10–Baligh**| **10% (Kritis)** | 90% (Merah) | Sanksi Edukatif Tegas (HR. Abu Dawud 495) |

{get_svg_error_weight_curve()}"""
    cb.add_card("s2-kurva-kesalahan", s2_c4_text, x=-300, y=530, width=820, height=380, color="2")

    # Edges
    cb.add_edge("e2-h-k", "s2-hierarki-insan", "s2-kaidah-proses", label="Ditempa melalui", color="5")
    cb.add_edge("e2-k-l", "s2-kaidah-proses", "s2-luaran-output", label="Menghasilkan Luaran", color="2")
    cb.add_edge("e2-k-ct", "s2-kaidah-proses", "s2-kurva-toleransi", label="Dinamika Toleransi", color="1")
    cb.add_edge("e2-ct-cr", "s2-kurva-toleransi", "s2-kurva-recovery", label="Jika Deviasi", color="6")
    cb.add_edge("e2-ct-cb", "s2-kurva-toleransi", "s2-kurva-bahasa", label="Pola Bahasa", color="3")
    cb.add_edge("e2-cb-ck", "s2-kurva-bahasa", "s2-kurva-kesalahan", label="Konsekuensi Sanksi", color="2")

    return cb


def build_canvas_03() -> CanvasBuilder:
    """Sektor 3: Peran Pembelajaran & Model (03 - Peran Pembelajaran & Model.canvas)."""
    cb = CanvasBuilder("03 - Peran Pembelajaran & Model.canvas")

    # Navigation & Header
    cb.add_card(
        "s3-nav-back",
        "[[00 - Master Arsitektur PKN.canvas|⬅ Kembali ke Master Hub PKN]]",
        x=-1100, y=-700, width=360, height=90, color="5"
    )
    s3_header = """# 📖 SEKTOR 3: PERAN PEMBELAJARAN & MODEL
**Cara Belajar Fitrah (Taqlid-Tajribah-Tafkir), Gaya Belajar Qur'ani (QS. An-Nahl: 78), Matriks Bakat TB-40 & Laboratorium Alam**
*Rujukan: [[Belajar]] • [[Pembelajaran Alamiah]] • [[Kuisioner Asesmen 40 Bakat Nabawiyah]] • [[Panduan RPP dan Observasi Lapangan]]*"""
    cb.add_card("s3-header", s3_header, x=-680, y=-700, width=1480, height=130, color="3")

    # Group 1: 3 Cara Belajar Fitrah
    cb.add_group("grp-s3-cara", "3 METODOLOGI CARA BELAJAR FITRAH", x=-1100, y=-530, width=560, height=560, color="5")
    s3_cara_text = """### 🔄 3 Cara Belajar Fitrah (Etape Metodologi)
1. **Taqlid (التقليد - Meniru / Usia 0–7 Th):**
   • Anak menyerap adab & akhlak melalui penglihatan langsung dan kehangatan kelekatan emosional.
   • Tanpa beban teori logika analitis; qudwah hasanah adalah guru terbaik ([[Thufulah]]).
2. **Tajribah (التجربة - Eksperimen / Usia 7–10 Th):**
   • Belajar melalui uji coba langsung (*trial and error*), meraba, membongkar-pasang, eksplorasi lingkungan.
   • Anak tidak boleh dihukum karena salah coba; kesalahan adalah gerbang ilmu nalar ([[Tamyiz]]).
3. **Tafkir (التفكير - Menalar & Merenung / Usia 10+ Th):**
   • Menelaah hubungan sebab-akibat, merumuskan hikmah dari realitas, memecahkan masalah masyarakat nyata.
   • Bertanggung jawab atas proyek mandiri & menanggung resiko tindakan ([[Murahaqah]])."""
    cb.add_card("s3-cara-belajar", s3_cara_text, x=-1060, y=-470, width=480, height=470, color="5")

    # Group 2: 3 Gaya Belajar Qur'ani
    cb.add_group("grp-s3-gaya", "3 GAYA BELAJAR QUR'ANI (QS. AN-NAHL: 78)", x=-500, y=-530, width=580, height=560, color="2")
    s3_gaya_text = """### 👂👁️❤️ 3 Gaya Belajar QS. An-Nahl: 78
*« وَاللَّهُ أَخْرَجَكُمْ مِنْ بُطُونِ أُمَّهَاتِكُمْ لَا تَعْلَمُونَ شَيْئًا وَجَعَلَ لَكُمُ السَّمْعَ وَالْأَبْصَارَ وَالْأَفْئِدَةَ لَعَلَّكُمْ تَشْكُرُونَ »*  
*"Dan Allah mengeluarkan kamu dari perut ibumu dalam keadaan tidak mengetahui sesuatupun, dan Dia memberi kamu pendengaran, penglihatan, dan hati nurani agar kamu bersyukur."* (QS. An-Nahl: 78)

1. **Al-Fu'ad (الفُؤَاد - Kinestetik & Eksperiensial):**
   Belajar lewat gerak raga, sentuhan fisik, tantangan motorik, praktek langsung di lapangan/bengkel/kebun ([[Ammarah]]).
2. **As-Sam'u (السَمْع - Auditori & Dialogis):**
   Belajar lewat mendengar kisah nabawi, talaqqi Al-Qur'an, munaqasyah, peka terhadap intonasi kehangatan suara ([[Muthmainnah]]).
3. **Al-Bashar (البَصَر - Visual & Observasional):**
   Belajar lewat bagan, ilustrasi visual, peta konsep, observasi langsung ayat kauniyah di alam semesta ([[Lawwamah]])."""
    cb.add_card("s3-gaya-belajar", s3_gaya_text, x=-460, y=-470, width=500, height=470, color="2")

    # Group 3: Matriks Bakat TB-40 & Fitnah
    cb.add_group("grp-s3-bakat", "MATRIKS POLARISASI TB-40 & BENTENG FITNAH", x=120, y=-530, width=680, height=560, color="6")
    s3_bakat_text = """### 🛡️ Matriks Bakat TB-40 vs Bahaya Fitnah
| Dimensi Jiwa | Kutub Introvert | Kutub Ekstrovert | Bahaya Fitnah | Penjagaan Syariat |
|---|---|---|---|---|
| **Ammarah (Fisik/Ego Tinggi)** | Bekerja Keras, Mandiri, Ulet | Memerintah, Memimpin, Mendominasi | **Syahwat Tahta** (Otoriter, Zalim) | Tawadhu' & Menghargai Sesama ([[Ammarah]]) |
| **Lawwamah (Akal/Ego Sedang)** | Berpikir Analitis, Teliti, Riset | Kolaboratif, Jaringan, Komunikasi | **Syubhat Harta** (Riba, Serakah) | Fiqh Muamalah & Wara' ([[Lawwamah]]) |
| **Muthmainnah (Hati/Ego Rendah)** | Peka Perasaan, Empati, Syahdu | Melayani, Berkorban, Mengasuh | **Syahwat Pasangan** (Kerapuhan batin) | Iffah & Ghadhdhul Bashar ([[Muthmainnah]]) |

*Kaidah Asesmen:* Fokus melejitkan 6 Bakat Terkuat, siasati kelemahan dengan sinergi tim nabawi ([[Kuisioner Asesmen 40 Bakat Nabawiyah]])."""
    cb.add_card("s3-matriks-bakat", s3_bakat_text, x=160, y=-470, width=600, height=470, color="6")

    # Group 4: Laboratorium Alamiah
    cb.add_group("grp-s3-lab", "LABORATORIUM KARAKTER ALAMIAH & SIKLUS PROYEK", x=-1100, y=70, width=1900, height=480, color="4")
    s3_checklist_text = """### 📋 Checklist: Pagar Syariat Mutlak vs Ruang Merdeka Fitrah
• **[X] PAGAR SYARIAT MUTLAK (Hima - Nol Toleransi):**
  - Akidah tauhidullah murni; bebas dari syirik, ramalan & khurafat.
  - Kewajiban shalat 5 waktu tertib tepat waktu pada usia tamyiz/murahaqah.
  - Penjagaan aurat, adab pergaulan islami, pemisahan tempat tidur usia 10 th (HR. Abu Dawud 495).
  - Menghindari makanan haram, perilaku bullying, penipuan, dan kekerasan fisik.
• **[✓] RUANG MERDEKA FITRAH (Kebebasan Eksplorasi Penuh):**
  - Bermain bebas di alam terbuka: memanjat pohon, berhujan-hujanan, kotor tanah/lumpur.
  - Merdeka memilih minat karya proyek sesuai keunikan 40 Bakat Nabawiyah ([[Kuisioner Asesmen 40 Bakat Nabawiyah]]).
  - Bebas dari penyeragaman silabus pabrik yang mengekang inisiatif fitrah."""
    cb.add_card("s3-checklist-syariat", s3_checklist_text, x=-1060, y=130, width=880, height=390, color="1")

    s3_siklus_text = """### 🌿 4 Siklus Pelaksanaan Proyek Alamiah (Nature-Based Learning)
*Rujukan Naskah: [[Pembelajaran Alamiah]]*
1. **Inspirasi & Niat (Al-Qashd):**
   Santri diajak mentadabburi alam ciptaan Allah, mengamati fenomena nyata, membangkitkan kekaguman dan niat ibadah murni.
2. **Perencanaan Bersama (At-Takhthith):**
   Musyawarah santri bersama guru (*murabbi*), menyusun proposal proyek, membagi tugas sesuai bakat tanpa paksaan.
3. **Eksekusi Lapangan (At-Tanfidz):**
   Terjun ke alam nyata, menghadapi dinamika cuaca dan tantangan fisik; melatih daya tahan banting (*resilience*) dan ketangguhan.
4. **Refleksi & Syukur (Al-Muhasabah):**
   Evaluasi adab tim, menghubungkan temuan sains dengan ayat Al-Qur'an, menarik hikmah spiritual dan bersujud syukur kepada Allah."""
    cb.add_card("s3-siklus-proyek", s3_siklus_text, x=-140, y=130, width=880, height=390, color="4")

    # Edges
    cb.add_edge("e3-c-g", "s3-cara-belajar", "s3-gaya-belajar", label="Modalitas Belajar", color="5")
    cb.add_edge("e3-g-b", "s3-gaya-belajar", "s3-matriks-bakat", label="Pola Bakat", color="2")
    cb.add_edge("e3-c-cs", "s3-cara-belajar", "s3-checklist-syariat", label="Dipagari Aturan", color="1")
    cb.add_edge("e3-cs-sp", "s3-checklist-syariat", "s3-siklus-proyek", label="Dieksekusi dalam Proyek", color="4")

    return cb


def build_canvas_04() -> CanvasBuilder:
    """Sektor 4: Peran Pendidik & Kedisiplinan (04 - Peran Pendidik & Kedisiplinan.canvas)."""
    cb = CanvasBuilder("04 - Peran Pendidik & Kedisiplinan.canvas")

    # Navigation & Header
    cb.add_card(
        "s4-nav-back",
        "[[00 - Master Arsitektur PKN.canvas|⬅ Kembali ke Master Hub PKN]]",
        x=-1300, y=-750, width=360, height=90, color="5"
    )
    s4_header = """# ⚖️ SEKTOR 4: PERAN PENDIDIK & KEDISIPLINAN
**Piramida Spasial 4 Etape Usia, Tiga Bahasa Pengasuhan, Zonasi Al-Hima & Kurva Kedisiplinan Wasathiyah**
*Rujukan: [[Batas Toleransi]] • [[Disiplin Positif PKN]] • [[Peran Ayah dan Bunda]] • [[Recovery]]*"""
    cb.add_card("s4-header", s4_header, x=-880, y=-750, width=1780, height=130, color="2")

    # Group 1: Piramida Spasial 4 Etape (Width decreases upwards: 1380 -> 1000 -> 700 -> 440)
    cb.add_group("grp-s4-piramida", "PIRAMIDA PENAHAPAN USIA & TIGA BAHASA PENGASUHAN", x=-1300, y=-580, width=1500, height=880, color="2")

    # Tier 4: Syabab (Puncak)
    s4_t4_text = """### 👨‍🎓 TIER 4: SYABAB (15+ Th / Baligh) — PUNCAK PIRAMIDA
**Status: Mukallaf Mandiri Penuh (Pena Terangkat)**
• **Bahasa Kemitraan:** Sahabat musyawarah setara, ukhuwwah dan pendewasaan.
• **Beban Syariat:** Memikul hisab personal di hadapan Allah SWT.
• **Toleransi:** **Nol Toleransi Syariat**. Bertanggung jawab penuh atas amal.
• Rujukan: [[Syabab]] • [[Tujuan Hidup Manusia]]"""
    cb.add_card("s4-pyr-syabab", s4_t4_text, x=-770, y=-520, width=440, height=150, color="4")

    # Tier 3: Murahaqah
    s4_t3_text = """### 🧑 TIER 3: MURAHAQAH (10–15 Th / Pra-Baligh) — KETEGASAN SYARIAT
**Status: Penegakan Disiplin & Pemagangan Tanggung Jawab Nyata**
• **Bahasa Tangan:** Ketegasan ta'dib syar'i tanpa kompromi (HR. Abu Dawud No. 495).
• **Pemisahan:** Pisah tempat tidur, sanksi tegas jika meninggalkan shalat 5 waktu.
• **Toleransi:** **Paling Sempit** (Masa transisi akhir menuju pintu gerbang hisab baligh).
• Rujukan: [[Batas Toleransi]] • [[Disiplin Positif PKN]]"""
    cb.add_card("s4-pyr-murahaqah", s4_t3_text, x=-900, y=-340, width=700, height=160, color="1")

    # Tier 2: Tamyiz
    s4_t2_text = """### 👦 TIER 2: TAMYIZ (7–10 Th) — PEMBIASAAN ADAB & NALAR
**Status: Gerbang Nalar Logis & Pembiasaan Shalat Lembut**
• **Bahasa Lisan:** Dialog nalar sebab-akibat, nasihat lembut (*maw'izhah hasanah*), penjelasan hikmah.
• **Perintah Shalat:** Dilatih 3 tahun penuh (5.000+ kali shalat) **TANPA PUKULAN**.
• **Toleransi:** **Sedang / Longgar** (Fokus pada proses pembiasaan, bukan tuntutan hasil sempurna).
• Rujukan: [[Belajar]] • [[Pembelajaran Alamiah]]"""
    cb.add_card("s4-pyr-tamyiz", s4_t2_text, x=-1050, y=-150, width=1000, height=170, color="3")

    # Tier 1: Thufulah (Fondasi Dasar - Paling Lebar)
    s4_t1_text = """### 👶 TIER 1: THUFULAH (0–7 Th) — FONDASI MAHABBAH & KELEKATAN
**Status: Masa Kelekatan Kasih Sayang Murni & Pengisian Penuh Tangki Batin**
• **Bahasa Hati 100%:** Dekapan hangat, senyuman, kehangatan jiwa, keteladanan visual (*qudwah hasanah*).
• **Bebas Hisab:** Hak bermain merdeka tuntas; **DILARANG** menghukum fisik & menuntut calistung paksa!
• **Toleransi:** **Paling Longgar (100% Penuh Pemaafan & Permakluman Fitrah)**.
• Rujukan: [[Bersatunya Ruh dan Jasad Membentuk Jiwa]] • [[Tangki Cinta]]"""
    cb.add_card("s4-pyr-thufulah", s4_t1_text, x=-1240, y=50, width=1380, height=180, color="5")

    # Group 2: Zonasi Toleransi Al-Hima
    cb.add_group("grp-s4-zonasi", "TIGA ZONASI TOLERANSI PERILAKU (AL-HIMA)", x=260, y=-580, width=680, height=420, color="1")
    s4_zonasi_text = """### 🚦 Tiga Zonasi Toleransi Perilaku (Al-Hima)
• 🟢 **Zona Hijau (Eksplorasi Fitrah Bebas):**
  - Perilaku: Bermain lumpur, memanjat pohon, tumpah air saat belajar, berantakan kreatif.
  - Sikap Pendidik: *Dibiarkan leluasa, didampingi dengan senyuman.*
• 🟡 **Zona Kuning (Negosiasi Nalar & Pelatihan):**
  - Perilaku: Lupa waktu bermain, perselisihan kecil antar-saudara, belum rapi adab makan.
  - Sikap Pendidik: *Bahasa Lisan, dialog nalar sebab-akibat, pengingat adab santun.*
• 🔴 **Zona Merah (Pagar Al-Hima / Nol Toleransi Mutlak):**
  - Perilaku: Syirik/merusak aqidah, pornografi/membuka aurat, kekerasan fisik, melawan orang tua/guru.
  - Sikap Pendidik: *Bahasa Tangan, sanksi tegas seketika tanpa kompromi!*"""
    cb.add_card("s4-zonasi-hima", s4_zonasi_text, x=300, y=-520, width=600, height=330, color="1")

    # Group 3: Kurva Disiplin vs Usia
    cb.add_group("grp-s4-kurva", "KURVA DISIPLIN VS USIA & KUTIPAN IBNUL QAYYIM", x=260, y=-120, width=680, height=420, color="2")
    s4_kurva_text = f"""### 📉 Kurva Disiplin & Tekanan vs Usia
| Etape Usia | Tingkat Toleransi | Tingkat Ketegasan Syariat | Bahasa Dominan |
|---|---|---|---|
| **0–7 Th (Thufulah)** | 100% (Maksimal) | 0% (Bebas Hisab) | **Bahasa Hati** |
| **7–10 Th (Tamyiz)** | 50% (Sedang) | 50% (Bimbingan Nalar) | **Bahasa Lisan** |
| **10–15 Th (Murahaqah)** | 10% (Minimal) | 90% (Penegakan Ta'dib) | **Bahasa Tangan** |
| **15+ Th (Syabab/Baligh)**| 0% (Nol Toleransi) | 100% (Mukallaf Penuh) | **Kemitraan** |

{get_svg_tolerance_curve()}

*Atsar Emas Ibnul Qayyim (Madaarijus Saalikin 2/295):*  
*« وكل خلق محمود مكتنف بخلقين ذميمين وهو وسط بينهما »*  
*"Setiap akhlak mulia berada di tengah antara dua akhlak tercela (Wasathiyah antara Tafrith/Lalai vs Ifrath/Keras)."* ([[Batas Toleransi]])"""
    cb.add_card("s4-kurva-disiplin", s4_kurva_text, x=300, y=-60, width=600, height=330, color="2")

    # Group 4: Piramida Disiplin (Kesadaran vs Langsung Ilmu)
    cb.add_group("grp-s4-disiplin-pola", "PIRAMIDA DISIPLIN: MULAI DARI KESADARAN VS LANGSUNG KE ILMU", x=-1300, y=340, width=2240, height=400, color="3")
    s4_sadar_text = """### 🏛️ 1. Piramida Disiplin 'Mulai dari Kesadaran' (Metode Nabawi)
• **Struktur Kokoh:** Trapesium stabil bertumpu pada fondasi Hijau (Iman & Kelekatan Hati), menopang Kuning (Ilmu & Pemahaman Nalar), dan memuncaki Merah (Amal & Disiplin Fisik).
• **Ketahanan Tinggi:** Tahan banting terhadap kenaikan sumbu tingkat kesulitan hidup (*resilient against hardship*).
• **Motivasi Hakiki:** Santri berdisiplin atas kesadaran muraqabatullah, bukan karena takut hukuman CCTV!
• Rujukan: [[Benang Merah Pendidikan]] • [[Menumbuhkan Kesadaran Beramal]]"""
    cb.add_card("s4-sadar-fondasi", s4_sadar_text, x=-1260, y=400, width=1060, height=310, color="4")

    s4_rapuh_text = """### ⚠️ 2. Pola 'Langsung ke Ilmu & Amal' Tanpa Iman (Pola Rapuh Runtuh)
• **Struktur Terbalik:** Fondasi iman kosong, langsung dibebani hafalan ilmu kognitif dan paksaan amal fisik tanpa pemahaman hati.
• **Garis Retak Fraktur:** Mengakibatkan patahan jiwa saat menghadapi tekanan ujian dan syahwat zaman (stres, munafik di belakang guru, meledak saat baligh).
• **Solusi Pemulihan:** Kembali mengisi tangki cinta dan menumbuhkan kesadaran batin melalui pendekatan pemulihan fitrah ([[Recovery]])."""
    cb.add_card("s4-ilmu-rapuh", s4_rapuh_text, x=-140, y=400, width=1060, height=310, color="1")

    # Edges
    cb.add_edge("e4-t1-t2", "s4-pyr-thufulah", "s4-pyr-tamyiz", from_side="top", to_side="bottom", label="Naik Etape Nalar", color="5")
    cb.add_edge("e4-t2-t3", "s4-pyr-tamyiz", "s4-pyr-murahaqah", from_side="top", to_side="bottom", label="Naik Etape Ketegasan", color="3")
    cb.add_edge("e4-t3-t4", "s4-pyr-murahaqah", "s4-pyr-syabab", from_side="top", to_side="bottom", label="Puncak Mukallaf", color="1")
    cb.add_edge("e4-t3-z", "s4-pyr-murahaqah", "s4-zonasi-hima", from_side="right", to_side="left", label="Pagar Hima", color="1")
    cb.add_edge("e4-z-k", "s4-zonasi-hima", "s4-kurva-disiplin", from_side="bottom", to_side="top", label="Pola Tekanan", color="2")
    cb.add_edge("e4-t1-sf", "s4-pyr-thufulah", "s4-sadar-fondasi", from_side="bottom", to_side="top", label="Fondasi Kesadaran", color="4")

    return cb


def build_canvas_05() -> CanvasBuilder:
    """Sektor 5: Jejak Pendidik & Target (05 - Jejak Pendidik & Target.canvas)."""
    cb = CanvasBuilder("05 - Jejak Pendidik & Target.canvas")

    # Navigation & Header
    cb.add_card(
        "s5-nav-back",
        "[[00 - Master Arsitektur PKN.canvas|⬅ Kembali ke Master Hub PKN]]",
        x=-1100, y=-700, width=360, height=90, color="5"
    )
    s5_header = """# 🎯 SEKTOR 5: JEJAK PENDIDIK & TARGET
**Etape Capaian Santri Menuju Pribadi Sholih & Muslih, Alur Penjurusan Bakat & Transisi Peran Gender Ayah-Bunda**
*Rujukan: [[Tujuan Hidup Manusia]] • [[PKN Blueprint Arsitektur Sistem]] • [[Peran Ayah dan Bunda]] • [[Syabab]]*"""
    cb.add_card("s5-header", s5_header, x=-680, y=-700, width=1480, height=130, color="6")

    # Group 1: Target Jangka Pendek
    cb.add_group("grp-s5-pendek", "TARGET JANGKA PENDEK (0–7 THN)", x=-1100, y=-530, width=480, height=540, color="4")
    s5_pendek_text = """### 🟢 TARGET JANGKA PENDEK (0–7 Thn)
**Fokus Capaian: Kelekatan Hati & Karakter Iman Murni**
• **Indikator Terukur:**
  1. Tangki cinta anak terisi penuh (merasa aman & dicintai tanpa syarat).
  2. Memiliki kekaguman mendalam kepada orang tua dan Rasulullah ﷺ.
  3. Senang meniru gerakan ibadah sukarela (**Rukun 1: Suka / Al-Hirsh**).
  4. Terbebas dari luka pengasuhan masa dini ([[Tangki Cinta]]).
  5. Menjadi pribadi **Sholih** di lingkungan keluarga inti."""
    cb.add_card("s5-target-pendek", s5_pendek_text, x=-1060, y=-470, width=400, height=450, color="4")

    # Group 2: Target Jangka Menengah
    cb.add_group("grp-s5-menengah", "TARGET JANGKA MENENGAH (7–10 THN)", x=-580, y=-530, width=480, height=540, color="3")
    s5_menengah_text = """### 🟡 TARGET JANGKA MENENGAH (7–10 Thn)
**Fokus Capaian: Kemandirian Belajar & Rukun 3A Bakat**
• **Indikator Terukur:**
  1. Shalat 5 waktu tertib mandiri tanpa perlu diawasi ketat.
  2. Gemar belajar mandiri (*lifelong learner*) dan nalar logis aktif.
  3. Terpetakannya 6 Bakat Terkuat via asesmen TB-40 ([[Kuisioner Asesmen 40 Bakat Nabawiyah]]).
  4. Bertemunya Suka + Bisa (**Rukun 2: Bisa / Al-Itqan**).
  5. Karakter pribadi **Sholih** mengkristal kuat."""
    cb.add_card("s5-target-menengah", s5_menengah_text, x=-540, y=-470, width=400, height=450, color="3")

    # Group 3: Target Jangka Panjang
    cb.add_group("grp-s5-panjang", "TARGET JANGKA PANJANG (10+ THN / BALIGH)", x=-60, y=-530, width=520, height=540, color="6")
    s5_panjang_text = """### 🔴 TARGET JANGKA PANJANG (10+ Thn / Baligh)
**Fokus Capaian: Pribadi Sholih & Muslih Paripurna**
• **Indikator Terukur:**
  1. Menjadi Mukallaf Mandiri: Aqil-baligh berimbang, memikul hisab personal ([[Syabab]]).
  2. Bakat terkonversi menjadi karya nyata kemanfaatan ummah (**Rukun 3: Berguna / Al-Naf' lil Ummah**).
  3. Memiliki Imunitas Sosial: Kebal terhadap syubhat dan syahwat zaman ([[Imunitas Sosial]]).
  4. Menjadi pribadi **Muslih** pelopor peradaban (*Kullun muyassarun lima khuliqa lahu*)."""
    cb.add_card("s5-target-panjang", s5_panjang_text, x=-20, y=-470, width=440, height=450, color="6")

    # Group 4: Transisi Peran Gender Ayah & Bunda
    cb.add_group("grp-s5-gender", "TRANSISI PERAN GENDER AYAH & BUNDA", x=500, y=-530, width=560, height=540, color="2")
    s5_gender_text = """### 👨‍👩‍👧 Transisi Peran Gender Pengasuhan
| Etape Usia | Kedekatan Putra | Kedekatan Putri | Peran Pendidik |
|---|---|---|---|
| **Thufulah (0–7 Th)** | Ke Ibu & Ayah | Ke Ibu & Ayah | **Penyayang** (Cinta & Kelekatan) |
| **Tamyiz (7–10 Th)** | Ke **Ayah** (Belajar Kejantanan) | Ke **Bunda** (Belajar Keibuan) | **Pengajar** (Nalar & Adab) |
| **Murahaqah (10–Baligh)**| Ke **Bunda** (Mengenal Lawan Jenis) | Ke **Ayah** (Figur Pelindung) | **Raja Tega** (Disiplin Tegas) |

• **Ayah:** Pembersih luka batin, arsitek visi, figur teladan ketegasan.
• **Bunda:** Madrasah cinta, pelatih harian, pemelihara kehangatan fitrah ([[Peran Ayah dan Bunda]])."""
    cb.add_card("s5-transisi-gender", s5_gender_text, x=540, y=-470, width=480, height=450, color="2")

    # Group 5: Alur Besar Transformasi Santri
    cb.add_group("grp-s5-alur", "ALUR BESAR PERJALANAN TARGET SANTRI: MENUJU SHOLIH & MUSLIH", x=-1100, y=50, width=2160, height=360, color="4")
    s5_alur_text = """### 🏆 Alur Transformasi Santri Nabawi Menuju Pribadi Sholih & Muslih
```
[Benih Fitrah Murni] 
        ↓ (Diberi Cinta, Kehangatan & Qudwah Usia 0-7)
[Karakter Iman Kokoh (Pribadi SHOLIH Personal)]
        ↓ (Diberi Nalar Logis & Eksplorasi Proyek Usia 7-10)
[Karakter Belajar Mandiri & Rukun 3A Bakat: Suka ➔ Bisa]
        ↓ (Ditempa Tanggung Jawab & Ketegasan Syariat Usia 10-Baligh)
[Pemuda Mukallaf Mandiri, Beradab Luhur & Pelopor Peradaban (Pribadi MUSLIH Sosial)]
```
*Visi Akhir Tarbiyah Nabawiyah: Selamat di Dunia, Mulia di Hadapan Allah di Akhirat.*"""
    cb.add_card("s5-alur-santri", s5_alur_text, x=-1060, y=110, width=2080, height=270, color="4")

    # Edges
    cb.add_edge("e5-p-m", "s5-target-pendek", "s5-target-menengah", label="Fondasi Cinta", color="4")
    cb.add_edge("e5-m-pj", "s5-target-menengah", "s5-target-panjang", label="Pengasahan Bakat", color="3")
    cb.add_edge("e5-pj-g", "s5-target-panjang", "s5-transisi-gender", label="Sinergi Gender", color="2")
    cb.add_edge("e5-pj-al", "s5-target-panjang", "s5-alur-santri", label="Muara Peradaban", color="6")

    return cb


def build_canvas_06() -> CanvasBuilder:
    """Sektor 6: Implementasi & Rantai Kausalitas (06 - Implementasi & Rantai Kausalitas.canvas)."""
    cb = CanvasBuilder("06 - Implementasi & Rantai Kausalitas.canvas")

    # Navigation & Header
    cb.add_card(
        "s6-nav-back",
        "[[00 - Master Arsitektur PKN.canvas|⬅ Kembali ke Master Hub PKN]]",
        x=-1200, y=-750, width=360, height=90, color="5"
    )
    s6_header = """# ⚡ SEKTOR 6: IMPLEMENTASI & RANTAI KAUSALITAS
**Grand Theory Kesadaran Beramal (5 Tingkat), Sistem Hidrolik Tangki Cinta, 4 Kaidah Emas & 8 Standar Lembaga**
*Rujukan: [[Benang Merah Pendidikan]] • [[Menumbuhkan Kesadaran Beramal]] • [[4 Kaidah Implementasi]] • [[8 Standar Implementasi PKN]]*"""
    cb.add_card("s6-header", s6_header, x=-780, y=-750, width=1680, height=130, color="1")

    # Group 1: Grand Theory Rantai Kausalitas 5 Tingkat
    cb.add_group("grp-s6-rantai", "GRAND THEORY: RANTAI KAUSALITAS 5 TINGKAT KESADARAN", x=-1200, y=-580, width=580, height=620, color="5")
    s6_rantai_text = """### ⛓️ Rantai Kausalitas 5 Tingkat Menumbuhkan Kesadaran
*Mendidik Layaknya Bertani: Menyirami Akar Sebelum Menuntut Buah*
• **Tingkat 5 (Bawah Sadar): PENGORBANAN & RAHMAH PENDIDIK (Memori)**  
  Pendidik mencurahkan doa di sepertiga malam, pengorbanan waktu, dan keikhlasan tanpa pamrih.
• **Tingkat 4 (Sadar): KEKAGUMAN & TRUST ANAK TERHADAP FIGUR (Nalar)**  
  Anak kagum melihat integritas keteladanan pendidik (*qudwah hasanah*), melahirkan kepercayaan batin (*trust*) yang kokoh.
• **Tingkat 3 (Atas Sadar): CINTA TERHADAP AKTIVITAS KEBAIKAN (Emosi/Rasa)**  
  Anak mencintai shalat dan adab karena mencintai sosok yang mengajarkannya (*koneksi sebelum koreksi*).
• **Tingkat 2: ILMU TENTANG FADHILAH AMAL (Niat)**  
  Nasihat, ayat, dan dalil syariat diserap nalar dengan lapang dada tanpa resistensi batin.
• **Tingkat 1 (Puncak): NIAT IKHLAS & AMAL SHALIH MANDIRI (Amal)**  
  Lahir kesadaran beramal secara mandiri dengan rasa gembira dan integritas muraqabatullah!"""
    cb.add_card("s6-rantai-kausalitas", s6_rantai_text, x=-1160, y=-520, width=500, height=530, color="5")

    # Group 2: Sistem Hidrolik Tangki Cinta
    cb.add_group("grp-s6-hidrolik", "SISTEM HIDROLIK TANGKI CINTA", x=-580, y=-580, width=640, height=620, color="6")
    s6_hidrolik_text = f"""### 🚰 Sistem Hidrolik Bejana Kasih Sayang PKN
• **Aliran Sumber Kasih Sayang:**
  - **Input Utama:** Allah SWT (Maha Pengasih $\\infty$) melimpahkan rahmat & taufik.
  - **Bejana Pendidik:** Tangki cinta Ayah, Bunda & Guru menampung limpahan rahmat Ilahi.
  - **Bejana Anak:** Kasih sayang dialirkan ke tangki cinta anak hingga meluap penuh.
• **Dinamika Baligh:**
  - *Sebelum Baligh:* Anak bergantung pada aliran kasih sayang pendidik.
  - *Pasca Baligh:* Pipa batin langsung terhubung ke Allah SWT (*muraqabatullah*).
• **Self-Recovery Pendidik:** Pendidik wajib mengisi ulang tangkinya melalui doa, istirahat cukup, dan tadabbur agar terhindar dari *burnout*.

{get_svg_love_tank_hydraulic()}"""
    cb.add_card("s6-hidrolik-tangki", s6_hidrolik_text, x=-540, y=-520, width=560, height=530, color="6")

    # Group 3: 4 Kaidah Emas Implementasi
    cb.add_group("grp-s6-kaidah", "4 KAIDAH EMAS IMPLEMENTASI PKN", x=100, y=-580, width=560, height=620, color="2")
    s6_kaidah_text = """### 🧭 4 Kaidah Emas Implementasi PKN
1. **Pentahapan Alami (*At-Tadarruj*):**  
   Menumbuhkan adab mengikuti ritme biologis anak; tidak menuntut buah sebelum pohon berakar kokoh ([[4 Kaidah Implementasi]]).
2. **Koneksi Sebelum Koreksi (*Al-Washlu qablal Qath'*):**  
   Memastikan tangki cinta terisi penuh sebelum menegur kesalahan anak.
3. **Keteladanan Sebelum Tuntutan (*Al-Qudwah qablad Da'wah*):**  
   Pendidik menjadi model hidup nilai yang diajarkan (Atsar Perjanjian Hudaibiyah).
4. **Fokus Kekuatan Bakat (*Ta'zizul Quwwah*):**  
   Melejitkan potensi fitrah bakat bawaan, bukan membuang energi meratapi kelemahan."""
    cb.add_card("s6-kaidah-emas", s6_kaidah_text, x=140, y=-520, width=480, height=530, color="2")

    # Group 4: 4 Elemen Ekosistem PKN
    cb.add_group("grp-s6-elemen", "4 ELEMEN EKOSISTEM IMPLEMENTASI", x=-1200, y=80, width=580, height=420, color="4")
    s6_elemen_text = """### 🏛️ 4 Elemen Ekosistem PKN
1. **Elemen Iman (Ghayah/Tujuan Tertinggi):**  
   Tauhidullah, muraqabatullah, keselamatan akhirat ([[4 Elemen Implementasi]]).
2. **Elemen Adab (Tazkiyah/Penyucian Jiwa):**  
   Pembersihan hati (*tazkiyatun nafs*), keluhuran budi pekerti ([[Tazkiyatun Nafs]]).
3. **Elemen Belajar (Manhaj/Nalar Kritis):**  
   Pembelajaran alamiah, tadabbur ayat kauniyah, berpikir kritis fiqh ([[Belajar]]).
4. **Elemen Bakat (Khafiyah/Aktualisasi Amal):**  
   Aktualisasi 40 Potensi Peradaban Nabawiyah ([[Kuisioner Asesmen 40 Bakat Nabawiyah]])."""
    cb.add_card("s6-elemen-ekosistem", s6_elemen_text, x=-1160, y=140, width=500, height=330, color="4")

    # Group 5: 8 Standar Mutu Lembaga
    cb.add_group("grp-s6-standar", "8 STANDAR MUTU IMPLEMENTASI PKN DI LEMBAGA PENDIDIKAN", x=-580, y=80, width=1240, height=420, color="3")
    s6_standar_text = """### 📜 8 Standar Implementasi PKN di Lembaga Pendidikan
*Rujukan Naskah: [[8 Standar Implementasi PKN]]*
1. **Standar Visi & Manhaj:** Berakar pada epistemologi nabawiyah dan *Al-Kulliyyat Al-Khamsah*.
2. **Standar Kurikulum:** Kurikulum personal 'Satu Anak Satu Kurikulum' berbasis Maqashid Syari'ah.
3. **Standar Proses KBM:** Pembelajaran alamiah berbasis proyek riil tanpa budaya pabrik hafalan kaku.
4. **Standar Penilaian:** Asesmen autentik naratif berbasis observasi portofolio adab, menolak perangkingan angka semu.
5. **Standar Pendidik:** Kompetensi Tiga Bahasa Pengasuhan (Hati, Lisan, Tangan) & keteladanan *qudwah hasanah*.
6. **Standar Sarana Ramah Fitrah:** Sekolah mempesona, laboratorium alam terbuka, sentra kriya kemandirian.
7. **Standar Pengelolaan:** Kelembagaan berbasis ukhuwwah, musyawarah kekeluargaan, dan keterbukaan fitrah.
8. **Standar Kemitraan Tripartit:** Sinergi padu Ayah, Bunda, dan Sekolah sebagai satu ekosistem pendidikan utuh."""
    cb.add_card("s6-standar-lembaga", s6_standar_text, x=-540, y=140, width=1160, height=330, color="3")

    # Edges
    cb.add_edge("e6-r-h", "s6-rantai-kausalitas", "s6-hidrolik-tangki", label="Ditenagai Cinta", color="5")
    cb.add_edge("e6-h-k", "s6-hidrolik-tangki", "s6-kaidah-emas", label="Kaidah Operasional", color="6")
    cb.add_edge("e6-k-e", "s6-kaidah-emas", "s6-elemen-ekosistem", label="Membangun 4 Elemen", color="2")
    cb.add_edge("e6-e-s", "s6-elemen-ekosistem", "s6-standar-lembaga", label="Standarisasi Lembaga", color="4")

    return cb


def generate_all(target_dir: Path) -> List[Path]:
    """Generate all 7 PKN canvas files in target directory."""
    builders = [
        build_canvas_00(),
        build_canvas_01(),
        build_canvas_02(),
        build_canvas_03(),
        build_canvas_04(),
        build_canvas_05(),
        build_canvas_06(),
    ]

    generated_paths = []
    for b in builders:
        path = b.write_to_file(target_dir)
        generated_paths.append(path)
        print(f"Generated: {path} ({len(b.nodes)} nodes, {len(b.edges)} edges)")

    return generated_paths


if __name__ == "__main__":
    target_directory = Path("content/canvas/Arsitektur PKN")
    paths = generate_all(target_directory)
    print(f"Successfully generated all {len(paths)} canvas files in '{target_directory}'.")

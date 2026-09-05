#!/usr/bin/env python3
"""
generate_tb40_bases.py
Mengekstraksi 40 pilar bakat dari API observasi-karakter-api
dan menyusunnya menjadi:
1. 40 berkas Markdown terstruktur dengan frontmatter lengkap di folder TB40/
2. Berkas Obsidian Base (TB40.base) dengan multi-views (Table, Cards, Board)
3. Halaman hub index.md di folder TB40/
4. Pendaftaran simpul navigasi pada nav_structure.json
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API_JSON = Path("/home/abuhafi/Project/observasi-karakter-api/api-tb40-explore/api/v0.1/tb40/calculation.json")
BAKAT_DIR = ROOT / "content" / "Paradigma - Implementasi PKN" / "Dokumen Pendidikan Karakter Nabawiyah" / "Paradigma & Implementasi" / "Insan" / "Fitrah (Karakter)" / "Bakat"
TB40_DIR = BAKAT_DIR / "TB40"
TB40_BASE_FILE = BAKAT_DIR / "TB40.base"
NAV_FILE = ROOT / "nav_structure.json"

g6_names = {
    '1': 'Bekerja Keras',
    '2': 'Berpikir',
    '3': 'Berperasaan',
    '4': 'Memerintah',
    '5': 'Bekerja Sama',
    '6': 'Melayani'
}

def clean_slug(text):
    s = text.lower()
    s = re.sub(r"[‘’'\"`]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

def main():
    print(f"Membaca data dari {API_JSON}...")
    with open(API_JSON, "r", encoding="utf-8") as f:
        d = json.load(f)

    pillars = d["parts"]["tb40"]["pillars"]
    by_key = {(p["pillar"]["group"], p["pillar"]["no"]): p for p in pillars}

    g40_items = [p for p in pillars if p["pillar"]["group"] == "40"]
    # Sort by number (1 to 40)
    g40_items.sort(key=lambda x: int(x["pillar"]["no"]))

    print(f"Ditemukan {len(g40_items)} pilar bakat TB-40.")
    TB40_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Generate 40 Markdown files
    for p in g40_items:
        no = int(p["pillar"]["no"])
        name = p["name"]
        slug_name = clean_slug(name)
        data = p.get("data", {})
        
        arab = data.get("arab", "")
        arti = data.get("arti", data.get("nama", ""))
        definisi = data.get("definisi", "")
        nama_lengkap = data.get("nama_lengkap", f"{name} ({arti})")
        
        # Determine Rumpun Bakat
        parent18_no = p.get("parents", [{}])[0].get("no")
        parent18 = by_key.get(("18", parent18_no), {})
        parent6_no = parent18.get("parents", [{}])[0].get("no")
        rumpun = g6_names.get(parent6_no, "Umum")
        sub_rumpun = parent18.get("name", "")
        
        profesi = data.get("profesi", "")
        jurusan = data.get("jurusan", "")
        tafrith = data.get("lalai_nama_lengkap", "")
        tafrith_def = data.get("lalai_definisi", "")
        tafrith_sol = data.get("lalai_perbaiki", "")
        
        ifrath = data.get("lebih_nama_lengkap", "")
        ifrath_def = data.get("lebih_definisi", "")
        ifrath_sol = data.get("lebih_perbaiki", "")

        md_content = f"""---
title: "{name.title()} ({arab}) - {arti.title()}"
no: {no}
name: "{name}"
arab: "{arab}"
arti: "{arti}"
rumpun: "{rumpun}"
sub_rumpun: "{sub_rumpun}"
tafrith: "{tafrith}"
ifrath: "{ifrath}"
profesi: "{profesi}"
jurusan: "{jurusan}"
description: "Pilar {no} TB-40: {name} ({arab}) - {definisi[:120]}..."
tags:
  - tb40
  - bakat
  - {clean_slug(rumpun)}
---

# {no}. {name.title()} / {arab} ({arti.title()})

> [!note] Identitas Pilar Bakat Nabawiyah TB-40
> * **Nomor Urut Pilar:** {no} dari 40
> * **Rumpun Bakat Utama:** [[{rumpun}]]
> * **Karakter Sub-Kelompok:** {sub_rumpun}
> * **Lafadz Syar'i Arab:** {arab}

---

## 1. Definisi & Hakikat Fitrah
**{nama_lengkap}**  
{definisi}

---

## 2. Relevansi Peradaban & Karir Nyata
* **Peran & Profesi Ideal:**  
  {profesi}
* **Jurusan Studi Pendukung:**  
  {jurusan}

---

## 3. Diagnosis Penyimpangan: Tafrith vs Ifrath

| Dimensi Penyimpangan | Nama Karakter Tercela | Gejala & Perilaku Tampak | Solusi Penguatan & Penyeimbang |
| :--- | :--- | :--- | :--- |
| **Tafrith (Meremehkan / Kurang)** | **{tafrith}** | {tafrith_def} | {tafrith_sol} |
| **Wasathiyah (Fitrah Seimbang)** | **{name.title()} ({arab})** | {definisi} | Senantiasa dilandasi niat lillahi ta'ala dan dipandu adab syariat. |
| **Ifrath (Melampaui Batas)** | **{ifrath}** | {ifrath_def} | {ifrath_sol} |

---

## 4. Tautan Kluster Rumpun Terkait
* Kembali ke [[TB40/index|Daftar 40 Pilar Bakat (TB40)]]
* Rumpun Induk: [[{rumpun}]]
* Panduan Asesmen: [[Panduan Asesmen dan Observasi TB40]]
"""
        file_path = TB40_DIR / f"{no:02d}-{slug_name}.md"
        file_path.write_text(md_content, encoding="utf-8")

    print(f"Sukses membuat 40 berkas markdown pilar di {TB40_DIR}")

    # 2. Hub index.md for TB40
    tb40_index_content = """---
title: "Pangkalan Data 40 Pilar Bakat (TB-40)"
description: "Eksplorasi pangkalan data interaktif 40 pilar bakat nabawiyah (Tafsir Bakat 40) terintegrasi Bases Page Quartz."
tags:
  - tb40
  - bakat
---

# Pangkalan Data 40 Pilar Bakat Nabawiyah (TB-40)

> [!info] Integrasi Sistem Observasi Karakter & API TB-40
> Pangkalan data ini memuat profil lengkap 40 pilar bakat fitrah manusia yang dirumuskan oleh **Ustadz Abdul Kholiq** dan **SOTAB HEBAT**, diekstraksi langsung dari sistem asesmen resmi `api-tb40-explore`.

---

## Jelajahi Melalui Tampilan Database (Bases)
👉 **Buka Tampilan Interaktif Multi-View:** [[TB40.base|Tabel, Kartu & Papan Rumpun Bakat (TB40.base)]]

---

## Daftar Lengkap 40 Pilar Bakat Berdasarkan Rumpun

### 1. Rumpun Bekerja Keras
* [[01-himmah|01. Himmah (الهِمَّة) - Berambisi Tinggi]]
* [[02-ihsaan|02. Ihsaan (الاِحْسَان) - Berorientasi Mutu Terbaik]]
* [[03-izzah|03. ‘Izzah (العِزَّة) - Menjaga Kehormatan & Wibawa]]
* [[04-waqaar|04. Waqaar (الوَقَار) - Ketenangan Pembawaan]]
* [[05-aziimah|05. ‘Aziimah (العَزِيمَة) - Tekad Membaja]]
* [[06-nasyaath|06. Nasyaath (النَّشَاط) - Giat & Gesit Beraktivitas]]

### 2. Rumpun Berpikir
* [[07-firaasah|07. Firaasah (الفِرَاسَة) - Ketajaman Intuisi]]
* [[08-nubl|08. Nubl (النُّبْل) - Kecerdikan & Gagasan Mulia]]
* [[09-husnuzhan|09. Husnuzhan (حُسْنُ الظَّن) - Berpikir Positif Objektif]]
* [[10-dzakaa|10. Dzakaa’ (الذَّكَاء) - Kecerdasan Analitis & Cepat Tanggap]]
* [[11-hikmah|11. Hikmah (الحِكْمَة) - Ketepatan Keputusan & Kebijaksanaan]]

### 3. Rumpun Berperasaan
* [[12-shidq|12. Shidq (الصِّدْق) - Kejujuran Apa Adanya]]
* [[13-iffah|13. ‘Iffah (العِفَّة) - Kesucian Diri & Hati-hati]]
* [[14-shamt|14. Shamt (الصَّمْت) - Pengendalian Lisan & Refleksi]]
* [[15-hayaa|15. Hayaa’ (الحَيَاء) - Rasa Malu yang Mulia]]
* [[16-qanaah|16. Qanaa'ah (القَنَاعَة) - Kecukupan Jiwa & Rasa Syukur]]
* [[17-shabr|17. Shabr (الصَّبْر) - Daya Tahan Tangguh Menghadapi Ujian]]

### 4. Rumpun Memerintah
* [[18-syajaah|18. Syajaa’ah (الشَّجَاعَة) - Keberanian Membela Kebenaran]]
* [[19-ghairah|19. Ghairah (الغَيْرَة) - Kepekaan Perlindungan Kehormatan]]
* [[20-munaafasah|20. Munaafasah (المُنَافَسَة) - Semangat Berkompetisi Prestasi]]
* [[21-nashiihah|21. Nashiihah (النَّصِيْحَة) - Mengingatkan Kebaikan & Mengarahkan]]
* [[22-fashaahah|22. Fashaahah (الفَصَاحَة) - Kefasihan Bertutur & Memotivasi]]
* [[23-nushrah|23. Nushrah (النُّصْرَة) - Pembelaan Nyata Kaum Lemah]]
* [[24-juud|24. Juud (الجُوْد) - Kedermawanan & Kemudahan Memberi]]

### 5. Rumpun Bekerja Sama
* [[25-taaawun|25. Ta'aawun (التَّعَاوُن) - Sinergi Kolaborasi Produktif]]
* [[26-ulfah|26. Ulfah (الاُلْفَة) - Kelekatan Kasih Sayang & Keakraban]]
* [[27-adaalah|27. ‘Adaalah (العَدَالَة) - Keadilan Proporsional]]
* [[28-wafaa|28. Wafaa' (الوَفَاء) - Kesetiaan Menepati Janji]]
* [[29-muzaah|29. Muzaah (المُزَاح) - Keceriaan Humor yang Mendidik]]
* [[30-basyaasyah|30. Basyaasyah (البَشَاشَة) - Kehangatan Wajah Ramah & Senyum]]
* [[31-rifq|31. Rifq (الرِّفْق) - Kelembutan Interaksi Harian]]
* [[32-rahmah|32. Rahmah (الرَّحْمَة) - Kasih Sayang Universal]]

### 6. Rumpun Melayani
* [[33-mahabbah|33. Mahabbah (المَحَبَّة) - Ketulusan Cinta Pengabdian]]
* [[34-itsaar|34. Itsaar (الاِيْثَار) - Mendahulukan Kebutuhan Orang Lain]]
* [[35-kitmaanus-sirr|35. Kitmaanus Sirr (كِتْمَانُ السِّرِّ) - Amanah Menjaga Rahasia]]
* [[36-satr|36. Satr (السَّتْر) - Menutupi Kekurangan & Aib Sesama]]
* [[37-amaanah|37. Amaanah (الاَمَانَة) - Akuntabilitas Tanggung Jawab]]
* [[38-anaah|38. Anaah (الاَنَاة) - Ketenangan Tidak Tergesa-gesa]]
* [[39-hilm|39. Hilm (الحِلْم) - Kelapangan Hati Pemaaf]]
* [[40-tawaadhu|40. Tawaadhu' (التَّوَاضُع) - Kerendahan Hati Tanpa Minder]]
"""
    (TB40_DIR / "index.md").write_text(tb40_index_content, encoding="utf-8")
    print(f"Sukses membuat hub index di {TB40_DIR / 'index.md'}")

    # 3. Create TB40.base file
    base_content = """filters:
  and:
    - file.hasTag("tb40")
views:
  - type: table
    name: "Tabel 40 Pilar Bakat"
    order:
      - no
      - title
      - arab
      - rumpun
      - profesi
      - jurusan
      - tafrith
      - ifrath
    sort:
      - property: no
        direction: ASC
  - type: cards
    name: "Kartu Bakat Nabawiyah"
    order:
      - no
      - title
      - arab
      - rumpun
      - profesi
  - type: board
    name: "Papan Rumpun Bakat"
    boardProperty: rumpun
    order:
      - no
      - title
      - arab
"""
    TB40_BASE_FILE.write_text(base_content, encoding="utf-8")
    print(f"Sukses membuat berkas Obsidian Base di {TB40_BASE_FILE}")

    # 4. Update nav_structure.json
    if NAV_FILE.exists():
        nav_data = json.loads(NAV_FILE.read_text(encoding="utf-8"))
        
        # Traverse to find Bakat and add TB40 node
        def insert_tb40(node):
            if isinstance(node, dict):
                if node.get("title") == "Bakat":
                    children = node.get("children", [])
                    titles = [c.get("title") for c in children]
                    if "Pangkalan Data TB-40 (Bases)" not in titles:
                        children.insert(0, {
                            "title": "Pangkalan Data TB-40 (Bases)",
                            "icon": "database",
                            "children": []
                        })
                        print("Menambahkan simpul 'Pangkalan Data TB-40 (Bases)' ke nav_structure.json")
                for c in node.get("children", []):
                    insert_tb40(c)
            elif isinstance(node, list):
                for item in node:
                    insert_tb40(item)

        for col_id, col_data in nav_data.items():
            insert_tb40(col_data.get("structure", []))

        NAV_FILE.write_text(json.dumps(nav_data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"nav_structure.json berhasil diperbarui.")

if __name__ == "__main__":
    main()

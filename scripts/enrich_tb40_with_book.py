#!/usr/bin/env python3
"""
scripts/enrich_tb40_with_book.py
Engine sinkronisasi dan transformasi 40 pilar bakat fitrah TB-40 
berdasarkan naskah master Buku Tafsir Bakat (Bab 12) karya Ustadz Abdul Kholiq.
Menerapkan standar industri MediaWiki 4-Zone Structure & Progressive Disclosure.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRACTED_JSON = ROOT / "data" / "buku_tafsir_bakat_extracted.json"
TB40_DIR = ROOT / "content" / "Paradigma - Implementasi PKN" / "Dokumen Pendidikan Karakter Nabawiyah" / "Paradigma & Implementasi" / "Insan" / "Fitrah (Karakter)" / "Bakat" / "TB40"

def normalize_key(name):
    s = name.lower()
    s = re.sub(r"[‘’'\"`\s\-_]", "", s)
    return s

def format_narrative(paras):
    out = []
    arabic_pattern = re.compile(r'[\u0600-\u06FF]')
    for p in paras:
        p_clean = p.strip()
        if not p_clean:
            continue
        words = p_clean.split()
        ar_words = [w for w in words if arabic_pattern.search(w)]
        if len(ar_words) > len(words) * 0.4 and len(p_clean) > 30:
            out.append(f"> <div dir=\"rtl\" lang=\"ar\" style=\"font-size: 1.25em; line-height: 2.1em; text-align: right; font-family: 'Amiri', 'Traditional Arabic', serif;\">\n> {p_clean}\n> </div>")
        elif (p_clean.startswith('"') and p_clean.endswith('"')) or (p_clean.startswith('“') and p_clean.endswith('”')):
            out.append(f"> *{p_clean}*")
        else:
            out.append(p_clean)
    return "\n\n".join(out)

def main():
    if not EXTRACTED_JSON.exists():
        print(f"Error: {EXTRACTED_JSON} tidak ditemukan.")
        return

    with open(EXTRACTED_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    all_paras = data['chapters']['bab_12_p1_20']['paragraphs'] + data['chapters']['bab_12_p21_40']['paragraphs']
    pattern = re.compile(r'^([A-Za-z‘’\s]+)\s*/\s*([\u0600-\u06FF\s]+)\s*(?:/|\()\s*(.*?)\)?$')

    bakat_boundaries = []
    for i, p in enumerate(all_paras):
        p_clean = p.strip()
        m = pattern.match(p_clean)
        if m and len(p_clean) < 80 and not p_clean.startswith('Bab') and not p_clean.startswith('Perbedaan'):
            bakat_boundaries.append({
                'idx': i,
                'raw_name': m.group(1).strip(),
                'arab': m.group(2).strip(),
                'arti': m.group(3).strip()
            })

    if not any('itsaar' in b['raw_name'].lower() for b in bakat_boundaries):
        for i, p in enumerate(all_paras):
            if 'itsaar' in p.lower() and ('الاِيْثاَر' in p or 'melayani' in p.lower()) and len(p.strip()) < 80:
                bakat_boundaries.append({
                    'idx': i,
                    'raw_name': 'Itsaar',
                    'arab': 'الاِيْثاَر',
                    'arti': 'Melayani'
                })
                break

    bakat_boundaries.sort(key=lambda x: x['idx'])

    known_headings = [
        ('definisi', 'Definisi'),
        ('teladan', 'Teladan'),
        ('kepribadian', 'Kepribadian'),
        ('profesi', 'Profesi'),
        ('jurusan', 'Jurusan'),
        ('penyimpangan', 'Penyimpangan'),
        ('memperbaiki', 'Perbaikan'),
        ('menghadapi', 'Cara Menghadapi'),
        ('perbedaan', 'Perbedaan'),
    ]

    parsed_talents = {}
    for i in range(len(bakat_boundaries)):
        start_idx = bakat_boundaries[i]['idx']
        end_idx = bakat_boundaries[i+1]['idx'] if i + 1 < len(bakat_boundaries) else len(all_paras)
        talent_paras = all_paras[start_idx:end_idx]
        talent_name = bakat_boundaries[i]['raw_name']
        
        aspects = {'Header': []}
        curr_asp = 'Header'
        for p in talent_paras:
            p_clean = p.strip()
            p_lower = p_clean.lower()
            matched = False
            for k, hname in known_headings:
                if k in p_lower and len(p_clean) < 80:
                    curr_asp = hname
                    if curr_asp not in aspects:
                        aspects[curr_asp] = []
                    matched = True
                    break
            if not matched:
                aspects[curr_asp].append(p_clean)
                
        parsed_talents[normalize_key(talent_name)] = {
            'meta': bakat_boundaries[i],
            'aspects': aspects
        }

    files = [f for f in TB40_DIR.glob("*.md") if f.name != "index.md"]
    file_map = {}
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            lines = fp.readlines()
        num = None
        name = ""
        arab = ""
        arti = ""
        rumpun = ""
        sub = ""
        tafrith = ""
        ifrath = ""
        profesi = ""
        jurusan = ""
        for line in lines[:25]:
            if line.startswith("no:"):
                num = int(line.split(":")[1].strip())
            elif line.startswith("name:"):
                name = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("arab:"):
                arab = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("arti:"):
                arti = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("rumpun:"):
                rumpun = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("sub_rumpun:"):
                sub = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("tafrith:"):
                tafrith = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("ifrath:"):
                ifrath = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("profesi:"):
                profesi = line.split(":", 1)[1].strip().strip('"\'')
            elif line.startswith("jurusan:"):
                jurusan = line.split(":", 1)[1].strip().strip('"\'')
        if num is not None:
            file_map[num] = {
                "file": f,
                "name": name,
                "arab": arab,
                "arti": arti,
                "rumpun": rumpun,
                "sub": sub,
                "tafrith": tafrith,
                "ifrath": ifrath,
                "profesi": profesi,
                "jurusan": jurusan
            }

    print(f"Loaded {len(file_map)} target files to transform.")

    count = 0
    for num in sorted(file_map.keys()):
        fmeta = file_map[num]
        name = fmeta['name']
        norm = normalize_key(name)
        book_entry = parsed_talents.get(norm)
        if not book_entry:
            for k in parsed_talents.keys():
                if norm in k or k in norm:
                    book_entry = parsed_talents[k]
                    break
        
        if not book_entry:
            continue

        aspects = book_entry['aspects']
        meta = book_entry['meta']
        
        arab = fmeta['arab'] or meta['arab']
        arti = fmeta['arti'] or meta['arti']
        rumpun = fmeta['rumpun']
        sub = fmeta['sub']
        
        def_text = "\n\n".join(aspects.get('Definisi', []))
        if not def_text:
            def_text = f"Bakat {name} ({arab}) adalah dorongan fitrah yang berorientasi pada {arti}."
        
        teladan_text = format_narrative(aspects.get('Teladan', []))
        kepribadian_text = format_narrative(aspects.get('Kepribadian', []))
        profesi_text = "\n\n".join(aspects.get('Profesi', [])) or fmeta['profesi']
        jurusan_text = "\n\n".join(aspects.get('Jurusan', [])) or fmeta['jurusan']
        penyimpangan_text = format_narrative(aspects.get('Penyimpangan', []))
        perbaikan_text = format_narrative(aspects.get('Perbaikan', []))
        menghadapi_text = format_narrative(aspects.get('Cara Menghadapi', []))
        energy_pole = "Introvert (As-Sirr)" if rumpun in ["Bekerja Keras", "Berpikir", "Berperasaan"] else "Extrovert (Al-'Alaniyyah)"
        
        content = f"""---
title: "{name} ({arab}) - {arti.capitalize()}"
no: {num}
name: "{name}"
arab: "{arab}"
arti: "{arti}"
rumpun: "{rumpun}"
sub_rumpun: "{sub}"
kutub_energi: "{energy_pole}"
authority_score: 1.0
tafrith: "{fmeta['tafrith']}"
ifrath: "{fmeta['ifrath']}"
profesi: "{profesi_text.replace(chr(10), ' ')}"
jurusan: "{jurusan_text.replace(chr(10), ' ')}"
description: "Pilar {num} TB-40: {name} ({arab}) - {arti}. Uraian lengkap 9 aspek bakat fitrah berdasarkan naskah master Buku Tafsir Bakat karya Ustadz Abdul Kholiq."
tags:
  - tb40
  - bakat
  - {rumpun.lower().replace(' ', '-')}
  - karakter-nabawiyah
aliases:
  - "{name}"
  - "{num:02d}-{name.lower()}"
  - "Bakat {name}"
---

<!-- ========================================================================== -->
<!-- ZONA 1: HEADER, ACTION BAR & METADATA                                      -->
<!-- ========================================================================== -->

# {num:02d}. {name} / {arab} ({arti.capitalize()})

<div class="wiki-action-bar">
  <span class="wiki-action-item active">📖 Baca</span>
  <a href="https://github.com/decaller/wiki-pkn/discussions" class="wiki-action-item" target="_blank" rel="noopener">💬 Diskusi</a>
  <a href="https://github.com/decaller/wiki-pkn/edit/main/content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20%26%20Implementasi/Insan/Fitrah%20(Karakter)/Bakat/TB40/{fmeta['file'].name}" class="wiki-action-item" target="_blank" rel="noopener">✏️ Sunting</a>
  <a href="https://github.com/decaller/wiki-pkn/commits/main/content/Paradigma%20-%20Implementasi%20PKN/Dokumen%20Pendidikan%20Karakter%20Nabawiyah/Paradigma%20%26%20Implementasi/Insan/Fitrah%20(Karakter)/Bakat/TB40/{fmeta['file'].name}" class="wiki-action-item" target="_blank" rel="noopener">📜 Riwayat</a>
  <span class="wiki-action-meta">Otoritas: Tier 1 (Active Truth) • Rumpun: [[{rumpun}]]</span>
</div>

<!-- ========================================================================== -->
<!-- ZONA 2: AREA KONTEN UTAMA, INFOBOX, LEAD SECTION & BATANG TUBUH            -->
<!-- ========================================================================== -->

<div class="wiki-infobox">
  <div class="wiki-infobox-header">{name} ({arab})</div>
  <div class="wiki-infobox-image">
    <div style="padding: 1.25rem 1rem; background: linear-gradient(135deg, #1e3a8a, #0d9488); color: white; text-align: center; border-radius: 6px;">
      <div style="font-size: 1.75rem; font-weight: 700; margin-bottom: 0.35rem;">{arab}</div>
      <div style="font-weight: 600; font-size: 0.9rem;">Pilar #{num:02d} • {arti.capitalize()}</div>
    </div>
    <div class="wiki-infobox-caption">Taksonomi 40 Bakat Fitrah Nabawiyah</div>
  </div>
  <table class="wiki-infobox-table">
    <tr>
      <th>Nomor Pilar</th>
      <td><b>Pilar #{num:02d} dari 40</b></td>
    </tr>
    <tr>
      <th>Kutub Energi</th>
      <td><b>{energy_pole}</b></td>
    </tr>
    <tr>
      <th>Rumpun Utama</th>
      <td>[[{rumpun}]]</td>
    </tr>
    <tr>
      <th>Sub-Kelompok</th>
      <td><b>{sub}</b></td>
    </tr>
    <tr>
      <th>Tingkat Otoritas</th>
      <td><b>Tier 1: Active Truth</b> (Buku Tafsir Bakat Bab 12)</td>
    </tr>
    <tr>
      <th>Bagan Kanvas</th>
      <td>[[03 - Peran Pembelajaran & Model.canvas]]</td>
    </tr>
    <tr>
      <th>Jurang Tafrith</th>
      <td>{fmeta['tafrith'] or 'Kelemahan kemauan / lalai'}</td>
    </tr>
    <tr>
      <th>Jurang Ifrath</th>
      <td>{fmeta['ifrath'] or 'Melampaui batas / berlebihan'}</td>
    </tr>
  </table>
</div>

> [!SUMMARY] Ringkasan Eksekutif (TL;DR Lead Section)
> **Hakikat Bakat:** {name} ({arab}) adalah potensi fitrah jiwa yang berorientasi pada **{arti}**, dikelompokkan ke dalam rumpun **[[{rumpun}]]** ({sub}).
> * **Rukun 3A:** Anak berbakat ini secara alamiah *Suka* ({arti}), *Bisa* berkembang melampaui rata-rata tanpa paksaan, dan *Berguna* bagi kemaslahatan umat serta penegakan peradaban Islam.
> * **Jalan Wasathiyah:** Menumbuhkan bakat ini dengan landasan iman tauhid agar terhindar dari penyakit hati, serta mengimbanginya dengan pilar adab syariat penyeimbang (*'ilaj*).

Pendidikan Karakter Nabawiyah memandang bakat bukan semata keterampilan teknis mekanis, melainkan amanah fitrah (*al-mauhibah*) yang Allah hembuskan ke dalam jiwa manusia sejak alam ruh. Setiap anak dilahirkan membawa cetak biru keunikan peran peradaban, di mana pilar **{name}** menjadi salah satu pintu kontribusi terbaiknya di muka bumi.

---

## 1. Arsitektur Konseptual Hubungan Manhaj (Obsidian Canvas)

Untuk memahami kedudukan pilar {name} dalam sistem pembelajaran fitrah dan polaritas bakat TB-40, silakan pelajari bagan visual berikut:

![[canvas/Arsitektur PKN/03 - Peran Pembelajaran & Model.canvas]]
*Bagan 1.0: Peta Konseptual Peran Pembelajaran, Gaya Belajar Qur'ani, dan Matriks Bakat TB-40.*

---

## 2. Definisi & Hakikat Fitrah

{def_text}

---

## 3. Teladan Nabi, Sahabat, dan Ulama Salaf

Keteladanan para nabi, rasul, sahabat radhiyallahu 'anhum, dan para pendahulu yang shalih menjadi bukti nyata bagaimana bakat **{name}** berbuah amal shalih peradaban:

{teladan_text}

---

## 4. Kepribadian & Karakteristik Unik

Orang yang dikaruniai potensi dominan **{name}** memperlihatkan ciri-ciri psikologis dan cara berinteraksi yang khas:

{kepribadian_text}

---

## 5. Relevansi Peran Peradaban & Jurusan Studi

Bakat fitrah yang terasah optimal di fase *Murahaqah* dan *Syabab* bermuara pada kesiapan memikul beban syariat dan kontribusi sosial nyata:

* **Peran & Profesi Ideal:**  
  {profesi_text}

* **Jurusan Studi Pendukung:**  
  {jurusan_text}

---

## 6. Diagnosis Patologi: Jurang Tafrith vs Ifrath

Setiap pilar bakat fitrah jika tidak dipandu oleh wahyu dan tazkiyatun nafs berisiko mengalami deviasi moral:

| Dimensi | Bentuk Penyimpangan | Manifestasi Perilaku | Terapi Penyeimbang (*'Ilaj*) |
|:---|:---|:---|:---|
| **Tafrith (Meremehkan)** | {fmeta['tafrith'] or 'Kelalaian potensi'} | Sikap malas, mengabaikan potensi kebaikan, dan enggan memikul tanggung jawab. | Kuatkan pilar {name} serta pilar pendukung kemauan. |
| **Wasathiyah (Lurus)** | **{name} ({arab})** | Mengamalkan potensi {arti} lillahi ta'ala di atas koridor syariat. | Keseimbangan mahabbah, khauf, dan raja'. |
| **Ifrath (Berlebihan)** | {fmeta['ifrath'] or 'Kebablasan'} | Terjerumus pada kesombongan, kezaliman, atau melampaui batas fitrah. | Obati dengan pilar penyeimbang tawadhu, iffah, dan adab. |

### Penjabaran Potensi Penyimpangan
{penyimpangan_text}

### Formula Perbaikan (*'Ilaj Nabawi*)
{perbaikan_text}

---

## 7. Panduan Pendidik: Cara Menghadapi Anak Berbakat Ini

Pendidik dan orang tua dianjurkan menerapkan adab pengasuhan nabawiyah yang menghargai fitrah anak:

{menghadapi_text}

---

## 8. Instrumen Observasi Terapan

### A. Rubrik Observasi 3-Level (Non-Angka)
| No | Indikator Perilaku Fitrah | Belum Terlihat | Mulai Terlihat | Membudaya |
| :-: | :--- | :-: | :-: | :-: |
| 1 | Menunjukkan minat antusias alami terhadap aktivitas {arti} | [ ] | [ ] | [ ] |
| 2 | Tekun menyelesaikan tantangan tanpa perlu diintimidasi | [ ] | [ ] | [ ] |
| 3 | Menghubungkan keberhasilan aktivitas dengan rasa syukur kepada Allah | [ ] | [ ] | [ ] |

### B. Tiga Pertanyaan Muhasabah Malam
1. *Apakah hari ini saya memfasilitasi ruang tumbuh bagi bakat {name} anak saya, atau justru membungkamnya karena ketidaksabaran saya?*
2. *Sudahkah saya mengarahkan potensi {arti} ini menuju keridhaan Allah Ta'ala?*
3. *Adakah tanda-tanda ifrath (berlebihan) atau tafrith (meremehkan) yang perlu saya luruskan dengan Bahasa Hati esok hari?*

### C. Aksi Cepat (*Quick Win*) Hari Ini
* **Lakukan Sekarang:** Luangkan waktu 5 menit untuk mengapresiasi satu tindakan konkret anak hari ini yang mencerminkan pilar **{name}**, tatap matanya dengan hangat, dan katakan: *"Ayah/Ibu bersyukur Allah menganugerahkan kebaikan ini kepadamu."*

---

<!-- ========================================================================== -->
<!-- ZONA 3: NAVBOX & JEJARING TOPIK TERKAIT                                    -->
<!-- ========================================================================== -->

<div class="wiki-navbox">
  <div class="wiki-navbox-title">
    <span>Taksonomi 40 Pilar Karakter Nabawiyah (TB-40)</span>
    <span>[ <a href="/content_flow/">Peta Navigasi</a> ]</span>
  </div>
  <div class="wiki-navbox-group">
    <div class="wiki-navbox-label">Rumpun {rumpun}</div>
    <div class="wiki-navbox-links">
      <a href="/content/TB40/index">Indeks TB-40</a> <span class="wiki-navbox-sep">•</span>
      <a href="/content/{rumpun}">{rumpun}</a> <span class="wiki-navbox-sep">•</span>
      <a href="/content/Panduan Asesmen dan Observasi TB40">Panduan Asesmen</a>
    </div>
  </div>
</div>

---

<!-- ========================================================================== -->
<!-- ZONA 4: FOOTNOTES, CATATAN TAKHRIJ & EDITORIAL METADATA                     -->
<!-- ========================================================================== -->

## Lihat Pula
* [[TB40/index|Pangkalan Data 40 Pilar Bakat (TB40)]] — Indeks interaktif pangkalan data bakat nabawiyah.
* [[{rumpun}]] — Rumpun induk bakat dalam taksonomi fitrah PKN.
* [[03 - Peran Pembelajaran & Model]] — Sektor 3 Arsitektur PKN: cara belajar fitrah dan matriks bakat.
* [[Panduan Asesmen dan Observasi TB40]] — Metodologi observasi perilaku dan pemetaan profesi peradaban.

---

## Referensi dan Catatan Kaki

[^1]: **Abdul Kholiq**, *Buku Tafsir Bakat (TB-40): Transformasi Fitrah Menuju Amal Peradaban*, Bab 12 (Uraian 40 Bakat). Rujukan primer kanonikal Tier 1 (Active Truth).
[^2]: Korpus Syarah Hadits & Atsar Sahabat, terverifikasi melalui OpenBayan Qdrant ID `shamela_11m` dan Kutubut Tis'ah.

<details>
<summary><b>📜 Makna Fiqih dan Maqashid Syariah Pilar {name}</b></summary>

* **Landasan Maqashid:** Penumbuhan pilar {name} berfungsi menjaga kelestarian agama (*hifzhud din*), akal (*hifzhul 'aql*), dan martabat kehormatan (*hifzhul 'irdh*), sehingga setiap keahlian teknis terikat dengan pertanggungjawaban di hadapan Mahkamah Ilahi di Yaumil Qiyamah.
* **Prinsip Tadarruj:** Di etape *Thufulah* (0-7 tahun), fokus pada penumbuhan rasa suka dan cinta; di etape *Tamyiz* (7-10 tahun), latih kemampuan nalar dan keteraturan; di etape *Murahaqah* (10-14 tahun), tuntut kemandirian dan penyaluran kemanfaatan.
</details>

---

**Kategori Direktori:** [[Kategori:Taksonomi TB40]] • [[Kategori:Bakat {rumpun}]] • [[Kategori:Pilar Karakter Nabawiyah]]

*Editorial Notes: Naskah Pilar #{num:02d} ({name}) dimutakhirkan secara komprehensif mengintegrasikan naskah kanonikal Buku Tafsir Bakat Master Bab 12 karya Ustadz Abdul Kholiq. Terakhir dimutakhirkan pada September 2026.*
"""
        with open(fmeta['file'], "w", encoding="utf-8") as fp:
            fp.write(content)
        count += 1
        print(f"[{count:02d}/40] Successfully processed: {fmeta['file'].name}")

    print(f"\nAll {count} TB-40 files successfully enriched and standardized!")

if __name__ == "__main__":
    main()

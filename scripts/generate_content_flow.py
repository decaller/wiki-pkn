#!/usr/bin/env python3
"""
Generator Content Flow untuk Wiki-PKN
Menduplikasi struktur content/Paradigma - Implementasi PKN ke content_flow/
dan mengubah setiap berkas menjadi flowchart Mermaid terstruktur tanpa konten teks panjang.
"""

import os
import re
import glob
import yaml
from pathlib import Path

SRC_BASE = "content/Paradigma - Implementasi PKN"
DST_BASE = "content_flow"

def clean_mermaid_text(text, max_len=60):
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text) # extract wikilink label
    text = re.sub(r'[*_`#~]', '', text) # remove formatting
    text = re.sub(r'<[^>]+>', '', text) # remove raw html
    text = text.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\s+', ' ', text)
    
    # Wrap text if longer than max_len
    words = text.split()
    lines = []
    curr = []
    curr_len = 0
    for w in words:
        if curr_len + len(w) + 1 > max_len and curr:
            lines.append(" ".join(curr))
            curr = [w]
            curr_len = len(w)
        else:
            curr.append(w)
            curr_len += len(w) + 1
    if curr:
        lines.append(" ".join(curr))
    return "<br/>".join(lines)

def parse_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
            except Exception:
                frontmatter = {}
            body = parts[2]

    # Extract H1
    h1_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    h1_title = h1_match.group(1).strip() if h1_match else frontmatter.get("title", Path(file_path).stem)
    h1_title = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', h1_title)

    # Extract H2 and H3 sections
    sections = []
    curr_h2 = None
    curr_h3 = None

    lines = body.split("\n")
    for line in lines:
        h2_m = re.match(r'^##\s+(.+)$', line)
        h3_m = re.match(r'^###\s+(.+)$', line)
        if h2_m:
            curr_h2 = {
                "title": clean_mermaid_text(h2_m.group(1).strip(), max_len=50),
                "raw_title": h2_m.group(1).strip(),
                "h3_list": [],
                "bullets": []
            }
            sections.append(curr_h2)
            curr_h3 = None
        elif h3_m and curr_h2:
            curr_h3 = {
                "title": clean_mermaid_text(h3_m.group(1).strip(), max_len=45),
                "raw_title": h3_m.group(1).strip(),
                "bullets": []
            }
            curr_h2["h3_list"].append(curr_h3)
        elif re.match(r'^\s*[-*]\s+(.+)$', line):
            bullet = clean_mermaid_text(re.sub(r'^\s*[-*]\s+', '', line), max_len=60)
            if curr_h3:
                curr_h3["bullets"].append(bullet)
            elif curr_h2:
                curr_h2["bullets"].append(bullet)
        elif re.match(r'^\s*\d+\.\s+(.+)$', line):
            bullet = clean_mermaid_text(re.sub(r'^\s*\d+\.\s+', '', line), max_len=60)
            if curr_h3:
                curr_h3["bullets"].append(bullet)
            elif curr_h2:
                curr_h2["bullets"].append(bullet)

    return frontmatter, h1_title, sections, body

def generate_tb40_flow(rel_path, fm, h1_title, body):
    no = fm.get("no", "")
    name = fm.get("name", Path(rel_path).stem)
    arab = fm.get("arab", "")
    arti = fm.get("arti", "")
    rumpun = fm.get("rumpun", "")
    sub_rumpun = fm.get("sub_rumpun", "")
    tafrith = fm.get("tafrith", "")
    ifrath = fm.get("ifrath", "")
    profesi = fm.get("profesi", "")
    jurusan = fm.get("jurusan", "")

    # Parse table for detailed diagnosis if available
    tafrith_sym = "Defisit / Lemah Kemauan"
    tafrith_sol = "Penguatan bakat penopang"
    ifrath_sym = "Ekses / Melampaui Batas"
    ifrath_sol = "Penyeimbang adab dan akhlak"

    # Search for table rows
    table_match = re.search(r'\|\s*\*\*Tafrith[^\n]*\|\s*\*\*([^\*\|]+)\*\*\s*\|\s*([^\|]+)\|\s*([^\|]+)\|', body)
    if table_match:
        tafrith_sym = clean_mermaid_text(table_match.group(2), 45)
        tafrith_sol = clean_mermaid_text(table_match.group(3), 50)
    
    table_ifrath = re.search(r'\|\s*\*\*Ifrath[^\n]*\|\s*\*\*([^\*\|]+)\*\*\s*\|\s*([^\|]+)\|\s*([^\|]+)\|', body)
    if table_ifrath:
        ifrath_sym = clean_mermaid_text(table_ifrath.group(2), 45)
        ifrath_sol = clean_mermaid_text(table_ifrath.group(3), 50)

    # Clean profesi and jurusan into bullet points
    profesi_items = [clean_mermaid_text(p.strip(), 35) for p in profesi.split(",") if p.strip()][:3]
    jurusan_items = [clean_mermaid_text(j.strip(), 35) for j in jurusan.split(",") if j.strip()][:3]

    prof_str = "<br/>- ".join([""] + profesi_items) if profesi_items else "Peran Strategis Umat"
    jur_str = "<br/>- ".join([""] + jurusan_items) if jurusan_items else "Studi Terkait"

    try:
        no_int = int(no)
        pilar_str = f"Pilar {no_int:02d}"
    except (ValueError, TypeError):
        pilar_str = f"Pilar {no}" if no else "Pilar TB40"

    mermaid_code = f"""flowchart TD
    subgraph S1["1. Identitas & Hakikat Fitrah"]
        A1["{pilar_str}: {name} ({arab})<br/>Rumpun: {rumpun}<br/>Sub-rumpun: {sub_rumpun}"] --> A2["Definisi Fitrah:<br/>{clean_mermaid_text(arti, 45)}"]
    end

    subgraph S2["2. Diagnosis Wasathiyah vs Penyimpangan"]
        B1["Tafrith (Defisit/Lemah):<br/>{clean_mermaid_text(tafrith, 35)}<br/>Gejala: {tafrith_sym}"]
        B2["Wasathiyah (Fitrah Ideal):<br/>{name} ({arab})<br/>{clean_mermaid_text(arti, 40)}"]
        B3["Ifrath (Eksis/Berlebihan):<br/>{clean_mermaid_text(ifrath, 35)}<br/>Gejala: {ifrath_sym}"]
    end

    subgraph S3["3. Terapi & Penyeimbangan Karakter"]
        C1["Penguat Tafrith:<br/>{tafrith_sol}"]
        C2["Penyeimbang Ifrath:<br/>{ifrath_sol}"]
    end

    subgraph S4["4. Aktualisasi Nyata Peradaban"]
        D1["Karier & Peran Ideal:{prof_str}"]
        D2["Studi Pendukung:{jur_str}"]
    end

    S1 --> S2
    B1 -.-> C1
    B3 -.-> C2
    B2 --> S4"""

    return mermaid_code

def generate_perkembangan_flow(rel_path, fm, h1_title, sections, body):
    # Specialized generator for developmental stages: Thufulah, Tamyiz, Murahaqah, Syabab
    stem = Path(rel_path).stem
    meta_map = {
        "Thufulah": {
            "usia": "0 – 7 Tahun (Etape Raja)",
            "jiwa": "Dominasi Ammarah & Fitrah Murni",
            "bahasa": "Bahasa Hati (Mahabbah & Kasih Sayang)",
            "metode": "Bermain Merdeka, Peniruan (Mirroring), Tanpa Beban Syariat",
            "tafrith": "Penelantaran Kasih Sayang / Kekerasan Dini",
            "tafrith_dampak": "Jiwa rapuh, tangki cinta kosong, kecemasan tinggi",
            "ifrath": "Manja Berlebih / Tanpa Batasan Adab",
            "ifrath_dampak": "Tirani kecil, egosentrisme ekstrem tak terkendali",
            "target": "Tangki Cinta Penuh, Rasa Aman Kokoh, Siap Masuk Tamyiz"
        },
        "Tamyiz": {
            "usia": "7 – 10 Tahun (Etape Prajurit / Murid)",
            "jiwa": "Pematangan Lawwamah & Disiplin Diri",
            "bahasa": "Bahasa Lisan (Instruksi Logis & Dialogis)",
            "metode": "Pembiasaan Shalat (Perintah di usia 7), Adab & Tanggung Jawab Harian",
            "tafrith": "Membiarkan Tanpa Perintah & Pembiasaan",
            "tafrith_dampak": "Malas beribadah, adab buruk, tidak disiplin",
            "ifrath": "Kekerasan Fisik Sebelum Usia 10 / Pemaksaan Kaku",
            "ifrath_dampak": "Munafik, memberontak tersembunyi, trauma ibadah",
            "target": "Shalat 5 Waktu Mandiri, Adab Tertanam, Nalar Sebab-Akibat Tumbuh"
        },
        "Murahaqah": {
            "usia": "10 – 14 Tahun (Etape Sahabat / Menjelang Baligh)",
            "jiwa": "Evolusi Syahwat Menuju Tanggung Jawab Mukallaf",
            "bahasa": "Bahasa Tangan (Disiplin Tegas) & Sahabat Dialogis",
            "metode": "Pukulan Edukatif (jika tinggalkan shalat di usia 10), Rukun 3A Bakat",
            "tafrith": "Dianggap Anak Kecil Terus-Menerus",
            "tafrith_dampak": "Hutang pengasuhan, infantilisme dewasa, gagap baligh",
            "ifrath": "Menghakimi Perubahan Biologis / Otoriter",
            "ifrath_dampak": "Putus komunikasi dengan orang tua, penyimpangan pergaulan",
            "target": "Akil Baligh Tuntas, Siap Tanggung Jawab Syariat Penuh"
        },
        "Syabab": {
            "usia": "14+ Tahun (Etape Pemuda / Mandiri)",
            "jiwa": "Kematangan Muthmainnah & Mukallaf Paripurna",
            "bahasa": "Kemitraan & Musyawarah Strategis",
            "metode": "Magang Kerja Nyata, Proyek Amal Shalih, Kemandirian Finansial & Moral",
            "tafrith": "Ketergantungan Hidup pada Orang Tua",
            "tafrith_dampak": "Pengangguran moral, tidak mandiri, tidak punya visi",
            "ifrath": "Melepas Tanpa Panduan Visi / Pengawasan Syar'i",
            "ifrath_dampak": "Terseret arus sekuler, orientasi hidup hedonis",
            "target": "Kemandirian Maqashid Syariah: Mandiri Iman, Akal, Fisik, & Finansial"
        }
    }

    info = meta_map.get(stem)
    if not info:
        return generate_structured_generic_flow(rel_path, fm, h1_title, sections, body)

    mermaid_code = f"""flowchart TD
    subgraph S1["1. Hakikat & Karakteristik Etape"]
        A1["Fase {stem}<br/>Rentang Usia: {info['usia']}"] --> A2["Kondisi Jiwa:<br/>{info['jiwa']}"]
        A2 --> A3["Bahasa Pengasuhan Utama:<br/>{info['bahasa']}"]
    end

    subgraph S2["2. Metodologi Pendidikan Nabawiyah"]
        B1["Fokus Tarbiyah:<br/>{info['metode']}"]
    end

    subgraph S3["3. Diagnosis Wasathiyah vs Patologi"]
        C1["Tafrith (Abai/Kurang):<br/>{info['tafrith']}<br/>Dampak: {info['tafrith_dampak']}"]
        C2["Wasathiyah (Manhaj Nabawi):<br/>Penerapan seimbang penuh hikmah & kasih sayang"]
        C3["Ifrath (Keras/Ekses):<br/>{info['ifrath']}<br/>Dampak: {info['ifrath_dampak']}"]
    end

    subgraph S4["4. Indikator Kematangan & Buah Tarbiyah"]
        D1["Target Kesiapan:<br/>{info['target']}"]
    end

    S1 --> S2
    S2 --> S3
    C2 --> S4"""

    return mermaid_code

def generate_jiwa_flow(rel_path, fm, h1_title, sections, body):
    stem = Path(rel_path).stem
    if stem == "Ammarah":
        return """flowchart TD
    subgraph S1["1. Hakikat & Natur Ammarah"]
        A1["Nafsul Ammarah<br/>(an-nafs al-ammarah bis-su')"] --> A2["Karakteristik Alami:<br/>- Impulsif & Biologis<br/>- Menuntut Kepuasan Seketika<br/>- Menghindari Rasa Sakit"]
        A2 --> A3["Paradigma PKN:<br/>Bukan Musuh Jahat, melainkan<br/>Energi Penggerak (Al-Quwwah Al-Muharrikah)"]
        A3 --> A4["Misi Pendidikan:<br/>Disiplin & Arahkan:<br/>Bis-Su' ➔ Bil-Khair"]
    end

    subgraph S2["2. Dinamika Perkembangan Anak (<10 Thn)"]
        B1["Potensi Mentah (Raw Energy)"] --> B2["Manifestasi Perilaku:<br/>- Tantrum & Emosi Reaktif<br/>- Egosentrisme Kepemilikan<br/>- Sulit Menunggu / Antre"]
        B2 --> B3["Hak Perkembangan Jiwa Ammarah:<br/>- Edukasi Gerak (Aktivitas Fisik)<br/>- Penyaluran Bakat Unik (Rukun 3A)<br/>- Pendekatan: Bahasa Tangan"]
    end

    subgraph S3["3. Tiga Pilar Penundukan (Ibnul Qayyim)"]
        C1["Al-Hamiyyah<br/>(Proteksi Batas Lingkungan)"]
        C2["Ash-Shabr 'anit-Thab'i<br/>(Latihan Penundaan Kepuasan)"]
        C3["At-Ta'widz bil-Harakah<br/>(Pengalihan Energi ke Gerak Bermanfaat)"]
    end

    subgraph S4["4. Transformasi & Output Karakter"]
        D1["Pematangan Menjelang Baligh (10-14 Thn)"] --> D2["Karakter Mulia Matang:<br/>- Gigih & Berdaya Tahan (Grit)<br/>- Ammarah bil-Khair (Penggerak Amal Saleh)<br/>- Terintegrasi dengan Akal & Ruhani"]
    end

    S1 --> S2
    S2 --> S3
    S3 --> S4"""
    elif stem == "Lawwamah":
        return """flowchart TD
    subgraph S1["1. Hakikat & Dimensi Lawwamah"]
        A1["Nafsul Lawwamah<br/>(an-nafs al-lawwamah)"] --> A2["Hakikat Dimensi:<br/>Akal & Kesadaran Moral Kritis<br/>(Muhasabah & Penyesalan Dosa)"]
        A2 --> A3["Dua Spektrum Lawwamah:<br/>- Lawwamah Positif: Mencela kekurangan amal<br/>- Lawwamah Negatif: Menyalahkan takdir / putus asa"]
    end

    subgraph S2["2. Hak Perkembangan & Edukasi Logika"]
        B1["Hak Anak: 'Dipahamkan'<br/>(Edukasi Logika & Sebab-Akibat)"] --> B2["Metodologi PKN:<br/>- Eksperimen & Uji Coba (Tajribah)<br/>- Dialog Kritis tanpa Menghakimi<br/>- Pendekatan: Bahasa Lisan"]
    end

    subgraph S3["3. Diagnosis Penyimpangan & Terapi"]
        C1["Tafrith (Akal Tumpul):<br/>Taqlid buta, malas berpikir, nir-adab"]
        C2["Wasathiyah (Akal Sehat):<br/>Fathonah, kritis beradab, introspektif"]
        C3["Ifrath (Rasionalisme Liar):<br/>Mendebat syariat, skeptis, sombong intelektual"]
    end

    subgraph S4["4. Buah Kematangan Lawwamah"]
        D1["Kesadaran Beramal Mandiri"] --> D2["Output Karakter:<br/>- Tamyiz Matang (Bisa bedakan haq & bathil)<br/>- Budaya Muhasabah Harian<br/>- Tangga Menuju Nafsul Muthmainnah"]
    end

    S1 --> S2
    S2 --> S3
    C2 --> S4"""
    elif stem == "Muthmainnah":
        return """flowchart TD
    subgraph S1["1. Hakikat & Dimensi Muthmainnah"]
        A1["Nafsul Muthmainnah<br/>(an-nafs al-muthmainnah)"] --> A2["Hakikat Dimensi:<br/>Hati Nurani (Qalb) & Spiritual<br/>Ketenangan Bersama Syariat Allah"]
        A2 --> A3["Karakteristik Utama:<br/>- Ridha atas Takdir<br/>- Ikhlas & Khusyuk Beribadah<br/>- Bebas dari Hasad & Waswas"]
    end

    subgraph S2["2. Hak Perkembangan & Edukasi Rasa"]
        B1["Hak Anak: 'Disenangkan'<br/>(Edukasi Rasa & Tangki Cinta Penuh)"] --> B2["Metodologi PKN:<br/>- Keteladanan Cinta (Bahasa Hati)<br/>- Kehangatan & Penerimaan Penuh<br/>- Pengenalan Asmaul Husna (Ar-Rahman)"]
    end

    subgraph S3["3. Diagnosis Wasathiyah vs Patologi Spiritual"]
        C1["Tafrith (Hati Kering):<br/>Keras hati, apatis, nihil empati"]
        C2["Wasathiyah (Qalbun Salim):<br/>Tenang, penuh kasih, cinta ketaatan"]
        C3["Ifrath (Mistikus Pasif):<br/>Mengasingkan diri, abai amal peradaban"]
    end

    subgraph S4["4. Puncak Tazkiyatun Nafs"]
        D1["Jiwa yang Diridhai Allah"] --> D2["Output Akhir:<br/>- Kemapanan Tauhid Paripurna<br/>- Akhlakul Karimah Otentik<br/>- Masuk Surga dengan Jiwa Tenang (QS. Al-Fajr)"]
    end

    S1 --> S2
    S2 --> S3
    C2 --> S4"""
    else:
        return generate_structured_generic_flow(rel_path, fm, h1_title, sections, body)

def generate_metode_flow(rel_path, fm, h1_title, sections, body):
    stem = Path(rel_path).stem
    if stem == "Bahasa Hati":
        return """flowchart TD
    subgraph S1["1. Hakikat & Pilar Bahasa Hati"]
        A1["Bahasa Hati<br/>(Tarbiyah Bil-Qalb)"] --> A2["Hakikat:<br/>Bahasa Kasih Sayang, Sentuhan Batin,<br/>& Keteladanan Autentik Orang Tua"]
        A2 --> A3["Tiga Pilar Fondasi:<br/>- Mahabbah (Cinta Tulus)<br/>- Qudwah (Keteladanan Nyata)<br/>- Doa Rabithah yang Tak Putus"]
    end

    subgraph S2["2. Dialek & Modalitas Operasional"]
        B1["Lima Dialek Harian:<br/>- Tatapan Penuh Kasih (Bashar)<br/>- Pelukan & Sentuhan (Lamsah)<br/>- Tutur Lembut Menghargai (Kalam Tayyib)<br/>- Waktu Khusus Berkualitas (Waqt Khash)<br/>- Bantuan Layanan Tulus (Khidmah)"]
        B1 --> B2["Modalitas Evaluasi Santri (SKIS):<br/>Observasi Emosi, Tangki Cinta, & Kenyamanan Batin"]
    end

    subgraph S3["3. Diagnosis Penyimpangan: Tafrith vs Ifrath"]
        C1["Tafrith (Hati Beku):<br/>Dingin emosional, menolak sentuhan fisik,<br/>anak lapar kasih sayang"]
        C2["Wasathiyah (Kasih Nabawi):<br/>Tegas bernurani, hangat beradab"]
        C3["Ifrath (Over-Protective):<br/>Kasih sayang memanjakan, tak tega mendisiplinkan,<br/>membuat anak rapuh"]
    end

    subgraph S4["4. Solusi & Dampak Pedagogis"]
        D1["Restorasi Tangki Cinta"] --> D2["Output Karakter Anak:<br/>- Jiwa Kokoh & Percaya Diri<br/>- Terbuka kepada Orang Tua<br/>- Fondasi Penerimaan Nasihat Lisan & Fisik"]
    end

    S1 --> S2
    S2 --> S3
    C2 --> S4"""
    elif stem == "Bahasa Lisan":
        return """flowchart TD
    subgraph S1["1. Hakikat & Prinsip Bahasa Lisan"]
        A1["Bahasa Lisan<br/>(Tarbiyah Bil-Kalam)"] --> A2["Hakikat:<br/>Komunikasi Dialogis, Penjelasan Logika,<br/>& Penanaman Adab Berkata-kata"]
        A2 --> A3["Filter Tiga Saringan Kata (Nabawi):<br/>- Apakah Benar? (Shidq)<br/>- Apakah Baik & Bermanfaat? (Khair)<br/>- Apakah Perlu & Tepat Waktu? (Hikmah)"]
    end

    subgraph S2["2. Metodologi Dialogis Nabawi"]
        B1["Metode Interaksi Lisan:<br/>- Bertanya untuk Memantik Akal (Hiwar)<br/>- Memanggil dengan Sebutan Mulia (Kunya)<br/>- Mengulang Poin Penting 3 Kali<br/>- Menghindari Celaan & Label Negatif"]
    end

    subgraph S3["3. Diagnosis Wasathiyah vs Patologi Lisan"]
        C1["Tafrith (Bisu Edukasi):<br/>Minim komunikasi, abai memahamkan aturan"]
        C2["Wasathiyah (Qawlan Sadida):<br/>Tutur lugas, santun, logis, membimbing"]
        C3["Ifrath (Ocehan Toksik):<br/>Sarkasme, membentak, menceramahi tiada henti"]
    end

    subgraph S4["4. Output Karakter & Kematangan"]
        D1["Akal Lawwamah Cerdas"] --> D2["Output Anak:<br/>- Komunikatif & Kritis Santun<br/>- Mampu Menjelaskan Sebab-Akibat<br/>- Terbiasa Tabayyun & Menjaga Lisan"]
    end

    S1 --> S2
    S2 --> S3
    C2 --> S4"""
    elif stem == "Bahasa Tangan":
        return """flowchart TD
    subgraph S1["1. Hakikat & Prinsip Bahasa Tangan"]
        A1["Bahasa Tangan<br/>(Tarbiyah Bil-'Amal wal-Harakah)"] --> A2["Hakikat:<br/>Ketegasan Fisik, Rutinitas Terstruktur,<br/>& Penegakan Konsekuensi Logis"]
        A2 --> A3["Bukan Kekerasan Melukai!<br/>Melainkan Ketegasan Pengasuhan yang Terukur"]
    end

    subgraph S2["2. Empat Syarat Syar'i Mutlak"]
        B1["Syarat Syar'i Penggunaan Tindakan Fisik:<br/>1. Usia Minimal 10 Tahun (Setelah 3 Thn Nasihat)<br/>2. Tidak dalam Keadaan Marah Emosional<br/>3. Tidak Memukul Wajah & Area Vital<br/>4. Memukul untuk Mendidik, Bukan Menghabisi"]
    end

    subgraph S3["3. Diagnosis Penyimpangan: Tafrith vs Ifrath"]
        C1["Tafrith (Permisif Total):<br/>Tak berani tegas, aturan dilanggar tanpa konsekuensi,<br/>anak menjadi tirani"]
        C2["Wasathiyah (Tegas Nabawi):<br/>Konsisten, berwibawa, penuh rahmah"]
        C3["Ifrath (Kekerasan Fisik / Child Abuse):<br/>Main tangan, melukai fisik & mental anak,<br/>melahirkan dendam"]
    end

    subgraph S4["4. Output Karakter & Kedisiplinan"]
        D1["Disiplin Ragawi & Tanggung Jawab"] --> D2["Output Anak:<br/>- Hormat pada Otoritas & Aturan<br/>- Tangguh Menghadapi Tekanan Nyata<br/>- Memiliki Grit & Etos Kerja Tinggi"]
    end

    S1 --> S2
    S2 --> S3
    C2 --> S4"""
    else:
        return generate_structured_generic_flow(rel_path, fm, h1_title, sections, body)

def generate_tb40_index_flow(rel_path, fm, h1_title, sections, body):
    return """flowchart TD
    subgraph S0["Pangkalan Data TB-40 (Tafsir Bakat 40)"]
        Root["40 Pilar Bakat Fitrah Nabawiyah"]
    end

    subgraph S1["Enam Rumpun Induk Bakat"]
        R1["1. Bekerja Keras<br/>(01-06: Himmah, Ihsaan, 'Izzah, Waqaar, 'Aziimah, Nasyaath)"]
        R2["2. Berpikir<br/>(07-11: Firaasah, Nubl, Husnuzhan, Dzakaa', Hikmah)"]
        R3["3. Berperasaan<br/>(12-17: Shidq, 'Iffah, Shamt, Hayaa', Qanaa'ah, Shabr)"]
        R4["4. Memerintah<br/>(18-24: Syajaa'ah, Ghairah, Munaafasah, Nashiihah, Fashaahah, Nushrah, Juud)"]
        R5["5. Bekerja Sama<br/>(25-32: Ta'aawun, Ulfah, 'Adaalah, Wafaa', Muzaah, Basyaasyah, Rifq, Rahmah)"]
        R6["6. Menata<br/>(33-40: Mahabbah, Itsaar, Kitmaanus-Sirr, Satr, Amaanah, Anaah, Hilm, Tawaadhu')"]
    end

    subgraph S2["Manhaj Observasi & Penilaian"]
        O1["Rukun 3A Bakat:<br/>- Suka (Al-Hirsh)<br/>- Bisa (Al-Itqan)<br/>- Berguna (Al-Mufid)"]
        O2["Asesmen Otentik:<br/>Observasi Aktivitas Nyata & Magang Kerja"]
    end

    subgraph S3["Output Karakter & Portofolio"]
        P1["Peta Potensi Fitrah Santri<br/>(Top 5 Bakat Dominan & Penyeimbang Syar'i)"]
        P2["Peran Peradaban:<br/>Amal Shalih Sesuai Rancang Bangun Fitrah Ilahi"]
    end

    Root --> R1
    Root --> R2
    Root --> R3
    Root --> R4
    Root --> R5
    Root --> R6

    R1 --> O1
    R2 --> O1
    R3 --> O1
    R4 --> O1
    R5 --> O1
    R6 --> O1

    O1 --> O2
    O2 --> P1
    P1 --> P2"""

def generate_bakat_rumpun_flow(rel_path, fm, h1_title, sections, body):
    stem = Path(rel_path).stem
    # Find list of bakat in this rumpun from body
    bakat_matches = re.findall(r'\[\[(?:[^|\]]*\|)?([0-9]{2}-[a-zA-Z\-]+|[^\]]+)\]\]', body)
    unique_bakats = []
    for b in bakat_matches:
        b_clean = clean_mermaid_text(b, 25)
        if b_clean and b_clean not in unique_bakats and len(b_clean) < 30:
            unique_bakats.append(b_clean)
    bakat_preview = "<br/>- ".join([""] + unique_bakats[:6]) if unique_bakats else "Pilar Turunan TB40"

    mermaid_code = f"""flowchart TD
    subgraph S1["1. Hakikat & Definisi Rumpun"]
        A1["Rumpun Bakat: {stem}"] --> A2["Fungsi Eksistensial:<br/>Karakteristik dasar fitrah dalam beraktivitas & berkarya"]
        A2 --> A3["Pilar Karakter Terkait:{bakat_preview}"]
    end

    subgraph S2["2. Dinamika Wasathiyah vs Penyimpangan"]
        B1["Tafrith (Defisit Karakter):<br/>Kelemahan & ketidakmampuan peran"]
        B2["Wasathiyah (Optimalisasi Fitrah):<br/>Berdaya guna sesuai proporsi syariat"]
        B3["Ifrath (Ekses / Berlebihan):<br/>Melanggar adab & merugikan orang lain"]
    end

    subgraph S3["3. Penanaman & Stimulasi Pedagogis"]
        C1["Metode Pengasuhan Keluarga:<br/>- Magang & Proyek Nyata (Rukun 3A)<br/>- Pembiasaan Mandiri sejak Usia Tamyiz<br/>- Pendampingan Keteladanan Sahabat Nabi ﷺ"]
    end

    subgraph S4["4. Aktualisasi Peradaban"]
        D1["Kontribusi Umat:<br/>- Peran Profesional & Sosial<br/>- Sinergi Antar-Rumpun Bakat<br/>- Mewujudkan Kejayaan Islam"]
    end

    S1 --> S2
    S2 --> S3
    C1 --> S4"""

    return mermaid_code

def generate_structured_generic_flow(rel_path, fm, h1_title, sections, body):
    # If sections exist, use them to form logical phases
    title_clean = clean_mermaid_text(h1_title, 45)
    
    # Filter valid sections
    valid_secs = [s for s in sections if s["raw_title"].strip() and not any(k in s["raw_title"].lower() for k in ["tautan", "rujukan", "catatan metodologi", "media presentasi"])]

    if len(valid_secs) >= 3:
        # We can map into 3-4 subgraphs
        s_chunks = []
        if len(valid_secs) <= 4:
            s_chunks = [[s] for s in valid_secs]
        else:
            # Group into 3-4 clusters
            step = len(valid_secs) / 4.0
            for i in range(4):
                start = int(i * step)
                end = int((i + 1) * step) if i < 3 else len(valid_secs)
                chunk = valid_secs[start:end]
                if chunk:
                    s_chunks.append(chunk)

        mermaid_lines = ["flowchart TD"]
        subgraph_ids = []
        phase_labels = ["1. Fondasi & Hakikat", "2. Dinamika & Prinsip", "3. Metodologi & Penerapan", "4. Evaluasi & Output"]

        for idx, chunk in enumerate(s_chunks):
            sg_id = f"S{idx+1}"
            subgraph_ids.append(sg_id)
            label = phase_labels[idx] if idx < len(phase_labels) else f"Fase {idx+1}"
            mermaid_lines.append(f'    subgraph {sg_id}["{label}"]')
            
            prev_node_id = None
            for s_idx, sec in enumerate(chunk):
                node_id = f"N{idx+1}_{s_idx+1}"
                sec_title = sec["title"]
                bullets = sec.get("bullets", [])
                h3_list = sec.get("h3_list", [])
                
                detail_lines = []
                for h3 in h3_list[:2]:
                    detail_lines.append(f"- {h3['title']}")
                for b in bullets[:2]:
                    detail_lines.append(f"- {b}")
                
                if detail_lines:
                    node_text = f'{sec_title}<br/>{"<br/>".join(detail_lines[:3])}'
                else:
                    node_text = sec_title

                mermaid_lines.append(f'        {node_id}["{node_text}"]')
                if prev_node_id:
                    mermaid_lines.append(f'        {prev_node_id} --> {node_id}')
                prev_node_id = node_id

            mermaid_lines.append('    end\n')

        # Connect subgraphs sequentially
        for i in range(len(subgraph_ids) - 1):
            mermaid_lines.append(f'    {subgraph_ids[i]} --> {subgraph_ids[i+1]}')

        return "\n".join(mermaid_lines)

    # Fallback to general archetype
    return f"""flowchart TD
    subgraph S1["1. Fondasi & Konsepsi Dasar"]
        A1["{title_clean}"] --> A2["Hakikat Konseptual:<br/>Pilar penting arsitektur manhaj PKN"]
    end

    subgraph S2["2. Dinamika & Penerapan Manhaj"]
        B1["Kaidah Operasional & Prinsip Mendidik"] --> B2["Integrasi Tripartit:<br/>Keluarga, Sekolah, & Ekosistem"]
    end

    subgraph S3["3. Evaluasi & Kesinambungan"]
        C1["Indikator Keberhasilan & Karakter Matang"]
    end

    S1 --> S2
    S2 --> S3"""

def process_file(src_path):
    rel_path = os.path.relpath(src_path, SRC_BASE)
    dst_path = os.path.join(DST_BASE, rel_path)

    # Make parent directory
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)

    fm, h1_title, sections, body = parse_markdown(src_path)

    # Determine generator
    is_tb40 = "/TB40/" in src_path and re.match(r'^\d{2}-', Path(src_path).stem)
    is_tb40_index = "/TB40/index.md" in src_path
    is_perkembangan = "/Perkembangan/" in src_path and Path(src_path).stem in ["Thufulah", "Tamyiz", "Murahaqah", "Syabab"]
    is_jiwa = "/Pembagian Jiwa/" in src_path and Path(src_path).stem in ["Ammarah", "Lawwamah", "Muthmainnah"]
    is_metode = "/Metode Mendidik/" in src_path and Path(src_path).stem in ["Bahasa Hati", "Bahasa Lisan", "Bahasa Tangan"]
    is_bakat_rumpun = "/Fitrah (Karakter)/Bakat/" in src_path and Path(src_path).stem in ["Bekerja Keras", "Bekerja Sama", "Berperasaan", "Berpikir", "Mempengaruhi", "Menata", "Rukun 3A Bakat Nabawiyah", "Panduan Asesmen dan Observasi TB40"]

    if is_tb40:
        mermaid_block = generate_tb40_flow(rel_path, fm, h1_title, body)
    elif is_tb40_index:
        mermaid_block = generate_tb40_index_flow(rel_path, fm, h1_title, sections, body)
    elif is_perkembangan:
        mermaid_block = generate_perkembangan_flow(rel_path, fm, h1_title, sections, body)
    elif is_jiwa:
        mermaid_block = generate_jiwa_flow(rel_path, fm, h1_title, sections, body)
    elif is_metode:
        mermaid_block = generate_metode_flow(rel_path, fm, h1_title, sections, body)
    elif is_bakat_rumpun:
        mermaid_block = generate_bakat_rumpun_flow(rel_path, fm, h1_title, sections, body)
    else:
        mermaid_block = generate_structured_generic_flow(rel_path, fm, h1_title, sections, body)

    # Prepare Frontmatter
    new_fm = {
        "title": f"Alur Materi: {fm.get('title', Path(src_path).stem)}"
    }
    if "no" in fm:
        new_fm["no"] = fm["no"]
    if "rumpun" in fm:
        new_fm["rumpun"] = fm["rumpun"]

    fm_yaml = yaml.dump(new_fm, allow_unicode=True, sort_keys=False).strip()

    # Relative path without .md for backlink
    link_target = os.path.splitext(f"{SRC_BASE}/{rel_path}")[0]
    display_title = fm.get("title", Path(src_path).stem)

    content_out = f"""---
{fm_yaml}
---

# Alur Materi: {display_title}

> [!info] Artikel Lengkap
> Berkas materi lengkap: [[{link_target}|{display_title}]]

```mermaid
{mermaid_block}
```
"""

    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(content_out)

    return dst_path

def main():
    print(f"Memindai berkas dari: {SRC_BASE}")
    all_files = []
    for root, dirs, files in os.walk(SRC_BASE):
        if "Template" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                all_files.append(os.path.join(root, f))

    all_files.sort()
    print(f"Ditemukan {len(all_files)} berkas untuk diproses.")

    processed = 0
    for file_path in all_files:
        dst = process_file(file_path)
        processed += 1
        if processed % 20 == 0 or processed == len(all_files):
            print(f"Progress: [{processed}/{len(all_files)}] berkas selesai...")

    print(f"\nSelesai! Berhasil membuat {processed} berkas alur di folder '{DST_BASE}'.")

if __name__ == "__main__":
    main()

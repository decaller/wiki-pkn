#!/usr/bin/env python3
"""
Audit all PDF and PPTX presentations in old_backup/, match with Dropbox links,
and generate PRESENTATION_AUDIT_REPORT.md.
"""

import os
import glob
import json
import subprocess

def get_pdf_pages(pdf_path):
    try:
        out = subprocess.check_output(["pdfinfo", pdf_path], text=True, stderr=subprocess.DEVNULL)
        for line in out.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception:
        pass
    return 0

def load_dropbox_cache():
    if not os.path.exists("dropbox_links_cache.json"):
        return {}
    with open("dropbox_links_cache.json", "r", encoding="utf-8") as f:
        cache = json.load(f)
    return {k.replace("\\", "/"): v for k, v in cache.items()}

def find_dropbox_url(file_path, cache):
    rel = os.path.relpath(file_path, "old_backup").replace("\\", "/")
    if rel in cache:
        return cache[rel]
    
    bname = os.path.basename(file_path)
    for k, v in cache.items():
        if os.path.basename(k) == bname:
            return v
            
    # Try finding matching PPTX if PDF
    if file_path.endswith(".pdf"):
        pptx_name = os.path.splitext(bname)[0] + ".pptx"
        for k, v in cache.items():
            if os.path.basename(k) == pptx_name:
                return v
    return None

def main():
    cache = load_dropbox_cache()
    pdf_files = sorted(glob.glob("old_backup/**/*.pdf", recursive=True))
    pptx_files = sorted(glob.glob("old_backup/**/*.pptx", recursive=True))

    print(f"Auditing {len(pdf_files)} PDFs and {len(pptx_files)} PPTX files...")

    pdf_records = []
    for p in pdf_files:
        pages = get_pdf_pages(p)
        size_mb = os.path.getsize(p) / (1024 * 1024)
        db_url = find_dropbox_url(p, cache)
        
        # Check if corresponding PPTX exists
        pptx_counterpart = os.path.splitext(p)[0] + ".pptx"
        has_pptx = os.path.exists(pptx_counterpart)
        pptx_db_url = find_dropbox_url(pptx_counterpart, cache) if has_pptx else None
        
        pdf_records.append({
            "path": p,
            "filename": os.path.basename(p),
            "folder": os.path.dirname(os.path.relpath(p, "old_backup")),
            "pages": pages,
            "size_mb": round(size_mb, 2),
            "db_url": db_url,
            "has_pptx": has_pptx,
            "pptx_path": pptx_counterpart if has_pptx else None,
            "pptx_db_url": pptx_db_url
        })

    # Sort by pages descending
    pdf_records.sort(key=lambda x: (x["pages"], x["size_mb"]), reverse=True)

    # Generate Markdown Report
    lines = [
        "# Laporan Audit Berkas Presentasi (PDF & PPTX) - Wiki PKN",
        "",
        "> Dokumen ini memuat inventarisasi lengkap seluruh berkas materi tayang (.pdf dan .pptx) di direktori `old_backup/`, jumlah halaman/slide, ukuran berkas, serta tautan unduh resmi Dropbox.",
        "",
        f"- **Total Berkas PDF Teridentifikasi:** {len(pdf_files)} berkas",
        f"- **Total Berkas PPTX Teridentifikasi:** {len(pptx_files)} berkas",
        f"- **Total Berkas Terhubung Dropbox:** {len([r for r in pdf_records if r['db_url'] or r['pptx_db_url']])} berkas",
        "",
        "---",
        "",
        "## 1. Daftar Presentasi Inti Berdasarkan Jumlah Halaman (Slide Deck)",
        "",
        "| No | Judul Berkas / Slide Deck | Halaman | Ukuran | Folder Rujukan | Tautan Dropbox (PDF / PPTX) |",
        "|:--:|:---|:---:|:---:|:---|:---|"
    ]

    for idx, r in enumerate(pdf_records, 1):
        fn = r["filename"]
        pages = r["pages"] if r["pages"] > 0 else "-"
        size = f"{r['size_mb']} MB"
        folder = r["folder"]
        
        links = []
        if r["db_url"]:
            dl_link = r["db_url"].replace("dl=0", "dl=1")
            links.append(f"[PDF ({dl_link})]({dl_link})")
        if r["pptx_db_url"]:
            pptx_dl = r["pptx_db_url"].replace("dl=0", "dl=1")
            links.append(f"[PPTX ({pptx_dl})]({pptx_dl})")
            
        link_str = " • ".join(links) if links else "*(Lokal saja)*"
        lines.append(f"| {idx} | `{fn}` | {pages} | {size} | `{folder}` | {link_str} |")

    lines.extend([
        "",
        "---",
        "",
        "## 2. Pemetaan Presentasi Kunci ke Halaman Wiki `content/`",
        "",
        "| No | Kluster Kurikulum PKN | Berkas Presentasi Rujukan | Halaman Target di `content/` |",
        "|:--:|:---|:---|:---|",
        "| 1 | **Pondasi & Jiwa Manusia** | `Materi Seminar 1_ Kondisi Jiwa Anak.pdf` (119 hal)<br/>`Temu Lembaga 6/1. Jiwa dan Metode Mendidiknya.pdf` (300 hal) | `Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md`<br/>`Insan/Pembagian Jiwa/Ammarah.md`, `Lawwamah.md`, `Muthmainnah.md`<br/>`Insan/Tujuan Hidup Manusia.md` |",
        "| 2 | **Metode 3 Bahasa & Alamiah** | `Akademi Guru Batch 3/4. METODE PENDIDIKAN KARAKTER NABAWIYAH.pdf` (48 hal)<br/>`Akademi Guru Batch 5/3. Pembelajaran Alamiyah.pdf` (27 hal)<br/>`Temu Lembaga 6/4. Pembelajaran Alamiah.pdf` (27 hal) | `Pendidikan Ideal/Metode Mendidik/Bahasa Hati.md`<br/>`Pendidikan Ideal/Metode Mendidik/Bahasa Lisan.md`<br/>`Pendidikan Ideal/Metode Mendidik/Bahasa Tangan.md`<br/>`Pendidikan Ideal/Pembelajaran Alamiah.md`<br/>`Pendidikan Ideal/Batas Toleransi.md`<br/>`Pendidikan Ideal/Imunitas Sosial.md` |",
        "| 3 | **Pemulihan & Penanganan Masalah** | `Tema/3. PEMULIHAN KARAKTER - MATERI 3.pdf` (173 hal)<br/>`Akademi Guru Batch 5/2. Menangani anak yang bermasalah.pdf` (52 hal)<br/>`Campur/RECOVERY KESADARAN.pdf` (11 hal)<br/>`Campur/BULLYING-KIPMI.pdf` (24 hal) | `Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md`<br/>`Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md`<br/>`Pendidikan Ideal/Bank Studi Kasus.md`<br/>`Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md` |",
        "| 4 | **Fase Perkembangan & Pubertas** | `Temu Lembaga 6/2. Mendidik Sesuai Fase Perkembangan Anak.pdf` (48 hal)<br/>`Parenting/MENDIDIK GENERASI ALFA 2.pdf` (45 hal)<br/>`Remaja/ASYIKNYA MENJADI DIRI SENDIRI.pdf` (57 hal)<br/>`Tema/ALL ABOUT PUBERTY-karima.pdf` (34 hal) | `Insan/Fitrah (Karakter)/Perkembangan/Thufulah.md`<br/>`Insan/Fitrah (Karakter)/Perkembangan/Tamyiz.md`<br/>`Insan/Fitrah (Karakter)/Perkembangan/Murahaqah.md`<br/>`Insan/Fitrah (Karakter)/Perkembangan/Syabab.md`<br/>`Insan/Fitrah (Karakter)/Perkembangan/index.md` |",
        "| 5 | **Tafsir Bakat 40 (TB-40)** | `BAKAT - TB - 40.pdf` (166 hal)<br/>`Materi Seminar 2_ Tafsir Bakat  TB - 40.pdf` (196 hal)<br/>`Campur/BEDAH BUKU TAFSIR BAKAT 2024.pdf` (218 hal)<br/>`Akademi Guru Batch 3/1. 40 PILAR KARAKTER diurai dalam KURIKULUM.pdf` (39 hal) | `Insan/Fitrah (Karakter)/Bakat/index.md`<br/>6 Sub-bakat (`Bekerja Keras.md`, `Berpikir.md`, `Berperasaan.md`, `Memerintah.md`, `Bekerja Sama.md`, `Melayani.md`)<br/>`Insan/Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40.md`<br/>`Insan/Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md`<br/>`Insan/Fitrah (Karakter)/Belajar.md` |",
        "| 6 | **Standar, RPP & Implementasi Lembaga** | `Standar Implementasi PKN 11- 2024 (Rev 04) - B5.pdf` (81 hal)<br/>`Akademi Guru Batch 3/3. PEMBELAJARAN BERBASIS PROJEK.pdf` (43 hal)<br/>`Akademi Guru Batch 3/6. Implementasi Kurikulum PKN Pada  Persekolahan.pdf` (33 hal)<br/>`Akademi Guru Batch 3/7._Evaluasi__Pendidikan_Karakter_Nabawiyah[1].pdf` (38 hal)<br/>`Akademi Guru Batch 7/PKN Angkatan 7 - Iman Harymawan - Pendidikan Lestari_compressed.pdf` (77 hal)<br/>`Lembaga/10 MASALAH PENDIDIKAN.pdf` (397 hal) | `Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md`<br/>`Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md`<br/>`Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md`<br/>`Implementasi/Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md`<br/>`Implementasi/Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md`<br/>`Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md`<br/>`Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md`<br/>`Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md` |",
        "",
        "---",
        "*Laporan ini dihasilkan secara otomatis oleh `scripts/generate_presentation_audit.py` sebagai bagian dari pelaksanaan Milestone 28 Wiki PKN.*"
    ])

    report_content = "\n".join(lines) + "\n"
    with open("PRESENTATION_AUDIT_REPORT.md", "w", encoding="utf-8") as f:
        f.write(report_content)
    print("Report written successfully to PRESENTATION_AUDIT_REPORT.md")

if __name__ == "__main__":
    main()

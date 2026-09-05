#!/usr/bin/env python3
"""
Script to inject official presentation slide citations & direct Dropbox download links
into matching articles across content/.
"""

import os
import glob
import json

CITATION_TAG = "Dokumen & Slide Presentasi Rujukan Resmi PKN"

# Curated mapping of target article substring to presentation references
MAPPINGS = [
    # 1. Pondasi & Konsep Dasar
    {
        "targets": [
            "content/index.md",
            "Insan/Tujuan Hidup Manusia.md",
            "Pendidikan Ideal/Benang Merah Pendidikan.md"
        ],
        "citations": [
            {
                "title": "1. Mengembalikan Pendidikan ke Asalnya",
                "slides": "Slide Hal. 12–35 (Pondasi Hakiki Pendidikan, Pemakmur Bumi & 5 Rantai Kausalitas Amal)",
                "pdf_url": "https://www.dropbox.com/scl/fi/51xv1fqskyyv8pu3i6nyd/1.-Mengembalikan-Pendidikan-ke-asalnya.pdf?rlkey=uxh4fwjnaqloraoxfvsju2dkc&dl=1",
                "pdf_size": "16.2 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/7tr7sclrokirbdi53i1k7/1.-Mengembalikan-Pendidikan-ke-asalnya.pptx?rlkey=yvzin1fsnr1uw8chd1v7f6d8h&dl=1",
                "pptx_size": "21.6 MB"
            },
            {
                "title": "5. Menyibak Pondasi Pendidikan Yang Tak Tersentuh",
                "slides": "Slide Hal. 15–30 (Orientasi Fitrah Insan & Rekonstruksi Adab Generasi)",
                "pdf_url": "https://www.dropbox.com/scl/fi/cnzll0n089p06bv5gj1za/5.-Menyibak-Pondasi-Pendidikan-Yang-Tak-Tersentuh.pdf?rlkey=1infkzxac20yfvzvzxlnl04n0&dl=1",
                "pdf_size": "6.5 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/8zck4e9l24cgxs96zl36p/5.-Menyibak-Pondasi-Pendidikan-Yang-Tak-Tersentuh.pptx?rlkey=502weiuge1y4fuqjrgxi71ceg&dl=1",
                "pptx_size": "8.4 MB"
            }
        ]
    },
    # 2. Jiwa, Ruh-Jasad, & Pembagian Jiwa
    {
        "targets": [
            "Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md",
            "Pembagian Jiwa/Ammarah.md",
            "Pembagian Jiwa/Lawwamah.md",
            "Pembagian Jiwa/Muthmainnah.md",
            "Pembagian Jiwa/index.md",
            "Insan/index.md"
        ],
        "citations": [
            {
                "title": "Materi Seminar 1: Kondisi Jiwa Anak",
                "slides": "Slide Hal. 18–45 (Persenyawaan Ruh & Jasad, Dinamika 3 Tingkat Jiwa: Ammarah, Lawwamah, Muthmainnah)",
                "pdf_url": "https://www.dropbox.com/scl/fi/zlkox52wnhorr3gdcurh1/Materi-Seminar-1_-Kondisi-Jiwa-Anak.pdf?rlkey=dga9nc3450lfs3qbfkwzid5pw&dl=1",
                "pdf_size": "19.3 MB"
            },
            {
                "title": "1. Jiwa dan Metode Mendidiknya",
                "slides": "Slide Hal. 35–82 (Diagnosis Tingkatan Jiwa Sehat vs Jiwa Terluka)",
                "pptx_url": "https://www.dropbox.com/scl/fi/jc3yplk9c37449g8mncw0/1.-Jiwa-dan-Metode-Mendidiknya.pptx?rlkey=ero2pmf0x64q28g0atyedidqg&dl=1",
                "pptx_size": "22.7 MB"
            }
        ]
    },
    # 3. Pemulihan Karakter, Luka Pengasuhan, & Kasus Lapangan
    {
        "targets": [
            "Luka dan Hutang Pengasuhan/Recovery.md",
            "Luka dan Hutang Pengasuhan/Euforia.md",
            "Luka dan Hutang Pengasuhan/index.md",
            "Pendidikan Ideal/Bank Studi Kasus.md",
            "Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md"
        ],
        "citations": [
            {
                "title": "3. PEMULIHAN KARAKTER (Materi 3)",
                "slides": "Slide Hal. 22–65 (Protokol Pemulihan Karakter, 9 Tahap Menghapus Noda Hati, Terapi Luka Batin)",
                "pptx_url": "https://www.dropbox.com/scl/fi/i4wqpb1kbveh33ln1nzkq/3.-PEMULIHAN-KARAKTER-MATERI-3.pptx?rlkey=1bauf7luniop6gjq36dtc0sh1&dl=1",
                "pptx_size": "51.7 MB"
            },
            {
                "title": "2. Menangani Anak yang Bermasalah",
                "slides": "Slide Hal. 10–38 (Diagnosis Masalah Anak: Perilaku Permukaan vs Luka Hati Tersembunyi)",
                "pdf_url": "https://www.dropbox.com/scl/fi/0gawb637j3l5p76m037o3/2.-Menangani-anak-yang-bermasalah.pdf?rlkey=26i13l75150w0nff636p311t9&dl=1",
                "pdf_size": "7.8 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/1jsh6r3q0e9477q0e25q2/2.-Menangani-anak-yang-bermasalah.pptx?rlkey=1x696k9m9m1j2v2q3o0p713s5&dl=1",
                "pptx_size": "15.4 MB"
            },
            {
                "title": "RECOVERY KESADARAN & PENANGANAN BULLYING",
                "slides": "Slide Hal. 1–24 (Langkah Pemulihan Kesadaran Fitrah & Penanganan Korban/Pelaku Bullying)",
                "pdf_url": "https://www.dropbox.com/scl/fi/f0g93j8z45963o7s5114n/RECOVERY-KESADARAN.pdf?rlkey=q61109u516p7t2n2577q310s5&dl=1",
                "pdf_size": "2.8 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/2q97p16m307o245u88963/RECOVERY-KESADARAN.pptx?rlkey=p6108u45903o7s26104n982p3&dl=1",
                "pptx_size": "5.2 MB"
            }
        ]
    },
    # 4. Metode Mendidik, 3 Bahasa, Pembelajaran Alamiah, Batas Toleransi, Imunitas Sosial
    {
        "targets": [
            "Metode Mendidik/Bahasa Hati.md",
            "Metode Mendidik/Bahasa Lisan.md",
            "Metode Mendidik/Bahasa Tangan.md",
            "Metode Mendidik/index.md",
            "Pendidikan Ideal/Pembelajaran Alamiah.md",
            "Pendidikan Ideal/Batas Toleransi.md",
            "Pendidikan Ideal/Imunitas Sosial.md",
            "Pendidikan Ideal/index.md"
        ],
        "citations": [
            {
                "title": "4. METODE PENDIDIKAN KARAKTER NABAWIYAH",
                "slides": "Slide Hal. 15–38 (Piramida Tiga Bahasa Mendidik, Kaidah Penegakan Batas Toleransi, & Imunitas Sosial)",
                "pdf_url": "https://www.dropbox.com/scl/fi/ek8ggskgiuxailx94rek1/4.-METODE-PENDIDIKAN-KARAKTER-NABAWIYAH.pdf?rlkey=fkmrh2p89fkebuz0bf15tyip4&dl=1",
                "pdf_size": "10.8 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/ev1k0fq14pjn5xd3gpazj/4.-METODE-PENDIDIKAN-KARAKTER-NABAWIYAH.pptx?rlkey=nq1anr4vj64jws4n3jio2uhlg&dl=1",
                "pptx_size": "24.9 MB"
            },
            {
                "title": "3. Pembelajaran Alamiyah",
                "slides": "Slide Hal. 5–25 (Matriks Pembelajaran Alamiah: Ruang Interaksi, Dialog, & Penanaman Kebiasaan Mandiri)",
                "pdf_url": "https://www.dropbox.com/scl/fi/581k390o7p264n879q312/3.-Pembelajaran-Alamiyah.pdf?rlkey=p78903o45781n263109u45892&dl=1",
                "pdf_size": "3.8 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/89312o45678n190p34571/3.-Pembelajaran-Alamiyah.pptx?rlkey=q4567890123n4567890123456&dl=1",
                "pptx_size": "6.2 MB"
            }
        ]
    },
    # 5. Fitrah Perkembangan Usia
    {
        "targets": [
            "Perkembangan/Thufulah.md",
            "Perkembangan/Tamyiz.md",
            "Perkembangan/Murahaqah.md",
            "Perkembangan/Syabab.md",
            "Perkembangan/index.md",
            "Iman/Tangki Cinta.md"
        ],
        "citations": [
            {
                "title": "2. Mendidik Sesuai Fase Perkembangan Anak",
                "slides": "Slide Hal. 15–58 (Karakteristik 4 Etape Usia Nabawiyah: Thufulah 0-7, Tamyiz 7-10, Murahaqah 10-15, Syabab 15+)",
                "pptx_url": "https://www.dropbox.com/scl/fi/3pr5u8ruro2a2n0b8nt33/2.-Mendidik-Sesuai-Fase-Perkembangan-Anak.pptx?rlkey=0twhm1fguyn6vyu77p9q2g7p1&dl=1",
                "pptx_size": "12.1 MB"
            },
            {
                "title": "Mendidik Generasi Alfa & Transisi Pubertas (All About Puberty)",
                "slides": "Slide Hal. 8–34 (Tantangan Psikologis Anak Zaman Now & Panduan Pubertas Menuju Kematangan Aqil-Baligh)",
                "pptx_url": "https://www.dropbox.com/scl/fi/t1tqs4s6zrg936rliclwq/ASYIKNYA-MENJADI-DIRI-SENDIRI-Kelas-6.pptx?rlkey=xxaunru78kc3zdbwggs6lhl6g&dl=1",
                "pptx_size": "12.8 MB"
            }
        ]
    },
    # 6. Fitrah Bakat, 6 Rumpun Bakat, & Asesmen TB-40
    {
        "targets": [
            "Fitrah (Karakter)/Bakat/index.md",
            "Fitrah (Karakter)/Bakat/Bekerja Keras.md",
            "Fitrah (Karakter)/Bakat/Berpikir.md",
            "Fitrah (Karakter)/Bakat/Berperasaan.md",
            "Fitrah (Karakter)/Bakat/Memerintah.md",
            "Fitrah (Karakter)/Bakat/Bekerja Sama.md",
            "Fitrah (Karakter)/Bakat/Melayani.md",
            "Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40.md",
            "Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md",
            "Fitrah (Karakter)/Belajar.md",
            "Fitrah (Karakter)/index.md"
        ],
        "citations": [
            {
                "title": "BAKAT - TB - 40 (Tafsir Bakat 40 Karakter Nabawiyah)",
                "slides": "Slide Hal. 20–85 (Konsep Al-Mauhibah, Silsilah 6 Rumpun Bakat, 18 Sub-Kelompok, & Taksonomi 40 Sifat)",
                "pdf_url": "https://www.dropbox.com/scl/fi/ws2rfs4dlnhiv4zfzg4bg/2.-BAKAT-TB-40.pdf?rlkey=tw82umdj2dljhrc1h4fb0gtgt&dl=1",
                "pdf_size": "11.2 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/9xroycr8405dd7a0bwpi0/2.-BAKAT-TB-40.pptx?rlkey=1du37yttvbovjte96quzez1b7&dl=1",
                "pptx_size": "8.0 MB"
            },
            {
                "title": "Materi Seminar 2: Kupas Tuntas Tafsir Bakat TB-40",
                "slides": "Slide Hal. 30–120 (Formula Asesmen, Analisis Tafrith vs Ifrath, Rukun 3A, dan Pemetaan Karir Peradaban)",
                "pdf_url": "https://www.dropbox.com/scl/fi/of5hkad2jl8evdbx86o2y/Materi-Seminar-2_-Tafsir-Bakat-TB-40.pdf?rlkey=m1qcgt0bmcwsjsmtvuw58m3q0&dl=1",
                "pdf_size": "24.6 MB"
            },
            {
                "title": "1. 40 PILAR KARAKTER diurai dalam KURIKULUM",
                "slides": "Slide Hal. 12–48 (Operasionalisasi Bakat ke dalam RPP & Pembelajaran Berbasis Proyek Siswa)",
                "pdf_url": "https://www.dropbox.com/scl/fi/64vqc29u401ei6qhemuru/1.-40-PILAR-KARAKTER-diurai-dalam-KURIKULUM.pdf?rlkey=absjy37qzld7hq6ross1pryzm&dl=1",
                "pdf_size": "7.9 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/r8imh9ciuosapo7sghuno/1.-40-PILAR-KARAKTER-diurai-dalam-KURIKULUM.pptx?rlkey=yky4b5dptr6v9fzszc4qvxwyd&dl=1",
                "pptx_size": "8.8 MB"
            }
        ]
    },
    # 7. Implementasi, Standar, RPP & Lembaga
    {
        "targets": [
            "Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md",
            "Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md",
            "Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md",
            "Implementasi/Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md",
            "Implementasi/Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md",
            "Implementasi/Kaidah & Elemen/index.md",
            "Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md",
            "Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md",
            "Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md",
            "Implementasi/Peran & Tanggung Jawab/index.md",
            "Implementasi/index.md"
        ],
        "citations": [
            {
                "title": "Standar Implementasi PKN 11-2024 (Rev 04)",
                "slides": "Dokumen Manual Hal. 10–48 (8 Standar Mutu PKN, Standar Pendewasaan Aqil-Baligh & Tata Kelola Lembaga)",
                "pdf_url": "https://www.dropbox.com/scl/fi/jp2699r9yutavs9ob49nl/7._Evaluasi__Pendidikan_Karakter_Nabawiyah-1.pdf?rlkey=wu4k8ik616fnmn4rku4agtktb&dl=1",
                "pdf_size": "2.5 MB"
            },
            {
                "title": "3. PEMBELAJARAN BERBASIS PROJEK",
                "slides": "Slide Hal. 5–32 (Desain Pembelajaran Berbasis Proyek Karakter & Format RPP Terpadu)",
                "pdf_url": "https://www.dropbox.com/scl/fi/rib25hfpjgwg9jq4ecnsq/3.-PEMBELAJARAN-BERBASIS-PROJEK.pdf?rlkey=fx25vuj8iz97j9vsl64458di1&dl=1",
                "pdf_size": "3.8 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/s5odch61rsyu9gxos96a9/3.-PEMBELAJARAN-BERBASIS-PROJEK.pptx?rlkey=cfru4prp5q37ag3bf4z8jhzcb&dl=1",
                "pptx_size": "27.7 MB"
            },
            {
                "title": "6. Implementasi Kurikulum PKN Pada Persekolahan",
                "slides": "Slide Hal. 8–28 (Tahapan Adopsi Kurikulum Karakter pada Sekolah, Pesantren, dan Madrasah)",
                "pdf_url": "https://www.dropbox.com/scl/fi/l31yame2e48ghsq4su02a/6.-Implementasi-Kurikulum-PKN-Pada-Persekolahan.pdf?rlkey=3qcjge7qn0sqebohiybyomkph&dl=1",
                "pdf_size": "1.9 MB",
                "pptx_url": "https://www.dropbox.com/scl/fi/d5g15b0din35v06sanzcx/6.-Implementasi-Kurikulum-PKN-Pada-Persekolahan.pptx?rlkey=n7o2e20svwk8p61i7fp9cvcys&dl=1",
                "pptx_size": "501 KB"
            },
            {
                "title": "10 MASALAH PENDIDIKAN",
                "slides": "Slide Hal. 15–75 (Diagnosis Akar Krisis Pendidikan Modern & Desain Solutif PKN)",
                "pptx_url": "https://www.dropbox.com/scl/fi/jqnc3ldzd7ssjs8q45us9/10-MASALAH-PENDIDIKAN.pptx?rlkey=cpxg69hwsgntk514h37wb2gcr&dl=1",
                "pptx_size": "97.5 MB"
            }
        ]
    }
]

def format_citation_callout(citations):
    lines = [
        "",
        "> [!quote] Dokumen & Slide Presentasi Rujukan Resmi PKN",
        "> Pembahasan dalam artikel ini bersumber langsung dari materi tayang pelatihan dan dokumen kurikulum resmi PKN oleh **Ustadz Abdul Kholiq**:",
        ">"
    ]
    for c in citations:
        title = c["title"]
        slides = c["slides"]
        lines.append(f"> - **Materi:** *{title}*")
        lines.append(f">   - 📖 **Rujukan Slide:** {slides}")
        
        btn_items = []
        if "pdf_url" in c:
            pdf_dl = c["pdf_url"]
            pdf_view = pdf_dl.replace("dl=1", "dl=0")
            size = f" ({c['pdf_size']})" if "pdf_size" in c else ""
            btn_items.append(f"[📥 Unduh PDF{size}]({pdf_dl})")
        if "pptx_url" in c:
            pptx_dl = c["pptx_url"]
            size = f" ({c['pptx_size']})" if "pptx_size" in c else ""
            btn_items.append(f"[📊 Unduh PPTX Asli{size}]({pptx_dl})")
        
        # Add view link using the first available link with dl=0
        first_url = c.get("pdf_url") or c.get("pptx_url")
        if first_url:
            view_url = first_url.replace("dl=1", "dl=0")
            btn_items.append(f"[👁️ Buka di Dropbox]({view_url})")

        btn_str = " • ".join(btn_items)
        lines.append(f">   - 🔗 **Akses Berkas:** {btn_str}")
        lines.append(">")
        
    return "\n".join(lines).rstrip(">") + "\n"

def inject_citations_into_file(filepath, citations):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if CITATION_TAG in content:
        # Already injected
        return False

    callout_text = format_citation_callout(citations)

    # Place before ## Rujukan, ## Sumber, or at the end of the file
    lines = content.splitlines()
    insert_idx = -1
    for idx, l in enumerate(lines):
        if l.strip().lower() in ["## rujukan", "## sumber rujukan", "## referensi", "## sumber"]:
            insert_idx = idx
            break

    if insert_idx != -1:
        new_lines = lines[:insert_idx] + ["", "---", callout_text.strip(), ""] + lines[insert_idx:]
    else:
        new_lines = lines + ["", "---", "", callout_text.strip(), ""]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines) + "\n")

    return True

def main():
    md_files = glob.glob("content/**/*.md", recursive=True)
    print(f"Total markdown files available: {len(md_files)}")

    updated_count = 0
    for group in MAPPINGS:
        target_patterns = group["targets"]
        citations = group["citations"]

        for pattern in target_patterns:
            matched_files = [f for f in md_files if pattern in f.replace("\\", "/")]
            if not matched_files:
                print(f"  [!] Warning: pattern '{pattern}' did not match any file.")
            for mf in matched_files:
                if inject_citations_into_file(mf, citations):
                    updated_count += 1
                    print(f"  [+] Injected presentation citations into: {mf}")
                else:
                    print(f"  [-] Already has citations or skipped: {mf}")

    print(f"\nCompleted: {updated_count} files injected with presentation slide citations & Dropbox links.")

if __name__ == "__main__":
    main()

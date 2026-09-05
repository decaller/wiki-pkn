#!/usr/bin/env python3
"""
enrich_batch3.py
Melengkapi artikel pada Klaster Hakikat Insan, Jiwa & Nilai Transendental (Batch 3)
dengan elemen-elemen baku template tanpa menghapus konten yang ada.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

BATCH3_ITEMS = {
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md": (
        "Bersatunya Ruh dan Jasad Membentuk Jiwa",
        "Hakikat Insan",
        "Anak diperlakukan hanya seperti mesin fisik yang diberi makan dan les kognitif tanpa pernah disentuh kebutuhan ruhaninya, memicu kehampaan eksistensial."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Tujuan Hidup Manusia.md": (
        "Tujuan Hidup Manusia",
        "Visi Kehidupan",
        "Remaja muslim menganggap sukses hidup hanya sebatas menjadi kaya raya dan terkenal, kehilangan orientasi ibadah dan khilafah fil ardh."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/index.md": (
        "Konsep Insan",
        "Antropologi Islam",
        "Pola pendidikan mereduksi manusia menjadi sekadar angka statistik dan pekerja industri, mengabaikan kemuliaan fitrah khalifah."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Ammarah.md": (
        "Jiwa Ammarah",
        "Dinamika Nafs",
        "Anak balita tantrum hebat membenturkan kepala ke lantai saat keinginannya ditolak, dan orang tua membalasnya dengan bentakan kasar."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Lawwamah.md": (
        "Jiwa Lawwamah",
        "Dinamika Nafs",
        "Anak usia 9 tahun merasa sangat bersalah setelah memecahkan piring dan menangis ketakutan karena mengira Allah akan membencinya selamanya."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/Muthmainnah.md": (
        "Jiwa Muthmainnah",
        "Dinamika Nafs",
        "Pendidik menuntut santri langsung bersikap tenang dan zuhud layaknya waliyullah, tanpa membimbing proses pergulatan batinnya dari tingkat ammarah."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/index.md": (
        "Pembagian Jiwa",
        "Psikospiritual Islam",
        "Orang tua memvonis anak yang berbuat salah sebagai 'anak jahat', tidak memahami bahwa jiwa anak sedang berada dalam fase dialektika nafs."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/index.md": (
        "Fitrah Keimanan",
        "Tauhid & Akidah",
        "Pengajaran akidah disampaikan sebagai hafalan pasal teologis yang kering tanpa pernah menumbuhkan rasa takjub dan cinta kepada Allah."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tawakkal dan Doa.md": (
        "Tawakkal dan Doa",
        "Spiritualitas Amal",
        "Keluarga mengalami stres berat saat anak gagal ujian masuk sekolah favorit karena mengandalkan usaha teknis semata tanpa kepasrahan doa."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tazkiyatun Nafs.md": (
        "Tazkiyatun Nafs",
        "Penyucian Jiwa",
        "Orang tua menuntut anak berakhlak mulia sementara diri sendiri hobi bergosip, pamer kemewahan, dan malas shalat tepat waktu."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/index.md": (
        "Faktor Internal dan Eksternal",
        "Ekosistem Tarbiyah",
        "Mendidik anak dengan keras di rumah namun membiarkannya bergaul bebas tanpa saringan di lingkungan yang toksik."
    ),
    "Renungan/Hak dan Kewajiban.md": (
        "Hak dan Kewajiban Insani",
        "Keadilan Nabawiyah",
        "Orang tua terus menuntut hak dihormati dan ditaati oleh anak, namun melalaikan kewajiban memberikan rasa aman, cinta, dan teladan shalih."
    ),
    "Renungan/index.md": (
        "Tafakkur & Renungan",
        "Kontemplasi Kehidupan",
        "Kehidupan keluarga berjalan seperti rutinitas mekanis yang hampa tanpa ada jeda waktu untuk merenungi tanda-tanda kebesaran Allah."
    )
}

def generate_enrichment(title, domain, scenario):
    callouts = f"""
> [!info] Refleksi Lapangan: Menjaga Kemurnian Batin dalam Dinamika {title}
> **Kondisi Faktual:** Sering kali pengasuhan terjebak pada tuntutan perilaku luar (*zhahir*) sementara kondisi ruhani dan dinamika batiniah (*bathin*) anak terabaikan, melahirkan kegersangan jiwa.  
> **Akar Masalah PKN:** Mereduksi manusia menjadi makhluk materialistis tanpa menghidupkan sambungan fitrah ketuhanan (*shibghatullah*) yang menjadi sumber kedamaian sejati.  
> **Langkah Penanganan Nabawiyah:**  
> 1. Hidupkan suasana ibadah yang khusyuk dan penuh penghayatan di lingkungan rumah.  
> 2. Bantu anak mengenali gejolak emosi dan bisikan jiwanya dengan bimbingan wahyu.  
> 3. Tanamkan orientasi akhirat sebagai kompas penentu seluruh cita-cita duniawi.

> [!warning] Peringatan Risiko Pengasuhan: Mengabaikan Aspek Ruhani {title}
> * **Bentuk Kesalahan:** Mengabaikan doa, meremehkan tazkiyatun nafs, atau membebani jiwa anak dengan ekspektasi duniawi yang melampaui batas fitrah.
> * **Dampak Terhadap Jiwa:** Lahirnya penyakit hati (hasad, riya', ujub, putus asa), kehampaan makna hidup, dan kerapuhan mental saat menghadapi ujian takdir.
> * **Pencegahan Nabawiyah:** Rasulullah ﷺ senantiasa berdoa: *"Ya Allah, karuniakanlah ketakwaan pada jiwaku dan sucikanlah ia, Engkaulah sebaik-baik yang mensucikannya"* (HR. Muslim).

> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Duduklah bersama anak di waktu fajar atau senja, tataplah pergantian warna langit bersama-sama, dan ajak bertafakkur: *"Siapakah yang menggerakkan matahari dan melukis awan seindah ini setiap hari tanpa lelah?"*
> * **Tujuan:** Menghidupkan kesadaran tauhid rububiyah dan menyejukkan kalbu anak dengan keagungan Allah SWT.
"""

    tafrith_ifrath = f"""
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam {title}

| Dimensi Penghayatan | Gejala Sikap yang Teramati | Dampak Psikospiritual pada Anak |
| :--- | :--- | :--- |
| **Tafrith (Materialisme Kering / Sekuler)** | Mengabaikan aspek ruhani, mendidik anak tanpa orientasi akhirat, dan memandang manusia hanya sebagai entitas biologis-ekonomi. | Jiwa anak gersang, mudah cemas, mengukur kemuliaan hanya dari materi, dan rentan krisis eksistensial. |
| **Ifrath (Spiritualisme Ekstrem / Ghuluw)** | Menafikan kebutuhan fisik jasmani, melarang anak bermain secara wajar, dan memaksakan kezuhudan sebelum tiba etape kematangan akal. | Anak tertekan, memendam kebencian pada simbol agama, atau mengalami disorientasi sosial di masyarakat. |
| **Al-Wasathiyah (Keseimbangan Fitrah Nabawi)** | Memadukan pemenuhan hak jasad secara halal dengan nutrisi ruhani yang berbobot, menempatkan dunia sebagai ladang akhirat. | Terbentuk kepribadian mukmin paripurna: sehat jasmaninya, cerdas akalnya, suci jiwanya (*muthmainnah*), dan berkontribusi nyata bagi umat. |
"""

    studi_kasus = f"""
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** {scenario}

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Introspeksi Spiritual Pendidik (Hari 1–3)**  
   Orang tua memperbanyak taubat, shalat malam, dan memohon hidayah bagi anak. Menyadari bahwa hati anak berada di antara dua jemari ar-Rahman.
2. **Fase 2: Pendekatan Welas Asih (*Sentuhan Ruhani*) (Hari 4–7)**  
   Menghadirkan kelembutan tanpa syarat. Menemani anak dalam keheningan, mengusap kepalanya seraya mendoakan keberkahan, dan menciptakan rasa aman di rumah.
3. **Fase 3: Dialog Makna Hidup (*Tadabbur Nalar*) (Pekan 2)**  
   Mengajak anak berdiskusi santai mengenai hakikat penciptaan manusia, kasih sayang Allah yang melimpah, dan indahnya ampunan bagi hamba yang bertaubat.
4. **Fase 4: Pembiasaan Amal & Keteladanan Nyata (Pekan 3 dst)**  
   Membangun ritme ibadah keluarga yang menyenangkan (tilawah bersama, sedekah subuh, membantu dhuafa) sebagai wujud nyata kesucian jiwa.
"""
    return callouts, tafrith_ifrath, studi_kasus

def enrich_file(rel_path, title, domain, scenario):
    file_path = CONTENT_DIR / rel_path
    if not file_path.exists():
        print(f"[ERROR] File not found: {rel_path}")
        return False

    content = file_path.read_text(encoding="utf-8")

    if "## Diagnosis Penyimpangan: Tafrith vs Ifrath" in content:
        print(f"[SKIP] Already enriched: {rel_path}")
        return True

    callouts, tafrith, studi_kasus = generate_enrichment(title, domain, scenario)

    # 1. Insert Callouts (after banner / disclaimer)
    banner_match = re.search(r"!\[\[assets/banners/[^\]]+\]\](?:\s*\*Gambar:[^\n]*\*)?", content)
    if banner_match:
        insert_pos = banner_match.end()
        content = content[:insert_pos] + "\n\n" + callouts.strip() + "\n" + content[insert_pos:]
    else:
        disclaimer_marker = "> Rangkuman materi kurikulum Pendidikan Karakter Nabawiyah"
        idx = content.find(disclaimer_marker)
        if idx != -1:
            end_callout = content.find("\n\n", idx)
            insert_pos = end_callout + 2 if end_callout != -1 else idx + 200
            content = content[:insert_pos] + "\n\n" + callouts.strip() + "\n" + content[insert_pos:]
        else:
            content = callouts.strip() + "\n\n" + content

    # 2. Insert Diagnosis & Studi Kasus
    addition_block = f"\n---\n\n{tafrith.strip()}\n\n---\n\n{studi_kasus.strip()}\n\n---\n"

    tautan_match = re.search(r"##\s+(?:Tautan|Rujukan Silang|Peta Konsep)", content, re.IGNORECASE)
    citation_match = re.search(r">\s*\[!quote\]\s+Dokumen\s+&\s+Slide", content, re.IGNORECASE)

    if tautan_match:
        pos = tautan_match.start()
        content = content[:pos] + addition_block + "\n" + content[pos:]
    elif citation_match:
        pos = citation_match.start()
        content = content[:pos] + addition_block + "\n" + content[pos:]
    else:
        content = content + "\n\n" + addition_block

    file_path.write_text(content, encoding="utf-8")
    print(f"[SUCCESS] Enriched: {rel_path}")
    return True

def main():
    print(f"Memulai pengayaan Batch 3: Klaster Hakikat Insan, Jiwa & Nilai Transendental ({len(BATCH3_ITEMS)} Artikel)...")
    success_count = 0
    for rel_path, (title, domain, scenario) in BATCH3_ITEMS.items():
        if enrich_file(rel_path, title, domain, scenario):
            success_count += 1
    print(f"\nSelesai: {success_count}/{len(BATCH3_ITEMS)} artikel Batch 3 berhasil diperkaya!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
enrich_batch4.py
Melengkapi seluruh sisa artikel pada Klaster Kerangka Implementasi, Kaidah,
Standar Lembaga, dan Hub Utama (Batch 4) dengan elemen baku template.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

BATCH4_ITEMS = {
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md": (
        "4 Elemen Implementasi",
        "Pondasi Kurikulum",
        "Lembaga pendidikan hanya fokus pada target akademik tanpa membangun ekosistem keteladanan guru dan keterlibatan orang tua."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md": (
        "4 Kaidah Implementasi",
        "Kaidah Penerapan",
        "Pendidik menuntut perubahan adab santri secara drastis dalam sepekan tanpa menerapkan kaidah kemudahan (*taisir*) dan penahapan (*tadarruj*)."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md": (
        "8 Standar Implementasi PKN",
        "Standar Mutu Lembaga",
        "Sekolah mengklaim menerapkan kurikulum fitrah nabawiyah namun instrumen penilaiannya masih menyalin mentah-mentah sistem pemeringkatan angka kaku."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md": (
        "Kaidah Implementasi Berbagai Lembaga",
        "Adaptasi Manhaj",
        "Pesantren dan sekolah formal menyalin kurikulum PKN tanpa menyesuaikan dengan kultur lokal dan kesiapan asatidzah di lapangan."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md": (
        "Panduan RPP dan Observasi Lapangan",
        "Instrumen Pembelajaran",
        "Guru merasa terbebani administrasi RPP tebal sehingga waktu interaksi hangat dengan santri tersita habis untuk mengetik dokumen formalitas."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/index.md": (
        "Kaidah dan Elemen Implementasi",
        "Kerangka Kerja",
        "Penerapan PKN di sekolah terhenti di level slogan spanduk tanpa pernah diterjemahkan ke dalam panduan teknis operasional harian."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Tanggung Jawab Pendidikan.md": (
        "Tanggung Jawab Pendidikan",
        "Amanah Tarbiyah",
        "Orang tua merasa lepas tanggung jawab setelah membayar SPP mahal, menganggap sekolah bertanggung jawab 100% atas moralitas anak."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/index.md": (
        "Peran dan Tanggung Jawab Pengasuhan",
        "Sinergi Tarbiyah",
        "Terjadinya lempar tanggung jawab antara ayah, ibu, dan pihak sekolah saat anak mengalami masalah kenakalan remaja."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/index.md": (
        "Implementasi Kurikulum PKN",
        "Manhaj Operasional",
        "Institusi pendidikan gagal mengeksekusi visi nabawiyah karena tidak memiliki tahapan peta jalan (*roadmap*) yang terukur."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Arahan Teknis Implementasi.md": (
        "Arahan Teknis Implementasi",
        "Eksekusi Lapangan",
        "Guru bingung memulai tahapan restorasi fitrah di kelas karena minimnya modul teknis SOP penanganan masalah adab santri."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight/SOTABH.md": (
        "SOTABH (School of Talent and Bakat)",
        "Pendidikan Bakat Berbasis Fitrah",
        "Sekolah bakat terjebak dalam komersialisasi panggung kompetisi tanpa menanamkan adab khidmah sosial dan kerendahan hati."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight/index.md": (
        "Insight PKN",
        "Wawasan Strategis",
        "Praktisi pendidikan mengadopsi teori psikologi Barat sekuler tanpa menyaringnya dengan timbangan wahyu dan sirah sahabat."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/index.md": (
        "Insight & Teknis",
        "Panduan Manhaj",
        "Kesenjangan antara konsep filosofis tinggi di ruang seminar dengan kenyataan benturan emosi harian di ruang kelas."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md": (
        "Asesmen 40 Bakat Nabawiyah",
        "Pemetaan Potensi",
        "Orang tua menjadikan hasil kuisioner bakat sebagai label mati yang membatasi potensi anak, bukan sebagai peta eksplorasi dinamis."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Panduan Asesmen dan Observasi TB40.md": (
        "Panduan Asesmen dan Observasi TB40",
        "Metodologi Observasi",
        "Penilai terlalu terburu-buru menyimpulkan bakat anak hanya dari satu peristiwa tanpa mengamati konsistensi Rukun 3A selama berbulan-bulan."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/PKN Blueprint Arsitektur Sistem.md": (
        "Cetak Biru Arsitektur PKN",
        "Arsitektur Sistem",
        "Implementasi sistem pendidikan tambal sulam tanpa memahami keterpaduan 5 level arsitektur kurikulum nabawiyah."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Bank Studi Kasus.md": (
        "Bank Studi Kasus Kurikulum Peristiwa",
        "Resolusi Masalah Karakter",
        "Guru menangani kasus perkelahian santri dengan hukuman fisik kurungan tanpa membedah akar luka batiniah dan hutang pengasuhannya."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/index.md": (
        "Paradigma & Implementasi PKN",
        "Sintesis Manhaj",
        "Dilema memadukan idealisme manhaj salafush shalih dengan tuntutan regulasi dinas pendidikan modern."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/FAQ Ringkas.md": (
        "FAQ Pertanyaan Kunci PKN",
        "Klarifikasi Manhaj",
        "Masyarakat keliru mengira PKN menolak sains modern atau menganggap PKN hanya cocok untuk pesantren pedesaan."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Referensi Kajian Video.md": (
        "Referensi Kajian Video PKN",
        "Khazanah Multimedia",
        "Penonton menyimak kajian video secara sepotong-sepotong di media sosial sehingga salah menangkap konteks fatwa tarbiyah Ustadz Abdul Kholiq."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/index.md": (
        "Korpus Dokumen PKN",
        "Basis Pengetahuan",
        "Kekayaan khazanah dokumen manhaj belum terindeks rapi sehingga sulit diakses oleh para asatidzah di pelosok daerah."
    ),
    "Paradigma - Implementasi PKN/index.md": (
        "Direktori Paradigma & Implementasi",
        "Peta Navigasi",
        "Pendidik pemula kebingungan menentukan urutan belajar konsep PKN dari hulu (filosofis tauhid) hingga hilir (RPP kelas)."
    ),
    "index.md": (
        "Gerbang Wiki PKN",
        "Ensiklopedia Manhaj",
        "Umat Islam membutuhkan basis pengetahuan tarbiyah nabawiyah yang shahih, komprehensif, terstruktur, dan aplikatif di era disrupsi peradaban."
    )
}

def generate_enrichment(title, domain, scenario):
    callouts = f"""
> [!info] Refleksi Lapangan: Realitas Penerapan {title}
> **Kondisi Faktual:** Dalam praktik nyata di lembaga dan rumah tangga, penerapan {title} sering menghadapi tantangan resistensi budaya lama dan tuntutan hasil instan.  
> **Akar Masalah PKN:** Ketidakselarasan antara standar ideal manhaj dengan kapasitas pendidik yang belum tuntas melakukan tazkiyatun nafs.  
> **Langkah Penanganan Nabawiyah:**  
> 1. Bangun pemahaman bersama (*idrak musytarak*) di kalangan pimpinan, guru, dan orang tua.  
> 2. Utamakan keteladanan nyata sebelum membuat aturan administratif yang kaku.  
> 3. Terapkan evaluasi berkala berbasis pertumbuhan karakter batin, bukan sekadar kelengkapan berkas fisik.

> [!warning] Peringatan Risiko: Jebakan Formalitas dalam {title}
> * **Bentuk Kesalahan:** Mengubah kurikulum fitrah nabawiyah menjadi sekadar rutinitas administratif formalitas tanpa ruh keimanan.
> * **Dampak Terhadap Jiwa:** Hilangnya keberkahan majelis ilmu, kejenuhan pendidik, dan kegagalan mencetak generasi mukallaf yang kokoh.
> * **Pencegahan Nabawiyah:** Jaga kemurnian niat lillahi ta'ala dan jadikan setiap tahapan implementasi sebagai amal jariyah penegak peradaban Islam.

> [!tip] Tips Praktis Hari Ini
> * **Aksi Sederhana:** Evaluasi satu prosedur pembelajaran atau kebiasaan rumah tangga hari ini: apakah ia mempermudah mekarnya fitrah anak ataukah justru membebani jiwa tanpa dalil yang jelas?
> * **Tujuan:** Memastikan seluruh instrumen berjalan di atas kaidah *at-taisir* (kemudahan) dan *ar-rifq* (kelembutan).
"""

    tafrith_ifrath = f"""
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam {title}

| Dimensi Operasional | Gejala Sikap yang Teramati | Dampak Psikospiritual pada Ekosistem |
| :--- | :--- | :--- |
| **Tafrith (Lalai / Ketiadaan Standar)** | Berjalan tanpa arah yang jelas, mengabaikan evaluasi mutu karakter, dan membiarkan distorsi fitrah tanpa tindakan korektif. | Ekosistem pendidikan menjadi stagnan, kualitas lulusan rapuh, dan visi peradaban Islam tidak tercapai. |
| **Ifrath (Birokratisasi Kaku / Memaksa)** | Membebani guru dan santri dengan target dokumen berlebihan, menuntut kesempurnaan instan, dan menghukum deviasi tanpa hikmah. | Guru mengalami stres kronis (*burnout*), santri kehilangan kegembiraan belajar, dan suasana lembaga menjadi dingin tanpa cinta. |
| **Al-Wasathiyah (Implementasi Hikmah Nabawiyah)** | Menegakkan standar mutu tinggi (*itqan*) yang dibingkai dengan kelapangan kasih sayang, pembinaan bertahap, dan keteladanan otentik. | Tercipta ekosistem tarbiyah yang hidup, penuh keberkahan, melahirkan lulusan berakhlak mulia dan siap memimpin peradaban. |
"""

    studi_kasus = f"""
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** {scenario}

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Rekalibrasi Visi & Niat (Hari 1–7)**  
   Pimpinan dan pendidik duduk bersama dalam majelis muhasabah. Mengakui kekurangan diri dan meluruskan orientasi semata-mata mencari ridha Allah.
2. **Fase 2: Dialog Terbuka & Pemetaan Kebutuhan (Pekan 2)**  
   Mendengarkan aspirasi dan kendala nyata yang dihadapi pelaksana lapangan dengan empati tanpa penghakiman.
3. **Fase 3: Penyederhanaan Sistem Berbasis Fitrah (Bulan 1)**  
   Memangkas birokrasi yang membebani dan memfokuskan energi pada penguatan interaksi *Bahasa Hati* dan *Bahasa Lisan*.
4. **Fase 4: Pembiasaan Budaya Mutu & Pendampingan Konsisten (Bulan 2 dst)**  
   Menegakkan standar dengan teladan nyata, pendampingan beradab, dan apresiasi tulus atas setiap kemajuan karakter santri.
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
    print(f"Memulai pengayaan Batch 4: Klaster Kerangka Implementasi, Kaidah & Standar Lembaga ({len(BATCH4_ITEMS)} Artikel)...")
    success_count = 0
    for rel_path, (title, domain, scenario) in BATCH4_ITEMS.items():
        if enrich_file(rel_path, title, domain, scenario):
            success_count += 1
    print(f"\nSelesai: {success_count}/{len(BATCH4_ITEMS)} artikel Batch 4 berhasil diperkaya!")

if __name__ == "__main__":
    main()

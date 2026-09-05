#!/usr/bin/env python3
"""
enrich_batch2.py
Melengkapi artikel pada Klaster Metode Mendidik, Pengasuhan & Pemulihan (Batch 2)
dengan elemen-elemen baku template tanpa menghapus konten yang ada.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

BATCH2_ITEMS = {
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Hati.md": (
        "Bahasa Hati",
        "Komunikasi Jiwa",
        "Anak usia 7 tahun sering mengamuk dan memukul adiknya saat ibu sibuk bekerja di depan laptop, menolak ditenangkan dengan mainan baru."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Lisan.md": (
        "Bahasa Lisan",
        "Komunikasi Nalar",
        "Orang tua selalu menasihati anak remaja dengan ceramah panjang satu arah selama 1 jam di meja makan, yang dibalas anak dengan tatapan kosong dan headphone."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Tangan.md": (
        "Bahasa Tangan",
        "Teladan Amal & Ketegasan",
        "Anak usia 10 tahun menolak membersihkan tumpahan minumannya dan menantang orang tua dengan berkata: 'Bunda saja yang bereskan!'"
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/index.md": (
        "Metode Mendidik Nabawiyah",
        "Metode Mendidik",
        "Orang tua terbalik menerapkan hierarki metode: menggunakan kekerasan fisik (tangan) di usia balita dan ceramah teoritis panjang saat anak sedang emosi."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Iman/Tangki Cinta.md": (
        "Tangki Cinta",
        "Kehangatan Emosional",
        "Anak usia 9 tahun mencari perhatian di sekolah dengan cara mencuri alat tulis temannya meskipun keluarganya berkecukupan secara materi."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Batas Toleransi.md": (
        "Batas Toleransi",
        "Disiplin Nabawiyah",
        "Orang tua tidak memiliki batas tegas, sehingga anak bebas bermain gawai hingga larut malam dan bolos shalat subuh tanpa konsekuensi."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Imunitas Sosial.md": (
        "Imunitas Sosial",
        "Ketahanan Mental",
        "Remaja muslim merasa minder dan malu mengakui dirinya tidak merayakan pesta tahun baru karena takut dikucilkan teman sekelasnya."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/index.md": (
        "Luka dan Hutang Pengasuhan",
        "Pemulihan Jiwa",
        "Orang tua yang dulu mengalami kekerasan verbal di masa kecil tanpa sadar meniru pola yang sama dengan membentak putra sulungnya setiap hari."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md": (
        "Euforia Pengasuhan",
        "Keseimbangan Batin",
        "Orang tua terlalu memuja prestasi anak di media sosial hingga anak mengalami kecemasan tinggi (*anxiety*) karena takut mengecewakan ekspektasi publik."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md": (
        "Recovery Jiwa",
        "Pemulihan Fitrah",
        "Remaja yang pernah mengalami trauma perundungan di sekolah mengalami mutisme selektif dan menolak keluar dari kamarnya selama berbulan-bulan."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Ayah dan Bunda.md": (
        "Peran Ayah dan Bunda",
        "Sinergi Pengasuhan",
        "Ayah menyerahkan 100% urusan pendidikan anak kepada ibu dengan dalih sudah lelah bekerja mencari nafkah, memicu sindrom *fatherless*."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md": (
        "Peran Guru dan Lembaga Pendidikan",
        "Kemitraan Tarbiyah",
        "Sekolah dan orang tua saling menyalahkan ketika nilai karakter anak merosot tanpa pernah duduk bersama menyusun kurikulum berbasis fitrah."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/index.md": (
        "Pendidikan Ideal",
        "Manhaj Kenabian",
        "Sekolah Islam modern terjebak dalam orientasi bisnis dan piala lomba semu, mengabaikan ketenangan jiwa (*muthmainnah*) dan adab santri."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Benang Merah Pendidikan.md": (
        "Benang Merah Pendidikan",
        "Filosofi Peradaban",
        "Kurikulum sekolah terpecah-pecah tanpa poros tauhid yang jelas, sehingga anak memandang ilmu agama dan ilmu sains sebagai dua kutub terpisah."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Menumbuhkan Kesadaran Beramal.md": (
        "Kesadaran Beramal",
        "Kematangan Jiwa",
        "Santri hanya rajin shalat berjamaah ketika ada ustadz pengawas yang memegang rotan, dan langsung bubar ketika pengawas tidak hadir."
    ),
    "Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Pembelajaran Alamiah.md": (
        "Pembelajaran Alamiah",
        "Tarbiyah Fitriyah",
        "Anak usia SD tidak mengenal nama-nama pohon di halamannya dan tidak tahu dari mana beras berasal karena terkurung dalam dinding kelas bertembok tebal."
    )
}

def generate_enrichment(title, domain, scenario):
    callouts = f"""
> [!info] Refleksi Lapangan: Problematika Nyata dalam Dinamika {title}
> **Kondisi Faktual:** Banyak keluarga dan institusi pendidikan menghadapi benturan nyata saat menerapkan {title}, di mana niat baik mendidik sering kali berujung pada perlawanan anak atau hasil yang semu.  
> **Akar Masalah PKN:** Mengabaikan kondisi kesiapan batin (*tahapan qalbiyah*) dan memaksakan instrumen lahiriah tanpa mengisi jembatan kelekatan kasih sayang terlebih dahulu.  
> **Langkah Penanganan Nabawiyah:**  
> 1. Mulai dari pemulihan keheningan kalbu pendidik (*tazkiyatun nafs*) dan doa yang tulus.  
> 2. Penuhi tangki cinta anak agar terjalin rasa aman (*trust*) yang kokoh.  
> 3. Terapkan prinsip penahapan (*tadarruj*) dan kelembutan hikmah (*rifq*) dalam menegakkan batasan syariat.

> [!warning] Peringatan Risiko Pengasuhan: Jebakan Fatal dalam {title}
> * **Bentuk Kesalahan:** Menggunakan ancaman, amarah tanpa kendali, atau menuntut perubahan instan dalam waktu semalam.
> * **Dampak Terhadap Jiwa:** Memadamkan gairah fitrah, menimbulkan kebencian tersembunyi, dan melahirkan generasi hipokrit yang hanya patuh saat diawasi.
> * **Pencegahan Nabawiyah:** Rasulullah ﷺ menegaskan: *"Sesungguhnya kelembutan tidaklah berada pada sesuatu melainkan ia akan menghiasinya, dan tidaklah kelembutan dicabut dari sesuatu melainkan ia akan memperburuknya"* (HR. Muslim).

> [!tip] Tips Praktis Pengasuhan Hari Ini
> * **Aksi Sederhana:** Tahan diri Anda dari memberikan teguran atau nasihat apapun selama 24 jam ke depan; gantikan seluruh interaksi dengan senyuman, pelukan hangat, dan pelayanan tulus.
> * **Tujuan:** Merestorasi saluran penerimaan batin anak sehingga nasihat berikutnya akan masuk laksana air sejuk di tanah yang subur.
"""

    tafrith_ifrath = f"""
## Diagnosis Penyimpangan: Tafrith vs Ifrath dalam {title}

| Dimensi Pendekatan | Gejala Sikap yang Teramati | Dampak Psikospiritual pada Anak |
| :--- | :--- | :--- |
| **Tafrith (Meremehkan / Melalaikan)** | Membiarkan tanpa arahan, permisif berlebihan, takut menegur karena khawatir anak menangis, dan tidak ada batasan moral yang jelas. | Anak tumbuh tanpa pegangan nilai (*anomi*), berjiwa rapuh, mudah terseret arus negatif lingkungan, dan tidak menghargai otoritas orang tua. |
| **Ifrath (Otoriter / Memaksa Berlebihan)** | Menuntut kesempurnaan mutlak, kaku tanpa toleransi, menghukum kesalahan dengan intimidasi, dan menafikan fitrah tahapan usia. | Jiwa anak terluka menahun (*trauma pengasuhan*), memendam dendam, mengalami krisis identitas, atau meledak memberontak saat dewasa. |
| **Al-Wasathiyah (Jalan Tengah Nabawiyah)** | Mengayomi dengan limpahan kasih sayang hakiki, menanamkan kesadaran nalar dialogis, seraya menegakkan batas toleransi secara tegas dan beradab. | Tumbuh generasi mukallaf yang merdeka jiwanya, lurus fitrahnya, ikhlas amalnya, dan memiliki imunitas moral yang kokoh di tengah peradaban modern. |
"""

    studi_kasus = f"""
## Studi Kasus Nyata & Solusi Kuratif Tadarruj

### Skenario Permasalahan
> **Kasus:** {scenario}

### Tahapan Solusi Kuratif Langkah-demi-Langkah (Manhaj Tadarruj)
1. **Fase 1: Pendinginan & Penghentian Celaan (Hari 1–3)**  
   Orang tua/guru menghentikan semua hukuman dan bentakan verbal. Mengakui bahwa ketegangan yang terjadi adalah sinyal ausnya hubungan batin yang harus diperbaiki dari pihak dewasa terlebih dahulu.
2. **Fase 2: Membuka Kembali Gerbang Jiwa (*Bahasa Hati*) (Hari 4–7)**  
   Fokus memenuhi kebutuhan afeksi dasar anak: mendampingi tanpa menggurui, menyajikan makanan kegemaran, dan memeluk hangat di waktu-waktu mustajab (sebelum tidur dan selepas subuh).
3. **Fase 3: Dialog Hikmah & Rekonstruksi Nalar (*Bahasa Lisan*) (Pekan 2)**  
   Mengajak anak berdialog santai di luar rumah (*walking & talking*). Menggunakan kalimat terbuka: *"Apa yang bisa Ayah/Bunda bantu agar kamu merasa lebih nyaman dan bersemangat?"*
4. **Fase 4: Penegasan Amanah & Adab Amal (*Bahasa Tangan*) (Pekan 3 dst)**  
   Merumuskan kesepakatan bersama yang adil dan realistis. Melatih tanggung jawab nyata dengan pendampingan penuh kasih sayang dan ketegasan tanpa kezaliman.
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
    print(f"Memulai pengayaan Batch 2: Klaster Metode Mendidik, Pengasuhan & Pemulihan ({len(BATCH2_ITEMS)} Artikel)...")
    success_count = 0
    for rel_path, (title, domain, scenario) in BATCH2_ITEMS.items():
        if enrich_file(rel_path, title, domain, scenario):
            success_count += 1
    print(f"\nSelesai: {success_count}/{len(BATCH2_ITEMS)} artikel Batch 2 berhasil diperkaya!")

if __name__ == "__main__":
    main()

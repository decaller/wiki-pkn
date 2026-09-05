#!/usr/bin/env python3
"""
enrich_metadata_tags.py
Menginjeksi metadata frontmatter 'tags' dan 'description' pada seluruh berkas
artikel materi non-template di content/ untuk memaksimalkan:
1. Popover Hover Preview (deskripsi padat & jernih)
2. Tag List Component (@quartz-community/tag-list)
3. Tag Aggregation Page (@quartz-community/tag-page)
Prinsip: ZERO DELETION pada body konten.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

# Rule-based tagging and description based on file path and title
TAG_RULES = [
    # Etape usia
    (r"Thufulah", ["thufulah", "etape-usia", "fitrah", "bahasa-hati"], "Panduan etape usia Thufulah (0–7 tahun): masa kelekatan fitrah, bermain alami, dan pemuasan tangki cinta tanpa hisab syariat."),
    (r"Tamyiz", ["tamyiz", "etape-usia", "adab", "shalat", "bahasa-lisan"], "Panduan etape usia Tamyiz (7–10 tahun): pembiasaan nalar adab, laboratorium shalat 3 tahun, dan observasi bakat Rukun 3A."),
    (r"Murahaqah", ["murahaqah", "etape-usia", "kedisiplinan", "bakat", "bahasa-tangan"], "Panduan etape usia Murahaqah (10–15 tahun): pendisiplinan berbatas syariat, pemisahan tempat tidur, dan pemagangan tanggung jawab."),
    (r"Syabab", ["syabab", "etape-usia", "kemandirian", "amal-shalih"], "Panduan etape usia Syabab (15+ tahun): kemitraan aqil-baligh, hisab syar'i mukallaf, dan karya peradaban penopang ummah."),
    
    # Bakat rumpun
    (r"Bekerja Keras", ["bakat-tb40", "bekerja-keras", "etos-kerja"], "Rumpun bakat Bekerja Keras: membedah pilar ketahanan kerja fisik, kegigihan, dan integritas ikhtiar amal shalih."),
    (r"Memerintah", ["bakat-tb40", "memerintah", "kepemimpinan"], "Rumpun bakat Memerintah: karakter qawwamah, ketegasan syari'ah, keberanian moral, dan kepemimpinan peradaban."),
    (r"Berpikir", ["bakat-tb40", "berpikir", "kecerdasan-nalar"], "Rumpun bakat Berpikir: analisis mendalam, perumusan hikmah, ketajaman firasah, dan inovasi gagasan."),
    (r"Bekerja Sama", ["bakat-tb40", "bekerja-sama", "sinergi-sosial"], "Rumpun bakat Bekerja Sama: kehangatan silaturahmi, keadilan proporsional, ukhuwwah, dan keceriaan komunikasi."),
    (r"Berperasaan", ["bakat-tb40", "berperasaan", "kelembutan-hati"], "Rumpun bakat Berperasaan: kepekaan nurani, rasa malu mulia, kejujuran batin, dan ketangguhan sabar."),
    (r"Melayani", ["bakat-tb40", "melayani", "khidmah"], "Rumpun bakat Melayani: ketulusan pengabdian, itsaar mendahulukan sesama, pemeliharaan amanah, dan kerendahan hati."),
    
    # Metode & Jiwa
    (r"Bahasa Hati", ["metode-mendidik", "bahasa-hati", "tazkiyatun-nafs"], "Hierarki Bahasa Hati: instrumen utama mendidik fitrah anak lewat tatapan mata, keteladanan batin, dan kebersihan jiwa pendidik."),
    (r"Bahasa Lisan", ["metode-mendidik", "bahasa-lisan", "tutur-kata"], "Penerapan Bahasa Lisan: filter tutur nabawi, larangan pelabelan negatif, dan seni berkomunikasi yang memuliakan nalar anak."),
    (r"Bahasa Tangan", ["metode-mendidik", "bahasa-tangan", "kedisiplinan"], "Penerapan Bahasa Tangan: batas tegas kedisiplinan syariat, larangan memukul wajah, dan sanksi edukatif tanpa mempermalukan."),
    (r"Tangki Cinta", ["pengasuhan", "tangki-cinta", "pemulihan-luka"], "Hakikat Tangki Cinta: daya bahan bakar batin anak, indikator tirisnya kasih sayang, dan metode restorasi kelekatan orang tua."),
    (r"Ammarah", ["jiwa", "ammarah", "tazkiyatun-nafs"], "Edukasi Jiwa Ammarah: mengenali dorongan primitif anak, strategi pengalihan energi positif, dan terapi menjinakkan tantrum."),
    (r"Lawwamah", ["jiwa", "lawwamah", "nurani"], "Penguatan Jiwa Lawwamah: mengasah kepekaan nurani penyesalan dosa dan menumbuhkan rasa malu kepada Allah."),
    (r"Muthmainnah", ["jiwa", "muthmainnah", "sakinah"], "Pencapaian Jiwa Muthmainnah: ketenangan batin berdzikir, ridha terhadap takdir, dan stabilitas emosi keluarga sakinah."),
    (r"Recovery", ["pemulihan-luka", "hutang-pengasuhan", "tazkiyatun-nafs"], "Protokol Pemulihan (Recovery): tahapan menyembuhkan trauma pengasuhan masa lalu dan melunasi hutang batin ayah-bunda."),
    (r"Euforia", ["dekonstruksi-mitos", "euforia", "ikhtiar-ikhlas"], "Dekonstruksi Jebakan Euforia: bahaya candu piala dan sanjungan semu yang merusak keikhlasan serta kemurnian fitrah beramal."),
    (r"Imunitas Sosial", ["imunitas-sosial", "benteng-keluarga", "peradaban"], "Membangun Imunitas Sosial: vaksinasi nalar dan ruhiyah anak agar kebal dari fitnah pergaulan dan pengaruh negatif lingkungan."),
    (r"Tawakkal dan Doa", ["ruhiyah", "doa", "tawakkal"], "Senjata Ruhiyah Tarbiyah: perimbangan ikhtiar optimal dan kepasrahan total melalui munajat sepertiga malam terakhir."),
    (r"Tazkiyatun Nafs", ["tazkiyatun-nafs", "pensucian-jiwa", "adab-pendidik"], "Tazkiyatun Nafs Pendidik: membersihkan bejana batin guru dan orang tua sebagai syarat mutlak mengalirkan hidayah ilmu."),
    (r"Peran Ayah dan Bunda", ["peran-ayah", "peran-bunda", "sinergi-keluarga"], "Sinergi Ayah dan Bunda: pembagian peran qawwamah visioner ayah dan hadhanah kehangatan bunda dalam mendidik anak."),
    (r"Peran Guru dan Lembaga", ["peran-guru", "lembaga-pendidikan", "adab-santri"], "Peran Guru dan Lembaga: merawat fitrah santri, meniadakan perundungan dan sistem ranking kaku model pabrik."),
    (r"Tanggung Jawab Pendidikan", ["tanggung-jawab", "hak-anak", "fiqh-tarbiyah"], "Tanggung Jawab Pendidikan: mandat mutlak keluarga yang tak dapat dibeli dengan SPP sekolah menurut syariat Islam."),
    (r"Hak dan Kewajiban", ["hak-anak", "kewajiban-syariat", "keadilan"], "Neraca Hak dan Kewajiban: penunaian hak asasi fitrah anak sebelum menuntut kewajiban hisab syariat."),
    (r"4 Kaidah Implementasi", ["kaidah-emas", "implementasi", "tadarruj"], "Empat Kaidah Emas PKN: satu anak satu kurikulum, tadarruj bertahap, teladan sebelum arahan, dan asah bakat dominan."),
    (r"8 Standar Implementasi", ["standar-mutu", "kelembagaan", "audit-pkn"], "Delapan Standar Mutu PKN 11/2024: pedoman audit kurikulum, pendewasaan santri, dan manajemen lembaga Islam."),
    (r"Benang Merah Pendidikan", ["benang-merah", "kurikulum", "visi-peradaban"], "Benang Merah Pendidikan: menautkan tauhid, adab, ilmu, dan amal menjadi kurikulum terpadu pembina generasi."),
    (r"Menumbuhkan Kesadaran Beramal", ["kesadaran-beramal", "motivasi-internal", "amal-shalih"], "Rantai Kausalitas 5 Tingkat: menggeser motivasi beramal dari sogokan materi menuju kesadaran murni lillahi ta'ala."),
    (r"Pembelajaran Alamiah", ["belajar-alami", "tadabbur-alam", "fitrah-nalar"], "Pembelajaran Alamiah: mengembalikan ruang belajar ke laboratorium alam terbuka yang mengasah indera dan syukur."),
    (r"SOTABH", ["sotabh", "observasi-bakat", "rukun-3a"], "Metodologi SOTAB HEBAT: panduan praktis observasi sifat alami anak dan validasi bakat melalui Rukun 3A."),
    (r"FAQ Ringkas", ["faq", "panduan-praktis", "tanya-jawab"], "Tanya Jawab Ringkas PKN: solusi cepat atas problematika umum pengasuhan anak harian di rumah dan sekolah."),
    (r"Referensi Kajian Video", ["kajian-video", "multimedia", "arsip-ceramah"], "Direktori Video Ceramah PKN: indeks 122 rekaman kajian Ustadz Abdul Kholiq lengkap dengan navigasi timestamp topik."),
    (r"Tujuan Hidup Manusia", ["tujuan-hidup", "khalifah", "ibadah"], "Arsitektur Tujuan Eksistensi: menyelaraskan penghambaan vertikal ('ibadah) dan kepemimpinan bumi (khilafah)."),
    (r"Bersatunya Ruh dan Jasad", ["hakikat-insan", "ruh-jasad", "jiwa"], "Integrasi Ruh, Jasad, dan Nafs: membedah anatomi penciptaan manusia dan keseimbangan asupan nutrisi batiniah."),
]

def get_metadata_for_file(file_path):
    rel_str = str(file_path)
    title = file_path.stem
    
    for pattern, tags, desc in TAG_RULES:
        if re.search(pattern, rel_str, re.IGNORECASE):
            return tags, desc
            
    # Default fallback
    return ["pendidikan-karakter", "fitrah-nabawiyah"], f"Kajian komprehensif {title} dalam kerangka manhaj Pendidikan Karakter Nabawiyah."

def update_frontmatter(file_path):
    content = file_path.read_text(encoding="utf-8")
    
    # Must start with frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not fm_match:
        return False
        
    fm_text = fm_match.group(1)
    body = content[fm_match.end():]
    
    tags, desc = get_metadata_for_file(file_path)
    
    # Check if tags already present
    has_tags = re.search(r"^tags:\s*", fm_text, re.MULTILINE)
    has_desc = re.search(r"^description:\s*", fm_text, re.MULTILINE)
    
    new_fm_lines = fm_text.splitlines()
    
    if not has_desc:
        new_fm_lines.append(f'description: "{desc}"')
        
    if not has_tags:
        new_fm_lines.append("tags:")
        for t in tags:
            new_fm_lines.append(f"  - {t}")
            
    new_fm = "\n".join(new_fm_lines)
    if new_fm != fm_text:
        new_content = f"---\n{new_fm}\n---\n" + body
        file_path.write_text(new_content, encoding="utf-8")
        return True
    return False

def main():
    print("Menginjeksi metadata tags dan description pada seluruh artikel...")
    updated = 0
    for f in sorted(CONTENT_DIR.rglob("*.md")):
        if "Template" in str(f) or "TB40/" in str(f):
            continue
        if update_frontmatter(f):
            print(f"[UPDATED] {f.relative_to(CONTENT_DIR)}")
            updated += 1
            
    print(f"\nSelesai: {updated} berkas berhasil diperkaya dengan tags & description!")

if __name__ == "__main__":
    main()

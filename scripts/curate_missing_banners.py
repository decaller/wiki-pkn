#!/home/abuhafi/Project/wiki-pkn/pexels-mcp-server/.venv/bin/python3
"""
curate_missing_banners.py
Mencari, mengaudit syariat (OMP AI Vision), mengunduh, dan menyematkan banner Pexels
untuk artikel-artikel penting Wiki PKN yang saat ini belum memiliki banner.
"""

import os
import sys
import json
import re
import subprocess
import tempfile
import requests
from pathlib import Path
from PIL import Image
import io
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
PEXELS_DIR = ROOT / "pexels-mcp-server"
BANNER_DIR = ROOT / "content" / "assets" / "banners"

load_dotenv(PEXELS_DIR / ".env")
load_dotenv(ROOT / ".env")

API_KEY = os.getenv("PEXELS_API_KEY", "")
BASE_URL = "https://api.pexels.com/v1"
OMP_BIN = "/home/abuhafi/.local/bin/omp"

# Target artikel dan keyword pencarian bertema syariat/alam/arsitektur/buku
TARGET_ARTICLES = [
    {
        "file": "content/index.md",
        "query": "grand mosque architecture arches",
        "banner_name": "banner_home_gerbang.webp",
        "caption": "Gerbang Peradaban dan Pendidikan Karakter Nabawiyah"
    },
    {
        "file": "content/Master Katalog Dalil Al-Quran.md",
        "query": "quran holy book open pages",
        "banner_name": "banner_katalog_quran.webp",
        "caption": "Katalog Dalil Al-Qur'anul Karim"
    },
    {
        "file": "content/Master Katalog Dalil Hadits dan Sunnah.md",
        "query": "ancient manuscript quill inkwell",
        "banner_name": "banner_katalog_hadits.webp",
        "caption": "Katalog Sunnah dan Hadits Nabawiyah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Bersatunya Ruh dan Jasad Membentuk Jiwa.md",
        "query": "sunrise over mountains morning light rays",
        "banner_name": "banner_ruh_jasad_jiwa.webp",
        "caption": "Penyatuan Ruh dan Jasad Membentuk Hakikat Jiwa Insan"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tawakkal dan Doa.md",
        "query": "peaceful dawn serene sky nature prayer",
        "banner_name": "banner_tawakkal_doa.webp",
        "caption": "Kepasrahan Tawakkal dan Senjata Doa"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/Tazkiyatun Nafs.md",
        "query": "crystal clear stream mountain spring water",
        "banner_name": "banner_tazkiyatun_nafs.webp",
        "caption": "Penyucian Jiwa (Tazkiyatun Nafs) Menuju Kesucian Fitrah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/Kuisioner Asesmen 40 Bakat Nabawiyah.md",
        "query": "vintage brass compass map astrolabe navigation",
        "banner_name": "banner_asesmen_bakat.webp",
        "caption": "Kompas Penjelajahan 40 Potensi Bakat Nabawiyah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/PKN Blueprint Arsitektur Sistem.md",
        "query": "architectural drawing blueprint compass ruler",
        "banner_name": "banner_blueprint_arsitektur.webp",
        "caption": "Cetak Biru Arsitektur Sistem Pendidikan Karakter Nabawiyah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Dokumen Pendidikan Karakter Nabawiyah/FAQ Ringkas.md",
        "query": "classic warm lantern light illumination",
        "banner_name": "banner_faq_ringkas.webp",
        "caption": "Pelita Jawaban atas Pertanyaan Fundamental PKN"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Bank Studi Kasus.md",
        "query": "classic study desk vintage notebook glasses pen",
        "banner_name": "banner_bank_studi_kasus.webp",
        "caption": "Dokumentasi dan Analisis Komparatif Studi Kasus Pendidikan"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/8 Standar Implementasi PKN.md",
        "query": "majestic ancient stone pillars columns",
        "banner_name": "banner_8_standar_pkn.webp",
        "caption": "Pilar-pilar 8 Standar Mutu Implementasi PKN"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Elemen Implementasi.md",
        "query": "geometric islamic patterns tile mosaic",
        "banner_name": "banner_4_elemen_implementasi.webp",
        "caption": "Empat Elemen Pondasi Implementasi Pendidikan Karakter"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/4 Kaidah Implementasi.md",
        "query": "balanced stones cairn harmony nature",
        "banner_name": "banner_4_kaidah_implementasi.webp",
        "caption": "Kaidah-Kaidah Keseimbangan dalam Penerapan PKN"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Panduan RPP dan Observasi Lapangan.md",
        "query": "outdoor field notebook nature forest trail",
        "banner_name": "banner_panduan_rpp_observasi.webp",
        "caption": "Panduan Observasi Lapangan dan Perancangan Pembelajaran Fitrah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/Bahasa Tangan.md",
        "query": "artisan woodworking hands craftsmanship tools",
        "banner_name": "banner_bahasa_tangan.webp",
        "caption": "Bahasa Tangan: Teladan Amal dan Keterampilan Nyata"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md",
        "query": "calm tranquil sea horizon stillness",
        "banner_name": "banner_euforia_pengasuhan.webp",
        "caption": "Meredam Euforia Pengasuhan Menuju Kedamaian Hati yang Seimbang"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Referensi Kajian Video.md",
        "query": "vintage audio microphone studio archive",
        "banner_name": "banner_referensi_kajian_video.webp",
        "caption": "Arsip Audio Visual Rekaman Kajian dan Dauroh Ilmiah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Arahan Teknis Implementasi.md",
        "query": "mountain road winding pathway journey",
        "banner_name": "banner_arahan_teknis.webp",
        "caption": "Peta Jalan dan Panduan Teknis Pelaksanaan di Lapangan"
    },
    {
        "file": "content/Renungan/index.md",
        "query": "night starry sky milky way galaxy desert",
        "banner_name": "banner_renungan_index.webp",
        "caption": "Tafakkur Malam: Merenungi Tanda-Tanda Kebesaran Ilahi"
    }
]

ISLAMIC_AUDIT_PROMPT = """Analisis gambar ini secara sangat teliti untuk website pendidikan Islam (Wiki PKN) dengan aturan syariat ketat:

KRITERIA WAJIB:
1. TIDAK BOLEH menampilkan wanita atau anak perempuan sama sekali (dewasa maupun anak-anak).
2. TIDAK BOLEH menampilkan aurat manusia (contoh DILARANG: pria tanpa baju/shirtless, celana pendek di atas lutut, pakaian ketat/terbuka, pakaian renang).
3. TIDAK BOLEH mengandung patung makhluk bernyawa, berhala, salib, atau simbol keagamaan non-Islam.
4. GAMBAR YANG DIPERBOLEHKAN:
   - Alam semesta (langit, gunung, bintang, laut, gurun, pohon).
   - Arsitektur (masjid, kubah, menara, pilar, perpustakaan, kota).
   - Objek & alat (buku, mushaf, kaligrafi, pena, timbangan, lentera, kompas, jam, kayu tukang).
   - Pria/anak laki-laki yang berpakaian sopan menutup aurat sempurna (baju lengan, celana panjang/gamis).

Balas HANYA format JSON valid berikut tanpa teks tambahan:
{
  "compliant": true,
  "has_women_or_girls": false,
  "has_exposed_aurat": false,
  "reason": "Alasan kepatuhan atau pelanggaran singkat"
}
"""

def extract_json(text):
    text = text.strip()
    if text.startswith("Working..."):
        text = text[len("Working..."):].strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        text = match.group(1).strip()
    try:
        return json.loads(text)
    except Exception:
        first_brace = text.find("{")
        last_brace = text.rfind("}")
        if first_brace != -1 and last_brace != -1:
            try:
                return json.loads(text[first_brace:last_brace+1])
            except Exception:
                pass
    return None

def verify_image_compliance(image_bytes):
    temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    temp_file.write(image_bytes)
    temp_file.close()

    try:
        cmd = [
            OMP_BIN, "-p",
            "--model", "gemini-2.5-flash",
            ISLAMIC_AUDIT_PROMPT,
            f"@{temp_file.name}"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=40)
        if res.returncode != 0:
            return {"compliant": False, "reason": f"OMP error: {res.stderr.strip()}"}
        result = extract_json(res.stdout)
        return result or {"compliant": False, "reason": "Failed to parse vision JSON"}
    finally:
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)

def search_and_find_compliant_photo(query, count=6):
    headers = {"Authorization": API_KEY}
    params = {
        "query": query,
        "orientation": "landscape",
        "per_page": count
    }
    resp = requests.get(f"{BASE_URL}/search", headers=headers, params=params, timeout=15)
    if resp.status_code != 200:
        print(f"  [ERROR] Pexels API {resp.status_code}: {resp.text}")
        return None

    photos = resp.json().get("photos", [])
    print(f"  Ditemukan {len(photos)} kandidat foto untuk query: '{query}'")

    for photo in photos:
        pid = photo["id"]
        med_url = photo["src"]["medium"]
        large_url = photo["src"]["large2x"]

        # Download preview for quick audit
        try:
            prev_resp = requests.get(med_url, timeout=10)
            if prev_resp.status_code != 200:
                continue
            audit = verify_image_compliance(prev_resp.content)
            if audit and audit.get("compliant", False):
                print(f"  -> [PASSED AUDIT] ID {pid}: {audit.get('reason')}")
                return {
                    "id": pid,
                    "url": large_url,
                    "photographer": photo["photographer"],
                    "reason": audit.get("reason")
                }
            else:
                print(f"  -> [REJECTED] ID {pid}: {audit.get('reason') if audit else 'non-compliant'}")
        except Exception as e:
            print(f"  -> [SKIP] ID {pid} error checking: {e}")
            continue

    return None

def crop_and_save(photo_url, output_path, target_width=1050, target_height=350):
    resp = requests.get(photo_url, timeout=30)
    resp.raise_for_status()
    img = Image.open(io.BytesIO(resp.content)).convert("RGB")
    src_w, src_h = img.size
    target_ratio = target_width / target_height
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        new_w = int(src_h * target_ratio)
        offset_x = (src_w - new_w) // 2
        crop_box = (offset_x, 0, offset_x + new_w, src_h)
    else:
        new_h = int(src_w / target_ratio)
        offset_y = (src_h - new_h) // 2
        crop_box = (0, offset_y, src_w, offset_y + new_h)

    cropped = img.crop(crop_box)
    resized = cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    resized.save(output_path, "WEBP", quality=85)
    print(f"  -> [SAVED] {output_path.name}")

def inject_banner_to_file(file_path, banner_filename, caption):
    doc_path = ROOT / file_path
    if not doc_path.exists():
        print(f"  [ERROR] File not found: {file_path}")
        return

    content = doc_path.read_text(encoding="utf-8")

    # If already has banner, skip
    if "assets/banners/" in content:
        print(f"  [SKIP] Banner already present in {file_path}")
        return

    banner_md = f"\n![[assets/banners/{banner_filename}]]\n*Gambar: {caption}*\n\n"

    # Find position right after disclaimer or after frontmatter
    disclaimer_marker = "> Rangkuman materi kurikulum Pendidikan Karakter Nabawiyah"
    if disclaimer_marker in content:
        idx = content.find(disclaimer_marker)
        # find end of callout block (after next double newline or non-> line)
        end_callout = content.find("\n\n", idx)
        if end_callout != -1:
            new_content = content[:end_callout+2] + banner_md + content[end_callout+2:].lstrip()
            doc_path.write_text(new_content, encoding="utf-8")
            print(f"  -> [INJECTED] Banner disematkan di {file_path}")
            return

    # If no disclaimer found, inject after frontmatter
    fm_match = re.match(r"^---\n[\s\S]*?\n---\n", content)
    if fm_match:
        end_fm = fm_match.end()
        new_content = content[:end_fm] + "\n" + banner_md + content[end_fm:].lstrip()
        doc_path.write_text(new_content, encoding="utf-8")
        print(f"  -> [INJECTED] Banner disematkan setelah frontmatter di {file_path}")
    else:
        new_content = banner_md + content
        doc_path.write_text(new_content, encoding="utf-8")
        print(f"  -> [INJECTED] Banner disematkan di awal file {file_path}")

def main():
    print(f"Memulai kurasi banner Pexels untuk {len(TARGET_ARTICLES)} artikel tanpa gambar...")
    BANNER_DIR.mkdir(parents=True, exist_ok=True)

    success_count = 0
    for i, item in enumerate(TARGET_ARTICLES, 1):
        print(f"\n[{i}/{len(TARGET_ARTICLES)}] Memproses: {item['file']}")
        banner_path = BANNER_DIR / item["banner_name"]

        # 1. Cari & Audit foto syar'i
        photo = search_and_find_compliant_photo(item["query"])
        if not photo:
            print(f"  [GAGAL] Tidak ditemukan foto yang lolos audit syariat untuk '{item['query']}'")
            continue

        # 2. Crop & Save
        try:
            crop_and_save(photo["url"], banner_path)
        except Exception as e:
            print(f"  [ERROR] Gagal download/crop: {e}")
            continue

        # 3. Inject banner ke artikel markdown
        inject_banner_to_file(item["file"], item["banner_name"], item["caption"])
        success_count += 1

    print(f"\n" + "="*60)
    print(f"SELESAI: Berhasil mengurasi & menyematkan {success_count}/{len(TARGET_ARTICLES)} banner baru!")
    print("="*60)

if __name__ == "__main__":
    main()

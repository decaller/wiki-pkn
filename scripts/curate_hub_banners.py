#!/home/abuhafi/Project/wiki-pkn/pexels-mcp-server/.venv/bin/python3
"""
curate_hub_banners.py
Kurasi batch kedua untuk artikel SOTABH dan 16 Hub Index Wiki PKN.
Semua melalui verifikasi OMP AI Vision untuk kepatuhan syariat.
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

TARGET_HUBS = [
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight/SOTABH.md",
        "query": "astronomy telescope brass antique observatory",
        "banner_name": "banner_sotabh.webp",
        "caption": "SOTABH: Menemukan dan Mengembangkan Bakat Nabawiyah Berbasis Fitrah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/index.md",
        "query": "serene mountain sunrise light rays",
        "banner_name": "banner_hub_insan.webp",
        "caption": "Pilar Hakikat Insan: Memahami Struktur Jasad, Ruh, dan Nafs"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/index.md",
        "query": "olive tree orchard sunlight landscape",
        "banner_name": "banner_hub_fitrah.webp",
        "caption": "Fitrah Insan: Menjaga dan Membina Potensi Suci Bawaan Ilahi"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Bakat/index.md",
        "query": "craftsman artist tools woodworking workshop",
        "banner_name": "banner_hub_bakat.webp",
        "caption": "Bakat dan Keunikan Potensi Nabawiyah Setiap Anak"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/index.md",
        "query": "green seedling sprouting from rich soil",
        "banner_name": "banner_hub_perkembangan.webp",
        "caption": "Tahapan Perkembangan Fitrah Menuju Usia Baligh dan Taklif"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Pembagian Jiwa/index.md",
        "query": "calm peaceful lake water mirror reflection mist",
        "banner_name": "banner_hub_pembagian_jiwa.webp",
        "caption": "Karakteristik Jiwa: Dinamika Ammarah, Lawwamah, dan Muthmainnah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/index.md",
        "query": "ancient stone masonry arch building craft",
        "banner_name": "banner_hub_implementasi.webp",
        "caption": "Kerangka Kerja Implementasi Kurikulum Karakter Nabawiyah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Internal & Eksternal/index.md",
        "query": "courtyard fountain water ripples mosaic sunlight",
        "banner_name": "banner_hub_internal_eksternal.webp",
        "caption": "Sinergi Faktor Internal Jiwa dan Ekosistem Lingkungan Eksternal"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/index.md",
        "query": "islamic architectural geometric wood carving",
        "banner_name": "banner_hub_kaidah_elemen.webp",
        "caption": "Kaidah-Kaidah Emas dan Elemen Kunci Pembelajaran Nabawiyah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/index.md",
        "query": "father and young boy walking peaceful path trees",
        "banner_name": "banner_hub_peran_tanggung_jawab.webp",
        "caption": "Peran dan Tanggung Jawab Pengasuhan: Ayah, Ibu, dan Pendidik"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/index.md",
        "query": "historic library courtyard arches islamic madrasah",
        "banner_name": "banner_hub_pendidikan_ideal.webp",
        "caption": "Cita-Cita Pendidikan Ideal Berdasarkan Manhaj Kenabian"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Metode Mendidik/index.md",
        "query": "calligraphy pen writing on parchment ink",
        "banner_name": "banner_hub_metode_mendidik.webp",
        "caption": "Ragam Metode Mendidik Nabawiyah: Keteladanan, Lisan, dan Hikmah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/index.md",
        "query": "grand islamic archway corridor perspective daylight",
        "banner_name": "banner_hub_paradigma_implementasi.webp",
        "caption": "Sintesis Paradigma Filosofis dan Eksekusi Lapangan PKN"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/index.md",
        "query": "antique astrolabe compass vintage navigational",
        "banner_name": "banner_hub_insight_teknis.webp",
        "caption": "Panduan Teknis, Standarisasi Mutu, dan Wawasan Lapangan"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Insight & Teknis/Insight/index.md",
        "query": "mountain peak sunrise golden hour horizon",
        "banner_name": "banner_hub_insight.webp",
        "caption": "Refleksi dan Wawasan Strategis Penerapan Pendidikan Karakter"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/index.md",
        "query": "ancient leather bound books library stack",
        "banner_name": "banner_hub_dokumen_pkn.webp",
        "caption": "Korpus Dokumen Kurikulum Pendidikan Karakter Nabawiyah"
    },
    {
        "file": "content/Paradigma - Implementasi PKN/index.md",
        "query": "historic ancient city minaret dawn sunrise",
        "banner_name": "banner_hub_paradigma_root.webp",
        "caption": "Peradaban Ilmu dan Fondasi Pendidikan Karakter Generasi Gemilang"
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

    if "assets/banners/" in content:
        print(f"  [SKIP] Banner already present in {file_path}")
        return

    banner_md = f"\n![[assets/banners/{banner_filename}]]\n*Gambar: {caption}*\n\n"

    disclaimer_marker = "> Rangkuman materi kurikulum Pendidikan Karakter Nabawiyah"
    if disclaimer_marker in content:
        idx = content.find(disclaimer_marker)
        end_callout = content.find("\n\n", idx)
        if end_callout != -1:
            new_content = content[:end_callout+2] + banner_md + content[end_callout+2:].lstrip()
            doc_path.write_text(new_content, encoding="utf-8")
            print(f"  -> [INJECTED] Banner disematkan di {file_path}")
            return

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
    print(f"Memulai kurasi banner Pexels untuk {len(TARGET_HUBS)} hub/halaman navigasi...")
    BANNER_DIR.mkdir(parents=True, exist_ok=True)

    success_count = 0
    for i, item in enumerate(TARGET_HUBS, 1):
        print(f"\n[{i}/{len(TARGET_HUBS)}] Memproses: {item['file']}")
        banner_path = BANNER_DIR / item["banner_name"]

        photo = search_and_find_compliant_photo(item["query"])
        if not photo:
            print(f"  [GAGAL] Tidak ditemukan foto yang lolos audit syariat untuk '{item['query']}'")
            continue

        try:
            crop_and_save(photo["url"], banner_path)
        except Exception as e:
            print(f"  [ERROR] Gagal download/crop: {e}")
            continue

        inject_banner_to_file(item["file"], item["banner_name"], item["caption"])
        success_count += 1

    print(f"\n" + "="*60)
    print(f"SELESAI: Berhasil mengurasi & menyematkan {success_count}/{len(TARGET_HUBS)} hub banner baru!")
    print("="*60)

if __name__ == "__main__":
    main()

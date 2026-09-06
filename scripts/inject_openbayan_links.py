#!/usr/bin/env python3
"""
Milestone 49: Injeksi link pencarian OpenBayan ke seluruh dalil Wiki PKN
- Update banner metodologi: "60 kitab klasik" → "seluruh dataset Maktabah Syamilah"
- Tambahkan link pencarian OpenBayan pada setiap dalil dan kata kunci Arab
"""

import os
import re
import urllib.parse
import glob
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"
OPENBAYAN_BASE = "https://openbayan.insanmustaqbal.or.id/search"

# ─── Fase 1: Pola teks lama → baru untuk banner metodologi ───────────────────

BANNER_REPLACEMENTS = [
    # Banner metodologi utama di semua file
    (
        r'korpus \*\*OpenBayan\*\* \(60 kitab klasik\)',
        'korpus **OpenBayan** (seluruh dataset **Maktabah Syamilah**)'
    ),
    # Variasi tanpa kurung
    (
        r'dari korpus \*\*OpenBayan\*\* \(`data/shamela_corpus\.db`\)',
        'dari korpus **OpenBayan** (terintegrasi penuh dengan seluruh dataset **Maktabah Syamilah**, `data/shamela_corpus.db`)'
    ),
    # Korpus Dalil & Atsar Klasik description
    (
        r'60 kitab rujukan standar Islam klasik \(tafsir induk, hadits Kutubus Sittah beserta syarahnya, dan ensiklopedia fiqih salaf\)',
        'seluruh dataset **Maktabah Syamilah** (ribuan kitab turats Islam klasik: tafsir induk, hadits Kutubus Sittah beserta syarahnya, ensiklopedia fiqih salaf, dan khazanah ulama)'
    ),
    # Frontmatter description di Korpus Dalil
    (
        r'Indeks korpus 60 kitab turats rujukan utama rekonstruksi manhaj PKN dari basis data OpenBayan',
        'Indeks korpus dalil dan turats rujukan manhaj PKN dari basis data OpenBayan (terintegrasi penuh dengan seluruh dataset Maktabah Syamilah)'
    ),
    # Di artikel Pengembangan Software
    (
        r'Pangkalan Data TB-40 Bases dan katalog 60 kitab hadits turats OpenBayan\.',
        'Pangkalan Data TB-40 Bases dan katalog dalil turats OpenBayan (terintegrasi penuh dengan seluruh dataset Maktabah Syamilah).'
    ),
    # Di Referensi/index.md
    (
        r'Indeks 60 kitab turats \(Kutubus Sittah, tafsir mu\'tabar, kitab tarbiyah ulama klasik\) yang diverifikasi melalui korpus OpenBayan\.',
        "Indeks dalil turats (Kutubus Sittah, tafsir mu'tabar, kitab tarbiyah ulama klasik) yang diverifikasi melalui korpus OpenBayan (seluruh dataset Maktabah Syamilah)."
    ),
]

# ─── Fase 2: Helper untuk generate link OpenBayan ────────────────────────────

def make_openbayan_url(arabic_text: str) -> str:
    """Generate URL pencarian OpenBayan dari teks Arab."""
    # Bersihkan tanda baca yang tidak perlu tapi pertahankan Arab
    clean = arabic_text.strip().strip('«»').strip()
    # Ambil maksimal 60 karakter pertama untuk query yang efektif
    if len(clean) > 80:
        # Cari spasi terdekat di batas 80 karakter
        cutoff = clean[:80].rfind(' ')
        if cutoff > 30:
            clean = clean[:cutoff]
        else:
            clean = clean[:80]
    encoded = urllib.parse.quote(clean, safe='')
    return f"{OPENBAYAN_BASE}?q={encoded}&lang=id"


def make_openbayan_link(arabic_text: str, label: str = "Telusuri di OpenBayan ↗") -> str:
    """Generate teks markdown link OpenBayan."""
    url = make_openbayan_url(arabic_text)
    return f'[🔍 {label}]({url})'


# ─── Pola regex untuk mendeteksi dalil ───────────────────────────────────────

# Pola 1: Baris "Kata Kunci OpenBayan:" dengan backtick
RE_KATA_KUNCI = re.compile(
    r'(\*\*Kata Kunci OpenBayan:\*\* `([^`]+)`)',
    re.MULTILINE
)

# Pola 2: Baris "📚 **Sumber Rujukan OpenBayan:**"
RE_SUMBER = re.compile(
    r'(^(> )?📚 \*\*Sumber Rujukan OpenBayan:\*\*[^\n]+)',
    re.MULTILINE
)

# Pola 3: Teks Arab dalam « » di dalam blockquote dalil
RE_ARAB_QUOTE = re.compile(
    r'(^> «\s*([^»]+)\s*»)',
    re.MULTILINE
)

# Pola 4: Dalil utama di index.md (« ... » tanpa prefix >)
RE_ARAB_PLAIN = re.compile(
    r'(^> «\s*([^»\n]{10,})\s*»)',
    re.MULTILINE
)

# Marker untuk menghindari duplikasi
OPENBAYAN_MARKER = '🔍'
OPENBAYAN_MARKER_TEXT = 'openbayan.insanmustaqbal.or.id'


def has_openbayan_link(text_block: str) -> bool:
    """Cek apakah sudah ada link OpenBayan di blok ini."""
    return OPENBAYAN_MARKER_TEXT in text_block


# ─── Proses per-file ─────────────────────────────────────────────────────────

def process_kata_kunci(content: str) -> tuple[str, int]:
    """
    Proses pola "Kata Kunci OpenBayan:" - tambahkan link setelah baris tersebut.
    Hanya di file Master Katalog Dalil Hadits.
    """
    count = 0
    lines = content.split('\n')
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = RE_KATA_KUNCI.search(line)
        if m:
            arabic = m.group(2).strip()
            link = make_openbayan_link(arabic)
            new_lines.append(line)
            # Cek apakah baris berikutnya sudah ada link OpenBayan
            next_line = lines[i+1] if i+1 < len(lines) else ''
            if OPENBAYAN_MARKER_TEXT not in next_line:
                new_lines.append(f'🔎 **Cari di OpenBayan:** {link}')
                count += 1
        else:
            new_lines.append(line)
        i += 1
    return '\n'.join(new_lines), count


def process_sumber_rujukan(content: str) -> tuple[str, int]:
    """
    Tambahkan link OpenBayan setelah setiap baris "📚 Sumber Rujukan OpenBayan:"
    menggunakan kata kunci yang ada di baris "Kata Kunci OpenBayan:" sebelumnya.
    """
    count = 0
    lines = content.split('\n')
    new_lines = []
    i = 0
    last_arabic = ''
    
    while i < len(lines):
        line = lines[i]
        
        # Cek pola kata kunci untuk simpan referensi
        m_kw = RE_KATA_KUNCI.search(line)
        if m_kw:
            last_arabic = m_kw.group(2).strip()
        
        # Cek pola teks Arab « »
        m_arab = RE_ARAB_PLAIN.match(line)
        if m_arab:
            last_arabic = m_arab.group(2).strip()
        
        new_lines.append(line)
        
        # Deteksi baris Sumber Rujukan
        if '📚 **Sumber Rujukan OpenBayan:**' in line or '📚 **Sumber Rujukan OpenBayan**' in line:
            # Cek baris berikutnya
            next_line = lines[i+1] if i+1 < len(lines) else ''
            if OPENBAYAN_MARKER_TEXT not in line and OPENBAYAN_MARKER_TEXT not in next_line:
                if last_arabic:
                    link = make_openbayan_link(last_arabic)
                    prefix = '> ' if line.startswith('>') else ''
                    new_lines.append(f'{prefix}🔍 **Telusuri di OpenBayan:** {link}')
                    count += 1
        i += 1
    
    return '\n'.join(new_lines), count


def process_dalil_callout(content: str) -> tuple[str, int]:
    """
    Proses callout [!quote] Dalil — tambahkan link OpenBayan setelah baris Arab « ».
    Hanya jika belum ada link OpenBayan di callout yang sama.
    """
    count = 0
    # Split per callout [!quote]
    # Cari semua blok > [!quote] Dalil
    pattern_callout = re.compile(
        r'(> \[!quote\] (?:Dalil[^\n]*|Rujukan[^\n]*)(?:\n(?:>.*)?)*)',
        re.MULTILINE
    )
    
    def process_callout_block(m):
        nonlocal count
        block = m.group(0)
        if OPENBAYAN_MARKER_TEXT in block:
            return block  # Sudah ada, skip
        
        # Cari teks Arab « » dalam blok ini
        arab_match = re.search(r'«\s*([^»]{10,})\s*»', block)
        if not arab_match:
            return block
        
        arabic = arab_match.group(1).strip()
        link = make_openbayan_link(arabic)
        
        # Cari posisi setelah baris relevansi PKN atau setelah baris sumber
        # Tambahkan di akhir callout sebelum newline terakhir
        lines = block.split('\n')
        insert_idx = len(lines)
        
        # Cari posisi yang tepat — setelah baris 💡 Relevansi atau 📚 Sumber
        for j, l in enumerate(lines):
            if '💡 **Relevansi' in l or '📚 **Sumber Rujukan' in l:
                insert_idx = j + 1
        
        if insert_idx <= len(lines):
            lines.insert(insert_idx, f'> 🔍 **Telusuri di OpenBayan:** {link}')
            count += 1
        
        return '\n'.join(lines)
    
    new_content = pattern_callout.sub(process_callout_block, content)
    return new_content, count


def process_index_dalils(content: str) -> tuple[str, int]:
    """
    Khusus untuk index.md — tambahkan link OpenBayan di bawah baris HR. atau QS. referensi.
    """
    count = 0
    # Cari pola: "— **HR. ... (No. ...).**" atau "— **HR. Muslim ...**"
    pattern_hr = re.compile(
        r'(> — \*\*HR\.[^\n]+\*\*\.?(?:\n(?:> )?)?)',
        re.MULTILINE
    )
    
    lines = content.split('\n')
    new_lines = []
    i = 0
    last_arabic = ''
    
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        
        # Simpan teks Arab terbaru
        m_arab = re.search(r'«\s*([^»]{15,})\s*»', line)
        if m_arab:
            last_arabic = m_arab.group(1).strip()
        
        # Setelah baris "— **HR.**" atau "— **QS.**" referensi, tambahkan link
        if re.search(r'^> — \*\*(?:HR|QS)\..*\*\*', line) and last_arabic:
            next_line = lines[i+1] if i+1 < len(lines) else ''
            if OPENBAYAN_MARKER_TEXT not in next_line and OPENBAYAN_MARKER_TEXT not in line:
                link = make_openbayan_link(last_arabic)
                new_lines.append(f'> 🔍 **Telusuri di OpenBayan:** {link}')
                count += 1
                last_arabic = ''  # Reset setelah digunakan
        i += 1
    
    return '\n'.join(new_lines), count


# ─── Main processing ─────────────────────────────────────────────────────────

def apply_banner_replacements(content: str) -> tuple[str, int]:
    """Terapkan semua penggantian teks banner metodologi."""
    count = 0
    for pattern, replacement in BANNER_REPLACEMENTS:
        new_content, n = re.subn(pattern, replacement, content)
        if n > 0:
            content = new_content
            count += n
    return content, count


def process_file(filepath: Path) -> dict:
    """Proses satu file markdown."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    content = original
    stats = {'path': str(filepath), 'banner_updates': 0, 'link_injections': 0}
    
    # Fase 1: Update banner
    content, n = apply_banner_replacements(content)
    stats['banner_updates'] = n
    
    # Fase 2: Injeksi link OpenBayan
    filename = filepath.name
    
    # Untuk Master Katalog Dalil Hadits — proses kata kunci + sumber rujukan
    if 'Master Katalog Dalil Hadits' in filename:
        content, n1 = process_sumber_rujukan(content)
        stats['link_injections'] += n1
    
    # Untuk semua file: proses callout [!quote] Dalil
    content, n2 = process_dalil_callout(content)
    stats['link_injections'] += n2
    
    # Untuk index.md: proses dalil utama
    if filename == 'index.md' and filepath.parent == CONTENT_DIR:
        content, n3 = process_index_dalils(content)
        stats['link_injections'] += n3
    
    # Tulis hanya jika ada perubahan
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        stats['modified'] = True
    else:
        stats['modified'] = False
    
    return stats


def main():
    """Jalankan proses utama."""
    md_files = sorted(CONTENT_DIR.rglob('*.md'))
    
    total_files = 0
    total_modified = 0
    total_banners = 0
    total_links = 0
    
    print(f"📁 Scanning {len(md_files)} file Markdown di {CONTENT_DIR}...")
    print("=" * 70)
    
    for filepath in md_files:
        # Skip template files
        if 'Template' in str(filepath):
            continue
        
        stats = process_file(filepath)
        total_files += 1
        
        if stats['modified']:
            total_modified += 1
            total_banners += stats['banner_updates']
            total_links += stats['link_injections']
            rel_path = filepath.relative_to(CONTENT_DIR)
            changes = []
            if stats['banner_updates'] > 0:
                changes.append(f"🔄 {stats['banner_updates']} banner update")
            if stats['link_injections'] > 0:
                changes.append(f"🔗 {stats['link_injections']} link injeksi")
            print(f"✅ {rel_path}: {' | '.join(changes)}")
    
    print("=" * 70)
    print(f"\n📊 RINGKASAN EKSEKUSI:")
    print(f"   📂 Total file diproses : {total_files}")
    print(f"   ✏️  File dimodifikasi   : {total_modified}")
    print(f"   🔄 Total banner update : {total_banners}")
    print(f"   🔗 Total link injeksi  : {total_links}")
    
    # Verifikasi: cek apakah masih ada "60 kitab klasik"
    print("\n🔍 Verifikasi sisa '60 kitab klasik'...")
    remaining = []
    for filepath in CONTENT_DIR.rglob('*.md'):
        with open(filepath, 'r', encoding='utf-8') as f:
            c = f.read()
        if '60 kitab klasik' in c:
            remaining.append(str(filepath.relative_to(CONTENT_DIR)))
    
    if remaining:
        print(f"⚠️  Masih ada di {len(remaining)} file:")
        for r in remaining:
            print(f"   - {r}")
    else:
        print("✅ Tidak ada sisa '60 kitab klasik' — 100% berhasil diganti!")
    
    # Verifikasi: hitung total link OpenBayan
    print("\n🔍 Verifikasi link OpenBayan terinjeksi...")
    total_ob_links = 0
    for filepath in CONTENT_DIR.rglob('*.md'):
        with open(filepath, 'r', encoding='utf-8') as f:
            c = f.read()
        total_ob_links += c.count(OPENBAYAN_MARKER_TEXT)
    print(f"✅ Total link OpenBayan di seluruh wiki: {total_ob_links}")


if __name__ == '__main__':
    main()

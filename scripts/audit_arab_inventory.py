#!/usr/bin/env python3
"""Regenerate the Arabic occurrence audit; never modify content files.

Run after editors finish: python3 scripts/audit_arab_inventory.py
Existing human classifications are reused by path + normalized text, not line ID.
New quotations without an explicit source/type remain flagged for editorial review.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path
import re
import unicodedata

ARABIC = re.compile(r'[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff\ufb50-\ufdff\ufe70-\ufeff]+')
HEADING = re.compile(r'^#{1,6} ')


def normalize(text):
    text = unicodedata.normalize('NFKD', text.replace('ﷺ', '').replace('ﷻ', ''))
    letters = ''.join(c for c in text if 'ARABIC' in unicodedata.name(c, '') and unicodedata.category(c).startswith('L'))
    return letters.translate(str.maketrans('أإآٱىؤئ', 'اااايوي')).replace('ـ', '')


def classify(text, context, normalized):
    if not normalized:
        return 'simbol_shalawat'
    if re.search(r'Telusuri|search\?q=|Rujukan Tafsir OpenBayan', text):
        return 'kutipan_tafsir' if 'Rujukan Tafsir OpenBayan' in text else 'tema_pencarian'
    if '<td>' in text or '<summary>' in text:
        return 'istilah'
    if len(normalized) < 18 and not re.search(r'«|﴿', text):
        return 'istilah'
    if re.search(r'QS\.|Q\.S\.|firman Allah|Surah', context, re.I):
        return 'dalil_quran'
    if re.search(r'HR\.|hadits|hadis|Bukhari|Muslim|Tirmidzi|Nasa.i|Abu Dawud', context, re.I):
        return 'dalil_hadits'
    if re.search(r'kaidah|Qayyim|Ghazali|Khaldun|Syathibi|atsar', context, re.I):
        return 'kutipan_ulama_atsar'
    return 'baru_perlu_klasifikasi'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root
    output = root / 'sources/audit_dalil_parenting'
    target = output / '07_inventaris_arab.json'
    prior = json.loads(target.read_text()) if target.exists() else {}
    old = {(b['path'], normalize(b['arabic'])): b for b in prior.get('blocks', [])}
    blocks = []
    files = []
    texts = {}
    for path in sorted((root / 'content').rglob('*.md')):
        relative = path.relative_to(root).as_posix()
        text = path.read_text()
        texts[relative] = text
        lines = text.splitlines()
        before = len(blocks)
        index = 0
        while index < len(lines):
            if not ARABIC.search(lines[index]):
                index += 1
                continue
            end = index
            while end + 1 < len(lines) and ARABIC.search(lines[end + 1]):
                end += 1
            raw = '\n'.join(lines[index:end + 1])
            arabic = ' '.join(ARABIC.findall(raw))
            normalized = normalize(arabic)
            context_start = max(0, index - 12)
            context_end = min(len(lines), end + 19)
            context = '\n'.join(lines[context_start:context_end])
            quote_start, quote_end = index, end
            while quote_start and lines[quote_start - 1].lstrip().startswith('>'):
                quote_start -= 1
            while quote_end + 1 < len(lines) and lines[quote_end + 1].lstrip().startswith('>'):
                quote_end += 1
            quote = '\n'.join(lines[quote_start:quote_end + 1])
            previous = old.get((relative, normalized), {})
            classification = previous.get('classification') or classify(raw, context, normalized)
            fragments = [normalize(a or b) for a, b in re.findall(r'«(.*?)»|﴿(.*?)﴾', raw, re.S)]
            blocks.append({'id': f'A{len(blocks)+1:05d}', 'path': relative,
                'line_start': index + 1, 'line_end': end + 1, 'text': raw,
                'arabic': arabic, 'normalized': normalized,
                'nas_fragments': [n for n in fragments if len(n) >= 18] or [normalized],
                'heading': next((l for l in reversed(lines[:index+1]) if HEADING.match(l)), None),
                'context': context, 'source_context': context, 'context_line_start': context_start + 1,
                'ref': re.findall(r'(?:QS\.|HR\.)[^\n|]{0,140}', context),
                'ref_status': 'contextual_not_verified', 'callout': re.findall(r'\[!([A-Za-z_-]+)\]', quote),
                'links': re.findall(r'\[\[([^\]]+)\]\]', context),
                'classification': classification, 'classification_reason': previous.get('classification_reason', 'New context classification; source not authenticated.'),
                'source_page': relative.startswith('content/Dalil/'),
                'owner': previous.get('owner', 'Main'), 'existing_dalil': []})
            index = end + 1
        files.append({'path': relative, 'sha256': hashlib.sha256(text.encode()).hexdigest(), 'arabic_blocks': len(blocks)-before})
    pages = [b for b in blocks if b['source_page'] and b['classification'] not in ('istilah', 'tema_pencarian', 'simbol_shalawat')]
    non_nas = {'istilah', 'istilah_dalam_prosa', 'tema_pencarian', 'simbol_shalawat', 'sintesis_penulis'}
    for block in blocks:
        if block['classification'] not in non_nas:
            matches = {}
            for page in pages:
                if page['path'] == block['path']:
                    continue
                for nas in block['nas_fragments']:
                    for other in page['nas_fragments']:
                        if min(len(nas), len(other)) < 25:
                            continue
                        match = 'exact' if nas == other else 'contained' if nas in other or other in nas else None
                        if not match and max(len(nas), len(other))/min(len(nas), len(other)) < 1.3:
                            if difflib.SequenceMatcher(None, nas, other, autojunk=False).ratio() >= .94:
                                match = 'variant_candidate'
                        if match:
                            matches[page['path']] = {'path': page['path'], 'line': page['line_start'], 'match': match}
            block['existing_dalil'] = list(matches.values())
        linked = []
        for link in block['links']:
            name = link.split('|')[0].split('#')[0].removesuffix('.md')
            candidates = [p for p in texts if p.startswith('content/Dalil/') and (p == 'content/' + name + '.md' or Path(p).stem == name)]
            linked.extend(candidates)
        block['linked_dalil'] = sorted(set(linked))
        block['callout_gap'] = block['classification'] not in non_nas and not block['callout']
        block['target_gap'] = block['classification'] not in non_nas and not block['source_page'] and not block['linked_dalil']
        block['action'] = 'halaman_sumber_existing' if block['source_page'] else 'tidak_perlu_halaman_dalil' if block['classification'] in non_nas else 'tautkan_existing' if block['existing_dalil'] else 'tinjau_sumber_dan_target'
    grouped = defaultdict(list)
    for block in blocks:
        if block['action'] == 'tinjau_sumber_dan_target':
            grouped[block['normalized']].append(block)
    groups = []
    for key, occurrences in grouped.items():
        identity = 'M' + hashlib.sha256(key.encode()).hexdigest()[:12]
        for block in occurrences:
            block['missing_group'] = identity
        groups.append({'id': identity, 'normalized': key, 'arabic': occurrences[0]['arabic'], 'occurrences': [b['id'] for b in occurrences], 'paths': sorted({b['path'] for b in occurrences}), 'classification': sorted({b['classification'] for b in occurrences})})
    counts = {'markdown_files': len(files), 'arabic_files': sum(bool(f['arabic_blocks']) for f in files), 'arabic_blocks': len(blocks), 'classification': dict(Counter(b['classification'] for b in blocks)), 'missing_groups_exact': len(groups), 'callout_gaps': sum(b['callout_gap'] for b in blocks), 'target_gaps': sum(b['target_gap'] for b in blocks), 'new_unclassified': sum(b['classification'] == 'baru_perlu_klasifikasi' for b in blocks)}
    manifest = {'scope': 'content/**/*.md', 'snapshot': datetime.now(timezone.utc).isoformat(), 'counts': counts, 'files': files, 'blocks': blocks, 'missing_groups': groups, 'methodology': {'note': 'Fresh complete enumeration; prior classifications reused by path+normalized text. Missing groups exact only; similarity candidate mappings are not source authentication. Context refs and links may belong to adjacent quotations. No live QAF used. Final editorial review remains required.'}}
    target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    report = ['# Inventaris Arab final-state', '', 'Snapshot: ' + manifest['snapshot'], '', 'Inventaris, bukan autentikasi riwayat. Referensi/link konteks bisa milik kutipan sebelah; gap adalah kandidat editorial, bukan hasil validasi halaman.', '', '```json', json.dumps(counts, ensure_ascii=False, indent=2), '```', '', '## Seluruh blok Arab', '']
    for b in blocks:
        report.extend([f"### {b['id']} — `{b['path']}:{b['line_start']}-{b['line_end']}`", '', f"Kategori: {b['classification']}; aksi: {b['action']}; callout: {b['callout']}; target: {b['linked_dalil']}; existing nas: {b['existing_dalil']}", '', b['text'], '', '**Konteks:**', '', b['source_context'], ''])
    (output / '07_inventaris_arab.md').write_text('\n'.join(report) + '\n')
    owners = defaultdict(list)
    for block in blocks:
        if block['path'] not in owners[block['owner']]:
            owners[block['owner']].append(block['path'])
    (output / '07_pembagian_ownership.json').write_text(json.dumps({
        'snapshot': manifest['snapshot'], 'owner_files': dict(owners),
        'assignment_note': 'Routing inherited by path+normalized text; new blocks assigned Main. Not a canonical page reservation.'
    }, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(counts, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

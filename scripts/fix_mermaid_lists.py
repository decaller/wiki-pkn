#!/usr/bin/env python3
"""
fix_mermaid_lists.py
Memperbaiki error Mermaid 'Unsupported markdown: list' di Quartz.
Mermaid v10+ memicu error jika label node atau subgraph berisi sintaks list Markdown:
- '1. ', '2. ', dst. diubah menjadi '1: ', '2: ', dst.
- '- ' atau '* ' diubah menjadi '• ' (Unicode bullet)
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

def sanitize_mermaid_block(code):
    lines = code.split("\n")
    new_lines = []
    
    for line in lines:
        new_line = line
        
        # 1. Ganti <br/>- atau <br/>* dengan <br/>• 
        new_line = re.sub(r"(<br\s*\/?>)\s*[-*]\s+", r"\1• ", new_line)
        
        # 2. Ganti ["- atau [*- dengan ["• 
        new_line = re.sub(r"(\[\"|\"|\|)\s*[-*]\s+", r"\1• ", new_line)
        
        # 3. Ganti nomor list seperti ["1. atau <br/>1. atau |1. dengan 1: 
        new_line = re.sub(r"(\[\"|\"|\||<br\s*\/?>|subgraph\s+[A-Za-z0-9_]+\[\")\s*(\d+)\.\s+", r"\1\2: ", new_line)
        
        # 4. Jika ada baris yang diawali nomor list di dalam multiline label
        # misal: baris diawali "1. " atau "2. "
        new_line = re.sub(r"^(\s*)(\d+)\.\s+([A-Za-z0-9\[\(\"\'\<])", r"\1\2: \3", new_line)
        
        new_lines.append(new_line)
        
    return "\n".join(new_lines)

def fix_file(file_path):
    txt = file_path.read_text(encoding="utf-8")
    
    def replacer(match):
        original_mermaid = match.group(1)
        fixed_mermaid = sanitize_mermaid_block(original_mermaid)
        return f"```mermaid{fixed_mermaid}```"
        
    new_txt = re.sub(r"```mermaid([\s\S]*?)```", replacer, txt)
    
    if new_txt != txt:
        file_path.write_text(new_txt, encoding="utf-8")
        return True
    return False

def main():
    print("Memeriksa dan memperbaiki seluruh blok Mermaid di content/...")
    modified_files = []
    
    for f in sorted(CONTENT_DIR.rglob("*.md")):
        if fix_file(f):
            modified_files.append(f.relative_to(CONTENT_DIR))
            print(f"[FIXED] {f.relative_to(CONTENT_DIR)}")
            
    print(f"\nSelesai: {len(modified_files)} berkas berhasil diperbaiki dari error 'Unsupported markdown: list'!")

if __name__ == "__main__":
    main()

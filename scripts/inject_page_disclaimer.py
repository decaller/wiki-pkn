#!/usr/bin/env python3
"""
Script to inject official AI & Contributor methodology disclaimer banner
at the top (right below H1 heading) of all markdown articles in content/.
"""

import os
import glob

DISCLAIMER_TAG = "Catatan Metodologi & Sumber Penyusunan Dokumen"

DISCLAIMER_BLOCK = """> [!note] Catatan Metodologi & Sumber Penyusunan Dokumen
> Dokumen ini merupakan hasil rangkuman dan rekonstruksi berbantuan kecerdasan buatan (AI) dari berbagai materi presentasi, modul kurikulum, dokumen standar lembaga, dan rekaman kajian **Pendidikan Karakter Nabawiyah (PKN)** yang diampu oleh **Ustadz Abdul Kholiq**.  
> 
> Naskah ini telah melalui verifikasi dan pengayaan ulang dalil-dalil Al-Qur'an dan Hadits shahih dari korpus **OpenBayan** (60 kitab klasik), serta diperkaya dengan sintesis intisari dan masukan berharga dari kawan-kawan **Himmatul Ummah**, **Insan Taqwa / Mustaqbal**, dan **Tim SOTAB HEBAT**.
"""

def inject_disclaimer(filepath: str) -> bool:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already injected
    if DISCLAIMER_TAG in content:
        return False

    lines = content.splitlines()

    # Check for missing frontmatter
    if not content.startswith("---"):
        # Determine title from H1 or filename
        title = os.path.splitext(os.path.basename(filepath))[0]
        for l in lines:
            if l.startswith("# "):
                title = l[2:].strip()
                break
        frontmatter = f"---\ntitle: \"{title}\"\n---\n\n"
        content = frontmatter + content
        lines = content.splitlines()

    # Find H1 line
    h1_idx = -1
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            h1_idx = idx
            break

    if h1_idx != -1:
        # Insert disclaimer right after H1
        # Check if the next line is blank, adjust accordingly
        new_lines = (
            lines[:h1_idx + 1] +
            ["", DISCLAIMER_BLOCK.strip(), ""] +
            lines[h1_idx + 1:]
        )
    else:
        # If no H1, insert after frontmatter
        fm_end = -1
        if lines[0].strip() == "---":
            for idx in range(1, len(lines)):
                if lines[idx].strip() == "---":
                    fm_end = idx
                    break
        if fm_end != -1:
            new_lines = (
                lines[:fm_end + 1] +
                ["", DISCLAIMER_BLOCK.strip(), ""] +
                lines[fm_end + 1:]
            )
        else:
            new_lines = [DISCLAIMER_BLOCK.strip(), ""] + lines

    # Clean up double blank lines
    result_text = "\n".join(new_lines) + "\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(result_text)

    return True

def main():
    md_files = sorted(glob.glob("content/**/*.md", recursive=True))
    print(f"Total markdown files found: {len(md_files)}")
    
    updated_count = 0
    for fp in md_files:
        if inject_disclaimer(fp):
            updated_count += 1
            print(f"  [+] Injected disclaimer: {fp}")
        else:
            print(f"  [-] Already present: {fp}")

    print(f"\nCompleted: {updated_count}/{len(md_files)} files updated.")

if __name__ == "__main__":
    main()

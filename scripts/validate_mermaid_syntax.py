#!/usr/bin/env python3
import os
import re
import glob
from pathlib import Path

FLOW_DIR = "content_flow"

def validate_mermaid(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    
    # Check frontmatter
    if not content.startswith("---"):
        errors.append("Missing frontmatter")
        
    # Check Callout
    if "> [!info] Artikel Lengkap" not in content:
        errors.append("Missing backlink callout")

    # Extract Mermaid block
    m = re.search(r'```mermaid\s*\n(.*?)\n```', content, re.DOTALL)
    if not m:
        errors.append("Missing or malformed mermaid block")
        return errors

    mermaid_code = m.group(1).strip()
    lines = mermaid_code.split("\n")

    if not any(lines[0].startswith(prefix) for prefix in ["flowchart", "graph"]):
        errors.append(f"Mermaid does not start with flowchart/graph: '{lines[0]}'")

    subgraph_count = 0
    end_count = 0

    for idx, line in enumerate(lines):
        l = line.strip()
        if not l or l.startswith("%%"):
            continue
        if l.startswith("subgraph"):
            subgraph_count += 1
            # Check subgraph syntax
            if not re.search(r'subgraph\s+[a-zA-Z0-9_]+\["[^"]*"\]', l):
                errors.append(f"Line {idx+1}: Malformed subgraph: '{l}'")
        elif l == "end":
            end_count += 1
        
        # Check node definitions with quotes
        # Find all brackets
        # Quotes inside brackets must not be unescaped
        node_matches = re.findall(r'([a-zA-Z0-9_]+)\["([^"]*)"\]', l)
        # Check for unquoted brackets e.g. Node[Some text without quotes]
        unquoted = re.findall(r'[a-zA-Z0-9_]+\[([^"][^\]]*)\]', l)
        if unquoted:
            for u in unquoted:
                # Subgraph handled separately
                if not l.startswith("subgraph"):
                    errors.append(f"Line {idx+1}: Unquoted node label bracket: '{u}'")

    if subgraph_count != end_count:
        errors.append(f"Subgraph mismatch: {subgraph_count} subgraph vs {end_count} end")

    return errors

def main():
    files = list(Path(FLOW_DIR).rglob("*.md"))
    print(f"Memvalidasi {len(files)} berkas di '{FLOW_DIR}'...")
    
    total_errors = 0
    for f in sorted(files):
        errs = validate_mermaid(f)
        if errs:
            print(f"❌ {f.relative_to(FLOW_DIR)}:")
            for e in errs:
                print(f"   - {e}")
            total_errors += len(errs)

    if total_errors == 0:
        print(f"✅ Seluruh {len(files)} berkas valid! Tidak ditemukan error sintaks Mermaid atau struktur berkas.")
    else:
        print(f"❌ Ditemukan {total_errors} kesalahan total.")

if __name__ == "__main__":
    main()

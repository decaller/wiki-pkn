import os
import json
import re

RENAME_MAP = {
    "Paradigma Insan": "Insan",
    "Paradigma Pendidikan Ideal": "Pendidikan Ideal",
    "Paradigma Implementasi": "Implementasi"
}

# 1. Update nav_structure.json
def update_nav_node(node):
    title = node.get("title")
    if title in RENAME_MAP:
        node["title"] = RENAME_MAP[title]
    if "children" in node:
        for child in node["children"]:
            update_nav_node(child)

with open("nav_structure.json", "r") as f:
    nav_data = json.load(f)
    
for coll_val in nav_data.values():
    if "collection" in coll_val:
        if coll_val["collection"].get("name") == "Dokumen Pendidikan Karakter Nabawiyah":
            coll_val["collection"]["name"] = "Paradigma"
            
    if "structure" in coll_val:
        for node in coll_val["structure"]:
            update_nav_node(node)

with open("nav_structure.json", "w") as f:
    json.dump(nav_data, f, indent=2)

# 2. Rename files and directories
paths_to_rename = []
for root, dirs, files in os.walk("content"):
    for d in dirs:
        if d in RENAME_MAP:
            paths_to_rename.append(os.path.join(root, d))
    for f in files:
        if f.endswith(".md"):
            name = f[:-3]
            if name in RENAME_MAP:
                paths_to_rename.append(os.path.join(root, f))

# Sort by length descending to rename deepest first
paths_to_rename.sort(key=len, reverse=True)

for path in paths_to_rename:
    dir_name = os.path.dirname(path)
    base_name = os.path.basename(path)
    if base_name.endswith(".md"):
        new_name = RENAME_MAP[base_name[:-3]] + ".md"
    else:
        new_name = RENAME_MAP[base_name]
    new_path = os.path.join(dir_name, new_name)
    print(f"Renaming {path} to {new_path}")
    os.rename(path, new_path)

# 3. Update file contents (frontmatter and links)
for root, dirs, files in os.walk("content"):
    for f in files:
        if f.endswith(".md"):
            filepath = os.path.join(root, f)
            with open(filepath, "r") as file:
                content = file.read()
            
            new_content = content
            for old_name, new_name in RENAME_MAP.items():
                # Replace frontmatter title
                new_content = re.sub(rf'^title:\s*"{old_name}"', f'title: "{new_name}"', new_content, flags=re.MULTILINE)
                new_content = re.sub(rf"^title:\s*{old_name}$", f"title: {new_name}", new_content, flags=re.MULTILINE)
                
                # Replace wiki links
                new_content = new_content.replace(f"[[{old_name}]]", f"[[{new_name}]]")
                new_content = new_content.replace(f"[[{old_name}|", f"[[{new_name}|")
                
            if new_content != content:
                with open(filepath, "w") as file:
                    file.write(new_content)
                print(f"Updated content in {filepath}")

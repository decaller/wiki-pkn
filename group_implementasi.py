import os
import json

GROUPS = {
    "Kaidah & Elemen": ["4 Kaidah Implementasi", "4 Elemen Implementasi"],
    "Internal & Eksternal": ["Tazkiyatun Nafs", "Tawakkal dan Doa"],
    "Peran & Tanggung Jawab": ["Tanggung Jawab Pendidikan", "Peran Ayah dan Bunda", "Peran Guru dan Lembaga Pendidikan"]
}

# 1. Update nav_structure.json
def group_implementasi(node):
    if node.get("title") == "Implementasi":
        old_children = node.get("children", [])
        new_children = []
        
        # Helper to find a child by title
        def find_child(title):
            for c in old_children:
                if c.get("title") == title:
                    return c
            return None
        
        for group_name, child_titles in GROUPS.items():
            group_node = {
                "title": group_name,
                "icon": "tools",
                "children": []
            }
            for title in child_titles:
                child = find_child(title)
                if child:
                    group_node["children"].append(child)
            new_children.append(group_node)
            
        node["children"] = new_children
        return True
    
    if "children" in node:
        for child in node["children"]:
            if group_implementasi(child):
                return True
    return False

with open("nav_structure.json", "r") as f:
    nav_data = json.load(f)
    
for coll_val in nav_data.values():
    if "structure" in coll_val:
        for node in coll_val["structure"]:
            if group_implementasi(node):
                break

with open("nav_structure.json", "w") as f:
    json.dump(nav_data, f, indent=2)

# 2. Move files in file system
import glob

# Find the Implementasi directory
impl_dirs = glob.glob("content/**/Implementasi", recursive=True)
if not impl_dirs:
    print("Implementasi directory not found!")
    exit(1)

impl_dir = impl_dirs[0]

for group_name, child_titles in GROUPS.items():
    group_dir = os.path.join(impl_dir, group_name)
    os.makedirs(group_dir, exist_ok=True)
    
    for title in child_titles:
        old_path = os.path.join(impl_dir, f"{title}.md")
        new_path = os.path.join(group_dir, f"{title}.md")
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Moved {old_path} to {new_path}")
        else:
            print(f"Warning: {old_path} not found")


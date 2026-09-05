import glob
import re
import os
import json
import hashlib
from collections import defaultdict, deque

CONTENT_DIR = "content"
CANVAS_DIR = os.path.join(CONTENT_DIR, "canvas")

def sanitize_filename(name):
    # Remove HTML tags
    name = re.sub(r'<[^>]+>', '', name)
    # Replace invalid filename characters
    name = re.sub(r'[\\/:*?"<>|]', ' - ', name)
    # Remove leading numbering like "## 1. ", "1: "
    name = re.sub(r'^[#\s\d\.\-\:]+', '', name)
    # Collapse multiple spaces and dashes
    name = re.sub(r'\s*-\s*', ' - ', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip(" -")

def clean_label(text):
    if not text:
        return ""
    text = text.strip()
    if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
        text = text[1:-1]
    # Replace <br/>, <br>, <br /> with \n
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    # Decode entities
    text = text.replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    return text.strip()

def estimate_node_size(text, shape='['):
    lines = text.split('\n')
    line_count = len(lines)
    max_line_len = max([len(l) for l in lines]) if lines else 10
    
    width = max(240, min(420, max_line_len * 9 + 40))
    if shape in ('{', '{{'):
        width = max(260, width)
        
    height = max(80, min(360, line_count * 26 + 36))
    return int(width), int(height)

def determine_color(label, shape, rank_val):
    lbl_lower = label.lower()
    if shape in ('{', '{{') or '?' in label or 'apakah' in lbl_lower:
        return "3" # yellow (decision)
    if any(k in lbl_lower for k in ['rusak', 'salah', 'bahaya', 'batal', 'penyimpangan', 'gagal', 'noda', 'negatif', 'hambatan']):
        return "1" # red (problem/warning)
    if any(k in lbl_lower for k in ['solusi', 'tujuan', 'sholih', 'muslih', 'sukses', 'fitrah', 'shahih', 'tuntas', 'hasil', 'output']):
        return "4" # green (solution/goal)
    if any(k in lbl_lower for k in ['fondasi', 'wahyu', 'allah', 'rasulullah', 'iman', 'akar', 'sumber', 'tauhid']):
        return "5" # blue (foundation)
        
    palette = ["5", "2", "6", "4", "3"]
    return palette[rank_val % len(palette)]

def parse_graph_flowchart(lines):
    direction = 'TD'
    parts = lines[0].split()
    if len(parts) > 1:
        direction = parts[1].upper()
        if direction not in ('TD', 'TB', 'LR', 'RL'):
            direction = 'TD'
    
    nodes = {}
    edges = []
    subgraphs = {}
    current_subgraph = None
    
    node_def_pattern = re.compile(
        r'([a-zA-Z0-9_–\-]+)\s*(\(\(\[?|\[\/?|\[\\?|\(\[?|\{\{?|\()(?:"([^"]*)"|\'([^\']*)\'|([^()\[\]{}]+))(\]\/?|\]\\?|\)\)?|\}\)?|\))'
    )

    for line in lines[1:]:
        line = line.strip()
        if not line or line.startswith('%%') or line.startswith('classDef') or line.startswith('class ') or line.startswith('style '):
            continue
        if line.startswith('direction '):
            continue
            
        if line.startswith('subgraph '):
            sg_rest = line[len('subgraph '):].strip()
            sg_m = re.match(r'([a-zA-Z0-9_–\-]+)\s*(?:\["([^"]*)"\]|\[([^\]]*)\]|\("([^"]*)"\)|\(([^)]*)\))?', sg_rest)
            if sg_m:
                sg_id = sg_m.group(1)
                sg_title = sg_m.group(2) or sg_m.group(3) or sg_m.group(4) or sg_m.group(5) or sg_id
                current_subgraph = sg_id
                subgraphs[sg_id] = {'title': clean_label(sg_title), 'nodes': set()}
            else:
                sg_id = sg_rest.replace('"', '').replace('[', '').replace(']', '')
                current_subgraph = sg_id
                subgraphs[sg_id] = {'title': sg_id, 'nodes': set()}
            continue
            
        if line == 'end':
            current_subgraph = None
            continue
            
        # Parse node definitions in this line
        for nm in node_def_pattern.finditer(line):
            nid = nm.group(1)
            nlabel = nm.group(3) or nm.group(4) or nm.group(5) or nid
            nshape = nm.group(2)
            nodes[nid] = {
                'label': clean_label(nlabel),
                'shape': nshape,
                'subgraph': current_subgraph
            }
            if current_subgraph and current_subgraph in subgraphs:
                subgraphs[current_subgraph]['nodes'].add(nid)
                
        # Parse edges
        tokens = re.split(r'(\s*(?:-->|==>|-\.->|---|==|--)\s*(?:\|[^|]*\|)?\s*)', line)
        if len(tokens) >= 3:
            for i in range(0, len(tokens) - 2, 2):
                src_raw = tokens[i].strip()
                arrow_raw = tokens[i+1].strip()
                tgt_raw = tokens[i+2].strip()
                
                edge_label = ""
                edge_style = "solid"
                if '-.-' in arrow_raw or '-.' in arrow_raw:
                    edge_style = "dotted"
                elif '==' in arrow_raw:
                    edge_style = "thick"
                    
                lbl_m = re.search(r'\|([^|]*)\|', arrow_raw)
                if lbl_m:
                    edge_label = clean_label(lbl_m.group(1))
                else:
                    lbl_m2 = re.search(r'(?:--|==|-\.)\s*(.*?)\s*(?:-->|==>|\.->)', arrow_raw)
                    if lbl_m2 and lbl_m2.group(1):
                        edge_label = clean_label(lbl_m2.group(1))
                        
                src_parts = [s.strip() for s in src_raw.split('&')]
                tgt_parts = [t.strip() for t in tgt_raw.split('&')]
                
                for s in src_parts:
                    s_id = s
                    sm = node_def_pattern.match(s)
                    if sm:
                        s_id = sm.group(1)
                        nodes[s_id] = {'label': clean_label(sm.group(3) or sm.group(4) or sm.group(5) or s_id), 'shape': sm.group(2), 'subgraph': current_subgraph}
                    elif s not in nodes and s not in subgraphs and re.match(r'^[a-zA-Z0-9_–\-]+$', s):
                        nodes[s] = {'label': s, 'shape': '[', 'subgraph': current_subgraph}
                        
                    if current_subgraph and current_subgraph in subgraphs and s_id in nodes:
                        subgraphs[current_subgraph]['nodes'].add(s_id)
                        
                    for t in tgt_parts:
                        t_id = t
                        tm = node_def_pattern.match(t)
                        if tm:
                            t_id = tm.group(1)
                            nodes[t_id] = {'label': clean_label(tm.group(3) or tm.group(4) or tm.group(5) or t_id), 'shape': tm.group(2), 'subgraph': current_subgraph}
                        elif t not in nodes and t not in subgraphs and re.match(r'^[a-zA-Z0-9_–\-]+$', t):
                            nodes[t] = {'label': t, 'shape': '[', 'subgraph': current_subgraph}
                            
                        if current_subgraph and current_subgraph in subgraphs and t_id in nodes:
                            subgraphs[current_subgraph]['nodes'].add(t_id)
                            
                        if s_id and t_id and s_id != t_id:
                            edges.append((s_id, t_id, edge_label, edge_style))
                            
    return {
        'type': 'graph',
        'direction': direction,
        'nodes': nodes,
        'edges': edges,
        'subgraphs': subgraphs
    }

def parse_mindmap(lines):
    nodes = {}
    edges = []
    stack = []
    
    node_id_counter = 0
    for line in lines[1:]:
        if not line.strip() or line.strip().startswith('%%'):
            continue
        indent = len(line) - len(line.lstrip())
        raw_text = line.strip()
        
        m = re.match(r'(?:root)?\s*(\(\(?|\[\[?|\{\{?)?(.*?)(?:\)\)?|\]\]?|\}\}?)?$', raw_text)
        label = raw_text
        if m:
            label = m.group(2) if m.group(2) else raw_text
            label = re.sub(r'^[(\[{]+|[)\]}]+$', '', label).strip()
            
        node_id_counter += 1
        curr_id = f"m_{node_id_counter}"
        nodes[curr_id] = {'label': clean_label(label), 'shape': '(', 'subgraph': None}
        
        while stack and stack[-1][0] >= indent:
            stack.pop()
            
        if stack:
            parent_id = stack[-1][1]
            edges.append((parent_id, curr_id, "", "solid"))
            
        stack.append((indent, curr_id))
        
    return {
        'type': 'mindmap',
        'direction': 'LR',
        'nodes': nodes,
        'edges': edges,
        'subgraphs': {}
    }

def parse_timeline(lines):
    nodes = {}
    edges = []
    title = "Timeline"
    periods = []
    current_period = None
    
    for line in lines[1:]:
        sline = line.strip()
        if not sline or sline.startswith('%%'):
            continue
        if sline.startswith('title '):
            title = clean_label(sline[6:])
            continue
        if ':' in sline:
            parts = [p.strip() for p in sline.split(':')]
            period_name = parts[0]
            events = [p for p in parts[1:] if p]
            if period_name:
                current_period = period_name
                periods.append({'period': period_name, 'events': events})
            elif current_period and periods:
                periods[-1]['events'].extend(events)
        elif current_period and periods:
            periods[-1]['events'].append(sline)
            
    prev_id = None
    for idx, p in enumerate(periods):
        p_id = f"time_{idx}"
        events_md = "\n".join([f"• {e}" for e in p['events']])
        label = f"### ⏳ {p['period']}\n\n{events_md}"
        nodes[p_id] = {'label': label, 'shape': '[', 'subgraph': None}
        if prev_id:
            edges.append((prev_id, p_id, "Lanjut", "solid"))
        prev_id = p_id
        
    return {
        'type': 'timeline',
        'title': title,
        'direction': 'LR',
        'nodes': nodes,
        'edges': edges,
        'subgraphs': {}
    }

def build_canvas_json(parsed):
    direction = parsed.get('direction', 'TD')
    nodes = parsed['nodes']
    edges = parsed['edges']
    subgraphs = parsed.get('subgraphs', {})
    
    # Identify which nodes belong to subgraphs
    node_to_sg = {}
    for sg_id, sg_info in subgraphs.items():
        for nid in sg_info['nodes']:
            node_to_sg[nid] = sg_id

    # Filter out subgraph IDs from individual nodes if they were added as nodes
    filtered_nodes = {nid: ninfo for nid, ninfo in nodes.items() if nid not in subgraphs}
    
    # Compute DAG layout
    all_elements = set(filtered_nodes.keys()) | set(subgraphs.keys())
    adj = defaultdict(set)
    in_degree = {elem: 0 for elem in all_elements}
    
    for src, tgt, _, _ in edges:
        if src in all_elements and tgt in all_elements:
            adj[src].add(tgt)
            in_degree[tgt] += 1
            
    roots = [elem for elem, deg in in_degree.items() if deg == 0]
    if not roots and all_elements:
        roots = [list(all_elements)[0]]
        
    rank = {}
    queue = deque([(r, 0) for r in roots])
    for r in roots:
        rank[r] = 0
        
    max_iter = len(all_elements) * 10
    iters = 0
    while queue and iters < max_iter:
        iters += 1
        curr, curr_rank = queue.popleft()
        for nxt in adj[curr]:
            if nxt not in rank or rank[nxt] < curr_rank + 1:
                rank[nxt] = curr_rank + 1
                queue.append((nxt, curr_rank + 1))
                
    for elem in all_elements:
        if elem not in rank:
            rank[elem] = 0
            
    for nid, sg_id in node_to_sg.items():
        if sg_id in rank and nid in filtered_nodes:
            sg_rank = rank[sg_id]
            if rank[nid] == 0:
                rank[nid] = sg_rank
            else:
                rank[nid] = max(rank[nid], sg_rank)

    rank_groups = defaultdict(list)
    for nid in filtered_nodes:
        r = rank.get(nid, 0)
        rank_groups[r].append(nid)
        
    sorted_ranks = sorted(rank_groups.keys())
    node_coords = {}
    
    COL_GAP = 70
    ROW_GAP = 90
    
    if direction in ('TD', 'TB'):
        current_y = 0
        for r in sorted_ranks:
            group = rank_groups[r]
            group.sort(key=lambda n: node_to_sg.get(n, ""))
            sizes = [estimate_node_size(filtered_nodes[nid]['label'], filtered_nodes[nid]['shape']) for nid in group]
            max_h = max([h for _, h in sizes]) if sizes else 80
            total_w = sum([w for w, _ in sizes]) + (len(group) - 1) * COL_GAP
            
            start_x = -total_w / 2
            curr_x = start_x
            for nid, (w, h) in zip(group, sizes):
                y_offset = (max_h - h) / 2
                node_coords[nid] = (int(curr_x), int(current_y + y_offset), w, h)
                curr_x += w + COL_GAP
                
            current_y += max_h + ROW_GAP
    else: # LR or RL
        current_x = 0
        for r in sorted_ranks:
            group = rank_groups[r]
            group.sort(key=lambda n: node_to_sg.get(n, ""))
            sizes = [estimate_node_size(filtered_nodes[nid]['label'], filtered_nodes[nid]['shape']) for nid in group]
            max_w = max([w for w, _ in sizes]) if sizes else 260
            total_h = sum([h for _, h in sizes]) + (len(group) - 1) * ROW_GAP
            
            start_y = -total_h / 2
            curr_y = start_y
            for nid, (w, h) in zip(group, sizes):
                x_offset = (max_w - w) / 2
                node_coords[nid] = (int(current_x + x_offset), int(curr_y), w, h)
                curr_y += h + ROW_GAP
                
            current_x += max_w + COL_GAP

    # Assemble JSON Canvas nodes
    nodes_json = []
    edges_json = []
    
    # 1. Subgraph Groups
    subgraph_coords = {}
    for sg_id, sg_info in subgraphs.items():
        sg_nodes = [nid for nid in sg_info['nodes'] if nid in node_coords]
        if sg_nodes:
            min_x = min(node_coords[n][0] for n in sg_nodes) - 30
            min_y = min(node_coords[n][1] for n in sg_nodes) - 50
            max_x = max(node_coords[n][0] + node_coords[n][2] for n in sg_nodes) + 30
            max_y = max(node_coords[n][1] + node_coords[n][3] for n in sg_nodes) + 30
            w = int(max_x - min_x)
            h = int(max_y - min_y)
            subgraph_coords[sg_id] = (int(min_x), int(min_y), w, h)
            nodes_json.append({
                "id": sg_id,
                "type": "group",
                "label": sg_info['title'],
                "x": int(min_x),
                "y": int(min_y),
                "width": w,
                "height": h,
                "color": "5"
            })

    # 2. Text Nodes
    for nid, (x, y, w, h) in node_coords.items():
        label = filtered_nodes[nid]['label']
        shape = filtered_nodes[nid]['shape']
        nodes_json.append({
            "id": nid,
            "type": "text",
            "text": label,
            "x": x,
            "y": y,
            "width": w,
            "height": h,
            "color": determine_color(label, shape, rank.get(nid, 0))
        })

    # 3. Edges with dynamic connection side
    for idx, (src, tgt, lbl, style) in enumerate(edges):
        src_pos = node_coords.get(src) or subgraph_coords.get(src)
        tgt_pos = node_coords.get(tgt) or subgraph_coords.get(tgt)
        
        if not src_pos or not tgt_pos:
            continue
            
        src_cx = src_pos[0] + src_pos[2] / 2
        src_cy = src_pos[1] + src_pos[3] / 2
        tgt_cx = tgt_pos[0] + tgt_pos[2] / 2
        tgt_cy = tgt_pos[1] + tgt_pos[3] / 2
        
        # Determine natural connection sides
        dx = tgt_cx - src_cx
        dy = tgt_cy - src_cy
        
        if abs(dy) >= abs(dx):
            from_side = "bottom" if dy >= 0 else "top"
            to_side = "top" if dy >= 0 else "bottom"
        else:
            from_side = "right" if dx >= 0 else "left"
            to_side = "left" if dx >= 0 else "right"
            
        edge_obj = {
            "id": f"e_{idx}_{src}_{tgt}",
            "fromNode": src,
            "fromSide": from_side,
            "toNode": tgt,
            "toSide": to_side
        }
        if lbl:
            edge_obj["label"] = lbl
        edges_json.append(edge_obj)

    return {
        "nodes": nodes_json,
        "edges": edges_json
    }

def main():
    os.makedirs(CANVAS_DIR, exist_ok=True)
    files = glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)
    
    total_diagrams = 0
    modified_files = 0
    used_canvas_names = set()
    conversion_map = []
    
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()
            
        matches = list(re.finditer(r'```mermaid\s*\n(.*?)\n```', content, re.DOTALL))
        if not matches:
            continue
            
        modified_files += 1
        new_content = content
        file_base = os.path.splitext(os.path.basename(fpath))[0]
        
        # If file is index.md, use folder name as prefix
        if file_base.lower() == 'index':
            parent_folder = os.path.basename(os.path.dirname(fpath))
            file_base = parent_folder if parent_folder and parent_folder != 'content' else 'Beranda'
            
        file_base = sanitize_filename(file_base)
        
        # Process in reverse order to preserve string indices during replacement
        for d_idx, m in reversed(list(enumerate(matches))):
            total_diagrams += 1
            code = m.group(1).strip()
            
            # Find preceding heading
            before_text = content[:m.start()]
            headings = re.findall(r'^(#{1,4}\s+.+)$', before_text, re.MULTILINE)
            if headings:
                heading_text = sanitize_filename(headings[-1])
            else:
                heading_text = f"Diagram {d_idx + 1}"
                
            # Build clean canvas name
            candidate_name = f"{file_base} - {heading_text}".strip()
            if candidate_name.endswith('.canvas'):
                candidate_name = candidate_name[:-7]
                
            # Truncate overly long names
            if len(candidate_name) > 80:
                candidate_name = candidate_name[:80].strip()
                
            # Ensure uniqueness
            unique_name = candidate_name
            counter = 2
            while unique_name in used_canvas_names:
                unique_name = f"{candidate_name}_{counter}"
                counter += 1
                
            used_canvas_names.add(unique_name)
            canvas_filename = f"{unique_name}.canvas"
            canvas_path = os.path.join(CANVAS_DIR, canvas_filename)
            
            # Parse diagram
            lines = [line.strip() for line in code.split('\n') if line.strip() and not line.strip().startswith('%%')]
            first_line = lines[0]
            kind = first_line.split()[0].lower()
            
            if kind in ('graph', 'flowchart'):
                parsed = parse_graph_flowchart(lines)
            elif kind == 'mindmap':
                parsed = parse_mindmap(lines)
            elif kind == 'timeline':
                parsed = parse_timeline(lines)
            else:
                parsed = parse_graph_flowchart(lines)
                
            # Build canvas json
            canvas_data = build_canvas_json(parsed)
            
            with open(canvas_path, "w", encoding="utf-8") as cfp:
                json.dump(canvas_data, cfp, indent=2, ensure_ascii=False)
                
            # Prepare clean transclusion replacement
            replacement = f"![[canvas/{canvas_filename}]]"
            
            new_content = new_content[:m.start()] + replacement + new_content[m.end():]
            conversion_map.append((fpath, canvas_filename))
            
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(new_content)
            
    print(f"Successfully converted {total_diagrams} diagrams across {modified_files} files!")
    print(f"Total .canvas files created in {CANVAS_DIR}: {len(used_canvas_names)}")

if __name__ == '__main__':
    main()

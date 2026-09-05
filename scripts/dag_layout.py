import json
import re
import math
from collections import defaultdict, deque

def estimate_node_size(text, shape='['):
    lines = text.split('\n')
    line_count = len(lines)
    max_line_len = max([len(l) for l in lines]) if lines else 10
    
    # Calculate width
    width = max(240, min(440, max_line_len * 9 + 40))
    if shape in ('{', '{{'): # diamond/decision
        width = max(260, width)
        
    # Calculate height
    height = max(80, min(360, line_count * 26 + 36))
    return int(width), int(height)

def compute_dag_layout(nodes, edges, subgraphs, direction='TD'):
    """
    Computes 2D layout for nodes, taking subgraphs and edges into account.
    """
    # Identify which nodes belong to which subgraph
    node_to_sg = {}
    for sg_id, sg_info in subgraphs.items():
        for nid in sg_info['nodes']:
            node_to_sg[nid] = sg_id

    # Construct unified graph with both nodes and subgraphs
    all_elements = set(nodes.keys()) | set(subgraphs.keys())
    
    adj = defaultdict(set)
    rev_adj = defaultdict(set)
    in_degree = {elem: 0 for elem in all_elements}
    
    for src, tgt, _, _ in edges:
        if src in all_elements and tgt in all_elements:
            adj[src].add(tgt)
            rev_adj[tgt].add(src)
            in_degree[tgt] += 1
            
    # Subgraph internal connections vs elements
    roots = [elem for elem, deg in in_degree.items() if deg == 0]
    if not roots and all_elements:
        roots = [list(all_elements)[0]]
        
    # Assign ranks
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
            
    # Propagate subgraph ranks to member nodes if member nodes don't have higher rank
    for nid, sg_id in node_to_sg.items():
        if sg_id in rank:
            sg_rank = rank[sg_id]
            # If node rank is 0, bump to sg_rank
            if rank[nid] == 0:
                rank[nid] = sg_rank
            else:
                rank[nid] = max(rank[nid], sg_rank)

    # Now group ONLY real nodes by rank (subgraphs will encompass their nodes)
    rank_groups = defaultdict(list)
    for nid in nodes:
        r = rank.get(nid, 0)
        rank_groups[r].append(nid)
        
    # Sort ranks
    sorted_ranks = sorted(rank_groups.keys())
    
    node_coords = {}
    COL_GAP = 70
    ROW_GAP = 90
    
    if direction in ('TD', 'TB'):
        current_y = 0
        for r in sorted_ranks:
            group = rank_groups[r]
            # Order group so nodes belonging to the same subgraph are adjacent
            group.sort(key=lambda n: node_to_sg.get(n, ""))
            
            sizes = [estimate_node_size(nodes[nid]['label'], nodes[nid]['shape']) for nid in group]
            max_h = max([h for _, h in sizes])
            total_w = sum([w for w, _ in sizes]) + (len(group) - 1) * COL_GAP
            
            start_x = -total_w / 2
            curr_x = start_x
            for nid, (w, h) in zip(group, sizes):
                y_offset = (max_h - h) / 2
                node_coords[nid] = (int(curr_x), int(current_y + y_offset), w, h)
                curr_x += w + COL_GAP
                
            current_y += max_h + ROW_GAP
    else: # LR
        current_x = 0
        for r in sorted_ranks:
            group = rank_groups[r]
            group.sort(key=lambda n: node_to_sg.get(n, ""))
            
            sizes = [estimate_node_size(nodes[nid]['label'], nodes[nid]['shape']) for nid in group]
            max_w = max([w for w, _ in sizes])
            total_h = sum([h for _, h in sizes]) + (len(group) - 1) * ROW_GAP
            
            start_y = -total_h / 2
            curr_y = start_y
            for nid, (w, h) in zip(group, sizes):
                x_offset = (max_w - w) / 2
                node_coords[nid] = (int(current_x + x_offset), int(curr_y), w, h)
                curr_y += h + ROW_GAP
                
            current_x += max_w + COL_GAP
            
    return node_coords, rank

def determine_color(label, shape, rank_val, total_ranks=5):
    lbl_lower = label.lower()
    if shape in ('{', '{{') or '?' in label or 'apakah' in lbl_lower:
        return "3" # yellow for decisions / questions
    if any(k in lbl_lower for k in ['rusak', 'salah', 'bahaya', 'batal', 'penyimpangan', 'gagal', 'noda', 'negatif', 'hambatan']):
        return "1" # red
    if any(k in lbl_lower for k in ['solusi', 'tujuan', 'sholih', 'muslih', 'sukses', 'fitrah', 'shahih', 'tuntas', 'hasil', 'output']):
        return "4" # green
    if any(k in lbl_lower for k in ['fondasi', 'wahyu', 'allah', 'rasulullah', 'iman', 'akar', 'sumber']):
        return "5" # blue / cyan
        
    palette = ["5", "2", "6", "4", "3"]
    return palette[rank_val % len(palette)]

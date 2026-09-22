#!/usr/bin/env python3
"""
scripts/verify_canvas_architecture.py

Automated Canvas Architecture Verification Tool for Pendidikan Karakter Nabawiyah (PKN).
Complies strictly with JSON Canvas 1.0 specification (jsoncanvas.org) and domain architecture contracts.

Executes 7 validation passes:
  - V1: Directory structure & file presence (00 through 06)
  - V2: Strict JSON parsing & well-formedness
  - V3: Node schema, types, integer coordinates, dimensions, colors
  - V4: Edge referential integrity & side/end enums
  - V5: Spatial geometry, group z-index order, containment & non-overlap
  - V6: Master hub navigation links (bidirectional 00 <-> 01..06)
  - V7: Pedagogical domain content verification & hygiene
"""

from __future__ import annotations

import argparse
import dataclasses
import json
from pathlib import Path
import re
import sys
from typing import Any, Dict, List, Optional, Set, Tuple
import xml.etree.ElementTree as ET


REQUIRED_CANVAS_FILES = [
    "00 - Master Arsitektur PKN.canvas",
    "01 - Komponen & Kurikulum PKN.canvas",
    "02 - Metode & Pendekatan Fisik-Ruh.canvas",
    "03 - Peran Pembelajaran & Model.canvas",
    "04 - Peran Pendidik & Kedisiplinan.canvas",
    "05 - Jejak Pendidik & Target.canvas",
    "06 - Implementasi & Rantai Kausalitas.canvas",
]

SUB_CANVAS_FILES = REQUIRED_CANVAS_FILES[1:]
MASTER_CANVAS_FILE = REQUIRED_CANVAS_FILES[0]

VALID_NODE_TYPES = {"text", "file", "link", "group"}
VALID_SIDES = {"top", "right", "bottom", "left"}
VALID_ENDS = {"none", "arrow"}
VALID_BG_STYLES = {"cover", "ratio", "repeat"}
COLOR_PRESETS = {"1", "2", "3", "4", "5", "6"}
HEX_COLOR_PATTERN = re.compile(r"^#(?:[0-9a-fA-F]{3}){1,2}$")
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
FORBIDDEN_PLACEHOLDERS = ["TODO", "FIXME", "TBD", "lorem ipsum", "DUMMY"]


@dataclasses.dataclass
class ValidationError:
    pass_id: str
    message: str
    canvas: Optional[str] = None
    node_id: Optional[str] = None
    edge_id: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

    def __str__(self) -> str:
        parts = [f"[{self.pass_id}]"]
        if self.canvas:
            parts.append(f"Canvas '{self.canvas}':")
        if self.node_id:
            parts.append(f"(Node {self.node_id})")
        if self.edge_id:
            parts.append(f"(Edge {self.edge_id})")
        parts.append(self.message)
        return " ".join(parts)


@dataclasses.dataclass
class ValidationPassResult:
    pass_id: str
    pass_name: str
    is_valid: bool
    errors: List[ValidationError] = dataclasses.field(default_factory=list)
    warnings: List[str] = dataclasses.field(default_factory=list)

    def add_error(
        self,
        message: str,
        canvas: Optional[str] = None,
        node_id: Optional[str] = None,
        edge_id: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.is_valid = False
        self.errors.append(
            ValidationError(
                pass_id=self.pass_id,
                message=message,
                canvas=canvas,
                node_id=node_id,
                edge_id=edge_id,
                details=details,
            )
        )

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)


class CanvasArchitectureValidator:
    """Validator implementing passes V1 through V7 for PKN Obsidian Canvases."""

    @staticmethod
    def is_strict_int(val: Any) -> bool:
        """JSON Canvas requires integer pixel offsets. Booleans are ints in Python, so exclude bool."""
        return isinstance(val, int) and not isinstance(val, bool)

    @staticmethod
    def is_valid_color(color: Any) -> bool:
        if not isinstance(color, str):
            return False
        if color in COLOR_PRESETS:
            return True
        return bool(HEX_COLOR_PATTERN.match(color))

    # -------------------------------------------------------------------------
    # PASS V1: Directory structure & file presence
    # -------------------------------------------------------------------------
    def validate_v1_files(self, dir_path: Path) -> ValidationPassResult:
        result = ValidationPassResult(
            pass_id="V1",
            pass_name="Directory Structure & File Presence",
            is_valid=True,
        )

        if not dir_path.exists():
            result.add_error(f"Canvas directory does not exist: '{dir_path}'")
            return result

        if not dir_path.is_dir():
            result.add_error(f"Path is not a directory: '{dir_path}'")
            return result

        for fname in REQUIRED_CANVAS_FILES:
            target = dir_path / fname
            if not target.exists():
                result.add_error(f"Missing required canvas file: '{fname}'", canvas=fname)
            elif not target.is_file():
                result.add_error(f"Path exists but is not a file: '{fname}'", canvas=fname)
            elif target.stat().st_size == 0:
                result.add_error(f"Canvas file is empty (0 bytes): '{fname}'", canvas=fname)

        return result

    # -------------------------------------------------------------------------
    # PASS V2: Strict JSON parsing & well-formedness
    # -------------------------------------------------------------------------
    def validate_v2_json(
        self,
        canvas_path: Optional[Path] = None,
        content: Optional[str] = None,
        canvas_name: str = "",
    ) -> Tuple[ValidationPassResult, Optional[Dict[str, Any]]]:
        name = canvas_name or (canvas_path.name if canvas_path else "unknown.canvas")
        result = ValidationPassResult(
            pass_id="V2",
            pass_name="Strict JSON Syntax & Structure",
            is_valid=True,
        )

        if content is None:
            if canvas_path is None or not canvas_path.exists():
                result.add_error(f"File not found for reading: {canvas_path}", canvas=name)
                return result, None
            try:
                content = canvas_path.read_text(encoding="utf-8")
            except Exception as e:
                result.add_error(f"Failed to read file: {e}", canvas=name)
                return result, None

        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            result.add_error(f"JSON syntax error: {e.msg} at line {e.lineno}, col {e.colno}", canvas=name)
            return result, None

        if not isinstance(data, dict):
            result.add_error(f"Root JSON element must be an object/dict, got {type(data).__name__}", canvas=name)
            return result, None

        if "nodes" not in data:
            result.add_error("Root object missing required 'nodes' array", canvas=name)
        elif not isinstance(data["nodes"], list):
            result.add_error(f"'nodes' must be an array, got {type(data['nodes']).__name__}", canvas=name)

        if "edges" not in data:
            result.add_error("Root object missing required 'edges' array", canvas=name)
        elif not isinstance(data["edges"], list):
            result.add_error(f"'edges' must be an array, got {type(data['edges']).__name__}", canvas=name)

        if result.is_valid:
            if len(data.get("nodes", [])) == 0:
                result.add_error("Canvas contains 0 nodes (canvas is empty/unbuilt)", canvas=name)

        return result, data if result.is_valid else None

    # -------------------------------------------------------------------------
    # PASS V3: Node schema & type constraints
    # -------------------------------------------------------------------------
    def validate_v3_nodes(self, nodes: List[Any], canvas_name: str = "") -> ValidationPassResult:
        result = ValidationPassResult(
            pass_id="V3",
            pass_name="Node Schema & Type Constraints",
            is_valid=True,
        )

        seen_node_ids: Set[str] = set()

        for idx, node in enumerate(nodes):
            if not isinstance(node, dict):
                result.add_error(f"Node at index {idx} is not an object/dict", canvas=canvas_name)
                continue

            node_id = node.get("id")
            if not isinstance(node_id, str) or not node_id.strip():
                result.add_error(
                    f"Node at index {idx} has invalid or missing 'id' (must be non-empty string)",
                    canvas=canvas_name,
                )
                continue

            if node_id in seen_node_ids:
                result.add_error(f"Duplicate node ID '{node_id}' detected", canvas=canvas_name, node_id=node_id)
            seen_node_ids.add(node_id)

            # Node Type
            node_type = node.get("type")
            if not isinstance(node_type, str) or node_type not in VALID_NODE_TYPES:
                result.add_error(
                    f"Invalid node type '{node_type}'. Must be one of {sorted(VALID_NODE_TYPES)}",
                    canvas=canvas_name,
                    node_id=node_id,
                )

            # Coordinates x, y
            x = node.get("x")
            y = node.get("y")
            if not self.is_strict_int(x):
                result.add_error(
                    f"Coordinate 'x' must be an integer, got {type(x).__name__} ({x})",
                    canvas=canvas_name,
                    node_id=node_id,
                )
            if not self.is_strict_int(y):
                result.add_error(
                    f"Coordinate 'y' must be an integer, got {type(y).__name__} ({y})",
                    canvas=canvas_name,
                    node_id=node_id,
                )

            # Dimensions width, height
            width = node.get("width")
            height = node.get("height")
            if not self.is_strict_int(width) or width <= 0:
                result.add_error(
                    f"Dimension 'width' must be a positive integer > 0, got {width}",
                    canvas=canvas_name,
                    node_id=node_id,
                )
            if not self.is_strict_int(height) or height <= 0:
                result.add_error(
                    f"Dimension 'height' must be a positive integer > 0, got {height}",
                    canvas=canvas_name,
                    node_id=node_id,
                )

            # Color (optional)
            if "color" in node:
                color = node["color"]
                if not self.is_valid_color(color):
                    result.add_error(
                        f"Invalid color value '{color}'. Must be string preset '1'-'6' or hex (#RGB/#RRGGBB)",
                        canvas=canvas_name,
                        node_id=node_id,
                    )

            # Type-specific payload validation
            if node_type == "text":
                text = node.get("text")
                if not isinstance(text, str):
                    result.add_error(
                        f"Text node missing required 'text' string attribute (got {type(text).__name__})",
                        canvas=canvas_name,
                        node_id=node_id,
                    )
                elif not text.strip():
                    result.add_error("Text node has empty 'text' content", canvas=canvas_name, node_id=node_id)

            elif node_type == "file":
                file_attr = node.get("file")
                if not isinstance(file_attr, str) or not file_attr.strip():
                    result.add_error(
                        "File node missing required non-empty 'file' path string",
                        canvas=canvas_name,
                        node_id=node_id,
                    )
                if "subpath" in node:
                    subpath = node.get("subpath")
                    if not isinstance(subpath, str) or not subpath.startswith("#"):
                        result.add_error(
                            f"File node 'subpath' must start with '#', got '{subpath}'",
                            canvas=canvas_name,
                            node_id=node_id,
                        )

            elif node_type == "link":
                url = node.get("url")
                if not isinstance(url, str) or not (url.startswith("http://") or url.startswith("https://")):
                    result.add_error(
                        f"Link node 'url' must be a valid HTTP/HTTPS URL string, got '{url}'",
                        canvas=canvas_name,
                        node_id=node_id,
                    )

            elif node_type == "group":
                if "label" in node and not isinstance(node.get("label"), str):
                    result.add_error(
                        f"Group node 'label' must be string, got {type(node.get('label')).__name__}",
                        canvas=canvas_name,
                        node_id=node_id,
                    )
                if "background" in node and not isinstance(node.get("background"), str):
                    result.add_error(
                        f"Group node 'background' must be string path, got {type(node.get('background')).__name__}",
                        canvas=canvas_name,
                        node_id=node_id,
                    )
                if "backgroundStyle" in node:
                    bg_style = node.get("backgroundStyle")
                    if bg_style not in VALID_BG_STYLES:
                        result.add_error(
                            f"Group 'backgroundStyle' must be one of {sorted(VALID_BG_STYLES)}, got '{bg_style}'",
                            canvas=canvas_name,
                            node_id=node_id,
                        )

        return result

    # -------------------------------------------------------------------------
    # PASS V4: Edge referential integrity & side/end enums
    # -------------------------------------------------------------------------
    def validate_v4_edges(
        self, edges: List[Any], node_ids: Set[str], canvas_name: str = ""
    ) -> ValidationPassResult:
        result = ValidationPassResult(
            pass_id="V4",
            pass_name="Edge Referential Integrity & Anchor Enums",
            is_valid=True,
        )

        seen_edge_ids: Set[str] = set()

        for idx, edge in enumerate(edges):
            if not isinstance(edge, dict):
                result.add_error(f"Edge at index {idx} is not an object/dict", canvas=canvas_name)
                continue

            edge_id = edge.get("id")
            if not isinstance(edge_id, str) or not edge_id.strip():
                result.add_error(
                    f"Edge at index {idx} has invalid or missing 'id' (must be non-empty string)",
                    canvas=canvas_name,
                )
                continue

            if edge_id in seen_edge_ids:
                result.add_error(f"Duplicate edge ID '{edge_id}' detected", canvas=canvas_name, edge_id=edge_id)
            seen_edge_ids.add(edge_id)

            # Referential integrity: fromNode & toNode
            from_node = edge.get("fromNode")
            to_node = edge.get("toNode")

            if not isinstance(from_node, str) or not from_node:
                result.add_error("Edge missing 'fromNode' string", canvas=canvas_name, edge_id=edge_id)
            elif from_node not in node_ids:
                result.add_error(
                    f"Dangling edge: 'fromNode' ID '{from_node}' does not exist in canvas nodes",
                    canvas=canvas_name,
                    edge_id=edge_id,
                )

            if not isinstance(to_node, str) or not to_node:
                result.add_error("Edge missing 'toNode' string", canvas=canvas_name, edge_id=edge_id)
            elif to_node not in node_ids:
                result.add_error(
                    f"Dangling edge: 'toNode' ID '{to_node}' does not exist in canvas nodes",
                    canvas=canvas_name,
                    edge_id=edge_id,
                )

            # Optional side anchors
            if "fromSide" in edge:
                from_side = edge.get("fromSide")
                if from_side not in VALID_SIDES:
                    result.add_error(
                        f"Invalid 'fromSide' '{from_side}'. Must be one of {sorted(VALID_SIDES)}",
                        canvas=canvas_name,
                        edge_id=edge_id,
                    )
            if "toSide" in edge:
                to_side = edge.get("toSide")
                if to_side not in VALID_SIDES:
                    result.add_error(
                        f"Invalid 'toSide' '{to_side}'. Must be one of {sorted(VALID_SIDES)}",
                        canvas=canvas_name,
                        edge_id=edge_id,
                    )

            # Optional line ends
            if "fromEnd" in edge:
                from_end = edge.get("fromEnd")
                if from_end not in VALID_ENDS:
                    result.add_error(
                        f"Invalid 'fromEnd' '{from_end}'. Must be one of {sorted(VALID_ENDS)}",
                        canvas=canvas_name,
                        edge_id=edge_id,
                    )
            if "toEnd" in edge:
                to_end = edge.get("toEnd")
                if to_end not in VALID_ENDS:
                    result.add_error(
                        f"Invalid 'toEnd' '{to_end}'. Must be one of {sorted(VALID_ENDS)}",
                        canvas=canvas_name,
                        edge_id=edge_id,
                    )

            # Optional color & label
            if "color" in edge:
                color = edge.get("color")
                if not self.is_valid_color(color):
                    result.add_error(
                        f"Invalid edge color '{color}'. Must be string preset '1'-'6' or hex",
                        canvas=canvas_name,
                        edge_id=edge_id,
                    )
            if "label" in edge and not isinstance(edge.get("label"), str):
                result.add_error(
                    f"Edge 'label' must be a string, got {type(edge.get('label')).__name__}",
                    canvas=canvas_name,
                    edge_id=edge_id,
                )

        return result

    # -------------------------------------------------------------------------
    # PASS V5: Spatial geometry, group z-index order, containment & non-overlap
    # -------------------------------------------------------------------------
    def validate_v5_geometry(self, nodes: List[Dict[str, Any]], canvas_name: str = "") -> ValidationPassResult:
        result = ValidationPassResult(
            pass_id="V5",
            pass_name="Spatial Geometry, Group Containment & Z-Index",
            is_valid=True,
        )

        valid_nodes = [
            n
            for n in nodes
            if isinstance(n, dict)
            and isinstance(n.get("id"), str)
            and self.is_strict_int(n.get("x"))
            and self.is_strict_int(n.get("y"))
            and self.is_strict_int(n.get("width"))
            and self.is_strict_int(n.get("height"))
            and n.get("width", 0) > 0
            and n.get("height", 0) > 0
        ]

        # Separate groups and regular nodes
        groups = [n for n in valid_nodes if n.get("type") == "group"]
        non_groups = [n for n in valid_nodes if n.get("type") != "group"]
        node_indices = {n["id"]: idx for idx, n in enumerate(valid_nodes)}

        # Helper: bounding box containment check
        def is_center_inside(child: Dict[str, Any], group: Dict[str, Any]) -> bool:
            cx = child["x"] + child["width"] / 2.0
            cy = child["y"] + child["height"] / 2.0
            gx1, gy1 = group["x"], group["y"]
            gx2, gy2 = gx1 + group["width"], gy1 + group["height"]
            return gx1 <= cx <= gx2 and gy1 <= cy <= gy2

        # 1. Group Containment & Z-Index Check
        # A node belongs to the smallest enclosing group whose bounding box covers its center
        node_group_assignment: Dict[str, Optional[str]] = {}

        for node in non_groups:
            node_id = node["id"]
            enclosing_groups: List[Dict[str, Any]] = []
            for g in groups:
                if is_center_inside(node, g):
                    enclosing_groups.append(g)

            if enclosing_groups:
                # Pick smallest area group if nested
                enclosing_groups.sort(key=lambda g: g["width"] * g["height"])
                assigned_group = enclosing_groups[0]
                node_group_assignment[node_id] = assigned_group["id"]

                # Check Z-Index order: Group MUST appear before enclosed child
                g_idx = node_indices[assigned_group["id"]]
                n_idx = node_indices[node_id]
                if g_idx > n_idx:
                    result.add_error(
                        f"Z-Index violation: Enclosing group '{assigned_group['id']}' (index {g_idx}) "
                        f"is defined AFTER child node '{node_id}' (index {n_idx}). "
                        f"Groups must precede member nodes in 'nodes' array.",
                        canvas=canvas_name,
                        node_id=node_id,
                    )

                # Check bounding box overflow: child must fit inside group with 10px safety margin
                tolerance = 10
                gx1, gy1 = assigned_group["x"], assigned_group["y"]
                gx2, gy2 = gx1 + assigned_group["width"], gy1 + assigned_group["height"]
                nx1, ny1 = node["x"], node["y"]
                nx2, ny2 = nx1 + node["width"], ny1 + node["height"]

                if (
                    nx1 < gx1 - tolerance
                    or ny1 < gy1 - tolerance
                    or nx2 > gx2 + tolerance
                    or ny2 > gy2 + tolerance
                ):
                    result.add_error(
                        f"Group bounding box overflow: Node '{node_id}' [x:{nx1}..{nx2}, y:{ny1}..{ny2}] "
                        f"exceeds group '{assigned_group['id']}' boundaries [x:{gx1}..{gx2}, y:{gy1}..{gy2}]",
                        canvas=canvas_name,
                        node_id=node_id,
                    )
            else:
                node_group_assignment[node_id] = None

        # 2. Non-overlap / Collision Check between sibling non-group cards
        # Only compare pairs belonging to the same container (same group or both root)
        for i in range(len(non_groups)):
            for j in range(i + 1, len(non_groups)):
                n1 = non_groups[i]
                n2 = non_groups[j]

                # Check if they share the same container
                if node_group_assignment.get(n1["id"]) != node_group_assignment.get(n2["id"]):
                    continue

                x1, y1, w1, h1 = n1["x"], n1["y"], n1["width"], n1["height"]
                x2, y2, w2, h2 = n2["x"], n2["y"], n2["width"], n2["height"]

                # Overlap calculation
                overlap_x = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
                overlap_y = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
                overlap_area = overlap_x * overlap_y

                if overlap_area > 0:
                    area1 = w1 * h1
                    area2 = w2 * h2
                    union_area = area1 + area2 - overlap_area
                    iou = overlap_area / union_area if union_area > 0 else 0.0

                    # Tolerance: IoU > 0.05 is a collision error
                    if iou > 0.05:
                        result.add_error(
                            f"Spatial collision: Node '{n1['id']}' and Node '{n2['id']}' overlap significantly "
                            f"(IoU: {iou:.3f}, Overlap Area: {overlap_area}px^2). Nodes must have clean spacing.",
                            canvas=canvas_name,
                            node_id=n1["id"],
                            details={"conflicting_node": n2["id"], "iou": iou},
                        )

        return result

    # -------------------------------------------------------------------------
    # PASS V6: Master hub navigation links (bidirectional 00 <-> 01..06)
    # -------------------------------------------------------------------------
    def validate_v6_navigation(
        self, canvases_data: Dict[str, Dict[str, Any]], dir_path: Optional[Path] = None
    ) -> ValidationPassResult:
        result = ValidationPassResult(
            pass_id="V6",
            pass_name="Master Hub Bidirectional Navigation Links",
            is_valid=True,
        )

        if MASTER_CANVAS_FILE not in canvases_data:
            result.add_error(f"Master Hub '{MASTER_CANVAS_FILE}' missing from canvas collection")
            return result

        master_data = canvases_data[MASTER_CANVAS_FILE]
        master_text_content = ""
        master_files: Set[str] = set()

        for node in master_data.get("nodes", []):
            if node.get("type") == "text" and isinstance(node.get("text"), str):
                master_text_content += "\n" + node.get("text", "")
            elif node.get("type") == "file" and isinstance(node.get("file"), str):
                master_files.add(node.get("file", ""))

        # Check forward links from Master Hub to all 6 sub-canvases
        for sub_name in SUB_CANVAS_FILES:
            base_sub_name = sub_name.replace(".canvas", "")
            # Subcanvas referenced via wikilink [[...]] or file node
            has_wikilink = bool(
                re.search(re.escape(sub_name), master_text_content)
                or re.search(re.escape(base_sub_name), master_text_content)
            )
            has_file_ref = any(sub_name in f or base_sub_name in f for f in master_files)

            if not (has_wikilink or has_file_ref):
                result.add_error(
                    f"Master Hub '{MASTER_CANVAS_FILE}' missing outgoing navigation link to '{sub_name}'",
                    canvas=MASTER_CANVAS_FILE,
                )

        # Check reverse back-links from each sub-canvas to Master Hub
        for sub_name in SUB_CANVAS_FILES:
            if sub_name not in canvases_data:
                continue  # V1 already reports missing file
            sub_data = canvases_data[sub_name]
            sub_text_content = ""
            sub_files: Set[str] = set()

            for node in sub_data.get("nodes", []):
                if node.get("type") == "text" and isinstance(node.get("text"), str):
                    sub_text_content += "\n" + node.get("text", "")
                elif node.get("type") == "file" and isinstance(node.get("file"), str):
                    sub_files.add(node.get("file", ""))

            master_base = MASTER_CANVAS_FILE.replace(".canvas", "")
            has_backlink = bool(
                re.search(re.escape(MASTER_CANVAS_FILE), sub_text_content)
                or re.search(re.escape(master_base), sub_text_content)
            )
            has_file_backlink = any(MASTER_CANVAS_FILE in f or master_base in f for f in sub_files)

            if not (has_backlink or has_file_backlink):
                result.add_error(
                    f"Sub-canvas '{sub_name}' missing return navigation link to Master Hub '{MASTER_CANVAS_FILE}'",
                    canvas=sub_name,
                )

        # Optional filesystem link resolution check
        if dir_path and dir_path.exists():
            for c_name, c_data in canvases_data.items():
                for node in c_data.get("nodes", []):
                    if node.get("type") == "file" and isinstance(node.get("file"), str):
                        target_file = node["file"]
                        # Resolve relative to dir_path or project root
                        resolved_path = (dir_path / target_file).resolve()
                        root_path = (dir_path.parent.parent.parent / target_file).resolve()
                        if not (resolved_path.exists() or root_path.exists()):
                            result.add_warning(
                                f"File node in '{c_name}' references unresolved file path: '{target_file}'"
                            )

        return result

    # -------------------------------------------------------------------------
    # PASS V7: Pedagogical domain content verification & hygiene
    # -------------------------------------------------------------------------
    def validate_v7_domain_content(self, canvas_name: str, canvas_data: Dict[str, Any]) -> ValidationPassResult:
        result = ValidationPassResult(
            pass_id="V7",
            pass_name="Pedagogical Domain Semantics & Hygiene",
            is_valid=True,
        )

        all_text = ""
        node_colors: Set[str] = set()
        has_svg_or_table = False

        for node in canvas_data.get("nodes", []):
            if isinstance(node, dict):
                node_id = node.get("id", "")
                if isinstance(node.get("text"), str):
                    t = node["text"]
                    all_text += "\n" + t
                    if "<svg" in t or ("|" in t and "---" in t):
                        has_svg_or_table = True

                    # Strict inline SVG XML validation
                    if "<svg" in t:
                        svg_blocks = re.findall(r"(<svg[\s\S]*?</svg>)", t)
                        open_count = len(re.findall(r"<svg\b", t))
                        if len(svg_blocks) < open_count:
                            result.add_error(
                                f"Node '{node_id}' contains unmatched or unclosed '<svg' tag",
                                canvas=canvas_name,
                                node_id=node_id,
                            )
                        for svg_str in svg_blocks:
                            try:
                                ET.fromstring(svg_str)
                            except ET.ParseError as err:
                                result.add_error(
                                    f"Node '{node_id}' contains malformed inline SVG XML: {err}",
                                    canvas=canvas_name,
                                    node_id=node_id,
                                )
                if isinstance(node.get("label"), str):
                    all_text += "\n" + node["label"]
                if "color" in node and isinstance(node["color"], str):
                    node_colors.add(node["color"])

        for edge in canvas_data.get("edges", []):
            if isinstance(edge, dict) and isinstance(edge.get("label"), str):
                all_text += "\n" + edge["label"]

        # 1. Content Hygiene Check: Forbidden placeholder strings
        for placeholder in FORBIDDEN_PLACEHOLDERS:
            # Word boundary regex for placeholder
            pattern = re.compile(rf"\b{re.escape(placeholder)}\b", re.IGNORECASE)
            if pattern.search(all_text):
                result.add_error(
                    f"Forbidden placeholder token '{placeholder}' found in canvas content",
                    canvas=canvas_name,
                )

        # 2. Sector-specific semantic requirements
        lower_text = all_text.lower()

        if "00 - Master" in canvas_name:
            # Macro formula and hub structure
            if not ("amal" in lower_text and "ilmu" in lower_text and "iman" in lower_text):
                result.add_error(
                    "Master Hub missing core pedagogical formula: 'Amal << Ilmu << Iman'",
                    canvas=canvas_name,
                )

        elif "01 - Komponen" in canvas_name:
            # 5 Sumber & 5 Pilar
            sources = ["qur'an", "sunnah", "sirah", "salaf"]
            missing_sources = [s for s in sources if s not in lower_text and s.replace("'", "") not in lower_text]
            if missing_sources:
                result.add_error(
                    f"Sektor 01 missing authoritative sources: {missing_sources}",
                    canvas=canvas_name,
                )

            pillars = ["aqidah", "ibadah", "akhlaq", "muamalah", "dakwah"]
            missing_pillars = [p for p in pillars if p not in lower_text]
            if missing_pillars:
                result.add_error(
                    f"Sektor 01 missing core component pillars: {missing_pillars}",
                    canvas=canvas_name,
                )

            if "stem" not in lower_text and "adab" not in lower_text:
                result.add_error(
                    "Sektor 01 missing Kurikulum Maqashid progression ('Adab' -> 'STEM')",
                    canvas=canvas_name,
                )

        elif "02 - Metode" in canvas_name:
            # Tripartit hierarchy & luaran
            hierarchy = ["jasad", "ruh"]
            missing_h = [h for h in hierarchy if h not in lower_text]
            if missing_h:
                result.add_error(
                    f"Sektor 02 missing Insan hierarchy components: {missing_h}",
                    canvas=canvas_name,
                )

            outcomes = ["akhlaq", "adab", "ilmu", "amal"]
            missing_o = [o for o in outcomes if o not in lower_text]
            if missing_o:
                result.add_error(
                    f"Sektor 02 missing Luaran Tarbiyah components: {missing_o}",
                    canvas=canvas_name,
                )

            if not has_svg_or_table:
                result.add_error(
                    "Sektor 02 missing graphic curve visual representation (SVG or structured table)",
                    canvas=canvas_name,
                )

        elif "03 - Peran Pembelajaran" in canvas_name:
            # Fitrah learning & styles
            learning_modes = ["taqlid", "tajribah", "tafkir"]
            missing_m = [m for m in learning_modes if m not in lower_text]
            if missing_m:
                result.add_error(
                    f"Sektor 03 missing 3 Cara Belajar Fitrah: {missing_m}",
                    canvas=canvas_name,
                )

            if not ("an-nahl" in lower_text or "pendengaran" in lower_text or "penglihatan" in lower_text):
                result.add_error(
                    "Sektor 03 missing Qur'anic learning style reference (QS An-Nahl:78)",
                    canvas=canvas_name,
                )

        elif "04 - Peran Pendidik" in canvas_name:
            # 3 Parenting languages, Stepped Pyramid, and Al-Hima Tolerance Zones
            languages = ["bahasa hati", "bahasa lisan", "bahasa tangan"]
            missing_lang = [l for l in languages if l not in lower_text]
            if missing_lang:
                result.add_error(
                    f"Sektor 04 missing 3 Parenting Languages: {missing_lang}",
                    canvas=canvas_name,
                )

            zones = ["hijau", "kuning", "merah"]
            missing_zones = [z for z in zones if z not in lower_text]
            if missing_zones:
                result.add_error(
                    f"Sektor 04 missing Zonasi Al-Hima tolerance zones: {missing_zones}",
                    canvas=canvas_name,
                )

            if not has_svg_or_table:
                result.add_error(
                    "Sektor 04 missing Discipline vs Age curve representation (SVG or structured table)",
                    canvas=canvas_name,
                )

        elif "05 - Jejak Pendidik" in canvas_name:
            # Santri targets: Sholih & Muslih
            if not ("sholih" in lower_text or "muslih" in lower_text or "shalih" in lower_text):
                result.add_error(
                    "Sektor 05 missing Santri target objectives: 'Sholih' & 'Muslih'",
                    canvas=canvas_name,
                )

        elif "06 - Implementasi" in canvas_name:
            # 5-level causality & Tangki Cinta
            causality = ["nalar", "niat", "amal"]
            missing_c = [c for c in causality if c not in lower_text]
            if missing_c:
                result.add_error(
                    f"Sektor 06 missing Grand Theory Kesadaran stages: {missing_c}",
                    canvas=canvas_name,
                )

            if "tangki cinta" not in lower_text and "hidrolik" not in lower_text:
                result.add_error(
                    "Sektor 06 missing 'Tangki Cinta' systemic hydraulic concept",
                    canvas=canvas_name,
                )

        return result

    # -------------------------------------------------------------------------
    # Composite Validation: Single Canvas & Full Suite
    # -------------------------------------------------------------------------
    def validate_single_canvas(
        self, canvas_path: Path, canvas_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, ValidationPassResult]:
        name = canvas_path.name
        passes: Dict[str, ValidationPassResult] = {}

        # V2: Strict JSON
        if canvas_data is None:
            v2_res, parsed_data = self.validate_v2_json(canvas_path=canvas_path, canvas_name=name)
            passes["V2"] = v2_res
            if not v2_res.is_valid or parsed_data is None:
                return passes
            canvas_data = parsed_data
        else:
            v2_res = ValidationPassResult("V2", "Strict JSON Syntax & Structure", True)
            passes["V2"] = v2_res

        nodes = canvas_data.get("nodes", [])
        edges = canvas_data.get("edges", [])

        # V3: Nodes
        v3_res = self.validate_v3_nodes(nodes, canvas_name=name)
        passes["V3"] = v3_res

        node_ids = {n["id"] for n in nodes if isinstance(n, dict) and isinstance(n.get("id"), str)}

        # V4: Edges
        v4_res = self.validate_v4_edges(edges, node_ids, canvas_name=name)
        passes["V4"] = v4_res

        # V5: Spatial Geometry & Z-Index
        v5_res = self.validate_v5_geometry(nodes, canvas_name=name)
        passes["V5"] = v5_res

        # V7: Domain Content
        v7_res = self.validate_v7_domain_content(name, canvas_data)
        passes["V7"] = v7_res

        return passes

    def validate_all(self, dir_path: Path) -> Dict[str, ValidationPassResult]:
        passes: Dict[str, ValidationPassResult] = {}

        # V1: Directory & files
        v1_res = self.validate_v1_files(dir_path)
        passes["V1"] = v1_res
        if not v1_res.is_valid:
            # If files or directory missing, stop early for remaining multi-canvas checks
            return passes

        canvases_data: Dict[str, Dict[str, Any]] = {}
        v2_aggregate = ValidationPassResult("V2", "Strict JSON Syntax & Structure", True)
        v3_aggregate = ValidationPassResult("V3", "Node Schema & Type Constraints", True)
        v4_aggregate = ValidationPassResult("V4", "Edge Referential Integrity & Anchor Enums", True)
        v5_aggregate = ValidationPassResult("V5", "Spatial Geometry, Group Containment & Z-Index", True)
        v7_aggregate = ValidationPassResult("V7", "Pedagogical Domain Semantics & Hygiene", True)

        for fname in REQUIRED_CANVAS_FILES:
            fpath = dir_path / fname
            v2_res, data = self.validate_v2_json(canvas_path=fpath, canvas_name=fname)
            if not v2_res.is_valid or data is None:
                v2_aggregate.is_valid = False
                v2_aggregate.errors.extend(v2_res.errors)
                continue

            canvases_data[fname] = data

            # Single canvas passes
            sub_passes = self.validate_single_canvas(canvas_path=fpath, canvas_data=data)
            for p_key, p_res in sub_passes.items():
                if p_key == "V3":
                    if not p_res.is_valid:
                        v3_aggregate.is_valid = False
                        v3_aggregate.errors.extend(p_res.errors)
                elif p_key == "V4":
                    if not p_res.is_valid:
                        v4_aggregate.is_valid = False
                        v4_aggregate.errors.extend(p_res.errors)
                elif p_key == "V5":
                    if not p_res.is_valid:
                        v5_aggregate.is_valid = False
                        v5_aggregate.errors.extend(p_res.errors)
                elif p_key == "V7":
                    if not p_res.is_valid:
                        v7_aggregate.is_valid = False
                        v7_aggregate.errors.extend(p_res.errors)

        passes["V2"] = v2_aggregate
        passes["V3"] = v3_aggregate
        passes["V4"] = v4_aggregate
        passes["V5"] = v5_aggregate

        # V6: Master Hub Navigation Links
        v6_res = self.validate_v6_navigation(canvases_data, dir_path=dir_path)
        passes["V6"] = v6_res

        passes["V7"] = v7_aggregate

        return passes


# -----------------------------------------------------------------------------
# CLI Runner & Pretty Formatter
# -----------------------------------------------------------------------------
def format_report(passes: Dict[str, ValidationPassResult], quiet: bool = False) -> Tuple[str, bool]:
    lines: List[str] = []
    all_clean = True

    lines.append("=" * 80)
    lines.append("PKN OBSIDIAN CANVAS ARCHITECTURE VERIFICATION REPORT")
    lines.append("=" * 80)

    pass_order = ["V1", "V2", "V3", "V4", "V5", "V6", "V7"]

    for p_id in pass_order:
        if p_id not in passes:
            continue
        res = passes[p_id]
        if not res.is_valid:
            all_clean = False
            status_tag = "[FAIL]"
        else:
            status_tag = "[PASS]"

        lines.append(f"{status_tag} {res.pass_id}: {res.pass_name}")

        if not res.is_valid:
            for err in res.errors:
                loc = f" in {err.canvas}" if err.canvas else ""
                n_loc = f" (Node: {err.node_id})" if err.node_id else ""
                e_loc = f" (Edge: {err.edge_id})" if err.edge_id else ""
                lines.append(f"       -> ERROR{loc}{n_loc}{e_loc}: {err.message}")

        if res.warnings:
            for warn in res.warnings:
                lines.append(f"       -> WARNING: {warn}")

    lines.append("-" * 80)
    total_errors = sum(len(r.errors) for r in passes.values())
    total_warnings = sum(len(r.warnings) for r in passes.values())

    if all_clean:
        lines.append(f"RESULT: 100% SUCCESS — All executed passes passed with 0 errors, {total_warnings} warnings.")
    else:
        lines.append(f"RESULT: VERIFICATION FAILED — Encountered {total_errors} errors, {total_warnings} warnings.")
    lines.append("=" * 80)

    return "\n".join(lines), all_clean


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify PKN Obsidian Canvas Architecture (JSON Canvas 1.0 & Domain Integrity)"
    )
    parser.add_argument(
        "--dir",
        type=str,
        default="content/canvas/Arsitektur PKN",
        help="Path to directory containing the 7 PKN canvas files (default: content/canvas/Arsitektur PKN)",
    )
    parser.add_argument(
        "--canvas",
        type=str,
        default=None,
        help="Path to a single .canvas file to validate (executes V2, V3, V4, V5, V7)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Execute full suite V1 through V7 on target directory",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress non-error output",
    )

    args = parser.parse_args()
    validator = CanvasArchitectureValidator()

    if args.canvas:
        canvas_path = Path(args.canvas)
        if not canvas_path.exists():
            print(f"Error: Canvas file does not exist: {canvas_path}", file=sys.stderr)
            return 1
        passes = validator.validate_single_canvas(canvas_path)
    else:
        dir_path = Path(args.dir)
        passes = validator.validate_all(dir_path)

    report_text, is_clean = format_report(passes, quiet=args.quiet)
    print(report_text)

    return 0 if is_clean else 1


if __name__ == "__main__":
    sys.exit(main())

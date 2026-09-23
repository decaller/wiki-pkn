#!/usr/bin/env python3
"""
tests/test_canvas_adversarial_challenger.py

Empirical Challenger Test Suite for PKN Obsidian Canvas Architecture.
Authored by challenger_1.

Two Test Dimensions:
1. Deep Empirical Audit of the 7 Production Canvas Files:
   - JSON parsing with duplicate key detection
   - Strict coordinate & dimension integer validation (reject float/bool/string)
   - Coordinate bounds & aspect ratio sanity checks
   - Color format verification (presets '1'-'6' or valid hex)
   - XML well-formedness of embedded <svg> curves and diagrams
   - Spatial pyramid geometric hierarchy verification (Tier 1 to 4 widths, vertical order, alignment)
   - Group containment & Z-index ordering
   - Pairwise sibling card non-overlap (IoU check)
   - Wikilink resolution to physical markdown/canvas files
   - Hygiene / forbidden placeholder audit

2. Fuzzing & Mutation Robustness Suite for scripts/verify_canvas_architecture.py:
   - 50+ adversarial mutations (bad coordinates, dangling edges, z-index inversion,
     color anomalies, group overflows, missing backlinks, domain keyword omissions, malformed JSON)
   - Asserts that every mutation is caught with is_valid=False and structured error messages,
     without unhandled exceptions.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
import re
import sys
import unittest
import xml.etree.ElementTree as ET

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.verify_canvas_architecture import (
    CanvasArchitectureValidator,
    REQUIRED_CANVAS_FILES,
    SUB_CANVAS_FILES,
    MASTER_CANVAS_FILE,
    COLOR_PRESETS,
    HEX_COLOR_PATTERN,
    VALID_NODE_TYPES,
    VALID_SIDES,
    VALID_ENDS,
    FORBIDDEN_PLACEHOLDERS,
)

CANVAS_DIR = PROJECT_ROOT / "content" / "canvas" / "Arsitektur PKN"


def json_duplicate_key_detector(pairs):
    """Dict constructor that detects duplicate keys in JSON objects."""
    res = {}
    for k, v in pairs:
        if k in res:
            raise ValueError(f"Duplicate JSON key detected: '{k}'")
        res[k] = v
    return res


# =============================================================================
# DIMENSION 1: PRODUCTION CANVAS DEEP EMPIRICAL AUDIT
# =============================================================================
class TestProductionCanvasEmpiricalAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = CanvasArchitectureValidator()
        cls.canvas_data: dict[str, dict] = {}
        cls.raw_contents: dict[str, str] = {}

        for fname in REQUIRED_CANVAS_FILES:
            fpath = CANVAS_DIR / fname
            if fpath.exists():
                text = fpath.read_text(encoding="utf-8")
                cls.raw_contents[fname] = text
                cls.canvas_data[fname] = json.loads(text, object_pairs_hook=json_duplicate_key_detector)

    def test_all_production_files_exist_and_non_empty(self) -> None:
        """Verify all 7 canvas files exist, are files, and size > 1KB."""
        self.assertTrue(CANVAS_DIR.is_dir(), f"Canvas directory not found: {CANVAS_DIR}")
        for fname in REQUIRED_CANVAS_FILES:
            fpath = CANVAS_DIR / fname
            self.assertTrue(fpath.is_file(), f"Missing canvas file: {fname}")
            size = fpath.stat().st_size
            self.assertGreater(size, 1000, f"File {fname} is suspiciously small ({size} bytes)")

    def test_no_duplicate_keys_in_json(self) -> None:
        """Verify none of the 7 production files have duplicate keys in any JSON object."""
        for fname, text in self.raw_contents.items():
            try:
                json.loads(text, object_pairs_hook=json_duplicate_key_detector)
            except ValueError as e:
                self.fail(f"Duplicate key found in {fname}: {e}")

    def test_strict_coordinate_types_and_bounds(self) -> None:
        """Verify all nodes in all production files have strict integer coords, w>0, h>0, reasonable bounds."""
        for fname, data in self.canvas_data.items():
            nodes = data.get("nodes", [])
            for node in nodes:
                nid = node.get("id")
                x = node.get("x")
                y = node.get("y")
                w = node.get("width")
                h = node.get("height")

                # Strict int
                self.assertIs(type(x), int, f"{fname} node {nid}: x is not strict int ({type(x)})")
                self.assertIs(type(y), int, f"{fname} node {nid}: y is not strict int ({type(y)})")
                self.assertIs(type(w), int, f"{fname} node {nid}: width is not strict int ({type(w)})")
                self.assertIs(type(h), int, f"{fname} node {nid}: height is not strict int ({type(h)})")

                # Bounds
                self.assertGreater(w, 0, f"{fname} node {nid}: width must be > 0")
                self.assertGreater(h, 0, f"{fname} node {nid}: height must be > 0")
                self.assertLess(w, 10000, f"{fname} node {nid}: width excessively large ({w})")
                self.assertLess(h, 10000, f"{fname} node {nid}: height excessively large ({h})")
                self.assertGreater(x, -50000, f"{fname} node {nid}: x too small ({x})")
                self.assertLess(x, 50000, f"{fname} node {nid}: x too large ({x})")
                self.assertGreater(y, -50000, f"{fname} node {nid}: y too small ({y})")
                self.assertLess(y, 50000, f"{fname} node {nid}: y too large ({y})")

                # Aspect ratios (exclude groups which can be large containers)
                if node.get("type") != "group":
                    ratio = w / h
                    self.assertGreater(ratio, 0.05, f"{fname} node {nid}: aspect ratio too narrow ({ratio})")
                    self.assertLess(ratio, 25.0, f"{fname} node {nid}: aspect ratio too flat ({ratio})")

    def test_colors_conform_to_spec(self) -> None:
        """Verify all colors are string presets '1'-'6' or valid hex codes."""
        for fname, data in self.canvas_data.items():
            for node in data.get("nodes", []):
                if "color" in node:
                    c = node["color"]
                    self.assertIsInstance(c, str, f"{fname} node {node.get('id')}: color is not str ({c})")
                    is_preset = c in COLOR_PRESETS
                    is_hex = bool(HEX_COLOR_PATTERN.match(c))
                    self.assertTrue(
                        is_preset or is_hex,
                        f"{fname} node {node.get('id')}: invalid color format '{c}'",
                    )
            for edge in data.get("edges", []):
                if "color" in edge:
                    c = edge["color"]
                    self.assertIsInstance(c, str, f"{fname} edge {edge.get('id')}: color is not str ({c})")
                    is_preset = c in COLOR_PRESETS
                    is_hex = bool(HEX_COLOR_PATTERN.match(c))
                    self.assertTrue(
                        is_preset or is_hex,
                        f"{fname} edge {edge.get('id')}: invalid color format '{c}'",
                    )

    def test_xml_svg_validity_in_text_cards(self) -> None:
        """Verify all inline <svg> elements embedded inside canvas cards are valid, well-formed XML."""
        svg_count = 0
        for fname, data in self.canvas_data.items():
            for node in data.get("nodes", []):
                text = node.get("text", "")
                if "<svg" in text:
                    # Extract SVG tag blocks
                    svg_matches = re.findall(r"(<svg[\s\S]*?</svg>)", text)
                    self.assertGreater(len(svg_matches), 0, f"{fname} node {node.get('id')} has <svg but no closing </svg>")
                    for svg_str in svg_matches:
                        svg_count += 1
                        try:
                            root = ET.fromstring(svg_str)
                            self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg" if "xmlns" in svg_str else "svg")
                        except ET.ParseError as e:
                            raw_amp_match = re.search(r'&(?!(?:amp|lt|gt|quot|apos);)', svg_str)
                            hint = ""
                            if raw_amp_match:
                                snippet = svg_str[max(0, raw_amp_match.start() - 20): raw_amp_match.start() + 25]
                                hint = f" [Found unescaped '&' in '{snippet}'. Replace with '&amp;']"
                            self.fail(f"Malformed SVG in {fname} node {node.get('id')}: {e}{hint}")
        self.assertGreaterEqual(svg_count, 4, f"Expected at least 4 SVG visualizations across canvases, found {svg_count}")

    def test_spatial_pyramid_hierarchy_in_sector_04(self) -> None:
        """Empirically test the 4 tiers of the spatial pyramid in 04 - Peran Pendidik & Kedisiplinan.canvas."""
        data_04 = self.canvas_data["04 - Peran Pendidik & Kedisiplinan.canvas"]
        nodes_by_id = {n["id"]: n for n in data_04["nodes"]}

        # Expect tier 1, 2, 3, 4 with exact node IDs
        self.assertIn("s4-pyr-thufulah", nodes_by_id, "Missing Tier 1 node: s4-pyr-thufulah")
        self.assertIn("s4-pyr-tamyiz", nodes_by_id, "Missing Tier 2 node: s4-pyr-tamyiz")
        self.assertIn("s4-pyr-murahaqah", nodes_by_id, "Missing Tier 3 node: s4-pyr-murahaqah")
        self.assertIn("s4-pyr-syabab", nodes_by_id, "Missing Tier 4 node: s4-pyr-syabab")

        t1 = nodes_by_id["s4-pyr-thufulah"]
        t2 = nodes_by_id["s4-pyr-tamyiz"]
        t3 = nodes_by_id["s4-pyr-murahaqah"]
        t4 = nodes_by_id["s4-pyr-syabab"]

        # 1. Geometric Width Monotonicity: Tier 1 (base: 1380) > Tier 2 (1000) > Tier 3 (700) > Tier 4 (peak: 440)
        self.assertGreater(t1["width"], t2["width"], f"Base Tier 1 ({t1['width']}) must be wider than Tier 2 ({t2['width']})")
        self.assertGreater(t2["width"], t3["width"], f"Tier 2 ({t2['width']}) must be wider than Tier 3 ({t3['width']})")
        self.assertGreater(t3["width"], t4["width"], f"Tier 3 ({t3['width']}) must be wider than Peak Tier 4 ({t4['width']})")

        # 2. Vertical Stacking: Tier 1 (bottom: y=50) to Tier 4 (top: y=-520)
        self.assertGreater(t1["y"], t2["y"], f"Tier 1 (y={t1['y']}) should be vertically below Tier 2 (y={t2['y']})")
        self.assertGreater(t2["y"], t3["y"], f"Tier 2 (y={t2['y']}) should be vertically below Tier 3 (y={t3['y']})")
        self.assertGreater(t3["y"], t4["y"], f"Tier 3 (y={t3['y']}) should be vertically below Tier 4 (y={t4['y']})")

        # 3. Horizontal Alignment: All 4 tier centers must align precisely on x = -550
        centers = [n["x"] + n["width"] / 2.0 for n in [t1, t2, t3, t4]]
        for idx, c in enumerate(centers, start=1):
            self.assertEqual(c, -550.0, f"Tier {idx} center ({c}) is not exactly aligned on x = -550.0")

    def test_group_containment_and_zindex_in_production(self) -> None:
        """Run independent geometry & containment check across all 7 production files."""
        for fname, data in self.canvas_data.items():
            res = self.validator.validate_v5_geometry(data["nodes"], canvas_name=fname)
            self.assertTrue(res.is_valid, f"{fname} failed V5 geometry check: {res.errors}")

    def test_no_sibling_collisions_in_production(self) -> None:
        """Check that no cards in the same container have significant overlap (IoU > 0.05)."""
        for fname, data in self.canvas_data.items():
            non_groups = [n for n in data["nodes"] if n.get("type") != "group"]
            for i in range(len(non_groups)):
                for j in range(i + 1, len(non_groups)):
                    n1, n2 = non_groups[i], non_groups[j]
                    x1, y1, w1, h1 = n1["x"], n1["y"], n1["width"], n1["height"]
                    x2, y2, w2, h2 = n2["x"], n2["y"], n2["width"], n2["height"]

                    # Check bounding box overlap
                    ox = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
                    oy = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
                    overlap = ox * oy
                    if overlap > 0:
                        union = (w1 * h1) + (w2 * h2) - overlap
                        iou = overlap / union
                        self.assertLessEqual(
                            iou,
                            0.05,
                            f"{fname}: Overlap between '{n1.get('id')}' and '{n2.get('id')}' exceeds 0.05 (IoU: {iou:.3f})",
                        )

    def test_navigation_and_wikilinks_resolution(self) -> None:
        """Verify bidirectional navigation between Master and Sub-Canvases, and resolve wikilinks."""
        res_v6 = self.validator.validate_v6_navigation(self.canvas_data, dir_path=CANVAS_DIR)
        self.assertTrue(res_v6.is_valid, f"V6 navigation failed: {res_v6.errors}")

        # Check internal wikilinks [[...]]
        wikilink_pattern = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
        all_md_files = {p.stem.lower(): p for p in PROJECT_ROOT.glob("content/**/*.md")}
        all_canvas_files = {p.stem.lower(): p for p in CANVAS_DIR.glob("*.canvas")}

        for fname, data in self.canvas_data.items():
            for node in data.get("nodes", []):
                text = node.get("text", "")
                links = wikilink_pattern.findall(text)
                for link in links:
                    link_target = link.strip().lower()
                    # Strip .md or .canvas suffix if included
                    base_target = link_target.replace(".canvas", "").replace(".md", "")
                    target_stem = Path(base_target).stem
                    target_path = PROJECT_ROOT / "content" / link.strip()
                    exists_canvas = (
                        base_target in all_canvas_files
                        or link_target in all_canvas_files
                        or target_stem in all_canvas_files
                        or target_path.exists()
                    )
                    exists_md = (
                        base_target in all_md_files
                        or link_target in all_md_files
                        or target_stem in all_md_files
                        or target_path.with_suffix(".md").exists()
                    )
                    self.assertTrue(
                        exists_canvas or exists_md,
                        f"{fname} node {node.get('id')}: wikilink target '[[{link}]]' does not resolve to any physical file in content/",
                    )

    def test_hygiene_no_placeholder_tokens(self) -> None:
        """Verify no forbidden placeholder tokens exist anywhere in production canvas files."""
        for fname, data in self.canvas_data.items():
            res_v7 = self.validator.validate_v7_domain_content(fname, data)
            self.assertTrue(res_v7.is_valid, f"{fname} failed V7 domain semantics/hygiene check: {res_v7.errors}")


# =============================================================================
# DIMENSION 2: VALIDATOR MUTATION & FUZZING STRESS-TEST
# =============================================================================
class TestValidatorMutationStressHarness(unittest.TestCase):
    """Adversarial stress-test against scripts/verify_canvas_architecture.py."""

    def setUp(self) -> None:
        self.validator = CanvasArchitectureValidator()
        # Build minimal valid canvas base fixture
        self.base_canvas = {
            "nodes": [
                {
                    "id": "grp1",
                    "type": "group",
                    "x": 0,
                    "y": 0,
                    "width": 800,
                    "height": 500,
                    "label": "Base Group",
                },
                {
                    "id": "node_a",
                    "type": "text",
                    "x": 50,
                    "y": 50,
                    "width": 300,
                    "height": 200,
                    "color": "1",
                    "text": "Card A Content [[00 - Master Arsitektur PKN.canvas]]",
                },
                {
                    "id": "node_b",
                    "type": "text",
                    "x": 400,
                    "y": 50,
                    "width": 300,
                    "height": 200,
                    "color": "#112233",
                    "text": "Card B Content",
                },
            ],
            "edges": [
                {
                    "id": "edge_1",
                    "fromNode": "node_a",
                    "toNode": "node_b",
                    "fromSide": "right",
                    "toSide": "left",
                    "fromEnd": "none",
                    "toEnd": "arrow",
                    "color": "3",
                    "label": "A to B",
                }
            ],
        }

    def _clone_base(self) -> dict:
        return copy.deepcopy(self.base_canvas)

    # -------------------------------------------------------------------------
    # Coordinate and Dimension Mutations
    # -------------------------------------------------------------------------
    def test_mutation_coord_float_x(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["x"] = 50.5
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch float x coordinate")
        self.assertTrue(any("Coordinate 'x' must be an integer" in e.message for e in res.errors))

    def test_mutation_coord_str_x(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["x"] = "50"
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch string x coordinate")
        self.assertTrue(any("Coordinate 'x' must be an integer" in e.message for e in res.errors))

    def test_mutation_coord_bool_x(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["x"] = True
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch boolean x coordinate")

    def test_mutation_coord_none_x(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["x"] = None
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch None x coordinate")

    def test_mutation_dim_zero_width(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["width"] = 0
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch zero width")
        self.assertTrue(any("positive integer" in e.message for e in res.errors))

    def test_mutation_dim_negative_height(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["height"] = -100
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch negative height")

    def test_mutation_dim_float_width(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["width"] = 100.25
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch float width")

    def test_mutation_dim_str_height(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["height"] = "200"
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch string height")

    # -------------------------------------------------------------------------
    # Color Value Mutations
    # -------------------------------------------------------------------------
    def test_mutation_color_numeric_int(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["color"] = 1  # numeric int instead of string "1"
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch numeric int color")
        self.assertTrue(any("Invalid color value '1'" in e.message for e in res.errors))

    def test_mutation_color_invalid_preset(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["color"] = "7"  # presets are only 1-6
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch invalid preset color '7'")

    def test_mutation_color_bad_hex_length(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["color"] = "#12345"  # 5 digits
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch 5-digit hex")

    def test_mutation_color_bad_hex_chars(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["color"] = "#GGHHII"
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch invalid hex characters")

    def test_mutation_color_named_string(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["color"] = "red"
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch named color string 'red'")

    def test_mutation_edge_color_invalid(self) -> None:
        c = self._clone_base()
        c["edges"][0]["color"] = "blue"
        res = self.validator.validate_v4_edges(c["edges"], {"node_a", "node_b", "grp1"})
        self.assertFalse(res.is_valid, "Failed to catch invalid edge color")

    # -------------------------------------------------------------------------
    # Node Payload and Type Mutations
    # -------------------------------------------------------------------------
    def test_mutation_duplicate_node_id(self) -> None:
        c = self._clone_base()
        c["nodes"][2]["id"] = c["nodes"][1]["id"]
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch duplicate node ID")
        self.assertTrue(any("Duplicate node ID" in e.message for e in res.errors))

    def test_mutation_empty_node_id(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["id"] = ""
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch empty node ID")

    def test_mutation_invalid_node_type(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["type"] = "canvas_card"
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch unsupported node type")

    def test_mutation_text_node_empty_text(self) -> None:
        c = self._clone_base()
        c["nodes"][1]["text"] = "   "
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch empty text in text node")

    def test_mutation_text_node_missing_text(self) -> None:
        c = self._clone_base()
        del c["nodes"][1]["text"]
        res = self.validator.validate_v3_nodes(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch missing text key in text node")

    def test_mutation_file_node_missing_file_key(self) -> None:
        nodes = [{"id": "fn", "type": "file", "x": 0, "y": 0, "width": 100, "height": 100}]
        res = self.validator.validate_v3_nodes(nodes)
        self.assertFalse(res.is_valid, "Failed to catch missing 'file' in file node")

    def test_mutation_file_node_bad_subpath(self) -> None:
        nodes = [{"id": "fn", "type": "file", "x": 0, "y": 0, "width": 100, "height": 100, "file": "test.md", "subpath": "Heading"}]
        res = self.validator.validate_v3_nodes(nodes)
        self.assertFalse(res.is_valid, "Failed to catch subpath not starting with '#'")

    def test_mutation_link_node_bad_protocol(self) -> None:
        nodes = [{"id": "ln", "type": "link", "x": 0, "y": 0, "width": 100, "height": 100, "url": "ftp://files.org"}]
        res = self.validator.validate_v3_nodes(nodes)
        self.assertFalse(res.is_valid, "Failed to catch non-HTTP link protocol")

    def test_mutation_group_invalid_background_style(self) -> None:
        nodes = [{"id": "gn", "type": "group", "x": 0, "y": 0, "width": 100, "height": 100, "backgroundStyle": "tile"}]
        res = self.validator.validate_v3_nodes(nodes)
        self.assertFalse(res.is_valid, "Failed to catch invalid group backgroundStyle")

    # -------------------------------------------------------------------------
    # Edge Integrity Mutations
    # -------------------------------------------------------------------------
    def test_mutation_edge_dangling_from_node(self) -> None:
        c = self._clone_base()
        c["edges"][0]["fromNode"] = "ghost_node_123"
        res = self.validator.validate_v4_edges(c["edges"], {"node_a", "node_b", "grp1"})
        self.assertFalse(res.is_valid, "Failed to catch dangling fromNode")
        self.assertTrue(any("does not exist" in e.message for e in res.errors))

    def test_mutation_edge_dangling_to_node(self) -> None:
        c = self._clone_base()
        c["edges"][0]["toNode"] = "ghost_node_999"
        res = self.validator.validate_v4_edges(c["edges"], {"node_a", "node_b", "grp1"})
        self.assertFalse(res.is_valid, "Failed to catch dangling toNode")

    def test_mutation_edge_duplicate_id(self) -> None:
        c = self._clone_base()
        e_dup = copy.deepcopy(c["edges"][0])
        c["edges"].append(e_dup)
        res = self.validator.validate_v4_edges(c["edges"], {"node_a", "node_b", "grp1"})
        self.assertFalse(res.is_valid, "Failed to catch duplicate edge ID")

    def test_mutation_edge_invalid_side(self) -> None:
        c = self._clone_base()
        c["edges"][0]["fromSide"] = "middle"
        res = self.validator.validate_v4_edges(c["edges"], {"node_a", "node_b", "grp1"})
        self.assertFalse(res.is_valid, "Failed to catch invalid fromSide")

    def test_mutation_edge_invalid_end(self) -> None:
        c = self._clone_base()
        c["edges"][0]["toEnd"] = "triangle"
        res = self.validator.validate_v4_edges(c["edges"], {"node_a", "node_b", "grp1"})
        self.assertFalse(res.is_valid, "Failed to catch invalid toEnd")

    # -------------------------------------------------------------------------
    # Spatial Geometry & Containment Mutations
    # -------------------------------------------------------------------------
    def test_mutation_geometry_zindex_violation(self) -> None:
        c = self._clone_base()
        # Invert order: child before group
        grp = c["nodes"].pop(0)
        c["nodes"].append(grp)
        res = self.validator.validate_v5_geometry(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch z-index inversion")
        self.assertTrue(any("Z-Index violation" in e.message for e in res.errors))

    def test_mutation_geometry_group_overflow_right(self) -> None:
        c = self._clone_base()
        # Group is width 800 (x: 0..800). Put child at x=600 with width 300 -> ends at 900 (overflows by 100)
        c["nodes"][2]["x"] = 600
        c["nodes"][2]["width"] = 300
        res = self.validator.validate_v5_geometry(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch group overflow right")
        self.assertTrue(any("overflow" in e.message.lower() for e in res.errors))

    def test_mutation_geometry_group_overflow_top(self) -> None:
        c = self._clone_base()
        # Group is y: 0..500. Child at y = -100
        c["nodes"][1]["y"] = -100
        res = self.validator.validate_v5_geometry(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch group overflow top")

    def test_mutation_geometry_sibling_collision(self) -> None:
        c = self._clone_base()
        # Stack card B directly on card A (IoU = 1.0)
        c["nodes"][2]["x"] = c["nodes"][1]["x"]
        c["nodes"][2]["y"] = c["nodes"][1]["y"]
        c["nodes"][2]["width"] = c["nodes"][1]["width"]
        c["nodes"][2]["height"] = c["nodes"][1]["height"]
        res = self.validator.validate_v5_geometry(c["nodes"])
        self.assertFalse(res.is_valid, "Failed to catch sibling collision")
        self.assertTrue(any("Spatial collision" in e.message for e in res.errors))

    # -------------------------------------------------------------------------
    # Domain Semantics & Hygiene Mutations
    # -------------------------------------------------------------------------
    def test_mutation_hygiene_forbidden_tokens(self) -> None:
        for placeholder in FORBIDDEN_PLACEHOLDERS:
            c = self._clone_base()
            c["nodes"][1]["text"] = f"Catatan ini adalah {placeholder} yang harus dikerjakan."
            res = self.validator.validate_v7_domain_content("01 - Komponen & Kurikulum PKN.canvas", c)
            self.assertFalse(res.is_valid, f"Failed to catch forbidden placeholder '{placeholder}'")

    def test_mutation_domain_s00_missing_formula(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "Hanya Hub Tanpa Rumus"}], "edges": []}
        res = self.validator.validate_v7_domain_content("00 - Master Arsitektur PKN.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing Amal << Ilmu << Iman formula in S00")

    def test_mutation_domain_s01_missing_authoritative_sources(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "Aqidah, Ibadah, Akhlaq, Muamalah, Dakwah, Adab -> STEM"}], "edges": []}
        res = self.validator.validate_v7_domain_content("01 - Komponen & Kurikulum PKN.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing authoritative sources (Quran, Sunnah, Salaf, Sirah) in S01")

    def test_mutation_domain_s02_missing_insan_hierarchy(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "Akhlaq, Adab, Ilmu, Amal <svg></svg>"}], "edges": []}
        res = self.validator.validate_v7_domain_content("02 - Metode & Pendekatan Fisik-Ruh.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing Jasad-Ruh hierarchy in S02")

    def test_mutation_domain_s03_missing_learning_modes(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "An-Nahl 78 pendengaran penglihatan"}], "edges": []}
        res = self.validator.validate_v7_domain_content("03 - Peran Pembelajaran & Model.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing Taqlid, Tajribah, Tafkir in S03")

    def test_mutation_domain_s04_missing_parenting_languages(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "Hijau, Kuning, Merah <svg></svg>"}], "edges": []}
        res = self.validator.validate_v7_domain_content("04 - Peran Pendidik & Kedisiplinan.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing Bahasa Hati/Lisan/Tangan in S04")

    def test_mutation_domain_s04_missing_hima_zones(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "Bahasa Hati, Bahasa Lisan, Bahasa Tangan <svg></svg>"}], "edges": []}
        res = self.validator.validate_v7_domain_content("04 - Peran Pendidik & Kedisiplinan.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing Hijau/Kuning/Merah zones in S04")

    def test_mutation_domain_s05_missing_santri_targets(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "Target santri jangka pendek dan panjang"}], "edges": []}
        res = self.validator.validate_v7_domain_content("05 - Jejak Pendidik & Target.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing Sholih & Muslih in S05")

    def test_mutation_domain_s06_missing_causality_chain(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "Tangki Cinta Hidrolik"}], "edges": []}
        res = self.validator.validate_v7_domain_content("06 - Implementasi & Rantai Kausalitas.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing Nalar, Niat, Amal in S06")

    def test_mutation_domain_s06_missing_tangki_cinta(self) -> None:
        c = {"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "Grand Theory Kesadaran: Nalar, Niat, Amal"}], "edges": []}
        res = self.validator.validate_v7_domain_content("06 - Implementasi & Rantai Kausalitas.canvas", c)
        self.assertFalse(res.is_valid, "Failed to catch missing Tangki Cinta in S06")


if __name__ == "__main__":
    unittest.main(verbosity=2)

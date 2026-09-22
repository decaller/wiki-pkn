#!/usr/bin/env python3
"""
tests/test_canvas_architecture.py

Comprehensive Test Suite for PKN Obsidian Canvas Architecture Validator.
Tests all 7 validation passes (V1 to V7) against positive fixtures and
adversarial/negative fixtures (missing nodes, broken edges, group overflow,
z-index violations, spatial collisions, malformed coordinates, invalid colors,
missing wikilinks, and domain keyword omissions).
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.verify_canvas_architecture import (
    CanvasArchitectureValidator,
    REQUIRED_CANVAS_FILES,
    SUB_CANVAS_FILES,
    MASTER_CANVAS_FILE,
)


class TestCanvasArchitectureValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = CanvasArchitectureValidator()

    # -------------------------------------------------------------------------
    # PASS V1: Directory Structure & File Presence
    # -------------------------------------------------------------------------
    def test_v1_directory_missing(self) -> None:
        """V1 should fail when the canvas directory does not exist."""
        non_existent_dir = Path("/tmp/non_existent_canvas_dir_12345")
        result = self.validator.validate_v1_files(non_existent_dir)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("does not exist" in e.message for e in result.errors))

    def test_v1_missing_canvas_files(self) -> None:
        """V1 should fail when any of the 7 required canvas files is missing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            dir_path = Path(tmpdir)
            # Create only 6 out of 7 files (omit 04)
            for fname in REQUIRED_CANVAS_FILES:
                if "04 - Peran Pendidik" in fname:
                    continue
                fpath = dir_path / fname
                fpath.write_text(json.dumps({"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "OK"}], "edges": []}))

            result = self.validator.validate_v1_files(dir_path)
            self.assertFalse(result.is_valid)
            missing_errs = [e for e in result.errors if "04 - Peran Pendidik" in e.message]
            self.assertEqual(len(missing_errs), 1)

    def test_v1_empty_canvas_file(self) -> None:
        """V1 should fail when a canvas file has 0 bytes."""
        with tempfile.TemporaryDirectory() as tmpdir:
            dir_path = Path(tmpdir)
            for fname in REQUIRED_CANVAS_FILES:
                fpath = dir_path / fname
                if "00 - Master" in fname:
                    fpath.touch()  # 0 bytes
                else:
                    fpath.write_text('{"nodes": [], "edges": []}')

            result = self.validator.validate_v1_files(dir_path)
            self.assertFalse(result.is_valid)
            empty_errs = [e for e in result.errors if "empty (0 bytes)" in e.message]
            self.assertEqual(len(empty_errs), 1)

    def test_v1_all_files_present_positive(self) -> None:
        """V1 should pass when all 7 canvas files are present and non-empty."""
        with tempfile.TemporaryDirectory() as tmpdir:
            dir_path = Path(tmpdir)
            for fname in REQUIRED_CANVAS_FILES:
                (dir_path / fname).write_text('{"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "A"}], "edges": []}')

            result = self.validator.validate_v1_files(dir_path)
            self.assertTrue(result.is_valid)
            self.assertEqual(len(result.errors), 0)

    # -------------------------------------------------------------------------
    # PASS V2: Strict JSON Syntax & Well-Formedness
    # -------------------------------------------------------------------------
    def test_v2_syntax_error(self) -> None:
        """V2 should fail on malformed JSON syntax."""
        bad_json = '{"nodes": [{"id": "1", "type": "text", "text": "bad" '  # unclosed
        result, data = self.validator.validate_v2_json(content=bad_json, canvas_name="bad.canvas")
        self.assertFalse(result.is_valid)
        self.assertIsNone(data)
        self.assertTrue(any("JSON syntax error" in e.message for e in result.errors))

    def test_v2_root_not_dict(self) -> None:
        """V2 should fail when JSON root is not an object/dict."""
        bad_root = '[{"nodes": []}]'
        result, data = self.validator.validate_v2_json(content=bad_root, canvas_name="list.canvas")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Root JSON element must be an object/dict" in e.message for e in result.errors))

    def test_v2_missing_nodes_or_edges_keys(self) -> None:
        """V2 should fail if 'nodes' or 'edges' keys are missing or not lists."""
        no_edges = '{"nodes": [{"id": "1", "type": "text", "x": 0, "y": 0, "width": 10, "height": 10, "text": "t"}]}'
        result, _ = self.validator.validate_v2_json(content=no_edges, canvas_name="no_edges.canvas")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("missing required 'edges' array" in e.message for e in result.errors))

        nodes_not_list = '{"nodes": "invalid", "edges": []}'
        result, _ = self.validator.validate_v2_json(content=nodes_not_list, canvas_name="nodes_string.canvas")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("'nodes' must be an array" in e.message for e in result.errors))

    def test_v2_empty_canvas_nodes(self) -> None:
        """V2 should fail if canvas has 0 nodes (unbuilt/empty canvas)."""
        empty_canvas = '{"nodes": [], "edges": []}'
        result, _ = self.validator.validate_v2_json(content=empty_canvas, canvas_name="empty.canvas")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("contains 0 nodes" in e.message for e in result.errors))

    def test_v2_valid_canvas_positive(self) -> None:
        """V2 should pass on well-formed JSON Canvas structure."""
        valid_json = '{"nodes": [{"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "OK"}], "edges": []}'
        result, data = self.validator.validate_v2_json(content=valid_json, canvas_name="valid.canvas")
        self.assertTrue(result.is_valid)
        self.assertIsNotNone(data)
        self.assertEqual(len(data["nodes"]), 1)

    # -------------------------------------------------------------------------
    # PASS V3: Node Schema & Type Constraints
    # -------------------------------------------------------------------------
    def test_v3_valid_nodes_all_types_positive(self) -> None:
        """V3 should pass for valid text, file, link, and group nodes."""
        nodes = [
            {
                "id": "text_1",
                "type": "text",
                "x": 0,
                "y": 0,
                "width": 300,
                "height": 150,
                "color": "1",
                "text": "### Heading\nContent",
            },
            {
                "id": "file_1",
                "type": "file",
                "x": 350,
                "y": 0,
                "width": 300,
                "height": 150,
                "color": "#336699",
                "file": "content/notes/note.md",
                "subpath": "#Section 1",
            },
            {
                "id": "link_1",
                "type": "link",
                "x": 700,
                "y": 0,
                "width": 300,
                "height": 150,
                "color": "6",
                "url": "https://jsoncanvas.org",
            },
            {
                "id": "group_1",
                "type": "group",
                "x": -50,
                "y": -50,
                "width": 1100,
                "height": 300,
                "label": "Container Group",
                "backgroundStyle": "cover",
            },
        ]
        result = self.validator.validate_v3_nodes(nodes, canvas_name="test.canvas")
        self.assertTrue(result.is_valid, msg=f"Errors: {result.errors}")

    def test_v3_duplicate_node_id(self) -> None:
        """V3 should detect duplicate node IDs."""
        nodes = [
            {"id": "dup1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "text": "A"},
            {"id": "dup1", "type": "text", "x": 200, "y": 0, "width": 100, "height": 100, "text": "B"},
        ]
        result = self.validator.validate_v3_nodes(nodes, canvas_name="test.canvas")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Duplicate node ID 'dup1'" in e.message for e in result.errors))

    def test_v3_invalid_node_type(self) -> None:
        """V3 should reject unsupported node types."""
        nodes = [
            {"id": "bad_type", "type": "image", "x": 0, "y": 0, "width": 100, "height": 100}
        ]
        result = self.validator.validate_v3_nodes(nodes, canvas_name="test.canvas")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Invalid node type 'image'" in e.message for e in result.errors))

    def test_v3_non_integer_coordinates(self) -> None:
        """V3 should reject float, string, or boolean coordinates."""
        # Float coordinate
        nodes_float = [
            {"id": "n1", "type": "text", "x": 10.5, "y": 0, "width": 100, "height": 100, "text": "T"}
        ]
        res1 = self.validator.validate_v3_nodes(nodes_float)
        self.assertFalse(res1.is_valid)
        self.assertTrue(any("Coordinate 'x' must be an integer" in e.message for e in res1.errors))

        # Boolean coordinate (bool is subclass of int in Python, must be caught)
        nodes_bool = [
            {"id": "n2", "type": "text", "x": True, "y": 0, "width": 100, "height": 100, "text": "T"}
        ]
        res2 = self.validator.validate_v3_nodes(nodes_bool)
        self.assertFalse(res2.is_valid)
        self.assertTrue(any("Coordinate 'x' must be an integer" in e.message for e in res2.errors))

    def test_v3_invalid_dimensions(self) -> None:
        """V3 should reject zero or negative width/height."""
        nodes = [
            {"id": "n1", "type": "text", "x": 0, "y": 0, "width": 0, "height": 100, "text": "T"},
            {"id": "n2", "type": "text", "x": 100, "y": 0, "width": 100, "height": -50, "text": "T"},
        ]
        result = self.validator.validate_v3_nodes(nodes)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Dimension 'width' must be a positive integer" in e.message for e in result.errors))
        self.assertTrue(any("Dimension 'height' must be a positive integer" in e.message for e in result.errors))

    def test_v3_invalid_color_values(self) -> None:
        """V3 should reject integer colors, invalid strings, and malformed hex."""
        # Integer color 1 (violates spec which requires string "1")
        nodes_int_color = [
            {"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "color": 1, "text": "T"}
        ]
        res1 = self.validator.validate_v3_nodes(nodes_int_color)
        self.assertFalse(res1.is_valid)
        self.assertTrue(any("Invalid color value '1'" in e.message for e in res1.errors))

        # Malformed hex
        nodes_bad_hex = [
            {"id": "n2", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100, "color": "#12345", "text": "T"}
        ]
        res2 = self.validator.validate_v3_nodes(nodes_bad_hex)
        self.assertFalse(res2.is_valid)
        self.assertTrue(any("Invalid color value '#12345'" in e.message for e in res2.errors))

    def test_v3_missing_text_in_text_node(self) -> None:
        """V3 should reject text nodes without a valid text string."""
        nodes = [
            {"id": "n1", "type": "text", "x": 0, "y": 0, "width": 100, "height": 100}
        ]
        result = self.validator.validate_v3_nodes(nodes)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Text node missing required 'text'" in e.message for e in result.errors))

    # -------------------------------------------------------------------------
    # PASS V4: Edge Referential Integrity & Side Enums
    # -------------------------------------------------------------------------
    def test_v4_valid_edges_positive(self) -> None:
        """V4 should pass for valid edges connecting existing nodes with valid enums."""
        node_ids = {"n1", "n2", "n3"}
        edges = [
            {
                "id": "e1",
                "fromNode": "n1",
                "toNode": "n2",
                "fromSide": "right",
                "toSide": "left",
                "fromEnd": "none",
                "toEnd": "arrow",
                "color": "2",
                "label": "Flow A->B",
            },
            {
                "id": "e2",
                "fromNode": "n2",
                "toNode": "n3",
                "fromSide": "bottom",
                "toSide": "top",
            },
        ]
        result = self.validator.validate_v4_edges(edges, node_ids, canvas_name="test.canvas")
        self.assertTrue(result.is_valid)
        self.assertEqual(len(result.errors), 0)

    def test_v4_dangling_from_or_to_node(self) -> None:
        """V4 should detect dangling edges pointing to nonexistent nodes."""
        node_ids = {"n1"}
        edges = [
            {"id": "e1", "fromNode": "n1", "toNode": "non_existent_target"},
            {"id": "e2", "fromNode": "non_existent_source", "toNode": "n1"},
        ]
        result = self.validator.validate_v4_edges(edges, node_ids)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("toNode' ID 'non_existent_target' does not exist" in e.message for e in result.errors))
        self.assertTrue(any("fromNode' ID 'non_existent_source' does not exist" in e.message for e in result.errors))

    def test_v4_duplicate_edge_id(self) -> None:
        """V4 should detect duplicate edge IDs."""
        node_ids = {"n1", "n2"}
        edges = [
            {"id": "dup_e", "fromNode": "n1", "toNode": "n2"},
            {"id": "dup_e", "fromNode": "n2", "toNode": "n1"},
        ]
        result = self.validator.validate_v4_edges(edges, node_ids)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Duplicate edge ID 'dup_e'" in e.message for e in result.errors))

    def test_v4_invalid_side_or_end_enum(self) -> None:
        """V4 should reject invalid side and line end enums."""
        node_ids = {"n1", "n2"}
        edges = [
            {
                "id": "e1",
                "fromNode": "n1",
                "toNode": "n2",
                "fromSide": "diagonal",
                "toEnd": "diamond",
            }
        ]
        result = self.validator.validate_v4_edges(edges, node_ids)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Invalid 'fromSide' 'diagonal'" in e.message for e in result.errors))
        self.assertTrue(any("Invalid 'toEnd' 'diamond'" in e.message for e in result.errors))

    # -------------------------------------------------------------------------
    # PASS V5: Spatial Geometry, Group Z-Index Order & Non-Overlap
    # -------------------------------------------------------------------------
    def test_v5_valid_group_containment_positive(self) -> None:
        """V5 should pass when a group precedes its enclosed child and fits with margin."""
        nodes = [
            # Group defined first (index 0)
            {
                "id": "grp1",
                "type": "group",
                "x": 0,
                "y": 0,
                "width": 600,
                "height": 400,
                "label": "Main Container",
            },
            # Child defined second (index 1), inside grp1 with ample padding
            {
                "id": "child1",
                "type": "text",
                "x": 50,
                "y": 50,
                "width": 200,
                "height": 100,
                "text": "Card 1",
            },
            # Child 2 sibling inside grp1, separated from child 1
            {
                "id": "child2",
                "type": "text",
                "x": 300,
                "y": 50,
                "width": 200,
                "height": 100,
                "text": "Card 2",
            },
        ]
        result = self.validator.validate_v5_geometry(nodes)
        self.assertTrue(result.is_valid, msg=f"Errors: {result.errors}")

    def test_v5_z_index_order_violation(self) -> None:
        """V5 should detect Z-Index violation if a group is defined AFTER its enclosed child."""
        nodes = [
            # Child defined BEFORE enclosing group
            {
                "id": "child1",
                "type": "text",
                "x": 50,
                "y": 50,
                "width": 200,
                "height": 100,
                "text": "Card 1",
            },
            # Group defined AFTER child
            {
                "id": "grp1",
                "type": "group",
                "x": 0,
                "y": 0,
                "width": 600,
                "height": 400,
                "label": "Late Group",
            },
        ]
        result = self.validator.validate_v5_geometry(nodes)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Z-Index violation" in e.message for e in result.errors))

    def test_v5_group_bounding_box_overflow(self) -> None:
        """V5 should detect when a child node overflows outside its enclosing group boundary."""
        nodes = [
            # Group bounds: x: 0..400, y: 0..300
            {
                "id": "grp1",
                "type": "group",
                "x": 0,
                "y": 0,
                "width": 400,
                "height": 300,
            },
            # Child center is inside group (x: 200, y: 150), but width extends to x = 500 (overflows by 100px)
            {
                "id": "child_overflow",
                "type": "text",
                "x": 100,
                "y": 50,
                "width": 400,  # 100 + 400 = 500 > 400
                "height": 100,
                "text": "Overflowing Card",
            },
        ]
        result = self.validator.validate_v5_geometry(nodes)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Group bounding box overflow" in e.message for e in result.errors))

    def test_v5_sibling_collision(self) -> None:
        """V5 should detect significant collision/overlap between sibling cards."""
        nodes = [
            # Two root-level sibling cards overlapping heavily
            {
                "id": "card_a",
                "type": "text",
                "x": 100,
                "y": 100,
                "width": 200,
                "height": 200,
                "text": "Card A",
            },
            {
                "id": "card_b",
                "type": "text",
                "x": 150,
                "y": 150,
                "width": 200,
                "height": 200,
                "text": "Card B",
            },
        ]
        result = self.validator.validate_v5_geometry(nodes)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Spatial collision" in e.message for e in result.errors))

    # -------------------------------------------------------------------------
    # PASS V6: Master Hub Navigation Links
    # -------------------------------------------------------------------------
    def test_v6_valid_bidirectional_navigation_positive(self) -> None:
        """V6 should pass when Master links to all 6 sub-canvases and all sub-canvases link back."""
        canvases_data = {}

        # Master Hub linking to 01..06
        master_nodes = []
        for sub_name in SUB_CANVAS_FILES:
            master_nodes.append({
                "id": f"link_to_{sub_name}",
                "type": "text",
                "x": 0,
                "y": 0,
                "width": 200,
                "height": 100,
                "text": f"Navigasi ke [[{sub_name}|Buka]]",
            })
        canvases_data[MASTER_CANVAS_FILE] = {"nodes": master_nodes, "edges": []}

        # Sub-canvases linking back to Master Hub
        for sub_name in SUB_CANVAS_FILES:
            canvases_data[sub_name] = {
                "nodes": [
                    {
                        "id": "back_to_hub",
                        "type": "text",
                        "x": 0,
                        "y": 0,
                        "width": 200,
                        "height": 100,
                        "text": f"Kembali ke [[{MASTER_CANVAS_FILE}|Master Hub PKN]]",
                    }
                ],
                "edges": [],
            }

        result = self.validator.validate_v6_navigation(canvases_data)
        self.assertTrue(result.is_valid, msg=f"Errors: {result.errors}")

    def test_v6_missing_subcanvas_link_from_master(self) -> None:
        """V6 should fail if Master Hub is missing a link to any sub-canvas."""
        canvases_data = {}
        # Master links to only 01..05, missing 06
        master_nodes = []
        for sub_name in SUB_CANVAS_FILES[:-1]:
            master_nodes.append({
                "id": f"link_to_{sub_name}",
                "type": "text",
                "x": 0,
                "y": 0,
                "width": 200,
                "height": 100,
                "text": f"Navigasi ke [[{sub_name}]]",
            })
        canvases_data[MASTER_CANVAS_FILE] = {"nodes": master_nodes, "edges": []}

        for sub_name in SUB_CANVAS_FILES:
            canvases_data[sub_name] = {
                "nodes": [{"id": "b", "type": "text", "x": 0, "y": 0, "width": 100, "height": 50, "text": f"[[{MASTER_CANVAS_FILE}]]"}],
                "edges": [],
            }

        result = self.validator.validate_v6_navigation(canvases_data)
        self.assertFalse(result.is_valid)
        self.assertTrue(any(f"missing outgoing navigation link to '{SUB_CANVAS_FILES[-1]}'" in e.message for e in result.errors))

    def test_v6_subcanvas_missing_return_link(self) -> None:
        """V6 should fail if a sub-canvas does not have a link back to Master Hub."""
        canvases_data = {}
        master_nodes = []
        for sub_name in SUB_CANVAS_FILES:
            master_nodes.append({
                "id": f"link_{sub_name}",
                "type": "text",
                "x": 0,
                "y": 0,
                "width": 100,
                "height": 50,
                "text": f"[[{sub_name}]]",
            })
        canvases_data[MASTER_CANVAS_FILE] = {"nodes": master_nodes, "edges": []}

        for idx, sub_name in enumerate(SUB_CANVAS_FILES):
            text_content = f"[[{MASTER_CANVAS_FILE}]]" if idx != 2 else "No backlink here!"
            canvases_data[sub_name] = {
                "nodes": [{"id": "b", "type": "text", "x": 0, "y": 0, "width": 100, "height": 50, "text": text_content}],
                "edges": [],
            }

        result = self.validator.validate_v6_navigation(canvases_data)
        self.assertFalse(result.is_valid)
        self.assertTrue(any(f"Sub-canvas '{SUB_CANVAS_FILES[2]}' missing return navigation link" in e.message for e in result.errors))

    # -------------------------------------------------------------------------
    # PASS V7: Pedagogical Domain Content & Hygiene
    # -------------------------------------------------------------------------
    def test_v7_forbidden_placeholders(self) -> None:
        """V7 should reject canvases containing placeholder tokens like TODO, TBD, FIXME."""
        bad_canvas = {
            "nodes": [
                {
                    "id": "n1",
                    "type": "text",
                    "x": 0,
                    "y": 0,
                    "width": 100,
                    "height": 50,
                    "text": "Kaidah ini adalah TODO untuk diselesaikan",
                }
            ],
            "edges": [],
        }
        result = self.validator.validate_v7_domain_content("06 - Implementasi & Rantai Kausalitas.canvas", bad_canvas)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Forbidden placeholder token 'TODO'" in e.message for e in result.errors))

    def test_v7_sector_04_pyramid_and_zones_positive(self) -> None:
        """V7 should pass Sektor 04 when 3 parenting languages, Hima zones, and curve are present."""
        data_04 = {
            "nodes": [
                {
                    "id": "pyramid_tier_1",
                    "type": "text",
                    "x": 0,
                    "y": 0,
                    "width": 300,
                    "height": 100,
                    "text": "### Fondasi: Bahasa Hati (0-7 Tahun)",
                },
                {
                    "id": "pyramid_tier_2",
                    "type": "text",
                    "x": 0,
                    "y": 120,
                    "width": 300,
                    "height": 100,
                    "text": "### Tingkat Menengah: Bahasa Lisan (7-10 Tahun)",
                },
                {
                    "id": "pyramid_tier_3",
                    "type": "text",
                    "x": 0,
                    "y": 240,
                    "width": 300,
                    "height": 100,
                    "text": "### Puncak Piramida: Bahasa Tangan (10-Baligh)",
                },
                {
                    "id": "hima_zones",
                    "type": "text",
                    "x": 350,
                    "y": 0,
                    "width": 300,
                    "height": 200,
                    "text": "Zonasi Al-Hima: Zona Hijau (Kebebasan), Zona Kuning (Nalar), Zona Merah (Disiplin Mutlak)",
                },
                {
                    "id": "curve_card",
                    "type": "text",
                    "x": 350,
                    "y": 220,
                    "width": 300,
                    "height": 200,
                    "text": "<svg viewBox='0 0 100 100'><path d='M0 100 L100 0' /></svg>",
                },
            ],
            "edges": [],
        }
        result = self.validator.validate_v7_domain_content("04 - Peran Pendidik & Kedisiplinan.canvas", data_04)
        self.assertTrue(result.is_valid, msg=f"Errors: {result.errors}")

    def test_v7_sector_04_missing_languages(self) -> None:
        """V7 should fail Sektor 04 when parenting languages are missing."""
        incomplete_04 = {
            "nodes": [
                {
                    "id": "n1",
                    "type": "text",
                    "x": 0,
                    "y": 0,
                    "width": 100,
                    "height": 50,
                    "text": "Bahasa Hati dan Zona Hijau, Kuning, Merah | --- |",
                }
            ],
            "edges": [],
        }
        result = self.validator.validate_v7_domain_content("04 - Peran Pendidik & Kedisiplinan.canvas", incomplete_04)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("missing 3 Parenting Languages" in e.message for e in result.errors))

    def test_v7_inline_svg_malformed_xml_rejected(self) -> None:
        """V7 should reject canvases containing malformed inline SVG XML (e.g. unescaped &)."""
        bad_svg_canvas = {
            "nodes": [
                {
                    "id": "svg_node",
                    "type": "text",
                    "x": 0,
                    "y": 0,
                    "width": 200,
                    "height": 100,
                    "text": "<svg><text>Self Recovery (Doa & Istirahat)</text></svg>",
                }
            ],
            "edges": [],
        }
        result = self.validator.validate_v7_domain_content("06 - Implementasi & Rantai Kausalitas.canvas", bad_svg_canvas)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("contains malformed inline SVG XML" in e.message for e in result.errors))

    def test_v7_inline_svg_unmatched_tag_rejected(self) -> None:
        """V7 should reject canvases containing unclosed <svg> tags."""
        unclosed_svg_canvas = {
            "nodes": [
                {
                    "id": "unclosed_svg_node",
                    "type": "text",
                    "x": 0,
                    "y": 0,
                    "width": 200,
                    "height": 100,
                    "text": "<svg viewBox='0 0 100 100'><rect width='100' height='100'/>",
                }
            ],
            "edges": [],
        }
        result = self.validator.validate_v7_domain_content("06 - Implementasi & Rantai Kausalitas.canvas", unclosed_svg_canvas)
        self.assertFalse(result.is_valid)
        self.assertTrue(any("contains unmatched or unclosed '<svg' tag" in e.message for e in result.errors))

    def test_v7_inline_svg_well_formed_xml_accepted(self) -> None:
        """V7 should accept valid inline SVG with properly escaped entities."""
        valid_svg_canvas = {
            "nodes": [
                {
                    "id": "valid_svg_node",
                    "type": "text",
                    "x": 0,
                    "y": 0,
                    "width": 200,
                    "height": 100,
                    "text": "<svg viewBox='0 0 100 100'><text>Doa &amp; Istirahat</text></svg>",
                }
            ],
            "edges": [],
        }
        result = self.validator.validate_v7_domain_content("test.canvas", valid_svg_canvas)
        svg_errors = [e for e in result.errors if "SVG" in e.message]
        self.assertEqual(len(svg_errors), 0, f"Expected 0 SVG errors, got: {svg_errors}")

    # -------------------------------------------------------------------------
    # CLI Integration Test
    # -------------------------------------------------------------------------
    def test_cli_single_canvas_validation(self) -> None:
        """Test invoking verify_canvas_architecture.py directly via CLI."""
        with tempfile.NamedTemporaryFile(suffix=".canvas", mode="w", delete=False) as tf:
            tf.write(json.dumps({
                "nodes": [
                    {
                        "id": "c1",
                        "type": "text",
                        "x": 0,
                        "y": 0,
                        "width": 100,
                        "height": 50,
                        "text": "Valid Card",
                    }
                ],
                "edges": [],
            }))
            temp_path = tf.name

        try:
            cmd = [sys.executable, str(PROJECT_ROOT / "scripts" / "verify_canvas_architecture.py"), "--canvas", temp_path]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, msg=f"CLI failed: {proc.stdout}\n{proc.stderr}")
            self.assertIn("100% SUCCESS", proc.stdout)
        finally:
            Path(temp_path).unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)

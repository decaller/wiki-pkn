#!/usr/bin/env python3
"""
Benchmark and Validation Script for Unstructured API Integration in Wiki PKN.
Validates adapter parsing, HTML-to-Markdown table conversion, element transformation,
and checks Unstructured API endpoint availability.
"""

import sys
import json
import time
from pathlib import Path
from unstructured_adapter import UnstructuredAdapter, UnstructuredAPIError

def test_html_table_conversion():
    print("1. Testing HTML-to-Markdown table converter...")
    adapter = UnstructuredAdapter()
    sample_html = """
    <table>
        <tr><th>Pilar Bakat</th><th>Kutub Positif</th><th>Kutub Negatif</th></tr>
        <tr><td>01. Himmah</td><td>Visi Luhur & Semangat Tinggi</td><td>Ujub & Angkuh</td></tr>
        <tr><td>02. Syaja'ah</td><td>Keberanian Membela Kebenaran</td><td>Nekat & Ceroboh</td></tr>
    </table>
    """
    md = adapter.html_table_to_markdown(sample_html)
    assert "| Pilar Bakat | Kutub Positif | Kutub Negatif |" in md, "Header row missing"
    assert "| 01. Himmah | Visi Luhur & Semangat Tinggi | Ujub & Angkuh |" in md, "Row 1 missing"
    print("   ✓ Table conversion passed cleanly:")
    print("   ----------------------------------")
    for line in md.strip().split("\n"):
        print(f"   {line}")
    print("   ----------------------------------")


def test_element_transformation():
    print("\n2. Testing element-to-Markdown and LangChain Document transformer...")
    adapter = UnstructuredAdapter()
    mock_elements = [
        {"element_id": "e1", "type": "Title", "text": "Konsep Umum PKN", "metadata": {"page_number": 1}},
        {"element_id": "e2", "type": "NarrativeText", "text": "Pendidikan Karakter Nabawiyah berakar pada fitrah tauhid.", "metadata": {"page_number": 1}},
        {"element_id": "e3", "type": "ListItem", "text": "Pilar 1: Menundukkan nafsu", "metadata": {"page_number": 1}},
        {"element_id": "e4", "type": "ListItem", "text": "Pilar 2: Menghidupkan kalbu", "metadata": {"page_number": 1}},
        {
            "element_id": "e5",
            "type": "Table",
            "text": "Etape Usia: Thufulah (0-7), Tamyiz (7-10)",
            "metadata": {
                "page_number": 2,
                "text_as_html": "<table><tr><th>Etape</th><th>Rentang Usia</th></tr><tr><td>Thufulah</td><td>0-7 Tahun</td></tr></table>"
            }
        }
    ]

    md = adapter.elements_to_markdown(mock_elements)
    assert "## Konsep Umum PKN" in md, "Title heading missing"
    assert "* Pilar 1: Menundukkan nafsu" in md, "List item missing"
    assert "| Thufulah | 0-7 Tahun |" in md, "Table markdown missing"
    print("   ✓ Element-to-Markdown generation passed.")

    lc_docs = adapter.elements_to_langchain_documents(mock_elements, source_path="presentations/00-konsep-umum-pkn.pptx")
    assert len(lc_docs) == 5, f"Expected 5 langchain docs, got {len(lc_docs)}"
    assert lc_docs[0]["metadata"]["filename"] == "00-konsep-umum-pkn.pptx"
    assert lc_docs[0]["metadata"]["category"] == "Title"
    print(f"   ✓ LangChain schema conversion passed ({len(lc_docs)} chunks produced).")


def test_healthcheck():
    print("\n3. Testing Unstructured API Healthcheck Endpoint...")
    adapter = UnstructuredAdapter()
    health = adapter.check_health()
    print(f"   Target URL : {health.get('api_url')}")
    print(f"   Status     : {health.get('status').upper()}")
    if health.get("status") == "healthy":
        print(f"   Endpoint   : {health.get('endpoint')} (HTTP {health.get('status_code')})")
    else:
        print(f"   Note       : Container not currently running locally on port 8005 (expected before container launch).")
        print(f"   Info       : Jalankan 'docker compose -f docker-compose.unstructured.yml up -d' untuk menyalakan container.")


def main():
    print("=" * 60)
    print("WIKI PKN - UNSTRUCTURED API INTEGRATION BENCHMARK & TEST")
    print("=" * 60)
    test_html_table_conversion()
    test_element_transformation()
    test_healthcheck()
    print("\n" + "=" * 60)
    print("All unit and schema tests PASSED successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

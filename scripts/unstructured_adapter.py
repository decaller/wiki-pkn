#!/usr/bin/env python3
"""
Unstructured API Client Adapter for Wiki PKN.
Supports self-hosted Unstructured Docker API (default: http://localhost:8005)
and Unstructured Cloud API for multi-modal document extraction (PDF, PPTX, XLSX, DOCX).
"""

import os
import sys
import json
import uuid
import hashlib
import mimetypes
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
import urllib.request
import urllib.error

# Default Configuration
DEFAULT_API_URL = os.getenv("UNSTRUCTURED_API_URL", "http://localhost:8005/general/v0/general")
DEFAULT_API_KEY = os.getenv("UNSTRUCTURED_API_KEY", "")
DEFAULT_STRATEGY = os.getenv("UNSTRUCTURED_STRATEGY", "auto")


class UnstructuredAPIError(Exception):
    """Exception raised when Unstructured API returns an error or is unreachable."""
    pass


class UnstructuredAdapter:
    """Client adapter for interacting with Unstructured API."""

    def __init__(self, api_url: Optional[str] = None, api_key: Optional[str] = None, timeout: int = 120):
        self.api_url = (api_url or DEFAULT_API_URL).rstrip("/")
        self.api_key = api_key or DEFAULT_API_KEY
        self.timeout = timeout

        # Derive base URL for healthcheck
        if "/general/v0/general" in self.api_url:
            self.base_url = self.api_url.split("/general/v0/general")[0]
        else:
            self.base_url = self.api_url

    def check_health(self) -> Dict[str, Any]:
        """Check connection to Unstructured API."""
        health_endpoints = [
            f"{self.base_url}/healthcheck",
            f"{self.base_url}/general/v0/general/openapi.json",
            f"{self.base_url}/openapi.json"
        ]

        last_err = None
        for endpoint in health_endpoints:
            try:
                req = urllib.request.Request(endpoint, headers={"User-Agent": "wiki-pkn-adapter/1.0"})
                if self.api_key:
                    req.add_header("unstructured-api-key", self.api_key)
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status in (200, 204):
                        return {
                            "status": "healthy",
                            "endpoint": endpoint,
                            "status_code": response.status,
                            "api_url": self.api_url
                        }
            except Exception as e:
                last_err = e

        return {
            "status": "unreachable",
            "error": str(last_err),
            "api_url": self.api_url,
            "base_url": self.base_url
        }

    def partition_document(
        self,
        file_path: Union[str, Path],
        strategy: str = "auto",
        chunking_strategy: Optional[str] = "by_title",
        max_characters: int = 1500,
        new_after_n_chars: int = 1200,
        combine_text_under_n_chars: int = 200,
        languages: Optional[List[str]] = None,
        extract_image_block_types: Optional[List[str]] = None,
        include_page_breaks: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Send document to Unstructured API and return list of partitioned elements.
        """
        path = Path(file_path).resolve()
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path}")

        fields = {
            "strategy": strategy,
            "max_characters": str(max_characters),
            "new_after_n_chars": str(new_after_n_chars),
            "combine_text_under_n_chars": str(combine_text_under_n_chars),
            "include_page_breaks": "true" if include_page_breaks else "false",
        }

        if chunking_strategy:
            fields["chunking_strategy"] = chunking_strategy

        if languages:
            fields["languages"] = json.dumps(languages)
        else:
            # Default to Indonesian, Arabic, and English support
            fields["languages"] = json.dumps(["ind", "ara", "eng"])

        if extract_image_block_types:
            fields["extract_image_block_types"] = json.dumps(extract_image_block_types)

        with open(path, "rb") as f:
            file_bytes = f.read()

        mime_type, _ = mimetypes.guess_type(path.name)
        if not mime_type:
            mime_type = "application/octet-stream"

        boundary = f"----WebKitFormBoundary{uuid.uuid4().hex}"
        body = self._build_multipart_body(fields, path.name, file_bytes, mime_type, boundary)

        req = urllib.request.Request(
            self.api_url,
            data=body,
            headers={
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "Content-Length": str(len(body)),
                "User-Agent": "wiki-pkn-adapter/1.0"
            },
            method="POST"
        )

        if self.api_key:
            req.add_header("unstructured-api-key", self.api_key)

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                if response.status == 200:
                    resp_data = response.read().decode("utf-8")
                    elements = json.loads(resp_data)
                    return elements
                else:
                    raise UnstructuredAPIError(f"HTTP {response.status}: {response.read().decode('utf-8', errors='ignore')}")
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8", errors="ignore")
            raise UnstructuredAPIError(f"Unstructured API HTTP Error {e.code}: {err_msg}") from e
        except urllib.error.URLError as e:
            raise UnstructuredAPIError(f"Failed to connect to Unstructured API at {self.api_url}: {e.reason}") from e

    def _build_multipart_body(
        self,
        fields: Dict[str, str],
        filename: str,
        file_bytes: bytes,
        mime_type: str,
        boundary: str
    ) -> bytes:
        """Build multipart/form-data payload without third-party dependencies."""
        body = bytearray()
        boundary_bytes = f"--{boundary}\r\n".encode("utf-8")

        for key, val in fields.items():
            body.extend(boundary_bytes)
            body.extend(f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode("utf-8"))
            body.extend(f"{val}\r\n".encode("utf-8"))

        body.extend(boundary_bytes)
        body.extend(f'Content-Disposition: form-data; name="files"; filename="{filename}"\r\n'.encode("utf-8"))
        body.extend(f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"))
        body.extend(file_bytes)
        body.extend(b"\r\n")

        body.extend(f"--{boundary}--\r\n".encode("utf-8"))
        return bytes(body)

    @staticmethod
    def html_table_to_markdown(html_str: str) -> str:
        """Convert basic HTML table markup to GitHub Flavored Markdown table."""
        if not html_str:
            return ""

        # Extract rows
        rows_match = re.findall(r"<tr[^>]*>(.*?)</tr>", html_str, re.DOTALL | re.IGNORECASE)
        if not rows_match:
            return ""

        table_data = []
        for row in rows_match:
            cols = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.DOTALL | re.IGNORECASE)
            clean_cols = [re.sub(r"<[^>]+>", "", col).strip().replace("\n", " ") for col in cols]
            if clean_cols:
                table_data.append(clean_cols)

        if not table_data:
            return ""

        # Normalize column counts
        max_cols = max(len(r) for r in table_data)
        normalized = [r + [""] * (max_cols - len(r)) for r in table_data]

        header = normalized[0]
        md_lines = []
        md_lines.append("| " + " | ".join(header) + " |")
        md_lines.append("| " + " | ".join(["---"] * max_cols) + " |")

        for row in normalized[1:]:
            md_lines.append("| " + " | ".join(row) + " |")

        return "\n".join(md_lines)

    def extract_tables(self, elements: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract table elements with converted Markdown and HTML text."""
        tables = []
        for el in elements:
            if el.get("type") == "Table":
                metadata = el.get("metadata", {})
                html_table = metadata.get("text_as_html", "")
                md_table = self.html_table_to_markdown(html_table) if html_table else ""
                tables.append({
                    "element_id": el.get("element_id"),
                    "text": el.get("text", ""),
                    "html": html_table,
                    "markdown": md_table,
                    "page_number": metadata.get("page_number")
                })
        return tables

    def elements_to_markdown(self, elements: List[Dict[str, Any]]) -> str:
        """Convert elements stream into clean Markdown content."""
        lines = []
        for el in elements:
            el_type = el.get("type", "")
            text = (el.get("text") or "").strip()
            metadata = el.get("metadata", {})

            if not text and el_type != "PageBreak":
                continue

            if el_type == "Title":
                # Detect level by title length or metadata
                lines.append(f"\n## {text}\n")
            elif el_type == "Header":
                lines.append(f"\n### {text}\n")
            elif el_type == "Subheader":
                lines.append(f"\n#### {text}\n")
            elif el_type == "ListItem":
                lines.append(f"* {text}")
            elif el_type == "Table":
                html_table = metadata.get("text_as_html", "")
                md_table = self.html_table_to_markdown(html_table)
                if md_table:
                    lines.append(f"\n{md_table}\n")
                else:
                    lines.append(f"\n```\n{text}\n```\n")
            elif el_type in ("NarrativeText", "CompositeElement"):
                lines.append(f"\n{text}\n")
            elif el_type == "PageBreak":
                lines.append("\n---\n")
            else:
                lines.append(f"\n{text}\n")

        return "\n".join(lines).strip()

    def elements_to_langchain_documents(
        self,
        elements: List[Dict[str, Any]],
        source_path: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Convert elements into LangChain-compatible Document representation for RAG pipelines.
        """
        documents = []
        source_name = Path(source_path).name if source_path else "unknown"

        for el in elements:
            text = (el.get("text") or "").strip()
            if not text:
                continue

            metadata = el.get("metadata", {}).copy()
            metadata["element_id"] = el.get("element_id")
            metadata["category"] = el.get("type")
            if source_path:
                metadata["source"] = str(source_path)
                metadata["filename"] = source_name

            documents.append({
                "page_content": text,
                "metadata": metadata
            })

        return documents

    def build_hierarchical_narrative_graph(
        self,
        elements: List[Dict[str, Any]],
        source_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Build a Two-Layer Graph:
        1. Structural Hierarchy (Tree-of-Content / TOC)
        2. Horizontal Narrative Flow (Bidirectional chunk sequence: prev <-> next)
        Compatible with SurrealDB RELATE syntax.
        """
        source_name = Path(source_path).name if source_path else "document"
        doc_root_id = re.sub(r'[^a-zA-Z0-9_]', '_', Path(source_name).stem).lower()

        toc_nodes = [{
            "id": f"toc_{doc_root_id}_root",
            "title": source_name,
            "level": 0,
            "parent_id": None,
            "path": source_name
        }]

        toc_stack = [toc_nodes[0]]
        chunk_nodes = []
        relate_edges = []

        chunk_idx = 0
        for el in elements:
            el_type = el.get("type", "")
            text = (el.get("text") or "").strip()
            if not text:
                continue

            el_id = el.get("element_id") or f"el_{chunk_idx}"

            # 1. Structural TOC Node (Title/Header/Subheader)
            if el_type in ("Title", "Header", "Subheader"):
                level = 1 if el_type == "Title" else (2 if el_type == "Header" else 3)
                clean_title = re.sub(r'\s+', ' ', text)[:100]
                slug = re.sub(r'[^a-zA-Z0-9_]', '_', clean_title.lower())[:30]
                node_id = f"toc_{doc_root_id}_{slug}_{len(toc_nodes)}"

                # Adjust TOC stack based on level
                while len(toc_stack) > level:
                    toc_stack.pop()
                parent_toc = toc_stack[-1]

                toc_item = {
                    "id": node_id,
                    "title": clean_title,
                    "level": level,
                    "parent_id": parent_toc["id"],
                    "path": f"{parent_toc['path']} > {clean_title}"
                }
                toc_nodes.append(toc_item)
                toc_stack.append(toc_item)
                relate_edges.append({
                    "from": f"toc:{node_id}",
                    "rel": "part_of",
                    "to": f"toc:{parent_toc['id']}"
                })
            else:
                # 2. Sequential Narrative Chunk
                active_toc = toc_stack[-1]
                chunk_idx += 1
                chunk_id = f"c_{doc_root_id}_{chunk_idx}"

                chunk_item = {
                    "id": chunk_id,
                    "element_id": el_id,
                    "category": el_type,
                    "text": text,
                    "seq_index": chunk_idx,
                    "part_of_toc_id": active_toc["id"],
                    "toc_path": active_toc["path"],
                    "prev_chunk_id": f"c_{doc_root_id}_{chunk_idx - 1}" if chunk_idx > 1 else None,
                    "next_chunk_id": None
                }

                if chunk_nodes:
                    chunk_nodes[-1]["next_chunk_id"] = chunk_id
                    relate_edges.append({
                        "from": f"chunk:{chunk_nodes[-1]['id']}",
                        "rel": "next",
                        "to": f"chunk:{chunk_id}"
                    })
                    relate_edges.append({
                        "from": f"chunk:{chunk_id}",
                        "rel": "previous",
                        "to": f"chunk:{chunk_nodes[-1]['id']}"
                    })

                chunk_nodes.append(chunk_item)
                relate_edges.append({
                    "from": f"chunk:{chunk_id}",
                    "rel": "part_of",
                    "to": f"toc:{active_toc['id']}"
                })

        # Generate SurrealQL preview statements
        surrealql_lines = []
        for toc in toc_nodes:
            escaped_title = toc['title'].replace('"', '\\"')
            surrealql_lines.append(f'CREATE toc:{toc["id"]} SET title = "{escaped_title}", level = {toc["level"]}, path = "{toc["path"]}";')
        for chunk in chunk_nodes[:30]:
            clean_text = chunk['text'].replace('"', '\\"').replace('\n', ' ')[:300]
            surrealql_lines.append(f'CREATE chunk:{chunk["id"]} SET text = "{clean_text}", seq_index = {chunk["seq_index"]}, toc_id = "{chunk["part_of_toc_id"]}";')
        for edge in relate_edges[:30]:
            surrealql_lines.append(f"RELATE {edge['from']}->{edge['rel']}->{edge['to']};")

        return {
            "source": str(source_path) if source_path else source_name,
            "toc_count": len(toc_nodes),
            "chunk_count": len(chunk_nodes),
            "edges_count": len(relate_edges),
            "toc_nodes": toc_nodes,
            "chunk_nodes": chunk_nodes,
            "relate_edges": relate_edges,
            "surrealql_preview": surrealql_lines
        }


    def process_file_with_cache(
        self,
        file_path: Union[str, Path],
        output_dir: Union[str, Path] = "data/extracted_elements",
        force: bool = False,
        **partition_kwargs
    ) -> Dict[str, Any]:
        """Process document with MD5 caching to avoid re-parsing unchanged files."""
        path = Path(file_path).resolve()
        out_dir = Path(output_dir).resolve()
        out_dir.mkdir(parents=True, exist_ok=True)

        # Calculate file hash
        hasher = hashlib.md5()
        with open(path, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        file_hash = hasher.hexdigest()

        cache_file = out_dir / f"{path.stem}_{file_hash[:10]}.json"
        md_file = out_dir / f"{path.stem}_{file_hash[:10]}.md"

        if cache_file.exists() and not force:
            with open(cache_file, "r", encoding="utf-8") as f:
                cached = json.load(f)
            return {
                "source": str(path),
                "cached": True,
                "elements_count": len(cached.get("elements", [])),
                "json_path": str(cache_file),
                "markdown_path": str(md_file) if md_file.exists() else None,
                "data": cached
            }

        elements = self.partition_document(path, **partition_kwargs)
        tables = self.extract_tables(elements)
        markdown_content = self.elements_to_markdown(elements)
        langchain_docs = self.elements_to_langchain_documents(elements, source_path=str(path))
        hierarchical_graph = self.build_hierarchical_narrative_graph(elements, source_path=str(path))

        payload = {
            "file_name": path.name,
            "file_path": str(path),
            "file_hash": file_hash,
            "elements_count": len(elements),
            "tables_count": len(tables),
            "toc_nodes_count": hierarchical_graph.get("toc_count", 0),
            "elements": elements,
            "tables": tables,
            "langchain_documents": langchain_docs,
            "hierarchical_graph": hierarchical_graph
        }

        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        return {
            "source": str(path),
            "cached": False,
            "elements_count": len(elements),
            "tables_count": len(tables),
            "json_path": str(cache_file),
            "markdown_path": str(md_file),
            "data": payload
        }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Unstructured API Adapter for Wiki PKN")
    parser.add_argument("--check-health", action="store_true", help="Check Unstructured API health")
    parser.add_argument("--file", type=str, help="Process single file (PDF/PPTX/DOCX)")
    parser.add_argument("--batch-dir", type=str, help="Process directory of files")
    parser.add_argument("--output-dir", type=str, default="data/extracted_elements", help="Output directory")
    parser.add_argument("--strategy", type=str, default="auto", choices=["auto", "fast", "hi_res", "ocr_only"])
    parser.add_argument("--api-url", type=str, default=DEFAULT_API_URL, help="API URL")
    parser.add_argument("--force", action="store_true", help="Force re-processing ignoring cache")

    args = parser.parse_args()
    adapter = UnstructuredAdapter(api_url=args.api_url)

    if args.check_health:
        result = adapter.check_health()
        print(json.dumps(result, indent=2))
        sys.exit(0 if result.get("status") == "healthy" else 1)

    if args.file:
        print(f"Processing file: {args.file} (strategy={args.strategy})...")
        try:
            res = adapter.process_file_with_cache(
                args.file,
                output_dir=args.output_dir,
                strategy=args.strategy,
                force=args.force
            )
            print(f"Success! Elements: {res['elements_count']}, JSON: {res['json_path']}")
        except Exception as e:
            print(f"Error processing file: {e}", file=sys.stderr)
            sys.exit(1)
        return

    if args.batch_dir:
        input_path = Path(args.batch_dir)
        if not input_path.is_dir():
            print(f"Error: {args.batch_dir} is not a valid directory", file=sys.stderr)
            sys.exit(1)

        supported_exts = {".pdf", ".pptx", ".docx", ".xlsx"}
        files = [p for p in input_path.rglob("*") if p.suffix.lower() in supported_exts]
        print(f"Found {len(files)} files to process in {args.batch_dir}")

        success_count = 0
        for idx, f in enumerate(files, 1):
            print(f"[{idx}/{len(files)}] Processing {f.name}...")
            try:
                res = adapter.process_file_with_cache(f, output_dir=args.output_dir, strategy=args.strategy, force=args.force)
                print(f"  -> Elements: {res['elements_count']} (cached: {res['cached']})")
                success_count += 1
            except Exception as e:
                print(f"  -> Error: {e}", file=sys.stderr)

        print(f"Batch processing complete: {success_count}/{len(files)} succeeded.")
        return

    parser.print_help()


if __name__ == "__main__":
    main()

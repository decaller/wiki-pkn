#!/usr/bin/env python3
"""Index extracted PKN elements and retrieve traceable passages from Qdrant."""

import csv
import argparse
import hashlib
import json
import os
import urllib.request
from pathlib import Path
from uuid import UUID

try:
    from qdrant_client import QdrantClient, models
except ImportError:
    QdrantClient = None
    models = None

REGISTRY = Path(__file__).resolve().parents[1] / "data/sources_registry.csv"


def ollama_embeddings(texts, model, url):
    vectors = []
    for text in texts:
        request = urllib.request.Request(
            url.rstrip("/") + "/api/embed",
            json.dumps({"model": model, "input": text}).encode(),
            {"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=120) as response:
            vectors.append(json.load(response)["embeddings"][0])
    return vectors


def _uuid(value):
    digest = hashlib.sha256(value.encode()).hexdigest()[:32]
    return str(UUID(digest))


def _collection(client, name, model, dimensions):
    if not client.collection_exists(name):
        client.create_collection(name, vectors_config=models.VectorParams(size=dimensions, distance=models.Distance.COSINE))
    info = client.get_collection(name)
    config = info.config.params.vectors
    if config.size != dimensions:
        raise ValueError(f"Collection {name} has dimension {config.size}, expected {dimensions}")
    sample, _ = client.scroll(name, limit=1, with_payload=True, with_vectors=False)
    if sample and sample[0].payload.get("embedding_model") != model:
        raise ValueError(f"Collection {name} uses a different embedding model")


def index_files(client, paths, embed, collection, model, dimensions, source_id=None):
    """Upsert new points, then remove obsolete points for each source."""
    if not source_id:
        raise ValueError("A curated source_id is required for indexing")
    with REGISTRY.open(encoding="utf-8", newline="") as registry:
        known_ids = {row["source_id"] for row in csv.DictReader(registry)}
    if source_id not in known_ids:
        raise ValueError(f"Unknown source_id: {source_id}")
    paths = list(paths)
    if len(paths) != 1:
        raise ValueError("Index exactly one extracted document per curated source_id invocation")
    _collection(client, collection, model, dimensions)
    indexed = 0
    for path in paths:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        source = data["file_path"]
        if data.get("source_id") and data["source_id"] != source_id:
            raise ValueError(f"Conflicting source_id for {source}")
        rows = []
        for position, element in enumerate(data["elements"]):
            text = (element.get("text") or "").strip()
            if not text:
                continue
            metadata = element.get("metadata") or {}
            page = metadata.get("page_number")
            rows.append((position, text, page, element.get("type")))
        vectors = embed([row[1] for row in rows]) if rows else []
        if len(vectors) != len(rows) or any(len(vector) != dimensions for vector in vectors):
            raise ValueError(f"Invalid embedding dimensions for {source}")
        points = []
        for (position, text, page, kind), vector in zip(rows, vectors):
            points.append(models.PointStruct(
                id=_uuid(f"{source}:{position}"), vector=vector,
                payload={"source": source, "source_id": source_id, "page": page,
                         "category": kind, "text": text, "embedding_model": model,
                         "file_hash": data.get("file_hash")},
            ))
        old_ids = set()
        existing_ids = set()
        offset = None
        while True:
            batch, offset = client.scroll(collection, scroll_filter=models.Filter(
                must=[models.FieldCondition(key="source", match=models.MatchValue(value=source))]
            ), limit=256, offset=offset, with_payload=True, with_vectors=False)
            old_ids.update(point.id for point in batch)
            existing_ids.update(point.payload.get("source_id") for point in batch)
            if offset is None:
                break
        if existing_ids and existing_ids != {source_id}:
            raise ValueError(f"Source {source} already indexed under {existing_ids}; review attribution")
        if points:
            client.upsert(collection, points=points, wait=True)
        obsolete = old_ids - {point.id for point in points}
        if obsolete:
            client.delete(collection, points_selector=models.PointIdsList(points=list(obsolete)), wait=True)
        indexed += len(points)
    return indexed


def search(client, query, embed, collection, model, dimensions, limit=5):
    if not client.collection_exists(collection):
        raise ValueError(f"Collection {collection} has not been indexed")
    _collection(client, collection, model, dimensions)
    vector = embed([query])[0]
    if len(vector) != dimensions:
        raise ValueError("Invalid query embedding dimensions")
    hits = client.query_points(collection, query=vector, limit=limit, with_payload=True).points
    return [{"score": hit.score, "text": hit.payload["text"],
             "source_id": hit.payload.get("source_id"),
             "citation": hit.payload["source"] + (f"#page={hit.payload['page']}" if hit.payload.get("page") else "")}
            for hit in hits]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["index", "search"])
    parser.add_argument("query", nargs="?")
    parser.add_argument("--input", type=Path, help="One extracted JSON document; required for index")
    parser.add_argument("--source-id", help="Curated ID from data/sources_registry.csv; required for index")
    parser.add_argument("--collection", default="pkn_internal")
    parser.add_argument("--model", default="qwen3-embedding:0.6b")
    parser.add_argument("--dimensions", type=int, default=1024)
    parser.add_argument("--qdrant-url", default=os.getenv("QDRANT_URL", "http://127.0.0.1:6335"))
    parser.add_argument("--ollama-url", default=os.getenv("OLLAMA_URL", "http://127.0.0.1:11434"))
    args = parser.parse_args()
    client = QdrantClient(url=args.qdrant_url, api_key=os.getenv("QDRANT_API_KEY"))
    embed = lambda texts: ollama_embeddings(texts, args.model, args.ollama_url)
    if args.action == "index":
        if not args.source_id or not args.input or not args.input.is_file():
            parser.error("index requires one JSON file via --input and its curated --source-id")
        print(json.dumps({"indexed": index_files(client, [args.input], embed, args.collection, args.model, args.dimensions, args.source_id)}))
    else:
        if not args.query:
            parser.error("search requires a query")
        print(json.dumps(search(client, args.query, embed, args.collection, args.model, args.dimensions), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

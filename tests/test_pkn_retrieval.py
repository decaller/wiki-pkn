import json
import tempfile
import unittest
from pathlib import Path

try:
    from qdrant_client import QdrantClient
    HAS_QDRANT = True
except ImportError:
    HAS_QDRANT = False

from scripts.pkn_retrieval import index_files, search


@unittest.skipUnless(HAS_QDRANT, "qdrant_client is not installed in the current Python environment")
class PknRetrievalTests(unittest.TestCase):
    def test_changed_document_replaces_stale_chunks_and_preserves_citations(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "lesson.json"
            payload = {
                "file_path": "/archive/lesson.pdf", "file_hash": "first",
                "elements": [
                    {"text": "Anak belajar melalui bermain.", "element_id": "a", "type": "NarrativeText", "metadata": {"page_number": 2}},
                    {"text": "Materi lama yang harus hilang.", "element_id": "b", "type": "NarrativeText", "metadata": {"page_number": 3}},
                ],
            }
            source.write_text(json.dumps(payload))
            client = QdrantClient(":memory:")
            def embed(texts):
                return [[1.0, 0.0] if "bermain" in text else [0.0, 1.0] for text in texts]
            index_files(client, [source], embed, "pkn_test", "test-model", 2, "BOOK-PKN-CORE-MANHAJ")
            hits = search(client, "bermain", embed, "pkn_test", "test-model", 2)
            self.assertEqual(hits[0]["citation"], "/archive/lesson.pdf#page=2")
            payload["file_hash"] = "second"
            payload["elements"] = [payload["elements"][0]]
            source.write_text(json.dumps(payload))
            index_files(client, [source], embed, "pkn_test", "test-model", 2, "BOOK-PKN-CORE-MANHAJ")
            self.assertEqual(client.count("pkn_test", exact=True).count, 1)
            self.assertEqual(len(search(client, "lama", embed, "pkn_test", "test-model", 2)), 1)

    def test_rejects_model_mismatch_before_mutating_index(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "lesson.json"
            source.write_text(json.dumps({"file_path": "/archive/lesson.pdf", "file_hash": "a", "elements": [{"text": "Isi", "metadata": {}}]}))
            client = QdrantClient(":memory:")
            embed = lambda texts: [[1.0, 0.0] for _ in texts]
            index_files(client, [source], embed, "pkn_test", "model-a", 2, "BOOK-PKN-CORE-MANHAJ")
            with self.assertRaises(ValueError):
                index_files(client, [source], embed, "pkn_test", "model-b", 2, "BOOK-PKN-CORE-MANHAJ")
            self.assertEqual(client.count("pkn_test", exact=True).count, 1)

    def test_rejects_relabeling_an_indexed_source(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "lesson.json"
            source.write_text(json.dumps({"file_path": "/archive/lesson.pdf", "elements": [{"text": "Isi", "metadata": {}}]}))
            client = QdrantClient(":memory:")
            embed = lambda texts: [[1.0, 0.0] for _ in texts]
            index_files(client, [source], embed, "pkn_test", "model-a", 2, "BOOK-PKN-CORE-MANHAJ")
            with self.assertRaises(ValueError):
                index_files(client, [source], embed, "pkn_test", "model-a", 2, "PPTX-PRESENTATIONS")
            hits = search(client, "Isi", embed, "pkn_test", "model-a", 2)
            self.assertEqual(hits[0]["source_id"], "BOOK-PKN-CORE-MANHAJ")

    def test_search_does_not_create_an_empty_collection(self):
        client = QdrantClient(":memory:")
        with self.assertRaises(ValueError):
            search(client, "Isi", lambda texts: [[1.0, 0.0]], "missing", "model-a", 2)
        self.assertFalse(client.collection_exists("missing"))

    def test_unknown_registry_source_does_not_create_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "lesson.json"
            source.write_text(json.dumps({"file_path": "/archive/lesson.pdf", "elements": [{"text": "Isi"}]}))
            client = QdrantClient(":memory:")
            with self.assertRaises(ValueError):
                index_files(client, [source], lambda texts: [[1.0, 0.0]], "pkn_test", "model-a", 2, "NOT-IN-REGISTRY")
            self.assertFalse(client.collection_exists("pkn_test"))


if __name__ == "__main__":
    unittest.main()

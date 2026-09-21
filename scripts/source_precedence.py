#!/usr/bin/env python3
"""
source_precedence.py
Modul perhitungan bobot presedensi sumber, time decay, dan pelacakan relasi SUPERSEDES
berbasis registry data/sources_registry.csv.
"""

import csv
import math
import datetime
import os

REGISTRY_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sources_registry.csv")

class SourcePrecedenceManager:
    def __init__(self, registry_file=REGISTRY_PATH):
        self.sources = {}
        self.current_year = datetime.datetime.now().year
        self.load_registry(registry_file)

    def load_registry(self, path):
        if not os.path.exists(path):
            return
        with open(path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                s_id = row["source_id"].strip()
                self.sources[s_id] = {
                    "source_id": s_id,
                    "title": row.get("title", ""),
                    "source_type": row.get("source_type", "article"),
                    "tier": int(row.get("tier", 3)),
                    "base_tier_weight": float(row.get("base_tier_weight", 0.5)),
                    "published_year": int(row.get("published_year", self.current_year)),
                    "decay_rate_lambda": float(row.get("decay_rate_lambda", 0.1)),
                    "status": row.get("status", "active"),
                    "superseded_by": row.get("superseded_by", "").strip() or None,
                    "file_path_or_url": row.get("file_path_or_url", ""),
                    "author": row.get("author", ""),
                    "notes": row.get("notes", "")
                }

    def compute_effective_weight(self, source_id, reference_year=None):
        if source_id not in self.sources:
            # Default weight for unregistered source
            return 0.35, "unregistered"
        
        src = self.sources[source_id]
        if reference_year is None:
            reference_year = self.current_year
            
        base_w = src["base_tier_weight"]
        pub_year = src["published_year"]
        decay_lambda = src["decay_rate_lambda"]
        status = src["status"]
        superseded_by = src["superseded_by"]

        # Delta time in years (bounded to >= 0)
        delta_t = max(0, reference_year - pub_year)

        # For divine / timeless sources (decay_lambda == 0)
        if decay_lambda == 0.0 or src["source_type"] == "dalil_syari":
            time_decay = 1.0
        else:
            time_decay = math.exp(-decay_lambda * delta_t)

        effective_weight = base_w * time_decay

        # Penalty if superseded
        if status == "superseded" or superseded_by:
            effective_weight *= 0.5

        return round(effective_weight, 4), status

    def get_supersedes_lineage(self, source_id):
        """Trace forward to find if there is a modern superseding source."""
        lineage = []
        curr = source_id
        while curr and curr in self.sources:
            next_src = self.sources[curr].get("superseded_by")
            if next_src:
                lineage.append(next_src)
                curr = next_src
            else:
                break
        return lineage

    def format_frontmatter_source(self, source_id, specific_locator=None):
        """Format YAML frontmatter block with tier, authority, and lineage status."""
        if source_id not in self.sources:
            return f"- id: \"{source_id}\"\n  authority: 0.4"

        src = self.sources[source_id]
        eff_weight, status = self.compute_effective_weight(source_id)
        lineage = self.get_supersedes_lineage(source_id)

        lines = [
            f"- source_id: \"{source_id}\"",
            f"  title: \"{src['title']}\"",
            f"  tier: {src['tier']}",
            f"  effective_authority: {eff_weight}",
            f"  status: \"{status}\""
        ]
        if specific_locator:
            lines.append(f"  locator: \"{specific_locator}\"")
        if lineage:
            lines.append(f"  superseded_by: \"{lineage[-1]}\"")
        return "\n".join(lines)


if __name__ == "__main__":
    mgr = SourcePrecedenceManager()
    print("=== TEST SOURCE PRECEDENCE & DECAY CALCULATOR ===")
    for s_id, s_data in mgr.sources.items():
        w, status = mgr.compute_effective_weight(s_id)
        lineage = mgr.get_supersedes_lineage(s_id)
        sup_text = f" (Superseded by: {lineage[-1]})" if lineage else ""
        print(f"[{s_id}] Tier {s_data['tier']} | Base: {s_data['base_tier_weight']} -> Effective: {w} | Status: {status}{sup_text}")

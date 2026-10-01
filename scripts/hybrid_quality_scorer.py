#!/usr/bin/env python3
"""
Hybrid Quality Scorer: Rule-Based Linter & System One Cognitive Evaluator.
Integrates deterministic grammar/mechanics checks with fast cognitive/semantic
decision heads (Inverted Pyramid, Zero-Fluff, Hick's Law / Scannability).

Formula:
    Score = (w1 * S_linter) + (w2 * P_system_one)
    where w1 = 0.4, w2 = 0.6. Pass threshold: Score >= 70.0.
"""

import argparse
import json
import os
import re
import sys
import time
from typing import Any, Dict, List, Optional, Tuple


# --- PROHIBITED & CLICHE PHRASES ---
CLICHE_OPENERS = [
    re.compile(r"^\s*di\s+era\s+(globalisasi|modern|digital|teknologi|yang\s+serba\s+cepat)", re.IGNORECASE),
    re.compile(r"^\s*seperti\s+yang\s+(telah\s+)?kita\s+ketahui\s+bersama", re.IGNORECASE),
    re.compile(r"^\s*tidak\s+dapat\s+dipungkiri\s+lagi", re.IGNORECASE),
    re.compile(r"^\s*pada\s+zaman\s+sekarang\s+ini", re.IGNORECASE),
    re.compile(r"^\s*dewasa\s+ini,\s*", re.IGNORECASE),
    re.compile(r"^\s*dalam\s+kehidupan\s+sehari-hari\s+yang\s+serba\s+kompleks", re.IGNORECASE),
]

PROHIBITED_MANHAJ_TERMS = {
    "etape": "fase",
    "archetype": "uswah sahabat",
    "arketype": "uswah sahabat",
    "behavioral conditioning": "penumbuhan kesadaran beramal",
    "cliftonstrengths": "Tafsir Bakat 40 (TB-40)",
    "punishment": "ta'dib",
    "reward and punishment": "targhib wa tarhib",
    "parenting permisif": "tarbiyah wasathiyah",
    "parenting otoriter": "tarbiyah wasathiyah",
    "tabula rasa": "fitrah insan",
}

PASSIVE_VERB_REGEX = re.compile(r"\b(di[a-z]{3,}(kan|i|kanlah)?|ter[a-z]{3,})\b", re.IGNORECASE)
ACTIVE_VERB_REGEX = re.compile(r"\b(me[a-z]{3,}|ber[a-z]{3,})\b", re.IGNORECASE)


def strip_markdown(text: str) -> str:
    """Strip code blocks, YAML frontmatter, HTML, and markdown link formatting for analysis."""
    # Remove YAML frontmatter
    text = re.sub(r"^---[\s\S]*?---\n", "", text, flags=re.MULTILINE)
    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Remove wikilinks [[Target|Label]] -> Label
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    # Remove wikilinks [[Target]] -> Target
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    # Remove standard markdown links [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def extract_sentences(text: str) -> List[str]:
    """Split text into sentences while respecting periods and abbreviations."""
    clean = strip_markdown(text)
    # Split on period, question mark, exclamation mark followed by whitespace or newline
    raw_sentences = re.split(r"(?<=[.!?])\s+", clean)
    sentences = [s.strip() for s in raw_sentences if s.strip() and len(s.strip().split()) > 1]
    return sentences


def count_syllables(word: str) -> int:
    """Heuristic syllable count for Indonesian words."""
    word = word.lower()
    vowels = "aiueo"
    count = 0
    prev_is_vowel = False
    for char in word:
        is_vowel = char in vowels
        if is_vowel:
            count += 1
        prev_is_vowel = is_vowel
    return max(1, count)


# ==============================================================================
# LAPISAN 1: DETERMINISTIC RULE-BASED LINTER
# ==============================================================================
class RuleBasedLinter:
    """Evaluates formal mechanics, grammar, sentence lengths, and style guide."""

    def __init__(self, max_sentence_words: int = 25, max_passive_ratio: float = 0.25):
        self.max_sentence_words = max_sentence_words
        self.max_passive_ratio = max_passive_ratio

    def evaluate(self, raw_content: str) -> Dict[str, Any]:
        violations: List[Dict[str, Any]] = []
        clean_text = strip_markdown(raw_content)
        lines = raw_content.splitlines()

        # 1. Prohibited Manhaj Vocabulary
        for line_idx, line in enumerate(lines, start=1):
            lower_line = line.lower()
            for bad_term, suggestion in PROHIBITED_MANHAJ_TERMS.items():
                if bad_term in lower_line:
                    violations.append({
                        "line": line_idx,
                        "rule": "prohibited_manhaj_vocabulary",
                        "severity": "HIGH",
                        "message": f"Ditemukan istilah '{bad_term}', disarankan menggunakan '{suggestion}'.",
                        "snippet": line.strip()[:80]
                    })

        # 2. Sentence Length Check (> 25 words)
        sentences = extract_sentences(raw_content)
        total_words = 0
        total_syllables = 0
        long_sentence_count = 0

        for sentence in sentences:
            words = sentence.split()
            word_count = len(words)
            total_words += word_count
            total_syllables += sum(count_syllables(w) for w in words)

            if word_count > self.max_sentence_words:
                long_sentence_count += 1
                violations.append({
                    "line": None,
                    "rule": "sentence_length_max_25",
                    "severity": "MEDIUM",
                    "message": f"Kalimat memiliki {word_count} kata (batas ideal: {self.max_sentence_words} kata).",
                    "snippet": sentence[:90] + ("..." if len(sentence) > 90 else "")
                })

        # 3. Passive Voice Ratio
        words_list = clean_text.split()
        passive_count = sum(1 for w in words_list if PASSIVE_VERB_REGEX.match(w))
        active_count = sum(1 for w in words_list if ACTIVE_VERB_REGEX.match(w))
        total_verbs = passive_count + active_count
        passive_ratio = (passive_count / total_verbs) if total_verbs > 0 else 0.0

        if passive_ratio > self.max_passive_ratio and total_verbs >= 5:
            violations.append({
                "line": None,
                "rule": "excessive_passive_voice",
                "severity": "LOW",
                "message": f"Rasio kalimat pasif ({passive_ratio * 100:.1f}%) melebihi ambang batas {self.max_passive_ratio * 100:.0f}%.",
                "snippet": f"Pasif: {passive_count}, Aktif: {active_count}"
            })

        # 4. Readability Indices
        num_sentences = max(1, len(sentences))
        asl = total_words / num_sentences
        asw = (total_syllables / total_words) if total_words > 0 else 2.0

        # Calculate S_linter (0 - 100)
        score = 100.0
        # Penalties:
        # High severity (vocabulary): -10 pts each
        vocab_penalties = sum(15 for v in violations if v["rule"] == "prohibited_manhaj_vocabulary")
        # Long sentences: -3 pts each, capped at 30
        sentence_penalties = min(30, long_sentence_count * 3)
        # Passive ratio penalty: up to -10
        passive_penalty = 10 if (passive_ratio > self.max_passive_ratio and total_verbs >= 5) else 0

        score = max(0.0, score - vocab_penalties - sentence_penalties - passive_penalty)

        return {
            "score": round(score, 1),
            "violations": violations,
            "metrics": {
                "total_words": total_words,
                "total_sentences": num_sentences,
                "asl": round(asl, 1),
                "asw": round(asw, 2),
                "passive_ratio_pct": round(passive_ratio * 100, 1),
                "long_sentence_count": long_sentence_count
            }
        }


# ==============================================================================
# LAPISAN 2: SYSTEM ONE DECISION HEAD (SEMANTIC & COGNITIVE)
# ==============================================================================
class SystemOneDecisionHead:
    """Fast semantic/cognitive classification head (Inverted Pyramid, Zero-Fluff, Hick's Law)."""

    def evaluate(self, raw_content: str) -> Dict[str, Any]:
        clean_text = strip_markdown(raw_content)
        lines = [line.strip() for line in raw_content.splitlines() if line.strip()]

        # 1. Inverted Pyramid Check
        # Inspect top 3 non-empty blocks / callouts
        pyramid_decision, pyramid_score, pyramid_note = self._check_inverted_pyramid(raw_content, lines)

        # 2. Zero-Fluff / Objectivity Score
        fluff_decision, fluff_score, fluff_note = self._check_zero_fluff(raw_content, lines)

        # 3. Hick's Law / Scannability Check
        scannability_decision, scannability_score, scannability_note = self._check_scannability(raw_content)

        # Composite Probability P_system_one (0 - 100)
        p_system_one = round(((pyramid_score + fluff_score + scannability_score) / 3.0) * 100.0, 1)

        return {
            "score": p_system_one,
            "decisions": {
                "inverted_pyramid": pyramid_decision,
                "zero_fluff": fluff_decision,
                "scannability": scannability_decision
            },
            "scores": {
                "inverted_pyramid": round(pyramid_score, 2),
                "zero_fluff": round(fluff_score, 2),
                "scannability": round(scannability_score, 2)
            },
            "notes": {
                "inverted_pyramid": pyramid_note,
                "zero_fluff": fluff_note,
                "scannability": scannability_note
            }
        }

    def _check_inverted_pyramid(self, raw: str, lines: List[str]) -> Tuple[str, float, str]:
        """Check if definition, summary, or core answer appears in the top section."""
        # Has SUMMARY/TLDR callout at the beginning
        has_summary_callout = bool(re.search(r"> ?\[!(SUMMARY|NOTE|INFO|TLDR|RINGKASAN)", raw, re.IGNORECASE))
        if has_summary_callout:
            return "Yes", 1.0, "Paragraf pembuka memuat callout TL;DR / Ringkasan Eksekutif."

        # Check the first 2 content paragraphs after H1
        first_content = ""
        found_h1 = False
        for line in lines:
            if line.startswith("# "):
                found_h1 = True
                continue
            if found_h1 and not line.startswith("#") and not line.startswith("---") and len(line) > 20:
                first_content = line
                break

        if not first_content and lines:
            first_content = lines[0]

        # Check if first content defines the subject ("adalah", "merupakan", "yaitu", "fase di mana")
        is_definitive = bool(re.search(r"\b(adalah|merupakan|ialah|yaitu|yakni|merujuk pada|berarti)\b", first_content, re.IGNORECASE))
        if is_definitive:
            return "Yes", 0.9, "Paragraf awal memuat definisi pokok secara langsung."
        elif len(first_content.split()) > 10:
            return "Weak", 0.5, "Paragraf awal kurang menegaskan definisi atau jawaban inti secara eksplisit."
        else:
            return "No", 0.0, "Dokumen tidak diawali dengan jawaban langsung atau ringkasan pembuka."

    def _check_zero_fluff(self, raw: str, lines: List[str]) -> Tuple[str, float, str]:
        """Check for rhetorical filler, clichés, or self-indulgent preambles."""
        fluff_found = []
        for line in lines[:10]:
            for pattern in CLICHE_OPENERS:
                if pattern.search(line):
                    fluff_found.append(line)

        if not fluff_found:
            return "Clean", 1.0, "Nihil basa-basi pengantar klise (Zero-Fluff terpenuhi)."
        elif len(fluff_found) == 1:
            return "Moderate Fluff", 0.5, f"Ditemukan 1 pembuka klise retoris: '{fluff_found[0][:50]}...'"
        else:
            return "Heavy Fluff", 0.0, f"Ditemukan {len(fluff_found)} pembuka klise retoris yang membebani pembaca."

    def _check_scannability(self, raw: str) -> Tuple[str, float, str]:
        """Evaluate Hick's law: chunking, micro-headings, bullet lists, tables, callouts."""
        paragraphs = [p.strip() for p in raw.split("\n\n") if p.strip() and not p.strip().startswith("#")]
        long_paragraphs = 0
        for p in paragraphs:
            sentences = re.split(r"[.!?]\s+", p)
            if len(sentences) > 5 and len(p.split()) > 90:
                long_paragraphs += 1

        has_headings = bool(re.search(r"^#{2,4}\s", raw, re.MULTILINE))
        has_lists = bool(re.search(r"^\s*[-*0-9.]\s", raw, re.MULTILINE))
        has_tables_or_callouts = ("|" in raw) or ("> [!" in raw)

        # Scannability criteria
        score = 1.0
        notes = []

        if long_paragraphs > 2:
            score -= 0.4
            notes.append(f"{long_paragraphs} paragraf terlalu panjang (dinding teks)")
        if not has_headings and len(raw.split()) > 200:
            score -= 0.3
            notes.append("Kurang sub-heading (H2/H3)")
        if not (has_lists or has_tables_or_callouts):
            score -= 0.3
            notes.append("Tidak ada elemen penguat pindai (tabel/daftar/callout)")

        score = max(0.0, score)
        if score >= 0.8:
            return "Optimized", 1.0, "Struktur pemecahan blok, heading, dan daftar sangat ramah pemindaian."
        else:
            desc = ", ".join(notes) if notes else "Kepadatan teks terlalu tinggi"
            return "Cluttered", score, f"Tampilan padat: {desc}."


# ==============================================================================
# LAPISAN 3: AGGREGATOR & SCORING ENGINE
# ==============================================================================
class HybridQualityScorer:
    """Combines Rule-Based Linter (Layer 1) and System One Model (Layer 2)."""

    def __init__(self, w1: float = 0.4, w2: float = 0.6, pass_threshold: float = 70.0):
        self.w1 = w1
        self.w2 = w2
        self.pass_threshold = pass_threshold
        self.linter = RuleBasedLinter()
        self.system_one = SystemOneDecisionHead()

    def evaluate_document(self, content: str, file_path: str = "document.md") -> Dict[str, Any]:
        t0 = time.perf_counter()

        linter_res = self.linter.evaluate(content)
        system_one_res = self.system_one.evaluate(content)

        s_linter = linter_res["score"]
        p_system_one = system_one_res["score"]

        # Mathematical score formula: Score = (w1 * S_linter) + (w2 * P_system_one)
        overall_score = round((self.w1 * s_linter) + (self.w2 * p_system_one), 1)
        status = "APPROVED" if overall_score >= self.pass_threshold else "NEEDS_REVISION"

        # Formulate actionable feedback
        actionable_feedback: List[str] = []

        # Feedback from Layer 1
        for viol in linter_res["violations"]:
            if viol["rule"] == "prohibited_manhaj_vocabulary":
                actionable_feedback.append(f"Ganti istilah non-manhaj: {viol['message']}")
            elif viol["rule"] == "sentence_length_max_25":
                actionable_feedback.append(f"Pecah kalimat panjang: \"{viol['snippet']}\"")
            elif viol["rule"] == "excessive_passive_voice":
                actionable_feedback.append(f"Kurangi kalimat pasif ({linter_res['metrics']['passive_ratio_pct']}%). Gunakan kalimat aktif.")

        # Feedback from Layer 2
        if system_one_res["decisions"]["inverted_pyramid"] in ["No", "Weak"]:
            actionable_feedback.append("Terapkan Piramida Terbalik: Letakkan intisari/definisi utama di kalimat/paragraf pertama (atau pasang callout [!SUMMARY]).")
        if system_one_res["decisions"]["zero_fluff"] != "Clean":
            actionable_feedback.append("Terapkan Zero-Fluff: Hapus kalimat basa-basi pengantar klise di awal dokumen.")
        if system_one_res["decisions"]["scannability"] == "Cluttered":
            actionable_feedback.append(f"Terapkan Scannability: {system_one_res['notes']['scannability']}")

        # Deduplicate actionable feedback while preserving order
        unique_feedback = list(dict.fromkeys(actionable_feedback))

        duration_ms = round((time.perf_counter() - t0) * 1000, 2)

        return {
            "document_path": file_path,
            "execution_time_ms": duration_ms,
            "overall_score": overall_score,
            "pass_threshold": self.pass_threshold,
            "status": status,
            "weights": {"w1_linter": self.w1, "w2_system_one": self.w2},
            "layers": {
                "layer_1_linter": linter_res,
                "layer_2_system_one": system_one_res
            },
            "actionable_feedback": unique_feedback
        }


def format_cli_report(res: Dict[str, Any]) -> str:
    """Format evaluation result for readable CLI output."""
    status_icon = "✅" if res["status"] == "APPROVED" else "❌"
    lines = [
        "=" * 70,
        f"⚡ HYBRID QUALITY SCORER (Rule-Based Linter + System One Head)",
        f"File: {res['document_path']} | Waktu: {res['execution_time_ms']} ms",
        "=" * 70,
        f"Status Akhir: {status_icon} {res['status']} (Skor: {res['overall_score']} / 100.0 | Batas: {res['pass_threshold']})",
        f"Formula: ({res['weights']['w1_linter']} * Linter: {res['layers']['layer_1_linter']['score']}) + "
        f"({res['weights']['w2_system_one']} * System One: {res['layers']['layer_2_system_one']['score']})",
        "-" * 70,
        "📋 KEPUTUSAN TERSTRUKTUR SYSTEM ONE:",
        f"  • Inverted Pyramid : {res['layers']['layer_2_system_one']['decisions']['inverted_pyramid']} ({res['layers']['layer_2_system_one']['notes']['inverted_pyramid']})",
        f"  • Zero-Fluff       : {res['layers']['layer_2_system_one']['decisions']['zero_fluff']} ({res['layers']['layer_2_system_one']['notes']['zero_fluff']})",
        f"  • Scannability     : {res['layers']['layer_2_system_one']['decisions']['scannability']} ({res['layers']['layer_2_system_one']['notes']['scannability']})",
        "-" * 70,
        "🔍 METRIK LAPISAN 1 (LINTER):",
        f"  • Panjang Kalimat Rata-rata (ASL): {res['layers']['layer_1_linter']['metrics']['asl']} kata",
        f"  • Kalimat > 25 Kata             : {res['layers']['layer_1_linter']['metrics']['long_sentence_count']} kalimat",
        f"  • Rasio Kalimat Pasif           : {res['layers']['layer_1_linter']['metrics']['passive_ratio_pct']}%",
        f"  • Total Pelanggaran             : {len(res['layers']['layer_1_linter']['violations'])} item",
    ]

    if res["actionable_feedback"]:
        lines.append("-" * 70)
        lines.append("🛠️ CATATAN PERBAIKAN SPESIFIK (ACTIONABLE FEEDBACK):")
        for idx, fb in enumerate(res["actionable_feedback"], start=1):
            lines.append(f"  {idx}. {fb}")

    lines.append("=" * 70)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Hybrid Quality Scorer for Wiki-PKN Documents")
    parser.add_argument("--file", help="Path to markdown document to evaluate")
    parser.add_argument("--text", help="Raw text string to evaluate")
    parser.add_argument("--dir", help="Audit all markdown files in directory")
    parser.add_argument("--json-out", help="Write evaluation output as JSON")
    parser.add_argument("--min-score", type=float, default=70.0, help="Minimum pass score threshold (default: 70.0)")
    args = parser.parse_args()

    scorer = HybridQualityScorer(pass_threshold=args.min_score)

    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File '{args.file}' not found.")
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        res = scorer.evaluate_document(content, file_path=args.file)
        print(format_cli_report(res))
        if args.json_out:
            with open(args.json_out, "w", encoding="utf-8") as jf:
                json.dump(res, jf, indent=2, ensure_ascii=False)
        sys.exit(0 if res["status"] == "APPROVED" else 1)

    elif args.text:
        res = scorer.evaluate_document(args.text, file_path="<raw_input>")
        print(format_cli_report(res))
        sys.exit(0 if res["status"] == "APPROVED" else 1)

    elif args.dir:
        results = []
        pass_count = 0
        fail_count = 0
        t_start = time.perf_counter()

        for root, _, files in os.walk(args.dir):
            for file in files:
                if file.endswith(".md"):
                    p = os.path.join(root, file)
                    with open(p, "r", encoding="utf-8") as f:
                        text = f.read()
                    res = scorer.evaluate_document(text, file_path=p)
                    results.append(res)
                    if res["status"] == "APPROVED":
                        pass_count += 1
                    else:
                        fail_count += 1

        total_time = round(time.perf_counter() - t_start, 2)
        avg_score = round(sum(r["overall_score"] for r in results) / max(1, len(results)), 1)
        print(f"Batch audit selesai: {len(results)} berkas dalam {total_time}s")
        print(f"Lulus (Score ≥ {args.min_score}): {pass_count}/{len(results)} ({(pass_count/max(1, len(results)))*100:.1f}%) | Rata-rata Skor: {avg_score}")

        if args.json_out:
            with open(args.json_out, "w", encoding="utf-8") as jf:
                json.dump({"summary": {"total": len(results), "passed": pass_count, "failed": fail_count, "average_score": avg_score}, "files": results}, jf, indent=2, ensure_ascii=False)
        sys.exit(0 if fail_count == 0 else 1)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

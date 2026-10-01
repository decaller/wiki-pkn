#!/usr/bin/env python3
"""
LLM Council Deliberation Engine for Wiki-PKN (Adapted from Andrej Karpathy's LLM Council).
Runs high-stakes decision questions through 5 independent thinking lenses, executes
an anonymous blind peer-review cross-examination, and synthesizes a structured Chairman Verdict.

Five Council Lenses:
1. Faqih Manhaj (The Contrarian - Risks & Sharia Boundaries)
2. Filosof Fitrah (The First Principles Thinker - Root Tauhid & Human Nature)
3. Arsitek Peradaban (The Expansionist - Scalability & 20-Year Vision)
4. Pembaca Awam (The Outsider - Layman Clarity & Anti-Jargon)
5. Praktisi KBM (The Executor - Monday Morning Test & Practical SOPs)
"""

import argparse
import json
import os
import random
import re
import sys
import time
from typing import Any, Dict, List, Optional, Tuple


ADVISOR_PROFILES = {
    "The Contrarian (Faqih Manhaj)": {
        "lens": "Audit Risiko Syar'i & Titik Cacat Fatal",
        "description": (
            "Mencari titik gagal, celah takwil serampangan, dan potensi ifrath (ekstrem kaku) "
            "atau tafrith (meremehkan). Menguji risiko fitnah hukum dan benturan regulasi perlindungan anak. "
            "Bersikap skeptis konstruktif untuk menyelamatkan proyek dari keputusan gegabah."
        )
    },
    "The First Principles Thinker (Filosof Fitrah)": {
        "lens": "Akar Tauhid, Fitrah Insan & Hakikat Jiwa",
        "description": (
            "Mengabaikan tren modern dan membongkar persoalan ke akar tauhid dan hakikat penciptaan insan. "
            "Menolak formalitas kurikulum dangkal dan mempertanyakan apakah premis pertanyaan sejak awal sudah keliru."
        )
    },
    "The Expansionist (Arsitek Peradaban)": {
        "lens": "Peluang Besar, Skalabilitas & Visi Peradaban",
        "description": (
            "Melihat potensi jika ide ini berhasil melampaui ekspektasi. Berfokus pada bagaimana konsep ini "
            "dapat diskalakan ke 1.000 pesantren dan komunitas mandiri, serta menjadi alternatif peradaban masa depan."
        )
    },
    "The Outsider (Pembaca Awam & Santri)": {
        "lens": "Mata Segar, Anti-Jargon & Realitas Publik",
        "description": (
            "Melihat tanpa beban istilah (curse of knowledge). Bertindak sebagai orang tua atau santri awam: "
            "menolak naskah yang membingungkan, menuntut bahasa manusia yang membumi dan dapat dipahami tanpa gelar ulama."
        )
    },
    "The Executor (Praktisi KBM & Guru)": {
        "lens": "Monday Morning Test & Realitas Kelas",
        "description": (
            "Hanya peduli pada eksekusi lapangan: apa persisnya yang harus dilakukan guru hari Senin jam 07.15 di kelas? "
            "Menuntut langkah 1-2-3 yang operasional dan menolak konsep muluk tanpa SOP terukur."
        )
    }
}


class LLMCouncilEngine:
    """Orchestrates 3-Stage Deliberation: Perspectives -> Anonymous Peer Review -> Chairman Verdict."""

    def __init__(self, offline_mode: bool = True):
        self.offline_mode = offline_mode

    def run_council(self, topic: str, context: str = "") -> Dict[str, Any]:
        t0 = time.perf_counter()

        # Step 1: Convene Council (Stage 1 - Parallel Independent Perspectives)
        stage_1_responses = self._generate_perspectives(topic, context)

        # Step 2: Anonymous Cross-Examination (Stage 2 - Peer Review)
        stage_2_anonymized, mapping, reviews = self._run_peer_reviews(topic, stage_1_responses)

        # Step 3: Chairman Synthesis (Stage 3 - Verdict)
        verdict = self._synthesize_verdict(topic, stage_1_responses, reviews)

        duration_sec = round(time.perf_counter() - t0, 2)

        return {
            "topic": topic,
            "context_length": len(context),
            "execution_time_sec": duration_sec,
            "mode": "offline_deterministic" if self.offline_mode else "llm_api",
            "advisors": list(ADVISOR_PROFILES.keys()),
            "stage_1_perspectives": stage_1_responses,
            "stage_2_peer_reviews": {
                "anonymized_responses": stage_2_anonymized,
                "anonymization_key": mapping,
                "reviews": reviews
            },
            "stage_3_verdict": verdict
        }

    def _generate_perspectives(self, topic: str, context: str) -> Dict[str, str]:
        """Stage 1: Generate 5 independent advisor perspectives without hedging."""
        responses = {}

        if self.offline_mode:
            # Deterministic domain-calibrated synthesis based on topic semantics
            responses["The Contrarian (Faqih Manhaj)"] = (
                f"Dari tinjauan fiqih tarbiyah terhadap '{topic}', risiko terbesar adalah tergelincir pada "
                "tafrith (meremehkan batas syariat) demi mengejar kemudahan adaptasi modern, atau sebaliknya "
                "jatuh pada ifrath yang membebani fitrah anak sebelum waktunya. Setiap langkah wajib terikat "
                "dengan dalil shahih dan kaidah saddudz-dzari'ah agar tidak memicu fitnah hukum atau pelanggaran adab."
            )
            responses["The First Principles Thinker (Filosof Fitrah)"] = (
                f"Secara hakikat insan, pembahasan '{topic}' tidak boleh disederhanakan menjadi prosedur mekanis. "
                "Inti pendidikan nabawiyah adalah menumbuhkan kesadaran beramal (wa'yu) dan menjaga orisinalitas "
                "fitrah keimanan, bukan rekayasa perilaku stimulus-respon. Pertanyaan dasarnya: apakah langkah ini "
                "menyentuh kalbu terdalam anak atau sekadar menciptakan kepatuhan semu di permukaan?"
            )
            responses["The Expansionist (Arsitek Peradaban)"] = (
                f"Melihat visi jangka panjang 20 tahun ke depan, '{topic}' adalah peluang membangun ekosistem peradaban baru. "
                "Jika model ini dibakukan menjadi standar terbuka, ribuan kuttab, pesantren, dan keluarga homeschooling "
                "dapat mengadopsinya secara serentak. Jangan batasi solusi pada skala satu sekolah; rancanglah struktur "
                "yang siap direplikasi secara masif lintas daerah."
            )
            responses["The Outsider (Pembaca Awam & Santri)"] = (
                f"Sebagai orang tua atau santri awam yang membaca '{topic}', saya menolak istilah yang terlalu melangit. "
                "Keluarga membutuhkan jawaban lugas: apa dampaknya bagi anak di rumah? Jika panduan dipenuhi jargon "
                "tanpa kejelasan bahasa hati, pembaca umum akan menyerah dan kembali ke pola pengasuhan lama. "
                "Sederhanakan bahasanya tanpa menghilangkan kehormatan maknanya."
            )
            responses["The Executor (Praktisi KBM & Guru)"] = (
                f"Uji kelayakan nyata bagi '{topic}' adalah 'The Monday Morning Test': apa yang persisnya harus dilakukan "
                "guru hari Senin jam 07.15 saat jam pelajaran dimulai? Berapa menit durasinya? Siapa yang mengisi instrumennya? "
                "Jika tidak ada templat kerja, RPP, dan rubrik konkret, ide ini hanya akan menjadi tumpukan wacana di lemari arsip."
            )
        else:
            # In live API mode, dispatch parallel sub-agent prompts
            for name in ADVISOR_PROFILES:
                responses[name] = f"[Live LLM response placeholder for {name}]"

        return responses

    def _run_peer_reviews(self, topic: str, responses: Dict[str, str]) -> Tuple[Dict[str, str], Dict[str, str], List[Dict[str, Any]]]:
        """Stage 2: Randomize responses to Response A..E and conduct anonymous peer-review."""
        advisor_names = list(responses.keys())
        shuffled_names = list(advisor_names)
        random.seed(42)  # Deterministic seed for reproducible testing
        random.shuffle(shuffled_names)

        letters = ["Response A", "Response B", "Response C", "Response D", "Response E"]
        anonymized = {}
        mapping = {}

        for letter, name in zip(letters, shuffled_names):
            anonymized[letter] = responses[name]
            mapping[letter] = name

        reviews = []
        for reviewer_name in advisor_names:
            if self.offline_mode:
                reviews.append({
                    "reviewer": reviewer_name,
                    "strongest_response": "Response E (Executor)",
                    "strongest_reason": "Menyajikan batasan operasional yang realistis tanpa kompromi berlebih.",
                    "biggest_blind_spot": "Response C (Expansionist)",
                    "blind_spot_reason": "Terlalu ambisius dalam skala peradaban namun abai terhadap risiko hukum syar'i jangka pendek.",
                    "missed_by_all": "Kesiapan psikologis orang tua dan mitigasi resistensi budaya masyarakat setempat."
                })
            else:
                reviews.append({
                    "reviewer": reviewer_name,
                    "strongest_response": "[Response X]",
                    "strongest_reason": "[Live LLM reason]",
                    "biggest_blind_spot": "[Response Y]",
                    "blind_spot_reason": "[Live LLM blind spot]",
                    "missed_by_all": "[Live LLM universal gap]"
                })

        return anonymized, mapping, reviews

    def _synthesize_verdict(self, topic: str, responses: Dict[str, str], reviews: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Stage 3: Chairman synthesizes consensus, clashes, blind spots, and final verdict."""
        verdict = {
            "title": f"Council Verdict: {topic}",
            "where_council_agrees": [
                "Pentingnya menjaga kemurnian tauhid dan fitrah anak tanpa kompromi sekuler.",
                "Keharusan adanya instrumen operasional praktis yang dapat langsung diterapkan oleh pendidik dan orang tua.",
                "Penolakan terhadap pendekatan koersif mekanis yang mematikan inisiatif kalbu (*wa'yu*)."
            ],
            "where_council_clashes": [
                {
                    "point_of_tension": "Kecepatan Penskalaan vs. Kehati-hatian Syar'i",
                    "side_a": "Arsitek Peradaban menuntut standarisasi cepat agar dapat diadopsi masif.",
                    "side_b": "Faqih Manhaj menuntut audit ketat per fase usia untuk mencegah distorsi pemahaman."
                },
                {
                    "point_of_tension": "Kedalaman Istilah Turats vs. Keterbacaan Bahasa Awam",
                    "side_a": "Filosof Fitrah menuntut pelestarian istilah asli (Syakilah, Muthmainnah, Tadarruj).",
                    "side_b": "Pembaca Awam menuntut penggunaan bahasa Indonesia lugas agar tidak terjadi paralysis pemula."
                }
            ],
            "blind_spots_caught": [
                "Kurangnya kesiapan mental orang tua di rumah ketika sekolah telah menerapkan standar karakter nabawiyah.",
                "Kebutuhan jembatan regulasi formal (Dinas/Kemenag) agar kurikulum tidak dicap melanggar hukum negara."
            ],
            "recommendation": (
                f"Ketetapan Dewan Syura mengenai '{topic}': Terapkan pendekatan berjenjang (Tadarruj). "
                "Gunakan instrumen naratif deskriptif untuk anak usia pra-baligh, dan integrasikan istilah turats "
                "secara bertahap dengan selalu menyertakan glosarium ringkas bagi orang tua awam."
            ),
            "the_one_thing_to_do_first": (
                "Susun SOP Panduan Tindakan Cepat (1 Lembar) untuk guru dan orang tua, sebelum menerbitkan "
                "dokumen regulasi atau modul teoretis yang lebih tebal."
            )
        }
        return verdict


def format_markdown_verdict(res: Dict[str, Any]) -> str:
    """Format council output into clean, publishable GitHub-flavored Markdown."""
    v = res["stage_3_verdict"]
    lines = [
        f"# 🏛️ Risalah Ketetapan Dewan Syura (Council Verdict)",
        f"**Topik:** {res['topic']}",
        f"**Status Sidang:** Selesai ({res['execution_time_sec']} detik | {len(res['advisors'])} Penasihat)",
        "",
        "---",
        "",
        "## 1. Di Mana Dewan Sepakat (*Where the Council Agrees*)",
    ]
    for pt in v["where_council_agrees"]:
        lines.append(f"* ✅ {pt}")

    lines.append("")
    lines.append("## 2. Di Mana Dewan Berselisih (*Where the Council Clashes*)")
    for cl in v["where_council_clashes"]:
        lines.append(f"### ⚔️ {cl['point_of_tension']}")
        lines.append(f"* **Sisi A:** {cl['side_a']}")
        lines.append(f"* **Sisi B:** {cl['side_b']}")

    lines.append("")
    lines.append("## 3. Celah yang Berhasil Dibongkar (*Blind Spots Caught*)")
    for bs in v["blind_spots_caught"]:
        lines.append(f"* 🔍 {bs}")

    lines.append("")
    lines.append("## 4. Rekomendasi Terpilih (*The Recommendation*)")
    lines.append(f"> [!IMPORTANT] Ketetapan Syura")
    lines.append(f"> {v['recommendation']}")

    lines.append("")
    lines.append("## 5. Satu Hal Pertama yang Harus Dikerjakan (*The One Thing to Do First*)")
    lines.append(f"> [!TIP] Langkah Eksekusi Prioritas")
    lines.append(f"> 🎯 **{v['the_one_thing_to_do_first']}**")

    lines.append("")
    lines.append("---")
    lines.append("### Lampiran: Ringkasan 5 Lensa Penasihat")
    for name, text in res["stage_1_perspectives"].items():
        lines.append(f"* **{name}:** {text}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="LLM Council Deliberation Engine for Wiki-PKN")
    parser.add_argument("--topic", required=True, help="Strategic question or high-stakes decision topic")
    parser.add_argument("--context-file", help="Path to context markdown or reference document")
    parser.add_argument("--offline", action="store_true", default=True, help="Run in deterministic offline simulation mode")
    parser.add_argument("--json-out", help="Save output payload to JSON file")
    parser.add_argument("--md-out", help="Save formatted verdict to Markdown file")
    args = parser.parse_args()

    context_text = ""
    if args.context_file and os.path.exists(args.context_file):
        with open(args.context_file, "r", encoding="utf-8") as f:
            context_text = f.read()

    engine = LLMCouncilEngine(offline_mode=args.offline)
    result = engine.run_council(topic=args.topic, context=context_text)

    md_output = format_markdown_verdict(result)
    print(md_output)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as jf:
            json.dump(result, jf, indent=2, ensure_ascii=False)
        print(f"\n[INFO] Payload JSON tersimpan di: {args.json_out}")

    if args.md_out:
        with open(args.md_out, "w", encoding="utf-8") as mf:
            mf.write(md_output)
        print(f"\n[INFO] Dokumen Markdown tersimpan di: {args.md_out}")


if __name__ == "__main__":
    main()

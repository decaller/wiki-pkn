#!/usr/bin/env python3
"""
qaf_research.py
Menggunakan qaf_wrapper untuk melakukan verifikasi silang (cross-verification)
dan mengekstraksi rujukan kitab klasik (maraji' turats) untuk pengayaan Wiki PKN.
"""

import sys
import json
from pathlib import Path

from dotenv import load_dotenv

QAF_DIR = Path("/home/abuhafi/Project/qaf_wrapper")
load_dotenv(QAF_DIR / ".env")
sys.path.insert(0, str(QAF_DIR))

from qaf import QafClient

OUTPUT_FILE = Path(__file__).resolve().parent.parent / "data" / "qaf_insights.json"
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

THEMATIC_QUERIES = [
    {
        "key": "etape_usia",
        "topic": "Tahapan Perkembangan Usia Anak dalam Islam (Thufulah, Tamyiz, Murahaqah, Syabab)",
        "question": "ما هي خصائص مراحل نمو الطفل في التربية الإسلامية: مرحلة الطفولة (دون السابعة)، والتمييز (7-10 سنوات)، والمراهقة (10-15 سنة)، والشباب أو البلوغ؟ وما هي الأحاديث والآثار النبوية وأقوال العلماء (مثل ابن القيم وابن الجوزي) في توجيه كل مرحلة؟"
    },
    {
        "key": "ammarah_lawwamah",
        "topic": "Penjinakan Jiwa Ammarah dan Bimbingan Menuju Muthmainnah",
        "question": "كيف يعالج المربي نزغات النفس الأمارة بالسوء عند الطفل ويوجهها لتصبح نفسا لوامة ثم مطمئنة؟ وما هي الضوابط النبوية في تفريغ طاقات الصبي دون كبت فطرته؟"
    },
    {
        "key": "hak_kewajiban_anak",
        "topic": "Hak Anak Atas Orang Tua dan Batasan Tanggung Jawab Pendidikan",
        "question": "ما هي حقوق الطفل الواجبة على الوالدين في الشريعة الإسلامية قبل البلوغ؟ وكيف قسم الفقهاء مسؤولية التربية والنفقة والتأديب بين الأب والأم والمعلم؟"
    },
    {
        "key": "metode_lisan_tangan",
        "topic": "Hierarki Metode Mendidik: Nasihat Lembut, Teguran Lisan, dan Batasan Disiplin",
        "question": "ما هي مراتب التأديب في الإسلام من الرفق والموعظة الحسنة إلى الحزم؟ وما هي ضوابط حديث 'مروا أولادكم بالصلاة لسبع واضربوهم عليها لعشر' وشروط الفقهاء في عدم إيذاء الطفل؟"
    }
]

def main():
    print(f"Menghubungkan ke Qaf AI via {QAF_DIR}...")
    client = QafClient()
    
    insights = {}
    if OUTPUT_FILE.exists():
        try:
            insights = json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
            print(f"Memuat {len(insights)} insight yang sudah tersimpan sebelumnya.")
        except Exception:
            insights = {}
            
    for item in THEMATIC_QUERIES:
        key = item["key"]
        if key in insights and insights[key].get("answer"):
            print(f"[SKIP] '{key}' sudah ada di database lokal.")
            continue
            
        print(f"\n[QUERYING QAF AI] {item['topic']}...")
        try:
            res = client.ask(item["question"])
            sources_summary = []
            for s in res.sources[:10]: # simpan 10 sumber teratas
                sources_summary.append({
                    "book_name": s.book_name,
                    "author_name": s.author_name,
                    "pages": s.pages,
                    "text": s.text[:400] if s.text else ""
                })
                
            insights[key] = {
                "topic": item["topic"],
                "question": item["question"],
                "title": res.title,
                "answer": res.answer,
                "sources_count": len(res.sources),
                "sources": sources_summary
            }
            print(f" -> Sukses! Mendapatkan jawaban ({len(res.answer)} karakter) dan {len(res.sources)} rujukan maraji'.")
            
            OUTPUT_FILE.write_text(json.dumps(insights, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            print(f" -> Gagal mengambil insight untuk '{key}': {e}")

    print(f"\nSelesai! Seluruh rujukan Qaf AI tersimpan di {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

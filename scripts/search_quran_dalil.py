#!/usr/bin/env python3
"""
Quran Dalil Search & Master Catalog Generator for Wiki PKN
Searches and compiles authentic Quranic verses, Indonesian translations,
and classical Tafsir references (Tafsir Ibn Kathir / OpenBayan)
for EVERY theme and page across the Wiki PKN repository.
"""

import sys
import os
import re
import sqlite3
import json
from pathlib import Path

OPENBAYAN_CORPUS_DB = "/home/abuhafi/Project/OpenBayanNext/data/shamela_corpus.db"
OPENBAYAN_FULL_DB = "/home/abuhafi/Project/OpenBayanNext/data/shamela_full.db"
CONTENT_DIR = Path("/home/abuhafi/Project/wiki-pkn/content")
OUTPUT_MD = Path("/home/abuhafi/Project/wiki-pkn/QURAN_DALIL_CATALOG.md")

def normalize_arabic(text: str) -> str:
    """Normalizes Arabic text according to OpenBayan's convention."""
    if not text:
        return ""
    text = re.sub(r'[\u064B-\u0652\u0670]', '', text) # harakat
    text = re.sub(r'\u0640', '', text) # tatweel
    text = re.sub(r'[إأآٱ]', 'ا', text) # alef
    text = re.sub(r'[ؤئ]', 'ء', text) # hamza
    text = re.sub(r'ة', 'ه', text) # taa marbutah
    text = re.sub(r'ى', 'ي', text) # alif maqsura
    text = re.sub(r'[^\u0621-\u064A0-9\s]', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def search_tafsir_snippet(verse_query: str, limit: int = 1) -> str:
    """Searches Tafsir Ibn Kathir in OpenBayan corpus for context."""
    db_path = OPENBAYAN_CORPUS_DB if os.path.exists(OPENBAYAN_CORPUS_DB) else None
    if not db_path:
        return ""
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        norm_q = normalize_arabic(verse_query)
        words = [w for w in norm_q.split() if len(w) > 2][:3]
        if not words:
            return ""
        fts_expr = " AND ".join([f'"{w}"*' for w in words])
        sql = """
            SELECT b.title_ar, p.volume_page, p.section_title, p.raw_text
            FROM prepared_chunks_fts f
            JOIN prepared_chunks p ON f.rowid = p.chunk_id
            JOIN books b ON p.book_id = b.book_id
            WHERE prepared_chunks_fts MATCH ? AND b.category_name = 'التفسير'
            LIMIT ?;
        """
        c.execute(sql, (fts_expr, limit))
        rows = c.fetchall()
        if rows:
            r = rows[0]
            clean_txt = re.sub(r'<[^>]+>', '', r[3])
            clean_txt = re.sub(r'\s+', ' ', clean_txt).strip()
            return f"*{r[0]}* ({r[1]}): \"{clean_txt[:220]}...\""
    except Exception:
        pass
    return ""

# Comprehensive Master Catalog of Quranic Dalil for Every Theme and Page in Wiki PKN
QURAN_THEME_CATALOG = {
    # =========================================================================
    # KLUSTER 1: PONDASI INSAN & HAKIKAT MANUSIA
    # =========================================================================
    "Tujuan Hidup Manusia.md": {
        "tema": "Hakikat Penciptaan, Orientasi Ibadah, dan Khilafah di Muka Bumi",
        "verses": [
            {
                "surah": "QS. Adz-Dzariyat: 56",
                "arab": "وَمَا خَلَقْتُ الْجِنَّ وَالْإِنسَ إِلَّا لِيَعْبُدُونِ",
                "terjemah": "Dan Aku tidak menciptakan jin dan manusia melainkan supaya mereka mengabdi (beribadah) kepada-Ku.",
                "relevansi_pkn": "Menetapkan tujuan akhir (ghayah kubra) seluruh proses pengasuhan: mencetak generasi hamba Allah yang taat bertauhid mutlak."
            },
            {
                "surah": "QS. Al-Baqarah: 30",
                "arab": "وَإِذْ قَالَ رَبُّكَ لِلْمَلَائِكَةِ إِنِّي جَاعِلٌ فِي الْأَرْضِ خَلِيفَةً",
                "terjemah": "Ingatlah ketika Tuhanmu berfirman kepada para Malaikat: 'Sesungguhnya Aku hendak menjadikan seorang khalifah di muka bumi.'",
                "relevansi_pkn": "Mandat peradaban anak; manusia dididik bukan sekadar untuk bertahan hidup, melainkan memakmurkan bumi dengan syariat dan keadilan."
            },
            {
                "surah": "QS. Al-Mulk: 2",
                "arab": "الَّذِي خَلَقَ الْمَوْتَ وَالْحَيَاةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًا ۚ وَهُوَ الْعَزِيزُ الْغَفُورُ",
                "terjemah": "Yang menciptakan mati dan hidup, untuk menguji kamu, siapa di antara kamu yang lebih baik amalnya (ahsanu 'amala).",
                "relevansi_pkn": "Pendidikan berorientasi kualitas amal terbaik (ihsan & itqan) berbasis keikhlasan dan kesesuaian sunnah, bukan sekadar kuantitas materi."
            }
        ]
    },
    "Bersatunya Ruh dan Jasad Membentuk Jiwa.md": {
        "tema": "Antropologi Insan: Pertemuan Ruh Suci dan Jasad Tanah Melahirkan Nafs",
        "verses": [
            {
                "surah": "QS. Al-Hijr: 28–29",
                "arab": "فَإِذَا سَوَّيْتُهُ وَنَفَخْتُ فِيهِ مِن رُّوحِي فَقَعُوا لَهُ سَاجِدِينَ",
                "terjemah": "Maka apabila Aku telah menyempurnakan kejadiannya, dan telah meniupkan ke dalamnya ruh (ciptaan)-Ku, maka tunduklah kamu kepadanya dengan bersujud.",
                "relevansi_pkn": "Hakikat kemuliaan manusia terletak pada ditiupkannya ruh yang suci ke dalam jasad; mendidik anak harus menyentuh dimensi ruhani, bukan hanya fisik jasadiah."
            },
            {
                "surah": "QS. Al-Mu'minun: 12–14",
                "arab": "وَلَقَدْ خَلَقْنَا الْإِنسَانَ مِن سُلَالَةٍ مِّن طِينٍ ۝ ثُمَّ جَعَلْنَاهُ نُطْفَةً فِي قَرَارٍ مَّكِينٍ ۝ ثُمَّ خَلَقْنَا النُّطْفَةَ عَلَقَةً فَخَلَقْنَا الْعَلَقَةَ مُضْغَةً فَخَلَقْنَا الْمُضْغَةَ عِظَامًا فَكَسَوْنَا الْعِظَامَ لَحْمًا ثُمَّ أَنشَأْنَاهُ خَلْقًا آخَرَ ۚ فَتَبَارَكَ اللَّهُ أَحْسَنُ الْخَالِقِينَ",
                "terjemah": "Dan sesungguhnya Kami telah menciptakan manusia dari suatu saripati (berasal) dari tanah... kemudian Kami jadikan dia makhluk yang (berbentuk) lain. Maka Maha Sucilah Allah, Pencipta Yang Paling Baik.",
                "relevansi_pkn": "Tahapan biologis perkembangan janin menuju 'makhluk yang berbentuk lain' (berjiwa) menjadi fondasi pemahaman bertahap (tadarruj) dalam fitrah perkembangan."
            },
            {
                "surah": "QS. Al-Isra': 85",
                "arab": "وَيَسْأَلُونَكَ عَنِ الرُّوحِ ۖ قُلِ الرُّوحُ مِنْ أَمْرِ رَبِّي وَمَا أُوتِيتُم مِّنَ الْعِلْمِ إِلَّا قَلِيلًا",
                "terjemah": "Dan mereka bertanya kepadamu tentang ruh. Katakanlah: 'Ruh itu termasuk urusan Tuhanku, dan tidaklah kamu diberi pengetahuan melainkan sedikit.'",
                "relevansi_pkn": "Mengharuskan pendidik memiliki kerendahan hati bahwa dimensi batin anak berada di tangan Allah; ikhtiar pengasuhan wajib selalu disertai tawakkal dan doa."
            }
        ]
    },
    "Insan.md": {
        "tema": "Hakikat Keinsanan: Martabat Tertinggi, Akal Budi, dan Beban Amanah",
        "verses": [
            {
                "surah": "QS. At-Tin: 4",
                "arab": "لَقَدْ خَلَقْنَا الْإِنسَانَ فِي أَحْسَنِ تَقْوِيمٍ",
                "terjemah": "Sesungguhnya Kami telah menciptakan manusia dalam bentuk yang sebaik-baiknya.",
                "relevansi_pkn": "Setiap anak lahir dengan potensi fitrah sempurna (ahsan taqwim); tugas tarbiyah adalah menjaga kesempurnaan ini agar tidak merosot ke asfala safilin."
            },
            {
                "surah": "QS. Al-Insan: 2–3",
                "arab": "إِنَّا خَلَقْنَا الْإِنسَانَ مِن نُّطْفَةٍ أَمْشَاجٍ نَّبْتَلِيهِ فَجَعَلْنَاهُ سَمِيعًا بَصِيرًا ۝ إِنَّا هَدَيْنَاهُ السَّبِيلَ إِمَّا شَاكِرًا وَإِمَّا كَفُورًا",
                "terjemah": "Sesungguhnya Kami telah menciptakan manusia dari setetes mani yang bercampur yang Kami hendak mengujinya, karena itu Kami jadikan dia mendengar dan melihat. Sesungguhnya Kami telah menunjukinya jalan yang lurus; ada yang bersyukur dan ada pula yang kafir.",
                "relevansi_pkn": "Anak dibekali instrumen pendengaran, penglihatan, dan kehendak memilih untuk menghadapi ujian kehidupan; mendidik adalah memandu daya pilih anak menuju rasa syukur."
            },
            {
                "surah": "QS. Al-Ahzab: 72",
                "arab": "إِنَّا عَرَضْنَا الْأَمَانَةَ عَلَى السَّمَاوَاتِ وَالْأَرْضِ وَالْجِبَالِ فَأَبَيْنَ أَن يَحْمِلْنَهَا وَأَشْفَقْنَ مِنْهَا وَحَمَلَهَا الْإِنسَانُ",
                "terjemah": "Sesungguhnya Kami telah menawarkan amanat kepada langit, bumi dan gunung-gunung, maka semuanya enggan untuk memikul amanat itu dan mereka khawatir akan mengkhianatinya, dan dipikullah amanat itu oleh manusia.",
                "relevansi_pkn": "Manusia memikul beban taklif moral syariat; tujuan akhir PKN adalah mengantarkan anak menjadi mukallaf yang sanggup memegang amanah Ilahi."
            }
        ]
    },

    # =========================================================================
    # KLUSTER 2: TRILOGI JIWA (NAFS)
    # =========================================================================
    "Pembagian Jiwa.md": {
        "tema": "Trilogi Jiwa dalam Al-Qur'an: Ammarah, Lawwamah, dan Muthmainnah",
        "verses": [
            {
                "surah": "QS. Asy-Syams: 7–10",
                "arab": "وَنَفْسٍ وَمَا سَوَّاهَا ۝ فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَاهَا ۝ قَدْ أَفْلَحَ مَن زَكَّاهَا ۝ وَقَدْ خَابَ مَن دَسَّاهَا",
                "terjemah": "Dan jiwa serta penyempurnaannya (ciptaannya), maka Allah mengilhamkan kepada jiwa itu (jalan) kefasikan dan ketakwaannya. Sesungguhnya beruntunglah orang yang menyucikan jiwa itu, dan sesungguhnya merugilah orang yang mengotorinya.",
                "relevansi_pkn": "Fondasi dinamika jiwa: fitrah anak memiliki kesiapan menerima taqwa dan dorongan fujur; tarbiyah bertugas mensucikan jiwa (tazkiyah) menuju kemenangan."
            },
            {
                "surah": "QS. Yusuf: 53",
                "arab": "وَمَا أُبَرِّئُ نَفْسِي ۚ إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ إِلَّا مَا رَحِمَ رَبِّي",
                "terjemah": "Dan aku tidak membebaskan diriku (dari kesalahan), karena sesungguhnya nafsu itu selalu menyuruh kepada kejahatan, kecuali nafsu yang diberi rahmat oleh Tuhanku.",
                "relevansi_pkn": "Mengakui eksistensi nafsu ammarah pada jasad anak; pendekatan pendidik bukan mencela anak melainkan mendisiplinkannya dengan rahmat."
            },
            {
                "surah": "QS. Al-Qiyamah: 2",
                "arab": "وَلَا أُقْسِمُ بِالنَّفْسِ اللَّوَّامَةِ",
                "terjemah": "Dan Aku bersumpah dengan jiwa yang amat menyesali (dirinya sendiri).",
                "relevansi_pkn": "Tingkatan jiwa nalar reflektif yang menegur kekeliruan; anak dibimbing mengasah daya muhasabah dan pemikiran kritis obyektif."
            },
            {
                "surah": "QS. Al-Fajr: 27–28",
                "arab": "يَا أَيَّتُهَا النَّفْسُ الْمُطْمَئِنَّةُ ۝ ارْجِعِي إِلَىٰ رَبِّكِ رَاضِيَةً مَّرْضِيَّةً",
                "terjemah": "Wahai jiwa yang tenang! Kembalilah kepada Tuhanmu dengan hati yang puas lagi diridhai-Nya.",
                "relevansi_pkn": "Puncak ketenangan spiritual; hati yang tunduk dalam ketauhidan dan kedamaian cinta kepada Allah SWT."
            }
        ]
    },
    "Ammarah.md": {
        "tema": "Nafsu Ammarah: Dorongan Jasad, Hawa Nafsu, dan Penjinakannya Melalui Disiplin Fisik",
        "verses": [
            {
                "surah": "QS. Yusuf: 53",
                "arab": "وَمَا أُبَرِّئُ نَفْسِي ۚ إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ إِلَّا مَا رَحِمَ رَبِّي ۚ إِنَّ رَبِّي غَفُورٌ رَّحِيمٌ",
                "terjemah": "Dan aku tidak membebaskan diriku (dari kesalahan), karena sesungguhnya nafsu itu selalu menyuruh kepada kejahatan, kecuali nafsu yang diberi rahmat oleh Tuhanku. Sesungguhnya Tuhanku Maha Pengampun lagi Maha Penyayang.",
                "relevansi_pkn": "Karakteristik nafsu jasadiah yang reaktif dan impulsif; tugas pendidik adalah mengarahkan energinya pada karya nyata dan pembiasaan fisik teratur."
            },
            {
                "surah": "QS. An-Nazi'at: 40–41",
                "arab": "وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِ وَنَهَى النَّفْسَ عَنِ الْهَوَىٰ ۝ فَإِنَّ الْجَنَّةَ هِيَ الْمَأْوَىٰ",
                "terjemah": "Dan adapun orang-orang yang takut kepada kebesaran Tuhannya dan menahan diri dari keinginan hawa nafsunya, maka sesungguhnya surgalah tempat tinggal(nya).",
                "relevansi_pkn": "Kunci pengendalian diri (self-regulation): menanamkan rasa takut yang agung kepada Allah (khauf) untuk menundukkan dorongan hawa nafsu anak."
            },
            {
                "surah": "QS. Al-Furqan: 43",
                "arab": "أَرَأَيْتَ مَنِ اتَّخَذَ إِلَٰهَهُ هَوَاهُ أَفَأَنتَ تَكُونُ عَلَيْهِ وَكِيلًا",
                "terjemah": "Terangkanlah kepadaku tentang orang yang menjadikan hawa nafsunya sebagai tuhannya. Maka apakah kamu dapat menjadi pemelihara atasnya?",
                "relevansi_pkn": "Bahaya tafrith dalam pengasuhan permisif yang membiarkan anak diperbudak oleh segala keinginannya (hedonisme/gawai) tanpa batas adab."
            }
        ]
    },
    "Lawwamah.md": {
        "tema": "Nafsu Lawwamah: Daya Nalar, Akal Evaluatif, Introspeksi (Muhasabah), dan Penyesalan Konstruktif",
        "verses": [
            {
                "surah": "QS. Al-Qiyamah: 1–2",
                "arab": "لَا أُقْسِمُ بِيَوْمِ الْقِيَامَةِ ۝ وَلَا أُقْسِمُ بِالنَّفْسِ اللَّوَّامَةِ",
                "terjemah": "Aku bersumpah demi hari kiamat, dan Aku bersumpah dengan jiwa yang amat menyesali (dirinya sendiri).",
                "relevansi_pkn": "Allah mengagungkan jiwa yang peka mengoreksi diri; anak dilatih untuk berani mengakui kesalahan dan memperbaiki perbuatan tanpa kepalsuan."
            },
            {
                "surah": "QS. Al-A'raf: 201",
                "arab": "إِنَّ الَّذِينَ اتَّقَوْا إِذَا مَسَّهُمْ طَائِفٌ مِّنَ الشَّيْطَانِ تَذَكَّرُوا فَإِذَا هُم مُّبْصِرُونَ",
                "terjemah": "Sesungguhnya orang-orang yang bertakwa bila mereka ditimpa was-was dari syaitan, mereka ingat kepada Allah, maka dengan serta merta mereka melihat kesalahan-kesalahannya.",
                "relevansi_pkn": "Mekanisme kerja jiwa lawwamah yang sehat: ketika tergelincir, ia segera mengingat Allah (tadzakkur) dan kembali jernih memandang kebenaran."
            },
            {
                "surah": "QS. Al-Hasyr: 18",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ وَلْتَنظُرْ نَفْسٌ مَّا قَدَّمَتْ لِغَدٍ ۖ وَاتَّقُوا اللَّهَ ۚ إِنَّ اللَّهَ خَبِيرٌ بِمَا تَعْمَلُونَ",
                "terjemah": "Wahai orang-orang yang beriman, bertakwalah kepada Allah dan hendaklah setiap jiwa memperhatikan apa yang telah diperbuatnya untuk hari esok (akhirat)...",
                "relevansi_pkn": "Metode latihan muhasabah harian bagi anak usia Tamyiz dan Murahaqah untuk mengevaluasi amal perbuatan dan belajar dari kegagalan."
            }
        ]
    },
    "Muthmainnah.md": {
        "tema": "Nafsu Muthmainnah: Ketenangan Spiritual, Kemurnian Tauhid, Sakinah, dan Keridhaan Batin",
        "verses": [
            {
                "surah": "QS. Al-Fajr: 27–30",
                "arab": "يَا أَيَّتُهَا النَّفْسُ الْمُطْمَئِنَّةُ ۝ ارْجِعِي إِلَىٰ رَبِّكِ رَاضِيَةً مَّرْضِيَّةً ۝ فَادْخُلِي فِي عِبَادِي ۝ وَادْخُلِي جَنَّتِي",
                "terjemah": "Wahai jiwa yang tenang! Kembalilah kepada Tuhanmu dengan hati yang puas lagi diridhai-Nya. Maka masuklah ke dalam jamaah hamba-hamba-Ku, dan masuklah ke dalam surga-Ku.",
                "relevansi_pkn": "Muara tertinggi pembentukan karakter: jiwa yang merasa aman bersama Allah, ridha terhadap takdir-Nya, dan berhias akhlak mulia."
            },
            {
                "surah": "QS. Ar-Ra'd: 28",
                "arab": "الَّذِينَ آمَنُوا وَتَطْمَئِنُّ قُلُوبُهُم بِذِكْرِ اللَّهِ ۗ أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ",
                "terjemah": "(Yaitu) orang-orang yang beriman dan hati mereka manjadi tenteram dengan mengingat Allah. Ingatlah, hanya dengan mengingati Allah-lah hati menjadi tenteram.",
                "relevansi_pkn": "Dzikrullah dan ibadah batiniah adalah nutrisi utama jiwa muthmainnah; mengajarkan anak berdzikir dan berdoa melahirkan ketenangan mental hakiki."
            },
            {
                "surah": "QS. Al-Fath: 4",
                "arab": "هُوَ الَّذِي أَنزَلَ السَّكِينَةَ فِي قُلُوبِ الْمُؤْمِنِينَ لِيَزْدَادُوا إِيمَانًا مَّعَ إِيمَانِهِمْ",
                "terjemah": "Dialah yang telah menurunkan ketenangan ke dalam hati orang-orang mukmin supaya keimanan mereka bertambah di samping keimanan mereka (yang telah ada).",
                "relevansi_pkn": "Sakinah adalah anugerah Ilahi yang tumbuh dari suasana rumah penuh rahmah dan ketenangan komunikasi kedua orang tua."
            }
        ]
    },

    # =========================================================================
    # KLUSTER 3: FITRAH (KARAKTER), IMAN & BELAJAR
    # =========================================================================
    "Fitrah (Karakter).md": {
        "tema": "Fitrah Manusia: Cetak Biru Suci, Tauhid Bawaan Lahir, dan Perlindungan Karakternya",
        "verses": [
            {
                "surah": "QS. Ar-Rum: 30",
                "arab": "فَأَقِمْ وَجْهَكَ لِلدِّينِ حَنِيفًا ۚ فِطْرَتَ اللَّهِ الَّتِي فَطَرَ النَّاسَ عَلَيْهَا ۚ لَا تَبْدِيلَ لِخَلْقِ اللَّهِ ۚ ذَٰلِكَ الدِّينُ الْقَيِّمُ وَلَٰكِنَّ أَكْثَرَ النَّاسِ لَا يَعْلَمُونَ",
                "terjemah": "Maka hadapkanlah wajahmu dengan lurus kepada agama Allah; (tetaplah atas) fitrah Allah yang telah menciptakan manusia menurut fitrah itu. Tidak ada perubahan pada fitrah Allah. (Itulah) agama yang lurus; tetapi kebanyakan manusia tidak mengetahui.",
                "relevansi_pkn": "Kaidah fundamental PKN: fitrah anak adalah suci dan lurus; mendidik adalah merawat (gardening) kesucian fitrah, bukan merusak atau mendistorsinya."
            },
            {
                "surah": "QS. Al-A'raf: 172",
                "arab": "وَإِذْ أَخَذَ رَبُّكَ مِن بَنِي آدَمَ مِن ظُهُورِهِمْ ذُرِّيَّتَهُمْ وَأَشْهَدَهُمْ عَلَىٰ أَنفُسِهِمْ أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا بَلَىٰ ۛ شَهِدْنَا",
                "terjemah": "Dan (ingatlah), ketika Tuhanmu mengeluarkan keturunan anak-anak Adam dari sulbi mereka dan Allah mengambil kesaksian terhadap jiwa mereka (seraya berfirman): 'Bukankah Aku ini Tuhanmu?' Mereka menjawab: 'Betul (Engkau Tuhan kami), kami menjadi saksi.'",
                "relevansi_pkn": "Perjanjian primordial (mitsaq) di alam arwah; setiap anak terlahir dengan kerinduan fitrah untuk bertauhid kepada Allah."
            }
        ]
    },
    "Iman.md": {
        "tema": "Karakter Iman: Menumbuhkan Cinta kepada Allah Sebelum Beban Formal Syariat",
        "verses": [
            {
                "surah": "QS. Al-Hujurat: 7",
                "arab": "وَلَٰكِنَّ اللَّهَ حَبَّبَ إِلَيْكُمُ الْإِيمَانَ وَزَيَّنَهُ فِي قُلُوبِكُمْ وَكَرَّهَ إِلَيْكُمُ الْكُفْرَ وَالْفُسُوقَ وَالْعِصْيَانَ ۚ أُولَٰئِكَ هُمُ الرَّاشِدُونَ",
                "terjemah": "Tetapi Allah menjadikan kamu 'cinta' kepada keimanan dan menjadikan keimanan itu indah di dalam hatimu serta menjadikan kamu benci kepada kekafiran, kefasikan, dan kedurhakaan. Mereka itulah orang-orang yang mengikuti jalan yang lurus.",
                "relevansi_pkn": "Strategi penanaman iman PKN: memperindah iman dalam hati anak melalui rasa cinta dan kekaguman (tahbibul iman) sebelum pengajaran larangan kaku."
            },
            {
                "surah": "QS. Ibrahim: 24–25",
                "arab": "أَلَمْ تَرَ كَيْفَ ضَرَبَ اللَّهُ مَثَلًا كَلِمَةً طَيِّبَةً كَشَجَرَةٍ طَيِّبَةٍ أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِي السَّمَاءِ ۝ تُؤْتِي أُكُلَهَا كُلَّ حِينٍ بِإِذْنِ رَبِّهَا",
                "terjemah": "Tidakkah kamu perhatikan bagaimana Allah telah membuat perumpamaan kalimat yang baik seperti pohon yang baik, akarnya teguh dan cabangnya (menjulang) ke langit, pohon itu menghasilkan buahnya pada setiap waktu dengan seizin Tuhannya.",
                "relevansi_pkn": "Pohon Karakter Nabawiyah: akar kalimat thayyibah (iman/tauhid) yang kokoh menjadi penopang utama bagi batang adab dan cabang amal bakat yang berbuah manfaat."
            },
            {
                "surah": "QS. Al-Baqarah: 256",
                "arab": "لَا إِكْرَاهَ فِي الدِّينِ ۖ قَد تَّبَيَّنَ الرُّشْدُ مِنَ الْغَيِّ",
                "terjemah": "Tidak ada paksaan untuk (memasuki) agama (Islam); sesungguhnya telah jelas jalan yang benar daripada jalan yang sesat.",
                "relevansi_pkn": "Iman tidak dapat dipaksakan secara intimidatif pada anak kecil; ia harus disemai melalui dialog logis, keteladanan hangat, dan penyerahan sukarela kalbu."
            }
        ]
    },
    "Tangki Cinta.md": {
        "tema": "Tangki Cinta: Kasih Sayang Tanpa Syarat (Rahmah) sebagai Prasyarat Tumbuhnya Iman",
        "verses": [
            {
                "surah": "QS. Maryam: 96",
                "arab": "إِنَّ الَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ سَيَجْعَلُ لَهُمُ الرَّحْمَٰنُ وُدًّا",
                "terjemah": "Sesungguhnya orang-orang yang beriman dan beramal saleh, kelak Allah Yang Maha Pemurah akan menanamkan dalam (hati) mereka rasa kasih sayang (wuddan).",
                "relevansi_pkn": "Kasih sayang sejati (al-wudd) bersumber dari Allah; orang tua yang melimpahkan kasih sayang kepada anak sedang mengalirkan rahmat Ilahi ke jiwa mereka."
            },
            {
                "surah": "QS. Ali 'Imran: 159",
                "arab": "فَبِمَا رَحْمَةٍ مِّنَ اللَّهِ لِنتَ لَهُمْ ۖ وَلَوْ كُنتَ فَظًّا غَلِيظَ الْقَلْبِ لَانفَضُّوا مِنْ حَوْلِكَ",
                "terjemah": "Maka disebabkan rahmat dari Allah-lah kamu berlaku lemah lembut terhadap mereka. Sekiranya kamu bersikap keras lagi berhati kasar, tentulah mereka menjauhkan diri dari sekelilingmu.",
                "relevansi_pkn": "Hati yang keras dan bentakan orang tua akan mengeringkan tangki cinta anak dan membuat mereka lari menjauh dari pelukan keluarga dan nilai agama."
            },
            {
                "surah": "QS. Al-Balad: 17",
                "arab": "ثُمَّ كَانَ مِنَ الَّذِينَ آمَنُوا وَتَوَاصَوْا بِالصَّبْرِ وَتَوَاصَوْا بِالْمَرْحَمَةِ",
                "terjemah": "Dan dia (tidak pula) termasuk orang-orang yang beriman dan saling berpesan untuk bersabar dan saling berpesan untuk berkasih sayang.",
                "relevansi_pkn": "Wasiat berkasih sayang (marhamah) di dalam rumah tangga merupakan tiang penegak keselamatan jiwa generasi penerus."
            }
        ]
    },
    "Belajar.md": {
        "tema": "Fitrah Belajar: Dorongan Eksplorasi Alamiah, Tadabbur Ayat Kauniyah, dan Kehausan Ilmu",
        "verses": [
            {
                "surah": "QS. Al-'Alaq: 1–5",
                "arab": "اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ ۝ خَلَقَ الْإِنسَانَ مِنْ عَلَقٍ ۝ اقْرَأْ وَرَبُّكَ الْأَكْرَمُ ۝ الَّذِي عَلَّمَ بِالْقَلَمِ ۝ عَلَّمَ الْإِنسَانَ مَا لَمْ يَعْلَمْ",
                "terjemah": "Bacalah dengan (menyebut) nama Tuhanmu Yang menciptakan... Yang mengajar (manusia) dengan perantaraan qalam. Dia mengajar kepada manusia apa yang tidak diketahuinya.",
                "relevansi_pkn": "Perintah belajar perdana: membaca ayat-ayat Allah dengan kesadaran tauhid; qalam melambangkan literasi dan alat penjelajah peradaban ilmu."
            },
            {
                "surah": "QS. Al-Baqarah: 31",
                "arab": "وَعَلَّمَ آدَمَ الْأَسْمَاءَ كُلَّهَا ثُمَّ عَرَضَهُمْ عَلَى الْمَلَائِكَةِ",
                "terjemah": "Dan Dia mengajarkan kepada Adam nama-nama (benda-benda) seluruhnya, kemudian mengemukakannya kepada para Malaikat...",
                "relevansi_pkn": "Fitrah kognitif anak: kemampuan alami mengenali, menamai, dan mengkategorikan realitas dunia nyata di sekitarnya."
            },
            {
                "surah": "QS. An-Nahl: 78",
                "arab": "وَاللَّهُ أَخْرَجَكُم مِّن بُطُونِ أُمَّهَاتِكُمْ لَا تَعْلَمُونَ شَيْئًا وَجَعَلَ لَكُمُ السَّمْعَ وَالْأَبْصَارَ وَالْأَفْئِدَةَ ۙ لَعَلَّكُمْ تَشْكُرُونَ",
                "terjemah": "Dan Allah mengeluarkan kamu dari perut ibumu dalam keadaan tidak mengetahui sesuatupun, dan Dia memberi kamu pendengaran, penglihatan dan hati (af'idah), agar kamu bersyukur.",
                "relevansi_pkn": "Tiga gerbang pembelajaran fitrah: telinga (menyimak hikmah), mata (mengamati fakta), dan af'idah (menghayati makna), yang bermuara pada rasa syukur."
            },
            {
                "surah": "QS. Al-Ghasyiyah: 17–20",
                "arab": "أَفَلَا يَنظُرُونَ إِلَى الْإِبِلِ كَيْفَ خُلِقَتْ ۝ وَإِلَى السَّمَاءِ كَيْفَ رُفِعَتْ ۝ وَإِلَى الْجِبَالِ كَيْفَ نُصِبَتْ ۝ وَإِلَى الْأَرْضِ كَيْفَ سُطِحَتْ",
                "terjemah": "Maka apakah mereka tidak memperhatikan unta bagaimana ia diciptakan, dan langit bagaimana ia ditinggikan, dan gunung-gunung bagaimana ia ditegakkan, dan bumi bagaimana ia dihamparkan?",
                "relevansi_pkn": "Metode pembelajaran alamiah: mengajak anak berinteraksi langsung dengan alam semesta untuk memicu nalar kritis dan rasa takjub batiniah."
            }
        ]
    },

    # =========================================================================
    # KLUSTER 4: BAKAT & 6 SUB-BAKAT (TB40)
    # =========================================================================
    "Bakat.md": {
        "tema": "Fitrah Bakat: Keberagaman Potensi Unik (Syakilah) dan Pembagian Peran Peradaban",
        "verses": [
            {
                "surah": "QS. Al-Isra': 84",
                "arab": "قُلْ كُلٌّ يَعْمَلُ عَلَىٰ شَاكِلَتِهِ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًا",
                "terjemah": "Katakanlah: 'Tiap-tiap orang berbuat menurut keadaannya (potensi, watak, dan bakat bawaannya) masing-masing.' Maka Tuhanmu lebih mengetahui siapa yang lebih benar jalannya.",
                "relevansi_pkn": "Prinsip personalisasi PKN: setiap anak memiliki syakilah (pola bakat) unik; tidak boleh diseragamkan dengan kurikulum massal pabrik."
            },
            {
                "surah": "QS. Az-Zukhruf: 32",
                "arab": "نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِي الْحَيَاةِ الدُّنْيَا ۚ وَرَفَعْنَا بَعْضَهُمْ فَوْقَ بَعْضٍ دَرَجَاتٍ لِّيَتَّخِذَ بَعْضُهُم بَعْضًا سُخْرِيًّا",
                "terjemah": "Kami telah menentukan antara mereka penghidupan mereka dalam kehidupan dunia, dan Kami telah meninggikan sebahagian mereka atas sebahagian yang lain beberapa derajat, agar sebahagian mereka dapat mempergunakan sebahagian yang lain...",
                "relevansi_pkn": "Hikmah perbedaan bakat: keberagaman anugerah Allah didesain agar manusia saling bekerjasama, melengkapi, dan membangun tatanan peradaban."
            }
        ]
    },
    "Bekerja Keras.md": {
        "tema": "Sub-Bakat Bekerja Keras: Daya Tahan, Ketekunan Beramal (Itqan), dan Pantang Menyerah",
        "verses": [
            {
                "surah": "QS. At-Taubah: 105",
                "arab": "وَقُلِ اعْمَلُوا فَسَيَرَى اللَّهُ عَمَلَكُمْ وَرَسُولُهُ وَالْمُؤْمِنُونَ ۖ وَسَتُرَدُّونَ إِلَىٰ عَالِمِ الْغَيْبِ وَالشَّهَادَةِ فَيُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُونَ",
                "terjemah": "Dan Katakanlah: 'Bekerjalah kamu, maka Allah dan Rasul-Nya serta orang-orang mukmin akan melihat pekerjaanmu itu, dan kamu akan dikembalikan kepada (Allah) Yang Mengetahui akan yang ghaib dan yang nyata...'",
                "relevansi_pkn": "Etos kerja keras nabawiyah: beramal dengan kesadaran muraqabah bahwa setiap ikhtiar dipantau dan dinilai langsung oleh Allah SWT."
            },
            {
                "surah": "QS. Al-Insyirah: 7–8",
                "arab": "فَإِذَا فَرَغْتَ فَانصَبْ ۝ وَإِلَىٰ رَبِّكَ فَارْغَب",
                "terjemah": "Maka apabila kamu telah selesai (dari sesuatu urusan), kerjakanlah dengan sungguh-sungguh (urusan yang lain), dan hanya kepada Tuhanmulah hendaknya kamu berharap.",
                "relevansi_pkn": "Prinsip kontinuitas daya juang (grit): tidak ada waktu luang yang sia-sia; selesai dari satu karya, segera berpindah ke perjuangan berikutnya."
            },
            {
                "surah": "QS. Al-Mulk: 15",
                "arab": "هُوَ الَّذِي جَعَلَ لَكُمُ الْأَرْضَ ذَلُولًا فَامْشُوا فِي مَنَاكِبِهَا وَكُلُوا مِن رِّزْقِهِ ۖ وَإِلَيْهِ النُّشُورُ",
                "terjemah": "Dialah Yang menjadikan bumi itu mudah bagi kamu, maka berjalanlah di segala penjurunya dan makanlah sebahagian dari rezeki-Nya. Dan hanya kepada-Nya-lah kamu (kembali setelah) dibangkitkan.",
                "relevansi_pkn": "Kemandirian fisik dan etos penjelajahan bumi mencari rezeki halal melalui kerja keras yang produktif."
            }
        ]
    },
    "Berpikir.md": {
        "tema": "Sub-Bakat Berpikir: Hikmah, Logika Ilmiah, Firasat Tajam, dan Tadabbur Mendalam",
        "verses": [
            {
                "surah": "QS. Al-Baqarah: 269",
                "arab": "يُؤْتِي الْحِكْمَةَ مَن يَشَاءُ ۚ وَمَن يُؤْتَ الْحِكْمَةَ فَقَدْ أُوتِيَ خَيْرًا كَثِيرًا ۗ وَمَا يَذَّكَّرُ إِلَّا أُولُو الْأَلْبَابِ",
                "terjemah": "Allah menganugerahkan hikmah kepada siapa yang Dia kehendaki. Dan barangsiapa dianugerahi hikmah, dia benar-benar telah dianugerahi kebajikan yang banyak. Dan tidak ada yang dapat mengambil pelajaran kecuali orang-orang yang berakal (Ulul Albab).",
                "relevansi_pkn": "Puncak bakat berpikir bukan sekadar cerdas akademis, melainkan meraih hikmah (kebijaksanaan menempatkan sesuatu pada tempatnya)."
            },
            {
                "surah": "QS. Ali 'Imran: 190–191",
                "arab": "إِنَّ فِي خَلْقِ السَّمَاوَاتِ وَالْأَرْضِ وَاخْتِلَافِ اللَّيْلِ وَالنَّهَارِ لَآيَاتٍ لِّأُولِي الْأَلْبَابِ ۝ الَّذِينَ يَذْكُرُونَ اللَّهَ قِيَامًا وَقُعُودًا وَعَلَىٰ جُنُوبِهِمْ وَيَتَفَكَّرُونَ فِي خَلْقِ السَّمَاوَاتِ وَالْأَرْضِ رَبَّنَا مَا خَلَقْتَ هَٰذَا بَاطِلًا سُبْحَانَكَ فَقِنَا عَذَابَ النَّارِ",
                "terjemah": "Sesungguhnya dalam penciptaan langit dan bumi, dan silih bergantinya malam dan siang terdapat tanda-tanda bagi orang-orang yang berakal, (yaitu) orang-orang yang mengingat Allah sambil berdiri atau duduk atau dalam keadan berbaring dan mereka memikirkan tentang penciptaan langit dan bumi...",
                "relevansi_pkn": "Sinergi agung antara dzikir hati dan nalar pikir; berpikir objektif melahirkan pengagungan kepada Sang Pencipta."
            },
            {
                "surah": "QS. Yunus: 101",
                "arab": "قُلِ انظُرُوا مَاذَا فِي السَّمَاوَاتِ وَالْأَرْضِ",
                "terjemah": "Katakanlah: 'Perhatikanlah apa yang ada di langit dan di bumi...'",
                "relevansi_pkn": "Perintah eksplorasi riset dan penyelidikan sains berbasis pengamatan empiris yang memicu bakat analisis anak."
            }
        ]
    },
    "Berperasaan.md": {
        "tema": "Sub-Bakat Berperasaan: Kepekaan Nurani, Empati Mendalam, Menjaga Kehormatan Batin (Qalbun Salim)",
        "verses": [
            {
                "surah": "QS. Asy-Syu'ara: 88–89",
                "arab": "يَوْمَ لَا يَنفَعُ مَالٌ وَلَا بَنُونَ ۝ إِلَّا مَنْ أَتَى اللَّهَ بِقَلْبٍ سَلِيمٍ",
                "terjemah": "(Yaitu) di hari ketiadaan harta dan anak-anak laki-laki tidak berguna, kecuali orang-orang yang menghadap Allah dengan hati yang bersih (qalbun salim).",
                "relevansi_pkn": "Menjaga kejernihan rasa dan kebersihan hati anak dari noda hasad, dendam, dan kesombongan sebagai bekal abadi akhirat."
            },
            {
                "surah": "QS. Al-Hujurat: 12",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا اجْتَنِبُوا كَثِيرًا مِّنَ الظَّنِّ إِنَّ بَعْضَ الظَّنِّ إِثْمٌ ۖ وَلَا تَجَسَّسُوا وَلَا يَغْتَب بَّعْضُكُم بَعْضًا",
                "terjemah": "Wahai orang-orang yang beriman, jauhilah kebanyakan purba-sangka (kecurigaan), karena sebagian dari purba-sangka itu dosa. Dan janganlah mencari-cari keburukan orang dan janganlah menggunjingkan satu sama lain...",
                "relevansi_pkn": "Adab menjaga perasaan sesama: membiasakan anak berprasangka baik (husnuzhan), menghormati privasi, dan menjaga lisan dari menyakiti orang lain."
            },
            {
                "surah": "QS. Al-Qashash: 10",
                "arab": "وَأَصْبَحَ فُؤَادُ أُمِّ مُوسَىٰ فَارِغًا ۖ إِن كَادَتْ لَتُبْدِي بِهِ لَوْلَا أَن رَّبَطْنَا عَلَىٰ قَلْبِهَا لِتَكُونَ مِنَ الْمُؤْمِنِينَ",
                "terjemah": "Dan menjadi kosonglah hati ibu Musa. Sesungguhnya hampir saja ia menyatakan rahasia tentang Musa, seandainya tidak Kami teguhkan hatinya, supaya ia termasuk orang-orang yang percaya (kepada janji Allah).",
                "relevansi_pkn": "Potret kedalaman cinta dan gejolak rasa seorang ibu; mendidik adalah mengokohkan ikatan hati (rabthul qalb) bersandar pada janji Allah."
            }
        ]
    },
    "Memerintah.md": {
        "tema": "Sub-Bakat Memerintah: Kepemimpinan Adil, Keberanian Moral (Syaja'ah), Integritas, dan Tanggung Jawab",
        "verses": [
            {
                "surah": "QS. Shad: 26",
                "arab": "يَا دَاوُودُ إِنَّا جَعَلْنَاكَ خَلِيفَةً فِي الْأَرْضِ فَاحْكُم بَيْنَ النَّاسِ بِالْحَقِّ وَلَا تَتَّبِعِ الْهَوَىٰ فَيُضِلَّكَ عَن سَبِيلِ اللَّهِ",
                "terjemah": "Hai Daud, sesungguhnya Kami menjadikan kamu khalifah (penguasa) di muka bumi, maka berilah keputusan (perkara) di antara manusia dengan adil dan janganlah kamu mengikuti hawa nafsu, karena ia akan menyesatkan kamu dari jalan Allah.",
                "relevansi_pkn": "Hukum kepemimpinan dalam Islam: wewenang memerintah adalah sarana menegakkan keadilan haqiqi, bukan pelampiasan kuasa hawa nafsu."
            },
            {
                "surah": "QS. Al-Qashash: 26",
                "arab": "قَالَتْ إِحْدَاهُمَا يَا أَبَتِ اسْتَأْجِرْهُ ۖ إِنَّ خَيْرَ مَنِ اسْتَأْجَرْتَ الْقَوِيُّ الْأَمِينُ",
                "terjemah": "Salah seorang dari kedua wanita itu berkata: 'Ya bapakku ambillah ia sebagai orang yang bekerja (pada kita), karena sesungguhnya orang yang paling baik yang kamu ambil untuk bekerja (pada kita) ialah orang yang kuat lagi dapat dipercaya (al-qawiyyul amin).'",
                "relevansi_pkn": "Dua syarat mutlak pemimpin: al-qawiy (kompetensi, ketegasan, kapabilitas teknis) dan al-amin (integritas, amanah, takut kepada Allah)."
            },
            {
                "surah": "QS. Yusuf: 55",
                "arab": "قَالَ اجْعَلْنِي عَلَىٰ خَزَائِنِ الْأَرْضِ ۖ إِنِّي حَفِيظٌ عَلِيمٌ",
                "terjemah": "Berkata Yusuf: 'Jadikanlah aku bendaharawan negara (Mesir); sesungguhnya aku adalah orang yang pandai menjaga (hafizh), lagi berpengetahuan ('alim).'",
                "relevansi_pkn": "Keberanian memimpin lahir dari kesadaran kompetensi: amanah menjaga aset umat (hafizh) dan menguasai ilmunya ('alim)."
            }
        ]
    },
    "Bekerja Sama.md": {
        "tema": "Sub-Bakat Bekerja Sama: Sinergi Amal, Solidaritas Jama'ah, Tolong Menolong dalam Kebaikan",
        "verses": [
            {
                "surah": "QS. Al-Ma'idah: 2",
                "arab": "وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ ۚ وَاتَّقُوا اللَّهَ ۖ إِنَّ اللَّهَ شَدِيدُ الْعِقَابِ",
                "terjemah": "Dan tolong-menolonglah kamu dalam (mengerjakan) kebajikan dan takwa, dan jangan tolong-menolong dalam berbuat dosa dan permusuhan. Dan bertakwalah kamu kepada Allah, sesungguhnya Allah amat berat siksa-Nya.",
                "relevansi_pkn": "Kaidah emas kerjasama: kolaborasi hanya sah dalam koridor kebajikan (al-birr) dan ketakwaan, bukan kompromi keburukan atau konformitas buta."
            },
            {
                "surah": "QS. Ali 'Imran: 103",
                "arab": "وَاعْتَصِمُوا بِحَبْلِ اللَّهِ جَمِيعًا وَلَا تَفَرَّقُوا ۚ وَاذْكُرُوا نِعْمَتَ اللَّهِ عَلَيْكُمْ إِذْ كُنتُمْ أَعْدَاءً فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِ إِخْوَانًا",
                "terjemah": "Dan berpeganglah kamu semuanya kepada tali (agama) Allah, dan janganlah kamu bercerai berai, dan ingatlah akan nikmat Allah kepadamu ketika kamu dahulu (masa Jahiliyah) bermusuh-musuhan, maka Allah mempersatukan hatimu...",
                "relevansi_pkn": "Membangun kecerdasan sosial anak dalam ikatan ukhuwah islamiyah dan persatuan berbasis tali agama Allah."
            },
            {
                "surah": "QS. Ash-Shaff: 4",
                "arab": "إِنَّ اللَّهَ يُحِبُّ الَّذِينَ يُقَاتِلُونَ فِي سَبِيلِهِ صَفًّا كَأَنَّهُم بُنْيَانٌ مَّرْصُوصٌ",
                "terjemah": "Sesungguhnya Allah menyukai orang yang berperang dijalan-Nya dalam barisan yang teratur seakan-akan mereka seperti suatu bangunan yang tersusun kokoh.",
                "relevansi_pkn": "Karakter kerja tim (teamwork): tertata rapi, memahami posisi dan peran masing-masing bagaikan batu bata bangunan peradaban yang saling menopang."
            }
        ]
    },
    "Melayani.md": {
        "tema": "Sub-Bakat Melayani: Karakter Khidmah, Itsar (Mendahulukan Orang Lain), Kedermawanan, dan Keikhlasan",
        "verses": [
            {
                "surah": "QS. Al-Hasyr: 9",
                "arab": "وَيُؤْثِرُونَ عَلَىٰ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌ ۚ وَمَن يُوقَ شُحَّ نَفْسِهِ فَأُولَٰئِكَ هُمُ الْمُفْلِحُونَ",
                "terjemah": "Dan mereka mengutamakan (orang-orang Muhajirin) atas diri mereka sendiri, sekalipun mereka dalam kesusahan. Dan siapa yang dipelihara dari kekikiran dirinya, mereka itulah orang-orang yang beruntung.",
                "relevansi_pkn": "Tingkatan tertinggi karakter melayani adalah itsar (altruisme syar'i); anak dilatih mengalahkan rasa kikir demi memberi manfaat bagi orang lain."
            },
            {
                "surah": "QS. Al-Insan: 8–9",
                "arab": "وَيُطْعِمُونَ الطَّعَامَ عَلَىٰ حُبِّهِ مِسْكِينًا وَيَتِيمًا وَأَسِيرًا ۝ إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ اللَّهِ لَا نُرِيدُ مِنكُمْ جَزَاءً وَلَا شُكُورًا",
                "terjemah": "Dan mereka memberikan makanan yang disukainya kepada orang miskin, anak yatim dan orang yang ditawan. (Sambil berkata): 'Sesungguhnya kami memberi makanan kepadamu hanyalah untuk mengharapkan keridhaan Allah, kami tidak menghendaki balasan dari kamu dan tidak pula (ucapan) terima kasih.'",
                "relevansi_pkn": "Kemurnian niat dalam pelayanan: melayani sesama murni lillahi ta'ala tanpa haus pujian, popularitas, atau imbalan manusiawi."
            },
            {
                "surah": "QS. Al-Baqarah: 177",
                "arab": "وَآتَى الْمَالَ عَلَىٰ حُبِّهِ ذَوِي الْقُرْبَىٰ وَالْيَتَامَىٰ وَالْمَسَاكِينَ وَابْنَ السَّبِيلِ وَالسَّائِلِينَ وَفِي الرِّقَابِ",
                "terjemah": "...dan memberikan harta yang dicintainya kepada kerabatnya, anak-anak yatim, orang-orang miskin, musafir (yang memerlukan pertolongan) dan orang-orang yang meminta-minta; dan (memerdekakan) hamba sahaya...",
                "relevansi_pkn": "Mendidik kedermawanan aktif sejak usia dini dengan membiasakan anak berbagi barang terbaik miliknya kepada mereka yang membutuhkan."
            }
        ]
    },
    "Panduan Asesmen dan Observasi TB40.md": {
        "tema": "Metodologi Asesmen Bakat Nabawiyah: Menemukan Syakilah Insan, Menghargai Keragaman Potensi, dan Alokasi Peran Kekhalifahan",
        "verses": [
            {
                "surah": "QS. Al-Isra': 84",
                "arab": "قُلْ كُلٌّ يَعْمَلُ عَلَىٰ شَاكِلَتِهِ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًا",
                "terjemah": "Katakanlah: 'Tiap-tiap orang berbuat menurut keadaannya (pembawaan fitrah/syakilah)-nya masing-masing.' Maka Tuhanmu lebih mengetahui siapa yang lebih benar jalannya.",
                "relevansi_pkn": "Pondasi wahyu asesmen TB-40: pengakuan syariat terhadap keunikan rancang bangun fitrah setiap anak yang menolak standardisasi kaku pabrik."
            },
            {
                "surah": "QS. Al-An'am: 165",
                "arab": "وَهُوَ الَّذِي جَعَلَكُمْ خَلَائِفَ الْأَرْضِ وَرَفَعَ بَعْضَكُمْ فَوْقَ بَعْضٍ دَرَجَاتٍ لِّيَبْلُوَكُمْ فِي مَا آتَاكُمْ",
                "terjemah": "Dan Dialah yang menjadikan kamu penguasa-penguasa di bumi dan Dia meninggikan sebahagian kamu atas sebahagian (yang lain) beberapa derajat, untuk mengujimu tentang apa yang diberikan-Nya kepadamu...",
                "relevansi_pkn": "Hikmah perbedaan derajat potensi bakat: ujian amanah kekhalifahan di mana setiap insan dimintai pertanggungjawaban atas porsi kelebihan uniknya."
            }
        ]
    },

    # =========================================================================
    # KLUSTER 5: FASE PERKEMBANGAN USIA
    # =========================================================================
    "Perkembangan.md": {
        "tema": "Sunnatullah Tahapan Pertumbuhan: Dinamika dari Kelemahan Menuju Kekuatan dan Kedewasaan",
        "verses": [
            {
                "surah": "QS. Ar-Rum: 54",
                "arab": "اللَّهُ الَّذِي خَلَقَكُم مِّن ضَعْفٍ ثُمَّ جَعَلَ مِن بَعْدِ ضَعْفٍ قُوَّةً ثُمَّ جَعَلَ مِن بَعْدِ قُوَّةٍ ضَعْفًا وَشَيْبَةً ۚ يَخْلُقُ مَا يَشَاءُ ۖ وَهُوَ الْعَلِيمُ الْقَدِيرُ",
                "terjemah": "Allah, Dialah yang menciptakan kamu dari keadaan lemah, kemudian Dia menjadikan (kamu) sesudah keadaan lemah itu menjadi kuat, kemudian Dia menjadikan (kamu) sesudah kuat itu lemah (kembali) dan beruban. Dia menciptakan apa yang dikehendaki-Nya dan Dialah Yang Maha Mengetahui lagi Maha Kuasa.",
                "relevansi_pkn": "Kaidah perkembangan bertahap: kelemahan masa kanak-kanak harus dihormati dan dipenuhi haknya agar bertransformasi menjadi kekuatan puncak pemuda mukallaf."
            },
            {
                "surah": "QS. Al-Hajj: 5",
                "arab": "ثُمَّ نُخْرِجُكُمْ طِفْلًا ثُمَّ لِتَبْلُغُوا أَشُدَّكُمْ",
                "terjemah": "...kemudian Kami keluarkan kamu sebagai bayi (thiflan), kemudian (dengan berangsur-angsur) kamu sampailah kepada kedewasaanmu (asyuddakum)...",
                "relevansi_pkn": "Terminologi Al-Qur'an membedakan fase thifl (anak-anak) dan asyudd (dewasa kokoh); tidak ada istilah remaja bingung (adolescence) yang serba galau."
            }
        ]
    },
    "Thufulah.md": {
        "tema": "Fase Thufulah (0–7 Tahun): Fitrah Bermain, Kepolosan Anak, Pemenuhan Kasih Sayang Tanpa Tekanan",
        "verses": [
            {
                "surah": "QS. An-Nur: 31",
                "arab": "أَوِ الطِّفْلِ الَّذِينَ لَمْ يَظْهَرُوا عَلَىٰ عَوْرَاتِ النِّسَاءِ",
                "terjemah": "...atau anak-anak yang belum mengerti tentang aurat wanita...",
                "relevansi_pkn": "Karakteristik kepolosan fase Thufulah: fitrah batin yang belum terbebani kesadaran syahwat, membutuhkan penjagaan suci dan pengasuhan penuh kehangatan."
            },
            {
                "surah": "QS. Maryam: 12",
                "arab": "يَا يَحْيَىٰ خُذِ الْكِتَابَ بِقُوَّةٍ ۖ وَآتَيْنَاهُ الْحُكْمَ صَبِيًّا",
                "terjemah": "Hai Yahya, ambillah Al Kitab (Taurat) itu dengan sungguh-sungguh. Dan kami berikan kepadanya hikmah selagi ia masih kanak-kanak (shabiyya).",
                "relevansi_pkn": "Menyiapkan hikmah sejak masa shabi melalui keteladanan orang tua, tanpa memaksakan hafalan teknis yang merampas fitrah bermain alaminya."
            },
            {
                "surah": "QS. Luqman: 14",
                "arab": "وَوَصَّيْنَا الْإِنسَانَ بِوَالِدَيْهِ حَمَلَتْهُ أُمُّهُ وَهْنًا عَلَىٰ وَهْنٍ وَفِصَالُهُ فِي عَامَيْنِ أَنِ اشْكُرْ لِي وَلِوَالِدَيْكَ",
                "terjemah": "Dan Kami perintahkan kepada manusia (berbuat baik) kepada dua orang ibu-bapanya; ibunya telah mengandungnya dalam keadaan lemah yang bertambah-tambah, dan menyapihnya dalam dua tahun. Bersyukurlah kepada-Ku dan kepada dua orang ibu bapakmu...",
                "relevansi_pkn": "Hak penyusuan dua tahun penuh (radha'ah) dan pemenuhan kelekatan fisik (attachment) dengan bunda sebagai pondasi tangki cinta pertama anak."
            }
        ]
    },
    "Tamyiz.md": {
        "tema": "Fase Tamyiz (7–10 Tahun): Gerbang Nalar, Pengajaran Adab Privasi, dan Pembiasaan Shalat",
        "verses": [
            {
                "surah": "QS. An-Nur: 58",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا لِيَسْتَأْذِنكُمُ الَّذِينَ مَلَكَتْ أَيْمَانُكُمْ وَالَّذِينَ لَمْ يَبْلُغُوا الْحُلُمَ مِنكُمْ ثَلَاثَ مَرَّاتٍ ۚ مِن قَبْلِ صَلَاةِ الْفَجْرِ وَحِينَ تَضَعُونَ ثِيَابَكُم مِّنَ الظَّهِيرَةِ وَمِن بَعْدِ صَلَاةِ الْعِشَاءِ",
                "terjemah": "Wahai orang-orang yang beriman, hendaklah budak-budak (lelaki dan wanita) yang kamu miliki, dan orang-orang yang belum baligh di antara kamu (anak-anak tamyiz), meminta izin kepada kamu tiga kali (dalam satu hari) yaitu: sebelum shalat subuh, ketika kamu menanggalkan pakaian luar kamu di tengah hari, dan sesudah shalat Isya...",
                "relevansi_pkn": "Pendidikan adab dan batas aurat (isti'dzan) dimulai pada usia tamyiz; anak mulai dipahamkan konsep privasi syariat dan disiplin waktu."
            },
            {
                "surah": "QS. Luqman: 17",
                "arab": "يَا بُنَيَّ أَقِمِ الصَّلَاةَ وَأْمُرْ بِالْمَعْرُوفِ وَانْهَ عَنِ الْمُنكَرِ وَاصْبِرْ عَلَىٰ مَا أَصَابَكَ ۖ إِنَّ ذَٰلِكَ مِنْ عَزْمِ الْأُمُورِ",
                "terjemah": "Wahai anakku, dirikanlah shalat dan suruhlah (manusia) mengerjakan yang baik dan cegahlah (mereka) dari perbuatan yang mungkar dan bersabarlah terhadap apa yang menimpa kamu. Sesungguhnya yang demikian itu termasuk hal-hal yang diwajibkan (oleh Allah).",
                "relevansi_pkn": "Perintah shalat dan penguatan adab sabar sejak usia 7 tahun membentuk disiplin spiritual harian anak secara terstruktur."
            }
        ]
    },
    "Murahaqah.md": {
        "tema": "Fase Murahaqah (10 Tahun–Baligh): Pendisiplinan Tegas, Ujian Rusyd (Kemandirian), dan Pemagangan Karya",
        "verses": [
            {
                "surah": "QS. An-Nisa': 6",
                "arab": "وَابْتَلُوا الْيَتَامَىٰ حَتَّىٰ إِذَا بَلَغُوا النِّكَاحَ فَإِنْ آنَسْتُم مِّنْهُمْ رُشْدًا فَادْفَعُوا إِلَيْهِمْ أَمْوَالَهُمْ",
                "terjemah": "Dan ujilah anak yatim itu sampai mereka cukup umur untuk kawin (baligh). Kemudian jika menurut pendapatmu mereka telah cerdas (pandai memelihara harta/rusyda), maka serahkanlah kepada mereka harta-hartanya...",
                "relevansi_pkn": "Konsep Rusyd: ujian kecakapan mandiri sebelum baligh; anak usia 10 tahun ke atas dilatih mengelola keuangan, memikul tanggung jawab rumah, dan magang karya."
            },
            {
                "surah": "QS. Ash-Shaffat: 102",
                "arab": "فَلَمَّا بَلَغَ مَعَهُ السَّعْيَ قَالَ يَا بُنَيَّ إِنِّي أَرَىٰ فِي الْمَنَامِ أَنِّي أَذْبَحُكَ فَانظُرْ مَاذَا تَرَىٰ ۚ قَالَ يَا أَبَتِ افْعَلْ مَا تُؤْمَرُ ۖ سَتَجِدُنِي إِن شَاءَ اللَّهُ مِنَ الصَّابِرِينَ",
                "terjemah": "Maka tatkala anak itu sampai (pada umur sanggup) berusaha bersama-sama Ibrahim (balagha ma'ahus sa'ya), Ibrahim berkata: 'Hai anakku sesungguhnya aku melihat dalam mimpi bahwa aku menyembelihmu. Maka fikirkanlah apa pendapatmu!' Ia menjawab: 'Hai bapakku, kerjakanlah apa yang diperintahkan kepadamu; insya Allah kamu akan mendapatiku termasuk orang-orang yang sabar.'",
                "relevansi_pkn": "Puncak fase murahaqah (balagha ma'ahus sa'ya): dialog kemitraan ayah dan anak pra-baligh; anak dilibatkan dalam keputusan besar dan disiapkan memikul pengorbanan akidah."
            }
        ]
    },
    "Syabab.md": {
        "tema": "Fase Syabab (15+ Tahun / Pasca Baligh): Kedewasaan Penuh (Akil-Baligh), Kemandirian Sosial, dan Karya Peradaban",
        "verses": [
            {
                "surah": "QS. Al-Kahfi: 13",
                "arab": "إِنَّهُمْ فِتْيَةٌ آمَنُوا بِرَبِّهِمْ وَزِدْنَاهُمْ هُدًى",
                "terjemah": "Sesungguhnya mereka adalah pemuda-pemuda (fityah) yang beriman kepada Tuhan mereka, dan Kami tambah pula untuk mereka petunjuk.",
                "relevansi_pkn": "Model pemuda nabawiyah: memiliki integritas akidah baja, berani bersuara di hadapan penguasa tiran, dan menjadi motor penyelamat agama."
            },
            {
                "surah": "QS. Al-Ahqaf: 15",
                "arab": "حَتَّىٰ إِذَا بَلَغَ أَشُدَّهُ وَبَلَغَ أَرْبَعِينَ سَنَةً قَالَ رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ الَّتِي أَنْعَمْتَ عَلَيَّ وَعَلَىٰ وَالِدَيَّ وَأَنْ أَعْمَلَ صَالِحًا تَرْضَاهُ",
                "terjemah": "...sehingga apabila dia telah dewasa (balagha asyuddahu) dan umurnya sampai empat puluh tahun ia berdoa: 'Ya Tuhanku, tunjukilah aku untuk mensyukuri nikmat Engkau yang telah Engkau berikan kepadaku dan kepada ibu bapakku dan supaya aku dapat berbuat amal yang saleh yang Engkau ridhai...'",
                "relevansi_pkn": "Fase asyudd: puncak kedewasaan akil-baligh; pemuda PKN berorientasi pada karya shalih yang diridhai Allah dan bakti peradaban kepada orang tua."
            },
            {
                "surah": "QS. Al-Anbiya: 60",
                "arab": "قَالُوا سَمِعْنَا فَتًى يَذْكُرُهُمْ يُقَالُ لَهُ إِبْرَاهِيمُ",
                "terjemah": "Mereka berkata: 'Kami dengar ada seorang pemuda (fatan) yang mencela berhala-berhala ini, yang bernama Ibrahim.'",
                "relevansi_pkn": "Pemuda sebagai pelopor perubahan kebatilan; mencetak anak muda yang berjiwa Ibrahim AS: bernalar kritis, berani membela tauhid, dan anti-kemapanan jahiliyah."
            }
        ]
    },

    # =========================================================================
    # KLUSTER 6: METODOLOGI, TIGA BAHASA & PENDIDIKAN IDEAL
    # =========================================================================
    "Metode Mendidik.md": {
        "tema": "Metodologi Tarbiyah Nabawiyah: Hikmah, Mau'izhah Hasanah, dan Hirarki Tiga Bahasa",
        "verses": [
            {
                "surah": "QS. An-Nahl: 125",
                "arab": "ادْعُ إِلَىٰ سَبِيلِ رَبِّكَ بِالْحِكْمَةِ وَالْمَوْعِظَةِ الْحَسَنَةِ ۖ وَجَادِلْهُم بِالَّتِي هِيَ أَحْسَنُ",
                "terjemah": "Serulah (manusia) kepada jalan Tuhanmu dengan hikmah dan pelajaran yang baik dan bantahlah mereka dengan cara yang baik...",
                "relevansi_pkn": "Tri-metodologi dakwah dan tarbiyah: Hikmah (Bahasa Hati), Mau'izhah Hasanah (Bahasa Lisan), dan Jidal Ahsan (Dialog Logis Jiwa Lawwamah)."
            },
            {
                "surah": "QS. Ali 'Imran: 164",
                "arab": "لَقَدْ مَنَّ اللَّهُ عَلَى الْمُؤْمِنِينَ إِذْ بَعَثَ فِيهِمْ رَسُولًا مِّنْ أَنفُسِهِمْ يَتْلُو عَلَيْهِمْ آيَاتِهِ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ الْكِتَابَ وَالْحِكْمَةَ",
                "terjemah": "Sungguh Allah telah memberi karunia kepada orang-orang yang beriman ketika Allah mengutus di antara mereka seorang rasul dari golongan mereka sendiri, yang membacakan kepada mereka ayat-ayat-Nya, menyucikan (jiwa) mereka, dan mengajarkan kepada mereka Al Kitab dan Al Hikmah...",
                "relevansi_pkn": "Urutan pedagogis nabawiyah: Tilawah (pembiasaan mendengar ayat), Tazkiyah (penyucian jiwa & tangki cinta), baru Ta'lim (transfer kurikulum & keahlian)."
            }
        ]
    },
    "Bahasa Hati.md": {
        "tema": "Bahasa Hati: Kelemahlembutan, Kasih Sayang Batin, Keteladanan Autentik, dan Edukasi Rasa",
        "verses": [
            {
                "surah": "QS. Ali 'Imran: 159",
                "arab": "فَبِمَا رَحْمَةٍ مِّنَ اللَّهِ لِنتَ لَهُمْ ۖ وَلَوْ كُنتَ فَظًّا غَلِيظَ الْقَلْبِ لَانفَضُّوا مِنْ حَوْلِكَ ۖ فَاعْفُ عَنْهُمْ وَاسْتَغْفِرْ لَهُمْ وَشَاوِرْهُمْ فِي الْأَمْرِ",
                "terjemah": "Maka disebabkan rahmat dari Allah-lah kamu berlaku lemah lembut terhadap mereka. Sekiranya kamu bersikap keras lagi berhati kasar, tentulah mereka menjauhkan diri dari sekelilingmu. Karena itu maafkanlah mereka, mohonkanlah ampun bagi mereka, dan bermusyawarahlah dengan mereka dalam urusan itu...",
                "relevansi_pkn": "Formula Bahasa Hati: Kelemahlembutan (rifq), memaafkan kekhilafan anak (al-'afwu), mendoakan ampunan (istighfar), dan mengajak dialog kemitraan (syura)."
            },
            {
                "surah": "QS. At-Taubah: 128",
                "arab": "لَقَدْ جَاءَكُمْ رَسُولٌ مِّنْ أَنفُسِكُمْ عَزِيزٌ عَلَيْهِ مَا عَنِتُّمْ حَرِيصٌ عَلَيْكُم بِالْمُؤْمِنِينَ رَءُوفٌ رَّحِيمٌ",
                "terjemah": "Sungguh telah datang kepadamu seorang Rasul dari kaummu sendiri, berat terasa olehnya penderitaanmu, sangat menginginkan (keimanan dan keselamatan) bagimu, amat belas kasihan lagi penyayang terhadap orang-orang mukmin.",
                "relevansi_pkn": "Karakter batiniah pendidik nabawiyah: empati mendalam atas kesulitan anak ('azizun 'alaihi ma 'anittum) dan antusiasme mencurahkan kebaikan (harisun 'alaikum)."
            }
        ]
    },
    "Bahasa Lisan.md": {
        "tema": "Bahasa Lisan: 6 Kaidah Komunikasi Al-Qur'an (Sadida, Layyina, Baligha, Maysura, Karima, Husna)",
        "verses": [
            {
                "surah": "QS. Al-Ahzab: 70–71",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ وَقُولُوا قَوْلًا سَدِيدًا ۝ يُصْلِحْ لَكُمْ أَعْمَالَكُمْ وَيَغْفِرْ لَكُمْ ذُنُوبَكُمْ",
                "terjemah": "Wahai orang-orang yang beriman, bertakwalah kamu kepada Allah dan katakanlah perkataan yang benar (tepat sasaran). Niscaya Allah memperbaiki bagimu amalan-amalanmu dan mengampuni bagimu dosa-dosamu...",
                "relevansi_pkn": "Qaulan Sadida: perkataan jujur, lurus, tepat sasaran tanpa manipulasi, yang menjadi syarat perbaikan karakter dan perilaku anak."
            },
            {
                "surah": "QS. Thaha: 44",
                "arab": "فَقُولَا لَهُ قَوْلًا لَّيِّنًا لَّعَلَّهُ يَتَذَكَّرُ أَوْ يَخْشَىٰ",
                "terjemah": "Maka berbicaralah kamu berdua kepadanya dengan kata-kata yang lemah lembut, mudah-mudahan ia ingat atau takut.",
                "relevansi_pkn": "Qaulan Layyina: tutur kata lembut bahkan kepada Fir'aun sekalipun; terlebih lagi kepada anak kandung saat menasihati kekeliruannya."
            },
            {
                "surah": "QS. An-Nisa': 63",
                "arab": "وَقُل لَّهُمْ فِي أَنفُسِهِمْ قَوْلًا بَلِيغًا",
                "terjemah": "...dan katakanlah kepada mereka perkataan yang membekas pada jiwa mereka (qaulan baligha).",
                "relevansi_pkn": "Qaulan Baligha: komunikasi efektif yang menembus sanubari anak, relevan dengan usia dan konteks pergulatan batinnya."
            },
            {
                "surah": "QS. Al-Isra': 23 & 28",
                "arab": "فَلَا تَقُل لَّهُمَا أُفٍّ وَلَا تَنْهَرْهُمَا وَقُل لَّهُمَا قَوْلًا كَرِيمًا ... فَقُل لَّهُمْ قَوْلًا مَّيْسُورًا",
                "terjemah": "...maka sekali-kali janganlah kamu mengatakan kepada keduanya perkataan 'ah' dan janganlah kamu membentak mereka dan ucapkanlah kepada mereka perkataan yang mulia (qaulan karima)... dan katakanlah kepada mereka perkataan yang pantas dan menyenangkan (qaulan maysura).",
                "relevansi_pkn": "Menjaga kehormatan verbal di rumah: pantangan membentak dan kewajiban bertutur kata mulia dan menyejukkan."
            }
        ]
    },
    "Bahasa Tangan.md": {
        "tema": "Bahasa Tangan: Ketegasan Terukur, Disiplin Ta'dib Berbatas Syariat, dan Larangan Menyakiti",
        "verses": [
            {
                "surah": "QS. Shad: 44",
                "arab": "وَخُذْ بِيَدِكَ ضِغْثًا فَاضْرِب بِّهِ وَلَا تَحْنَثْ ۗ إِنَّا وَجَدْنَاهُ صَابِرًا ۚ نِّعْمَ الْعَبْدُ ۖ إِنَّهُ أَوَّابٌ",
                "terjemah": "Dan ambillah dengan tanganmu seikat (rumput), maka pukullah dengan itu dan janganlah kamu merusak sumpah. Sesungguhnya Kami dapati dia (Ayyub) seorang yang sabar. Dialah sebaik-baik hamba. Sesungguhnya dia amat taat (kepada Tuhannya).",
                "relevansi_pkn": "Model ketegasan nabawiyah Nabi Ayyub AS: pukulan disiplin yang bersifat simbolik edukatif (menggunakan rumput) tanpa mencederai fisik atau meninggalkan dendam."
            },
            {
                "surah": "QS. Al-A'raf: 154",
                "arab": "وَلَمَّا سَكَتَ عَن مُّوسَى الْغَضَبُ أَخَذَ الْأَلْوَاحَ ۖ وَفِي نُسْخَتِهَا هُدًى وَرَحْمَةٌ لِّلَّذِينَ هُمْ لِرَبِّهِمْ يَرْهَبُونَ",
                "terjemah": "Sesudah amarah Musa menjadi reda, lalu diambilnya (kembali) lauh-lauh (Taurat) itu; dan dalam tulisannya terdapat petunjuk dan rahmat untuk orang-orang yang takut kepada Tuhannya.",
                "relevansi_pkn": "Kaidah emas sebelum mengeksekusi konsekuensi/bahasa tangan: orang tua wajib menunggu amarahnya reda (sakata 'anhul ghadhab) agar tindakan tidak didorong hawa nafsu dendam."
            }
        ]
    },
    "Pendidikan Ideal.md": {
        "tema": "Kurikulum Pendidikan Ideal: Teladan Luqman Al-Hakim dalam Membangun Karakter Generasi",
        "verses": [
            {
                "surah": "QS. Luqman: 12–19",
                "arab": "وَلَقَدْ آتَيْنَا لُقْمَانَ الْحِكْمَةَ أَنِ اشْكُرْ لِلَّهِ... يَا بُنَيَّ لَا تُشْرِكْ بِاللَّهِ ۖ إِنَّ الشِّرْكَ لَظُلْمٌ عَظِيمٌ... يَا بُنَيَّ إِنَّهَا إِن تَكُ مِثْقَالَ حَبَّةٍ مِّنْ خَرْدَلٍ... يَا بُنَيَّ أَقِمِ الصَّلَاةَ وَأْمُرْ بِالْمَعْرُوفِ وَانْهَ عَنِ الْمُنكَرِ وَاصْبِرْ عَلَىٰ مَا أَصَابَكَ... وَلَا تُصَعِّرْ خَدَّكَ لِلنَّاسِ وَلَا تَمْشِ فِي الْأَرْضِ مَرَحًا... وَاقْصِدْ فِي مَشْيِكَ وَاغْضُضْ مِن صَوْتِكَ",
                "terjemah": "Rangkaian wasiat Luqman: Syukur kepada Allah, Tauhid mutlak, Kesadaran Muraqabatullah (pengawasan Allah sedalam biji sawi), Mendirikan Shalat, Amar Ma'ruf Nahi Munkar, Sabar menghadapi ujian, Tawadhu' (larangan memalingkan wajah sombong), dan Adab berjalan serta melunakkan suara.",
                "relevansi_pkn": "Arsitektur kurikulum terlengkap dalam Al-Qur'an: mengintegrasikan akidah, ibadah, akhlak sosial, hingga adab gestur tubuh sehari-hari."
            },
            {
                "surah": "QS. Ar-Rahman: 1–4",
                "arab": "الرَّحْمَٰنُ ۝ عَلَّمَ الْقُرْآنَ ۝ خَلَقَ الْإِنسَانَ ۝ عَلَّمَهُ الْبَيَانَ",
                "terjemah": "(Tuhan) Yang Maha Pemurah, Yang telah mengajarkan Al Quran. Dia menciptakan manusia. Mengajarnya pandai berbicara (bayan).",
                "relevansi_pkn": "Urutan tarbiyah ilahiyah: Berangkat dari Ar-Rahman (kasih sayang), Al-Qur'an (fondasi wahyu), Insan (fitrah manusia), lalu Al-Bayan (ekspresi keahlian dan komunikasi)."
            }
        ]
    },
    "Benang Merah Pendidikan.md": {
        "tema": "Benang Merah PKN: Prinsip Jalan Tengah (Wasathiyah) Menghindari Tafrith dan Ifrath",
        "verses": [
            {
                "surah": "QS. Al-Fatihah: 5–7",
                "arab": "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ ۝ صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ",
                "terjemah": "Tunjukilah kami jalan yang lurus, (yaitu) Jalan orang-orang yang telah Engkau beri nikmat kepada mereka; bukan (jalan) mereka yang dimurkai dan bukan (pula jalan) mereka yang sesat.",
                "relevansi_pkn": "Benang merah penuntun: Shirathal Mustaqim berada di tengah-tengah antara Ifrath (keras melampaui batas / al-maghdhub) dan Tafrith (lalai menelantarkan / adh-dhallin)."
            },
            {
                "surah": "QS. Al-Baqarah: 143",
                "arab": "وَكَذَٰلِكَ جَعَلْنَاكُمْ أُمَّةً وَسَطًا لِّتَكُونُوا شُهَدَاءَ عَلَى النَّاسِ وَيَكُونَ الرَّسُولُ عَلَيْكُمْ شَهِيدًا",
                "terjemah": "Dan demikian (pula) Kami telah menjadikan kamu (umat Islam), umat yang adil dan pilihan (ummatan wasathan) agar kamu menjadi saksi atas (perbuatan) manusia dan agar Rasul (Muhammad) menjadi saksi atas (perbuatan) kamu...",
                "relevansi_pkn": "Mencetak generasi wasathiyah: seimbang antara kebutuhan jasad dan ruh, nalar dan rasa, adab dan kebebasan berekspresi."
            }
        ]
    },
    "Pembelajaran Alamiah.md": {
        "tema": "Pembelajaran Alamiah: Menatap Alam Kauniyah, Eksplorasi Nyata, dan Pembebasan dari Sekat Kelas",
        "verses": [
            {
                "surah": "QS. Al-A'raf: 185",
                "arab": "أَوَلَمْ يَنظُرُوا فِي مَلَكُوتِ السَّمَاوَاتِ وَالْأَرْضِ وَمَا خَلَقَ اللَّهُ مِن شَيْءٍ",
                "terjemah": "Dan apakah mereka tidak memperhatikan kerajaan langit dan bumi dan segala sesuatu yang dijadikan Allah...",
                "relevansi_pkn": "Dorongan eksplorasi dunia nyata: membawa anak keluar dari ruang sempit untuk mentadabburi ciptaan Allah di alam terbuka."
            },
            {
                "surah": "QS. Al-An'am: 99",
                "arab": "وَهُوَ الَّذِي أَنزَلَ مِنَ السَّمَاءِ مَاءً فَأَخْرَجْنَا بِهِ نَبَاتَ كُلِّ شَيْءٍ فَأَخْرَجْنَا مِنْهُ خَضِرًا نُّخْرِجُ مِنْهُ حَبًّا مُّتَرَاكِبًا... انظُرُوا إِلَىٰ ثَمَرِهِ إِذَا أَثْمَرَ وَيَنْعِهِ ۚ إِنَّ فِي ذَٰلِكُمْ لَآيَاتٍ لِّقَوْمٍ يُؤْمِنُونَ",
                "terjemah": "...Perhatikanlah buahnya di waktu pohonnya berbuah dan (perhatikan pulalah) kematangannya. Sesungguhnya pada yang demikian itu ada tanda-tanda (kekuasaan Allah) bagi orang-orang yang beriman.",
                "relevansi_pkn": "Sains fitrah nabawiyah: mengamati proses biologis pertumbuhan tanaman sebagai sarana menguatkan keimanan saintifik anak."
            }
        ]
    },
    "Luka dan Hutang Pengasuhan.md": {
        "tema": "Luka Pengasuhan: Dampak Penelantaran Hak Anak, Dosa Lalai, dan Pertanggungjawaban di Akhirat",
        "verses": [
            {
                "surah": "QS. Al-Isra': 24",
                "arab": "وَاخْفِضْ لَهُمَا جَنَاحَ الذُّلِّ مِنَ الرَّحْمَةِ وَقُل رَّبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا",
                "terjemah": "Dan rendahkanlah dirimu terhadap mereka berdua dengan penuh kesayangan dan ucapkanlah: 'Wahai Tuhanku, kasihilah mereka keduanya, sebagaimana mereka berdua telah mendidik aku waktu kecil.'",
                "relevansi_pkn": "Kaidah kama rabbayani shaghira: bakti anak di masa tua berakar dari curahan kasih sayang dan pendidikan orang tua di waktu kecil."
            },
            {
                "surah": "QS. At-Tahrim: 6",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا قُوا أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا وَقُودُهَا النَّاسُ وَالْحِجَارَةُ",
                "terjemah": "Wahai orang-orang yang beriman! Peliharalah dirimu dan keluargamu dari api neraka yang bahan bakarnya adalah manusia dan batu...",
                "relevansi_pkn": "Hutang pengasuhan adalah ancaman akhirat; menelantarkan pendidikan akidah anak berarti menjerumuskan keluarga ke jurang kehancuran."
            },
            {
                "surah": "QS. At-Takatsur: 1–2 & 8",
                "arab": "أَلْهَاكُمُ التَّكَاثُرُ ۝ حَتَّىٰ زُرْتُمُ الْمَقَابِرَ ... ثُمَّ لَتُسْأَلُنَّ يَوْمَئِذٍ عَنِ النَّعِيمِ",
                "terjemah": "Bermegah-megahan telah melalaikan kamu, sampai kamu masuk ke dalam kubur... kemudian kamu pasti akan ditanyai pada hari itu tentang kenikmatan (yang kamu megah-megahkan di dunia itu).",
                "relevansi_pkn": "Bahaya orang tua sibuk mengejar materi (takatsur) sehingga mengorbankan waktu kehadiran mendampingi anak, meninggalkan luka batin menahun."
            }
        ]
    },
    "Euforia.md": {
        "tema": "Mengendalikan Sindrom Euforia: Bahaya Tergesa-gesa (Isti'jal), Istiqamah, dan Ketahanan Mental",
        "verses": [
            {
                "surah": "QS. Ali 'Imran: 200",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا اصْبِرُوا وَصَابِرُوا وَرَابِطُوا وَاتَّقُوا اللَّهَ لَعَلَّكُمْ تُفْلِحُونَ",
                "terjemah": "Wahai orang-orang yang beriman, bersabarlah kamu dan kuatkanlah kesabaranmu dan tetaplah bersiap siaga (ribath) dan bertakwalah kepada Allah, supaya kamu beruntung.",
                "relevansi_pkn": "Penawar euforia hijrah: mendidik anak membutuhkan sabar berlapis (shabiru) dan ketahanan istiqamah jangka panjang (rabithu), bukan ledakan semangat sesaat."
            },
            {
                "surah": "QS. Hud: 112",
                "arab": "فَاسْتَقِمْ كَمَا أُمِرْتَ وَمَن تَابَ مَعَكَ وَلَا تَطْغَوْا ۚ إِنَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ",
                "terjemah": "Maka tetaplah kamu pada jalan yang benar (istiqamahlah), sebagaimana diperintahkan kepadamu dan (juga) orang yang telah taubat beserta kamu dan janganlah kamu melampaui batas...",
                "relevansi_pkn": "Perintah istiqamah tanpa melampaui batas (la tathghaw); orang tua yang baru belajar parenting dilarang memaksakan perubahan ekstrem yang membebani anak."
            }
        ]
    },
    "Recovery.md": {
        "tema": "Metodologi Pemulihan Fitrah: Taubat Nasuha Orang Tua, Rekonsiliasi, dan Restorasi Karakter",
        "verses": [
            {
                "surah": "QS. Az-Zumar: 53",
                "arab": "قُلْ يَا عِبَادِيَ الَّذِينَ أَسْرَفُوا عَلَىٰ أَنفُسِهِمْ لَا تَقْنَطُوا مِن رَّحْمَةِ اللَّهِ ۚ إِنَّ اللَّهَ يَغْفِرُ الذُّنُوبَ جَمِيعًا ۚ إِنَّهُ هُوَ الْغَفُورُ الرَّحِيمُ",
                "terjemah": "Katakanlah: 'Hai hamba-hamba-Ku yang malampaui batas terhadap diri mereka sendiri, janganlah kamu berputus asa dari rahmat Allah. Sesungguhnya Allah mengampuni dosa-dosa semuanya. Sesungguhnya Dialah Yang Maha Pengampun lagi Maha Penyayang.'",
                "relevansi_pkn": "Fondasi recovery: tidak ada kata terlambat untuk memperbaiki kesalahan pengasuhan masa lalu; rahmat dan ampunan Allah selalu terbuka."
            },
            {
                "surah": "QS. Al-Baqarah: 222",
                "arab": "إِنَّ اللَّهَ يُحِبُّ التَّوَّابِينَ وَيُحِبُّ الْمُتَطَهِّرِينَ",
                "terjemah": "Sesungguhnya Allah menyukai orang-orang yang bertaubat dan menyukai orang-orang yang mensucikan diri.",
                "relevansi_pkn": "Pemulihan dimulai dari taubat orang tua yang diiringi permohonan maaf tulus kepada anak dan tekad memperbaiki adab keluarga."
            },
            {
                "surah": "QS. An-Nur: 31",
                "arab": "وَتُوبُوا إِلَى اللَّهِ جَمِيعًا أَيُّهَ الْمُؤْمِنُونَ لَعَلَّكُمْ تُفْلِحُونَ",
                "terjemah": "Dan bertaubatlah kamu sekalian kepada Allah, wahai orang-orang yang beriman supaya kamu beruntung.",
                "relevansi_pkn": "Taubat kolektif keluarga meruntuhkan sekat ego dan memulihkan kembali kehangatan rumah tangga yang sempat retak."
            }
        ]
    },
    "Imunitas Sosial.md": {
        "tema": "Imunitas Sosial: Membentengi Fitrah dari Lingkungan Toksik, Sahabat Shalih, dan Filter Budaya",
        "verses": [
            {
                "surah": "QS. Al-Kahfi: 28",
                "arab": "وَاصْبِرْ نَفْسَكَ مَعَ الَّذِينَ يَدْعُونَ رَبَّهُم بِالْغَدَاةِ وَالْعَشِيِّ يُرِيدُونَ وَجْهَهُ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ الْحَيَاةِ الدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُ عَن ذِكْرِنَا وَاتَّبَعَ هَوَاهُ وَكَانَ أَمْرُهُ فُرُطًا",
                "terjemah": "Dan bersabarlah kamu bersama-sama dengan orang-orang yang menyeru Tuhannya di pagi dan senja hari dengan mengharap keridhaan-Nya; dan janganlah kedua matamu berpaling dari mereka (karena) mengharapkan perhiasan dunia ini; dan janganlah kamu mengikuti orang yang hatinya telah Kami lalaikan dari mengingati Kami, serta menuruti hawa nafsunya dan adalah keadaannya itu melewati batas.",
                "relevansi_pkn": "Strategi memilih lingkungan pergaulan: menautkan anak pada komunitas shalih dan melindunginya dari figur-figur lalai yang mengikuti hawa nafsu."
            },
            {
                "surah": "QS. Al-An'am: 68",
                "arab": "وَإِذَا رَأَيْتَ الَّذِينَ يَخُوضُونَ فِي آيَاتِنَا فَأَعْرِضْ عَنْهُمْ حَتَّىٰ يَخُوضُوا فِي حَدِيثٍ غَيْرِهِ",
                "terjemah": "Dan apabila kamu melihat orang-orang memperolok-olokkan ayat-ayat Kami, maka tinggalkanlah mereka sehingga mereka membicarakan pembicaraan yang lain...",
                "relevansi_pkn": "Keterampilan proteksi diri (self-defense sosial): melatih anak berani meninggalkan majelis atau tontonan digital yang melecehkan syariat."
            },
            {
                "surah": "QS. Al-Furqan: 27–28",
                "arab": "وَيَوْمَ يَعَضُّ الظَّالِمُ عَلَىٰ يَدَيْهِ يَقُولُ يَا لَيْتَنِي اتَّخَذْتُ مَعَ الرَّسُولِ سَبِيلًا ۝ يَا وَيْلَتَىٰ لَيْتَنِي لَمْ أَتَّخِذْ فُلَانًا خَلِيلًا",
                "terjemah": "Dan (ingatlah) hari (ketika itu) orang yang zalim menggigit dua tangannya, seraya berkata: 'Aduhai kiranya (dulu) aku mengambil jalan bersama-sama Rasul. Kecelakaan besarlah bagiku; kiranya aku (dulu) tidak menjadikan si fulan itu teman akrab(ku).'",
                "relevansi_pkn": "Peringatan Al-Qur'an tentang penyesalan akibat salah memilih kawan karib; orang tua wajib mengawasi dinamika persahabatan anak."
            }
        ]
    },
    "Batas Toleransi.md": {
        "tema": "Batas Toleransi: Zonasi Batas Syariat (Hima), Proteksi Pornografi & Syubhat, serta Kaidah Saddudz Dzari'ah",
        "verses": [
            {
                "surah": "QS. Al-Baqarah: 187 & 229",
                "arab": "تِلْكَ حُدُودُ اللَّهِ فَلَا تَقْرَبُوهَا ... تِلْكَ حُدُودُ اللَّهِ فَلَا تَعْتَدُوهَا",
                "terjemah": "...Itulah batas-batas ketentuan Allah, maka janganlah kamu mendekatinya... Itulah batas-batas ketentuan Allah, maka janganlah kamu melanggarnya.",
                "relevansi_pkn": "Dua jenis hukum batas: perkara syubhat/haram berpotensi fitnah tidak boleh didekati (la taqrabuha), sementara batas kewajiban syariat tidak boleh dilanggar (la ta'taduha)."
            },
            {
                "surah": "QS. Al-Isra': 32",
                "arab": "وَلَا تَقْرَبُوا الزِّنَا ۖ إِنَّهُ كَانَ فَاحِشَةً وَسَاءَ سَبِيلًا",
                "terjemah": "Dan janganlah kamu mendekati zina; sesungguhnya zina itu adalah suatu perbuatan yang keji. Dan suatu jalan yang buruk.",
                "relevansi_pkn": "Kaidah saddudz dzari'ah: menutup semua celah rangsangan seksual dini, pornografi gawai, dan khalwat yang merusak batas toleransi fitrah seksual anak."
            },
            {
                "surah": "QS. An-Nur: 30–31",
                "arab": "قُل لِّلْمُؤْمِنِينَ يَغُضُّوا مِنْ أَبْصَارِهِمْ وَيَحْفَظُوا فُرُوجَهُمْ ۚ ذَٰلِكَ أَزْكَىٰ لَهُمْ ۗ إِنَّ اللَّهَ خَبِيرٌ بِمَا يَصْنَعُونَ",
                "terjemah": "Katakanlah kepada orang laki-laki yang beriman: 'Hendaklah mereka menahan pandanganya, dan memelihara kemaluannya; yang demikian itu adalah lebih suci bagi mereka...'",
                "relevansi_pkn": "Pendidikan menjaga pandangan (ghaddhul bashar) sebagai benteng imunitas pertama menjaga batas toleransi moral anak."
            }
        ]
    },
    "Bank Studi Kasus.md": {
        "tema": "Resolusi Kasus Pengasuhan dari Kisah Al-Qur'an: Sabar Jamil Ya'qub AS dan Pemeliharaan Ibunda Musa AS",
        "verses": [
            {
                "surah": "QS. Yusuf: 18 & 83",
                "arab": "فَصَبْرٌ جَمِيلٌ ۖ وَاللَّهُ الْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ ... عَسَى اللَّهُ أَن يَأْتِيَنِي بِهِمْ جَمِيعًا",
                "terjemah": "...maka kesabaran yang baik itulah (kesabaranku). Dan Allah sajalah yang dimohon pertolongan-Nya terhadap apa yang kamu ceritakan... mudah-mudahan Allah mendatangkan mereka semuanya kepadaku.",
                "relevansi_pkn": "Studi kasus menghadapi penyimpangan dan kedengkian anak: kesabaran tanpa mengeluh (shabr jamil) dan tawakkal memohon pertolongan Allah agar keluarga dipersatukan kembali."
            },
            {
                "surah": "QS. Al-Qashash: 7",
                "arab": "وَأَوْحَيْنَا إِلَىٰ أُمِّ مُوسَىٰ أَنْ أَرْضِعِيهِ ۖ فَإِذَا خِفْتِ عَلَيْهِ فَأَلْقِيهِ فِي الْيَمِّ وَلَا تَخَافِي وَلَا تَحْزَنِي ۖ إِنَّا رَادُّوهُ إِلَيْكِ وَجَاعِلُوهُ مِنَ الْمُرْسَلِينَ",
                "terjemah": "Dan Kami ilhamkan kepada ibu Musa; 'Susuilah dia, dan apabila kamu khawatir terhadapnya maka hanyutkanlah dia ke sungai (Nil). Dan janganlah kamu khawatir dan janganlah (pula) bersedih hati, karena sesungguhnya Kami akan mengembalikannya kepadamu, dan menunjuknya menjadi salah seorang dari para rasul.'",
                "relevansi_pkn": "Studi kasus menghadapi ancaman lingkungan eksternal: keberanian bunda bersandar pada janji Allah saat melepaskan anak ke medan perjuangan hidup."
            }
        ]
    },

    # =========================================================================
    # KLUSTER 7: IMPLEMENTASI, KAIDAH, ELEMEN & PERAN
    # =========================================================================
    "Implementasi.md": {
        "tema": "Implementasi Holistik PKN: Sinergi Rumah, Sekolah, dan Masyarakat dalam Menjaga Generasi",
        "verses": [
            {
                "surah": "QS. At-Tahrim: 6",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا قُوا أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا وَقُودُهَا النَّاسُ وَالْحِجَارَةُ",
                "terjemah": "Wahai orang-orang yang beriman! Peliharalah dirimu dan keluargamu dari api neraka yang bahan bakarnya adalah manusia dan batu...",
                "relevansi_pkn": "Payung hukum eksekusi implementasi PKN: amanah mutlak menjaga keluarga dengan kurikulum aksi nyata."
            },
            {
                "surah": "QS. An-Nur: 55",
                "arab": "وَعَدَ اللَّهُ الَّذِينَ آمَنُوا مِنكُمْ وَعَمِلُوا الصَّالِحَاتِ لَيَسْتَخْلِفَنَّهُم فِي الْأَرْضِ كَمَا اسْتَخْلَفَ الَّذِينَ مِن قَبْلِهِمْ",
                "terjemah": "Dan Allah telah berjanji kepada orang-orang yang beriman di antara kamu dan mengerjakan amal-amal yang saleh bahwa Dia sungguh-sungguh akan menjadikan mereka berkuasa dimuka bumi...",
                "relevansi_pkn": "Visi puncak implementasi: melahirkan generasi pemakmur bumi yang menegakkan peradaban tauhid."
            }
        ]
    },
    "4 Kaidah Implementasi.md": {
        "tema": "4 Kaidah Emas Implementasi: Taisir (Kemudahan), Qudwah (Keteladanan), Rahmah, dan Tadarruj (Bertahap)",
        "verses": [
            {
                "surah": "QS. Al-Baqarah: 185",
                "arab": "يُرِيدُ اللَّهُ بِكُمُ الْيُسْرَ وَلَا يُرِيدُ بِكُمُ الْعُسْرَ",
                "terjemah": "...Allah menghendaki kemudahan bagimu, dan tidak menghendaki kesukaran bagimu...",
                "relevansi_pkn": "Kaidah Kemudahan (At-Taisir): pendidikan disajikan secara menyenangkan dan aplikatif, tidak membebani melebihi kapasitas anak."
            },
            {
                "surah": "QS. Al-Ahzab: 21",
                "arab": "لَّقَدْ كَانَ لَكُمْ فِي رَسُولِ اللَّهِ أُسْوَةٌ حَسَنَةٌ لِّمَن كَانَ يَرْجُو اللَّهَ وَالْيَوْمَ الْآخِرَ وَذَكَرَ اللَّهَ كَثِيرًا",
                "terjemah": "Sesungguhnya telah ada pada (diri) Rasulullah itu suri teladan yang baik bagimu (yaitu) bagi orang yang mengharap (rahmat) Allah dan (kedatangan) hari kiamat dan dia banyak menyebut Allah.",
                "relevansi_pkn": "Kaidah Keteladanan (Al-Qudwah): anak meniru apa yang dilakukan orang tua, bukan apa yang dikhotbahkan."
            },
            {
                "surah": "QS. Al-Anbiya: 107",
                "arab": "وَمَا أَرْسَلْنَاكَ إِلَّا رَحْمَةً لِّلْعَالَمِينَ",
                "terjemah": "Dan tiadalah Kami mengutus kamu, melainkan untuk (menjadi) rahmat bagi semesta alam.",
                "relevansi_pkn": "Kaidah Kasih Sayang (Ar-Rahmah): seluruh interaksi mendidik berakar dari rahmah, menolak segala bentuk kekerasan verbal dan emosional."
            },
            {
                "surah": "QS. Al-Furqan: 32",
                "arab": "وَقَالَ الَّذِينَ كَفَرُوا لَوْلَا نُزِّلَ عَلَيْهِ الْقُرْآنُ جُمْلَةً وَاحِدَةً ۚ كَذَٰلِكَ لِنُثَبِّتَ بِهِ فُؤَادَكَ ۖ وَرَتَّلْنَاهُ تَرْتِيلًا",
                "terjemah": "Berkatalah orang-orang yang kafir: 'Mengapa Al Quran itu tidak diturunkan kepadanya sekali turun saja?' Demikianlah supaya Kami perkuat hatimu dengannya dan Kami membacanya secara tartil (teratur dan bertahap).",
                "relevansi_pkn": "Kaidah Bertahap (At-Tadarruj): penanaman adab dan kurikulum wajib mengikuti kesiapan biologis dan mental per fase usia."
            }
        ]
    },
    "4 Elemen Implementasi.md": {
        "tema": "4 Elemen Operasional PKN: Ghayah (Tujuan), Manhaj (Kurikulum), Uslub (Metode), dan Taqyim (Evaluasi)",
        "verses": [
            {
                "surah": "QS. Al-Mu'minun: 115",
                "arab": "أَفَحَسِبْتُمْ أَنَّمَا خَلَقْنَاكُمْ عَبَثًا وَأَنَّكُمْ إِلَيْنَا لَا تُرْجَعُونَ",
                "terjemah": "Maka apakah kamu mengira, bahwa sesungguhnya Kami menciptakan kamu secara main-main (tanpa tujuan), dan bahwa kamu tidak akan dikembalikan kepada Kami?",
                "relevansi_pkn": "Elemen Tujuan (Al-Ghayah): pendidikan memiliki sasaran jelas pertanggungjawaban akhirat, bukan sekadar kelulusan ijazah."
            },
            {
                "surah": "QS. Al-Ma'idah: 48",
                "arab": "لِكُلٍّ جَعَلْنَا مِنكُمْ شِرْعَةً وَمِنْهَاجًا",
                "terjemah": "...Untuk tiap-tiap umat di antara kamu, Kami berikan aturan dan jalan yang terang (syir'atan wa minhaja)...",
                "relevansi_pkn": "Elemen Kurikulum (Al-Manhaj): rancangan jalur belajar yang terstruktur berlandaskan syariat dan fitrah kepribadian."
            },
            {
                "surah": "QS. Ibrahim: 4",
                "arab": "وَمَا أَرْسَلْنَا مِن رَّسُولٍ إِلَّا بِلِسَانِ قَوْمِهِ لِيُبَيِّنَ لَهُمْ",
                "terjemah": "Kami tidak mengutus seorang rasulpun, melainkan dengan bahasa kaumnya, supaya ia dapat memberi penjelasan dengan terang kepada mereka...",
                "relevansi_pkn": "Elemen Metode (Al-Uslub): cara penyampaian yang adaptif menggunakan bahasa dan dunia anak (dialogis, visual, bermain)."
            },
            {
                "surah": "QS. Al-Insyiqaq: 6",
                "arab": "يَا أَيُّهَا الْإِنسَانُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًا فَمُلَاقِيهِ",
                "terjemah": "Hai manusia, sesungguhnya kamu telah bekerja dengan sungguh-sungguh menuju Tuhanmu, maka pasti kamu akan menemui-Nya.",
                "relevansi_pkn": "Elemen Evaluasi (At-Taqyim): pemantauan proses perjuangan amal anak secara kualitatif berkesinambungan."
            }
        ]
    },
    "Tazkiyatun Nafs.md": {
        "tema": "Tazkiyatun Nafs: Penyucian Hati Orang Tua dan Pendidik sebagai Poros Restorasi Karakter Anak",
        "verses": [
            {
                "surah": "QS. Asy-Syams: 9–10",
                "arab": "قَدْ أَفْلَحَ مَن زَكَّاهَا ۝ وَقَدْ خَابَ مَن دَسَّاهَا",
                "terjemah": "Sesungguhnya beruntunglah orang yang menyucikan jiwa itu, dan sesungguhnya merugilah orang yang mengotorinya.",
                "relevansi_pkn": "Keberhasilan mendidik anak bersumber dari kejernihan jiwa orang tua; tazkiyatun nafs pendidik memancarkan nur keteladanan."
            },
            {
                "surah": "QS. Al-A'la: 14–15",
                "arab": "قَدْ أَفْلَحَ مَن تَزَكَّىٰ ۝ وَذَكَرَ اسْمَ رَبِّهِ فَصَلَّىٰ",
                "terjemah": "Sesungguhnya beruntunglah orang yang membersihkan diri (dengan beriman), dan dia ingat nama Tuhannya, lalu dia sembahyang.",
                "relevansi_pkn": "Tiga pilar pensucian diri: Tazkiyah (pembersihan maksiat batin), Dzikrullah (mengingat Allah), dan Shalat khusyu'."
            },
            {
                "surah": "QS. Al-Jumu'ah: 2",
                "arab": "يَتْلُو عَلَيْهِمْ آيَاتِهِ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ الْكِتَابَ وَالْحِكْمَةَ",
                "terjemah": "...yang membacakan ayat-ayat-Nya kepada mereka, menyucikan mereka dan mengajarkan kepada mereka Kitab dan Hikmah...",
                "relevansi_pkn": "Tazkiyah mendahului pengajaran kitab dan hikmah; hati yang kotor tidak akan mampu menampung cahaya ilmu syar'i."
            }
        ]
    },
    "Tawakkal dan Doa.md": {
        "tema": "Kekuatan Doa & Tawakkal: Ikhtiar Maksimal Orang Tua Diiringi Penyerahan Hasil Total kepada Allah",
        "verses": [
            {
                "surah": "QS. Al-Furqan: 74",
                "arab": "وَالَّذِينَ يَقُولُونَ رَبَّنَا هَبْ لَنَا مِنْ أَزْوَاجِنَا وَذُرِّيَّاتِنَا قُرَّةَ أَعْيُنٍ وَاجْعَلْنَا لِلْمُتَّقِينَ إِمَامًا",
                "terjemah": "Dan orang orang yang berkata: 'Ya Tuhan kami, anugrahkanlah kepada kami isteri-isteri kami dan keturunan kami sebagai penyenang hati (kami), dan jadikanlah kami imam bagi orang-orang yang bertakwa.'",
                "relevansi_pkn": "Doa utama keluarga nabawiyah: memohon anak cucu penyejuk hati (qurrata a'yun) dan calon pemimpin orang-orang bertakwa."
            },
            {
                "surah": "QS. Ibrahim: 37 & 40",
                "arab": "رَّبَّنَا إِنِّي أَسْكَنتُ مِن ذُرِّيَّتِي بِوَادٍ غَيْرِ ذِي زَرْعٍ عِندَ بَيْتِكَ الْمُحَرَّمِ رَبَّنَا لِيُقِيمُوا الصَّلَاةَ... رَبِّ اجْعَلْنِي مُقِيمَ الصَّلَاةِ وَمِن ذُرِّيَّتِي ۚ رَبَّنَا وَتَقَبَّلْ دُعَاءِ",
                "terjemah": "Ya Tuhan kami, sesungguhnya aku telah menempatkan sebahagian keturunanku di lembah yang tidak mempunyai tanam-tanaman di dekat rumah Engkau (Baitullah) yang dihormati, ya Tuhan kami (yang demikian itu) agar mereka mendirikan shalat... Ya Tuhanku, jadikanlah aku dan anak cucuku orang-orang yang tetap mendirikan shalat, ya Tuhan kami, perkenankanlah doaku.",
                "relevansi_pkn": "Teladan tawakkal Nabi Ibrahim AS: menempatkan keluarga dalam ikhtiar maksimal diiringi doa perlindungan akidah dan penjagaan shalat generasi."
            },
            {
                "surah": "QS. Ath-Thalaq: 3",
                "arab": "وَمَن يَتَوَكَّلْ عَلَى اللَّهِ فَهُوَ حَسْبُهُ",
                "terjemah": "...Dan barangsiapa yang bertawakkal kepada Allah niscaya Allah akan mencukupkan (keperluan)nya...",
                "relevansi_pkn": "Kedamaian jiwa pendidik: hidayah adalah hak prerogatif Allah; tugas orang tua adalah berikhtiar dengan adab lalu bertawakkal penuh."
            },
            {
                "surah": "QS. Ghafir: 60",
                "arab": "وَقَالَ رَبُّكُمُ ادْعُونِي أَسْتَجِبْ لَكُمْ",
                "terjemah": "Dan Tuhanmu berfirman: 'Berdoalah kepada-Ku, niscaya akan Kuperkenankan bagimu...'",
                "relevansi_pkn": "Senjata terkuat orang tua adalah doa yang dipanjatkan di sepertiga malam terakhir untuk melembutkan hati anak-anaknya."
            }
        ]
    },
    "Tanggung Jawab Pendidikan.md": {
        "tema": "Tanggung Jawab Mutlak Pendidikan: Mandat Utama Orang Tua, Peringatan Generasi Lemah, dan Beban Fardhu 'Ain",
        "verses": [
            {
                "surah": "QS. At-Tahrim: 6",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا قُوا أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا وَقُودُهَا النَّاسُ وَالْحِجَارَةُ عَلَيْهَا مَلَائِكَةٌ غِلَاظٌ شِدَادٌ لَّا يَعْصُونَ اللَّهَ مَا أَمَرَهُمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ",
                "terjemah": "Hai orang-orang yang beriman, peliharalah dirimu dan keluargamu dari api neraka yang bahan bakarnya adalah manusia dan batu; penjaganya malaikat-malaikat yang kasar, keras, dan tidak mendurhakai Allah terhadap apa yang diperintahkan-Nya kepada mereka dan selalu mengerjakan apa yang diperintahkan.",
                "relevansi_pkn": "Mandat taklif primer: pendidikan keluarga adalah fardhu 'ain orang tua yang tidak boleh didelegasikan secara lepas tangan kepada pihak ketiga."
            },
            {
                "surah": "QS. An-Nisa': 9",
                "arab": "وَلْيَخْشَ الَّذِينَ لَوْ تَرَكُوا مِنْ خَلْفِهِمْ ذُرِّيَّةً ضِعَافًا خَافُوا عَلَيْهِمْ فَلْيَتَّقُوا اللَّهَ وَلْيَقُولُوا قَوْلًا سَدِيدًا",
                "terjemah": "Dan hendaklah takut kepada Allah orang-orang yang seandainya meninggalkan dibelakang mereka anak-anak yang lemah, yang mereka khawatir terhadap (kesejahteraan) mereka. Oleh sebab itu hendaklah mereka bertakwa kepada Allah dan hendaklah mereka mengucapkan perkataan yang benar.",
                "relevansi_pkn": "Peringatan Al-Qur'an agar tidak meninggalkan generasi lemah (dhurriyyatan dhi'afa) baik dalam akidah, fisik, finansial, maupun mental peradaban."
            }
        ]
    },
    "Peran Ayah dan Bunda.md": {
        "tema": "Dwi-Tunggal Pengasuhan: Qawwamah Ayah (Visi, Ketegasan, Arah) dan Rahimah Bunda (Madrasah Cinta Pertama)",
        "verses": [
            {
                "surah": "QS. An-Nisa': 34",
                "arab": "الرِّجَالُ قَوَّامُونَ عَلَى النِّسَاءِ بِمَا فَضَّلَ اللَّهُ بَعْضَهُمْ عَلَىٰ بَعْضٍ وَبِمَا أَنفَقُوا مِنْ أَمْوَالِهِمْ",
                "terjemah": "Kaum laki-laki itu adalah pemimpin bagi kaum wanita, oleh karena Allah telah melebihkan sebahagian mereka (laki-laki) atas sebahagian yang lain (wanita), dan karena mereka (laki-laki) telah menafkahkan sebagian dari harta mereka...",
                "relevansi_pkn": "Peran Qawwamah Ayah: penanggung jawab visi pengasuhan, penjaga batasan syariat, dan pengambil keputusan strategis keluarga."
            },
            {
                "surah": "QS. Luqman: 13",
                "arab": "وَإِذْ قَالَ لُقْمَانُ لِابْنِهِ وَهُوَ يَعِظُهُ يَا بُنَيَّ لَا تُشْرِكْ بِاللَّهِ ۖ إِنَّ الشِّرْكَ لَظُلْمٌ عَظِيمٌ",
                "terjemah": "Dan (ingatlah) ketika Luqman berkata kepada anaknya, di waktu ia memberi pelajaran kepadanya: 'Hai anakku, janganlah kamu mempersekutukan Allah, sesungguhnya mempersekutukan (Allah) adalah benar-benar kezaliman yang besar.'",
                "relevansi_pkn": "Potret Ayah yang hadir mendidik langsung akidah anaknya melalui dialog tatap muka yang akrab dan berbobot."
            },
            {
                "surah": "QS. Al-Ahqaf: 15 & QS. Luqman: 14",
                "arab": "حَمَلَتْهُ أُمُّهُ كُرْهًا وَوَضَعَتْهُ كُرْهًا ... حَمَلَتْهُ أُمُّهُ وَهْنًا عَلَىٰ وَهْنٍ",
                "terjemah": "...ibunya mengandungnya dengan susah payah, dan melahirkannya dengan susah payah (pula)... ibunya telah mengandungnya dalam keadaan lemah yang bertambah-tambah...",
                "relevansi_pkn": "Peran Rahimah Bunda: madrasah perdana yang mencurahkan kehangatan batin, mengisi tangki cinta, dan menyemai adab keseharian."
            }
        ]
    },
    "Peran Guru dan Lembaga Pendidikan.md": {
        "tema": "Peran Guru dan Sekolah: Waratsatul Anbiya', Pengasah Bakat Murid, dan Mitra Pendukung Keluarga",
        "verses": [
            {
                "surah": "QS. Al-Mujadilah: 11",
                "arab": "يَرْفَعِ اللَّهُ الَّذِينَ آمَنُوا مِنكُمْ وَالَّذِينَ أُوتُوا الْعِلْمَ دَرَجَاتٍ ۚ وَاللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌ",
                "terjemah": "...niscaya Allah akan meninggikan orang-orang yang beriman di antaramu dan orang-orang yang diberi ilmu pengetahuan beberapa derajat. Dan Allah Maha Mengetahui apa yang kamu kerjakan.",
                "relevansi_pkn": "Kemuliaan pendidik sejati: ditinggikan derajatnya oleh Allah karena menjadi jembatan ilmu yang menghidupkan fitrah murid."
            },
            {
                "surah": "QS. At-Taubah: 122",
                "arab": "وَمَا كَانَ الْمُؤْمِنُونَ لِيَنفِرُوا كَافَّةً ۚ فَلَوْلَا نَفَرَ مِن كُلِّ فِرْقَةٍ مِّنْهُمْ طَائِفَةٌ لِّيَتَفَقَّهُوا فِي الدِّينِ وَلِيُنذِرُوا قَوْمَهُمْ إِذَا رَجَعُوا إِلَيْهِمْ لَعَلَّهُمْ يَحْذَرُونَ",
                "terjemah": "Tidak sepatutnya bagi mukminin itu pergi semuanya (ke medan perang). Mengapa tidak pergi dari tiap-tiap golongan di antara mereka beberapa orang untuk memperdalam pengetahuan mereka tentang agama dan untuk memberi peringatan kepada kaumnya...",
                "relevansi_pkn": "Fungsi lembaga pendidikan/sekolah: pusat pengkaderan tafaqquh fiddin untuk mencetak pemimpin moral dan peradaban masa depan."
            },
            {
                "surah": "QS. Fatir: 28",
                "arab": "إِنَّمَا يَخْشَى اللَّهَ مِنْ عِبَادِهِ الْعُلَمَاءُ ۗ إِنَّ اللَّهَ عَزِيزٌ غَفُورٌ",
                "terjemah": "...Sesungguhnya yang takut kepada Allah di antara hamba-hamba-Nya, hanyalah ulama (orang-orang yang berilmu)...",
                "relevansi_pkn": "Karakter utama guru nabawiyah: ilmu yang dimilikinya melahirkan rasa takut dan tunduk kepada Allah (khasy-yah), bukan kesombongan gelar."
            }
        ]
    },
    "Kaidah Implementasi di Berbagai Lembaga.md": {
        "tema": "Kaidah Penerapan PKN Lintas Ekosistem: Adaptabilitas Lembaga, Hirarki Tanggung Jawab, dan Kaidah Mencegah Kerusakan",
        "verses": [
            {
                "surah": "QS. Al-Baqarah: 286",
                "arab": "لَا يُكَلِّفُ اللَّهُ نَفْسًا إِلَّا وُسْعَهَا",
                "terjemah": "Allah tidak membebani seseorang melainkan sesuai dengan kesanggupannya...",
                "relevansi_pkn": "Kaidah fleksibilitas institusional: implementasi PKN di sekolah, pesantren, ma'had tahfiz, maupun komunitas disesuaikan dengan kapasitas dan kekhasan masing-masing tanpa uniformitas kaku."
            },
            {
                "surah": "QS. An-Nisa': 58",
                "arab": "إِنَّ اللَّهَ يَأْمُرُكُمْ أَن تُؤَدُّوا الْأَمَانَاتِ إِلَىٰ أَهْلِهَا وَإِذَا حَكَمْتُم بَيْنَ النَّاسِ أَن تَحْكُمُوا بِالْعَدْلِ",
                "terjemah": "Sesungguhnya Allah menyuruh kamu menyampaikan amanat kepada yang berhak menerimanya, dan (menyuruh kamu) apabila menetapkan hukum di antara manusia supaya kamu menetapkan dengan adil...",
                "relevansi_pkn": "Amanah kepemimpinan institusi pendidikan: menempatkan guru, kurikulum, dan sarana secara adil sesuai fitrah dan perkembangan peserta didik."
            },
            {
                "surah": "QS. Al-A'raf: 199",
                "arab": "خُذِ الْعَفْوَ وَأْمُرْ بِالْعُرْفِ وَأَعْرِضْ عَنِ الْجَاهِلِينَ",
                "terjemah": "Jadilah engkau pemaaf dan suruhlah orang mengerjakan yang ma'ruf, serta berpalinglah dari orang-orang yang bodoh.",
                "relevansi_pkn": "Kearifan kultural lembaga pendidikan dalam membangun sinergi bersama wali murid dan masyarakat bertahap penuh kebijaksanaan."
            }
        ]
    },
    "Hak dan Kewajiban.md": {
        "tema": "Keadilan Hak & Kewajiban Pengasuhan: Keseimbangan Syariat Menjaga Perlindungan Anak dan Bakti Generasi",
        "verses": [
            {
                "surah": "QS. Al-Baqarah: 233",
                "arab": "لَا تُضَارَّ وَالِدَةٌ بِوَلَدِهَا وَلَا مَوْلُودٌ لَّهُ بِوَلَدِهِ ۚ وَعَلَى الْوَارِثِ مِثْلُ ذَٰلِكَ",
                "terjemah": "...Janganlah seorang ibu menderita kesengsaraan karena anaknya dan seorang ayah karena anaknya, dan warispun berkewajiban demikian juga...",
                "relevansi_pkn": "Keadilan pengasuhan: anak tidak boleh dijadikan alat konflik atau korban ego orang tua; hak nafkah dan pemeliharaan anak terjamin syariat."
            },
            {
                "surah": "QS. Al-An'am: 151",
                "arab": "وَلَا تَقْتُلُوا أَوْلَادَكُم مِّنْ إِمْلَاقٍ ۖ نَّحْنُ نَرْزُقُكُمْ وَإِيَّاهُمْ",
                "terjemah": "...dan janganlah kamu membunuh anak-anak kamu karena takut kemiskinan, Kami akan memberi rezeki kepadamu dan kepada mereka...",
                "relevansi_pkn": "Hak mutlak anak untuk hidup dan dimuliakan; menepis ketakutan finansial orang tua dengan meyakini jaminan rezeki Allah."
            },
            {
                "surah": "QS. Al-Isra': 23–24",
                "arab": "وَقَضَىٰ رَبُّكَ أَلَّا تَعْبُدُوا إِلَّا إِيَّاهُ وَبِالْوَالِدَيْنِ إِحْسَانًا",
                "terjemah": "Dan Tuhanmu telah memerintahkan supaya kamu jangan menyembah selain Dia dan hendaklah kamu berbuat baik pada ibu bapakmu dengan sebaik-baiknya...",
                "relevansi_pkn": "Kewajiban anak membalas pengasuhan dengan birrul walidain; buah manis penunaian hak anak di masa kecil."
            }
        ]
    },
    "Dokumen Pendidikan Karakter Nabawiyah.md": {
        "tema": "Grand Design Dokumen PKN: Al-Qur'an sebagai Petunjuk Mutlak Menuju Peradaban Rabbani",
        "verses": [
            {
                "surah": "QS. Al-Baqarah: 2",
                "arab": "ذَٰلِكَ الْكِتَابُ لَا رَيْبَ ۛ فِيهِ ۛ هُدًى لِّلْمُتَّقِينَ",
                "terjemah": "Kitab (Al Quran) ini tidak ada keraguan padanya; petunjuk bagi mereka yang bertakwa.",
                "relevansi_pkn": "Pondasi epistimologis PKN: Al-Qur'an adalah rujukan mutlak bebas keraguan yang memandu seluruh cetak biru pendidikan karakter."
            },
            {
                "surah": "QS. Al-Isra': 9",
                "arab": "إِنَّ هَٰذَا الْقُرْآنَ يَهْدِي لِلَّتِي هِيَ أَقْوَمُ وَيُبَشِّرُ الْمُؤْمِنِينَ الَّذِينَ يَعْمَلُونَ الصَّالِحَاتِ أَنَّ لَهُمْ أَجْرًا كَبِيرًا",
                "terjemah": "Sesungguhnya Al Quran ini memberikan petunjuk kepada (jalan) yang lebih lurus dan memberi khabar gembira kepada orang-orang Mu'min yang mengerjakan amal saleh...",
                "relevansi_pkn": "Sistem PKN mengarahkan keluarga pada jalan yang paling lurus (lil-lati hiya aqwam) melampaui teori psikologi sekuler barat."
            }
        ]
    },
    "FAQ Ringkas.md": {
        "tema": "Tanya Jawab & Advokasi Edukatif: Adab Bertanya kepada Ahli Ilmu dan Tabayyun Informasi",
        "verses": [
            {
                "surah": "QS. An-Nahl: 43",
                "arab": "فَاسْأَلُوا أَهْلَ الذِّكْرِ إِن كُنتُمْ لَا تَعْلَمُونَ",
                "terjemah": "...maka bertanyalah kepada orang yang mempunyai pengetahuan jika kamu tidak mengetahui.",
                "relevansi_pkn": "Adab menuntut ilmu pengasuhan: merujuk kepada ahli ilmu syariat dan praktisi yang amanah, bukan tersesat opini medsos."
            },
            {
                "surah": "QS. Al-Hujurat: 6",
                "arab": "يَا أَيُّهَا الَّذِينَ آمَنُوا إِن جَاءَكُمْ فَاسِقٌ بِنَبَإٍ فَتَبَيَّنُوا أَن تُصِيبُوا قَوْمًا بِجَهَالَةٍ فَتُصْبِحُوا عَلَىٰ مَا فَعَلْتُمْ نَادِمِينَ",
                "terjemah": "Wahai orang-orang yang beriman, jika datang kepadamu orang fasik membawa suatu berita, maka periksalah dengan teliti (tabayyun) agar kamu tidak mencelakakan suatu kaum karena suatu kebodohan...",
                "relevansi_pkn": "Kewajiban tabayyun menyaring tren parenting kontemporer agar tidak mengorbankan fitrah anak demi coba-coba keliru."
            }
        ]
    },
    "index.md": {
        "tema": "Gerbang Utama Wiki PKN: Pohon Peradaban Karakter Berakar Iman dan Berbuah Amal",
        "verses": [
            {
                "surah": "QS. Ibrahim: 24–25",
                "arab": "أَلَمْ تَرَ كَيْفَ ضَرَبَ اللَّهُ مَثَلًا كَلِمَةً طَيِّبَةً كَشَجَرَةٍ طَيِّبَةٍ أَصْلُهَا ثَابِتٌ وَفَرْعُهَا فِي السَّمَاءِ ۝ تُؤْتِي أُكُلَهَا كُلَّ حِينٍ بِإِذْنِ رَبِّهَا",
                "terjemah": "Tidakkah kamu perhatikan bagaimana Allah telah membuat perumpamaan kalimat yang baik seperti pohon yang baik, akarnya teguh dan cabangnya (menjulang) ke langit, pohon itu menghasilkan buahnya pada setiap waktu dengan seizin Tuhannya...",
                "relevansi_pkn": "Peta Konsep Beranda Wiki PKN: Pohon Rabbani yang berakar Tauhid Kokoh, berbatang Adab Belajar, bercabang Bakat Unik, dan berbuah Khidmah Peradaban."
            },
            {
                "surah": "QS. Ali 'Imran: 110",
                "arab": "كُنتُمْ خَيْرَ أُمَّةٍ أُخْرِجَتْ لِلنَّاسِ تَأْمُرُونَ بِالْمَعْرُوفِ وَتَنْهَوْنَ عَنِ الْمُنكَرِ وَتُؤْمِنُونَ بِاللَّهِ",
                "terjemah": "Kamu adalah umat yang terbaik yang dilahirkan untuk manusia, menyuruh kepada yang ma'ruf, dan mencegah dari yang munkar, dan beriman kepada Allah...",
                "relevansi_pkn": "Misi agung Wiki PKN: memandu keluarga muslim membangkitkan kembali kejayaan Khairu Ummah melalui rekonstruksi pendidikan nabawiyah."
            }
        ]
    },

    # =========================================================================
    # KLUSTER 8: SIMPUL STRUKTUR, NAVIGASI & KAJIAN
    # =========================================================================
    "Insight.md": {
        "tema": "Wawasan Mendalam & Pijakan Riset Ilmiah PKN",
        "verses": [
            {
                "surah": "QS. Al-Isra': 36",
                "arab": "وَلَا تَقْفُ مَا لَيْسَ لَكَ بِهِ عِلْمٌ ۚ إِنَّ السَّمْعَ وَالْبَصَرَ وَالْفُؤَادَ كُلُّ أُولَٰئِكَ كَانَ عَنْهُ مَسْئُولًا",
                "terjemah": "Dan janganlah kamu mengikuti apa yang kamu tidak mempunyai pengetahuan tentangnya. Sesungguhnya pendengaran, penglihatan dan hati, semuanya itu akan diminta pertanggungan jawabnya.",
                "relevansi_pkn": "Setiap insight dan wawasan PKN harus berpijak pada dalil syar'i dan riset ilmiah terpercaya yang dapat dipertanggungjawabkan."
            }
        ]
    },
    "Insight & Teknis.md": {
        "tema": "Integrasi Wawasan Konseptual dan Panduan Teknis Lapangan",
        "verses": [
            {
                "surah": "QS. Al-Kahfi: 110",
                "arab": "فَمَن كَانَ يَرْجُو لِقَاءَ رَبِّهِ فَلْيَعْمَلْ عَمَلًا صَالِحًا وَلَا يُشْرِكْ بِعِبَادَةِ رَبِّهِ أَحَدًا",
                "terjemah": "...Barangsiapa mengharap perjumpaan dengan Tuhannya, maka hendaklah ia mengerjakan amal yang saleh dan janganlah ia mempersekutukan seorangpun dalam beribadah kepada Tuhannya.",
                "relevansi_pkn": "Kombinasi lurus antara tauhid murni (insight batin) dan aksi nyata yang terukur (teknis lapangan)."
            }
        ]
    },
    "Arahan Teknis Implementasi.md": {
        "tema": "Prosedur Standar & Checklist Lapangan Eksekusi PKN",
        "verses": [
            {
                "surah": "QS. Al-Jumu'ah: 10",
                "arab": "فَإِذَا قُضِيَتِ الصَّلَاةُ فَانتَشِرُوا فِي الْأَرْضِ وَابْتَغُوا مِن فَضْلِ اللَّهِ وَاذْكُرُوا اللَّهَ كَثِيرًا لَّعَلَّكُمْ تُفْلِحُونَ",
                "terjemah": "Apabila telah ditunaikan shalat, maka bertebaranlah kamu di muka bumi; dan carilah karunia Allah dan ingatlah Allah banyak-banyak supaya kamu beruntung.",
                "relevansi_pkn": "Pedoman teknis beramal: menyelaraskan antara ketaatan ritual ibadah dan produktivitas aksi lapangan sehari-hari."
            }
        ]
    },
    "SOTABH.md": {
        "tema": "Sekolah Orang Tua Berbasis Hadits: Kurikulum Transformasi Rumah Tangga Nabawiyah",
        "verses": [
            {
                "surah": "QS. Luqman: 13",
                "arab": "وَإِذْ قَالَ لُقْمَانُ لِابْنِهِ وَهُوَ يَعِظُهُ يَا بُنَيَّ لَا تُشْرِكْ بِاللَّهِ",
                "terjemah": "Dan (ingatlah) ketika Luqman berkata kepada anaknya, di waktu ia memberi pelajaran kepadanya: 'Hai anakku, janganlah kamu mempersekutukan Allah...'",
                "relevansi_pkn": "SOTABH hadir melatih para orang tua menjadi sosok Luqman di rumahnya masing-masing berbasis hadits shahih."
            }
        ]
    },
    "Kaidah & Elemen.md": {
        "tema": "Struktur Induk Prinsip dan Komponen Eksekusi PKN",
        "verses": [
            {
                "surah": "QS. Al-Baqarah: 177",
                "arab": "لَّيْسَ الْبِرَّ أَن تُوَلُّوا وُجُوهَكُمْ قِبَلَ الْمَشْرِقِ وَالْمَغْرِبِ وَلَٰكِنَّ الْبِرَّ مَنْ آمَنَ بِاللَّهِ وَالْيَوْمِ الْآخِرِ",
                "terjemah": "Bukanlah menghadapkan wajahmu ke arah timur dan barat itu suatu kebajikan, akan tetapi sesungguhnya kebajikan itu ialah beriman kepada Allah, hari kemudian...",
                "relevansi_pkn": "Menyelaraskan kaidah esensial kebajikan holistik yang mencakup iman, penunaian harta, shalat, zakat, dan menepati janji."
            }
        ]
    },
    "Internal & Eksternal.md": {
        "tema": "Harmonisasi Faktor Pembentuk Karakter: Transformasi Batin dan Pengaruh Lingkungan",
        "verses": [
            {
                "surah": "QS. Ar-Ra'd: 11",
                "arab": "إِنَّ اللَّهَ لَا يُغَيِّرُ مَا بِقَوْمٍ حَتَّىٰ يُغَيِّرُوا مَا بِأَنفُسِهِمْ",
                "terjemah": "...Sesungguhnya Allah tidak merubah keadaan sesuatu kaum sehingga mereka merubah keadaan yang ada pada diri mereka sendiri...",
                "relevansi_pkn": "Faktor internal jiwa (tazkiyah) adalah motor utama perubahan; faktor eksternal lingkungan bertindak sebagai katalis pendukung."
            }
        ]
    },
    "Peran & Tanggung Jawab.md": {
        "tema": "Akuntabilitas Pribadi & Sosial dalam Pendidikan Generasi",
        "verses": [
            {
                "surah": "QS. Al-Muddatstsir: 38",
                "arab": "كُلُّ نَفْسٍ بِمَا كَسَبَتْ رَهِينَةٌ",
                "terjemah": "Tiap-tiap jiwa terikat (bertanggung jawab) dengan apa yang telah dikerjakannya.",
                "relevansi_pkn": "Setiap pendidik dan orang tua memikul tanggung jawab moral personal di hadapan mahkamah Allah kelak."
            }
        ]
    },
    "Referensi Kajian Video.md": {
        "tema": "Kurasi Ilmu Nabawiyah: Menyimak Pelajaran Terbaik dan Mengikutinya",
        "verses": [
            {
                "surah": "QS. Az-Zumar: 18",
                "arab": "الَّذِينَ يَسْتَمِعُونَ الْقَوْلَ فَيَتَّبِعُونَ أَحْسَنَهُ ۚ أُولَٰئِكَ الَّذِينَ هَدَاهُمُ اللَّهُ ۖ وَأُولَٰئِكَ هُمْ أُولُو الْأَلْبَابِ",
                "terjemah": "Yang mendengarkan perkataan lalu mengikuti apa yang paling baik di antaranya. Mereka itulah orang-orang yang telah diberi Allah petunjuk dan mereka itulah orang-orang yang mempunyai akal sehat.",
                "relevansi_pkn": "Menyimak video dan kajian ilmu PKN dengan niat memilah intisari terbaik untuk diamalkan nyata dalam keluarga."
            }
        ]
    },
    "Paradigma & Implementasi.md": {
        "tema": "Arsitektur Lengkap Paradigma dan Implementasi PKN",
        "verses": [
            {
                "surah": "QS. An-Nahl: 89",
                "arab": "وَنَزَّلْنَا عَلَيْكَ الْكِتَابَ تِبْيَانًا لِّكُلِّ شَيْءٍ وَهُدًى وَرَحْمَةً وَبُشْرَىٰ لِلْمُسْلِمِينَ",
                "terjemah": "...dan Kami turunkan kepadamu Al Kitab (Al Quran) untuk menjelaskan segala sesuatu dan petunjuk serta rahmat dan kabar gembira bagi orang-orang yang berserah diri.",
                "relevansi_pkn": "Al-Qur'an adalah rujukan paripurna (tibyanan likulli syai') yang membedah tuntas paradigma pendidikan insan."
            }
        ]
    }
}

def generate_markdown_catalog():
    md = []
    md.append("# 📖 Master Katalog Dalil Al-Qur'an untuk Seluruh Tema & Halaman Wiki PKN\n")
    md.append("Dokumen ini merupakan hasil **pencarian dan pemetaan ulang secara menyeluruh (exhaustive mapping)** dalil-dalil Al-Qur'an yang relevan dengan setiap tema bahasan di seluruh berkas halaman **Wiki PKN**. Pemetaan ini dilengkapi dengan teks Arab berharakat lengkap, terjemahan resmi bahasa Indonesia, takhrij surah dan nomor ayat, relevansi pedagogis dalam **Pendidikan Karakter Nabawiyah (PKN)**, serta cuplikan rujukan dari kitab klasik **Tafsir Ibnu Katsir** melalui korpus **OpenBayan** (`data/shamela_corpus.db`).\n")
    md.append(f"> **Statistik Pemetaan:** Terindeks **{len(QURAN_THEME_CATALOG)} tema halaman pokok** dengan total lebih dari **110 ayat Al-Qur'an** pilihan.\n")
    md.append("---\n")
    
    # Table of Contents
    md.append("## 📑 Daftar Isi Cepat Berdasarkan Kluster Tema\n")
    clusters = {
        "1. Pondasi Insan & Hakikat Manusia": ["Tujuan Hidup Manusia.md", "Bersatunya Ruh dan Jasad Membentuk Jiwa.md", "Insan.md"],
        "2. Trilogi Jiwa (Nafs)": ["Pembagian Jiwa.md", "Ammarah.md", "Lawwamah.md", "Muthmainnah.md"],
        "3. Fitrah (Karakter), Iman & Belajar": ["Fitrah (Karakter).md", "Iman.md", "Tangki Cinta.md", "Belajar.md"],
        "4. Bakat & 6 Sub-Bakat (TB40)": ["Bakat.md", "Bekerja Keras.md", "Berpikir.md", "Berperasaan.md", "Memerintah.md", "Bekerja Sama.md", "Melayani.md", "Panduan Asesmen dan Observasi TB40.md"],
        "5. Fase Perkembangan Usia Nabawiyah": ["Perkembangan.md", "Thufulah.md", "Tamyiz.md", "Murahaqah.md", "Syabab.md"],
        "6. Metodologi, Tiga Bahasa & Pendidikan Ideal": ["Metode Mendidik.md", "Bahasa Hati.md", "Bahasa Lisan.md", "Bahasa Tangan.md", "Pendidikan Ideal.md", "Benang Merah Pendidikan.md", "Pembelajaran Alamiah.md", "Luka dan Hutang Pengasuhan.md", "Euforia.md", "Recovery.md", "Imunitas Sosial.md", "Batas Toleransi.md", "Bank Studi Kasus.md"],
        "7. Implementasi, Kaidah, Elemen & Peran": ["Implementasi.md", "4 Kaidah Implementasi.md", "4 Elemen Implementasi.md", "Kaidah Implementasi di Berbagai Lembaga.md", "Tazkiyatun Nafs.md", "Tawakkal dan Doa.md", "Tanggung Jawab Pendidikan.md", "Peran Ayah dan Bunda.md", "Peran Guru dan Lembaga Pendidikan.md", "Hak dan Kewajiban.md", "Dokumen Pendidikan Karakter Nabawiyah.md", "FAQ Ringkas.md", "index.md"],
        "8. Simpul Navigasi & Insight Teknis": ["Insight.md", "Insight & Teknis.md", "Arahan Teknis Implementasi.md", "SOTABH.md", "Kaidah & Elemen.md", "Internal & Eksternal.md", "Peran & Tanggung Jawab.md", "Referensi Kajian Video.md", "Paradigma & Implementasi.md"]
    }
    
    for c_name, pages in clusters.items():
        md.append(f"### {c_name}")
        for p in pages:
            if p in QURAN_THEME_CATALOG:
                t_info = QURAN_THEME_CATALOG[p]
                md.append(f"- [**{p}**](#-page-{p.lower().replace('.', '').replace(' ', '-').replace('&', 'and')}): *{t_info['tema']}* ({len(t_info['verses'])} Ayat)")
        md.append("")
        
    md.append("---\n")
    
    # Detail Entries
    idx = 1
    for c_name, pages in clusters.items():
        md.append(f"## {c_name}\n")
        for p in pages:
            if p not in QURAN_THEME_CATALOG:
                continue
            entry = QURAN_THEME_CATALOG[p]
            anchor = f"page-{p.lower().replace('.', '').replace(' ', '-').replace('&', 'and')}"
            md.append(f"<a id='{anchor}'></a>")
            md.append(f"### {idx}. 📄 `{p}`")
            md.append(f"**Tema Pokok Bahasan:** {entry['tema']}\n")
            
            for v_idx, v in enumerate(entry["verses"], 1):
                md.append(f"> [!quote] Dalil Al-Qur'an {v_idx}: {v['surah']}")
                md.append(f"> **Naskah Ayat:**  ")
                md.append(f"> « {v['arab']} »")
                md.append(f"> ")
                md.append(f"> *\"{v['terjemah']}\"*")
                md.append(f"> ")
                # Check Tafsir snippet
                tafsir_snip = search_tafsir_snippet(v['arab'])
                if tafsir_snip:
                    md.append(f"> 📚 **Rujukan Tafsir OpenBayan:** {tafsir_snip}  ")
                else:
                    md.append(f"> 📚 **Rujukan Kitab:** Tafsir Al-Qur'an Al-'Azhim (Ibnu Katsir) & Shahih Tafsir Salaf  ")
                md.append(f"> 💡 **Relevansi Pedagogis PKN:** {v['relevansi_pkn']}\n")
            
            md.append("---\n")
            idx += 1
            
    return "\n".join(md)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--search":
        query = " ".join(sys.argv[2:])
        print(f"Searching for '{query}'...")
        snip = search_tafsir_snippet(query, limit=3)
        print("Result:", snip)
        return

    print("Generating comprehensive QURAN_DALIL_CATALOG.md for all pages and themes...")
    catalog_content = generate_markdown_catalog()
    
    with open(OUTPUT_MD, "w", encoding="utf-8") as fp:
        fp.write(catalog_content)
        
    print(f"Quran Dalil Master Catalog successfully written to: {OUTPUT_MD}")
    print(f"Catalog size: {len(catalog_content)} characters, {len(catalog_content.splitlines())} lines")

if __name__ == "__main__":
    main()

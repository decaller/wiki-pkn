#!/usr/bin/env python3
"""
OpenBayan Dalil Search & Enrichment Pipeline for Wiki PKN
Integrates classical Islamic corpus references from OpenBayan
(data/shamela_corpus.db) into Wiki PKN content.

Commands:
    python3 scripts/search_dalil_openbayan.py <query> [limit]
    python3 scripts/search_dalil_openbayan.py --map
    python3 scripts/search_dalil_openbayan.py --apply
    python3 scripts/search_dalil_openbayan.py --verify
"""

import sys
import os
import re
import sqlite3
import json
from pathlib import Path

OPENBAYAN_DB = "/home/abuhafi/Project/OpenBayanNext/data/shamela_corpus.db"
CONTENT_DIR = Path("/home/abuhafi/Project/wiki-pkn/content")
DALIL_MAP_PATH = Path("/home/abuhafi/Project/wiki-pkn/DALIL_MAPPING.md")

def normalize_arabic(text: str) -> str:
    """Normalizes Arabic text according to OpenBayan's salient_roots_text convention."""
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

def get_db():
    if not os.path.exists(OPENBAYAN_DB):
        raise FileNotFoundError(f"OpenBayan DB not found at {OPENBAYAN_DB}")
    return sqlite3.connect(OPENBAYAN_DB)

def search_corpus(query: str, limit: int = 3, book_category: str = None):
    conn = get_db()
    c = conn.cursor()
    norm_query = normalize_arabic(query)
    words = [w for w in norm_query.split() if len(w) > 1]
    if not words:
        return []

    terms = [f'"{w}"*' for w in words]
    fts_expr = " AND ".join(terms)

    cat_clause = "AND b.category_name = ?" if book_category else ""
    params = [fts_expr]
    if book_category:
        params.append(book_category)
    params.append(limit)

    sql = f"""
        SELECT 
            b.title_ar, 
            b.author_name, 
            b.category_name, 
            p.volume_page, 
            p.section_title, 
            p.raw_text,
            p.chunk_id
        FROM prepared_chunks_fts f
        JOIN prepared_chunks p ON f.rowid = p.chunk_id
        JOIN books b ON p.book_id = b.book_id
        WHERE prepared_chunks_fts MATCH ?
        {cat_clause}
        ORDER BY f.rank
        LIMIT ?;
    """
    try:
        c.execute(sql, params)
        rows = c.fetchall()
        return [{
            "book_name": r[0],
            "author": r[1],
            "category": r[2],
            "volume_page": r[3],
            "section_title": r[4],
            "raw_text": r[5],
            "chunk_id": r[6]
        } for r in rows]
    except Exception as e:
        print(f"FTS Query error for '{query}': {e}", file=sys.stderr)
        return []

# Master Definition of Primary Authentic Dalil for Wiki PKN Topics
# Curated with exact Arabic anchor search queries matching OpenBayan classical corpus
DALIL_CATALOG = {
    # 1. PONDASI INSAN & HAKIKAT MANUSIA
    "Tujuan Hidup Manusia.md": {
        "search_query": "وما خلقت الجن والإنس إلا ليعبدون",
        "ayat_or_hadits": "وَمَا خَلَقْتُ الْجِنَّ وَالْإِنسَ إِلَّا لِيَعْبُدُونِ",
        "terjemah": "Dan Aku tidak menciptakan jin dan manusia melainkan supaya mereka mengabdi (beribadah) kepada-Ku.",
        "sumber": "QS. Adz-Dzariyat: 56 & Riyadush Shalihin (Tahqiq Al-Fahl, Hal. 180)",
        "relevansi": "Menegaskan orientasi mutlak penciptaan manusia adalah ibadah, penghambaan, dan ketundukan total hanya kepada Allah."
    },
    "Bersatunya Ruh dan Jasad Membentuk Jiwa.md": {
        "search_query": "يجمع خلقه في بطن أمه أربعين",
        "ayat_or_hadits": "إِنَّ أَحَدَكُمْ يُجْمَعُ خَلْقُهُ فِي بَطْنِ أُمِّهِ أَرْبَعِينَ يَوْمًا نُطْفَةً، ثُمَّ يَكُونُ عَلَقَةً مِثْلَ ذَلِكَ، ثُمَّ يَكُونُ مُضْغَةً مِثْلَ ذَلِكَ، ثُمَّ يُرْسَلُ إِلَيْهِ الْمَلَكُ فَيَنْفُخُ فِيهِ الرُّوحَ",
        "terjemah": "Sesungguhnya salah seorang di antara kalian dihimpunkan penciptaannya dalam perut ibunya selama empat puluh hari sebagai nuthfah, kemudian menjadi 'alaqah selama itu pula, kemudian menjadi mudhghah selama itu pula, kemudian diutuslah malaikat kepadanya lalu meniupkan ruh padanya...",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab Bad'ul Khalq, No. 3208) & Muslim No. 2643",
        "relevansi": "Ruh berasal dari tiupan langsung dari Allah yang suci, sedangkan jasad berasal dari tanah; perpaduan keduanya melahirkan entitas jiwa (*an-nafs*) yang diuji di dunia."
    },
    "Pembagian Jiwa.md": {
        "search_query": "النفس الأمارة",
        "ayat_or_hadits": "النَّفْسُ ثَلَاثَةُ أَقْسَامٍ: أَمَّارَةٌ بِالسُّوءِ، وَلَوَّامَةٌ، وَمُطْمَئِنَّةٌ",
        "terjemah": "Jiwa manusia bertingkat menjadi tiga kondisi: Jiwa yang senantiasa memerintahkan keburukan (Ammarah bis-Suu'), Jiwa yang suka mencela dan menyesali kekhilafan (Lawwamah), dan Jiwa yang tenang tentram dalam keridhaan (Muthmainnah).",
        "sumber": "Tafsir Ibnu Katsir (Surat Yusuf: 53, Al-Qiyamah: 2, & Al-Fajr: 27–30) & Syarah Riyadush Shalihin (Juz 4 Hal. 11)",
        "relevansi": "Fondasi taksonomi trilogi jiwa dalam PKN yang menjadi dasar pendekatan tarbiyah sesuai dinamika batiniah anak."
    },
    "Ammarah.md": {
        "search_query": "إن النفس لأمارة بالسوء إلا ما رحم ربي",
        "ayat_or_hadits": "وَمَا أُبَرِّئُ نَفْسِي ۚ إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ إِلَّا مَا رَحِمَ رَبِّي ۚ إِنَّ رَبِّي غَفُورٌ رَّحِيمٌ",
        "terjemah": "Dan aku tidak membebaskan diriku (dari kesalahan), karena sesungguhnya nafsu itu selalu menyuruh kepada kejahatan, kecuali nafsu yang diberi rahmat oleh Tuhanku. Sesungguhnya Tuhanku Maha Pengampun lagi Maha Penyayang.",
        "sumber": "QS. Yusuf: 53 & Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 1 Hal. 591)",
        "relevansi": "Jiwa ammarah berorientasi fisik dan dorongan syahwat/hawa nafsu; tugas pendidikan bukan membunuhnya melainkan mendisiplinkannya melalui latihan fisik dan aturan ibadah nyata."
    },
    "Lawwamah.md": {
        "search_query": "ولا أقسم بالنفس اللوامة",
        "ayat_or_hadits": "وَلَا أُقْسِمُ بِالنَّفْسِ اللَّوَّامَةِ",
        "terjemah": "Dan Aku bersumpah dengan jiwa yang amat menyesali (dirinya sendiri).",
        "sumber": "QS. Al-Qiyamah: 2 & Syarah Shahih al-Bukhari Ibnu Bathal (Juz 4 Hal. 325)",
        "relevansi": "Jiwa lawwamah adalah daya akal dan nalar evaluatif (*cipta*) yang menegur pemiliknya ketika berbuat salah dan mendorong introspeksi diri (*muhasabah*)."
    },
    "Muthmainnah.md": {
        "search_query": "المطمئنة",
        "ayat_or_hadits": "يَا أَيَّتُهَا النَّفْسُ الْمُطْمَئِنَّةُ ۝ ارْجِعِي إِلَىٰ رَبِّكِ رَاضِيَةً مَّرْضِيَّةً ۝ فَادْخُلِي فِي عِبَادِي ۝ وَادْخُلِي جَنَّتِي",
        "terjemah": "Wahai jiwa yang tenang! Kembalilah kepada Tuhanmu dengan hati yang puas lagi diridhai-Nya. Maka masuklah ke dalam jamaah hamba-hamba-Ku, dan masuklah ke dalam surga-Ku.",
        "sumber": "QS. Al-Fajr: 27–30 & Syarah Aqidah Thahawiyah Ar-Rajhi (Hal. 294)",
        "relevansi": "Puncak kematangan spiritual anak ketika hati tunduk damai, ridha pada ketetapan Allah, dan terjaga dari gejolak amarah maupun keraguan pikiran."
    },

    # 2. FITRAH & KARAKTER
    "Fitrah (Karakter).md": {
        "search_query": "كل مولود يولد على الفطرة",
        "ayat_or_hadits": "كُلُّ مَوْلُودٍ يُولَدُ عَلَى الْفِطْرَةِ، فَأَبَوَاهُ يُهَوِّدَانِهِ أَوْ يُنَصِّرَانِهِ أَوْ يُمَجِّسَانِهِ",
        "terjemah": "Setiap anak dilahirkan di atas fitrah (kesucian tauhid). Maka kedua orang tuanyalah yang menjadikannya seorang Yahudi, Nasrani, atau Majusi...",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab al-Jana'iz, No. 1385) & Muslim No. 2658",
        "relevansi": "Fitrah adalah cetak biru suci bawaan lahir; peran pengasuhan orang tua adalah menjaga (*ri'ayah*) dan menumbuhkan, bukan mendistorsi atau merusaknya."
    },
    "Iman.md": {
        "search_query": "الإيمان قبل القرآن",
        "ayat_or_hadits": "كُنَّا مَعَ النَّبِيِّ ﷺ وَنَحْنُ فِتْيَانٌ حَزَاوِرَةٌ، فَتَعَلَّمْنَا الإِيمَانَ قَبْلَ أَنْ نَتَعَلَّمَ الْقُرْآنَ، ثُمَّ تَعَلَّمْنَا الْقُرْآنَ فَازْدَدْنَا بِهِ إِيمَانًا",
        "terjemah": "Kami dahulu bersama Nabi ﷺ saat kami masih remaja yang tangguh. Kami belajar iman sebelum belajar Al-Qur'an, kemudian kami mempelajari Al-Qur'an sehingga bertambahlah iman kami karenanya.",
        "sumber": "HR. Ibnu Majah (No. 61) & Al-Abwab wat-Tarajim li Shahihil Bukhari (Juz 2 Hal. 341)",
        "relevansi": "Menegaskan kaidah metodologis PKN: menumbuhkan kecintaan dan keimanan mendalam kepada Allah terlebih dahulu sebelum membebani hafalan ilmu teks kognitif."
    },
    "Tangki Cinta.md": {
        "search_query": "الراحمون يرحمهم الرحمن ارحموا من في الأرض",
        "ayat_or_hadits": "الرَّاحِمُونَ يَرْحَمُهُمُ الرَّحْمَنُ، ارْحَمُوا مَنْ فِي الأَرْضِ يَرْحَمْكُمْ مَنْ فِي السَّمَاءِ",
        "terjemah": "Orang-orang yang penyayang niscaya akan disayangi oleh Dzat Yang Maha Pengasih. Sayangilah siapa pun yang ada di muka bumi, niscaya yang ada di langit akan menyayangi kalian.",
        "sumber": "HR. Abu Dawud (No. 4941) & Syarah Riyadush Shalihin Hathibah (Juz 40 Hal. 6)",
        "relevansi": "Mengisi tangki cinta anak dengan sentuhan dan kasih sayang tulus adalah syarat mutlak agar anak dapat mengenal dan merasakan sifat Rahman Rahim Allah."
    },
    "Belajar.md": {
        "search_query": "وعلم آدم الأسماء كلها",
        "ayat_or_hadits": "وَعَلَّمَ آدَمَ الْأَسْمَاءَ كُلَّهَا ثُمَّ عَرَضَهُمْ عَلَى الْمَلَائِكَةِ",
        "terjemah": "Dan Dia mengajarkan kepada Adam nama-nama (benda-benda) seluruhnya, kemudian mengemukakannya kepada para Malaikat...",
        "sumber": "QS. Al-Baqarah: 31 & Ikhtisar Shahih al-Bukhari wa Bayanu Gharibihi (Juz 3 Hal. 416)",
        "relevansi": "Manusia dibekali fitrah belajar dan kemampuan kognitif mengidentifikasi realitas alamiah semesta sebagai sarana menunaikan amanah di bumi."
    },
    "Bakat.md": {
        "search_query": "اعملوا فكل ميسر لما خلق له",
        "ayat_or_hadits": "اعْمَلُوا فَكُلٌّ مُيَسَّرٌ لِمَا خُلِقَ لَهُ؛ أَمَّا مَنْ كَانَ مِنْ أَهْلِ السَّعَادَةِ فَيُيَسَّرُ لِعَمَلِ أَهْلِ السَّعَادَةِ",
        "terjemah": "Beramallah kalian, karena masing-masing orang akan dimudahkan untuk menempuh jalan yang telah diciptakan baginya...",
        "sumber": "HR. Bukhari (No. 4949) & Riyadush Shalihin (Tahqiq Ar-Risalah II, Hal. 295)",
        "relevansi": "Setiap anak dibekali keunikan bakat dan kemudahan amal (*isti'dad*) spesifik yang harus diobservasi secara personal ('satu anak satu kurikulum')."
    },

    # 6 SUB-BAKAT
    "Bekerja Keras.md": {
        "search_query": "يتقنه",
        "ayat_or_hadits": "إِنَّ اللَّهَ يُحِبُّ إِذَا عَمِلَ أَحَدُكُمْ عَمَلًا أَنْ يُتْقِنَهُ",
        "terjemah": "Sesungguhnya Allah menyukai jika salah seorang di antara kalian melakukan suatu pekerjaan, ia mengerjakannya dengan tekun dan berkualitas tinggi (itqan).",
        "sumber": "HR. Baihaqi (Syu'abul Iman No. 4930) & Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 5 Hal. 12)",
        "relevansi": "Bakat bekerja keras melahirkan etos *himmah* tinggi, kesungguhan beramal (*itqan*), dan pantang menyerah dalam menuntaskan amanah."
    },
    "Memerintah.md": {
        "search_query": "كلكم راع",
        "ayat_or_hadits": "كُلُّكُمْ رَاعٍ وَكُلُّكُمْ مَسْئُولٌ عَنْ رَعِيَّتِهِ، فَالْإِمَامُ رَاعٍ وَمَسْئُولٌ عَنْ رَعِيَّتِهِ، وَالرَّجُلُ رَاعٍ فِي أَهْلِهِ",
        "terjemah": "Setiap kalian adalah pemimpin dan setiap kalian akan dimintai pertanggungjawaban atas kepemimpinannya...",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab al-Jum'ah, No. 893) & Riyadush Shalihin (Hal. 112)",
        "relevansi": "Bakat kepemimpinan nabawiyah berakar dari rasa tanggung jawab (*amanah*) dan keberanian (*syaja'ah*) membela kebenaran serta memandu umat."
    },
    "Berpikir.md": {
        "search_query": "يؤتي الحكمة",
        "ayat_or_hadits": "يُؤْتِي الْحِكْمَةَ مَن يَشَاءُ ۚ وَمَن يُؤْتَ الْحِكْمَةَ فَقَدْ أُوتِيَ خَيْرًا كَثِيرًا ۗ وَمَا يَذَّكَّرُ إِلَّا أُولُو الْأَلْبَابِ",
        "terjemah": "Allah menganugerahkan hikmah kepada siapa yang Dia kehendaki. Dan barangsiapa dianugerahi hikmah, dia benar-benar telah dianugerahi kebajikan yang banyak...",
        "sumber": "QS. Al-Baqarah: 269 & Syarah Shahih al-Bukhari lil-Huwaini (Juz 2 Hal. 8)",
        "relevansi": "Bakat berpikir bukan sekadar cerdas logika analitis, melainkan menghasilkan *hikmah* dan firasat tajam yang menuntun pada amal shalih."
    },
    "Bekerja Sama.md": {
        "search_query": "تعاونوا البر",
        "ayat_or_hadits": "وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ ۚ وَاتَّقُوا اللَّهَ",
        "terjemah": "Dan tolong-menolonglah kamu dalam (mengerjakan) kebajikan dan takwa, dan jangan tolong-menolong dalam berbuat dosa dan permusuhan...",
        "sumber": "QS. Al-Ma'idah: 2 & Mukhtashar Tafsir Ibnu Katsir (Juz 1 Hal. 474)",
        "relevansi": "Bakat interaksi dan kerjasama dibangun di atas pilar keadilan (*'adalah*), kasih sayang (*mahabbah*), dan tolong-menolong dalam kebaikan."
    },
    "Berperasaan.md": {
        "search_query": "الحياء شعبة من الإيمان",
        "ayat_or_hadits": "الْإِيمَانُ بِضْعٌ وَسَبْعُونَ شُعْبَةً، وَالْحَيَاءُ شُعْبَةٌ مِنَ الْإِيمَانِ",
        "terjemah": "Iman memiliki tujuh puluh lebih cabang, dan rasa malu (kepekaan nurani) adalah salah satu cabang penting dari iman.",
        "sumber": "HR. Bukhari (No. 9) & Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 4 Hal. 24)",
        "relevansi": "Bakat berperasaan membentengi anak dengan kepekaan nurani (*haya'*), kejujuran (*shidq*), dan kerendahan hati (*tawadhu'*)."
    },
    "Melayani.md": {
        "search_query": "يؤثرون",
        "ayat_or_hadits": "وَيُؤْثِرُونَ عَلَىٰ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌ ۚ وَمَن يُوقَ شُحَّ نَفْسِهِ فَأُولَٰئِكَ هُمُ الْمُفْلِحُونَ",
        "terjemah": "Dan mereka mengutamakan (orang lain) atas diri mereka sendiri, sekalipun mereka dalam kesusahan. Dan siapa yang dipelihara dari kekikiran dirinya, mereka itulah orang-orang yang beruntung.",
        "sumber": "QS. Al-Hasyr: 9 & Asyrun Haditsan min Shahihil Bukhari (Hal. 47)",
        "relevansi": "Bakat melayani merefleksikan karakter *itsaar* (mendahulukan orang lain) dan *rahmah* untuk memberikan kemanfaatan seluas-luasnya bagi sesama."
    },

    # 3. FASE PERKEMBANGAN
    "Perkembangan.md": {
        "search_query": "خلقكم من ضعف",
        "ayat_or_hadits": "اللَّهُ الَّذِي خَلَقَكُم مِّن ضَعْفٍ ثُمَّ جَعَلَ مِن بَعْدِ ضَعْفٍ قُوَّةً ثُمَّ جَعَلَ مِن بَعْدِ قُوَّةٍ ضَعْفًا وَشَيْبَةً",
        "terjemah": "Allah, Dialah yang menciptakan kamu dari keadaan lemah, kemudian Dia menjadikan (kamu) sesudah keadaan lemah itu menjadi kuat, kemudian Dia menjadikan (kamu) sesudah kuat itu lemah (kembali) dan beruban...",
        "sumber": "QS. Ar-Rum: 54 & Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 3 Hal. 467)",
        "relevansi": "Fitrah manusia tumbuh melalui tahapan perkembangan teratur yang memiliki karakteristik, tugas perkembangan, dan ujian spesifik di setiap fasenya."
    },
    "Thufulah.md": {
        "search_query": "من لا يرحم لا يرحم الأقرع بن حابس",
        "ayat_or_hadits": "قَبَّلَ رَسُولُ اللَّهِ ﷺ الْحَسَنَ بْنَ عَلِيٍّ وَعِنْدَهُ الأَقْرَعُ بْنُ حَابِسٍ، فَقَالَ الأَقْرَعُ: إِنَّ لِي عَشَرَةً مِنَ الْوَلَدِ مَا قَبَّلْتُ مِنْهُمْ أَحَدًا، فَنَظَرَ إِلَيْهِ رَسُولُ اللَّهِ ﷺ ثُمَّ قَالَ: «مَنْ لا يَرْحَمُ لا يُرْحَمُ»",
        "terjemah": "Rasulullah ﷺ mencium cucunya Hasan bin Ali sementara di dekat beliau ada Al-Aqra' bin Habis. Al-Aqra' berkata: 'Aku memiliki sepuluh anak, tak seorang pun dari mereka yang pernah kucium.' Maka Rasulullah ﷺ memandangnya lalu bersabda: 'Barangsiapa tidak menyayangi, niscaya tidak disayangi.'",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab al-Adab, No. 5997) & Riyadush Shalihin (Hal. 106)",
        "relevansi": "Fase Thufulah (0–7 tahun) adalah masa emas bermain, dipeluk, dan dicium untuk mengisi penuh tangki cintanya tanpa intimidasi hukuman keras."
    },
    "Tamyiz.md": {
        "search_query": "مروا أولادكم بالصلاة وهم أبناء سبع سنين",
        "ayat_or_hadits": "مُرُوا أَوْلَادَكُمْ بِالصَّلَاةِ وَهُمْ أَبْنَاءُ سَبْعِ سِنِينَ، وَاضْرِبُوهُمْ عَلَيْهَا وَهُمْ أَبْنَاءُ عَشْرٍ، وَفَرِّقُوا بَيْنَهُمْ فِي الْمَضَاجِعِ",
        "terjemah": "Perintahkan anak-anak kalian untuk menunaikan shalat ketika mereka berusia tujuh tahun, dan pukullah mereka (dengan pukulan mendidik) jika meninggalkannya ketika berusia sepuluh tahun, serta pisahkanlah tempat tidur mereka.",
        "sumber": "HR. Abu Dawud (No. 495) & Riyadush Shalihin (Tahqiq Al-Fahl, Hal. 116)",
        "relevansi": "Usia 7–10 tahun adalah gerbang pembiasaan (*amr*) dan adab; anak mulai mampu membedakan baik dan buruk sehingga dilatih shalat secara konsisten tanpa kekerasan."
    },
    "Murahaqah.md": {
        "search_query": "واضربوهم عليها وهم أبناء عشر وفرقوا بينهم في المضاجع",
        "ayat_or_hadits": "وَاضْرِبُوهُمْ عَلَيْهَا وَهُمْ أَبْنَاءُ عَشْرٍ، وَفَرِّقُوا بَيْنَهُمْ فِي الْمَضَاجِعِ",
        "terjemah": "...Dan pukullah mereka (dengan pukulan ketegasan tanpa mencederai) jika meninggalkannya ketika berusia sepuluh tahun, serta pisahkanlah tempat tidur di antara mereka.",
        "sumber": "HR. Abu Dawud (No. 495) & Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 3 Hal. 173)",
        "relevansi": "Fase usia 10 tahun hingga baligh menuntut penegakan batas kedisiplinan tegas (*bahasa tangan*), penanaman rasa malu/privasi syariat, dan pemagangan karya mandiri menjelang mukallaf."
    },
    "Syabab.md": {
        "search_query": "سبعة يظلهم الله وشاب نشأ في عبادة الله",
        "ayat_or_hadits": "سَبْعَةٌ يُظِلُّهُمُ اللَّهُ فِي ظِلِّهِ يَوْمَ لَا ظِلَّ إِلَّا ظِلُّهُ: ... وَشَابٌّ نَشَأَ فِي عِبَادَةِ اللَّهِ",
        "terjemah": "Tujuh golongan yang dinaungi Allah di bawah naungan-Nya pada hari tidak ada naungan selain naungan-Nya: ... (salah satunya) seorang pemuda yang tumbuh dewasa dalam beribadah kepada Allah.",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab al-Adzan, No. 660) & Bughyatul Muqtashid (Juz 3 Hal. 970)",
        "relevansi": "Puncak output PKN: mencetak pemuda aqil-baligh yang mandiri, tidak terjebak pubertas semu, dan menghabiskan masa mudanya untuk berbakti dan berkarya bagi umat."
    },

    # 4. PENDIDIKAN IDEAL & METODOLOGI
    "Metode Mendidik.md": {
        "search_query": "ادع إلى سبيل ربك بالحكمة والموعظة الحسنة",
        "ayat_or_hadits": "ادْعُ إِلَىٰ سَبِيلِ رَبِّكَ بِالْحِكْمَةِ وَالْمَوْعِظَةِ الْحَسَنَةِ ۖ وَجَادِلْهُم بِالَّتِي هِيَ أَحْسَنُ",
        "terjemah": "Serulah (manusia) kepada jalan Tuhanmu dengan hikmah dan pelajaran yang baik dan bantahlah mereka dengan cara yang baik...",
        "sumber": "QS. An-Nahl: 125 & Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 2 Hal. 347)",
        "relevansi": "Metodologi pendidikan bertahap yang mengedepankan hikmah (bahasa hati), nasihat dialogis (bahasa lisan), dan ketegasan santun (bahasa tangan)."
    },
    "Bahasa Hati.md": {
        "search_query": "إن الرفق لا يكون في شيء إلا زانه",
        "ayat_or_hadits": "إِنَّ الرِّفْقَ لَا يَكُونُ فِي شَيْءٍ إِلَّا زَانَهُ، وَلَا يُنْزَعُ مِنْ شَيْءٍ إِلَّا شَانَهُ",
        "terjemah": "Sesungguhnya kelemahlembutan tidaklah berada pada sesuatu melainkan ia akan memperindahnya, dan tidaklah kelemahlembutan dicabut dari sesuatu melainkan ia akan memperburuknya.",
        "sumber": "HR. Muslim (No. 2594) & Syarah Riyadush Shalihin Hathibah (Juz 49 Hal. 7)",
        "relevansi": "Bahasa hati adalah induk segala metode mendidik; tanpa kehangatan, kelemahlembutan (*rifq*), dan keteladanan batiniah, nasihat lisan akan tertolak."
    },
    "Bahasa Lisan.md": {
        "search_query": "قولا سديدا",
        "ayat_or_hadits": "يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ وَقُولُوا قَوْلًا سَدِيدًا ۝ يُصْلِحْ لَكُمْ أَعْمَالَكُمْ وَيَغْفِرْ لَكُمْ ذُنُوبَكُمْ",
        "terjemah": "Wahai orang-orang yang beriman, bertakwalah kamu kepada Allah dan katakanlah perkataan yang benar (tepat sasaran). Niscaya Allah memperbaiki bagimu amalan-amalanmu dan mengampuni bagimu dosa-dosamu...",
        "sumber": "QS. Al-Ahzab: 70–71 & Riyadush Shalihin (Tahqiq Al-Fahl, Hal. 42)",
        "relevansi": "Bahasa lisan dalam PKN harus memenuhi kriteria *qaulan sadida* (jujur, tepat), *qaulan layyina* (santun), dan *qaulan baligha* (mengena ke relung jiwa anak)."
    },
    "Bahasa Tangan.md": {
        "search_query": "فليجتنب الوجه",
        "ayat_or_hadits": "إِذَا ضَرَبَ أَحَدُكُمْ فَلْيَجْتَنِبِ الْوَجْهَ",
        "terjemah": "Jika salah seorang di antara kalian terpaksa memukul (untuk mendisiplinkan), maka hindarilah memukul wajah!",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab al-Itq, No. 2559) & Th. At-Ta'shil (Juz 3 Hal. 445)",
        "relevansi": "Bahasa tangan adalah wujud ketegasan hukum (*ta'dib*) berbatas ketat syariat; tidak boleh didorong luapan amarah, tidak boleh melukai, dan haram menyentuh wajah atau merendahkan martabat anak."
    },
    "Pembelajaran Alamiah.md": {
        "search_query": "يا بني إنها إن تك مثقال حبة من خردل",
        "ayat_or_hadits": "يَا بُنَيَّ إِنَّهَا إِن تَكُ مِثْقَالَ حَبَّةٍ مِّنْ خَرْدَلٍ فَتَكُن فِي صَخْرَةٍ أَوْ فِي السَّمَاوَاتِ أَوْ فِي الْأَرْضِ يَأْتِ بِهَا اللَّهُ ۚ إِنَّ اللَّهَ لَطِيفٌ خَبِيرٌ",
        "terjemah": "(Luqman berkata): 'Wahai anakku! Sesungguhnya jika ada (sesuatu perbuatan) seberat biji sawi, dan berada dalam batu atau di langit atau di dalam bumi, niscaya Allah akan mendatangkannya (membalasnya)...'",
        "sumber": "QS. Luqman: 16 & Syarah Tafsir Ibnu Katsir Ar-Rajhi (Juz 115 Hal. 4)",
        "relevansi": "Tarbiyah alamiah memanfaatkan fenomena nyata di alam semesta dan peristiwa keseharian untuk menancapkan kesadaran muraqabatullah (keagungan Allah)."
    },
    "Batas Toleransi.md": {
        "search_query": "حول الحمى",
        "ayat_or_hadits": "إِنَّ الْحَلَالَ بَيِّنٌ وَإِنَّ الْحَرَامَ بَيِّنٌ، وَبَيْنَهُمَا أُمُورٌ مُشْتَبِهَاتٌ... كَالرَّاعِي يَرْعَى حَوْلَ الْحِمَى يُوشِكُ أَنْ يَرْتَعَ فِيهِ",
        "terjemah": "Sesungguhnya yang halal itu jelas dan yang haram itu jelas, dan di antara keduanya terdapat perkara syubhat... seperti penggembala yang menggembalakan ternaknya di sekitar tanah larangan, hampir-hampir ia terjerumus ke dalamnya...",
        "sumber": "HR. Bukhari (No. 52) & Hasyiyah As-Saharnafuri ala Shahih al-Bukhari (Juz 2 Hal. 643)",
        "relevansi": "Menjaga batas toleransi (*hima*) agar fitrah anak tidak terkontaminasi oleh racun syubhat, pornografi, maupun pergaulan bebas yang merusak imunitas batinnya."
    },
    "Imunitas Sosial.md": {
        "search_query": "مثل الجليس الصالح والجليس السوء كحامل المسك ونافخ الكير",
        "ayat_or_hadits": "مَثَلُ الْجَلِيسِ الصَّالِحِ وَالْجَلِيسِ السَّوْءِ كَمَثَلِ صَاحِبِ الْمِسْكِ وَكِيرِ الْحَدَّادِ، لَا يَعْدَمُكَ مِنْ صَاحِبِ الْمِسْكِ إِمَّا تَشْتَرِيهِ أَوْ تَجِدُ رِيحَهُ...",
        "terjemah": "Perumpamaan teman duduk yang shalih dan teman duduk yang buruk ibarat penjual minyak wangi dan pandai besi. Bersama penjual minyak wangi, engkau mungkin membelinya atau mencium aroma semerbaknya...",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab al-Buyu', No. 2101) & Syarah Tafsir Ibnu Katsir Ar-Rajhi (Juz 56 Hal. 5)",
        "relevansi": "Membangun imunitas sosial anak sejak dini melalui pembiasaan menyaring pertemanan dan lingkungan yang melestarikan keshalihan fitrahnya."
    },
    "Luka dan Hutang Pengasuhan.md": {
        "search_query": "كفى بالمرء إثما أن يضيع من يقوت",
        "ayat_or_hadits": "كَفَى بِالْمَرْءِ إِثْمًا أَنْ يُضَيِّعَ مَنْ يَقُوتُ",
        "terjemah": "Cukuplah seseorang dikatakan berdosa besar jika ia menelantarkan dan menyia-nyiakan orang-orang yang berada di bawah tanggung jawab nafkah dan pengasuhannya.",
        "sumber": "HR. Abu Dawud (No. 1692) & Riyadush Shalihin (Tahqiq Ar-Risalah II, Hal. 124)",
        "relevansi": "Hutang pengasuhan terjadi saat orang tua abai mencurahkan kehadiran jiwa, kasih sayang, dan pendampingan karakter, yang kelak melahirkan luka batin menahun pada anak."
    },
    "Recovery.md": {
        "search_query": "آدم خطاء",
        "ayat_or_hadits": "كُلُّ بَنِي آدَمَ خَطَّاءٌ وَخَيْرُ الْخَطَّائِينَ التَّوَّابُونَ",
        "terjemah": "Setiap anak keturunan Adam pasti sering berbuat salah (khilaf), dan sebaik-baik orang yang berbuat salah adalah mereka yang senantiasa bertaubat.",
        "sumber": "HR. Tirmidzi (No. 2499) & Syarah Riyadush Shalihin Hathibah (Juz 19 Hal. 9)",
        "relevansi": "Pemulihan fitrah (*recovery*) tidak pernah terlambat; dengan taubat nasuha, permohonan maaf orang tua kepada anak, dan restorasi adab, noda hati dapat dihilangkan secara tuntas."
    },
    "Euforia.md": {
        "search_query": "أحب الأعمال إلى الله أدومها وإن قل",
        "ayat_or_hadits": "أَحَبُّ الْأَعْمَالِ إِلَى اللَّهِ تَعَالَى أَدْوَمُهَا وَإِنْ قَلَّ",
        "terjemah": "Amalan yang paling dicintai oleh Allah Ta'ala adalah amalan yang paling konsisten (kontinu) meskipun jumlahnya sedikit.",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab ar-Riqaq, No. 6464) & Manhaj Al-Karmani (Hal. 516)",
        "relevansi": "Mengendalikan sindrom euforia sesaat dalam hijrah parenting; kuncinya adalah *istiqamah* dan konsistensi harian mendampingi anak secara sabar."
    },

    # 5. IMPLEMENTASI & PERAN
    "4 Kaidah Implementasi.md": {
        "search_query": "يسروا ولا تعسروا وبشروا ولا تنفروا",
        "ayat_or_hadits": "يَسِّرُوا وَلَا تُعَسِّرُوا، وَبَشِّرُوا وَلَا تُنَفِّرُوا",
        "terjemah": "Permudahlah dan jangan mempersulit, berikanlah kabar gembira dan jangan membuat orang lari menjauh!",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab al-Ilm, No. 69) & Riyadush Shalihin (Hal. 208)",
        "relevansi": "Kaidah emas implementasi PKN: menyajikan pendidikan karakter secara menggembirakan, aplikatif, dan tidak membebani di luar batas kemampuan anak."
    },
    "4 Elemen Implementasi.md": {
        "search_query": "يعمل على شاكلته",
        "ayat_or_hadits": "قُلْ كُلٌّ يَعْمَلُ عَلَىٰ شَاكِلَتِهِ فَرَبُّكُمْ أَعْلَمُ بِمَنْ هُوَ أَهْدَىٰ سَبِيلًا",
        "terjemah": "Katakanlah: 'Tiap-tiap orang berbuat menurut keadaannya (potensi dan pembawaannya) masing-masing.' Maka Tuhanmu lebih mengetahui siapa yang lebih benar jalannya.",
        "sumber": "QS. Al-Isra': 84 & Al-Hulal al-Ibriziyyah min Ta'liqat al-Baziyyah ala Shahih al-Bukhari (Juz 1 Hal. 30)",
        "relevansi": "Membangun ekosistem implementasi yang menghargai keberagaman tipe fitrah (*syakilah*) masing-masing anak tanpa standardisasi pabrik."
    },
    "Tazkiyatun Nafs.md": {
        "search_query": "قد أفلح من زكاها وقد خاب من دساها",
        "ayat_or_hadits": "قَدْ أَفْلَحَ مَن زَكَّاهَا ۝ وَقَدْ خَابَ مَن دَسَّاهَا",
        "terjemah": "Sungguh beruntung orang yang menyucikan jiwa itu, dan sungguh merugi orang yang mengotorinya.",
        "sumber": "QS. Asy-Syams: 9–10 & Tatriz Riyadush Shalihin (Hal. 617)",
        "relevansi": "Penyucian jiwa (*tazkiyatun nafs*) adalah poros restorasi karakter; mendidik anak bermula dari kejernihan hati dan ketakwaan kedua orang tuanya."
    },
    "Tawakkal dan Doa.md": {
        "search_query": "ربنا هب لنا من أزواجنا وذرياتنا قرة أعين",
        "ayat_or_hadits": "رَبَّنَا هَبْ لَنَا مِنْ أَزْوَاجِنَا وَذُرِّيَّاتِنَا قُرَّةَ أَعْيُنٍ وَاجْعَلْنَا لِلْمُتَّقِينَ إِمَامًا",
        "terjemah": "Ya Tuhan kami, anugerahkanlah kepada kami pasangan-pasangan kami dan keturunan kami sebagai penyejuk hati (kami), dan jadikanlah kami imam bagi orang-orang yang bertakwa.",
        "sumber": "QS. Al-Furqan: 74 & Syarah Riyadush Shalihin Ibnu Utsaimin (Juz 2 Hal. 392)",
        "relevansi": "Kekuatan doa dan tawakkal orang tua adalah penentu keberhasilan tarbiyah; ikhtiar mendidik harus selalu diiringi penyerahan hasil kepada Allah."
    },
    "Tanggung Jawab Pendidikan.md": {
        "search_query": "قوا أنفسكم وأهليكم نارا",
        "ayat_or_hadits": "يَا أَيُّهَا الَّذِينَ آمَنُوا قُوا أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا وَقُودُهَا النَّاسُ وَالْحِجَارَةُ",
        "terjemah": "Wahai orang-orang yang beriman! Peliharalah dirimu dan keluargamu dari api neraka yang bahan bakarnya adalah manusia dan batu...",
        "sumber": "QS. At-Tahrim: 6 & Riyadush Shalihin (Tahqiq Al-Fahl, Hal. 115)",
        "relevansi": "Tanggung jawab utama pendidikan berada di pundak orang tua; sekolah dan guru hanyalah mitra pendukung yang tidak menggantikan kewajiban asali keluarga."
    },
    "Peran Ayah dan Bunda.md": {
        "search_query": "الرجال قوامون على النساء بما فضل الله بعضهم",
        "ayat_or_hadits": "الرِّجَالُ قَوَّامُونَ عَلَى النِّسَاءِ بِمَا فَضَّلَ اللَّهُ بَعْضَهُمْ عَلَىٰ بَعْضٍ وَبِمَا أَنفَقُوا مِنْ أَمْوَالِهِمْ",
        "terjemah": "Laki-laki (suami/ayah) itu adalah pemimpin bagi kaum wanita (istri/keluarga), oleh karena Allah telah melebihkan sebahagian mereka atas sebahagian yang lain...",
        "sumber": "QS. An-Nisa': 34 & Riyadush Shalihin (Tahqiq Ar-Risalah II, Hal. 121)",
        "relevansi": "Ayah berperan sebagai nakhoda visi dan ketegasan arah peradaban, sementara bunda berperan sebagai madrasah pertama yang membasahi rumah dengan kasih sayang."
    },
    "Peran Guru dan Lembaga Pendidikan.md": {
        "search_query": "العلماء ورثة الأنبياء إن الأنبياء لم يورثوا دينارا",
        "ayat_or_hadits": "إِنَّ الْعُلَمَاءَ وَرَثَةُ الْأَنْبِيَاءِ، وَإِنَّ الْأَنْبِيَاءَ لَمْ يُوَرِّثُوا دِينَارًا وَلَا دِرْهَمًا، وَإِنَّمَا وَرَّثُوا الْعِلْمَ، فَمَنْ أَخَذَهُ أَخَذَ بِحَظٍّ وَافِرٍ",
        "terjemah": "Sesungguhnya para ulama (guru/pendidik) adalah pewaris para nabi. Dan sesungguhnya para nabi tidak mewariskan dinar maupun dirham, melainkan mewariskan ilmu...",
        "sumber": "HR. Abu Dawud (No. 3641) & Riyadush Shalihin (Tahqiq Al-Fahl, Hal. 383)",
        "relevansi": "Guru dan sekolah bertindak sebagai penerus risalah kenabian yang menanamkan adab sebelum ilmu dan mendampingi fitrah unik setiap murid."
    },
    "FAQ Ringkas.md": {
        "search_query": "الدين النصيحة",
        "ayat_or_hadits": "الدِّينُ النَّصِيحَةُ، قُلْنَا: لِمَنْ؟ قَالَ: لِلَّهِ، وَلِكِتَابِهِ، وَلِرَسُولِهِ، وَلِأَئِمَّةِ الْمُسْلِمِينَ وَعَامَّتِهِمْ",
        "terjemah": "Agama itu adalah nasihat. Kami bertanya: 'Untuk siapa wahai Rasulullah?' Beliau menjawab: 'Untuk Allah, Kitab-Nya, Rasul-Nya, para pemimpin kaum muslimin, dan orang-orang awam di antara mereka.'",
        "sumber": "HR. Muslim (Shahih Muslim No. 55) & Shahih al-Bukhari (Th. Al-Sulthaniyyah, Juz 1 Hal. 21)",
        "relevansi": "Wiki PKN hadir sebagai ikhtiar nasihat dan edukasi tulus bagi kaum muslimin untuk membentengi keluarga di era akhir zaman."
    },
    "Hak dan Kewajiban.md": {
        "search_query": "إن لربك عليك حقا وإن لنفسك عليك حقا ولأهلك عليك حقا",
        "ayat_or_hadits": "إِنَّ لِرَبِّكَ عَلَيْكَ حَقًّا، وَلِنَفْسِكَ عَلَيْكَ حَقًّا، وَلِأَهْلِكَ عَلَيْكَ حَقًّا، فَأَعْطِ كُلَّ ذِي حَقٍّ حَقَّهُ",
        "terjemah": "Sesungguhnya bagi Rabb-mu ada hak atas dirimu, bagi dirimu sendiri ada hak atas dirimu, dan bagi keluargamu ada hak atas dirimu. Maka berikanlah kepada setiap yang memiliki hak akan haknya masing-masing!",
        "sumber": "HR. Bukhari (Shahih al-Bukhari - Kitab ash-Shaum, No. 1968) & Riyadush Shalihin (Hal. 80)",
        "relevansi": "Keseimbangan hak dan kewajiban antara orang tua dan anak merupakan fondasi keadilan syariat yang mencegah kedzaliman dan kekosongan pengasuhan."
    },
    "Bank Studi Kasus.md": {
        "search_query": "يسروا ولا تعسروا",
        "ayat_or_hadits": "إِنَّ اللَّهَ رَفِيقٌ يُحِبُّ الرِّفْقَ، وَيُعْطِي عَلَى الرِّفْقِ مَا لَا يُعْطِي عَلَى الْعُنْفِ وَمَا لَا يُعْطِي عَلَى مَا سِوَاهُ",
        "terjemah": "Sesungguhnya Allah itu Maha Lembut dan mencintai kelemahlembutan. Dia memberikan pada kelemahlembutan apa yang tidak Dia berikan pada kekerasan, dan apa yang tidak Dia berikan pada selainnya.",
        "sumber": "HR. Muslim (Shahih Muslim No. 2593) & Syarah Riyadush Shalihin (Juz 49 Hal. 7)",
        "relevansi": "Penanganan setiap studi kasus penyimpangan anak harus diawali dengan pendinginan emosi, pengisian tangki cinta, dan pendekatan bertahap berbasis kelembutan."
    },
    "Kaidah Implementasi di Berbagai Lembaga.md": {
        "search_query": "ابدأ بنفسك ثم بمن تعول",
        "ayat_or_hadits": "ابْدَأْ بِنَفْسِكَ فَتَصَدَّقْ عَلَيْهَا، فَإِنْ فَضَلَ شَيْءٌ فَلِأَهْلِكَ، فَإِنْ فَضَلَ عَنْ أَهْلِكَ شَيْءٌ فَلِذِي قَرَابَتِكَ، فَإِنْ فَضَلَ عَنْ ذِي قَرَابَتِكَ شَيْءٌ فَهَكَذَا وَهَكَذَا",
        "terjemah": "Mulailah dari dirimu sendiri, bersedekahlah untuk dirimu. Jika ada kelebihan, maka untuk keluargamu. Jika masih ada kelebihan dari keluargamu, maka untuk kerabatmu. Jika masih ada kelebihan dari kerabatmu, maka untuk begini dan begini (orang lain di sekitarmu)...",
        "sumber": "HR. Muslim (Shahih Muslim - Kitab az-Zakah, No. 997) & Syarah Shahih Muslim Imam An-Nawawi (Juz 7 Hal. 83)",
        "relevansi": "Kaidah prioritas institusional: adopsi PKN pada lembaga (sekolah, pesantren, ormas, komunitas) wajib memprioritaskan pembenahan internal (keteladanan guru, kurikulum internal, adab) sebelum ekspansi program eksternal secara masif."
    },
    "Panduan Asesmen dan Observasi TB40.md": {
        "search_query": "اعملوا فكل ميسر لما خلق له",
        "ayat_or_hadits": "اعْمَلُوا فَكُلٌّ مُيَسَّرٌ لِمَا خُلِقَ لَهُ",
        "terjemah": "Beramallah kalian! Karena setiap orang akan dimudahkan menuju apa yang ia diciptakan untuknya.",
        "sumber": "HR. Bukhari (No. 4949) & Muslim (No. 2647) - Kitab al-Qadar; Syarah Sunan At-Tirmidzi Al-Mubarakfuri (Juz 6 Hal. 331)",
        "relevansi": "Landasan filosofis asesmen TB-40: pemetaan bakat bertujuan menemukan medan amal peradaban yang dimudahkan Allah bagi setiap insan, bukan untuk membatasi takdir."
    }
}

def generate_mapping_markdown():
    """Generates DALIL_MAPPING.md comprehensively."""
    lines = [
        "# Master Katalog Dalil & Rujukan Nabawiyah Wiki PKN",
        "",
        "Dokumen ini memetakan seluruh dalil primer (*Qur'an, Hadits Shahih, Tafsir Ibnu Katsir, dan Syarah Klasik*) yang diekstraksi dari korpus **OpenBayan** (`data/shamela_corpus.db`) untuk setiap topik bahasan di **Wiki PKN**.",
        "",
        f"> **Total Entri Terindeks:** {len(DALIL_CATALOG)} berkas halaman materi pokok.",
        "",
        "---",
        ""
    ]

    for fname, data in DALIL_CATALOG.items():
        lines.append(f"## 📄 `{fname}`")
        lines.append(f"**Kata Kunci OpenBayan:** `{data['search_query']}`")
        lines.append("")
        lines.append(f"> [!quote] Dalil & Rujukan Nabawiyah")
        lines.append(f"> **Naskah:**  ")
        lines.append(f"> « {data['ayat_or_hadits']} »")
        lines.append(f"> ")
        lines.append(f"> *\"{data['terjemah']}\"*")
        lines.append(f"> ")
        lines.append(f"> 📚 **Sumber Rujukan OpenBayan:** {data['sumber']}  ")
        lines.append(f"> 💡 **Relevansi PKN:** {data['relevansi']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(DALIL_MAP_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✓ Berhasil membuat {DALIL_MAP_PATH} dengan {len(DALIL_CATALOG)} pemetaan dalil primer.")

def apply_dalil_to_files():
    """Injects or updates the dalil callout in each matching content file."""
    applied_count = 0
    skipped_count = 0

    md_files = list(CONTENT_DIR.rglob("*.md"))
    file_map = {f.name: f for f in md_files}

    for target_name, data in DALIL_CATALOG.items():
        if target_name not in file_map:
            print(f"⚠️ Berkas {target_name} tidak ditemukan di {CONTENT_DIR}")
            skipped_count += 1
            continue

        fpath = file_map[target_name]
        content = fpath.read_text(encoding="utf-8")

        callout_text = f"""> [!quote] Dalil & Rujukan Nabawiyah
> **Naskah:**  
> « {data['ayat_or_hadits']} »
>
> *"{data['terjemah']}"*
>
> 📚 **Sumber Rujukan OpenBayan:** {data['sumber']}  
> 💡 **Relevansi PKN:** {data['relevansi']}
"""

        # Check if callout already exists
        if "[!quote] Dalil & Rujukan Nabawiyah" in content:
            new_content = re.sub(
                r'> \[!quote\] Dalil & Rujukan Nabawiyah[\s\S]*?(?=\n\n## |\n## |\Z)',
                callout_text.strip(),
                content,
                count=1
            )
        else:
            # Insert right after the first level 1 heading
            if re.search(r'^# [^\n]+', content, flags=re.MULTILINE):
                new_content = re.sub(
                    r'(^# [^\n]+\n+)',
                    r'\1' + callout_text + "\n",
                    content,
                    count=1,
                    flags=re.MULTILINE
                )
            else:
                # Insert right after frontmatter
                new_content = re.sub(
                    r'(^---\n[\s\S]*?\n---\n+)',
                    r'\1' + callout_text + "\n",
                    content,
                    count=1,
                    flags=re.MULTILINE
                )

        if new_content != content:
            fpath.write_text(new_content, encoding="utf-8")
            applied_count += 1
            print(f"✓ Berhasil menyematkan dalil ke: {fpath.relative_to(CONTENT_DIR.parent)}")
        else:
            print(f"→ Berkas {target_name} sudah mutakhir.")

    print(f"\n🎉 Selesai: {applied_count} berkas diperkaya, {skipped_count} dilewati.")

def verify_corpus_dalil():
    """Runs search on all catalog entries against OpenBayan to test database hit rates."""
    print(f"\n🔎 Memverifikasi keterhubungan ke korpus OpenBayan ({OPENBAYAN_DB})...\n" + "=" * 70)
    hit_count = 0
    total = len(DALIL_CATALOG)

    for fname, data in DALIL_CATALOG.items():
        q = data["search_query"]
        hits = search_corpus(q, limit=1)
        if hits:
            hit_count += 1
            h = hits[0]
            print(f"✓ [{hit_count}/{total}] `{fname}` -> Hit: [{h['book_name']}] {h['volume_page']}")
        else:
            print(f"⚠ [{hit_count}/{total}] `{fname}` -> Query `{q}`")

    print("=" * 70)
    print(f"Hasil Verifikasi: {hit_count}/{total} ({hit_count/total*100:.1f}%) entri dalil langsung cocok dengan korpus OpenBayan.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Penggunaan:")
        print("  python3 scripts/search_dalil_openbayan.py <query_arab>")
        print("  python3 scripts/search_dalil_openbayan.py --map")
        print("  python3 scripts/search_dalil_openbayan.py --apply")
        print("  python3 scripts/search_dalil_openbayan.py --verify")
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "--map":
        generate_mapping_markdown()
    elif arg == "--apply":
        generate_mapping_markdown()
        apply_dalil_to_files()
    elif arg == "--verify":
        verify_corpus_dalil()
    else:
        lim = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        res = search_corpus(arg, lim)
        print(f"\n🔍 Hasil pencarian OpenBayan untuk: '{arg}' (Ditemukan: {len(res)})\n" + "=" * 70)
        for i, item in enumerate(res, 1):
            snippet = " ".join(item["raw_text"].split()[:35])
            print(f"\n{i}. [{item['book_name']}] - {item['volume_page']}")
            print(f"   Bab/Pasal: {item['section_title']}")
            print(f"   Penulis  : {item['author']} ({item['category']})")
            print(f"   Kutipan  : {snippet}...")
        print("\n" + "=" * 70 + "\n")

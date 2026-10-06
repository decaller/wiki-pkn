#!/usr/bin/env python3
"""
Generator 31 Halaman Dalil Mandiri PKN (Zero-Token First)
Membangun dokumen Markdown berstandar Quartz v5 4-Zone untuk seluruh
broken link target yang tersisa dari run OMP.
"""

import os

DALIL_PAGES = {
    "dalil-amal-ikhlas-mengharap-wajah-allah": {
        "title": "Hadits Syarat Diterimanya Amal: Keikhlasan Niat",
        "description": "Nas, takhrij, syarah salaf, dan penerapan keikhlasan niat pendidik PKN dari HR. An-Nasa'i no. 3140.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Takhrij", "SyarahSalaf", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Sunan An-Nasa'i, Kitab al-Jihad, no. 3140",
            "Ibnul Qayyim, Madarijus Salikin, 2/68"
        ],
        "matan": "« إِنَّ اللَّهَ لاَ يَقْبَلُ مِنَ الْعَمَلِ إِلاَّ مَا كَانَ لَهُ خَالِصًا وَابْتُغِيَ بِهِ وَجْهُهُ »",
        "terjemahan": "Sesungguhnya Allah tidak akan menerima suatu amal perbuatan kecuali amalan yang murni (ikhlas) semata-mata untuk-Nya dan dicari dengannya wajah-Nya.",
        "takhrij": "HR. An-Nasa'i No. 3140, Kitab al-Jihad, hadits hasan shahih.",
        "syarah": "Ibnul Qayyim Al-Jauziyyah dalam Madarijus Salikin (2/68) menegaskan bahwa amal tanpa keikhlasan laksana musafir yang mengisi kantong bekalnya dengan pasir; memberatkan perjalanan namun tidak memberi manfaat. Bagi pendidik, ketiadaan ikhlas menjadikan transfer ilmu hampa nur keimanan.",
        "analisis": "Dalam PKN, ruhul mudarris berakar pada ketulusan niat. Pendidik menunaikan pengajaran sebagai ibadah dan amanah peradaban, bukan semata transaksi upah administratif.",
        "related": ["Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi", "Tazkiyatun Nafs", "index"]
    },
    "dalil-keutamaan-mengajar-kebaikan": {
        "title": "Hadits Keutamaan Mengajarkan Kebaikan kepada Manusia",
        "description": "Nas, takhrij, dan syarah semesta mendoakan guru kebaikan dari HR. At-Tirmidzi no. 2685.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Takhrij", "SyarahSalaf", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Sunan At-Tirmidzi, Kitab al-'Ilm, no. 2685",
            "Imam Al-Ghazali, Ihya' 'Ulumiddin, Kitab al-'Ilm, Bab 1"
        ],
        "matan": "« فَضْلُ الْعَالِمِ عَلَى الْعَابِدِ كَفَضْلِي عَلَى أَدْنَاكُمْ... إِنَّ اللَّهَ وَمَلَائِكَتَهُ وَأَهْلَ السَّمَوَاتِ وَالأَرَضِينَ حَتَّى النَّمْلَةَ فِي جُحْرِهَا وَحَتَّى الْحُوتَ لَيُصَلُّونَ عَلَى مُعَلِّمِ النَّاسِ الْخَيْرَ »",
        "terjemahan": "Keutamaan orang yang berilmu atas ahli ibadah laksana keutamaanku atas orang yang paling rendah di antara kalian... Sesungguhnya Allah, para malaikat-Nya, dan seluruh penghuni langit dan bumi hingga semut di sarangnya dan ikan di lautan senantiasa mendoakan kebaikan bagi orang yang mengajarkan kebaikan kepada manusia.",
        "takhrij": "HR. At-Tirmidzi No. 2685, hadits hasan shahih.",
        "syarah": "Imam Al-Ghazali dalam Ihya' 'Ulumiddin menjelaskan bahwa semesta mendoakan guru kebaikan karena ilmu yang diajarkannya memelihara keharmonisan sunnatullah di bumi dan mencegah kerusakan fitrah.",
        "analisis": "Profesi pendidik karakter nabawiyah memiliki derajat kemuliaan peradaban tertinggi. Mengajar adab dan tauhid adalah warisan para nabi.",
        "related": ["Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi", "Peran Guru dan Lembaga Pendidikan"]
    },
    "dalil-kelembutan-nabi-mengajar": {
        "title": "Hadits Keteladanan Pendidik: Kelembutan Nabi Mengajar",
        "description": "Nas, takhrij, dan syarah riwayat Mu'awiyah bin al-Hakam dari HR. Muslim no. 537.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Takhrij", "SyarahSalaf", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih Muslim, Kitab al-Masajid, no. 537",
            "Imam An-Nawawi, Syarah Shahih Muslim, 5/20"
        ],
        "matan": "« فَبِأَبِي هُوَ وَأُمِّي، مَا رَأَيْتُ مُعَلِّمًا قَبْلَهُ وَلاَ بَعْدَهُ أَحْسَنَ تَعْلِيمًا مِنْهُ، فَوَاللَّهِ مَا كَهَرَنِي وَلاَ ضَرَبَنِي وَلاَ شَتَمَنِي، قَالَ: إِنَّ هَذِهِ الصَّلاَةَ لاَ يَصْلُحُ فِيهَا شَيْءٌ مِنْ كَلاَمِ النَّاسِ... »",
        "terjemahan": "Demi ayah dan ibuku sebagai tebusannya, aku belum pernah melihat seorang pendidik pun sebelum maupun sesudahnya yang lebih baik pengajarannya daripada beliau. Demi Allah, beliau tidak membentakku, tidak memukulku, dan tidak mencelaku...",
        "takhrij": "HR. Muslim No. 537, Kitab al-Masajid wa Mawadhi' ash-Shalah.",
        "syarah": "Imam An-Nawawi dalam Syarah Shahih Muslim (5/20) menegaskan keindahan pedagogi Rasulullah ﷺ yang tidak mempermalukan orang yang belum tahu, melainkan membimbing dengan hikmah dan kelembutan.",
        "analisis": "Metode pengajaran Nabi mengutamakan koneksi hati dan dialog hikmah daripada amarah. Kesalahan santri dihadapi sebagai kesempatan belajar (teachable moment).",
        "related": ["Kaidah Pedagogis KH. Abdullah Syukri Zarkasyi", "Bahasa Hati", "Bahasa Lisan"]
    },
    "dalil-atsar-utsman-hati-kalam-allah": {
        "title": "Atsar Utsman bin Affan: Kesucian Hati dan Kalamullah",
        "description": "Atsar Utsman bin Affan mengenai hubungan kesucian hati dengan kecintaan membaca Al-Qur'an.",
        "tags": ["DalilSyar'i", "AtsarSahabat", "TazkiyatunNafs", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Ibnu Abi Syaibah, Al-Mushannaf, 7/151; Al-Baihaqi, Syu'abul Iman, 3/399",
            "Ibnul Qayyim, Al-Jawab Al-Kafi, hlm. 95"
        ],
        "matan": "« لَوْ أَنَّ قُلُوبَنَا طَهُرَتْ مَا شَبِعْنَا مِنْ كَلَامِ رَبِّنَا »",
        "terjemahan": "Seandainya hati kita suci dan bersih, niscaya kita tidak akan pernah merasa kenyang (bosan) dari Kalam (Al-Qur'an) Rabb kita.",
        "takhrij": "Diriwayatkan oleh Ibnu Abi Syaibah dalam Al-Mushannaf (no. 35741) dan dinukil oleh Ibnul Qayyim dalam Al-Jawab Al-Kafi.",
        "syarah": "Ibnul Qayyim menjelaskan bahwa kebosanan terhadap Al-Qur'an bersumber dari kotoran syahwat dan noda dosa yang menutupi cermin hati. Ketika hati dibersihkan, Kalamullah menjadi penyejuk jiwa yang tiada tara.",
        "analisis": "Membangun kecintaan anak kepada Al-Qur'an dimulai dengan membersihkan persepsi, menjaga konsumsi yang halal, dan menjauhkan dari racun fitrah.",
        "related": ["Renungan/Persepsi Positif", "Tazkiyatun Nafs", "Tangki Cinta"]
    },
    "dalil-nabi-duduk-di-antara-sahabat": {
        "title": "Hadits Kerendahan Hati: Nabi Duduk Berbaur Bersama Sahabat",
        "description": "Nas dan syarah keteladanan Nabi ﷺ duduk bersama sahabat tanpa sekat feodal.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Karakter", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Sunan Abu Dawud, no. 4698; Sunan An-Nasa'i, no. 5036",
            "Al-Mubarakfuri, Tuhfatul Ahwadzi, 9/74"
        ],
        "matan": "« كَانَ رَسُولُ اللَّهِ ﷺ يَجْلِسُ بَيْنَ ظَهْرَانَيْ أَصْحَابِهِ، فَيَجِيءُ الْغَرِيبُ فَلَا يَدْرِي أَيُّهُمْ هُوَ حَتَّى يَسْأَلَ »",
        "terjemahan": "Rasulullah ﷺ senantiasa duduk berbaur di tengah-tengah para sahabatnya, sampai-sampai apabila datang orang asing yang belum mengenal beliau, orang itu tidak tahu mana beliau hingga bertanya...",
        "takhrij": "HR. Abu Dawud No. 4698 dan An-Nasa'i No. 5036, shahih.",
        "syarah": "Para ulama menjelaskan bahwa riwayat ini menunjukkan puncak ketawadhu'an pemimpin agung. Beliau tidak membuat singgasana terpisah, melainkan menyatu dalam denyut kehidupan umatnya.",
        "analisis": "Pendidik dan orang tua tidak membangun benteng keangkuhan formalistik di hadapan anak. Wibawa sejati lahir dari keteladanan dan kedekatan, bukan dari jarak feodal.",
        "related": ["Renungan/Persepsi Positif", "Peran Ayah dan Bunda", "Peran Guru dan Lembaga Pendidikan"]
    },
    "dalil-kecintaan-amr-bin-al-ash-kepada-nabi": {
        "title": "Riwayat Amr bin Al-Ash: Wibawa dan Cinta kepada Rasulullah ﷺ",
        "description": "Kesaksian Amr bin Al-Ash mengenai perpaduan cinta mendalam dan wibawa agung Nabi ﷺ.",
        "tags": ["DalilSyar'i", "AtsarSahabat", "SirahNabawiyah", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih Muslim, Kitab al-Iman, no. 121"
        ],
        "matan": "« وَمَا كَانَ أَحَدٌ أَحَبَّ إِلَيَّ مِنْ رَسُولِ اللهِ ﷺ، وَلاَ أَجَلَّ فِي عَيْنِي مِنْهُ، وَمَا كُنْتُ أُطِيقُ أَنْ أَمْلَأَ عَيْنَيَّ مِنْهُ إِجْلاَلاً لَهُ، وَلَوْ سُئِلْتُ أَنْ أَصِفَهُ مَا أَطَقْتُ، لِأَنِّي لَمْ أَكُنْ أَمْلَأُ عَيْنَيَّ مِنْهُ »",
        "terjemahan": "Tidak ada seorang pun yang lebih aku cintai selain Rasulullah ﷺ, dan tidak ada yang lebih agung di mataku selain beliau. Namun aku tidak sanggup memandang beliau lama-lama karena memuliakannya...",
        "takhrij": "HR. Muslim No. 121, Kitab al-Iman.",
        "syarah": "Imam An-Nawawi menjelaskan bahwa penghormatan para sahabat kepada Nabi ﷺ bersumber dari kewibawaan Ilahi dan cinta batin, bukan rasa takut akan siksa atau paksaan lahiriah.",
        "analisis": "Kewibawaan pendidik terbangun ketika anak mencintai gurunya secara mendalam. Kepatuhan sukarela lahir dari cinta yang memuliakan.",
        "related": ["Renungan/Persepsi Positif", "Bahasa Hati", "Tangki Cinta"]
    },
    "dalil-hr-abu-dawud-1109": {
        "title": "Hadits Nabi Menjeda Khutbah Demi Cucu",
        "description": "Nas, takhrij, dan syarah Nabi ﷺ turun dari mimbar saat khutbah untuk memeluk Hasan dan Husain.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "PendidikanAnak", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Sunan Abu Dawud, no. 1109; Jami' At-Tirmidzi, no. 3774",
            "Al-Khaththabi, Ma'alimus Sunan, 1/263"
        ],
        "matan": "« كَانَ رَسُولُ اللَّهِ ﷺ يَخْطُبُنَا إِذْ جَاءَ الْحَسَنُ وَالْحُسَيْنُ عَلَيْهِمَا قَمِيصَانِ أَحْمَرَانِ يَمْشِيَانِ وَيَعْثُرَانِ، فَنَزَلَ رَسُولُ اللَّهِ ﷺ مِنَ الْمِنْبَرِ، فَحَمَلَهُمَا وَوَضَعَهُمَا بَيْنَ يَدَيْهِ »",
        "terjemahan": "Rasulullah ﷺ sedang berkhutbah di hadapan kami di atas mimbar, tiba-tiba datanglah Hasan dan Husain mengenakan baju merah sambil berjalan tertatih-tatih dan terjatuh. Maka beliau langsung turun dari mimbar, lalu menggendong keduanya dan mendudukkan mereka di hadapan beliau...",
        "takhrij": "HR. Abu Dawud No. 1109, At-Tirmidzi No. 3774 (shahih), An-Nasa'i No. 1413.",
        "syarah": "Al-Khaththabi menjelaskan bahwa tindakan Nabi ﷺ menunjukkan kelembutan kasih sayang melampaui protokoler formal demi menjaga keselamatan emosional anak usia dini.",
        "analisis": "Pada fase usia dini (0–7 tahun), pelukan dan rasa aman anak didahulukan di atas formalitas majelis. Anak merasakan masjid sebagai tempat penuh kehangatan.",
        "related": ["Renungan/Hak dan Kewajiban", "Thufulah", "Tangki Cinta"]
    },
    "dalil-hr-bukhari-6038": {
        "title": "Hadits Pelayanan Anas bin Malik: 10 Tahun Membimbing Tanpa Celaan",
        "description": "Nas dan syarah kesabaran Rasulullah ﷺ membimbing Anas bin Malik selama sepuluh tahun tanpa celaan.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "MetodeMendidik", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab al-Adab, no. 6038; Shahih Muslim, no. 2309",
            "Ibnu Hajar Al-Asqalani, Fathul Bari, 10/457"
        ],
        "matan": "« خَدَمْتُ رَسُولَ اللَّهِ ﷺ عَشْرَ سِنِينَ، فَمَا قَالَ لِي أُفٍّ قَطُّ، وَمَا قَالَ لِشَيْءٍ صَنَعْتُهُ: لِمَ صَنَعْتَهُ؟ وَلَا لِشَيْءٍ تَرَكْتُهُ: لِمَ تَرَكْتَهُ؟ »",
        "terjemahan": "Sungguh aku telah melayani Rasulullah ﷺ selama sepuluh tahun, dan beliau tidak pernah sekalipun berkata kepadaku 'Ah', tidak pernah mencela apa yang aku perbuat: 'Mengapa engkau melakukannya?', dan tidak pernah menyalahkan apa yang aku tinggalkan: 'Mengapa engkau tidak melakukannya?'.",
        "takhrij": "HR. Bukhari No. 6038 dan Muslim No. 2309.",
        "syarah": "Al-Hafizh Ibnu Hajar menjelaskan bahwa kesabaran Nabi ﷺ terhadap anak/pembantu mencerminkan kesempurnaan akhlak dan pemahaman akan takdir serta pentahapan kedewasaan.",
        "analisis": "Hak anak pada masa pertumbuhan adalah belajar dari kesalahan tanpa dihantui caci maki. Mengurangi celaan verbal menjaga ketulusan jiwa anak.",
        "related": ["Bahasa Hati", "Renungan/Hak dan Kewajiban", "Disiplin Positif PKN"]
    },
    "dalil-qs-18-54": {
        "title": "QS. Al-Kahfi: 54 — Beragam Perumpamaan dan Karakter Membantah",
        "description": "Nas dan tafsir QS. Al-Kahfi ayat 54 mengenai pentingnya permisalan dan narasi dalam pendidikan.",
        "tags": ["DalilSyar'i", "AlQuran", "Tafsir", "PendidikanKarakterNabawiyah"],
        "sources": [
            "QS. Al-Kahfi [18]: 54",
            "Tafsir Ibnu Katsir, 5/168"
        ],
        "matan": "« وَلَقَدْ صَرَّفْنَا فِي هَذَا الْقُرْآنِ لِلنَّاسِ مِن كُلِّ مَثَلٍ ۚ وَكَانَ الْإِنسَانُ أَكْثَرَ شَيْءٍ جَدَلًا »",
        "terjemahan": "Dan sesungguhnya Kami telah menjelaskan berulang-ulang kepada manusia dalam Al-Qur'an ini bermacam-macam perumpamaan. Namun manusia adalah makhluk yang paling banyak membantah.",
        "takhrij": "QS. Al-Kahfi [18]: 54.",
        "syarah": "Ibnu Katsir menjelaskan bahwa Allah menyajikan berbagai analogi, kisah, dan permisalan agar manusia memahami kebenaran dengan mudah dan terhindar dari perdebatan kosong.",
        "analisis": "Dalam PKN, pengajaran adab menggunakan kisah nyata dan perumpamaan konkrit (Storytelling Sirah) agar menembus logika keras anak tanpa memicu debat defensif.",
        "related": ["Renungan/Hak dan Kewajiban", "Bank Cerita Sirah dan Apersepsi KBM"]
    },
    "dalil-pena-diangkat-tiga-golongan": {
        "title": "Hadits Diangkatnya Pena Taklif dari Tiga Golongan",
        "description": "Nas, takhrij, dan batasan taklif anak sebelum baligh dari HR. Abu Dawud no. 4403.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "UshulFiqih", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Sunan Abu Dawud, no. 4403; Jami' At-Tirmidzi, no. 1423",
            "Al-Khaththabi, Ma'alimus Sunan, 3/298"
        ],
        "matan": "« رُفِعَ الْقَلَمُ عَنْ ثَلَاثَةٍ: عَنِ النَّائِمِ حَتَّى يَسْتَيْقِظَ، وَعَنِ الصَّبِيِّ حَتَّى يَحْتَلِمَ، وَعَنِ الْمَجْنُونِ حَتَّى يَعْقِلَ »",
        "terjemahan": "Diangkat pena (pencatat amal) dari tiga orang: dari orang yang tidur sampai ia bangun, dari anak kecil sampai ia bermimpi basah (baligh), dan dari orang gila sampai ia berakal.",
        "takhrij": "HR. Abu Dawud No. 4403, At-Tirmidzi No. 1423, Ibnu Majah No. 2041, shahih.",
        "syarah": "Para fuqaha menjelaskan bahwa anak kecil belum dikenakan taklif hukum pertanggungjawaban dosa secara mutlak sampai ia mencapai kematangan akil baligh.",
        "analisis": "Anak sebelum baligh berada dalam fase pembiasaan dan latihan (tamrin), bukan penjatuhan vonis dosa atau hukuman pidana. Pendidik bersikap membina, bukan menghakimi.",
        "related": ["Renungan/Disiplin Positif PKN", "Tamyiz", "Murahaqah"]
    },
    "dalil-qs-57-25": {
        "title": "QS. Al-Hadid: 25 — Kitab, Mizan, dan Kekuatan Besi",
        "description": "Nas dan tafsir QS. Al-Hadid: 25 mengenai integrasi wahyu, keadilan, dan teknologi dalam peradaban.",
        "tags": ["DalilSyar'i", "AlQuran", "Tafsir", "PendidikanKarakterNabawiyah"],
        "sources": [
            "QS. Al-Hadid [57]: 25",
            "Tafsir Ibnu Katsir, 8/27"
        ],
        "matan": "« لَقَدْ أَرْسَلْنَا رُسُلَنَا بِالْبَيِّنَاتِ وَأَنزَلْنَا مَعَهُمُ الْكِتَابَ وَالْمِيزَانَ لِيَقُومَ النَّاسُ بِالْقِسْطِ ۖ وَأَنزَلْنَا الْحَدِيدَ فِيهِ بَأْسٌ شَدِيدٌ وَمَنَافِعُ لِلنَّاسِ »",
        "terjemahan": "Sungguh, Kami telah mengutus rasul-rasul Kami dengan bukti-bukti yang nyata dan Kami turunkan bersama mereka Kitab dan neraca (keadilan) agar manusia dapat berlaku adil. Dan Kami ciptakan besi yang mempunyai kekuatan hebat dan banyak manfaat bagi manusia...",
        "takhrij": "QS. Al-Hadid [57]: 25.",
        "syarah": "Syaikhul Islam Ibnu Taimiyyah menegaskan bahwa tegaknya agama bersumber dari Kitab yang memberi petunjuk dan Besi yang membela keadilan.",
        "analisis": "Pendidikan Karakter Nabawiyah memadukan ilmu syar'i (Kitab), objektivitas keadilan (Mizan), dan instrumen teknologi modern (Besi/Software) demi kemaslahatan dakwah.",
        "related": ["Pengembangan Software dan Ekosistem Digital PKN", "Bakat/Bekerja Keras"]
    },
    "dalil-hr-tirmidhi-2687": {
        "title": "Hadits Hikmah adalah Barang Hilang Orang Mukmin",
        "description": "Nas, takhrij, dan makna hikmah sebagai barang berharga yang dicari mukmin dari HR. At-Tirmidzi no. 2687.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Epistemologi", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Jami' At-Tirmidzi, no. 2687; Sunan Ibnu Majah, no. 4169",
            "Al-Mubarakfuri, Tuhfatul Ahwadzi, 7/393"
        ],
        "matan": "« الْكَلِمَةُ الْحِكْمَةُ ضَالَّةُ الْمُؤْمِنِ، فَحَيْثُ وَجَدَهَا فَهُوَ أَحَقُّ بِهَا »",
        "terjemahan": "Kalimat hikmah adalah barang hilang milik orang mukmin; di mana pun ia menemukannya, maka ia lebih berhak atasnya.",
        "takhrij": "HR. At-Tirmidzi No. 2687 dan Ibnu Majah No. 4169, diriwayatkan dengan sanad yang diperbincangkan namun maknanya shahih menurut kesepakatan ulama.",
        "syarah": "Para ulama menjelaskan bahwa seorang mukmin senantiasa menyerap kebaikan, ilmu bermanfaat, dan kebenaran dari mana pun asalnya dengan tetap menimbang pada timbangan syariat.",
        "analisis": "PKN bersikap terbuka terhadap alat, teknologi, dan instrumen empiris modern selama selaras dengan fitrah tauhid dan manhaj nabawiyah.",
        "related": ["Pengembangan Software dan Ekosistem Digital PKN", "Bakat/Berpikir"]
    },
    "dalil-atsar-ali-ajarkan-ilmu-dan-adab": {
        "title": "Atsar Ali bin Abi Thalib: Ajarkan Ilmu dan Adab kepada Keluarga",
        "description": "Atsar Ali bin Abi Thalib dalam menafsirkan perintah menjaga keluarga dari api neraka.",
        "tags": ["DalilSyar'i", "AtsarSahabat", "TafsirQuran", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Tafsir Ath-Thabari, 23/491; Al-Hakim, Al-Mustadrak, 2/494",
            "Ibnu Katsir, Tafsir Al-Qur'an Al-'Azhim, 8/188"
        ],
        "matan": "« عَلِّمُوهُمْ وَأَدِّبُوهُمْ »",
        "terjemahan": "Ajarkanlah ilmu kepada mereka dan bimbinglah adab mereka.",
        "takhrij": "Diriwayatkan oleh Al-Hakim dalam Al-Mustadrak (2/494) dan dishahihkannya, serta dinukil oleh Ath-Thabari dalam penafsiran QS. At-Tahrim: 6.",
        "syarah": "Ali bin Abi Thalib menjelaskan bahwa makna menjaga diri dan keluarga dari api neraka adalah dengan memberikan pendidikan ilmu agama yang benar dan pembiasaan adab mulia.",
        "analisis": "Pendidikan keluarga mengintegrasikan dua pilar utama: ta'lim (transfer pengetahuan syariat) dan ta'dib (internalisasi adab dan karakter).",
        "related": ["Tanggung Jawab Pendidikan", "Peran Ayah dan Bunda", "dalil-talim-dan-tadib-keluarga"]
    },
    "dalil-atsar-rabbani-shighar-ilm": {
        "title": "Atsar Ibnu Abbas: Pendidik Rabbani dan Pentahapan Ilmu",
        "description": "Atsar Ibnu Abbas mengenai pendidik rabbani yang mendidik dari ilmu kecil sebelum ilmu besar.",
        "tags": ["DalilSyar'i", "AtsarSahabat", "Tadarruj", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab al-'Ilm, Bab al-'Ilm Qabla al-Qaul wa al-'Amal",
            "Ibnu Hajar Al-Asqalani, Fathul Bari, 1/161"
        ],
        "matan": "« الرَّبَّانِيُّ: الَّذِي يُرَبِّي النَّاسَ بِصِغَارِ العِلْمِ قَبْلَ كِبَارِهِ »",
        "terjemahan": "Pendidik yang Rabbani adalah orang yang mendidik manusia dengan ilmu-ilmu dasar (sederhana) sebelum ilmu-ilmu yang besar (rumit).",
        "takhrij": "Atsar Ibnu Abbas diriwayatkan secara mu'allaq oleh Al-Bukhari dalam Shahih-nya, Kitab al-'Ilm.",
        "syarah": "Al-Hafizh Ibnu Hajar menjelaskan bahwa tarbiyah rabbaniyah mensyaratkan pentahapan (tadarruj), memulai dari hal yang mudah dan pokok sebelum hal-hal yang rumit dan berat.",
        "analisis": "Prinsip Tadarruj dalam PKN: tidak membebani anak dengan target kurikulum yang melompati fase kematangan jiwanya.",
        "related": ["Prinsip Tadarruj", "Kaidah Implementasi di Berbagai Lembaga"]
    },
    "dalil-doa-orang-tua-mustajab": {
        "title": "Hadits Doa Orang Tua: Senjata Mustajab Pengasuhan",
        "description": "Nas, takhrij, dan syarah tiga doa mustajab termasuk doa orang tua untuk anak dari HR. Abu Dawud no. 1536.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Doa", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Sunan Abu Dawud, no. 1536; Jami' At-Tirmidzi, no. 1905",
            "Ibnul Qayyim, Zadul Ma'ad, 4/170"
        ],
        "matan": "« ثَلَاثُ دَعَوَاتٍ مُسْتَجَابَاتٍ لَا شَكَّ فِيهِنَّ: دَعْوَةُ الْمَظْلُومِ، وَدَعْوَةُ الْمُسَافِرِ، وَدَعْوَةُ الْوَالِدِ لِوَلَدِهِ »",
        "terjemahan": "Tiga doa yang mustajab, tiada keraguan di dalamnya: doanya orang yang terzalimi, doanya musafir, dan doanya orang tua untuk anaknya.",
        "takhrij": "HR. Abu Dawud No. 1536, At-Tirmidzi No. 1905, hasan shahih.",
        "syarah": "Ibnul Qayyim dalam Zadul Ma'ad menjelaskan bahwa doa orang tua mustajab karena bersumber dari lubuk hati yang paling ikhlas dan dipenuhi rasa belas kasih mendalam.",
        "analisis": "Doa orang tua adalah senjata utama tarbiyah PKN yang menembus batas ikhtiar teknis manusiawi dan menjemput pertolongan Allah Ta'ala.",
        "related": ["Tawakkal dan Doa", "Peran Ayah dan Bunda"]
    },
    "dalil-hr-abu-dawud-3641": {
        "title": "Hadits Keutamaan Penuntut Ilmu: Naungan Sayap Malaikat",
        "description": "Nas dan syarah kemuliaan thalabul ilmi dan doa penghuni langit dan bumi dari HR. Abu Dawud no. 3641.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "ThalabulIlmi", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Sunan Abu Dawud, no. 3641; Jami' At-Tirmidzi, no. 2682",
            "Ibnu Rajab Al-Hanbali, Jami'ul 'Ulum wal Hikam, 2/297"
        ],
        "matan": "« مَنْ سَلَكَ طَرِيقًا يَطْلُبُ فِيهِ عِلْمًا سَلَكَ اللَّهُ بِهِ طَرِيقًا مِنْ طُرُقِ الْجَنَّةِ، وَإِنَّ الْمَلَائِكَةَ لَتَضَعُ أَجْنِحَتَهَا رِضًا لِطَالِبِ الْعِلْمِ... »",
        "terjemahan": "Barang siapa menempuh jalan untuk menuntut ilmu, Allah akan mudahkan baginya jalan menuju surga. Dan sesungguhnya para malaikat membentangkan sayapnya karena ridha kepada penuntut ilmu...",
        "takhrij": "HR. Abu Dawud No. 3641, shahih.",
        "syarah": "Ibnu Rajab menjelaskan bahwa bentangan sayap malaikat adalah bentuk pemuliaan dan perlindungan ilahi kepada para penuntut ilmu yang ikhlas.",
        "analisis": "Pendidikan karakter memupuk rasa takzim terhadap ilmu sejak dini agar santri merasakan manisnya belajar di bawah naungan rahmat.",
        "related": ["Peran Guru dan Lembaga Pendidikan", "Belajar"]
    },
    "dalil-hr-bukhari-1458": {
        "title": "Hadits Mu'adz bin Jabal: Skala Prioritas Dakwah dan Tarbiyah",
        "description": "Nas dan syarah hierarki dakwah tauhid sebelum shalat dari pesan Nabi ﷺ kepada Mu'adz bin Jabal.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Tadarruj", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab az-Zakah, no. 1458; Shahih Muslim, no. 19",
            "Ibnu Hajar Al-Asqalani, Fathul Bari, 3/357"
        ],
        "matan": "« إِنَّكَ تَقْدَمُ عَلَى قَوْمٍ أَهْلِ كِتَابٍ، فَلْيَكُنْ أَوَّلَ مَا تَدْعُوهُمْ إِلَيْهِ عِبَادَةُ اللَّهِ، فَإِذَا عَرَفُوا اللَّهَ، فَأَخْبِرْهُمْ أَنَّ اللَّهَ قَدْ فَرَضَ عَلَيْهِمْ خَمْسَ صَلَوَاتٍ... »",
        "terjemahan": "Sesungguhnya engkau akan mendatangi kaum Ahli Kitab. Maka hendaklah perkara pertama yang engkau serukan kepada mereka adalah beribadah kepada Allah (tauhid). Jika mereka telah mengenal Allah, beritahukanlah bahwa Allah mewajibkan shalat lima waktu...",
        "takhrij": "HR. Bukhari No. 1458 dan Muslim No. 19.",
        "syarah": "Ibnu Hajar menjelaskan kaidah prioritas: fondasi akidah dan mengenal Allah harus kokoh sebelum pembebanan syariat amal lahiriah.",
        "analisis": "Prioritas Program PKN: menanamkan fitrah iman dan cinta kepada Allah mendahului penegakan kedisiplinan aturan teknis.",
        "related": ["Prioritasi Program Lembaga Berbasis Maqashid Syariah", "Prinsip Tadarruj"]
    },
    "dalil-hr-bukhari-3038": {
        "title": "Hadits Nilai Petunjuk: Lebih Berharga dari Unta Merah",
        "description": "Nas dan syarah keutamaan membimbing satu jiwa menuju hidayah dari HR. Bukhari no. 3038.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Pendidik", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab al-Jihad, no. 3038; Shahih Muslim, no. 2406",
            "An-Nawawi, Syarah Shahih Muslim, 15/178"
        ],
        "matan": "« فَوَاللَّهِ لَأَنْ يَهْدِيَ اللَّهُ بِكَ رَجُلًا وَاحِدًا، خَيْرٌ لَكَ مِنْ أَنْ يَكُونَ لَكَ حُمْرُ النَّعَمِ »",
        "terjemahan": "Demi Allah, sungguh jika Allah memberi petunjuk kepada satu orang saja melalui perantaramu, itu jauh lebih baik bagimu daripada engkau memiliki unta merah (harta paling berharga bangsa Arab).",
        "takhrij": "HR. Bukhari No. 3038 dan Muslim No. 2406.",
        "syarah": "Imam An-Nawawi menjelaskan bahwa unta merah adalah metafora kemewahan duniawi tertinggi. Menyelamatkan satu jiwa manusia dari kegelapan menuju cahaya hidayah melampaui seluruh nilai materi.",
        "analisis": "Orientasi pendidik PKN bukan pada kuantitas hafalan semata, melainkan pada kebangkitan kesadaran batin anak didik.",
        "related": ["Peran Guru dan Lembaga Pendidikan", "Menumbuhkan Kesadaran Beramal"]
    },
    "dalil-hr-bukhari-4993": {
        "title": "Hadits Aisyah: Pentahapan Turunnya Al-Qur'an dan Tarbiyah Keimanan",
        "description": "Nas, takhrij, dan syarah hikmah turunnya surat Al-Mufashshal sebelum hukum halal-haram.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Tadarruj", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab Fadha'ilil Qur'an, no. 4993",
            "Ibnu Hajar Al-Asqalani, Fathul Bari, 9/40"
        ],
        "matan": "« إِنَّمَا نَزَلَ أَوَّلَ مَا نَزَلَ مِنْهُ سُورَةٌ مِنَ المُفَصَّلِ، فِيهَا ذِكْرُ الجَنَّةِ وَالنَّارِ، حَتَّى إِذَا ثَابَ النَّاسُ إِلَى الإِسْلاَمِ نَزَلَ الحَلاَلُ وَالحَرَامُ... »",
        "terjemahan": "Sesungguhnya yang mula-mula turun dari Al-Qur'an adalah surat-surat Al-Mufashshal yang di dalamnya menceritakan surga dan neraka. Hingga ketika manusia telah condong kepada Islam, barulah turun ayat tentang halal dan haram...",
        "takhrij": "HR. Bukhari No. 4993.",
        "syarah": "Al-Hafizh Ibnu Hajar membedah kaidah tadarruj: pembangunan akidah dan penumbuhan rasa cinta serta takut kepada Allah harus mendahului penegakan hukum larangan.",
        "analisis": "Kaidah implementasi PKN: tanamkan fitrah iman di masa kecil agar ketika dewasa aturan syariat dipatuhi dengan kerelaan sukarela.",
        "related": ["4 Kaidah Implementasi", "Prinsip Tadarruj"]
    },
    "dalil-hr-bukhari-68": {
        "title": "Hadits Memilih Waktu Nasihat: Menjaga Kejenuhan Jiwa",
        "description": "Nas dan syarah keteladanan Nabi ﷺ dan Ibnu Mas'ud dalam memilih waktu menasihati murid.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Pedagogi", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab al-'Ilm, no. 68; Shahih Muslim, no. 2821",
            "Ibnu Hajar Al-Asqalani, Fathul Bari, 1/162"
        ],
        "matan": "« كَانَ النَّبِيُّ ﷺ يَتَخَوَّلُنَا بِالْمَوْعِظَةِ فِي الأَيَّامِ، كَرَاهَةَ السَّآمَةِ عَلَيْنَا »",
        "terjemahan": "Nabi ﷺ senantiasa memilih-milih waktu yang tepat untuk menasihati kami dalam beberapa hari, karena khawatir menimbulkan kejenuhan pada kami.",
        "takhrij": "HR. Bukhari No. 68 dan Muslim No. 2821.",
        "syarah": "Ibnu Hajar menjelaskan pentingnya menjaga kesiapan mental anak didik. Nasihat yang dihujankan tanpa henti dapat menimbulkan antipati dan resistensi.",
        "analisis": "Pedagogi PKN: nasihat diberikan secara proporsional dan situasional, memanfaatkan momentum alami (KBM Berbasis Peristiwa).",
        "related": ["Peran Guru dan Lembaga Pendidikan", "Bahasa Lisan"]
    },
    "dalil-hr-bukhari-69": {
        "title": "Hadits Kaidah Kemudahan: Yassiru wa La Tu'assiru",
        "description": "Nas dan syarah perintah mempermudah dan menggembirakan dari HR. Bukhari no. 69.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Pedagogi", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab al-'Ilm, no. 69; Shahih Muslim, no. 1734",
            "Ibnu Hajar Al-Asqalani, Fathul Bari, 1/163"
        ],
        "matan": "« يَسِّرُوا وَلاَ تُعَسِّرُوا، وَبَشِّرُوا وَلاَ تُنَفِّرُوا »",
        "terjemahan": "Permudahlah dan jangan mempersulit, berikanlah kabar gembira dan jangan membuat orang lari (menjauh).",
        "takhrij": "HR. Bukhari No. 69 dan Muslim No. 1734.",
        "syarah": "Ibnu Hajar menjelaskan bahwa prinsip mempermudah berlaku dalam pengajaran dan ibadah, menjauhkan manusia dari beban yang memberatkan jiwa.",
        "analisis": "Pendidikan Karakter Nabawiyah menekankan pendekatan tausir (kemudahan) dan apresiasi positif agar anak mencintai agama.",
        "related": ["Kaidah Implementasi di Berbagai Lembaga", "dalil-mengajar-badui-dengan-kemudahan"]
    },
    "dalil-hr-bukhari-71": {
        "title": "Hadits Pemahaman Agama: Tanda Kebaikan Hamba",
        "description": "Nas dan syarah hadits barang siapa yang Allah kehendaki kebaikan maka difahamkan dalam agama.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Tafaqquh", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab al-'Ilm, no. 71; Shahih Muslim, no. 1037",
            "Ibnu Hajar Al-Asqalani, Fathul Bari, 1/164"
        ],
        "matan": "« مَنْ يُرِدِ اللَّهُ بِهِ خَيْرًا يُفَقِّهْهُ فِي الدِّينِ »",
        "terjemahan": "Barang siapa yang Allah kehendaki kebaikan baginya, niscaya Allah akan memahamkannya dalam urusan agama.",
        "takhrij": "HR. Bukhari No. 71 dan Muslim No. 1037.",
        "syarah": "Para ulama menjelaskan bahwa fiqh di sini bukan sekadar hafalan hukum fiqih lahiriah, melainkan bashirah (pemahaman mendalam tentang hakikat syariat dan keimanan).",
        "analisis": "Target utama pendidikan PKN adalah kesadaran dan pemahaman (tadzawwuq ad-din), bukan sekadar kepatuhan mekanis.",
        "related": ["Program dan Kegiatan Pendidikan Karakter Nabawiyah", "Menumbuhkan Kesadaran Beramal"]
    },
    "dalil-hr-bukhari-7288": {
        "title": "Hadits Ketaatan Semampunya: Menjauhi Larangan dan Melaksanakan Perintah",
        "description": "Nas, takhrij, dan syarah kewajiban menjauhi larangan mutlak dan menjalankan perintah semampunya.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "UshulFiqih", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih al-Bukhari, Kitab al-I'tisham, no. 7288; Shahih Muslim, no. 1337",
            "Ibnu Hajar Al-Asqalani, Fathul Bari, 13/251"
        ],
        "matan": "« مَا نَهَيْتُكُمْ عَنْهُ فَاجْتَنِبُوهُ، وَمَا أَمَرْتُكُمْ بِهِ فَأْتُوا مِنْهُ مَا اسْتَطَعْتُمْ »",
        "terjemahan": "Apa saja yang aku larang bagi kalian maka jauhilah, dan apa saja yang aku perintahkan kepada kalian maka laksanakanlah semampu kalian.",
        "takhrij": "HR. Bukhari No. 7288 dan Muslim No. 1337.",
        "syarah": "Ibnu Hajar menjelaskan bahwa larangan wajib dijauhi total karena meninggalkan sesuatu tidak memerlukan tenaga fisik, sedangkan perintah terkait kemampuan biologis manusia.",
        "analisis": "Kaidah praktisi PKN: menerapkan prinsip pentahapan amal sesuai kesiapan anak, tidak menuntut beban di luar batas kemampuannya.",
        "related": ["Kaidah Implementasi di Berbagai Lembaga", "Prinsip Tadarruj"]
    },
    "dalil-hr-muslim-55": {
        "title": "Hadits Agama adalah Nasihat (Ad-Dinu An-Nashihah)",
        "description": "Nas dan syarah hadits pokok tentang agama adalah ketulusan nasihat bagi Allah, Rasul-Nya, dan sesama.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "UshulFiqih", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih Muslim, Kitab al-Iman, no. 55",
            "Imam An-Nawawi, Syarah Shahih Muslim, 2/37"
        ],
        "matan": "« الدِّينُ النَّصِيحَةُ » قُلْنَا: لِمَنْ؟ قَالَ: « لِلَّهِ وَلِكِتَابِهِ وَلِرَسُولِهِ وَلِأَئِمَّةِ الْمُسْلِمِينَ وَعَامَّتِهِمْ »",
        "terjemahan": "Agama itu adalah nasihat (ketulusan). Kami bertanya: Untuk siapa? Beliau menjawab: Untuk Allah, Kitab-Nya, Rasul-Nya, para pemimpin kaum muslimin, dan orang-orang mukmin pada umumnya.",
        "takhrij": "HR. Muslim No. 55, Kitab al-Iman.",
        "syarah": "Imam An-Nawawi menegaskan bahwa nashihah adalah menginginkan kebaikan secara tulus bagi pihak yang dinasihati tanpa motif dengki atau manipulasi.",
        "analisis": "Pendidikan karakter nabawiyah berpijak pada ketulusan cinta pendidik yang menginginkan keselamatan dunia-akhirat bagi anak didiknya.",
        "related": ["FAQ Ringkas", "Bahasa Lisan", "Master Katalog Dalil Hadits dan Sunnah"]
    },
    "dalil-hr-muslim-997": {
        "title": "Hadits Ibda' Binafsik: Memulai Teladan dari Diri Sendiri",
        "description": "Nas dan syarah prinsip memulai dari diri sendiri sebelum mendidik tanggungan.",
        "tags": ["DalilSyar'i", "HaditsNabawi", "Tazkiyah", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Shahih Muslim, Kitab az-Zakah, no. 997",
            "An-Nawawi, Syarah Shahih Muslim, 7/83"
        ],
        "matan": "« ابْدَأْ بِنَفْسِكَ ثُمَّ بِمَنْ تَعُولُ »",
        "terjemahan": "Mulailah dari dirimu sendiri, kemudian kepada orang-orang yang menjadi tanggunganmu.",
        "takhrij": "HR. Muslim No. 997 dari Jabir bin Abdillah radhiyallahu 'anhu.",
        "syarah": "Imam An-Nawawi menjelaskan urutan tanggung jawab nafkah dan perbaikan: diri sendiri mendahului orang lain agar memiliki kekuatan menopang sesama.",
        "analisis": "Kaidah emas PKN: Teladan mendahului arahan (ibda' binafsik). Orang tua memperbaiki diri terlebih dahulu sebelum menuntut kesalehan anak.",
        "related": ["Kaidah Implementasi di Berbagai Lembaga", "Peran Ayah dan Bunda"]
    },
    "dalil-kaidah-akhaff-dhararain": {
        "title": "Kaidah Fiqhiyyah: Mengambil Risiko Paling Ringan (Akhaffudh-Dhararain)",
        "description": "Prinsip ushul fiqih mengambil bahaya yang lebih ringan tatkala terjadi benturan dua kemafsadatan.",
        "tags": ["DalilSyar'i", "KaidahFiqih", "MaqashidSyariah", "PendidikanKarakterNabawiyah"],
        "sources": [
            "As-Suyuthi, Al-Asybah wan Nazha'ir, hlm. 87; Ibnu Nujaim, Al-Asybah wan Nazha'ir, hlm. 89"
        ],
        "matan": "« إِذَا تَعَارَضَتْ مَفْسَدَتَانِ رُوعِيَ أَعْظَمُهُمَا ضَرَرًا بِارْتِكَابِ أَخَفِّهِمَا »",
        "terjemahan": "Apabila berbenturan dua mafsadat (kerusakan), maka hindarilah mafsadat yang lebih besar dengan memilih mafsadat yang lebih ringan.",
        "takhrij": "Kaidah Fiqhiyyah Kubra yang disepakati seluruh madzhab Islam.",
        "syarah": "Para ulama ushul menetapkan kaidah ini untuk menavigasi dilema nyata ketika tidak mungkin selamat dari kedua mudharat secara bersamaan.",
        "analisis": "Aplikasi PKN: dalam situasi dilematis sekolah/keluarga, utamakan keselamatan aqidah dan jiwa anak di atas kerugian administratif duniawi.",
        "related": ["Prioritasi Program Lembaga Berbasis Maqashid Syariah", "dalil-kaidah-darul-mafasid"]
    },
    "dalil-kaidah-darul-mafasid": {
        "title": "Kaidah Fiqhiyyah: Menolak Kerusakan Lebih Didahulukan (Dar'ul Mafasid)",
        "description": "Prinsip ushul fiqih mendahulukan pencegahan bahaya daripada mengejar kemaslahatan.",
        "tags": ["DalilSyar'i", "KaidahFiqih", "MaqashidSyariah", "PendidikanKarakterNabawiyah"],
        "sources": [
            "As-Suyuthi, Al-Asybah wan Nazha'ir, hlm. 87; Tajuddin As-Subki, Al-Asybah wan Nazha'ir, 1/105"
        ],
        "matan": "« دَرْءُ الْمَفَاسِدِ مُقَدَّمٌ عَلَى جَلْبِ الْمَصَالِحِ »",
        "terjemahan": "Menolak kerusakan dan bahaya (mafsadat) harus didahulukan daripada mengejar kemaslahatan.",
        "takhrij": "Kaidah Fiqhiyyah Asasiyyah yang bersumber dari ruh Al-Qur'an dan Sunnah.",
        "syarah": "As-Suyuthi menjelaskan bahwa syariat sangat memperhatikan penutupan pintu-pintu keburukan agar fondasi agama tidak runtuh.",
        "analisis": "Proteksi PKN: menyingkirkan racun gadget dan pergaulan bebas didahulukan sebelum mengejar prestasi lomba yang berisiko merusak adab santri.",
        "related": ["Kaidah Implementasi di Berbagai Lembaga", "Prioritasi Program Lembaga Berbasis Maqashid Syariah"]
    },
    "dalil-kaidah-ma-la-yatimmul-wajib": {
        "title": "Kaidah Fiqhiyyah: Sarana Penyempurna Kewajiban Menjadi Wajib",
        "description": "Prinsip ushul fiqih: apa yang menjadi prasyarat mutlak bagi kewajiban, maka hukumnya ikut menjadi wajib.",
        "tags": ["DalilSyar'i", "KaidahFiqih", "UshulFiqih", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Al-Ghazali, Al-Mustashfa, hlm. 68; Al-Amidi, Al-Ihkam fi Ushulil Ahkam, 1/158"
        ],
        "matan": "« مَا لَا يَتِمُّ الْوَاجِبُ إِلَّا بِهِ فَهُوَ وَاجِبٌ »",
        "terjemahan": "Sesuatu yang tanpanya suatu kewajiban tidak dapat terlaksana sempurna, maka sesuatu itu hukumnya menjadi wajib.",
        "takhrij": "Kaidah Ushul Fiqih fundamental mu'tabar.",
        "syarah": "Imam Al-Ghazali menjelaskan bahwa kewajiban mencakup seluruh wasilah (sarana) yang menjadi syarat tercapainya tujuan syariat tersebut.",
        "analisis": "Pembinaan ketahanan mental dan tazkiyatun nafs bagi guru adalah prasyarat terselenggaranya KBM beradab; maka alokasi waktu pembinaan guru hukumnya wajib.",
        "related": ["Prioritasi Program Lembaga Berbasis Maqashid Syariah", "Peran Guru dan Lembaga Pendidikan"]
    },
    "dalil-kaidah-ma-la-yudrak": {
        "title": "Kaidah Fiqhiyyah: Apa yang Tidak Tercapai Seluruhnya Jangan Ditinggal Seluruhnya",
        "description": "Prinsip ushul fiqih kemudahan dan realistis: pencapaian sebagian maslahat lebih baik daripada meninggalkannya total.",
        "tags": ["DalilSyar'i", "KaidahFiqih", "Tadarruj", "PendidikanKarakterNabawiyah"],
        "sources": [
            "As-Suyuthi, Al-Asybah wan Nazha'ir, hlm. 159"
        ],
        "matan": "« مَا لَا يُدْرَكُ كُلُّهُ لَا يُتْرَكُ جُلُّهُ »",
        "terjemahan": "Apa yang tidak dapat dicapai seluruhnya, janganlah ditinggalkan sebagian besarnya (yang masih mampu dilakukan).",
        "takhrij": "Kaidah Fiqhiyyah Furuiyyah yang masyhur di kalangan fuqaha.",
        "syarah": "Kaidah ini melarang keputusasaan perfeksinis. Keterbatasan kemampuan tidak boleh menjadi alasan untuk menghentikan amal kebaikan yang sanggup dikerjakan.",
        "analisis": "Implementasi PKN yang bertahap: jika sebuah keluarga/sekolah belum mampu menerapkan seluruh standar ideal, mulailah dari pembiasaan adab yang termudah.",
        "related": ["Prinsip Tadarruj", "Kaidah Implementasi di Berbagai Lembaga"]
    },
    "dalil-qs-7-31": {
        "title": "QS. Al-A'raf: 31 — Keseimbangan Berhias dan Larangan Berlebih-lebihan",
        "description": "Nas dan tafsir QS. Al-A'raf ayat 31 mengenai perintah menjaga keseimbangan hidup dan larangan israf.",
        "tags": ["DalilSyar'i", "AlQuran", "Tafsir", "PendidikanKarakterNabawiyah"],
        "sources": [
            "QS. Al-A'raf [7]: 31",
            "Tafsir Ibnu Katsir, 3/405"
        ],
        "matan": "« يَا بَنِي آدَمَ خُذُوا زِينَتَكُمْ عِندَ كُلِّ مَسْجِدٍ وَكُلُوا وَاشْرَبُوا وَلَا تُسْرِفُوا ۚ إِنَّهُ لَا يُحِبُّ الْمُسْرِفِينَ »",
        "terjemahan": "Wahai anak cucu Adam! Pakailah pakaianmu yang bagus pada setiap (memasuki) masjid, makan dan minumlah, tetapi jangan berlebih-lebihan. Sungguh, Allah tidak menyukai orang-orang yang berlebih-lebihan.",
        "takhrij": "QS. Al-A'raf [7]: 31.",
        "syarah": "Ibnu Katsir menjelaskan bahwa ayat ini menetapkan etika berpakaian rapi dan adab makan-minum yang proporsional tanpa terjerumus pada sifat boros dan sombong.",
        "analisis": "Pengelolaan program lembaga PKN: mengutamakan fungsi esensial daripada seremonial mewah yang membebani wali santri.",
        "related": ["Prioritasi Program Lembaga Berbasis Maqashid Syariah", "Master Katalog Dalil Al-Quran"]
    },
    "dalil-syathibi-tahsiniyyat": {
        "title": "Kaidah Asy-Syathibi: Batasan Tahsiniyyat yang Membatalkan Asal",
        "description": "Kaidah Maqashid Syariah Imam Asy-Syathibi mengenai perkara pelengkap yang berakibat membatalkan perkara pokok.",
        "tags": ["DalilSyar'i", "MaqashidSyariah", "KaidahFiqih", "PendidikanKarakterNabawiyah"],
        "sources": [
            "Imam Asy-Syathibi, Al-Muwafaqat fi Ushulisy Syari'ah, 2/20"
        ],
        "matan": "« كُلُّ تَحْسِينِيٍّ يَعُودُ عَلَى أَصْلِهِ بِالْإِبْطَالِ فَلَا يَصِحُّ اعْتِبَارُهُ »",
        "terjemahan": "Setiap perkara pelengkap/penyempurna (tahsiniyyat) yang berakibat pada pembatalan hukum pokoknya (dharuriyyat), maka gugurlah keabsahannya.",
        "takhrij": "Kaidah Maqashid Syariah karya Imam Abu Ishaq Asy-Syathibi.",
        "syarah": "Asy-Syathibi memaparkan bahwa unsur pelengkap bertujuan memperindah dan menyempurnakan hal pokok. Manakala perhiasan tersebut merusak intinya, ia harus disingkirkan.",
        "analisis": "Program seremonial (tahsiniyyat) seperti wisuda mewah atau panggung megah yang menekan ekonomi orang tua miskin tertolak secara syar'i.",
        "related": ["Prioritasi Program Lembaga Berbasis Maqashid Syariah", "dalil-kaidah-darul-mafasid"]
    }
}

content_dalil_dir = "/home/abuhafi/Project/wiki-pkn/content/Dalil"

created = 0
for slug, data in DALIL_PAGES.items():
    file_path = os.path.join(content_dalil_dir, f"{slug}.md")
    
    tags_str = "\n".join(f"  - {t}" for t in data["tags"])
    sources_str = "\n".join(f'  - reference: "{s}"' for s in data["sources"])
    related_links = "\n".join(f"- [[{r}]]" for r in data["related"])
    
    content = f"""---
title: "{data['title']}"
description: "{data['description']}"
tags:
{tags_str}
sources:
{sources_str}
---

# {data['title']}

> [!summary] Ringkasan & Kaidah Penerapan PKN
> {data['analisis']}

---

## 1. Nas dan Takhrij

> [!quote] Nas Dalil Rujukan
> {data['matan']}
> 
> **Terjemahan kerja Indonesia:**
> *"{data['terjemahan']}"*
> 
> 📚 **Takhrij Sumber:** {data['takhrij']}

---

## 2. Syarah Ulama Salaf & Faedah Fiqih

> [!quote] Kutipan Penjelasan Ulama Mu'tabar
> {data['syarah']}

---

## 3. Integrasi Pedagogis & Relevansi Manhaj PKN

{data['analisis']}

---

## 4. Tautan Terkait

{related_links}
- [[Master Katalog Dalil Hadits dan Sunnah|Master Katalog Dalil Hadits dan Sunnah]]
- [[index|Beranda Utama Wiki PKN]]
"""
    with open(file_path, "w", encoding="utf-8") as fp:
        fp.write(content)
    created += 1

print(f"Sukses membangun {created} halaman dalil mandiri!")

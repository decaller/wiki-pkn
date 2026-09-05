#!/usr/bin/env python3
"""
enrich_etape_usia.py
Menambahkan subbab '## Penerapan Berdasarkan Etape Usia Nabawiyah' pada 16 artikel substantif
yang belum memilikinya, diselaraskan dengan verifikasi rujukan turats Qaf AI.
Strict rule: ZERO DELETION (hanya menyisipkan konten baru sebelum ## Tautan atau di akhir).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

ETAPE_SECTIONS = {
    "4 Kaidah Implementasi.md": """
## Penerapan 4 Kaidah Emas Berdasarkan Etape Usia Nabawiyah

Dalam kaidah fiqh tarbiyah Islam (*maraji': Tuhfatul Maudud karya Ibnul Qayyim*), penerapan 4 kaidah emas PKN harus mengikuti kematangan fitrah anak secara bertahap (*tadarruj*):

1. **Fase Thufulah (0–7 Tahun — Masa Kelekatan & Kelembutan Fitrah):**
   * **Fokus Kaidah:** Dominansi Kaidah 1 (Satu Anak Satu Kurikulum) dan Kaidah 3 (Mendidik dengan Keteladanan & Bahasa Hati).
   * **Praktek:** Anak belum memiliki nalar beban syariat (*khitab taklif*). Perlakukan dengan limpahan kasih sayang, bermain bersama, dan perlindungan total dari kata-kata kasar. Keteladanan adab orang tua diserap secara murni lewat pandangan mata (*al-muhakah*).
2. **Fase Tamyiz (7–10 Tahun — Pembiasaan Nalar & Pembentukan Adab):**
   * **Fokus Kaidah:** Kaidah 2 (Tadarruj / Bertahap) dan Kaidah 4 (Fokus Kekuatan Bakat).
   * **Praktek:** Masa pembiasaan shalat 3 tahun penuh (5.000+ waktu shalat) tanpa kekerasan fisik, melatih nalar sebab-akibat, dan menugaskan tanggung jawab harian di rumah yang menumbuhkan rasa percaya diri.
3. **Fase Murahaqah (10–15 Tahun — Pendisiplinan & Pemagangan Tanggung Jawab):**
   * **Fokus Kaidah:** Penegakan batas syariat yang tegas namun adil (*Kaidah Wasathiyah*).
   * **Praktek:** Pemisahan tempat tidur (*tafriq fil madhaji'*), sanksi edukatif tanpa mempermalukan di depan umum, serta pemagangan proyek nyata untuk menguji ketangguhan karakter dan bakat kepemimpinannya.
4. **Fase Syabab (15+ Tahun — Kemitraan Menuju Aqil-Baligh & Karya Peradaban):**
   * **Fokus Kaidah:** Transformasi hubungan dari figur otoritas menjadi sahabat kemitraan sejati (*Ukhuwwah & Syuraka'*).
   * **Praktek:** Anak telah memikul hisab syar'i (*mukallaf*). Dilibatkan dalam musyawarah keluarga, pengelolaan finansial mandiri, dan penyaluran bakat untuk kemaslahatan ummah.
""",

    "Kaidah Implementasi di Berbagai Lembaga.md": """
## Penerapan Kaidah Lembaga Berdasarkan Etape Usia Nabawiyah

Lembaga pendidikan Islam (PAUD/TK, SD/Madrasah Ibtidaiyah, SMP/Pesantren, hingga SMA/Aliyah) wajib mengadaptasi desain kurikulum berbasis etape usia nabawi (*maraji': Al-Fatawa al-Kubra Ibnu Taimiyah & Ihya Ulumiddin Al-Ghazali*):

1. **Jenjang PAUD/TK (Fase Thufulah 0–7 Tahun):**
   * Bebas dari target calistung kaku dan beban ujian akademik; sekolah adalah taman bermain alami yang merawat fitrah keimanan dan kebahagiaan belajar.
2. **Jenjang SD / MI (Fase Tamyiz 7–10 Tahun):**
   * Fokus pada pembiasaan ibadah praktis, adab pergaulan islami, dan observasi minat-bakat melalui eksplorasi alam terbuka tanpa rangking kelas komparatif.
3. **Jenjang SMP / MTs / Pesantren Awal (Fase Murahaqah 10–15 Tahun):**
   * Penegakan disiplin adab berasrama, program mentoring bakat terarah, dan latihan tanggung jawab sosial (khidmah santri).
4. **Jenjang SMA / MA / Mahad Aly (Fase Syabab 15+ Tahun):**
   * Pemagangan profesional, inkubasi karya kemandirian umat, dan pembekalan fiqh dakwah peradaban.
""",

    "Peran Guru dan Lembaga Pendidikan.md": """
## Penerapan Peran Guru Berdasarkan Etape Usia Nabawiyah

Guru sebagai murabbi ruhani (*maraji': Al-Adab al-Mufrad Al-Bukhari & Risalah al-Mu'allimin karya Sahnun*) mengemban peran spesifik pada tiap etape santri:

1. **Guru Fase Thufulah (0–7 Tahun):** Berperan sebagai figur pengganti ibu (*ummun muthabbiqah*), menyiram cinta, memeluk, dan menuntun doa dengan riang gembira.
2. **Guru Fase Tamyiz (7–10 Tahun):** Berperan sebagai teladan adab (*uswatun hasanah*), mengurai alasan logis di balik perintah syariat, dan melatih kemandirian tanpa mencela kekurangan anak.
3. **Guru Fase Murahaqah (10–15 Tahun):** Berperan sebagai mentor kepemimpinan (*mu'addib wa musyir*), berdialog tentang gejolak syahwat, dan menjaga benteng pergaulan santri.
4. **Guru Fase Syabab (15+ Tahun):** Berperan sebagai rekan diskusi intelektual (*syarik fikri*), membimbing karya riset peradaban, dan mendoakan keberkahan dakwah murid di malam hari.
""",

    "Tanggung Jawab Pendidikan.md": """
## Pembagian Tanggung Jawab Pendidikan Lintas Etape Usia

Berdasarkan konsensus fuqaha (*maraji': Al-Mawsu'ah al-Fiqhiyyah al-Kuwaitiyyah & Tuhfatul Maudud*), tanggung jawab nafkah, pengasuhan (*hadhanah*), dan pengajaran (*ta'dib*) bergeser secara harmonis:

1. **Etape Thufulah (0–7 Tahun):** Hak mutlak kelekatan ibu dalam hadhanah; ayah menjamin nafkah halal dan stabilitas ketenangan rumah tangga.
2. **Etape Tamyiz (7–10 Tahun):** Ayah mulai memimpin edukasi ibadah shalat dan memantau interaksi sosial; ibu mendampingi kebiasaan adab harian.
3. **Etape Murahaqah (10–15 Tahun):** Ayah mengawal penegakan batasan hukum (*hudud*) dan melatih ketangguhan mental anak; ibu menjadi tempat mencurahkan gejolak emosi.
4. **Etape Syabab (15+ Tahun):** Orang tua beralih peran sebagai dewan penasihat (*syura*); anak dilatih menanggung konsekuensi hukum dan finansial pribadinya.
""",

    "Peran & Tanggung Jawab/index.md": """
## Peta Sinergi Peran & Tanggung Jawab Lintas Etape Usia

Sinergi tripartit (Ayah, Bunda, Guru) bergerak dinamis mengikuti kurva kematangan fitrah anak:

1. **Fase Thufulah (0–7 Tahun):** Bunda 70% (kehangatan hadhanah), Ayah 30% (proteksi & pilar visi), Guru sebagai fasilitator bermain.
2. **Fase Tamyiz (7–10 Tahun):** Keseimbangan Ayah-Bunda 50%-50% dalam pembiasaan adab shalat; Guru sebagai mitra pembentukan etika belajar.
3. **Fase Murahaqah (10–15 Tahun):** Ayah 60% (penegakan prinsip & mentoring maskulinitas/feminitas), Bunda 40% (penjaga kehangatan batin), Guru sebagai pembimbing bakat.
4. **Fase Syabab (15+ Tahun):** Kemitraan tripartit penuh untuk mengantarkan anak mandiri memikul beban taklif dan dakwah.
""",

    "Implementasi/index.md": """
## Alur Implementasi Kurikulum PKN Berdasarkan 4 Etape Usia

Implementasi kurikulum PKN di lapangan bergerak linear namun fleksibel mengikuti 4 etape penciptaan:

1. **Etape Thufulah (Taman Fitrah 0–7 Th):** Penanaman cinta kepada Allah dan Rasul-Nya melalui keindahan ciptaan-Nya; bebas dari tekanan hafalan tanpa makna.
2. **Etape Tamyiz (Sekolah Adab 7–10 Th):** Penguatan rukun iman, tata cara ibadah bersuci dan shalat, serta penjelajahan sifat-sifat bakat dominan.
3. **Etape Murahaqah (Kawah Kepemimpinan 10–15 Th):** Pengasahan keterampilan spesifik, latihan kerja nyata, dan pembentengan syahwat serta muru'ah.
4. **Etape Syabab (Akademi Mandiri 15+ Th):** Integrasi ilmu syar'i dan kepakaran duniawi untuk melahirkan karya monumental penopang kejayaan umat.
""",

    "Pembagian Jiwa/Ammarah.md": """
## Penjinakan Jiwa Ammarah Berdasarkan Etape Usia Nabawiyah

Sifat primitif nafsu ammarah (*maraji': Ihya Ulumiddin karya Al-Ghazali & Majallat al-Bayan*) bermutasi seiring pertambahan usia anak dan menuntut pendekatan kuratif yang berbeda:

1. **Ammarah Fase Thufulah (0–7 Tahun):**
   * *Bentuk Gejala:* Tantrum, menangis bergulingan saat mainan direbut, memukul tanpa nalar.
   * *Terapi Nabawi:* Dekap dengan tenang (*holding therapy*), alihkan perhatian pada objek lain, jangan dipukul atau dibentak karena akal tamyiznya belum mekar.
2. **Ammarah Fase Tamyiz (7–10 Tahun):**
   * *Bentuk Gejala:* Berbohong untuk membela diri, egois enggan berbagi, membantah nasihat ringan.
   * *Terapi Nabawi:* Ajak dialog nalar sebab-akibat saat emosi reda, latih puasa sunnah bertahap untuk mengekang syahwat konsumtif, dan ajarkan istighfar.
3. **Ammarah Fase Murahaqah (10–15 Tahun):**
   * *Bentuk Gejala:* Memberontak terhadap aturan rumah, kecanduan gawai secara sembunyi-sembunyi, agresivitas fisik.
   * *Terapi Nabawi:* Salurkan energi fisik ke dalam olahraga sunnah berkeringat (panahan, bela diri, berenang), beri tanggung jawab proyek menantang, tegakkan konsekuensi logis yang disepakati bersama.
4. **Ammarah Fase Syabab (15+ Tahun):**
   * *Bentuk Gejala:* Tergoda syahwat pornografi, hedonisme pergaulan bebas, kesombongan intelektual.
   * *Terapi Nabawi:* Bimbingan shaum Dawud/Senin-Kamis, tazkiyatun nafs terstruktur, serta dorongan segera menikah jika sudah berkemampuan (*al-ba'ah*).
""",

    "Benang Merah Pendidikan.md": """
## Penerapan Benang Merah Pendidikan Berdasarkan Etape Usia

Prinsip benang merah (Tauhid $\rightarrow$ Adab $\rightarrow$ Ilmu $\rightarrow$ Amal) diterapkan berkesinambungan lintas etape:

1. **Thufulah (0–7 Th):** Benang Tauhid dianyam lewat pengenalan asma Allah yang Maha Pengasih di alam raya.
2. **Tamyiz (7–10 Th):** Benang Adab ditegakkan melalui penghormatan kepada orang tua, guru, dan adab thalabul ilmi.
3. **Murahaqah (10–15 Th):** Benang Ilmu & Bakat diasah untuk menguasai kompetensi nyata yang bermanfaat bagi sesama.
4. **Syabab (15+ Th):** Benang Kesadaran Beramal mekar menjadi amal jariyah dan peran kepemimpinan peradaban.
""",

    "Luka dan Hutang Pengasuhan/Recovery.md": """
## Protokol Pemulihan (Recovery) Berdasarkan Etape Usia

Waktu intervensi pemulihan luka pengasuhan menentukan kecepatan restorasi fitrah (*maraji': Fatawa al-Shabaka al-Islamiyya*):

1. **Recovery pada Etape Thufulah (0–7 Th):**
   * Sangat cepat pulih (hitungan pekan) cukup dengan kehadiran fisik orang tua yang hangat, tatapan mata penuh kasih, dan pelukan harian 8 kali.
2. **Recovery pada Etape Tamyiz (7–10 Th):**
   * Memerlukan rekonstruksi dialog, permohonan maaf tulus dari ayah/bunda atas kekasaran masa lalu, dan pemberian ruang validasi emosi.
3. **Recovery pada Etape Murahaqah (10–15 Th):**
   * Membutuhkan figur ketiga (mentor/guru bijak) jika komunikasi orang tua-anak mengalami kebuntuan (*blocking*), disertai pembersihan residu trauma perundungan.
4. **Recovery pada Etape Syabab (15+ Th):**
   * Bersifat muhasabah mandiri (*self-recovery*), pemahaman qada dan qadar, serta memutus mata rantai pengasuhan toksik (*toxic parenting*) melalui tazkiyatun nafs intensif.
""",

    "Pendidikan Ideal/index.md": """
## Arsitektur Pendidikan Ideal Berdasarkan 4 Etape Usia

Pendidikan ideal adalah pendidikan yang tunduk pada tahapan fitrah penciptaan, bukan ambisi kurikulum manusia:

1. **Etape Thufulah (0–7 Th):** Rumah cinta dan kelekatan; bermain adalah sarana belajar terbaik.
2. **Etape Tamyiz (7–10 Th):** Sekolah dasar kehidupan; pembiasaan shalat, adab bertutur, dan penemuan bakat.
3. **Etape Murahaqah (10–15 Th):** Ma'had tarbiyah dan pemagangan; penempaan daya juang (*adversity quotient*) dan ketahanan syahwat.
4. **Etape Syabab (15+ Th):** Universitas peradaban; kemandirian karya, penegakan sunnah, dan pembinaan keluarga sakinah.
""",

    "Renungan/Hak dan Kewajiban.md": """
## Penyelarasan Hak dan Kewajiban Berdasarkan Etape Usia

Keadilan syariat tampak pada proporsi perimbangan antara hak dan kewajiban anak (*maraji': Al-Mawsu'ah al-Fiqhiyyah al-Kuwaitiyyah*):

1. **Thufulah (0–7 Th):** Hak 100%, Kewajiban 0%. Anak berhak atas perlindungan, kasih sayang, nafkah, dan imunisasi fitrah tanpa tuntutan hisab.
2. **Tamyiz (7–10 Th):** Hak 80%, Kewajiban 20%. Anak mulai dilatih memikul kewajiban adab dan ibadah ringan secara sukarela.
3. **Murahaqah (10–15 Th):** Hak 50%, Kewajiban 50%. Kewajiban syariat ditegakkan seimbang dengan hak pembimbingan dan apresiasi karya.
4. **Syabab (15+ Th):** Kewajiban Penuh (*Mukallaf*). Hak beralih menjadi tanggung jawab memberi kontribusi bagi orang tua dan umat.
""",

    "Renungan/index.md": """
## Muhasabah Perjalanan Mendidik di Tiap Etape Usia

Setiap etape usia anak adalah amanah tak berulang yang menuntut perenungan mendalam:

1. **Renungan Etape Thufulah:** Apakah kita telah memberikan tatapan mata penuh kehangatan, ataukah kita telah mencuri masa kecil mereka dengan layar gawai dingin?
2. **Renungan Etape Tamyiz:** Apakah kita mendidik shalat dengan cinta keteladanan, atau sekadar ancaman marah yang membuat mereka menjauhi masjid?
3. **Renungan Etape Murahaqah:** Apakah kita menjadi teman bicara yang aman saat badai pubertas datang, atau hakim yang selalu memvonis salah?
4. **Renungan Etape Syabab:** Sudahkah kita melepaskan mereka menjadi rajawali peradaban yang mandiri di hadapan Allah?
""",

    "Implementasi/Internal & Eksternal/Tawakkal dan Doa.md": """
## Orientasi Doa dan Tawakkal Sesuai Etape Perkembangan Anak

Doa orang tua adalah senjata utama tarbiyah (*maraji': Al-Adzkar karya Imam An-Nawawi*), dengan fokus munajat yang berganti sesuai etape:

1. **Doa Etape Thufulah:** Memohon perlindungan fitrah dari gangguan setan (*U'idzukuma bi kalimaatillaahit taammah*) dan kesehatan jasad.
2. **Doa Etape Tamyiz:** Memohon agar anak dicintai keimanan dan dihiasi keindahan shalat (*Rabbij'alni muqiimash shalaati wa min dzurriyyati*).
3. **Doa Etape Murahaqah:** Memohon kesucian diri, penjagaan dari fitnah syahwat, dan diteguhkan dalam ketaatan (*Allahumma inni as'alukal huda wat tuqa wal 'afafa wal ghina*).
4. **Doa Etape Syabab:** Memohon keturunan yang menjadi penyejuk pandangan dan imam bagi orang-orang bertakwa (*Qurrata a'yunin waj'alna lil muttaqiina imaama*).
""",

    "Insight & Teknis/Insight/SOTABH.md": """
## Penerapan SOTAB HEBAT Berdasarkan Etape Usia Nabawiyah

Observasi bakat SOTABH (*Sifat, Observasi, Temu Bakat HEBAT*) mengikuti tahapan kematangan fitrah:

1. **Fase Thufulah (0–7 Th):** Eksplorasi bebas tanpa asesmen formal; orang tua mencatat kecenderungan gerak dan respon sensorik alami anak.
2. **Fase Tamyiz (7–10 Th):** Pengamatan Rukun 3A (*Suka, Bisa, Bermanfaat*) dalam aktivitas harian dan penugasan proyek mini kelompok.
3. **Fase Murahaqah (10–15 Th):** Pengisian Kuisioner 40 Bakat Nabawiyah (TB-40), validasi silang antara penilaian mandiri dan observasi mentor.
4. **Fase Syabab (15+ Th):** Portofolio karya bakat nyata, magang profesional sesuai bakat dominan, dan kontribusi solusi bagi problem umat.
""",

    "Pendidikan Ideal/Imunitas Sosial.md": """
## Pembentukan Imunitas Sosial Berdasarkan Etape Usia Nabawiyah

Membangun imunitas dari polusi lingkungan jahiliyah modern membutuhkan tahapan terstruktur:

1. **Etape Thufulah (0–7 Th — Proteksi Steril):** Mengisolasi anak dari paparan gawai bebas, konten kekerasan, dan bahasa kotor; lingkungan rumah menjadi benteng steril.
2. **Etape Tamyiz (7–10 Th — Vaksinasi Nalar):** Mengenalkan realitas sosial secara terbimbing, melatih anak membedakan mana adab terpuji dan mana perilaku tercela di lingkungannya.
3. **Etape Murahaqah (10–15 Th — Latihan Kekebalan di Medan Nyata):** Melatih ketahanan mental terhadap tekanan teman sebaya (*peer pressure*), membangun identitas diri yang bangga dengan syariat Islam.
4. **Etape Syabab (15+ Th — Agen Imunitas Peradaban):** Anak bukan lagi sekadar kebal dari maksiat, melainkan menjadi pembawa obat bagi kerusakan masyarakat (*muslih*).
""",

    "Pendidikan Ideal/Luka dan Hutang Pengasuhan/Euforia.md": """
## Mencegah Racun Euforia Semu Berdasarkan Etape Usia

Euforia piala dan pujian palsu (*maraji': Dzammul Jahi wal Riya' karya Al-Ghazali*) merusak keikhlasan di tiap jenjang usia:

1. **Etape Thufulah (0–7 Th):** Hindari mengikutsertakan balita dalam kontes lomba kecantikan atau kelucuan komersial yang merusak kemurnian fitrahnya.
2. **Etape Tamyiz (7–10 Th):** Puji proses kerja keras dan kejujurannya (*Al-Itqan*), bukan hasil angka rapor atau piala yang memicu riya' dan kesombongan.
3. **Etape Murahaqah (10–15 Th):** Bimbing anak agar tidak haus validasi (*like & followers*) di media sosial; tanamkan kebanggaan pada amal sembunyi-sembunyi.
4. **Etape Syabab (15+ Th):** Tautkan karya prestasi dengan niat lillahi ta'ala dan kemaslahatan akhirat, membebaskan jiwa dari jebakan pujian manusia.
"""
}

def insert_before_links(content, section_text):
    patterns = [
        r"(##\s+(?:[0-9]+\.\s+)?Tautan[^\n]*)",
        r"(##\s+(?:[0-9]+\.\s+)?Peta Konsep[^\n]*)",
        r"(##\s+(?:[0-9]+\.\s+)?Referensi[^\n]*)",
    ]
    for pat in patterns:
        m = re.search(pat, content, re.IGNORECASE)
        if m:
            idx = m.start()
            return content[:idx] + section_text.strip() + "\n\n---\n\n" + content[idx:]
    return content.rstrip() + "\n\n---\n\n" + section_text.strip() + "\n"

def main():
    print("Menambahkan Etape Usia Nabawiyah pada 16 artikel substantif...")
    count = 0
    for file_key, section_text in ETAPE_SECTIONS.items():
        matched_files = list(CONTENT_DIR.rglob(file_key))
        if not matched_files:
            print(f"[WARN] File tidak ditemukan: {file_key}")
            continue
        target_file = matched_files[0]
        content = target_file.read_text(encoding="utf-8")
        
        # Cek jika sudah ada
        if "## Penerapan Berdasarkan Etape Usia" in content or "## Penerapan 4 Kaidah Emas Berdasarkan Etape Usia" in content or "## Penerapan Kaidah Lembaga Berdasarkan Etape Usia" in content or "## Penerapan Peran Guru Berdasarkan Etape Usia" in content or "## Pembagian Tanggung Jawab Pendidikan Lintas Etape" in content or "## Peta Sinergi Peran & Tanggung Jawab Lintas Etape" in content or "## Alur Implementasi Kurikulum PKN Berdasarkan 4 Etape" in content or "## Penjinakan Jiwa Ammarah Berdasarkan Etape Usia" in content or "## Penerapan Benang Merah Pendidikan Berdasarkan Etape" in content or "## Protokol Pemulihan (Recovery) Berdasarkan Etape Usia" in content or "## Arsitektur Pendidikan Ideal Berdasarkan 4 Etape" in content or "## Penyelarasan Hak dan Kewajiban Berdasarkan Etape" in content or "## Muhasabah Perjalanan Mendidik di Tiap Etape" in content or "## Orientasi Doa dan Tawakkal Sesuai Etape" in content or "## Penerapan SOTAB HEBAT Berdasarkan Etape" in content or "## Pembentukan Imunitas Sosial Berdasarkan Etape" in content or "## Mencegah Racun Euforia Semu Berdasarkan Etape" in content:
            print(f"[SKIP] Sudah ada etape usia di {file_key}")
            continue
            
        new_content = insert_before_links(content, section_text)
        target_file.write_text(new_content, encoding="utf-8")
        print(f"[UPDATED] {file_key} (+Etape Usia)")
        count += 1
        
    print(f"\nSelesai: {count} artikel berhasil diperkaya dengan Etape Usia Nabawiyah!")

if __name__ == "__main__":
    main()

# scripts/integrate_official_docs.py
"""
Integrates insights from official docs:
- old_backup/official_docs/Panduan Implementasi Standar PKN (A4).docx
- old_backup/official_docs/Menumbuhkan Kesadaran Beramal (E-book).docx
- old_backup/Kaidah Implementasi PKN dalam berbagai Lembaga.md

Actions:
1. Create content/.../Implementasi/Kaidah Implementasi di Berbagai Lembaga.md
2. Enrich Peran Guru dan Lembaga Pendidikan.md
3. Enrich Benang Merah Pendidikan.md
4. Enrich Syabab.md
5. Enrich Recovery.md
6. Update Implementasi.md & index.md navigation
"""

import os

BASE_DIR = '/home/abuhafi/Project/wiki-pkn'

# =============================================================================
# 1. NEW ARTICLE: Kaidah Implementasi di Berbagai Lembaga.md
# =============================================================================

KAIDAH_LEMBAGA_CONTENT = """---
title: "Kaidah Implementasi PKN dalam Berbagai Lembaga"
tags:
  - pkn
  - implementasi_lembaga
  - sekolah_islam
  - pesantren
  - kaidah_ushul
  - manajemen_sekolah
---

# Kaidah Implementasi PKN dalam Berbagai Lembaga

Penerapan kurikulum Pendidikan Karakter Nabawiyah (PKN) pada institusi pendidikan formal maupun non-formal—seperti Sekolah Islam Terpadu (SIT), Madrasah, Pondok Pesantren/Ma'had, hingga Komunitas Homeschooling—memiliki dinamika tantangan yang berbeda dengan penerapan di ranah domestik keluarga. Lembaga pendidikan melibatkan banyak pemangku kepentingan (*stakeholders*): yayasan pemilik modal, dewan guru senior, kurikulum dinas pemerintah, ekspektasi orang tua wali santri, hingga budaya birokrasi yang telah mengakar puluhan tahun.

Para perumus manhaj PKN (Ustadz Abdul Kholiq dan Bayu Issetyadi) dalam dokumen resmi *Panduan Implementasi Standar PKN pada Lembaga Pendidikan Islam* menegaskan bahwa peralihan menuju sistem nabawiyah tidak boleh dilakukan secara serampangan, emosional, atau revolusioner frontal. Pengelola lembaga wajib mengadopsi **5 Kaidah Emas Strategi Adopsi** yang berakar kuat pada kaidah ushul fiqih Islam, didukung oleh **4 Tingkatan Evolusi Kelembagaan**.

> [!quote] Dalil & Rujukan Nabawiyah: Menolak Kerusakan dan Memulai dari yang Mampu
> **Kaidah Ushul Fiqih & Hadits Shahih:**  
> « دَرْءُ الْمَفَاسِدِ مُقَدَّمٌ عَلَى جَلْبِ الْمَصَالِحِ »  
> *"Menolak kerusakan dan bahaya (mafsadat) harus didahulukan daripada mengejar kemaslahatan."*  
> — **Kaidah Fiqhiyyah Kubra (As-Suyuthi dalam Al-Asybah wan Nazha'ir Hal. 87)**  
>  
> « ابْدَأْ بِنَفْسِكَ ثُمَّ بِمَنْ تَعُولُ »  
> *"Mulailah dari dirimu sendiri, kemudian kepada orang-orang yang menjadi tanggunganmu."*  
> — **HR. Muslim (No. 997) dari Jabir bin Abdillah radhiyallahu 'anhu**  
>  
> « مَا نَهَيْتُكُمْ عَنْهُ فَاجْتَنِبُوهُ، وَمَا أَمَرْتُكُمْ بِهِ فَأْتُوا مِنْهُ مَا اسْتَطَعْتُمْ »  
> *"Apa saja yang aku larang bagi kalian maka jauhilah, dan apa saja yang aku perintahkan kepada kalian maka laksanakanlah semampu kalian."*  
> — **HR. Bukhari (No. 7288) & Muslim (No. 1337)**  
>  
> 📚 **Relevansi PKN:** Kaidah-kaidah ini menjadi rem spiritual sekaligus panduan taktis bagi kepala sekolah dan mudir pesantren: jangan sampai ambisi menerapkan sistem ideal nabawiyah justru memicu perpecahan yayasan, penolakan massal guru, atau kebangkrutan operasional lembaga.

---

## 1. Lima Kaidah Emas Implementasi di Lembaga

Berdasarkan dokumen master *Kaidah Implementasi PKN dalam Berbagai Lembaga*, terdapat 5 pilar navigasi kebijakan:

```mermaid
graph TD
    K1["1. Mulai Dari Pribadi<br/>(Ibda' Binafsik)"] --> K2["2. Utamakan Hindari Mudhorot<br/>(Dar'ul Mafasid)"]
    K2 --> K3["3. Mulai Dari yang Mudah & Tidak Ideal<br/>(Ma La Yudraku Kulluh)"]
    K3 --> K4["4. Pilih Mudhorot yang Terkecil<br/>(Irtikabu Akhaffidh Dhararain)"]
    K4 --> K5["5. Sesuaikan Ekspektasi<br/>(Tadarruj & Sabar Proses)"]
    K5 --> Sukses["Keberlanjutan Dakwah Pendidikan Nabawiyah"]
```

### 1. Mulai Dari Pribadi (*Ibda' Binafsik*)
- **Prinsip:** Guru atau ustadz tidak perlu menunggu yayasan mengeluarkan Surat Keputusan (SK) resmi atau merombak kurikulum nasional untuk mulai mendidik secara nabawiyah.
- **Operasional di Kelas:** Mulailah dari diri sendiri di kelas yang kita ajar: menyapa murid dengan senyuman tulus, menghentikan bentakan dan ancaman nilai, menerapkan [[Bahasa Hati]], serta memuji proses usaha anak. Perubahan aura batin seorang guru akan memancar nyata dan menjadi argumen hidup yang paling meyakinkan bagi rekan-rekan sejawatnya.

### 2. Utamakan Menghindari Mudhorot (*Dar'ul Mafasid Muqaddamun 'ala Jalbil Mashalih*)
- **Prinsip:** Mencegah perpecahan, keresahan wali murid, atau konflik horizontal antar-guru jauh lebih didahulukan daripada memaksakan program baru yang belum dipahami oleh seluruh tim.
- **Operasional di Lembaga:** Jika kebijakan menghapus pekerjaan rumah (PR) atau meniadakan ujian tertulis akan memicu kepanikan massal wali murid yang belum teredukasi, jangan terapkan secara mendadak. Hindari mudharat hilangnya kepercayaan masyarakat terhadap lembaga dakwah.

### 3. Mulai Dari yang Mudah dan Tidak Ideal (*Mā Lā Yudraku Kulluh Lā Yutraku Julluh*)
- **Prinsip:** *“Apa yang tidak bisa diraih seluruhnya, jangan ditinggalkan sebagian besarnya.”* Tidak ada alasan untuk menunda penerapan PKN hanya karena sarana fisik sekolah belum ideal (misalnya belum memiliki gedung alam terbuka).
- **Operasional di Lembaga:** Mulailah dari langkah-langkah mikro yang mudah dan berbiaya nol:
  - Menyisipkan 15 menit *circle time* atau tadabbur ayat kauniyah sebelum jam pelajaran dimulai.
  - Membuka jam curhat pribadi antara musyrif asrama dengan santri binaannya.
  - Menghapus hukuman fisik yang merendahkan martabat murid (*restorasi adab*).

### 4. Pilih Mudhorot yang Terkecil (*Irtikabu Akhaffidh-Dhararain*)
- **Prinsip:** Tatkala lembaga dihadapkan pada dua pilihan dilematis yang sama-sama memiliki risiko negatif, pilihlah alternatif yang dampaknya paling ringan bagi integritas fitrah siswa.
- **Operasional di Lembaga:** Misalnya, lembaga wajib mematuhi target administrasi ujian kelulusan pemerintah agar ijazah santri diakui negara. Pilihlah mudharat administratif ini sembari meminimalisir dampaknya: ikuti ujian secara tertib, namun netralisir stres kognitif santri dengan suasana asrama yang penuh kasih sayang, olahraga sunnah, dan kepastian bahwa nilai ujian bukanlah tolok ukur kemuliaan mereka di hadapan Allah.

### 5. Sesuaikan Ekspektasi (*At-Tadarruj wa Mudaratun-Nas*)
- **Prinsip:** Menata ulang target keberhasilan; sadari bahwa mencetak generasi sekelas sahabat membutuhkan waktu belasan tahun. Jangan terjebak sindrom [[Euforia]] yang menuntut santri langsung berubah menjadi malaikat dalam tempo satu semester.
- **Operasional di Lembaga:** Bersabarlah terhadap proses adaptasi para pendidik dan anak. Rayakan setiap kemajuan 1% dalam adab dan hubungan batin, serta hindari frustrasi yang memicu keputusasaan manajemen.

---

## 2. Empat Tingkatan Evolusi Kelembagaan Menuju PKN

Dokumen *Panduan Implementasi Standar PKN pada Lembaga Pendidikan Islam* membagi etape adopsi ke dalam 4 tingkatan terukur:

| Tingkatan Adopsi | Ruang Lingkup Perubahan | Fokus Aksi Manajemen | Sasaran Utama |
|---|---|---|---|
| **Tingkat 1 (Awal)** | Individu Pendidik & Lingkaran Terdekat | Penyesuaian *mindset* pendidik, pembersihan niat (*tazkiyah*), penerapan Bahasa Cinta di jam mengajar mandiri. | Tidak mengubah sistem lembaga; membangun model percontohan mikro. |
| **Tingkat 2** | Antar-Pendidik & Kolaboratif | *Sharing* pemikiran dalam forum guru, kolaborasi informal, mengidentifikasi bakat santri via asesmen/firasat, memasukkan observasi alamiah. | Meluaskan pengaruh tanpa merombak struktur organisasi formal. |
| **Tingkat 3** | Kebijakan Parsial / Pilot Project | Mengambil kebijakan resmi pada area terbatas (misal: divisi asrama/pondok, divisi kesiswaan), meniadakan hukuman fisik, mengubah sistem apresiasi. | Menguji coba sistem baru pada kluster terkendali sebelum diterapkan menyeluruh. |
| **Tingkat 4 (Lanjut)** | Transformasi Holistik Berkelanjutan | Restrukturisasi total kurikulum: memadukan kurikulum fardhu 'ain wajib dengan portofolio 40 bakat pilihan, manajemen sarpras mandiri oleh santri. | Mewujudkan ekosistem madrasah nabawiyah mandiri yang berkesinambungan. |

---

## 3. Matriks Komparatif Penerapan di 3 Jenis Lembaga

Setiap tipologi lembaga memiliki medan perjuangan dan strategi penetrasi yang khas:

| Aspek Strategis | Sekolah Islam Formal (SDIT/SMPIT) | Pondok Pesantren / Ma'had Berasrama | Komunitas Homeschooling / PKBM |
|---|---|---|---|
| **Tantangan Terbesar** | Tuntutan kurikulum dinas, drill ujian nasional, dan ekspektasi ranking dari wali murid. | Budaya senioritas, beban hafalan quran target tinggi, potensi kelelahan fisik santri. | Konsistensi orang tua, keterbatasan fasilitas laboratorium/olahraga bersama. |
| **Titik Masuk Terbaik** | Integrasi pembelajaran alamiah dalam P5/ekskul, pelatihan bahasa cinta bagi wali kelas. | Menjadikan musyrif asrama sebagai figur ayah pengganti, restrukturisasi jam tidur dan gizi. | Desain kurikulum berbasis 40 pilar bakat unik anak, magang kerja langsung di dunia nyata. |
| **Kaidah Kunci yang Dipakai** | *Pilih Mudhorot Terkecil* (kompromi administrasi, fokus pada adab di kelas). | *Utamakan Hindari Mudhorot* (hapus perpeloncoan santri, hidupkan tangki cinta). | *Mulai Dari yang Mudah* (fleksibilitas penuh, fokus pada proyek minat anak). |

---

## 4. Standar Penjaminan Mutu Kelembagaan PKN

Berdasarkan klausul audit resmi, terdapat 6 standar penjaminan mutu kelembagaan yang wajib dievaluasi berkala:
1. **Standar Visi-Misi:** Menjadikan tauhid dan fungsi kekhalifahan sebagai kompas tertinggi seluruh program.
2. **Standar Perencanaan:** Menyediakan diferensiasi beban materi (*multi-leveling*) agar tidak ada siswa yang frustrasi akibat beban yang melampaui kapasitasnya.
3. **Standar Proses:** Menjamin urutan penumbuhan: Iman (Bahasa Cinta) → Belajar (Eksperimen Alam) → Bakat (Rukun 3A).
4. **Standar Pendewasaan (Akil-Baligh):** Membekali santri putra pemandirian finansial dan santriwati manajemen kerumahtanggaan.
5. **Standar Recovery:** Mengoperasionalkan protokol diagnosis hutang pengasuhan dan pemulihan luka batin santri.
6. **Standar SDM Pendidik:** Menugaskan guru sesuai potensi uniknya dan mengadakan sesi pembinaan batin (*self-recovery* pendidik).

> [!reflection] Lembar Evaluasi Pimpinan & Pengelola Lembaga
> - Apakah selama ini kita menuntut guru-guru kita menerapkan kelembutan kepada siswa, sementara manajemen yayasan memperlakukan para guru secara kaku, dingin, dan menekan?
> - Sudahkah lembaga kita menerapkan kaidah *Dar'ul Mafasid*—menjaga ukhuwah dan kehangatan ekosistem—sebelum memaksakan target-target program yang ambisius?

---

## Tautan Rujukan Terkait

* [[Peran Guru dan Lembaga Pendidikan]] — Kedudukan guru sebagai Waratsatul Anbiya' dan mitra komplementer orang tua.
* [[4 Kaidah Implementasi]] — Prinsip metodologis penumbuhan fitrah anak.
* [[Implementasi]] — Paradigma menyeluruh implementasi kurikulum PKN.
* [[Benang Merah Pendidikan]] — Kritik terhadap sistem schooling pabrik Prusia.
* [[Recovery]] — Penanganan kelembagaan terhadap ketidaksesuaian perkembangan santri.
"""

# =============================================================================
# 2. ENRICH Peran Guru dan Lembaga Pendidikan.md
# =============================================================================

PERAN_GURU_PATH = os.path.join(BASE_DIR, 'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Peran & Tanggung Jawab/Peran Guru dan Lembaga Pendidikan.md')

PERAN_GURU_ADDITION = """

---

## 4. Standar Mutu Kelembagaan & 4 Tingkatan Evolusi Sekolah PKN

Berdasarkan dokumen master *Panduan Implementasi Standar PKN pada Lembaga Pendidikan Islam* (Abdul Kholiq & Bayu Issetyadi), transformasi sekolah konvensional menuju madrasah nabawiyah dilakukan melalui **Empat Tingkatan Adopsi**:

```mermaid
graph LR
    T1["Tingkat 1: Mindset Pribadi<br/>Perbaikan Diri Pendidik di Kelas"] --> T2["Tingkat 2: Kolaborasi Sejawat<br/>Meluaskan Pengaruh & Asesmen Bakat"]
    T2 --> T3["Tingkat 3: Kebijakan Parsial<br/>Pilot Project Asrama/Kesiswaan Tanpa Hukuman"]
    T3 --> T4["Tingkat 4: Holistik Berkelanjutan<br/>Kurikulum Fardhu 'Ain & Pilihan Bakat Penuh"]
```

1. **Tingkat 1 (Menata Ulang Mindset Diri Sendiri):** Guru memulai dari perbaikan cara pandang terhadap fitrah anak. Menerapkan 5 Bahasa Cinta di jam pelajarannya sendiri tanpa menunggu persetujuan birokrasi yayasan.
2. **Tingkat 2 (Meluaskan Pengaruh tanpa Merubah Sistem):** Berbagi wawasan santai dengan rekan guru sejawat, mulai mengobservasi fadhilah dan 40 pilar [[Bakat]] siswa, serta menyisipkan rencana pembelajaran alamiah yang kontekstual.
3. **Tingkat 3 (Kebijakan untuk Ruang Lingkup Tertentu/Parsial):** Lembaga menetapkan kebijakan resmi pada divisi percontohan (misalnya bidang kesiswaan atau asrama) dengan **menghapus sanksi fisik/hukuman yang mempermalukan**, menggantinya dengan restitusi adab dan pendampingan musyrif berbasis cinta.
4. **Tingkat 4 (Implementasi Holistik & Menuju Sempurna):** Penyelarasan menyeluruh antara kurikulum materi wajib syariat (*fardhu 'ain*) dengan materi pilihan bakat fungsional, serta penyiapan kemandirian santri mukallaf sebelum lulus.

Untuk panduan mendalam mengenai 5 strategi ushul fiqih dalam mengelola konflik adopsi sistem di lembaga, rujuk panduan lengkap di:  
👉 **[[Kaidah Implementasi di Berbagai Lembaga]]**.
"""

# =============================================================================
# 3. ENRICH Benang Merah Pendidikan.md
# =============================================================================

BENANG_MERAH_PATH = os.path.join(BASE_DIR, 'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Benang Merah Pendidikan.md')

BENANG_MERAH_ADDITION = """

---

## 4. Grand Theory Kesadaran Beramal: Rantai Kausalitas 5 Tingkat

Berdasarkan naskah *Menumbuhkan Kesadaran Beramal* (Abdul Kholiq), kegagalan terbesar model schooling modern adalah **menuntut hasil akhir (Amal & Disiplin) secara instan melalui paksaan, ancaman nilai, atau iming-iming materiil**, melompati fondasi cinta dan kepercayaan batin.

Pendidikan Karakter Nabawiyah merumuskan **Pola Lima Tingkat Sebab Hadirnya Amal Sadar**:

```mermaid
graph TD
    L5["❤️ TINGKAT 5: PENGORBANAN & RAHMAH PENDIDIK<br/>Orang tua/guru mencurahkan kasih sayang murni, doa malam, dan pengorbanan waktu"]
    L4["🌟 TINGKAT 4: KEKAGUMAN TERHADAP FIGUR (USWAH HASANAH)<br/>Anak kagum, terpikat oleh akhlak pendidik, dan melahirkan Kepercayaan Penuh (Trust)"]
    L3["✨ TINGKAT 3: CINTA TERHADAP AKTIVITAS KEBAIKAN<br/>Anak mencintai shalat, belajar, dan adab karena mencintai sosok yang mengajarkannya"]
    L2["📖 TINGKAT 2: ILMU TENTANG FADHILAH AMAL<br/>Penjelasan hikmah dan ayat Al-Qur'an diserap dengan lapang dada tanpa resistensi"]
    L1["🎯 TINGKAT 1: NIAT & AMAL SHALIH MANDIRI<br/>Anak beramal dengan gembira, konsisten, dan memiliki integritas muraqabatullah tanpa perlu diawasi CCTV"]

    L5 --> L4
    L4 --> L3
    L3 --> L2
    L2 --> L1
```

### Metafora Agraris: Mendidik Layaknya Bertani
Rasulullah ﷺ menyabdakan perumpamaan agung tentang hati manusia dan ilmu:
> « مَثَلُ مَا بَعَثَنِي اللَّهُ بِهِ مِنَ الْهُدَى وَالْعِلْمِ كَمَثَلِ الْغَيْثِ الْكَثِيرِ أَصَابَ أَرْضًا... »  
> *"Perumpamaan petunjuk dan ilmu yang dengannya Allah mengutusku adalah bagaikan hujan lebat yang menyiram bumi..."*  
> — **HR. Bukhari (No. 79) dari Abu Musa Al-Asy'ari radhiyallahu 'anhu**

* **Tanah Subur:** Menyerap air dan menumbuhkan tanaman (analogi anak yang tangki cintanya penuh dan hatinya gembur menerima adab).
* **Tanah Keras:** Menampung air untuk kemanfaatan sesama.
* **Tanah Tandus/Batu Licin:** Menolak air dan membiarkannya mengalir sia-sia.

**Kaidah Agraris Nabawiyah:** Seorang petani bijak tidak akan pernah menabur pupuk dan benih di atas tanah yang kering berbatu. Jika anak membangkang, jangan jejali dengan ceramah panjang. Basahi dan gemburkan dahulu tanah hatinya dengan pelukan, pemaafan, dan pengorbanan kasih sayang.

---

## 5. Anatomy of Trust (Tujuh Pilar Kepercayaan Batin Anak)

Kesadaran beramal hanya akan bersemi di atas tanah **Kepercayaan Batin (*Trust*)** antara anak dan pendidik. Dokumen resmi PKN merumuskan 7 pilar pembangun kepercayaan:
1. **Boundaries (Batas yang Jelas):** Menegakkan aturan yang konsisten; anak merasa aman tatkala tahu mana zona halal dan zona haram.
2. **Reliability (Keandalan Sikap):** Orang tua menepati janji; perkataan selaras dengan perbuatan nyata.
3. **Accountability (Keberanian Mengakui Salah):** Pendidik berani meminta maaf secara ksatria tatkala keliru membentak anak.
4. **Vault (Menjaga Kerahasiaan):** Tidak menceritakan kelemahan atau aib anak kepada tetangga, keluarga besar, atau media sosial.
5. **Integrity (Integritas Nilai):** Memilih jalan kebenaran syariat daripada kenyamanan pragmatis.
6. **Non-Judgment (Tidak Menghakimi):** Mendengarkan keluh kesah anak dengan empati tanpa langsung mencap "kamu berdosa".
7. **Generosity (Kemurahan Prasangka):** Selalu berprasangka baik pada niat awal anak tatkala ia melakukan kekeliruan teknis.
"""

# =============================================================================
# 4. ENRICH Syabab.md
# =============================================================================

SYABAB_PATH = os.path.join(BASE_DIR, 'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Insan/Fitrah (Karakter)/Perkembangan/Syabab.md')

SYABAB_ADDITION = """

---

## 4. Standar Kurikulum Pendewasaan Lembaga: Pemandirian Putra & Putri

Berdasarkan klausul resmi *Standar Pendewasaan (Akil Baligh)* dalam *Panduan Implementasi Standar PKN*:

```mermaid
graph TD
    subgraph STANDAR_PENDEWASAAN["STANDAR KURIKULUM AKIL-BALIGH LEMBAGA"]
        Putra["SANTRI PUTRA (QAWWAMAH)<br/>1. Pemandirian Finansial & Bisnis Riil<br/>2. Pengelolaan Sarpras Ma'had Sendiri<br/>3. Magang Nyata (Apprenticeship)<br/>4. Kepemimpinan Lapangan & Bela Diri"]
        Putri["SANTRIWATI (RAHIMAH)<br/>1. Manajemen Kerumahtanggaan (Housekeeping)<br/>2. Kuliner Gizi Halalan Thayyiban<br/>3. Psikologi Pengasuhan & Karakter Anak<br/>4. Fiqih Kewanitaan & Adab Istri Sholihah"]
    end

    Putra --> Output["Generasi Syabab Mandiri & Siap Menikah Bertanggung Jawab"]
    Putri --> Output
```

1. **Pemandirian Finansial Santri Putra:**
   - Santri usia 15 tahun ke atas tidak lagi diperlakukan sebagai anak kecil yang sekadar meminta uang saku. Ma'had memfasilitasi unit usaha riil (pertanian, peternakan, percetakan, IT, perdagangan).
   - Pengelolaan operasional harian sekolah/pondok (kelistrikan, kebersihan sarana, perbaikan inventaris) didelegasikan kepada santri senior untuk melatih kepemilikan rasa tanggung jawab (*ownership*).
2. **Pemandirian Kerumahtanggaan Santriwati:**
   - Santriwati dibekali ilmu aplikatif tata laksana rumah tangga: tata kelola finansial domestik, keterampilan memasak sehat tanpa pengawet berbahaya, menjahit, pertolongan pertama kesehatan keluarga, serta psikologi perkembangan anak usia dini.
   - Program ini mencetak calon ibu peradaban yang bangga atas peran mulianya sebagai *Rabbatul Bait* (Ratu Rumah Tangga).
"""

# =============================================================================
# 5. ENRICH Recovery.md
# =============================================================================

RECOVERY_PATH = os.path.join(BASE_DIR, 'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Pendidikan Ideal/Luka dan Hutang Pengasuhan/Recovery.md')

RECOVERY_ADDITION = """

---

## 4. Matriks Diagnosis Kelembagaan: Penanganan 4 Tipe Hutang Pengasuhan

Dokumen resmi *Panduan Implementasi Standar PKN* menetapkan protokol pemilahan antara **Ketidaksesuaian Proses** (faktor kompetensi guru/kurikulum) dengan **Ketidaksesuaian Perkembangan Individu** (adanya hutang pengasuhan dari masa kecil):

| Tipe Kasus | Kondisi Karakter Santri | Diagnosis Hutang Pengasuhan | Protokol Intervensi Pemulihan (*Recovery*) |
|:---:|---|---|---|
| **Tipe 1** | Iman (✅), Belajar (✅), Bakat (❌) | Bakat unik dan minat karya belum teridentifikasi. | Lakukan asesmen bakat, berikan proyek pemandirian berbasis Rukun 3A (Suka, Bisa, Berguna), libatkan dalam magang lapangan. |
| **Tipe 2** | Iman (✅), Belajar (❌), Bakat (❌) | Nalar kritis dan kegembiraan belajar mati akibat schooling kaku. | Perbesar interaksi alam terbuka (*tadabbur*), bebaskan eksperimen mandiri (*trial & error*), hapus ketakutan terhadap nilai angka. |
| **Tipe 3** | Iman (❌), Belajar (✅), Bakat (✅) | Kering spiritualitas; taat hanya jika diawasi; tangki cinta bocor. | **Fokus Penuh pada Karakter Iman:** Hentikan sementara tuntutan beban hafalan/akademis; guyur dengan Bahasa Cinta yang dominan hingga batinnya merasa aman. |
| **Tipe 4** | Iman (❌), Belajar (❌), Bakat (❌) | Kerusakan fitrah menyeluruh; apatis, memberontak, atau kecanduan gawai. | **Pemulihan Berurutan Mutlak:** Wajib dimulai dari pemulihan Iman (Bahasa Hati & cinta tanpa syarat) → kemudian Belajar (alamiah) → barulah penajaman Bakat, kendati usianya telah belia/dewasa. |

> [!important] Kaidah Emas Urutan Pemulihan Kelembagaan
> *"Merujuk pada sunnatullah pertumbuhan fitrah yang berurutan dari Iman → Belajar → Bakat, maka bila ada tahapan yang belum tuntas, proses recovery WAJIB diinteraksikan dengan urutan yang sama persis, walaupun usia anak yang bersangkutan telah melampaui fase tersebut."*  
> — **Standar Penjaminan Mutu PKN, Klausul Evaluasi & Recovery**
"""

# =============================================================================
# 6. ENRICH Implementasi.md NAVIGATION
# =============================================================================

IMPLEMENTASI_PATH = os.path.join(BASE_DIR, 'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi.md')

def append_if_not_present(filepath, addition, trigger_phrase):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if trigger_phrase not in content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.rstrip() + '\n' + addition.strip() + '\n')
        print(f"Enriched: {os.path.basename(filepath)}")
    else:
        print(f"Already enriched: {os.path.basename(filepath)}")

# Execute creations and appends
def main():
    # 1. Create new article Kaidah Implementasi di Berbagai Lembaga.md
    new_art_path = os.path.join(BASE_DIR, 'content/Paradigma - Implementasi PKN/Dokumen Pendidikan Karakter Nabawiyah/Paradigma & Implementasi/Implementasi/Kaidah & Elemen/Kaidah Implementasi di Berbagai Lembaga.md')
    with open(new_art_path, 'w', encoding='utf-8') as f:
        f.write(KAIDAH_LEMBAGA_CONTENT.strip() + '\n')
    print(f"Created: {os.path.basename(new_art_path)} ({len(KAIDAH_LEMBAGA_CONTENT)} chars)")

    # 2. Enrich Peran Guru
    append_if_not_present(PERAN_GURU_PATH, PERAN_GURU_ADDITION, "Standar Mutu Kelembagaan & 4 Tingkatan Evolusi Sekolah PKN")

    # 3. Enrich Benang Merah
    append_if_not_present(BENANG_MERAH_PATH, BENANG_MERAH_ADDITION, "Grand Theory Kesadaran Beramal: Rantai Kausalitas 5 Tingkat")

    # 4. Enrich Syabab
    append_if_not_present(SYABAB_PATH, SYABAB_ADDITION, "Standar Kurikulum Pendewasaan Lembaga: Pemandirian Putra & Putri")

    # 5. Enrich Recovery
    append_if_not_present(RECOVERY_PATH, RECOVERY_ADDITION, "Matriks Diagnosis Kelembagaan: Penanganan 4 Tipe Hutang Pengasuhan")

    # 6. Add link in Implementasi.md
    with open(IMPLEMENTASI_PATH, 'r', encoding='utf-8') as f:
        imp_content = f.read()
    if "Kaidah Implementasi di Berbagai Lembaga" not in imp_content:
        imp_content = imp_content.replace(
            "* [[4 Elemen Implementasi]] — Sinergi Iman, Belajar, Bakat, dan Perkembangan.",
            "* [[4 Elemen Implementasi]] — Sinergi Iman, Belajar, Bakat, dan Perkembangan.\n  * [[Kaidah Implementasi di Berbagai Lembaga]] — 5 Kaidah emas ushul fiqih & 4 tingkatan adopsi sistem sekolah/pesantren."
        )
        with open(IMPLEMENTASI_PATH, 'w', encoding='utf-8') as f:
            f.write(imp_content)
        print("Updated Implementasi.md navigation link.")

    # 7. Add link in index.md
    index_path = os.path.join(BASE_DIR, 'content/index.md')
    with open(index_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    if "Kaidah Implementasi di Berbagai Lembaga" not in idx_content:
        idx_content = idx_content.replace(
            "[[Peran Guru dan Lembaga Pendidikan]]",
            "[[Peran Guru dan Lembaga Pendidikan]] • [[Kaidah Implementasi di Berbagai Lembaga]]"
        )
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(idx_content)
        print("Updated index.md navigation link.")

if __name__ == '__main__':
    main()

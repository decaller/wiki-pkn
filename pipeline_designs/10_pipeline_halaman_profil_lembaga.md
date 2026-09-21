# Desain Pipeline 10: Halaman Profil Lembaga & Praktik Baik Sekolah Pengadopsi (Institutional Best Practices)

Dokumen ini mengatur arsitektur pipeline pemrosesan dokumen untuk mempublikasikan **Halaman Profil Lembaga, Sekolah, Pesantren Mitra, dan Studi Lapangan Pengadopsi PKN**.

---

## 1. Karakteristik & Target Output Halaman

Halaman profil lembaga menyajikan bukti empiris keberhasilan penerapan PKN di berbagai institusi pendidikan Islam (SDIT, Pesantren, Sekolah Alam, Homeschooling Group, dll.).
- **Tujuan Utama:** Menjadi wahana saling belajar antar institusi (*benchmarking*), mendokumentasikan model adaptasi kurikulum, mencatat kendala transisi dari sistem lama ke sistem nabawiyah, serta memberikan kontak rujukan bagi pegiat pendidikan yang ingin berkunjung/studi banding.
- **Komponen Kunci Output Markdown:**
  - **Identitas Institusi:** Nama sekolah/pesantren, lokasi, yayasan penaung, jenjang pendidikan, dan tahun mulai mengadopsi PKN.
  - **Model Integrasi Kurikulum:** Bagaimana sekolah mengintegrasikan PKN (apakah sebagai kurikulum utama utuh, program pembiasaan harian, atau matrikulasi adab santri).
  - **Dinamika Transisi & Kendala Lapangan:** Kisah nyata tantangan meyakinkan orang tua murid dan pelatihan guru.
  - **Praktik Terbaik (*Best Practices*):** Program unggulan yang terbukti menumbuhkan karakter santri (misal: halaqah subuh ayah-anak, magang bakat usia baligh, ekspedisi kemandirian).
  - **Tabel Rekapitulasi Metrik Perkembangan.**
  - **Verifikasi Izin Publikasi (Consent Gate).**

---

## 2. Sumber Bahan Baku (Multi-Modal Ingestion)

1. **Dokumen Profil Sekolah & Laporan Tahunan:** Brosur, naskah kurikulum internal, dan laporan akreditasi sekolah.
2. **Wawancara Audio Kepala Sekolah / Yayasan:** Rekaman wawancara mendalam mengenai riwayat penerapan PKN.
3. **Dokumentasi Visual & Kegiatan:** Foto kegiatan santri beresolusi optimal.

---

## 3. Diagram Alur State Graph LangGraph

```mermaid
flowchart TD
    subgraph S1["1. Fase Ingestion Profil Lembaga"]
        N1_1["SchoolDocLoaderNode<br/>Ekstraksi berkas profil & kurikulum sekolah mitra"]
        N1_2["InterviewTranscriptParser<br/>Parsing catatan wawancara pimpinan & kepala sekolah"]
        N1_1 & N1_2 --> N1_Merge["Data Mentah Institusi"]
    end

    subgraph S2["2. Fase Verifikasi Izin & Keamanan Data"]
        N2_1["ConsentGatekeeperNode<br/>Pengecekan surat izin rilis data publik dari yayasan"]
        N2_2["StudentAnonymizerNode<br/>Sensor data pribadi santri di foto / catatan disiplin"]
        N1_Merge --> N2_1 --> N2_2
    end

    subgraph S3["3. Fase Analisis Model Adopsi"]
        N3_1["AdoptionModelClassifierNode<br/>Klasifikasi model (Full Kurikulum, Suplemen Adab, Asrama)"]
        N3_2["BestPracticeSynthesizerNode<br/>Ekstraksi program unggulan dan solusi kendala transisi"]
        N3_3["BenchmarkingMatrixBuilderNode<br/>Penyusunan tabel komparasi metrik lembaga"]
        N2_2 --> N3_1 --> N3_2 & N3_3
    end

    subgraph S4["4. Fase Perakitan Dokumen Profil"]
        N4_1["InstitutionMarkdownAssembler<br/>Format profil standar, galeri kegiatan, & info kontak"]
        N3_2 & N3_3 --> N4_1
    end

    subgraph S5["5. Gerbang Tinjauan Manusia (HITL Gate)"]
        N5_HITL{"SchoolPrincipalGate<br/>Review & Persetujuan Kepala Sekolah Mitra"}
        N5_Live["Simpan ke content/Referensi/Lembaga/"]
        N5_Hold["Klarifikasi Data dengan Pihak Sekolah"]
        N4_1 --> N5_HITL
        N5_HITL -->|Disetujui Tertulis| N5_Live
        N5_HITL -->|Ada Koreksi Data/Foto| N5_Hold
        N5_Hold --> N2_1
    end
```

---

## 4. Spesifikasi Node & State Schema

### Skema State Spesifik: `InstitutionProfileState`

```python
from typing import TypedDict, List, Dict, Any, Optional

class AdoptionModel(TypedDict):
    category: str                   # 'Kurikulum Penuh', 'Suplemen Pembiasaan', 'Pesantren Terpadu'
    year_started: int
    pilot_grade: str                # e.g., 'Dimulai dari jenjang TK dan Kelas 1 SD'
    teacher_training_method: str

class SchoolBestPractice(TypedDict):
    program_name: str
    target_character_trait: str     # Sesuai pilar TB40
    operational_routine: str
    impact_observed: str

class InstitutionProfileState(TypedDict):
    school_name: str
    city_province: str
    leadership_contact: str
    official_website_url: Optional[str]
    has_written_consent: bool
    adoption_details: AdoptionModel
    best_practices: List[SchoolBestPractice]
    transitional_challenges_solved: List[Dict[str, str]]
    markdown_output: str
    hitl_approved: bool
```

### Rincian Fungsi Node Kunci:
1. **`ConsentGatekeeperNode`**: Mengunci status publikasi sampai terdapat verifikasi persetujuan tertulis dari pengurus yayasan/kepala sekolah untuk mencegah sengketa data atau pelanggaran privasi internal.
2. **`BestPracticeSynthesizerNode`**: Mengambil sari program unggulan sekolah dan menerjemahkannya ke dalam bahasa sistem yang dapat direplikasi oleh sekolah lain (*replicable SOP*).

---

## 5. Strategi Prompting AI

```markdown
### System Prompt: BestPracticeSynthesizerNode
Anda adalah Analis Manajemen Lembaga Pendidikan Islam.
Susun profil implementasi sekolah mitra PKN ini dengan gaya laporan profesional:

1. Fokuskan ulasan pada **proses transformasi**: bagaimana sekolah merubah budaya lama (yang mungkin serba menuntut angka dan ancaman) menjadi budaya saling menyayangi berbasis fitrah.
2. Ungkapkan kendala nyata yang dihadapi (misal: resistensi orang tua santri yang mencemaskan ujian nasional) dan strategi komunikasi yang ditempuh sekolah untuk mengatasinya.
3. Hindari nada promosi/marketing berlebihan; kedepankan semangat berbagi ilmu (*ta'awun 'alal birri wat taqwa*).
```

---

## 6. Level Kebutuhan Human-in-the-Loop (HITL)

- **Tingkat Kebutuhan HITL:** `Sedang`
- **Kriteria Tinjauan:**
  - Konfirmasi keabsahan data kontak dan alamat lembaga.
  - Verifikasi keaslian foto dan izin publikasi dari orang tua santri yang bersangkutan.
  - Keselarasan program sekolah dengan prinsip manhaj PKN.

---

## 7. Contoh Cuplikan Dokumen Markdown Terformat

```markdown
---
title: "Profil Lembaga: Sekolah Karakter Nabawiyah Insan Mustaqbal"
description: "Model implementasi penuh kurikulum fitrah dan penjenjangan 3 bahasa pendidik pada jenjang pendidikan dasar."
tags:
  - profil-lembaga
  - sekolah-mitra
  - best-practices
---

# Profil Lembaga: Sekolah Karakter Insan Mustaqbal

Lembaga pendidikan dasar yang berfokus pada integrasi fitrah iman dan penumbuhan bakat 40 karakter nabawiyah sejak usia dini...

## 🏫 Identitas & Riwayat Adopsi
- **Jenjang:** SD (Kelas 1 - 6).
- **Lokasi:** Jawa Barat, Indonesia.
- **Mulai Adopsi PKN:** Tahun 2021.
- **Model Adopsi:** Implementasi Kurikulum Penuh (Peniadaan sistem ranking angka & penggantian dengan Rapor Deskripsi Fitrah).

## 🌟 Praktik Terbaik Unggulan (*Best Practices*)
1. **Morning Heart Connection (15 Menit Pertama):** Setiap pagi guru menyambut santri di depan gerbang dengan senyuman dan menanyakan kabar tangki cinta mereka sebelum pelajaran dimulai.
2. **Program Magang Bakat (Usia 10-12 Tahun):** Santri magang pada unit usaha sekolah sesuai hasil asesmen TB40 masing-masing.
```

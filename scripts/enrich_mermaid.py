#!/usr/bin/env python3
"""
enrich_mermaid.py
Menambahkan diagram Mermaid yang bersih dan valid (bebas error 'Unsupported markdown: list')
pada 14 artikel konseptual yang belum memiliki diagram alur visual.
Strict rule: ZERO DELETION (hanya menyisipkan konten baru sebelum ## Tautan atau di akhir).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"

MERMAID_SECTIONS = {
    "Thufulah.md": """
## Visualisasi Dinamika Fitrah Etape Thufulah (0–7 Tahun)

```mermaid
flowchart TD
    subgraph Thufulah["ETAPE THUFULAH (0-7 TAHUN)"]
        A["1: Kebutuhan Mutlak<br/>• Limpahan Kasih Sayang Murni<br/>• Rasa Aman & Kelekatan Fisik<br/>• Bermain Bebas Tanpa Beban"]
        B["2: Resapan Qudwah (Al-Muhakah)<br/>• Meniru Gerak & Lisan Orang Tua<br/>• Belajar Alami Lewat Indera Sensorik<br/>• Fitrah Tauhid Disiram Keindahan Alam"]
        C["3: Penjagaan Fitrah<br/>• Nihil Hisab Syariat (La Taklif)<br/>• Bebas Bentakan & Trauma Fisik<br/>• Tangki Cinta Terisi Penuh"]
    end
    A --> B
    B --> C
    C --> Output["Pondasi Jiwa Kokoh Menuju Tamyiz"]
```
""",

    "Tamyiz.md": """
## Visualisasi Gerbang Nalar & Pembiasaan Adab Etape Tamyiz (7–10 Tahun)

```mermaid
flowchart TD
    subgraph Tamyiz["ETAPE TAMYIZ (7-10 TAHUN)"]
        T1["1: Mekarnya Akal Selektif<br/>• Mampu Membedakan Baik vs Buruk<br/>• Memahami Hubungan Sebab-Akibat<br/>• Mulai Terbuka pada Dialog Nalar"]
        T2["2: Laboratorium Pembiasaan Shalat<br/>• 3 Tahun Penuh (5000+ Waktu Shalat)<br/>• Dilatih Bersuci & Tertib Ibadah<br/>• Tanpa Pukulan atau Paksaan Melukai"]
        T3["3: Observasi Rukun 3A Bakat<br/>• Menjelajahi Berbagai Aktivitas<br/>• Menemukan sukA (Al-Hirsh)<br/>• Mengasah bisA (Al-Itqan)"]
    end
    T1 --> T2
    T2 --> T3
    T3 --> Output["Kesiapan Mental Memasuki Murahaqah"]
```
""",

    "Murahaqah.md": """
## Visualisasi Tangga Kesiapan Baligh Etape Murahaqah (10–15 Tahun)

```mermaid
flowchart TD
    subgraph Murahaqah["ETAPE MURAHAQAH (10-15 TAHUN)"]
        M1["1: Badai Pubertas & Gejolak Syahwat<br/>• Perubahan Hormon & Fisik Drastis<br/>• Godaan Emosi & Pengaruh Teman<br/>• Pemisahan Ranjang (Tafriqul Madhaji)"]
        M2["2: Penegakan Batas Syariat (Hudud)<br/>• Ketegasan Pendidik Penuh Adab<br/>• Konsekuensi Logis Terukur<br/>• Perlindungan Muru'ah & Kehormatan"]
        M3["3: Pemagangan Peran Nyata<br/>• Penugasan Proyek Kemandirian<br/>• Pengasahan Bakat Spesifik<br/>• Tanggung Jawab Sosial & Finansial"]
    end
    M1 --> M2
    M2 --> M3
    M3 --> Output["Insan Mukallaf Siap Berdikari (Syabab)"]
```
""",

    "Bahasa Lisan.md": """
## Visualisasi Filter Tutur Lisan Nabawi (Tiga Saringan Kata)

```mermaid
flowchart TD
    subgraph Lisan["FILTER TUTUR KATA PENDIDIK"]
        In["Kata / Dorongan yang Ingin Diucapkan"]
        F1{"Filter 1: Ash-Shidq<br/>Apakah Benar & Bebas Labeling?"}
        F2{"Filter 2: Al-Adab<br/>Apakah Santun & Memuliakan Fitrah?"}
        F3{"Filter 3: Al-Manfa'ah<br/>Apakah Berdaya Ubah & Bernilai Doa?"}
        Speak["Ucapkan dengan Nada Teduh & Sejajar Mata"]
        Silent["Tahan Lisan / Alihkan ke Doa Batin"]
    end

    In --> F1
    F1 -- Ya --> F2
    F1 -- Tidak --> Silent
    F2 -- Ya --> F3
    F2 -- Tidak --> Silent
    F3 -- Ya --> Speak
    F3 -- Tidak --> Silent
```
""",

    "Tujuan Hidup Manusia.md": """
## Visualisasi Arsitektur Visi Kehidupan: 'Ibadah & Khilafah

```mermaid
flowchart TD
    subgraph Visi["ARSITEKTUR TUJUAN EKSISTENSI INSAN"]
        Pillar1["1: Hubungan Vertikal ('Ibadah)<br/>• Penghambaan Murni Lillahi Ta'ala<br/>• Ketaatan Syariat Lahir & Batin<br/>• Meraih Ridha & Jannah Allah"]
        Pillar2["2: Hubungan Horizontal (Khilafah)<br/>• Memakmurkan Bumi (Imaratul Ardh)<br/>• Menegakkan Keadilan & Kebajikan<br/>• Memanfaatkan Bakat Demi Maslahat Umat"]
    end
    Pillar1 <--> Pillar2
    Pillar1 --> Goal["KEBAHAGIAAN PARIPURNA (AS-SA'ADAH)<br/>Selamat di Dunia & Mulia di Akhirat"]
    Pillar2 --> Goal
```
""",

    "Tanggung Jawab Pendidikan.md": """
## Visualisasi Sinergi Tripartit Tanggung Jawab Pendidikan

```mermaid
flowchart TD
    subgraph Sinergi["TRIANGEL SINERGI PENDIDIKAN NABAWIYAH"]
        Ayah["AYAH (Qawwam & Visioner)<br/>• Penanggung Jawab Aqidah Utama<br/>• Pemberi Nafkah Halal<br/>• Penegak Prinsip & Disiplin"]
        Bunda["BUNDA (Madrasatul Ula)<br/>• Pemuas Tangki Cinta & Kelekatan<br/>• Pembiasaan Adab Harian<br/>• Penjaga Kehangatan Rumah"]
        Guru["GURU & SEKOLAH (Mitra Murabbi)<br/>• Transmisi Ilmu Terstruktur<br/>• Fasilitator Eksplorasi Bakat<br/>• Penguat Adab Kolektif"]
    end
    Ayah <--> Bunda
    Ayah <--> Guru
    Bunda <--> Guru
    Ayah --> Anak["ANAK BERFITRAH KOKOH & BERKARYA"]
    Bunda --> Anak
    Guru --> Anak
```
""",

    "Kaidah & Elemen/index.md": """
## Visualisasi Integrasi Kaidah dan Elemen PKN

```mermaid
flowchart TD
    subgraph Fondasi["4 KAIDAH EMAS PKN"]
        K1["1: Satu Anak Satu Kurikulum"]
        K2["2: Tadarruj (Bertahap Alami)"]
        K3["3: Teladan Sebelum Arahan"]
        K4["4: Asah Bakat Dominan"]
    end

    subgraph Pilar["4 ELEMEN STRUKTURAL PKN"]
        E1["Elemen 1: Manusia Beriman (Insan)"]
        E2["Elemen 2: Adab & Akhlak Nabawiyah"]
        E3["Elemen 3: Ilmu & Wawasan Luas"]
        E4["Elemen 4: Amal Shalih & Peradaban"]
    end

    Fondasi ==> Pilar
    Pilar ==> Buah["GENERASI KHALIFAH RABBANIYAH"]
```
""",

    "Insight & Teknis/Insight/index.md": """
## Visualisasi Jalur Transformasi Wawasan (Insight) ke Implementasi

```mermaid
flowchart LR
    A["Kajian & Buku PKN<br/>(Wawasan Kognitif)"] --> B["Tazkiyatun Nafs<br/>(Pembersihan Hati Pendidik)"]
    B --> C["Observasi Fitrah & Rukun 3A<br/>(Instrumen SOTABH)"]
    C --> D["Ekosistem Rumah & Kelas<br/>(Aksi Lapangan Berkelanjutan)"]
```
""",

    "Renungan/Hak dan Kewajiban.md": """
## Visualisasi Neraca Keadilan Hak dan Kewajiban Anak

```mermaid
flowchart TD
    subgraph Neraca["NERACA HAK & KEWAJIBAN FITRAH"]
        Hak["HAK ANAK DARI ORANG TUA<br/>• Cinta Tanpa Syarat & Kelembutan<br/>• Perlindungan Jiwa & Raga<br/>• Nafkah Halal & Nama Mulia<br/>• Pendidikan Agama & Adab"]
        Kewajiban["KEWAJIBAN ANAK SECARA BERTAHAP<br/>• 0-7 Th: Nol Kewajiban Syariat<br/>• 7-10 Th: Pembiasaan Shalat & Adab<br/>• 10-15 Th: Disiplin & Tanggung Jawab<br/>• 15+ Th: Berbakti (Birrul Walidain)"]
    end
    Hak ==> Kewajiban
    Kewajiban ==> Ridha["RIDHA ALLAH & KEBERKAHAN KELUARGA"]
```
""",

    "FAQ Ringkas.md": """
## Visualisasi Pohon Keputusan Problem Pengasuhan Cepat

```mermaid
flowchart TD
    Start["Anak Menunjukkan Perilaku Bermasalah"] --> Q1{"Apakah Usianya di Bawah 7 Tahun?"}
    Q1 -- Ya --> A1["Dekap & Alihkan Perhatian<br/>(Jangan Dihukum / Bentak)"]
    Q1 -- Tidak --> Q2{"Apakah Tangki Cintanya Kosong?"}
    Q2 -- Ya --> A2["Pulihkan Kelekatan Dulu<br/>(Waktu Khusus 15 Menit)"]
    Q2 -- Tidak --> Q3{"Apakah Ini Luapan Bakat yang Tersumbat?"}
    Q3 -- Ya --> A3["Salurkan ke Wadah Positif SOTABH"]
    Q3 -- Tidak --> A4["Tegakkan Konsekuensi Logis Bersama"]
```
""",

    "Referensi Kajian Video.md": """
## Visualisasi Jalur Belajar Video Kajian PKN

```mermaid
flowchart LR
    V1["1: Seri Fondasi Insan<br/>(Hakikat Jiwa & Fitrah)"] --> V2["2: Seri Metode Tarbiyah<br/>(Bahasa Hati & Batas Toleransi)"]
    V2 --> V3["3: Seri Peta Bakat 40<br/>(Observasi & Rukun 3A)"]
    V3 --> V4["4: Seri Implementasi Lembaga<br/>(Kaidah Emas & Standar Mutu)"]
```
""",

    "Kuisioner Asesmen 40 Bakat Nabawiyah.md": """
## Visualisasi Alur Pengisian dan Scoring Kuisioner TB-40

```mermaid
flowchart TD
    Step1["1: Menyiapkan Diri dalam Kondisi Rileks & Jujur"] --> Step2["2: Membaca 40 Pernyataan Sifat dengan Seksama"]
    Step2 --> Step3["3: Menentukan Pilihan: Sangat Gue / Netral / Bukan Gue"]
    Step3 --> Step4["4: Pemetaan Warna (Merah: Bakat Kuat, Hitam: Kelemahan Minor)"]
    Step4 --> Step5["5: Diskusi Konfirmasi Bersama Mentor / Orang Tua"]
    Step5 --> Step6["6: Penyusunan Rencana Aksi Pengembangan Bakat Dominan"]
```
""",

    "Internal & Eksternal/index.md": """
## Visualisasi Dinamika Faktor Ruhiyah dan Ekosistem Lingkungan

```mermaid
flowchart TD
    subgraph Dinamika["DIALETIKA FAKTOR PENDIDIKAN"]
        Internal["FAKTOR INTERNAL (Inti)<br/>• Kesucian Niat Pendidik<br/>• Kekuatan Doa Sepertiga Malam<br/>• Ketenangan Jiwa Rumah Tangga"]
        Eksternal["FAKTOR EKSTERNAL (Pelindung)<br/>• Lingkungan Tetangga Shalih<br/>• Sekolah Ramah Fitrah<br/>• Filter Paparan Media Digital"]
    end
    Internal <==> Eksternal
    Internal --> Benteng["IMUNITAS GENERASI MUKALLAF"]
    Eksternal --> Benteng
```
""",

    "index.md": """
## Visualisasi Arsitektur Pengetahuan Wiki PKN

```mermaid
flowchart TD
    Home["BERANDA WIKI PENDIDIKAN KARAKTER NABAWIYAH"]
    Home --> C1["1: FONDASI INSAN & JIWA<br/>(Ruh, Jasad, Nafs, Fitrah)"]
    Home --> C2["2: FITRAH & BAKAT 40<br/>(TB-40, Rukun 3A, Etape Usia)"]
    Home --> C3["3: METODE & PENGASUHAN<br/>(Bahasa Hati, Tangki Cinta, Recovery)"]
    Home --> C4["4: IMPLEMENTASI & LEMBAGA<br/>(4 Kaidah, Standar Mutu, RPP)"]
```
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
    print("Menambahkan diagram Mermaid konseptual pada 14 artikel...")
    count = 0
    for file_key, section_text in MERMAID_SECTIONS.items():
        matched_files = list(CONTENT_DIR.rglob(file_key))
        if not matched_files:
            print(f"[WARN] File tidak ditemukan: {file_key}")
            continue
            
        target_file = [f for f in matched_files if "Template" not in str(f)][0]
        content = target_file.read_text(encoding="utf-8")
        
        # Cek apakah sudah ada mermaid di file ini
        if "```mermaid" in content:
            print(f"[SKIP] Sudah ada mermaid di {target_file.relative_to(CONTENT_DIR)}")
            continue
            
        new_content = insert_before_links(content, section_text)
        target_file.write_text(new_content, encoding="utf-8")
        print(f"[UPDATED] {target_file.relative_to(CONTENT_DIR)} (+Mermaid)")
        count += 1
        
    print(f"\nSelesai: {count} artikel berhasil diperkaya dengan diagram Mermaid konseptual!")

if __name__ == "__main__":
    main()

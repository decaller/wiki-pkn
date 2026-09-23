# Evidence-Based Research Workflow: Panduan Riset Ilmiah, Audit Replikasi & Komparasi Teori PKN

Dokumen ini memuat panduan metodologis untuk membangun alur kerja riset berbasis bukti (*evidence-based research workflow*) yang dirancang khusus untuk memotong bias/hype *pop-science*, mengaudit status replikasi penelitian, mengisolasi data mekanistik yang solid, serta menyintesis dan mengomparasikannya secara proporsional dengan **Teori Pendidikan Karakter Nabawiyah (PKN)**.

Pedoman ini menjadi acuan operasional bagi implementasi tugas riset pada [TODO.md](../TODO.md) dan melengkapi spesifikasi [Pipeline 08: Halaman Komparasi Konsep & Kurikulum Pendidikan](08_pipeline_halaman_komparasi_konsep.md).

---

## 1. Landasan & Arsitektur Pipeline Riset

Building an evidence-based research workflow—specifically one designed to bypass pop-science hype, audit replication status, and isolate hard mechanistic data—requires tools categorized by their function in the analytical pipeline.

```
[ Discovery & Citation Graph ] ──► [ Verification & Retraction Audit ]
                                                │
                                                ▼
[ Local Synthesis & Vault ]    ◄── [ Systematic Screening & Extraction ]
         │
         ▼
[ Komparasi Teori PKN (Matriks 6 Dimensi & Filter Syar'i) ]
```

---

## 2. Peta Perangkat Berdasarkan Fungsi Pipeline

### 1. Discovery & Citation Graph Engines
Perangkat ini melacak bagaimana artikel ilmiah terhubung secara kronologis dan konseptual, memungkinkan peneliti melewati kekacauan kata kunci (*keyword clutter*) dan melihat apakah suatu temuan merupakan anomali terisolasi (*isolated outlier*) atau bagian dari konsensus ilmiah yang telah mapan.

| Tool | Type / Access | Core Function in Rigorous Research |
|---|---|---|
| **OpenAlex** | Open Source / Free API | Katalog terbuka terbesar dari sistem riset global (>250M karya ilmiah). Berbeda dari Google Scholar, seluruh graf, afiliasi penulis, dan metadata pendana dapat diakses melalui endpoint terbuka, menjadikannya sumber data utama untuk analisis literatur programatik. |
| **Semantic Scholar** | Free / Open API | Menggunakan NLP untuk mengkategorikan sitasi berdasarkan intensi (*Methodology*, *Background*, atau *Result Comparison*) serta menandai *"Highly Influential Citations"*, meniadakan tebak-tebakan tentang alasan suatu artikel dikutip. |
| **Connected Papers / Litmaps** | Freemium / Web | Memvisualisasikan jaringan ko-sitasi. Sangat berguna untuk menemukan karya terdahulu (*seminal ancestor papers*) dan karya turunan (*subsequent replications or disputes*) dari target paper dalam dua klik. |
| **Consensus.app** | Closed / Freemium | Mencari artikel *peer-reviewed* menggunakan pertanyaan bahasa alami (natural language) dan menghasilkan *"Consensus Meter"* berbasis apakah temuan empiris yang diekstraksi sepakat (*agree*), tidak sepakat (*disagree*), atau belum konklusif. |

---

### 2. Verification, Replicability & Retraction Auditing
Perangkat ini mengidentifikasi apakah suatu studi telah didiskreditkan, digugat oleh upaya replikasi berikutnya, atau ditarik (*retracted*) oleh penerbit ilmiah:

* **scite.ai (Smart Citations):**
  * **Mekanisme:** Alih-alih menampilkan jumlah sitasi mentah, scite memanfaatkan *deep learning* untuk mengklasifikasikan sitasi ke dalam 3 kategori: *Mentioning*, *Supporting*, atau *Contrasting*.
  * **Kegunaan Riset:** Memberikan peringatan dini instan jika suatu paper psikologi atau neurosains populer ternyata memiliki 50 sitasi yang menunjukkan bahwa temuannya gagal direplikasi (*replication crisis*).
* **Retraction Watch Database:**
  * **Mekanisme:** Basis data internasional komprehensif yang melacak pencabutan artikel (*retractions*), pernyataan kekhawatiran (*expressions of concern*), serta investigasi pabrik artikel ilmiah (*paper-mill investigations*).
  * **Kegunaan Riset:** Memverifikasi apakah paper yang dirujuk ditarik pasca-publikasi akibat pemalsuan data atau tinjauan sejawat yang dikompromikan. (Dapat diintegrasikan langsung ke dalam *reference manager*).
* **Open Science Framework (OSF.io):**
  * **Mekanisme:** Repositori terpusat untuk pra-registrasi studi (*preregistrations*), data terbuka (*open data*), dan kode sumber terbuka (*open code*).
  * **Kegunaan Riset:** Memeriksa apakah artikel final yang dipublikasikan penulis sesuai dengan protokol yang didaftarkan sebelumnya, atau apakah mereka mengubah hipotesis pasca-pengujian (*HARKing / p-hacking*).

---

### 3. Model Context Protocol (MCP) Servers for AI Agents
Server Model Context Protocol (MCP) memungkinkan antarmuka LLM lokal maupun terkelola (seperti Claude Desktop, Cursor, atau orkestrator agen lokal) mengeksekusi *tool calls* terstruktur langsung ke API akademik terverifikasi, bukan mengarang atau berhalusinasi literatur ilmiah:

* **PubMed / NCBI MCP Server:**
  * **Fungsi:** Memberikan LLM akses bawaan untuk melakukan kueri ke MEDLINE/PubMed menggunakan istilah MeSH, mengambil XML teks lengkap akses terbuka PubMed Central (PMC), dan memverifikasi data klinis/fisiologis langsung dari *National Library of Medicine*.
* **Semantic Scholar MCP Server:**
  * **Fungsi:** Memungkinkan LLM menerima input DOI paper, mengambil graf sitasi presisi, menarik abstrak artikel yang mengutipnya, dan mengembalikan metrik sitasi berpengaruh (*influential citations*).
* **Zotero Local MCP Server:**
  * **Fungsi:** Menjembatani LLM langsung ke database SQLite lokal Zotero dan penyimpanan PDF lokal. Pengguna dapat memvalidasi: *"Kueri koleksi Zotero saya tentang cognitive reserve dan ekstrak hanya paper yang menggunakan randomized controlled trials."* Model membaca teks PDF lokal riil, bukan teks internet umum.
* **Fetch / Puppeteer MCP Server (Markdown Scraper):**
  * **Fungsi:** Digunakan untuk mem-parsing preprint (arXiv, bioRxiv) dan repositori data terbuka langsung menjadi format Markdown bersih, mengeliminasi iklan dan boilerplate UI untuk konsumsi jendela konteks (*context window*) LLM yang efisien.

---

### 4. Systematic Screening & Extraction Software
Ketika mengevaluasi puluhan hingga ratusan artikel untuk mengeliminasi bias seleksi manusia (*human selection bias*):

* **ASReview (Active Learning for Systematic Reviews):**
  * **Tipe:** Sepenuhnya Open Source (Python / Utrecht University).
  * **Mekanisme:** Menggunakan algoritma *machine learning active learning* untuk mengurutkan ulang kandidat paper selama proses *screening* berdasarkan keputusan inklusi/eksklusi awal peneliti.
  * **Kegunaan Riset:** Mengurangi beban pembacaan yang diperlukan untuk menemukan 95% paper relevan hingga 70–80%, tanpa terkunci pada vendor komersial (*vendor lock-in*).
* **Rayyan:**
  * **Tipe:** Freemium / Web App.
  * **Mekanisme:** Platform *screening* multi-reviewer terdedikasi yang dirancang untuk *systematic review* sesuai standar PRISMA.
  * **Kegunaan Riset:** Memungkinkan *double-blind title and abstract screening* dengan fitur resolusi konflik bawaan, mencegah bias konfirmasi (*confirmation bias*) satu reviewer mencemari kumpulan studi yang dipilih.

---

### 5. Local Synthesis & Personal Knowledge Architecture
Untuk mencegah distorsi teoretis (*theoretical drift*) dan mengorganisir catatan empiris dengan asal-usul sumber yang *immutable* (tidak dapat diubah):

```
[ Primary Source PDF ] ──► [ Zotero (Metadata + Retraction Watch Alert) ]
                                      │
                                      ▼ (Better BibTeX / Markdown Export)
                           [ Local Graph Vault (Obsidian / Logseq) ]
                                      │
                                      ▼
             [ Model Context Protocol (MCP) / Local Vector RAG ]
```

* **Zotero (Open Source):**
  * Pasang plugin **Zotero-Retraction-Watch** (secara otomatis menandai paper yang ditarik dengan warna merah di perpustakaan digital).
  * Pasang plugin **Better BibTeX** (menghasilkan *citation keys* terstandarisasi seperti `smith2024homeostasis` untuk tautan Markdown yang bersih).
* **Obsidian / Logseq (Local Markdown Vaults):**
  * Perlakukan setiap paper sebagai **catatan atomik (*atomic note*)** dengan *frontmatter* terstruktur:
    ```yaml
    ---
    title: "Paper Title"
    authors: [Author A, Author B]
    year: 2024
    doi: "10.xxxx/yyyy"
    methodology: "Double-blind RCT / Longitudinal Cohort"
    sample_size: 1250
    measurement_type: "Direct / Latent Proxy"
    preregistered: true
    replication_status: "Successfully replicated / Mixed / Failed"
    key_mechanisms: ["Dopaminergic reward pathway", "Prefrontal executive control"]
    ---
    ```
  * Hindari catatan "ringkasan umum" yang pasif. Tulis catatan yang melacak **klaim mekanistik (*mechanistic claims*)** dan tautkan seluruh artikel yang mendukung atau membantah klaim spesifik tersebut.

---

## 3. Integrasi & Komparasi Kritis dengan Teori Pendidikan Karakter Nabawiyah (PKN)

Setelah data empiris berhasil diisolasi, disaring dari krisis replikasi, dan diverifikasi klaim mekanistiknya, tahap krusial berikutnya adalah melakukan **telaah kritis dan komparasi dengan paradigma Pendidikan Karakter Nabawiyah (PKN)**:

### A. Prinsip Pemilahan: *Wasilah* (Sarana Teknis) vs *Ghayah* (Tujuan Hakiki)
1. **Validasi Data Mekanistik (Sarana / *Wasilah*):**
   - Temuan neurosains, tahapan myelinisasi otak anak, rentang atensi, atau dinamika hormon stres (kortisol) merupakan sunnatullah pada aspek fisik-biologis manusia (*alam kauniyah*).
   - Selama metodologinya valid, lolos replikasi, dan bebas dari cacat fabrikasi, temuan mekanistik ini diakui sebagai penguat deskriptif atas sunnatullah tumbuh kembang anak.
2. **Kritik Asumsi Filosofis (Tujuan / *Ghayah* & Aksiologi):**
   - Menolak keras reduksionisme materialistik (misal: pandangan bahwa manusia hanyalah produk reaksi kimiawi otak tanpa ruh dan fitrah).
   - Menolak relativisme moral (moralitas anak dianggap sekadar konsensus sosial, bukan bimbingan wahyu).
   - Mendekonstruksi teori sekuler yang menafikan alam akhirat, hisab, dan ridha Allah sebagai muara tertinggi pembentukan karakter.

### B. Matriks Evaluasi 6 Dimensi Komparatif
Sintesis riset eksternal wajib dipetakan ke dalam matriks 6 dimensi standar Wiki PKN ([Pipeline 08](08_pipeline_halaman_komparasi_konsep.md)):
1. **Hakikat Insan (*Ontologi*):** Pandangan teori riset vs Konsep Fitrah Tauhid dan Nafs dalam Islam.
2. **Tujuan Puncak Pendidikan (*Ghayah*):** Keberhasilan duniawi/sosial-ekonomi semata vs *Sa'adatud Darain* (kebahagiaan dunia & keselamatan akhirat).
3. **Peran Pendidik (*Murabbi*):** Fasilitator netral vs Teladan (*Uswah*), penyampai amanah (*Mu'allim/Murabbi*), dan pendidik yang mendoakan santri.
4. **Pendekatan Disiplin & Konsekuensi (*Adab & 'Uqubah*):** Behaviorisme reward-punishment vs Tadarrub, penanaman rasa malu (*Haya'*), tadarruj syar'i, dan kasih sayang.
5. **Orientasi Hasil (*Najaah*):** Metrik numerik/kompetitif vs Kesadaran beramal, keikhlasan, dan integritas kepribadian (*Syakhsiyah Islamiyah*).
6. **Keterikatan dengan Akhirat & Ridha Allah:** Dimensi yang umumnya nihil dalam riset konvensional dan menjadi pilar distingtif absolut dalam PKN.

---

## 4. Alur Kerja Praktis untuk Peneliti & Kontributor Wiki-PKN

1. **Identifikasi Topik Bahasan:** Misal *Regulasi Emosi Anak Usia Dini*, *Dampak Gadget terhadap Dopamin*, atau *Gaya Pengasuhan Authoritative vs Otoriter*.
2. **Kueri Mesin Sitasi & Graf:** Gunakan OpenAlex dan Semantic Scholar untuk memetakan paper rujukan utama (*landmark papers*).
3. **Audit Replikasi & Retraksi:** Cek paper target di scite.ai dan Retraction Watch Database. Jika paper bermasalah atau gagal replikasi, beri catatan kritis atau diskualifikasi dari rujukan utama.
4. **Ekstraksi Terstruktur:** Simpan metadata dan catatan klaim mekanistik di Zotero + Obsidian.
5. **Sintesis Komparasi PKN:** Rujuk dalil Al-Qur'an dan Sunnah bersanad, syarah ulama salaf, serta buku rujukan Ustadz Abdul Kholiq.
6. **Publikasi Hasil:** Tulis artikel ensiklopedis berstandar MediaWiki 4-Zone di direktori `content/Paradigma - Implementasi PKN/` atau direktori tematik terkait.

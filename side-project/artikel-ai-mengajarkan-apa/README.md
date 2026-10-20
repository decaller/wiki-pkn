# Wake-Up Call AI: Kalau AI Bisa Lebih Pintar, Terus Kita Mengajarkan Apa?

Paket konten edukasi ringkas untuk media sosial dan poster minimalis yang memadukan Manhaj Pendidikan Karakter Nabawiyah (PKN) dengan pendekatan *Pembelajaran Alamiyah Mustaqbal Way (Sandbox & Out of the Box)*.

## Daftar Berkas

- `artikel_wake_up_call_ai_sosmed.md`: Naskah artikel ringkas siap sebar untuk media sosial (WhatsApp, Telegram, Facebook, Instagram).
- `poster_philosophy.md`: Filosofi desain poster minimalis (*Editorial Horizon*).
- `poster_minimalis_ai.typ`: Sumber tata letak Typst untuk poster minimalis (A4 portrait, tipografi besar).
- `poster_minimalis_ai.pdf`: Hasil kompilasi poster cetak/digital dalam format PDF (1 halaman).
- `poster_minimalis_ai.png`: Hasil render poster resolusi tinggi (240 PPI) siap bagikan ke media sosial via Typst.
- `build_poster_openpencil.js`: Skrip perakit OpenPencil / FigCraft berbasis Figma Plugin API.
- `poster_openpencil.fig`: Dokumen master desain Figma asli yang dihasilkan oleh OpenPencil CLI (dapat dibuka langsung di Figma & OpenPencil).
- `poster_openpencil.figcraft`: Dokumen format FigCraft untuk dibuka dan disunting di aplikasi FigCraft desktop.
- `poster_openpencil.png`: Hasil ekspor poster beresolusi tinggi (2x: 1190 × 1684 px) dari OpenPencil.
- `poster_openpencil.pdf`: Versi PDF resolusi tinggi dari poster OpenPencil.
- `preview_poster_openpencil.png`: Pratinjau poster OpenPencil ukuran ringkas untuk tampilan cepat.
- `assets/stock_hero_seedling.jpg`: Foto stok resolusi tinggi (Unsplash) — tunas tanaman yang tumbuh keluar dari kotak semai sebagai metafora *Penumbuh Iman* sekaligus *Sandbox & Out of the Box*.

## Cara Kompilasi Ulang Poster

### Versi OpenPencil / FigCraft (Figma Engine A4)

```bash
# 1. Bangun dokumen Figma (.fig) via OpenPencil CLI
bun run /home/abuhafi/Project/open-pencil/packages/cli/bin/openpencil.js eval \
  "/home/abuhafi/Project/open-pencil/figma-resources/14 Screen Education Apps.fig" \
  -o side-project/artikel-ai-mengajarkan-apa/poster_openpencil.fig \
  --stdin < side-project/artikel-ai-mengajarkan-apa/build_poster_openpencil.js

# 2. Ekspor ke PNG resolusi 2x (1190 × 1684 px)
bun run /home/abuhafi/Project/open-pencil/packages/cli/bin/openpencil.js export \
  side-project/artikel-ai-mengajarkan-apa/poster_openpencil.fig \
  -o side-project/artikel-ai-mengajarkan-apa/poster_openpencil.png -s 2

# 3. Salin untuk FigCraft
cp side-project/artikel-ai-mengajarkan-apa/poster_openpencil.fig \
   side-project/artikel-ai-mengajarkan-apa/poster_openpencil.figcraft
```

### Versi Typst (Alternatif)

```bash
typst compile --font-path /home/abuhafi/Project/Presentasi/sandbox-ootb/other/fonts \
  side-project/artikel-ai-mengajarkan-apa/poster_minimalis_ai.typ \
  side-project/artikel-ai-mengajarkan-apa/poster_minimalis_ai.pdf

typst compile --font-path /home/abuhafi/Project/Presentasi/sandbox-ootb/other/fonts \
  side-project/artikel-ai-mengajarkan-apa/poster_minimalis_ai.typ \
  side-project/artikel-ai-mengajarkan-apa/poster_minimalis_ai.png --format png --ppi 240
```

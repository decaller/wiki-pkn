const fs = await import('node:fs');
const path = await import('node:path');

// Asset paths
const projectDir = '/home/abuhafi/Project/wiki-pkn/side-project/artikel-ai-mengajarkan-apa';
const seedlingImgPath = path.join(projectDir, 'assets/stock_hero_seedling.jpg');

function loadImageHash(filePath) {
  if (fs.existsSync(filePath)) {
    const data = fs.readFileSync(filePath);
    const img = figma.createImage(new Uint8Array(data));
    return img.hash;
  }
  return null;
}

const seedlingImgHash = loadImageHash(seedlingImgPath);

// Clear current page
figma.currentPage.name = "Poster Minimalis Wake-Up Call AI (OpenPencil A4)";
figma.currentPage.children.forEach(c => c.remove());

// Color helper
const c = (r, g, b) => ({ r: r / 255, g: g / 255, b: b / 255 });

const COLOR_BG = c(248, 247, 244);       // Warm paper linen (#F8F7F4)
const COLOR_WHITE = c(255, 255, 255);
const COLOR_DARK = c(15, 23, 42);         // Slate 900 (#0F172A)
const COLOR_BODY = c(51, 65, 85);         // Slate 700 (#334155)
const COLOR_MUTED = c(100, 116, 139);     // Slate 500 (#64748B)
const COLOR_LINE = c(203, 213, 225);      // Slate 300 (#CBD5E1)
const COLOR_LINE_LIGHT = c(226, 232, 240);// Slate 200 (#E2E8F0)
const COLOR_TEAL = c(15, 118, 110);       // Deep Teal 700 (#0F766E)
const COLOR_TEAL_BG = c(240, 253, 250);   // Teal 50 (#F0FDFA)
const COLOR_AMBER = c(180, 83, 9);        // Warm Amber 700 (#B45309)
const COLOR_AMBER_BG = c(254, 243, 199);  // Amber 50 (#FEF3C7)

// Standard A4 dimensions in Figma points
const A4_WIDTH = 595;
const A4_HEIGHT = 842;

// Master Frame (A4 Artboard)
const board = figma.createFrame();
figma.currentPage.appendChild(board);
board.name = "Poster Wake-Up Call AI (A4)";
board.x = 0;
board.y = 0;
board.resize(A4_WIDTH, A4_HEIGHT);
board.fills = [{ type: "SOLID", color: COLOR_BG }];

// Helper: Text Node (Strict Min 14pt)
function createText(parent, opts) {
  const t = figma.createText();
  parent.appendChild(t);
  t.name = opts.name || "Text";
  t.characters = opts.text || "";
  t.x = opts.x || 0;
  t.y = opts.y || 0;
  t.resize(opts.width || 200, opts.height || 24);
  t.textAutoResize = opts.textAutoResize || "NONE";
  
  // Enforce minimum 14pt
  const reqFontSize = opts.fontSize || 14;
  t.fontSize = Math.max(14, reqFontSize);
  
  if (opts.textAlign) t.textAlignHorizontal = opts.textAlign;
  t.fontName = {
    family: opts.fontFamily || "Inter",
    style: opts.fontStyle || "Regular"
  };
  t.fills = [{ type: "SOLID", color: opts.color || COLOR_DARK }];
  return t;
}

// Helper: Rectangle
function createRect(parent, opts) {
  const r = figma.createRectangle();
  parent.appendChild(r);
  r.name = opts.name || "Rect";
  r.x = opts.x || 0;
  r.y = opts.y || 0;
  r.resize(opts.width || 100, opts.height || 100);
  if (opts.radius) r.cornerRadius = opts.radius;
  if (opts.fill) r.fills = [{ type: "SOLID", color: opts.fill }];
  else if (opts.fill === null) r.fills = [];
  if (opts.stroke) {
    r.strokes = [{ type: "SOLID", color: opts.stroke }];
    r.strokeWeight = opts.strokeWeight || 1;
  }
  if (opts.imageHash) {
    r.fills = [{ type: "IMAGE", scaleMode: opts.scaleMode || "FILL", imageHash: opts.imageHash }];
  }
  return r;
}

// Helper: Frame Container
function createFrame(parent, opts) {
  const f = figma.createFrame();
  parent.appendChild(f);
  f.name = opts.name || "Frame";
  f.x = opts.x || 0;
  f.y = opts.y || 0;
  f.resize(opts.width || 100, opts.height || 100);
  if (opts.radius) f.cornerRadius = opts.radius;
  if (opts.fill) f.fills = [{ type: "SOLID", color: opts.fill }];
  else if (opts.fill === null) f.fills = [];
  if (opts.stroke) {
    f.strokes = [{ type: "SOLID", color: opts.stroke }];
    f.strokeWeight = opts.strokeWeight || 1;
  }
  return f;
}

// ==============================================================================
// 1. TOP EDITORIAL BAR
// ==============================================================================
createText(board, {
  name: "Top Tag Left",
  text: "WAKE-UP CALL PENDIDIKAN",
  x: 24,
  y: 22,
  width: 320,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_TEAL,
});

createText(board, {
  name: "Top Tag Right",
  text: "PKN × MUSTAQBAL WAY",
  x: 345,
  y: 22,
  width: 226,
  height: 20,
  fontSize: 14,
  fontStyle: "SemiBold",
  textAlign: "RIGHT",
  color: COLOR_MUTED,
});

// Top Divider
createRect(board, {
  name: "Top Divider",
  x: 24,
  y: 46,
  width: 547,
  height: 2,
  fill: COLOR_DARK,
});

// ==============================================================================
// 2. MONUMENTAL HEADLINE (28PT BOLD)
// ==============================================================================
createText(board, {
  name: "Headline Line 1",
  text: "KALAU AI BISA LEBIH PINTAR,",
  x: 24,
  y: 56,
  width: 547,
  height: 34,
  fontSize: 28,
  fontStyle: "Bold",
  color: COLOR_DARK,
});

createText(board, {
  name: "Headline Line 2",
  text: "KITA MENGAJARKAN APA?",
  x: 24,
  y: 92,
  width: 547,
  height: 34,
  fontSize: 28,
  fontStyle: "Bold",
  color: COLOR_TEAL,
});

// Subtitle / Deck
createText(board, {
  name: "Headline Subtitle",
  text: "Saat mesin menghafal rumus dan menghitung dalam sedetik, bertahan di metode lama\nhanya melatih anak untuk kalah. Saatnya kita bergerak dan berbelok.",
  x: 24,
  y: 132,
  width: 547,
  height: 42,
  fontSize: 14,
  fontStyle: "Medium",
  color: COLOR_BODY,
});

// ==============================================================================
// 3. MINIMALIST HERO VISUAL CARD + QUOTE BANNER
// ==============================================================================
const heroBox = createFrame(board, {
  name: "Hero Visual Container",
  x: 24,
  y: 182,
  width: 547,
  height: 146,
  radius: 8,
  fill: null,
  stroke: COLOR_LINE,
  strokeWeight: 1,
});

if (seedlingImgHash) {
  createRect(heroBox, {
    name: "Hero Photo Fill",
    x: 0,
    y: 0,
    width: 547,
    height: 146,
    radius: 8,
    imageHash: seedlingImgHash,
  });
}

// Quote Banner Overlay at bottom of Hero Card
const quoteBanner = createFrame(heroBox, {
  name: "Hero Quote Overlay",
  x: 0,
  y: 92,
  width: 547,
  height: 54,
  radius: 0,
  fill: c(15, 23, 42), // Solid dark slate (#0F172A)
});

createText(quoteBanner, {
  name: "Hero Quote Text",
  text: "“AI memiliki triliunan rumus, tapi buta arah jika manusia\ntidak memahami pola dan tidak memiliki iman.”",
  x: 16,
  y: 10,
  width: 515,
  height: 36,
  fontSize: 14.5,
  fontStyle: "Medium",
  color: c(248, 250, 252),
});

// ==============================================================================
// 4. MICRO SECTION INDICATOR
// ==============================================================================
createText(board, {
  name: "Section Header",
  text: "DUA PERAN UTAMA GURU & ORANG TUA YANG TAK TERGANTIKAN",
  x: 24,
  y: 338,
  width: 547,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_DARK,
});

// ==============================================================================
// 5. DUA KOLOM PERAN UTAMA (2 CARDS SIDE-BY-SIDE)
// ==============================================================================
const CARD_W = 266;
const CARD_H = 416;
const CARD_Y = 364;

// ------------------------------------------------------------------------------
// KOLOM 1: PENUMBUH IMAN (DEEP TEAL ACCENT)
// ------------------------------------------------------------------------------
const col1 = createFrame(board, {
  name: "Card Col 1: Penumbuh Iman",
  x: 24,
  y: CARD_Y,
  width: CARD_W,
  height: CARD_H,
  radius: 8,
  fill: COLOR_WHITE,
  stroke: COLOR_LINE,
  strokeWeight: 1,
});

// Top colored accent bar
createRect(col1, {
  name: "Col 1 Accent Bar",
  x: 0,
  y: 0,
  width: CARD_W,
  height: 5,
  fill: COLOR_TEAL,
});

// Role Tag Pill
createRect(col1, {
  name: "Col 1 Pill Box",
  x: 14,
  y: 14,
  width: 86,
  height: 24,
  radius: 4,
  fill: COLOR_TEAL_BG,
  stroke: COLOR_TEAL,
  strokeWeight: 1,
});
createText(col1, {
  name: "Col 1 Pill Text",
  text: "PERAN 01",
  x: 18,
  y: 18,
  width: 78,
  height: 18,
  fontSize: 14,
  fontStyle: "Bold",
  textAlign: "CENTER",
  color: COLOR_TEAL,
});

// Card Title
createText(col1, {
  name: "Col 1 Title",
  text: "Penumbuh Iman",
  x: 14,
  y: 44,
  width: 238,
  height: 26,
  fontSize: 20,
  fontStyle: "Bold",
  color: COLOR_DARK,
});

createText(col1, {
  name: "Col 1 Subtitle",
  text: "Hidayah, Qudwah & Imunitas Batin",
  x: 14,
  y: 72,
  width: 238,
  height: 18,
  fontSize: 14,
  fontStyle: "Medium",
  color: COLOR_TEAL,
});

// Divider inside Card 1
createRect(col1, {
  name: "Col 1 Inner Divider",
  x: 14,
  y: 96,
  width: 238,
  height: 1,
  fill: COLOR_LINE_LIGHT,
});

// Poin 1.1: Doa Malam & Hakikat Hidayah
createText(col1, {
  name: "Col 1 Poin 1 Title",
  text: "• Doa Malam & Hakikat Hidayah",
  x: 14,
  y: 106,
  width: 238,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_TEAL,
});
createText(col1, {
  name: "Col 1 Poin 1 Body",
  text: "Hidayah hak mutlak Allah; linangan doa\ndi sepertiga malam & keteladanan jiwa\nmendahului seluruh teknik mengajar.",
  x: 14,
  y: 128,
  width: 238,
  height: 56,
  fontSize: 14,
  fontStyle: "Regular",
  color: COLOR_BODY,
});

// Poin 1.2: Koneksi Sebelum Koreksi
createText(col1, {
  name: "Col 1 Poin 2 Title",
  text: "• Koneksi Sebelum Koreksi",
  x: 14,
  y: 196,
  width: 238,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_TEAL,
});
createText(col1, {
  name: "Col 1 Poin 2 Body",
  text: "Membasuh bejana cinta (Bahasa Hati)\n& merawat fitrah batin, bukan menuntut\nadab lewat bentakan yang melukai.",
  x: 14,
  y: 218,
  width: 238,
  height: 56,
  fontSize: 14,
  fontStyle: "Regular",
  color: COLOR_BODY,
});

// Poin 1.3: Imunitas Batin Muraqabatullah
createText(col1, {
  name: "Col 1 Poin 3 Title",
  text: "• Imunitas Batin (1 ≪ Banyak)",
  x: 14,
  y: 286,
  width: 238,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_TEAL,
});
createText(col1, {
  name: "Col 1 Poin 3 Body",
  text: "Menanamkan muraqabatullah agar anak\nteguh memegang adab di tengah banjir\nsyubhat & arus gawai tanpa batas.",
  x: 14,
  y: 308,
  width: 238,
  height: 56,
  fontSize: 14,
  fontStyle: "Regular",
  color: COLOR_BODY,
});

// ------------------------------------------------------------------------------
// KOLOM 2: PENDIDIK POLA (WARM AMBER ACCENT)
// ------------------------------------------------------------------------------
const col2 = createFrame(board, {
  name: "Card Col 2: Pendidik Pola",
  x: 305,
  y: CARD_Y,
  width: CARD_W,
  height: CARD_H,
  radius: 8,
  fill: COLOR_WHITE,
  stroke: COLOR_LINE,
  strokeWeight: 1,
});

// Top colored accent bar
createRect(col2, {
  name: "Col 2 Accent Bar",
  x: 0,
  y: 0,
  width: CARD_W,
  height: 5,
  fill: COLOR_AMBER,
});

// Role Tag Pill
createRect(col2, {
  name: "Col 2 Pill Box",
  x: 14,
  y: 14,
  width: 86,
  height: 24,
  radius: 4,
  fill: COLOR_AMBER_BG,
  stroke: COLOR_AMBER,
  strokeWeight: 1,
});
createText(col2, {
  name: "Col 2 Pill Text",
  text: "PERAN 02",
  x: 18,
  y: 18,
  width: 78,
  height: 18,
  fontSize: 14,
  fontStyle: "Bold",
  textAlign: "CENTER",
  color: COLOR_AMBER,
});

// Card Title
createText(col2, {
  name: "Col 2 Title",
  text: "Pendidik Pola",
  x: 14,
  y: 44,
  width: 238,
  height: 26,
  fontSize: 20,
  fontStyle: "Bold",
  color: COLOR_DARK,
});

createText(col2, {
  name: "Col 2 Subtitle",
  text: "Pentahapan Fitrah & Wahana Nyata",
  x: 14,
  y: 72,
  width: 238,
  height: 18,
  fontSize: 14,
  fontStyle: "Medium",
  color: COLOR_AMBER,
});

// Divider inside Card 2
createRect(col2, {
  name: "Col 2 Inner Divider",
  x: 14,
  y: 96,
  width: 238,
  height: 1,
  fill: COLOR_LINE_LIGHT,
});

// Poin 2.1: Mengajar To The Point
createText(col2, {
  name: "Col 2 Poin 1 Title",
  text: "• Mengajar To The Point",
  x: 14,
  y: 106,
  width: 238,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_AMBER,
});
createText(col2, {
  name: "Col 2 Poin 1 Body",
  text: "Pahami esensi pola cara kerja ilmu di alam;\nAI adalah pelayan (khadim) kalkulasi,\nbukan penuntun atau imam hidup.",
  x: 14,
  y: 128,
  width: 238,
  height: 56,
  fontSize: 14,
  fontStyle: "Regular",
  color: COLOR_BODY,
});

// Poin 2.2: Pentahapan Belajar Fitrah
createText(col2, {
  name: "Col 2 Poin 2 Title",
  text: "• Pentahapan Belajar Fitrah",
  x: 14,
  y: 196,
  width: 238,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_AMBER,
});
createText(col2, {
  name: "Col 2 Poin 2 Body",
  text: "Taqlid (0–7 th / Suka) → Sandbox\n(7–10 th / Bisa) → Out of the Box\n(10+ th / Berguna nyata bagi umat).",
  x: 14,
  y: 218,
  width: 238,
  height: 56,
  fontSize: 14,
  fontStyle: "Regular",
  color: COLOR_BODY,
});

// Poin 2.3: Fardhu 'Ain vs Kifayah
createText(col2, {
  name: "Col 2 Poin 3 Title",
  text: "• Fardhu 'Ain vs Kifayah",
  x: 14,
  y: 286,
  width: 238,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_AMBER,
});
createText(col2, {
  name: "Col 2 Poin 3 Body",
  text: "Wajib seragam dalam iman & adab (Sholih);\nnamun lejitkan 6 bakat terkuat untuk\nmemberi solusi bagi zaman (Muslih).",
  x: 14,
  y: 308,
  width: 238,
  height: 56,
  fontSize: 14,
  fontStyle: "Regular",
  color: COLOR_BODY,
});

// ==============================================================================
// 6. BOTTOM FOOTER STATEMENT
// ==============================================================================
createRect(board, {
  name: "Bottom Divider",
  x: 24,
  y: 792,
  width: 547,
  height: 1.5,
  fill: COLOR_DARK,
});

createText(board, {
  name: "Footer Callout",
  text: "Jangan latih anak bersaing dengan kalkulator. Didik mereka memimpin teknologi.",
  x: 24,
  y: 802,
  width: 440,
  height: 20,
  fontSize: 14,
  fontStyle: "Bold",
  color: COLOR_DARK,
});

createText(board, {
  name: "Footer Brand",
  text: "Wiki PKN • Insan Taqwa",
  x: 430,
  y: 802,
  width: 141,
  height: 20,
  fontSize: 14,
  fontStyle: "SemiBold",
  textAlign: "RIGHT",
  color: COLOR_MUTED,
});

console.log("Successfully rebuilt OpenPencil Poster synchronized with Ustadz Abdul Khaliq style!");

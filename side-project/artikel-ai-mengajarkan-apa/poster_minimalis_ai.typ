#set document(
  title: "Wake-Up Call AI: Kalau AI Lebih Pintar, Lalu Kita Mengajarkan Apa?",
  author: "Pendidikan Karakter Nabawiyah (PKN) • Mustaqbal Way",
)

// Palet Minimalis Editorial Horizon
#let bg-paper = rgb("#F8F7F4")
#let ink-dark = rgb("#0F172A")
#let ink-body = rgb("#334155")
#let ink-muted = rgb("#64748B")
#let line-subtle = rgb("#CBD5E1")

#let teal-accent = rgb("#0F766E")
#let amber-accent = rgb("#B45309")

#set page(
  paper: "a4",
  margin: (x: 16mm, top: 13mm, bottom: 13mm),
  fill: bg-paper,
)

#set text(
  font: ("Montserrat", "Noto Sans", "DejaVu Sans"),
  fill: ink-dark,
  size: 13pt,
  lang: "id",
)

#set par(
  justify: false,
  leading: 0.52em,
  spacing: 0.65em,
)

// Helper untuk butir poin di dalam kartu tanpa spasi paragraf berlebih
#let pillar-point(title, desc, accent-color) = {
  stack(
    spacing: 1.8mm,
    text(size: 12.8pt, weight: "bold", fill: accent-color)[#title],
    text(size: 11.2pt, weight: "regular", fill: ink-body)[#desc],
  )
}

// =========================================================================
// 1. TOP EDITORIAL BAR
// =========================================================================
#grid(
  columns: (1fr, auto),
  align: (left + horizon, right + horizon),
  text(size: 10pt, weight: "bold", tracking: 0.14em, fill: teal-accent)[
    WAKE-UP CALL PENDIDIKAN
  ],
  text(size: 10pt, weight: "semibold", tracking: 0.06em, fill: ink-muted)[
    PKN × MUSTAQBAL WAY
  ]
)

#v(2mm)
#line(length: 100%, stroke: 1.5pt + ink-dark)
#v(4mm)

// =========================================================================
// 2. MONUMENTAL HEADLINE (TEKS BESAR & TEGAS)
// =========================================================================
#stack(
  spacing: 2.5mm,
  text(size: 29.5pt, weight: "black", fill: ink-dark, tracking: -0.02em)[
    KALAU AI BISA LEBIH PINTAR,
  ],
  text(size: 29.5pt, weight: "black", fill: teal-accent, tracking: -0.02em)[
    KITA MENGAJARKAN APA?
  ]
)

#v(3.5mm)

#text(size: 13pt, weight: "medium", fill: ink-body)[
  Saat mesin mampu menghafal rumus dan menghitung dalam sedetik, bertahan di metode lama hanya melatih anak untuk kalah. *Sudah saatnya kita bergerak dan berbelok.*
]

#v(4.5mm)

// =========================================================================
// 3. MINIMALIST HERO STOCK IMAGE + QUOTE OVERLAY
// =========================================================================
#box(
  width: 100%,
  height: 57mm,
  radius: 6pt,
  clip: true,
  stroke: 0.75pt + line-subtle,
)[
  #image("assets/stock_hero_seedling.jpg", width: 100%, height: 100%, fit: "cover")
  #place(
    bottom + left,
    dx: 0mm,
    dy: 0mm,
    rect(
      width: 100%,
      fill: rgb(15, 23, 42, 225),
      inset: (x: 14pt, y: 9.5pt),
    )[
      #text(size: 11.8pt, weight: "medium", fill: rgb("#F8FAFC"))[
        “AI punya triliunan rumus, tapi buta arah jika manusia tidak memahami *pola* dan tidak memiliki *iman*.”
      ]
    ]
  )
]

#v(5mm)

// =========================================================================
// 4. DUA PERAN UTAMA GURU (2 KOLOM MINIMALIS, TEKS BESAR)
// =========================================================================
#grid(
  columns: (1fr, 1fr),
  gutter: 6mm,

  // KOLOM 1: PENUMBUH IMAN
  rect(
    width: 100%,
    height: 116mm,
    fill: rgb("#FFFFFF"),
    stroke: (top: 4.5pt + teal-accent, rest: 0.75pt + line-subtle),
    radius: (bottom: 6pt),
    inset: (x: 14pt, top: 13pt, bottom: 13pt),
  )[
    #stack(
      spacing: 3.2mm,
      text(size: 10.5pt, weight: "bold", tracking: 0.12em, fill: teal-accent)[
        PERAN 01
      ],
      text(size: 19.5pt, weight: "extrabold", fill: ink-dark)[
        Penumbuh Iman
      ],
      line(length: 100%, stroke: 0.75pt + line-subtle),
      stack(
        spacing: 5mm,
        pillar-point(
          "• Doa Malam & Hidayah",
          [Hidayah hak mutlak Allah; linangan doa malam & keteladanan jiwa mendahului seluruh metode.],
          teal-accent,
        ),
        pillar-point(
          "• Koneksi Sebelum Koreksi",
          [Membasuh bejana cinta (_Bahasa Hati_) & kuatkan watak dasar, bukan menuntut adab secara kaku.],
          teal-accent,
        ),
        pillar-point(
          "• Imunitas Batin (1 ≪ N)",
          [Menancapkan _muraqabatullah_ agar anak teguh memegang adab di tengah banjir syubhat digital.],
          teal-accent,
        ),
      )
    )
  ],

  // KOLOM 2: PENDIDIK POLA
  rect(
    width: 100%,
    height: 116mm,
    fill: rgb("#FFFFFF"),
    stroke: (top: 4.5pt + amber-accent, rest: 0.75pt + line-subtle),
    radius: (bottom: 6pt),
    inset: (x: 14pt, top: 13pt, bottom: 13pt),
  )[
    #stack(
      spacing: 3.2mm,
      text(size: 10.5pt, weight: "bold", tracking: 0.12em, fill: amber-accent)[
        PERAN 02
      ],
      text(size: 19.5pt, weight: "extrabold", fill: ink-dark)[
        Pendidik Pola
      ],
      line(length: 100%, stroke: 0.75pt + line-subtle),
      stack(
        spacing: 5mm,
        pillar-point(
          [• Mengajar _To The Point_],
          [Pahami esensi pola cara kerja ilmu di alam nyata; AI adalah pelayan (_khadim_), bukan penuntun.],
          amber-accent,
        ),
        pillar-point(
          [• Pentahapan Belajar Fitrah],
          [_Taqlid_ (0–7 th / Suka) $->$ _Sandbox_ (7–10 th / Bisa) $->$ _Out of the Box_ (10+ th / Berguna).],
          amber-accent,
        ),
        pillar-point(
          [• Fardhu 'Ain vs Kifayah],
          [Wajib seragam dalam iman & adab (_Sholih_); lejitkan 6 bakat terkuat untuk peradaban (_Muslih_).],
          amber-accent,
        ),
      )
    )
  ]
)

#v(1fr)

// =========================================================================
// 5. BOTTOM FOOTER STATEMENT
// =========================================================================
#line(length: 100%, stroke: 1.2pt + ink-dark)
#v(2.5mm)
#grid(
  columns: (1fr, auto),
  align: (left + horizon, right + horizon),
  text(size: 10.8pt, weight: "bold", fill: ink-dark)[
    Jangan latih anak bersaing dengan kalkulator. Didik mereka memimpin teknologi.
  ],
  text(size: 9.8pt, weight: "semibold", fill: ink-muted)[
    Wiki PKN • Insan Taqwa
  ]
)

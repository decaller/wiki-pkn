import test from "node:test"
import assert from "node:assert/strict"
import { h } from "preact"
import renderToString from "preact-render-to-string"
import OutlineNav from "./OutlineNav"
import { QuartzComponentProps } from "../../../../quartz/components/types"

// The plugin build transforms JSX with the classic Preact factory.
;(globalThis as typeof globalThis & { React: { createElement: typeof h } }).React = { createElement: h }
function renderNav(files: Array<{ slug: string; title: string }>, current = "index") {
  const allFiles = files.map(({ slug, title }) => ({ slug, frontmatter: { title } }))
  return renderToString(
    OutlineNav()({
      fileData: { slug: current },
      allFiles,
    } as QuartzComponentProps),
  )
}

function renderedFirasat(html: string): string {
  return html.match(/<li class="outline-file">(?:<a [^>]*>|<span [^>]*>)Firasat<\/[^>]+><\/li>/)?.[0] ?? ""
}

test("ambiguous substring matches do not render a misleading Firasat link", () => {
  const first = { slug: "example/firasat-a", title: "Panduan Firasat A" }
  const second = { slug: "example/firasat-b", title: "Panduan Firasat B" }
  for (const files of [[first, second], [second, first]]) {
    const html = renderNav(files)
    assert.match(renderedFirasat(html), /<span class="unlinked-item">Firasat<\/span>/)
  }
})

test("a unique substring match still links to its page", () => {
  const html = renderNav([{ slug: "example/firasat-a", title: "Panduan Firasat A" }])
  assert.match(renderedFirasat(html), /data-slug="example\/firasat-a"/)
})

test("an exact title outranks a competing substring match", () => {
  const html = renderNav([
    { slug: "example/firasat-a", title: "Panduan Firasat A" },
    { slug: "example/firasat", title: "Firasat" },
  ])
  assert.match(renderedFirasat(html), /data-slug="example\/firasat"/)
})

test("duplicate exact titles do not depend on input order", () => {
  const first = { slug: "example/firasat-a", title: "Firasat" }
  const second = { slug: "example/firasat-b", title: "Firasat" }
  for (const files of [[first, second], [second, first]]) {
    assert.match(renderedFirasat(renderNav(files)), /<span class="unlinked-item">Firasat<\/span>/)
  }
})

test("TB-40 number prefix does not choose a page when two candidates share it", () => {
  const files = [
    { slug: "tb40/01-himmah", title: "Another first trait" },
    { slug: "tb40/01-other", title: "Another first trait variant" },
  ]
  for (const ordered of [files, [...files].reverse()]) {
    const html = renderNav(ordered)
    assert.match(html, /<span class="unlinked-item">01\. Himmah \(Bercita-Cita Tinggi\)<\/span>/)
  }
})

test("explicit slug links the real Tazkiyatun Nafs nav entry", () => {
  const slug = "paradigma---implementasi-pkn/dokumen-pendidikan-karakter-nabawiyah/paradigma--and--implementasi/implementasi/internal--and--eksternal/tazkiyatun-nafs"
  const html = renderNav([
    { slug: "other/tazkiyatun-nafs", title: "Tazkiyatun Nafs" },
    { slug, title: "Tazkiyatun Nafs" },
  ], slug)
  assert.match(html, new RegExp(`data-slug="${slug}"[^>]*>Tazkiyatun Nafs<`))
  assert.match(html, /class="folder-outer open"/)
})

test("an unavailable explicit slug stays unlinked instead of choosing another same-title page", () => {
  const html = renderNav([{ slug: "other/tazkiyatun-nafs", title: "Tazkiyatun Nafs" }])
  assert.match(html, /<span class="unlinked-item">Tazkiyatun Nafs<\/span>/)
})

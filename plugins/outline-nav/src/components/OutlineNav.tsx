import fs from "fs"
import path from "path"
import { JSX } from "preact"
import { resolveRelative } from "@quartz-community/utils"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../../../../quartz/components/types"
import { NavItem, NavStructure, OutlineNavOptions } from "../types"

function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/&/g, "-and-")
    .replace(/[\s\(\)]+/g, "-")
    .replace(/[^a-z0-9\-]/g, "")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "")
}

function buildSlugMap(allFiles: QuartzComponentProps["allFiles"]): Map<string, string> {
  const map = new Map<string, string>()
  
  // Sort so non-tag pages are processed after tag pages, ensuring real content takes priority
  const sortedFiles = [...allFiles].sort((a, b) => {
    const aIsTag = a.slug?.startsWith("tags/") ? 1 : 0
    const bIsTag = b.slug?.startsWith("tags/") ? 1 : 0
    return bIsTag - aIsTag // tags first, then real content overrides them
  })

  for (const file of sortedFiles) {
    if (!file.slug) continue
    const title = file.frontmatter?.title as string | undefined
    if (title) {
      map.set(title.toLowerCase().trim(), file.slug)
    }
    const aliases = file.frontmatter?.aliases as string[] | undefined
    if (Array.isArray(aliases)) {
      for (const alias of aliases) {
        if (typeof alias === "string") {
          map.set(alias.toLowerCase().trim(), file.slug)
        }
      }
    }
    const slugParts = file.slug.split("/")
    const lastPart = slugParts[slugParts.length - 1]
    map.set(lastPart.toLowerCase(), file.slug)
    if (lastPart === "index" && slugParts.length > 1) {
      map.set(slugParts[slugParts.length - 2].toLowerCase(), file.slug)
    }
  }
  return map
}

function resolveNodeSlug(
  title: string,
  slugMap: Map<string, string>,
  allFiles: QuartzComponentProps["allFiles"],
): string | null {
  const tLow = title.toLowerCase().trim()
  if (tLow === "home" || tLow === "beranda" || tLow === "beranda utama") {
    return "index"
  }
  if (slugMap.has(tLow)) {
    return slugMap.get(tLow)!
  }

  const sTitle = slugify(title)
  if (slugMap.has(sTitle)) {
    return slugMap.get(sTitle)!
  }

  for (const file of allFiles) {
    if (!file.slug) continue
    const parts = file.slug.split("/")
    const last = parts[parts.length - 1]
    const prev = parts.length > 1 ? parts[parts.length - 2] : ""
    if (last === sTitle || last === sTitle + "-pkn" || (last === "index" && prev === sTitle)) {
      return file.slug
    }
  }

  for (const file of allFiles) {
    if (!file.slug) continue
    const fTitle = (file.frontmatter?.title as string | undefined)?.toLowerCase().trim()
    if (fTitle && fTitle.includes(tLow)) {
      return file.slug
    }
    if (file.slug.includes(sTitle)) {
      return file.slug
    }
  }

  return null
}

function hasActiveDescendant(item: NavItem, activeSlug: string, slugMap: Map<string, string>, allFiles: QuartzComponentProps["allFiles"]): boolean {
  const slug = resolveNodeSlug(item.title, slugMap, allFiles)
  if (slug === activeSlug) return true
  if (item.children) {
    for (const child of item.children) {
      if (hasActiveDescendant(child, activeSlug, slugMap, allFiles)) return true
    }
  }
  return false
}

export default ((userOpts?: OutlineNavOptions) => {
  const OutlineNav: QuartzComponent = (props: QuartzComponentProps) => {
    const { fileData, allFiles } = props
    const currentSlug = fileData.slug ?? "index"

    let navStructure: NavStructure | null = null
    try {
      const navPath = path.join(process.cwd(), "nav_structure.json")
      if (fs.existsSync(navPath)) {
        const raw = fs.readFileSync(navPath, "utf-8")
        navStructure = JSON.parse(raw) as NavStructure
      }
    } catch {
      navStructure = null
    }

    if (!navStructure) {
      return <div class="outline-nav">No navigation structure found</div>
    }

    const slugMap = buildSlugMap(allFiles)

    const renderItem = (item: NavItem, depth: number, parentPath: string): JSX.Element => {
      const nodeSlug = resolveNodeSlug(item.title, slugMap, allFiles)
      const isFolder = item.children && item.children.length > 0
      const currentPath = parentPath ? `${parentPath}/${item.title}` : item.title
      const isActive = nodeSlug ? nodeSlug === currentSlug : false
      const isAncestor = isFolder ? hasActiveDescendant(item, currentSlug, slugMap, allFiles) : false
      const defaultOpen = isAncestor || depth < 1

      if (isFolder) {
        return (
          <li class="outline-folder" data-folderpath={currentPath}>
            <div class="outline-folder-container">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2.5"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="folder-icon"
              >
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
              {nodeSlug ? (
                <a
                  href={resolveRelative(fileData.slug!, nodeSlug as any)}
                  class={`outline-folder-title ${isActive ? "active" : ""}`}
                  data-slug={nodeSlug}
                >
                  {item.title}
                </a>
              ) : (
                <span class="outline-folder-title">{item.title}</span>
              )}
            </div>
            <div class={`folder-outer ${defaultOpen ? "open" : ""}`}>
              <ul class="outline-nav-sublist">
                {item.children!.map((child) => renderItem(child, depth + 1, currentPath))}
              </ul>
            </div>
          </li>
        )
      }

      return (
        <li class="outline-file">
          {nodeSlug ? (
            <a
              href={resolveRelative(fileData.slug!, nodeSlug as any)}
              class={isActive ? "active" : ""}
              data-slug={nodeSlug}
            >
              {item.title}
            </a>
          ) : (
            <span class="unlinked-item">{item.title}</span>
          )}
        </li>
      )
    }

    const collections = Object.values(navStructure)

    return (
      <div class="outline-nav nav-files-container" id="outline-nav-root">
        <button
          type="button"
          class="outline-nav-toggle desktop-outline-nav"
          aria-label="Toggle Outline Navigation"
        >
          <h2>{userOpts?.title ?? "Navigasi Dokumen"}</h2>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="14"
            height="14"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="fold"
          >
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </button>

        <div class="outline-nav-content">
          <ul class="outline-nav-ul">
            {collections.map((col) => (
              <li class="outline-collection" key={col.collection.name}>
                <div class="collection-header">
                  <span>{col.collection.name}</span>
                </div>
                <ul class="outline-collection-structure">
                  {col.structure.map((item) => renderItem(item, 0, col.collection.name))}
                </ul>
              </li>
            ))}
          </ul>
        </div>
      </div>
    )
  }

  OutlineNav.afterDOMLoaded = `
(() => {
  function initOutlineNav() {
    const root = document.getElementById("outline-nav-root")
    if (!root) return

    const navContent = root.querySelector(".outline-nav-content")
    if (!navContent) return

    // 1. Restore scroll position
    const savedScroll = sessionStorage.getItem("outlineNavScrollTop")
    if (savedScroll !== null) {
      navContent.scrollTop = parseInt(savedScroll, 10)
    } else {
      const activeLink = navContent.querySelector("a.active")
      if (activeLink) {
        activeLink.scrollIntoView({ block: "nearest", behavior: "smooth" })
      }
    }

    // 2. Restore folder collapse/expand states from localStorage
    let folderStates = {}
    try {
      folderStates = JSON.parse(localStorage.getItem("outlineNavFolders") || "{}")
    } catch {}

    const folders = root.querySelectorAll(".outline-folder")
    folders.forEach(folder => {
      const path = folder.getAttribute("data-folderpath")
      const outer = folder.querySelector(":scope > .folder-outer")
      if (!path || !outer) return

      if (folderStates[path] !== undefined) {
        if (folderStates[path]) {
          outer.classList.add("open")
        } else {
          outer.classList.remove("open")
        }
      }
    })

    // 3. Ensure active item's ancestors are always expanded
    const currentActive = root.querySelector("a.active")
    if (currentActive) {
      let cur = currentActive.closest(".outline-folder")
      while (cur) {
        const outer = cur.querySelector(":scope > .folder-outer")
        if (outer) outer.classList.add("open")
        cur = cur.parentElement ? cur.parentElement.closest(".outline-folder") : null
      }
    }

    // 4. Folder toggle clicks
    folders.forEach(folder => {
      const icon = folder.querySelector(":scope > .outline-folder-container > .folder-icon")
      const path = folder.getAttribute("data-folderpath")
      const outer = folder.querySelector(":scope > .folder-outer")
      if (!icon || !outer || !path) return

      const toggle = (e) => {
        e.stopPropagation()
        const isOpen = outer.classList.toggle("open")
        try {
          folderStates = JSON.parse(localStorage.getItem("outlineNavFolders") || "{}")
          folderStates[path] = isOpen
          localStorage.setItem("outlineNavFolders", JSON.stringify(folderStates))
        } catch {}
      }

      icon.onclick = toggle
    })

    // 5. Header toggle click
    const headerToggle = root.querySelector(".outline-nav-toggle")
    if (headerToggle) {
      headerToggle.onclick = (e) => {
        e.stopPropagation()
        root.classList.toggle("collapsed")
      }
    }
  }

  document.addEventListener("prenav", () => {
    const navContent = document.querySelector(".outline-nav-content")
    if (navContent) {
      sessionStorage.setItem("outlineNavScrollTop", navContent.scrollTop.toString())
    }
  })

  document.addEventListener("nav", initOutlineNav)
  document.addEventListener("render", initOutlineNav)
  if (document.readyState === "complete" || document.readyState === "interactive") {
    initOutlineNav()
  }
})()
`

  OutlineNav.css = `
.outline-nav {
  display: flex;
  flex-direction: column;
  overflow-y: hidden;
  min-height: 1.2rem;
  flex: 0 1 auto;
  margin-top: 0.5rem;
}

.outline-nav.collapsed {
  flex: 0 1 1.2rem;
}

.outline-nav.collapsed .outline-nav-content {
  display: none;
}

.outline-nav.collapsed .fold {
  transform: rotateZ(-90deg);
}

.outline-nav .fold {
  margin-left: 0.5rem;
  transition: transform 0.25s ease;
  opacity: 0.8;
}

.outline-nav button.desktop-outline-nav {
  background-color: transparent;
  border: none;
  text-align: left;
  cursor: pointer;
  padding: 0;
  color: var(--dark);
  display: flex;
  align-items: center;
  margin-bottom: 0.6rem;
}

.outline-nav button.desktop-outline-nav h2 {
  font-size: 0.95rem;
  display: inline-block;
  margin: 0;
  font-weight: 700;
  color: var(--darkgray);
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.outline-nav-content {
  list-style: none;
  overflow-y: auto;
  overscroll-behavior: contain;
  max-height: calc(100vh - 12rem);
  padding-right: 6px;
}

.outline-nav-content::-webkit-scrollbar {
  width: 4px;
}

.outline-nav-content::-webkit-scrollbar-track {
  background: transparent;
}

.outline-nav-content::-webkit-scrollbar-thumb {
  background: var(--lightgray);
  border-radius: 4px;
}

.outline-nav-content::-webkit-scrollbar-thumb:hover {
  background: var(--gray);
}

.outline-nav-ul, .outline-nav-content ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.collection-header {
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--gray);
  margin-bottom: 0.35rem;
  letter-spacing: 0.05em;
}

.outline-nav-content .folder-outer > ul {
  overflow: hidden;
  margin-left: 5px;
  padding-left: 0.75rem;
  border-left: 1px solid var(--lightgray);
}

.outline-nav-content li {
  margin: 0.2rem 0;
}

.outline-nav-content li > a {
  color: var(--dark);
  opacity: 0.8;
  font-size: 0.88rem;
  line-height: 1.45rem;
  display: inline-block;
  text-decoration: none;
  transition: color 0.2s ease, opacity 0.2s ease;
}

.outline-nav-content li > a:hover {
  opacity: 1;
  color: var(--secondary);
}

.outline-nav-content li > a.active {
  opacity: 1;
  color: var(--secondary);
  font-weight: 700;
}

.outline-folder-container {
  display: flex;
  align-items: center;
  user-select: none;
}

.outline-folder-container .folder-icon {
  margin-right: 5px;
  color: var(--secondary);
  cursor: pointer;
  transition: transform 0.2s ease;
  flex-shrink: 0;
}

li.outline-folder:not(:has(> .folder-outer.open)) > .outline-folder-container .folder-icon {
  transform: rotate(-90deg);
}

.outline-folder-title {
  color: var(--dark);
  font-size: 0.9rem;
  font-weight: 600;
  line-height: 1.5rem;
  display: inline-block;
  text-decoration: none;
  opacity: 0.9;
  transition: color 0.2s ease;
}

.outline-folder-title:hover {
  color: var(--secondary);
  opacity: 1;
}

.outline-folder-title.active {
  color: var(--secondary);
  font-weight: 700;
  opacity: 1;
}

.unlinked-item {
  color: var(--gray);
  font-size: 0.88rem;
  line-height: 1.45rem;
}

.folder-outer {
  display: none;
}

.folder-outer.open {
  display: block;
}
`

  return OutlineNav
}) as QuartzComponentConstructor<OutlineNavOptions>

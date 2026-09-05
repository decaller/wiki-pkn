// plugins/outline-nav/src/components/OutlineNav.tsx
import fs from "fs";
import path from "path";
import { resolveRelative } from "@quartz-community/utils";
import { jsx, jsxs } from "preact/jsx-runtime";
function slugify(text) {
  return text.toLowerCase().replace(/&/g, "-and-").replace(/[\s\(\)]+/g, "-").replace(/[^a-z0-9\-]/g, "").replace(/-+/g, "-").replace(/^-|-$/g, "");
}
function buildSlugMap(allFiles) {
  const map = /* @__PURE__ */ new Map();
  const sortedFiles = [...allFiles].sort((a, b) => {
    const aIsTag = a.slug?.startsWith("tags/") ? 1 : 0;
    const bIsTag = b.slug?.startsWith("tags/") ? 1 : 0;
    return bIsTag - aIsTag;
  });
  for (const file of sortedFiles) {
    if (!file.slug) continue;
    const title = file.frontmatter?.title;
    if (title) {
      map.set(title.toLowerCase().trim(), file.slug);
    }
    const aliases = file.frontmatter?.aliases;
    if (Array.isArray(aliases)) {
      for (const alias of aliases) {
        if (typeof alias === "string") {
          map.set(alias.toLowerCase().trim(), file.slug);
        }
      }
    }
    const slugParts = file.slug.split("/");
    const lastPart = slugParts[slugParts.length - 1];
    map.set(lastPart.toLowerCase(), file.slug);
    if (lastPart === "index" && slugParts.length > 1) {
      map.set(slugParts[slugParts.length - 2].toLowerCase(), file.slug);
    }
  }
  return map;
}
function resolveNodeSlug(title, slugMap, allFiles) {
  const tLow = title.toLowerCase().trim();
  if (tLow === "home" || tLow === "beranda" || tLow === "beranda utama") {
    return "index";
  }
  if (slugMap.has(tLow)) {
    return slugMap.get(tLow);
  }
  const tbMatch = title.match(/^0?(\d{1,2})[\.\s\-]/);
  if (tbMatch) {
    const num = tbMatch[1].padStart(2, "0");
    for (const file of allFiles) {
      if (!file.slug) continue;
      const last = file.slug.split("/").pop() ?? "";
      if (last.startsWith(`${num}-`) && file.slug.toLowerCase().includes("tb40")) {
        return file.slug;
      }
    }
  }
  const sTitle = slugify(title);
  if (slugMap.has(sTitle)) {
    return slugMap.get(sTitle);
  }
  for (const file of allFiles) {
    if (!file.slug) continue;
    const parts = file.slug.split("/");
    const last = parts[parts.length - 1];
    const prev = parts.length > 1 ? parts[parts.length - 2] : "";
    if (last === sTitle || last === sTitle + "-pkn" || last === "index" && prev === sTitle) {
      return file.slug;
    }
  }
  for (const file of allFiles) {
    if (!file.slug) continue;
    const fTitle = file.frontmatter?.title?.toLowerCase().trim();
    if (fTitle && fTitle.includes(tLow)) {
      return file.slug;
    }
    if (file.slug.includes(sTitle)) {
      return file.slug;
    }
  }
  return null;
}
function hasActiveDescendant(item, activeSlug, slugMap, allFiles) {
  const slug = resolveNodeSlug(item.title, slugMap, allFiles);
  if (slug === activeSlug) return true;
  if (item.children) {
    for (const child of item.children) {
      if (hasActiveDescendant(child, activeSlug, slugMap, allFiles)) return true;
    }
  }
  return false;
}
var OutlineNav_default = ((userOpts) => {
  const OutlineNav = (props) => {
    const { fileData, allFiles } = props;
    const currentSlug = fileData.slug ?? "index";
    let navStructure = null;
    try {
      const navPath = path.join(process.cwd(), "nav_structure.json");
      if (fs.existsSync(navPath)) {
        const raw = fs.readFileSync(navPath, "utf-8");
        navStructure = JSON.parse(raw);
      }
    } catch {
      navStructure = null;
    }
    if (!navStructure) {
      return /* @__PURE__ */ jsx("div", { class: "outline-nav", children: "No navigation structure found" });
    }
    const slugMap = buildSlugMap(allFiles);
    const renderItem = (item, depth, parentPath) => {
      const nodeSlug = resolveNodeSlug(item.title, slugMap, allFiles);
      const isFolder = item.children && item.children.length > 0;
      const currentPath = parentPath ? `${parentPath}/${item.title}` : item.title;
      const isActive = nodeSlug ? nodeSlug === currentSlug : false;
      const isAncestor = isFolder ? hasActiveDescendant(item, currentSlug, slugMap, allFiles) : false;
      const defaultOpen = isAncestor || depth < 1;
      if (isFolder) {
        return /* @__PURE__ */ jsxs("li", { class: "outline-folder", "data-folderpath": currentPath, children: [
          /* @__PURE__ */ jsxs("div", { class: "outline-folder-container", children: [
            /* @__PURE__ */ jsx(
              "svg",
              {
                xmlns: "http://www.w3.org/2000/svg",
                width: "14",
                height: "14",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                "stroke-width": "2.5",
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                class: "folder-icon",
                children: /* @__PURE__ */ jsx("polyline", { points: "6 9 12 15 18 9" })
              }
            ),
            nodeSlug ? /* @__PURE__ */ jsx(
              "a",
              {
                href: resolveRelative(fileData.slug, nodeSlug),
                class: `outline-folder-title ${isActive ? "active" : ""}`,
                "data-slug": nodeSlug,
                children: item.title
              }
            ) : /* @__PURE__ */ jsx("span", { class: "outline-folder-title", children: item.title })
          ] }),
          /* @__PURE__ */ jsx("div", { class: `folder-outer ${defaultOpen ? "open" : ""}`, children: /* @__PURE__ */ jsx("ul", { class: "outline-nav-sublist", children: item.children.map((child) => renderItem(child, depth + 1, currentPath)) }) })
        ] });
      }
      return /* @__PURE__ */ jsx("li", { class: "outline-file", children: nodeSlug ? /* @__PURE__ */ jsx(
        "a",
        {
          href: resolveRelative(fileData.slug, nodeSlug),
          class: isActive ? "active" : "",
          "data-slug": nodeSlug,
          children: item.title
        }
      ) : /* @__PURE__ */ jsx("span", { class: "unlinked-item", children: item.title }) });
    };
    const collections = Object.values(navStructure);
    return /* @__PURE__ */ jsxs("div", { class: "outline-nav nav-files-container", id: "outline-nav-root", children: [
      /* @__PURE__ */ jsxs(
        "button",
        {
          type: "button",
          class: "outline-nav-toggle desktop-outline-nav",
          "aria-label": "Toggle Outline Navigation",
          children: [
            /* @__PURE__ */ jsxs("div", { class: "outline-nav-header-left", children: [
              /* @__PURE__ */ jsxs(
                "svg",
                {
                  xmlns: "http://www.w3.org/2000/svg",
                  width: "15",
                  height: "15",
                  viewBox: "0 0 24 24",
                  fill: "none",
                  stroke: "currentColor",
                  "stroke-width": "2",
                  "stroke-linecap": "round",
                  "stroke-linejoin": "round",
                  class: "outline-header-icon",
                  children: [
                    /* @__PURE__ */ jsx("rect", { x: "3", y: "3", width: "7", height: "7" }),
                    /* @__PURE__ */ jsx("rect", { x: "14", y: "3", width: "7", height: "7" }),
                    /* @__PURE__ */ jsx("rect", { x: "14", y: "14", width: "7", height: "7" }),
                    /* @__PURE__ */ jsx("rect", { x: "3", y: "14", width: "7", height: "7" })
                  ]
                }
              ),
              /* @__PURE__ */ jsx("h2", { children: userOpts?.title ?? "Navigasi Dokumen" })
            ] }),
            /* @__PURE__ */ jsx(
              "svg",
              {
                xmlns: "http://www.w3.org/2000/svg",
                width: "14",
                height: "14",
                viewBox: "0 0 24 24",
                fill: "none",
                stroke: "currentColor",
                "stroke-width": "2.5",
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                class: "fold",
                children: /* @__PURE__ */ jsx("polyline", { points: "6 9 12 15 18 9" })
              }
            )
          ]
        }
      ),
      /* @__PURE__ */ jsx("div", { class: "outline-nav-content", children: /* @__PURE__ */ jsx("ul", { class: "outline-nav-ul", children: collections.map((col) => /* @__PURE__ */ jsxs("li", { class: "outline-collection", children: [
        /* @__PURE__ */ jsx("div", { class: "collection-header", children: /* @__PURE__ */ jsx("span", { children: col.collection.name }) }),
        /* @__PURE__ */ jsx("ul", { class: "outline-collection-structure", children: col.structure.map((item) => renderItem(item, 0, col.collection.name)) })
      ] }, col.collection.name)) }) })
    ] });
  };
  OutlineNav.afterDOMLoaded = `
(() => {
  function initOutlineNav() {
    const root = document.getElementById("outline-nav-root")
    if (!root) return

    const navContent = root.querySelector(".outline-nav-content")
    if (!navContent) return

    const isMobile = window.innerWidth <= 800

    // On mobile, collapse by default on page load to keep reading area clean
    if (isMobile) {
      root.classList.add("collapsed")
    }

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
`;
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
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
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
  justify-content: space-between;
  margin-bottom: 0.6rem;
  width: 100%;
}

.outline-nav-header-left {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.outline-nav-header-left .outline-header-icon {
  color: var(--secondary);
  opacity: 0.85;
  flex-shrink: 0;
}

.outline-nav button.desktop-outline-nav h2 {
  font-size: 0.85rem;
  display: inline-block;
  margin: 0;
  font-weight: 700;
  color: var(--darkgray);
  letter-spacing: 0.04em;
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
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--gray);
  margin-top: 0.6rem;
  margin-bottom: 0.35rem;
  letter-spacing: 0.06em;
}

.outline-collection:first-child .collection-header {
  margin-top: 0;
}

.outline-nav-content .folder-outer > ul {
  overflow: hidden;
  margin-left: 6px;
  padding-left: 0.75rem;
  border-left: 1px solid var(--lightgray);
}

.outline-nav-content li {
  margin: 0.15rem 0;
}

.outline-nav-content li > a {
  color: var(--dark);
  opacity: 0.82;
  font-size: 0.88rem;
  line-height: 1.45rem;
  display: inline-block;
  text-decoration: none;
  padding: 0.15rem 0.35rem;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.outline-nav-content li > a:hover {
  opacity: 1;
  color: var(--secondary);
  background-color: var(--highlight);
}

.outline-nav-content li > a.active {
  opacity: 1;
  color: var(--secondary);
  font-weight: 700;
  background-color: var(--highlight);
}

.outline-folder-container {
  display: flex;
  align-items: center;
  user-select: none;
}

.outline-folder-container .folder-icon {
  margin-right: 4px;
  color: var(--secondary);
  cursor: pointer;
  transition: transform 0.2s ease;
  flex-shrink: 0;
  padding: 4px 6px;
  margin: -4px 0;
  border-radius: 4px;
}

.outline-folder-container .folder-icon:hover {
  background-color: var(--highlight);
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
  padding: 0.15rem 0.35rem;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.outline-folder-title:hover {
  color: var(--secondary);
  opacity: 1;
  background-color: var(--highlight);
}

.outline-folder-title.active {
  color: var(--secondary);
  font-weight: 700;
  opacity: 1;
  background-color: var(--highlight);
}

.unlinked-item {
  color: var(--gray);
  font-size: 0.88rem;
  line-height: 1.45rem;
  padding: 0.15rem 0.35rem;
}

.folder-outer {
  display: none;
}

.folder-outer.open {
  display: block;
}

/* =========================================
   Mobile Viewport Styles (<= 800px)
   ========================================= */
@media all and (max-width: 800px) {
  .outline-nav {
    width: 100%;
    flex: 1 1 100%;
    order: 10;
    margin: 0.6rem 0 0.5rem 0;
    border: 1px solid var(--lightgray);
    border-radius: 8px;
    background-color: var(--light);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    padding: 0.6rem 0.85rem;
    box-sizing: border-box;
    transition: background-color 0.2s ease, border-color 0.2s ease;
  }

  .outline-nav button.desktop-outline-nav {
    margin-bottom: 0;
    padding: 0.15rem 0;
    min-height: 36px;
  }

  .outline-nav button.desktop-outline-nav h2 {
    font-size: 0.9rem;
    color: var(--dark);
  }

  .outline-nav:not(.collapsed) {
    border-color: var(--secondary);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
  }

  .outline-nav:not(.collapsed) button.desktop-outline-nav {
    margin-bottom: 0.6rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--lightgray);
  }

  .outline-nav-content {
    max-height: 55vh;
    padding-right: 4px;
    padding-top: 0.2rem;
  }

  .outline-nav-content li {
    margin: 0.25rem 0;
  }

  .outline-nav-content li > a,
  .outline-folder-title {
    font-size: 0.92rem;
    line-height: 1.6rem;
    padding: 0.25rem 0.45rem;
  }

  .outline-folder-container .folder-icon {
    padding: 6px 8px;
    margin: -6px 0;
    touch-action: manipulation;
  }
}
`;
  return OutlineNav;
});

// plugins/outline-nav/src/index.ts
var index_default = OutlineNav_default;
export {
  OutlineNav_default as OutlineNav,
  index_default as default
};

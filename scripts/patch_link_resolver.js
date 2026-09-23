import fs from "fs";
import path from "path";

const filesToPatch = [
  "node_modules/@quartz-community/crawl-links/dist/index.js",
  "node_modules/@quartz-community/utils/dist/path.js"
];

// 1. Folder index resolution patch
for (const relPath of filesToPatch) {
  const fullPath = path.resolve(process.cwd(), relPath);
  if (!fs.existsSync(fullPath)) continue;

  let code = fs.readFileSync(fullPath, "utf-8");
  const target = "return targetCanonical === fileName;";
  const replacement = `if (targetCanonical === fileName) return true;\n        if (fileName === "index" && parts.length > 1 && targetCanonical === parts.at(-2)) return true;\n        return false;`;

  if (code.includes(target)) {
    code = code.replace(target, replacement);
    fs.writeFileSync(fullPath, code, "utf-8");
    console.log(`[patch] Applied folder index resolution patch to: ${relPath}`);
  } else if (code.includes("parts.at(-2)")) {
    console.log(`[patch] Already patched: ${relPath}`);
  }
}

// 1b. Fix broken wikilinkRegex in OFM
const ofmPath = path.resolve(process.cwd(), "node_modules/@quartz-community/obsidian-flavored-markdown/dist/index.js");
if (fs.existsSync(ofmPath)) {
  let ofmCode = fs.readFileSync(ofmPath, "utf-8");
  const brokenTarget = "var wikilinkRegex = new RegExp(\n  /!?\\[\\[([^[]\\]#|\\\\]+)?(#+[^[]\\]#|\\\\]+)?(\\\\?\\|[^[]\\]#]*)?\\]\\]/g\n);";
  const fixedRegex = "var wikilinkRegex = new RegExp(\n  /!?\\[\\[([^\\[\\]#|]+)?(#+[^\\[\\]#|]+)?(?:\\|([^\\[\\]]+))?\\]\\]/g\n);";
  if (ofmCode.includes(brokenTarget)) {
    ofmCode = ofmCode.replace(brokenTarget, fixedRegex);
    fs.writeFileSync(ofmPath, ofmCode, "utf-8");
    console.log(`[patch] Applied broken wikilinkRegex fix to OFM!`);
  } else if (ofmCode.includes("([^\\[\\]#|]+)?(#+[^\\[\\]#|]+)?(?:\\|([^\\[\\]]+))?")) {
    console.log(`[patch] Already patched OFM wikilinkRegex.`);
  }
}

// 2. Raw HTML Wikilinks and Link Resolution patch in crawl-links
const crawlLinksPath = path.resolve(process.cwd(), "node_modules/@quartz-community/crawl-links/dist/index.js");
if (fs.existsSync(crawlLinksPath)) {
  let crawlCode = fs.readFileSync(crawlLinksPath, "utf-8");
  const rawPatchMarker = "/* RAW_HTML_WIKILINK_PATCH */";
  if (!crawlCode.includes(rawPatchMarker)) {
    const targetHook = "visit(tree, \"element\", (node) => {";
    const rawPatchCode = `${rawPatchMarker}
            visit(tree, (node) => {
              if (node.type === "raw" && typeof node.value === "string") {
                node.value = node.value.replace(
                  /!?\\[\\[([^\\[\\]#|]+)?(#+[^\\[\\]#|]+)?(?:\\|([^\\[\\]]+))?\\]\\]/g,
                  (fullMatch, rawFp, rawHeading, rawAlias) => {
                    if (fullMatch.startsWith("!")) return fullMatch;
                    const fp = rawFp?.trim() ?? "";
                    const anchor = rawHeading?.trim() ?? "";
                    let alias = rawAlias?.trim() ?? "";
                    if (!alias) {
                      alias = fp && anchor ? fp + " > " + anchor.replace(/^#+/, "") : fp || anchor.replace(/^#+/, "");
                    }
                    if (!fp && !anchor) return fullMatch;
                    if (isAbsoluteUrlWithOptions(fp)) {
                      return \`<a href="\${fp}" class="external external-link">\${alias}</a>\`;
                    }
                    const target = fp + anchor;
                    const dest = transformLink(fileSlug, target, transformOptions);
                    try {
                      const url = new URL(dest, "https://base.com/" + stripSlashes(curSlug, true));
                      const canonicalDest = url.pathname;
                      const [destCanonicalRaw] = splitAnchor(canonicalDest);
                      let destCanonical = destCanonicalRaw;
                      if (destCanonical.endsWith("/")) destCanonical += "index";
                      const full = decodeURIComponent(stripSlashes(destCanonical, true));
                      outgoing.add(simplifySlug(full));
                      return \`<a href="\${dest}" class="internal internal-link" data-slug="\${full}">\${alias}</a>\`;
                    } catch (e) {
                      return \`<a href="\${dest}" class="internal internal-link">\${alias}</a>\`;
                    }
                  }
                );
                node.value = node.value.replace(
                  /<a\\s+([^>]*?)href=(["\\x27])(.*?)\\2([^>]*)>/gi,
                  (match, pre, quote, dest, post) => {
                    if (isAbsoluteUrlWithOptions(dest) || dest.startsWith("#") || dest.startsWith("mailto:")) {
                      return match;
                    }
                    let cleanDest = dest;
                    if (cleanDest.startsWith("/content/")) cleanDest = cleanDest.slice("/content/".length);
                    if (cleanDest.startsWith("/")) cleanDest = cleanDest.slice(1);
                    const transformed = transformLink(fileSlug, cleanDest, transformOptions);
                    return \`<a \${pre}href=\${quote}\${transformed}\${quote}\${post}>\`;
                  }
                );
              }
            });
            ${targetHook}`;
    if (crawlCode.includes(targetHook)) {
      crawlCode = crawlCode.replace(targetHook, rawPatchCode);
      fs.writeFileSync(crawlLinksPath, crawlCode, "utf-8");
      console.log(`[patch] Applied Raw HTML Wikilink & Link Resolution patch to CrawlLinks!`);
    }
  } else {
    console.log(`[patch] Already patched CrawlLinks with Raw HTML Wikilink support.`);
  }
}

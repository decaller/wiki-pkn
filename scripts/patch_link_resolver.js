import fs from "fs";
import path from "path";

const filesToPatch = [
  "node_modules/@quartz-community/crawl-links/dist/index.js",
  "node_modules/@quartz-community/utils/dist/path.js"
];

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

import esbuild from "esbuild"
import fs from "fs"
import path from "path"
import { fileURLToPath } from "url"

const __dirname = path.dirname(fileURLToPath(import.meta.url))

async function build() {
  const distDir = path.join(__dirname, "dist")
  if (!fs.existsSync(distDir)) {
    fs.mkdirSync(distDir, { recursive: true })
  }

  // Build main entry
  await esbuild.build({
    entryPoints: [
      path.join(__dirname, "src/index.ts"),
      path.join(__dirname, "src/components/index.ts"),
    ],
    outdir: distDir,
    bundle: true,
    format: "esm",
    platform: "node",
    target: "node20",
    jsx: "automatic",
    jsxImportSource: "preact",
    external: [
      "preact",
      "preact/*",
      "@quartz-community/*",
      "fs",
      "path",
      "url",
    ],
  })

  // Write TypeScript declaration files
  const dtsContent = `import { QuartzComponent, QuartzComponentConstructor } from "../quartz/components/types";
export interface OutlineNavOptions {
  title?: string;
  folderDefaultState?: "collapsed" | "open";
  useSavedState?: boolean;
}
declare const OutlineNav: QuartzComponentConstructor<OutlineNavOptions>;
export { OutlineNav };
export default OutlineNav;
`
  fs.writeFileSync(path.join(distDir, "index.d.ts"), dtsContent)

  const compDtsDir = path.join(distDir, "components")
  if (!fs.existsSync(compDtsDir)) {
    fs.mkdirSync(compDtsDir, { recursive: true })
  }
  fs.writeFileSync(path.join(compDtsDir, "index.d.ts"), `export { OutlineNav, default } from "../index.js";\n`)

  console.log("✓ outline-nav built successfully!")
}

build().catch((err) => {
  console.error("Build failed:", err)
  process.exit(1)
})

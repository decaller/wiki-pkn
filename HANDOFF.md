# Project Handoff: Wiki PKN

This document summarizes the recent development work to implement a custom, hierarchical sidebar navigation in this Quartz project based on an exported Outline structure.

## Overview
The main goal was to replace the default Quartz `Explorer` component with a custom `OutlineNav` component that precisely replicates a provided JSON hierarchy (`nav_structure.json`), while also cleaning up and restructuring the underlying Markdown files in the `content/` folder to match.

## Key Architecture & Components

### 1. `nav_structure.json`
- **Location:** Project Root
- **Purpose:** Acts as the source of truth for the sidebar navigation. It defines the exact hierarchy, titles, and icons for collections and documents.
- **Changes Made:** Iteratively cleaned up to flatten the root level (now nested under "Paradigma"), removed redundant prefixes (e.g., removing "Fase" from "Fase Thufulah", or "Insan" from child nodes), and removed unused properties (`id`, `url`, `color`).

### 2. Custom Plugin: `OutlineNav`
- **Location:** `plugins/outline-nav/`
- **Purpose:** A custom Quartz component that parses `nav_structure.json` and renders a nested `<ul>` HTML sidebar.
- **Features Implemented:**
  - **Dynamic Link Resolution:** Maps JSON titles to Quartz slugs by checking file frontmatter titles and fallback slug suffixes.
  - **Expand/Collapse Logic:** Folders can be toggled via chevron buttons.
  - **Initial Depth Limiting:** Automatically collapses deep nodes (depth >= 2) on initial load to keep the sidebar clean.
  - **Collapsible Main Title:** The "Outline Navigation" header is a toggle button that collapses the entire tree, mirroring the default Explorer plugin.
  - **State Persistence:** Uses `localStorage` to remember which folders are opened or closed, ensuring the tree state is retained seamlessly across page navigations (PJAX).

### 3. Automation Scripts
- **Location:** Project Root (`rename_script.py`, `rename_fase.py`, `rename_more.py`, `rename_paradigma.py`, `group_implementasi.py`)
- **Purpose:** Used to perform bulk updates across the `content/` directory so the physical files matched the simplified JSON structure.
- **Actions Performed:** Renamed physical `.md` files, created new subdirectories (e.g., grouping the `Implementasi` items), updated the YAML `title` frontmatter in each file, and patched internal wikilinks (e.g., `[[Old Title]]` -> `[[New Title]]`).

## Development Workflow

If you need to make future changes to the `OutlineNav` plugin:

1. **Edit the Plugin:**
   Modify `plugins/outline-nav/src/components/OutlineNav.tsx`.

2. **Rebuild the Plugin:**
   Navigate into the plugin directory and run the build script.
   ```bash
   cd plugins/outline-nav
   npm run build
   ```

3. **Restart Quartz:**
   Since Quartz loads components on startup, kill the running server and start it again.
   ```bash
   cd ../../
   npx quartz build --serve --port 8888
   ```

## Next Steps / Maintenance
- Any new files added to the `content/` directory must be manually added to `nav_structure.json` if you want them to appear in the `OutlineNav` sidebar.
- Ensure the `title` frontmatter in new Markdown files exactly matches the title provided in `nav_structure.json` so the plugin can resolve the correct URL slug.

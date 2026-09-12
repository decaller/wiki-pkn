# SEO Implementation & Technical Audit: Quartz

An SEO audit of Quartz reveals a split between standard technical baselines that are fully covered and advanced optimizations that require custom implementation to meet modern web best practices.

---

### 1. What is Already Implemented (Baseline Compliance)

* **Pre-rendered Architecture (SSG):** Generates static HTML at build time, yielding optimal Time to First Byte (TTFB) and rendering performance that aligns with Core Web Vitals criteria.
* **On-Page Metadata Management:** Maps Markdown frontmatter directly to HTML `<head>` tags, handling basic `title`, `description`, and custom `permalink` properties.
* **Search Engine Discovery:** Automatically emits an XML sitemap (`sitemap.xml`) and RSS feed (`index.xml`) via the `ContentIndex` plugin, enabling standard crawler discovery.
* **Social Sharing Preview Generation:** Utilizes Satori-based plugins (`CustomOgImages`) to programmatically generate dynamic Open Graph and Twitter Card images, supporting social media visibility.
* **Link Equity & Redirect Integrity:** Manages legacy path redirects and case normalization via `AliasRedirects`, minimizing broken links and mitigating 404 crawl errors.

---

### 2. Improvements Needed (Best-Practice Gaps)

* **Schema.org Structured Data (Critical Gap):**
  * *Current State:* Quartz does not natively emit JSON-LD markup.
  * *Best Practice:* Enterprise and high-performing documentation sites implement `TechArticle`, `Article`, or `BreadcrumbList` schemas to qualify for rich snippets and enhanced search visibility.
  * *Improvement:* Inject JSON-LD blocks into the document layout templates.

* **Canonical URL Enforcement:**
  * *Current State:* Relies on default routing without programmatic self-referencing canonical tags.
  * *Best Practice:* Every page should declare an explicit `<link rel="canonical">` tag to prevent indexing penalties from duplicate content or trailing-slash discrepancies.
  * *Improvement:* Add canonical tag generation to the core page layout emitter.

* **Granular Robots & Indexing Control:**
  * *Current State:* Lacks fine-grained, frontmatter-driven configuration for `robots` meta tags (`noindex`, `nofollow`, `noarchive`).
  * *Best Practice:* Professional sites require page-level control to block draft, administrative, or duplicate pages from search engine indexing.
  * *Improvement:* Extend frontmatter parsing to conditionally inject meta robots directives.

* **Semantic Heading Auditing:**
  * *Current State:* Relies entirely on the author's Markdown structure.
  * *Best Practice:* Search engines depend on a strict, unbroken hierarchy (a single unique `H1` followed sequentially by `H2` and `H3` nodes).
  * *Improvement:* Implement a build-time linter or warning system to flag malformed document structures.

* **Image SEO & Asset Optimization:**
  * *Current State:* No native enforcement of descriptive `alt` attributes or automated modern format conversion (WebP/AVIF) for inline images.
  * *Best Practice:* Image search and accessibility standards require validated `alt` text and compressed vector/raster assets.
  * *Improvement:* Enforce alt-text validation through a remark/rehype plugin during the build pipeline.

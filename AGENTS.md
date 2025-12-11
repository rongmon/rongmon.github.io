# Website Migration Agent Specification

## Goal
Convert an existing static HTML/CSS website (based on Helios HTML5 UP template) into a Markdown-based website that is easy to maintain, update, and version-control. The output should be a clean, modern, responsive HTML site generated automatically from Markdown sources.

## Current Site Analysis
- **Template**: Helios by HTML5 UP
- **HTML Pages**: 12 (index.html + 11 content pages)
- **Navigation Structure**: Hierarchical menu with Research subpages
- **Assets**: 32MB images directory with 30+ image files
- **Current Assets**: Existing CSS (main.css, ie8.css), JavaScript dependencies (jQuery, skel, etc.)
- **Analytics**: Google Analytics (gtag) embedded in header
- **Domain**: GitHub Pages (CNAME file present)

## Target Framework Recommendation
**Recommended: Hugo** (instead of MkDocs)

**Rationale**:
- Hugo is better suited for personal/professional portfolio sites with image-heavy content
- MkDocs is more documentation-focused; less ideal for portfolio/research websites
- Hugo's theme ecosystem has excellent portfolio/academic site themes
- Hugo performs better with large image directories (32MB+)
- Suggested theme: **[Academic](https://github.com/gcushen/hugo-academic)** or **[Minimal](https://github.com/calintat/minimal)**

## Responsibilities of the Agent

### 1. Content Extraction & Conversion
- Parse all 12 `.html` pages and extract:
  - Page title and metadata
  - Headings and section structure
  - Body text and paragraphs
  - Images with paths (update to `/static/images/`)
  - Internal links (convert from `.html` to relative paths)
  - Google Analytics code (preserve as front matter or partial)
  - Special formatting (lists, blockquotes, embedded media)
- Convert each page into clean Markdown (`.md`) with YAML front matter
- **Key pages to migrate**:
  - index.html → _index.md (home page)
  - Research.html → research/_index.md
  - JWST.html, IFU.html, FB.html, outflow.html, CGM.html, photoz.html → research/[topic].md
  - Education.html → academics.md
  - Publications.html → publications.md
  - People.html → people.md
  - Press_Release.html → press.md
  - Code.html → software.md
  - Meetings.html → events.md

### 2. Navigation Structure Preservation
- Retain the current hierarchical navigation:
  - Home
  - Academics
  - Research (with 6 sub-topics)
  - Publications
  - Events
  - People
  - Press Release
- Update Hugo menu configuration to match existing structure
- Convert relative internal links from `.html` references to proper Hugo shortcodes/relative paths

### 3. Image Asset Management
- **Directory structure**: Move all images from `/images` to `/static/images/`
- Update all image references in Markdown files
- Preserve subdirectories if they exist
- Consider image optimization for web (optional but recommended)

### 4. Styling & Theme Configuration
- Select and configure Hugo theme (Academic or Minimal recommended)
- Preserve branding: personal name, astrophysicist title, color scheme
- Ensure mobile responsiveness
- Add custom CSS overrides in `/assets/css/custom.css` if needed for specific styling
- Remove IE8 compatibility code (unnecessary for modern sites)

### 5. Analytics & Metadata Preservation
- Migrate Google Analytics (gtag ID: G-LKH1FTLZSQ) to Hugo config or base template partial
- Preserve CNAME file for GitHub Pages
- Update robots.txt if needed

### 6. Build System Setup
- Create `config.toml` with:
  - Base URL (rongmon.github.io)
  - Title and author metadata
  - Menu structure (main navigation)
  - Theme configuration
  - Analytics integration
- Create reproducible build process:
  ```bash
  hugo mod tidy
  hugo
  ```
- Ensure output directory is set to `public/` (default for GitHub Pages)

### 7. Special Considerations
- **Research subdirectories**: Research_Files/ and PY205_Score_Projection/ may contain supplementary materials - assess if these should be served as downloadable assets or migrated to pages
- **Gallery/Image-heavy content**: Use Hugo's figure shortcodes for better image handling
- **Code references**: Code.html mentions research software packages - ensure proper linking/embedding in software.md
- **Headers/Footers**: Common header appears in all pages - configure in Hugo base template

### 8. Final Deliverables
The agent must produce:
- Organized `/content/` directory with Markdown files
- `/static/images/` with all image assets
- Properly configured `config.toml`
- `/themes/` directory with selected Hugo theme
- `.github/workflows/deploy.yml` (for automated deployment to GitHub Pages)
- `/archetypes/` templates for consistent front matter
- Updated README with build/deployment instructions
- `public/` directory with compiled static HTML output

## Migration Execution Steps

1. **Audit Phase**
   - Document all page content and structure
   - List all images and verify paths
   - Identify special elements (code blocks, tables, iframes, etc.)

2. **Setup Phase**
   - Initialize Hugo project structure
   - Select and configure theme
   - Set up Hugo config.toml

3. **Content Conversion**
   - Convert HTML pages to Markdown with front matter
   - Create content directory structure matching navigation
   - Update all image and internal link references

4. **Asset Migration**
   - Copy images to /static/images/
   - Verify all asset links work correctly

5. **Theme Customization**
   - Apply branding and colors
   - Configure navigation in config.toml
   - Add analytics integration

6. **Testing Phase**
   - Build and verify all pages render correctly
   - Test internal navigation
   - Verify images display properly
   - Test on mobile devices
   - Check link functionality

7. **Deployment**
   - Set up GitHub Actions workflow for automated builds
   - Deploy to GitHub Pages
   - Verify live site functionality

## Rules & Best Practices
- Use clean, readable Markdown with proper YAML front matter
- Minimize inline HTML (Hugo shortcodes preferred)
- Maintain accessibility standards (alt text for images, semantic headings)
- Keep file names simple, lowercase, hyphenated (e.g., `galactic-outflows.md`)
- Preserve existing URL structure where possible for SEO
- Document any custom configurations in the README
- Ensure Git history remains intact during migration

---


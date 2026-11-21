# Asiimwe Derick — personal-brand platform

A static, multi-page personal-brand site. No framework, no build step at runtime: HTML, one shared
stylesheet layer and one shared script. Deploys automatically to GitHub Pages from `main`.

## Structure

- `build.py` — the generator. All page content lives here; run `python3 build.py` to regenerate
  every page, `assets/site-index.json`, `sitemap.xml` and `robots.txt`.
- `styles.css` — the original design system (tokens, hero, sections).
- `assets/site.css` — the platform layer (cards, timeline, search, assistant, light theme, print).
- `assets/site.js` — theme toggle, mobile nav, site search, on-site assistant, local analytics.
- `assets/site-index.json` — search + assistant index (generated, do not hand-edit).
- `assets/derick-asiimwe-cv.pdf`, `assets/qr-site.png` — generated downloads.

## Editing content

1. Open `build.py`, find the page block (`about = page_head_block(...)` etc.).
2. Edit the text. Blocks marked `edit(...)` in the HTML are deliberate placeholders where personal
   facts are still needed (schools, awards, testimonials, press, events, reading list).
3. Run `python3 build.py`, then commit and push.

## Adding a page

Add `add("newpage.html", "Title", "Description", "keywords", body_html)` in `build.py`, then add it
to `NAV` or `MORE` (or `SITEMAP_GROUPS`) so it is reachable. The sitemap and search index update
automatically.

## Conventions

- One `<h1>` per page, real headings below it, descriptive `alt` on every image.
- Internal links are relative (`about.html`), anchors are real ids.
- No third-party tracking. Analytics are local-only; see `track()` in `assets/site.js`.

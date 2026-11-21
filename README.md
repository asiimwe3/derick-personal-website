# Asiimwe Derick — personal-brand platform

**Live site: https://asiimwe3.github.io/derick-personal-website/**

Personal-brand headquarters for Asiimwe Derick: founder of DeryCode Technologies, CEO of Sageco Evergreen.
Built as a fast static site — no framework, no runtime build, one shared stylesheet and one shared script.

## Pages
Home · About · Journey · Skills & CV · Ventures · Projects · Impact · Writing (+ 3 articles) · Vision ·
Speaking · Gallery · Services · Investors · Contact · Media kit · Ask Derick AI · Site map ·
Privacy · Terms · Disclaimer · 404

## Features
- Clean white DeryCode-style design system, dark mode available from the header toggle
- Client-side search over every page (press `/`)
- "Ask Derick AI" — answers from this site's own content, no API key, works offline
- CV as a printable page and as a PDF download
- QR code for sharing the site in person
- Per-page SEO: canonical URLs, Open Graph, Twitter cards, JSON-LD, sitemap.xml, robots.txt
- Accessibility: skip link, focus states, alt text, keyboard-dismissable overlays

## Editing
All content lives in `build.py`. Edit the page text there, then:

```bash
python3 build.py
```

That regenerates every HTML page, the search index and `sitemap.xml`.
Styles: `styles.css` (design tokens and layout) and `assets/site.css` (component layer).
Behaviour: `assets/site.js`.

## Contact
derickasiimwe849@gmail.com · WhatsApp +256 762 306 675

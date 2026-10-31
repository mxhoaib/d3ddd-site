# D3DDD Blog

Static Markdown → HTML blog for https://d3ddd.com/blog/

## Add a post

1. Create `posts/<slug>.md` with YAML front matter:

```yaml
---
title: "..."
slug: my-slug
date: YYYY-MM-DD
category: megaprojects
category_title: Megaprojects
description: "…"
image: /assets/img/blog/my-og.jpg
image_alt: "…"
image_credit: "…"
canonical: https://original.example/post
---
```

`canonical` is optional. When set, the article `<link rel="canonical">` uses that URL (republished posts point at the original). Omit images rather than hot-linking them. End a republished post with one line: `Originally published on [ShoaibSite](original-url).`

2. From repo root:

```bash
python3 scripts/build_blog.py
```

3. Commit generated `blog/**`, `sitemap.xml`, and assets. Keep OG images compressed (JPEG ~60–70 quality).

## Rules

- **Author block required on every post:** byline (top) + author box (bottom) for Shoaib Hussan (founder of D3DDD) with Instagram @mxhaib, LinkedIn (https://www.linkedin.com/in/mshoaib94) and Fiverr. Generated automatically by `AUTHOR_BYLINE` / `AUTHOR_BOX` in `scripts/build_blog.py` — do not remove.

- Cite real sources; no invented stats.
- Soft-link D3DDD service pages (`/services/…`) and existing socials.
- Top bar / footer: `info@d3ddd.com` + d3ddd.com only (no phone/WhatsApp).
- GoatCounter snippet: `d3dddsites`.

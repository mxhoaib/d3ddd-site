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
---
```

2. From repo root:

```bash
python3 scripts/build_blog.py
```

3. Commit generated `blog/**`, `sitemap.xml`, and assets. Keep OG images compressed (JPEG ~60–70 quality).

## Rules

- Cite real sources; no invented stats.
- Soft-link D3DDD service pages and existing socials.
- Top bar / footer: `info@d3ddd.com` + d3ddd.com only (no phone/WhatsApp).
- GoatCounter snippet: `d3dddsites`.

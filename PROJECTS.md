# D3DDD Projects / Portfolio

Placeholder structure for real project case studies on https://d3ddd.com/projects/

## Rules

- Do **not** invent client names, photos, metrics or case studies.
- Only publish owner-approved projects with permission to show.
- Keep images compressed (JPEG ~60–70 quality or optimized WebP/SVG diagrams).
- Soft-link the matching service page under `/services/…`.

## Add a project (when ready)

1. Add images under `assets/img/projects/<slug>/` (compressed).
2. Add an entry in the projects builder (or a `projects/*.md` source once introduced) with:
   - `title`, `slug`, `location` (city / emirate)
   - `service` (one of: drafting, designing, estimation, 3d, web)
   - `summary` (what was delivered — factual)
   - `image` + `image_alt`
3. Rebuild the static site and commit generated `projects/**` + `sitemap.xml`.

## Live page

`/projects/` is a “coming soon” placeholder until the first real upload.

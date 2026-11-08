# Arabic article 01 — local editorial draft

Nothing in this branch has been pushed or deployed. The article remains `status: DRAFT`.

- Source: `posts/ar/what-are-marble-shop-drawings.md`
- Planned URL: `https://d3ddd.com/ar/blog/what-are-marble-shop-drawings/`
- Build local review files: `python3 scripts/build_blog.py --arabic-only --include-drafts`
- Standard builds skip Arabic sources marked DRAFT; `--include-drafts` is an explicit local preview opt-in. Preview HTML has `noindex, follow`.
- After owner approval, change status to PUBLISHED and rebuild. Do not deploy the draft preview artifacts or their index/feed/sitemap references. A standard build does not delete already generated preview files, so use a clean output checkout or remove preview artifacts before any unrelated deployment.

## Minimal build extension

`scripts/build_ar_blog.py` reads `posts/ar/*.md` with the existing frontmatter/Markdown parser. It reuses the shared shell, author-byline/author-box markup, business schema and article schema, localizing the Arabic article and site navigation. Arabic-only CSS is isolated in `assets/ar-blog.css`. No image files or additional Python dependencies were added.

It generates an RTL `ar-AE` article, Arabic index, category page and RSS feed, plus sitemap entries and a link from the English blog index. The English sibling receives reciprocal hreflang links (ar/ar-AE, en/en-AE and English x-default). Both versions have self-canonicals. Six FAQPage entries are derived from the visible FAQ, not separately authored. Article language and translationOfWork are explicit.

Use `--arabic-only` to avoid rebuilding unrelated English posts. Pre-existing Related-sidebar rewrites from the initial full build were restored; only the English sibling's hreflang and the English index's Arabic chip change.

## Validation

- 1,563 visible article words, excluding title/byline/navigation/author box.
- SEO title 53 characters; description 159 characters.
- One H1, H2/H3 structure, six matching visible/schema FAQs; JSON-LD parses.
- Existing images have Arabic alt text; no new images and no inline style attributes on Arabic outputs.
- Required live article/service/contact/project links and both image URLs returned HTTP 200.
- RSS and sitemap parse as XML; reciprocal hreflang present; local build repeatable.
- RTL markup and CSS verified statically. Browser rendering/mobile-menu testing and the requested 390px Playwright screenshot remain unverified: no browser/subagent execution tool was available. No screenshot was fabricated.

External review files: `/workspace/seo/blog/ar-01-what-are-marble-shop-drawings.md` and `/workspace/websites/d3ddd-seo-shots/ar-blog-01-validation.json`.

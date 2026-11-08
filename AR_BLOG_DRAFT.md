# Arabic article 01 — published

Owner approved. The article status is `PUBLISHED`.

- Source: `posts/ar/what-are-marble-shop-drawings.md`
- URL: `https://d3ddd.com/ar/blog/what-are-marble-shop-drawings/`
- Publish build: `python3 scripts/build_blog.py --arabic-only` (do not pass `--include-drafts`). Published Arabic posts are included; sources marked DRAFT are skipped.
- Draft previews use `python3 scripts/build_blog.py --arabic-only --include-drafts`. Preview HTML has `noindex, follow`. A standard build does not delete already generated preview files, so rebuild after changing status so the published page, index, feed and sitemap replace the preview.

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

#!/usr/bin/env python3
"""Build static blog pages from posts/*.md. Run from repo root: python3 scripts/build_blog.py"""
from __future__ import annotations
import html, json, os, re, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.chdir(ROOT)

import markdown

D = "https://d3ddd.com"
EMAIL = "info@d3ddd.com"
GOAT = '<script data-goatcounter="https://d3dddsites.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
POSTS_DIR = ROOT / "posts"
BLOG_DIR = ROOT / "blog"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)

def parse_post(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    m = FM_RE.match(raw)
    if not m:
        raise SystemExit(f"Missing front matter: {path}")
    meta, body = m.group(1), m.group(2)
    data = {}
    for line in meta.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"').strip("'")
    for req in ("title", "slug", "date", "category", "category_title", "description"):
        if req not in data:
            raise SystemExit(f"{path.name}: missing {req}")
    data["body_md"] = body.strip()
    data["body_html"] = markdown.markdown(
        body,
        extensions=["extra", "sane_lists", "smarty"],
    )
    data["word_count"] = len(re.findall(r"\w+", body))
    data["url"] = f"{D}/blog/{data['slug']}/"
    data["image"] = data.get("image") or f"{D}/assets/img/og-image.png"
    if data["image"].startswith("/"):
        data["image"] = D + data["image"]
    data["image_alt"] = data.get("image_alt") or data["title"]
    data["image_credit"] = data.get("image_credit") or ""
    return data

def esc(s: str) -> str:
    return html.escape(s, quote=True)

def topbar(prefix: str) -> str:
    return (
        f'<div class="topbar"><span><a href="mailto:{EMAIL}">{EMAIL}</a></span>'
        f'<span><a href="{D}/">d3ddd.com</a></span></div>'
    )

def nav(prefix: str, current: str = "") -> str:
    items = [
        (f"{prefix}", "Home", "home"),
        (f"{prefix}services/", "Services", "services"),
        (f"{prefix}projects/", "Projects", "projects"),
        (f"{prefix}marble.html", "Marble Shop Drawings", "marble"),
        (f"{prefix}website-design.html", "Website Design", "website"),
        (f"{prefix}blog/", "Blog", "blog"),
        (f"{prefix}about.html", "About", "about"),
        (f"{prefix}contact.html", "Contact", "contact"),
    ]
    links = []
    for href, label, key in items:
        cur = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    links.append(f'<a class="lang" href="{prefix}ar/" hreflang="ar" lang="ar">العربية</a>')
    return "".join(links)

def footer(prefix: str) -> str:
    return f'''<footer><div class="grid"><div><div class="logo"><span>D3</span><strong>DDD</strong><small>Dubai 3D Design &amp; Draft</small></div>
<p style="margin-top:16px;max-width:340px">Architectural drafting, designing, estimation, 3D visualization and websites in Dubai, Abu Dhabi, Sharjah and across the UAE.</p>
<p style="margin-top:12px"><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{D}/">d3ddd.com</a></p></div>
<div><h2>Services</h2>
<a href="{prefix}services/">All services</a>
<a href="{prefix}services/architectural-drafting/">Architectural drafting</a>
<a href="{prefix}services/architectural-designing/">Architectural designing</a>
<a href="{prefix}services/architectural-estimation/">Architectural estimation</a>
<a href="{prefix}services/3d-rendering-modeling-visualization/">3D rendering &amp; visualization</a>
<a href="{prefix}services/website-development-designing/">Website development</a>
</div>
<div><h2>Company</h2><a href="{prefix}projects/">Projects</a><a href="{prefix}about.html">About</a><a href="{prefix}blog/">Blog</a><a href="{prefix}contact.html">Contact</a></div>
<div><h2>Contact</h2><a href="{prefix}contact.html">Send an enquiry</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{prefix}blog/feed.xml">RSS</a><span>Dubai, United Arab Emirates</span></div></div>
<div class="copy">© <span data-year>2026</span> D3DDD – Dubai 3D Design &amp; Draft. All rights reserved.</div></footer>'''

def shell(title: str, desc: str, canonical: str, body: str, prefix: str, ld: list, og_type: str = "website", image: str | None = None, current: str = "blog", og_url: str | None = None) -> str:
    img = image or f"{D}/assets/img/og-image.png"
    social_url = og_url or canonical
    ld_json = json.dumps({"@context": "https://schema.org", "@graph": ld}, ensure_ascii=False)
    return f'''<!DOCTYPE html>
<html lang="en-AE" dir="ltr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{esc(canonical)}">
<link rel="alternate" type="application/rss+xml" title="D3DDD Blog" href="{D}/blog/feed.xml">
<meta name="geo.region" content="AE-DU"><meta name="geo.placename" content="Dubai, United Arab Emirates">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="D3DDD – Dubai 3D Design &amp; Draft">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(social_url)}"><meta property="og:locale" content="en_AE">
<meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{img}">
<meta name="theme-color" content="#0e0e0c"><meta name="format-detection" content="telephone=no">
<link rel="icon" href="{prefix}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="{prefix}assets/style.css" as="style"><link rel="stylesheet" href="{prefix}assets/style.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@1,500&display=swap" media="print" onload="this.media='all'">
<script type="application/ld+json">{ld_json}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
{topbar(prefix)}
<header class="site-header"><a class="logo" href="{prefix}" aria-label="D3DDD – Dubai 3D Design &amp; Draft"><span>D3</span><strong>DDD</strong><small>Dubai 3D Design &amp; Draft</small></a>
<button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav">☰</button>
<nav class="nav" id="nav" aria-label="Main">{nav(prefix, current)}</nav></header>
<main id="main">{body}</main>
{footer(prefix)}
<script src="{prefix}assets/config.js" defer></script><script src="{prefix}assets/site.js" defer></script>
{GOAT}</body></html>'''

def business_ld() -> dict:
    return {
        "@type": ["ProfessionalService", "LocalBusiness"],
        "@id": f"{D}/#business",
        "name": "D3DDD – Dubai 3D Design & Draft",
        "url": f"{D}/",
        "email": EMAIL,
        "logo": f"{D}/assets/img/logo.svg",
        "image": f"{D}/assets/img/og-image.png",
        "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"},
        "areaServed": [
            {"@type": "City", "name": "Dubai"},
            {"@type": "Place", "name": "Palm Jumeirah, Dubai"},
            {"@type": "Country", "name": "United Arab Emirates"},
            {"@type": "Place", "name": "New York, NY, United States"},
            {"@type": "Place", "name": "London, United Kingdom"},
        ],
        "sameAs": [
            "https://www.fiverr.com/mxhoaib",
            "https://www.instagram.com/mxhaib/",
            "https://www.linkedin.com/in/mshoaib94",
        ],
    }

def crumbs_ld(items: list[tuple[str, str]]) -> dict:
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(items)
        ],
    }

IG = "https://www.instagram.com/mxhaib/"
FIVERR = "https://www.fiverr.com/mxhoaib"
LINKEDIN = "https://www.linkedin.com/in/mshoaib94"
# Required on every article: author byline + author box (see BLOG.md)
AUTHOR_BYLINE = (
    '<div class="byline"><span class="av" aria-hidden="true">SH</span><span>Written by '
    '<strong>Shoaib Hussan</strong><br><small>Founder, D3DDD · '
    f'<a href="{IG}" rel="me noopener" target="_blank">@mxhaib</a> · '
    f'<a href="{LINKEDIN}" rel="me noopener" target="_blank">LinkedIn</a></small></span></div>'
)
AUTHOR_BOX = (
    '<aside class="author-box" aria-label="About the author"><span class="av lg" aria-hidden="true">SH</span>'
    '<div><p class="eyebrow">About the author</p><h2>Shoaib Hussan</h2>'
    '<p>Draftsman and founder of '
    '<strong>D3DDD – Dubai 3D Design &amp; Draft</strong>. Shop drawings, marble &amp; stone detailing, '
    '3D visualisation and construction documentation for contractors and fabricators across the Gulf.</p>'
    f'<p class="socials"><a href="{IG}" rel="me noopener" target="_blank">Instagram @mxhaib</a>'
    f'<a href="{LINKEDIN}" rel="me noopener" target="_blank">LinkedIn</a>'
    f'<a href="{FIVERR}" rel="me noopener" target="_blank">Hire on Fiverr</a>'
    '<a href="../../contact.html">Work with D3DDD →</a></p></div></aside>'
)

def article_ld(p: dict) -> dict:
    return {
        "@type": "Article",
        "headline": p["title"],
        "description": p["description"],
        "datePublished": p["date"],
        "dateModified": p["date"],
        "image": p["image"],
        "author": {"@type": "Person", "name": "Shoaib Hussan", "jobTitle": "Founder, D3DDD – Dubai 3D Design & Draft", "url": f"{D}/about.html", "sameAs": [IG, LINKEDIN, FIVERR]},
        "publisher": {"@id": f"{D}/#business"},
        "mainEntityOfPage": p["url"],
        "articleSection": p["category_title"],
        "inLanguage": "en-AE",
        "wordCount": p["word_count"],
    }

def load_posts() -> list[dict]:
    posts = [parse_post(p) for p in sorted(POSTS_DIR.glob("*.md"))]
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts

def write(path: Path, html_out: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html_out, encoding="utf-8")

def build_index(posts: list[dict]) -> None:
    cards = []
    for p in posts:
        cards.append(
            f'<a class="card post-card" href="{esc(p["slug"])}/">'
            f'<figure><img src="{esc(p["image"])}" alt="{esc(p["image_alt"])}" width="1200" height="630" loading="lazy" decoding="async"></figure>'
            f'<div class="b"><p class="eyebrow">{esc(p["category_title"])}</p>'
            f'<time datetime="{esc(p["date"])}">{esc(p["date"])}</time>'
            f'<h2>{esc(p["title"])}</h2><p>{esc(p["description"])}</p>'
            f'<span class="more">Read article →</span></div></a>'
        )
    cats = sorted({(p["category"], p["category_title"]) for p in posts})
    chips = "".join(
        f'<a class="chip" href="category/{esc(c)}/">{esc(t)}</a>' for c, t in cats
    )
    byline = AUTHOR_BYLINE.replace("../../", "../")
    body = f'''<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a> / <span>Blog</span></nav>
<p class="eyebrow">Insights</p><h1>Architecture &amp; drafting <em>notes.</em></h1>
<p>Researched articles on megaprojects, stone detailing and documentation habits — written for contractors, fabricators and design teams.</p>
{byline}
<p class="chips" style="margin-top:18px">{chips}<a class="chip" href="feed.xml">RSS</a></p></section>
<section class="section"><div class="wrap"><div class="grid g3 post-grid">{"".join(cards)}</div></div></section>'''
    ld = [
        business_ld(),
        {"@type": "Blog", "name": "D3DDD Blog", "url": f"{D}/blog/", "publisher": {"@id": f"{D}/#business"}},
        crumbs_ld([("Home", f"{D}/"), ("Blog", f"{D}/blog/")]),
    ]
    write(
        BLOG_DIR / "index.html",
        shell(
            "Blog – Architecture & Drafting Insights | D3DDD",
            "Researched articles on megaprojects, marble shop drawings and drafting practice from D3DDD in Dubai.",
            f"{D}/blog/",
            body,
            "../",
            ld,
        ),
    )

def build_article(p: dict, all_posts: list[dict]) -> None:
    related = [x for x in all_posts if x["slug"] != p["slug"]][:2]
    rel_html = "".join(
        f'<li><a href="../{esc(r["slug"])}/">{esc(r["title"])}</a></li>' for r in related
    )
    credit = f'<p class="img-credit">{esc(p["image_credit"])}</p>' if p["image_credit"] else ""
    body = f'''<article class="article">
<section class="page-hero">
<nav class="crumbs" aria-label="Breadcrumb"><a href="../../">Home</a> / <a href="../">Blog</a> / <a href="../category/{esc(p["category"])}/">{esc(p["category_title"])}</a> / <span>{esc(p["title"])}</span></nav>
<p class="eyebrow">{esc(p["category_title"])}</p>
<h1>{esc(p["title"])}</h1>
<p class="meta"><time datetime="{esc(p["date"])}">{esc(p["date"])}</time> · {p["word_count"]} words</p>
{AUTHOR_BYLINE}
</section>
<section class="section"><div class="wrap article-wrap">
<figure class="hero-fig"><img src="{esc(p["image"])}" alt="{esc(p["image_alt"])}" width="1200" height="630" fetchpriority="high" decoding="async">{credit}</figure>
<div class="prose">{p["body_html"]}</div>
{AUTHOR_BOX}
<aside class="box related"><h2>Related</h2><ul>{rel_html}</ul>
<p style="margin-top:14px"><a class="btn" href="../../contact.html">Request a quote →</a>
<a class="btn ghost" href="../">All articles</a></p></aside>
</div></section></article>'''
    ld = [
        business_ld(),
        article_ld(p),
        crumbs_ld([
            ("Home", f"{D}/"),
            ("Blog", f"{D}/blog/"),
            (p["category_title"], f"{D}/blog/category/{p['category']}/"),
            (p["title"], p["url"]),
        ]),
    ]
    write(
        BLOG_DIR / p["slug"] / "index.html",
        shell(
            f'{p["title"]} | D3DDD Blog',
            p["description"],
            p.get("canonical") or p["url"],
            body,
            "../../",
            ld,
            og_type="article",
            image=p["image"],
            og_url=p["url"],
        ),
    )

def build_categories(posts: list[dict]) -> None:
    by_cat: dict[str, list[dict]] = {}
    titles: dict[str, str] = {}
    for p in posts:
        by_cat.setdefault(p["category"], []).append(p)
        titles[p["category"]] = p["category_title"]
    for cat, items in by_cat.items():
        cards = "".join(
            f'<a class="card post-card" href="../../{esc(p["slug"])}/">'
            f'<div class="b"><time datetime="{esc(p["date"])}">{esc(p["date"])}</time>'
            f'<h2>{esc(p["title"])}</h2><p>{esc(p["description"])}</p>'
            f'<span class="more">Read article →</span></div></a>'
            for p in items
        )
        title = titles[cat]
        body = f'''<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="../../../">Home</a> / <a href="../../">Blog</a> / <span>{esc(title)}</span></nav>
<p class="eyebrow">Category</p><h1>{esc(title)}</h1></section>
<section class="section"><div class="wrap"><div class="grid g2 post-grid">{cards}</div></div></section>'''
        ld = [
            business_ld(),
            crumbs_ld([
                ("Home", f"{D}/"),
                ("Blog", f"{D}/blog/"),
                (title, f"{D}/blog/category/{cat}/"),
            ]),
        ]
        write(
            BLOG_DIR / "category" / cat / "index.html",
            shell(
                f"{title} – D3DDD Blog",
                f"Articles in {title} from the D3DDD blog.",
                f"{D}/blog/category/{cat}/",
                body,
                "../../../",
                ld,
            ),
        )

def build_rss(posts: list[dict]) -> None:
    items = []
    for p in posts:
        items.append(
            f"<item><title>{esc(p['title'])}</title><link>{p['url']}</link>"
            f"<guid isPermaLink=\"true\">{p['url']}</guid>"
            f"<pubDate>{datetime.strptime(p['date'], '%Y-%m-%d').strftime('%a, %d %b %Y 00:00:00 +0400')}</pubDate>"
            f"<description>{esc(p['description'])}</description></item>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>'
        f"<title>D3DDD Blog</title><link>{D}/blog/</link>"
        "<description>Architecture and drafting insights from D3DDD.</description>"
        f"<language>en-ae</language>{''.join(items)}</channel></rss>\n"
    )
    write(BLOG_DIR / "feed.xml", xml)

def patch_sitemap(posts: list[dict]) -> None:
    sm = ROOT / "sitemap.xml"
    text = sm.read_text(encoding="utf-8") if sm.exists() else (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n'
    )
    # strip previous blog urls
    text = re.sub(r"\s*<url><loc>https://d3ddd\.com/blog/[^<]*</loc>.*?</url>", "", text)
    entries = [
        f'  <url><loc>{D}/blog/</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>',
        f'  <url><loc>{D}/blog/feed.xml</loc><changefreq>weekly</changefreq><priority>0.3</priority></url>',
    ]
    cats = sorted({p["category"] for p in posts})
    for c in cats:
        entries.append(
            f'  <url><loc>{D}/blog/category/{c}/</loc><changefreq>weekly</changefreq><priority>0.5</priority></url>'
        )
    for p in posts:
        entries.append(
            f'  <url><loc>{p["url"]}</loc><lastmod>{p["date"]}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>'
        )
    if "</urlset>" not in text:
        text = text.rstrip() + "\n</urlset>\n"
    text = text.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
    sm.write_text(text, encoding="utf-8")
    robots = ROOT / "robots.txt"
    r = robots.read_text(encoding="utf-8") if robots.exists() else "User-agent: *\nAllow: /\n"
    if "Sitemap:" not in r:
        r = r.rstrip() + f"\nSitemap: {D}/sitemap.xml\n"
    elif f"{D}/sitemap.xml" not in r:
        r = r.rstrip() + f"\nSitemap: {D}/sitemap.xml\n"
    robots.write_text(r if r.endswith("\n") else r + "\n", encoding="utf-8")

def main() -> None:
    posts = load_posts()
    if not posts:
        raise SystemExit("No posts in posts/")
    build_index(posts)
    for p in posts:
        build_article(p, posts)
    build_categories(posts)
    build_rss(posts)
    patch_sitemap(posts)
    print(f"blog: {len(posts)} posts → blog/")

if __name__ == "__main__":
    main()

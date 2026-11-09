"""Arabic blog extension. Editorial drafts require --include-drafts (local review only)."""
from __future__ import annotations
import re
from datetime import datetime
from html.parser import HTMLParser


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def visible_text(markup):
    parser = VisibleText()
    parser.feed(markup)
    return ' '.join(parser.parts).strip()


def load_arabic(b, include_drafts=False):
    posts = []
    for path in sorted((b.POSTS_DIR / 'ar').glob('*.md')):
        p = b.parse_post(path)
        if p.get('status', '').upper() == 'DRAFT' and not include_drafts:
            continue
        p['url'] = f"{b.D}/ar/blog/{p['slug']}/"
        p['lang'] = 'ar-AE'
        posts.append(p)
    return sorted(posts, key=lambda p: p['date'], reverse=True)


def alternates(b, p):
    pairs = [('ar-AE', p['url']), ('ar', p['url'])]
    twin = p.get('translation_of')
    if twin:
        en = f"{b.D}/blog/{twin}/"
        pairs += [('en-AE', en), ('en', en), ('x-default', en)]
    else:
        # No English article exists; do not point en hreflang at another URL.
        pairs.append(('x-default', p['url']))
    return ''.join(f'<link rel="alternate" hreflang="{lang}" href="{url}">' for lang, url in pairs)


def author(b):
    byline = b.AUTHOR_BYLINE.replace('Written by ', 'بقلم ').replace('Shoaib Hussan', 'شعيب حسن').replace('Founder, D3DDD', 'مؤسس D3DDD')
    box = b.AUTHOR_BOX.replace('About the author', 'عن الكاتب').replace('Shoaib Hussan', 'شعيب حسن')
    box = box.replace('Draftsman and founder of ', 'رسام ومؤسس ')
    box = box.replace('Shop drawings, marble &amp; stone detailing, 3D visualisation and construction documentation for contractors and fabricators across the Gulf.', 'رسومات تنفيذية وتفاصيل للرخام والحجر، وإظهار ثلاثي الأبعاد ووثائق تنفيذ للمقاولين والمصنّعين في الخليج.')
    box = box.replace('../../contact.html', '/ar/contact.html').replace('Work with D3DDD →', 'تواصل مع D3DDD')
    return byline, box


def shell(b, title, desc, url, body, ld, p=None):
    social = (p.get('og_image') or p['image']) if p else None
    out = b.shell(title, desc, url, body, '/', ld, og_type='article' if p else 'website', image=social)
    out = out.replace('<html lang="en-AE" dir="ltr">', '<html lang="ar-AE" dir="rtl">')
    out = out.replace('og:site_name" content="D3DDD – Dubai 3D Design &amp; Draft', 'og:site_name" content="D3DDD – دبي للتصميم والرسم ثلاثي الأبعاد')
    out = out.replace('content="en_AE"', 'content="ar_AE"').replace('Skip to content', 'انتقل إلى المحتوى').replace('Open menu', 'فتح القائمة')
    out = out.replace('href="https://d3ddd.com/blog/feed.xml"', 'href="https://d3ddd.com/ar/blog/feed.xml"')
    out = out.replace('title="D3DDD Blog"', 'title="مدونة D3DDD بالعربية"')
    out = out.replace('DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@1,500', 'Tajawal:wght@400;700&family=DM+Sans:wght@400;600;700')
    nav = ''.join(f'<a href="{href}">{label}</a>' for href, label in [('/ar/', 'الرئيسية'), ('/ar/services/', 'الخدمات'), ('/projects/', 'المشاريع'), ('/ar/marble.html', 'رسومات الرخام'), ('/ar/blog/', 'المدونة'), ('/ar/contact.html', 'تواصل معنا')])
    en = f"/blog/{p['translation_of']}/" if p and p.get('translation_of') else '/blog/'
    nav += f'<a class="lang" href="{en}" hreflang="en-AE" lang="en">English</a>'
    out = out.replace(b.nav('/', 'blog'), nav)
    foot = '''<footer><div class="grid"><div><h2>D3DDD</h2><p>رسومات تنفيذية وتفاصيل رخام وإظهار ثلاثي الأبعاد لمشاريع دبي وأبوظبي والشارقة والإمارات.</p></div><div><h2>الخدمات والمشاريع</h2><a href="/ar/marble.html">رسومات الرخام</a><a href="/projects/">المشاريع</a></div><div><h2>المدونة</h2><a href="/ar/blog/">مقالات بالعربية</a><a href="/blog/" lang="en">English blog</a><a href="/ar/blog/feed.xml">خلاصة RSS</a></div><div><h2>تواصل معنا</h2><a href="/ar/contact.html">نموذج التواصل</a><a href="https://instagram.com/mxhaib" rel="me noopener" target="_blank">Instagram</a><a href="https://www.linkedin.com/in/mshoaib94" rel="me noopener" target="_blank">LinkedIn</a><address class="postal">Dubai, United Arab Emirates</address></div></div><div class="copy">© D3DDD. جميع الحقوق محفوظة.</div></footer>'''
    out = out.replace(b.footer('/'), foot)
    extras = '<link rel="stylesheet" href="/assets/ar-blog.css">'
    if p:
        out = out.replace('og:image:width" content="1200', 'og:image:width" content="1600').replace('og:image:height" content="630', 'og:image:height" content="1304')
        extras += alternates(b, p)
        extras += f'<meta name="keywords" content="{b.esc(p.get("keywords", ""))}">'
        extras += f'<meta property="og:image:alt" content="{b.esc(p["image_alt"])}"><meta name="twitter:image:alt" content="{b.esc(p["image_alt"])}">'
        if p.get('status', '').upper() == 'DRAFT':
            out = out.replace('index, follow, max-image-preview:large', 'noindex, follow')
    return out.replace('</head>', extras + '</head>')


def faq_ld(b, p):
    # Schema answers come from the visible FAQ, preventing content/schema drift.
    match = re.search(r'^## (?:الأسئلة الشائعة|أسئلة شائعة).*$', p['body_md'], re.M)
    if not match:
        raise SystemExit(f"{p['slug']}: missing FAQ heading")
    section = p['body_md'][match.end():].split('\n## ', 1)[0]
    items = []
    for question in section.split('\n### ')[1:]:
        name, answer = question.split('\n', 1)
        items.append({'@type': 'Question', 'name': name.strip(), 'acceptedAnswer': {'@type': 'Answer', 'text': visible_text(b.markdown.markdown(answer))}})
    return {'@type': 'FAQPage', 'inLanguage': 'ar-AE', 'mainEntity': items}


def build_arabic(b, english_posts, include_drafts=False):
    posts = load_arabic(b, include_drafts)
    if not posts:
        return
    base = b.ROOT / 'ar/blog'
    byline, box = author(b)
    for p in posts:
        # Count rendered prose, excluding Markdown syntax and link destinations.
        p['word_count'] = len(visible_text(p['body_html']).split())
        twin = p.get('translation_of')
        en = next((x for x in english_posts if x['slug'] == twin), None) if twin else None
        if twin and en is None:
            raise SystemExit(f"{p['slug']}: translation_of {twin} has no English post")
        article = b.article_ld(p)
        article['inLanguage'] = 'ar-AE'
        article['author']['name'] = 'شعيب حسن'
        article['author']['jobTitle'] = 'مؤسس D3DDD'
        if en:
            article['translationOfWork'] = {'@type': 'Article', 'url': en['url'], 'inLanguage': 'en-AE'}
        body = f'''<article class="article"><section class="page-hero"><nav class="crumbs" aria-label="مسار التنقل"><a href="/ar/">الرئيسية</a> / <a href="/ar/blog/">المدونة</a> / <a href="/ar/blog/category/{p['category']}/">{b.esc(p['category_title'])}</a></nav><p class="eyebrow">{b.esc(p['category_title'])}</p><h1>{b.esc(p['title'])}</h1><p class="meta"><time datetime="{p['date']}">{p['date']}</time> · {p['word_count']} كلمة</p>{byline}</section><section class="section"><div class="wrap article-wrap"><figure class="hero-fig"><img src="{b.esc(p['image'])}" alt="{b.esc(p['image_alt'])}" width="1600" height="1304" fetchpriority="high" decoding="async"></figure><div class="prose">{p['body_html']}</div>{box}</div></section></article>'''
        ld = [b.business_ld(), article, faq_ld(b, p), b.crumbs_ld([('الرئيسية', b.D + '/ar/'), ('المدونة', b.D + '/ar/blog/'), (p['title'], p['url'])])]
        b.write(base / p['slug'] / 'index.html', shell(b, p.get('seo_title', p['title']), p['description'], p['url'], body, ld, p))
        # Only the English sibling changes; other articles' Related lists stay intact.
        if en:
            sibling = b.BLOG_DIR / en['slug'] / 'index.html'
            text = sibling.read_text()
            text = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">', '', text)
            text = text.replace('</head>', alternates(b, p) + '</head>')
            sibling.write_text(text)
    cards = ''.join(f'<a class="card post-card" href="{p["url"].replace(b.D, "")}"><div class="b"><h2>{b.esc(p["title"])}</h2><p>{b.esc(p["description"])}</p></div></a>' for p in posts)
    def listing(title, url, items):
        body = f'<section class="page-hero"><h1>{title}</h1><p>مقالات عملية للمقاولين والمصنّعين وفرق التشطيبات في الإمارات.</p></section><section class="section"><div class="wrap grid g2 post-grid">{items}</div></section>'
        return shell(b, title + ' | D3DDD', 'أدلة عملية بالعربية عن رسومات الرخام والتنسيق والتصنيع لمشاريع الإمارات.', url, body, [b.business_ld()])
    b.write(base / 'index.html', listing('مدونة D3DDD بالعربية', b.D + '/ar/blog/', cards))
    for cat in sorted({p['category'] for p in posts}):
        items = [p for p in posts if p['category'] == cat]
        cat_cards = ''.join(f'<a class="card post-card" href="/ar/blog/{p["slug"]}/"><div class="b"><h2>{b.esc(p["title"])}</h2><p>{b.esc(p["description"])}</p></div></a>' for p in items)
        b.write(base / 'category' / cat / 'index.html', listing(items[0]['category_title'], f'{b.D}/ar/blog/category/{cat}/', cat_cards))
    items = ''.join(f'<item><title>{b.esc(p["title"])}</title><link>{p["url"]}</link><guid isPermaLink="true">{p["url"]}</guid><pubDate>{datetime.strptime(p["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 00:00:00 +0400")}</pubDate><description>{b.esc(p["description"])}</description></item>' for p in posts)
    b.write(base / 'feed.xml', f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>مدونة D3DDD بالعربية</title><link>{b.D}/ar/blog/</link><description>رسومات الرخام والتشطيبات في الإمارات</description><language>ar-ae</language>{items}</channel></rss>')
    # Link to the Arabic index without adding Arabic posts to English Related lists.
    idx = b.BLOG_DIR / 'index.html'
    text = idx.read_text()
    chip = '<a class="chip" href="/ar/blog/" lang="ar" hreflang="ar-AE">مقالات بالعربية</a>'
    text = text.replace(chip, "").replace('<a class="chip" href="feed.xml">RSS</a>', '<a class="chip" href="feed.xml">RSS</a>' + chip)
    idx.write_text(text)
    sm = b.ROOT / 'sitemap.xml'
    text = re.sub(r'\s*<url><loc>https://d3ddd\.com/ar/blog/[^<]*</loc>.*?</url>', '', sm.read_text())
    urls = [b.D + '/ar/blog/', b.D + '/ar/blog/feed.xml'] + [f'{b.D}/ar/blog/category/{cat}/' for cat in sorted({p['category'] for p in posts})] + [p['url'] for p in posts]
    entries = '\n'.join(f'  <url><loc>{url}</loc></url>' for url in urls)
    sm.write_text(text.replace('</urlset>', entries + '\n</urlset>'))
    print(f'Arabic blog: {len(posts)} posts (include_drafts={include_drafts})')

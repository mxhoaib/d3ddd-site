# D3DDD static site generator (English + Arabic). Edit content here, then run: python3 build.py
import json, os
D = "https://d3ddd.com/"
EMAIL = "dxb3ddeaign@gmail.com"
BILINGUAL = ["index.html", "services.html", "marble.html", "website-design.html", "about.html", "contact.html"]
AREAS = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Umm Al Quwain", "Fujairah"]

def url(lang, fn):
    base = D + ("ar/" if lang == "ar" else "")
    return base + ("" if fn == "index.html" else fn)

def img(P, name, alt, eager=False, w=400, h=300):
    return (f'<img src="{P}assets/img/drawings/{name}.svg" alt="{alt}" width="{w}" height="{h}" '
            f'{"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} decoding="async">')

ORG_ID = D + "#business"
def business_ld(lang):
    return {"@type": ["ProfessionalService", "LocalBusiness"], "@id": ORG_ID,
            "name": "D3DDD – Dubai 3D Design & Draft", "alternateName": ["D3DDD", "دبي للتصميم والرسم ثلاثي الأبعاد"],
            "url": D, "logo": D + "assets/img/logo.svg", "image": D + "assets/img/og-image.png",
            "email": EMAIL,
            "description": "Marble and stone shop drawings, AutoCAD drafting, fit-out drawings, 3D rendering and contractor website design in Dubai and across the UAE.",
            "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressRegion": "Dubai", "addressCountry": "AE"},
            "areaServed": [{"@type": "City", "name": a} for a in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah"]] + [{"@type": "Country", "name": "United Arab Emirates"}],
            "knowsLanguage": ["en", "ar"],
            "contactPoint": {"@type": "ContactPoint", "email": EMAIL, "contactType": "sales", "availableLanguage": ["English", "Arabic"]},
            "sameAs": []}

def crumbs_ld(lang, items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def service_ld(name, desc, u, offers=None):
    s = {"@type": "Service", "name": name, "description": desc, "url": u, "provider": {"@id": ORG_ID},
         "areaServed": [{"@type": "City", "name": a} for a in ["Dubai", "Abu Dhabi", "Sharjah"]] + [{"@type": "Country", "name": "United Arab Emirates"}]}
    if offers: s["offers"] = offers
    return s

def faq_ld(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs, title, eyebrow):
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'<section class="section alt faq" id="faq" aria-labelledby="faq-h"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h2 id="faq-h" style="margin-bottom:20px">{title}</h2>{items}</div></section>'

# ---------------------------------------------------------------- language strings
T = {
 "en": dict(dir="ltr", locale="en_AE", P="", nav=[("index.html","Home"),("services.html","Services"),("marble.html","Marble Shop Drawings"),("website-design.html","Website Design"),("about.html","About"),("contact.html","Contact")],
   login="Client Login", menu="Open menu", skip="Skip to content", switch="العربية",
   tagline="Marble & stone shop drawings, AutoCAD drafting, 3D rendering and contractor websites in Dubai, Abu Dhabi, Sharjah and across the UAE.",
   f_services="Services", f_company="Company", f_contact="Contact", portal="Client portal", rights="All rights reserved.", home="Home",
   cta_eye="Let’s work together", cta_h="Your vision. Our precision.", cta_p="Send your drawings, sketches, dimensions or project requirements for a quote — in English or Arabic.", cta_wa="Email us", cta_form="Send an enquiry",
   fonts="family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@1,500&family=Tajawal:wght@500&display=swap"),
 "ar": dict(dir="rtl", locale="ar_AE", P="../", nav=[("index.html","الرئيسية"),("services.html","الخدمات"),("marble.html","رسومات الرخام"),("website-design.html","تصميم المواقع"),("about.html","من نحن"),("contact.html","تواصل معنا")],
   login="بوابة العملاء", menu="فتح القائمة", skip="انتقل إلى المحتوى", switch="English",
   tagline="رسومات تنفيذية للرخام والحجر، مخططات أوتوكاد، تصميم ثلاثي الأبعاد ومواقع إلكترونية للمقاولين في دبي وأبوظبي والشارقة وجميع أنحاء الإمارات.",
   f_services="الخدمات", f_company="الشركة", f_contact="التواصل", portal="بوابة العملاء", rights="جميع الحقوق محفوظة.", home="الرئيسية",
   cta_eye="لنعمل معاً", cta_h="رؤيتك. دقتنا.", cta_p="أرسل مخططاتك أو رسوماتك الأولية أو المقاسات أو متطلبات مشروعك للحصول على عرض سعر — بالعربية أو الإنجليزية.", cta_wa="راسلنا عبر البريد", cta_form="أرسل استفسارك",
   fonts="family=Tajawal:wght@400;500;700&family=DM+Sans:wght@400;600;700&display=swap"),
}

def head(lang, fn, title, desc, ld_nodes, noindex=False, bilingual=True, preload=None):
    t = T[lang]; P = t["P"]; canon = url(lang, fn)
    alts = ""
    if bilingual:
        alts = (f'<link rel="alternate" hreflang="en-AE" href="{url("en", fn)}"><link rel="alternate" hreflang="en" href="{url("en", fn)}">'
                f'<link rel="alternate" hreflang="ar-AE" href="{url("ar", fn)}"><link rel="alternate" hreflang="ar" href="{url("ar", fn)}">'
                f'<link rel="alternate" hreflang="x-default" href="{url("en", fn)}">')
    og_alt = 'ar_AE' if lang == 'en' else 'en_AE'
    ld = json.dumps({"@context": "https://schema.org", "@graph": [business_ld(lang)] + ld_nodes}, ensure_ascii=False)
    pre = f'<link rel="preload" as="image" href="{P}assets/img/drawings/{preload}.svg" fetchpriority="high">' if preload else ""
    return f'''<!DOCTYPE html>
<html lang="{"ar-AE" if lang=="ar" else "en-AE"}" dir="{t["dir"]}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta name="robots" content="{"noindex, follow" if noindex else "index, follow, max-image-preview:large"}">
<link rel="canonical" href="{canon}">{alts}
<meta name="geo.region" content="AE-DU"><meta name="geo.placename" content="Dubai, United Arab Emirates"><meta name="geo.position" content="25.2048;55.2708"><meta name="ICBM" content="25.2048, 55.2708">
<meta property="og:type" content="website"><meta property="og:site_name" content="D3DDD – Dubai 3D Design &amp; Draft"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}"><meta property="og:locale" content="{t["locale"]}"><meta property="og:locale:alternate" content="{og_alt}"><meta property="og:image" content="{D}assets/img/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="D3DDD – architectural line drawing of a marble kitchen island">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{D}assets/img/og-image.png">
<meta name="theme-color" content="#0e0e0c"><meta name="format-detection" content="telephone=no"><link rel="icon" href="{P}assets/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{P}assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="{P}assets/style.css" as="style"><link rel="stylesheet" href="{P}assets/style.css">{pre}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{t["fonts"]}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?{t["fonts"]}"></noscript>
<script type="application/ld+json">{ld}</script></head>'''

def shell(lang, fn, title, desc, body, ld_nodes=(), noindex=False, bilingual=True, scripts="", preload=None):
    t = T[lang]; P = t["P"]
    nav = "".join(f'<a href="{h if h!="index.html" else "./"}"{" aria-current=page" if h==fn else ""}>{n}</a>' for h, n in t["nav"])
    other = "ar" if lang == "en" else "en"
    sw_href = (("ar/" if lang == "en" else "../") + ("" if fn == "index.html" else fn)) if bilingual else ("ar/" if lang == "en" else "../")
    if lang == "en" and not bilingual and fn in ("login.html","signup.html","dashboard.html"): sw_href = "ar/"
    login_href = f"{P}login.html"
    S = {k: v for k, v in t.items()}
    fs = "".join(f'<a href="{h}">{n}</a>' for h, n in t["nav"][1:4])
    fc = "".join(f'<a href="{h}">{n}</a>' for h, n in [t["nav"][4], t["nav"][5]]) + f'<a href="{login_href}">{t["portal"]}</a>'
    return head(lang, fn, title, desc, list(ld_nodes), noindex, bilingual, preload) + f'''<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="site-header"><a class="logo" href="{"./" if lang=="en" or True else ""}" aria-label="D3DDD – Dubai 3D Design &amp; Draft"><span>D3</span><strong>DDD</strong><small>Dubai 3D Design &amp; Draft</small></a>
<button class="menu-toggle" aria-label="{t["menu"]}" aria-expanded="false" aria-controls="nav">☰</button>
<nav class="nav" id="nav" aria-label="Main">{nav}<a class="lang" href="{sw_href}" hreflang="{other}" lang="{other}">{t["switch"]}</a><a class="pill" href="{login_href}">{t["login"]}</a></nav></header>
<main id="main">{body}</main>
<footer><div class="grid"><div><div class="logo"><span>D3</span><strong>DDD</strong><small>Dubai 3D Design &amp; Draft</small></div><p style="margin-top:16px;max-width:340px">{t["tagline"]}</p></div>
<div><h2>{t["f_services"]}</h2>{fs}</div><div><h2>{t["f_company"]}</h2>{fc}</div>
<div><h2>{t["f_contact"]}</h2><a href="contact.html">{t["cta_form"]}</a><a href="mailto:{EMAIL}">{EMAIL}</a><span>{"Dubai, United Arab Emirates" if lang=="en" else "دبي، الإمارات العربية المتحدة"}</span></div></div>
<div class="copy">© <span data-year>2026</span> D3DDD – Dubai 3D Design &amp; Draft. {t["rights"]}</div></footer>
<script src="{P}assets/config.js" defer></script><script src="{P}assets/site.js" defer></script>{scripts}</body></html>'''

def cta(lang):
    t = T[lang]
    return f'<section class="cta-band"><p class="eyebrow">{t["cta_eye"]}</p><h2>{t["cta_h"]}</h2><p>{t["cta_p"]}</p><div class="actions"><a class="btn" href="contact.html">{t["cta_form"]}</a><a class="btn ghost" href="mailto:{EMAIL}">{t["cta_wa"]}</a></div></section>'

def crumb_html(lang, name):
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="./">{T[lang]["home"]}</a> / <span>{name}</span></nav>'

def page_hero(lang, eyebrow, h1, p, name):
    return f'<section class="page-hero">{crumb_html(lang, name)}<p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p>{p}</p></section>'

from content import build_pages  # page content lives in content.py
out = build_pages(globals())
for (lang, fn), html in out.items():
    path = ("ar/" if lang == "ar" else "") + fn
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(html)

# portal pages (English only, noindex)
ns = {}; exec(open("portal_pages.py").read(), ns)
for fn, (t, d, b, *rest) in ns["pages"].items():
    open(fn, "w").write(shell("en", fn, t, d, b, (), True, False, rest[1] if len(rest) > 1 else ""))

# sitemap with hreflang alternates
x = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for fn in BILINGUAL:
    for lang in ("en", "ar"):
        pr = "1.0" if fn == "index.html" else "0.8"
        x.append(f'  <url><loc>{url(lang, fn)}</loc><changefreq>monthly</changefreq><priority>{pr}</priority>'
                 f'<xhtml:link rel="alternate" hreflang="en-AE" href="{url("en", fn)}"/><xhtml:link rel="alternate" hreflang="ar-AE" href="{url("ar", fn)}"/>'
                 f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("en", fn)}"/></url>')
x.append('</urlset>')
open("sitemap.xml", "w").write("\n".join(x) + "\n")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /dashboard.html\nDisallow: /login.html\nDisallow: /signup.html\nDisallow: /thank-you.html\nDisallow: /ar/thank-you.html\nSitemap: {D}sitemap.xml\n")
print("built", len(out) + len(ns["pages"]), "pages")

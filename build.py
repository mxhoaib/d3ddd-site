# D3DDD static site generator (English + Arabic). Edit content here, then run: python3 build.py
import html, json, os
import site_search
from contact_config import whatsapp_html, analytics_snippet, mail_link, social_links, business_node, area_served
D = "https://d3ddd.com/"
EMAIL = "info@d3ddd.com"
BILINGUAL = ["index.html", "services.html", "marble.html", "website-design.html", "about.html", "contact.html"]
AREAS = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Umm Al Quwain", "Fujairah"]

def url(lang, fn):
    base = D + ("ar/" if lang == "ar" else "")
    if fn in ("", "index.html"):
        return base
    if fn.endswith("/index.html"):
        return base + fn[:-len("index.html")]
    return base + fn

def prefix(lang, fn):
    depth = fn.count("/")
    if lang == "ar":
        depth += 1
    return "../" * depth

def href(lang, fn, target):
    # Same-language pages. prefix() is for assets and is one level deeper under /ar/.
    p = "../" * fn.count("/")
    if target in ("", "index.html"):
        return p if p else "./"
    return p + target

def en_href(lang, fn, target):
    # Blog and individual project sheets exist in English only.
    return prefix(lang, fn) + target

SERVICE_FOOTER = [
    ("services/architectural-drafting/", "Architectural drafting", "الرسم المعماري التنفيذي"),
    ("fitout-shop-drawings/", "Fit-out &amp; joinery drawings", "رسومات الفيت آوت والنجارة"),
    ("services/architectural-designing/", "Architectural designing", "التصميم المعماري"),
    ("services/architectural-estimation/", "Architectural estimation", "حساب الكميات"),
    ("services/3d-rendering-modeling-visualization/", "3D rendering & visualization", "تصميم ثلاثي الأبعاد"),
    ("services/website-development-designing/", "Website development", "تطوير المواقع"),
]

INDUSTRY_LINKS = [
    ("construction-companies-uae/", "Construction companies", "شركات المقاولات"),
    ("real-estate-developers-uae/", "Real estate developers", "المطورون العقاريون"),
    ("interior-design-companies-uae/", "Interior design firms", "شركات التصميم الداخلي"),
    ("marble-contractors-uae/", "Marble contractors", "مقاولو الرخام"),
]

EN_ONLY_PATHS = {path for path, _, _ in INDUSTRY_LINKS} | {"fitout-shop-drawings/"}

def site_href(lang, fn, target):
    if target in EN_ONLY_PATHS:
        return en_href(lang, fn, target)
    return href(lang, fn, target)

def img(P, name, alt, eager=False, w=400, h=300):
    return (f'<img src="{P}assets/img/drawings/{name}.svg" alt="{alt}" width="{w}" height="{h}" '
            f'{"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} decoding="async">')

ORG_ID = D + "#business"
def business_ld(lang, fn=""):
    node = business_node()
    # Homepage only: Organization typing plus the main-services catalogue on the one business node.
    if fn == "index.html":
        node = dict(node)
        types = list(node.get("@type") or [])
        if "Organization" not in types:
            node["@type"] = ["Organization"] + types
        if HOME_CATALOG.get(lang):
            node["hasOfferCatalog"] = HOME_CATALOG[lang]
    return node

# Filled by content.py for the EN/AR homepages: {"en": OfferCatalog, "ar": OfferCatalog}
HOME_CATALOG = {}

def crumbs_ld(lang, items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def service_ld(name, desc, u, offers=None):
    s = {"@type": "Service", "name": name, "description": desc, "url": u, "provider": {"@id": ORG_ID},
         "areaServed": area_served()}
    if offers: s["offers"] = offers
    return s

def faq_ld(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs, title, eyebrow):
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'<section class="section alt faq" id="faq" aria-labelledby="faq-h"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h2 id="faq-h" class="mb-20">{title}</h2>{items}</div></section>'

# ---------------------------------------------------------------- language strings
T = {
 "en": dict(dir="ltr", locale="en_AE", P="", nav=[("index.html","Home"),("services/","Services"),("projects/","Projects"),("marble.html","Marble Shop Drawings"),("website-design.html","Website Design"),("blog/","Blog"),("apps/","Web Apps"),("about.html","About"),("contact.html","Contact")],
   login="Client Login", menu="Open menu", skip="Skip to content", switch="العربية",
   tagline="Marble & stone shop drawings, AutoCAD drafting, 3D rendering and contractor websites in Dubai, Abu Dhabi, Sharjah and across the UAE.",
   f_services="Services", f_company="Company", f_industries="Industries", f_contact="Contact", portal="Client portal", rights="All rights reserved.", home="Home",
   cta_eye="Let’s work together", cta_h="Your vision. Our precision.", cta_p="Send your drawings, sketches, dimensions or project requirements for a quote — in English or Arabic.", cta_wa="Email us", cta_form="Send an enquiry",
   fonts="family=DM+Sans:wght@400;600;700&family=Playfair+Display:ital,wght@1,500&family=Tajawal:wght@500&display=swap"),
 "ar": dict(dir="rtl", locale="ar_AE", P="../", nav=[("index.html","الرئيسية"),("services/","الخدمات"),("projects/","المشاريع"),("marble.html","رسومات الرخام"),("website-design.html","تصميم المواقع"),("blog/","المدونة"),("apps/","تطبيقات الويب"),("about.html","من نحن"),("contact.html","تواصل معنا")],
   login="بوابة العملاء", menu="فتح القائمة", skip="انتقل إلى المحتوى", switch="English",
   tagline="رسومات تنفيذية للرخام والحجر، مخططات أوتوكاد، تصميم ثلاثي الأبعاد ومواقع إلكترونية للمقاولين في دبي وأبوظبي والشارقة وجميع أنحاء الإمارات.",
   f_services="الخدمات", f_company="الشركة", f_industries="القطاعات", f_contact="التواصل", portal="بوابة العملاء", rights="جميع الحقوق محفوظة.", home="الرئيسية",
   cta_eye="لنعمل معاً", cta_h="رؤيتك. دقتنا.", cta_p="أرسل مخططاتك أو رسوماتك الأولية أو المقاسات أو متطلبات مشروعك للحصول على عرض سعر — بالعربية أو الإنجليزية.", cta_wa="راسلنا عبر البريد", cta_form="أرسل استفسارك",
   fonts="family=Tajawal:wght@400;700&family=DM+Sans:wght@400;600;700&display=swap"),
}

def head(lang, fn, title, desc, ld_nodes, noindex=False, bilingual=True, preload=None, og_image=None, extra_head=""):
    t = T[lang]
    P = prefix(lang, fn)
    canon = url(lang, fn)
    alts = ""
    if bilingual:
        alts = (
            '<link rel="alternate" hreflang="en-AE" href="%s"><link rel="alternate" hreflang="en" href="%s">'
            '<link rel="alternate" hreflang="ar-AE" href="%s"><link rel="alternate" hreflang="ar" href="%s">'
            '<link rel="alternate" hreflang="x-default" href="%s">'
        ) % (url("en", fn), url("en", fn), url("ar", fn), url("ar", fn), url("en", fn))
    og_alt = "ar_AE" if lang == "en" else "en_AE"
    ld = json.dumps({"@context": "https://schema.org", "@graph": [business_ld(lang, fn)] + list(ld_nodes)}, ensure_ascii=False)
    pre = ""
    if preload:
        pre = '<link rel="preload" as="image" href="%sassets/img/drawings/%s.svg" fetchpriority="high">' % (P, preload)
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    lang_attr = "ar-AE" if lang == "ar" else "en-AE"
    # og_image: optional (absolute_url, width, height, alt); default is the site-wide OG image.
    og_src, og_w, og_h, og_a = og_image or (D + "assets/img/og-image.png", 1200, 630, "D3DDD – architectural line drawing of a marble kitchen island")
    og_tags = ('<meta property="og:image" content="%s"><meta property="og:image:width" content="%s"><meta property="og:image:height" content="%s"><meta property="og:image:alt" content="%s">'
               % (og_src, og_w, og_h, og_a))
    return (
        '<!DOCTYPE html>\n'
        '<html lang="%s" dir="%s"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>%s</title><meta name="description" content="%s">\n'
        '<meta name="robots" content="%s">\n'
        '<link rel="canonical" href="%s">%s\n'
        '<meta name="geo.region" content="AE-DU"><meta name="geo.placename" content="Dubai, United Arab Emirates"><meta name="geo.position" content="25.2048;55.2708"><meta name="ICBM" content="25.2048, 55.2708">\n'
        '<meta property="og:type" content="website"><meta property="og:site_name" content="D3DDD – Dubai 3D Design &amp; Draft"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s"><meta property="og:locale" content="%s"><meta property="og:locale:alternate" content="%s">%s\n'
        '<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s"><meta name="twitter:image" content="%s">\n'
        '<meta name="theme-color" content="#0e0e0c"><meta name="format-detection" content="telephone=no"><link rel="icon" href="%sassets/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="%sassets/img/favicon.svg">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="preload" href="%sassets/style.css" as="style"><link rel="stylesheet" href="%sassets/style.css">%s%s\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?%s" media="print" onload="this.media=\'all\'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?%s"></noscript>\n'
        '<script type="application/ld+json">%s</script>\n'
        '<meta name="google-site-verification" content="5lkd8Q8BFpICgD4ixvCvKxc2GmHxE7pH7XFaXVRZG-s" />%s</head>'
    ) % (
        lang_attr, t["dir"], title, desc, robots, canon, alts,
        title, desc, canon, t["locale"], og_alt, og_tags,
        title, desc, og_src, P, P, P, P, pre, extra_head, t["fonts"], t["fonts"], ld, analytics_snippet(),
    )

def nav_href(lang, fn, h):
    if h == "index.html":
        return href(lang, fn, "")
    if h.startswith("blog"):
        return en_href(lang, fn, h)
    return site_href(lang, fn, h)

def _on_page(fn, target):
    return (fn == target) or (target.endswith("/") and (fn == target + "index.html" or fn.startswith(target)))

def _menu_links(lang, fn, items):
    en = lang == "en"
    parts = []
    for path, en_label, ar_label in items:
        cur = ' aria-current="page"' if _on_page(fn, path) else ""
        parts.append('<a href="%s"%s>%s</a>' % (site_href(lang, fn, path), cur, en_label if en else ar_label))
    return "".join(parts)

def services_menu(lang, fn):
    en = lang == "en"
    items = [
        ("services/", "All services", "كل الخدمات"),
        ("services/architectural-drafting/", "Architectural drafting", "الرسم المعماري التنفيذي"),
        ("services/architectural-designing/", "Architectural designing", "التصميم المعماري"),
        ("fitout-shop-drawings/", "Fit-out &amp; joinery drawings", "رسومات الفيت آوت والنجارة"),
        ("services/architectural-estimation/", "Architectural estimation", "حساب الكميات"),
        ("services/3d-rendering-modeling-visualization/", "3D visualization", "تصميم ثلاثي الأبعاد"),
        ("marble.html", "Marble shop drawings", "رسومات الرخام"),
        ("services/website-development-designing/", "Website development", "تطوير المواقع"),
    ]
    label = "Services" if en else "الخدمات"
    caret = "Show services" if en else "عرض الخدمات"
    current = _on_page(fn, "services/") or _on_page(fn, "fitout-shop-drawings/")
    cur = " aria-current=page" if current else ""
    return (
        '<div class="nav-group"><a href="%s"%s>%s</a>'
        '<button type="button" class="nav-drop" aria-expanded="false" aria-controls="nav-services" aria-label="%s">▾</button>'
        '<div class="nav-sub" id="nav-services"><div class="nav-sub-panel">%s</div></div></div>'
    ) % (site_href(lang, fn, "services/"), cur, label, caret, _menu_links(lang, fn, items))

def industries_menu(lang, fn):
    en = lang == "en"
    label = "Industries" if en else "القطاعات"
    current = any(_on_page(fn, path) for path, _, _ in INDUSTRY_LINKS)
    cur = " aria-current=page" if current else ""
    return (
        '<div class="nav-group"><button type="button" class="nav-drop nav-drop-label" aria-expanded="false" aria-controls="nav-industries"%s>%s</button>'
        '<div class="nav-sub" id="nav-industries"><div class="nav-sub-panel">%s</div></div></div>'
    ) % (cur, label, _menu_links(lang, fn, INDUSTRY_LINKS))

GOAT = '<script data-goatcounter="https://d3dddsites.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'

def shell(lang, fn, title, desc, body, ld_nodes=(), noindex=False, bilingual=True, scripts="", preload=None, og_image=None, extra_head="", switch=None):
    t = T[lang]
    P = prefix(lang, fn)
    nav_parts = []
    for h, n in t["nav"]:
        if h == "services/":
            nav_parts.append(services_menu(lang, fn))
            nav_parts.append(industries_menu(lang, fn))
            continue
        current = _on_page(fn, h)
        cur = " aria-current=page" if current else ""
        nav_parts.append('<a href="%s"%s>%s</a>' % (nav_href(lang, fn, h), cur, n))
    nav = "".join(nav_parts)
    other = "ar" if lang == "en" else "en"
    if bilingual:
        if lang == "en":
            if fn == "index.html":
                sw_href = "ar/"
            elif fn.endswith("/index.html"):
                sw_href = "/ar/" + fn[: -len("index.html")]
            else:
                sw_href = "ar/" + fn
        else:
            if fn == "index.html":
                sw_href = "../"
            elif fn.endswith("/index.html"):
                sw_href = "/" + fn[: -len("index.html")]
            else:
                sw_href = "../" + fn
    else:
        sw_href = "ar/" if lang == "en" else "../"
    if lang == "en" and not bilingual and fn in ("login.html", "signup.html", "dashboard.html"):
        sw_href = "ar/"
    if switch:
        sw_href = switch
    blog_href = en_href(lang, fn, "blog/")
    fs = '<a href="%s">%s</a>' % (href(lang, fn, "services/"), "All services" if lang == "en" else "كل الخدمات")
    for path, label_en, label_ar in SERVICE_FOOTER:
        fs += '<a href="%s">%s</a>' % (site_href(lang, fn, path), label_en if lang == "en" else label_ar)
    fi = ""
    for path, label_en, label_ar in INDUSTRY_LINKS:
        fi += '<a href="%s">%s</a>' % (site_href(lang, fn, path), label_en if lang == "en" else label_ar)
    company = [
        ("projects/", "Projects", "المشاريع"),
        ("blog/", "Blog", "المدونة"),
        ("about.html", "About", "من نحن"),
        ("resources/uae-directories/", "UAE Directories", "أدلة الإمارات"),
        ("contact.html", "Contact", "تواصل معنا"),
    ]
    fc = ""
    for path, en_label, ar_label in company:
        english_only = path.startswith("blog") or path.startswith("resources/")
        target = en_href(lang, fn, path) if english_only else href(lang, fn, path)
        cur = ' aria-current="page"' if _on_page(fn, path) else ""
        fc += '<a href="%s"%s>%s</a>' % (target, cur, en_label if lang == "en" else ar_label)
    blog_label = "Blog" if lang == "en" else "المدونة"
    loc = "Dubai, United Arab Emirates"
    home_href = href(lang, fn, "")
    contact_href = href(lang, fn, "contact.html")
    enquiry_label = "Enquiry form" if lang == "en" else "نموذج الاستفسار"
    top = ('<div class="topbar"><span><a href="%s">%s</a> · %s</span>'
           '<span><a href="%s">d3ddd.com</a></span></div>') % (contact_href, enquiry_label, mail_link(contact_href), D)
    if P:
        body = body.replace('href="contact.html"', 'href="%s"' % contact_href)
        body = body.replace('href="services.html"', 'href="%s"' % href(lang, fn, "services/"))
        body = body.replace('href="marble.html"', 'href="%s"' % href(lang, fn, "marble.html"))
        body = body.replace('href="website-design.html"', 'href="%s"' % href(lang, fn, "website-design.html"))
        body = body.replace('href="./"', 'href="%s"' % home_href)
    # Homepage only: line-art hero. No third-party scene runtime.
    if fn == "index.html":
        scripts = '<script src="%sassets/hero.js" defer></script>' % P + (scripts or "")
    return head(lang, fn, title, desc, list(ld_nodes), noindex, bilingual, preload, og_image, extra_head) + (
        '<body>\n'
        '<a class="skip" href="#main">%s</a>\n'
        '%s\n'
        '<header class="site-header"><a class="logo" href="%s" aria-label="D3DDD – Dubai 3D Design and Draft"><span>D3</span><strong>DDD</strong><small>Dubai 3D Design &amp; Draft</small></a>\n'
        '<button class="menu-toggle" aria-label="%s" aria-expanded="false" aria-controls="nav">☰</button>\n'
        '<nav class="nav" id="nav" aria-label="Main">%s<a class="lang" href="%s" hreflang="%s" lang="%s">%s</a></nav>%s</header>\n'
        '<main id="main">%s</main>\n'
        '<footer><div class="grid"><div><div class="logo"><span>D3</span><strong>DDD</strong><small>Dubai 3D Design &amp; Draft</small></div><p class="footer-intro">%s</p>\n'
        '<p class="mt-12">%s%s · <a href="%s">d3ddd.com</a></p>%s</div>\n'
        '<div><h2>%s</h2>%s</div><div><h2>%s</h2>%s</div><div><h2>%s</h2>%s</div>\n'
        '<div><h2>%s</h2><a href="%s">%s</a>%s%s<a href="%s">%s</a><address class="postal">%s</address></div></div>\n'
        '<div class="copy">© <span data-year>2026</span> D3DDD – Dubai 3D Design &amp; Draft. %s</div></footer>\n'
        '%s\n<script src="%sassets/config.js" defer></script><script src="%sassets/site.js" defer></script>%s%s%s</body></html>'
    ) % (
        t["skip"], top, home_href, t["menu"], nav, sw_href, other, other, t["switch"], site_search.header_html(lang), body,
        t["tagline"], mail_link(contact_href), whatsapp_html(lang), D, social_links(lang), t["f_services"], fs, t["f_company"], fc, t["f_industries"], fi,
        t["f_contact"], contact_href, t["cta_form"], mail_link(contact_href), whatsapp_html(lang), blog_href, blog_label, loc,
        t["rights"], site_search.dialog_html(lang), P, P, scripts, site_search.script_tag(P), GOAT,
    )

def cta(lang):
    t = T[lang]
    return f'<section class="cta-band"><p class="eyebrow">{t["cta_eye"]}</p><h2>{t["cta_h"]}</h2><p>{t["cta_p"]}</p><div class="actions"><a class="btn" href="contact.html">{t["cta_form"]}</a>{mail_link("contact.html", t["cta_wa"], "btn ghost mail-link")}</div></section>'

def crumb_html(lang, name):
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="./">{T[lang]["home"]}</a> / <span>{name}</span></nav>'

def page_hero(lang, eyebrow, h1, p, name):
    return f'<section class="page-hero">{crumb_html(lang, name)}<p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p>{p}</p></section>'

# Append one dict to list another free tool on /apps/ and /ar/apps/.
APPS = [
    {
        "slug": "still",
        "title_en": "Still — Free Online Image Straightener & Photo Leveler",
        "title_ar": "Still — تقويم الصور وتسويتها مجاناً عبر الإنترنت",
        "desc_en": "Straighten and level photos in the browser. It runs on your device and nothing is uploaded.",
        "desc_ar": "قوّم الصور المائلة وسوِّ الأفق في المتصفح. يعمل على جهازك ولا يُرفع أي ملف.",
    },
]

def build_app_pages():
    pages = {}
    for lang in ("en", "ar"):
        fn = "apps/index.html"
        home = href(lang, fn, "")
        if lang == "en":
            title = "Web Apps - Useful Free Tools | D3DDD"
            desc = "Useful free browser tools from D3DDD. Straighten and level photos on your device, with nothing uploaded."
            eyebrow, h1, lead = "Free tools", "Web <em>apps.</em>", "Useful free tools that run in your browser, on your device."
            crumb, home_l, open_label = "Web Apps", "Home", "Open app →"
        else:
            title = "تطبيقات الويب - أدوات مجانية مفيدة | D3DDD"
            desc = "أدوات مجانية مفيدة من D3DDD تعمل في المتصفح على جهازك، دون رفع أي ملف."
            eyebrow, h1, lead = "أدوات مجانية", "تطبيقات <em>الويب</em>", "أدوات مجانية مفيدة تعمل في المتصفح على جهازك."
            crumb, home_l, open_label = "تطبيقات الويب", "الرئيسية", "افتح التطبيق ←"
        cards = []
        for i, app in enumerate(APPS, 1):
            name = app["title_en"] if lang == "en" else app["title_ar"]
            blurb = app["desc_en"] if lang == "en" else app["desc_ar"]
            cards.append(
                '<a class="card post-card" href="/apps/%s/"><div class="b"><span class="num">%02d</span><h2>%s</h2><p>%s</p><span class="more">%s</span></div></a>'
                % (app["slug"], i, html.escape(name), html.escape(blurb), open_label)
            )
        body = (
            '<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="%s">%s</a> / <span>%s</span></nav>'
            '<p class="eyebrow">%s</p><h1>%s</h1><p>%s</p></section>'
            '<section class="section"><div class="wrap"><div class="grid g2">%s</div></div></section>'
        ) % (home, home_l, crumb, eyebrow, h1, lead, "".join(cards))
        body += cta(lang)
        items = {"@type": "ItemList", "name": crumb, "itemListElement": [
            {"@type": "ListItem", "position": i, "name": app["title_en"] if lang == "en" else app["title_ar"], "url": url("en", "apps/%s/" % app["slug"])}
            for i, app in enumerate(APPS, 1)]}
        ld = [crumbs_ld(lang, [(home_l, url(lang, "index.html")), (crumb, url(lang, "apps/"))]), items]
        page = shell(lang, fn, title, desc, body, ld)
        pages[(lang, fn)] = page
    return pages

from content import build_pages  # page content lives in content.py
from service_pages import build_service_pages, SERVICES as SERVICE_DEFS

site_search.write_index(APPS)

globals()["prefix"] = prefix
globals()["href"] = href

out = build_pages(globals())
out.update(build_service_pages(globals()))
from landing_pages import build_landing_pages
out.update(build_landing_pages(globals()))
from directories_page import build_directory_page
out.update(build_directory_page(globals()))
from project_pages import build_project_pages, PROJECTS  # portfolio: /projects/ grid, project pages, related blocks
out.update(build_project_pages(globals(), out))
out.update(build_app_pages())

# Legacy services.html -> /services/ redirect
for lang in ("en", "ar"):
    target = url(lang, "services/")
    lang_attr = "ar-AE" if lang == "ar" else "en-AE"
    label = "الخدمات" if lang == "ar" else "Services"
    redir = (
        '<!DOCTYPE html><html lang="%s"><head><meta charset="UTF-8">'
        '<meta http-equiv="refresh" content="0;url=%s">'
        '<link rel="canonical" href="%s"><title>Services – D3DDD</title>'
        '<script>location.replace(%s)</script></head>'
        '<body><main id="main"><h1>%s</h1><p><a href="%s">%s – D3DDD</a></p></main>%s</body></html>'
    ) % (lang_attr, target, target, json.dumps(target), label, target, label, GOAT)
    out[(lang, "services.html")] = redir

# GitHub Pages has no server 301. /about and /about.html are both HTTP 200 when only
# about.html exists, because Pages serves the .html file at the extensionless path.
# A directory index at /about/ is a separate document: noindex, canonical, and a
# meta refresh of 0. On hosts that prefer the directory, /about and /about/ serve
# that stub. On hosts that still serve about.html at /about, the matching page
# runs a same-document script that sends only the extensionless path to the .html
# canonical, so /about.html itself is not noindexed and does not refresh.
EXTLESS = {
    "about.html": "/about",
    "contact.html": "/contact",
    "marble.html": "/marble",
    "website-design.html": "/website-design",
}

def extless_script(path):
    return ('<script>if(location.pathname.replace(/\\/+$/,"")==="%s")'
            'location.replace("%s.html"+location.search+location.hash);</script>' % (path, path))

def redirect_stub(target):
    return (
        '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'
        '<meta name="robots" content="noindex, follow">'
        '<meta http-equiv="refresh" content="0;url=%s">'
        '<link rel="canonical" href="%s">'
        '<title>Redirecting…</title>'
        '<script>location.replace(%s)</script></head>'
        '<body><main id="main"><p><a href="%s">Continue</a></p></main></body></html>'
    ) % (target, target, json.dumps(target), target)

for (lang, fn), html in out.items():
    if lang == "en" and fn in EXTLESS:
        html = html.replace("</head>", extless_script(EXTLESS[fn]) + "</head>", 1)
    path = ("ar/" if lang == "ar" else "") + fn
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(html)

for fn, path in EXTLESS.items():
    target = D + fn
    stub_dir = path.lstrip("/")
    os.makedirs(stub_dir, exist_ok=True)
    open(stub_dir + "/index.html", "w", encoding="utf-8").write(redirect_stub(target))

ns = {}
exec(open("portal_pages.py", encoding="utf-8").read(), ns)
for fn, (t, d, b, *rest) in ns["pages"].items():
    open(fn, "w", encoding="utf-8").write(shell("en", fn, t, d, b, (), True, False, rest[1] if len(rest) > 1 else ""))
for portal in ("login.html", "signup.html", "dashboard.html"):
    if os.path.exists(portal):
        os.remove(portal)

BILINGUAL_PAGES = [
    "index.html", "about.html", "contact.html", "marble.html", "website-design.html",
    "services/", "projects/", "apps/",
] + ["services/%s/" % s["slug"] for s in SERVICE_DEFS]

# Schema, titles and case studies in this deploy. apps/still/ is not regenerated; its lastmod is the last commit that changed it.
DEPLOY_LASTMOD = "2026-11-14"
STILL_LASTMOD = "2026-11-12"

x = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for fn in BILINGUAL_PAGES:
    for lang in ("en", "ar"):
        pr = "1.0" if fn == "index.html" else ("0.9" if fn.startswith("services") else "0.8")
        x.append(
            '  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>%s</priority>'
            '<xhtml:link rel="alternate" hreflang="en-AE" href="%s"/><xhtml:link rel="alternate" hreflang="ar-AE" href="%s"/>'
            '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/></url>'
            % (url(lang, fn), DEPLOY_LASTMOD, pr, url("en", fn), url("ar", fn), url("en", fn))
        )
x.append('  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>' % (url("en", "apps/still/"), STILL_LASTMOD))
for pr in PROJECTS:  # project pages are English only (no hreflang alternates)
    x.append('  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>' % (url("en", "projects/%s/" % pr["slug"]), DEPLOY_LASTMOD))
for fn, pr in (
    ("fitout-shop-drawings/", "0.8"),
    ("construction-companies-uae/", "0.8"),
    ("real-estate-developers-uae/", "0.8"),
    ("interior-design-companies-uae/", "0.8"),
    ("marble-contractors-uae/", "0.8"),
    ("resources/uae-directories/", "0.5"),
):
    x.append('  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>%s</priority></url>' % (url("en", fn), DEPLOY_LASTMOD, pr))
x.append("</urlset>")
open("sitemap.xml", "w", encoding="utf-8").write("\n".join(x) + "\n")
open("robots.txt", "w", encoding="utf-8").write(
    "User-agent: *\nAllow: /\nDisallow: /dashboard.html\nDisallow: /login.html\nDisallow: /signup.html\n"
    "Disallow: /thank-you.html\nDisallow: /ar/thank-you.html\nSitemap: %ssitemap.xml\n" % D
)
print("built", len(out) + len(ns["pages"]), "pages")

import runpy
runpy.run_path("scripts/build_blog.py", run_name="__main__")

def write_llms():
    """llmstxt.org page: https://d3ddd.com/llms.txt"""
    posts = []
    for path in sorted(Path_posts()):
        title, slug = "", ""
        for line in open(path, encoding="utf-8"):
            if line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("slug:"):
                slug = line.split(":", 1)[1].strip().strip('"')
            elif line.strip() == "---" and title and slug:
                break
        if title and slug:
            url_path = ("ar/blog/%s/" % slug) if "posts/ar/" in str(path).replace("\\", "/") or path.parent.name == "ar" else ("blog/%s/" % slug)
            posts.append((title, url_path))
    lines = [
        "# D3DDD - Dubai 3D Design & Draft",
        "",
        "> Marble and stone shop drawings, AutoCAD drafting, fit-out drawings, 3D rendering and contractor websites for Dubai, Abu Dhabi, Sharjah and the rest of the UAE. Founded by Shoaib Hussan. English and Arabic.",
        "",
        "D3DDD prepares fabrication and installation drawings that contractors, fabricators and consultants can review. Drawing sets are issued as AutoCAD DWG and PDF. Shop-drawing fees are quoted per project. Published website prices are the Starter (AED 1,200), Business (AED 2,000) and Premium (AED 3,500+) packages, with the 5-page contractor website at AED 2,000 and a 50% deposit. There is no street address and no phone number. The studio is in Dubai, United Arab Emirates.",
        "",
        "## Services",
        "",
        "- [Marble and stone shop drawings](https://d3ddd.com/marble.html): Fabrication drawings, cutting lists, slab layouts and BOQ for stone.",
        "- [Fit-out and joinery shop drawings](https://d3ddd.com/fitout-shop-drawings/): Joinery, ceilings, partitions, kitchens, wardrobes and interior elevations.",
        "- [Architectural drafting](https://d3ddd.com/services/architectural-drafting/): Shop drawings, CAD detailing, as-built, joinery and fit-out sets.",
        "- [Architectural designing](https://d3ddd.com/services/architectural-designing/): Concept layouts, space planning, elevations and design development.",
        "- [Architectural estimation](https://d3ddd.com/services/architectural-estimation/): BOQ, quantity take-offs, material schedules and tender packages.",
        "- [3D rendering and visualization](https://d3ddd.com/services/3d-rendering-modeling-visualization/): Still renders, modeling and walkthroughs.",
        "- [Website development](https://d3ddd.com/services/website-development-designing/): Business sites and landing pages for contractors.",
        "- [All services](https://d3ddd.com/services/): The five service lines, in English.",
        "- [الخدمات](https://d3ddd.com/ar/services/): The same services in Arabic.",
        "",
        "## Key pages",
        "",
        "- [Home](https://d3ddd.com/): English homepage.",
        "- [Arabic home](https://d3ddd.com/ar/): Arabic homepage.",
        "- [Projects](https://d3ddd.com/projects/): Marble and stone shop-drawing portfolio.",
        "- [About](https://d3ddd.com/about.html): The studio.",
        "- [Website packages](https://d3ddd.com/website-design.html): AED and CAD website prices and demo themes.",
        "- [Blog](https://d3ddd.com/blog/): Drafting and shop-drawing notes. English only.",
        "",
        "## Industries",
        "",
        "- [Construction companies](https://d3ddd.com/construction-companies-uae/): Outsourced architectural and technical drawing support for UAE contractors.",
        "- [Real estate developers](https://d3ddd.com/real-estate-developers-uae/): 3D visualization, presentation stills and design coordination.",
        "- [Interior design firms](https://d3ddd.com/interior-design-companies-uae/): Interior renders, joinery drawings and material coordination.",
        "- [Marble contractors](https://d3ddd.com/marble-contractors-uae/): Shop drawings, slab layouts, cutting lists and stone quantities.",
        "",
        "## Projects",
        "",
    ]
    for pr in PROJECTS:
        lines.append("- [%s](https://d3ddd.com/projects/%s/): %s" % (pr["title"], pr["slug"], pr.get("short", "").replace("&amp;", "&")))
    lines += ["", "## Blog", ""]
    for title, url_path in posts:
        lines.append("- [%s](https://d3ddd.com/%s)" % (title, url_path))
    lines += [
        "",
        "## Contact",
        "",
        "- Email: info@d3ddd.com",
        "- [Enquiry form](https://d3ddd.com/contact.html): Preferred way to send drawings and ask for a quote.",
        "- [Arabic enquiry form](https://d3ddd.com/ar/contact.html): The same form in Arabic.",
        "- Instagram: https://www.instagram.com/dubai3ddd/",
        "- LinkedIn: https://www.linkedin.com/in/mshoaib94",
        "- WhatsApp username (no phone number published): @mxhoaib",
        "",
        "## Founder",
        "",
        "Shoaib Hussan, founder of D3DDD – Dubai 3D Design & Draft. Draftsman working with contractors, fabricators and consultants in the UAE.",
        "",
        "## Areas served",
        "",
        "Dubai, Abu Dhabi, Sharjah, Ajman, Ras Al Khaimah, Umm Al Quwain and Fujairah, across the United Arab Emirates. Work is delivered digitally. No street address is published.",
        "",
    ]
    open("llms.txt", "w", encoding="utf-8").write("\n".join(lines))
    sm = open("sitemap.xml", encoding="utf-8").read()
    loc = D + "llms.txt"
    if loc not in sm:
        sm = sm.replace("</urlset>", '  <url><loc>%s</loc><lastmod>2026-11-14</lastmod><changefreq>monthly</changefreq><priority>0.3</priority></url>\n</urlset>' % loc)
        open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("wrote llms.txt")

def Path_posts():
    import pathlib
    root = pathlib.Path("posts")
    return list(root.glob("*.md")) + list((root / "ar").glob("*.md"))

write_llms()

# Hub + dedicated service pages. Used by build.py (the /projects/ portfolio lives in project_pages.py).
from __future__ import annotations
import json
from pathlib import Path
from longform import hub_bundle, service_bundle

SERVICES = json.loads((Path(__file__).parent / "services_data.json").read_text(encoding="utf-8"))

# English Service nodes for the pages this expansion covers. areaServed and provider
# stay on the shared helper. No numeric price except the owner-approved single still.
EN_SERVICE_SCHEMA = {
    "architectural-drafting": {
        "name": "Architectural drafting",
        "serviceType": "Architectural drafting and AutoCAD 2D construction drawings",
        "description": "Architectural drafting and AutoCAD 2D construction drawings in Dubai and the UAE: shop drawings, fit-out sets, joinery elevations and as-built CAD for contractors, issued as DWG and PDF. Quoted per project.",
        "offers": {
            "@type": "Offer",
            "name": "Architectural drafting",
            "description": "Quote on request. Scope, fee and delivery date are confirmed in writing before work starts.",
            "priceCurrency": "AED",
        },
    },
    "architectural-estimation": {
        "name": "Quantity estimation / BOQ",
        "serviceType": "Quantity take-off, bill of quantities and material schedules",
        "description": "Quantity take-off and BOQ services in the UAE: measured bills, material schedules and tender packages from your drawings, quoted per project.",
        "offers": {
            "@type": "Offer",
            "name": "Quantity estimation / BOQ",
            "description": "Quote on request. Quoted per package. Scope, fee and delivery date are confirmed in writing before work starts.",
            "priceCurrency": "AED",
        },
    },
    "3d-rendering-modeling-visualization": {
        "name": "3D rendering, modeling & visualization",
        "serviceType": "3D modeling, 3D rendering and architectural visualization",
        "description": "3D modeling and architectural visualization in Dubai: still renders, material studies, models and walkthroughs. A single still render is 650 AED (50% upfront); additional views and modeling packages are quoted per project.",
        "offers": [
            {
                "@type": "Offer",
                "name": "Single 3D render",
                "description": "One still render as agreed in the quote, PNG or JPG, 50% upfront. Additional views, modeling-only packages and walkthroughs are quoted separately.",
                "price": "650",
                "priceCurrency": "AED",
            },
            {
                "@type": "Offer",
                "name": "Additional 3D visualization",
                "description": "Quote on request for extra views, material options, 3D modeling packages, walkthroughs and related visualization work. Scope, fee and delivery date are confirmed in writing before work starts.",
                "priceCurrency": "AED",
            },
        ],
    },
    "architectural-designing": {
        "name": "Architectural designing",
        "serviceType": "Architectural concept design, space planning and design development",
        "description": "Architectural designing in Dubai and the UAE: concept layouts, space planning, elevations and design development that can move into CAD drawings. Quoted per project.",
        "offers": {
            "@type": "Offer",
            "name": "Architectural designing",
            "description": "Quote on request. Scope, fee and delivery date are confirmed in writing before work starts.",
            "priceCurrency": "AED",
        },
    },
}


def related_services(g, lang, fn, slug):
    groups = {
        "architectural-drafting": [
            ("fitout-shop-drawings/", "FIT", "Fit-out and joinery", "Ceilings, partitions, kitchens and wardrobes."),
            ("marble.html", "STONE", "Marble shop drawings", "Fabrication drawings, slab layouts and cutting lists."),
            ("services/architectural-estimation/", "BOQ", "Estimation and BOQ", "Quantities measured from the drafted sheets."),
            ("construction-companies-uae/", "SITE", "Construction companies", "Outsourced drawing support for contractors."),
            ("interior-design-companies-uae/", "INT", "Interior firms", "Joinery drawings and material coordination."),
            ("projects/villa-ground-floor-marble-flooring-layout/", "PLAN", "Villa floor layout", "A drafted ground-floor stone set-out."),
            ("projects/villa-swimming-pool-and-outdoor-majlis-tiling-details/", "POOL", "Villa swimming pool and outdoor seating tiling details", "External tiling set tagged as architectural drafting."),
        ],
        "architectural-designing": [
            ("projects/villa-ground-floor-marble-flooring-layout/", "PLAN", "Luxury villa ground floor flooring layout", "A design-stage flooring option tagged as architectural designing."),
        ],
        "architectural-estimation": [
            ("marble.html", "STONE", "Marble shop drawings", "The sheets stone quantities are measured from."),
            ("services/architectural-drafting/", "CAD", "Architectural drafting", "The wider drawing set behind a bill."),
            ("construction-companies-uae/", "SITE", "Construction companies", "Tender and shop-drawing support for contractors."),
            ("marble-contractors-uae/", "YARD", "Marble contractors", "Cutting lists, slab layouts and stone quantities."),
            ("projects/marble-slab-cutting-layout-bathroom-cladding/", "SLAB", "Bathroom slab nesting", "Numbered panels a yard can price."),
            ("projects/villa-ground-floor-marble-flooring-layout/", "PLAN", "Villa floor layout", "Areas that become a flooring schedule."),
            ("blog/marble-quantity-calculation-reduce-waste/", "QTY", "How to calculate marble quantities and reduce waste", "A take-off guide beside the estimation service."),
        ],
        "3d-rendering-modeling-visualization": [
            ("real-estate-developers-uae/", "DEV", "Real estate developers", "Presentation stills and design coordination."),
            ("interior-design-companies-uae/", "INT", "Interior firms", "Renders coordinated with joinery and stone."),
            ("services/architectural-designing/", "DES", "Architectural design", "Layouts that the images are built from."),
            ("marble.html", "STONE", "Marble shop drawings", "The measured sheets a render must not replace."),
            ("projects/entrance-lobby-waterjet-marble-medallion-flooring/", "LOBBY", "Lobby medallion", "A feature floor that reads in a presentation."),
            ("projects/luxury-bathroom-marble-cladding-shop-drawings/", "BATH", "Bathroom cladding", "Stone junctions a material study should follow."),
        ],
    }
    items = groups.get(slug)
    if not items:
        return ""
    cards = []
    for target, num, title, text in items:
        cards.append(
            '<a class="card" href="%s"><div class="b"><span class="num">%s</span><h3>%s</h3><p>%s</p></div></a>'
            % (g["href"](lang, fn, target), num, title, text)
        )
    return (
        '<section class="section" id="related"><div class="wrap"><p class="eyebrow">Related</p>'
        '<h2 class="mb-24">Continue to the matching service, industry or sheet</h2>'
        '<div class="grid g3">%s</div></div></section>' % "".join(cards)
    )


def build_service_pages(g):
    shell, img, cta = g["shell"], g["img"], g["cta"]
    crumbs_ld, service_ld, url = g["crumbs_ld"], g["service_ld"], g["url"]
    out = {}
    arrow = "\u2192"

    def service_page(lang, s):
        t = s[lang]
        fn = f"services/{s['slug']}/index.html"
        P = g["prefix"](lang, fn)
        contact = g["href"](lang, fn, "contact.html")
        marble = g["href"](lang, fn, "marble.html")
        webpkg = g["href"](lang, fn, "website-design.html")
        hub = g["href"](lang, fn, "services/")
        home = g["href"](lang, fn, "")
        subs = "".join(
            f'<div class="card"><div class="b"><h3>{a}</h3><p>{b}</p></div></div>'
            for a, b in t["subs"]
        )
        deliver = "".join(f"<li>{x}</li>" for x in t["deliver"])
        extra = ""
        if t.get("marble_link"):
            label = "Marble shop drawings " + arrow if lang == "en" else "رسومات الرخام " + arrow
            extra += f'<p class="mt-16"><a class="btn ghost" href="{marble}">{label}</a></p>'
        if t.get("web_link"):
            label = "Contractor website package " + arrow if lang == "en" else "باقة موقع المقاولين " + arrow
            extra += f'<p class="mt-16"><a class="btn ghost" href="{webpkg}">{label}</a></p>'
        if lang == "en":
            home_l, svc_l, sub_h, soft, soft_p = (
                "Home", "Services", "Sub-services", "Next step",
                "Share drawings, sketches or a short brief for a quote by email — no phone required on this site.",
            )
            contact_l = "Email D3DDD"
        else:
            home_l, svc_l, sub_h, soft, soft_p = (
                "الرئيسية", "الخدمات", "الخدمات الفرعية", "الخطوة التالية",
                "أرسل المخططات أو الرسومات الأولية أو وصفاً مختصراً لعرض سعر عبر البريد — دون رقم هاتف على هذا الموقع.",
            )
            contact_l = "راسل D3DDD"
        svc_q = {
            "architectural-drafting": "drafting",
            "3d-rendering-modeling-visualization": "3d",
            "architectural-designing": "design",
            "architectural-estimation": "estimation",
            "website-development-designing": "website",
        }.get(s["slug"], "")
        contact_q = contact + (("?service=" + svc_q) if svc_q else "")
        body = f'''<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">{home_l}</a> / <a href="{hub}">{svc_l}</a> / <span>{t["name"]}</span></nav>
<p class="eyebrow">{t["eyebrow"]}</p><h1>{t["h1"]}</h1><p>{t["lead"]}</p></section>
<section class="section"><div class="wrap split"><figure>{img(P, s["img"], t["name"], True)}</figure><div><span class="num">{s["num"]}</span><h2>{t["name"]}</h2><p>{t["intro"]}</p>
<ul class="check">{deliver}</ul>
<p class="mt-18"><a class="btn" href="{contact_q}">{t["cta_label"]} {arrow}</a></p>{extra}</div></div></section>
<section class="section alt"><div class="wrap"><p class="eyebrow">{sub_h}</p><h2 class="mb-24">{sub_h}</h2>
<div class="grid g3">{subs}</div>
<div class="notice mt-28"><strong>{soft}:</strong> {soft_p} <a href="{contact_q}">{contact_l}</a>.</div>
</div></section>'''
        guide, faqs = service_bundle(
            lang, s["slug"],
            lambda target, lang=lang, fn=fn: g["href"](lang, fn, target),
            lambda target, lang=lang, fn=fn: g["en_href"](lang, fn, target),
        )
        faq_title = "Frequently asked questions" if lang == "en" else "الأسئلة الشائعة"
        faq_eye = "FAQ" if lang == "en" else "أسئلة وأجوبة"
        body += guide + g["faq_html"](faqs, faq_title, faq_eye)
        if lang == "en":
            body += related_services(g, lang, fn, s["slug"])
        body += cta(lang).replace('href="contact.html"', f'href="{contact}"')
        page_url = url(lang, f"services/{s['slug']}/")
        schema = EN_SERVICE_SCHEMA.get(s["slug"]) if lang == "en" else None
        if schema:
            offers = schema["offers"]
            if isinstance(offers, list):
                offers = [{**offer, "url": page_url} for offer in offers]
            else:
                offers = {**offers, "url": page_url}
            svc_node = service_ld(schema["name"], schema["description"], page_url, offers=offers, service_type=schema["serviceType"])
        else:
            svc_node = service_ld(t["name"].replace("&amp;", "&"), t["desc"], page_url)
        ld = [
            crumbs_ld(lang, [(home_l, url(lang, "index.html")), (svc_l, url(lang, "services/")), (t["name"], url(lang, f"services/{s['slug']}/"))]),
            svc_node,
            g["faq_ld"](faqs),
        ]
        out[(lang, fn)] = shell(lang, fn, t["title"], t["desc"], body, ld, preload=s["img"])

    for lang in ("en", "ar"):
        fn = "services/index.html"
        P = g["prefix"](lang, fn)
        cards = []
        for s in SERVICES:
            t = s[lang]
            cards.append(
                f'<a class="card" href="{s["slug"]}/"><figure>{img(P, s["img"], t["name"])}</figure>'
                f'<div class="b"><span class="num">{s["num"]}</span><h3>{t["name"]}</h3><p>{t["short"]}</p></div></a>'
            )
        home = g["href"](lang, fn, "")
        marble = g["href"](lang, fn, "marble.html")
        webpkg = g["href"](lang, fn, "website-design.html")
        fitout = g["href"](lang, fn, "fitout-shop-drawings/")
        contractors = g["href"](lang, fn, "construction-companies-uae/")
        developers = g["href"](lang, fn, "real-estate-developers-uae/")
        interiors = g["href"](lang, fn, "interior-design-companies-uae/")
        yards = g["href"](lang, fn, "marble-contractors-uae/")
        if lang == "en":
            hero = f'''<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">Home</a> / <span>Services</span></nav>
<p class="eyebrow">Services — Dubai &amp; UAE</p>
<h1>Drafting, design, estimation, 3D and web services in the UAE</h1>
<p>Architectural drafting, designing, estimation, 3D visualization and website development — practical packages for Dubai, Abu Dhabi, Sharjah and the wider Gulf. Led by Shoaib Hussan / D3DDD. <span lang="ar" class="ar-touch">خدماتنا في الإمارات والخليج</span></p></section>'''
            contact = g["href"](lang, fn, "contact.html")
            more = f'''<section class="section alt" id="get-started"><div class="wrap"><p class="eyebrow">Clear paths to a quote</p><h2>Marble shop drawings, AutoCAD drafting &amp; shop drawing <em>approval</em></h2>
<p class="lede-top">Blog readers and project teams: pick a path, then send drawings through the enquiry form. This site does not publish a phone number.</p>
<div class="grid g3 mt-24">
<div class="card"><div class="b"><span class="num">STONE</span><h3>Marble shop drawings</h3><p>Fabrication drawings, cutting lists and BOQ.</p><div class="actions mt-12"><a class="btn" href="{contact}?service=marble">Request quote</a><a class="btn ghost" href="{marble}">Marble shop drawing details</a></div></div></div>
<div class="card"><div class="b"><span class="num">CAD</span><h3>AutoCAD drafting</h3><p>Shop drawings and fit-out CAD sets.</p><div class="actions mt-12"><a class="btn" href="{contact}?service=drafting">Request quote</a><a class="btn ghost" href="architectural-drafting/">Architectural drafting details</a></div></div></div>
<div class="card"><div class="b"><span class="num">3D</span><h3>Shop drawing approval / 3D</h3><p>Renders that support client and consultant approval.</p><div class="actions mt-12"><a class="btn" href="{contact}?service=3d">Request quote</a><a class="btn ghost" href="3d-rendering-modeling-visualization/">3D rendering details</a></div></div></div>
</div></div></section>
<section class="section"><div class="wrap"><p class="eyebrow">Specialist pages</p><h2>Also available</h2>
<div class="grid g3 mt-24">
<a class="card" href="{fitout}"><div class="b"><span class="num">FIT</span><h3>Fit-out &amp; joinery shop drawings</h3><p>Ceilings, partitions, kitchens, wardrobes and interior elevations.</p></div></a>
<a class="card" href="{marble}"><div class="b"><span class="num">STONE</span><h3>Marble &amp; stone shop drawings</h3><p>Fabrication drawings, cutting lists and BOQ for stone works.</p></div></a>
<a class="card" href="{webpkg}"><div class="b"><span class="num">WEB</span><h3>Contractor website package</h3><p>AED 2,000 · 5 pages · enquiry-focused — pricing and demos.</p></div></a>
</div></div></section>
<section class="section alt"><div class="wrap"><p class="eyebrow">Industries</p><h2>Who the drawings are for</h2>
<div class="grid g4 mt-24">
<a class="card" href="{contractors}"><div class="b"><h3>Construction companies</h3><p>Technical drafting support for UAE contractors.</p></div></a>
<a class="card" href="{developers}"><div class="b"><h3>Real estate developers</h3><p>Visualization and presentation stills.</p></div></a>
<a class="card" href="{interiors}"><div class="b"><h3>Interior design firms</h3><p>Joinery drawings and material coordination.</p></div></a>
<a class="card" href="{yards}"><div class="b"><h3>Marble contractors</h3><p>Shop drawings, slab layouts and cutting lists.</p></div></a>
</div></div></section>'''
            title = "Architectural Drafting &amp; 3D Services UAE | D3DDD"
            desc = "D3DDD services in Dubai and the UAE: architectural drafting, designing, estimation, 3D rendering and website development for Gulf contractors."
            name = "Services"
            home_l = "Home"
        else:
            hero = f'''<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">الرئيسية</a> / <span>الخدمات</span></nav>
<p class="eyebrow">الخدمات — دبي والإمارات</p>
<h1>خمس خطوط خدمة لـ<em>التصميم والرسم والويب</em> في الخليج</h1>
<p>رسم تنفيذي، تصميم معماري، حساب كميات، تصور ثلاثي الأبعاد وتطوير مواقع — باقات عملية لدبي وأبوظبي والشارقة والخليج. بإشراف شعيب حسين / D3DDD.</p></section>'''
            contact = g["href"](lang, fn, "contact.html")
            more = f'''<section class="section alt" id="get-started"><div class="wrap"><p class="eyebrow">مسارات واضحة لعرض السعر</p><h2>رسومات الرخام، مخططات أوتوكاد واعتماد الرسومات <em>التنفيذية</em></h2>
<p class="lede-top">لقراء المدونة وفرق المشاريع: اختر المسار ثم أرسل المخططات عبر نموذج الاستفسار. هذا الموقع لا ينشر رقم هاتف.</p>
<div class="grid g3 mt-24">
<div class="card"><div class="b"><span class="num">حجر</span><h3>رسومات الرخام</h3><p>رسومات تصنيع وقوائم قص وجداول كميات.</p><div class="actions mt-12"><a class="btn" href="{contact}?service=marble">اطلب عرض سعر</a><a class="btn ghost" href="../marble.html">تفاصيل رسومات الرخام</a></div></div></div>
<div class="card"><div class="b"><span class="num">أوتوكاد</span><h3>مخططات أوتوكاد</h3><p>رسومات تنفيذية ومجموعات CAD للفيت آوت.</p><div class="actions mt-12"><a class="btn" href="{contact}?service=drafting">اطلب عرض سعر</a><a class="btn ghost" href="architectural-drafting/">تفاصيل الرسم التنفيذي</a></div></div></div>
<div class="card"><div class="b"><span class="num">3D</span><h3>اعتماد الرسومات / 3D</h3><p>تصاميم تساعد على اعتماد الشكل قبل التصنيع.</p><div class="actions mt-12"><a class="btn" href="{contact}?service=3d">اطلب عرض سعر</a><a class="btn ghost" href="3d-rendering-modeling-visualization/">تفاصيل التصميم ثلاثي الأبعاد</a></div></div></div>
</div></div></section>
<section class="section"><div class="wrap"><p class="eyebrow">صفحات متخصصة</p><h2>أيضاً متاح</h2>
<div class="grid g2 mt-24">
<a class="card" href="{marble}"><div class="b"><span class="num">حجر</span><h3>رسومات الرخام والحجر</h3><p>رسومات تصنيع وقوائم قص وجداول كميات.</p></div></a>
<a class="card" href="{webpkg}"><div class="b"><span class="num">ويب</span><h3>باقة موقع المقاولين</h3><p>2,000 درهم · 5 صفحات — الأسعار والنماذج.</p></div></a>
</div></div></section>'''
            title = "الخدمات | رسم تنفيذي، تصميم، كميات، 3D ومواقع في الإمارات – D3DDD"
            desc = "خدمات D3DDD في دبي والإمارات: رسم معماري تنفيذي، تصميم، حساب كميات، تصميم ثلاثي الأبعاد وتطوير مواقع."
            name = "الخدمات"
            home_l = "الرئيسية"
        body = hero + f'<section class="section"><div class="wrap"><div class="grid g3">{"".join(cards)}</div></div></section>' + more
        guide, faqs = hub_bundle(
            lang,
            lambda target, lang=lang, fn=fn: g["href"](lang, fn, target),
            lambda target, lang=lang, fn=fn: g["en_href"](lang, fn, target),
        )
        faq_title = "Frequently asked questions" if lang == "en" else "الأسئلة الشائعة"
        faq_eye = "FAQ" if lang == "en" else "أسئلة وأجوبة"
        body += guide + g["faq_html"](faqs, faq_title, faq_eye)
        body += cta(lang).replace('href="contact.html"', f'href="{g["href"](lang, fn, "contact.html")}"')
        ld_services = [
            service_ld(s[lang]["name"].replace("&amp;", "&"), s[lang]["desc"], url(lang, f"services/{s['slug']}/"))
            for s in SERVICES
        ]
        ld = [crumbs_ld(lang, [(home_l, url(lang, "index.html")), (name, url(lang, "services/"))]), g["faq_ld"](faqs)] + ld_services
        out[(lang, fn)] = shell(lang, fn, title, desc, body, ld)

        for s in SERVICES:
            service_page(lang, s)

        # /projects/ (grid + project pages) is generated by project_pages.py

    return out

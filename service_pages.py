# Hub + dedicated service pages + portfolio placeholder. Used by build.py.
from __future__ import annotations
import json
from pathlib import Path

SERVICES = json.loads((Path(__file__).parent / "services_data.json").read_text(encoding="utf-8"))


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
            extra += f'<p style="margin-top:16px"><a class="btn ghost" href="{marble}">{label}</a></p>'
        if t.get("web_link"):
            label = "Contractor website package " + arrow if lang == "en" else "باقة موقع المقاولين " + arrow
            extra += f'<p style="margin-top:16px"><a class="btn ghost" href="{webpkg}">{label}</a></p>'
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
<p style="margin-top:18px"><a class="btn" href="{contact_q}">{t["cta_label"]} {arrow}</a></p>{extra}</div></div></section>
<section class="section alt"><div class="wrap"><p class="eyebrow">{sub_h}</p><h2 style="margin-bottom:24px">{sub_h}</h2>
<div class="grid g3">{subs}</div>
<div class="notice" style="margin-top:28px"><strong>{soft}:</strong> {soft_p} <a href="{contact_q}">{contact_l}</a>.</div>
</div></section>'''
        body += cta(lang).replace('href="contact.html"', f'href="{contact}"')
        ld = [
            crumbs_ld(lang, [(home_l, url(lang, "index.html")), (svc_l, url(lang, "services/")), (t["name"], url(lang, f"services/{s['slug']}/"))]),
            service_ld(t["name"].replace("&amp;", "&"), t["desc"], url(lang, f"services/{s['slug']}/")),
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
        if lang == "en":
            hero = f'''<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">Home</a> / <span>Services</span></nav>
<p class="eyebrow">Services — Dubai &amp; UAE</p>
<h1>Five service lines for Gulf <em>design, drafting &amp; web</em></h1>
<p>Architectural drafting, designing, estimation, 3D visualization and website development — practical packages for Dubai, Abu Dhabi, Sharjah and the wider Gulf. Led by Shoaib Hussan / D3DDD. <span lang="ar" class="ar-touch">خدماتنا في الإمارات والخليج</span></p></section>'''
            contact = g["href"](lang, fn, "contact.html")
            more = f'''<section class="section alt" id="get-started"><div class="wrap"><p class="eyebrow">Clear paths to a quote</p><h2>Marble shop drawings, AutoCAD drafting &amp; shop drawing <em>approval</em></h2>
<p style="color:var(--muted);max-width:720px;margin-top:10px">Blog readers and project teams: pick a path, then email drawings for a quote — site contact is email only.</p>
<div class="grid g3" style="margin-top:24px">
<div class="card"><div class="b"><span class="num">STONE</span><h3>Marble shop drawings</h3><p>Fabrication drawings, cutting lists and BOQ.</p><div class="actions" style="margin-top:12px"><a class="btn" href="{contact}?service=marble">Request quote</a><a class="btn ghost" href="{marble}">Details</a></div></div></div>
<div class="card"><div class="b"><span class="num">CAD</span><h3>AutoCAD drafting</h3><p>Shop drawings and fit-out CAD sets.</p><div class="actions" style="margin-top:12px"><a class="btn" href="{contact}?service=drafting">Request quote</a><a class="btn ghost" href="architectural-drafting/">Details</a></div></div></div>
<div class="card"><div class="b"><span class="num">3D</span><h3>Shop drawing approval / 3D</h3><p>Renders that support client and consultant approval.</p><div class="actions" style="margin-top:12px"><a class="btn" href="{contact}?service=3d">Request quote</a><a class="btn ghost" href="3d-rendering-modeling-visualization/">Details</a></div></div></div>
</div></div></section>
<section class="section"><div class="wrap"><p class="eyebrow">Specialist pages</p><h2>Also available</h2>
<div class="grid g2" style="margin-top:24px">
<a class="card" href="{marble}"><div class="b"><span class="num">STONE</span><h3>Marble &amp; stone shop drawings</h3><p>Fabrication drawings, cutting lists and BOQ for stone works.</p></div></a>
<a class="card" href="{webpkg}"><div class="b"><span class="num">WEB</span><h3>Contractor website package</h3><p>AED 2,000 · 5 pages · enquiry-focused — pricing and demos.</p></div></a>
</div></div></section>'''
            title = "Services | Architectural Drafting, Design, Estimation, 3D & Web UAE – D3DDD"
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
<p style="color:var(--muted);max-width:720px;margin-top:10px">لقراء المدونة وفرق المشاريع: اختر المسار ثم أرسل المخططات بالبريد — التواصل عبر البريد فقط.</p>
<div class="grid g3" style="margin-top:24px">
<div class="card"><div class="b"><span class="num">حجر</span><h3>رسومات الرخام</h3><p>رسومات تصنيع وقوائم قص وجداول كميات.</p><div class="actions" style="margin-top:12px"><a class="btn" href="{contact}?service=marble">اطلب عرض سعر</a><a class="btn ghost" href="../marble.html">التفاصيل</a></div></div></div>
<div class="card"><div class="b"><span class="num">أوتوكاد</span><h3>مخططات أوتوكاد</h3><p>رسومات تنفيذية ومجموعات CAD للفيت آوت.</p><div class="actions" style="margin-top:12px"><a class="btn" href="{contact}?service=drafting">اطلب عرض سعر</a><a class="btn ghost" href="architectural-drafting/">التفاصيل</a></div></div></div>
<div class="card"><div class="b"><span class="num">3D</span><h3>اعتماد الرسومات / 3D</h3><p>تصاميم تساعد على اعتماد الشكل قبل التصنيع.</p><div class="actions" style="margin-top:12px"><a class="btn" href="{contact}?service=3d">اطلب عرض سعر</a><a class="btn ghost" href="3d-rendering-modeling-visualization/">التفاصيل</a></div></div></div>
</div></div></section>
<section class="section"><div class="wrap"><p class="eyebrow">صفحات متخصصة</p><h2>أيضاً متاح</h2>
<div class="grid g2" style="margin-top:24px">
<a class="card" href="{marble}"><div class="b"><span class="num">حجر</span><h3>رسومات الرخام والحجر</h3><p>رسومات تصنيع وقوائم قص وجداول كميات.</p></div></a>
<a class="card" href="{webpkg}"><div class="b"><span class="num">ويب</span><h3>باقة موقع المقاولين</h3><p>2,000 درهم · 5 صفحات — الأسعار والنماذج.</p></div></a>
</div></div></section>'''
            title = "الخدمات | رسم تنفيذي، تصميم، كميات، 3D ومواقع في الإمارات – D3DDD"
            desc = "خدمات D3DDD في دبي والإمارات: رسم معماري تنفيذي، تصميم، حساب كميات، تصميم ثلاثي الأبعاد وتطوير مواقع."
            name = "الخدمات"
            home_l = "الرئيسية"
        body = hero + f'<section class="section"><div class="wrap"><div class="grid g3">{"".join(cards)}</div></div></section>' + more
        body += cta(lang).replace('href="contact.html"', f'href="{g["href"](lang, fn, "contact.html")}"')
        ld_services = [
            service_ld(s[lang]["name"].replace("&amp;", "&"), s[lang]["desc"], url(lang, f"services/{s['slug']}/"))
            for s in SERVICES
        ]
        ld = [crumbs_ld(lang, [(home_l, url(lang, "index.html")), (name, url(lang, "services/"))])] + ld_services
        out[(lang, fn)] = shell(lang, fn, title, desc, body, ld)

        for s in SERVICES:
            service_page(lang, s)

        # projects placeholder
        fn = "projects/index.html"
        P = g["prefix"](lang, fn)
        contact = g["href"](lang, fn, "contact.html")
        home = g["href"](lang, fn, "")
        services_href = g["href"](lang, fn, "services/")
        if lang == "en":
            title = "Projects & Portfolio | Coming Soon – D3DDD Dubai"
            desc = "D3DDD project portfolio placeholder — structure ready for real UAE and Gulf project uploads. No invented case studies."
            body = f'''<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">Home</a> / <span>Projects</span></nav>
<p class="eyebrow">Portfolio — ready for uploads</p>
<h1>Projects &amp; portfolio <em>coming soon</em></h1>
<p>This page is structured for real project case studies from Shoaib Hussan / D3DDD. We do not invent client names, photos or results. When the owner uploads approved projects, they will appear here.</p></section>
<section class="section"><div class="wrap split"><figure>{img(P, "svc-projects", "Empty portfolio frames ready for project uploads", True)}</figure>
<div><h2>How projects will be listed</h2>
<p>Each future project entry is expected to include:</p>
<ul class="check">
<li>Project title and location (city / emirate)</li>
<li>Service line (drafting, design, estimation, 3D or web)</li>
<li>Short scope note (what was delivered)</li>
<li>Owner-approved images or drawings only</li>
<li>Optional link back to the relevant <a href="{services_href}">service page</a></li>
</ul>
<p class="notice" style="margin-top:20px">See <code>PROJECTS.md</code> in the repository for the upload checklist. Until then, this page stays an honest placeholder — not a gallery of fictional work.</p>
<p style="margin-top:18px"><a class="btn" href="{contact}">Send an enquiry</a>
<a class="btn ghost" href="{services_href}" style="margin-inline-start:8px">Browse services</a></p>
</div></div></section>'''
            home_l, proj_l = "Home", "Projects"
        else:
            title = "المشاريع والمحفظة | قريباً – D3DDD دبي"
            desc = "صفحة محفظة مشاريع D3DDD جاهزة لرفع مشاريع حقيقية في الإمارات والخليج — دون دراسات حالة مخترعة."
            body = f'''<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">الرئيسية</a> / <span>المشاريع</span></nav>
<p class="eyebrow">المحفظة — جاهزة للرفع</p>
<h1>المشاريع والمحفظة <em>قريباً</em></h1>
<p>هذه الصفحة مهيأة لدراسات مشاريع حقيقية من شعيب حسين / D3DDD. لا نخترع أسماء عملاء أو صوراً أو نتائج. عند رفع المالك لمشاريع معتمدة ستظهر هنا.</p></section>
<section class="section"><div class="wrap split"><figure>{img(P, "svc-projects", "إطارات محفظة فارغة جاهزة لرفع المشاريع", True)}</figure>
<div><h2>كيف ستُعرض المشاريع</h2>
<ul class="check">
<li>عنوان المشروع والموقع (مدينة / إمارة)</li>
<li>خط الخدمة (رسم، تصميم، كميات، 3D أو ويب)</li>
<li>ملاحظة نطاق مختصرة</li>
<li>صور أو مخططات معتمدة من المالك فقط</li>
<li>رابط اختياري لصفحة الخدمة ذات الصلة</li>
</ul>
<p class="notice" style="margin-top:20px">راجع ملف <code>PROJECTS.md</code> في المستودع. حتى ذلك الحين تبقى هذه الصفحة مكاناً صادقاً — وليست معرضاً لأعمال وهمية.</p>
<p style="margin-top:18px"><a class="btn" href="{contact}">أرسل استفساراً</a></p>
</div></div></section>'''
            home_l, proj_l = "الرئيسية", "المشاريع"
        body += cta(lang).replace('href="contact.html"', f'href="{contact}"')
        ld = [crumbs_ld(lang, [(home_l, url(lang, "index.html")), (proj_l, url(lang, "projects/"))])]
        out[(lang, fn)] = shell(lang, fn, title, desc, body, ld, preload="svc-projects")

    return out

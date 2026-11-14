# Portfolio: /projects/ grid (EN + AR), English project pages with a zoomable gallery,
# and "Related projects" blocks on the matching service pages. Used by build.py.
# Source copy: projects_src/<slug>.md (owner-approved page.md) + projects_src/projects.json (order, card text, service).
# Images: assets/img/projects/<slug>/ (web-optimised, one copy each).
from __future__ import annotations
import html, json, re
from pathlib import Path
import markdown
from PIL import Image  # only used to read image sizes for width/height attributes

ROOT = Path(__file__).parent
SRC = ROOT / "projects_src"
IMG_DIR = "assets/img/projects"

# service key -> (EN page fn, label, contact ?service= value)
SERVICE_PAGES = {
    "marble": ("marble.html", "Marble &amp; stone shop drawings", "marble"),
    "architectural-drafting": ("services/architectural-drafting/index.html", "Architectural drafting", "drafting"),
    "architectural-designing": ("services/architectural-designing/index.html", "Architectural designing", "design"),
    "architectural-estimation": ("services/architectural-estimation/index.html", "Architectural estimation", "estimation"),
    "3d-rendering-modeling-visualization": ("services/3d-rendering-modeling-visualization/index.html", "3D rendering &amp; visualization", "3d"),
}
def project_body_html(main: str) -> str:
    """Render the case-study body. Gallery images stay in the template. Owner-confirm gaps are omitted."""
    kept = []
    for line in main.splitlines():
        if line.startswith("# ") or line.startswith("!["):
            continue
        if line.strip() == "*By Shoaib Hussan, Founder of D3DDD*":
            continue
        if line.startswith("**Software:**"):
            continue
        kept.append(line)
    text = "\n".join(kept)
    text = re.sub(r"[^.!?\n]*\[OWNER TO CONFIRM\][^.!?\n]*[.!?]?", "", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    rendered = markdown.markdown(text, extensions=["extra", "sane_lists"])
    if "OWNER TO CONFIRM" in rendered:
        raise SystemExit("OWNER TO CONFIRM leaked into a project page")
    return rendered


def parse_page_md(text: str) -> dict:
    _, fm, body = text.split("---\n", 2)
    meta, key = {}, None
    for line in fm.splitlines():
        if line.startswith("  - ") and key:
            meta.setdefault(key, []).append(line[4:].strip())
        elif ":" in line:
            key, val = line.split(":", 1)
            key, val = key.strip(), val.strip()
            meta[key] = json.loads(val) if val.startswith('"') else (val or [])
    main, _, cta = body.partition("\n---\n")
    paras = []
    for block in re.split(r"\n\s*\n", main.strip()):
        b = block.strip()
        if not b or b.startswith("# ") or b.startswith("![") or (b.startswith("*") and not b.startswith("**")):
            continue
        if b.startswith("**Software:**"):
            continue
        paras.append(b)
    meta["paragraphs"] = paras
    meta["body_html"] = project_body_html(main)
    m = re.search(r"\*\*(.+?)\*\*\s*(.*?)\s*at \[", cta, re.S)
    meta["cta_h"], meta["cta_p"] = (m.group(1).strip(), m.group(2).strip()) if m else ("Need drawings like these?", "Send your design drawings and get a quote.")
    return meta


def load_projects() -> list[dict]:
    out = []
    for i, entry in enumerate(json.loads((SRC / "projects.json").read_text(encoding="utf-8"))):
        p = parse_page_md((SRC / (entry["slug"] + ".md")).read_text(encoding="utf-8"))
        assert p["slug"] == entry["slug"], entry["slug"]
        p.update(entry)
        p["num"] = "%02d" % (i + 1)
        sizes = {}
        for f in [p["thumbnail"]] + p["images"]:
            with Image.open(ROOT / IMG_DIR / p["slug"] / f) as im:
                sizes[f] = im.size
        p["sizes"] = sizes
        out.append(p)
    return out


PROJECTS = load_projects()


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def md_inline(s: str) -> str:
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?m)^(Deliverables:)", r"<strong>\1</strong>", s)
    return s


def card(p: dict, P: str, lang: str = "en", heading: str = "h3") -> str:
    thumb = p["thumbnail"]; w, h = p["sizes"][thumb]
    link = f'{P}projects/{p["slug"]}/'
    attrs = ' lang="en" dir="ltr"' if lang == "ar" else ""
    more = "View project &rarr;" if lang == "en" else "عرض المشروع (بالإنجليزية) &larr;"
    return (f'<a class="pj-card" href="{link}"><figure><img src="{P}{IMG_DIR}/{p["slug"]}/{thumb}" '
            f'alt="{esc(p["title"])} – thumbnail" width="{w}" height="{h}" loading="lazy" decoding="async"></figure>'
            f'<div class="pj-card-b"><span class="num">{p["num"]} · {p["category"]}</span>'
            f'<{heading}{attrs}>{esc(p["title"])}</{heading}><p{attrs}>{esc(p["short"])}</p><span class="pj-more">{more}</span></div></a>')


def build_project_pages(g, out: dict) -> dict:
    shell, crumbs_ld, url, href, D = g["shell"], g["crumbs_ld"], g["url"], g["href"], g["D"]
    pages = {}
    css = lambda P: f'<link rel="stylesheet" href="{P}assets/projects.css">'
    gal_js = lambda P: f'<script src="{P}assets/gallery.js" defer></script>'

    # ---------------------------------------------------------------- /projects/ grid (EN + AR)
    for lang in ("en", "ar"):
        fn = "projects/index.html"
        P = g["prefix"](lang, fn)
        home, contact = href(lang, fn, ""), href(lang, fn, "contact.html")
        cards = "".join(card(p, P, lang, "h2") for p in PROJECTS)
        if lang == "en":
            title = "Projects &amp; Portfolio | Marble Shop Drawings Dubai – D3DDD"
            desc = "Selected D3DDD marble shop drawings in Dubai: waterjet medallions, villa flooring, bathroom cladding, vanities, slab cutting plans and pool tiling."
            hero = (f'<section class="page-hero pj-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">Home</a> / <span>Projects</span></nav>'
                    f'<p class="eyebrow">Portfolio — Dubai &amp; UAE</p><h1>Marble shop drawings and stone projects in Dubai</h1></section>'
                    f'<section class="section"><div class="wrap copy">'
                    f'<p>This portfolio shows selected marble and stone shop drawings, slab layouts and tiling details prepared by Shoaib Hussan / D3DDD for villas and residences in Dubai. The set includes waterjet medallion and flooring layouts, bathroom cladding, vanity fabrication drawings, slab-by-slab cutting plans, door-frame and skirting nesting, and external pool and terrace tiling.</p>'
                    f'<p>Each project page explains the scope, the drawings delivered and the software used. Client details have been removed from every sheet.</p>'
                    f'<p>These sheets are typical of the <a href="{href(lang, fn, "marble.html")}">marble and stone shop drawings</a> D3DDD prepares for contractors, fabricators and designers in Dubai and the UAE: plans, elevations, sections, edge profiles, piece numbers and cutting layouts that can be reviewed before stone is cut. Two of the projects are tagged on their own pages as <a href="{href(lang, fn, "services/architectural-designing/")}">architectural designing</a> (the ground-floor flooring layout) and <a href="{href(lang, fn, "services/architectural-drafting/")}">architectural drafting</a> (the pool and outdoor tiling set), rather than as marble shop drawings.</p>'
                    f'<p>If you have a villa or interior stone package that needs a similar set, <a href="{contact}">request a quote</a>.</p>'
                    f'</div></section>')
            home_l, proj_l = "Home", "Projects"
        else:
            title = "المشاريع والمحفظة | رسومات الرخام التنفيذية دبي – D3DDD"
            desc = "مشاريع مختارة من D3DDD في دبي: ميداليات رخام بالقص المائي، مخططات أرضيات فلل، رسومات مغاسل وتكسيات حمامات، مخططات قص الألواح وتفاصيل تبليط المسابح."
            hero = (f'<section class="page-hero pj-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">الرئيسية</a> / <span>المشاريع</span></nav>'
                    f'<p class="eyebrow">المحفظة — دبي والإمارات</p><h1>مشاريع <em>مختارة</em></h1>'
                    f'<p>رسومات تنفيذية للرخام والحجر وتوزيع الألواح وتفاصيل التبليط من إعداد شعيب حسين / D3DDD لفلل ومساكن في دبي. '
                    f'أُزيلت بيانات العملاء من جميع اللوحات. صفحات المشاريع التفصيلية متاحة حالياً باللغة الإنجليزية.</p></section>')
            home_l, proj_l = "الرئيسية", "المشاريع"
        body = hero + f'<section class="section"><div class="wrap"><div class="pj-grid">{cards}</div></div></section>'
        body += g["cta"](lang).replace('href="contact.html"', f'href="{contact}"')
        items = {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": url("en", f"projects/{p['slug']}/"), "name": p["title"]} for i, p in enumerate(PROJECTS)]}
        ld = [crumbs_ld(lang, [(home_l, url(lang, "index.html")), (proj_l, url(lang, "projects/"))]), items]
        # explicit switcher target: the default relative "ar/projects/" breaks on nested pages
        switch = "../ar/projects/" if lang == "en" else "../../projects/"
        pages[(lang, fn)] = shell(lang, fn, title, desc, body, ld, extra_head=css(P), switch=switch)

    # ---------------------------------------------------------------- project pages (EN)
    for i, p in enumerate(PROJECTS):
        lang, fn = "en", f"projects/{p['slug']}/index.html"
        P = g["prefix"](lang, fn)
        svc_fn, svc_label, svc_q = SERVICE_PAGES[p["service"]]
        svc_href = href(lang, fn, svc_fn[:-len("index.html")] if svc_fn.endswith("/index.html") else svc_fn)
        contact = href(lang, fn, "contact.html") + "?service=" + svc_q
        home, projects = href(lang, fn, ""), href(lang, fn, "projects/")
        t = esc(p["title"])
        paras = p["body_html"]
        shots = []
        for n, f in enumerate(p["images"]):
            w, h = p["sizes"][f]
            src = f'{P}{IMG_DIR}/{p["slug"]}/{f}'
            alt = f'{p["title"]} – drawing {n + 1}'
            shots.append(f'<a class="pj-shot" href="{src}" data-caption="{esc(alt)}"><img src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"><span class="pj-zoom" aria-hidden="true">+</span></a>')
        others = [PROJECTS[(i + k) % len(PROJECTS)] for k in (1, 2, 3)]
        more = "".join(card(o, P) for o in others)
        body = f'''<section class="page-hero pj-hero"><nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">Home</a> / <a href="{projects}">Projects</a> / <span>{t}</span></nav>
<p class="eyebrow">{p["num"]} · {p["category"]} · Dubai</p><h1 class="pj-title">{t}</h1><p>{esc(p["short"])}</p>
<p class="pj-by">By Shoaib Hussan, Founder of D3DDD</p></section>
<section class="section"><div class="wrap pj-body"><div class="pj-text">{paras}</div>
<aside class="pj-meta" aria-label="Project details"><dl><div><dt>Service</dt><dd><a href="{svc_href}">{svc_label}</a></dd></div><div><dt>Location</dt><dd>Dubai, UAE</dd></div>
<div><dt>Software</dt><dd>{esc(p["software"])}</dd></div><div><dt>Drawings shown</dt><dd>{len(p["images"])} sheets</dd></div></dl>
<a class="btn" href="{contact}">Request a quote &rarr;</a></aside></div></section>
<section class="section alt" aria-labelledby="gal-h"><div class="wrap"><p class="eyebrow">Gallery</p><h2 id="gal-h">The <em>drawings</em></h2>
<p class="pj-hint">Select a drawing to open it full screen. Scroll, pinch or double-tap to zoom; swipe or use the arrow keys to move between sheets.</p>
<div class="pj-gallery" data-gallery>{"".join(shots)}</div></div></section>
<section class="cta-band"><p class="eyebrow">Let’s work together</p><h2>{esc(p["cta_h"])}</h2><p>{esc(p["cta_p"])}</p>
<div class="actions"><a class="btn" href="{contact}">Send your drawings &rarr;</a><a class="btn ghost" href="{projects}">All projects</a></div></section>
<section class="section"><div class="wrap"><p class="eyebrow">Portfolio</p><h2 class="mb-28">More <em>projects</em></h2><div class="pj-grid pj-sm">{more}</div></div></section>'''
        first = p["images"][0]; fw, fh = p["sizes"][first]
        og = (f'{D}{IMG_DIR}/{p["slug"]}/{first}', fw, fh, esc(p["title"]) + " – shop drawing")
        ld = [crumbs_ld(lang, [("Home", url(lang, "index.html")), ("Projects", url(lang, "projects/")), (p["title"], url(lang, f"projects/{p['slug']}/"))]),
              {"@type": "CreativeWork", "name": p["title"], "description": p["meta_description"], "url": url(lang, f"projects/{p['slug']}/"),
               "image": [f'{D}{IMG_DIR}/{p["slug"]}/{f}' for f in p["images"]], "creator": {"@type": "Person", "name": "Shoaib Hussan"},
               "publisher": {"@id": D + "#business"}, "locationCreated": {"@type": "Place", "name": "Dubai, United Arab Emirates"}}]
        seo = esc(p["seo_title"]) if p.get("seo_title") else t + " | D3DDD"
        page = shell(lang, fn, seo, esc(p["meta_description"]), body, ld, bilingual=False,
                     scripts=gal_js(P), og_image=og, extra_head=css(P), switch=P + "ar/projects/")
        pages[(lang, fn)] = page

    # ---------------------------------------------------------------- related projects on service pages (EN)
    for key, (svc_fn, _, _) in SERVICE_PAGES.items():
        rel = [p for p in PROJECTS if p["service"] == key]
        if not rel or ("en", svc_fn) not in out:
            continue
        P = g["prefix"]("en", svc_fn)
        block = (f'<section class="section pj-related" aria-labelledby="rel-h"><div class="wrap"><p class="eyebrow">Portfolio</p>'
                 f'<h2 class="mb-28" id="rel-h">Related <em>projects</em></h2><div class="pj-grid pj-sm">{"".join(card(p, P) for p in rel)}</div>'
                 f'<p class="mt-28"><a class="btn ghost" href="{P}projects/">All projects &rarr;</a></p></div></section>')
        page = out[("en", svc_fn)]
        assert page.count('<section class="cta-band">') == 1, svc_fn
        page = page.replace('<section class="cta-band">', block + '<section class="cta-band">')
        out[("en", svc_fn)] = page.replace("</head>", css(P) + "</head>", 1)
    return pages

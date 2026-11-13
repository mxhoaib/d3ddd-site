# Static site search index and the shared header control.
# Built by build.py from pages, services, projects, posts and web apps.
import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "assets" / "search-index.json"
JS_PATH = ROOT / "assets" / "js" / "site-search.js"

COPY = {
    "en": {
        "label": "Search",
        "placeholder": "Search services, pages, and articles…",
        "close": "Close",
    },
    "ar": {
        "label": "بحث",
        "placeholder": "ابحث في الخدمات والصفحات والمقالات…",
        "close": "إغلاق",
    },
}

ICON = (
    '<svg class="search-ico" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">'
    '<circle cx="10.5" cy="10.5" r="5.25" fill="none" stroke="currentColor" stroke-width="1.5"/>'
    '<path d="M10.5 3.2v2.1M10.5 15.7v2.1M3.2 10.5h2.1M15.7 10.5h2.1M14.6 14.6l3.4 3.4" '
    'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'
    "</svg>"
)

_sha_cache = {}


def _sha(path):
    key = str(path)
    if key not in _sha_cache:
        _sha_cache[key] = hashlib.sha1(Path(path).read_bytes()).hexdigest()[:10]
    return _sha_cache[key]


def _plain(text):
    text = html.unescape(text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _clip(text, limit=170):
    text = _plain(text)
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0].rstrip(".,;:—-")
    return (cut or text[:limit].rstrip()) + "…"


def _path(fn, lang):
    path = fn
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    elif path == "index.html":
        path = ""
    base = "/ar/" if lang == "ar" else "/"
    if not path:
        return "/ar/" if lang == "ar" else "/"
    return base + path


def header_html(lang):
    c = COPY[lang]
    label = html.escape(c["label"], quote=True)
    return (
        '<div class="site-search">'
        '<button type="button" class="search-trigger" aria-expanded="false" aria-controls="site-search-dialog" '
        'aria-haspopup="dialog" aria-label="%s">%s<span class="search-word">%s</span></button></div>'
        % (label, ICON, label)
    )


def dialog_html(lang):
    c = COPY[lang]
    label = html.escape(c["label"], quote=True)
    placeholder = html.escape(c["placeholder"], quote=True)
    close = html.escape(c["close"], quote=True)
    rev = _sha(INDEX_PATH)
    return (
        '<div class="search-overlay" id="site-search-dialog" hidden role="dialog" aria-modal="true" '
        'aria-label="%s" data-index="/assets/search-index.json?v=%s">'
        '<form class="search-panel" role="search" action="#" method="get">'
        '<div class="search-field">%s'
        '<input id="site-search-input" type="text" role="combobox" aria-autocomplete="list" aria-expanded="false" '
        'aria-controls="site-search-list" aria-label="%s" placeholder="%s" autocomplete="off" autocorrect="off" '
        'autocapitalize="off" spellcheck="false" enterkeyhint="search">'
        '<kbd class="search-hint" aria-hidden="true">/</kbd>'
        '<button type="button" class="search-close">%s</button></div>'
        '<p class="search-status" role="status"></p>'
        '<div class="search-list" id="site-search-list" role="listbox" aria-label="%s"></div>'
        "</form></div>"
        % (label, rev, ICON, label, placeholder, close, label)
    )


def script_tag(prefix):
    return '<script src="%sassets/js/site-search.js?v=%s" defer></script>' % (prefix, _sha(JS_PATH))


def _add(items, seen, lang, url, kind, title, snippet, keywords):
    title = _plain(title)
    title = re.sub(r"\s+[|–—-]\s+D3DDD\b.*$", "", title).strip()
    if not title or not url:
        return
    key = (lang, url)
    if key in seen:
        return
    seen.add(key)
    items.append({
        "title": title,
        "snippet": _clip(snippet),
        "url": url,
        "type": kind,
        "lang": lang,
        "keywords": _plain(keywords),
    })


def _front_matter(path):
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return {}
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}
    data = {}
    for line in parts[1].splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip().strip('"').strip("'")
    return data


def _posts(lang):
    folder = ROOT / "posts" / "ar" if lang == "ar" else ROOT / "posts"
    found = []
    if not folder.is_dir():
        return found
    for path in sorted(folder.glob("*.md")):
        meta = _front_matter(path)
        if meta.get("status", "").upper() == "DRAFT":
            continue
        slug = meta.get("slug") or path.stem
        title = meta.get("title")
        if not title or not slug:
            continue
        desc = meta.get("description") or meta.get("meta_description") or ""
        keys = " ".join(
            piece for piece in (
                meta.get("category_title"),
                meta.get("category"),
                meta.get("keywords"),
                meta.get("primary_keyword"),
            ) if piece
        )
        url = ("/ar/blog/%s/" % slug) if lang == "ar" else ("/blog/%s/" % slug)
        found.append((url, title, desc, keys))
    return found


def write_index(apps):
    """Write assets/search-index.json. apps is build.APPS."""
    import json as _json
    from project_pages import PROJECTS

    services = _json.loads((ROOT / "services_data.json").read_text(encoding="utf-8"))
    from landing_pages import _DATA as landing

    items = []
    seen = set()

    core = [
        ("en", "/", "page", "Home",
         "Architectural drafting, marble shop drawings, fit-out detailing, estimation and 3D visualization across Dubai and the UAE.",
         "home drafting"),
        ("ar", "/ar/", "page", "الرئيسية",
         "رسومات تنفيذية للرخام والحجر ومخططات معمارية وتصميم ثلاثي الأبعاد وحساب كميات في دبي والإمارات.",
         "الرئيسية"),
        ("en", "/services/", "service", "Services",
         "Architectural drafting, designing, estimation, 3D visualization and website development for Gulf contractors.",
         "services"),
        ("ar", "/ar/services/", "service", "الخدمات",
         "رسم معماري تنفيذي، تصميم، حساب كميات، تصميم ثلاثي الأبعاد وتطوير مواقع.",
         "الخدمات"),
        ("en", "/projects/", "page", "Projects",
         "Selected marble and stone shop drawings, slab layouts and tiling details from Dubai villas.",
         "portfolio projects"),
        ("ar", "/ar/projects/", "page", "المشاريع",
         "مشاريع مختارة لرسومات الرخام التنفيذية وتوزيع الألواح وتفاصيل التبليط.",
         "المشاريع"),
        ("en", "/marble.html", "service", "Marble shop drawings",
         "Fabrication plans, slab layouts, cutting lists and stone quantities for UAE yards, issued as DWG and PDF.",
         "marble shop drawings stone fabrication cutting list"),
        ("ar", "/ar/marble.html", "service", "رسومات الرخام التنفيذية",
         "رسومات تصنيع وقوائم قص وتوزيع ألواح وجداول كميات للرخام والحجر في دبي والإمارات.",
         "رسومات الرخام shop drawings"),
        ("en", "/website-design.html", "service", "Website design",
         "Contractor websites for the UAE: 5 pages, an enquiry form and SEO basics.",
         "website web design contractor"),
        ("ar", "/ar/website-design.html", "service", "تصميم المواقع",
         "تصميم مواقع للمقاولين: 5 صفحات ونموذج استفسار وأساسيات SEO.",
         "موقع ويب"),
        ("en", "/about.html", "page", "About",
         "D3DDD is a Dubai studio for marble shop drawings, AutoCAD drafting and 3D rendering.",
         "about studio"),
        ("ar", "/ar/about.html", "page", "من نحن",
         "استوديو رسم هندسي وتصميم في دبي لرسومات الرخام التنفيذية ومخططات أوتوكاد والتصميم ثلاثي الأبعاد.",
         "من نحن"),
        ("en", "/contact.html", "page", "Contact",
         "Request a quote for shop drawings, drafting, estimation, 3D rendering or a contractor website.",
         "contact quote enquiry"),
        ("ar", "/ar/contact.html", "page", "تواصل معنا",
         "اطلب عرض سعر للرسومات التنفيذية أو التصميم ثلاثي الأبعاد أو موقع للمقاولين.",
         "تواصل استفسار"),
        ("en", "/blog/", "blog", "Blog",
         "Articles on marble shop drawings, drafting practice, estimation and visualization.",
         "blog articles"),
        ("ar", "/ar/blog/", "blog", "المدونة",
         "مقالات عملية عن رسومات الرخام والتنسيق والتصنيع لمشاريع الإمارات.",
         "مدونة"),
        ("en", "/apps/", "app", "Web apps",
         "Free browser tools from D3DDD, including the Still photo leveler.",
         "web apps still"),
        ("ar", "/ar/apps/", "app", "تطبيقات الويب",
         "أدوات مجانية تعمل في المتصفح، ومنها Still لتقويم الصور.",
         "still تطبيقات ويب"),
        ("en", "/resources/uae-directories/", "page", "UAE directories",
         "Maps, UAE business directories, and construction and design listing sites.",
         "directories listings"),
    ]
    for lang, url, kind, title, snippet, keys in core:
        _add(items, seen, lang, url, kind, title, snippet, keys)

    extra_keys = {
        "architectural-estimation": "estimation BOQ quantity takeoff",
        "3d-rendering-modeling-visualization": "3d visualization rendering modelling modeling",
        "architectural-drafting": "autocad shop drawings drafting",
        "architectural-designing": "architectural design space planning",
        "website-development-designing": "website development web design",
    }
    for service in services:
        slug = service["slug"]
        for lang in ("en", "ar"):
            block = service[lang]
            _add(
                items, seen, lang,
                "/ar/services/%s/" % slug if lang == "ar" else "/services/%s/" % slug,
                "service",
                block.get("name"),
                block.get("short") or block.get("desc") or "",
                " ".join(piece for piece in (block.get("desc"), extra_keys.get(slug, "")) if piece),
            )

    for page in landing:
        fn = page["fn"]
        kind = "service" if fn.startswith("fitout-") else "page"
        keys = "fit-out joinery shop drawings" if kind == "service" else ""
        _add(items, seen, "en", _path(fn, "en"), kind, page.get("title"), page.get("desc"), keys)

    for project in PROJECTS:
        _add(
            items, seen, "en",
            "/projects/%s/" % project["slug"],
            "page",
            project.get("title"),
            project.get("short") or project.get("meta_description") or "",
            " ".join(piece for piece in (project.get("category"), project.get("service"), "project") if piece),
        )

    for app in apps:
        slug = app["slug"]
        _add(
            items, seen, "en", "/apps/%s/" % slug, "app",
            app.get("title_en"), app.get("desc_en"),
            "still app image straightener photo leveler straighten photos",
        )
        _add(
            items, seen, "ar", "/apps/%s/" % slug, "app",
            app.get("title_ar"), app.get("desc_ar"),
            "still تطبيق تقويم الصور تسوية",
        )

    for lang in ("en", "ar"):
        for url, title, desc, keys in _posts(lang):
            _add(items, seen, lang, url, "blog", title, desc, keys)

    items.sort(key=lambda row: (row["lang"], row["type"], row["url"]))
    blob = json.dumps({"items": items}, ensure_ascii=False, indent=2)
    lowered = blob.lower()
    if "marble shop drawings" not in lowered:
        raise SystemExit("search index missing marble shop drawings")
    if "/apps/still/" not in blob:
        raise SystemExit("search index missing /apps/still/")
    if "/blog/marble-quantity-calculation-reduce-waste/" not in blob:
        raise SystemExit("search index missing the marble quantity article")
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(blob + "\n", encoding="utf-8")
    _sha_cache.pop(str(INDEX_PATH), None)
    print("search index", len(items), "items", _sha(INDEX_PATH))
    return _sha(INDEX_PATH)

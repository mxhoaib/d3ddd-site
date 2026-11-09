# English resources page: /resources/uae-directories/
# Official homepages only. Checked before this list was written.
import re

FN = "resources/uae-directories/index.html"
TITLE = "UAE Business Directories | D3DDD"
DESC = "Maps, UAE directories, and construction and design listing sites, with the D3DDD name, website and email."


def _a(href, label, follow):
    rel = "noopener" if follow else "noopener nofollow"
    return '<a href="%s" target="_blank" rel="%s">%s</a>' % (href, rel, label)


def _card(href, label, follow, line):
    return '<article class="card"><div class="b"><h3>%s</h3><p>%s</p></div></article>' % (
        _a(href, label, follow), line)


def _group(heading, cards):
    return '<div class="dir-group"><h2>%s</h2><div class="grid g3 dir-grid">%s</div></div>' % (
        heading, "".join(cards))


def strip_instagram(html):
    """This page must not link Instagram @mxhaib. The shared footer otherwise would."""
    html = re.sub(
        r'<a class="social-link" href="https://instagram.com/mxhaib"[^>]*>.*?</a>',
        "",
        html,
    )
    html = html.replace(', "https://www.instagram.com/mxhaib/"', "")
    html = html.replace('"https://www.instagram.com/mxhaib/", ', "")
    return html


def build_directory_page(g):
    shell = g["shell"]
    P = g["prefix"]("en", FN)
    home = P or "./"
    maps = [
        _card("https://business.google.com/", "Google Business Profile", True,
              "The business listing that can appear on Google Search and Maps."),
        _card("https://business.apple.com/", "Apple Business Connect", True,
              "How a business appears on Apple Maps. The tool now opens on Apple Business."),
        _card("https://www.bing.com/forbusiness/", "Bing Places", True,
              "Microsoft’s listing for Bing Search and Bing Maps."),
    ]
    uae = [
        _card("https://www.yello.ae/", "Yello.ae", False,
              "A UAE directory of company profiles."),
    ]
    construction = [
        _card("https://buildeey.com/", "Buildeey", False,
              "A directory of construction professionals and suppliers, with a UAE section."),
        _card("https://www.protenders.com/", "ProTenders", False,
              "A construction tendering platform with company profiles."),
    ]
    business = [
        _card("https://www.dubaichambers.com/", "Dubai Chamber", True,
              "The official chamber for licensed Dubai companies, and its member directory."),
        _card("https://www.linkedin.com/", "LinkedIn", True,
              "The professional network, where a business can publish a company page."),
    ]
    design = [
        _card("https://www.houzz.com/", "Houzz", False,
              "A design and construction directory for professional profiles and project photos."),
        _card("https://architizer.com/", "Architizer", False,
              "An architecture directory for firm profiles and project portfolios."),
    ]
    body = (
        '<section class="page-hero"><nav class="crumbs" aria-label="Breadcrumb">'
        '<a href="%s">Home</a> / <span>UAE directories</span></nav>'
        '<p class="eyebrow">Resources — Dubai &amp; UAE</p>'
        '<h1>UAE business <em>directories.</em></h1>'
        '<p>Maps, local directories, and construction and design sites a drafting studio in Dubai may use. '
        'Each link is that site’s own homepage. A link here is not a listing, and it is not a Dubai Chambers membership.</p>'
        '</section>'
        '<section class="section"><div class="wrap copy">'
        '<h2>Name, website and email</h2>'
        '<dl class="nap">'
        '<div><dt>Name</dt><dd>D3DDD - Dubai 3D Design &amp; Draft</dd></div>'
        '<div><dt>Website</dt><dd><a href="https://d3ddd.com/">https://d3ddd.com</a></dd></div>'
        '<div><dt>Email</dt><dd>info@d3ddd.com</dd></div>'
        '</dl>'
        '<p class="mt-18">Drawing enquiries still go through the <a href="%scontact.html">enquiry form</a>.</p>'
        '</div></section>'
        '<section class="section alt"><div class="wrap">'
        '%s%s%s%s%s'
        '<p class="dir-note mt-28">Opening an account, claiming a profile, or applying for a membership is done by the business owner on that site.</p>'
        '</div></section>'
    ) % (
        home,
        P,
        _group("Maps and search", maps),
        _group("UAE directories", uae),
        _group("Construction and tenders", construction),
        _group("Business", business),
        _group("Design", design),
    )
    ld = [g["crumbs_ld"]("en", [
        ("Home", g["D"]),
        ("UAE directories", g["D"] + "resources/uae-directories/"),
    ])]
    html = shell(
        "en", FN, TITLE, DESC, body, ld,
        bilingual=False, switch=P + "ar/",
    )
    return {("en", FN): strip_instagram(html)}

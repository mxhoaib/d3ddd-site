# Shared contact settings for build.py and scripts/build_blog.py.
import json
# WhatsApp: there is no official click-to-chat link for usernames yet (wa.me only accepts phone numbers),
# so the username is shown as text. To make it a link later, set WHATSAPP_NUMBER to the full international
# number, digits only (no +, spaces or leading 0), then rebuild: python3 build.py
WHATSAPP_USERNAME = "mxhoaib"
WHATSAPP_NUMBER = ""

WA_ICON = ('<svg class="wa-ico" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>')

def whatsapp_html(lang="en"):
    """'WhatsApp: @username' with icon; a wa.me link only once WHATSAPP_NUMBER is set."""
    if not WHATSAPP_USERNAME:
        return ""
    label = "واتساب" if lang == "ar" else "WhatsApp"
    inner = f'{WA_ICON}<span>{label}: <bdi dir="ltr">@{WHATSAPP_USERNAME}</bdi></span>'
    num = "".join(ch for ch in WHATSAPP_NUMBER if ch.isdigit())
    if num:
        return f'<a class="wa-contact" href="https://wa.me/{num}" target="_blank" rel="noopener">{inner}</a>'
    return f'<span class="wa-contact">{inner}</span>'

# GA4 measurement ID (G-XXXXXXXX). No ID is stored in this repo; leave blank to skip the tag.
ANALYTICS_ID = ""

IG_URL = "https://www.instagram.com/dubai3ddd/"
LI_URL = "https://www.linkedin.com/in/mshoaib94"
IG_ICON = ('<svg class="soc-ico" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false">'
           '<path fill="currentColor" d="M7 3h10a4 4 0 0 1 4 4v10a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V7a4 4 0 0 1 4-4zm10 2H7a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2zm-5 3.2A3.8 3.8 0 1 1 8.2 12 3.8 3.8 0 0 1 12 8.2zm0 2A1.8 1.8 0 1 0 13.8 12 1.8 1.8 0 0 0 12 10.2zM17.2 6.8a1 1 0 1 1-1 1 1 1 0 0 1 1-1z"/></svg>')
LI_ICON = ('<svg class="soc-ico" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false">'
           '<path fill="currentColor" d="M6.5 9H4V20h2.5zM5.2 4A1.6 1.6 0 1 0 5.2 7.2 1.6 1.6 0 0 0 5.2 4zM20 20h-2.5v-5.6c0-1.8-.8-2.4-1.8-2.4s-2 .9-2 2.5V20H11V9h2.4v1.5c.5-.8 1.6-1.8 3.3-1.8 2.2 0 3.3 1.4 3.3 4.1z"/></svg>')

def analytics_snippet():
    """gtag snippet, or empty when ANALYTICS_ID is blank."""
    aid = (ANALYTICS_ID or "").strip()
    if not aid:
        return ""
    return (
        '<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>'
        '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
        "gtag('js',new Date());gtag('config',%s);</script>"
    ) % (aid, json.dumps(aid))

def mail_link(fallback_href, label=None, class_name="mail-link"):
    """Link whose address is assembled in assets/site.js from data-u and data-d.
    Until JS runs, it points at the enquiry form. noscript shows the obfuscated fallback.
    """
    inner = '<span class="mail-slot">Email</span>' if label is None else label
    return (
        f'<a class="{class_name}" data-u="info" data-d="d3ddd.com" href="{fallback_href}">{inner}</a>'
        '<noscript> info [at] d3ddd.com</noscript>'
    )

def social_links(lang="en"):
    """Labelled Instagram and LinkedIn icons. WhatsApp is separate and unchanged."""
    ig = "إنستغرام" if lang == "ar" else "Instagram"
    li = "لينكدإن" if lang == "ar" else "LinkedIn"
    return (
        f'<p class="social-row"><a class="social-link" href="{IG_URL}" rel="me noopener" target="_blank">{IG_ICON}<span>{ig}</span></a>'
        f'<a class="social-link" href="{LI_URL}" rel="me noopener" target="_blank">{LI_ICON}<span>{li}</span></a></p>'
    )

def area_served():
    """Cities named on the site, plus the UAE. New York, London and Palm Jumeirah are not listed in the copy."""
    cities = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Umm Al Quwain", "Fujairah"]
    return [{"@type": "City", "name": name} for name in cities] + [{"@type": "Country", "name": "United Arab Emirates"}]

def business_node():
    email = "info@d3ddd.com"
    origin = "https://d3ddd.com/"
    return {
        "@type": ["ProfessionalService", "LocalBusiness"],
        "@id": origin + "#business",
        "name": "D3DDD – Dubai 3D Design & Draft",
        "alternateName": ["D3DDD", "دبي للتصميم والرسم ثلاثي الأبعاد"],
        "url": origin,
        "logo": origin + "assets/img/logo.svg",
        "image": origin + "assets/img/og-image.png",
        "email": email,
        "priceRange": "AED",
        "description": "Marble and stone shop drawings, AutoCAD drafting, fit-out drawings, 3D rendering and contractor website design in Dubai and across the UAE.",
        "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressRegion": "Dubai", "addressCountry": "AE"},
        "areaServed": area_served(),
        "knowsLanguage": ["en", "ar"],
        "contactPoint": {"@type": "ContactPoint", "email": email, "contactType": "sales", "availableLanguage": ["English", "Arabic"]},
        "sameAs": [
            "https://www.fiverr.com/mxhoaib",
            "https://www.instagram.com/dubai3ddd/",
            "https://www.linkedin.com/in/mshoaib94",
        ],
        "paymentAccepted": "PayPal",
    }

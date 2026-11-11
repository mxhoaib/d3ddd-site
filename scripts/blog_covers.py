#!/usr/bin/env python3
"""Topic covers for blog posts that were using the generic site banner.

Line art follows illustrations.py and the homepage palette in assets/style.css:
dark ground, gold and cream strokes, round caps, short labels. Each post gets
an SVG hero and a 1200×630 JPEG for og:image, twitter:image and Article schema.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "img" / "blog"
POSTS = ROOT / "posts"

BG = "#0e0e0c"
CARD = "#1b1a17"
INK = "#ece6da"
MUTED = "#a9a296"
GOLD = "#c9a96e"
GOLD2 = "#e2c99a"
LINE = "#3a362e"


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, text, size=16, fill=MUTED, anchor="middle", spacing="1.2"):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{fill}" '
        f'stroke="none" font-family="Inter, Liberation Sans, sans-serif" '
        f'font-size="{size}" letter-spacing="{spacing}">{esc(text)}</text>'
    )


def line(a, b, stroke=GOLD, sw=2.2, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
        f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"{extra}/>'
    )


def rect(x, y, w, h, stroke=GOLD, sw=2.2, fill="none", op=1, rx=0):
    fill_attr = f' fill="{fill}"' if fill != "none" else ' fill="none"'
    op_attr = f' fill-opacity="{op}"' if fill != "none" else ""
    rx_attr = f' rx="{rx}"' if rx else ""
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"{rx_attr}'
        f'{fill_attr}{op_attr} stroke="{stroke}" stroke-width="{sw}"/>'
    )


def circle(cx, cy, r, stroke=GOLD, sw=2.2, fill="none", op=1):
    fill_attr = f' fill="{fill}"' if fill != "none" else ' fill="none"'
    op_attr = f' fill-opacity="{op}"' if fill != "none" else ""
    return (
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"{fill_attr}{op_attr} '
        f'stroke="{stroke}" stroke-width="{sw}"/>'
    )


def poly(pts, stroke=GOLD, sw=2.2, fill="none", op=1):
    points = " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
    fill_attr = f' fill="{fill}"' if fill != "none" else ' fill="none"'
    op_attr = f' fill-opacity="{op}"' if fill != "none" else ""
    return (
        f'<polygon points="{points}"{fill_attr}{op_attr} stroke="{stroke}" '
        f'stroke-width="{sw}" stroke-linejoin="round"/>'
    )


def path(d, stroke=GOLD, sw=2.2, fill="none", op=1, dash=None):
    fill_attr = f' fill="{fill}"' if fill != "none" else ' fill="none"'
    op_attr = f' fill-opacity="{op}"' if fill != "none" else ""
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<path d="{d}"{fill_attr}{op_attr} stroke="{stroke}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round"{dash_attr}/>'
    )


def I(x, y, z, ox, oy, s=1.0):
    return (ox + (x - y) * 0.8660254 * s, oy + (x + y) * 0.5 * s - z * s)


def zbox(x, y, z, w, d, h, ox, oy, s=1.0, stroke=GOLD, sw=2.2, top=0.16, side=0.07):
    P = lambda X, Y, Z: I(X, Y, Z, ox, oy, s)
    top_pts = [P(x, y, z + h), P(x + w, y, z + h), P(x + w, y + d, z + h), P(x, y + d, z + h)]
    right = [P(x + w, y, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x + w, y, z + h)]
    front = [P(x, y + d, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x, y + d, z + h)]
    return (
        poly(front, stroke, sw, GOLD, side)
        + poly(right, stroke, sw, GOLD, side * 0.65)
        + poly(top_pts, stroke, sw, GOLD, top)
    )


def check(x, y, stroke=GOLD2):
    return path(f"M {x:.1f} {y:.1f} l 8 10 l 18 -22", stroke, 2.6)


def tick_h(x1, x2, y, label):
    return (
        line((x1, y), (x2, y), GOLD2, 1.6)
        + line((x1, y - 7), (x1, y + 7), GOLD2, 1.6)
        + line((x2, y - 7), (x2, y + 7), GOLD2, 1.6)
        + T((x1 + x2) / 2, y - 12, label, 15, GOLD2, spacing="0.6")
    )


def tick_v(x, y1, y2, label, anchor="start", lx=12):
    return (
        line((x, y1), (x, y2), GOLD2, 1.6)
        + line((x - 7, y1), (x + 7, y1), GOLD2, 1.6)
        + line((x - 7, y2), (x + 7, y2), GOLD2, 1.6)
        + T(x + lx, (y1 + y2) / 2 + 5, label, 15, GOLD2, anchor, spacing="0.6")
    )


def sheet(x, y, w, h, title=None):
    body = rect(x, y, w, h, GOLD, 2.3, CARD, 1, 8)
    body += line((x, y + 42), (x + w, y + 42), LINE, 1.5)
    if title:
        body += T(x + 18, y + 28, title, 15, GOLD2, "start", "1.4")
    return body


def cover(title: str, body: str, label: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img">
<title>{esc(title)}</title>
<rect width="1200" height="630" fill="{BG}"/>
<defs>
<radialGradient id="glow" cx="58%" cy="40%" r="62%">
<stop offset="0%" stop-color="{GOLD}" stop-opacity="0.15"/>
<stop offset="72%" stop-color="{GOLD}" stop-opacity="0.03"/>
<stop offset="100%" stop-color="{GOLD}" stop-opacity="0"/>
</radialGradient>
</defs>
<rect width="1200" height="630" fill="url(#glow)"/>
<rect x="32" y="32" width="1136" height="566" rx="18" fill="none" stroke="{GOLD}" stroke-opacity="0.28" stroke-width="1.5"/>
{body}
<line x1="72" y1="556" x2="156" y2="556" stroke="{GOLD}" stroke-width="2"/>
{T(172, 562, "D3DDD", 15, GOLD2, "start", "2")}
{T(1128, 562, label, 15, MUTED, "end", "2.2")}
</svg>
'''


def tower(x, yb, w, h):
    top = yb - h
    parts = [rect(x, top, w, h, GOLD, 2.2, GOLD, 0.08)]
    y = top + 16
    while y < yb - 12:
        parts.append(line((x + 7, y), (x + w - 7, y), GOLD2, 1.15))
        y += 18
    return "".join(parts)


def burj(x, base):
    levels = [(36, 0, 78), (28, 78, 58), (20, 136, 50), (13, 186, 42), (8, 228, 34)]
    parts = []
    for half, y0, h in levels:
        y = base - y0
        parts.append(
            poly(
                [(x - half, y), (x + half, y), (x + half * 0.62, y - h), (x - half * 0.62, y - h)],
                GOLD,
                2.1,
                GOLD,
                0.1,
            )
        )
    tip = base - 262
    parts.append(line((x, tip), (x, tip - 78), GOLD2, 2.2))
    return "".join(parts)


def skyline(base=478):
    parts = [
        line((640, base), (1110, base), GOLD, 2.2),
        tower(668, base, 42, 150),
        tower(722, base, 34, 108),
        burj(812, base),
        tower(900, base, 48, 176),
        tower(962, base, 30, 96),
        tower(1006, base, 54, 132),
        tower(1072, base, 26, 74),
    ]
    return "".join(parts)


def draw_bim():
    ox, oy, s = 300, 392, 1.02
    w, d = 168, 112
    parts = [skyline(), zbox(0, 0, 0, w, d, 9, ox, oy, s, sw=2.3, top=0.2)]
    for cx, cy in ((10, 10), (10, d - 22), (w - 22, 10), (w - 22, d - 22)):
        parts.append(zbox(cx, cy, 16, 12, 12, 52, ox, oy, s, sw=1.7, top=0.12, side=0.1))
    parts.append(zbox(0, 0, 78, w, d, 9, ox, oy, s, sw=2.3, top=0.18))
    parts.append(zbox(36, 28, 87, 52, 40, 30, ox, oy, s, stroke=GOLD2, sw=1.8, top=0.1, side=0.08))
    parts.append(zbox(0, 0, 148, w, d, 8, ox, oy, s, sw=2.3, top=0.22))
    parts.append(zbox(18, 46, 156, 132, 16, 14, ox, oy, s, stroke=GOLD2, sw=1.8, top=0.2, side=0.12))
    for z, name in ((18, "STR"), (96, "ARCH"), (164, "MEP")):
        p = I(w + 6, 18, z, ox, oy, s)
        parts.append(T(p[0] + 14, p[1], name, 15, GOLD2, "start", "1.6"))
    parts.append(rect(168, 128, 86, 34, GOLD, 1.8, GOLD, 0.14, 17))
    parts.append(T(211, 151, "IFC", 16, GOLD2, spacing="1.8"))
    return "".join(parts)


def draw_ifc():
    ox, oy, s = 250, 430, 1.15
    parts = [zbox(0, 0, 0, 92, 70, 150, ox, oy, s, sw=2.3, top=0.18)]
    parts.append(zbox(92, 18, 0, 58, 48, 78, ox, oy, s, sw=2.2, top=0.14))
    # window bands on the tower front face
    for t in (0.25, 0.45, 0.65, 0.82):
        z = 18 + 120 * t
        a = I(6, 70, z, ox, oy, s)
        b = I(86, 70, z, ox, oy, s)
        parts.append(line(a, b, GOLD2, 1.3))
    parts.append(path("M 560 300 H 690", GOLD, 2.4))
    parts.append(poly([(690, 300), (674, 290), (674, 310)], GOLD, 2.2, GOLD, 1))
    parts.append(T(625, 284, "EXPORT", 14, GOLD2, spacing="1.8"))
    parts.append(sheet(730, 128, 340, 360, "IFC 4"))
    parts.append(rect(760, 196, 280, 70, GOLD2, 1.8, GOLD, 0.08, 6))
    parts.append(T(900, 238, ".IFC", 28, INK, spacing="1.2"))
    rows = [("UNITS  ·  mm", 300), ("CLASSIFICATION", 344), ("COORDINATES", 388)]
    for label, y in rows:
        parts.append(check(770, y - 12))
        parts.append(T(812, y, label, 16, INK, "start", "0.8"))
    return "".join(parts)


def draw_clash():
    ox, oy, s = 470, 250, 2.15
    parts = [
        zbox(0, 36, 18, 210, 26, 22, ox, oy, s, sw=2.5, top=0.18, side=0.09),
        zbox(92, -10, 26, 22, 150, 22, ox, oy, s, stroke=GOLD2, sw=2.5, top=0.22, side=0.12),
    ]
    hit = I(103, 49, 40, ox, oy, s)
    parts.append(circle(hit[0], hit[1], 34, GOLD2, 2.8, GOLD, 0.16))
    parts.append(line((hit[0] - 14, hit[1] - 14), (hit[0] + 14, hit[1] + 14), INK, 2.6))
    parts.append(line((hit[0] + 14, hit[1] - 14), (hit[0] - 14, hit[1] + 14), INK, 2.6))
    parts.append(T(hit[0], hit[1] + 58, "CLASH", 16, GOLD2, spacing="2"))
    parts.append(sheet(78, 150, 250, 250, "REPORT"))
    for i, (label, mark) in enumerate((("DUCT  vs  BEAM", True), ("PIPE  vs  DUCT", True), ("CEILING  SOFT", False))):
        y = 230 + i * 48
        parts.append(rect(100, y - 16, 22, 22, GOLD2 if mark else MUTED, 1.8, "none", 1, 3))
        if mark:
            parts.append(line((106, 230 + i * 48 - 16), (116, 246 + i * 48 - 16), GOLD2, 2.2))
            parts.append(line((116, 230 + i * 48 - 16), (106, 246 + i * 48 - 16), GOLD2, 2.2))
        parts.append(T(136, y, label, 14, INK if mark else MUTED, "start", "0.6"))
    return "".join(parts)


def draw_nesting():
    parts = [rect(70, 110, 620, 390, GOLD, 2.5, CARD, 1, 4)]
    parts.append(path("M 110 190 C 220 140, 280 250, 400 190 C 500 140, 560 240, 650 200", GOLD2, 1.6))
    parts.append(path("M 120 340 C 240 300, 320 400, 460 350 C 540 320, 590 400, 660 360", GOLD2, 1.5))
    parts.append(path("M 276 110 V 500 M 482 110 V 500 M 70 305 H 690", GOLD, 1.8, dash="7 6"))
    labels = [(173, 220, "01"), (379, 220, "02"), (586, 220, "03"), (173, 400, "04"), (379, 400, "05"), (586, 400, "06")]
    for x, y, name in labels:
        parts.append(T(x, y, name, 22, GOLD2, spacing="1"))
    parts.append(sheet(760, 110, 360, 390, "CUTTING LIST"))
    parts.append(line((784, 196), (1096, 196), LINE, 1.4))
    parts.append(T(800, 184, "PIECE", 13, GOLD2, "start", "1"))
    parts.append(T(980, 184, "QTY", 13, GOLD2, "start", "1"))
    parts.append(T(1060, 184, "UNIT", 13, GOLD2, "start", "1"))
    rows = [("01", "1.20", "m²"), ("02", "0.84", "m²"), ("03", "1.05", "m²"), ("04", "0.66", "m²"), ("05", "0.92", "m²"), ("06", "0.71", "m²")]
    for i, (piece, qty, unit) in enumerate(rows):
        y = 232 + i * 36
        parts.append(T(800, y, piece, 16, INK, "start", "0.4"))
        parts.append(T(980, y, qty, 16, INK, "start", "0.4"))
        parts.append(T(1060, y, unit, 16, MUTED, "start", "0.4"))
    parts.append(T(800, 470, "YIELD", 14, GOLD2, "start", "1.4"))
    return "".join(parts)


def draw_render():
    ox, oy, s = 200, 300, 1.35
    parts = [zbox(0, 0, 0, 210, 140, 5, ox, oy, s, sw=2.2, top=0.1)]
    parts.append(zbox(0, 0, 5, 7, 140, 108, ox, oy, s, sw=2.2, top=0.08, side=0.1))
    parts.append(zbox(0, 0, 5, 210, 7, 108, ox, oy, s, sw=2.2, top=0.08, side=0.06))
    # window on the back wall face
    win = [I(x, 7, z, ox, oy, s) for x, z in ((48, 86), (130, 86), (130, 36), (48, 36))]
    parts.append(poly(win, GOLD2, 2, GOLD, 0.08))
    parts.append(line(I(89, 7, 36, ox, oy, s), I(89, 7, 86, ox, oy, s), GOLD2, 1.5))
    parts.append(zbox(22, 36, 5, 72, 30, 22, ox, oy, s, sw=2, top=0.14))
    parts.append(zbox(22, 36, 27, 72, 10, 16, ox, oy, s, stroke=GOLD2, sw=1.7, top=0.12))
    parts.append(zbox(112, 48, 5, 42, 36, 16, ox, oy, s, sw=1.9, top=0.12))
    hang = I(150, 28, 108, ox, oy, s)
    lamp = I(150, 28, 62, ox, oy, s)
    parts.append(line(hang, lamp, GOLD2, 1.6))
    parts.append(poly([(lamp[0] - 16, lamp[1]), (lamp[0] + 16, lamp[1] - 8), (lamp[0] + 8, lamp[1] + 14)], GOLD2, 1.8, GOLD, 0.15))
    # camera and rays
    parts.append(rect(860, 168, 150, 78, GOLD, 2.2, CARD, 1, 8))
    parts.append(circle(1010, 206, 34, GOLD2, 2.4))
    parts.append(circle(1010, 206, 14, GOLD, 1.8, GOLD, 0.3))
    room = I(120, 40, 50, ox, oy, s)
    parts.append(line((976, 206), room, GOLD2, 1.5, "5 5"))
    parts.append(line((976, 180), I(89, 7, 60, ox, oy, s), GOLD2, 1.4, "5 5"))
    parts.append(line((976, 232), I(58, 50, 20, ox, oy, s), GOLD2, 1.4, "5 5"))
    parts.append(T(935, 278, "CAMERA", 14, MUTED, spacing="1.6"))
    return "".join(parts)


def draw_stair():
    parts = []
    x, y = 150, 470
    tw, rh, n = 92, 42, 7
    parts.append(line((x - 36, y + 18), (x + tw * n - 20, y - rh * n + 8), GOLD, 3))
    parts.append(line((x - 16, y + 36), (x + tw * n, y - rh * n + 26), GOLD2, 2))
    for i in range(n):
        parts.append(line((x + i * tw, y - i * rh), (x + i * tw, y - (i + 1) * rh), INK, 2.4))
        parts.append(line((x + i * tw - 14, y - (i + 1) * rh), (x + (i + 1) * tw, y - (i + 1) * rh), GOLD, 2.6))
        parts.append(line((x + i * tw - 14, y - (i + 1) * rh + 8), (x + (i + 1) * tw, y - (i + 1) * rh + 8), GOLD2, 1.3))
    # landing and wall
    land_x = x + tw * n
    land_y = y - rh * n
    parts.append(line((land_x, land_y), (land_x + 90, land_y), GOLD, 2.6))
    parts.append(line((land_x + 90, land_y), (land_x + 90, land_y - 70), MUTED, 2))
    for i in (1, 3, 5):
        fx = x + i * tw + 20
        fy = y - i * rh + 28
        parts.append(circle(fx, fy, 6, GOLD2, 1.8, GOLD, 0.2))
    parts.append(tick_h(x, x + tw, y + 28, "TREAD"))
    parts.append(tick_v(x - 28, y, y - rh, "RISER", "end", -8))
    parts.append(T(x + 3 * tw + 24, y - 3 * rh + 62, "STRINGER", 14, GOLD2, "start", "1.2"))
    parts.append(T(land_x + 8, land_y - 18, "NOSING", 15, GOLD2, "start", "1.4"))
    return "".join(parts)


def draw_floor_wall():
    ox, oy, s = 250, 300, 1.28
    parts = [zbox(0, 0, 0, 180, 130, 6, ox, oy, s, sw=2.3, top=0.12)]
    for i in (1, 2):
        a = I(180 * i / 3, 0, 6, ox, oy, s)
        b = I(180 * i / 3, 130, 6, ox, oy, s)
        parts.append(line(a, b, GOLD2, 1.4))
        c = I(0, 130 * i / 3, 6, ox, oy, s)
        d = I(180, 130 * i / 3, 6, ox, oy, s)
        parts.append(line(c, d, GOLD2, 1.4))
    parts.append(path(
        "M {0:.0f} {1:.0f} C {2:.0f} {3:.0f}, {4:.0f} {5:.0f}, {6:.0f} {7:.0f}".format(
            *I(20, 30, 6, ox, oy, s), *I(70, 10, 6, ox, oy, s), *I(90, 50, 6, ox, oy, s), *I(150, 24, 6, ox, oy, s)
        ),
        GOLD2,
        1.4,
    ))
    parts.append(T(300, 520, "FLOOR", 15, GOLD2, spacing="2"))
    # bookmatched wall elevation
    parts.append(rect(700, 90, 390, 400, GOLD, 2.4, CARD, 1, 4))
    parts.append(line((895, 90), (895, 490), GOLD, 1.6))
    parts.append(line((700, 290), (1090, 290), GOLD, 1.6))
    parts.append(path("M 730 150 C 800 190, 840 130, 880 170", GOLD2, 1.5))
    parts.append(path("M 1060 150 C 990 190, 950 130, 910 170", GOLD2, 1.5))
    parts.append(path("M 730 340 C 810 390, 850 320, 880 360", GOLD2, 1.5))
    parts.append(path("M 1060 340 C 980 390, 940 320, 910 360", GOLD2, 1.5))
    parts.append(tick_v(1112, 90, 490, "H", "start", 14))
    parts.append(T(895, 524, "WALL CLADDING", 15, GOLD2, spacing="1.8"))
    return "".join(parts)


def draw_shop():
    parts = [sheet(120, 78, 960, 450, "SHOP DWG   ·   STN-101")]
    parts.append(rect(170, 160, 460, 250, GOLD, 2.2))
    parts.append(path("M 210 230 C 300 190, 340 280, 430 230 C 500 190, 540 270, 600 240", GOLD2, 1.5))
    parts.append(path("M 200 340 C 300 310, 360 390, 470 340", GOLD2, 1.4))
    parts.append(circle(400, 285, 46, GOLD2, 2))
    parts.append(tick_h(170, 630, 440, "2 400"))
    parts.append(tick_v(660, 160, 410, "800"))
    parts.append(rect(760, 170, 270, 180, MUTED, 1.6))
    parts.append(line((760, 206), (1030, 206), LINE, 1.3))
    parts.append(line((760, 242), (1030, 242), LINE, 1.3))
    parts.append(line((760, 278), (1030, 278), LINE, 1.3))
    parts.append(line((760, 314), (1030, 314), LINE, 1.3))
    parts.append(T(780, 196, "TITLE", 13, GOLD2, "start", "1.2"))
    parts.append(T(895, 232, "DWG", 16, INK, spacing="1"))
    parts.append(T(990, 232, "PDF", 16, GOLD2, spacing="1"))
    parts.append(T(895, 304, "REV A", 16, GOLD2, spacing="1"))
    return "".join(parts)


def draw_checklist():
    parts = [rect(150, 118, 420, 390, GOLD, 2.4, CARD, 1, 10)]
    parts.append(rect(270, 86, 180, 48, GOLD2, 2, CARD, 1, 10))
    parts.append(circle(360, 110, 8, GOLD, 1.8))
    rows = [("PIECE ID", True), ("EDGE PROFILE", True), ("JOINT LAYOUT", True), ("THICKNESS", True), ("SITE MEASURE", False)]
    for i, (label, done) in enumerate(rows):
        y = 190 + i * 58
        parts.append(rect(186, y - 18, 26, 26, GOLD2 if done else MUTED, 1.8, "none", 1, 4))
        if done:
            parts.append(check(190, y - 10))
        parts.append(T(232, y, label, 18, INK if done else MUTED, "start", "0.8"))
    parts.append(rect(680, 160, 360, 280, GOLD, 2.2, CARD, 1, 6))
    parts.append(path("M 720 250 C 800 210, 860 300, 980 240", GOLD2, 1.6))
    parts.append(path("M 730 360 C 840 320, 900 400, 1000 350", GOLD2, 1.5))
    parts.append(circle(860, 300, 36, GOLD, 1.8))
    parts.append(T(860, 470, "SLAB", 15, GOLD2, spacing="2"))
    return "".join(parts)


def draw_smart_blocks():
    parts = [line((120, 340), (760, 340), MUTED, 2)]
    parts.append(line((250, 340), (250, 210), GOLD, 2.6))
    parts.append(path("M 250 340 A 130 130 0 0 1 380 210", GOLD2, 1.8))
    for px, py in ((250, 340), (250, 210), (380, 340)):
        parts.append(rect(px - 8, py - 8, 16, 16, GOLD2, 1.8, GOLD, 0.35, 2))
    parts.append(line((520, 340), (520, 210), GOLD, 2.2, "7 6"))
    parts.append(path("M 520 340 A 130 130 0 0 1 650 210", GOLD2, 1.6, dash="7 6"))
    parts.append(path("M 430 270 H 500", GOLD, 2))
    parts.append(poly([(500, 270), (486, 262), (486, 278)], GOLD, 2, GOLD, 1))
    parts.append(line((700, 160), (700, 220), GOLD2, 2.2))
    parts.append(line((670, 190), (730, 190), GOLD2, 2.2))
    parts.append(line((678, 168), (722, 212), GOLD, 1.6))
    parts.append(line((722, 168), (678, 212), GOLD, 1.6))
    parts.append(rect(748, 128, 70, 32, GOLD, 1.6, GOLD, 0.14, 16))
    parts.append(T(783, 150, "AI", 16, GOLD2, spacing="1.5"))
    parts.append(rect(860, 230, 220, 220, GOLD, 2, CARD, 1, 8))
    parts.append(T(970, 280, "BLOCK", 18, INK, spacing="1.6"))
    parts.append(line((900, 310), (1040, 310), LINE, 1.4))
    parts.append(line((900, 350), (1000, 350), LINE, 1.4))
    parts.append(line((900, 390), (1020, 390), LINE, 1.4))
    parts.append(T(970, 424, "DYNAMIC", 14, GOLD2, spacing="1.4"))
    return "".join(parts)


def draw_floor_plan():
    parts = [rect(120, 110, 620, 400, INK, 3)]
    parts.append(rect(138, 128, 584, 364, GOLD, 2))
    # interior wall with door gap
    parts.append(line((138, 300), (540, 300), GOLD, 2.2))
    parts.append(line((630, 300), (722, 300), GOLD, 2.2))
    parts.append(line((540, 300), (540, 210), GOLD2, 2.2))
    parts.append(path("M 630 300 C 630 250, 590 210, 540 210", GOLD2, 1.6))
    parts.append(line((460, 128), (460, 280), MUTED, 2, "8 6"))
    parts.append(T(300, 220, "MAJLIS", 20, INK, spacing="1.6"))
    parts.append(T(680, 230, "NEW", 16, GOLD2, spacing="1.4"))
    parts.append(T(400, 250, "EX", 14, MUTED, spacing="1"))
    parts.append(T(400, 410, "HALL", 20, INK, spacing="1.6"))
    parts.append(line((96, 150), (96, 118), GOLD, 2))
    parts.append(poly([(96, 108), (90, 124), (102, 124)], GOLD, 1.5, GOLD, 1))
    parts.append(T(96, 100, "N", 13, GOLD2))
    parts.append(sheet(800, 140, 300, 340, "ACA"))
    parts.append(T(830, 230, "WALLS", 18, INK, "start", "1"))
    parts.append(T(830, 280, "DOORS", 18, INK, "start", "1"))
    parts.append(T(830, 330, "SPACES", 18, INK, "start", "1"))
    parts.append(T(830, 390, "RENOVATION", 16, GOLD2, "start", "1"))
    parts.append(line((830, 410), (1000, 410), GOLD, 2))
    parts.append(line((830, 430), (1000, 430), MUTED, 2, "8 6"))
    return "".join(parts)


def draw_standards():
    parts = [sheet(70, 100, 460, 420, "LAYERS")]
    rows = [
        ("A-WALL", False, 2.8, GOLD),
        ("A-DOOR", False, 2.2, GOLD2),
        ("A-GLAZ", True, 1.8, GOLD2),
        ("A-DIM", False, 1.4, MUTED),
        ("XREF", True, 1.8, MUTED),
        ("A-ANNO", False, 1.5, INK),
    ]
    for i, (name, dashed, sw, color) in enumerate(rows):
        y = 180 + i * 52
        parts.append(T(96, y, name, 16, INK, "start", "0.8"))
        parts.append(line((250, y - 6), (490, y - 6), color, sw, "8 6" if dashed else None))
    parts.append(rect(620, 120, 480, 370, GOLD, 2.3))
    parts.append(rect(660, 170, 400, 250, GOLD2, 2))
    parts.append(line((660, 300), (860, 300), GOLD, 2.4))
    parts.append(line((980, 170), (980, 280), GOLD2, 1.8, "8 6"))
    parts.append(line((900, 170), (900, 420), MUTED, 1.6))
    parts.append(T(860, 450, "XREF PLAN", 15, GOLD2, spacing="1.6"))
    return "".join(parts)


def draw_draftsight():
    parts = [rect(80, 90, 1040, 430, GOLD, 2.3, CARD, 1, 8)]
    parts.append(rect(80, 90, 220, 36, GOLD, 1.6, GOLD, 0.12, 0))
    parts.append(T(190, 114, "DRAWING.DWG", 14, GOLD2, spacing="0.8"))
    # crosshair
    parts.append(line((600, 150), (600, 460), GOLD2, 1.2))
    parts.append(line((140, 300), (1060, 300), GOLD2, 1.2))
    parts.append(rect(430, 250, 8, 8, GOLD, 1.4, GOLD, 0.8))
    # simple 2D plan under the cursor
    parts.append(rect(250, 190, 360, 220, INK, 2.4))
    parts.append(line((250, 300), (430, 300), GOLD, 2))
    parts.append(line((500, 190), (500, 270), GOLD, 2))
    parts.append(path("M 430 300 A 70 70 0 0 1 500 230", GOLD2, 1.6))
    parts.append(rect(760, 200, 250, 180, MUTED, 1.8))
    parts.append(line((760, 250), (1010, 250), LINE, 1.3))
    parts.append(line((760, 300), (1010, 300), LINE, 1.3))
    parts.append(T(885, 236, "2D", 20, INK, spacing="1.5"))
    parts.append(T(140, 500, "COMMAND:  LINE", 15, GOLD2, "start", "1.2"))
    return "".join(parts)


def draw_forma():
    ox, oy, s = 280, 360, 1.15
    parts = [path("M 150 360 C 210 240, 290 200, 450 230 C 590 250, 650 360, 570 410 C 430 470, 210 450, 150 360 Z", GOLD, 2.2, GOLD, 0.06)]
    parts.append(zbox(0, 0, 0, 70, 50, 90, ox, oy, s, sw=2.2, top=0.2))
    parts.append(zbox(84, 10, 0, 48, 40, 54, ox, oy, s, stroke=GOLD2, sw=2, top=0.16))
    parts.append(zbox(24, 62, 0, 56, 36, 36, ox, oy, s, sw=2, top=0.12))
    # sun
    parts.append(circle(900, 150, 36, GOLD2, 2.4, GOLD, 0.15))
    parts.append(path("M 820 210 Q 900 250 990 190", GOLD, 1.8))
    for ang in range(6):
        import math
        a = math.radians(-40 + ang * 22)
        parts.append(line((900 + math.cos(a) * 48, 150 + math.sin(a) * 48), (900 + math.cos(a) * 70, 150 + math.sin(a) * 70), GOLD2, 1.6))
    # wind arrows
    for i, y in enumerate((300, 346, 392)):
        parts.append(line((820, y), (1040 - i * 30, y), GOLD, 1.8))
        parts.append(poly([(1040 - i * 30, y), (1024 - i * 30, y - 7), (1024 - i * 30, y + 7)], GOLD, 1.6, GOLD, 1))
    parts.append(T(300, 130, "MASSING", 15, GOLD2, spacing="1.8"))
    parts.append(T(900, 250, "SUN", 14, GOLD2, spacing="1.6"))
    parts.append(T(930, 430, "WIND", 14, GOLD2, spacing="1.6"))
    return "".join(parts)


def draw_permit():
    parts = [
        rect(210, 150, 460, 320, LINE, 1.6, "#141410", 1, 6),
        rect(180, 132, 460, 320, MUTED, 1.6, "#17160f", 1, 6),
        sheet(150, 114, 460, 320, "A-101  ·  PDF"),
    ]
    parts.append(rect(190, 180, 200, 140, GOLD, 1.8))
    parts.append(line((190, 250), (390, 250), GOLD2, 1.3))
    parts.append(line((290, 180), (290, 320), GOLD2, 1.3))
    parts.append(line((430, 190), (560, 190), LINE, 1.5))
    parts.append(line((430, 220), (540, 220), LINE, 1.5))
    parts.append(line((430, 250), (560, 250), LINE, 1.5))
    # stamp
    parts.append(circle(860, 280, 110, GOLD, 2.6))
    parts.append(circle(860, 280, 92, GOLD2, 1.4))
    parts.append(check(820, 276, GOLD2))
    parts.append(T(860, 250, "REVIEWED", 16, GOLD2, spacing="1.6"))
    parts.append(T(860, 320, "SET", 16, INK, spacing="2"))
    parts.append(T(860, 450, "LAYERS  ·  TITLE  ·  DIMS", 14, MUTED, spacing="1.2"))
    return "".join(parts)


def draw_allocation():
    parts = [sheet(64, 96, 640, 420, "SLAB  01  ·  ALLOCATION")]
    parts.append(rect(96, 176, 250, 148, GOLD, 2.1))
    parts.append(rect(366, 176, 300, 148, GOLD, 2.1))
    parts.append(line((356, 176), (356, 324), GOLD2, 1.3, "3 5"))
    parts.append(T(356, 164, "KERF", 12, GOLD2, spacing="0.8"))
    parts.append(path("M 118 248 C 190 196, 280 268, 346 232", GOLD2, 1.5))
    parts.append(path("M 366 232 C 440 196, 540 268, 640 232", GOLD2, 1.5))
    parts.append(path("M 130 300 C 200 268, 280 318, 346 292", GOLD2, 1.3))
    parts.append(path("M 366 292 C 450 268, 560 318, 648 292", GOLD2, 1.3))
    parts.append(T(221, 270, "P-01", 18, INK, spacing="1"))
    parts.append(T(516, 270, "P-02", 18, INK, spacing="1"))
    parts.append(rect(96, 348, 168, 122, GOLD, 2.0))
    parts.append(rect(284, 348, 176, 122, GOLD, 2.0))
    parts.append(rect(480, 348, 186, 122, LINE, 1.6))
    parts.append(T(180, 416, "P-03", 16, GOLD2, spacing="1"))
    parts.append(T(372, 416, "P-04", 16, GOLD2, spacing="1"))
    parts.append(T(573, 408, "OFFCUT", 13, MUTED, spacing="1.1"))
    parts.append(T(384, 492, "VEIN MATCH", 14, MUTED, spacing="1.6"))
    parts.append(sheet(740, 96, 400, 420, "BOOK MATCH"))
    parts.append(rect(768, 178, 160, 248, GOLD, 2.1))
    parts.append(rect(948, 178, 160, 248, GOLD, 2.1))
    parts.append(line((928, 178), (928, 426), GOLD2, 1.3, "4 5"))
    parts.append(path("M 788 250 C 840 210, 880 300, 918 238", GOLD2, 1.6))
    parts.append(path("M 1088 250 C 1036 210, 996 300, 958 238", GOLD2, 1.6))
    parts.append(path("M 800 338 C 848 308, 888 378, 918 328", GOLD2, 1.4))
    parts.append(path("M 1076 338 C 1028 308, 988 378, 958 328", GOLD2, 1.4))
    parts.append(T(848, 300, "A", 16, INK, spacing="1"))
    parts.append(T(1028, 300, "A'", 16, INK, spacing="1"))
    parts.append(T(940, 470, "MIRROR  ·  SLAB 02", 14, MUTED, spacing="1.2"))
    return "".join(parts)


def draw_shop_vs_fab():
    parts = [sheet(72, 92, 460, 410, "SHOP  ·  APPROVAL")]
    parts.append(rect(104, 168, 270, 190, GOLD, 2.1))
    parts.append(line((194, 168), (194, 358), GOLD2, 1.4))
    parts.append(line((284, 168), (284, 358), GOLD2, 1.4))
    parts.append(line((104, 262), (374, 262), GOLD2, 1.4))
    parts.append(path("M 124 214 C 180 180, 230 246, 300 204", GOLD2, 1.4))
    parts.append(path("M 130 310 C 200 280, 250 340, 340 308", GOLD2, 1.3))
    parts.append(circle(430, 250, 64, GOLD, 2.4))
    parts.append(circle(430, 250, 52, GOLD2, 1.3))
    parts.append(check(402, 248, GOLD2))
    parts.append(T(430, 226, "APPROVED", 12, GOLD2, spacing="1.1"))
    parts.append(T(430, 286, "REV B", 13, INK, spacing="1.4"))
    parts.append(T(302, 470, "LAYOUT  ·  JOINTS", 14, MUTED, spacing="1.1"))
    parts.append(T(600, 318, "VS", 26, GOLD2, spacing="3"))
    parts.append(sheet(668, 92, 460, 410, "FAB  ·  P-04"))
    parts.append(rect(708, 168, 230, 156, GOLD, 2.2))
    parts.append(rect(778, 206, 96, 72, GOLD2, 1.8, CARD, 1, 18))
    parts.append(T(823, 248, "SINK", 13, GOLD2, spacing="1.2"))
    parts.append(tick_h(708, 938, 352, "860"))
    parts.append(tick_v(958, 168, 324, "540", "start", 12))
    parts.append(T(708, 400, "EDGE  E1", 15, GOLD2, "start", "0.8"))
    parts.append(T(860, 400, "THK  20", 15, INK, "start", "0.8"))
    parts.append(line((708, 418), (1088, 418), LINE, 1.3))
    parts.append(T(708, 448, "CUT LIST", 14, MUTED, "start", "1.4"))
    parts.append(T(860, 448, "P-04", 14, GOLD2, "start", "1"))
    return "".join(parts)


def draw_p6():
    def panel(x, title, bars, link):
        body = [rect(x, 108, 470, 410, GOLD, 2.3, CARD, 1, 10)]
        body.append(T(x + 235, 156, title, 22, GOLD2, spacing="1.6"))
        body.append(line((x + 28, 178), (x + 442, 178), LINE, 1.4))
        for i, (label, start, w) in enumerate(bars):
            y = 204 + i * 48
            body.append(T(x + 28, y + 18, label, 14, MUTED, "start", "0.5"))
            body.append(rect(x + 118 + start, y, w, 24, GOLD if i % 2 == 0 else GOLD2, 1.6, GOLD, 0.2, 4))
            if link and i < len(bars) - 1 and bars[i + 1][1] + 6 >= start + w:
                x1 = x + 118 + start + w
                y1 = y + 12
                y2 = y + 60
                x2 = x + 118 + bars[i + 1][1]
                body.append(path(f"M {x1:.0f} {y1:.0f} V {y2:.0f} H {x2:.0f}", GOLD2, 1.3))
        return "".join(body)

    p6 = [("MOB", 0, 40), ("DRAW", 48, 52), ("STONE", 108, 52), ("FIX", 168, 48), ("SNAG", 224, 44), ("HAND", 276, 40)]
    msp = [("MOB", 0, 70), ("DRAW", 0, 160), ("STONE", 0, 120), ("FIX", 0, 90), ("SNAG", 0, 60), ("HAND", 0, 48)]
    return panel(60, "P6", p6, True) + panel(670, "MSP", msp, False) + T(600, 320, "VS", 22, GOLD2, spacing="2")


COVERS = {
    "dubai-bim-mandate-2026-submission-guide": (
        "Isometric BIM model split into architecture, structure and MEP layers beside a Dubai skyline",
        draw_bim,
        "BIM LAYERS",
    ),
    "ifc-openbim-workflow-dubai-bim-submissions": (
        "Building model exported to an IFC file with unit, classification and coordinate checks",
        draw_ifc,
        "IFC EXPORT",
    ),
    "navisworks-clash-detection-uae-coordination": (
        "Clash detection view of a duct crossing a pipe, with the overlap marked",
        draw_clash,
        "CLASH DETECTION",
    ),
    "slab-nesting-cutting-lists-gulf": (
        "Marble slab nesting layout beside a cutting-list quantity sheet",
        draw_nesting,
        "SLAB NESTING",
    ),
    "chaos-vantage-realtime-ray-tracing-vray": (
        "Ray-traced 3D interior with a camera sending light rays into the room",
        draw_render,
        "RAY TRACE",
    ),
    "stone-staircase-shop-drawings-treads-risers": (
        "Stone stair section showing treads, risers, a stringer and fixing points",
        draw_stair,
        "TREAD · RISER",
    ),
    "marble-flooring-wall-cladding-shop-drawings": (
        "Marble floor tile layout and a bookmatched wall cladding elevation",
        draw_floor_wall,
        "FLOOR + WALL",
    ),
    "what-are-marble-shop-drawings": (
        "Annotated marble shop drawing with a slab plan, sink cut-out, dimensions and title block",
        draw_shop,
        "SHOP DRAWING",
    ),
    "marble-shop-drawings-checklist-uae": (
        "Marble shop-drawing checklist with piece, edge, joint and thickness items ticked",
        draw_checklist,
        "CHECKLIST",
    ),
    "autocad-2026-new-features-smart-blocks-ai": (
        "AutoCAD Smart Block door with grip points and an AI assist spark",
        draw_smart_blocks,
        "SMART BLOCK",
    ),
    "autocad-architecture-toolset-uae-floor-plans": (
        "Architectural floor plan with walls, a door swing and existing versus new work",
        draw_floor_plan,
        "FLOOR PLAN",
    ),
    "autocad-drafting-standards-gulf-fitout": (
        "CAD layer standards list beside a fit-out plan drawn on named layers",
        draw_standards,
        "LAYER STANDARD",
    ),
    "draftsight-dwg-drafting-trial-guide": (
        "2D DWG drafting workspace with a floor plan and a command line",
        draw_draftsight,
        "DWG DRAFTING",
    ),
    "autodesk-forma-site-design-ai-planning": (
        "Site massing options with a sun path and wind arrows for early planning",
        draw_forma,
        "SITE PLANNING",
    ),
    "build-in-dubai-drawing-package-tips": (
        "Permit drawing package of stacked sheets with a review check",
        draw_permit,
        "PERMIT SET",
    ),
    "primavera-p6-vs-microsoft-project-uae-fit-out": (
        "Side-by-side fit-out schedules, a linked P6 programme and a simpler bar chart",
        draw_p6,
        "P6 · MSP",
    ),
    "marble-shop-drawings-vs-fabrication-drawings": (
        "Side-by-side marble drawings: an approved shop layout and a numbered fabrication piece with a sink cut-out",
        draw_shop_vs_fab,
        "SHOP · FAB",
    ),
    "marble-slab-allocation-cutting-optimization": (
        "Marble slab layout with numbered pieces, a saw kerf, continuous vein matching and a book-matched pair",
        draw_allocation,
        "SLAB LAYOUT",
    ),
}


def upsert_front_matter(slug: str, alt: str) -> None:
    path = POSTS / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        raise SystemExit(f"Missing front matter: {path}")
    fields = {
        "image": f"/assets/img/blog/{slug}.svg",
        "og_image": f"/assets/img/blog/{slug}.jpg",
        "image_alt": alt,
    }
    lines = match.group(1).splitlines()
    seen = set()
    rewritten = []
    for line in lines:
        key = line.split(":", 1)[0].strip() if ":" in line else ""
        if key in fields:
            value = fields[key]
            if key == "image_alt":
                rewritten.append(f'{key}: "{value}"')
            else:
                rewritten.append(f"{key}: {value}")
            seen.add(key)
        else:
            rewritten.append(line)
    for key, value in fields.items():
        if key not in seen:
            if key == "image_alt":
                rewritten.append(f'{key}: "{value}"')
            else:
                rewritten.append(f"{key}: {value}")
    tail = text[match.end():]
    if match.group(0).endswith("\n\n") and not tail.startswith("\n"):
        tail = "\n" + tail
    new = "---\n" + "\n".join(rewritten) + "\n---\n" + tail
    if new != text:
        path.write_text(new, encoding="utf-8")


def rasterize(svg: str, dest: Path) -> None:
    import io
    import cairosvg
    from PIL import Image

    png = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=1200, output_height=630)
    image = Image.open(io.BytesIO(png)).convert("RGB")
    image.save(dest, "JPEG", quality=78, optimize=True, progressive=True, subsampling=0)
    if dest.stat().st_size > 120_000:
        image.save(dest, "JPEG", quality=62, optimize=True, progressive=True, subsampling=1)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, (alt, draw, label) in COVERS.items():
        svg = cover(alt, draw(), label)
        svg_path = OUT / f"{slug}.svg"
        jpg_path = OUT / f"{slug}.jpg"
        svg_path.write_text(svg, encoding="utf-8")
        if svg_path.stat().st_size > 40_000:
            raise SystemExit(f"{svg_path.name} is {svg_path.stat().st_size} bytes")
        rasterize(svg, jpg_path)
        upsert_front_matter(slug, alt)
        print(f"{slug}: svg {svg_path.stat().st_size}  jpg {jpg_path.stat().st_size}")


if __name__ == "__main__":
    main()

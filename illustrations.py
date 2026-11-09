# Inline line illustrations for the homepage. Strokes and fills use the
# CSS theme variables in assets/style.css only. No external image files.

def _svg(label, body, vb="0 0 400 300"):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + vb + '" role="img" '
        'fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
        "<title>" + label + "</title>" + body + "</svg>"
    )


def _t(x, y, text, anchor="middle", fill="var(--muted)", size=12):
    return (
        '<text x="%g" y="%g" text-anchor="%s" fill="%s" font-size="%g">%s</text>'
        % (x, y, anchor, fill, size, text)
    )


def svg_design():
    body = (
        '<rect x="22" y="28" width="196" height="214" rx="3" stroke="var(--line)"/>'
        '<rect x="40" y="52" width="160" height="148" stroke="var(--ink)"/>'
        '<path d="M40 118 H200 M112 52 V200" stroke="var(--muted)"/>'
        '<path d="M40 96 V118" stroke="var(--gold2)"/>'
        '<path d="M40 96 A22 22 0 0 1 62 118" stroke="var(--gold2)" stroke-width="1.2"/>'
        '<path d="M62 52 V64 M88 52 V64 M136 52 V64 M168 52 V64" stroke="var(--gold2)" stroke-width="1.2"/>'
        '<circle cx="72" cy="84" r="13" stroke="var(--gold2)" stroke-width="1.2"/>'
        '<rect x="132" y="140" width="46" height="28" rx="2" stroke="var(--muted)"/>'
        '<path d="M40 214 H200" stroke="var(--muted)" stroke-width="1.1"/>'
        '<path d="M40 208 V220 M200 208 V220" stroke="var(--muted)" stroke-width="1.1"/>'
        '<path d="M186 46 V70" stroke="var(--gold)"/>'
        '<path d="M186 46 l-4.5 8 h9 Z" fill="var(--gold)" stroke="none"/>'
        + _t(186, 84, "N", fill="var(--gold2)", size=11)
        + _t(120, 248, "FLOOR PLAN", size=11)
        + '<path d="M248 214 H386" stroke="var(--line)"/>'
        '<rect x="262" y="124" width="112" height="90" stroke="var(--ink)"/>'
        '<path d="M250 124 L318 70 L386 124" stroke="var(--gold)"/>'
        '<rect x="278" y="146" width="20" height="26" stroke="var(--gold2)"/>'
        '<rect x="338" y="146" width="20" height="26" stroke="var(--gold2)"/>'
        '<path d="M304 214 V176 H332 V214" stroke="var(--muted)"/>'
        + _t(318, 248, "ELEVATION", size=11)
    )
    return _svg("Building elevation and floor plan", body)


def svg_draft():
    body = (
        '<rect x="20" y="18" width="360" height="264" rx="3" stroke="var(--ink)"/>'
        '<rect x="30" y="28" width="340" height="244" stroke="var(--line)"/>'
        '<path d="M30 56 H370" stroke="var(--line)"/>'
        + _t(48, 48, "SHOP DWG  ·  A-101", anchor="start", fill="var(--gold2)", size=13)
        + '<rect x="52" y="76" width="148" height="96" stroke="var(--gold)"/>'
        '<path d="M52 124 H200 M118 76 V172" stroke="var(--muted)"/>'
        '<path d="M52 172 V206 M200 172 V206" stroke="var(--muted)" stroke-width="1.1"/>'
        '<path d="M52 198 H96 M156 198 H200" stroke="var(--gold2)"/>'
        '<path d="M52 198 l8 -3.5 M52 198 l8 3.5 M200 198 l-8 -3.5 M200 198 l-8 3.5" stroke="var(--gold2)"/>'
        + _t(126, 194, "4 200", fill="var(--gold2)", size=12)
        + '<path d="M200 76 H222 M200 172 H222" stroke="var(--muted)" stroke-width="1.1"/>'
        '<path d="M214 76 V108 M214 140 V172" stroke="var(--gold2)"/>'
        '<path d="M214 76 l-3.5 8 M214 76 l3.5 8 M214 172 l-3.5 -8 M214 172 l3.5 -8" stroke="var(--gold2)"/>'
        + _t(228, 128, "2 800", anchor="start", fill="var(--gold2)", size=12)
        + '<rect x="248" y="168" width="108" height="86" stroke="var(--muted)"/>'
        '<path d="M248 190 H356 M248 212 H356 M248 232 H356" stroke="var(--line)"/>'
        + _t(302, 184, "TITLE", size=11)
        + _t(278, 206, "DWG", anchor="start", fill="var(--gold2)", size=12)
        + _t(328, 206, "PDF", anchor="start", fill="var(--ink)", size=12)
    )
    return _svg("CAD sheet with dimension lines", body)


def svg_marble():
    body = (
        '<rect x="36" y="46" width="250" height="168" rx="2" stroke="var(--ink)"/>'
        '<path d="M36 130 H286" stroke="var(--muted)"/>'
        '<path d="M120 46 V214 M200 46 V214" stroke="var(--line)"/>'
        '<path d="M56 78 C90 60 110 110 150 86 C190 62 210 108 250 84" stroke="var(--gold2)" stroke-width="1.2"/>'
        '<path d="M70 160 C110 140 130 188 176 164 C214 144 240 186 270 168" stroke="var(--gold2)" stroke-width="1.1"/>'
        '<ellipse cx="158" cy="96" rx="28" ry="18" stroke="var(--gold)"/>'
        '<path d="M36 232 H286" stroke="var(--muted)" stroke-width="1.1"/>'
        '<path d="M36 226 V238 M286 226 V238" stroke="var(--muted)" stroke-width="1.1"/>'
        + _t(161, 228, "2 400", fill="var(--gold2)", size=12)
        + '<path d="M310 70 H360 V150" stroke="var(--muted)"/>'
        '<path d="M310 70 q18 8 18 28" stroke="var(--gold2)"/>'
        + _t(336, 176, "EDGE", size=11)
        + _t(161, 268, "SLAB LAYOUT", size=11)
    )
    return _svg("Marble slab layout with a sink cut-out", body)


def svg_estimate():
    rows = [(78, "Floor", "86", "m²"), (110, "Cladding", "42", "m²"), (142, "Vanity", "2", "no."), (174, "Skirting", "38", "m")]
    lines = [
        '<rect x="24" y="32" width="214" height="228" rx="3" stroke="var(--ink)"/>',
        '<rect x="24" y="32" width="214" height="34" fill="var(--gold)" fill-opacity="0.16" stroke="none"/>',
        '<path d="M24 66 H238 M24 98 H238 M24 130 H238 M24 162 H238 M24 194 H238" stroke="var(--line)"/>',
        '<path d="M128 32 V260 M188 32 V260" stroke="var(--line)"/>',
        _t(76, 54, "ITEM", fill="var(--gold2)", size=11),
        _t(158, 54, "QTY", fill="var(--gold2)", size=11),
        _t(212, 54, "UNIT", fill="var(--gold2)", size=11),
    ]
    for y, item, qty, unit in rows:
        lines.append(_t(36, y, item, anchor="start", fill="var(--ink)", size=13))
        lines.append(_t(158, y, qty, fill="var(--ink)", size=13))
        lines.append(_t(212, y, unit, fill="var(--muted)", size=12))
    lines.append(_t(76, 224, "BOQ", fill="var(--gold2)", size=12))
    lines.append('<rect x="258" y="78" width="118" height="156" rx="12" stroke="var(--gold)"/>')
    lines.append('<rect x="272" y="92" width="90" height="26" rx="4" stroke="var(--gold2)"/>')
    lines.append(_t(316, 110, "1,284", fill="var(--gold2)", size=13))
    for r in range(4):
        for c in range(3):
            x = 274 + c * 32
            y = 132 + r * 22
            lines.append('<rect x="%d" y="%d" width="24" height="16" rx="3" stroke="var(--muted)" stroke-width="1.1"/>' % (x, y))
    return _svg("Bill of quantities and a calculator", "".join(lines))


def svg_viz():
    body = (
        '<path d="M46 168 L138 124 L230 168 L138 212 Z" stroke="var(--ink)"/>'
        '<path d="M46 168 L46 96 L138 52 L138 124 Z" stroke="var(--gold)"/>'
        '<path d="M138 124 L138 52 L230 96 L230 168 Z" stroke="var(--gold)"/>'
        '<path d="M78 168 L138 140 L198 168 L138 196 Z" stroke="var(--muted)" stroke-width="1.1"/>'
        '<path d="M60 162 L81 151 L81 112 L60 122 Z" stroke="var(--gold2)"/>'
        '<path d="M186 89 L213 102 L213 130 L186 117 Z" stroke="var(--gold2)"/>'
        '<path d="M199.5 95.5 V123.5" stroke="var(--gold2)" stroke-width="1.1"/>'
        '<path d="M268 110 L310 88 L352 110 L310 132 Z" stroke="var(--ink)"/>'
        '<path d="M268 110 L268 162 L310 184 L310 132" stroke="var(--gold)"/>'
        '<path d="M310 132 L310 184 L352 162 L352 110" stroke="var(--gold)"/>'
        '<path d="M268 162 L310 140 L352 162 M310 140 V88" stroke="var(--muted)" stroke-width="1.15" stroke-dasharray="3 3"/>'
        + _t(138, 248, "ISOMETRIC ROOM", size=11)
        + _t(310, 214, "WIREFRAME", size=11)
    )
    return _svg("Isometric room and wireframe cube", body)


def svg_uae():
    # Coastline and borders from the public-domain simplified UAE polygon
    # (lon/lat), drawn with an equirectangular projection. City dots sit on land.
    land = (
        "M57.8,197.0 L71.7,192.8 L74.6,216.4 L135.6,202.8 L200.1,205.1 "
        "L247.2,207.6 L300.7,149.5 L358.8,94.3 L408.1,41.3 L423.0,70.6 "
        "L433.6,138.6 L393.7,138.9 L387.3,194.9 L401.1,206.9 L365.8,223.8 "
        "L365.6,258.9 L342.9,294.5 L340.9,329.2 L325.1,347.3 L90.7,304.0 L60.8,216.9 Z"
    )
    labels = [
        (242, 52, "Ras Al Khaimah", "end"),
        (242, 76, "Umm Al Quwain", "end"),
        (242, 100, "Ajman", "end"),
        (242, 124, "Sharjah", "end"),
        (242, 148, "Dubai", "end"),
        (292, 206, "Abu Dhabi", "start"),
        (448, 124, "Fujairah", "start"),
    ]
    dots = [
        (398.2, 64.2),
        (367.9, 85.2),
        (364.7, 97.2),
        (356.1, 102.3),
        (345.7, 114.5),
        (276.0, 179.0),
        (429.2, 121.0),
    ]
    leaders = (
        '<g fill="none" stroke="var(--muted)" stroke-width="0.8">'
        '<path d="M248 48 H360 L398.2 64.2"/>'
        '<path d="M248 72 H332 L367.9 85.2"/>'
        '<path d="M248 96 H332 L364.7 97.2"/>'
        '<path d="M248 120 H322 L356.1 102.3"/>'
        '<path d="M248 144 H312 L345.7 114.5"/>'
        '<path d="M286 196 L276 182"/>'
        '<path d="M444 120 H433"/>'
        "</g>"
    )
    parts = [
        '<path d="' + land + '" fill="var(--gold)" fill-opacity="0.16" stroke="var(--gold)" stroke-width="1.7"/>',
        leaders,
    ]
    for x, y in dots:
        parts.append(
            '<circle cx="%g" cy="%g" r="3.3" fill="var(--gold)" stroke="var(--card)" stroke-width="1.4"/>' % (x, y)
        )
    for x, y, name, anchor in labels:
        parts.append(_t(x, y, name, anchor=anchor, fill="var(--ink)", size=13))
    return _svg(
        "Map of the United Arab Emirates marking Abu Dhabi, Dubai, Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah and Fujairah",
        "".join(parts),
        "0 0 540 372",
    )


def svg_cut():
    body = (
        '<rect x="36" y="48" width="250" height="176" rx="2" stroke="var(--ink)"/>'
        '<path d="M52 86 C100 64 120 120 168 92 C210 68 230 118 268 96" stroke="var(--gold2)" stroke-width="1.2"/>'
        '<path d="M48 150 C96 132 130 176 180 154 C220 136 246 178 274 162" stroke="var(--gold2)" stroke-width="1.1"/>'
        '<path d="M120 48 V224 M196 48 V224 M36 136 H286" stroke="var(--gold)" stroke-dasharray="5 4"/>'
        + _t(78, 100, "01", fill="var(--gold2)", size=13)
        + _t(158, 100, "02", fill="var(--gold2)", size=13)
        + _t(240, 100, "03", fill="var(--gold2)", size=13)
        + _t(78, 186, "04", fill="var(--gold2)", size=13)
        + _t(158, 186, "05", fill="var(--gold2)", size=13)
        + _t(240, 186, "06", fill="var(--gold2)", size=13)
        + '<circle cx="330" cy="96" r="36" stroke="var(--gold)" fill="var(--gold)" fill-opacity="0.12"/>'
        '<path d="M312 96 l12 13 l26 -28" stroke="var(--gold2)" stroke-width="2.6"/>'
        + _t(161, 268, "CUT FROM THE APPROVED SET", size=11)
    )
    return _svg("Stone slab with cut lines and a check mark, before fabrication", body)


def svg_delivered():
    body = (
        '<rect x="78" y="36" width="230" height="188" rx="3" stroke="var(--line)"/>'
        '<rect x="58" y="52" width="230" height="188" rx="3" stroke="var(--muted)"/>'
        '<rect x="36" y="70" width="236" height="190" rx="3" stroke="var(--ink)" fill="var(--card)"/>'
        '<path d="M36 98 H272" stroke="var(--line)"/>'
        + _t(52, 90, "PDF", anchor="start", fill="var(--gold2)", size=13)
        + _t(210, 90, "DWG", anchor="start", fill="var(--ink)", size=13)
        + '<rect x="56" y="116" width="120" height="78" stroke="var(--gold)"/>'
        '<path d="M56 150 H176 M108 116 V194" stroke="var(--muted)"/>'
        '<path d="M190 124 H252 M190 142 H244 M190 160 H252 M190 178 H230" stroke="var(--muted)" stroke-width="1.2"/>'
        '<path d="M56 214 H176" stroke="var(--gold2)" stroke-width="1.1"/>'
        '<path d="M56 208 V220 M176 208 V220" stroke="var(--gold2)" stroke-width="1.1"/>'
        + _t(154, 252, "ISSUED SET", fill="var(--muted)", size=11)
    )
    return _svg("Stacked drawing sheets marked PDF and DWG", body)


def svg_review():
    body = (
        '<rect x="28" y="40" width="168" height="200" rx="3" stroke="var(--ink)"/>'
        '<path d="M28 66 H196" stroke="var(--line)"/>'
        + _t(44, 58, "REV A", anchor="start", fill="var(--gold2)", size=12)
        + '<rect x="46" y="84" width="120" height="78" stroke="var(--muted)"/>'
        '<path d="M46 118 H166 M100 84 V162" stroke="var(--line)"/>'
        '<circle cx="124" cy="108" r="16" stroke="var(--gold2)" stroke-width="1.3"/>'
        '<path d="M58 150 H150" stroke="var(--gold2)" stroke-width="1.3"/>'
        '<path d="M150 150 l-8 -4 M150 150 l-8 4" stroke="var(--gold2)"/>'
        '<path d="M206 130 H248" stroke="var(--gold)"/>'
        '<path d="M248 130 l-10 -5 M248 130 l-10 5" stroke="var(--gold)"/>'
        '<circle cx="312" cy="130" r="48" stroke="var(--gold)" stroke-width="1.8"/>'
        '<circle cx="312" cy="130" r="40" stroke="var(--gold2)" stroke-width="1.1"/>'
        + _t(312, 126, "APPROVED", fill="var(--gold2)", size=11)
        + _t(312, 142, "REV B", fill="var(--ink)", size=11)
        + '<circle cx="70" cy="268" r="4" fill="var(--gold)" stroke="none"/>'
        '<circle cx="168" cy="268" r="4" fill="var(--muted)" stroke="var(--gold)"/>'
        '<circle cx="312" cy="268" r="4" fill="var(--gold)" stroke="none"/>'
        '<path d="M78 268 H160 M176 268 H304" stroke="var(--line)"/>'
        + _t(70, 288, "SUBMIT", size=10)
        + _t(168, 288, "REDLINE", size=10)
        + _t(312, 288, "APPROVE", size=10)
    )
    return _svg("Shop drawing with markup and an approval stamp", body)


def svg_turnaround():
    body = (
        '<circle cx="118" cy="118" r="70" stroke="var(--ink)"/>'
        '<circle cx="118" cy="118" r="3" fill="var(--gold)" stroke="none"/>'
        '<path d="M118 58 V66 M118 170 V178 M58 118 H66 M170 118 H178" stroke="var(--muted)" stroke-width="1.2"/>'
        '<path d="M118 118 L96 96" stroke="var(--gold)" stroke-width="2"/>'
        '<path d="M118 118 L164 96" stroke="var(--gold2)" stroke-width="1.6"/>'
        + _t(118, 48, "12", fill="var(--muted)", size=11)
        + _t(118, 196, "6", fill="var(--muted)", size=11)
        + '<path d="M40 236 H360" stroke="var(--line)"/>'
        '<circle cx="70" cy="236" r="6" fill="var(--card)" stroke="var(--gold)"/>'
        '<circle cx="200" cy="236" r="7" fill="var(--gold)" stroke="var(--gold)"/>'
        '<circle cx="330" cy="236" r="6" fill="var(--card)" stroke="var(--gold)"/>'
        + _t(70, 262, "QUOTE", size=11)
        + _t(200, 262, "DRAFT", fill="var(--gold2)", size=11)
        + _t(330, 262, "ISSUE", size=11)
    )
    return _svg("Clock and a quote, draft, issue timeline", body)


def svg_next():
    body = (
        '<path d="M48 196 C 96 196, 108 92, 164 92 S 230 196, 286 150" stroke="var(--gold)"/>'
        '<path d="M286 150 l-12 -4 M286 150 l-4 -12" stroke="var(--gold)" stroke-width="1.6"/>'
        '<circle cx="48" cy="196" r="7" fill="var(--gold)" stroke="var(--card)" stroke-width="1.5"/>'
        '<circle cx="164" cy="92" r="7" fill="var(--card)" stroke="var(--gold)" stroke-width="1.6"/>'
        '<circle cx="286" cy="150" r="7" fill="var(--gold)" stroke="var(--card)" stroke-width="1.5"/>'
        + _t(48, 224, "DRAWINGS", size=11)
        + _t(164, 72, "QUOTE", fill="var(--gold2)", size=11)
        + _t(286, 176, "CONTACT", fill="var(--gold2)", size=11)
        + '<rect x="312" y="112" width="64" height="44" rx="4" stroke="var(--ink)"/>'
        '<path d="M312 112 L344 138 L376 112" stroke="var(--gold2)"/>'
        + _t(344, 178, "ENQUIRY", size=11)
    )
    return _svg("Path from the drawings to the enquiry form", body)

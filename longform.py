# Longer page copy for the homepage, marble page and /services/ pages.
# Imported by content.py and service_pages.py. No invented prices, clients or regulations.
from illustrations import svg_cut, svg_delivered, svg_review, svg_turnaround, svg_next

def _a(href, text, en=False):
    extra = ' lang="en" dir="ltr"' if en else ""
    return '<a href="%s"%s>%s</a>' % (href, extra, text)

def _ul(items):
    return "<ul>" + "".join("<li>%s</li>" % item for item in items) + "</ul>"


def _guide(rows):
    # rows: (heading, svg, inner html). Illustration beside the copy on desktop.
    parts = ['<section class="section" id="guide"><div class="wrap guide-list">']
    for i, (title, svg, inner) in enumerate(rows):
        flip = " guide-flip" if i % 2 else ""
        parts.append(
            '<article class="split guide-row%s"><figure class="illu">%s</figure>'
            '<div class="copy"><h2>%s</h2>%s</div></article>' % (flip, svg, title, inner)
        )
    parts.append("</div></section>")
    return "".join(parts)


def _html(blocks):
    parts = ['<section class="section" id="guide"><div class="wrap copy">']
    for block in blocks:
        kind = block[0]
        if kind == "h":
            parts.append("<h2>%s</h2>" % block[1])
        elif kind == "h3":
            parts.append("<h3>%s</h3>" % block[1])
        elif kind == "p":
            parts.append("<p>%s</p>" % block[1])
        elif kind == "ul":
            parts.append("<ul>" + "".join("<li>%s</li>" % item for item in block[1]) + "</ul>")
        elif kind == "ol":
            parts.append('<ol class="steps mt-14">' + "".join("<li>%s</li>" % item for item in block[1]) + "</ol>")
    parts.append("</div></section>")
    return "".join(parts)

def _links(lang, here, root):
    en = lang == "en"
    proj = lambda slug, title: _a(root("projects/%s/" % slug), title, en=not en)
    blog = lambda slug, title: _a(root("blog/%s/" % slug), title, en=not en)
    return {
        "home": _a(here(""), "Home" if en else "الرئيسية"),
        "services": _a(here("services/"), "all services" if en else "كل الخدمات"),
        "marble": _a(here("marble.html"), "marble and stone shop drawings" if en else "رسومات الرخام والحجر"),
        "draft": _a(here("services/architectural-drafting/"), "architectural drafting" if en else "الرسم المعماري التنفيذي"),
        "design": _a(here("services/architectural-designing/"), "architectural designing" if en else "التصميم المعماري"),
        "estim": _a(here("services/architectural-estimation/"), "architectural estimation" if en else "حساب الكميات"),
        "viz": _a(here("services/3d-rendering-modeling-visualization/"), "3D rendering" if en else "التصميم ثلاثي الأبعاد"),
        "web": _a(here("services/website-development-designing/"), "website development" if en else "تطوير المواقع"),
        "webpkg": _a(here("website-design.html"), "website packages" if en else "باقات المواقع"),
        "projects": _a(here("projects/"), "projects" if en else "المشاريع"),
        "about": _a(here("about.html"), "about the studio" if en else "من نحن"),
        "contact": _a(here("contact.html"), "enquiry form" if en else "نموذج الاستفسار"),
        "blog": _a(root("blog/"), "blog" if en else "المدونة", en=not en),
        "b_what": blog("what-are-marble-shop-drawings/", "What are marble shop drawings?" if en else "ما هي رسومات الرخام التنفيذية؟"),
        "b_check": blog("marble-shop-drawings-checklist-uae/", "UAE marble shop-drawing checklist" if en else "قائمة مراجعة رسومات الرخام"),
        "b_slab": blog("slab-nesting-cutting-lists-gulf/", "slab nesting and cutting lists" if en else "توزيع الألواح وقوائم القص"),
        "b_stair": blog("stone-staircase-shop-drawings-treads-risers/", "stone staircase shop drawings" if en else "رسومات درج الحجر"),
        "b_std": blog("autocad-drafting-standards-gulf-fitout/", "AutoCAD standards for Gulf fit-out" if en else "معايير أوتوكاد للتشطيب"),
        "b_dubai": blog("build-in-dubai-drawing-package-tips/", "drawing-package notes for Dubai" if en else "ملاحظات باقة المخططات في دبي"),
        "b_bim": blog("dubai-bim-mandate-2026-submission-guide/", "Dubai BIM submission notes" if en else "ملاحظات تسليم BIM في دبي"),
        "p_lobby": proj("entrance-lobby-waterjet-marble-medallion-flooring/", "entrance lobby waterjet medallion"),
        "p_floor": proj("villa-ground-floor-marble-flooring-layout/", "villa ground-floor flooring layout"),
        "p_pool": proj("villa-swimming-pool-and-outdoor-majlis-tiling-details/", "pool and outdoor majlis tiling"),
        "p_bath": proj("luxury-bathroom-marble-cladding-shop-drawings/", "bathroom marble cladding"),
        "p_vanity": proj("venatino-marble-bath-vanity-shop-drawing/", "Venatino bath vanity"),
        "p_paon": proj("paonazzetto-marble-vanity-tops-shop-drawings/", "Paonazzetto vanity tops"),
        "p_nest": proj("marble-slab-cutting-layout-bathroom-cladding/", "bathroom slab nesting"),
        "p_door": proj("fusion-blue-marble-door-frame-and-skirting-slab-layout/", "Fusion Blue door frames and skirting"),
        "fitout": _a(root("fitout-shop-drawings/"), "Fit-out and joinery shop drawings" if en else "رسومات الفيت آوت والنجارة"),
        "estim_boq": _a(here("services/architectural-estimation/"), "Quantity estimation and BOQ" if en else "حساب الكميات"),
        "estim_name": _a(here("services/architectural-estimation/"), "estimation and BOQ" if en else "حساب الكميات"),
        "estim_word": _a(here("services/architectural-estimation/"), "estimation" if en else "حساب الكميات"),
        "viz_model": _a(here("services/3d-rendering-modeling-visualization/"), "3D modeling and rendering" if en else "التصميم ثلاثي الأبعاد"),
        "viz_named": _a(here("services/3d-rendering-modeling-visualization/"), "3D rendering and modeling" if en else "التصميم ثلاثي الأبعاد"),
        "contact_form": _a(here("contact.html"), "contact form" if en else "نموذج الاستفسار"),
        "marble_cap": _a(here("marble.html"), "Marble and stone shop drawings" if en else "رسومات الرخام والحجر"),
        "marble_shop": _a(here("marble.html"), "marble shop drawings" if en else "رسومات الرخام"),
        "draft_shop": _a(here("services/architectural-drafting/"), "shop drawings" if en else "الرسومات التنفيذية"),
        "pool_set": proj("villa-swimming-pool-and-outdoor-majlis-tiling-details/", "villa swimming pool and outdoor seating tiling set"),
        "floor_lux": proj("villa-ground-floor-marble-flooring-layout/", "luxury villa ground-floor flooring layout"),
        "bath_short": proj("luxury-bathroom-marble-cladding-shop-drawings/", "bathroom cladding"),
        "b_std_full": blog("autocad-drafting-standards-gulf-fitout/", "AutoCAD drafting standards for Gulf fit-out"),
        "b_marble_qty": blog("marble-quantity-calculation-reduce-waste/", "How to calculate marble quantities and reduce waste"),
        "b_drafting": blog("architectural-drafting-services-uae/", "architectural drafting services in the UAE"),
        "b_concept": blog("concept-drawings-vs-construction-drawings/", "concept drawings versus construction drawings"),
        "b_takeoff": blog("what-is-a-quantity-takeoff/", "what a quantity take-off is"),
        "b_boqdiff": blog("boq-vs-estimation-vs-quotation/", "how a BOQ differs from an estimate and a quotation"),
        "b_rmodel": blog("3d-rendering-vs-3d-modeling/", "how 3D rendering differs from 3D modeling"),
        "b_vizok": blog("3d-visualization-uae-interior-approvals/", "how 3D visualization helps interior approvals"),
    }

def home_bundle(lang, here, root):
    L = _links(lang, here, root)
    if lang == "en":
        html = _guide([
            (
                "Why shop drawings matter before anything is cut",
                svg_cut(),
                "<p>Shop drawings name every piece, joint, thickness, edge and cut-out before stone is cut in Dubai, Abu Dhabi, Sharjah and the UAE. Send drawings through the %s; scope, price and date are confirmed in writing, and only website packages have published prices.</p>" % L["contact"],
            ),
            (
                "What a delivered set contains",
                svg_delivered(),
                _ul([
                    "DWG and PDF shop drawings for Dubai, Abu Dhabi, Sharjah and the UAE: plans, elevations, sections, joints, edges and cut-outs.",
                    "Piece marks, a cutting list or bill of quantities, and a revision table.",
                    "Notes in English, Arabic, or both.",
                ]),
            ),
            (
                "How consultant review usually works in Dubai, Abu Dhabi and Sharjah",
                svg_review(),
                "<p>In Dubai, Abu Dhabi and Sharjah the contractor submits shop drawings to the consultant; comments return on the PDF and fabrication waits for the revised approval. A shop drawing is not a permit.</p>"
                "<p>Title block and copies follow your project checklist. Notes are on the %s, including %s and %s.</p>" % (L["blog"], L["b_dubai"], L["b_bim"]),
            ),
            (
                "Turnaround",
                svg_turnaround(),
                "<p>Shop-drawing turnaround in Dubai, Abu Dhabi, Sharjah and the UAE is the date in the written quote. Comment rounds start when the comments arrive, and a missing site size pauses only that sheet.</p>",
            ),
            (
                "Where to go next",
                svg_next(),
                "<p>For shop drawings, see %s, %s, %s, %s and %s. Websites with published prices: %s and %s.</p>"
                "<p>Dubai villa sheets are in the %s: %s, %s, %s and %s. Read %s or the %s.</p>"
                % (L["marble"], L["draft"], L["design"], L["estim"], L["viz"], L["web"], L["webpkg"],
                   L["projects"], L["p_bath"], L["p_floor"], L["p_nest"], L["p_vanity"], L["b_what"], L["b_check"]),
            ),
        ])
        faqs = [
            ("Why do shop drawings matter before stone is cut?", "They freeze piece sizes, joints, thickness, edges and cut-outs while the material can still be nested. Once a slab is cut, a wrong opening or a vein running the wrong way is a replacement, not a pencil correction."),
            ("How does consultant approval usually work in Dubai, Abu Dhabi and Sharjah?", "The contractor submits the shop drawings to the project’s consultant — architect, interior designer or engineer, as the contract names them. Comments come back on the PDF or as a list. The sheets are revised, the revision is raised, and the set is resubmitted until that reviewer approves it for fabrication. Requirements differ by project. Send any checklist you have been given. A shop drawing is not a permit."),
            ("How is turnaround agreed?", "With the quote, in writing, before drafting starts. The date depends on the number of areas, how complete the source drawings are, and how many comment rounds follow. There is no single public lead time."),
            ("What is in the first issue?", "DWG and PDF sheets covering the agreed scope: plans, elevations, sections and the details needed to fabricate or install. Quantities and slab layouts are included when they are part of the quote. Notes can be in English, Arabic or both."),
            ("Can you start from sketches or site sizes only?", "Yes, if the sketches or measured sizes are enough to draw the scope. Where a dimension is missing, that sheet waits until you send it. Say what you have when you use the enquiry form."),
            ("Do the website prices apply to shop drawings?", "No. Shop drawings, drafting, design and estimation are quoted per project. A single 3D still render is 650 AED, with 50% upfront; other 3D work is quoted per project. Website packages are AED 1,200, AED 2,000 and AED 3,500+, with the 5-page contractor site at AED 2,000 and 50% paid upfront."),
        ]
    else:
        html = _html([
            ("h", "لماذا تهم الرسومات التنفيذية قبل القص"),
            ("p", "المخطط التصميمي يوضح النية: أرضية رخام، جدار حجر، مغسلة، درج. الرسم التنفيذي يوضح كيف تُنفَّذ هذه النية. يسمّي كل قطعة وفاصل وسماكة وحافة وفتحة، وهو اللوحة التي ينظر إليها المصنع وفريق الموقع والاستشاري معاً. في أعمال التشطيب في الإمارات يكون الخطأ هنا مكلفاً. يُطلب الحجر ويُوزَّع على الألواح ويُقص من المجموعة المعتمدة. فتحة مغسلة ناقصة عشرين مليمتراً، أو عرق يجري في الاتجاه الخطأ، أو زاوية لا تطابق الجدار المجاور، ليست تعديلاً سريعاً في الموقع."),
            ("p", "يعدّ D3DDD هذه المجموعات للمقاولين ومصانع الحجر وورش النجارة والاستشاريين ومصممي الديكور في دبي وأبوظبي والشارقة وبقية الإمارات. التسليم رقمي. ترسل المخططات المعمارية أو الداخلية أو الرسومات الأولية أو مقاسات الموقع أو الصور عبر %s، ويُؤكد نطاق العمل والسعر وموعد التسليم كتابياً قبل بدء الرسم. رسومات التنفيذ والرسم والتصميم وحساب الكميات والتصميم ثلاثي الأبعاد تُسعَّر حسب المشروع. الأسعار المنشورة في هذا الموقع هي باقات المواقع فقط." % L["contact"]),
            ("h", "ماذا تحتوي المجموعة المسلَّمة"),
            ("p", "التسليم المعتاد هو ملف أوتوكاد DWG وملف PDF للوحات نفسها. ملف DWG هو ملف العمل: طبقات وأبعاد حقيقية وترقيم قطع يستطيع المصنع الاستمرار عليه. ملف PDF هو ما يعلّق عليه أكثر الاستشاريين وما يُطبع في الموقع. إذا شمل النطاق كميات أو قوائم قص أو جدول كميات، تُرتَّب الجداول بحيث يمكن نقلها إلى جدول بيانات. أعمال التصميم ثلاثي الأبعاد تُسلَّم صوراً عالية الدقة. أي صيغة أخرى تُناقش عند طلب عرض السعر، ولا تُفترض مسبقاً."),
            ("ul", [
                "مساقط وواجهات وقطاعات والتفاصيل المكبرة التي يحتاجها العمل فعلاً.",
                "توزيع الفواصل وشكل الحافة والسماكة والتشطيب والفتحات مثل المغاسل والموقد والمآخذ.",
                "ترقيم قطع يطابق قائمة القص أو مخطط الألواح عند توزيع الحجر.",
                "جدول مراجعات، حتى تكون جولة الملاحظات إصدارًا جديداً لا استبدالاً صامتاً للملف.",
                "ملاحظات بالإنجليزية أو العربية أو باللغتين. اذكر اللغة المطلوبة مع الاستفسار.",
            ]),
            ("h", "كيف تسير مراجعة الاستشاري عادة في دبي وأبوظبي والشارقة"),
            ("p", "في أكثر مشاريع التشطيب في هذه الإمارات الثلاث يقدّم المقاول الرسم التخصصي — الحجر أو النجارة أو المجموعة المعمارية المنسّقة — إلى استشاري المشروع. المراجع هو من تسمّيه الاتفاقية: المعماري أو مصمم الديكور أو المهندس أو أكثر من طرف. تعود الملاحظات على ملف PDF أو على نسخة معلَّمة أو في قائمة ملاحظات. يُعدَّل الرسم وتُحدَّد مواضع التغيير ويُرفع رقم المراجعة ثم تُعاد المجموعة. التصنيع ينتظر حتى يعتمد ذلك المراجع الإصدار الذي طلب رؤيته. D3DDD لا يحل محل الاستشاري، والرسم التنفيذي ليس تصريح بناء."),
            ("p", "ما يختلف بين دبي وأبوظبي والشارقة، ومن مشروع إلى آخر، هو لوحة العنوان وعدد نسخ المراجعة وهل يريد المقاول الرئيسي خطاب إحالة أو قائمة لوحات معينة. لا توجد استمارة وطنية واحدة للرسومات التنفيذية. إذا كان لدى مشروعك قائمة تحقق فأرسلها مع المخططات وستُتبع. مجموعات التصاريح وتسليم نماذج BIM نطاق مختلف عن رسم التصنيع. إذا احتاج المشروع إليهما يُتفق على ذلك على حدة. ملاحظات عن باقات المخططات وعن تسليم BIM في دبي موجودة في %s، ومنها %s و%s." % (L["blog"], L["b_dubai"], L["b_bim"])),
            ("h", "موعد التسليم"),
            ("p", "لا يوجد موعد عام ثابت، لأن مغسلة واحدة ليست كأرضية فيلا. يُكتب موعد التسليم في عرض السعر ويُؤكد قبل بدء الرسم. جولة الملاحظات بعد رد الاستشاري إصدار لاحق يُجدول عند وصول تلك الملاحظات. المقاس الناقص من الموقع يوقف اللوحة المتأثرة إلى أن ترسله. إذا كان الموعد حرجاً فاذكر ذلك في الاستفسار وأرسل ما لديك من مخططات حتى لو كانت رسومات أولية."),
            ("h", "إلى أين بعد ذلك"),
            ("p", "أعمال تصنيع الحجر في صفحة %s. مجموعات أوتوكاد الأوسع تحت %s. المخططات المبكرة في %s، والكميات في %s، وصور العرض في %s. مواقع المقاولين بالأسعار المنشورة بالدرهم تحت %s وصفحة %s." % (L["marble"], L["draft"], L["design"], L["estim"], L["viz"], L["web"], L["webpkg"])),
            ("p", "تعرض %s نوع اللوحات التي أُعدت لفلل في دبي: %s و%s و%s و%s. لقراءة قصيرة قبل إرسال الباقة ابدأ بـ%s أو %s. مقالات المدونة بالإنجليزية." % (L["projects"], L["p_bath"], L["p_floor"], L["p_nest"], L["p_vanity"], L["b_what"], L["b_check"])),
        ])
        faqs = [
            ("لماذا تهم الرسومات التنفيذية قبل قص الحجر؟", "لأنها تثبّت مقاسات القطع والفواصل والسماكات والحواف والفتحات بينما لا يزال يمكن توزيع الحجر على الألواح. بعد القص، الفتحة الخطأ أو اتجاه العرق الخطأ استبدال لا تصحيح بقلم."),
            ("كيف يتم اعتماد الاستشاري عادة في دبي وأبوظبي والشارقة؟", "يقدّم المقاول الرسومات التنفيذية إلى استشاري المشروع، وهو المعماري أو مصمم الديكور أو المهندس حسب ما تسمّيه الاتفاقية. تعود الملاحظات على PDF أو في قائمة. تُعدَّل اللوحات ويُرفع رقم المراجعة وتُعاد حتى يعتمدها ذلك المراجع للتصنيع. المتطلبات تختلف بين المشاريع. أرسل أي قائمة تحقق استلمتها. الرسم التنفيذي ليس تصريحاً."),
            ("كيف يُتفق على موعد التسليم؟", "كتابياً مع عرض السعر وقبل بدء الرسم. يعتمد الموعد على عدد المناطق واكتمال المخططات المصدر وعدد جولات الملاحظات. لا توجد مدة عامة واحدة معلنة."),
            ("ماذا يتضمن الإصدار الأول؟", "لوحات DWG وPDF للنطاق المتفق عليه: مساقط وواجهات وقطاعات والتفاصيل اللازمة للتصنيع أو التركيب. الكميات وتوزيع الألواح تدخل إذا كانت جزءاً من العرض. الملاحظات يمكن أن تكون بالعربية أو الإنجليزية أو باللغتين."),
            ("هل يمكن البدء من رسومات أولية أو مقاسات موقع فقط؟", "نعم إذا كانت كافية لرسم النطاق. حيث ينقص مقاس تتوقف تلك اللوحة حتى ترسله. اذكر ما هو متوفر عند استخدام نموذج الاستفسار."),
            ("هل أسعار المواقع تنطبق على الرسومات التنفيذية؟", "لا. الرسومات التنفيذية والرسم والتصميم وحساب الكميات تُسعَّر حسب المشروع. صورة ثلاثية الأبعاد واحدة بـ650 درهم مع 50% مقدماً، وما زاد من الصور يُسعَّر حسب المشروع. أسعار باقات المواقع: 1,200 و2,000 و3,500+ درهم، وموقع المقاول من 5 صفحات بـ2,000 درهم مع 50% مقدماً."),
        ]
    return html, faqs

def marble_bundle(lang, here, root):
    L = _links(lang, here, root)
    if lang == "en":
        html = _html([
            ("h", "What a marble shop drawing is for"),
            ("p", "Marble and stone shop drawings are the fabrication and installation set for a specific job. They sit between the interior designer’s intent and the bridge saw. A countertop, a vanity, a stair, a bookmatched wall or a floor layout each needs its own information: plan, elevations, sections, edge, thickness, finish, joint, and every cut-out. The %s explains the idea in more detail, and the %s is the short list fabricators actually tick." % (L["b_what"], L["b_check"])),
            ("p", "D3DDD draws these sets in AutoCAD for contractors and stone workshops working in Dubai, Abu Dhabi, Sharjah and across the UAE. The price is quoted per project after the drawings are reviewed. Nothing on this page is a rate card. Send the architectural set, the interior elevations, slab photos or a measured sketch through the %s." % L["contact"]),
            ("h", "Deliverables"),
            ("ul", [
                "Shop drawings: plans, elevations, sections and enlarged details with stone name, thickness, edge and finish.",
                "Fabrication drawings: mitres, tolerances, joints, and the CNC or waterjet notes the workshop asked for.",
                "Cutting lists and slab layouts that follow the vein, including bookmatching where the design depends on it.",
                "Quantity take-off and an Excel-ready summary when estimation is part of the quote.",
                "DWG plus PDF, with a revision table. Arabic notes on request, alongside or instead of English.",
            ]),
            ("h", "File formats"),
            ("p", "DWG is the file the factory keeps. PDF is the file the consultant marks and the site prints. If the quote includes a cutting list or a bill of quantities, that schedule is laid out for a spreadsheet. Renderings of a feature, when they are part of the same job, are images, not a substitute for the measured sheets. If a workshop needs a particular layer name or a title block, send a sample and the set will follow it."),
            ("h", "From enquiry to installation"),
            ("ol", [
                "Send the design drawings, sizes and any slab photos.",
                "The scope, price and delivery date are confirmed in writing.",
                "The first issue goes out as DWG and PDF.",
                "You, the fabricator or the consultant comment.",
                "The revision is issued, then the workshop cuts and the site installs.",
            ]),
            ("p", "Turnaround is the date in that written quote. A pair of vanities is a smaller set than a villa ground floor with waterjet and bookmatched walls. A consultant’s comment round is another issue, not a surprise rewrite of the fee, and it is timed when the comments arrive. If a site size is still open, that sheet is flagged and left until the size is known."),
            ("h", "Consultant review, in general terms"),
            ("p", "In Dubai, Abu Dhabi and Sharjah the stone shop drawings are usually one package inside the contractor’s submission to the project consultant. The reviewer checks them against the interior elevations: joint positions, edge profiles, splash heights, niche sizes, and how the stone meets joinery, glass and sanitaryware. Comments return on the PDF. The revised issue carries a new revision number so the factory does not cut from a superseded sheet. Some projects want a transmittal and a fixed title block; some only want the PDF by email. Send whatever rule your project already uses. D3DDD does not invent an authority submission, and these drawings are not a permit set. If the same project also needs coordinated architectural sheets, that work sits under %s." % L["draft"]),
            ("p", "Staircases need tread, riser and fixing information that a floor plan will not carry. The note on %s walks through that kind of sheet. Slab nesting — which piece comes from which slab so the vein continues — is covered in %s." % (L["b_stair"], L["b_slab"])),
            ("h", "Work you can look at"),
            ("p", "The %s are real sheets with client marks removed: %s, %s, %s, %s, %s and %s. Floor layouts such as %s and external work such as %s show the same drafting habit on a larger plan. If the job is still at concept stage, %s and %s can sit alongside the shop drawings so the client sees the material before it is approved for cutting." % (L["projects"], L["p_bath"], L["p_vanity"], L["p_paon"], L["p_nest"], L["p_door"], L["p_lobby"], L["p_floor"], L["p_pool"], L["design"], L["viz"])),
        ])
        faqs = [
            ("What do you need before quoting marble shop drawings?", "The design drawings or sketches, stone name and thickness if you already know them, slab photos when vein matching matters, and the areas in scope. A deadline helps. Send them through the enquiry form."),
            ("Which formats are delivered?", "AutoCAD DWG and PDF as standard. Cutting lists and quantity summaries are spreadsheet-ready when they are included in the quote. Other formats are only agreed if you ask for them."),
            ("Do you draw vanities, floors, stairs and cladding?", "Yes. Countertops, vanities, staircases, wall cladding, flooring, kitchen islands, fireplaces and waterjet inlays are the usual scope. Each is quoted from the drawings you send."),
            ("Who approves the stone drawings in Dubai, Abu Dhabi or Sharjah?", "Typically the project consultant named by the contractor: architect, interior designer or engineer. The exact checklist, title block and number of copies come from that project. Send them if you have them. Approval to fabricate is the reviewer’s, not a municipal stamp on the shop drawing."),
            ("Can the notes be in Arabic?", "Yes. Notes can be English, Arabic or bilingual. Say which when you enquire."),
            ("Is estimation included?", "Quantity take-off and an Excel-ready cost summary are available and priced with the drawing scope. They are not added silently. See architectural estimation if the package is a full BOQ rather than a stone schedule."),
        ]
    else:
        html = _html([
            ("h", "فيمَ تُستخدم رسومات الرخام التنفيذية"),
            ("p", "رسومات الرخام والحجر التنفيذية هي مجموعة التصنيع والتركيب لمشروع بعينه. تقع بين نية مصمم الديكور ومنشار الجسر. سطح المطبخ والمغسلة والدرج والجدار متطابق العروق ومخطط الأرضية يحتاج كل منها معلوماته: المسقط والواجهات والقطاعات والحافة والسماكة والتشطيب والفاصل وكل فتحة. يشرح %s الفكرة بمزيد من التفصيل، و%s قائمة قصيرة يستخدمها المصنع." % (L["b_what"], L["b_check"])),
            ("p", "يرسم D3DDD هذه المجموعات بالأوتوكاد لمقاولين وورش حجر تعمل في دبي وأبوظبي والشارقة وجميع الإمارات. السعر حسب المشروع بعد مراجعة المخططات. هذه الصفحة ليست لائحة أسعار. أرسل المجموعة المعمارية أو واجهات الديكور أو صور الألواح أو كروكي المقاسات عبر %s." % L["contact"]),
            ("h", "المسلّمات"),
            ("ul", [
                "رسومات تنفيذية: مساقط وواجهات وقطاعات وتفاصيل مكبرة مع اسم الحجر والسماكة والحافة والتشطيب.",
                "رسومات تصنيع: زوايا وتفاوتات وفواصل وملاحظات CNC أو الووترجت التي طلبتها الورشة.",
                "قوائم قص وتوزيع ألواح يتبع العرق، مع تطابق العروق حيث يعتمد التصميم عليه.",
                "حصر كميات وملخص جاهز لبرنامج الجداول عندما يكون التقدير جزءاً من العرض.",
                "DWG مع PDF وجدول مراجعات. ملاحظات عربية عند الطلب، مع الإنجليزية أو بدلاً منها.",
            ]),
            ("h", "صيغ الملفات"),
            ("p", "DWG هو الملف الذي يبقيه المصنع. PDF هو الملف الذي يعلّم عليه الاستشاري ويطبعه الموقع. إذا شمل العرض قائمة قص أو جدول كميات يُرتَّب الجدول لبرنامج جداول. صور العنصر المميز، إن كانت جزءاً من العمل نفسه، صور لا تغني عن اللوحات المقاسة. إذا احتاجت الورشة أسماء طبقات معينة أو لوحة عنوان فأرسل نموذجاً وتُتبع المجموعة ذلك النموذج."),
            ("h", "من الاستفسار إلى التركيب"),
            ("ol", [
                "أرسل مخططات التصميم والمقاسات وأي صور للألواح.",
                "يُؤكد النطاق والسعر وموعد التسليم كتابياً.",
                "يخرج الإصدار الأول بصيغة DWG وPDF.",
                "تبدي أنت أو المصنع أو الاستشاري الملاحظات.",
                "يصدر التعديل ثم يقص المصنع ويركب الموقع.",
            ]),
            ("p", "موعد التسليم هو التاريخ المكتوب في ذلك العرض. مغسلتان مجموعة أصغر من دور أرضي لفيلّا مع قص مائي وجدران متطابقة العروق. جولة ملاحظات الاستشاري إصدار آخر تُوقَّت عند وصول الملاحظات، وليست إعادة كتابة صامتة للسعر. إذا بقي مقاس موقع مفتوحاً تُعلَّم تلك اللوحة وتُترك حتى يُعرف المقاس."),
            ("h", "مراجعة الاستشاري بعبارات عامة"),
            ("p", "في دبي وأبوظبي والشارقة تكون رسومات الحجر عادة حزمة داخل تسليم المقاول إلى استشاري المشروع. يراجعها المراجع مقابل واجهات الديكور: مواضع الفواصل وحواف الحجر وارتفاع الظهر ومقاسات التجاويف وكيف يلتقي الحجر بالنجارة والزجاج والأدوات الصحية. تعود الملاحظات على PDF. يحمل الإصدار المعدّل رقم مراجعة جديداً حتى لا يقص المصنع من لوحة ملغاة. بعض المشاريع يريد خطاب إحالة ولوحة عنوان ثابتة، وبعضها يكتفي بملف PDF في البريد. أرسل القاعدة التي يستخدمها مشروعك فعلاً. لا يخترع D3DDD تسليماً لجهة رسمية، وهذه الرسومات ليست مجموعة تصريح. إذا احتاج المشروع أيضاً لوحات معمارية منسّقة فهذا العمل تحت %s." % L["draft"]),
            ("p", "الدرج يحتاج معلومات الدوسة والقائمة والتثبيت التي لا يحملها مسقط الأرضية. تمر ملاحظة %s على هذا النوع من اللوحات. توزيع الألواح — أي قطعة من أي لوح حتى يستمر العرق — مشروح في %s." % (L["b_stair"], L["b_slab"])),
            ("h", "أعمال يمكن الاطلاع عليها"),
            ("p", "%s لوحات حقيقية أُزيلت منها بيانات العملاء: %s و%s و%s و%s و%s و%s. مخططات الأرضيات مثل %s والأعمال الخارجية مثل %s تظهر عادة الرسم نفسها على مسقط أكبر. إذا كان العمل لا يزال في مرحلة المفهوم فيمكن أن يرافق الرسومات %s و%s حتى يرى العميل الخامة قبل اعتماد القص." % (L["projects"], L["p_bath"], L["p_vanity"], L["p_paon"], L["p_nest"], L["p_door"], L["p_lobby"], L["p_floor"], L["p_pool"], L["design"], L["viz"])),
        ])
        faqs = [
            ("ماذا يلزم قبل تسعير رسومات الرخام؟", "مخططات التصميم أو الرسومات الأولية، واسم الحجر وسماكته إن كانا معروفين، وصور الألواح حين يهم تطابق العرق، والمناطق الداخلة في النطاق. الموعد النهائي مفيد. أرسلها عبر نموذج الاستفسار."),
            ("ما الصيغ التي تُسلَّم؟", "أوتوكاد DWG وPDF بشكل أساسي. قوائم القص وملخصات الكميات جاهزة للجداول حين تكون داخلة في العرض. الصيغ الأخرى لا تُعتمد إلا إذا طلبتها."),
            ("هل ترسمون المغاسل والأرضيات والدرج والتكسيات؟", "نعم. أسطح المطابخ والمغاسل والدرج وتكسية الجدران والأرضيات وجزر المطبخ والمدافئ وتطعيم الووترجت هي النطاق المعتاد. كل منها يُسعَّر من المخططات التي ترسلها."),
            ("من يعتمد رسومات الحجر في دبي أو أبوظبي أو الشارقة؟", "عادة استشاري المشروع الذي يسمّيه المقاول: معماري أو مصمم ديكور أو مهندس. قائمة التحقق ولوحة العنوان وعدد النسخ تأتي من ذلك المشروع. أرسلها إن وُجدت. اعتماد التصنيع قرار المراجع لا ختم بلدية على الرسم التنفيذي."),
            ("هل يمكن أن تكون الملاحظات بالعربية؟", "نعم. الملاحظات يمكن أن تكون بالإنجليزية أو العربية أو باللغتين. اذكر ذلك عند الاستفسار."),
            ("هل حساب الكميات مشمول؟", "حصر الكميات وملخص تكلفة جاهز للجداول متاحان ويُسعَّران مع نطاق الرسم. لا يُضافان بصمت. راجع حساب الكميات إذا كانت الحزمة جدول كميات كاملاً لا جدول حجر فقط."),
        ]
    return html, faqs

def _service_en(slug, L):
    common_tail = (
        ("h", "Turnaround and the written quote"),
        ("p", "Every drawing service on this site is quoted per project. The delivery date is part of that quote and is confirmed before work starts. A comment round is a later issue, scheduled when the comments arrive. There is no published day-rate and no published square-metre rate. The AED figures elsewhere on the site — 1,200, 2,000 and 3,500+, and the 5-page contractor website at AED 2,000 with 50% upfront — are website packages only."),
        ("h", "Keep going"),
        ("p", "Send the package through the %s. Stone-specific sheets are on %s. The wider CAD service is %s, early layouts are %s, quantities are %s, images are %s, and sites are %s. Issued examples are collected under %s. Shorter notes live on the %s." % (L["contact"], L["marble"], L["draft"], L["design"], L["estim"], L["viz"], L["web"], L["projects"], L["blog"])),
    )
    pages = {
        "architectural-drafting": [
            ("h", "What architectural drafting covers here"),
            ("p", "Architectural drafting at D3DDD is the measured AutoCAD work that follows a design: shop drawings, fit-out sheets, joinery elevations, as-built records and, when you ask for it, a permit-oriented set prepared from your design package. Requirements for permits differ by emirate and by the authority that project actually uses, so the checklist has to come from you. The studio does not publish a code clause or a submission portal as if it were universal."),
            ("p", "The usual client is a fit-out contractor, a joinery workshop or a consultant who needs the sheets redrawn so a site team can build from them. Shoaib Hussan draws them in Dubai for projects across the UAE. Source material can be a consultant’s PDF, an older DWG, a marked-up print or a survey. Say which layers and which title block the project already uses; matching them saves a comment round."),
            ("h", "Deliverables and formats"),
            ("ul", [
                "DWG and PDF of the same issue, with a revision table.",
                "Plans, elevations, sections, reflected ceiling plans and the details the scope names.",
                "Joinery elevations with heights, materials and hardware notes when joinery is included.",
                "As-built sheets that record what was built, for handover or a later alteration.",
                "English notes, with Arabic on request.",
            ]),
            ("p", "DWG is the file other consultants coordinate against. PDF is the file that gets marked up. A stone package that needs cutting lists is better handled on the marble page, and the two can be quoted together if the job has both. Layer habits for Gulf fit-out packages are discussed in %s." % L["b_std"]),
            ("h", "AutoCAD 2D drafting and construction drawings"),
            ("p", "Architectural drafting at D3DDD is 2D AutoCAD work issued as DWG and PDF. The live service already names the usual sheets: plans, elevations, sections, reflected ceiling plans and the details the scope includes, plus joinery elevations and as-built records when those are in the quote. That is the construction-drawing set a contractor, fabricator or consultant can mark up and coordinate against."),
            ("p", "A design drawing shows intent: room layout, a finish, a joinery line. A construction or shop drawing shows execution: dimensions, layers, junctions and a revision table so the site is not building from a mixed set. Both can be drawn in AutoCAD. The difference is the stage and the amount of measured detail. Early layouts and space planning belong on the %s page. Once a layout is approved, this page is where it is turned into construction-ready CAD. See %s." % (L["design"], L["b_concept"])),
            ("p", "Source material can already be a consultant’s PDF, an older DWG, a marked-up print or a survey — that is stated on the live page. If you only have a PDF or a scan, say so in the enquiry; redrawing it to a layered DWG is drafting work, not a new service line. If the project already has layer names and a title block, send a sample so the new issue can follow them. A practical note on layer habits is on the blog: %s. That note is guidance, not a claim that one standard is mandatory in every emirate." % L["b_std_full"]),
            ("p", "Permit-oriented sheets stay on the same rule as the live page: they are prepared only from the checklist you supply, because requirements differ by emirate and by the authority the project actually uses. A drafted CAD set is not, by itself, a permit or a BIM submission. Background reading already linked from this page includes %s and %s." % (L["b_dubai"], L["b_bim"])),
            ("h", "How this sits next to marble, fit-out and quantities"),
            ("p", "%s remain a distinct deliverable: cutting lists, slab layouts and piece-tagged stone sheets. They can be quoted with a drafting set when a job has both, but they are not the primary offer of this page. %s cover ceilings, partitions, kitchens, wardrobes and interior elevations in more detail. %s measures the drafted sheets. %s can illustrate the same design; a picture does not replace the DWG." % (L["marble_cap"], L["fitout"], L["estim_boq"], L["viz_model"])),
            ("p", "An external construction-drawing example already in the portfolio is the %s." % L["pool_set"]),
            ("p", "Architectural drafting is quoted per project. Scope, fee and delivery date are confirmed in writing before work starts. There is no published day-rate or square-metre rate for this service. To ask for a quote, send the current drawings or a survey through the %s. A longer guide to %s is on the blog." % (L["contact_form"], L["b_drafting"])),
            ("h", "Review in Dubai, Abu Dhabi and Sharjah"),
            ("p", "Drafted fit-out sets in these emirates normally travel with the contractor’s submission to the project consultant. The architect or interior designer checks them against the approved design: partitions, ceiling heights, joinery lines, wet-area build-ups and the points where trades meet. Comments come back on the PDF or as a list. The next issue raises the revision and clouds the changes so the site does not build from a mixed set. Abu Dhabi jobs often ask for a transmittal; Sharjah jobs sometimes have only the designer as reviewer; Dubai jobs range from a single interior designer to a full consultant team. The drawing follows the rule you send. It is not, by itself, a permit or a BIM submission. If the project also needs those, they are a separate line in the quote. Background reading is on %s and %s." % (L["b_dubai"], L["b_bim"])),
            ("p", "External and wet-area sheets in the portfolio include %s. Floor set-out that starts as a drafting plan includes %s." % (L["p_pool"], L["p_floor"])),
        ],
        "architectural-designing": [
            ("h", "Design that can become a drawing"),
            ("p", "Architectural designing here is the step before fabrication drawings: concept plans, space planning, elevations and design development for villas, apartments, offices and fit-outs. The aim is a layout a client can approve and a drafter can later dimension. It is not a substitute for a signed consultancy appointment, and it is not a permit design unless that scope is written into the quote."),
            ("p", "You might arrive with a brief and a plot or an apartment outline, or with a designer’s sketch that needs to be tested against furniture, circulation and wet areas. The work is done for owners, interior designers and contractors in Dubai, Abu Dhabi, Sharjah and the wider UAE. Fees are per project. Send the brief and any survey through the enquiry form."),
            ("h", "What you receive"),
            ("ul", [
                "Plan options that test rooms, furniture and the feature zones you care about.",
                "A developed plan once one option is chosen, with key dimensions.",
                "Elevations and sections for finishes and heights, enough to brief stone and joinery.",
                "A short note of materials where the design depends on them.",
                "DWG and PDF, so the same file can move into shop drawings without being redrawn from a picture.",
            ]),
            ("p", "If the next step is fabrication, the developed drawings hand across to %s or to %s. If the client needs to see the material before they choose, %s can be quoted with the design. A flooring layout that began as a plan is in the portfolio as %s." % (L["draft"], L["marble"], L["viz"], L["p_floor"])),
            ("h", "How this meets consultant review"),
            ("p", "Design drawings and shop drawings are often reviewed by different people, sometimes weeks apart. In Dubai, Abu Dhabi and Sharjah the early layout may be approved by the client and the interior designer, while the later shop drawings go to the project consultant for fabrication. Keeping the design in DWG means the shop-drawing set starts from the approved plan rather than from a traced PDF. D3DDD does not claim that a concept layout satisfies a municipality. If a project needs a permit package, that checklist is yours to send, and it is scoped separately from space planning."),
            ("p", "Turnaround follows the same rule as the rest of the studio: the date is confirmed in writing with the price. Two plan options for an apartment are not the same duration as a villa with external majlis and pool. Comment rounds are further issues."),
            ("h", "From a concept layout to CAD construction drawings"),
            ("p", "Architectural designing on this page is the step before fabrication drawings: plan options, space planning, a developed plan with key dimensions, and elevations or sections that can brief stone and joinery. The files are already issued as DWG and PDF so the next stage does not start from a traced picture."),
            ("p", "You can arrive with a brief and a plot, an apartment outline, or a designer’s sketch that still needs to be tested against furniture, circulation and wet areas — that intake is already on the live page. The work is for owners, interior designers and contractors in Dubai, Abu Dhabi, Sharjah and the wider UAE. Two plan options for an apartment are not the same duration as a villa with an external majlis and pool; the delivery date is confirmed in writing with the price, and comment rounds are later issues."),
            ("p", "That next stage after an approved layout is %s — AutoCAD 2D construction drawings, shop drawings, as-built or fit-out sheets, quoted as a separate step unless both are written into one quote. If the approved design includes marble or stone that must be cut, continue to %s. If the client needs to see a material or a room before they choose, %s can be quoted with the design; renders are not included in a design package unless the quote says so. A single still render, when commissioned on its own, has an owner-approved pack price of 650 AED (50%% upfront). Quantities for a tender or an order are %s. Read %s for the same hand-off." % (L["draft"], L["marble_shop"], L["viz_named"], L["estim_name"], L["b_concept"])),
            ("p", "In Dubai, Abu Dhabi and Sharjah the early layout may be approved by the client and the interior designer, while later shop drawings go to the project consultant for fabrication. Keeping the design in DWG means the construction-drawing set starts from the approved plan rather than from a traced PDF. D3DDD does not claim that a concept layout satisfies a municipality."),
            ("p", "A published example of a design-stage layout (tagged architectural designing, not shop drawings) is the %s, prepared as a design option for approval before detailed marble drawings." % L["floor_lux"]),
            ("p", "Design work is quoted per project. Send the brief, plot or survey through the %s." % L["contact_form"]),
        ],
        "architectural-estimation": [
            ("h", "Quantities that match the sheets"),
            ("p", "Architectural estimation here means measuring the drawings: bills of quantities, take-offs, material schedules and the bundles contractors send out for pricing. The numbers are taken from the plans, elevations and schedules, and the assumptions are written down. A quantity that cannot be seen on a drawing is marked as an assumption, not hidden inside a total."),
            ("p", "Stone quantities and slab layouts can sit inside a marble package or be measured on their own. Joinery, flooring, wall finishes and ceiling areas are measured when those drawings exist. The work is for contractors and estimators in Dubai, Abu Dhabi, Sharjah and the other emirates. It is quoted per package. There is no published rate per page or per square metre."),
            ("h", "Deliverables and formats"),
            ("ul", [
                "A bill of quantities organised so a revision of the drawings can be compared with the previous issue.",
                "Take-off notes that say which sheet each figure came from.",
                "Material schedules for stone, joinery or finishes, ready to send to a supplier.",
                "Spreadsheet files, plus PDF when you need a frozen copy for a tender.",
                "An updated issue when the design or the site size changes, quoted as its own step if the change is large.",
            ]),
            ("p", "DWG and PDF remain the drawing formats when drawings are part of the same quote. The spreadsheet is the format for the numbers. If you only need a cutting list for one bathroom, that is a smaller job than a tender bill for a whole villa. Say which one you want."),
            ("h", "Using the bill in a UAE fit-out"),
            ("p", "On projects in Dubai, Abu Dhabi and Sharjah the bill is often attached to the same submission as the shop drawings. The consultant comments on the drawings; the contractor uses the bill to price or to order. When a comment changes a height or a stone thickness, the quantities have to move with the revision or the order will not match the approved sheet. D3DDD updates the figures against the revised issue when that update is in the quote. Nothing here is a claim about a particular tender law or a mandatory bill format. If your client has a template, send it and the schedules will follow the template."),
            ("p", "Measured stone work you can compare with a schedule includes %s and %s. The nesting note on the %s is the practical side of a cutting list." % (L["p_nest"], L["p_bath"], L["b_slab"])),
        ],
        "3d-rendering-modeling-visualization": [
            ("h", "Images that help a decision, not a substitute for dimensions"),
            ("p", "3D rendering, modeling and visualization at D3DDD are the pictures and models clients and consultants look at before they approve a material or a layout. A still render can show vein direction, joinery colour and light. It cannot be measured with a tape. Fabrication still needs the DWG and PDF shop drawings. The two are often quoted together so the picture and the sheets describe the same design."),
            ("p", "Typical work is an interior room, a marble feature, a façade study or a short walkthrough. Models are built from the drawings you send. If those drawings are still a sketch, the image is labelled as a study. The service is for designers, contractors and owners in Dubai, Abu Dhabi, Sharjah and the rest of the UAE. A single still has a published pack price; further views and spaces are quoted after the brief is clear."),
            ("h", "What is delivered"),
            ("ul", [
                "PNG or JPG stills at the resolution agreed in the quote.",
                "More than one material option when you are choosing stone or joinery finishes.",
                "A model file on request, if a later drafter or renderer needs it.",
                "A short camera path when a walkthrough is part of the scope.",
                "Notes that point back to the drawing sheets, so the picture does not drift away from the dimensions.",
            ]),
            ("p", "DWG and PDF are not the deliverable of a render-only job. They are the deliverable of the drafting and marble services, which can be commissioned with the images. A single 3D still render is 650 AED, with 50% upfront. Additional views, material options, a standalone model file, walkthroughs and multi-view sets are quoted on request."),
            ("h", "3D modeling and 3D rendering"),
            ("p", "3D modeling is the digital model built from the drawings you send — rooms, joinery, stone features, a façade or an outdoor space. 3D rendering is the still image (PNG or JPG) produced from that model, or from a model you already have, to show materials, vein direction, lighting and massing. Visualization here includes both, plus a short camera path when a walkthrough is in the scope. The live page is clear that a still render cannot be measured with a tape. Fabrication still needs the DWG and PDF %s or, for stone, the %s." % (L["draft_shop"], L["marble_shop"])),
            ("p", "If the source is only a sketch, the image is labelled as a study, as the live page already says. If shop drawings and images are commissioned together, the render should follow the same material and joint logic as the sheets, and an update to the image is described in the quote when those sheets change. The blog goes further on %s and on %s." % (L["b_rmodel"], L["b_vizok"])),
            ("h", "Single 3D render — owner-approved price"),
            ("p", "A single 3D still render is 650 AED, with 50% upfront. That figure is an owner-approved pack price for one agreed still (PNG or JPG at the resolution written into the quote). It is not the website-package price list, and it is not a square-metre rate."),
            ("p", "The following remain quoted on request: additional views or material options, a model file issued on its own, interior or exterior sets of more than one still, walkthroughs, and VR-ready or product-close-up scenes. Say which views you need, which materials you are considering, and whether the model should be handed to a later drafter."),
            ("p", "Typical pairings already on this page include the %s, %s and %s. Early layouts can come from %s. Request a quote or a single-render booking through the %s." % (L["p_lobby"], L["p_bath"], L["p_floor"], L["design"], L["contact_form"])),
            ("h", "Where the images sit in a review"),
            ("p", "In Dubai, Abu Dhabi and Sharjah a render is often what the client approves, while the shop drawings are what the consultant approves for fabrication. Mixing those two decisions causes trouble: a vein that looked acceptable in a picture may be impossible on the slabs that arrived, and a picture with no joint lines does not tell the factory where to cut. When both are in the quote, the render is updated if the approved shop drawings change the design, and that update is described in the quote rather than assumed. The studio does not claim that a render is an authority submission. It is a decision tool."),
            ("p", "Sheets that pair well with a material study include %s, %s and %s. If you are comparing real-time tools for your own team, the blog has a note on Chaos Vantage; the production images for a project are still scoped here." % (L["p_lobby"], L["p_bath"], L["p_floor"])),
        ],
        "website-development-designing": [
            ("h", "Websites, with the prices that are actually published"),
            ("p", "Website development at D3DDD is for contractors, workshops and studios that need a clear site and a way for visitors to enquire. It is separate from shop drawings. Drawing work is quoted per project. Website work uses the packages already listed on this site."),
            ("ul", [
                "Starter: CAD 599 or AED 1,200. One page, mobile layout, contact form, basic SEO.",
                "Business: CAD 999 or AED 2,000. Up to five pages, with the same mobile layout, form and basic SEO. This is the contractor website package, 50% upfront and the balance on completion.",
                "Premium: CAD 1,799+ or AED 3,500+. More pages and custom features, still mobile, with a form and basic SEO. The plus means the figure moves with the features you add.",
            ]),
            ("p", "Domain registration, hosting and paid stock photographs are not included unless that is written down. Payments for these packages go through PayPal. The enquiry on the finished site can point at whatever channel you actually use. This studio’s own site lists an email assembled in the browser and the enquiry form, and it does not publish a phone number."),
            ("h", "What the build includes"),
            ("ul", [
                "A mobile-friendly build of the agreed pages.",
                "An enquiry path: a form, a clear contact link, or both.",
                "Basic SEO: titles, descriptions and readable URLs. Not a promise of rankings.",
                "One review cycle after the first build, then go-live once the balance is paid.",
                "Demo themes you can look at before choosing a direction. They are samples, not client projects.",
            ]),
            ("p", "There is no DWG deliverable for a website. If you also need drawings, add %s or %s to the same enquiry and they will be quoted on their own." % (L["marble"], L["draft"])),
            ("h", "How a site job runs, including across the emirates"),
            ("p", "The steps are the same whether the business is in Dubai, Abu Dhabi or Sharjah, because the site is delivered online. You pay the 50% deposit, send logos, text and photographs, the pages are built, you review them, and the balance is paid when the site is ready to go live. Nothing here is a claim about a trade-licence display rule or a tourism permit. If your activity needs a particular disclaimer or a licence number on the page, send the wording and it will be placed where you ask. Content in Arabic, English or both is a normal request; say so at the start so the layout is designed for it, including right-to-left pages when Arabic is the primary language."),
            ("p", "The package details and the live demo themes are on %s. Drawing samples, if you want the site to point at real sheets later, are under %s." % (L["webpkg"], L["projects"])),
        ],
    }
    blocks = list(pages[slug]) + list(common_tail)
    if slug == "architectural-estimation":
        blocks += [
            ("h", "How to read the schedule"),
            ("p", "A take-off is only useful if someone else can check it. Each line names the sheet it came from and the unit: square metres of flooring, linear metres of skirting, or a count of sink cut-outs. When a villa has both a stone package and a joinery package, the two schedules stay separate so a stone yard is not asked to price cabinet carcasses. If the consultant already uses an empty bill template, send it with the drawings and the numbers will follow that column order. Assumptions such as joint width or cutting waste sit in the header of the schedule, not buried in a cell, so the person pricing the work can change them."),
            ("h", "Quantity take-off and the bill of quantities"),
            ("p", "A quantity take-off is the measurement itself: areas, linear metres and counts taken from the plans, elevations and schedules, with a note of which sheet each figure came from. A bill of quantities (BOQ) is the structured document those measurements are organised into, so a revision of the drawings can be compared with the previous issue and a contractor or supplier can price or order from it. Both already sit on this service. The live page also offers material schedules and, when asked, an early cost plan to compare options before tender."),
            ("p", "D3DDD does not publish a mandatory UAE bill format or a tender-law claim. If the client already has an empty template, send it with the drawings and the schedules follow that column order — that rule is already on the live page. Assumptions such as joint width or cutting waste stay in the header, not hidden in a total. The blog explains %s and %s." % (L["b_takeoff"], L["b_boqdiff"])),
            ("h", "What can be measured"),
            ("p", "Stone quantities (areas, linear metres, piece counts, with the cutting-waste assumption written down) can sit inside a %s package or be measured from drawings you already have. A stone-specific how-to is the blog guide %s. This service page is wider than that article: joinery, flooring, wall finishes and ceiling areas are measured when those drawings exist, and the stone schedule is kept separate from a joinery schedule so a yard is not asked to price cabinet carcasses." % (L["marble_shop"], L["b_marble_qty"])),
            ("p", "The numbers only match the build if they move with the drawing revision. When a consultant comment changes a height or a thickness, the take-off has to be updated against that issue. Large redesigns are quoted as their own step, as the live FAQ already states."),
            ("p", "Estimation is quoted per package. It is not a published square-metre or per-page rate, and it is not a website package price. Send the drawings (and a template, if you have one) through the %s. If you also need the sheets measured from, see %s." % (L["contact_form"], L["draft"])),
        ]
    faqs = {
        "architectural-drafting": [
            ("What is included in architectural drafting?", "Shop drawings, fit-out and joinery sheets, CAD details and as-built records, issued as DWG and PDF. Permit-oriented sheets are prepared only from the checklist you supply, because requirements differ by emirate and by project."),
            ("How are comments handled?", "Comments on the PDF are revised into a new issue with a raised revision. The delivery date for that issue is agreed when the comments arrive. The first date is the one written into the quote."),
            ("Do you follow a Gulf layer standard?", "The set can follow the layer names and title block you already use. Send a sample. A practical note on fit-out standards is on the blog; it is guidance, not a claim that one standard is mandatory."),
            ("Can stone and joinery be in one quote?", "Yes. Say so in the enquiry. Marble shop drawings have their own page because the cutting list and slab layout are a distinct deliverable."),
            ("Which emirates?", "Dubai, Abu Dhabi, Sharjah, Ajman, Ras Al Khaimah, Umm Al Quwain and Fujairah. Files are sent digitally."),
            ("What is the difference between architectural drafting and construction drawings?", "On this service they are the same body of work: measured AutoCAD 2D sheets — plans, elevations, sections, details and, where scoped, as-built or fit-out drawings — issued as DWG and PDF. “Construction drawings” here means the dimensioned set used to build or fabricate from, not a separate product line."),
            ("Do you provide AutoCAD 2D drafting, or only 3D?", "The drafting service is 2D AutoCAD (DWG and PDF). %s is a separate service and can be quoted with the drawings." % L["viz_model"]),
            ("Can you convert a PDF or a scanned drawing into a DWG?", "Yes, when that redraw is written into the quote. Send the file and say which layers or title block the project already uses, if you have them."),
            ("What should I send to get a drafting quote?", "The current design or survey (PDF or DWG), the sheets you need, the emirate, and whether stone, joinery or a permit checklist is part of the same job. Use the %s. Fees are quoted per project." % L["contact_form"]),
        ],
        "architectural-designing": [
            ("What do I receive from design work?", "Plan options, a developed layout, and the elevations or sections needed to brief later drawings, in DWG and PDF. Renders are a separate service."),
            ("Is this a permit design?", "Only if a permit package is written into the quote, and only from the requirements you send. A concept layout is not presented as an authority approval."),
            ("Can the design continue into shop drawings?", "Yes. The DWG is the starting point for architectural drafting or marble shop drawings, quoted as the next step."),
            ("How long does a design take?", "The date is confirmed with the quote. It depends on how many options you want and how complete the survey or brief is."),
            ("Do you work in Arabic?", "Notes and communication can be in Arabic, English or both."),
            ("When should I use designing instead of drafting?", "Use this page when the layout is still being decided: options, space planning and design development. Use %s when an approved design needs measured construction or shop drawings in AutoCAD." % L["draft"]),
            ("Are 3D renders included in a design package?", "No, unless the quote says so. %s is a separate service. A single still render has an owner-approved pack price of 650 AED (50%% upfront); other views are quoted." % L["viz_model"]),
            ("Can you start from a sketch or a survey only?", "Yes. The live page already accepts a brief and a plot, an apartment outline, or a designer’s sketch. Completeness of that brief affects the delivery date, which is confirmed with the quote."),
            ("Do you do space planning for villas and apartments in Dubai?", "Yes. The live service lists villas, apartments, offices and F&amp;B fit-outs, for clients in Dubai and across the UAE."),
        ],
        "architectural-estimation": [
            ("What is an estimation package?", "A bill of quantities, take-off, material schedule or tender bundle measured from your drawings, with the assumptions written down. Delivered as a spreadsheet and PDF."),
            ("Are drawing fees included?", "Only when drawings are part of the same quote. A numbers-only package does not include new DWG sheets."),
            ("Do quantities update after consultant comments?", "Yes, when the update is included. A large redesign is quoted as its own step so the bill stays tied to the approved revision."),
            ("Can you measure stone only?", "Yes. Slab areas, piece counts and cutting waste can be scheduled with the marble drawings or from drawings you already have."),
            ("Is there a fixed rate?", "No. Estimation is quoted per package. It is not a published square-metre or per-page rate, and it is not a website package price."),
            ("What is a quantity take-off, and how is it different from a BOQ?", "A take-off is the measurement from the drawings. A BOQ is the structured bill those measurements are placed in, organised so a later revision can be compared and a contractor or supplier can price or order from it. This service prepares both, plus material schedules when they are in the quote."),
            ("Which trades and units can you measure?", "Whatever is visible on the drawings in the scope: for example square metres of flooring or finishes, linear metres of skirting, and counts of cut-outs. Stone, joinery, wall finishes and ceilings are measured when those sheets exist. A quantity that cannot be seen on a drawing is marked as an assumption."),
            ("Do you follow a standard UAE tender template?", "Only if you send one. There is no single format claimed on this page. If your client has a template, the schedules follow it."),
            ("Can you prepare a take-off from PDFs only?", "Yes, when the figures can be read from the PDF set. Say so in the enquiry. New DWG sheets are included only when drawings are part of the same quote."),
        ],
        "3d-rendering-modeling-visualization": [
            ("Do renders replace shop drawings?", "No. A render shows the intent. Fabrication needs DWG and PDF shop drawings with dimensions, joints and cut-outs."),
            ("What files do I get?", "PNG or JPG stills, a model file if you asked for one, and a walkthrough if that was in the quote. A single 3D still render is 650 AED, with 50% upfront. Additional views or material options, a model file issued on its own, interior or exterior sets of more than one still, walkthroughs, and VR-ready or product-close-up scenes are quoted on request."),
            ("Can you match the marble drawings?", "Yes, when both are commissioned. The image should follow the same material and the same joint logic as the sheets."),
            ("What do you need from me?", "Drawings or a clear sketch, the materials you are considering, and the views you need. Photographs of the space help."),
            ("Is a render an approval document?", "It helps a client decide. Consultant approval for fabrication is still done on the shop drawings. The studio does not treat a picture as a permit."),
            ("What does the 650 AED single 3D render include?", "One still render, as agreed in the quote, delivered as a PNG or JPG at the agreed resolution, with 50% upfront. Extra views, material options, a standalone model file, walkthroughs and multi-view sets are quoted separately."),
            ("What is the difference between 3D modeling and 3D rendering?", "Modeling is the 3D model built from your drawings. Rendering is the still image produced from a model. This service covers both. A model file is included only when you ask for it in the quote."),
            ("Do you offer walkthroughs and exterior views?", "Yes, when they are in the scope. Exterior visualization and simple camera paths are already listed as sub-services. They are quoted on request, not included in the single-still pack price."),
            ("Will a render match the shop drawings?", "When both are commissioned, the image should follow the same material and joint logic as the sheets. A render still does not replace dimensioned DWG and PDF drawings for fabrication."),
        ],
        "website-development-designing": [
            ("What does the AED 2,000 package include?", "The Business package is up to five pages, mobile-friendly, with a contact form and basic SEO. Half is paid upfront and the balance on completion. Domain, hosting and paid stock images are extra unless agreed in writing."),
            ("What are the other website prices?", "Starter is AED 1,200 (CAD 599) for one page. Premium starts at AED 3,500 (CAD 1,799) and rises with custom features. Drawing services are not included in these figures."),
            ("Can the site be in Arabic?", "Yes. Say so at the start. Arabic-first pages are laid out right to left."),
            ("Do you publish a phone number on the site you build?", "Only if you want one. D3DDD’s own site does not list a phone number. Your site can use the enquiry channel you actually answer."),
            ("How does the job start?", "A 50% deposit, then your logo, text and photographs. You review the build, then the balance is paid at go-live."),
        ],
    }
    return _html(blocks), faqs[slug]

def _service_ar(slug, L):
    common_tail = (
        ("h", "الموعد والعرض المكتوب"),
        ("p", "كل خدمة رسم في هذا الموقع تُسعَّر حسب المشروع. موعد التسليم جزء من ذلك العرض ويُؤكد قبل بدء العمل. جولة الملاحظات إصدار لاحق يُجدول عند وصولها. لا يوجد سعر يوم منشور ولا سعر للمتر المربع. أرقام الدرهم في مكان آخر من الموقع — 1,200 و2,000 و3,500+، وموقع المقاول من خمس صفحات بـ2,000 درهم مع 50% مقدماً — هي باقات مواقع فقط."),
        ("h", "للمتابعة"),
        ("p", "أرسل الباقة عبر %s. لوحات الحجر في %s. خدمة أوتوكاد الأوسع هي %s، والمخططات المبكرة %s، والكميات %s، والصور %s، والمواقع %s. الأمثلة المنشورة مجموعة تحت %s. الملاحظات الأقصر في %s وهي بالإنجليزية." % (L["contact"], L["marble"], L["draft"], L["design"], L["estim"], L["viz"], L["web"], L["projects"], L["blog"])),
    )
    pages = {
        "architectural-drafting": [
            ("h", "ماذا يشمل الرسم المعماري التنفيذي هنا"),
            ("p", "الرسم المعماري في D3DDD هو عمل أوتوكاد المقاس الذي يلي التصميم: رسومات تنفيذية ولوحات تشطيب وواجهات نجارة ومخططات كما بُني، وعند الطلب مجموعة ذات طابع تصريح تُعد من باقة تصميمك. متطلبات التصاريح تختلف بين الإمارات وبين الجهة التي يستخدمها المشروع فعلاً، لذلك يجب أن تأتي قائمة التحقق منك. لا ينشر الاستوديو بند نظام أو بوابة تسليم كأنها عامة."),
            ("p", "العميل المعتاد مقاول تشطيب أو ورشة نجارة أو استشاري يحتاج إعادة رسم اللوحات حتى يستطيع فريق الموقع البناء منها. يرسمها شعيب حسين في دبي لمشاريع في أنحاء الإمارات. المادة المصدر قد تكون PDF من الاستشاري أو DWG قديماً أو طبعة معلَّمة أو رفع مساحي. اذكر الطبقات ولوحة العنوان التي يستخدمها المشروع؛ مطابقتها توفر جولة ملاحظات."),
            ("h", "المسلّمات والصيغ"),
            ("ul", [
                "DWG وPDF للإصدار نفسه مع جدول مراجعات.",
                "مساقط وواجهات وقطاعات ومخططات أسقف والتفاصيل التي يسمّيها النطاق.",
                "واجهات نجارة بالارتفاعات والمواد وملاحظات الإكسسوار حين تكون النجارة مشمولة.",
                "لوحات كما بُني تسجّل ما نُفّذ، للتسليم أو لتعديل لاحق.",
                "ملاحظات بالإنجليزية، وبالعربية عند الطلب.",
            ]),
            ("p", "DWG هو الملف الذي ينسّق عليه الاستشاريون الآخرون. PDF هو الملف الذي تُوضع عليه الملاحظات. حزمة الحجر التي تحتاج قوائم قص أنسب في صفحة الرخام، ويمكن تسعير الاثنين معاً إذا كان العمل يشملهما. عادات الطبقات لحزم التشطيب في الخليج مناقشة في %s." % L["b_std"]),
            ("h", "المراجعة في دبي وأبوظبي والشارقة"),
            ("p", "مجموعات التشطيب المرسومة في هذه الإمارات تسير عادة مع تسليم المقاول إلى استشاري المشروع. يراجعها المعماري أو مصمم الديكور مقابل التصميم المعتمد: القواطع وارتفاعات الأسقف وخطوط النجارة وتراكيب المناطق الرطبة ونقاط التقاء الحرف. تعود الملاحظات على PDF أو في قائمة. يرفع الإصدار التالي رقم المراجعة ويظلل التغيير حتى لا يبني الموقع من مجموعة مختلطة. أعمال أبوظبي تطلب غالباً خطاب إحالة، وأعمال الشارقة قد يكون المراجع فيها المصمم فقط، وأعمال دبي تتراوح بين مصمم ديكور واحد وفريق استشاري كامل. يتبع الرسم القاعدة التي ترسلها. هو بذاته ليس تصريحاً ولا تسليم BIM. إذا احتاج المشروع إليهما فهما بند منفصل في العرض. خلفية للقراءة في %s و%s." % (L["b_dubai"], L["b_bim"])),
            ("p", "لوحات خارجية ومناطق رطبة في الأعمال تشمل %s. توزيع أرضية بدأ كمخطط رسم يشمل %s." % (L["p_pool"], L["p_floor"])),
        ],
        "architectural-designing": [
            ("h", "تصميم يمكن أن يصبح رسماً"),
            ("p", "التصميم المعماري هنا هو الخطوة قبل رسومات التصنيع: مخططات مفهومية وتخطيط مساحات وواجهات وتطوير تصميم للفلل والشقق والمكاتب والتشطيبات. الهدف مخطط يستطيع العميل اعتماده ويستطيع الرسام لاحقاً وضع أبعاده. ليس بديلاً عن تعيين استشاري موقّع، وليس تصميم تصريح إلا إذا كُتب ذلك النطاق في العرض."),
            ("p", "قد تصل بموجز ومخطط أرض أو حدود شقة، أو بكروكي مصمم يحتاج اختباراً مقابل الأثاث والحركة والمناطق الرطبة. العمل لملاك ومصممي ديكور ومقاولين في دبي وأبوظبي والشارقة وبقية الإمارات. الأتعاب حسب المشروع. أرسل الموجز وأي رفع عبر نموذج الاستفسار."),
            ("h", "ماذا تستلم"),
            ("ul", [
                "خيارات مساقط تختبر الغرف والأثاث ومناطق العناصر التي تهمك.",
                "مسقطاً مطوراً بعد اختيار خيار، بأبعاد رئيسية.",
                "واجهات وقطاعات للتشطيبات والارتفاعات تكفي لإحاطة الحجر والنجارة.",
                "ملاحظة قصيرة عن المواد حيث يعتمد التصميم عليها.",
                "DWG وPDF حتى ينتقل الملف نفسه إلى الرسومات التنفيذية دون إعادة رسم من صورة.",
            ]),
            ("p", "إذا كانت الخطوة التالية التصنيع تنتقل المخططات المطورة إلى %s أو إلى %s. إذا احتاج العميل رؤية الخامة قبل الاختيار يمكن تسعير %s مع التصميم. مخطط أرضية بدأ كمسقط موجود في الأعمال بعنوان %s." % (L["draft"], L["marble"], L["viz"], L["p_floor"])),
            ("h", "كيف يلتقي هذا بمراجعة الاستشاري"),
            ("p", "غالباً ما يراجع مخططات التصميم والرسومات التنفيذية أشخاص مختلفون، وأحياناً بفاصل أسابيع. في دبي وأبوظبي والشارقة قد يعتمد العميل ومصمم الديكور المخطط المبكر، بينما تذهب الرسومات التنفيذية لاحقاً إلى استشاري المشروع للتصنيع. إبقاء التصميم بصيغة DWG يعني أن مجموعة التنفيذ تبدأ من المسقط المعتمد لا من PDF مرسوم بالتتبع. لا يدّعي D3DDD أن المخطط المفهومي يفي ببلدية. إذا احتاج المشروع حزمة تصريح فقائمة التحقق تُرسل من طرفك وتُسعَّر منفصلة عن تخطيط المساحة."),
            ("p", "الموعد يتبع قاعدة الاستوديو نفسها: يُؤكد التاريخ كتابياً مع السعر. خيارا مسقط لشقة ليسا بمدة فيلا بمجلس خارجي ومسبح. جولات الملاحظات إصدارات لاحقة."),
        ],
        "architectural-estimation": [
            ("h", "كميات تطابق اللوحات"),
            ("p", "حساب الكميات هنا يعني القياس من المخططات: جداول كميات وحصر وجداول مواد والحزم التي يرسلها المقاول للتسعير. تُؤخذ الأرقام من المساقط والواجهات والجداول، وتُكتب الافتراضات. الكمية التي لا تُرى على رسم تُعلَّم افتراضاً ولا تُخفى داخل الإجمالي."),
            ("p", "كميات الحجر وتوزيع الألواح قد تكون داخل حزمة رخام أو تُقاس وحدها. النجارة والأرضيات وتشطيبات الجدران ومساحات الأسقف تُقاس عندما توجد تلك المخططات. العمل لمقاولين وحاسبي كميات في دبي وأبوظبي والشارقة وبقية الإمارات. يُسعَّر لكل حزمة. لا يوجد سعر منشور للصفحة أو للمتر المربع."),
            ("h", "المسلّمات والصيغ"),
            ("ul", [
                "جدول كميات مرتب بحيث يمكن مقارنة مراجعة المخططات بالإصدار السابق.",
                "ملاحظات حصر تقول من أي لوحة جاء كل رقم.",
                "جداول مواد للحجر أو النجارة أو التشطيبات جاهزة لمورّد.",
                "ملفات جداول، مع PDF حين تحتاج نسخة مجمّدة لمناقصة.",
                "إصدار محدّث حين يتغير التصميم أو مقاس الموقع، ويُسعَّر خطوة مستقلة إذا كان التغيير كبيراً.",
            ]),
            ("p", "تبقى DWG وPDF صيغ الرسم حين تكون المخططات جزءاً من العرض نفسه. ملف الجدول هو صيغة الأرقام. إذا كنت تحتاج قائمة قص لحمام واحد فهذا عمل أصغر من جدول مناقصة لفيلّا كاملة. اذكر أيهما تريد."),
            ("h", "استخدام الجدول في تشطيب بالإمارات"),
            ("p", "في مشاريع دبي وأبوظبي والشارقة يُرفق الجدول غالباً مع الرسومات التنفيذية في التسليم نفسه. الاستشاري يعلّق على المخططات، والمقاول يستخدم الجدول للتسعير أو للطلب. حين تغيّر ملاحظة ارتفاعاً أو سماكة حجر يجب أن تتحرك الكميات مع المراجعة وإلا لن يطابق الطلب اللوحة المعتمدة. يحدّث D3DDD الأرقام مقابل الإصدار المعدّل حين يكون التحديث داخل العرض. لا شيء هنا ادّعاء عن نظام مناقصات بعينه أو صيغة جدول إلزامية. إذا كان لدى عميلك نموذج فأرسله وستتبع الجداول ذلك النموذج."),
            ("p", "أعمال حجر مقيسة يمكن مقارنتها بجدول تشمل %s و%s. ملاحظة التوزيع في %s هي الجانب العملي لقائمة القص." % (L["p_nest"], L["p_bath"], L["b_slab"])),
        ],
        "3d-rendering-modeling-visualization": [
            ("h", "صور تساعد على قرار ولا تغني عن الأبعاد"),
            ("p", "التصميم ثلاثي الأبعاد والنمذجة والتصور في D3DDD هي الصور والنماذج التي ينظر إليها العميل والاستشاري قبل اعتماد خامة أو مخطط. الصورة الثابتة تستطيع إظهار اتجاه العرق ولون النجارة والضوء. لا يمكن قياسها بالمتر. التصنيع يبقى بحاجة إلى رسومات DWG وPDF. غالباً ما يُسعَّر الاثنان معاً حتى تصف الصورة واللوحات التصميم نفسه."),
            ("p", "العمل المعتاد غرفة داخلية أو عنصر رخام أو دراسة واجهة أو مسار تجوّل قصير. تُبنى النماذج من المخططات التي ترسلها. إذا كانت تلك المخططات ما زالت كروكي تُعلَّم الصورة دراسة. الخدمة لمصممين ومقاولين وملاك في دبي وأبوظبي والشارقة وبقية الإمارات، وتُسعَّر لكل لقطة أو فراغ بعد وضوح الموجز."),
            ("h", "ماذا يُسلَّم"),
            ("ul", [
                "صور PNG أو JPG بالدقة المتفق عليها في العرض.",
                "أكثر من خيار خامة حين تختار تشطيب الحجر أو النجارة.",
                "ملف نموذج عند الطلب إذا احتاجه رسام أو مصور لاحقاً.",
                "مسار كاميرا قصير حين يكون التجوّل داخل النطاق.",
                "ملاحظات تعود إلى لوحات الرسم حتى لا تبتعد الصورة عن الأبعاد.",
            ]),
            ("p", "DWG وPDF ليسا مسلّم عمل الصور فقط. هما مسلّم خدمات الرسم والرخام التي يمكن طلبها مع الصور. صورة ثابتة واحدة بـ650 درهم، مع 50% مقدماً. اللقطات الإضافية وملف النموذج ومشاهد التجوّل تُسعَّر عند الطلب."),
            ("h", "أين تقع الصور في المراجعة"),
            ("p", "في دبي وأبوظبي والشارقة غالباً ما تكون الصورة ما يعتمده العميل، بينما الرسومات التنفيذية هي ما يعتمده الاستشاري للتصنيع. خلط القرارين يسبب مشكلة: عرق بدا مقبولاً في صورة قد يكون مستحيلاً على الألواح التي وصلت، وصورة بلا خطوط فواصل لا تقول للمصنع أين يقص. حين يكون الاثنان في العرض تُحدَّث الصورة إذا غيّرت الرسومات المعتمدة التصميم، ويُذكر ذلك التحديث في العرض ولا يُفترض. لا يدّعي الاستوديو أن الصورة تسليم لجهة. هي أداة قرار."),
            ("p", "لوحات تناسب دراسة الخامة تشمل %s و%s و%s." % (L["p_lobby"], L["p_bath"], L["p_floor"])),
        ],
        "website-development-designing": [
            ("h", "المواقع، بالأسعار المنشورة فعلاً"),
            ("p", "تطوير المواقع في D3DDD للمقاولين والورش والاستوديوهات التي تحتاج موقعاً واضحاً وطريقة ليرسل الزائر استفساراً. هو منفصل عن الرسومات التنفيذية. عمل الرسم يُسعَّر حسب المشروع. عمل المواقع يستخدم الباقات المذكورة أصلاً في هذا الموقع."),
            ("ul", [
                "البداية: 599 دولاراً كندياً أو 1,200 درهم. صفحة واحدة وتخطيط للجوال ونموذج تواصل وأساسيات SEO.",
                "الأعمال: 999 دولاراً كندياً أو 2,000 درهم. حتى خمس صفحات مع التخطيط نفسه والنموذج وأساسيات SEO. هذه باقة موقع المقاول، 50% مقدماً والباقي عند التسليم.",
                "المميزة: 1,799+ دولاراً كندياً أو 3,500+ درهم. صفحات أكثر وميزات مخصصة، مع الجوال والنموذج وأساسيات SEO. علامة الزائد تعني أن الرقم يتحرك مع الميزات التي تضيفها.",
            ]),
            ("p", "تسجيل النطاق والاستضافة وصور المخزون المدفوعة غير مشمولة إلا إذا كُتب ذلك. دفع هذه الباقات عبر PayPal. الاستفسار في الموقع الجاهز يمكن أن يشير إلى القناة التي ترد عليها فعلاً. موقع الاستوديو نفسه يعرض بريداً يُركَّب في المتصفح ونموذج استفسار، ولا ينشر رقم هاتف."),
            ("h", "ماذا يشمل البناء"),
            ("ul", [
                "بناء متوافقاً مع الجوال للصفحات المتفق عليها.",
                "مسار استفسار: نموذج أو رابط تواصل واضح أو كلاهما.",
                "أساسيات SEO: عناوين وأوصاف وروابط مقروءة. ليس وعداً بترتيب في البحث.",
                "دورة مراجعة واحدة بعد البناء الأول، ثم الإطلاق بعد دفع الباقي.",
                "نماذج يمكن الاطلاع عليها قبل اختيار الاتجاه. هي عينات لا مشاريع عملاء.",
            ]),
            ("p", "لا يوجد مسلّم DWG لموقع. إذا احتجت رسومات أيضاً فأضف %s أو %s إلى الاستفسار نفسه وستُسعَّر وحدها." % (L["marble"], L["draft"])),
            ("h", "كيف يسير عمل الموقع، بما في ذلك بين الإمارات"),
            ("p", "الخطوات واحدة سواء كان النشاط في دبي أو أبوظبي أو الشارقة لأن الموقع يُسلَّم عبر الإنترنت. تدفع العربون 50% وترسل الشعار والنص والصور، تُبنى الصفحات وتراجعها، ويُدفع الباقي حين يصبح الموقع جاهزاً للإطلاق. لا شيء هنا ادّعاء عن قاعدة عرض رخصة تجارية أو تصريح سياحي. إذا كان نشاطك يحتاج تنويهاً معيناً أو رقم رخصة في الصفحة فأرسل الصياغة وستوضع حيث تطلب. المحتوى بالعربية أو الإنجليزية أو باللغتين طلب عادي؛ اذكره من البداية حتى يُصمم التخطيط له، بما في ذلك الصفحات من اليمين إلى اليسار حين تكون العربية اللغة الأساسية."),
            ("p", "تفاصيل الباقة والنماذج المباشرة في %s. عينات الرسم، إذا أردت أن يشير الموقع لاحقاً إلى لوحات حقيقية، تحت %s." % (L["webpkg"], L["projects"])),
        ],
    }
    faqs = {
        "architectural-drafting": [
            ("ماذا يشمل الرسم المعماري التنفيذي؟", "رسومات تنفيذية ولوحات تشطيب ونجارة وتفاصيل أوتوكاد ومخططات كما بُني، بصيغة DWG وPDF. لوحات التصاريح تُعد فقط من قائمة التحقق التي ترسلها، لأن المتطلبات تختلف بين الإمارات والمشاريع."),
            ("كيف تُعالج الملاحظات؟", "ملاحظات الـPDF تُعدَّل في إصدار جديد برقم مراجعة أعلى. موعد ذلك الإصدار يُتفق عليه عند وصول الملاحظات. الموعد الأول هو المكتوب في العرض."),
            ("هل تتبعون معيار طبقات خليجياً؟", "يمكن أن تتبع المجموعة أسماء الطبقات ولوحة العنوان التي تستخدمها. أرسل نموذجاً. ملاحظة عملية عن معايير التشطيب في المدونة إرشاد لا ادّعاء بأن معياراً واحداً إلزامي."),
            ("هل يمكن جمع الحجر والنجارة في عرض واحد؟", "نعم. اذكر ذلك في الاستفسار. لرسومات الرخام صفحة لأن قائمة القص وتوزيع الألواح مسلّم مستقل."),
            ("أي الإمارات؟", "دبي وأبوظبي والشارقة وعجمان ورأس الخيمة وأم القيوين والفجيرة. الملفات تُرسل رقمياً."),
        ],
        "architectural-designing": [
            ("ماذا أستلم من عمل التصميم؟", "خيارات مساقط ومخططاً مطوراً والواجهات أو القطاعات اللازمة لإحاطة الرسومات اللاحقة، بصيغة DWG وPDF. الصور ثلاثية الأبعاد خدمة منفصلة."),
            ("هل هذا تصميم تصريح؟", "فقط إذا كُتبت حزمة التصريح في العرض، وفقط من المتطلبات التي ترسلها. المخطط المفهومي لا يُقدَّم كاعتماد جهة."),
            ("هل يمكن أن يكتمل التصميم رسومات تنفيذية؟", "نعم. ملف DWG هو نقطة بداية الرسم المعماري أو رسومات الرخام، ويُسعَّر الخطوة التالية."),
            ("كم يستغرق التصميم؟", "يُؤكد التاريخ مع العرض. يعتمد على عدد الخيارات واكتمال الرفع أو الموجز."),
            ("هل تعملون بالعربية؟", "الملاحظات والتواصل يمكن أن يكونا بالعربية أو الإنجليزية أو باللغتين."),
        ],
        "architectural-estimation": [
            ("ما هي حزمة حساب الكميات؟", "جدول كميات أو حصر أو جدول مواد أو حزمة طرح مقيسة من مخططاتك مع كتابة الافتراضات. تُسلَّم جدولاً وPDF."),
            ("هل أتعاب الرسم مشمولة؟", "فقط حين تكون المخططات جزءاً من العرض نفسه. حزمة الأرقام وحدها لا تشمل لوحات DWG جديدة."),
            ("هل تتحدث الكميات بعد ملاحظات الاستشاري؟", "نعم حين يكون التحديث مشمولاً. إعادة التصميم الكبيرة تُسعَّر خطوة مستقلة حتى يبقى الجدول مربوطاً بالمراجعة المعتمدة."),
            ("هل يمكن قياس الحجر فقط؟", "نعم. مساحات الألواح وعدد القطع وهدر القص يمكن جدولتها مع رسومات الرخام أو من مخططات لديك."),
            ("هل هناك سعر ثابت؟", "لا. التقدير يُسعَّر لكل حزمة. ليس سعراً منشوراً للمتر أو للصفحة، وليس سعر باقة موقع."),
        ],
        "3d-rendering-modeling-visualization": [
            ("هل الصور تغني عن الرسومات التنفيذية؟", "لا. الصورة تُظهر النية. التصنيع يحتاج رسومات DWG وPDF بأبعاد وفواصل وفتحات."),
            ("ما الملفات التي أستلمها؟", "صوراً PNG أو JPG، وملف نموذج إذا طلبته، وتجولاً إذا كان في العرض. صورة ثابتة واحدة بـ650 درهم مع 50% مقدماً، وما زاد على ذلك يُسعَّر عند الطلب."),
            ("هل يمكن مطابقة رسومات الرخام؟", "نعم حين يُطلب الاثنان. ينبغي أن تتبع الصورة الخامة نفسها ومنطق الفواصل نفسه في اللوحات."),
            ("ماذا تحتاجون مني؟", "مخططات أو كروكي واضح والمواد التي تفكر فيها واللقطات المطلوبة. صور المكان تساعد."),
            ("هل الصورة وثيقة اعتماد؟", "تساعد العميل على القرار. اعتماد الاستشاري للتصنيع يبقى على الرسومات التنفيذية. لا يتعامل الاستوديو مع الصورة كتصريح."),
        ],
        "website-development-designing": [
            ("ماذا تشمل باقة 2,000 درهم؟", "باقة الأعمال حتى خمس صفحات متوافقة مع الجوال مع نموذج تواصل وأساسيات SEO. النصف مقدماً والباقي عند التسليم. النطاق والاستضافة وصور المخزون المدفوعة إضافية إلا باتفاق مكتوب."),
            ("ما أسعار المواقع الأخرى؟", "البداية 1,200 درهم (599 دولاراً كندياً) لصفحة واحدة. المميزة تبدأ من 3,500 درهم (1,799 دولاراً كندياً) وترتفع مع الميزات. خدمات الرسم غير داخلة في هذه الأرقام."),
            ("هل يمكن أن يكون الموقع بالعربية؟", "نعم. اذكر ذلك من البداية. الصفحات العربية أساساً تُرتَّب من اليمين إلى اليسار."),
            ("هل تنشرون رقم هاتف في الموقع الذي تبنونه؟", "فقط إذا أردت ذلك. موقع D3DDD نفسه لا يعرض رقم هاتف. موقعك يمكن أن يستخدم قناة الاستفسار التي ترد عليها."),
            ("كيف يبدأ العمل؟", "عربون 50% ثم الشعار والنص والصور. تراجع البناء ثم يُدفع الباقي عند الإطلاق."),
        ],
    }
    extra = {
        "architectural-drafting": [
            ("h", "ماذا ترسل حتى يبدأ الرسم دون توقف"),
            ("p", "أفضل بداية هي ملفات التصميم التي يعتمدها المشروع الآن، لا نسخة قديمة من مرحلة المفهوم. أرسل المساقط والواجهات والقطاعات التي تغيّر التشطيب، ولوحة العنوان إن كانت مفروضة، وأسماء الطبقات إن كان المنسّق سيفحص الملف. إذا كان الرفع المساحي يختلف عن مخطط المعماري فاذكر أيهما يُعتمد. الفتحات التي تخص الأعمال الصحية والكهرباء — مغسلة، مغناطيس باب، وحدة تكييف مخفية — يجب أن تظهر في الرسم التنفيذي حتى لا يُغلق الجدار ثم يُفتح. إن لم تكن هذه الفتحات معروفة بعد، تُترك اللوحة معلَّمة وتُستكمل في المراجعة التالية بدل تخمين مقاس."),
            ("p", "في دبي يكثر أن يراجع مصمم الديكور الداخلي خطوط النجارة بينما يراجع الاستشاري المعماري القواطع والمناسيب. في أبوظبي يُطلب أحياناً جدول إحالة يربط رقم اللوحة برقم المراجعة. في الشارقة قد يكتفي المشروع بمصمم واحد يعلّق على ملف PDF. لا نكتب هذه الاختلافات كأنها نظام ملزم. هي ما نراه حين يرسل المقاول تعليمات مشروعه، والرسم يتبع تلك التعليمات. إذا وصلت التعليمات متأخرة يصدر الإصدار الأول على لوحة عنوان عادية ثم تُستبدل في المراجعة."),
        ],
        "architectural-designing": [
            ("h", "ماذا نختبر في المخطط قبل أن يُرسم للتصنيع"),
            ("p", "تخطيط المساحة في فيلا إماراتية يختبر أشياء لا تظهر في شقة: مدخل الضيوف ومجلس الرجال ومسار العائلة والمطبخ بالنسبة لغرفة الطعام، وأين يجلس المجلس الخارجي بالنسبة للمسبح. في الشقة يكون الاختبار أبسط: عرض الممر، وفتح باب الحمام على المغسلة، ومكان الخزانة دون إغلاق النافذة. نرسم خيارين حين يكون القرار بينهما حقيقياً، لا خمس نسخ تختلف في تحريك كرسي. الخيار المرفوض يُحفظ في الملف حتى يستطيع العميل العودة إليه، ولا يُحذف بصمت."),
            ("p", "الواجهات في هذه المرحلة ليست رسماً تنفيذياً للحجر. هي ارتفاع تقريبي للظهر والرف والتجويف حتى يعرف صاحب العمل إن كان العنصر يناسبه قبل أن تُقاس كل فتحة. حين يُعتمد الاتجاه تنتقل الأبعاد إلى الرسم التنفيذي أو إلى رسومات الرخام. إن طُلبت صورة ثلاثية الأبعاد في الوقت نفسه نثبت زاوية الكاميرا على المسقط المعتمد حتى لا تُظهر الصورة جداراً غير موجود في المخطط. الموعد يُكتب مع السعر: مسقط شقة ليس كدور أرضي لفيلّا مع فناء."),
            ("p", "نسلّم المخطط المفهومي بصيغة DWG وPDF حتى لا يُعاد رسمه من صورة لاحقاً. إن كان لديك رفع مساحي أو مخطط شقة من المطوّر فأرسله مع الموجز، واذكر إن كان المجلس أو المطبخ هو الفراغ الذي لا تريد التنازل عنه. الخيار الذي لا يُختار يبقى في الملف للرجوع، ولا نعدّه نسخة نهائية. التصميم هنا لا يُقدَّم كتصريح بناء، وإذا احتاج المشروع حزمة تصريح تُذكر وحدها في العرض مع قائمة التحقق التي ترسلها. التواصل في هذه المرحلة بالعربية أو الإنجليزية أو باللغتين، حسب ما تفضّل كتابته على اللوحات."),
        ],
        "architectural-estimation": [
            ("h", "كيف يُراجع الجدول مع اللوحة"),
            ("p", "الجدول الذي لا يشير إلى رقم اللوحة لا يستطيع مراجع آخر فحصه. لذلك يُذكر مصدر كل بند: مسقط الأرضية لبلاط الصالة، واجهة الحمام لتكسية الجدار، جدول القطع لعدد فتحات المغاسل. وحدات القياس تبقى ظاهرة: متر مربع للأرضيات، متر طولي للإزار، عدد للقطع الخاصة. إذا اجتمع حجر ونجارة في المشروع نفسه يبقيان في جدولين حتى لا يسعّر مصنع الرخام هياكل الخزائن. حين يغيّر الاستشاري سماكة الحجر من سنتيمترين إلى ثلاثة، يتغير البند في المراجعة نفسها التي تتغير فيها اللوحة، وإلا ذهب الطلب إلى المورّد على الرقم القديم."),
            ("p", "لا نفرض صيغة مناقصة. بعض المقاولين في دبي وأبوظبي يستخدمون نموذجاً من استشاري المشروع، وبعضهم جدول أعمدة بسيطاً يكفي للمصنع. أرسل النموذج الفارغ مع المخططات إن وُجد. الافتراضات — مثل هدر القص أو عرض الفاصل — تُكتب في رأس الجدول لا داخل الخلية، حتى يستطيع من يسعّر أن يغيرها إن اختلفت سياسة الورشة. التحديث بعد جولة ملاحظات كبيرة يُسعَّر وحده لأن إعادة قياس فيلا كاملة ليست تصحيحاً لخلية واحدة."),
            ("p", "الحصر من رسم غير مكتمل يُعلَّم بما نقص: إن لم تُرسم واجهة حمام بعد، لا نضع رقماً لتكسيتها كأن القياس تم. يمكن إصدار جدول أولي للمناطق المعروفة ثم إكمال الباقي مع المراجعة. هذا أوضح لمصنع الحجر من رقم واحد بلا مصدر. الأسعار المنشورة في الموقع لا تُستخدم هنا؛ أتعاب الحصر تُكتب في العرض حسب عدد اللوحات ونوع البنود، وتُؤكد كتابياً قبل بدء أي قياس فعلي."),
        ],
        "3d-rendering-modeling-visualization": [
            ("h", "ما الذي تثبته الصورة وما الذي لا تثبته"),
            ("p", "الصورة تصلح لقرار الخامة واللون واتجاه العرق وإحساس الفراغ. لا تصلح لقياس فتحة أو فاصل. لذلك نطلب المخطط أو كروكي بأبعاد تقريبية قبل بناء النموذج، ونكتب في العرض عدد اللقطات لا عبارة مفتوحة مثل «صور كافية». لقطة للمجلس، ولقطة للمطبخ، ولقطة تفصيلية لجدار الرخام، ثلاث لقطات بثلاث مدد. إضافة لقطة لاحقة تُسعَّر وحدها. إذا وصلت ألواح الحجر بعد الصورة وتبيّن أن العرق لا يطابق ما رُسم، فالصورة دراسة وليست عقد توريد."),
            ("p", "في مراجعة مشروع في دبي أو أبوظبي أو الشارقة قد يعتمد العميل الصورة في اجتماع، ثم يعتمد الاستشاري الرسومات التنفيذية بعد أسابيع. إن تغيّر ارتفاع الظهر أو مكان التجويف في الرسم المعتمد ولم تُحدَّث الصورة، يعرض الموقع صورة لم تعد صحيحة. حين تكون الصورة والرسم في العرض نفسه نذكر هل تشمل الرسوم تحديث الصورة بعد الاعتماد. الإضاءة في الصورة إضاءة عرض، لا حساب إنارة تنفيذياً، ولا ندّعي أنها تحقق متطلباً لجهة ترخيص."),
            ("p", "الملفات المسلّمة صور PNG أو JPG بالدقة المكتوبة في العرض، وملف النموذج فقط إذا طُلب. صورة ثابتة واحدة في هذه الصفحة بـ650 درهم مع 50% مقدماً، والباقي عند الطلب. أرسل المواد التي تفكر فيها وعدد الفراغات، وإن كانت الألواح قد وصلت فصورها تساعد على تقريب العرق. الصورة أداة قرار للعميل، واعتماد التصنيع يبقى على رسومات DWG وPDF. اذكر المدينة — دبي أو أبوظبي أو الشارقة أو غيرها — في الاستفسار حتى نفهم سياق المراجعة، حتى لو كان تسليم الملفات رقمياً بالكامل ومن دون زيارة للموقع."),
        ],
        "website-development-designing": [
            ("h", "ماذا نحتاج منك قبل بناء الصفحات"),
            ("p", "الشعار، والنص الذي تريد نشره، وصور الأعمال التي تملك حق استخدامها. لا نؤلف أسماء مشاريع ولا أرقاماً عن سنوات خبرة. إن لم يكن النص جاهزاً يمكن أن نرتب العناوين من نقاط ترسلها، ويبقى المعنى ملكك وتراجعه قبل الإطلاق. صفحات العربية من البداية تختلف عن ترجمة تُلصق لاحقاً على تخطيط إنجليزي: الاتجاه من اليمين، وطول السطر، ومكان الزر. اذكر اللغة الأساسية في أول رسالة."),
            ("p", "المراجعة دورة واحدة ضمن الباقة: تجمع ملاحظاتك على الصفحات المبنية، نعدّل، ثم تدفع الباقي عند الجاهزية للإطلاق. تغيير النطاق بعد الموافقة — إضافة متجر أو عشر صفحات جديدة — خارج الباقة ويُكتب عرضه وحده. النطاق والاستضافة تبقى على حسابك ما لم يُتفق كتابة على غير ذلك. الموقع لا يُنشر برقم هاتف إلا إذا أعطيت الرقم. باقات الرسم ليست داخلة في سعر الصفحة."),
        ],
    }
    return _html(list(pages[slug]) + extra.get(slug, []) + list(common_tail)), faqs[slug]

def service_bundle(lang, slug, here, root):
    L = _links(lang, here, root)
    if lang == "en":
        return _service_en(slug, L)
    return _service_ar(slug, L)

def hub_bundle(lang, here, root):
    L = _links(lang, here, root)
    if lang == "en":
        html = _html([
            ("h", "How the five services fit together"),
            ("p", "D3DDD is one studio, so a project can move from a layout to measured drawings to quantities to a picture of the result without changing hands at every step. You do not have to buy all of it. Most enquiries are one service: a stone package, a fit-out set, a bill, a set of stills, or a website. The %s is the right place to send whichever of those you need, with the drawings or the brief attached in the email that the form opens." % L["contact"]),
            ("p", "%s is the fabrication set for marble and other stone: plans, edges, cut-outs, cutting lists and slab layouts, in DWG and PDF. %s is the broader AutoCAD work: shop drawings, joinery, fit-out sheets and as-built records. %s is the earlier plan work, space planning and elevations, still issued as DWG so it can become shop drawings later. %s measures those drawings into a bill or a material schedule. %s produces the stills and walkthroughs people approve before the factory cuts. %s builds the contractor’s own site and publishes the website package prices. A single 3D still render is also a published pack price of 650 AED (50%% upfront); every other drawing or visualization scope is quoted per project." % (L["marble"], L["draft"], L["design"], L["estim"], L["viz"], L["web"])),
            ("h", "Shared deliverables"),
            ("p", "Drawing services are issued as AutoCAD DWG and PDF unless the quote says otherwise. The DWG is editable and layered. The PDF is what a consultant marks up and what a site prints. Spreadsheets are added when the scope includes a cutting list, a bill of quantities or a cost summary. Renders are PNG or JPG. Websites are pages, not drawings. Notes on drawings can be English, Arabic or both."),
            ("h", "A typical path in Dubai, Abu Dhabi or Sharjah"),
            ("p", "A fit-out in any of these emirates usually has two different approvals, and they should not be confused. The client and the interior designer approve the look: the layout, the material, sometimes a render. The project consultant approves the shop drawings for fabrication: dimensions, joints, build-ups and the interfaces between trades. Comments come back on the PDF. The next issue raises the revision. What differs by emirate and by project is the title block, the transmittal, and whether more than one consultant reviews the set. D3DDD follows the checklist you send. The studio does not publish a municipal procedure as if it were the same in every city, and a shop drawing is not a building permit. Where a project also needs a permit package or a BIM submission, that scope is quoted separately. The blog notes on %s and %s describe those topics without turning them into a promise." % (L["b_dubai"], L["b_bim"])),
            ("p", "Turnaround is agreed in the quote, in writing, before drafting starts. It depends on how many rooms or sheets are involved and on how complete the source files are. A comment round is timed when the comments arrive. Missing dimensions pause only the sheets they affect."),
            ("h", "Prices, stated only where they exist"),
            ("p", "Shop drawings, drafting, design and estimation are quoted per project. A single 3D still render is 650 AED, with 50%% upfront; other 3D work is quoted per project. There is no day rate on this site. Website packages are published: Starter AED 1,200 (CAD 599), Business AED 2,000 (CAD 999) for up to five pages, and Premium from AED 3,500 (CAD 1,799). The five-page contractor website is the AED 2,000 package, 50%% upfront. Domain, hosting and paid stock images are extra unless agreed in writing. Details and demo themes are on %s." % L["webpkg"]),
            ("h", "Examples and further reading"),
            ("p", "Look through %s before you send a stone or drafting enquiry: %s, %s, %s and %s are typical sheets. For a written explanation, start with %s, the %s, or %s. %s is the short version of who draws the work." % (L["projects"], L["p_bath"], L["p_floor"], L["p_pool"], L["p_lobby"], L["b_what"], L["b_check"], L["b_std"], L["about"])),
        ])
        faqs = [
            ("Which service should I ask for?", "Stone fabrication drawings: marble shop drawings. General fit-out or joinery CAD: architectural drafting. Layouts before detailing: architectural designing. A bill or take-off: architectural estimation. Pictures: 3D rendering. A company site: website development. If the job spans two of these, say so on the enquiry form."),
            ("What file will I receive?", "Drawings: DWG and PDF. Quantities: a spreadsheet and a PDF. Renders: PNG or JPG. Websites: the live pages agreed in the package. Other formats only if they are written into the quote."),
            ("How does approval work?", "You or your consultant comment on the PDF. The revision is reissued. For shop drawings in Dubai, Abu Dhabi and Sharjah that reviewer is usually the project consultant named in the contract. Send their checklist if you have one. The studio does not issue permits."),
            ("How fast is it?", "The date is confirmed with the quote. It is not a fixed public lead time. Comment rounds and missing site sizes move the later issues."),
            ("What is priced already?", "Website packages are AED 1,200, AED 2,000 and AED 3,500+, with 50% upfront. A single 3D still render is 650 AED, with 50% upfront. All other drawing and 3D work is quoted per project."),
            ("Do you work outside Dubai?", "Yes. Abu Dhabi, Sharjah, Ajman, Ras Al Khaimah, Umm Al Quwain, Fujairah and the rest of the UAE. Delivery is digital."),
        ]
    else:
        html = _html([
            ("h", "كيف تجتمع الخدمات الخمس"),
            ("p", "D3DDD استوديو واحد، فيستطيع المشروع أن ينتقل من مخطط إلى رسومات مقاسة إلى كميات إلى صورة للنتيجة دون تغيير الجهة في كل خطوة. لست مضطراً لشراء الكل. أكثر الاستفسارات خدمة واحدة: حزمة حجر أو مجموعة تشطيب أو جدول أو مجموعة صور أو موقع. %s هو المكان المناسب لإرسال أي منها، مع المخططات أو الموجز في الرسالة التي يفتحها النموذج." % L["contact"]),
            ("p", "%s هي مجموعة تصنيع الرخام والحجر: مساقط وحواف وفتحات وقوائم قص وتوزيع ألواح بصيغة DWG وPDF. %s هو عمل أوتوكاد الأوسع: رسومات تنفيذية ونجارة ولوحات تشطيب ومخططات كما بُني. %s هو عمل المخطط المبكر وتخطيط المساحة والواجهات، ويُسلَّم أيضاً DWG حتى يصبح لاحقاً رسومات تنفيذية. %s يقيس تلك المخططات إلى جدول كميات أو جدول مواد. %s ينتج الصور الثابتة ومشاهد التجوّل التي يعتمدها الناس قبل قص المصنع. %s يبني موقع المقاول نفسه وتنشر فيه أسعار باقات المواقع. صورة ثلاثية الأبعاد واحدة لها سعر منشور هو 650 درهم مع 50%% مقدماً، وكل رسم أو تصور آخر يُسعَّر حسب المشروع." % (L["marble"], L["draft"], L["design"], L["estim"], L["viz"], L["web"])),
            ("h", "مسلّمات مشتركة"),
            ("p", "خدمات الرسم تُسلَّم أوتوكاد DWG وPDF ما لم يقل العرض غير ذلك. DWG قابل للتعديل وذو طبقات. PDF هو ما يعلّم عليه الاستشاري وما يطبعه الموقع. تُضاف الجداول حين يشمل النطاق قائمة قص أو جدول كميات أو ملخص تكلفة. الصور PNG أو JPG. المواقع صفحات لا رسومات. ملاحظات الرسومات يمكن أن تكون بالإنجليزية أو العربية أو باللغتين."),
            ("h", "مسار معتاد في دبي أو أبوظبي أو الشارقة"),
            ("p", "لتشطيب في أي من هذه الإمارات عادة اعتمادان مختلفان، ولا ينبغي الخلط بينهما. العميل ومصمم الديكور يعتمدان الشكل: المخطط والخامة وأحياناً الصورة. استشاري المشروع يعتمد الرسومات التنفيذية للتصنيع: الأبعاد والفواصل والتراكيب ونقاط التقاء الحرف. تعود الملاحظات على PDF. يرفع الإصدار التالي رقم المراجعة. ما يختلف بين الإمارات والمشاريع هو لوحة العنوان وخطاب الإحالة وهل يراجع المجموعة أكثر من استشاري. يتبع D3DDD قائمة التحقق التي ترسلها. لا ينشر الاستوديو إجراء بلدية كأنه واحد في كل مدينة، والرسم التنفيذي ليس تصريح بناء. حيث يحتاج المشروع أيضاً حزمة تصريح أو تسليم BIM يُسعَّر ذلك النطاق منفصلاً. ملاحظات المدونة عن %s و%s تصف هذه الموضوعات من غير أن تحوّلها إلى وعد." % (L["b_dubai"], L["b_bim"])),
            ("p", "يُتفق على موعد التسليم في العرض كتابياً قبل بدء الرسم. يعتمد على عدد الغرف أو اللوحات وعلى اكتمال الملفات المصدر. جولة الملاحظات تُوقَّت عند وصولها. المقاسات الناقصة توقف اللوحات التي تخصها فقط."),
            ("h", "الأسعار، حيث توجد فقط"),
            ("p", "الرسومات التنفيذية والرسم والتصميم وحساب الكميات تُسعَّر حسب المشروع. صورة ثلاثية الأبعاد واحدة بـ650 درهم مع 50%% مقدماً، وما زاد من الصور يُسعَّر حسب المشروع. لا يوجد سعر يوم في هذا الموقع. باقات المواقع منشورة: البداية 1,200 درهم (599 دولاراً كندياً)، والأعمال 2,000 درهم (999 دولاراً كندياً) حتى خمس صفحات، والمميزة من 3,500 درهم (1,799 دولاراً كندياً). موقع المقاول من خمس صفحات هو باقة 2,000 درهم، 50%% مقدماً. النطاق والاستضافة وصور المخزون المدفوعة إضافية إلا باتفاق مكتوب. التفاصيل والنماذج في %s." % L["webpkg"]),
            ("h", "أمثلة وقراءة إضافية"),
            ("p", "راجع %s قبل إرسال استفسار حجر أو رسم: %s و%s و%s و%s لوحات نموذجية. لشرح مكتوب ابدأ بـ%s أو %s أو %s. %s نسخة قصيرة عمّن يرسم العمل. المدونة بالإنجليزية." % (L["projects"], L["p_bath"], L["p_floor"], L["p_pool"], L["p_lobby"], L["b_what"], L["b_check"], L["b_std"], L["about"])),
        ])
        faqs = [
            ("أي خدمة أطلب؟", "رسومات تصنيع الحجر: رسومات الرخام. أوتوكاد عام للتشطيب أو النجارة: الرسم المعماري. مخططات قبل التفصيل: التصميم المعماري. جدول أو حصر: حساب الكميات. صور: التصميم ثلاثي الأبعاد. موقع شركة: تطوير المواقع. إذا امتد العمل إلى خدمتين فاذكر ذلك في النموذج."),
            ("أي ملف سأستلم؟", "الرسومات: DWG وPDF. الكميات: جدولاً وPDF. الصور: PNG أو JPG. المواقع: الصفحات المتفق عليها في الباقة. الصيغ الأخرى فقط إذا كُتبت في العرض."),
            ("كيف يتم الاعتماد؟", "تبدي أنت أو استشاريك الملاحظات على PDF. يُعاد إصدار المراجعة. في الرسومات التنفيذية في دبي وأبوظبي والشارقة يكون المراجع عادة استشاري المشروع المسمى في العقد. أرسل قائمة التحقق إن وُجدت. الاستوديو لا يصدر تصاريح."),
            ("ما سرعة التسليم؟", "يُؤكد التاريخ مع العرض. ليست مدة عامة ثابتة. جولات الملاحظات ومقاسات الموقع الناقصة تحرّك الإصدارات اللاحقة."),
            ("ما المسعّر مسبقاً؟", "باقات المواقع: 1,200 و2,000 و3,500+ درهم مع 50% مقدماً. صورة ثلاثية الأبعاد واحدة بـ650 درهم مع 50% مقدماً. كل رسم أو تصور آخر يُسعَّر حسب المشروع."),
            ("هل تعملون خارج دبي؟", "نعم. أبوظبي والشارقة وعجمان ورأس الخيمة وأم القيوين والفجيرة وبقية الإمارات. التسليم رقمي."),
        ]
    return html, faqs

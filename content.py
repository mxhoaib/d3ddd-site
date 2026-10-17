# Page content for English and Arabic. Used by build.py.
def build_pages(g):
    shell, img, cta, page_hero, faq_html, faq_ld = g["shell"], g["img"], g["cta"], g["page_hero"], g["faq_html"], g["faq_ld"]
    crumbs_ld, service_ld, url, T, WA = g["crumbs_ld"], g["service_ld"], g["url"], g["T"], None
    out = {}
    THEMES=[('carpentry-joinery', 'Carpentry & Joinery', 'النجارة والأعمال الخشبية'), ('marble-stone', 'Marble & Stone', 'الرخام والحجر'), ('fitout-interiors', 'Fit-out & Interiors', 'التشطيبات الداخلية'), ('contracting-construction', 'Contracting & Construction', 'المقاولات والبناء'), ('engineering-consultants', 'Engineering Consultants', 'الاستشارات الهندسية'), ('trading', 'Trading', 'التجارة'), ('interior-designers', 'Interior Designers', 'مصممو الديكور الداخلي')]
    PP='https://paypal.me/imshoi'
    def demos(lang):
        en=lang=="en"
        cards="".join(f'<a class="card" href="https://mxhoaib.github.io/d3ddd-demos/{k}/" target="_blank" rel="noopener"><div class="b"><span class="num">{"DEMO" if en else "نموذج"} {i+1:02d}</span><h3>{e if en else a}</h3><p>{"View live demo theme ↗" if en else "شاهد النموذج المباشر ↗"}</p></div></a>' for i,(k,e,a) in enumerate(THEMES))
        h=("Demo themes","Website demo themes for UAE contractors","Live sample websites by trade — pick a theme and we tailor it to your brand.") if en else ("نماذج التصاميم","نماذج مواقع للمقاولين في الإمارات","مواقع تجريبية مباشرة حسب التخصص — اختر النموذج ونخصصه لعلامتك التجارية.")
        return f'<section class="section" id="demos" aria-labelledby="demos-h"><div class="wrap"><p class="eyebrow">{h[0]}</p><h2 id="demos-h">{h[1]}</h2><p style="color:var(--muted);margin:10px 0 30px">{h[2]}</p><div class="grid g4">{cards}</div></div></section>'
    def packages(lang):
        if lang=="en":
            return f'''<section class="section alt" id="packages" aria-labelledby="pkg-h"><div class="wrap"><p class="eyebrow">Packages</p><h2 id="pkg-h" style="margin-bottom:30px">Website, shop drawing &amp; 3D render packages</h2><div class="grid g2">
<div class="card"><div class="b"><p class="eyebrow">Contractor Website</p><p class="price">AED 2,000 <small>approx. CAD 750</small></p><p>5-page mobile-friendly website, enquiry form and SEO basics. 50% (AED 1,000) upfront, balance on completion.</p><div class="actions" style="margin-top:18px"><a class="btn" href="{PP}" target="_blank" rel="noopener">Pay deposit via PayPal</a><a class="btn ghost" href="website-design.html">Package details</a></div></div></div>
<div class="card"><div class="b"><p class="eyebrow">Shop drawings &amp; 3D renders</p><p class="price" style="font-size:30px">Quoted per project</p><p>Marble &amp; stone shop drawings, AutoCAD drafting, fit-out drawings and 3D renders, priced on scope. Send your drawings for a quote.</p><div class="actions" style="margin-top:18px"><a class="btn ghost" href="contact.html">Request a quote</a></div></div></div></div>
<p style="color:var(--muted);font-size:13px;margin-top:16px">Payments are processed by PayPal. Please put your name or invoice reference in the PayPal note.</p></div></section>'''
        return f'''<section class="section alt" id="packages" aria-labelledby="pkg-h"><div class="wrap"><p class="eyebrow">الباقات</p><h2 id="pkg-h" style="margin-bottom:30px">باقات المواقع والرسومات التنفيذية والتصميم ثلاثي الأبعاد</h2><div class="grid g2">
<div class="card"><div class="b"><p class="eyebrow">باقة موقع المقاولين</p><p class="price">2,000 درهم <small dir="ltr">approx. CAD 750</small></p><p>موقع من 5 صفحات متوافق مع الجوال مع نموذج استفسار وأساسيات SEO. 50% (1,000 درهم) مقدماً والباقي عند التسليم.</p><div class="actions" style="margin-top:18px"><a class="btn" href="{PP}" target="_blank" rel="noopener">ادفع العربون عبر PayPal</a><a class="btn ghost" href="website-design.html">تفاصيل الباقة</a></div></div></div>
<div class="card"><div class="b"><p class="eyebrow">الرسومات التنفيذية والتصميم ثلاثي الأبعاد</p><p class="price" style="font-size:30px">حسب المشروع</p><p>رسومات الرخام والحجر التنفيذية ومخططات أوتوكاد ورسومات التشطيبات والتصميم ثلاثي الأبعاد، بسعر حسب نطاق العمل. أرسل مخططاتك للحصول على عرض سعر.</p><div class="actions" style="margin-top:18px"><a class="btn ghost" href="contact.html">اطلب عرض سعر</a></div></div></div></div>
<p style="color:var(--muted);font-size:13px;margin-top:16px">تتم المدفوعات عبر PayPal. يرجى كتابة اسمك أو رقم الفاتورة في ملاحظة الدفع.</p></div></section>'''
    def bc(lang, fn, name): return crumbs_ld(lang, [(T[lang]["home"], url(lang, "index.html")), (name, url(lang, fn))])
    WEB_OFFER = {"@type": "Offer", "price": "2000", "priceCurrency": "AED", "description": "Contractor Website – 5 pages, 50% upfront"}

    # =============================== ENGLISH ===============================
    L = "en"; P = ""
    faq_en = [
     ("What are marble shop drawings?", "Marble shop drawings are detailed fabrication and installation drawings for stone works — plans, elevations, sections, joint layouts, edge profiles, cut-outs, thickness and finish — prepared so fabricators and site teams in Dubai and the UAE can cut and install accurately."),
     ("Which areas of the UAE do you serve?", "We work with contractors, fabricators, consultants and designers in Dubai, Abu Dhabi, Sharjah, Ajman, Ras Al Khaimah and across the UAE. Most work is delivered digitally, so location is not a barrier."),
     ("What file formats do you deliver?", "AutoCAD DWG and PDF drawing sets as standard. 3D renderings are delivered as high-resolution images. Other formats can be discussed when you request a quote."),
     ("What do I need to send for a quote?", "Architectural or interior drawings, sketches, site dimensions, photos or a short description of the scope and deadline. Send them through the enquiry form on our contact page or by email to info@d3ddd.com."),
     ("Do you provide drawings in Arabic?", "Yes. We communicate in English and Arabic, and drawing notes can be prepared in English, Arabic or both."),
     ("How much does a contractor website cost?", "Our Contractor Website package is AED 2,000 for a 5-page, mobile-friendly website with WhatsApp button and enquiry form. 50% is paid upfront and the balance on completion."),
    ]
    body = f'''
<section class="hero" aria-labelledby="h1"><div><p class="eyebrow">🇦🇪 Dubai • Abu Dhabi • Sharjah • UAE</p>
<h1 id="h1">Shop drawings &amp; 3D design in Dubai — ideas into <em>precise</em> spaces.</h1><span class="ar-touch" lang="ar">رسومات تنفيذية وتصميم ثلاثي الأبعاد في دبي</span>
<p class="lead">Marble &amp; stone shop drawings, AutoCAD drafting, fit-out drawings and 3D rendering for contractors, fabricators, consultants and designers across the UAE.</p>
<div class="actions"><a class="btn" href="contact.html">Request a quote →</a><a class="btn ghost" href="services.html">Explore services</a></div></div>
<figure>{img(P,"hero-marble-kitchen","Isometric line drawing of a marble kitchen island with waterfall edge, pendant lights and dimension lines",True,520,420)}</figure></section>
<section class="section" aria-labelledby="svc-h"><div class="wrap"><div class="split"><div><p class="eyebrow">Design • Detail • Deliver</p><h2 id="svc-h">Marble shop drawings, AutoCAD drafting &amp; 3D rendering — one <em>UAE studio.</em></h2></div>
<div><p>D3DDD combines technical drafting with visual design and real-world marble and fit-out knowledge. The result is documentation that looks refined and works on site — from a single vanity detail to a complete interior visualization package.</p></div></div>
<div class="grid g4" style="margin-top:50px">
<a class="card" href="marble.html"><figure>{img(P,"marble-shop-drawing","Marble countertop shop drawing with sink cut-out, dimensions, veining and edge section")}</figure><div class="b"><span class="num">01</span><h3>Marble &amp; Stone Shop Drawings</h3><p>Shop drawings, cutting lists, fabrication details and BOQ for stone works.</p></div></a>
<a class="card" href="services.html#drafting"><figure>{img(P,"elevation","Wall elevation line drawing with joinery, arched niche and dimension")}</figure><div class="b"><span class="num">02</span><h3>AutoCAD Drafting &amp; Fit-out Drawings</h3><p>Plans, elevations, sections and construction-ready DWG documentation.</p></div></a>
<a class="card" href="services.html#3d"><figure>{img(P,"sofa","Line drawing of a three-seat sofa in front elevation")}</figure><div class="b"><span class="num">03</span><h3>3D Rendering &amp; Visualization</h3><p>Realistic interior and exterior concepts before work starts on site.</p></div></a>
<a class="card" href="website-design.html"><figure>{img(P,"web-wireframe","Website wireframe drawing: browser layout, mobile view and HTML code")}</figure><div class="b"><span class="num">04</span><h3>Website Design for Contractors</h3><p>5-page website with WhatsApp button — AED 2,000.</p></div></a>
</div></div></section>
<section class="section alt" aria-labelledby="how-h"><div class="wrap"><p class="eyebrow">How we work</p><h2 id="how-h" style="margin-bottom:40px">Send. Review. Draft. <em>Deliver.</em></h2>
<ol class="steps"><li>Send drawings</li><li>We review</li><li>Draft</li><li>You approve</li><li>Deliver DWG / PDF</li></ol>
<div class="tags"><span>COUNTERTOPS</span><span>VANITIES</span><span>STAIRCASES</span><span>WALL CLADDING</span><span>FLOORING</span><span>KITCHEN ISLANDS</span><span>FIREPLACES</span><span>WATERJET INLAYS</span></div></div></section>
<section class="section" aria-labelledby="why-h"><div class="wrap"><h2 id="why-h" style="margin-bottom:30px">Why contractors in the UAE choose D3DDD</h2><div class="grid g3">
<div class="card"><div class="b"><h3>📐 UAE-standard workflow</h3><p>Drawing sets structured for contractor, consultant and fabricator coordination in the UAE.</p></div></div>
<div class="card"><div class="b"><h3>🌐 English &amp; Arabic</h3><p>We communicate and annotate in English and Arabic. <span lang="ar">نتواصل بالعربية والإنجليزية.</span></p></div></div>
<div class="card"><div class="b"><h3>💳 Simple PayPal payments</h3><p>Pay your website deposit or project invoices securely through PayPal.</p></div></div></div>
<p class="areas" style="margin-top:30px"><strong>Areas served:</strong> Dubai, Abu Dhabi, Sharjah, Ajman, Ras Al Khaimah, Umm Al Quwain, Fujairah — across the UAE.</p></div></section>
{demos("en")}{packages("en")}{faq_html(faq_en,"Frequently asked questions","FAQ")}{cta(L)}'''
    out[(L,"index.html")] = shell(L,"index.html","Shop Drawings Dubai | Marble Shop Drawings, AutoCAD Drafting & 3D Rendering UAE – D3DDD",
        "D3DDD: marble & stone shop drawings, AutoCAD drafting, fit-out drawings and 3D rendering in Dubai, Abu Dhabi & Sharjah. Request a fast quote online.",
        body,[faq_ld(faq_en),{"@type":"WebSite","@id":url(L,"index.html")+"#website","url":url(L,"index.html"),"name":"D3DDD","inLanguage":"en-AE","publisher":{"@id":g["ORG_ID"]}}],preload="hero-marble-kitchen")

    name="Services"
    body = page_hero(L,"Services — Dubai &amp; UAE","Shop drawings, AutoCAD drafting, 3D rendering &amp; <em>website design</em> in the UAE","Practical documentation and visuals for interiors, fit-outs and premium spaces in Dubai, Abu Dhabi, Sharjah and across the Emirates. <span lang=\"ar\" class=\"ar-touch\">خدماتنا في جميع أنحاء الإمارات</span>",name) + f'''
<section class="section" id="marble"><div class="wrap split"><figure>{img(P,"marble-shop-drawing","Marble vanity top shop drawing with joint, sink cut-out and section A–A")}</figure><div><span class="num">01</span><h2>Marble &amp; Stone Shop Drawings</h2><p>Build-ready shop drawings with dimensions, sections, elevations, material specifications and coordinated details, plus cutting lists, fabrication drawings and estimation.</p><ul class="check"><li>Shop &amp; fabrication drawings</li><li>Cutting lists &amp; slab layouts</li><li>Quantity takeoffs &amp; BOQ</li></ul><p><a class="btn" href="marble.html">Marble shop drawings in detail →</a></p></div></div></section>
<section class="section alt" id="drafting"><div class="wrap split"><div><span class="num">02</span><h2>AutoCAD Drafting &amp; Fit-out Drawings</h2><p>Plans, elevations, sections, details and construction-ready AutoCAD (DWG) documentation for residential and commercial interiors and fit-out projects.</p><ul class="check"><li>Space planning &amp; furniture layouts</li><li>Joinery &amp; fit-out details</li><li>Ceiling, flooring &amp; wall elevations</li><li>DWG and PDF deliverables</li></ul></div><figure>{img(P,"elevation","AutoCAD-style wall elevation drawing with joinery units and niche")}</figure></div></section>
<section class="section" id="3d"><div class="wrap split"><figure>{img(P,"kitchen","Kitchen cabinet elevation line drawing for 3D visualization")}</figure><div><span class="num">03</span><h2>3D Rendering &amp; Visualization</h2><p>Realistic interior and exterior 3D renderings that help clients and approvers see the finished space before work starts.</p><ul class="check"><li>Interior 3D renders</li><li>Material &amp; finish options</li><li>Marble feature concepts</li><li>Presentation visuals</li></ul></div></div></section>
<section class="section alt" id="web"><div class="wrap split"><div><span class="num">04</span><h2>Website Design for Contractors</h2><p>Fast, mobile-friendly websites for contractors and fit-out companies in the UAE, with WhatsApp enquiries built in.</p><p class="price" style="margin-top:16px">AED 2,000 <small>Contractor Website · 50% upfront</small></p><p><a class="btn" href="website-design.html">See the package →</a></p></div><figure>{img(P,"web-wireframe","Browser and mobile wireframe drawing with HTML code for a contractor website")}</figure></div></section>{cta(L)}'''
    out[(L,"services.html")] = shell(L,"services.html","Services | Shop Drawings, AutoCAD Drafting, 3D Rendering & Websites in Dubai – D3DDD",
        "Marble shop drawings, AutoCAD drafting, fit-out drawings, 3D rendering and contractor website design for Dubai, Abu Dhabi, Sharjah and the UAE.",body,
        [bc(L,"services.html",name),service_ld("Marble and stone shop drawings","Marble and stone shop drawings, cutting lists and fabrication drawings.",url(L,"marble.html")),
         service_ld("AutoCAD drafting and fit-out drawings","Construction-ready AutoCAD drawings for interiors and fit-out.",url(L,"services.html")+"#drafting"),
         service_ld("3D rendering","Interior and exterior 3D visualization.",url(L,"services.html")+"#3d"),
         service_ld("Contractor website design","5-page contractor website with WhatsApp button.",url(L,"website-design.html"),WEB_OFFER)])

    name="Marble Shop Drawings"
    body = page_hero(L,"🇦🇪 Complete marble documentation","Marble &amp; stone shop drawings in Dubai &amp; the <em>UAE</em>","Shop drawings, cutting lists, fabrication drawings, designing and BOQ for marble and stone works — for contractors and fabricators in Dubai, Abu Dhabi and Sharjah. <span lang=\"ar\" class=\"ar-touch\">رسومات الرخام والحجر التنفيذية</span>",name) + f'''
<section class="section"><div class="wrap"><div class="split" style="margin-bottom:50px"><figure>{img(P,"marble-shop-drawing","Marble countertop shop drawing: plan, joint, sink cut-out, dimensions and edge profile section")}</figure><div><h2>One partner. <em>Every detail.</em></h2><p>Everything your marble project needs between design, quantity, fabrication and execution, prepared as clean AutoCAD drawing sets.</p></div></div>
<div class="grid g3">
<div class="card"><div class="b"><h3>📐 Shop Drawings</h3><p>Plans, elevations, sections and enlarged details with dimensions, stone type, thickness, edge profile and finish.</p></div></div>
<div class="card"><div class="b"><h3>📋 Cutting Lists</h3><p>Piece schedules and slab layouts planned to reduce waste and simplify fabrication.</p></div></div>
<div class="card"><div class="b"><h3>⚙️ Fabrication Drawings</h3><p>Tolerances, profiles, joints, mitres and CNC / waterjet information for manufacturing and installation.</p></div></div>
<div class="card"><div class="b"><h3>✨ Marble Designing</h3><p>2D layouts and 3D concepts, material selection and bookmatching or pattern guidance.</p></div></div>
<div class="card"><div class="b"><h3>🧮 Estimation &amp; BOQ</h3><p>Quantity takeoffs, rate analysis and Excel-ready cost summaries.</p></div></div>
<div class="card"><div class="b"><h3>🤝 Project Support</h3><p>Coordination with contractors, consultants and fabricators from concept to execution.</p></div></div></div></div></section>
<section class="section alt"><div class="wrap split"><figure>{img(P,"cladding","Bookmatched marble wall cladding elevation drawing with veining")}</figure><div><p class="eyebrow">Every cut starts with a clear drawing</p><h2>Applications</h2><div class="tags"><span>COUNTERTOPS</span><span>VANITIES</span><span>STAIRCASES</span><span>WALL CLADDING</span><span>FLOORING</span><span>KITCHEN ISLANDS</span><span>FIREPLACES</span><span>WATERJET INLAYS</span></div>
<h3 style="margin-top:36px">Process</h3><ol class="steps" style="margin-top:14px"><li>Send</li><li>Review</li><li>Draft</li><li>Approve</li><li>Fabricate</li><li>Install</li></ol></div></div></section>{cta(L)}'''
    out[(L,"marble.html")] = shell(L,"marble.html","Marble Shop Drawings Dubai | Stone Shop Drawings, Cutting Lists & BOQ UAE – D3DDD",
        "Marble and stone shop drawings in Dubai, Abu Dhabi and Sharjah: fabrication drawings, cutting lists, slab layouts and BOQ in AutoCAD DWG/PDF.",body,
        [bc(L,"marble.html",name),service_ld("Marble and stone shop drawings","Shop drawings, cutting lists, fabrication drawings and BOQ for marble and stone works in the UAE.",url(L,"marble.html"))])

    name="Website Design"
    body = page_hero(L,"Website design for contractors — UAE","Contractor website design in Dubai — <em>AED 2,000</em>","A professional 5-page website that turns visitors into WhatsApp enquiries. <span lang=\"ar\" class=\"ar-touch\">تصميم مواقع للمقاولين</span>",name) + f'''
<section class="section"><div class="wrap split"><div class="card"><div class="b"><p class="eyebrow">Contractor Website</p><p class="price">AED 2,000 <small>approx. CAD 750</small></p><p>50% (AED 1,000) upfront to start, 50% balance on completion before go-live.</p>
<ul class="check"><li>5 pages: Home, Services, Projects, About, Contact</li><li>Contact buttons &amp; email links</li><li>Enquiry form</li><li>Mobile-responsive design</li><li>SEO basics: titles, descriptions, sitemap</li><li>Connect your existing domain</li></ul>
<div class="actions" style="margin-top:20px"><a class="btn" href="https://paypal.me/imshoi" target="_blank" rel="noopener">Pay deposit via PayPal</a><a class="btn ghost" href="contact.html">Start your website</a><a class="btn ghost" href="mailto:info@d3ddd.com?subject=Contractor%20Website%20package">Ask by email</a></div></div></div>
<div><figure>{img(P,"web-wireframe","Website wireframe: desktop browser layout, mobile screen and HTML code")}</figure><h3 style="margin-top:24px">How it works</h3><ol class="steps" style="margin-top:14px"><li>50% deposit</li><li>Send content</li><li>We build</li><li>You review</li><li>Balance &amp; go live</li></ol><p class="notice" style="margin-top:24px">Domain registration, hosting fees and paid stock imagery, if needed, are not included unless agreed in writing.</p></div></div></section>'''
    body += demos(L)
    out[(L,"website-design.html")] = shell(L,"website-design.html","Contractor Website Design Dubai | 5-Page Website AED 2,000 – D3DDD",
        "Website design for contractors in Dubai & the UAE: 5 pages, WhatsApp button, enquiry form and SEO basics for AED 2,000 (50% upfront).",body,
        [bc(L,"website-design.html",name),service_ld("Contractor website design","5-page mobile-friendly contractor website with WhatsApp button and enquiry form.",url(L,"website-design.html"),WEB_OFFER)])

    name="About"
    body = page_hero(L,"About D3DDD","A Dubai design &amp; drafting studio built for <em>real projects.</em>","Dubai 3D Design &amp; Draft — technical drafting, 3D visualization and marble know-how under one roof. <span lang=\"ar\" class=\"ar-touch\">استوديو تصميم ورسم هندسي في دبي</span>",name) + f'''
<section class="section"><div class="wrap split"><figure>{img(P,"table","Isometric line drawing of a dining table")}</figure><div><h2>Our approach</h2><p>D3DDD — Dubai 3D Design &amp; Draft — combines technical drafting with visual design and hands-on marble and fit-out knowledge.</p><p>We work with contractors, fabricators, consultants, interior designers and project teams across the UAE, preparing documentation that is clean, organized and practical to use on site.</p><ul class="check"><li>Precision: accurate dimensions and annotations</li><li>Clarity: organized sheets for easy coordination</li><li>Responsiveness: quick replies by email in English &amp; Arabic</li></ul></div></div></section>{cta(L)}'''
    out[(L,"about.html")] = shell(L,"about.html","About D3DDD | Dubai 3D Design & Draft – Drafting & Shop Drawing Studio UAE",
        "D3DDD is a Dubai drafting and design studio for marble shop drawings, AutoCAD drafting and 3D rendering, serving contractors across the UAE in English and Arabic.",body,[bc(L,"about.html",name)])

    name="Contact"
    body = page_hero(L,"Get a quote — Dubai &amp; UAE","Contact D3DDD for shop drawings, drafting &amp; <em>3D rendering</em>","Send drawings, sketches, dimensions or requirements. We reply by email, in English or Arabic. <span lang=\"ar\" class=\"ar-touch\">تواصل معنا للحصول على عرض سعر</span>",name) + f'''
<section class="section"><div class="wrap split" style="align-items:start"><div>
<form class="enquiry card" style="padding:28px" name="enquiry" method="post" action="mailto:info@d3ddd.com?subject=Website%20enquiry" enctype="text/plain">
<p class="hp"><label>Leave empty <input name="company_website"></label></p>
<div class="row"><div><label for="n">Name *</label><input id="n" name="name" required autocomplete="name"></div><div><label for="p">Phone (optional)</label><input id="p" name="phone" type="tel" autocomplete="tel"></div></div>
<div class="row"><div><label for="e">Email *</label><input id="e" name="email" type="email" required autocomplete="email"></div><div><label for="s">Service</label><select id="s" name="service"><option>Marble / stone shop drawings</option><option>Cutting lists / fabrication drawings</option><option>Estimation / BOQ</option><option>AutoCAD drafting / fit-out drawings</option><option>3D rendering</option><option>Contractor Website (AED 2,000)</option><option>Other</option></select></div></div>
<label for="m">Project details *</label><textarea id="m" name="message" required placeholder="Scope, location (e.g. Dubai, Abu Dhabi), deadline…"></textarea>
<p class="notice" style="margin-top:14px">Sending opens your email app with the details filled in. Attach drawings to that email before sending, or email us directly at <a href="mailto:info@d3ddd.com"><u>info@d3ddd.com</u></a>.</p>
<div class="actions" style="margin-top:18px"><button class="btn" type="submit">Send enquiry by email</button></div></form></div>
<div><h2 style="font-size:26px">Direct contact</h2><ul class="check"><li><a href="mailto:info@d3ddd.com">info@d3ddd.com</a></li><li>Dubai, United Arab Emirates — serving the whole UAE</li></ul></div></div></section>'''
    out[(L,"contact.html")] = shell(L,"contact.html","Contact D3DDD | Shop Drawings & 3D Rendering Quote Dubai & UAE",
        "Get a quote for marble shop drawings, AutoCAD drafting, fit-out drawings, 3D rendering or a contractor website in Dubai and the UAE.",body,[bc(L,"contact.html",name),{"@type":"ContactPage","url":url(L,"contact.html"),"about":{"@id":g["ORG_ID"]}}])
    out[(L,"thank-you.html")] = shell(L,"thank-you.html","Thank you | D3DDD","Your enquiry has been received.",
        '<section class="page-hero" style="min-height:60vh"><p class="eyebrow">Received</p><h1>Thank you.</h1><p>We’ll reply shortly. You can also email us at info@d3ddd.com.</p><p style="margin-top:24px"><a class="btn" href="./">Back to home</a></p></section>',(),True,False)

    # =============================== ARABIC ===============================
    L = "ar"; P = "../"
    faq_ar = [
     ("ما هي الرسومات التنفيذية للرخام؟", "الرسومات التنفيذية للرخام (Shop Drawings) هي مخططات تفصيلية للتصنيع والتركيب تشمل المساقط والواجهات والقطاعات وتوزيع الفواصل وتشطيب الحواف والفتحات والسماكات، ليتمكن المصنع وفريق الموقع في دبي والإمارات من القص والتركيب بدقة."),
     ("ما هي المناطق التي تخدمونها في الإمارات؟", "نعمل مع المقاولين ومصانع الرخام والاستشاريين والمصممين في دبي وأبوظبي والشارقة وعجمان ورأس الخيمة وجميع أنحاء الإمارات، ومعظم الأعمال تُسلَّم إلكترونياً."),
     ("ما صيغ الملفات التي تسلمونها؟", "نسلّم مخططات أوتوكاد بصيغة DWG وملفات PDF بشكل أساسي، والتصاميم ثلاثية الأبعاد كصور عالية الدقة. يمكن مناقشة صيغ أخرى عند طلب عرض السعر."),
     ("ماذا أرسل للحصول على عرض سعر؟", "أرسل المخططات المعمارية أو الداخلية أو الرسومات الأولية أو مقاسات الموقع أو الصور مع وصف مختصر للمطلوب والموعد النهائي، عبر نموذج الاستفسار في صفحة التواصل أو البريد info@d3ddd.com."),
     ("هل تقدمون الرسومات باللغة العربية؟", "نعم، نتواصل بالعربية والإنجليزية، ويمكن كتابة ملاحظات المخططات بالعربية أو الإنجليزية أو باللغتين."),
     ("كم تكلفة موقع إلكتروني للمقاول؟", "باقة موقع المقاولين بسعر 2,000 درهم إماراتي لموقع من 5 صفحات متوافق مع الجوال مع زر واتساب ونموذج استفسار، تُدفع 50% مقدماً والباقي عند التسليم."),
    ]
    body = f'''
<section class="hero" aria-labelledby="h1"><div><p class="eyebrow">🇦🇪 دبي • أبوظبي • الشارقة • الإمارات</p>
<h1 id="h1">رسومات تنفيذية وتصميم ثلاثي الأبعاد في دبي — نحوّل الأفكار إلى مساحات <em>دقيقة</em>.</h1>
<p class="lead">رسومات الرخام والحجر التنفيذية، مخططات أوتوكاد، رسومات أعمال التشطيبات الداخلية (فيت آوت) وتصميم ثلاثي الأبعاد للمقاولين ومصانع الرخام والاستشاريين والمصممين في جميع أنحاء الإمارات.</p>
<div class="actions"><a class="btn" href="contact.html">اطلب عرض سعر ←</a><a class="btn ghost" href="services.html">تعرّف على خدماتنا</a></div></div>
<figure>{img(P,"hero-marble-kitchen","رسم خطي أيزومتري لجزيرة مطبخ من الرخام مع إنارة معلّقة وخطوط أبعاد",True,520,420)}</figure></section>
<section class="section" aria-labelledby="svc-h"><div class="wrap"><div class="split"><div><p class="eyebrow">تصميم • تفاصيل • تسليم</p><h2 id="svc-h">رسومات الرخام ومخططات أوتوكاد والتصميم ثلاثي الأبعاد — استوديو <em>واحد</em> في الإمارات.</h2></div>
<div><p>يجمع D3DDD بين الرسم الهندسي الفني والتصميم البصري والخبرة العملية في أعمال الرخام والتشطيبات، لنقدّم مخططات أنيقة وعملية في الموقع — من تفصيلة مغسلة واحدة إلى مشروع تصميم داخلي متكامل.</p></div></div>
<div class="grid g4" style="margin-top:50px">
<a class="card" href="marble.html"><figure>{img(P,"marble-shop-drawing","رسم تنفيذي لسطح رخام مع فتحة مغسلة وأبعاد وعروق الرخام وقطاع الحافة")}</figure><div class="b"><span class="num">01</span><h3>رسومات الرخام والحجر التنفيذية</h3><p>رسومات تنفيذية وقوائم قص وتفاصيل تصنيع وجداول كميات لأعمال الحجر.</p></div></a>
<a class="card" href="services.html#drafting"><figure>{img(P,"elevation","رسم واجهة جدار مع خزائن وتجويف مقوّس وأبعاد")}</figure><div class="b"><span class="num">02</span><h3>مخططات أوتوكاد ورسومات التشطيبات</h3><p>مساقط وواجهات وقطاعات ومخططات DWG جاهزة للتنفيذ.</p></div></a>
<a class="card" href="services.html#3d"><figure>{img(P,"sofa","رسم خطي لأريكة ثلاثية بواجهة أمامية")}</figure><div class="b"><span class="num">03</span><h3>تصميم ثلاثي الأبعاد (3D)</h3><p>تصورات واقعية للمساحات الداخلية والخارجية قبل بدء التنفيذ.</p></div></a>
<a class="card" href="website-design.html"><figure>{img(P,"web-wireframe","رسم تخطيطي لموقع إلكتروني: متصفح وشاشة جوال وكود HTML")}</figure><div class="b"><span class="num">04</span><h3>تصميم مواقع للمقاولين</h3><p>موقع من 5 صفحات مع زر واتساب — 2,000 درهم.</p></div></a>
</div></div></section>
<section class="section alt" aria-labelledby="how-h"><div class="wrap"><p class="eyebrow">طريقة العمل</p><h2 id="how-h" style="margin-bottom:40px">أرسل. نراجع. نرسم. <em>نسلّم.</em></h2>
<ol class="steps"><li>أرسل المخططات</li><li>نراجعها</li><li>نرسم</li><li>توافق عليها</li><li>نسلّم DWG / PDF</li></ol>
<div class="tags"><span>أسطح المطابخ</span><span>المغاسل</span><span>الدرج</span><span>تكسية الجدران</span><span>الأرضيات</span><span>جزر المطبخ</span><span>المدافئ</span><span>تطعيم الووترجت</span></div></div></section>
<section class="section" aria-labelledby="why-h"><div class="wrap"><h2 id="why-h" style="margin-bottom:30px">لماذا يختار المقاولون في الإمارات D3DDD</h2><div class="grid g3">
<div class="card"><div class="b"><h3>📐 منهجية عمل وفق معايير الإمارات</h3><p>مجموعات مخططات منظمة للتنسيق بين المقاول والاستشاري والمصنع.</p></div></div>
<div class="card"><div class="b"><h3>🌐 العربية والإنجليزية</h3><p>نتواصل ونكتب ملاحظات المخططات بالعربية والإنجليزية.</p></div></div>
<div class="card"><div class="b"><h3>💳 دفع سهل عبر PayPal</h3><p>ادفع عربون الموقع أو فواتير المشاريع بأمان عبر PayPal.</p></div></div></div>
<p class="areas" style="margin-top:30px"><strong>المناطق التي نخدمها:</strong> دبي، أبوظبي، الشارقة، عجمان، رأس الخيمة، أم القيوين، الفجيرة — في جميع أنحاء الإمارات.</p></div></section>
{demos("ar")}{packages("ar")}{faq_html(faq_ar,"الأسئلة الشائعة","أسئلة وأجوبة")}{cta(L)}'''
    out[(L,"index.html")] = shell(L,"index.html","رسومات تنفيذية دبي | رسومات الرخام، مخططات أوتوكاد وتصميم ثلاثي الأبعاد في الإمارات – D3DDD",
        "D3DDD: رسومات تنفيذية للرخام والحجر، مخططات أوتوكاد، رسومات التشطيبات وتصميم ثلاثي الأبعاد في دبي وأبوظبي والشارقة. اطلب عرض سعر سريع عبر الإنترنت.",
        body,[faq_ld(faq_ar),{"@type":"WebSite","@id":url(L,"index.html")+"#website","url":url(L,"index.html"),"name":"D3DDD","inLanguage":"ar-AE","publisher":{"@id":g["ORG_ID"]}}],preload="hero-marble-kitchen")

    name="الخدمات"
    body = page_hero(L,"الخدمات — دبي والإمارات","رسومات تنفيذية ومخططات أوتوكاد وتصميم ثلاثي الأبعاد و<em>تصميم مواقع</em> في الإمارات","مخططات عملية وتصاميم بصرية للمساحات الداخلية وأعمال التشطيبات في دبي وأبوظبي والشارقة وجميع الإمارات.",name) + f'''
<section class="section" id="marble"><div class="wrap split"><figure>{img(P,"marble-shop-drawing","رسم تنفيذي لسطح مغسلة رخام مع فاصل وفتحة مغسلة وقطاع")}</figure><div><span class="num">01</span><h2>رسومات الرخام والحجر التنفيذية</h2><p>رسومات تنفيذية جاهزة للتصنيع تتضمن الأبعاد والقطاعات والواجهات ومواصفات المواد والتفاصيل المنسّقة، بالإضافة إلى قوائم القص ورسومات التصنيع وحساب الكميات.</p><ul class="check"><li>رسومات تنفيذية ورسومات تصنيع</li><li>قوائم القص وتوزيع الألواح</li><li>حصر الكميات وجداول BOQ</li></ul><p><a class="btn" href="marble.html">تفاصيل رسومات الرخام ←</a></p></div></div></section>
<section class="section alt" id="drafting"><div class="wrap split"><div><span class="num">02</span><h2>مخططات أوتوكاد ورسومات التشطيبات الداخلية</h2><p>مساقط وواجهات وقطاعات وتفاصيل ومخططات أوتوكاد (DWG) جاهزة للتنفيذ للمشاريع السكنية والتجارية وأعمال الفيت آوت.</p><ul class="check"><li>تخطيط المساحات وتوزيع الأثاث</li><li>تفاصيل النجارة والتشطيبات</li><li>مخططات الأسقف والأرضيات والواجهات</li><li>تسليم بصيغة DWG و PDF</li></ul></div><figure>{img(P,"elevation","رسم واجهة جدار بأسلوب أوتوكاد مع وحدات نجارة")}</figure></div></section>
<section class="section" id="3d"><div class="wrap split"><figure>{img(P,"kitchen","رسم واجهة خزائن مطبخ للتصميم ثلاثي الأبعاد")}</figure><div><span class="num">03</span><h2>تصميم ثلاثي الأبعاد في دبي</h2><p>تصاميم ثلاثية الأبعاد واقعية للمساحات الداخلية والخارجية تساعد العميل وجهات الاعتماد على رؤية النتيجة قبل التنفيذ.</p><ul class="check"><li>تصاميم داخلية 3D</li><li>خيارات المواد والتشطيبات</li><li>تصاميم مميزة بالرخام</li><li>صور للعرض والتقديم</li></ul></div></div></section>
<section class="section alt" id="web"><div class="wrap split"><div><span class="num">04</span><h2>تصميم مواقع للمقاولين</h2><p>مواقع سريعة ومتوافقة مع الجوال لشركات المقاولات والتشطيبات في الإمارات مع استفسارات واتساب مباشرة.</p><p class="price" style="margin-top:16px">2,000 درهم <small>باقة موقع المقاولين · 50% مقدماً</small></p><p><a class="btn" href="website-design.html">تفاصيل الباقة ←</a></p></div><figure>{img(P,"web-wireframe","رسم تخطيطي لمتصفح وجوال مع كود HTML لموقع مقاول")}</figure></div></section>{cta(L)}'''
    out[(L,"services.html")] = shell(L,"services.html","الخدمات | رسومات تنفيذية، مخططات أوتوكاد، تصميم ثلاثي الأبعاد ومواقع في دبي – D3DDD",
        "رسومات الرخام التنفيذية، مخططات أوتوكاد، رسومات التشطيبات، تصميم ثلاثي الأبعاد وتصميم مواقع للمقاولين في دبي وأبوظبي والشارقة.",body,
        [bc(L,"services.html",name),service_ld("رسومات الرخام والحجر التنفيذية","رسومات تنفيذية وقوائم قص ورسومات تصنيع للرخام.",url(L,"marble.html")),
         service_ld("مخططات أوتوكاد ورسومات التشطيبات","مخططات أوتوكاد جاهزة للتنفيذ.",url(L,"services.html")+"#drafting"),
         service_ld("تصميم ثلاثي الأبعاد","تصاميم ثلاثية الأبعاد داخلية وخارجية.",url(L,"services.html")+"#3d"),
         service_ld("تصميم مواقع للمقاولين","موقع من 5 صفحات مع زر واتساب.",url(L,"website-design.html"),WEB_OFFER)])

    name="رسومات الرخام"
    body = page_hero(L,"🇦🇪 توثيق متكامل لأعمال الرخام","رسومات الرخام والحجر التنفيذية في دبي و<em>الإمارات</em>","رسومات تنفيذية وقوائم قص ورسومات تصنيع وتصميم وجداول كميات لأعمال الرخام والحجر — للمقاولين والمصانع في دبي وأبوظبي والشارقة.",name) + f'''
<section class="section"><div class="wrap"><div class="split" style="margin-bottom:50px"><figure>{img(P,"marble-shop-drawing","رسم تنفيذي لسطح رخام: مسقط وفاصل وفتحة مغسلة وأبعاد وقطاع الحافة")}</figure><div><h2>شريك واحد. <em>كل التفاصيل.</em></h2><p>كل ما يحتاجه مشروع الرخام بين التصميم والكميات والتصنيع والتنفيذ، في مجموعات مخططات أوتوكاد واضحة ومنظمة.</p></div></div>
<div class="grid g3">
<div class="card"><div class="b"><h3>📐 الرسومات التنفيذية</h3><p>مساقط وواجهات وقطاعات وتفاصيل مكبّرة مع الأبعاد ونوع الحجر والسماكة وشكل الحافة والتشطيب.</p></div></div>
<div class="card"><div class="b"><h3>📋 قوائم القص</h3><p>جداول القطع وتوزيع الألواح لتقليل الهدر وتسهيل التصنيع.</p></div></div>
<div class="card"><div class="b"><h3>⚙️ رسومات التصنيع</h3><p>التفاوتات والحواف والفواصل والزوايا ومعلومات CNC والووترجت للتصنيع والتركيب.</p></div></div>
<div class="card"><div class="b"><h3>✨ تصميم الرخام</h3><p>مخططات ثنائية الأبعاد وتصاميم ثلاثية الأبعاد واختيار المواد وتطابق العروق (بوك ماتش).</p></div></div>
<div class="card"><div class="b"><h3>🧮 حساب الكميات والتكاليف</h3><p>حصر الكميات وتحليل الأسعار وملخصات تكلفة جاهزة لبرنامج Excel.</p></div></div>
<div class="card"><div class="b"><h3>🤝 دعم المشروع</h3><p>التنسيق مع المقاولين والاستشاريين والمصانع من الفكرة حتى التنفيذ.</p></div></div></div></div></section>
<section class="section alt"><div class="wrap split"><figure>{img(P,"cladding","رسم واجهة تكسية جدار رخام بعروق متطابقة")}</figure><div><p class="eyebrow">كل قصّة تبدأ برسم واضح</p><h2>مجالات التطبيق</h2><div class="tags"><span>أسطح المطابخ</span><span>المغاسل</span><span>الدرج</span><span>تكسية الجدران</span><span>الأرضيات</span><span>جزر المطبخ</span><span>المدافئ</span><span>تطعيم الووترجت</span></div>
<h3 style="margin-top:36px">مراحل العمل</h3><ol class="steps" style="margin-top:14px"><li>الإرسال</li><li>المراجعة</li><li>الرسم</li><li>الاعتماد</li><li>التصنيع</li><li>التركيب</li></ol></div></div></section>{cta(L)}'''
    out[(L,"marble.html")] = shell(L,"marble.html","رسومات الرخام التنفيذية دبي | رسومات الحجر وقوائم القص وجداول الكميات – D3DDD",
        "رسومات تنفيذية للرخام والحجر في دبي وأبوظبي والشارقة: رسومات تصنيع، قوائم قص، توزيع الألواح وجداول كميات بصيغة أوتوكاد DWG و PDF.",body,
        [bc(L,"marble.html",name),service_ld("رسومات الرخام والحجر التنفيذية","رسومات تنفيذية وقوائم قص ورسومات تصنيع وجداول كميات للرخام في الإمارات.",url(L,"marble.html"))])

    name="تصميم المواقع"
    body = page_hero(L,"تصميم مواقع للمقاولين — الإمارات","تصميم مواقع للمقاولين في دبي — <em>2,000 درهم</em>","موقع احترافي من 5 صفحات يحوّل الزوار إلى استفسارات عبر واتساب.",name) + f'''
<section class="section"><div class="wrap split"><div class="card"><div class="b"><p class="eyebrow">باقة موقع المقاولين</p><p class="price">2,000 درهم <small dir="ltr">approx. CAD 750</small></p><p>50% (1,000 درهم) مقدماً للبدء، و50% عند الانتهاء وقبل إطلاق الموقع.</p>
<ul class="check"><li>5 صفحات: الرئيسية، الخدمات، المشاريع، من نحن، تواصل معنا</li><li>أزرار تواصل وروابط بريد إلكتروني</li><li>نموذج استفسار</li><li>تصميم متوافق مع الجوال</li><li>أساسيات تحسين محركات البحث (SEO)</li><li>ربط النطاق (الدومين) الحالي</li></ul>
<div class="actions" style="margin-top:20px"><a class="btn" href="https://paypal.me/imshoi" target="_blank" rel="noopener">ادفع العربون عبر PayPal</a><a class="btn ghost" href="contact.html">ابدأ موقعك</a><a class="btn ghost" href="mailto:info@d3ddd.com">اسأل عبر البريد</a></div></div></div>
<div><figure>{img(P,"web-wireframe","رسم تخطيطي لموقع: متصفح وشاشة جوال وكود HTML")}</figure><h3 style="margin-top:24px">كيف نعمل</h3><ol class="steps" style="margin-top:14px"><li>دفعة 50%</li><li>أرسل المحتوى</li><li>نبني الموقع</li><li>تراجعه</li><li>الدفعة الثانية والإطلاق</li></ol><p class="notice" style="margin-top:24px">لا تشمل الباقة تسجيل النطاق ورسوم الاستضافة والصور المدفوعة إن لزمت، إلا إذا تم الاتفاق على ذلك كتابياً.</p></div></div></section>'''
    body += demos(L)
    out[(L,"website-design.html")] = shell(L,"website-design.html","تصميم مواقع للمقاولين دبي | موقع 5 صفحات بسعر 2,000 درهم – D3DDD",
        "تصميم مواقع للمقاولين في دبي والإمارات: 5 صفحات، زر واتساب، نموذج استفسار وأساسيات SEO بسعر 2,000 درهم (50% مقدماً).",body,
        [bc(L,"website-design.html",name),service_ld("تصميم مواقع للمقاولين","موقع من 5 صفحات متوافق مع الجوال مع زر واتساب ونموذج استفسار.",url(L,"website-design.html"),WEB_OFFER)])

    name="من نحن"
    body = page_hero(L,"عن D3DDD","استوديو تصميم ورسم هندسي في دبي لـ<em>مشاريع حقيقية.</em>","دبي للتصميم والرسم ثلاثي الأبعاد — رسم هندسي وتصميم ثلاثي الأبعاد وخبرة في الرخام تحت سقف واحد.",name) + f'''
<section class="section"><div class="wrap split"><figure>{img(P,"table","رسم خطي أيزومتري لطاولة طعام")}</figure><div><h2>منهجيتنا</h2><p>يجمع D3DDD — دبي للتصميم والرسم ثلاثي الأبعاد — بين الرسم الهندسي الفني والتصميم البصري والخبرة العملية في الرخام وأعمال التشطيبات.</p><p>نعمل مع المقاولين ومصانع الرخام والاستشاريين ومصممي الديكور الداخلي وفرق المشاريع في جميع أنحاء الإمارات، ونقدّم مخططات واضحة ومنظمة وعملية في الموقع.</p><ul class="check"><li>الدقة: أبعاد وملاحظات صحيحة</li><li>الوضوح: لوحات منظمة لتسهيل التنسيق</li><li>سرعة التواصل: ردود سريعة عبر البريد بالعربية والإنجليزية</li></ul></div></div></section>{cta(L)}'''
    out[(L,"about.html")] = shell(L,"about.html","من نحن | D3DDD دبي للتصميم والرسم – استوديو رسومات تنفيذية في الإمارات",
        "D3DDD استوديو رسم هندسي وتصميم في دبي متخصص في رسومات الرخام التنفيذية ومخططات أوتوكاد والتصميم ثلاثي الأبعاد للمقاولين في الإمارات.",body,[bc(L,"about.html",name)])

    name="تواصل معنا"
    body = page_hero(L,"اطلب عرض سعر — دبي والإمارات","تواصل مع D3DDD للرسومات التنفيذية ومخططات أوتوكاد و<em>التصميم ثلاثي الأبعاد</em>","أرسل المخططات أو الرسومات الأولية أو المقاسات أو المتطلبات، وسنرد عبر البريد بالعربية أو الإنجليزية.",name) + f'''
<section class="section"><div class="wrap split" style="align-items:start"><div>
<form class="enquiry card" style="padding:28px" name="enquiry-ar" method="post" action="mailto:info@d3ddd.com?subject=Website%20enquiry" enctype="text/plain">
<p class="hp"><label>اتركه فارغاً <input name="company_website"></label></p>
<div class="row"><div><label for="n">الاسم *</label><input id="n" name="name" required autocomplete="name"></div><div><label for="p">الهاتف (اختياري)</label><input id="p" name="phone" type="tel" autocomplete="tel" dir="ltr"></div></div>
<div class="row"><div><label for="e">البريد الإلكتروني *</label><input id="e" name="email" type="email" required autocomplete="email" dir="ltr"></div><div><label for="s">الخدمة</label><select id="s" name="service"><option>رسومات الرخام والحجر التنفيذية</option><option>قوائم القص / رسومات التصنيع</option><option>حساب الكميات / BOQ</option><option>مخططات أوتوكاد / رسومات التشطيبات</option><option>تصميم ثلاثي الأبعاد</option><option>موقع للمقاولين (2,000 درهم)</option><option>أخرى</option></select></div></div>
<label for="m">تفاصيل المشروع *</label><textarea id="m" name="message" required placeholder="نطاق العمل، الموقع (مثلاً دبي أو أبوظبي)، الموعد النهائي…"></textarea>
<p class="notice" style="margin-top:14px">عند الإرسال سيفتح تطبيق البريد لديك مع تعبئة التفاصيل. أرفق المخططات بالرسالة قبل إرسالها، أو راسلنا مباشرة على <a href="mailto:info@d3ddd.com"><u>info@d3ddd.com</u></a>.</p>
<div class="actions" style="margin-top:18px"><button class="btn" type="submit">أرسل الاستفسار عبر البريد</button></div></form></div>
<div><h2 style="font-size:26px">تواصل مباشر</h2><ul class="check"><li><a href="mailto:info@d3ddd.com">info@d3ddd.com</a></li><li>دبي، الإمارات العربية المتحدة — نخدم جميع الإمارات</li></ul></div></div></section>'''
    out[(L,"contact.html")] = shell(L,"contact.html","تواصل مع D3DDD | عرض سعر رسومات تنفيذية وتصميم ثلاثي الأبعاد دبي والإمارات",
        "اطلب عرض سعر لرسومات الرخام التنفيذية أو مخططات أوتوكاد أو رسومات التشطيبات أو التصميم ثلاثي الأبعاد أو موقع للمقاولين في دبي والإمارات.",body,[bc(L,"contact.html",name),{"@type":"ContactPage","url":url(L,"contact.html"),"about":{"@id":g["ORG_ID"]}}])
    out[(L,"thank-you.html")] = shell(L,"thank-you.html","شكراً لك | D3DDD","تم استلام استفسارك.",
        '<section class="page-hero" style="min-height:60vh"><p class="eyebrow">تم الاستلام</p><h1>شكراً لك.</h1><p>سنرد عليك قريباً. يمكنك أيضاً مراسلتنا على info@d3ddd.com.</p><p style="margin-top:24px"><a class="btn" href="./">العودة للرئيسية</a></p></section>',(),True,False)
    return out

/* D3DDD sales chat. Scripted answers only — not a language model.
   Leads use the same mailto path as the enquiry form in assets/site.js:
   the address is assembled from data-u and data-d, then location.href opens mailto:.
   A test may set window.__D3DDD_MAILTO_SINK to capture that URL instead. */
(function () {
  if (typeof window !== "undefined" && window.__D3DDD_SALES_CHAT) return;
  if (typeof window !== "undefined") window.__D3DDD_SALES_CHAT = true;

  var COPY = {
    en: {
      title: "D3DDD",
      subtitle: "Shop drawings and drafting",
      open: "Open chat",
      close: "Close chat",
      toUrdu: "Switch to Urdu",
      toEnglish: "Switch to English",
      messageLabel: "Message",
      placeholder: "Type a question",
      send: "Send",
      hello: "Hello. I am the D3DDD assistant. Ask about marble and stone shop drawings, drafting, estimation, 3D renders or websites, or send your details for a quote.",
      getQuote: "Get a quote",
      fallback: "I can help with marble and stone shop drawings, architectural and fit-out drafting, estimation, 3D renders and websites.\nShop drawings cover layouts, elevations, sections, fixing, edges, cutting lists and slab nesting. Files are DWG and PDF. Packs start from around AED 1,200, with 50% upfront.\nChoose a topic below, or tap Get a quote and leave your details. You can put the question in the scope line. The team will reply by email.",
      useButtons: "Please choose one of the buttons below.",
      emailBad: "That email does not look valid. Please try again.",
      needThis: "Please add that before we continue.",
      skipped: "Skipped",
      yes: "Yes",
      no: "No",
      skip: "Skip",
      back: "Back",
      sendEnquiry: "Send enquiry",
      restart: "Start again",
      closeChat: "Close",
      summaryIntro: "Please check this summary. If it looks right, send it and your email app will open.",
      thanks: "Thank you. Your email app should open with this enquiry. Please send that message so it reaches the team. If it does not open, copy the summary and email it to ADDRESS.",
      drawingsYes: "Please email the files to ADDRESS. This chat cannot take attachments. You can attach the PDF or DWG in the email that opens when you send this enquiry.",
      drawingsNo: "No problem. You can email drawings later to ADDRESS.",
      again: "We can start again. Ask a question, or send your details.",
      nameQ: "What is your name?",
      companyQ: "Which company is this for? You can skip this.",
      phoneQ: "What is the best phone or WhatsApp number? You can skip this.",
      emailQ: "What email should we reply to?",
      projectQ: "What do you need?",
      siteQ: "Which emirate, and what is the site or area? You can skip this.",
      scopeQ: "Briefly, what is the scope? You can skip this.",
      stoneQ: "Stone type, thickness and finish, if you know them (for example 20 mm, honed). You can skip this.",
      drawingsQ: "Do you have drawings to send?",
      timelineQ: "What is the timeline? You can skip this.",
      budgetQ: "What budget do you have in mind? You can skip this.",
      foundQ: "How did you find us? You can skip this.",
      namePh: "Your name",
      companyPh: "Company",
      phonePh: "Phone or WhatsApp",
      emailPh: "name@company.com",
      sitePh: "Emirate and site",
      scopePh: "Scope",
      stonePh: "Stone, thickness, finish",
      timelinePh: "Timeline",
      budgetPh: "Budget",
      foundPh: "How you found us",
      quick: {
        marble: "Marble & stone shop drawings",
        drafting: "Architectural & fit-out drafting",
        estimation: "Estimation",
        viz: "3D visualization",
        website: "Websites",
        payment: "Prices & payment",
        lead: "Send my details"
      },
      projects: {
        marble: "Marble & stone shop drawings",
        drafting: "Architectural & fit-out drafting",
        estimation: "Estimation",
        viz: "3D visualization",
        website: "Website",
        other: "Other"
      },
    },
    ur: {
      title: "D3DDD",
      subtitle: "شاپ ڈرائنگ اور ڈرافٹنگ",
      open: "گفتگو کھولیں",
      close: "گفتگو بند کریں",
      toUrdu: "اردو میں دیکھیں",
      toEnglish: "انگریزی میں دیکھیں",
      messageLabel: "پیغام",
      placeholder: "سوال لکھیں",
      send: "بھیجیں",
      hello: "السلام علیکم۔ میں D3DDD کا معاون ہوں۔ ماربل شاپ ڈرائنگ، ڈرافٹنگ، تخمینہ، تھری ڈی رینڈر یا ویب سائٹ کے بارے میں پوچھیں، یا کوٹ کے لیے اپنی تفصیل بھیجیں۔",
      getQuote: "کوٹ حاصل کریں",
      fallback: "میں ماربل اور پتھر کی شاپ ڈرائنگ، آرکیٹیکچرل اور فٹ آؤٹ ڈرافٹنگ، تخمینہ، تھری ڈی رینڈر اور ویب سائٹ میں مدد کر سکتا ہوں۔\nشاپ ڈرائنگ میں لے آؤٹ، ایلیویشن، سیکشن، فکسنگ، کنارے، کٹنگ لسٹ اور سلیب نیسٹنگ شامل ہو سکتی ہے۔ فائل DWG اور PDF ہوتی ہے۔ پیکج تقریباً 1,200 درہم سے ہیں، 50 فیصد پیشگی۔\nنیچے کوئی موضوع چنیں، یا کوٹ حاصل کریں اور اپنی تفصیل لکھیں۔ سوال دائرہ کار کی سطر میں لکھ سکتے ہیں۔ ٹیم ای میل سے جواب دے گی۔",
      useButtons: "براہ کرم نیچے دیے بٹن میں سے ایک چنیں۔",
      emailBad: "یہ ای میل درست نہیں لگتی۔ دوبارہ لکھیں۔",
      needThis: "آگے بڑھنے سے پہلے یہ لکھیں۔",
      skipped: "چھوڑ دیا",
      yes: "ہاں",
      no: "نہیں",
      skip: "چھوڑیں",
      back: "پیچھے",
      sendEnquiry: "انکوائری بھیجیں",
      restart: "دوبارہ شروع",
      closeChat: "بند کریں",
      summaryIntro: "براہ کرم یہ خلاصہ دیکھیں۔ درست ہو تو بھیجیں، ای میل ایپ کھل جائے گی۔",
      thanks: "شکریہ۔ آپ کی ای میل ایپ میں یہ انکوائری کھلنی چاہیے۔ وہ پیغام بھیجیں تاکہ ٹیم تک پہنچے۔ اگر نہ کھلے تو یہی خلاصہ ADDRESS پر ای میل کریں۔",
      drawingsYes: "فائلیں ADDRESS پر ای میل کریں۔ یہ چیٹ منسلکات نہیں لیتی۔ انکوائری بھیجتے وقت کھلنے والی ای میل میں PDF یا DWG منسلک کر سکتے ہیں۔",
      drawingsNo: "کوئی بات نہیں۔ ڈرائنگ بعد میں ADDRESS پر ای میل کر سکتے ہیں۔",
      again: "دوبارہ شروع کر سکتے ہیں۔ سوال پوچھیں، یا تفصیل بھیجیں۔",
      nameQ: "آپ کا نام کیا ہے؟",
      companyQ: "کمپنی کا نام؟ یہ قدم چھوڑ سکتے ہیں۔",
      phoneQ: "فون یا واٹس ایپ نمبر؟ یہ قدم چھوڑ سکتے ہیں۔",
      emailQ: "جواب کس ای میل پر بھیجیں؟",
      projectQ: "کس کام کی ضرورت ہے؟",
      siteQ: "کون سا امارت، اور سائٹ یا علاقہ؟ یہ قدم چھوڑ سکتے ہیں۔",
      scopeQ: "کام کا مختصر دائرہ کیا ہے؟ یہ قدم چھوڑ سکتے ہیں۔",
      stoneQ: "پتھر کی قسم، موٹائی اور فنش، اگر معلوم ہو (مثلاً 20 ملی میٹر، ہونڈ)۔ یہ قدم چھوڑ سکتے ہیں۔",
      drawingsQ: "کیا ڈرائنگ موجود ہیں؟",
      timelineQ: "ٹائم لائن کیا ہے؟ یہ قدم چھوڑ سکتے ہیں۔",
      budgetQ: "بجٹ کا اندازہ؟ یہ قدم چھوڑ سکتے ہیں۔",
      foundQ: "آپ نے ہمیں کہاں سے جانا؟ یہ قدم چھوڑ سکتے ہیں۔",
      namePh: "آپ کا نام",
      companyPh: "کمپنی",
      phonePh: "فون یا واٹس ایپ",
      emailPh: "name@company.com",
      sitePh: "امارت اور سائٹ",
      scopePh: "دائرہ کار",
      stonePh: "پتھر، موٹائی، فنش",
      timelinePh: "ٹائم لائن",
      budgetPh: "بجٹ",
      foundPh: "کہاں سے جانا",
      quick: {
        marble: "ماربل اور پتھر کی شاپ ڈرائنگ",
        drafting: "آرکیٹیکچرل اور فٹ آؤٹ ڈرافٹنگ",
        estimation: "تخمینہ",
        viz: "تھری ڈی ویژولائزیشن",
        website: "ویب سائٹس",
        payment: "قیمت اور ادائیگی",
        lead: "تفصیل بھیجیں"
      },
      projects: {
        marble: "ماربل اور پتھر کی شاپ ڈرائنگ",
        drafting: "آرکیٹیکچرل اور فٹ آؤٹ ڈرافٹنگ",
        estimation: "تخمینہ",
        viz: "تھری ڈی ویژولائزیشن",
        website: "ویب سائٹ",
        other: "کچھ اور"
      },
    }
  };

  var INTENTS = [
    { id: "edges", pri: 88, keys: [["edge profile", 26], ["which edge", 24], ["edge", 22], ["bullnose", 24], ["half bullnose", 26], ["demi bullnose", 26], ["full bullnose", 26], ["chamfer", 24], ["bevel", 22], ["ogee", 24], ["lambs tongue", 26], ["lamb tongue", 26], ["mitred", 22], ["mitered", 22], ["mitre", 22], ["eased edge", 24], ["pencil edge", 24], ["eased", 22], ["arris", 24], ["square edge", 24], ["waterfall edge", 24], ["ایج پروفائل", 26], ["ایج", 22], ["کنارہ", 22], ["کنارے", 22], ["بل نوز", 24], ["اوگی", 24], ["kinara", 22], ["edge profle", 24]] },
    { id: "thickness", pri: 88, keys: [["thickness", 24], ["how thick", 24], ["what thickness", 26], ["18mm", 24], ["20mm", 24], ["30mm", 24], ["motai", 24], ["motayi", 24], ["motaai", 24], ["موٹائی", 26], ["کتنا موٹا", 24]] },
    { id: "finishes", pri: 88, keys: [["polished", 24], ["honed", 24], ["leathered", 24], ["flamed", 24], ["surface finish", 26], ["what finish", 24], ["which finish", 24], ["stone finish", 24], ["finish type", 24], ["the finish", 22], ["فنش", 24], ["پالش", 24], ["ہونڈ", 24], ["لیدرڈ", 24], ["فلیمڈ", 24]] },
    { id: "vein", pri: 88, keys: [["bookmatch", 26], ["book match", 26], ["vein match", 26], ["vein direction", 24], ["vein", 22], ["بک میچ", 26], ["وین میچ", 24], ["bookmatched", 26]] },
    { id: "slab", pri: 88, keys: [["slab nesting", 26], ["slab nest", 26], ["nesting", 22], ["slab photo", 26], ["slab picture", 24], ["slab image", 24], ["سلیب", 22], ["نیسٹنگ", 24], ["cnc nest", 24]] },
    { id: "cutting-list", pri: 88, keys: [["cutting list", 26], ["piece schedule", 26], ["cut list", 24], ["excel", 22], ["piece id", 22], ["کٹنگ لسٹ", 26], ["پیس شیڈول", 26], ["ایکسل", 22], ["schedule of pieces", 24]] },
    { id: "revisions", pri: 88, keys: [["revision", 24], ["title block", 24], ["clouded", 24], ["revision table", 26], ["rev cloud", 24], ["ریویژن", 24], ["ٹائٹل بلاک", 26], ["cloud", 16]] },
    { id: "not-for-cut", pri: 88, keys: [["not for cut", 26], ["naat for cut", 24], ["site dimension", 22], ["unconfirmed dimension", 24], ["ناٹ فار کٹ", 26], ["notforcut", 26]] },
    { id: "formats", pri: 88, keys: [["dwg", 24], ["pdf", 20], ["file format", 26], ["which format", 24], ["what format", 24], ["autocad file", 22], ["فارمیٹ", 24], ["ڈی ڈبلیو جی", 24]] },
    { id: "sections-fixing", pri: 88, keys: [["mechanical anchor", 26], ["adhesive", 24], ["fixing detail", 26], ["fixing method", 24], ["anchor", 22], ["build up", 22], ["section detail", 24], ["fixing", 20], ["سیکشن", 22], ["فکسنگ", 24], ["اینکر", 24], ["adhesive or mechanical", 26]] },
    { id: "layouts", pri: 88, keys: [["layout plan", 26], ["floor plan", 24], ["wall elevation", 26], ["setting out", 26], ["expansion joint", 24], ["piece number", 22], ["layout", 20], ["لے آؤٹ", 24], ["ایلیویشن", 20]] },
    { id: "vanity", pri: 80, keys: [["vanity", 24], ["vanities", 24], ["vaniti", 24], ["wash basin", 22], ["basin top", 22], ["وینٹی", 24], ["vanity top", 26]] },
    { id: "countertop", pri: 80, keys: [["countertop", 24], ["counter top", 24], ["worktop", 24], ["kitchen top", 24], ["counter", 22], ["کاؤنٹر", 24]] },
    { id: "island", pri: 80, keys: [["kitchen island", 26], ["island top", 24], ["island", 22], ["آئلینڈ", 24], ["kitchin island", 26]] },
    { id: "stairs", pri: 80, keys: [["staircase", 26], ["stair", 24], ["tread", 22], ["riser", 22], ["nosing", 24], ["seedhi", 24], ["seediyan", 24], ["seedi", 24], ["سیڑھ", 24]] },
    { id: "cladding", pri: 80, keys: [["cladding", 24], ["wall clad", 24], ["clading", 24], ["کلیڈنگ", 24]] },
    { id: "flooring", pri: 82, keys: [["flooring", 26], ["marble floor", 26], ["floor tile", 24], ["floor layout", 26], ["فرش", 24], ["farsh", 24]] },
    { id: "fireplace", pri: 80, keys: [["fireplace", 26], ["fire place", 26], ["فائر پلیس", 26], ["hearth", 22]] },
    { id: "waterjet", pri: 80, keys: [["waterjet", 26], ["water jet", 26], ["medallion", 24], ["inlay", 22], ["inlays", 22], ["واٹر جیٹ", 26], ["انلے", 22]] },
    { id: "skirting", pri: 80, keys: [["skirting", 26], ["skirtng", 24], ["baseboard", 22], ["اسکرٹنگ", 26], ["skirting board", 26]] },
    { id: "pool", pri: 80, keys: [["swimming pool", 26], ["pool", 22], ["terrace", 22], ["terrace tiling", 26], ["outdoor tiling", 24], ["پول", 22], ["ٹیرس", 22], ["majlis tiling", 24]] },
    { id: "door-frame", pri: 80, keys: [["door frame", 26], ["doorframe", 26], ["door jamb", 24], ["چوکھٹ", 24], ["lintel", 20]] },
    { id: "no-supply", pri: 96, keys: [["sell slab", 26], ["sell marble", 26], ["sell stone", 26], ["supply slab", 26], ["supply marble", 24], ["stock slab", 26], ["buy slab", 24], ["do you sell", 22], ["سلیب بیچ", 26]] },
    { id: "shop-what", pri: 86, keys: [["what are shop drawing", 26], ["what is a shop drawing", 26], ["what are marble shop", 26], ["what is marble shop", 26], ["shop drawing kya", 26], ["naqsha kya", 26], ["شاپ ڈرائنگ کیا", 26], ["what are fabrication drawing", 24], ["what is a fabrication drawing", 26], ["naksha kya", 26]] },
    { id: "shop-vs-design", pri: 86, keys: [["design drawing", 24], ["shop vs", 24], ["shop versus", 24], ["versus design", 24], ["vs design", 24], ["design vs", 24], ["shop or design", 24], ["ڈیزائن ڈرائنگ", 24], ["design intent", 22]] },
    { id: "why-needed", pri: 86, keys: [["consultant approval", 26], ["before fabrication", 24], ["why shop drawing", 26], ["why are shop", 26], ["why needed", 24], ["why are they needed", 24], ["why do we need shop", 26], ["irreversible", 22], ["منظوری", 22], ["consultant", 20], ["کنسلٹنٹ", 20]] },
    { id: "full-set", pri: 86, keys: [["full set", 24], ["complete set", 24], ["what is included", 22], ["what do you include", 20], ["what does the set include", 26], ["what does a set include", 26], ["kya shamil", 28], ["shamil kya", 28], ["کیا شامل", 28], ["what do shop drawings include", 26], ["contents of", 20], ["what is in the set", 24], ["what goes into", 22]] },
    { id: "what-to-send", pri: 86, keys: [["what should i send", 26], ["what do i send", 26], ["what to send", 26], ["what do you need from", 24], ["what do you need", 22], ["which files", 24], ["what files", 24], ["kya bhej", 24], ["کیا بھیج", 26], ["what should we send", 26], ["documents do you need", 24]] },
    { id: "how-to-start", pri: 84, keys: [["how to start", 26], ["how do i start", 26], ["how do we start", 26], ["how to begin", 26], ["how do we begin", 26], ["how do you start", 26], ["get started", 22], ["how does it work", 22], ["kaise shuru", 26], ["kaise start", 24], ["کیسے شروع", 26], ["next step", 20], ["how do i begin", 26]] },
    { id: "draft-bim", pri: 90, keys: [["bim", 26], ["revit", 24], ["municipal submission", 26], ["municipality", 24], ["municipal", 22], ["submit to the municipality", 26], ["dubai municipality", 26], ["not bim", 26], ["بلڈنگ انفارمیشن", 24]] },
    { id: "draft-permit", pri: 88, keys: [["permit oriented", 26], ["permit set", 26], ["permit drawing", 26], ["building permit", 24], ["authority checklist", 24], ["for permit", 22], ["permit", 20]] },
    { id: "draft-arabic", pri: 88, keys: [["arabic note", 26], ["bilingual", 26], ["in arabic", 24], ["arabic notes", 26], ["عربی نوٹ", 26], ["دو زبان", 24], ["bilingual note", 26]] },
    { id: "draft-layers", pri: 88, keys: [["layer standard", 26], ["cad layer", 26], ["layers", 22], ["layer names", 24], ["our layers", 24], ["لیئر", 22]] },
    { id: "draft-rcp", pri: 88, keys: [["reflected ceiling", 26], ["rcp", 26], ["ceiling plan", 24], ["سیلنگ پلان", 24]] },
    { id: "draft-overview", pri: 70, keys: [["architectural drafting", 26], ["fit out", 22], ["fitout", 22], ["construction drawing", 24], ["autocad 2d", 26], ["autocad", 18], ["architectural drawing", 24], ["joinery drawing", 24], ["joinery", 20], ["as built", 22], ["as-built", 22], ["ڈرافٹنگ", 22], ["آٹوکیڈ", 20], ["فٹ آؤٹ", 22], ["shop drawing of joinery", 24]] },
    { id: "interior", pri: 72, keys: [["interior design", 26], ["space planning", 26], ["concept layout", 26], ["design development", 24], ["انٹیریر", 24], ["space plan", 24]] },
    { id: "estimation", pri: 74, keys: [["estimation", 24], ["estimate", 22], ["boq", 26], ["bill of quantit", 26], ["quantity take", 24], ["takeoff", 24], ["take off", 24], ["material schedule", 24], ["تخمین", 24], ["بی او کیو", 26], ["کوانٹٹی", 22], ["quantity", 20], ["tender", 20]] },
    { id: "viz", pri: 74, keys: [["3d", 20], ["render", 24], ["rendering", 24], ["visualisation", 24], ["visualization", 24], ["walkthrough", 22], ["رینڈر", 24], ["تھری ڈی", 24], ["still render", 26]] },
    { id: "website", pri: 74, keys: [["website", 24], ["web site", 24], ["web design", 24], ["landing page", 22], ["starter", 20], ["premium package", 22], ["ویب سائٹ", 24], ["website package", 26], ["business package", 20]] },
    { id: "pricing", pri: 92, keys: [["how much", 26], ["price", 26], ["pricing", 26], ["cost", 28], ["kitna", 26], ["kitne", 26], ["kitni", 26], ["qeemat", 26], ["keemat", 26], ["qemat", 26], ["qimat", 26], ["kimat", 26], ["قیمت", 26], ["کتنا", 26], ["کتنے", 26], ["aed", 22], ["dirham", 22], ["درہم", 20], ["upfront", 24], ["deposit", 22], ["50 percent", 26], ["advance", 20], ["پیشگی", 24], ["ادائیگی", 22], ["payment", 20], ["charges", 20], ["fee", 20], ["daam", 24], ["rate", 18], ["how much is", 26], ["quotation price", 24]] },
    { id: "place", pri: 78, keys: [["where are you", 26], ["based in", 24], ["which emirate", 24], ["do you cover", 26], ["abu dhabi", 22], ["sharjah", 20], ["ajman", 20], ["ras al khaimah", 22], ["fujairah", 22], ["umm al quwain", 22], ["delivery", 20], ["all emirates", 24], ["across the uae", 24], ["turnaround", 24], ["lead time", 24], ["how long does", 24], ["how long do", 24], ["how long to", 24], ["how long will", 24], ["when will", 24], ["kitne din", 28], ["how much time", 28], ["kab tak", 24], ["timeline", 22], ["دبئی میں", 22], ["امارات", 20], ["where do you deliver", 26], ["do you deliver", 24], ["remotely", 20]] },
    { id: "shop-overview", pri: 40, keys: [["shop drawing", 20], ["fabrication drawing", 20], ["marble", 16], ["marbal", 16], ["stone", 16], ["drawing", 16], ["naqsha", 16], ["naksha", 16], ["ماربل", 16], ["شاپ ڈرائنگ", 16], ["خاکہ", 16], ["sang e marmar", 16], ["installation drawing", 20]] },
  ];
  var ANSWERS = {
  "en": {
    "edges": "Standard edge profiles:\n• Pencil / eased edge\n• Bullnose: full, half and demi\n• Chamfer / bevel (45°)\n• Ogee / lamb’s tongue\n• Mitred corners (thick look or a cladding return)\n• Square edge with an eased arris\nCustom profiles can be drawn on request. Each edge is coded on the sheet.",
    "thickness": "Common thicknesses on these drawings are 18 mm, 20 mm and 30 mm.\nThe thickness you specify is written on the plan and the section, with the stone name and finish.\nTell us the thickness when you send the drawings. If it is still open, say so.\nThe exact price is confirmed in writing after we review the drawings.",
    "finishes": "The finish is noted on the drawing.\nCommon finishes are polished, honed, leathered and flamed.\nSealing is noted where your specification asks for it.\nSend the finish with the stone name and thickness.",
    "vein": "Vein direction and bookmatching are shown when the design depends on them.\nBookmatching mirrors the vein. Vein matching keeps the grain running from piece to piece.\nIf you send slab photos, this is set out on the nesting layout so the workshop can follow it.",
    "slab": "Slab nesting is drawn when you send slab photos.\nPieces are laid on the slab for CNC or waterjet cutting, so the vein can be followed and waste reduced.\nSend the photos with the design drawings and the stone name.\nThe nesting is issued with the DWG and PDF set.",
    "cutting-list": "The piece schedule lists every piece: ID, size, edge code, quantity and location.\nThe same numbers are on the plans, so the workshop and the site use one list.\nIt can be exported to Excel.\nIt sits with the shop drawings, which are issued as DWG and PDF.",
    "revisions": "Each issue has a revision table and a title block. Changes are clouded.\nIf you send your own title block and layer standard, the sheets follow them.\nThis applies to stone shop drawings and to architectural sets.\nFiles are DWG and PDF.",
    "not-for-cut": "If a site dimension is not confirmed, it is marked “not for cut” until it is verified.\nThose sizes are not for the saw.\nSend site measurements, or confirm that the drawings match the built site.",
    "formats": "Shop drawings and drafting sets are issued as DWG and PDF.\nDWG is the AutoCAD file. PDF is for review and for the site.\nA cutting list can be exported to Excel when it is part of the set.\nAny other format is used only if it is agreed in the quote.",
    "sections-fixing": "Sections show the build-up, the edge, and how the stone meets skirting, glass, joinery and thresholds.\nFixing is drawn as specified: adhesive, or mechanical anchors.\nThe stone name, thickness and finish are noted on the same detail.\nFiles are DWG and PDF.",
    "layouts": "Layout plans cover the floor and the wall elevations.\nThey show the setting-out point, piece sizes, joint widths, expansion joints, borders, inlays and piece numbers.\nElevations tie each panel number back to the cutting list.\nFiles are DWG and PDF.",
    "vanity": "Yes. Vanity tops are part of the marble and stone shop drawings.\nThe set shows the layout, piece sizes, joints, edge profiles, thickness, finish and how the top meets the joinery.\nA cutting list can be included. Files are DWG and PDF.\nPacks start from around AED 1,200. The exact price is confirmed after we see your drawings.",
    "countertop": "Countertop shop drawings show the plan, piece sizes, joints, edge profile, thickness and finish.\nSections show the edge and the fixing or support that is specified.\nA cutting list can be included. Files are DWG and PDF.\nThe exact price is confirmed in writing after we review the drawings.",
    "island": "Kitchen-island shop drawings cover the stone top: layout, joints, edge profiles, thickness and finish.\nSections show the edge and how the top meets the joinery.\nA cutting list can be included. Files are DWG and PDF.\nThe exact price is confirmed after we review your drawings.",
    "stairs": "Stair shop drawings cover treads, risers and nosings.\nThey show piece sizes, edge profiles, thickness, finish and the fixing that is specified.\nA cutting list can be included. Files are DWG and PDF.\nThe exact price is confirmed after we review the stair drawings.",
    "cladding": "Wall-cladding drawings include elevations with panel sizes, joints and piece numbers.\nSections show the build-up and the fixing: adhesive or mechanical anchors, as specified.\nJunctions with openings and other trades are shown. Files are DWG and PDF.\nThe exact price is confirmed after we review the drawings.",
    "flooring": "Flooring shop drawings are layout plans with a setting-out point, piece sizes, joint widths and expansion joints.\nBorders, inlays and piece numbers are shown, with the stone, thickness and finish.\nA cutting list can be included. Files are DWG and PDF.\nThe exact price is confirmed after we review the drawings.",
    "fireplace": "Fireplace stone is drawn as a shop-drawing package: layout, piece sizes, joints, edges, thickness and finish.\nFixing is shown as specified. A cutting list can be included.\nFiles are DWG and PDF.\nSend the design drawings, and the exact price is confirmed in writing.",
    "waterjet": "Waterjet medallions and inlays are drawn in the shop-drawing set.\nThe layout shows the pattern, the joints and the piece numbers.\nSlab nesting for waterjet can be prepared when you send slab photos.\nFiles are DWG and PDF. The exact price is confirmed after review.",
    "skirting": "Skirting is drawn with the stone package: piece sizes, joints, thickness, finish and the junction with the floor or the wall.\nDoor frames can sit in the same kind of set, and both can be nested when you send slab photos.\nFiles are DWG and PDF.\nThe exact price is confirmed after we review the drawings.",
    "pool": "Pool and terrace tiling is drawn as a shop-drawing layout: piece sizes, joints, edges and piece numbers.\nSections show the build-up and the edges that are in the design you send.\nFiles are DWG and PDF.\nThe exact price is confirmed after we review the drawings.",
    "door-frame": "Door-frame stone is drawn with piece sizes, joints and the profile.\nIt can be nested with skirting on the slab photos you send, so the vein can continue.\nFiles are DWG and PDF.\nThe exact price is confirmed after we review the drawings.",
    "no-supply": "D3DDD prepares the drawings. The studio does not sell or stock slabs.\nSend slab photos when you want nesting, plus the stone name, thickness and finish.\nShop drawings are issued as DWG and PDF. Packs start from around AED 1,200.",
    "shop-what": "Shop drawings are detailed AutoCAD fabrication and installation drawings.\nThey show how marble or stone will be cut, finished and installed.\nDesign drawings show the intent. Shop drawings show the execution: piece sizes, joints, edges, fixing and interfaces.\nYou receive DWG and PDF.",
    "shop-vs-design": "Design drawings show the intent: the look and the layout.\nShop drawings show the execution: piece sizes, joints, edges, fixing and how the stone meets other work.\nOn most UAE projects, fabrication follows the shop drawings after the consultant approves them.\nShop drawings are issued as DWG and PDF.",
    "why-needed": "On most UAE projects the consultant approves shop drawings before fabrication.\nCutting stone is irreversible. A wrong cut means new slabs and delay.\nThe drawings also set slab nesting, vein matching and bookmatching, and they coordinate joinery, MEP, glass, metal and sanitaryware.\nThey give quantities for the BOQ, and on site each piece is numbered.",
    "full-set": "A complete set usually includes:\n• Layout plans and wall elevations, with setting-out, joints, borders, inlays and piece numbers\n• Sections: build-up, adhesive or mechanical fixing, edge profiles and interfaces\n• Stone, thickness, finish, vein direction, bookmatching, and a cutting list that can go to Excel\n• Slab nesting when you send slab photos, plus a revision table and title block\nUnconfirmed site sizes are marked “not for cut”. Files are DWG and PDF.",
    "what-to-send": "Please email:\n• Architectural or design drawings (PDF or DWG)\n• Site measurements or a sketch\n• Slab photos, if you have them\n• Stone name, thickness and finish\n• Your deadline\nSend the files to ADDRESS. This chat cannot take attachments. Price and delivery are confirmed in writing after review.",
    "how-to-start": "Email the design drawings, measurements or a sketch, the stone name, thickness, finish and your deadline to ADDRESS.\nWe review them and confirm the price and delivery in writing.\nAll jobs are 50% upfront.\nWe are based in Dubai and deliver the files digitally across the UAE.",
    "draft-bim": "Drafting here is AutoCAD 2D construction drawings, not BIM.\nA BIM model or a municipal permit submission is not included unless it is quoted separately.\nPermit-oriented sheets can still be prepared from the checklist you send.\nShop drawings and construction sets are issued as DWG and PDF.",
    "draft-permit": "Permit-oriented sets are drawn from the checklist you send. Requirements vary by emirate.\nThe set is AutoCAD 2D: plans, elevations, sections and details, as your list requires.\nDrawing the set is not the same as lodging it with the municipality. Submission is separate unless it is quoted.\nThis is not a BIM service.",
    "draft-arabic": "English notes are standard on the drawings.\nArabic or bilingual notes are added when you ask for them.\nSay which you want, on the stone set or the architectural set.\nThe price of that scope is confirmed with the rest of the job.",
    "draft-layers": "If you send a title block and a layer standard, the drawings follow them.\nEach issue still has a revision table, and changes can be clouded.\nNotes are in English unless you ask for Arabic or bilingual notes.\nFiles are AutoCAD DWG and PDF.",
    "draft-rcp": "Yes. Reflected ceiling plans are part of the architectural and fit-out set.\nThey are AutoCAD 2D, with details as the job needs, and a revision table.\nYour title block and layers are followed when you send them.\nThis is not BIM. The price is confirmed after we review the drawings.",
    "draft-overview": "Architectural and fit-out drafting is AutoCAD 2D: plans, elevations, sections, reflected ceiling plans and details, with a revision table.\nEnglish notes are standard. Arabic or bilingual notes are available on request. Your title block and layers are followed when you send them.\nPermit-oriented sets can be drawn from your checklist. This is not BIM, and not a municipal submission, unless that is quoted.\nThe price is confirmed in writing after review. All jobs are 50% upfront.",
    "interior": "Interior design support covers concept layouts, space planning and elevations, then design development before shop drawings.\nThe aim is a layout that can later be dimensioned.\nIt is not a signed consultancy appointment, and not a permit design, unless that is written into the quote.\nThe fee is confirmed after we review the brief.",
    "estimation": "Estimation covers a BOQ, quantity take-off in square metres and linear metres, material schedules and tender packages measured from the drawings.\nStone quantities can be taken from the shop drawings when that work is included.\nSchedules can be Excel-ready, and assumptions are written down.\nThere is no published rate per square metre. The price is confirmed after we review the drawings. All jobs are 50% upfront.",
    "viz": "3D visualization covers still renders, material studies, presentation images and simple walkthroughs.\nA single still render starts from AED 650.\nRenders are for approval and presentation only. They are not fabrication drawings.\nThe exact price is confirmed in writing. All jobs are 50% upfront.",
    "website": "Website packages, 50% upfront:\n• Starter, AED 1,200: 1 page, mobile-friendly, contact form, SEO basics\n• Business, AED 2,000: up to 5 pages, mobile-friendly, contact form, SEO basics\n• Premium, AED 3,500+: more pages and custom features\nDomain, hosting and stock images are extra unless agreed.\nDemo themes cover carpentry, marble, fit-out, contracting, consultants, trading and interior designers.",
    "pricing": "Marble and stone shop-drawing packs start from around AED 1,200.\nA single still render starts from AED 650. Renders are for approval, not fabrication.\nWebsites: Starter AED 1,200, Business AED 2,000, Premium from AED 3,500. Domain and hosting are extra unless agreed.\nDrafting and estimation are priced after we review the drawings.\nAll jobs are 50% upfront. Exact price and delivery are confirmed in writing after that review.",
    "place": "D3DDD is based in Dubai.\nFiles are delivered digitally across the UAE: Abu Dhabi, Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah and Fujairah as well.\nThe exact delivery is confirmed in writing with the price.\nAll jobs are 50% upfront.",
    "shop-overview": "Marble and stone shop drawings are AutoCAD fabrication and installation drawings, issued as DWG and PDF.\nA set can include plans, elevations, sections, fixing, edge profiles, a cutting list and slab nesting when you send slab photos.\nWork covers vanities, countertops, islands, stairs, cladding, flooring, fireplaces, waterjet inlays, skirting and pool or terrace tiling.\nPacks start from around AED 1,200, with 50% upfront. The exact price is confirmed after we review your drawings."
  },
  "ur": {
    "edges": "کنارے کے عام پروفائل:\n• پنسل / ایزڈ ایج\n• بل نوز: فل، ہاف اور ڈیمی\n• چیمفر / بیول (45°)\n• اوگی / لیمبز ٹنگ\n• مائٹرڈ کونے (موٹا رخ یا کلیڈنگ ریٹرن)\n• اسکوائر ایج، ہلکی ایزڈ ایریس کے ساتھ\nخصوصی پروفائل درخواست پر بن سکتا ہے۔ ہر کنارے کا کوڈ شیٹ پر ہوتا ہے۔",
    "thickness": "ان ڈرائنگز پر عام موٹائی 18، 20 اور 30 ملی میٹر ہے۔\nجو موٹائی آپ بتائیں، وہ پلان اور سیکشن پر پتھر کے نام اور فنش کے ساتھ لکھی جاتی ہے۔\nڈرائنگ بھیجتے وقت موٹائی لکھ دیں۔ اگر ابھی طے نہیں، یہ بھی بتا دیں۔\nدرست قیمت ڈرائنگ دیکھنے کے بعد تحریر میں طے ہوتی ہے۔",
    "finishes": "فنش ڈرائنگ پر لکھا جاتا ہے۔\nعام فنش پالش، ہونڈ، لیدرڈ اور فلیمڈ ہیں۔\nسیلنگ وہاں لکھی جاتی ہے جہاں آپ کی اسپیسفکیشن مانگے۔\nفنش، پتھر کا نام اور موٹائی ساتھ بھیجیں۔",
    "vein": "وین کی سمت اور بک میچنگ وہاں دکھائی جاتی ہے جہاں ڈیزائن ان پر منحصر ہو۔\nبک میچنگ وین کا آئینہ بناتی ہے۔ وین میچنگ دانے کو ٹکڑے سے ٹکڑے تک جوڑتی ہے۔\nسلیب کی تصاویر ملنے پر یہ نیسٹنگ لے آؤٹ پر سیٹ ہوتا ہے، تاکہ ورکشاپ اسی پر چلے۔",
    "slab": "سلیب نیسٹنگ تب بنتی ہے جب آپ سلیب کی تصاویر بھیجیں۔\nٹکڑے سلیب پر CNC یا واٹر جیٹ کٹنگ کے لیے رکھے جاتے ہیں، تاکہ وین رہے اور ضیاع کم ہو۔\nتصاویر، ڈیزائن ڈرائنگ اور پتھر کا نام ساتھ بھیجیں۔\nنیسٹنگ DWG اور PDF سیٹ کے ساتھ ملتی ہے۔",
    "cutting-list": "پیس شیڈول ہر ٹکڑا لکھتا ہے: آئی ڈی، سائز، ایج کوڈ، تعداد اور جگہ۔\nوہی نمبر پلان پر ہوتے ہیں، اس لیے ورکشاپ اور سائٹ ایک فہرست استعمال کرتی ہیں۔\nیہ ایکسل میں برآمد ہو سکتا ہے۔\nیہ شاپ ڈرائنگ کے ساتھ ہوتا ہے، جو DWG اور PDF میں ملتی ہے۔",
    "revisions": "ہر ایشو میں ریویژن ٹیبل اور ٹائٹل بلاک ہوتا ہے۔ تبدیلیاں کلاؤڈ ہوتی ہیں۔\nاگر آپ اپنا ٹائٹل بلاک اور لیئر معیار بھیجیں تو شیٹس اسی پر چلتی ہیں۔\nیہ پتھر کی شاپ ڈرائنگ اور آرکیٹیکچرل سیٹ دونوں پر لاگو ہے۔\nفائلیں DWG اور PDF ہوتی ہیں۔",
    "not-for-cut": "اگر سائٹ کی کوئی پیمائش تصدیق شدہ نہیں، تو وہ “ناٹ فار کٹ” لکھی جاتی ہے جب تک چیک نہ ہو۔\nیہ سائز آرے کے لیے نہیں ہوتے۔\nسائٹ کی پیمائش بھیجیں، یا تصدیق کریں کہ ڈرائنگ بنی ہوئی سائٹ سے میل کھاتی ہے۔",
    "formats": "شاپ ڈرائنگ اور ڈرافٹنگ سیٹ DWG اور PDF میں ملتے ہیں۔\nDWG آٹوکیڈ فائل ہے۔ PDF جائزے اور سائٹ کے لیے ہے۔\nکٹنگ لسٹ ایکسل میں جا سکتی ہے جب وہ سیٹ کا حصہ ہو۔\nکوئی اور فارمیٹ صرف تب استعمال ہوتا ہے جب کوٹ میں طے ہو۔",
    "sections-fixing": "سیکشن بلڈ اپ، کنارہ، اور پتھر کا اسکرٹنگ، شیشے، جوئنری اور تھریشولڈ سے ملاپ دکھاتے ہیں۔\nفکسنگ ویسی بنتی ہے جیسی بتائی جائے: چپکنے والا، یا مکینیکل اینکر۔\nپتھر کا نام، موٹائی اور فنش اسی ڈیٹیل پر لکھے جاتے ہیں۔\nفائلیں DWG اور PDF ہوتی ہیں۔",
    "layouts": "لے آؤٹ پلان فرش اور دیوار کی ایلیویشن ڈھانپتے ہیں۔\nان میں سیٹنگ آؤٹ پوائنٹ، ٹکڑے کا سائز، جوڑ کی چوڑائی، ایکسپینشن جوڑ، بارڈر، انلے اور پیس نمبر ہوتے ہیں۔\nایلیویشن ہر پینل کا نمبر کٹنگ لسٹ سے جوڑتی ہے۔\nفائلیں DWG اور PDF ہوتی ہیں۔",
    "vanity": "جی ہاں۔ وینٹی ٹاپ ماربل اور پتھر کی شاپ ڈرائنگ کا حصہ ہیں۔\nسیٹ میں لے آؤٹ، ٹکڑے کا سائز، جوڑ، ایج پروفائل، موٹائی، فنش، اور ٹاپ کا جوئنری سے ملاپ ہوتا ہے۔\nکٹنگ لسٹ شامل ہو سکتی ہے۔ فائلیں DWG اور PDF ہوتی ہیں۔\nپیکج تقریباً 1,200 درہم سے ہیں۔ درست قیمت ڈرائنگ دیکھنے کے بعد طے ہوتی ہے۔",
    "countertop": "کاؤنٹر ٹاپ کی شاپ ڈرائنگ میں پلان، ٹکڑے کا سائز، جوڑ، ایج پروفائل، موٹائی اور فنش ہوتا ہے۔\nسیکشن کنارہ اور وہ فکسنگ یا سہارا دکھاتے ہیں جو بتایا گیا ہو۔\nکٹنگ لسٹ شامل ہو سکتی ہے۔ فائلیں DWG اور PDF ہوتی ہیں۔\nدرست قیمت ڈرائنگ کے جائزے کے بعد تحریر میں طے ہوتی ہے۔",
    "island": "کچن آئلینڈ کی شاپ ڈرائنگ پتھر کے ٹاپ کو ڈھانپتی ہے: لے آؤٹ، جوڑ، ایج پروفائل، موٹائی اور فنش۔\nسیکشن کنارہ اور ٹاپ کا جوئنری سے ملاپ دکھاتے ہیں۔\nکٹنگ لسٹ شامل ہو سکتی ہے۔ فائلیں DWG اور PDF ہوتی ہیں۔\nدرست قیمت آپ کی ڈرائنگ کے جائزے کے بعد طے ہوتی ہے۔",
    "stairs": "سیڑھیوں کی شاپ ڈرائنگ ٹریڈ، رائزر اور نوزنگ ڈھانپتی ہے۔\nاس میں ٹکڑے کا سائز، ایج پروفائل، موٹائی، فنش اور بتائی گئی فکسنگ ہوتی ہے۔\nکٹنگ لسٹ شامل ہو سکتی ہے۔ فائلیں DWG اور PDF ہوتی ہیں۔\nدرست قیمت سیڑھی کی ڈرائنگ دیکھنے کے بعد طے ہوتی ہے۔",
    "cladding": "وال کلیڈنگ کی ڈرائنگ میں ایلیویشن، پینل کا سائز، جوڑ اور پیس نمبر ہوتے ہیں۔\nسیکشن بلڈ اپ اور فکسنگ دکھاتے ہیں: چپکنے والا یا مکینیکل اینکر، جیسا بتایا جائے۔\nکھلنے والی جگہوں اور دوسرے کام سے ملاپ دکھایا جاتا ہے۔ فائلیں DWG اور PDF ہوتی ہیں۔\nدرست قیمت ڈرائنگ کے جائزے کے بعد طے ہوتی ہے۔",
    "flooring": "فرش کی شاپ ڈرائنگ لے آؤٹ پلان ہوتی ہے: سیٹنگ آؤٹ، ٹکڑے کا سائز، جوڑ کی چوڑائی اور ایکسپینشن جوڑ۔\nبارڈر، انلے اور پیس نمبر، پتھر، موٹائی اور فنش کے ساتھ دکھائے جاتے ہیں۔\nکٹنگ لسٹ شامل ہو سکتی ہے۔ فائلیں DWG اور PDF ہوتی ہیں۔\nدرست قیمت ڈرائنگ کے جائزے کے بعد طے ہوتی ہے۔",
    "fireplace": "فائر پلیس کا پتھر شاپ ڈرائنگ پیکج میں بنتا ہے: لے آؤٹ، ٹکڑے کا سائز، جوڑ، کنارے، موٹائی اور فنش۔\nفکسنگ ویسی دکھائی جاتی ہے جیسی بتائی جائے۔ کٹنگ لسٹ شامل ہو سکتی ہے۔\nفائلیں DWG اور PDF ہوتی ہیں۔\nڈیزائن ڈرائنگ بھیجیں، درست قیمت تحریر میں طے ہوگی۔",
    "waterjet": "واٹر جیٹ میڈالین اور انلے شاپ ڈرائنگ سیٹ میں بنتے ہیں۔\nلے آؤٹ میں پیٹرن، جوڑ اور پیس نمبر ہوتے ہیں۔\nسلیب کی تصاویر ملنے پر واٹر جیٹ کے لیے سلیب نیسٹنگ بن سکتی ہے۔\nفائلیں DWG اور PDF ہوتی ہیں۔ درست قیمت جائزے کے بعد طے ہوتی ہے۔",
    "skirting": "اسکرٹنگ پتھر کے پیکج کے ساتھ بنتی ہے: ٹکڑے کا سائز، جوڑ، موٹائی، فنش، اور فرش یا دیوار سے ملاپ۔\nدروازے کے فریم اسی طرح کے سیٹ میں آ سکتے ہیں، اور سلیب کی تصاویر پر دونوں کی نیسٹنگ ہو سکتی ہے۔\nفائلیں DWG اور PDF ہوتی ہیں۔\nدرست قیمت ڈرائنگ کے جائزے کے بعد طے ہوتی ہے۔",
    "pool": "پول اور ٹیرس کی ٹائلنگ شاپ ڈرائنگ لے آؤٹ میں بنتی ہے: ٹکڑے کا سائز، جوڑ، کنارے اور پیس نمبر۔\nسیکشن بلڈ اپ اور وہ کنارے دکھاتے ہیں جو آپ کے بھیجے ڈیزائن میں ہوں۔\nفائلیں DWG اور PDF ہوتی ہیں۔\nدرست قیمت ڈرائنگ کے جائزے کے بعد طے ہوتی ہے۔",
    "door-frame": "دروازے کے فریم کا پتھر ٹکڑے کے سائز، جوڑ اور پروفائل کے ساتھ بنتا ہے۔\nآپ کی سلیب تصاویر پر یہ اسکرٹنگ کے ساتھ نیسٹ ہو سکتا ہے، تاکہ وین جاری رہے۔\nفائلیں DWG اور PDF ہوتی ہیں۔\nدرست قیمت ڈرائنگ کے جائزے کے بعد طے ہوتی ہے۔",
    "no-supply": "D3DDD ڈرائنگ بناتا ہے۔ سٹوڈیو سلیب نہ بیچتا ہے نہ اسٹاک رکھتا ہے۔\nنیسٹنگ کے لیے سلیب کی تصاویر بھیجیں، اور پتھر کا نام، موٹائی اور فنش۔\nشاپ ڈرائنگ DWG اور PDF میں ملتی ہے۔ پیکج تقریباً 1,200 درہم سے ہیں۔",
    "shop-what": "شاپ ڈرائنگ آٹوکیڈ کی تفصیلی فیبریکیشن اور انسٹالیشن ڈرائنگ ہوتی ہے۔\nاس میں بتایا جاتا ہے کہ ماربل یا پتھر کیسے کٹے گا، فنش ہوگا اور لگے گا۔\nڈیزائن ڈرائنگ ارادہ دکھاتی ہے۔ شاپ ڈرائنگ عمل دکھاتی ہے: ٹکڑے کا سائز، جوڑ، کنارہ، فکسنگ اور ملاپ۔\nفائل DWG اور PDF میں ملتی ہے۔",
    "shop-vs-design": "ڈیزائن ڈرائنگ ارادہ دکھاتی ہے: شکل اور لے آؤٹ۔\nشاپ ڈرائنگ عمل دکھاتی ہے: ٹکڑے کا سائز، جوڑ، کنارہ، فکسنگ، اور پتھر کا دوسرے کام سے ملاپ۔\nزیادہ تر متحدہ عرب امارات کے منصوبوں پر کنسلٹنٹ کی منظوری کے بعد فیبریکیشن شاپ ڈرائنگ سے ہوتی ہے۔\nشاپ ڈرائنگ DWG اور PDF میں ملتی ہے۔",
    "why-needed": "زیادہ تر متحدہ عرب امارات کے منصوبوں پر کنسلٹنٹ فیبریکیشن سے پہلے شاپ ڈرائنگ منظور کرتا ہے۔\nپتھر کاٹنا واپس نہیں ہوتا۔ غلط کٹ کا مطلب نئی سلیب اور تاخیر ہے۔\nڈرائنگ سلیب نیسٹنگ، وین میچنگ اور بک میچنگ بھی طے کرتی ہیں، اور جوئنری، ایم ای پی، شیشہ، دھات اور سینیٹری وئیر سے ملاپ کرتی ہیں۔\nبی او کیو کے لیے مقدار ملتی ہے، اور سائٹ پر ہر ٹکڑے کا نمبر ہوتا ہے۔",
    "full-set": "مکمل سیٹ میں عموماً یہ شامل ہوتا ہے:\n• لے آؤٹ پلان اور دیوار کی ایلیویشن، سیٹنگ آؤٹ، جوڑ، بارڈر، انلے اور پیس نمبر کے ساتھ\n• سیکشن: بلڈ اپ، چپکنے والی یا مکینیکل فکسنگ، ایج پروفائل اور ملاپ\n• پتھر، موٹائی، فنش، وین کی سمت، بک میچنگ، اور کٹنگ لسٹ جو ایکسل میں جا سکے\n• سلیب کی تصاویر پر نیسٹنگ، اور ریویژن ٹیبل و ٹائٹل بلاک\nغیر تصدیق شدہ سائٹ سائز “ناٹ فار کٹ” لکھے جاتے ہیں۔ فائلیں DWG اور PDF ہوتی ہیں۔",
    "what-to-send": "براہ کرم ای میل کریں:\n• آرکیٹیکچرل یا ڈیزائن ڈرائنگ (PDF یا DWG)\n• سائٹ کی پیمائش یا خاکہ\n• سلیب کی تصاویر، اگر ہوں\n• پتھر کا نام، موٹائی اور فنش\n• آپ کی ڈیڈ لائن\nفائلیں ADDRESS پر بھیجیں۔ یہ چیٹ منسلکہ نہیں لیتی۔ قیمت اور ڈیلیوری جائزے کے بعد تحریر میں طے ہوتی ہے۔",
    "how-to-start": "ڈیزائن ڈرائنگ، پیمائش یا خاکہ، پتھر کا نام، موٹائی، فنش اور ڈیڈ لائن ADDRESS پر ای میل کریں۔\nہم دیکھ کر قیمت اور ڈیلیوری تحریر میں کنفرم کرتے ہیں۔\nہر کام پر 50 فیصد پیشگی ہے۔\nہم دبئی میں ہیں اور فائلیں تمام متحدہ عرب امارات میں ڈیجیٹل بھیجتے ہیں۔",
    "draft-bim": "یہاں ڈرافٹنگ آٹوکیڈ 2D کنسٹرکشن ڈرائنگ ہے، BIM نہیں۔\nBIM ماڈل یا میونسپل پرمٹ جمع کرانا شامل نہیں، جب تک الگ کوٹ نہ ہو۔\nپرمٹ کے لیے شیٹس آپ کی چیک لسٹ سے پھر بھی بن سکتی ہیں۔\nشاپ ڈرائنگ اور کنسٹرکشن سیٹ DWG اور PDF میں ملتے ہیں۔",
    "draft-permit": "پرمٹ والی سیٹیں آپ کی بھیجی چیک لسٹ سے بنتی ہیں۔ تقاضے امارت کے حساب سے بدلتے ہیں۔\nسیٹ آٹوکیڈ 2D ہوتی ہے: پلان، ایلیویشن، سیکشن اور ڈیٹیل، جیسی آپ کی فہرست ہو۔\nسیٹ بنانا میونسپلٹی میں جمع کرانا نہیں ہے۔ جمع کروانا الگ ہے، جب تک کوٹ نہ ہو۔\nیہ BIM سروس نہیں۔",
    "draft-arabic": "ڈرائنگ پر انگریزی نوٹس معیار ہیں۔\nعربی یا دو زبانی نوٹس آپ کے کہنے پر شامل ہوتے ہیں۔\nبتائیں کہ پتھر کے سیٹ پر چاہییں یا آرکیٹیکچرل سیٹ پر۔\nاس کام کی قیمت باقی جاب کے ساتھ طے ہوتی ہے۔",
    "draft-layers": "اگر آپ ٹائٹل بلاک اور لیئر کا معیار بھیجیں تو ڈرائنگ اسی پر چلتی ہے۔\nہر ایشو میں ریویژن ٹیبل رہتا ہے، اور تبدیلیاں کلاؤڈ ہو سکتی ہیں۔\nنوٹس انگریزی میں ہوتے ہیں، جب تک آپ عربی یا دو زبانی نوٹس نہ مانگیں۔\nفائلیں آٹوکیڈ DWG اور PDF ہوتی ہیں۔",
    "draft-rcp": "جی ہاں۔ ریفلیکٹڈ سیلنگ پلان آرکیٹیکچرل اور فٹ آؤٹ سیٹ کا حصہ ہیں۔\nیہ آٹوکیڈ 2D ہوتے ہیں، ضرورت کے مطابق ڈیٹیل اور ریویژن ٹیبل کے ساتھ۔\nآپ کا ٹائٹل بلاک اور لیئرز، اگر بھیجیں، فالو ہوتے ہیں۔\nیہ BIM نہیں۔ قیمت ڈرائنگ کے جائزے کے بعد طے ہوتی ہے۔",
    "draft-overview": "آرکیٹیکچرل اور فٹ آؤٹ ڈرافٹنگ آٹوکیڈ 2D ہے: پلان، ایلیویشن، سیکشن، ریفلیکٹڈ سیلنگ پلان اور ڈیٹیل، ریویژن ٹیبل کے ساتھ۔\nانگریزی نوٹس معیار ہیں۔ عربی یا دو زبانی نوٹس درخواست پر۔ آپ کا ٹائٹل بلاک اور لیئرز، اگر بھیجیں، فالو ہوتے ہیں۔\nپرمٹ والی سیٹ آپ کی چیک لسٹ سے بن سکتی ہے۔ یہ BIM نہیں، اور میونسپل جمع کرانا نہیں، جب تک کوٹ نہ ہو۔\nقیمت جائزے کے بعد تحریر میں طے ہوتی ہے۔ ہر کام پر 50 فیصد پیشگی ہے۔",
    "interior": "انٹیریر ڈیزائن سپورٹ میں تصوراتی لے آؤٹ، اسپیس پلاننگ اور ایلیویشن، پھر شاپ ڈرائنگ سے پہلے ڈیزائن ڈیولپمنٹ شامل ہے۔\nمقصد ایسا لے آؤٹ ہے جسے بعد میں ڈائمینشن دیا جا سکے۔\nیہ دستخط شدہ کنسلٹنسی تقرری نہیں، اور پرمٹ ڈیزائن نہیں، جب تک کوٹ میں لکھا نہ ہو۔\nفیس بریف دیکھنے کے بعد طے ہوتی ہے۔",
    "estimation": "تخمینے میں بی او کیو، مربع میٹر اور لمبائی میٹر میں کوانٹٹی ٹیک آف، میٹریل شیڈول، اور ڈرائنگ سے ناپے ٹینڈر پیکج شامل ہیں۔\nپتھر کی مقدار شاپ ڈرائنگ سے نکل سکتی ہے جب یہ کام شامل ہو۔\nشیڈول ایکسل میں جا سکتے ہیں، اور مفروضے لکھے جاتے ہیں۔\nمربع میٹر کی کوئی شائع شدہ ریٹ نہیں۔ قیمت ڈرائنگ کے جائزے کے بعد طے ہوتی ہے۔ ہر کام پر 50 فیصد پیشگی ہے۔",
    "viz": "تھری ڈی ویژولائزیشن میں اسٹل رینڈر، میٹریل اسٹڈی، پریزنٹیشن تصاویر اور سادہ واک تھرو شامل ہیں۔\nایک اسٹل رینڈر 650 درہم سے شروع ہوتا ہے۔\nرینڈر منظوری اور پیشکش کے لیے ہیں۔ یہ فیبریکیشن ڈرائنگ نہیں۔\nدرست قیمت تحریر میں طے ہوتی ہے۔ ہر کام پر 50 فیصد پیشگی ہے۔",
    "website": "ویب سائٹ پیکج، 50 فیصد پیشگی:\n• سٹارٹر، 1,200 درہم: 1 صفحہ، موبائل، رابطہ فارم، بنیادی SEO\n• بزنس، 2,000 درہم: 5 صفحات تک، موبائل، رابطہ فارم، بنیادی SEO\n• پریمیم، 3,500 درہم سے: مزید صفحات اور حسبِ ضرورت فیچر\nڈومین، ہوسٹنگ اور اسٹاک تصاویر الگ ہیں، جب تک طے نہ ہوں۔\nڈیمو تھیمز: کارپینٹری، ماربل، فٹ آؤٹ، کنٹریکٹنگ، کنسلٹنٹ، ٹریڈنگ اور انٹیریر ڈیزائنرز۔",
    "pricing": "ماربل اور پتھر کی شاپ ڈرائنگ کے پیکج تقریباً 1,200 درہم سے شروع ہوتے ہیں۔\nایک اسٹل رینڈر 650 درہم سے ہے۔ رینڈر منظوری کے لیے ہیں، فیبریکیشن کے لیے نہیں۔\nویب سائٹ: سٹارٹر 1,200 درہم، بزنس 2,000 درہم، پریمیم 3,500 درہم سے۔ ڈومین اور ہوسٹنگ الگ ہیں، جب تک طے نہ ہوں۔\nڈرافٹنگ اور تخمینہ ڈرائنگ کے جائزے کے بعد قیمت پاتے ہیں۔\nہر کام پر 50 فیصد پیشگی ہے۔ درست قیمت اور ڈیلیوری اس جائزے کے بعد تحریر میں طے ہوتی ہے۔",
    "place": "D3DDD دبئی میں ہے۔\nفائلیں تمام متحدہ عرب امارات میں ڈیجیٹل پہنچتی ہیں: ابوظبی، شارجہ، عجمان، ام القوین، راس الخیمہ اور فجیرہ بھی۔\nدرست ڈیلیوری قیمت کے ساتھ تحریر میں طے ہوتی ہے۔\nہر کام پر 50 فیصد پیشگی ہے۔",
    "shop-overview": "ماربل اور پتھر کی شاپ ڈرائنگ آٹوکیڈ کی فیبریکیشن اور انسٹالیشن ڈرائنگ ہے، DWG اور PDF میں۔\nسیٹ میں پلان، ایلیویشن، سیکشن، فکسنگ، ایج پروفائل، کٹنگ لسٹ، اور سلیب کی تصاویر پر نیسٹنگ شامل ہو سکتی ہے۔\nکام میں وینٹی، کاؤنٹر ٹاپ، آئلینڈ، سیڑھیاں، کلیڈنگ، فرش، فائر پلیس، واٹر جیٹ انلے، اسکرٹنگ اور پول یا ٹیرس ٹائلنگ آتی ہے۔\nپیکج تقریباً 1,200 درہم سے ہیں، 50 فیصد پیشگی۔ درست قیمت ڈرائنگ دیکھنے کے بعد طے ہوتی ہے۔"
  }
};

  function fold(s) {
    return String(s || "")
      .replace(/[\u0660-\u0669]/g, function (ch) { return String(ch.charCodeAt(0) - 0x0660); })
      .replace(/[\u06F0-\u06F9]/g, function (ch) { return String(ch.charCodeAt(0) - 0x06F0); })
      .toLowerCase()
      .replace(/[\u064B-\u0652\u0670\u0640]/g, "")
      .replace(/\u064A/g, "\u06CC")
      .replace(/\u0643/g, "\u06A9")
      .replace(/['’`]/g, "")
      .replace(/\bwhats\b/g, "what is")
      .replace(/\bwhos\b/g, "who is")
      .replace(/%/g, " percent ")
      .replace(/&/g, " and ")
      .replace(/(\d+)\s*mm\b/g, "$1mm")
      .replace(/\b3\s*d\b/g, "3d")
      .replace(/\b2\s*d\b/g, "2d")
      .replace(/[^\u0600-\u06FFa-z0-9]+/g, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function stem(w) {
    if (!/^[a-z0-9]+$/.test(w)) return w;
    if (w.length > 4 && w.slice(-3) === "ies") return w.slice(0, -3) + "y";
    if (w.length > 4 && /(?:ches|shes|sses|xes|zes)$/.test(w)) return w.slice(0, -2);
    if (w.length > 3 && w.charAt(w.length - 1) === "s" && w.slice(-2) !== "ss") return w.slice(0, -1);
    return w;
  }

  function hamming(a, b) {
    if (a.length !== b.length) return 99;
    var n = 0, i;
    for (i = 0; i < a.length; i++) if (a.charCodeAt(i) !== b.charCodeAt(i)) n++;
    return n;
  }

  function editDist(a, b) {
    var la = a.length, lb = b.length, i, j, cost;
    if (a === b) return 0;
    if (!la) return lb;
    if (!lb) return la;
    if (Math.abs(la - lb) > 2) return 3;
    var dp = new Array(la + 1);
    for (i = 0; i <= la; i++) {
      dp[i] = new Array(lb + 1);
      dp[i][0] = i;
    }
    for (j = 0; j <= lb; j++) dp[0][j] = j;
    for (i = 1; i <= la; i++) {
      for (j = 1; j <= lb; j++) {
        cost = a.charCodeAt(i - 1) === b.charCodeAt(j - 1) ? 0 : 1;
        dp[i][j] = dp[i - 1][j] + 1;
        if (dp[i][j - 1] + 1 < dp[i][j]) dp[i][j] = dp[i][j - 1] + 1;
        if (dp[i - 1][j - 1] + cost < dp[i][j]) dp[i][j] = dp[i - 1][j - 1] + cost;
        if (i > 1 && j > 1 && a.charCodeAt(i - 1) === b.charCodeAt(j - 2) && a.charCodeAt(i - 2) === b.charCodeAt(j - 1)) {
          if (dp[i - 2][j - 2] + 1 < dp[i][j]) dp[i][j] = dp[i - 2][j - 2] + 1;
        }
      }
    }
    return dp[la][lb];
  }

  function tokenSim(qTok, kTok) {
    if (!qTok || !kTok) return 0;
    if (qTok === kTok) return 1;
    var qs = stem(qTok);
    var ks = stem(kTok);
    if (qs === ks) return 1;
    if (ks.length <= 3 || qs.length <= 3) return 0;
    var longer = qs.length >= ks.length ? qs : ks;
    var shorter = qs.length >= ks.length ? ks : qs;
    var nonAscii = /[^\u0000-\u007f]/.test(shorter);
    var minPrefix = nonAscii ? 3 : 5;
    var maxExtra = nonAscii ? 6 : 4;
    if (shorter.length >= minPrefix && longer.indexOf(shorter) === 0 && (longer.length - shorter.length) <= maxExtra) return 0.94;
    var d = editDist(qs, ks);
    var minL = qs.length < ks.length ? qs.length : ks.length;
    if (d === 1 && minL >= 5) {
      if (qs.length === ks.length && hamming(qs, ks) === 1 && minL < 8) return 0;
      return 0.88;
    }
    if (d === 2 && minL >= 8) return 0.74;
    return 0;
  }

  function phraseScore(tokens, phrase, weight) {
    var parts = fold(phrase).split(" ");
    var p, i, j, sim, best, used, sum, ok, avg, bestAvg, end, t, clean = [];
    for (i = 0; i < parts.length; i++) if (parts[i]) clean.push(parts[i]);
    parts = clean;
    if (!parts.length || !weight) return 0;
    if (parts.length === 1) {
      best = 0;
      for (i = 0; i < tokens.length; i++) {
        sim = tokenSim(tokens[i], parts[0]);
        if (sim > best) best = sim;
      }
      return best >= 0.74 ? weight * best : 0;
    }
    var width = parts.length + 2;
    bestAvg = 0;
    for (i = 0; i < tokens.length; i++) {
      end = i + width;
      if (end > tokens.length) end = tokens.length;
      if (end - i < parts.length) break;
      used = [];
      sum = 0;
      ok = true;
      for (p = 0; p < parts.length; p++) {
        best = 0;
        t = -1;
        for (j = i; j < end; j++) {
          if (used[j]) continue;
          sim = tokenSim(tokens[j], parts[p]);
          if (sim > best) { best = sim; t = j; }
        }
        if (t < 0 || best < 0.74) { ok = false; break; }
        used[t] = 1;
        sum += best;
      }
      if (!ok) continue;
      avg = sum / parts.length;
      if (avg > bestAvg) bestAvg = avg;
    }
    return bestAvg >= 0.74 ? weight * bestAvg : 0;
  }

  function blocked(id, tokens) {
    var blob = " " + tokens.join(" ") + " ";
    if (id === "finishes") {
      var material = /polished|honed|leather|flamed|flame|surface|stone|marble|فنش|پالش|ہونڈ/.test(blob);
      var timing = /\b(when|timeline|deadline|kab)\b/.test(blob) || blob.indexOf(" how long ") !== -1 || blob.indexOf(" when will ") !== -1;
      if (timing && !material) return true;
    }
    if (id === "revisions" && blob.indexOf(" cloud ") !== -1 && blob.indexOf(" revision ") === -1 && blob.indexOf(" title ") === -1 && blob.indexOf(" clouded ") === -1) {
      return true;
    }
    return false;
  }

  function scoreIntent(tokens, intent) {
    if (blocked(intent.id, tokens)) return 0;
    var peak = 0, sum = 0, i, s;
    for (i = 0; i < intent.keys.length; i++) {
      s = phraseScore(tokens, intent.keys[i][0], intent.keys[i][1]);
      if (s > peak) peak = s;
      sum += s;
    }
    if (peak < 13) return 0;
    var extra = sum - peak;
    if (extra > 6) extra = 6;
    return peak + extra * 0.1;
  }

  function matchIntent(raw) {
    var folded = fold(raw);
    if (!folded) return null;
    var tokens = folded.split(" ");
    var best = null, bestScore = 0, bestPri = -1, i, s, pri;
    for (i = 0; i < INTENTS.length; i++) {
      s = scoreIntent(tokens, INTENTS[i]);
      pri = INTENTS[i].pri || 0;
      if (s > bestScore + 0.001 || (s > 0 && Math.abs(s - bestScore) <= 0.001 && pri > bestPri)) {
        bestScore = s;
        bestPri = pri;
        best = INTENTS[i].id;
      }
    }
    return best;
  }

  function wantsLead(raw) {
    var q = fold(raw);
    var phrases = ["get a quote", "get quote", "request a quote", "need a quote", "want a quote", "send my details", "get in touch", "quotation please", "quote please", "کوٹ حاصل", "تفصیل بھیج"];
    var i;
    if (!q) return false;
    if (q === "quote" || q === "quotes" || q === "quotation" || q === "کوٹ") return true;
    for (i = 0; i < phrases.length; i++) {
      if (q.indexOf(fold(phrases[i])) !== -1) return true;
    }
    return false;
  }

  var STEPS = [
    { id: "name", kind: "text", required: true, auto: "name" },
    { id: "company", kind: "text", required: false, auto: "organization" },
    { id: "phone", kind: "text", required: false, auto: "tel" },
    { id: "email", kind: "email", required: true, auto: "email" },
    { id: "project", kind: "choice", required: true },
    { id: "site", kind: "text", required: false, auto: "off" },
    { id: "scope", kind: "text", required: false, auto: "off" },
    { id: "stone", kind: "text", required: false, auto: "off", marble: true },
    { id: "drawings", kind: "yesno", required: false },
    { id: "timeline", kind: "text", required: false, auto: "off" },
    { id: "budget", kind: "text", required: false, auto: "off" },
    { id: "found", kind: "text", required: false, auto: "off" }
  ];

  var lang = "en";
  try {
    if (sessionStorage.getItem("d3ddd-chat-lang") === "ur") lang = "ur";
  } catch (err) {}

  var open = false;
  var greeted = false;
  var mode = "chat";
  var stepId = "name";
  var lead = {};
  var sending = false;
  var offerQuote = false;

  function copy() { return COPY[lang] || COPY.en; }

  function studioAddress() {
    var nodes = document.querySelectorAll("[data-u][data-d]");
    var i, u, d;
    for (i = 0; i < nodes.length; i++) {
      u = nodes[i].getAttribute("data-u") || "";
      d = nodes[i].getAttribute("data-d") || "";
      if (u && d && u.indexOf("@") < 0 && d.indexOf("@") < 0 && d.indexOf(".") > 0) return u + "@" + d;
    }
    return "info@d3ddd.com";
  }

  function withAddr(text) {
    return String(text || "").replace(/ADDRESS/g, studioAddress());
  }

  function isEmail(v) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
  }

  function visibleSteps() {
    var out = [];
    var i;
    for (i = 0; i < STEPS.length; i++) {
      if (STEPS[i].marble && lead.project !== "marble") continue;
      out.push(STEPS[i]);
    }
    return out;
  }

  function currentStep() {
    var list = visibleSteps();
    var i;
    for (i = 0; i < list.length; i++) if (list[i].id === stepId) return list[i];
    return list[0];
  }

  function promptFor(step) {
    return copy()[step.id + "Q"] || "";
  }

  if (typeof window !== "undefined") {
    window.__D3DDD_MATCH = function (text) { return matchIntent(text); };
    window.__D3DDD_SCORE = function (text) {
      var tokens = fold(text).split(" ");
      var out = [], i, s;
      for (i = 0; i < INTENTS.length; i++) {
        s = scoreIntent(tokens, INTENTS[i]);
        if (s) out.push([INTENTS[i].id, Math.round(s * 100) / 100]);
      }
      return out;
    };
    window.__D3DDD_ANSWER = function (id, language) {
      var table = ANSWERS[language] || ANSWERS.en;
      return table[id] || "";
    };
  }
  if (typeof document === "undefined") return;

  var root = document.createElement("div");
  root.className = "d3-chat";
  root.innerHTML =
    '<button type="button" class="d3-chat-launcher" aria-expanded="false" aria-controls="d3-chat-panel">' +
      '<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true" focusable="false"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="M5 6.5h14a1.5 1.5 0 0 1 1.5 1.5v7.2a1.5 1.5 0 0 1-1.5 1.5H9.2L5 20.2z"/></svg>' +
    "</button>" +
    '<section id="d3-chat-panel" class="d3-chat-panel" role="dialog" aria-modal="false" aria-labelledby="d3-chat-title" hidden>' +
      '<header class="d3-chat-head">' +
        '<div class="d3-chat-id"><strong id="d3-chat-title"></strong><small class="d3-chat-sub"></small></div>' +
        '<button type="button" class="d3-chat-lang"></button>' +
        '<button type="button" class="d3-chat-x"></button>' +
      "</header>" +
      '<div class="d3-chat-log" role="log" aria-live="polite"></div>' +
      '<div class="d3-chat-replies"></div>' +
      '<form class="d3-chat-form" action="#" method="post" novalidate>' +
        '<label class="d3-chat-sr" for="d3-chat-input"></label>' +
        '<input id="d3-chat-input" class="d3-chat-input" type="text" maxlength="1000" autocomplete="off">' +
        '<button class="d3-chat-send" type="submit"></button>' +
      "</form>" +
    "</section>";

  var launcher = root.querySelector(".d3-chat-launcher");
  var panel = root.querySelector(".d3-chat-panel");
  var titleEl = root.querySelector("#d3-chat-title");
  var subEl = root.querySelector(".d3-chat-sub");
  var langBtn = root.querySelector(".d3-chat-lang");
  var closeBtn = root.querySelector(".d3-chat-x");
  var logEl = root.querySelector(".d3-chat-log");
  var replies = root.querySelector(".d3-chat-replies");
  var form = root.querySelector(".d3-chat-form");
  var labelEl = root.querySelector("label");
  var input = root.querySelector(".d3-chat-input");
  var sendBtn = root.querySelector(".d3-chat-send");

  function push(role, text) {
    var el = document.createElement("div");
    el.className = "d3-chat-msg d3-chat-msg-" + role;
    el.textContent = text;
    logEl.appendChild(el);
    logEl.scrollTop = logEl.scrollHeight;
    return el;
  }

  function pushUser(text) { push("user", text); }
  function pushBot(text) { push("bot", text); }

  function pushAnswer(id) {
    var table = ANSWERS[lang] || ANSWERS.en;
    var text = table[id] || ANSWERS.en[id] || "";
    offerQuote = true;
    try { window.__D3DDD_LAST_INTENT = id; } catch (err) {}
    var el = push("bot", withAddr(text));
    if (el && el.setAttribute) el.setAttribute("data-intent", id);
    renderControls();
  }

  function pushFallback() {
    offerQuote = true;
    try { window.__D3DDD_LAST_INTENT = "fallback"; } catch (err) {}
    var el = push("bot", withAddr(copy().fallback));
    if (el && el.setAttribute) el.setAttribute("data-intent", "fallback");
    renderControls();
  }

  function pushSummary(text) {
    var wrap = document.createElement("div");
    wrap.className = "d3-chat-msg d3-chat-msg-bot";
    var pre = document.createElement("pre");
    pre.className = "d3-chat-summary";
    pre.textContent = text;
    wrap.appendChild(pre);
    logEl.appendChild(wrap);
    logEl.scrollTop = logEl.scrollHeight;
  }

  function addReply(text, fn, cls) {
    var b = document.createElement("button");
    b.type = "button";
    b.textContent = text;
    if (cls) b.className = cls;
    b.addEventListener("click", fn);
    replies.appendChild(b);
  }

  function renderControls() {
    var c = copy();
    var keep = input.value;
    replies.textContent = "";
    form.hidden = true;
    if (mode === "chat") {
      form.hidden = false;
      input.type = "text";
      input.autocomplete = "off";
      input.placeholder = c.placeholder;
      if (offerQuote) addReply(c.getQuote, function () { startLead(true, c.getQuote); }, "d3-chat-primary");
      var quickIds = offerQuote
        ? ["marble", "drafting", "estimation", "viz", "website", "payment"]
        : ["marble", "drafting", "estimation", "viz", "website", "payment", "lead"];
      quickIds.forEach(function (id) {
        addReply(c.quick[id], function () { onQuick(id); });
      });
    } else if (mode === "lead") {
      var step = currentStep();
      if (step.kind === "choice") {
        ["marble", "drafting", "estimation", "viz", "website", "other"].forEach(function (id) {
          addReply(c.projects[id], function () { chooseProject(id); });
        });
      } else if (step.kind === "yesno") {
        addReply(c.yes, function () { answerDrawings("yes"); });
        addReply(c.no, function () { answerDrawings("no"); });
      } else {
        form.hidden = false;
        input.type = step.kind === "email" ? "email" : "text";
        input.setAttribute("inputmode", step.id === "phone" ? "tel" : (step.kind === "email" ? "email" : "text"));
        input.autocomplete = step.auto || "off";
        input.placeholder = c[step.id + "Ph"] || c.placeholder;
        input.value = keep || lead[step.id] || "";
      }
      if (!step.required) addReply(c.skip, skipStep, "d3-chat-skip");
      if (step.id !== "name") addReply(c.back, goBack, "d3-chat-skip");
    } else if (mode === "confirm") {
      addReply(c.sendEnquiry, sendLead, "d3-chat-primary");
      addReply(c.restart, restart, "d3-chat-skip");
    } else if (mode === "done") {
      addReply(c.closeChat, function () { setOpen(false); });
    }
    sendBtn.textContent = c.send;
    labelEl.textContent = c.messageLabel;
  }

  function applyLang() {
    var c = copy();
    panel.lang = lang === "ur" ? "ur" : "en";
    panel.dir = lang === "ur" ? "rtl" : "ltr";
    titleEl.textContent = c.title;
    subEl.textContent = c.subtitle;
    langBtn.textContent = lang === "ur" ? "English" : "اردو / Urdu";
    langBtn.setAttribute("aria-pressed", lang === "ur" ? "true" : "false");
    langBtn.setAttribute("aria-label", lang === "ur" ? c.toEnglish : c.toUrdu);
    closeBtn.textContent = "\u00d7";
    closeBtn.setAttribute("aria-label", c.close);
    launcher.setAttribute("aria-label", open ? c.close : c.open);
    try { sessionStorage.setItem("d3ddd-chat-lang", lang); } catch (err) {}
    renderControls();
  }

  function setOpen(next) {
    open = !!next;
    launcher.setAttribute("aria-expanded", open ? "true" : "false");
    launcher.setAttribute("aria-label", open ? copy().close : copy().open);
    panel.hidden = !open;
    if (open) {
      if (!greeted) {
        greeted = true;
        pushBot(copy().hello);
        renderControls();
      }
      liftFloaters();
      var focusEl = !form.hidden ? input : replies.querySelector("button");
      if (focusEl) focusEl.focus();
    } else if (launcher) {
      launcher.focus();
    }
  }

  function onQuick(id) {
    if (mode !== "chat") return;
    if (id === "lead") {
      startLead(true);
      return;
    }
    var quickIntent = { marble: "shop-overview", drafting: "draft-overview", estimation: "estimation", viz: "viz", website: "website", payment: "pricing" };
    pushUser(copy().quick[id]);
    pushAnswer(quickIntent[id] || "shop-overview");
  }

  function startLead(fromButton, userLabel) {
    if (mode === "lead" || mode === "confirm" || mode === "done") return;
    if (fromButton) pushUser(userLabel || copy().quick.lead);
    mode = "lead";
    lead = {};
    stepId = "name";
    sending = false;
    input.value = "";
    pushBot(copy().nameQ);
    renderControls();
  }

  function goNext() {
    var list = visibleSteps();
    var idx = 0;
    var i;
    for (i = 0; i < list.length; i++) if (list[i].id === stepId) idx = i;
    input.value = "";
    if (idx + 1 < list.length) {
      stepId = list[idx + 1].id;
      pushBot(promptFor(list[idx + 1]));
      renderControls();
    } else {
      showSummary();
    }
  }

  function goBack() {
    var list = visibleSteps();
    var idx = 0;
    var i;
    for (i = 0; i < list.length; i++) if (list[i].id === stepId) idx = i;
    if (idx <= 0) return;
    stepId = list[idx - 1].id;
    input.value = "";
    pushBot(promptFor(list[idx - 1]));
    renderControls();
  }

  function skipStep() {
    var step = currentStep();
    if (!step || step.required) return;
    pushUser(copy().skipped);
    lead[step.id] = "";
    goNext();
  }

  function chooseProject(id) {
    lead.project = id;
    pushUser(copy().projects[id]);
    goNext();
  }

  function answerDrawings(val) {
    lead.drawings = val;
    pushUser(val === "yes" ? copy().yes : copy().no);
    pushBot(withAddr(val === "yes" ? copy().drawingsYes : copy().drawingsNo));
    goNext();
  }

  function onText(raw) {
    var value = String(raw || "").trim();
    if (!value) return false;
    if (mode === "lead") {
      var step = currentStep();
      if (!step || step.kind === "choice" || step.kind === "yesno") {
        pushBot(copy().useButtons);
        return false;
      }
      if (step.required && !value) {
        pushBot(copy().needThis);
        return false;
      }
      if (step.kind === "email" && !isEmail(value)) {
        pushUser(value);
        pushBot(copy().emailBad);
        return false;
      }
      pushUser(value);
      lead[step.id] = value;
      goNext();
      return true;
    }
    if (mode !== "chat") return false;
    pushUser(value);
    var q = fold(value);
    var topic = matchIntent(q);
    input.value = "";
    if (topic) {
      pushAnswer(topic);
      return true;
    }
    if (wantsLead(q)) {
      startLead(false);
      return true;
    }
    pushFallback();
    return true;
  }

  function blank(v) {
    var s = String(v || "").trim();
    return s || "Not provided";
  }

  function summaryBody() {
    var project = COPY.en.projects[lead.project] || "";
    var lines = [
      "New chat lead",
      "",
      "Name: " + blank(lead.name),
      "Company: " + blank(lead.company),
      "Phone / WhatsApp: " + blank(lead.phone),
      "Email: " + blank(lead.email),
      "Project type: " + blank(project),
      "Emirate and site: " + blank(lead.site),
      "Scope: " + blank(lead.scope)
    ];
    if (lead.project === "marble") lines.push("Stone type / thickness / finish: " + blank(lead.stone));
    lines.push("Drawings available: " + (lead.drawings === "yes" ? "Yes" : lead.drawings === "no" ? "No" : "Not provided"));
    lines.push("Timeline: " + blank(lead.timeline));
    lines.push("Budget: " + blank(lead.budget));
    lines.push("How they found us: " + blank(lead.found));
    if (lead.drawings === "yes") lines.push("Files: attach PDF or DWG to this email.");
    lines.push("Page: " + location.href);
    return lines.join("\n");
  }

  function summarySubject() {
    var parts = [];
    var name = String(lead.name || "").trim();
    var company = String(lead.company || "").trim();
    var project = COPY.en.projects[lead.project] || "";
    if (name) parts.push(name);
    if (company) parts.push(company);
    if (project) parts.push(project);
    return "New chat lead: " + parts.join(", ");
  }

  function showSummary() {
    mode = "confirm";
    input.value = "";
    pushBot(copy().summaryIntro);
    pushSummary(summaryBody());
    renderControls();
  }

  function deliver(url) {
    if (typeof window.__D3DDD_MAILTO_SINK === "function") {
      window.__D3DDD_MAILTO_SINK(url);
      return;
    }
    location.href = url;
  }

  function sendLead() {
    if (sending || mode !== "confirm") return;
    sending = true;
    var addr = studioAddress();
    var subject = summarySubject();
    var body = summaryBody();
    var url = "mailto:" + addr + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    try {
      if (typeof window.gtag === "function") {
        window.gtag("event", "chat_lead_submit", { project_type: COPY.en.projects[lead.project] || "" });
      }
    } catch (err) {}
    deliver(url);
    mode = "done";
    pushBot(withAddr(copy().thanks));
    renderControls();
  }

  function restart() {
    mode = "chat";
    lead = {};
    stepId = "name";
    sending = false;
    offerQuote = false;
    input.value = "";
    pushBot(copy().again);
    renderControls();
  }

  function tabbables() {
    var nodes = panel.querySelectorAll("button, input, a");
    var list = [];
    var i, el, style;
    for (i = 0; i < nodes.length; i++) {
      el = nodes[i];
      if (el.disabled || el.closest("[hidden]")) continue;
      style = window.getComputedStyle(el);
      if (style.display === "none" || style.visibility === "hidden") continue;
      list.push(el);
    }
    return list;
  }

  function liftFloaters() {
    var lift = 0;
    var nodes = document.body.querySelectorAll("a, button");
    var i, el, st, r;
    for (i = 0; i < nodes.length; i++) {
      el = nodes[i];
      if (!el || el.closest(".d3-chat")) continue;
      st = window.getComputedStyle(el);
      if (st.position !== "fixed") continue;
      r = el.getBoundingClientRect();
      if (r.width < 20 || r.height < 20) continue;
      if ((window.innerWidth - r.right) < 140 && (window.innerHeight - r.bottom) < 160) {
        lift = Math.max(lift, Math.round(r.height + 14));
      }
    }
    root.style.setProperty("--d3-chat-lift", lift + "px");
  }

  launcher.addEventListener("click", function () { setOpen(!open); });
  closeBtn.addEventListener("click", function () { setOpen(false); });
  langBtn.addEventListener("click", function () {
    lang = lang === "ur" ? "en" : "ur";
    applyLang();
    if (mode === "lead") pushBot(promptFor(currentStep()));
    else if (mode === "confirm") pushBot(copy().summaryIntro);
  });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    onText(input.value);
  });
  panel.addEventListener("keydown", function (e) {
    if (e.key !== "Tab" || panel.hidden) return;
    var list = tabbables();
    if (!list.length) return;
    var first = list[0];
    var last = list[list.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape" || !open) return;
    var search = document.getElementById("site-search-dialog");
    if (search && !search.hidden) return;
    setOpen(false);
  });
  window.addEventListener("resize", liftFloaters);

  var mounted = false;
  function mount() {
    if (mounted || !document.body) return;
    mounted = true;
    var links = document.querySelectorAll('link[href*="sales-chat.css"]');
    var i;
    for (i = 0; i < links.length; i++) links[i].media = "all";
    applyLang();
    liftFloaters();
    document.body.appendChild(root);
  }
  var cssLink = document.querySelector('link[href*="sales-chat.css"]');
  if (cssLink && !cssLink.sheet) {
    cssLink.addEventListener("load", mount);
    setTimeout(mount, 1500);
  } else {
    mount();
  }
})();

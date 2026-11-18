/* D3DDD sales chat. Scripted answers only — not a language model.
   Leads use the same mailto path as the enquiry form in assets/site.js:
   the address is assembled from data-u and data-d, then location.href opens mailto:.
   A test may set window.__D3DDD_MAILTO_SINK to capture that URL instead. */
(function () {
  if (window.__D3DDD_SALES_CHAT) return;
  window.__D3DDD_SALES_CHAT = true;

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
      unknown: "I do not have that detail here. The team will confirm it by email. Send your details and we will include your question with the enquiry.",
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
      answers: {
        marble: "Marble and stone shop drawings are AutoCAD fabrication and installation drawings. A set can include layout plans and elevations with piece numbering and joints, sections and fixing details, edge profiles, and material and finish notes. Thickness is typically 18, 20 or 30 mm. Finishes are polished, honed, leathered or flamed. Vein matching and bookmatching can be shown. You also receive a piece schedule and a cutting list that can be exported to Excel, slab nesting when you provide slab photos, and a revision table. The work covers vanities, countertops, kitchen islands, stairs, cladding, flooring and waterjet inlays. Packs start from around AED 1,200. The exact price and delivery are confirmed in writing after we review your drawings. All jobs are 50% upfront. We are based in Dubai and deliver digitally across all UAE emirates.",
        drafting: "Architectural and fit-out drafting is AutoCAD 2D construction drawings: plans, elevations, sections, reflected ceiling plans and details. The price is confirmed after we review your drawings. The exact price and delivery are confirmed in writing. All jobs are 50% upfront. We are based in Dubai and deliver digitally across all UAE emirates.",
        estimation: "Estimation covers BOQ, quantity take-off and material schedules. The price is confirmed after review. The exact price and delivery are confirmed in writing after we review the drawings. All jobs are 50% upfront. We are based in Dubai and deliver digitally across all UAE emirates.",
        viz: "3D visualization is still renders, from AED 650 per render. Renders are for approval, not fabrication. The exact price and delivery are confirmed in writing after we review the drawings. All jobs are 50% upfront. We are based in Dubai and deliver digitally across all UAE emirates.",
        website: "Websites: Starter AED 1,200 for 1 page, Business AED 2,000 for up to 5 pages, and Premium from AED 3,500. Domain and hosting are extra unless agreed. All jobs are 50% upfront. The exact price and delivery are confirmed in writing after we review what you need. We are based in Dubai and deliver digitally across all UAE emirates.",
        payment: "Marble and stone shop-drawing packs start from around AED 1,200. Still renders start from AED 650 per render, and renders are for approval, not fabrication. Websites: Starter AED 1,200 (1 page), Business AED 2,000 (up to 5 pages), Premium from AED 3,500. Domain and hosting are extra unless agreed. Architectural and fit-out drafting, and estimation (BOQ, quantity take-off and material schedules), are priced after we review the drawings. All jobs are 50% upfront. The exact price and delivery are confirmed in writing after that review. We are based in Dubai and deliver digitally across all UAE emirates.",
        place: "D3DDD is based in Dubai. Files are delivered digitally across all UAE emirates. The exact price and delivery are confirmed in writing after we review the drawings, and all jobs are 50% upfront."
      }
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
      unknown: "یہ تفصیل میرے پاس نہیں۔ ٹیم ای میل سے کنفرم کرے گی۔ اپنی تفصیل بھیجیں، سوال انکوائری کے ساتھ چلا جائے گا۔",
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
      answers: {
        marble: "ماربل اور پتھر کی شاپ ڈرائنگ آٹوکیڈ میں بننے والی فیبریکیشن اور انسٹالیشن ڈرائنگ ہوتی ہے۔ اس میں لے آؤٹ پلان اور ایلیویشن شامل ہو سکتے ہیں، ٹکڑوں کی نمبرنگ اور جوڑ کے ساتھ، سیکشن اور فکسنگ کی تفصیل، ایج پروفائل، اور میٹریل و فنش کے نوٹس۔ موٹائی عموماً 18، 20 یا 30 ملی میٹر ہوتی ہے، اور فنش پالش، ہونڈ، لیدرڈ یا فلیمڈ ہو سکتا ہے۔ وین میچنگ اور بک میچنگ دکھائی جا سکتی ہے۔ پیس شیڈول اور کٹنگ لسٹ ایکسل میں برآمد ہو سکتی ہے، سلیب کی تصاویر ملنے پر سلیب نیسٹنگ ہوتی ہے، اور ریویژن ٹیبل شامل ہوتا ہے۔ کام میں وینٹی، کاؤنٹر ٹاپ، کچن آئلینڈ، سیڑھیاں، کلیڈنگ، فرش اور واٹر جیٹ انلے شامل ہیں۔ پیکج تقریباً 1,200 درہم سے شروع ہوتے ہیں۔ درست قیمت اور ڈیلیوری ڈرائنگ دیکھنے کے بعد تحریر میں طے ہوتی ہے۔ ہر کام پر 50 فیصد پیشگی ہے۔ ہم دبئی میں ہیں اور تمام متحدہ عرب امارات میں ڈیجیٹل ڈیلیوری کرتے ہیں۔",
        drafting: "آرکیٹیکچرل اور فٹ آؤٹ ڈرافٹنگ آٹوکیڈ 2D کنسٹرکشن ڈرائنگ ہے: پلان، ایلیویشن، سیکشن، ریفلیکٹڈ سیلنگ پلان اور ڈیٹیل۔ قیمت ڈرائنگ دیکھنے کے بعد طے ہوتی ہے۔ درست قیمت اور ڈیلیوری تحریر میں کنفرم ہوتی ہے۔ ہر کام پر 50 فیصد پیشگی ہے۔ ہم دبئی میں ہیں اور تمام امارات میں ڈیجیٹل ڈیلیوری کرتے ہیں۔",
        estimation: "تخمینے میں بی او کیو، کوانٹٹی ٹیک آف اور میٹریل شیڈول شامل ہیں۔ قیمت جائزے کے بعد طے ہوتی ہے۔ درست قیمت اور ڈیلیوری ڈرائنگ دیکھنے کے بعد تحریر میں کنفرم ہوتی ہے۔ ہر کام پر 50 فیصد پیشگی ہے۔ ہم دبئی میں ہیں اور تمام امارات میں ڈیجیٹل ڈیلیوری کرتے ہیں۔",
        viz: "تھری ڈی ویژولائزیشن اسٹل رینڈر ہے، ہر رینڈر 650 درہم سے۔ رینڈر منظوری کے لیے ہوتے ہیں، فیبریکیشن کے لیے نہیں۔ درست قیمت اور ڈیلیوری ڈرائنگ دیکھنے کے بعد تحریر میں کنفرم ہوتی ہے۔ ہر کام پر 50 فیصد پیشگی ہے۔ ہم دبئی میں ہیں اور تمام امارات میں ڈیجیٹل ڈیلیوری کرتے ہیں۔",
        website: "ویب سائٹ: سٹارٹر 1,200 درہم (1 صفحہ)، بزنس 2,000 درہم (5 صفحات تک)، پریمیم 3,500 درہم سے۔ ڈومین اور ہوسٹنگ الگ ہیں جب تک کہ طے نہ ہو۔ ہر کام پر 50 فیصد پیشگی ہے۔ درست قیمت اور ڈیلیوری ضرورت دیکھنے کے بعد تحریر میں کنفرم ہوتی ہے۔ ہم دبئی میں ہیں اور تمام امارات میں ڈیجیٹل ڈیلیوری کرتے ہیں۔",
        payment: "ماربل اور پتھر کی شاپ ڈرائنگ کے پیکج تقریباً 1,200 درہم سے شروع ہوتے ہیں۔ اسٹل رینڈر 650 درہم فی رینڈر سے ہیں، اور رینڈر منظوری کے لیے ہیں، فیبریکیشن کے لیے نہیں۔ ویب سائٹ: سٹارٹر 1,200 درہم (1 صفحہ)، بزنس 2,000 درہم (5 صفحات تک)، پریمیم 3,500 درہم سے۔ ڈومین اور ہوسٹنگ الگ ہیں جب تک کہ طے نہ ہو۔ آرکیٹیکچرل اور فٹ آؤٹ ڈرافٹنگ، اور تخمینہ (بی او کیو، کوانٹٹی ٹیک آف، میٹریل شیڈول)، ڈرائنگ کے جائزے کے بعد قیمت پاتے ہیں۔ ہر کام پر 50 فیصد پیشگی ہے۔ درست قیمت اور ڈیلیوری اس جائزے کے بعد تحریر میں کنفرم ہوتی ہے۔ ہم دبئی میں ہیں اور تمام امارات میں ڈیجیٹل ڈیلیوری کرتے ہیں۔",
        place: "D3DDD دبئی میں ہے۔ فائلیں تمام متحدہ عرب امارات میں ڈیجیٹل پہنچائی جاتی ہیں۔ درست قیمت اور ڈیلیوری ڈرائنگ دیکھنے کے بعد تحریر میں طے ہوتی ہے، اور ہر کام پر 50 فیصد پیشگی ہے۔"
      }
    }
  };

  var TOPICS = {
    marble: ["marble", "stone", "shop drawing", "fabrication drawing", "vanity", "vanities", "countertop", "counter top", "kitchen island", "cladding", "waterjet", "inlay", "bookmatch", "vein match", "cutting list", "piece schedule", "slab nest", "edge profile", "honed", "leathered", "flamed", "ماربل", "سنگ مرمر", "شاپ ڈرائنگ", "وینٹی", "کاؤنٹر", "سلیب"],
    drafting: ["drafting", "autocad", "auto cad", "construction drawing", "fit-out", "fitout", "fit out", "joinery", "reflected ceiling", "rcp", "آرکیٹیکچرل", "فٹ آؤٹ", "آٹوکیڈ", "ڈرافٹنگ"],
    estimation: ["estimation", "estimate", "boq", "quantity take", "take-off", "takeoff", "take off", "material schedule", "bill of quantit", "تخمین", "بی او کیو"],
    viz: ["3d", "render", "visualisation", "visualization", "تھری ڈی", "رینڈر", "ویژول"],
    website: ["website", "web site", "web design", "landing page", "starter", "premium", "ویب سائٹ", "ویب سائٹس"],
    payment: ["price", "pricing", "cost", "how much", "payment", "upfront", "deposit", "fee", "aed", "درہم", "قیمت", "ادائیگی", "پیشگی"],
    place: ["where are you", "based in", "which emirate", "do you cover", "do you work", "ابو ظبی", "دبئی میں", "امارات"]
  };

  var LEAD_KEYS = ["quote", "quotation", "send my details", "get in touch", "کوٹ", "تفصیل بھیج"];

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

  function escRe(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function hasTerm(q, term) {
    var t = String(term).toLowerCase();
    if (!t) return false;
    if (/^[a-z0-9%]+$/.test(t) && t.length <= 3) {
      return new RegExp("(^|[^a-z0-9])" + escRe(t) + "([^a-z0-9]|$)").test(q);
    }
    return q.indexOf(t) !== -1;
  }

  function norm(s) {
    return String(s || "").toLowerCase().replace(/\s+/g, " ").trim();
  }

  function scoreTopic(q, keys) {
    var score = 0;
    var i;
    for (i = 0; i < keys.length; i++) {
      if (hasTerm(q, keys[i])) score += keys[i].length;
    }
    return score;
  }

  function foreignWord(q) {
    var allow = {
      charge: 1, charges: 1, charged: 1, rate: 1, rates: 1, dirham: 1, dirhams: 1,
      package: 1, packages: 1, please: 1, thanks: 1, thank: 1, hello: 1, project: 1,
      projects: 1, drawing: 1, drawings: 1, service: 1, services: 1, detail: 1,
      details: 1, quote: 1, quotation: 1, about: 1, would: 1, could: 1, should: 1,
      there: 1, their: 1, email: 1, need: 1, want: 1, send: 1, hello: 1, price: 1,
      prices: 1, pricing: 1, payment: 1, upfront: 1, deposit: 1
    };
    var keys = [];
    var id, i, k, words, w, known, j;
    for (id in TOPICS) {
      if (!Object.prototype.hasOwnProperty.call(TOPICS, id)) continue;
      for (i = 0; i < TOPICS[id].length; i++) {
        k = TOPICS[id][i].toLowerCase();
        if (/[a-z]/.test(k)) keys.push(k);
      }
    }
    words = q.split(/[^a-z0-9]+/);
    for (i = 0; i < words.length; i++) {
      w = words[i];
      if (w.length < 6 || allow[w]) continue;
      known = false;
      for (j = 0; j < keys.length; j++) {
        if (keys[j].indexOf(w) !== -1) { known = true; break; }
        if (keys[j].length >= 4 && w.indexOf(keys[j]) !== -1) { known = true; break; }
      }
      if (!known) return w;
    }
    return "";
  }

  function matchTopic(q) {
    var ids = ["marble", "drafting", "estimation", "viz", "website"];
    var scores = {};
    var best = null;
    var bestScore = 0;
    var i;
    for (i = 0; i < ids.length; i++) {
      scores[ids[i]] = scoreTopic(q, TOPICS[ids[i]]);
      if (scores[ids[i]] > bestScore) {
        bestScore = scores[ids[i]];
        best = ids[i];
      }
    }
    if (scores.drafting && scores.marble && !hasTerm(q, "marble") && !hasTerm(q, "stone") && (hasTerm(q, "joinery") || hasTerm(q, "fit-out") || hasTerm(q, "fitout") || hasTerm(q, "fit out"))) {
      best = "drafting";
    }
    if (best) return best;
    if (foreignWord(q)) return null;
    if (scoreTopic(q, TOPICS.payment)) return "payment";
    if (scoreTopic(q, TOPICS.place)) return "place";
    return null;
  }

  function wantsLead(q) {
    var i;
    for (i = 0; i < LEAD_KEYS.length; i++) {
      if (q.indexOf(LEAD_KEYS[i]) !== -1) return true;
    }
    return false;
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
      ["marble", "drafting", "estimation", "viz", "website", "payment", "lead"].forEach(function (id) {
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
    pushUser(copy().quick[id]);
    pushBot(copy().answers[id]);
    renderControls();
  }

  function startLead(fromButton) {
    if (mode === "lead" || mode === "confirm" || mode === "done") return;
    if (fromButton) pushUser(copy().quick.lead);
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
    var q = norm(value);
    var topic = matchTopic(q);
    input.value = "";
    if (topic) {
      pushBot(copy().answers[topic]);
      renderControls();
      return true;
    }
    if (wantsLead(q)) {
      startLead(false);
      return true;
    }
    pushBot(copy().unknown);
    renderControls();
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

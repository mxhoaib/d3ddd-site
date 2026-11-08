(function () {
  document.documentElement.classList.add("js");
  var t = document.querySelector(".menu-toggle"), n = document.querySelector(".nav");
  if (t) t.onclick = function () {
    n.classList.toggle("open");
    t.setAttribute("aria-expanded", n.classList.contains("open"));
  };
  document.querySelectorAll("[data-year]").forEach(function (e) { e.textContent = new Date().getFullYear(); });

  function mailAddr(el) {
    if (!el) return "";
    var u = el.getAttribute("data-u"), d = el.getAttribute("data-d");
    if (!u || !d) return "";
    return u + "@" + d;
  }
  document.querySelectorAll("a.mail-link[data-u][data-d]").forEach(function (a) {
    var addr = mailAddr(a);
    if (!addr) return;
    a.href = "mailto:" + addr;
    var slot = a.querySelector(".mail-slot");
    if (slot) slot.textContent = addr;
  });

  var f = document.querySelector("form.enquiry");
  if (f) {
    var map = {
      marble: "Marble / stone shop drawings",
      stone: "Marble / stone shop drawings",
      "shop-drawings": "Marble / stone shop drawings",
      drafting: "Architectural drafting",
      autocad: "Architectural drafting",
      "shop-drawing-approval": "3D rendering / modeling / visualization",
      approval: "3D rendering / modeling / visualization",
      "3d": "3D rendering / modeling / visualization",
      rendering: "3D rendering / modeling / visualization",
      design: "Architectural designing",
      estimation: "Architectural estimation",
      website: "Website development & designing",
      web: "Website development & designing",
      "رسومات الرخام والحجر التنفيذية": "رسومات الرخام والحجر التنفيذية",
      "الرسم المعماري التنفيذي": "الرسم المعماري التنفيذي",
      "التصميم المعماري": "التصميم المعماري",
      "حساب الكميات والتقدير": "حساب الكميات والتقدير",
      "تصميم ثلاثي الأبعاد / نمذجة": "تصميم ثلاثي الأبعاد / نمذجة",
      "تطوير وتصميم المواقع": "تطوير وتصميم المواقع"
    };
    var arMap = {
      marble: "رسومات الرخام والحجر التنفيذية",
      stone: "رسومات الرخام والحجر التنفيذية",
      "shop-drawings": "رسومات الرخام والحجر التنفيذية",
      drafting: "الرسم المعماري التنفيذي",
      autocad: "الرسم المعماري التنفيذي",
      "3d": "تصميم ثلاثي الأبعاد / نمذجة",
      rendering: "تصميم ثلاثي الأبعاد / نمذجة",
      approval: "تصميم ثلاثي الأبعاد / نمذجة",
      "shop-drawing-approval": "تصميم ثلاثي الأبعاد / نمذجة",
      design: "التصميم المعماري",
      estimation: "حساب الكميات والتقدير",
      website: "تطوير وتصميم المواقع",
      web: "تطوير وتصميم المواقع"
    };
    try {
      var q = new URLSearchParams(location.search).get("service");
      if (q) {
        var key = q.toLowerCase().trim(), sel = f.querySelector("[name=service]");
        var arabic = document.documentElement.lang.indexOf("ar") === 0;
        var label = (arabic ? arMap : map)[key];
        if (sel) {
          if (label) {
            for (var i = 0; i < sel.options.length; i++) {
              if (sel.options[i].text.replace(/&amp;/g, "&") === label || sel.options[i].value === label) {
                sel.selectedIndex = i;
                break;
              }
            }
          } else {
            for (var j = 0; j < sel.options.length; j++) {
              if (sel.options[j].text.toLowerCase().indexOf(key) !== -1) {
                sel.selectedIndex = j;
                break;
              }
            }
          }
        }
      }
    } catch (err) {}
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var addr = mailAddr(f);
      if (!addr) return;
      var d = new FormData(f);
      if (d.get("company_website")) return;
      var L = document.documentElement.lang.indexOf("ar") === 0;
      var lab = L ? ["الاسم", "الهاتف", "البريد", "الخدمة", "التفاصيل"] : ["Name", "Phone", "Email", "Service", "Details"];
      var body = [
        lab[0] + ": " + (d.get("name") || ""),
        lab[1] + ": " + (d.get("phone") || ""),
        lab[2] + ": " + (d.get("email") || ""),
        lab[3] + ": " + (d.get("service") || ""),
        "",
        lab[4] + ":",
        (d.get("message") || "")
      ].join("\n");
      location.href = "mailto:" + addr + "?subject=" + encodeURIComponent((L ? "استفسار من الموقع – " : "Website enquiry – ") + (d.get("service") || "")) + "&body=" + encodeURIComponent(body);
    });
  }
  document.querySelectorAll("[data-cur]").forEach(function (sec) {
    function set(c) {
      sec.setAttribute("data-cur", c);
      sec.querySelectorAll("[data-set-cur]").forEach(function (b) {
        b.setAttribute("aria-pressed", b.dataset.setCur === c);
      });
    }
    set(sec.getAttribute("data-cur"));
    sec.querySelectorAll("[data-set-cur]").forEach(function (b) {
      b.onclick = function () { set(b.dataset.setCur); };
    });
  });
})();

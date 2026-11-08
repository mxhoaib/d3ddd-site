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
      marble: "Marble & Stone Shop Drawings",
      stone: "Marble & Stone Shop Drawings",
      "shop-drawings": "Marble & Stone Shop Drawings",
      drafting: "Architectural Drafting",
      autocad: "Architectural Drafting",
      fitout: "Fit-Out & Joinery Drawings",
      "fit-out": "Fit-Out & Joinery Drawings",
      joinery: "Fit-Out & Joinery Drawings",
      "shop-drawing-approval": "3D Visualization",
      approval: "3D Visualization",
      "3d": "3D Visualization",
      rendering: "3D Visualization",
      visualization: "3D Visualization",
      design: "Other",
      estimation: "Estimation & BOQ",
      boq: "Estimation & BOQ",
      website: "Other",
      web: "Other",
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
      var fields = [
        ["name", "Name", "الاسم"],
        ["company", "Company", "الشركة"],
        ["phone", "Phone", "الهاتف"],
        ["whatsapp", "WhatsApp", "واتساب"],
        ["email", "Email", "البريد"],
        ["service", "Service", "الخدمة"],
        ["location", "Location", "الموقع"]
      ];
      var lines = [];
      fields.forEach(function (row) {
        if (!f.elements[row[0]]) return;
        lines.push((L ? row[2] : row[1]) + ": " + (d.get(row[0]) || ""));
      });
      lines.push("");
      lines.push((L ? "التفاصيل" : "Details") + ":");
      lines.push(d.get("message") || "");
      if (typeof window.gtag === "function") {
        window.gtag("event", "enquiry_submit", {
          service: d.get("service") || "",
          location: d.get("location") || ""
        });
      }
      location.href = "mailto:" + addr + "?subject=" + encodeURIComponent((L ? "استفسار من الموقع – " : "Website enquiry – ") + (d.get("service") || "")) + "&body=" + encodeURIComponent(lines.join("\n"));
    });
  }
  document.addEventListener("click", function (ev) {
    if (typeof window.gtag !== "function" || !ev.target.closest) return;
    var el = ev.target.closest("a.mail-link, a.wa-contact, .wa-contact");
    if (!el) return;
    if (el.classList.contains("wa-contact")) window.gtag("event", "whatsapp_click");
    else window.gtag("event", "mailto_click");
  });
  document.querySelectorAll(".nav-drop").forEach(function (btn) {
    btn.addEventListener("click", function (ev) {
      ev.preventDefault();
      ev.stopPropagation();
      var group = btn.parentElement;
      var open = !group.classList.contains("open");
      document.querySelectorAll(".nav-group.open").forEach(function (other) {
        if (other === group) return;
        other.classList.remove("open");
        var otherBtn = other.querySelector(".nav-drop");
        if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
      });
      group.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
  document.addEventListener("click", function () {
    document.querySelectorAll(".nav-group.open").forEach(function (group) {
      group.classList.remove("open");
      var btn = group.querySelector(".nav-drop");
      if (btn) btn.setAttribute("aria-expanded", "false");
    });
  });
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

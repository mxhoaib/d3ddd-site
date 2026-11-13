(function () {
  var trigger = document.querySelector(".search-trigger");
  var dialog = document.getElementById("site-search-dialog");
  if (!trigger || !dialog) return;

  var form = dialog.querySelector("form");
  var input = document.getElementById("site-search-input");
  var list = document.getElementById("site-search-list");
  var status = dialog.querySelector(".search-status");
  var hint = dialog.querySelector(".search-hint");
  var closeBtn = dialog.querySelector(".search-close");
  var rtl = document.documentElement.getAttribute("dir") === "rtl";
  var lang = rtl ? "ar" : "en";
  var copy = lang === "ar" ? {
    groups: { service: "الخدمات", page: "الصفحات", blog: "المدونة", app: "تطبيقات الويب" },
    order: ["service", "page", "blog", "app"],
    suggest: "اقتراحات",
    empty: "لا توجد نتائج. جرّب خدمة أو صفحة أو موضوعاً من المدونة.",
    loading: "جارٍ تحميل البحث…",
    error: "تعذر تحميل البحث. حاول مرة أخرى.",
    suggestions: ["رسومات الرخام", "تصميم ثلاثي الأبعاد", "حساب الكميات", "Still"]
  } : {
    groups: { service: "Services", page: "Pages", blog: "Blog", app: "Web Apps" },
    order: ["service", "page", "blog", "app"],
    suggest: "Suggestions",
    empty: "Nothing matches that yet. Try a service, a page, or a topic from the blog.",
    loading: "Loading search…",
    error: "Search could not be loaded. Please try again.",
    suggestions: ["marble shop drawings", "3D visualization", "estimation", "Still app"]
  };

  var indexPromise = null;
  var options = [];
  var active = -1;
  var lastFocus = null;
  var open = false;

  function norm(value) {
    return (value || "").toLowerCase().replace(/\s+/g, " ").trim();
  }

  function escapeReg(value) {
    return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (ch) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch];
    });
  }

  function hasWord(hay, word) {
    if (!word) return false;
    if (/[a-z0-9]/i.test(word)) {
      return new RegExp("(^|[^a-z0-9])" + escapeReg(word) + "(?![a-z0-9])", "i").test(hay);
    }
    return hay.indexOf(word) !== -1;
  }

  function fieldHit(field, words, phrase) {
    if (!field) return 0;
    var n = 0;
    for (var i = 0; i < words.length; i++) if (hasWord(field, words[i])) n++;
    if (phrase && field.indexOf(phrase) !== -1) n += words.length;
    return n;
  }

  function score(item, phrase, words) {
    var title = norm(item.title);
    var snippet = norm(item.snippet);
    var keys = norm(item.keywords);
    var url = norm(item.url);
    var blob = title + " " + snippet + " " + keys + " " + url;
    for (var i = 0; i < words.length; i++) {
      if (!hasWord(blob, words[i])) return 0;
    }
    var s = 0;
    var titleHits = 0;
    for (var t = 0; t < words.length; t++) if (hasWord(title, words[t])) titleHits++;
    if (titleHits === words.length) s += 100;
    else s += titleHits * 20;
    if (phrase && title.indexOf(phrase) !== -1) s += 30;
    if (title === phrase) s += 40;
    s += fieldHit(keys, words, phrase) * 8;
    s += fieldHit(snippet, words, phrase) * 4;
    s += fieldHit(url, words, phrase) * 3;
    return s;
  }

  function typeRank(type) {
    if (type === "service") return 4;
    if (type === "page") return 3;
    if (type === "app") return 2;
    return 1;
  }

  function titleHits(item, words) {
    var title = norm(item.title);
    var n = 0;
    for (var i = 0; i < words.length; i++) if (hasWord(title, words[i])) n++;
    return n;
  }

  function highlight(text, phrase, words) {
    var alts = [];
    if (phrase && phrase.length > 1) alts.push(phrase);
    words.forEach(function (word) {
      if (word.length > 1 && alts.indexOf(word) === -1) alts.push(word);
    });
    if (!alts.length) return escapeHtml(text);
    var re = new RegExp("(" + alts.map(escapeReg).join("|") + ")", "ig");
    var out = "";
    var last = 0;
    var match;
    while ((match = re.exec(text))) {
      out += escapeHtml(text.slice(last, match.index)) + "<mark>" + escapeHtml(match[1]) + "</mark>";
      last = match.index + match[0].length;
      if (match.index === re.lastIndex) re.lastIndex++;
    }
    return out + escapeHtml(text.slice(last));
  }

  function loadIndex() {
    if (!indexPromise) {
      var url = dialog.getAttribute("data-index") || "/assets/search-index.json";
      indexPromise = fetch(url, { credentials: "same-origin" }).then(function (res) {
        if (!res.ok) throw new Error("index");
        return res.json();
      }).then(function (data) {
        return (data && data.items) || [];
      }).catch(function (err) {
        indexPromise = null;
        throw err;
      });
    }
    return indexPromise;
  }

  function matches(items, phrase) {
    var words = phrase.split(" ").filter(function (word) { return word.length > 1; });
    if (!words.length) return [];
    var ranked = [];
    items.forEach(function (item) {
      if (item.lang !== lang) return;
      var value = score(item, phrase, words);
      if (value > 0) ranked.push({ item: item, score: value, hits: titleHits(item, words), type: typeRank(item.type) });
    });
    ranked.sort(function (a, b) {
      if (b.hits !== a.hits) return b.hits - a.hits;
      if (b.type !== a.type) return b.type - a.type;
      if (b.score !== a.score) return b.score - a.score;
      return a.item.title.localeCompare(b.item.title);
    });
    return ranked.slice(0, 20);
  }

  function suggestions(items) {
    var picked = [];
    var seen = {};
    copy.suggestions.forEach(function (phrase) {
      var found = matches(items, norm(phrase));
      if (!found.length) return;
      var item = found[0].item;
      if (seen[item.url]) return;
      seen[item.url] = true;
      picked.push(item);
    });
    return picked;
  }

  function setActive(index) {
    if (!options.length) {
      active = -1;
      input.removeAttribute("aria-activedescendant");
      return;
    }
    if (index < 0) index = options.length - 1;
    if (index >= options.length) index = 0;
    active = index;
    options.forEach(function (el, n) {
      el.setAttribute("aria-selected", n === active ? "true" : "false");
    });
    var chosen = options[active];
    input.setAttribute("aria-activedescendant", chosen.id);
    var box = list.getBoundingClientRect();
    var row = chosen.getBoundingClientRect();
    if (row.top < box.top) list.scrollTop -= box.top - row.top;
    else if (row.bottom > box.bottom) list.scrollTop += row.bottom - box.bottom;
  }

  function rowHtml(item, id, phrase, words) {
    var snippet = item.snippet || copy.groups[item.type] || "";
    return (
      '<a class="search-hit" role="option" id="' + id + '" href="' + escapeHtml(item.url) + '" aria-selected="false">' +
      '<span class="search-title">' + highlight(item.title, phrase, words) + "</span>" +
      '<span class="search-snip">' + highlight(snippet, phrase, words) + "</span>" +
      '<span class="search-path">' + escapeHtml(item.url) + "</span></a>"
    );
  }

  function paint(items, raw) {
    var phrase = norm(raw);
    var suggesting = !phrase;
    var rows = [];
    var words = [];
    status.textContent = "";
    if (suggesting) {
      suggestions(items).forEach(function (item) { rows.push(item); });
      list.setAttribute("aria-label", copy.suggest);
    } else {
      words = phrase.split(" ").filter(function (word) { return word.length > 1; });
      var grouped = { service: [], page: [], blog: [], app: [] };
      matches(items, phrase).forEach(function (hit) {
        (grouped[hit.item.type] || grouped.page).push(hit.item);
      });
      copy.order.forEach(function (type) {
        grouped[type].forEach(function (item) { rows.push(item); });
      });
      list.setAttribute("aria-label", lang === "ar" ? "نتائج البحث" : "Search results");
    }
    if (hint) hint.hidden = !suggesting;
    if (!rows.length) {
      list.innerHTML = "";
      options = [];
      active = -1;
      input.removeAttribute("aria-activedescendant");
      input.setAttribute("aria-expanded", "false");
      if (!suggesting) status.textContent = copy.empty;
      return;
    }
    var html = "";
    var cursor = 0;
    if (suggesting) {
      html += '<div class="search-label" role="presentation">' + escapeHtml(copy.suggest) + "</div>";
      rows.forEach(function (item) {
        html += rowHtml(item, "ss-opt-" + cursor, "", []);
        cursor++;
      });
    } else {
      var groupedHtml = { service: "", page: "", blog: "", app: "" };
      var counts = { service: 0, page: 0, blog: 0, app: 0 };
      rows.forEach(function (item) {
        var type = groupedHtml.hasOwnProperty(item.type) ? item.type : "page";
        groupedHtml[type] += rowHtml(item, "ss-opt-" + cursor, phrase, words);
        counts[type]++;
        cursor++;
      });
      copy.order.forEach(function (type) {
        if (!counts[type]) return;
        html += '<div class="search-label" role="presentation">' + escapeHtml(copy.groups[type]) + "</div>" + groupedHtml[type];
      });
    }
    list.innerHTML = html;
    options = Array.prototype.slice.call(list.querySelectorAll('[role="option"]'));
    active = -1;
    input.removeAttribute("aria-activedescendant");
    input.setAttribute("aria-expanded", "true");
    options.forEach(function (el, index) {
      el.addEventListener("mousemove", function () { setActive(index); });
    });
  }

  function render() {
    var raw = input.value;
    if (!options.length) status.textContent = copy.loading;
    loadIndex().then(function (items) {
      if (!open || input.value !== raw) return;
      paint(items, raw);
    }).catch(function () {
      if (!open) return;
      list.innerHTML = "";
      options = [];
      status.textContent = copy.error;
    });
  }

  function focusables() {
    return Array.prototype.filter.call(
      dialog.querySelectorAll("input, button, a[href]"),
      function (el) { return !el.hasAttribute("disabled") && el.offsetParent !== null; }
    );
  }

  function show() {
    if (open) {
      input.focus();
      return;
    }
    lastFocus = document.activeElement;
    open = true;
    dialog.hidden = false;
    trigger.setAttribute("aria-expanded", "true");
    document.body.classList.add("search-open");
    var nav = document.getElementById("nav");
    var menu = document.querySelector(".menu-toggle");
    if (nav) nav.classList.remove("open");
    if (menu) menu.setAttribute("aria-expanded", "false");
    render();
    input.focus();
    input.select();
  }

  function hide() {
    if (!open) return;
    open = false;
    dialog.hidden = true;
    trigger.setAttribute("aria-expanded", "false");
    input.setAttribute("aria-expanded", "false");
    document.body.classList.remove("search-open");
    var back = lastFocus && lastFocus.focus ? lastFocus : trigger;
    lastFocus = null;
    back.focus();
  }

  function go() {
    if (active < 0 && options.length) setActive(0);
    if (active >= 0 && options[active]) window.location.href = options[active].getAttribute("href");
  }

  function typingTarget(el) {
    if (!el || !el.tagName) return false;
    var tag = el.tagName;
    return tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || el.isContentEditable;
  }

  trigger.addEventListener("click", function () {
    if (open) hide();
    else show();
  });
  closeBtn.addEventListener("click", hide);
  dialog.addEventListener("click", function (event) {
    if (event.target === dialog) hide();
  });
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    go();
  });
  input.addEventListener("input", render);
  input.addEventListener("keydown", function (event) {
    if (event.key === "ArrowDown") {
      event.preventDefault();
      setActive(active + 1);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      setActive(active < 0 ? options.length - 1 : active - 1);
    } else if (event.key === "Home") {
      if (!options.length) return;
      event.preventDefault();
      setActive(0);
    } else if (event.key === "End") {
      if (!options.length) return;
      event.preventDefault();
      setActive(options.length - 1);
    } else if (event.key === "Enter") {
      if (!options.length) return;
      event.preventDefault();
      go();
    }
  });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && open) {
      event.preventDefault();
      hide();
      return;
    }
    if (open && event.key === "Tab") {
      var nodes = focusables();
      if (!nodes.length) return;
      var first = nodes[0];
      var last = nodes[nodes.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
      return;
    }
    if (open || event.altKey || typingTarget(event.target)) return;
    var shortcut = (event.metaKey || event.ctrlKey) && (event.key === "k" || event.key === "K");
    if (event.key === "/" && !event.metaKey && !event.ctrlKey) shortcut = true;
    if (!shortcut) return;
    event.preventDefault();
    show();
  });

  loadIndex().catch(function () {});
})();

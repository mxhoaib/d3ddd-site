/* Homepage hero motion. Transform and opacity only. Pauses off-screen.
   Reduced motion keeps the finished drawing and skips parallax. */
(function () {
  var root = document.documentElement;
  var scene = document.querySelector(".hero-scene");
  if (!scene) return;

  var reduce = false;
  try {
    reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (e) {}
  if (reduce) {
    root.classList.add("hero-static");
    return;
  }

  var hero = scene.closest(".hero");
  var next = hero ? hero.nextElementSibling : null;
  var fine = false;
  try {
    fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  } catch (e2) {}
  var rtl = root.getAttribute("dir") === "rtl";
  // Mirror the drawing for Arabic, then turn pills and loose text back so they read normally.
  function unflipNode(el, cx, cy) {
    el.setAttribute(
      "transform",
      "translate(" + cx + " " + cy + ") scale(-1 1) translate(" + (-cx) + " " + (-cy) + ")"
    );
  }
  function applyRtl() {
    if (!rtl) return;
    var rootG = scene.querySelector(".scene-root");
    if (!rootG) return;
    rootG.removeAttribute("transform");
    var pills = scene.querySelectorAll(".pill");
    for (var i = 0; i < pills.length; i++) {
      var g = pills[i];
      var at = (g.getAttribute("data-at") || "0 0").split(/\s+/);
      var x = parseFloat(at[0]) || 0;
      var y = parseFloat(at[1]) || 0;
      var rect = g.querySelector("rect");
      var w = rect ? parseFloat(rect.getAttribute("width")) || 0 : 0;
      var h = rect ? parseFloat(rect.getAttribute("height")) || 26 : 26;
      g.setAttribute(
        "transform",
        "translate(" + x + " " + y + ") translate(" + (w / 2) + " " + (h / 2) + ") scale(-1 1) translate(" + (-w / 2) + " " + (-h / 2) + ")"
      );
    }
    var texts = scene.querySelectorAll(".scene-root text");
    for (var j = 0; j < texts.length; j++) {
      var t = texts[j];
      if (t.closest && t.closest(".pill")) continue;
      t.removeAttribute("transform");
      var tx = parseFloat(t.getAttribute("x")) || 0;
      var ty = parseFloat(t.getAttribute("y")) || 0;
      var tw = t.getComputedTextLength ? t.getComputedTextLength() : 0;
      var anchor = t.getAttribute("text-anchor") || "start";
      var left = tx;
      if (anchor === "middle") left = tx - tw / 2;
      else if (anchor === "end") left = tx - tw;
      var fs = parseFloat(t.getAttribute("font-size")) || 13;
      unflipNode(t, left + tw / 2, ty - fs * 0.35);
    }
    rootG.setAttribute("transform", "translate(720 0) scale(-1 1)");
  }
  applyRtl();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(applyRtl);

  var mx = 0, my = 0, tx = 0, ty = 0;
  var scrollP = 0;
  var inView = true;
  var running = false;
  var taken = false;
  var ex = 0.56, exTarget = 0.56, p0 = 0, ex0 = 0.56;

  function frame() {
    if (document.hidden) {
      running = false;
      return;
    }
    mx += (tx - mx) * 0.075;
    my += (ty - my) * 0.075;
    if (taken) ex += (exTarget - ex) * 0.09;
    var mxOut = rtl ? -mx : mx;
    scene.style.setProperty("--mx", mxOut.toFixed(4));
    scene.style.setProperty("--my", my.toFixed(4));
    scene.style.setProperty("--scroll", scrollP.toFixed(4));
    if (taken) scene.style.setProperty("--ex", ex.toFixed(4));
    var idle = Math.abs(tx - mx) < 0.003 && Math.abs(ty - my) < 0.003 && (!taken || Math.abs(exTarget - ex) < 0.004);
    if (!inView && idle) {
      running = false;
      return;
    }
    requestAnimationFrame(frame);
  }

  function kick() {
    if (running) return;
    running = true;
    requestAnimationFrame(frame);
  }

  function measure() {
    if (!hero) return;
    var r = hero.getBoundingClientRect();
    var h = r.height || 1;
    var p = -r.top / (h * 0.82);
    if (p < 0) p = 0;
    if (p > 1) p = 1;
    scrollP = p;
    if (!taken && p > 0.04) {
      var cur = parseFloat(window.getComputedStyle(scene).getPropertyValue("--ex"));
      taken = true;
      p0 = p;
      ex0 = isFinite(cur) ? cur : 0.56;
      ex = ex0;
      scene.classList.add("is-driven");
    }
    if (taken) {
      var span = 1 - p0 || 1;
      var t = (p - p0) / span;
      if (t < 0) t = 0;
      if (t > 1) t = 1;
      exTarget = ex0 + t * (1 - ex0);
    }
    if (inView) kick();
  }

  if (hero && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      inView = false;
      for (var i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) inView = true;
      }
      if (inView) kick();
    }, { threshold: 0, rootMargin: "80px" });
    io.observe(hero);
  }

  window.addEventListener("scroll", measure, { passive: true });
  window.addEventListener("resize", measure, { passive: true });

  if (fine) {
    window.addEventListener("pointermove", function (e) {
      if (!hero) return;
      var r = hero.getBoundingClientRect();
      var outside = e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
      if (outside) {
        if (tx || ty) {
          tx = 0;
          ty = 0;
          kick();
        }
        return;
      }
      tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
      ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
      kick();
    }, { passive: true });
  }

  if (next && next.classList && next.classList.contains("section") && "IntersectionObserver" in window) {
    var nr = next.getBoundingClientRect();
    var vh = window.innerHeight || 800;
    if (nr.top > vh * 0.82) {
      next.classList.add("hero-await");
      var revealed = false;
      function show() {
        if (revealed) return;
        revealed = true;
        next.classList.add("is-revealed");
      }
      var nio = new IntersectionObserver(function (entries) {
        for (var j = 0; j < entries.length; j++) {
          if (entries[j].isIntersecting) show();
        }
      }, { threshold: 0.12 });
      nio.observe(next);
      window.setTimeout(show, 2800);
    }
  }

  document.addEventListener("visibilitychange", function () {
    if (!document.hidden) kick();
  });

  measure();
  kick();
})();

// Homepage hero: furnished living/dining room. The Spline runtime is imported only
// after the page has loaded and the browser is idle, so it never blocks first paint.
// If WebGL is missing, the visitor prefers reduced motion, the CDN fails, or the
// scene does not finish within 25s, the gold gradient grid stays in place.
const RUNTIME = "https://unpkg.com/@splinetool/runtime@2.0.126/build/runtime.js";
const SCENE = "https://prod.spline.design/7Q6BdrThb-USp2wy/scene.splinecode";

const root = document.documentElement;

function webglOk() {
  try {
    const c = document.createElement("canvas");
    const gl = window.WebGLRenderingContext && (c.getContext("webgl2") || c.getContext("webgl"));
    if (gl) {
      const lose = gl.getExtension("WEBGL_lose_context");
      if (lose) lose.loseContext();
    }
    return !!gl;
  } catch (e) {
    return false;
  }
}

function reducedMotion() {
  try {
    return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (e) {
    return false;
  }
}

function fail() {
  root.classList.add("no-webgl");
}

function start() {
  const canvas = document.getElementById("room3d");
  if (!canvas || root.classList.contains("no-webgl")) return;
  if (reducedMotion() || !webglOk()) {
    fail();
    return;
  }

  let gaveUp = false;
  const timer = window.setTimeout(() => {
    if (!root.classList.contains("room-ready")) {
      gaveUp = true;
      fail();
    }
  }, 25000);

  const scene = canvas.dataset.scene || SCENE;
  import(RUNTIME).then((mod) => {
    const Application = mod && mod.Application;
    if (typeof Application !== "function") throw new Error("missing runtime");
    const app = new Application(canvas);
    const mq = window.matchMedia("(max-width: 900px)");
    const fit = () => {
      try { app.setZoom(mq.matches ? 0.32 : 0.7); } catch (e) {}
    };
    return app.load(scene).then(() => {
      if (gaveUp || root.classList.contains("no-webgl")) {
        try { app.stop(); } catch (e) {}
        return;
      }
      try {
        (app.getAllObjects() || []).forEach((o) => {
          const name = String((o && o.name) || "");
          if (/^Text/.test(name) || /furnify/i.test(name)) o.visible = false;
        });
      } catch (e) {}
      try { app.setBackgroundColor("rgba(14,14,12,0)"); } catch (e) {}
      try {
        const em = app.eventManager;
        if (em) em.preventScroll = false;
      } catch (e) {}
      // The scene prevents default on wheel, which traps scrolling while the pointer is over the room.
      canvas.addEventListener("wheel", (e) => { e.stopImmediatePropagation(); }, { capture: true, passive: true });
      fit();
      if (mq.addEventListener) mq.addEventListener("change", fit);
      else if (mq.addListener) mq.addListener(fit);

      const hero = canvas.closest(".hero");
      if (hero && typeof app.stop === "function" && typeof app.play === "function" && "IntersectionObserver" in window) {
        const io = new IntersectionObserver((entries) => {
          entries.forEach((en) => {
            try {
              if (reducedMotion() || root.classList.contains("no-webgl")) app.stop();
              else if (en.isIntersecting) app.play();
              else app.stop();
            } catch (e) {}
          });
        });
        io.observe(hero);
      }

      try {
        const rm = window.matchMedia("(prefers-reduced-motion: reduce)");
        const onRm = () => {
          if (!rm.matches) return;
          try { app.stop(); } catch (e) {}
          root.classList.remove("room-ready");
          fail();
        };
        if (rm.addEventListener) rm.addEventListener("change", onRm);
        else if (rm.addListener) rm.addListener(onRm);
      } catch (e) {}

      window.clearTimeout(timer);
      requestAnimationFrame(() => root.classList.add("room-ready"));
    });
  }).catch(() => {
    window.clearTimeout(timer);
    fail();
  });
}

function schedule() {
  const run = () => {
    const ric = window.requestIdleCallback;
    if (typeof ric === "function") ric(() => start(), { timeout: 2000 });
    else window.setTimeout(start, 1);
  };
  if (document.readyState === "complete") run();
  else window.addEventListener("load", run, { once: true });
}

schedule();

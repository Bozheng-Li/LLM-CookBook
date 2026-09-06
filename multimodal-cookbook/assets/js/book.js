/* 多模态大模型 Cookbook · 站点运行时
 * 依赖同目录 manifest.js（BOOK）。 */
(function () {
  "use strict";

  /* ---------- 主题 ---------- */
  const savedTheme = localStorage.getItem("mmcook-theme") ||
    (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  document.documentElement.setAttribute("data-theme", savedTheme);

  /* ---------- 侧边栏 ---------- */
  const sidebar = document.getElementById("sidebar");
  const here = location.pathname.split("/").pop() || "index.html";
  if (sidebar && typeof BOOK !== "undefined") {
    let html = `<div class="side-brand"><a href="index.html">
      <div class="b-title">🍳 ${BOOK.title}</div>
      <div class="b-sub">${BOOK.subtitle}</div></a></div>`;
    BOOK.parts.forEach((part, pi) => {
      html += `<div class="side-part">${part.name}</div>`;
      part.chapters.forEach(ch => {
        const active = ch.path === here ? " active" : "";
        html += `<a class="side-ch${active}" href="${ch.path}"><span class="no">${ch.no}</span>${ch.title}</a>`;
      });
    });
    sidebar.innerHTML = html;
  }

  /* ---------- 上下章导航 ---------- */
  const pagerHost = document.querySelector(".pager");
  if (pagerHost && typeof BOOK !== "undefined") {
    const flat = [];
    BOOK.parts.forEach(p => p.chapters.forEach(c => flat.push(c)));
    const idx = flat.findIndex(c => c.path === here);
    let html = "";
    if (idx > 0) html += `<a href="${flat[idx-1].path}" class="prev"><span class="dir">← 上一章</span>${flat[idx-1].no} ${flat[idx-1].title}</a>`;
    else html += `<a href="index.html" class="prev"><span class="dir">← 返回</span>全书首页与学习路径</a>`;
    if (idx >= 0 && idx < flat.length - 1) html += `<a href="${flat[idx+1].path}" class="next"><span class="dir">下一章 →</span>${flat[idx+1].no} ${flat[idx+1].title}</a>`;
    pagerHost.innerHTML = html;
  }

  /* ---------- 阅读进度 + 回到顶部 ---------- */
  const bar = document.getElementById("progress-bar");
  const backtop = document.getElementById("backtop");
  window.addEventListener("scroll", () => {
    const h = document.documentElement;
    const pct = h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight) * 100;
    if (bar) bar.style.width = pct + "%";
    if (backtop) backtop.classList.toggle("show", h.scrollTop > 600);
  }, { passive: true });
  if (backtop) backtop.addEventListener("click", () => scrollTo({ top: 0, behavior: "smooth" }));

  /* ---------- 主题切换 / 移动端菜单 ---------- */
  const themeBtn = document.getElementById("theme-btn");
  if (themeBtn) themeBtn.addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", cur);
    localStorage.setItem("mmcook-theme", cur);
  });
  const menuBtn = document.getElementById("menu-btn");
  if (menuBtn) menuBtn.addEventListener("click", () => sidebar && sidebar.classList.toggle("open"));

  /* ---------- 搜索 ---------- */
  const input = document.getElementById("search-input");
  const results = document.getElementById("search-results");
  let INDEX = null;
  async function loadIndex() {
    if (INDEX) return INDEX;
    try {
      const r = await fetch("assets/js/search-index.json");
      INDEX = await r.json();
    } catch (e) {
      try { const r2 = await fetch("../assets/js/search-index.json"); INDEX = await r2.json(); }
      catch (e2) { INDEX = []; }
    }
    return INDEX;
  }
  async function buildResults(q) {
    const idx = await loadIndex();
    const ql = q.toLowerCase();
    const hits = [];
    for (const item of idx) {
      const t = (item.t || "").toLowerCase(), h = (item.h || "").toLowerCase(), k = (item.k || "").toLowerCase();
      if (t.includes(ql) || h.includes(ql) || k.includes(ql)) {
        hits.push(item);
        if (hits.length >= 30) break;
      }
    }
    if (!results) return;
    if (!hits.length) { results.style.display = "none"; return; }
    results.innerHTML = hits.map(it =>
      `<a class="sr-item" href="${it.p.startsWith("http") ? it.p : it.p}"><span class="sr-ch">${it.c}</span><br>${it.t}${it.h ? " · " + it.h : ""}</a>`
    ).join("");
    results.style.display = "block";
  }
  if (input && results) {
    input.addEventListener("input", e => {
      const q = e.target.value.trim();
      if (q.length >= 1) buildResults(q); else results.style.display = "none";
    });
    document.addEventListener("click", e => {
      if (!e.target.closest("#search-box")) results.style.display = "none";
    });
  }

  /* ---------- 简易代码高亮 ---------- */
  const KW = ["def","class","return","if","elif","else","for","while","import","from","as","with","try","except","finally","raise","yield","lambda","not","and","or","in","is","None","True","False","pass","break","continue","global","assert","async","await","del","self","function","const","let","var","echo","export","cd","pip","python","git","sudo","apt","conda","torch","do","then","fi","esac","case","int","float","double","void","struct","public","private","static","new","this","match"];
  function highlight(src) {
    let s = src.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    const store = [];
    function keep(html) { store.push(html); return `\x00${store.length - 1}\x00`; }
    s = s.replace(/(&quot;|"|')(?:\\.|(?!\1)[^\\\n])*\1/g, m => keep(`<span class="tok-str">${m}</span>`));
    s = s.replace(/(#[^\n]*|\/\/[^\n]*)/g, m => keep(`<span class="tok-com">${m}</span>`));
    s = s.replace(/@[\w.]+/g, m => keep(`<span class="tok-dec">${m}</span>`));
    s = s.replace(/\b(\d+\.?\d*(?:e-?\d+)?)\b/gi, m => keep(`<span class="tok-num">${m}</span>`));
    s = s.replace(new RegExp(`\\b(${KW.join("|")})\\b`, "g"), m => keep(`<span class="tok-kw">${m}</span>`));
    s = s.replace(/\b([A-Za-z_]\w*)(?=\()/g, m => keep(`<span class="tok-fn">${m}</span>`));
    s = s.replace(/\x00(\d+)\x00/g, (_, i) => store[+i]);
    return s;
  }
  document.querySelectorAll("pre").forEach(pre => {
    if (pre.dataset.hl) return;
    pre.dataset.hl = "1";
    const codeEl = pre.querySelector("code") || pre;
    const src = codeEl.textContent;
    codeEl.innerHTML = highlight(src);
  });

  /* ---------- 代码复制 ---------- */
  document.querySelectorAll(".copy-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const pre = btn.closest(".code-wrap").querySelector("pre");
      navigator.clipboard.writeText(pre.innerText).then(() => {
        btn.textContent = "已复制 ✓";
        setTimeout(() => (btn.textContent = "复制"), 1600);
      });
    });
  });

  /* ---------- 图片加载失败兜底 ---------- */
  document.querySelectorAll("figure img").forEach(img => {
    img.addEventListener("error", () => {
      const ph = document.createElement("div");
      ph.className = "img-fallback";
      ph.textContent = "🖼 该论文图片离线不可用（联网后刷新即可恢复）";
      img.replaceWith(ph);
    });
  });

  /* ---------- 标题锚点 ---------- */
  document.querySelectorAll("h2[id], h3[id]").forEach(h => {
    const a = document.createElement("a");
    a.className = "sec-anchor"; a.href = "#" + h.id; a.textContent = "¶";
    h.appendChild(a);
  });
})();

/* AI Agent Cookbook — client app */
(function () {
  "use strict";

  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };

  /* ---------- theme ---------- */
  var THEME_KEY = "aac-theme";
  function applyTheme(t) {
    document.documentElement.setAttribute("data-theme", t);
    var btns = $$(".theme-toggle");
    btns.forEach(function (b) { b.textContent = t === "dark" ? "☀️ 浅色" : "🌙 深色"; });
  }
  function initTheme() {
    var saved = null;
    try { saved = localStorage.getItem(THEME_KEY); } catch (e) {}
    var t = saved || (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    applyTheme(t);
    $$(".theme-toggle").forEach(function (b) {
      b.addEventListener("click", function () {
        var cur = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
        applyTheme(cur);
        try { localStorage.setItem(THEME_KEY, cur); } catch (e) {}
      });
    });
  }

  /* ---------- progress bar + toTop ---------- */
  function initProgress() {
    var bar = $("#progress"), toTop = $("#toTop");
    function upd() {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      var p = max > 0 ? (h.scrollTop / max) * 100 : 0;
      if (bar) bar.style.width = p + "%";
      if (toTop) toTop.classList.toggle("show", h.scrollTop > 500);
    }
    window.addEventListener("scroll", upd, { passive: true });
    upd();
    if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
  }

  /* ---------- sidebar (mobile) ---------- */
  function markActive() {
    var here = location.pathname.split("/").pop() || "index.html";
    var links = $$(".toc-part-body a");
    var active = null;
    links.forEach(function (a) {
      var target = a.getAttribute("href").split("/").pop().split("#")[0];
      a.classList.toggle("active", target === here);
      if (target === here) active = a;
    });
    return active;
  }
  function initSidebar() {
    var sb = $(".sidebar"), scrim = $(".scrim"), btn = $(".menu-btn");
    var active = markActive();
    if (!sb || !btn) return;
    function close() { sb.classList.remove("open"); if (scrim) scrim.classList.remove("show"); }
    btn.addEventListener("click", function () {
      sb.classList.toggle("open");
      if (scrim) scrim.classList.toggle("show", sb.classList.contains("open"));
    });
    if (scrim) scrim.addEventListener("click", close);
    // open the part containing active link
    if (active) {
      var part = active.closest(".toc-part");
      if (part) part.classList.add("open");
    } else {
      $$(".toc-part").forEach(function (p, i) { if (i < 1) p.classList.add("open"); });
    }
    $$(".toc-part-head").forEach(function (h) {
      h.addEventListener("click", function () { h.parentElement.classList.toggle("open"); });
    });
    // auto-scroll sidebar to active
    if (active && sb.scrollIntoView) {
      setTimeout(function () {
        var box = $(".toc-nav");
        if (box) box.scrollTop = active.offsetTop - box.clientHeight / 3;
      }, 60);
    }
  }

  /* ---------- search ---------- */
  var SEARCH_INDEX = null;
  function normText(s) { return (s || "").replace(/\s+/g, " ").trim(); }
  function loadIndex() {
    if (SEARCH_INDEX) return Promise.resolve(SEARCH_INDEX);
    return fetch("assets/search-index.json")
      .then(function (r) { if (!r.ok) throw new Error("index missing"); return r.json(); })
      .then(function (d) { SEARCH_INDEX = d; return d; })
      .catch(function () { SEARCH_INDEX = []; return SEARCH_INDEX; });
  }
  function snippet(text, q) {
    var i = text.toLowerCase().indexOf(q.toLowerCase());
    if (i < 0) return text.slice(0, 90);
    var start = Math.max(0, i - 30);
    return (start > 0 ? "…" : "") + text.slice(start, start + 110) + "…";
  }
  function scoreDoc(doc, terms) {
    var hay = doc.title.toLowerCase(), body = doc.body.toLowerCase();
    var score = 0, all = true;
    terms.forEach(function (t) {
      var inTitle = hay.indexOf(t) >= 0, inBody = body.indexOf(t) >= 0;
      if (!inTitle && !inBody) all = false;
      if (inTitle) score += 12;
      if (inBody) score += 3;
      if (hay.indexOf(t) === 0) score += 6;
    });
    return all ? score : -1;
  }
  function initSearch() {
    var input = $("#searchInput"), box = $("#searchResults");
    if (!input || !box) return;
    var activeIdx = -1, items = [], results = [];
    function render(q) {
      var terms = normText(q).toLowerCase().split(/\s+/).filter(Boolean);
      if (!terms.length) { box.classList.remove("open"); box.innerHTML = ""; return; }
      loadIndex().then(function (idx) {
        results = idx.map(function (doc) { return { doc: doc, s: scoreDoc(doc, terms) }; })
          .filter(function (x) { return x.s >= 0; })
          .sort(function (a, b) { return b.s - a.s; })
          .slice(0, 12);
        if (!results.length) {
          box.innerHTML = '<div class="sr-empty">没有找到「' + q.replace(/</g, "&lt;") + '」相关内容</div>';
        } else {
          box.innerHTML = results.map(function (r, i) {
            return '<a class="sr-item" data-i="' + i + '" href="' + r.doc.file + '">' +
              '<div class="sr-title">' + r.doc.title.replace(/</g, "&lt;") + "</div>" +
              '<div class="sr-snippet">' + snippet(r.doc.body, terms[0]) + "</div></a>";
          }).join("");
        }
        items = $$(".sr-item", box);
        activeIdx = -1;
        box.classList.add("open");
        items.forEach(function (el) {
          el.addEventListener("click", function () { box.classList.remove("open"); input.value = ""; });
        });
      });
    }
    var deb = null;
    input.addEventListener("input", function () {
      clearTimeout(deb);
      deb = setTimeout(function () { render(input.value); }, 160);
    });
    input.addEventListener("focus", function () { if (input.value) render(input.value); });
    input.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        if (!items.length) return;
        activeIdx = (activeIdx + (e.key === "ArrowDown" ? 1 : -1) + items.length) % items.length;
        items.forEach(function (el, i) { el.classList.toggle("active", i === activeIdx); });
        items[activeIdx].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter") {
        if (activeIdx >= 0 && items[activeIdx]) { window.location.href = items[activeIdx].getAttribute("href"); }
        else if (items.length) { window.location.href = items[0].getAttribute("href"); }
      } else if (e.key === "Escape") {
        box.classList.remove("open"); input.blur();
      }
    });
    document.addEventListener("click", function (e) {
      if (!box.contains(e.target) && e.target !== input) box.classList.remove("open");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "/" && document.activeElement !== input && !/input|textarea/i.test(document.activeElement.tagName)) {
        e.preventDefault(); input.focus();
      }
    });
  }

  /* ---------- copy code ---------- */
  function initCopy() {
    $$(".codeblock").forEach(function (cb) {
      var btn = $(".copy", cb), pre = $("pre", cb);
      if (!btn || !pre) return;
      btn.addEventListener("click", function () {
        var text = pre.innerText;
        function done(ok) {
          btn.textContent = ok ? "已复制 ✓" : "复制失败";
          setTimeout(function () { btn.textContent = "复制"; }, 1600);
        }
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(false); });
        } else {
          var ta = document.createElement("textarea");
          ta.value = text; document.body.appendChild(ta); ta.select();
          try { document.execCommand("copy"); done(true); } catch (e) { done(false); }
          document.body.removeChild(ta);
        }
      });
    });
  }

  /* ---------- right page map ---------- */
  function initPageMap() {
    var map = $(".pagemap");
    if (!map) return;
    var hs = $$("h2[id], h3[id]", $(".content") || document);
    if (hs.length < 2) { map.style.display = "none"; return; }
    var html = '<div class="pm-title">本页目录</div>';
    hs.forEach(function (h) {
      if (!h.id) return;
      var cls = h.tagName === "H3" ? ' style="padding-left:20px;font-size:11.5px"' : "";
      html += '<a href="#' + h.id + '"' + cls + ">" + h.textContent.replace(/^[#§\d.\s]+/, "") + "</a>";
    });
    map.innerHTML = html;
    var links = $$("a", map);
    function highlight() {
      var cur = -1;
      hs.forEach(function (h, i) {
        var r = h.getBoundingClientRect();
        if (r.top < 140) cur = i;
      });
      links.forEach(function (a, i) { a.classList.toggle("active", i === cur); });
    }
    window.addEventListener("scroll", highlight, { passive: true });
    highlight();
  }

  /* ---------- init ---------- */
  document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initProgress();
    initSidebar();
    initSearch();
    initCopy();
    initPageMap();
  });
})();

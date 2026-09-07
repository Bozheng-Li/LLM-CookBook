/* 全站导航：侧边栏、上一章/下一章、页内目录、搜索、进度条、回到顶部 */
(function () {
  var M = window.COOKBOOK_MANIFEST;
  if (!M) return;
  var path = location.pathname.split("/").pop() || M.home;

  /* ---------- 阅读进度条 & 回到顶部 ---------- */
  var bar = document.createElement("div"); bar.id = "progress-bar";
  document.body.appendChild(bar);
  var topBtn = document.createElement("button"); topBtn.id = "back-top"; topBtn.textContent = "↑";
  topBtn.title = "回到顶部";
  document.body.appendChild(topBtn);
  window.addEventListener("scroll", function () {
    var h = document.documentElement;
    var pct = (h.scrollTop) / (h.scrollHeight - h.clientHeight) * 100;
    bar.style.width = pct + "%";
    topBtn.className = h.scrollTop > 400 ? "show" : "";
  });
  topBtn.onclick = function () { window.scrollTo({ top: 0, behavior: "smooth" }); };

  /* ---------- 侧边栏 ---------- */
  var sidebar = document.getElementById("sidebar");
  if (!sidebar) return;
  var html = '<span class="brand"><a href="' + M.home + '">' + M.title + "</a>" +
    '<span class="sub">' + M.subtitle + "</span></span>" +
    '<div class="searchbox"><input id="cb-search" type="search" placeholder="搜索章节标题…（回车打开搜索页）"></div>';
  M.parts.forEach(function (part) {
    html += '<div class="part-title">' + part.title + "</div>";
    part.chapters.forEach(function (ch) {
      var cur = path && ch.file.indexOf(path) !== -1 ? ' class="chap active"' : ' class="chap"';
      html += '<a' + cur + ' data-title="' + ch.title + '" href="' + ch.file + '">' + ch.title + "</a>";
    });
  });
  sidebar.innerHTML = html;

  /* ---------- 侧边栏搜索（过滤标题） ---------- */
  var input = document.getElementById("cb-search");
  input.addEventListener("input", function () {
    var q = input.value.trim().toLowerCase();
    sidebar.querySelectorAll("a.chap").forEach(function (a) {
      var hit = !q || a.getAttribute("data-title").toLowerCase().indexOf(q) !== -1;
      a.classList.toggle("search-hidden", !hit);
    });
    sidebar.querySelectorAll(".part-title").forEach(function (p) { p.style.display = q ? "none" : ""; });
  });
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      var q = input.value.trim();
      if (q) location.href = M.home.replace("index.html", "") + "search.html?q=" + encodeURIComponent(q);
    }
  });

  /* ---------- 上一章 / 下一章 ---------- */
  var flat = [];
  M.parts.forEach(function (p) { p.chapters.forEach(function (c) { flat.push({ part: p.title, ch: c }); }); });
  var idx = flat.findIndex(function (f) { return path && f.ch.file.indexOf(path) !== -1; });
  var footer = document.querySelector(".chapter-footer");
  if (footer && idx !== -1) {
    var pn = '<div class="prev-next">';
    pn += idx > 0
      ? '<a href="' + flat[idx - 1].ch.file + '"><span class="dir">← 上一章</span><span class="pn-title">' + flat[idx - 1].ch.title + "</span></a>"
      : '<a href="' + M.home + '"><span class="dir">← 返回</span><span class="pn-title">本书首页</span></a>';
    pn += idx < flat.length - 1
      ? '<a href="' + flat[idx + 1].ch.file + '"><span class="dir">下一章 →</span><span class="pn-title">' + flat[idx + 1].ch.title + "</span></a>"
      : '<a href="' + M.home + '"><span class="dir">全书完</span><span class="pn-title">返回首页</span></a>';
    pn += "</div>";
    footer.innerHTML = pn + '<div class="edit-github">《' + M.title + "》 · 持续更新 · 欢迎 Star 与 PR</div>" + footer.innerHTML;
  }

  /* ---------- 页内目录（自动生成 h2） ---------- */
  var tocBox = document.getElementById("auto-toc");
  if (tocBox) {
    var h2s = document.querySelectorAll(".content h2");
    var items = [];
    h2s.forEach(function (h2, i) {
      if (!h2.id) h2.id = "sec-" + (i + 1);
      items.push('<li><a href="#' + h2.id + '">' + h2.textContent + "</a></li>");
    });
    if (items.length) tocBox.innerHTML = '<div class="toc-title">📑 本页目录</div><ol>' + items.join("") + "</ol>";
  }
})();

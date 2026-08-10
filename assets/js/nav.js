/* ===========================================================
   nav.js — 侧边栏 / 搜索 / 难度筛选 / 主题切换 / 阅读进度 / 面包屑 / 上下页
   依赖:window.TOC (toc.js)、window.SEARCH_INDEX (search-index.js)、window.ROOT
   =========================================================== */
(function () {
  'use strict';

  var ROOT = window.ROOT;
  if (ROOT === undefined) {
    var navScript = document.currentScript;
    var navSrc = navScript && navScript.getAttribute('src') || '';
    ROOT = navSrc.indexOf('/') >= 0 ? navSrc.replace(/assets\/js\/nav\.js(?:\?.*)?$/, '') : '';
  }
  var TOC = window.TOC || { parts: [] };
  var IDX = window.SEARCH_INDEX || [];
  var CUR_PART = document.body.getAttribute('data-part') || '';
  var CUR_TOPIC = document.body.getAttribute('data-topic') || '';
  var LEVEL_LABEL = { basic: '入门', inter: '进阶', adv: '高级' };
  var READ_KEY = 'cb_read_v1';
  var THEME_KEY = 'cb_theme_v1';

  function url(p) { return ROOT + p; }
  function partUrl(part) { return url('pages/' + part.id + '/index.html'); }
  function topicUrl(part, topic) { return url('pages/' + part.id + '/' + topic.id + '.html'); }
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html !== undefined) e.innerHTML = html;
    return e;
  }

  /* 当前页的 root 相对路径(用于已读标记与搜索索引对齐) */
  function currentHref() {
    if (!CUR_PART) return 'index.html';
    if (!CUR_TOPIC) return 'pages/' + CUR_PART + '/index.html';
    return 'pages/' + CUR_PART + '/' + CUR_TOPIC + '.html';
  }

  /* ---------------- 扁平索引 ---------------- */
  var flat = [];
  TOC.parts.forEach(function (part) {
    flat.push({ part: part, topic: null, href: partUrl(part) });
    part.topics.forEach(function (topic) {
      flat.push({ part: part, topic: topic, href: topicUrl(part, topic) });
    });
  });
  var totalTopics = flat.filter(function (it) { return it.topic; }).length;

  /* ---------------- 主题 ---------------- */
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    try { localStorage.setItem(THEME_KEY, theme); } catch (e) {}
    var hl = document.getElementById('hljs-theme');
    if (hl) {
      hl.href = theme === 'dark'
        ? 'https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github-dark.min.css'
        : 'https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github.min.css';
    }
    if (typeof window.CB_SET_THEME === 'function') window.CB_SET_THEME(theme);
  }
  function initTheme() {
    var saved;
    try { saved = localStorage.getItem(THEME_KEY); } catch (e) {}
    if (!saved) saved = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    applyTheme(saved);
  }

  /* ---------------- 阅读进度 ---------------- */
  function getRead() {
    try { return JSON.parse(localStorage.getItem(READ_KEY) || '[]'); } catch (e) { return []; }
  }
  function setRead(arr) {
    try { localStorage.setItem(READ_KEY, JSON.stringify(arr)); } catch (e) {}
  }
  function markCurrentRead() {
    if (!CUR_TOPIC) return; // 仅知识点页计入已读
    var arr = getRead();
    var h = currentHref();
    if (arr.indexOf(h) === -1) { arr.push(h); setRead(arr); }
  }
  function readCount() {
    var arr = getRead(), set = {};
    arr.forEach(function (h) { set[h] = 1; });
    var n = 0;
    flat.forEach(function (it) { if (it.topic && set[it.href]) n++; });
    return n;
  }

  /* ---------------- 顶栏 ---------------- */
  function buildTopbar() {
    var host = document.getElementById('topbar');
    if (!host) return;
    host.className = 'topbar';
    var isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    host.innerHTML =
      '<button class="menu-btn" id="menuBtn" aria-label="菜单">' +
        '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M2 4h12M2 8h12M2 12h12"/></svg>' +
      '</button>' +
      '<a class="brand" href="' + url('index.html') + '">' +
        '<span class="logo">LLM</span>' +
        '<span class="bt">' + TOC.site.title + '</span>' +
        '<span class="ver">' + TOC.site.version + '</span>' +
      '</a>' +
      '<div class="search-box">' +
        '<span class="icon"><svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5L14 14" stroke-linecap="round"/></svg></span>' +
        '<input type="text" id="searchInput" placeholder="搜索知识点、关键词、正文…  (按 /)" autocomplete="off">' +
        '<div class="search-results" id="searchResults"></div>' +
      '</div>' +
      '<button class="theme-toggle" id="themeBtn" aria-label="切换主题" title="切换浅色/暗色">' +
        (isDark
          ? '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="3.2"/><path d="M8 1.5v1.6M8 12.9v1.6M1.5 8h1.6M12.9 8h1.6M3.4 3.4l1.1 1.1M11.5 11.5l1.1 1.1M12.6 3.4l-1.1 1.1M4.5 11.5l-1.1 1.1" stroke-linecap="round"/></svg>'
          : '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M13.5 9.2A5.3 5.3 0 0 1 6.8 2.5a5.3 5.3 0 1 0 6.7 6.7Z" stroke-linejoin="round"/></svg>') +
      '</button>';
    var btn = document.getElementById('themeBtn');
    btn.addEventListener('click', function () {
      var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      btn.innerHTML = next === 'dark'
        ? '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="3.2"/><path d="M8 1.5v1.6M8 12.9v1.6M1.5 8h1.6M12.9 8h1.6M3.4 3.4l1.1 1.1M11.5 11.5l1.1 1.1M12.6 3.4l-1.1 1.1M4.5 11.5l-1.1 1.1" stroke-linecap="round"/></svg>'
        : '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M13.5 9.2A5.3 5.3 0 0 1 6.8 2.5a5.3 5.3 0 1 0 6.7 6.7Z" stroke-linejoin="round"/></svg>';
    });
  }

  /* ---------------- 侧边栏 ---------------- */
  function buildSidebar() {
    var host = document.getElementById('sidebar');
    if (!host) return;
    host.className = 'sidebar';

    var readSet = {};
    getRead().forEach(function (h) { readSet[h] = 1; });

    var filter = el('div', 'filter-row');
    filter.innerHTML =
      '<span class="filter-chip active" data-lv="all">全部</span>' +
      '<span class="filter-chip" data-lv="basic">入门</span>' +
      '<span class="filter-chip" data-lv="inter">进阶</span>' +
      '<span class="filter-chip" data-lv="adv">高级</span>';
    host.appendChild(filter);

    TOC.parts.forEach(function (part) {
      var wrap = el('div', 'nav-part' + (part.id === CUR_PART ? ' open' : ''));
      var head = el('div', 'nav-part-head');
      head.innerHTML =
        '<svg class="caret" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3.5L10.5 8L6 12.5"/></svg>' +
        '<span class="pnum">' + part.num + '</span>' +
        '<span>' + part.title + '</span>' +
        (part.frontier ? '<span class="fire">前沿</span>' : '');
      head.addEventListener('click', function () { wrap.classList.toggle('open'); });
      wrap.appendChild(head);

      var list = el('div', 'nav-topics');
      var idxLink = el('a', 'nav-topic' + (part.id === CUR_PART && !CUR_TOPIC ? ' current' : ''));
      idxLink.href = partUrl(part);
      idxLink.innerHTML = '<span class="dot" style="background:#b4b2a9"></span><span>本篇目录</span>';
      list.appendChild(idxLink);

      part.topics.forEach(function (topic) {
        var read = !!readSet[topicUrl(part, topic)];
        var a = el('a', 'nav-topic' + (part.id === CUR_PART && topic.id === CUR_TOPIC ? ' current' : '') + (read ? ' read' : ''));
        a.href = topicUrl(part, topic);
        a.setAttribute('data-lv', topic.level);
        a.innerHTML = '<span class="dot ' + topic.level + '"></span><span>' + topic.title + '</span>' +
          (read ? '<span class="ti-check">✓</span>' : '');
        list.appendChild(a);
      });
      wrap.appendChild(list);
      host.appendChild(wrap);
    });

    // 固定入口(术语表 / 依赖图)
    var extra = el('div', 'nav-extra');
    extra.innerHTML =
      '<a href="' + url('glossary.html') + '">' +
        '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 4.5h12M2 8h12M2 11.5h8" stroke-linecap="round"/></svg>术语表</a>' +
      '<a href="' + url('dependency.html') + '">' +
        '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="4" cy="4" r="1.8"/><circle cx="12" cy="8" r="1.8"/><circle cx="5" cy="12" r="1.8"/><path d="M5.6 4.6 10.4 7.2M5 10.4 4.4 5.8" stroke-linecap="round"/></svg>知识依赖图</a>';
    host.appendChild(extra);

    // 阅读进度
    var foot = el('div', 'sidebar-foot');
    host.appendChild(foot);
    renderProgress(foot);

    // 难度筛选
    filter.addEventListener('click', function (e) {
      var chip = e.target.closest('.filter-chip');
      if (!chip) return;
      filter.querySelectorAll('.filter-chip').forEach(function (c) { c.classList.remove('active'); });
      chip.classList.add('active');
      var lv = chip.getAttribute('data-lv');
      document.querySelectorAll('.nav-topic[data-lv], .topic-item[data-lv]').forEach(function (n) {
        n.classList.toggle('filtered-out', lv !== 'all' && n.getAttribute('data-lv') !== lv);
      });
      if (lv !== 'all') {
        document.querySelectorAll('.nav-part').forEach(function (p) { p.classList.add('open'); });
      }
    });

    var cur = host.querySelector('.nav-topic.current');
    if (cur) setTimeout(function () {
      var t = cur.offsetTop - host.clientHeight / 2;
      if (t > 0) host.scrollTop = t;
    }, 60);
  }

  function renderProgress(foot) {
    var n = readCount();
    var pct = totalTopics ? Math.round(n / totalTopics * 100) : 0;
    foot.innerHTML =
      '<div class="sf-row"><span>阅读进度</span>' +
      '<span class="sf-count">' + n + ' / ' + totalTopics + '</span></div>' +
      '<div class="sf-bar"><div class="sf-fill" style="width:' + pct + '%"></div></div>' +
      '<div style="margin-top:7px;text-align:right"><span class="sf-reset" id="resetRead">清除进度</span></div>';
    var r = document.getElementById('resetRead');
    if (r) r.addEventListener('click', function () {
      setRead([]);
      document.querySelectorAll('.nav-topic.read').forEach(function (n) {
        n.classList.remove('read');
        var c = n.querySelector('.ti-check'); if (c) c.remove();
      });
      renderProgress(foot);
    });
  }

  /* ---------------- 搜索(全文 + 片段) ---------------- */
  function bindSearch() {
    var input = document.getElementById('searchInput');
    var box = document.getElementById('searchResults');
    if (!input || !box) return;

    function snippet(text, q) {
      if (!text) return '';
      var i = text.toLowerCase().indexOf(q);
      if (i < 0) return text.slice(0, 70);
      var s = Math.max(0, i - 30);
      var e = Math.min(text.length, i + q.length + 50);
      var seg = (s > 0 ? '…' : '') + text.slice(s, e) + (e < text.length ? '…' : '');
      var re = new RegExp('(' + q.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
      return seg.replace(re, '<mark>$1</mark>');
    }

    function render(q) {
      q = q.trim().toLowerCase();
      if (!q) { box.classList.remove('show'); return; }
      var hits = [];
      // 1) TOC 精确匹配(标题/关键词)优先
      flat.forEach(function (it) {
        var title = it.topic ? it.topic.title : it.part.title;
        var hay = (title + ' ' + (it.topic ? (it.topic.desc || '') + ' ' + (it.topic.keywords || []).join(' ') : it.part.desc) + ' ' + it.part.title).toLowerCase();
        if (hay.indexOf(q) !== -1) {
          hits.push({ href: it.href, part: it.part, title: title, level: it.topic ? it.topic.level : 'basic', snippet: '' });
        }
      });
      // 2) 全文索引补充(正文命中)
      if (IDX.length) {
        IDX.forEach(function (e) {
          if (e.href === 'index.html') return;
          if (hits.some(function (h) { return h.href === e.href; })) return;
          var t = (e.title + ' ' + (e.text || '')).toLowerCase();
          var idx = t.indexOf(q);
          if (idx !== -1) {
            var part = null;
            flat.forEach(function (it) { if (it.href === e.href) part = it.part; });
            hits.push({ href: e.href, part: part, title: e.title, level: e.level || 'basic', snippet: snippet(e.text || '', q) });
          }
        });
      }
      hits = hits.slice(0, 14);
      if (!hits.length) {
        box.innerHTML = '<div class="sr-empty">没找到相关知识点</div>';
      } else {
        box.innerHTML = hits.map(function (it) {
          var lv = it.level || 'basic';
          return '<a class="sr-item" href="' + it.href + '">' +
            '<span class="sr-hd"><span class="sr-part">' + (it.part ? it.part.num + ' · ' + it.part.title : '首页') + '</span>' +
            '<span class="level ' + lv + '">' + LEVEL_LABEL[lv] + '</span></span>' +
            '<span style="font-weight:600">' + it.title + '</span>' +
            (it.snippet ? '<span class="sr-snippet">' + it.snippet + '</span>' : '') +
            '</a>';
        }).join('');
      }
      box.classList.add('show');
    }

    input.addEventListener('input', function () { render(this.value); });
    input.addEventListener('focus', function () { if (this.value.trim()) render(this.value); });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.search-box')) box.classList.remove('show');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && document.activeElement !== input) { e.preventDefault(); input.focus(); }
      if (e.key === 'Escape') { box.classList.remove('show'); input.blur(); }
    });
  }

  /* ---------------- 移动端菜单 ---------------- */
  function bindMenu() {
    var btn = document.getElementById('menuBtn');
    var sb = document.getElementById('sidebar');
    if (!btn || !sb) return;
    var ov = el('div', 'overlay');
    document.body.appendChild(ov);
    function toggle(on) { sb.classList.toggle('open', on); ov.classList.toggle('show', on); }
    btn.addEventListener('click', function () { toggle(!sb.classList.contains('open')); });
    ov.addEventListener('click', function () { toggle(false); });
  }

  /* ---------------- 面包屑 + 上下页 ---------------- */
  function buildCrumbAndPager() {
    var part = null, topic = null, idx = -1;
    TOC.parts.forEach(function (p) { if (p.id === CUR_PART) part = p; });
    if (part && CUR_TOPIC) {
      part.topics.forEach(function (t) { if (t.id === CUR_TOPIC) topic = t; });
    }
    flat.forEach(function (it, i) {
      if (it.part.id === CUR_PART && it.topic && it.topic.id === CUR_TOPIC) idx = i;
    });

    var cb = document.getElementById('breadcrumb');
    if (cb && part) {
      cb.className = 'breadcrumb';
      var html = '<a href="' + url('index.html') + '">首页</a><span class="sep">/</span>' +
                 '<a href="' + partUrl(part) + '">' + part.num + ' ' + part.title + '</a>';
      if (topic) html += '<span class="sep">/</span><span>' + topic.title + '</span>';
      cb.innerHTML = html;
    }

    var pg = document.getElementById('pager');
    if (pg && idx >= 0) {
      pg.className = 'pager';
      var prev = flat[idx - 1], next = flat[idx + 1], h = '';
      if (prev) h += '<a class="prev" href="' + prev.href + '"><span class="pg-label">← 上一节 · ' + prev.part.num + '</span><span class="pg-title">' + (prev.topic ? prev.topic.title : prev.part.title) + '</span></a>';
      if (next) h += '<a class="next" href="' + next.href + '"><span class="pg-label">下一节 · ' + next.part.num + ' →</span><span class="pg-title">' + (next.topic ? next.topic.title : next.part.title) + '</span></a>';
      pg.innerHTML = h;
    }
  }

  /* ---------------- 展开/收起全部(深入层) ---------------- */
  function buildDeepTools() {
    if (!CUR_TOPIC) return; // 仅知识点页
    var container = document.querySelector('.container');
    if (!container) return;
    var deeps = document.querySelectorAll('details.deep');
    if (!deeps.length) return;
    var bar = el('div', 'deep-tools');
    bar.innerHTML = '<button id="expandAll">展开全部</button><button id="collapseAll">收起全部</button>';
    var h2 = container.querySelector('h2');
    if (h2) h2.parentNode.insertBefore(bar, h2);
    else container.insertBefore(bar, container.firstChild);
    document.getElementById('expandAll').addEventListener('click', function () {
      deeps.forEach(function (d) { d.open = true; });
    });
    document.getElementById('collapseAll').addEventListener('click', function () {
      deeps.forEach(function (d) { d.open = false; });
    });
  }

  /* ---------------- 页内小目录 ---------------- */
  function buildPageToc() {
    var host = document.getElementById('pageToc');
    if (!host) return;
    var hs = document.querySelectorAll('.container h2');
    if (hs.length < 2) { host.style.display = 'none'; return; }
    var html = '<div class="pt-head">本页目录</div>';
    hs.forEach(function (h, i) {
      if (!h.id) h.id = 'sec-' + i;
      html += '<a href="#' + h.id + '">' + h.textContent + '</a>';
    });
    host.className = 'page-toc';
    host.innerHTML = html;
    var links = host.querySelectorAll('a');
    window.addEventListener('scroll', function () {
      var pos = window.scrollY + 120, active = 0;
      hs.forEach(function (h, i) { if (h.offsetTop <= pos) active = i; });
      links.forEach(function (a, i) { a.classList.toggle('active', i === active); });
    }, { passive: true });
  }

  /* ---------------- 補充深化资料 ---------------- */
  function loadResourceCards() {
    if (!CUR_PART || document.querySelector('.resource-deepening')) return;
    var script = document.createElement('script');
    script.src = url('assets/js/resources.js');
    script.async = true;
    script.onload = function () {
      if (typeof window.CB_RENDER_RESOURCES === 'function') window.CB_RENDER_RESOURCES();
    };
    script.onerror = function () {
      // 资料脚本失败时保留正文与手工参考文献，不阻塞页面阅读。
    };
    document.head.appendChild(script);
  }

  function loadTechnicalDepth() {
    if (!CUR_TOPIC || document.querySelector('.technical-deepening')) return;
    var script = document.createElement('script');
    script.src = url('assets/js/depth.js');
    script.async = true;
    script.onload = function () { if (typeof window.CB_RENDER_DEPTH === 'function') window.CB_RENDER_DEPTH(); };
    document.head.appendChild(script);
  }

  /* ---------------- 启动 ---------------- */
  function init() {
    initTheme();
    buildTopbar();
    buildSidebar();
    bindSearch();
    bindMenu();
    buildCrumbAndPager();
    buildDeepTools();
    buildPageToc();
    markCurrentRead();
    loadTechnicalDepth();
    loadResourceCards();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  window.CookbookNav = { flat: flat, url: url, topicUrl: topicUrl, partUrl: partUrl };
})();

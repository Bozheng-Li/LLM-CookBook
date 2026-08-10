/* ===========================================================
   render.js — Mermaid / KaTeX / highlight.js / Chart.js 初始化
   全部走 CDN,按需生效;无网络时页面仍可正常阅读。
   提供 window.CB_SET_THEME(theme) 供主题切换时重新着色。

   v2.0 · 2026-08-07
   - Mermaid 升级至 11.x,统一精致配色 + 圆角节点 + 入场动画
   - 流程图布局参数优化(nodeSpacing / rankSpacing / padding)
   - 保留深浅主题切换与图表重着色能力
   =========================================================== */
(function () {
  'use strict';

  var LIGHT = {
    background: '#ffffff',
    primaryColor: '#e6f1fb', primaryTextColor: '#0c447c', primaryBorderColor: '#185fa5',
    lineColor: '#8a91a1', lineColorHover: '#185fa5',
    secondaryColor: '#faeeda', secondaryTextColor: '#633806', secondaryBorderColor: '#ba7517',
    tertiaryColor: '#eaf3de', tertiaryTextColor: '#173404', tertiaryBorderColor: '#639922',
    noteBkgColor: '#f1f3f6', noteTextColor: '#4a5160', noteBorderColor: '#d0d5de',
    clusterBkg: '#f7f9fc', clusterBorder: '#c6cfdb',
    edgeLabelBackground: '#ffffff', fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif',
    fontSize: '14px'
  };
  var DARK = {
    background: '#181b21',
    primaryColor: '#14283d', primaryTextColor: '#cfe2f5', primaryBorderColor: '#4f9be0',
    lineColor: '#5a626e', lineColorHover: '#4f9be0',
    secondaryColor: '#2e2410', secondaryTextColor: '#e0a44b', secondaryBorderColor: '#e0a44b',
    tertiaryColor: '#16321a', tertiaryTextColor: '#7ec85a', tertiaryBorderColor: '#7ec85a',
    noteBkgColor: '#20242c', noteTextColor: '#b3b9c4', noteBorderColor: '#383f4a',
    clusterBkg: '#1e232b', clusterBorder: '#323a46',
    edgeLabelBackground: '#20242c', fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif',
    fontSize: '14px'
  };

  function mermaidCfg(theme) {
    var v = theme === 'dark' ? DARK : LIGHT;
    return {
      startOnLoad: false,
      theme: 'base',
      securityLevel: 'loose',
      maxTextSize: 1000000,
      fontFamily: v.fontFamily,
      themeVariables: v,
      flowchart: {
        curve: 'basis', padding: 16, nodeSpacing: 55, rankSpacing: 62,
        useMaxWidth: true, htmlLabels: true
      },
      sequence: { useMaxWidth: true, actorMargin: 50, messageMargin: 42, boxMargin: 10 },
      state: { useMaxWidth: true, radius: 8 },
      class: { useMaxWidth: true }
    };
  }

  /* 注入全局图表样式:圆角节点 + 入场动画 + 标签描边 */
  function injectFigStyles() {
    var css =
      '@keyframes cbFigIn{from{opacity:0;transform:translateY(9px)}to{opacity:1;transform:none}}' +
      '.mermaid svg{animation:cbFigIn .55s cubic-bezier(.22,.61,.36,1) both}' +
      '.mermaid svg .node rect,.mermaid svg .node circle,.mermaid svg .node polygon,.mermaid svg .node path' +
      '{shape-rendering:geometricPrecision}' +
      '.mermaid svg .node rect{rx:10px}' +
      '.mermaid svg .label{font-weight:500}' +
      '.mermaid svg .edgeLabel{background:transparent!important}' +
      '.mermaid svg .cluster rect{rx:12px}' +
      '.mermaid svg .flowchart-link{stroke-linecap:round}';
    var st = document.createElement('style');
    st.textContent = css;
    document.head.appendChild(st);
  }

  function initMermaid() {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize(mermaidCfg('light'));
  }

  /* 保存每个 Mermaid 节点的原始源码,供主题切换时重渲染 */
  function saveMermaidSrc() {
    document.querySelectorAll('.mermaid').forEach(function (n) {
      if (n.dataset.src === undefined && n.textContent.trim()) n.dataset.src = n.textContent;
    });
  }

  function reThemeMermaid(theme) {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize(mermaidCfg(theme));
    var nodes = document.querySelectorAll('.mermaid');
    nodes.forEach(function (n) {
      if (n.dataset.src === undefined) return;
      var host = document.createElement('div');
      host.className = 'mermaid';
      host.dataset.src = n.dataset.src;
      host.textContent = n.dataset.src;
      n.replaceWith(host);
    });
    try {
      mermaid.run({ nodes: document.querySelectorAll('.mermaid') });
    } catch (e) { /* 重渲染失败时保留旧图 */ }
    initFigureZoom();
  }

  /* KaTeX: 自动渲染 $...$ 与 $$...$$ */
  function initKatex() {
    if (typeof renderMathInElement === 'undefined') return;
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\[', right: '\\]', display: true },
        { left: '\\(', right: '\\)', display: false },
        { left: '$', right: '$', display: false }
      ],
      ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option'],
      throwOnError: false,
      strict: 'ignore'
    });
  }

  /* 代码高亮 */
  function initHighlight() {
    if (typeof hljs === 'undefined') return;
    document.querySelectorAll('pre code').forEach(function (b) {
      try { hljs.highlightElement(b); } catch (e) { /* noop */ }
    });
  }

  /* 图表和论文插图在正文中按列宽显示，点击后打开原尺寸阅读层。 */
  function initFigureZoom() {
    document.querySelectorAll('.mermaid').forEach(function (node) {
      node.dataset.cbZoom = 'ready';
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.setAttribute('aria-label', '放大查看流程图');
    });
    if (document.body.dataset.cbZoomBound) return;
    document.body.dataset.cbZoomBound = '1';
    document.addEventListener('click', function (event) {
      var source = event.target.closest('.mermaid, .paper-figure img');
      if (!source || event.target.closest('.cb-zoom-layer')) return;
      var visual = source.matches('img') ? source.cloneNode(true) : source.querySelector('svg');
      if (!visual) return;
      var layer = document.createElement('div');
      layer.className = 'cb-zoom-layer';
      layer.setAttribute('role', 'dialog');
      layer.setAttribute('aria-modal', 'true');
      var panel = document.createElement('div');
      panel.className = 'cb-zoom-panel';
      var close = document.createElement('button');
      close.className = 'cb-zoom-close';
      close.type = 'button';
      close.setAttribute('aria-label', '关闭放大视图');
      close.textContent = '×';
      panel.appendChild(close);
      panel.appendChild(visual);
      layer.appendChild(panel);
      document.body.appendChild(layer);
      document.body.style.overflow = 'hidden';
      function dismiss() { layer.remove(); document.body.style.overflow = ''; document.removeEventListener('keydown', onKey); }
      function onKey(e) { if (e.key === 'Escape') dismiss(); }
      close.addEventListener('click', dismiss);
      layer.addEventListener('click', function (e) { if (e.target === layer) dismiss(); });
      document.addEventListener('keydown', onKey);
      close.focus();
    });
    document.addEventListener('keydown', function (event) {
      var node = document.activeElement;
      if (event.key === 'Enter' && node && node.matches('.mermaid')) node.click();
    });
  }

  /* Chart.js 默认(随主题变化) */
  function chartTheme(theme) {
    if (typeof Chart === 'undefined') return;
    var dark = theme === 'dark';
    Chart.defaults.color = dark ? '#b3b9c4' : '#4a5160';
    Chart.defaults.borderColor = dark ? '#2a2f38' : '#e3e6ec';
    Chart.defaults.font.family = '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif';
    Chart.defaults.font.size = 12;
    Chart.defaults.plugins.legend.labels.boxWidth = 12;
    Chart.defaults.plugins.legend.labels.usePointStyle = true;
    Chart.defaults.maintainAspectRatio = false;
  }

  function init() {
    injectFigStyles();
    initMermaid();
    initKatex();
    initHighlight();
    chartTheme('light');
    saveMermaidSrc();
    // 若页面初始即为暗色(nav.js 已设置 data-theme),对齐图表与图
    if (document.documentElement.getAttribute('data-theme') === 'dark') {
      chartTheme('dark');
      reThemeMermaid('dark');
    }
    // 首次渲染统一走 run()
    try {
      if (typeof mermaid !== 'undefined') mermaid.run({ nodes: document.querySelectorAll('.mermaid') });
    } catch (e) { /* noop */ }
    initFigureZoom();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

  /* 供页面自定义图表使用的配色 */
  window.CB_COLORS = {
    blue: '#378add', blueSoft: '#e6f1fb',
    amber: '#ef9f27', amberSoft: '#faeeda',
    green: '#639922', greenSoft: '#eaf3de',
    red: '#e24b4a', redSoft: '#fcebeb',
    purple: '#7f77dd', purpleSoft: '#eeedfe',
    teal: '#1d9e75', tealSoft: '#e1f5ee',
    gray: '#888780', graySoft: '#f1efe8'
  };

  /* 页面可把自建图表实例推入此数组,主题切换时统一重着色 */
  window.CB_CHARTS = window.CB_CHARTS || [];

  function recolorCharts(theme) {
    var dark = theme === 'dark';
    var tick = dark ? '#7c828e' : '#858c9a';
    var grid = dark ? '#2a2f38' : '#e3e6ec';
    window.CB_CHARTS.forEach(function (ch) {
      if (!ch || !ch.options) return;
      var o = ch.options;
      if (o.scales) {
        ['x', 'y'].forEach(function (ax) {
          if (o.scales[ax]) {
            if (o.scales[ax].ticks) o.scales[ax].ticks.color = tick;
            if (o.scales[ax].title) o.scales[ax].title.color = tick;
            if (o.scales[ax].grid) o.scales[ax].grid.color = grid;
          }
        });
      }
      if (o.plugins && o.plugins.legend && o.plugins.legend.labels) o.plugins.legend.labels.color = dark ? '#b3b9c4' : '#4a5160';
      if (o.plugins && o.plugins.title) o.plugins.title.color = dark ? '#e8eaed' : '#1a1d24';
      try { ch.update(); } catch (e) {}
    });
  }

  /* 主题切换入口:重着色 Mermaid / Chart 并通知页面重绘自定义图表 */
  window.CB_SET_THEME = function (theme) {
    chartTheme(theme);
    reThemeMermaid(theme);
    recolorCharts(theme);
    window.dispatchEvent(new CustomEvent('cb-theme-change', { detail: { theme: theme } }));
  };
})();

/* ===========================================================
   render.js — Mermaid / KaTeX / highlight.js / Chart.js 初始化
   浏览器运行时依赖均为本地资源,按页面内容加载。
   提供 window.CB_SET_THEME(theme) 供主题切换时重新着色。

   v2.0 · 2026-08-07
   - Mermaid 升级至 11.x,统一精致配色 + 圆角节点 + 入场动画
   - 流程图布局参数优化(nodeSpacing / rankSpacing / padding)
   - 保留深浅主题切换与图表重着色能力
   =========================================================== */
(function () {
  'use strict';

  /* 这里的色值与 theme.css 的 --cat-* 槽位对齐（蓝 / 绿 / 琥珀），
     让 Mermaid 专项图和原生 HTML 图读起来是同一套系统。
     文字仍走各自的深色 ink，不用槽位色当正文色。
     lineColor / clusterBorder 与原生流程图的 --flow-line 同值，
     两类图并排出现时连线粗细与灰度一致。 */
  var LIGHT = {
    background: '#ffffff',
    primaryColor: '#eaf3fd', primaryTextColor: '#1a1d24', primaryBorderColor: '#2a78d6',
    lineColor: '#c3cbd6', lineColorHover: '#2a78d6',
    secondaryColor: '#fdf4e0', secondaryTextColor: '#1a1d24', secondaryBorderColor: '#eda100',
    tertiaryColor: '#e6f7f1', tertiaryTextColor: '#1a1d24', tertiaryBorderColor: '#1baf7a',
    noteBkgColor: '#f4f6f8', noteTextColor: '#4a5160', noteBorderColor: '#d0d5de',
    clusterBkg: '#f6f7f9', clusterBorder: '#d0d5de',
    titleColor: '#1a1d24',
    edgeLabelBackground: '#ffffff', fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif',
    fontSize: '15px'
  };
  var DARK = {
    background: '#181b21',
    primaryColor: '#16283c', primaryTextColor: '#e8eaed', primaryBorderColor: '#3987e5',
    lineColor: '#596575', lineColorHover: '#3987e5',
    secondaryColor: '#2c2411', secondaryTextColor: '#e8eaed', secondaryBorderColor: '#c98500',
    tertiaryColor: '#122d26', tertiaryTextColor: '#e8eaed', tertiaryBorderColor: '#199e70',
    noteBkgColor: '#1d2128', noteTextColor: '#b3b9c4', noteBorderColor: '#383f4a',
    clusterBkg: '#1e232b', clusterBorder: '#383f4a',
    titleColor: '#e8eaed',
    edgeLabelBackground: '#20242c', fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif',
    fontSize: '15px'
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
        curve: 'linear', padding: 18, nodeSpacing: 52, rankSpacing: 64,
        useMaxWidth: true, htmlLabels: true
      },
      sequence: { useMaxWidth: true, actorMargin: 60, messageMargin: 46, boxMargin: 12 },
      state: { useMaxWidth: true, radius: 8 },
      class: { useMaxWidth: true }
    };
  }

  /* 注入全局图表样式:圆角节点 + 入场动画 + 标签描边。
     圆角与 theme.css 的 --radius-sm(6px) / --radius(10px) 对齐，
     Mermaid 节点和原生 HTML 流程图节点因此是同一个弧度。 */
  function injectFigStyles() {
    var css =
      '@keyframes cbFigIn{from{opacity:0;transform:translateY(9px)}to{opacity:1;transform:none}}' +
      '.mermaid svg{animation:cbFigIn .55s cubic-bezier(.22,.61,.36,1) both}' +
      '@media (prefers-reduced-motion: reduce){.mermaid svg{animation:none}}' +
      '.mermaid svg .node rect,.mermaid svg .node circle,.mermaid svg .node polygon,.mermaid svg .node path' +
      '{shape-rendering:geometricPrecision;stroke-width:1.4px}' +
      '.mermaid svg .node rect{rx:6px}' +
      '.mermaid svg .label,.mermaid svg .nodeLabel{font-size:15px!important;font-weight:600;line-height:1.45}' +
      '.mermaid svg .edgeLabel{background:transparent!important;font-size:13px!important;font-weight:600}' +
      '.mermaid svg .messageText,.mermaid svg .loopText,.mermaid svg .state-note text{font-size:14px!important}' +
      '.mermaid svg .cluster rect{rx:10px}' +
      /* 连线加粗到 2px、圆头收尾，与原生 HTML 流程图的连接器保持同一手感 */
      '.mermaid svg .flowchart-link{stroke-width:2px;stroke-linecap:round}' +
      '.mermaid svg .messageLine0,.mermaid svg .messageLine1{stroke-width:1.8px}';
    var st = document.createElement('style');
    st.textContent = css;
    document.head.appendChild(st);
  }

  function initMermaid() {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize(mermaidCfg('light'));
  }

  /* 保存每个 Mermaid 节点的原始源码,供主题切换时重渲染 */
  var mermaidSources = [];
  /* 静态站点构建会把部分手写 HTML 压成一行。flowchart/timeline 可以
     容忍空白，但 sequenceDiagram 把换行当作语句边界；例如
     `autonumber participant` 会被 Mermaid 当作一条非法命令。只在这
     一类图上恢复命令边界，保持正文和其它 Mermaid 语法不受影响。 */
  function normalizeSequenceDiagram(source) {
    if (!/^\s*sequenceDiagram\b/.test(source)) return source;
    return source
      .replace(/^(\s*sequenceDiagram)\s+autonumber\s+/, '$1\nautonumber\n')
      .replace(/\s+(?=participant\s+\S+\s+as\s+)/g, '\n')
      .replace(/\s+(?=Note\s+(?:over|right of|left of)\s+)/g, '\n')
      .replace(/\s+(?=[A-Za-z0-9_]+\s*(?:-->>|->>|-->|->)\s*[A-Za-z0-9_]+)/g, '\n');
  }
  function saveMermaidSrc() {
    if (mermaidSources.length) return;
    document.querySelectorAll('.mermaid').forEach(function (n) {
      var source = normalizeSequenceDiagram(n.textContent);
      n.textContent = source;
      mermaidSources.push(source);
    });
  }

  function reThemeMermaid(theme) {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize(mermaidCfg(theme));
    var nodes = document.querySelectorAll('.mermaid');
    nodes.forEach(function (n, index) {
      if (mermaidSources[index] === undefined) return;
      var host = document.createElement('div');
      host.className = 'mermaid';
      host.textContent = mermaidSources[index];
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

  /* 图表和论文插图在正文中按列宽显示，点击后打开可缩放阅读层。 */
  function initFigureZoom() {
    /* 三类可放大的东西：Mermaid 容器、论文插图、烘焙出的流程图 SVG。
       点击委托与键盘激活都用这一份，免得加了一处漏了另一处。 */
    var ZOOM_SOURCE = '.mermaid, .image-figure img, .flow-figure .flow-svg, .classic-figure .classic-svg';
    document.querySelectorAll('.mermaid').forEach(function (node) {
      node.dataset.cbZoom = 'ready';
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.setAttribute('aria-label', '放大查看流程图');
    });
    /* 流程图 SVG 只加可聚焦，不动 role/aria。它烘焙时已经带了
       role="img" + aria-labelledby(图注) + aria-describedby(节点与连线全文)，
       改成 role="button" 会把这套读屏信息一起丢掉；而 aria-labelledby 在
       命名计算里本来就压过 aria-label，补一句「放大查看」也是空转。
       可放大的提示交给 fig-flow.css 的 cursor: zoom-in 与焦点环。 */
    document.querySelectorAll('.flow-figure .flow-svg').forEach(function (node) {
      node.dataset.cbZoom = 'ready';
      node.setAttribute('tabindex', '0');
    });
    /* 手绘 SVG 和流程图一样：保留 role="img" 的完整读屏描述，
       只给键盘焦点和放大手势，不把语义降级成普通按钮。 */
    document.querySelectorAll('.classic-figure .classic-svg').forEach(function (node) {
      node.dataset.cbZoom = 'ready';
      node.setAttribute('tabindex', '0');
    });
    document.querySelectorAll('.image-figure img').forEach(function (node) {
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.setAttribute('aria-label', '放大查看图片');
    });
    if (document.body.dataset.cbZoomBound) return;
    document.body.dataset.cbZoomBound = '1';
    document.addEventListener('click', function (event) {
      var source = event.target.closest(ZOOM_SOURCE);
      if (!source || event.target.closest('.cb-zoom-layer')) return;
      /* Mermaid 是容器要往里取 svg；插图和流程图 SVG 自己就是那张图。 */
      var visual = source.matches('img, svg') ? source : source.querySelector('svg');
      if (!visual) return;
      visual = visual.cloneNode(true);
      /* 副本别再当放大入口：留着 tabindex 会在弹层里多一个跳不出去的焦点点。 */
      visual.removeAttribute('tabindex');
      visual.removeAttribute('data-cb-zoom');
      var layer = document.createElement('div');
      layer.className = 'cb-zoom-layer';
      layer.setAttribute('role', 'dialog');
      layer.setAttribute('aria-modal', 'true');
      layer.setAttribute('aria-label', '图表放大视图');
      var panel = document.createElement('div');
      panel.className = 'cb-zoom-panel';
      var toolbar = document.createElement('div');
      toolbar.className = 'cb-zoom-toolbar';
      var caption = document.createElement('div');
      caption.className = 'cb-zoom-caption';
      caption.textContent = source.closest('figure')?.querySelector('figcaption')?.textContent?.trim() || '图表';
      var controls = document.createElement('div');
      controls.className = 'cb-zoom-controls';
      function tool(symbol, label) {
        var button = document.createElement('button');
        button.type = 'button';
        button.textContent = symbol;
        button.title = label;
        button.setAttribute('aria-label', label);
        controls.appendChild(button);
        return button;
      }
      var zoomOut = tool('−', '缩小');
      var zoomReset = tool('↺', '重置缩放');
      var zoomIn = tool('+', '放大');
      var status = document.createElement('output');
      status.className = 'cb-zoom-status';
      status.setAttribute('aria-live', 'polite');
      var close = document.createElement('button');
      close.className = 'cb-zoom-close';
      close.type = 'button';
      close.setAttribute('aria-label', '关闭放大视图');
      close.title = '关闭';
      close.textContent = '×';
      controls.appendChild(status);
      controls.appendChild(close);
      toolbar.appendChild(caption);
      toolbar.appendChild(controls);
      var viewport = document.createElement('div');
      viewport.className = 'cb-zoom-viewport';
      var stage = document.createElement('div');
      stage.className = 'cb-zoom-stage';
      stage.appendChild(visual);
      viewport.appendChild(stage);
      panel.appendChild(toolbar);
      panel.appendChild(viewport);
      layer.appendChild(panel);
      document.body.appendChild(layer);
      document.body.style.overflow = 'hidden';
      var naturalWidth = source.matches('img') ? (source.naturalWidth || source.clientWidth) : (visual.viewBox?.baseVal?.width || source.clientWidth);
      var naturalHeight = source.matches('img') ? (source.naturalHeight || source.clientHeight) : (visual.viewBox?.baseVal?.height || source.clientHeight);
      var scale = 1;
      function applyScale(next) {
        scale = Math.max(0.5, Math.min(3, next));
        visual.style.width = Math.round(naturalWidth * scale) + 'px';
        visual.style.height = Math.round(naturalHeight * scale) + 'px';
        visual.style.maxWidth = 'none';
        visual.style.maxHeight = 'none';
        status.value = Math.round(scale * 100) + '%';
        status.textContent = status.value;
      }
      function fitScale() {
        return Math.max(1, Math.min(1.35, 980 / Math.max(naturalWidth, 1)));
      }
      var fitted = fitScale();
      applyScale(fitted);
      /* loading="lazy" 的插图可能还没解码就被点开：那时 naturalWidth 是 0，
         退到 clientWidth 只剩占位框的十几像素，放大层会开出一张缩略图。
         副本解码完成后按真实尺寸重算——用户已经手调过缩放就只换尺寸不换倍率。 */
      if (visual.matches('img') && !visual.complete) {
        visual.addEventListener('load', function () {
          if (!visual.naturalWidth) return;
          var keepFit = scale === fitted;
          naturalWidth = visual.naturalWidth;
          naturalHeight = visual.naturalHeight;
          applyScale(keepFit ? fitScale() : scale);
        }, { once: true });
      }
      zoomOut.addEventListener('click', function () { applyScale(scale - 0.2); });
      zoomReset.addEventListener('click', function () { applyScale(1); });
      zoomIn.addEventListener('click', function () { applyScale(scale + 0.2); });
      function dismiss() {
        layer.remove();
        document.body.style.overflow = '';
        document.removeEventListener('keydown', onKey);
        if (source && typeof source.focus === 'function') source.focus();
      }
      function onKey(e) {
        if (e.key === 'Escape') dismiss();
        else if (e.key === '+' || e.key === '=') applyScale(scale + 0.2);
        else if (e.key === '-') applyScale(scale - 0.2);
        else if (e.key === '0') applyScale(1);
      }
      close.addEventListener('click', dismiss);
      layer.addEventListener('click', function (e) { if (e.target === layer) dismiss(); });
      document.addEventListener('keydown', onKey);
      close.focus();
    });
    document.addEventListener('keydown', function (event) {
      var node = document.activeElement;
      if ((event.key === 'Enter' || event.key === ' ') && node && node.matches(ZOOM_SOURCE)) {
        event.preventDefault();
        /* 不用 node.click()：click() 只定义在 HTMLElement 上，SVGElement 没有
           （它从 HTMLOrSVGElement 拿到的只有 focus/blur/dataset），
           对流程图 SVG 调用会抛 TypeError，键盘就再也打不开放大层。
           派发一个会冒泡的 click 事件，走的还是上面那个委托处理器。 */
        node.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
      }
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

  /**
   * 横滚容器只在真的溢出时才可聚焦。
   *
   * 烘焙期给 .flow-scroll 一律写死 tabindex="0"（JS 挂掉时也能用键盘滚），
   * 但 314 张带壳图里绝大多数在桌面宽度下根本不溢出，全留着就是 300 多个
   * 按 Tab 只会停一下、什么也做不了的空停留点，而每张图的 SVG 本身还要占一个
   * （放大入口）。所以这里按实测溢出量收回：不溢出就摘掉 tabindex 和 role，
   * 窗口尺寸变了再算一次。
   */
  function initFlowScroll() {
    var boxes = document.querySelectorAll('.flow-scroll');
    if (!boxes.length) return;
    function sync() {
      boxes.forEach(function (box) {
        var overflows = box.scrollWidth - box.clientWidth > 1;
        if (overflows) {
          box.setAttribute('tabindex', '0');
          box.setAttribute('role', 'region');
        } else {
          box.removeAttribute('tabindex');
          box.removeAttribute('role');
        }
      });
    }
    sync();
    var pending = false;
    window.addEventListener('resize', function () {
      if (pending) return;
      pending = true;
      requestAnimationFrame(function () { pending = false; sync(); });
    });
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
    initFlowScroll();
  }

  // The UMD bundle registers its load handler before this script. Disable
  // auto-start and capture source while the bottom-of-body markup is intact.
  // 引导放在文件末尾：页面里的自定义图表脚本紧跟在 render.js 之后执行，
  // 必须先备好 CB_COLORS / CB_CHARTS 再引导，否则暗色首屏会拿到浅色取值。
  /* 供页面自定义图表使用的配色。
     取值与 theme.css 的 --cat-* 槽位同源，两套主题各自选步（不是浅色值的明暗翻转），
     因此深浅模式下都通过了明度带、色度下限、色盲相邻可分辨与对比度校验。
     teal 归并到 green：原来两者几乎同色，留 key 只为兼容已有页面。 */
  var PALETTES = {
    light: {
      blue: '#2a78d6', blueSoft: '#eaf3fd',
      amber: '#eda100', amberSoft: '#fdf4e0',
      green: '#1baf7a', greenSoft: '#e6f7f1',
      red: '#e34948', redSoft: '#fdedec',
      purple: '#4a3aa7', purpleSoft: '#eeecfa',
      teal: '#1baf7a', tealSoft: '#e6f7f1',
      gray: '#5b6675', graySoft: '#f4f6f8'
    },
    dark: {
      blue: '#3987e5', blueSoft: '#16283c',
      amber: '#c98500', amberSoft: '#2c2411',
      green: '#199e70', greenSoft: '#122d26',
      red: '#e66767', redSoft: '#331d1d',
      purple: '#9085e9', purpleSoft: '#23203a',
      teal: '#199e70', tealSoft: '#122d26',
      gray: '#8c97a6', graySoft: '#1d2128'
    }
  };
  var paletteKeys = Object.keys(PALETTES.light);
  window.CB_COLORS = Object.assign({}, PALETTES.light);

  /* 主题切换时，已建好的 Chart 实例里的 dataset 颜色不会自动更新。
     这里按「旧主题的哪个 key」反查，再换成新主题同一个 key 的取值，
     所以颜色仍然跟着同一个数据系列，不会因为换主题而重排。 */
  function swapSeriesColors(from, to) {
    var lookup = {};
    paletteKeys.forEach(function (key) { lookup[PALETTES[from][key].toLowerCase()] = PALETTES[to][key]; });
    function mapped(value) {
      if (typeof value === 'string') return lookup[value.toLowerCase()] || value;
      if (Array.isArray(value)) return value.map(mapped);
      return value;
    }
    window.CB_CHARTS.forEach(function (ch) {
      if (!ch || !ch.data || !ch.data.datasets) return;
      ch.data.datasets.forEach(function (ds) {
        ['backgroundColor', 'borderColor', 'pointBackgroundColor', 'pointBorderColor', 'hoverBackgroundColor', 'hoverBorderColor'].forEach(function (prop) {
          if (ds[prop] !== undefined) ds[prop] = mapped(ds[prop]);
        });
      });
    });
  }

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
  var currentTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
  if (currentTheme === 'dark') window.CB_COLORS = Object.assign(window.CB_COLORS, PALETTES.dark);

  window.CB_SET_THEME = function (theme) {
    var next = theme === 'dark' ? 'dark' : 'light';
    if (next !== currentTheme) {
      swapSeriesColors(currentTheme, next);
      Object.assign(window.CB_COLORS, PALETTES[next]);
      currentTheme = next;
    }
    chartTheme(theme);
    reThemeMermaid(theme);
    recolorCharts(theme);
    window.dispatchEvent(new CustomEvent('cb-theme-change', { detail: { theme: theme } }));
  };

  initMermaid();
  saveMermaidSrc();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();

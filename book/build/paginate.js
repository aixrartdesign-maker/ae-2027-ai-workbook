(function () {
  'use strict';
  var MM = 96 / 25.4;
  var PAGE_H = 220 * MM;
  var MIN_SHRINK = 0.70;
  var MAX_GROW = 1.45;
  var stats = { splits: 0, shrinks: 0, defers: 0, grown: 0 };

  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function px(v) { return parseFloat(v) || 0; }

  // ---------- normalization ----------
  function isBlockEl(n) {
    if (n.nodeType !== 1) return false;
    var t = n.tagName;
    return t === 'DIV' || t === 'UL' || t === 'OL' || t === 'TABLE' || t === 'P' || t === 'FIGURE';
  }
  function wrapAnon(box) {
    var kids = Array.prototype.slice.call(box.childNodes);
    var hasBlock = kids.some(isBlockEl);
    if (!hasBlock) return;
    var run = null;
    kids.forEach(function (n) {
      if (isBlockEl(n)) { run = null; return; }
      if (n.nodeType === 3 && !n.textContent.trim() && !run) return;
      if (!run) { run = document.createElement('div'); run.className = 'anon'; box.insertBefore(run, n); }
      run.appendChild(n);
    });
  }
  function normalize() {
    $$('.layer3, .role, .howto').forEach(wrapAnon);
    $$('.sc-grid').forEach(function (g) {
      var kids = $$(':scope > .sc', g);
      if (kids.length <= 2) return;
      var parent = g.parentNode;
      for (var i = 0; i < kids.length; i += 2) {
        var row = document.createElement('div'); row.className = 'sc-grid';
        row.appendChild(kids[i]); if (kids[i + 1]) row.appendChild(kids[i + 1]);
        parent.insertBefore(row, g);
      }
      parent.removeChild(g);
    });
  }

  // ---------- item collection ----------
  function kindOf(el) {
    if (el.matches('figure.shot, .pair')) return 'fig';
    if (el.matches('h2, h3, .ch-no, h1.ch, .part')) return 'head';
    return 'block';
  }
  function collect() {
    var items = [];
    var part = '', chap = '';
    Array.prototype.slice.call(document.body.children).forEach(function (sec) {
      if (sec.tagName !== 'SECTION' || sec.classList.contains('cover')) return;
      var brk = sec.dataset.break === '1';
      var fill = sec.dataset.fill === '1';
      if (sec.classList.contains('part')) {
        var d = document.createElement('div'); d.className = 'part'; d.id = sec.id;
        while (sec.firstChild) d.appendChild(sec.firstChild);
        part = d.querySelector('.no').textContent.trim() + ' · ' + d.querySelector('h1').textContent.trim();
        items.push({ el: d, brk: brk, kind: 'head', part: part, chap: '', chapStart: true });
        sec.parentNode.removeChild(sec);
        return;
      }
      var kids = Array.prototype.slice.call(sec.children);
      var h = sec.querySelector('h1.ch'), no = sec.querySelector('.ch-no');
      var title = h ? h.childNodes[0].textContent.trim() : '';
      chap = (no ? no.textContent.trim() + '   ' : '') + title.split(' — ')[0];
      if (kids.length) kids[0].classList.add('chap-start');
      kids.forEach(function (k, i) {
        items.push({ el: k, brk: brk && i === 0, kind: kindOf(k), part: part, chap: chap, chapStart: i === 0, fillEnd: fill && i === kids.length - 1 });
      });
      sec.parentNode.removeChild(sec);
    });
    items.forEach(function (it, i) { it.idx = i; });
    return items;
  }

  // ---------- pages ----------
  var pages = [];
  function newPage() {
    var pg = document.createElement('div'); pg.className = 'pg';
    pg.innerHTML = '<div class="pg-head"><span class="hl"></span><span class="hr"></span></div><div class="pg-body"></div><div class="pg-foot"></div>';
    var anchor = document.getElementById('colophon') || document.getElementById('backcover');
    document.body.insertBefore(pg, anchor);
    var P = { pg: pg, body: pg.querySelector('.pg-body'), items: [], deferred: 0 };
    pages.push(P);
    return P;
  }
  function used(P) {
    var last = P.body.lastElementChild; if (!last) return 0;
    return last.getBoundingClientRect().bottom - P.body.getBoundingClientRect().top;
  }
  function fits(P) { return used(P) <= PAGE_H + 0.6; }

  // ---------- figure sizing ----------
  function mediaOf(fig) { return $$('img, svg.dia', fig); }
  function aspect(m) {
    if (m.tagName === 'IMG') return m.naturalWidth / m.naturalHeight;
    var vb = m.viewBox.baseVal; return vb.width / vb.height;
  }
  function availW(m) {
    var f = m.closest('figure'); var cs = getComputedStyle(f);
    var pad = px(cs.paddingLeft) + px(cs.paddingRight) + px(cs.borderLeftWidth) + px(cs.borderRightWidth);
    var pr = f.parentNode;
    if (pr.classList.contains('pair')) {
      var n = pr.children.length, gap = px(getComputedStyle(pr).columnGap) || 4 * MM;
      return (pr.clientWidth - gap * (n - 1)) / n - pad - 1;
    }
    return f.clientWidth - px(cs.paddingLeft) - px(cs.paddingRight);
  }
  function baseMaxH(m) {
    var f = m.closest('figure');
    if (m.tagName !== 'IMG') return 1e6;
    if (f.parentNode.classList.contains('pair')) return 60 * MM;
    if (f.classList.contains('half')) return 54 * MM;
    if (f.classList.contains('wide')) return 112 * MM;
    return 84 * MM;
  }
  function setH(m, h) {
    var a = aspect(m), W = availW(m);
    var w = Math.min(W, h * a); h = w / a;
    m.style.width = w + 'px'; m.style.height = h + 'px';
    m._h = h;
  }
  function sizeFig(fig) {
    mediaOf(fig).forEach(function (m) {
      if (m._h) return;
      var a = aspect(m), W = availW(m);
      var h = Math.min(baseMaxH(m), W / a);
      if (m.tagName === 'IMG') h = Math.min(h, m.naturalHeight * 1.2);
      setH(m, h); m._base = m._h;
    });
  }
  function shrinkFig(P, fig) {
    var over = used(P) - PAGE_H; if (over <= 0) return true;
    var ms = mediaOf(fig); if (!ms.length) return false;
    var old = ms.map(function (m) { return m._h; });
    var pair = fig.classList.contains('pair');
    var tot = pair ? Math.max.apply(null, old) : old.reduce(function (a, b) { return a + b; }, 0);
    var want = tot - over - 1.5;
    if (want < tot * MIN_SHRINK || want < 24 * MM) return false;
    var r = want / tot;
    ms.forEach(function (m, i) { setH(m, old[i] * r); });
    if (!fits(P)) {
      ms.forEach(function (m, i) { setH(m, old[i] * r - 8); });
      if (!fits(P) || (old[0] * r - 8) < tot * MIN_SHRINK * 0.98) { ms.forEach(function (m, i) { setH(m, old[i]); }); return false; }
    }
    stats.shrinks++;
    return true;
  }
  function growFigs(P, left) {
    var ms = [];
    $$('figure.shot', P.body).forEach(function (f) {
      if (f.parentNode.classList.contains('pair')) return;
      mediaOf(f).forEach(function (m) {
        var a = aspect(m), W = availW(m);
        var cap = Math.min(W / a, m._h * MAX_GROW, 125 * MM);
        if (m.tagName === 'IMG') cap = Math.min(cap, m.naturalHeight * 1.25);
        if (cap - m._h > 1) ms.push({ m: m, room: cap - m._h });
      });
    });
    if (!ms.length) return;
    var total = ms.reduce(function (a, b) { return a + b.room; }, 0);
    var g = Math.min(left - 0.8, total); if (g <= 0.5) return;
    ms.forEach(function (o) { setH(o.m, o.m._h + o.room * g / total); });
    var guard = 0;
    while (!fits(P) && guard++ < 6) { ms.forEach(function (o) { setH(o.m, o.m._h - 2); }); }
    stats.grown++;
  }

  // ---------- tighten: free a little room for an unbreakable block ----------
  function setGap(el, prev, target) {
    var mb = px(getComputedStyle(prev).marginBottom);
    el.style.marginTop = (target >= mb ? target : target - mb) + 'px';
  }
  function tighten(P, over, okFn) {
    okFn = okFn || function () { return fits(P); };
    if (over > 15 * MM) return false;
    var kids = Array.prototype.slice.call(P.body.children);
    var ms = [];
    $$('figure.shot', P.body).forEach(function (f) {
      mediaOf(f).forEach(function (m) { var room = m._h - (m._base || m._h) * 0.86; if (room > 1) ms.push({ m: m, room: room, h: m._h }); });
    });
    var gaps = [];
    for (var i = 1; i < kids.length; i++) {
      var g = kids[i].getBoundingClientRect().top - kids[i - 1].getBoundingClientRect().bottom;
      if (g > 2.4 * MM) gaps.push({ el: kids[i], prev: kids[i - 1], g: g, room: g * 0.2, old: kids[i].style.marginTop });
    }
    var total = ms.reduce(function (a, b) { return a + b.room; }, 0) + gaps.reduce(function (a, b) { return a + b.room; }, 0);
    if (total < over + 1.5) return false;
    var f = (over + 1.5) / total;
    for (var t = 0; t < 4; t++) {
      ms.forEach(function (o) { setH(o.m, o.h - o.room * f); });
      gaps.forEach(function (o) { setGap(o.el, o.prev, o.g - o.room * f); });
      if (okFn()) { stats.tight = (stats.tight || 0) + 1; return true; }
      f = Math.min(1, f * 1.15);
    }
    ms.forEach(function (o) { setH(o.m, o.h); });
    gaps.forEach(function (o) { o.el.style.marginTop = o.old; });
    return false;
  }

  // ---------- splitting ----------
  function lineHeightOf(el) {
    var cs = getComputedStyle(el); var lh = parseFloat(cs.lineHeight);
    if (isNaN(lh)) lh = parseFloat(cs.fontSize) * 1.5;
    return lh;
  }
  function linesOf(el) {
    var lh = lineHeightOf(el);
    var r = document.createRange(); r.selectNodeContents(el);
    var rs = Array.prototype.slice.call(r.getClientRects()).filter(function (q) { return q.width > 0.5 && q.height > 2 && q.height < lh * 2.2; });
    var cs = rs.map(function (q) { return (q.top + q.bottom) / 2; }).sort(function (a, b) { return a - b; });
    var lines = [];
    cs.forEach(function (c) {
      var L = lines[lines.length - 1];
      if (L && c - L.c < lh * 0.5) { L.n++; L.c = L.c + (c - L.c) / L.n; }
      else lines.push({ c: c, n: 1 });
    });
    return { lines: lines, lh: lh };
  }
  function charCenter(node, o) {
    var r = document.createRange();
    var len = node.textContent.length;
    for (var k = o; k < len; k++) {
      r.setStart(node, k); r.setEnd(node, k + 1);
      var q = r.getClientRects();
      for (var j = 0; j < q.length; j++) { if (q[j].width > 0.2 && q[j].height > 2) return (q[j].top + q[j].bottom) / 2; }
    }
    return Infinity;
  }
  function cutAtLine(el, boundaryY) {
    var tw = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
    var node, found = null, off = 0;
    while ((node = tw.nextNode())) {
      var len = node.textContent.length; if (!len) continue;
      var rr = document.createRange(); rr.selectNodeContents(node);
      var q = Array.prototype.slice.call(rr.getClientRects()).filter(function (x) { return x.width > 0.2 && x.height > 2; });
      if (!q.length) continue;
      var lastC = (q[q.length - 1].top + q[q.length - 1].bottom) / 2;
      if (lastC < boundaryY) continue;
      var lo = 0, hi = len - 1;
      if (charCenter(node, 0) >= boundaryY) { found = node; off = 0; break; }
      while (hi - lo > 1) { var mid = (lo + hi) >> 1; if (charCenter(node, mid) >= boundaryY) hi = mid; else lo = mid; }
      found = node; off = hi; break;
    }
    if (!found) return null;
    var range = document.createRange();
    range.setStart(found, off); range.setEndAfter(el.lastChild);
    var frag = range.extractContents();
    var rest = el.cloneNode(false); rest.removeAttribute('id');
    rest.appendChild(frag);
    var f = rest.firstChild;
    while (f && f.nodeType === 3 && !f.textContent.trim()) { rest.removeChild(f); f = rest.firstChild; }
    if (f && f.nodeType === 3) f.textContent = f.textContent.replace(/^\s+/, '');
    if (!rest.textContent.trim()) return null;
    return rest;
  }
  function splitInline(el, limit, isFit) {
    var cs = getComputedStyle(el);
    var maxB = limit - px(cs.paddingBottom) - px(cs.borderBottomWidth);
    var hasTitle = el.firstElementChild && el.firstElementChild.tagName === 'B' && getComputedStyle(el.firstElementChild).display === 'block';
    var minHead = hasTitle ? 3 : 2, minTail = 2;
    if (el.classList.contains('prompt')) { minHead = 2; minTail = 1; }
    var info = linesOf(el), L = info.lines, lh = info.lh;
    if (L.length < minHead + minTail) return null;
    var k = 0; while (k < L.length && L[k].c + lh / 2 <= maxB + 0.5) k++;
    k = Math.min(k, L.length - minTail);
    for (var t = 0; t < 3; t++) {
      if (k < minHead) return null;
      var backup = el.innerHTML;
      var rest = cutAtLine(el, (L[k - 1].c + L[k].c) / 2);
      if (rest && isFit()) { el.classList.add('sp-a'); rest.classList.add('sp-b'); return rest; }
      el.innerHTML = backup;
      k--;
    }
    return null;
  }
  function splitList(el, limit, isFit) {
    var lis = Array.prototype.slice.call(el.children);
    var n = 0; while (n < lis.length && lis[n].getBoundingClientRect().bottom <= limit + 0.5) n++;
    if (n >= lis.length) n = lis.length - 1;
    var rest = el.cloneNode(false); rest.removeAttribute('id');
    for (var i = n; i < lis.length; i++) rest.appendChild(lis[i]);
    // try to split the straddling li
    var first = rest.firstElementChild, piece = null;
    if (first) {
      el.appendChild(first);
      if (!first.querySelector('ul,ol,table,div')) piece = splitInline(first, limit, isFit);
      if (piece) { piece.classList.add('li-cont'); rest.insertBefore(piece, rest.firstChild); n++; }
      else rest.insertBefore(first, rest.firstChild);
    }
    if (n < 1) { while (rest.firstChild) el.appendChild(rest.firstChild); return null; }
    if (el.tagName === 'OL') rest.setAttribute('start', (parseInt(el.getAttribute('start') || '1', 10)) + n - (piece ? 1 : 0));
    el.classList.add('sp-a'); rest.classList.add('sp-b');
    return rest;
  }
  function splitTable(el, limit, isFit) {
    var rows = Array.prototype.slice.call(el.rows);
    var hasHead = rows.length && rows[0].querySelector('th');
    var sct = el.classList.contains('sct');
    var bodyCount = rows.length - (hasHead ? 1 : 0);
    if (bodyCount < 2) return null;
    var n = 0; while (n < rows.length && rows[n].getBoundingClientRect().bottom <= limit + 0.5) n++;
    if (rows.length - n < 1) n = rows.length - 1;
    if (rows.length - n === 1 && n - (hasHead ? 1 : 0) >= 3) n--;
    while (sct && n > 0 && rows[n - 1].classList.contains('cat')) n--;
    var nb = n - (hasHead ? 1 : 0);
    if (nb < 1) return null;
    var headRow = hasHead ? rows[0] : null;
    if (sct) { for (var q = n - 1; q >= 0; q--) { if (rows[q].classList.contains('cat')) { headRow = rows[q]; break; } } if (rows[n].classList.contains('cat')) headRow = null; }
    var rest = el.cloneNode(false); rest.removeAttribute('id');
    var cg = el.querySelector('colgroup'); if (cg) rest.appendChild(cg.cloneNode(true));
    var tb = document.createElement('tbody');
    if (headRow) tb.appendChild(headRow.cloneNode(true));
    for (var i = n; i < rows.length; i++) tb.appendChild(rows[i]);
    rest.appendChild(tb);
    el.classList.add('sp-a'); rest.classList.add('sp-b');
    return rest;
  }
  function isInlineBox(el) {
    if (el.tagName === 'P' || el.classList.contains('anon') || el.tagName === 'LI') return true;
    if (!el.matches('.why, .tip, .note, .warn, .prompt, .howto, .ok, .stuck')) return false;
    return !Array.prototype.some.call(el.children, function (c) { return isBlockEl(c); });
  }
  function splitBlocks(el, limit, isFit) {
    var cs = getComputedStyle(el);
    var maxB = limit - px(cs.paddingBottom) - px(cs.borderBottomWidth);
    var kids = Array.prototype.slice.call(el.children);
    var j = 0; while (j < kids.length && kids[j].getBoundingClientRect().bottom <= maxB + 0.5) j++;
    if (j >= kids.length) return null;
    var childRest = splitAny(kids[j], maxB, isFit, true);
    var isHeader = function (c) { return c.matches('.lh, .rh, .lbl, .sh'); };
    if (!childRest && (j === 0 || (j === 1 && isHeader(kids[0])))) return null;
    var rest = el.cloneNode(false); rest.removeAttribute('id');
    if (childRest) { rest.appendChild(childRest); j++; }
    for (var i = j; i < kids.length; i++) rest.appendChild(kids[i]);
    if (!rest.firstChild) return null;
    el.classList.add('sp-a'); rest.classList.add('sp-b');
    return rest;
  }
  function splitAny(el, limit, isFit, nested) {
    var h = el.getBoundingClientRect().height;
    if (el.tagName === 'TABLE') return splitTable(el, limit, isFit);
    if (el.tagName === 'UL' || el.tagName === 'OL') return splitList(el, limit, isFit);
    if (el.matches('figure, .pair, .step, .cols3, .sc-grid, .toc2, .mission, h1, h2, h3, .ch-no, .part, .lead, .src')) return null;
    if (isInlineBox(el)) {
      if (el.tagName !== 'P' && !nested && h < (el.classList.contains('prompt') ? 14 : 25) * MM) return null;
      return splitInline(el, limit, isFit);
    }
    if (el.matches('.layer3, .role, .howto, .why, .tip, .note, .warn')) {
      if (!nested && h < 22 * MM) return null;
      return splitBlocks(el, limit, isFit);
    }
    return null;
  }

  // ---------- justification ----------
  function gapWeight(prev, cur) {
    if (prev.matches('h1, h2, h3, .ch-no')) return 0.15;
    if (cur.matches('.ch-no.chap-start, .part')) return 4;
    if (cur.matches('h2')) return 3;
    if (cur.matches('figure, .pair, table, .cols3') || prev.matches('figure, .pair, table, .cols3')) return 1.6;
    if (cur.matches('.step') && prev.matches('.step')) return 0.7;
    return 1;
  }
  function absorbGaps(P, cap) {
    var kids = Array.prototype.slice.call(P.body.children);
    var left = PAGE_H - used(P);
    if (left <= 1 || kids.length < 2) return;
    var gaps = [];
    for (var i = 1; i < kids.length; i++) {
      var g = kids[i].getBoundingClientRect().top - kids[i - 1].getBoundingClientRect().bottom;
      gaps.push({ el: kids[i], prev: kids[i - 1], g: g, w: gapWeight(kids[i - 1], kids[i]), old: kids[i].style.marginTop });
    }
    var W = gaps.reduce(function (a, b) { return a + b.w; }, 0);
    var unit = Math.min((left - 0.5) / W, cap);
    var guard = 0;
    do {
      gaps.forEach(function (o) { setGap(o.el, o.prev, o.g + unit * o.w); });
      if (fits(P)) return;
      unit = unit * 0.92 - 0.05;
    } while (unit > 0 && guard++ < 40);
    gaps.forEach(function (o) { o.el.style.marginTop = o.old; });
  }
  function absorbInner(P, capA, capB, capC, capD) {
    var left = PAGE_H - used(P);
    if (left <= 1.2) return;
    var trs = $$('table:not(.sct) tr', P.body).filter(function (r) { return !r.querySelector('th'); });
    var trs2 = $$('table.sct tr', P.body).filter(function (r) { return !r.classList.contains('cat'); });
    var lis = $$('li', P.body), stp = $$('.step', P.body);
    var room = trs.length * capA + trs2.length * capB + lis.length * capC + stp.length * capD;
    if (room <= 0) return;
    var f = Math.min(1, (left - 0.6) / room);
    var hs = trs.map(function (r) { return r.getBoundingClientRect().height; }), hs2 = trs2.map(function (r) { return r.getBoundingClientRect().height; });
    var lb = lis.map(function (l) { return px(getComputedStyle(l).marginBottom); }), sb = stp.map(function (l) { return px(getComputedStyle(l).marginBottom); });
    var guard = 0;
    do {
      trs.forEach(function (r, i) { r.style.height = (hs[i] + capA * f) + 'px'; });
      trs2.forEach(function (r, i) { r.style.height = (hs2[i] + capB * f) + 'px'; });
      lis.forEach(function (l, i) { l.style.marginBottom = (lb[i] + capC * f) + 'px'; });
      stp.forEach(function (l, i) { l.style.marginBottom = (sb[i] + capD * f) + 'px'; });
      if (fits(P)) return;
      f = f * 0.9 - 0.01;
    } while (f > 0 && guard++ < 40);
    trs.forEach(function (r, i) { r.style.height = hs[i] + 'px'; }); trs2.forEach(function (r, i) { r.style.height = hs2[i] + 'px'; });
    lis.forEach(function (l, i) { l.style.marginBottom = lb[i] + 'px'; }); stp.forEach(function (l, i) { l.style.marginBottom = sb[i] + 'px'; });
  }
  function absorbBoxes(P, cap) {
    var left = PAGE_H - used(P);
    if (left <= 1.2) return;
    var bx = $$('.prompt, .tip, .note, .warn, .why, .layer3, .ok, .stuck, .mission, .howto', P.body).filter(function (b) { return !b.parentNode.closest('.prompt, .tip, .note, .warn, .why, .layer3, .howto'); });
    if (!bx.length) return;
    var pt = bx.map(function (b) { return px(getComputedStyle(b).paddingTop); }), pb = bx.map(function (b) { return px(getComputedStyle(b).paddingBottom); });
    var f = Math.min(1, (left - 0.6) / (bx.length * cap * 2));
    var guard = 0;
    do {
      bx.forEach(function (b, i) { b.style.paddingTop = (pt[i] + cap * f) + 'px'; b.style.paddingBottom = (pb[i] + cap * f) + 'px'; });
      if (fits(P)) return;
      f = f * 0.9 - 0.01;
    } while (f > 0 && guard++ < 40);
    bx.forEach(function (b, i) { b.style.paddingTop = pt[i] + 'px'; b.style.paddingBottom = pb[i] + 'px'; });
  }
  function finalize(P, forced) {
    var kids = Array.prototype.slice.call(P.body.children);
    if (!kids.length) return;
    var left = PAGE_H - used(P);
    if (left > 1.5) { growFigs(P, left); left = PAGE_H - used(P); }
    var st = P.body.querySelector('[data-stretch]');
    if (st && left > 1) { st.style.height = (st.getBoundingClientRect().height + left - 0.5) + 'px'; left = PAGE_H - used(P); }
    P.rawLeft = left;
    if (!P.last) {
      absorbGaps(P, (forced ? 6 : 2.6) * MM);
      absorbInner(P, (forced ? 2.6 : 1.6) * MM, 0.6 * MM, 0.8 * MM, 1.0 * MM);
      if (PAGE_H - used(P) > 2.5 * MM) absorbBoxes(P, 1.3 * MM);
      if (PAGE_H - used(P) > 4 * MM) {
        absorbGaps(P, (forced ? 4 : 1.8) * MM);
        absorbInner(P, 1.2 * MM, 0.5 * MM, 0.6 * MM, 0.8 * MM);
      }
    }
    P.left = PAGE_H - used(P);
  }

  // ---------- main ----------
  function run() {
    normalize();
    var queue = collect();
    var P = newPage();
    var carry = [];
    function desc(it) { if (!it) return '-'; var e = it.el; return e.tagName.toLowerCase() + (e.className ? '.' + String(e.className).split(' ').slice(0, 2).join('.') : '') + ':' + (e.textContent || '').trim().slice(0, 14); }
    function closePage(forced, why) {
      P.dbg = { why: why || '', next: desc(queue[0]), next2: desc(queue[1]), carry: carry.map(desc), items: P.items.map(function (x) { return desc(x).split(':')[0]; }) };
      // keep-with-next: pull trailing heads
      var pulled = [];
      while (P.items.length > 1 && P.items[P.items.length - 1].kind === 'head') {
        var lastIt = P.items[P.items.length - 1];
        if (lastIt.el.classList.contains('part')) {
          var prevEl = P.items[P.items.length - 2].el;
          var leftIfPulled = PAGE_H - (prevEl.getBoundingClientRect().bottom - P.body.getBoundingClientRect().top);
          if (leftIfPulled > 20 * MM) { lastIt.el.classList.add('part-end'); break; }
        }
        var it = P.items.pop(); P.body.removeChild(it.el); pulled.unshift(it);
      }
      finalize(P, forced);
      var back = carry.concat(pulled).sort(function (a, b) { return a.idx - b.idx; });
      carry = [];
      if (queue.length && queue[0].cont) { var c0 = queue.shift(); queue = [c0].concat(back, queue); }
      else queue = back.concat(queue);
      P = newPage();
    }
    var guard = 0;
    while ((queue.length || carry.length) && guard++ < 20000) {
      if (!queue.length) { closePage(false); continue; }
      var it = queue.shift();
      if (it.brk && (P.items.length || carry.length)) { queue.unshift(it); closePage(carry.length === 0); continue; }
      it.brk = false;
      if (carry.length >= 3 && it.el.matches && it.el.matches('h2') && P.items.length) { queue.unshift(it); closePage(false, 'h2-after-deferred'); continue; }
      P.body.appendChild(it.el);
      if (it.kind === 'fig') (it.el.matches('figure.shot') ? [it.el] : $$('figure.shot', it.el)).forEach(sizeFig);
      if (fits(P)) {
        if (it.kind === 'fig' && P.deferred > 0) {
          // keep figure order: once a figure is deferred, later ones wait too
          P.body.removeChild(it.el);
          if (P.deferred >= 4) { queue.unshift(it); closePage(false, 'fig-after-4-deferred'); continue; }
          carry.push(it); P.deferred++; stats.defers++; continue;
        }
        P.items.push(it);
        continue;
      }
      // overflow
      if (it.kind === 'fig') {
        if (P.deferred === 0 && shrinkFig(P, it.el)) { P.items.push(it); continue; }
        P.body.removeChild(it.el);
        var nxt = queue[0];
        var boundary = !nxt || nxt.chapStart || nxt.brk;
        if (P.items.length === 0) { // cannot fit even on empty page: force
          P.body.appendChild(it.el); mediaOf(it.el).forEach(function (m) { setH(m, m._h * 0.8); }); P.items.push(it); continue;
        }
        if (!boundary && P.deferred < 4) { carry.push(it); P.deferred++; stats.defers++; continue; }
        queue.unshift(it); closePage(false, 'fig-nofit boundary=' + boundary + ' def=' + P.deferred); continue;
      }
      var limit = P.body.getBoundingClientRect().top + PAGE_H;
      var rest = null;
      if (it.kind === 'block') {
        var backup = it.el.cloneNode(true);
        rest = splitAny(it.el, limit, function () { return fits(P); }, false);
        if (!rest && P.items.length) {
          // free a few mm so that the smallest acceptable head (first row / first item / two lines) fits
          P.body.replaceChild(backup, it.el); it.el = backup; backup = it.el.cloneNode(true);
          var target = null, e0 = it.el;
          if (e0.tagName === 'TABLE' && e0.rows.length >= 3) target = e0.rows[e0.rows[0].querySelector('th') ? 1 : 0];
          else if ((e0.tagName === 'UL' || e0.tagName === 'OL') && e0.children.length >= 2) target = e0.children[0];
          if (target) {
            var need = target.getBoundingClientRect().bottom - limit + 1;
            var okT = function () { return target.getBoundingClientRect().bottom <= limit + 0.3; };
            if (need > 0 && need < 13 * MM && tighten(P, need, okT)) rest = splitAny(it.el, limit, function () { return fits(P); }, false);
          } else if (e0.tagName === 'P' && !e0.classList.contains('lead') && !e0.classList.contains('src')) {
            var li0 = linesOf(e0);
            if (li0.lines.length >= 4) {
              var need2 = li0.lines[1].c + li0.lh / 2 - limit + 1;
              var okP = function () { var q = linesOf(e0); return q.lines[1].c + q.lh / 2 <= limit + 0.3; };
              if (need2 > 0 && need2 < 13 * MM && tighten(P, need2, okP)) rest = splitAny(it.el, limit, function () { return fits(P); }, false);
            }
          }
        }
        if (rest && !fits(P)) rest = null;
        if (!rest) { P.body.replaceChild(backup, it.el); it.el = backup; }
      }
      if (rest) {
        stats.splits++;
        P.items.push(it);
        queue.unshift({ el: rest, kind: 'block', part: it.part, chap: it.chap, idx: it.idx + 0.5, cont: true });
        closePage(false, 'split'); continue;
      }
      if (P.items.length && tighten(P, used(P) - PAGE_H)) { P.items.push(it); continue; }
      P.body.removeChild(it.el);
      if (P.items.length === 0) { P.body.appendChild(it.el); P.items.push(it); continue; }
      queue.unshift(it); closePage(false, 'block-nofit');
    }
    // last page
    if (!P.items.length && pages.length > 1) { P.pg.parentNode.removeChild(P.pg); pages.pop(); P = pages[pages.length - 1]; }
    else { P.last = true; finalize(P, false); }
    P.last = true;

    // colophon
    var colo = document.getElementById('colophon');
    if (colo) {
      var lastP = pages[pages.length - 1];
      lastP.body.appendChild(colo);
      var ch = colo.getBoundingClientRect().height;
      var kidsBottom = 0;
      Array.prototype.slice.call(lastP.body.children).forEach(function (c) { if (c !== colo) kidsBottom = Math.max(kidsBottom, c.getBoundingClientRect().bottom - lastP.body.getBoundingClientRect().top); });
      if (kidsBottom + ch + 10 * MM > PAGE_H) { var NP = newPage(); NP.items.push({ part: lastP.items[0].part, chap: lastP.items[0].chap }); NP.body.appendChild(colo); NP.last = true; NP.left = 0; }
    }

    // pad interior to a multiple of 8 with MEMO pages, kept before the final (colophon) page
    var need = (8 - pages.length % 8) % 8;
    var lastPg = pages[pages.length - 1];
    for (var mi = 0; mi < need; mi++) {
      var mp = document.createElement('div'); mp.className = 'pg memo';
      mp.innerHTML = '<div class="pg-head"><span class="hl"></span><span class="hr"></span></div><div class="pg-body"><div class="memo-h">MEMO</div><div class="memo-lines"></div></div><div class="pg-foot"></div>';
      document.body.insertBefore(mp, document.getElementById('backcover'));
      pages.push({ pg: mp, body: mp.querySelector('.pg-body'), items: [{ part: '', chap: '' }] });
    }
    // running heads + page numbers (cover = page 1)
    var title = '애프터이펙트 2027 완전 실습';
    pages.forEach(function (Pg, i) {
      var no = i + 2;
      Pg.no = no;
      var f = Pg.items[0] || {};
      Pg.pg.querySelector('.hl').textContent = f.part || title;
      Pg.pg.querySelector('.hr').textContent = (f.chap || '').replace(/\s{2,}/g, '  ');
      Pg.pg.querySelector('.pg-foot').textContent = no;
      Pg.pg.dataset.no = no;
    });
    // TOC numbers
    $$('.pn[data-target]').forEach(function (s) {
      var t = document.getElementById(s.dataset.target);
      if (t) { var pg = t.closest('.pg'); if (pg) s.textContent = pg.dataset.no; }
    });
    // report
    var report = pages.map(function (Pg) {
      var over = used(Pg) - PAGE_H;
      return { dbg: Pg.dbg, no: Pg.no, left: Math.round((Pg.left || 0) / MM * 10) / 10, raw: Math.round((Pg.rawLeft || 0) / MM * 10) / 10, over: over > 1 ? Math.round(over / MM * 10) / 10 : 0, n: Pg.items.length, last: !!Pg.last };
    });
    window.__report = { pages: pages.length + 1, stats: stats, rows: report };
    window.__done = true;
  }

  function start() {
    var imgs = $$('img');
    var pending = imgs.filter(function (i) { return !i.complete; });
    if (!pending.length) { run(); return; }
    var n = pending.length;
    pending.forEach(function (i) { var cb = function () { if (--n === 0) run(); }; i.addEventListener('load', cb); i.addEventListener('error', cb); });
  }
  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);
})();

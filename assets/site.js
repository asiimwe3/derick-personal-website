/* Derick personal-brand platform — shared behaviour */
(function () {
  'use strict';
  var root = document.documentElement;

  /* ---------- theme ---------- */
  var THEME_KEY = 'dp-theme';
  function applyTheme(t) {
    root.setAttribute('data-theme', t);
    var btn = document.getElementById('themeBtn');
    if (btn) {
      btn.innerHTML = t === 'light' ? '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a6.6 6.6 0 0 0 9.8 9.8z"/></svg>' : '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
      btn.setAttribute('aria-label', t === 'light' ? 'Switch to dark mode' : 'Switch to light mode');
    }
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', t === 'light' ? '#ffffff' : '#0b0f17');
  }
  var saved = null;
  try { saved = localStorage.getItem(THEME_KEY); } catch (e) {}
  /* Clean white is the default; dark is one tap away. */
  applyTheme(saved || 'light');
  document.addEventListener('click', function (e) {
    var t = e.target.closest('#themeBtn');
    if (!t) return;
    var next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    applyTheme(next);
    try { localStorage.setItem(THEME_KEY, next); } catch (err) {}
  });

  /* ---------- mobile nav ---------- */
  var menu = document.querySelector('.menu');
  var nav = document.querySelector('.header nav');
  if (menu && nav) {
    menu.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menu.setAttribute('aria-expanded', String(open));
      menu.innerHTML = open ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>' : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>';
    });
  }
  var more = document.querySelector('.nav-more');
  if (more) {
    var mbtn = more.querySelector('button');
    if (mbtn) mbtn.addEventListener('click', function (e) { e.stopPropagation(); more.classList.toggle('open'); });
    document.addEventListener('click', function (e) { if (!more.contains(e.target)) more.classList.remove('open'); });
  }

  /* ---------- current page highlight ---------- */
  var here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.header nav a[href]').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === here) a.setAttribute('aria-current', 'page');
  });

  /* ---------- year ---------- */
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  /* ---------- search ---------- */
  var wrap = document.getElementById('searchWrap');
  var input = document.getElementById('searchInput');
  var out = document.getElementById('searchResults');
  var index = null;

  function loadIndex() {
    if (index) return Promise.resolve(index);
    return fetch('assets/site-index.json').then(function (r) { return r.json(); }).then(function (d) { index = d; return d; });
  }
  function openSearch() {
    if (!wrap) return;
    wrap.classList.add('open');
    loadIndex();
    setTimeout(function () { if (input) input.focus(); }, 30);
  }
  function closeSearch() { if (wrap) wrap.classList.remove('open'); }

  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-search-open]')) { e.preventDefault(); openSearch(); }
    if (e.target === wrap) closeSearch();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); openSearch(); }
    if (e.key === 'Escape') closeSearch();
  });

  function render(q) {
    if (!out) return;
    q = (q || '').trim().toLowerCase();
    if (!q) { out.innerHTML = '<p class="hint" style="padding:6px 12px">Start typing to search pages, projects, writing and sections.</p>'; return; }
    var hits = (index || []).map(function (item) {
      var hay = (item.title + ' ' + item.desc + ' ' + (item.keys || '')).toLowerCase();
      var score = 0;
      if (item.title.toLowerCase().indexOf(q) > -1) score += 10;
      if (hay.indexOf(q) > -1) score += 4;
      q.split(/\s+/).forEach(function (w) { if (w.length > 2 && hay.indexOf(w) > -1) score += 1; });
      return { item: item, score: score };
    }).filter(function (h) { return h.score > 0; }).sort(function (a, b) { return b.score - a.score; }).slice(0, 12);

    out.innerHTML = hits.length
      ? hits.map(function (h) {
          return '<a href="' + h.item.url + '"><b>' + h.item.title + '</b><span>' + h.item.desc + '</span></a>';
        }).join('')
      : '<p class="hint" style="padding:6px 12px">Nothing matched. Try “projects”, “vision”, “contact” or “writing”.</p>';
  }
  if (input) {
    input.addEventListener('input', function () { loadIndex().then(function () { render(input.value); }); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { var first = out.querySelector('a'); if (first) location.href = first.getAttribute('href'); }
    });
    render('');
  }

  /* ---------- ask-me assistant (on-site, offline, no external API) ---------- */
  var log = document.getElementById('chatLog');
  var form = document.getElementById('chatForm');
  var field = document.getElementById('chatInput');
  var ANSWERS = [
    { k: ['invest', 'investment', 'raise', 'funding', 'deck', 'angel'], a: 'Derick is opening DeryCode Technologies and Sageco Evergreen to angel and strategic investors. Both are early stage and already operating. Ask for the deck at <a href="mailto:derickasiimwe849@gmail.com?subject=Investing%20in%20DeryCode%20and%20Sageco%20Evergreen">derickasiimwe849@gmail.com</a>, or read the investor page: <a href="investors.html">Investment &amp; business opportunities</a>.' },
    { k: ['derycode', 'company', 'companies', 'business', 'businesses', 'venture', 'ventures', 'run', 'software', 'website', 'developer'], a: 'DeryCode Technologies is his software company in Uganda: offline-first business systems, websites and AI tools, built and supported directly. More: <a href="ventures.html">Ventures</a> and <a href="https://derycode.online" target="_blank" rel="noreferrer">derycode.online</a>.' },
    { k: ['sageco', 'land', 'property', 'real estate', 'houses', 'plots'], a: 'Sageco Evergreen is the property platform he leads as CEO: verified listings, GPS boundaries, escrow-protected payments. See <a href="ventures.html">Ventures</a> and <a href="https://sageco-evergreen.vercel.app" target="_blank" rel="noreferrer">the platform</a>.' },
    { k: ['who', 'about', 'biography', 'yourself', 'derick'], a: 'Asiimwe Derick is a young social entrepreneur from Kyenjojo, western Uganda. Founder of DeryCode Technologies and CEO of Sageco Evergreen. Read the full biography: <a href="about.html">About</a>.' },
    { k: ['age', 'born', 'old', 'birthday'], a: 'Derick was born on 9 January 2006 in Kyenjojo, Uganda.' },
    { k: ['contact', 'email', 'reach', 'whatsapp', 'call', 'phone'], a: 'Email <a href="mailto:derickasiimwe849@gmail.com">derickasiimwe849@gmail.com</a>. All inquiry routes are on the <a href="contact.html">contact page</a>.' },
    { k: ['project', 'portfolio', 'built', 'work', 'client'], a: 'Projects, products and client work are collected on <a href="projects.html">Projects</a>, with case studies and live links.' },
    { k: ['vision', 'goal', 'future', '2030', '2040', 'plan'], a: 'Vision 2040: from builder to global investor. The roadmap, 1 to 20 year goals and Vision 2030 are on <a href="vision.html">Vision</a>.' },
    { k: ['skill', 'skills', 'stack', 'technology', 'tech'], a: 'Skills and expertise, plus the CV download, are on <a href="skills.html">Skills &amp; CV</a>.' },
    { k: ['writing', 'blog', 'article', 'insight'], a: 'Writing on technology, business, leadership and ideas: <a href="writing.html">Writing</a>.' },
    { k: ['speak', 'event', 'press', 'media', 'interview'], a: 'Speaking, media and press are on <a href="speaking.html">Speaking &amp; media</a>. Media kit: <a href="mediakit.html">Media kit</a>.' },
    { k: ['mentor', 'mentorship', 'youth', 'impact', 'community'], a: 'Leadership, mentorship, social impact and youth work are on <a href="impact.html">Impact</a>.' },
    { k: ['cv', 'resume', 'download'], a: 'Download the CV here: <a href="assets/derick-asiimwe-cv.pdf" download>Derick Asiimwe — CV (PDF)</a>.' },
    { k: ['hire', 'service', 'consult', 'partner', 'collaborate'], a: 'Services, consulting and partnership options are on <a href="services.html">Services &amp; collaboration</a>.' },
    { k: ['gallery', 'photo', 'picture', 'video'], a: 'Photos and moments: <a href="gallery.html">Gallery</a>.' },
    { k: ['site', 'website', 'build', 'hire developer', 'need a website'], a: 'For a website or software build, DeryCode Technologies handles it: <a href="https://derycode.online" target="_blank" rel="noreferrer">derycode.online</a> or WhatsApp 0762 306 675.' }
  ];
  function answer(q) {
    q = q.toLowerCase();
    var best = null, bestScore = 0;
    ANSWERS.forEach(function (item) {
      var s = 0;
      item.k.forEach(function (k) { if (q.indexOf(k) > -1) s += k.length + 2; });
      if (s > bestScore) { bestScore = s; best = item; }
    });
    if (best) return best.a;
    return 'I answer from this site only. Try asking about his biography, companies, projects, vision, skills, writing, speaking or how to get in touch. You can also <a href="contact.html">contact Derick directly</a>.';
  }
  function bubble(text, who) {
    var d = document.createElement('div');
    d.className = 'msg ' + who;
    d.innerHTML = text;
    log.appendChild(d);
    log.scrollTop = log.scrollHeight;
  }
  if (form && log) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = (field.value || '').trim();
      if (!v) return;
      bubble(v.replace(/[<>]/g, ''), 'me');
      field.value = '';
      setTimeout(function () { bubble(answer(v), 'ai'); }, 220);
    });
    document.querySelectorAll('[data-ask]').forEach(function (b) {
      b.addEventListener('click', function () {
        if (field) field.value = b.getAttribute('data-ask');
        if (form) form.dispatchEvent(new Event('submit', { cancelable: true }));
      });
    });
  }

  /* ---------- visitor analytics (privacy-first, local only) ---------- */
  /* Replace the body of track() with your endpoint when you connect a provider. */
  function track() {
    try {
      var key = 'dp-visits';
      var data = JSON.parse(localStorage.getItem(key) || '{}');
      var day = new Date().toISOString().slice(0, 10);
      data[day] = (data[day] || 0) + 1;
      data.last = here;
      localStorage.setItem(key, JSON.stringify(data));
    } catch (e) {}
  }
  track();
})();

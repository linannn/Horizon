(function () {
  'use strict';

  /** Replace ⭐️ N/10 with a colored badge in h2, h3, and li elements */
  function processScoreBadges() {
    var scoreRe = /⭐️\s*(\d+(?:\.\d+)?)\/10/;
    var targets = document.querySelectorAll('.main-content h2, .main-content h3, .main-content li');
    targets.forEach(function (el) {
      var m = el.innerHTML.match(scoreRe);
      if (!m) return;
      var score = parseFloat(m[1]);
      var tier;
      if (score >= 9) tier = 'high';
      else if (score >= 7) tier = 'good';
      else if (score >= 5) tier = 'mid';
      else tier = 'low';
      el.innerHTML = el.innerHTML.replace(
        scoreRe,
        '<span class="score-badge" data-tier="' + tier + '">' + m[1] + '</span>'
      );
    });
  }

  /** Add semantic classes to tag lines, source lines, and background paragraphs */
  function markSemanticElements() {
    var paragraphs = document.querySelectorAll('.main-content p');
    paragraphs.forEach(function (p) {
      var text = p.textContent.trim();

      // Tag line: starts with Tags or 标签 (bold prefix rendered by Markdown)
      if (/^(Tags|标签)\s*:/.test(text)) {
        p.classList.add('tag-line');
        return;
      }

      // Source line: pattern like "source · site · date"
      if (/^(rss|reddit|github|hackernews|hn|telegram)\s*·/i.test(text)) {
        p.classList.add('source-line');
        return;
      }
    });
  }

  function articleLanguage() {
    var path = window.location.pathname.replace(/\/$/, '');
    if (/-zh(?:\.html)?$/.test(path)) return 'zh';
    if (/-en(?:\.html)?$/.test(path)) return 'en';
    return null;
  }

  function replaceLinkedSentence(container, parts) {
    if (!container) return;
    var links = Array.prototype.slice.call(container.querySelectorAll('a'));
    if (links.length < parts.length - 1) return;
    var nodes = [];
    parts.forEach(function (text, index) {
      if (text) nodes.push(document.createTextNode(text));
      if (index < parts.length - 1) nodes.push(links[index].cloneNode(true));
    });
    container.replaceChildren.apply(container, nodes);
  }

  function localizeArticleChrome(lang) {
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en-US';
    if (lang !== 'zh') return;

    var skipLink = document.querySelector('a[href="#content"]');
    if (skipLink) skipLink.textContent = '跳至正文';
    var repositoryButton = document.querySelector('.page-header .btn');
    if (repositoryButton) repositoryButton.textContent = '在 GitHub 上查看';
    replaceLinkedSentence(
      document.querySelector('.site-footer-owner'),
      ['', ' 由 ', ' 维护。']
    );
    replaceLinkedSentence(
      document.querySelector('.site-footer-credits'),
      ['本页面由 ', ' 生成。']
    );
  }

  /** Set up EN/中文 language toggle as a page-level control */
  function setupLanguageToggle() {
    // Create toggle buttons
    var toggle = document.createElement('div');
    toggle.className = 'lang-toggle';

    var btnEn = document.createElement('button');
    btnEn.textContent = 'EN';
    btnEn.type = 'button';

    var btnZh = document.createElement('button');
    btnZh.textContent = '中文';
    btnZh.type = 'button';

    toggle.appendChild(btnEn);
    toggle.appendChild(btnZh);
    toggle.setAttribute('role', 'group');
    toggle.setAttribute('aria-label', 'Language / 语言');

    // Insert at top of body
    document.body.insertBefore(toggle, document.body.firstChild);

    // Read saved preference, default to zh
    var saved = null;
    try { saved = localStorage.getItem('horizon-lang'); } catch (e) { /* noop */ }
    var pageLang = articleLanguage();
    var currentLang = pageLang || (saved === 'en' ? 'en' : 'zh');

    function updateButtons(lang) {
      if (lang === 'en') {
        btnEn.classList.add('active');
        btnZh.classList.remove('active');
        btnEn.setAttribute('aria-pressed', 'true');
        btnZh.setAttribute('aria-pressed', 'false');
      } else {
        btnZh.classList.add('active');
        btnEn.classList.remove('active');
        btnEn.setAttribute('aria-pressed', 'false');
        btnZh.setAttribute('aria-pressed', 'true');
      }
    }

    // Index page: toggle lang-section visibility
    var zhSection = document.getElementById('lang-zh');
    var enSection = document.getElementById('lang-en');

    function showSection(lang) {
      if (!zhSection || !enSection) return;
      if (lang === 'en') {
        enSection.classList.remove('hidden');
        zhSection.classList.add('hidden');
      } else {
        zhSection.classList.remove('hidden');
        enSection.classList.add('hidden');
      }
    }

    // Article page: redirect to the other language version
    function switchArticleLang(lang) {
      var path = window.location.pathname;
      var target = null;
      if (lang === 'en' && /-zh(?:\.html)?$/.test(path.replace(/\/$/, ''))) {
        target = path.replace(/-zh(\.html)?$/, '-en$1').replace(/-zh\/$/, '-en/');
      } else if (lang === 'zh' && /-en(?:\.html)?$/.test(path.replace(/\/$/, ''))) {
        target = path.replace(/-en(\.html)?$/, '-zh$1').replace(/-en\/$/, '-zh/');
      }
      if (target) window.location.href = target;
    }

    function setLang(lang) {
      currentLang = lang;
      updateButtons(lang);
      try { localStorage.setItem('horizon-lang', lang); } catch (e) { /* noop */ }
      if (zhSection && enSection) {
        showSection(lang);
      } else {
        switchArticleLang(lang);
      }
    }

    btnEn.addEventListener('click', function () { setLang('en'); });
    btnZh.addEventListener('click', function () { setLang('zh'); });

    // Initialize
    updateButtons(currentLang);
    if (pageLang) localizeArticleChrome(pageLang);
    if (zhSection && enSection) {
      showSection(currentLang);
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    processScoreBadges();
    markSemanticElements();
    setupLanguageToggle();
  });
})();

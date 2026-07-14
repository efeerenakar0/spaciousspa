import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'GOOGLE TRANSLATE HACKS' not in css:
    css_hacks = """
/* ============================================================
   GOOGLE TRANSLATE HACKS
   ============================================================ */
body { top: 0 !important; }
.goog-te-banner-frame { display: none !important; }
.skiptranslate { display: none !important; }
#goog-gt-tt { display: none !important; }
.goog-text-highlight { background-color: transparent !important; box-shadow: none !important; }
"""
    css += css_hacks
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Update main.js
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

if 'LANGUAGE TRANSLATION' not in js:
    js_lang = """
  // ============================================================
  // LANGUAGE TRANSLATION (Google Translate Integration)
  // ============================================================
  const langOptions = document.querySelectorAll('.lang-option');
  const currentLangBtn = document.getElementById('currentLangBtn');
  
  const langMap = {
    'tr': '🇹🇷 TR',
    'en': '🇬🇧 EN',
    'ru': '🇷🇺 RU',
    'de': '🇩🇪 DE'
  };

  function triggerGoogleTranslate(langCode) {
    const select = document.querySelector('.goog-te-combo');
    if (select) {
      select.value = langCode;
      select.dispatchEvent(new Event('change'));
    } else {
      setTimeout(() => triggerGoogleTranslate(langCode), 500);
    }
  }

  langOptions.forEach(opt => {
    opt.addEventListener('click', (e) => {
      e.preventDefault();
      const lang = opt.getAttribute('data-lang');
      
      langOptions.forEach(o => o.classList.remove('active'));
      opt.classList.add('active');
      if (currentLangBtn) {
        currentLangBtn.innerHTML = `${langMap[lang]} <i class="fa fa-chevron-down"></i>`;
      }
      
      triggerGoogleTranslate(lang);
      localStorage.setItem('preferred_lang', lang);
    });
  });

  window.addEventListener('load', () => {
    const savedLang = localStorage.getItem('preferred_lang');
    if (savedLang && savedLang !== 'tr') {
      const opt = document.querySelector(`.lang-option[data-lang="${savedLang}"]`);
      if (opt) {
        // Just trigger translation and update UI, without triggering the click event to avoid loops
        langOptions.forEach(o => o.classList.remove('active'));
        opt.classList.add('active');
        if (currentLangBtn) {
          currentLangBtn.innerHTML = `${langMap[savedLang]} <i class="fa fa-chevron-down"></i>`;
        }
        triggerGoogleTranslate(savedLang);
      }
    }
  });
"""
    js = js.replace('// ============================================================', js_lang + '\n  // ============================================================', 1)
    with open('main.js', 'w', encoding='utf-8') as f:
        f.write(js)

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_lang_selector = """      <div class="lang-selector">
        <button class="lang-btn">🇹🇷 TR <i class="fa fa-chevron-down"></i></button>
        <div class="lang-dropdown">
          <a href="#" class="active">🇹🇷 Türkçe</a>
          <a href="#">🇬🇧 English</a>
          <a href="#">🇷🇺 Русский</a>
          <a href="#">🇩🇪 Deutsch</a>
        </div>
      </div>"""

new_lang_selector = """      <div class="lang-selector">
        <button class="lang-btn" id="currentLangBtn">🇹🇷 TR <i class="fa fa-chevron-down"></i></button>
        <div class="lang-dropdown">
          <a href="#" class="lang-option active" data-lang="tr">🇹🇷 Türkçe</a>
          <a href="#" class="lang-option" data-lang="en">🇬🇧 English</a>
          <a href="#" class="lang-option" data-lang="ru">🇷🇺 Русский</a>
          <a href="#" class="lang-option" data-lang="de">🇩🇪 Deutsch</a>
        </div>
      </div>"""

if new_lang_selector not in html:
    html = html.replace(old_lang_selector, new_lang_selector)

google_script = """<!-- ====== Google Translate ====== -->
<div id="google_translate_element" style="display:none;"></div>
<script type="text/javascript">
  function googleTranslateElementInit() {
    new google.translate.TranslateElement({
      pageLanguage: 'tr',
      includedLanguages: 'en,ru,de,tr',
      autoDisplay: false
    }, 'google_translate_element');
  }
</script>
<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

<script src="https://www.youtube.com/iframe_api"></script>"""

if 'google_translate_element' not in html:
    html = html.replace('<script src="https://www.youtube.com/iframe_api"></script>', google_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Files updated successfully.")

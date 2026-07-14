/* ===================================================
   SPACIOUS SPA – main.js v2.0
   Fethiye / Muğla
   =================================================== */

(function () {
  'use strict';

  
  // ============================================================
  // LANGUAGE TRANSLATION (Robust Cookie & Widget Integration)
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
    // 1. Set the Google Translate cookie directly
    document.cookie = `googtrans=/tr/${langCode}; path=/`;
    document.cookie = `googtrans=/tr/${langCode}; domain=${window.location.hostname}; path=/`;

    // 2. Try to trigger the widget programmatically
    const select = document.querySelector('.goog-te-combo');
    if (select) {
      select.value = langCode;
      select.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
    } else {
      // 3. If widget hasn't loaded or is hidden, reload the page to apply the cookie
      window.location.reload();
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
      
      localStorage.setItem('preferred_lang', lang);
      
      if (lang === 'tr') {
        // To revert to original language, clear the cookies
        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
        document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=${window.location.hostname}; path=/`;
        window.location.reload();
      } else {
        triggerGoogleTranslate(lang);
      }
    });
  });

  window.addEventListener('load', () => {
    const savedLang = localStorage.getItem('preferred_lang');
    if (savedLang && savedLang !== 'tr') {
      const opt = document.querySelector(`.lang-option[data-lang="${savedLang}"]`);
      if (opt) {
        langOptions.forEach(o => o.classList.remove('active'));
        opt.classList.add('active');
        if (currentLangBtn) {
          currentLangBtn.innerHTML = `${langMap[savedLang]} <i class="fa fa-chevron-down"></i>`;
        }
        // Don't trigger translation here, because Google Translate automatically reads the cookie!
      }
    }
  });

  // ============================================================
  // TOPBAR – hide on scroll down, show on scroll up
  // ============================================================
  const topbar = document.getElementById('topbar');
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const cur = window.scrollY;
    if (topbar) {
      topbar.classList.toggle('hidden', cur > lastScroll && cur > 80);
    }
    lastScroll = cur;
  }, { passive: true });

  // ============================================================
  // HEADER – sticky style on scroll
  // ============================================================
  const header = document.getElementById('header');
  function updateHeader() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 60);
  }
  window.addEventListener('scroll', updateHeader, { passive: true });
  updateHeader();

  // ============================================================
  // MOBILE MENU
  // ============================================================
  const hamburger     = document.getElementById('hamburger');
  const mobileMenu    = document.getElementById('mobileMenu');
  const mobileOverlay = document.getElementById('mobileOverlay');
  const mobileClose   = document.getElementById('mobileClose');

  function openMenu()  { mobileMenu.classList.add('open'); mobileOverlay.classList.add('active'); document.body.style.overflow = 'hidden'; }
  function closeMenu() { mobileMenu.classList.remove('open'); mobileOverlay.classList.remove('active'); document.body.style.overflow = ''; }

  if (hamburger)     hamburger.addEventListener('click', openMenu);
  if (mobileClose)   mobileClose.addEventListener('click', closeMenu);
  if (mobileOverlay) mobileOverlay.addEventListener('click', closeMenu);
  document.querySelectorAll('.mobile-link').forEach(l => l.addEventListener('click', closeMenu));

  // ============================================================
  // HERO VIDEO (Placeholder for future JS if needed)
  // ============================================================
  // Video plays inline automatically.

  // ============================================================
  // SMOOTH SCROLL
  // ============================================================
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = (header ? header.offsetHeight : 0) + (topbar ? topbar.offsetHeight : 0);
        window.scrollTo({ top: target.getBoundingClientRect().top + window.pageYOffset - offset, behavior: 'smooth' });
      }
    });
  });

  // ============================================================
  // ACTIVE NAV LINK
  // ============================================================
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link:not(.nav-cta)');

  new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + id));
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' }).observe || sections.forEach(sec => {
    new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + e.target.id));
      });
    }, { rootMargin: '-40% 0px -55% 0px' }).observe(sec);
  });
  // Proper usage:
  const sectionObs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + id));
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  sections.forEach(sec => sectionObs.observe(sec));

  // ============================================================
  // SCROLL REVEAL
  // ============================================================
  const revealEls = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right, .reveal-fade');
  const revealObs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('revealed'); revealObs.unobserve(entry.target); }
    });
  }, { threshold: 0.12 });
  revealEls.forEach(el => revealObs.observe(el));

  // ============================================================
  // TO TOP BUTTON
  // ============================================================
  const toTop = document.getElementById('toTop');
  if (toTop) {
    window.addEventListener('scroll', () => toTop.classList.toggle('visible', window.scrollY > 400), { passive: true });
    toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  // ============================================================
  // FAQ ACCORDION
  // ============================================================
  document.querySelectorAll('[data-faq]').forEach(item => {
    const btn = item.querySelector('.faq-q');
    if (!btn) return;
    btn.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      // Close all
      document.querySelectorAll('[data-faq].open').forEach(el => el.classList.remove('open'));
      // Toggle current
      if (!isOpen) item.classList.add('open');
    });
  });

  // ============================================================
  // GALLERY LIGHTBOX (simple)
  // ============================================================
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lb = document.createElement('div');
  lb.id = 'lightbox';
  lb.innerHTML = `
    <div class="lb-overlay"></div>
    <div class="lb-content">
      <button class="lb-close"><i class="fa fa-times"></i></button>
      <img class="lb-img" src="" alt=""/>
    </div>
  `;
  document.body.appendChild(lb);

  // Inline style for lightbox
  const lbStyle = document.createElement('style');
  lbStyle.textContent = `
    #lightbox { display: none; position: fixed; inset: 0; z-index: 5000; align-items: center; justify-content: center; }
    #lightbox.active { display: flex; }
    .lb-overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.9); cursor: pointer; }
    .lb-content { position: relative; z-index: 1; max-width: 90vw; max-height: 90vh; }
    .lb-img { max-width: 90vw; max-height: 85vh; object-fit: contain; border-radius: 4px; display: block; }
    .lb-close { position: absolute; top: -44px; right: 0; color: #fff; font-size: 22px; background: none; border: none; cursor: pointer; padding: 8px; }
  `;
  document.head.appendChild(lbStyle);

  galleryItems.forEach(item => {
    item.style.cursor = 'pointer';
    item.addEventListener('click', () => {
      const bg = item.style.backgroundImage;
      const url = bg.replace(/^url\(["']?/, '').replace(/["']?\)$/, '');
      lb.querySelector('.lb-img').src = url;
      lb.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  });
  lb.querySelector('.lb-overlay').addEventListener('click', closeLightbox);
  lb.querySelector('.lb-close').addEventListener('click', closeLightbox);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLightbox(); });
  function closeLightbox() { lb.classList.remove('active'); document.body.style.overflow = ''; }

  // ============================================================
  // CONTACT FORM → WhatsApp redirect
  // ============================================================
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const name    = document.getElementById('name').value.trim();
      const phone   = document.getElementById('phone').value.trim();
      const service = document.getElementById('service').value;
      const date    = document.getElementById('date').value;
      const time    = document.getElementById('time').value;
      const persons = document.getElementById('persons').value;
      const lang    = document.getElementById('lang').value;
      const message = document.getElementById('message').value.trim();

      if (!name || !phone || !service) {
        alert('Lütfen adınızı, telefonunuzu ve hizmet seçimini yapınız.');
        return;
      }

      const serviceNames = {
        spa:     'SPA & Masaj',
        hamam:   'Türk Hamamı',
        beauty:  'Güzellik Bakımı',
        sauna:   'Sauna',
        pool:    'Yüzme Havuzu',
        couple:  'Çift Paketi',
        package: 'Tam Gün Spa Paketi'
      };
      const langNames = { tr:'Türkçe', en:'English', ar:'العربية', ru:'Русский', de:'Deutsch', uk:'Українська' };

      let text = `*Spacious Spa – Randevu Talebi*\n`;
      text += `📍 Karagözler Mah. Fevzi Çakmak Cd. No:17, Fethiye/Muğla\n\n`;
      text += `👤 *Ad Soyad:* ${name}\n`;
      text += `📞 *Telefon:* ${phone}\n`;
      text += `🌐 *Dil:* ${langNames[lang] || lang}\n`;
      text += `💆 *Hizmet:* ${serviceNames[service] || service}\n`;
      text += `👥 *Kişi:* ${persons}\n`;
      if (date) text += `📅 *Tarih:* ${date}\n`;
      if (time) text += `🕐 *Saat:* ${time}\n`;
      if (message) text += `📝 *Not:* ${message}\n`;

      const waNumber = '905161664800';
      window.open(`https://wa.me/${waNumber}?text=${encodeURIComponent(text)}`, '_blank');
    });
  }

  // ============================================================
  // PARALLAX – disable on iOS
  // ============================================================
  const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
  if (isIOS) {
    document.querySelectorAll('.parallax-banner').forEach(el => {
      el.style.backgroundAttachment = 'scroll';
    });
  }

  // ============================================================
  // GALLERY extra rows need height fix
  // ============================================================
  function fixGallery() {
    document.querySelectorAll('.gallery-item').forEach(item => {
      if (!item.classList.contains('gallery-item-tall') && !item.classList.contains('gallery-item-wide')) {
        if (window.innerWidth > 640) item.style.height = '280px';
        else item.style.height = '220px';
      }
    });
  }
  fixGallery();
  window.addEventListener('resize', fixGallery);

  // ============================================================
  // TABBED GALLERY FILTERING
  // ============================================================
  const filters = document.querySelectorAll('.gallery-filter');
  const galleryGridItems = document.querySelectorAll('.gallery-grid .gallery-item');

  filters.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active class from all buttons
      filters.forEach(f => f.classList.remove('active'));
      // Add active class to clicked button
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      galleryGridItems.forEach(item => {
        const category = item.getAttribute('data-category');
        
        // Hide all initially for smooth transition
        item.style.opacity = '0';
        item.style.transform = 'scale(0.95)';
        
        setTimeout(() => {
          if (filterValue === 'all' || filterValue === category) {
            item.style.display = '';
            // Small delay to allow display to apply before opacity/transform transition
            setTimeout(() => {
              item.style.opacity = '1';
              item.style.transform = 'scale(1)';
            }, 50);
          } else {
            item.style.display = 'none';
          }
        }, 300); // Wait for fade out
      });
    });
  });

  // Add transition to gallery items for smooth filtering
  galleryGridItems.forEach(item => {
    item.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
  });

})();

/* ============================================================
   MUSIC PLAYER (YouTube Iframe API)
   ============================================================ */
let ytPlayer;
let isMusicPlaying = false;

window.onYouTubeIframeAPIReady = function() {
  ytPlayer = new YT.Player('ytPlayer', {
    height: '1',
    width: '1',
    videoId: '1ZYbU82GVz4', // 3 Hour Relaxing Spa Music
    playerVars: {
      'autoplay': 1,
      'mute': 1, // Start muted to guarantee autoplay
      'controls': 0,
      'disablekb': 1,
      'fs': 0,
      'loop': 1,
      'playlist': '1ZYbU82GVz4',
      'modestbranding': 1
    },
    events: {
      'onReady': onPlayerReady
    }
  });
};

function onPlayerReady(event) {
  const musicBtn = document.getElementById('musicBtn');
  const musicIcon = document.getElementById('musicIcon');
  const musicLabel = document.querySelector('.music-label');

  if (musicBtn) {
    musicLabel.textContent = 'Spa Müziği Çal';

    musicBtn.addEventListener('click', () => {
      if (isMusicPlaying) {
        ytPlayer.pauseVideo();
        musicIcon.className = 'fa fa-play';
        musicLabel.textContent = 'Spa Müziği Çal';
        musicBtn.classList.remove('playing');
        isMusicPlaying = false;
      } else {
        ytPlayer.unMute();
        ytPlayer.setVolume(100); // MAXIMUM VOLUME
        ytPlayer.playVideo();
        musicIcon.className = 'fa fa-pause';
        musicLabel.textContent = 'Müziği Durdur';
        musicBtn.classList.add('playing');
        isMusicPlaying = true;
      }
    });

    const startMusicOnInteract = () => {
      if (!isMusicPlaying && ytPlayer && ytPlayer.unMute) {
        ytPlayer.unMute();
        ytPlayer.setVolume(100); // MAXIMUM VOLUME
        if (ytPlayer.getPlayerState() !== 1) ytPlayer.playVideo();
        
        musicIcon.className = 'fa fa-pause';
        musicLabel.textContent = 'Müziği Durdur';
        musicBtn.classList.add('playing');
        isMusicPlaying = true;
      }
      document.removeEventListener('click', startMusicOnInteract);
      document.removeEventListener('scroll', startMusicOnInteract);
      document.removeEventListener('keydown', startMusicOnInteract);
      document.removeEventListener('touchstart', startMusicOnInteract);
    };

    document.addEventListener('click', startMusicOnInteract);
    document.addEventListener('scroll', startMusicOnInteract, {once: true});
    document.addEventListener('keydown', startMusicOnInteract, {once: true});
    document.addEventListener('touchstart', startMusicOnInteract, {once: true});
  }
}

/* Paweł Sudomir — interakcje i animacje (bez zależności) */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const root = document.documentElement;

  /* Rok w stopce */
  $$('[data-year]').forEach(el => (el.textContent = new Date().getFullYear()));

  /* Nagłówek: przezroczysty nad hero, pełny po przewinięciu, chowa się przy przewijaniu w dół */
  const header = $('.header');
  const hero = $('.hero');
  const alwaysSolid = header && header.dataset.solid === '1';
  let lastY = scrollY;
  const onScroll = () => {
    const y = scrollY;
    if (header) {
      const limit = hero ? hero.offsetHeight - 90 : 10;
      header.classList.toggle('is-solid', alwaysSolid || y > limit);
      const hide = y > lastY && y > 400 && !document.body.classList.contains('menu-open');
      header.classList.toggle('is-hidden', hide);
    }
    lastY = y;
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Menu mobilne */
  const burger = $('.burger');
  const menu = $('#mobile-menu');
  const setMenu = open => {
    document.body.classList.toggle('menu-open', open);
    burger?.setAttribute('aria-expanded', String(open));
    burger?.setAttribute('aria-label', open ? 'Zamknij menu' : 'Otwórz menu');
    menu?.setAttribute('aria-hidden', String(!open));
  };
  burger?.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
  $$('#mobile-menu a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  addEventListener('keydown', e => e.key === 'Escape' && setMenu(false));
  matchMedia('(min-width: 961px)').addEventListener('change', e => e.matches && setMenu(false));

  /* Odsłanianie elementów przy przewijaniu + liczniki */
  const countUp = el => {
    const end = +el.dataset.count;
    if (reduce || !end) return;
    const t0 = performance.now(), dur = 1500;
    const step = t => {
      const p = Math.min(1, (t - t0) / dur);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    };
    el.textContent = '0';
    requestAnimationFrame(step);
  };
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        $$('[data-count]', e.target).forEach(countUp);
        io.unobserve(e.target);
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    $$('.rv').forEach(el => io.observe(el));
  } else {
    $$('.rv').forEach(el => el.classList.add('in'));
  }

  /* Hasło: słowa podświetlają się w miarę przewijania */
  const words = $('[data-words]');
  let wordEls = [];
  if (words) {
    const wrap = node => {
      [...node.childNodes].forEach(n => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) frag.appendChild(document.createTextNode(part));
            else { const s = document.createElement('span'); s.className = 'w'; s.textContent = part; frag.appendChild(s); }
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') wrap(n);
      });
    };
    wrap(words);
    wordEls = $$('.w', words);
    wordEls.forEach((w, i) => w.style.setProperty('--i', i));
  }

  /* Paralaksa (hero, sekcja pasji, zdjęcia w galerii) */
  const par = $$('[data-parallax]');
  const floats = $$('[data-float]');
  let ticking = false;
  const frame = () => {
    ticking = false;
    const vh = innerHeight;
    if (!reduce) {
      par.forEach(el => {
        const box = el.parentElement.getBoundingClientRect();
        if (box.bottom < 0 || box.top > vh) return;
        const k = parseFloat(el.dataset.parallax);
        el.style.transform = `translate3d(0, ${(-box.top) * k}px, 0)`;
      });
      if (innerWidth > 760) floats.forEach(el => {
        const box = el.getBoundingClientRect();
        const mid = box.top + box.height / 2 - vh / 2;
        el.style.translate = `0 ${mid * parseFloat(el.dataset.float)}px`;
      });
    }
  };
  const req = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  addEventListener('scroll', req, { passive: true });
  addEventListener('resize', req);
  frame();

  /* Karuzela opinii: strzałki, przeciąganie myszą, klawiatura */
  const track = $('[data-track]');
  if (track) {
    const prev = $('[data-prev]'), next = $('[data-next]');
    const stepW = () => (track.firstElementChild?.offsetWidth || 400) + 16;
    prev?.addEventListener('click', () => track.scrollBy({ left: -stepW(), behavior: reduce ? 'auto' : 'smooth' }));
    next?.addEventListener('click', () => track.scrollBy({ left: stepW(), behavior: reduce ? 'auto' : 'smooth' }));
    const upd = () => {
      if (prev) prev.disabled = track.scrollLeft < 8;
      if (next) next.disabled = track.scrollLeft + track.clientWidth > track.scrollWidth - 8;
    };
    track.addEventListener('scroll', upd, { passive: true });
    addEventListener('resize', upd); upd();
    track.addEventListener('keydown', e => {
      if (e.key === 'ArrowRight') { e.preventDefault(); next?.click(); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); prev?.click(); }
    });
    let down = false, sx = 0, sl = 0, moved = false;
    track.addEventListener('pointerdown', e => {
      if (e.pointerType !== 'mouse') return;
      down = true; moved = false; sx = e.clientX; sl = track.scrollLeft;
    });
    addEventListener('pointermove', e => {
      if (!down) return;
      const dx = e.clientX - sx;
      if (Math.abs(dx) > 4) { moved = true; track.classList.add('dragging'); }
      track.scrollLeft = sl - dx;
    });
    addEventListener('pointerup', () => {
      if (!down) return;
      down = false;
      track.classList.remove('dragging');
      if (moved) {
        const w = stepW();
        track.scrollTo({ left: Math.round(track.scrollLeft / w) * w, behavior: 'smooth' });
      }
    });
  }

  /* Opinie: „Czytaj całość” + okno z pełną treścią */
  const dlg = $('#review-dialog');
  const markReadMore = () => $$('.review').forEach(card => {
    const q = $('blockquote', card), btn = $('[data-read]', card);
    if (q && btn) btn.classList.toggle('on', q.scrollHeight > q.clientHeight + 2);
  });
  markReadMore(); addEventListener('resize', markReadMore);
  document.fonts?.ready.then(markReadMore);
  $$('[data-read]').forEach(btn => btn.addEventListener('click', () => {
    if (!dlg) return;
    const card = btn.closest('.review');
    const body = $('.rd-body', dlg);
    body.innerHTML = `<div class="q" aria-hidden="true">“</div>${$('blockquote', card).outerHTML}${$('figcaption', card).outerHTML}`;
    dlg.showModal ? dlg.showModal() : dlg.setAttribute('open', '');
  }));
  dlg?.addEventListener('click', e => { if (e.target === dlg || e.target.closest('[data-close]')) dlg.close(); });

  /* Galeria na mobile: zacznij od środkowego zdjęcia */
  const gallery = $('[data-gallery]');
  if (gallery && innerWidth <= 760) {
    const mid = gallery.children[1];
    requestAnimationFrame(() => (gallery.scrollLeft = mid.offsetLeft - (gallery.clientWidth - mid.offsetWidth) / 2));
  }

  root.classList.add('js');
})();

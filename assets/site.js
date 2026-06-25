/* A La Cart concept sites — shared behavior (reveal, nav state, quote rotator, quote-form success) */
(function () {
  document.body.classList.add('js-on');

  // scroll reveal (.reveal = fade/rise, .poly = settling polaroid)
  var reveals = document.querySelectorAll('.reveal, .poly');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -7% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }
  // failsafe: never leave content hidden
  setTimeout(function () { document.querySelectorAll('.reveal:not(.in), .poly:not(.in)').forEach(function (el) { el.classList.add('in'); }); }, 3000);

  // parallax (elements with data-parallax move slower than scroll)
  var px = document.querySelectorAll('[data-parallax]');
  if (px.length && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var tick = function () {
      px.forEach(function (el) {
        var r = el.getBoundingClientRect(), mid = r.top + r.height / 2 - window.innerHeight / 2;
        el.style.transform = 'translateY(' + (mid * -0.08) + 'px) scale(1.12)';
      });
    };
    tick(); window.addEventListener('scroll', tick, { passive: true });
  }

  // sticky nav state
  var nav = document.querySelector('[data-nav]');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 24); };
    onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
  }

  // rotating single-quote block: <div data-rotator><blockquote class="q">..</blockquote>..</div>
  document.querySelectorAll('[data-rotator]').forEach(function (r) {
    var qs = r.querySelectorAll('.q'); if (qs.length < 2) return;
    var i = 0; qs[0].classList.add('on');
    setInterval(function () {
      qs[i].classList.remove('on'); i = (i + 1) % qs.length; qs[i].classList.add('on');
    }, 5200);
  });

  // horizontal deck arrows (scrapbook service deck)
  document.querySelectorAll('.deck-arrow').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var wrap = btn.closest('.deck-wrap'); if (!wrap) return;
      var deck = wrap.querySelector('.deck'); if (!deck) return;
      var amt = Math.max(320, deck.clientWidth * 0.8);
      deck.scrollBy({ left: btn.dataset.dir === 'next' ? amt : -amt, behavior: 'smooth' });
    });
  });

  // quote-request form success
  var f = document.getElementById('quoteForm');
  if (f) {
    f.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var wrap = document.getElementById('quoteWrap');
      var nameEl = f.querySelector('[name=name]');
      var first = nameEl && nameEl.value ? (', ' + nameEl.value.split(' ')[0]) : '';
      wrap.innerHTML =
        '<div class="quote-success">' +
        '<div class="qcheck"><svg viewBox="0 0 52 52"><circle cx="26" cy="26" r="23"/><path d="M16 27l7 7 14-15"/></svg></div>' +
        '<h3>Thank you' + first + '!</h3>' +
        '<p>Your request is on its way. Rebecca will reply within one business day with availability and pricing.</p></div>';
      wrap.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }
})();

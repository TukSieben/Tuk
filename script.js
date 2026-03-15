// ── Panel switching (show() defined inline in HTML for reliability) ──
// Wrap the global show to add animations after switching
(function() {
  var _original = window.show;
  window.show = function(id, el) {
    _original(id, el);
    var panel = document.getElementById('panel-' + id);
    if (panel) animatePanel(panel);
  };
})();

// ── Animate panel elements on reveal ─────────────────────────
function animatePanel(panel) {
  var items = panel.querySelectorAll('.p-row, .links-title, .hero-name, .hero-content');
  items.forEach(function(el, i) {
    el.style.opacity = '0';
    el.style.transform = 'translateY(10px)';
    el.style.transition = 'none';
    requestAnimationFrame(function() {
      requestAnimationFrame(function() {
        el.style.transition = 'opacity 0.35s ease ' + (i * 55) + 'ms, transform 0.35s ease ' + (i * 55) + 'ms';
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
      });
    });
  });
}

// ── Sidebar items fade in on load ────────────────────────────
function initSidebar() {
  var items = document.querySelectorAll('.s-item, .s-label');
  items.forEach(function(el, i) {
    el.style.opacity = '0';
    el.style.transform = 'translateX(-6px)';
    setTimeout(function() {
      el.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
      el.style.opacity = '1';
      el.style.transform = 'translateX(0)';
    }, 80 + i * 60);
  });
}

// ── Topbar fade in ────────────────────────────────────────────
function initTopbar() {
  var bar = document.querySelector('.topbar');
  if (!bar) return;
  bar.style.opacity = '0';
  setTimeout(function() {
    bar.style.transition = 'opacity 0.4s ease';
    bar.style.opacity = '1';
  }, 30);
}

// ── Hero subtle parallax on mousemove ────────────────────────
function initParallax() {
  var hero = document.querySelector('.hero');
  if (!hero) return;
  hero.addEventListener('mousemove', function(e) {
    var rect = hero.getBoundingClientRect();
    var x = (e.clientX - rect.left) / rect.width - 0.5;
    var y = (e.clientY - rect.top)  / rect.height - 0.5;
    var content = hero.querySelector('.hero-content');
    if (content) {
      content.style.transform = 'translate(' + (x * 6) + 'px, ' + (y * 4) + 'px)';
      content.style.transition = 'transform 0.15s ease';
    }
  });
  hero.addEventListener('mouseleave', function() {
    var content = hero.querySelector('.hero-content');
    if (content) {
      content.style.transform = 'translate(0,0)';
      content.style.transition = 'transform 0.5s ease';
    }
  });
}

// ── Init ──────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
  initTopbar();
  initSidebar();
  var active = document.querySelector('.panel.active');
  if (active) animatePanel(active);
  initParallax();
});

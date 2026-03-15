// ── Panel switching ──────────────────────────────────────────
function show(id, el) {
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.s-item').forEach(s => s.classList.remove('active'));
  const panel = document.getElementById('panel-' + id);
  panel.classList.add('active');
  el.classList.add('active');
  animatePanel(panel);
}

// ── Animate panel elements on reveal ─────────────────────────
function animatePanel(panel) {
  const items = panel.querySelectorAll('.p-row, .links-title, .hero-name, .hero-content');
  items.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(10px)';
    el.style.transition = 'none';
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        el.style.transition = `opacity 0.35s ease ${i * 55}ms, transform 0.35s ease ${i * 55}ms`;
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
      });
    });
  });
}

// ── Sidebar items fade in on load ────────────────────────────
function initSidebar() {
  const items = document.querySelectorAll('.s-item, .s-label');
  items.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateX(-6px)';
    setTimeout(() => {
      el.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
      el.style.opacity = '1';
      el.style.transform = 'translateX(0)';
    }, 80 + i * 60);
  });
}

// ── Topbar fade in ────────────────────────────────────────────
function initTopbar() {
  const bar = document.querySelector('.topbar');
  if (!bar) return;
  bar.style.opacity = '0';
  setTimeout(() => {
    bar.style.transition = 'opacity 0.4s ease';
    bar.style.opacity = '1';
  }, 30);
}

// ── Hero grid subtle parallax on mousemove ────────────────────
function initParallax() {
  const hero = document.querySelector('.hero');
  if (!hero) return;
  hero.addEventListener('mousemove', (e) => {
    const rect = hero.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top)  / rect.height - 0.5;
    hero.style.backgroundPosition = `${50 + x * 4}% ${50 + y * 4}%`;
    const glow = hero.querySelector('.hero-content');
    if (glow) {
      glow.style.transform = `translate(${x * 6}px, ${y * 4}px)`;
      glow.style.transition = 'transform 0.15s ease';
    }
  });
  hero.addEventListener('mouseleave', () => {
    const glow = hero.querySelector('.hero-content');
    if (glow) {
      glow.style.transform = 'translate(0,0)';
      glow.style.transition = 'transform 0.5s ease';
    }
  });
}

// ── Link row hover cursor trail (subtle dot) ──────────────────
function initRowHover() {
  document.querySelectorAll('.p-row').forEach(row => {
    row.addEventListener('mouseenter', () => {
      row.style.transition = 'padding-left 0.22s cubic-bezier(.22,1,.36,1)';
    });
  });
}

// ── Init ──────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  initTopbar();
  initSidebar();
  // animate the default visible panel
  const active = document.querySelector('.panel.active');
  if (active) animatePanel(active);
  initParallax();
  initRowHover();
});

/* ═══════════════════════════════════════════
   tuk — script.js
   Subtle effects only. No libraries.
═══════════════════════════════════════════ */

/**
 * Spotlight: tracks mouse across interactive cards
 * and paints a faint accent-colored highlight.
 */
const spotlightTargets = document.querySelectorAll('.link-card, .project-card');

spotlightTargets.forEach(el => {
  el.addEventListener('mousemove', e => {
    const r   = el.getBoundingClientRect();
    const x   = ((e.clientX - r.left) / r.width  * 100).toFixed(1);
    const y   = ((e.clientY - r.top)  / r.height * 100).toFixed(1);
    el.style.backgroundImage =
      `radial-gradient(circle at ${x}% ${y}%, rgba(0,229,255,0.055) 0%, transparent 65%)`;
  });

  el.addEventListener('mouseleave', () => {
    el.style.backgroundImage = '';
  });
});

/**
 * Blinking cursor after the hero subtitle.
 */
const sub = document.querySelector('.hero-sub');
if (sub) {
  const style = document.createElement('style');
  style.textContent = `
    @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
    .cursor {
      display: inline-block;
      margin-left: 2px;
      color: var(--accent);
      font-size: 0.9em;
      animation: blink 1.1s step-end infinite;
    }
  `;
  document.head.appendChild(style);

  const cursor = document.createElement('span');
  cursor.className = 'cursor';
  cursor.textContent = '_';
  sub.appendChild(cursor);
}

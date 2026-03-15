/* ═══════════════════════════════════════════
   tuk — script.js
   Lightweight interactions only.
═══════════════════════════════════════════ */

/* Ripple effect on card click */
document.querySelectorAll('.card-link').forEach(card => {
  card.addEventListener('click', function (e) {
    const circle = document.createElement('span');
    const diameter = Math.max(card.clientWidth, card.clientHeight);
    const radius = diameter / 2;
    const rect = card.getBoundingClientRect();

    circle.style.cssText = `
      position: absolute;
      width: ${diameter}px;
      height: ${diameter}px;
      left: ${e.clientX - rect.left - radius}px;
      top: ${e.clientY - rect.top - radius}px;
      background: rgba(145, 71, 255, 0.12);
      border-radius: 50%;
      transform: scale(0);
      animation: ripple 450ms ease-out forwards;
      pointer-events: none;
    `;

    card.style.position = 'relative';
    card.style.overflow = 'hidden';
    card.appendChild(circle);
    setTimeout(() => circle.remove(), 500);
  });
});

/* Inject ripple keyframe once */
const s = document.createElement('style');
s.textContent = `@keyframes ripple { to { transform: scale(2.5); opacity: 0; } }`;
document.head.appendChild(s);

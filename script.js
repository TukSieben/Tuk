/* ═══════════════════════════════════════════
   SOCIALS SITE — script.js
   Subtle interactivity only — no frameworks
═══════════════════════════════════════════ */

/**
 * Card spotlight effect:
 * Tracks the mouse position inside each card
 * and adds a subtle radial highlight at the cursor.
 */
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width  * 100).toFixed(1);
    const y = ((e.clientY - rect.top)  / rect.height * 100).toFixed(1);

    card.style.setProperty('--mx', `${x}%`);
    card.style.setProperty('--my', `${y}%`);
    card.style.backgroundImage =
      `radial-gradient(circle at ${x}% ${y}%, rgba(124,106,247,0.06) 0%, transparent 65%)`;
  });

  card.addEventListener('mouseleave', () => {
    card.style.backgroundImage = '';
  });
});

/**
 * Typed cursor blink on the tagline.
 * Adds a blinking "|" caret after the tagline text.
 */
const tagline = document.querySelector('.tagline');
if (tagline) {
  const caret = document.createElement('span');
  caret.textContent = '|';
  caret.style.cssText = `
    display: inline-block;
    margin-left: 2px;
    color: var(--accent);
    animation: blink 1s step-end infinite;
    font-size: 0.9em;
  `;

  // Inject @keyframes blink once
  if (!document.getElementById('blink-style')) {
    const style = document.createElement('style');
    style.id = 'blink-style';
    style.textContent = `
      @keyframes blink {
        0%, 100% { opacity: 1; }
        50%       { opacity: 0; }
      }
    `;
    document.head.appendChild(style);
  }

  tagline.appendChild(caret);
}

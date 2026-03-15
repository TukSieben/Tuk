# 🌐 Socials Site

A minimal, dark personal link page — inspired by dev aesthetics.  
Built with plain HTML, CSS, and vanilla JS. No frameworks, no build step.

---

## 📁 File Structure

```
socials-site/
├── index.html   ← Page structure & content
├── style.css    ← All styling (edit here for design changes)
├── script.js    ← Subtle interactivity (spotlight + cursor blink)
└── README.md    ← This file
```

---

## ✏️ How to Customize

### 1. Your Name & Tagline
Open `index.html` and replace all occurrences of `yourname` and `yourusername` with your actual name.

### 2. Avatar
Replace the `<img src="...">` in the `.avatar-ring` with your own image:
```html
<img class="avatar" src="assets/avatar.jpg" alt="Avatar" width="90" height="90" />
```
Or keep the DiceBear placeholder and change the `seed=` param to your name.

### 3. Socials
Edit the links inside the `#socials` section — just swap the `href` values.  
Remove or add `<li>` blocks as needed.

### 4. Projects
Each project is a `<li class="project-item">` block.  
- Change `.project-name` href and text
- Change `.project-desc` text
- Change `.project-status` class: `status-live` / `status-wip` / `status-hidden`
- Change `.tag` values for your tech stack

### 5. Colors & Fonts
All design tokens are CSS variables at the top of `style.css`:
```css
:root {
  --accent: #7c6af7;   /* ← change accent color here */
  --bg:     #0b0b0f;   /* ← change background here  */
  ...
}
```

---

## 🚀 Deploy to GitHub Pages

1. Create a new GitHub repository (e.g. `yourname.github.io` for a root domain)
2. Push all files to the `main` branch
3. Go to **Settings → Pages → Source → Deploy from branch → main / root**
4. Your site will be live at `https://yourusername.github.io/repo-name/`

> **Tip:** Name the repo `yourusername.github.io` to get `https://yourusername.github.io` as the URL directly.

---

## 🎨 Features

- Dark terminal aesthetic with noise + glow background
- Animated card entrance (fade up on load)
- Mouse spotlight effect on cards
- Blinking cursor on tagline
- Fully responsive (mobile-friendly)
- Zero dependencies — just open `index.html` in a browser

---

© 2026 · yourname

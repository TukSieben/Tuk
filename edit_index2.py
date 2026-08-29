import sys

css = """
/* Language Toggle */
.lang-toggle-btn {
    background: transparent;
    border: 1px solid var(--card-border);
    color: var(--text-primary);
    font-family: var(--font-primary);
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    padding: 6px 10px;
    border-radius: 8px;
    transition: var(--transition);
    margin-right: 12px;
}
.lang-toggle-btn:hover {
    border-color: var(--primary);
    color: var(--primary);
}

/* Stats Section */
.stats-section {
    padding: 40px 24px;
    display: flex;
    justify-content: center;
}
.stats-container {
    max-width: 1000px;
    width: 100%;
    display: flex;
    justify-content: space-around;
    gap: 20px;
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 20px;
    padding: 40px 20px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
}
.stat-item {
    text-align: center;
    flex: 1;
}
.stat-number {
    font-family: var(--font-headline);
    font-size: 3.5rem;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 8px;
    line-height: 1;
}
.stat-label {
    font-size: 1.1rem;
    color: var(--text-secondary);
    font-weight: 600;
}
@media (max-width: 768px) {
    .stats-container {
        flex-direction: column;
        gap: 40px;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)

js_to_add = """
        // Language Toggle Logic
        const langToggleBtn = document.getElementById('langToggleBtn');
        let currentLang = localStorage.getItem('tuk_lang') || 'en';

        function updateLanguage(lang) {
            document.querySelectorAll('[data-en][data-de]').forEach(el => {
                el.innerHTML = lang === 'de' ? el.getAttribute('data-de') : el.getAttribute('data-en');
            });
            langToggleBtn.textContent = lang === 'de' ? 'DE' : 'EN';
            
            // Re-bind email copy text if it changed
            if (lang === 'de') {
                copyText.innerText = 'tukk@tuta.io'; // keep email
            }
        }

        langToggleBtn.addEventListener('click', () => {
            currentLang = currentLang === 'en' ? 'de' : 'en';
            localStorage.setItem('tuk_lang', currentLang);
            updateLanguage(currentLang);
        });

        // Initialize language
        updateLanguage(currentLang);

        // Counter Animation Logic
        const counters = document.querySelectorAll('.counter');
        const counterObserver = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = +counter.getAttribute('data-target');
                    const duration = 2000; // ms
                    const step = target / (duration / 16); // 60fps
                    let current = 0;

                    const updateCounter = () => {
                        current += step;
                        if (current < target) {
                            counter.innerText = Math.ceil(current);
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.innerText = target;
                        }
                    };

                    updateCounter();
                    obs.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => {
            counterObserver.observe(counter);
        });
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('    </script>\n</body>', js_to_add + '    </script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

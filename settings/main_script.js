// --- Global Transitions & Audio Feedback ---

document.addEventListener('DOMContentLoaded', () => {
    // 0. Clean URL (Remove index.html from URL bar)
    if (window.location.pathname.endsWith('index.html')) {
        const cleanUrl = window.location.pathname.replace('index.html', '');
        window.history.replaceState({}, document.title, cleanUrl);
    }

    // 1. Page Transitions (Fade Out)
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            
            // Only transition for internal links
            if (href && !href.startsWith('http') && !href.startsWith('#')) {
                e.preventDefault();
                document.body.classList.add('fade-out');
                setTimeout(() => {
                    window.location.href = href;
                }, 400);
            }
        });
    });

    // 2. Audio Feedback (Click Sound)
    // Create a very subtle procedural click sound using Web Audio API
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    
    function playClickSound() {
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        const oscillator = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();

        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(150, audioCtx.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);

        gainNode.gain.setValueAtTime(0.05, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);

        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);

        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.1);
    }

    function playHoverSound() {
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }
        const oscillator = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();

        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(800, audioCtx.currentTime); // Höherer Ton für Hover
        oscillator.frequency.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);

        gainNode.gain.setValueAtTime(0.01, audioCtx.currentTime); // Extrem leise
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);

        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);

        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.05);
    }

    // Attach sounds to all interactive elements
    const interactiveElements = document.querySelectorAll('a, button, .accordion-header');
    interactiveElements.forEach(el => {
        el.addEventListener('click', () => {
            playClickSound();
        });
        el.addEventListener('mouseenter', () => {
            playHoverSound();
        });
    });

    // 3. Dynamic Scroll Progress Bar
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
        const windowScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (windowScroll / height) * 100;
        progressBar.style.width = scrolled + '%';
    });
});

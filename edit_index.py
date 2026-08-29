import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Lang Toggle Button
html = html.replace('<!-- Theme Switch -->', '<button id="langToggleBtn" class="lang-toggle-btn">EN</button>\n                <!-- Theme Switch -->')

# Add data-en / data-de to logo subtitle
html = html.replace('<div class="logo-subtitle">Twitch Moderator & Event Coordinator</div>', '<div class="logo-subtitle" data-en="Twitch Moderator & Event Coordinator" data-de="Twitch Moderator & Event Koordinator">Twitch Moderator & Event Coordinator</div>')

# Add data-en / data-de to roles link
html = html.replace('<a href="/roles" class="nav-text-link">Roles</a>', '<a href="/roles" class="nav-text-link" data-en="Roles" data-de="Rollen">Roles</a>')

# Add data-en / data-de to headline
old_headline = '''<h1 class="headline fade-up delay-1">
                    Your stream.<br>
                    <span class="highlight">Your rules.</span>
                </h1>'''
new_headline = '''<h1 class="headline fade-up delay-1" data-en="Your stream.<br><span class=&quot;highlight&quot;>Your rules.</span>" data-de="Dein Stream.<br><span class=&quot;highlight&quot;>Deine Regeln.</span>">
                    Your stream.<br>
                    <span class="highlight">Your rules.</span>
                </h1>'''
html = html.replace(old_headline, new_headline)

# Add data-en / data-de to subtitle
old_sub = '''<p class="subtitle fade-up delay-2">
                    A great moderator has your back. We manage the chat and handle the background tasks, so you can focus 100% on entertaining your community.
                </p>'''
new_sub = '''<p class="subtitle fade-up delay-2" data-en="A great moderator has your back. We manage the chat and handle the background tasks, so you can focus 100% on entertaining your community." data-de="Ein guter Moderator hält dir den Rücken frei. Wir managen den Chat und erledigen die Hintergrundaufgaben, damit du dich zu 100% auf die Unterhaltung deiner Community konzentrieren kannst.">
                    A great moderator has your back. We manage the chat and handle the background tasks, so you can focus 100% on entertaining your community.
                </p>'''
html = html.replace(old_sub, new_sub)

# Add span to Join Discord
old_discord = '''</svg>
                        Join Discord
                    </a>'''
new_discord = '''</svg>
                        <span data-en="Join Discord" data-de="Discord beitreten">Join Discord</span>
                    </a>'''
html = html.replace(old_discord, new_discord)

# Add stats section after hero section
stats_section = '''    <!-- Stats Section -->
    <section class="stats-section fade-up delay-1">
        <div class="stats-container">
            <div class="stat-item">
                <h3 class="stat-number"><span class="counter" data-target="130">0</span>+</h3>
                <p class="stat-label" data-en="Streamers" data-de="Streamer">Streamers</p>
            </div>
            <div class="stat-item">
                <h3 class="stat-number"><span class="counter" data-target="5">0</span>+</h3>
                <p class="stat-label" data-en="Years Experience" data-de="Jahre Erfahrung">Years Experience</p>
            </div>
            <div class="stat-item">
                <h3 class="stat-number"><span class="counter" data-target="15">0</span>M+</h3>
                <p class="stat-label" data-en="Total Followers" data-de="Gesamtfollower">Total Followers</p>
            </div>
        </div>
    </section>

    <!-- Tooling Section -->'''
html = html.replace('<!-- Tooling Section -->', stats_section)

# Tooling badges and text
html = html.replace('<div class="chatty-badge">Moderation Tool</div>', '<div class="chatty-badge" data-en="Moderation Tool" data-de="Moderations-Tool">Moderation Tool</div>')
html = html.replace('<h2>I use <span class="chatty-highlight">Chatty</span> <img src="32.png" alt="Chatty Icon" class="chatty-inline-icon"></h2>', '<h2 data-en="I use <span class=&quot;chatty-highlight&quot;>Chatty</span> <img src=&quot;32.png&quot; alt=&quot;Chatty Icon&quot; class=&quot;chatty-inline-icon&quot;>" data-de="Ich nutze <span class=&quot;chatty-highlight&quot;>Chatty</span> <img src=&quot;32.png&quot; alt=&quot;Chatty Icon&quot; class=&quot;chatty-inline-icon&quot;>">I use <span class="chatty-highlight">Chatty</span> <img src="32.png" alt="Chatty Icon" class="chatty-inline-icon"></h2>')
html = html.replace('<p>I use the chat tool <a href="https://chatty.github.io/" target="_blank" rel="noopener noreferrer">Chatty</a> to moderate streamers because it is much clearer and easier to follow in fast-moving chats.</p>', '<p data-en="I use the chat tool <a href=&quot;https://chatty.github.io/&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;>Chatty</a> to moderate streamers because it is much clearer and easier to follow in fast-moving chats." data-de="Ich nutze das Chat-Tool <a href=&quot;https://chatty.github.io/&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;>Chatty</a>, um Streamer zu moderieren, da es viel übersichtlicher ist und es leichter fällt, schnellen Chats zu folgen.">I use the chat tool <a href="https://chatty.github.io/" target="_blank" rel="noopener noreferrer">Chatty</a> to moderate streamers because it is much clearer and easier to follow in fast-moving chats.</p>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

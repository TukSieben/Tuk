import re

streamers = [
    ("funnymike", "33,100,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/a14ac3ab-e622-41f5-ad66-b115e154b58f-profile_image-300x300.png"),
    ("yaboyyywill", "13,000,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/58c15d49-5152-408e-99aa-6d85cfbff149-profile_image-300x300.png"),
    ("PlaqueBoyMax", "6,000,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/14f0fcfd-00d4-4004-9379-93e0c6336f5e-profile_image-300x300.png"),
    ("ilikehaskell", "4,500,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/47926a3e-8f58-48ea-8e3c-a81197906175-profile_image-300x300.png"),
    ("Amar", "3,500,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/a1f93c9d-7fb0-4af8-aba9-86f64f956d55-profile_image-300x300.png"),
    ("xRohat", "2,500,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/dc99030e-69b1-4e11-b381-e1507c991ff0-profile_image-300x300.png"),
    ("Letshe", "2,500,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/ac84abbb-11dc-47e2-a156-c1b9411264b2-profile_image-300x300.png"),
    ("marco_scm", "1,500,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/e3670edc-cbb1-4ff2-bf2e-3593b44495f8-profile_image-300x300.png"),
    ("reemknocks", "1,000,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/c0bc29bf-12eb-49c9-85a0-422acb35ea3d-profile_image-300x300.png"),
    ("chefstrobel", "970,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/cea26e66-4095-4c3e-8467-c4d46fd7aaf6-profile_image-300x300.png"),
    ("noahreyli", "900,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/7ec428c9-c18c-455e-ab4a-8c4ddce872b6-profile_image-300x300.png"),
    ("timgioh", "730,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/ef50d7aa-f208-48e8-a497-3971073888c6-profile_image-300x300.png"),
    ("julistria", "140,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/416a09b8-1334-434b-b9d0-d8f65e6e86ac-profile_image-300x300.png"),
    ("LENA", "50,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/9f603e20-6186-4112-a797-a38ec7165c49-profile_image-300x300.png"),
    ("Lele", "35,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/054eb80b-1fcb-4c16-b85b-7f63ebd01d85-profile_image-300x300.png"),
    ("Kanyuji", "28,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/8452f070-747c-4df7-80f4-7a1ce5c904c8-profile_image-300x300.png"),
    ("Regy", "15,000+ Reach", "https://static-cdn.jtvnw.net/jtv_user_pictures/27d4aa6d-bae3-4465-9b66-ca89fb480acf-profile_image-300x300.png")
]

grid_html = '\\n'
for i, (name, reach, avatar) in enumerate(streamers):
    delay = min((i % 6) + 1, 6)
    grid_html += f'''                <a href="https://twitch.tv/{name}" target="_blank" rel="noopener noreferrer" class="streamer-card fade-up delay-{delay}">
                    <img src="{avatar}" alt="{name}" class="streamer-avatar">
                    <div class="streamer-info">
                        <h3>{name} <img src="https://static-cdn.jtvnw.net/badges/v1/d12a2e27-16f6-41d0-ab77-b780518f00a3/2" alt="Verified" class="verified-badge"></h3>
                        <p class="followers"><span style="color: #ffffff; font-weight: 600;">{reach.split(" ")[0]}</span> <i style="color: var(--text-secondary);">Reach</i></p>
                    </div>
                </a>\n\n'''

with open('roles/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace streamers-grid contents
pattern = re.compile(r'<div class="streamers-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
new_grid = f'<div class="streamers-grid">{grid_html}            </div>\n        </div>\n    </section>'
content = pattern.sub(new_grid, content)

with open('roles/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Roles page updated for reemknocks.")

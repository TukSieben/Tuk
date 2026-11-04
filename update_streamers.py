import re

streamers = [
    ("PlaqueBoyMax", 2875141, "https://static-cdn.jtvnw.net/jtv_user_pictures/cbfd449c-97b5-448c-82bd-f55b12cd4a97-profile_image-300x300.png"),
    ("Amar", 1876573, "https://static-cdn.jtvnw.net/jtv_user_pictures/a1f93c9d-7fb0-4af8-aba9-86f64f956d55-profile_image-300x300.png"),
    ("Letshe", 1820111, "https://static-cdn.jtvnw.net/jtv_user_pictures/ac84abbb-11dc-47e2-a156-c1b9411264b2-profile_image-300x300.png"),
    ("funnymike", 1604997, "https://static-cdn.jtvnw.net/jtv_user_pictures/a14ac3ab-e622-41f5-ad66-b115e154b58f-profile_image-300x300.png"),
    ("xRohat", 1370420, "https://static-cdn.jtvnw.net/jtv_user_pictures/dc99030e-69b1-4e11-b381-e1507c991ff0-profile_image-300x300.png"),
    ("noahreyli", 795353, "https://static-cdn.jtvnw.net/jtv_user_pictures/1a0db90e-6af8-4b5e-b933-6ce0cd1093dc-profile_image-300x300.png"),
    ("chefstrobel", 730726, "https://static-cdn.jtvnw.net/jtv_user_pictures/cea26e66-4095-4c3e-8467-c4d46fd7aaf6-profile_image-300x300.png"),
    ("marco_scm", 560437, "https://static-cdn.jtvnw.net/jtv_user_pictures/e3670edc-cbb1-4ff2-bf2e-3593b44495f8-profile_image-300x300.png"),
    ("timgioh", 481376, "https://static-cdn.jtvnw.net/jtv_user_pictures/ef50d7aa-f208-48e8-a497-3971073888c6-profile_image-300x300.png"),
    ("ilikehaskell", 461664, "https://static-cdn.jtvnw.net/jtv_user_pictures/47926a3e-8f58-48ea-8e3c-a81197906175-profile_image-300x300.png"),
    ("reemknocks", 427041, "https://static-cdn.jtvnw.net/jtv_user_pictures/c0bc29bf-12eb-49c9-85a0-422acb35ea3d-profile_image-300x300.png"),
    ("yaboyyywill", 175690, "https://static-cdn.jtvnw.net/jtv_user_pictures/58c15d49-5152-408e-99aa-6d85cfbff149-profile_image-300x300.png"),
    ("corey2u", 148384, "https://static-cdn.jtvnw.net/jtv_user_pictures/77646afc-a034-4ee8-a4a0-9e9f08c66bf6-profile_image-300x300.png"),
    ("tthereal65", 61036, "https://static-cdn.jtvnw.net/jtv_user_pictures/c9d4df91-9714-406f-b622-6266316d56b2-profile_image-300x300.png"),
    ("LENA", 40141, "https://static-cdn.jtvnw.net/jtv_user_pictures/9f603e20-6186-4112-a797-a38ec7165c49-profile_image-300x300.png"),
    ("julistria", 37705, "https://static-cdn.jtvnw.net/jtv_user_pictures/416a09b8-1334-434b-b9d0-d8f65e6e86ac-profile_image-300x300.png"),
    ("Lele", 26342, "https://static-cdn.jtvnw.net/jtv_user_pictures/054eb80b-1fcb-4c16-b85b-7f63ebd01d85-profile_image-300x300.png"),
    ("risukuni", 24047, "https://static-cdn.jtvnw.net/jtv_user_pictures/c09194f8-1695-4f45-b8f0-9fc388f23e5e-profile_image-300x300.png"),
    ("Regy", 14392, "https://static-cdn.jtvnw.net/jtv_user_pictures/7a27cdb6-0974-4703-975a-1d6d7952b007-profile_image-300x300.png"),
    ("Kanyuji", 11642, "https://static-cdn.jtvnw.net/jtv_user_pictures/d8573d63-4cad-4c4f-894a-0b44a5bc4cde-profile_image-300x300.png")
]

grid_html = '\n'
for i, (name, followers, avatar) in enumerate(streamers):
    delay = (i % 4) + 1
    grid_html += f'''            <a href="https://twitch.tv/{name}" target="_blank" rel="noopener noreferrer" class="streamer-card fade-up delay-{delay}">
                <img src="{avatar}" alt="{name}" class="streamer-avatar">
                <div class="streamer-info">
                    <h3>{name} <img src="https://static-cdn.jtvnw.net/badges/v1/d12a2e27-16f6-41d0-ab77-b780518f00a3/2" alt="Verified" class="verified-badge"></h3>
                    <p class="followers">{followers:,} followers</p>
                </div>
                <svg class="streamer-arrow" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>\n\n'''

with open('roles/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<div class="streamers-grid">.*?</div>\s*</main>', re.DOTALL)
new_grid = f'<div class="streamers-grid">{grid_html}        </div>\n    </main>'
content = pattern.sub(new_grid, content)

with open('roles/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Roles page updated.")

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

stats_pattern = re.compile(r'(\s*<!-- Stats Section -->\s*<section class="stats-section.*?</section>)', re.DOTALL)
stats_match = stats_pattern.search(html)

if stats_match:
    stats_block = stats_match.group(1)
    # Remove from current location
    html = html.replace(stats_block, '')
    
    # Insert before Simple Footer
    html = html.replace('    <!-- Simple Footer -->', stats_block.lstrip() + '\n\n    <!-- Simple Footer -->')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

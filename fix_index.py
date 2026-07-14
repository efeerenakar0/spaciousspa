import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 2. Alesta
alesta_block = re.search(r'(<!-- 2\. Alesta Spacious Spa -->.*?<div class="branch-actions">)(.*?)(</div>)', html, re.DOTALL)
if alesta_block:
    new_actions = alesta_block.group(2).replace('sube-deluxe.html', 'sube-alesta.html')
    html = html[:alesta_block.start(2)] + new_actions + html[alesta_block.end(2):]

# 3. Ramada
ramada_block = re.search(r'(<!-- 3\. Ramada Spacious Spa -->.*?<div class="branch-actions">)(.*?)(</div>)', html, re.DOTALL)
if ramada_block:
    new_actions = ramada_block.group(2).replace('sube-deluxe.html', 'sube-ramada.html')
    html = html[:ramada_block.start(2)] + new_actions + html[ramada_block.end(2):]

# 4. Euro Park
euro_block = re.search(r'(<!-- 4\. Euro Park Spacious Spa -->.*?<div class="branch-actions">)(.*?)(</div>)', html, re.DOTALL)
if euro_block:
    new_actions = euro_block.group(2).replace('sube-deluxe.html', 'sube-europark.html')
    html = html[:euro_block.start(2)] + new_actions + html[euro_block.end(2):]

# 5. Garcia
garcia_block = re.search(r'(<!-- 5\. Garcia Resort Spa -->.*?<div class="branch-actions">)(.*?)(</div>)', html, re.DOTALL)
if garcia_block:
    new_actions = garcia_block.group(2).replace('sube-deluxe.html', 'sube-garcia.html')
    html = html[:garcia_block.start(2)] + new_actions + html[garcia_block.end(2):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

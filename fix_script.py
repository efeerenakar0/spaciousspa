with open('generate_branch_pages.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re

# Protect names in python dictionary
code = code.replace('"Deluxe Spacious Spa"', '"<span class=\\"notranslate\\">Deluxe Spacious Spa</span>"')
code = code.replace('"Alesta Spacious Spa"', '"<span class=\\"notranslate\\">Alesta Spacious Spa</span>"')
code = code.replace('"Ramada Spacious Spa"', '"<span class=\\"notranslate\\">Ramada Spacious Spa</span>"')
code = code.replace('"Euro Park Spacious Spa"', '"<span class=\\"notranslate\\">Euro Park Spacious Spa</span>"')
code = code.replace('"Garcia Resort Spa"', '"<span class=\\"notranslate\\">Garcia Resort Spa</span>"')

with open('generate_branch_pages.py', 'w', encoding='utf-8') as f:
    f.write(code)

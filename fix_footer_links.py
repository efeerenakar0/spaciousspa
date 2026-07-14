with open('generate_branch_pages.py', 'r') as f:
    code = f.read()

replacement = """    for sec in sections:
        header_part = header_part.replace(f'href="#{sec}"', f'href="index.html#{sec}"')
        footer_part = footer_part.replace(f'href="#{sec}"', f'href="index.html#{sec}"')"""

code = code.replace("""    for sec in sections:
        header_part = header_part.replace(f'href="#{sec}"', f'href="index.html#{sec}"')""", replacement)

with open('generate_branch_pages.py', 'w') as f:
    f.write(code)

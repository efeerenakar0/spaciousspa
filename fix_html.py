import re
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix alt attributes: 
    # Find `alt="... <span class="[ ]*notranslate">...</span> ..."`
    # It might be `alt="Deluxe <span class=" notranslate">Spacious Spa</span>"`
    # The double quote on class=" terminates the alt attribute early!
    
    # We will simply find any `<span class="notranslate">` or `<span class=" notranslate">` and `</span>` 
    # that are inside an `alt` or `href` attribute. Since the HTML is technically broken, standard regex is tricky,
    # but we can just replace the specific literal broken strings!
    
    bad_strings = [
        ('alt="Deluxe <span class=" notranslate">Spacious Spa</span>"', 'alt="Deluxe Spacious Spa"'),
        ('alt="Alesta <span class=" notranslate">Spacious Spa</span>"', 'alt="Alesta Spacious Spa"'),
        ('alt="Ramada <span class=" notranslate">Spacious Spa</span>"', 'alt="Ramada Spacious Spa"'),
        ('alt="Euro Park <span class=" notranslate">Spacious Spa</span>"', 'alt="Euro Park Spacious Spa"'),
        ('alt="<span class="notranslate">Deluxe Spacious Spa</span> Görseli"', 'alt="Deluxe Spacious Spa Görseli"'),
        ('alt="<span class="notranslate">Alesta Spacious Spa</span> Görseli"', 'alt="Alesta Spacious Spa Görseli"'),
        ('alt="<span class="notranslate">Ramada Spacious Spa</span> Görseli"', 'alt="Ramada Spacious Spa Görseli"'),
        ('alt="<span class="notranslate">Garcia Resort Spa</span> Görseli"', 'alt="Garcia Resort Spa Görseli"'),
        ('alt="<span class="notranslate">Euro Park Spacious Spa</span> Görseli"', 'alt="Euro Park Spacious Spa Görseli"'),
        ('alt="<span class="notranslate">Spacious Spa</span> Görseli"', 'alt="Spacious Spa Görseli"'),
        ('alt="<span class=" notranslate">Deluxe Spacious Spa</span> Görseli"', 'alt="Deluxe Spacious Spa Görseli"'),
        ('alt="<span class=" notranslate">Alesta Spacious Spa</span> Görseli"', 'alt="Alesta Spacious Spa Görseli"'),
        ('alt="<span class=" notranslate">Ramada Spacious Spa</span> Görseli"', 'alt="Ramada Spacious Spa Görseli"'),
        ('alt="<span class=" notranslate">Garcia Resort Spa</span> Görseli"', 'alt="Garcia Resort Spa Görseli"'),
        ('href="https://wa.me/905161664800?text=Merhaba, <span class="notranslate">Spacious Spa</span> hakkında bilgi almak\n    istiyorum."', 'href="https://wa.me/905161664800?text=Merhaba, Spacious Spa hakkında bilgi almak istiyorum."'),
        ('href="https://wa.me/905161664800?text=Merhaba, <span class=" notranslate">Spacious Spa</span> hakkında bilgi almak\n    istiyorum."', 'href="https://wa.me/905161664800?text=Merhaba, Spacious Spa hakkında bilgi almak istiyorum."')
    ]
    
    for bad, good in bad_strings:
        content = content.replace(bad, good)
        
    # Just in case there are others
    content = re.sub(r'alt="([^"]*)<span class=" ?notranslate">([^<]*)</span>([^"]*)"', r'alt="\1\2\3"', content)
    
    # Let's also do a general replace for the multiline href issue just in case the spaces don't match exactly
    content = re.sub(r'href="https://wa.me/905161664800\?text=Merhaba, <span class=" ?notranslate">Spacious Spa</span> hakkında bilgi almak\s*istiyorum."', 'href="https://wa.me/905161664800?text=Merhaba, Spacious Spa hakkında bilgi almak istiyorum."', content, flags=re.MULTILINE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for html_file in glob.glob('*.html'):
    fix_file(html_file)

print("Done fixing HTML files.")

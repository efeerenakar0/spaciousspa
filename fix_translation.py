import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add notranslate to brand names
names_to_protect = [
    "Spacious Spa",
    "Deluxe Spacious Spa",
    "Alesta Spacious Spa",
    "Ramada Spacious Spa",
    "Euro Park Spacious Spa",
    "Garcia Resort Spa",
    "Alesta Yacht Hotel",
    "Ramada by Wyndham",
    "Euro Park Hotel",
    "Garcia Resort"
]

# We need to be careful not to wrap something that's already inside a tag attribute or already wrapped.
# A safe way is to replace only when not inside a tag.
# For simplicity, we can do targeted replacements on known structures, or use a regex that avoids tags.
def wrap_notranslate(match):
    return f'<span class="notranslate">{match.group(0)}</span>'

for name in names_to_protect:
    # Replace the name only if it is NOT preceded by <span class="notranslate"> and NOT inside an HTML tag attribute.
    # Actually, a simpler way since we control the HTML is to just replace the text directly.
    # But wait, we might mess up alt="Spacious Spa" or similar attributes.
    # So we replace >Spacious Spa< or similar, but it can be at the start or end of text.
    # Let's use negative lookahead and lookbehind to avoid replacing inside attributes like alt="Spacious Spa"
    # or inside already wrapped <span class="notranslate">Spacious Spa</span>
    pattern = r'(?<!<span class="notranslate">)(?<!alt=")(?<!title=")(?<!content=")(?<!@)' + re.escape(name) + r'(?!</span>)'
    html = re.sub(pattern, wrap_notranslate, html)

# 2. Translate Services section to English
services_start = html.find('<!-- ====== SERVICES ====== -->')
services_end = html.find('<!-- ====== PRICING ====== -->')

if services_start != -1 and services_end != -1:
    services_html = html[services_start:services_end]
    
    # Do replacements in services_html
    services_html = services_html.replace('Hizmetlerimiz', 'Our Services')
    services_html = services_html.replace('Ruhunuzu ve bedeninizi yenileyecek size özel lüks spa bakımlarını keşfedin.', 'Discover our exclusive luxury spa treatments designed to rejuvenate your body and soul.')
    
    # Kapalı Yüzme Havuzu -> Indoor Swimming Pool
    services_html = services_html.replace('Kapalı Yüzme Havuzu', 'Indoor Swimming Pool')
    services_html = services_html.replace('Şubelerimizde bulunan ferah ve ısıtmalı kapalı yüzme havuzlarında rahatlayın.', 'Relax in our spacious and heated indoor swimming pools available at our branches.')
    
    # Replace "Randevu Al" with "Book Now" inside service cards
    services_html = services_html.replace('Randevu Al', 'Book Now')
    
    # The titles like Turkish Hammam, Balinese Massage, etc. are already mostly English!
    # Wait, some text inside the cards is Turkish:
    services_html = services_html.replace('Geleneksel kese ve köpük masajı ile cildinizi arındıran eşsiz hamam ritüeli.', 'A unique hammam ritual that purifies your skin with traditional scrub and foam massage.')
    services_html = services_html.replace('Uzak Doğu\'nun mistik dokunuşlarıyla derin bir rahatlama ve stresten arınma deneyimi.', 'A deep relaxation and stress relief experience with the mystical touches of the Far East.')
    services_html = services_html.replace('Kas gerginliklerini azaltan, güçlü ve derin doku baskı teknikleri uygulanan masaj.', 'A massage applying strong and deep tissue pressure techniques to reduce muscle tension.')
    services_html = services_html.replace('Kan dolaşımını hızlandıran, vücudu rahatlatan klasik ve yumuşak İsveç tekniği.', 'A classic and gentle Swedish technique that accelerates blood circulation and relaxes the body.')
    services_html = services_html.replace('Doğal bitki öz yağlarıyla uygulanan, ruhu ve bedeni dinlendiren kokulu masaj.', 'A fragrant massage applied with natural essential oils, soothing the body and soul.')
    services_html = services_html.replace('Isıtılmış volkanik taşlarla enerji noktalarınıza uygulanan şifalı terapi.', 'A healing therapy applied to your energy points with heated volcanic stones.')
    services_html = services_html.replace('Esneme ve baskı hareketleriyle bedene esneklik kazandıran uzak doğu masajı.', 'A Far Eastern massage that provides flexibility to the body through stretching and pressure movements.')
    services_html = services_html.replace('Eşiniz veya sevdiklerinizle aynı odada paylaşılan özel masaj deneyimi.', 'A special massage experience shared in the same room with your partner or loved ones.')
    services_html = services_html.replace('Ayak tabanındaki belirli noktalara uygulanan baskı ile tüm vücudu rahatlatma tekniği.', 'A technique to relax the entire body through pressure applied to specific points on the soles of the feet.')
    services_html = services_html.replace('Günün yorgunluğunu atan, ayak ve bacak bölgesine odaklı özel masaj.', 'A special massage focused on the foot and leg area, relieving the tiredness of the day.')
    services_html = services_html.replace('Lüks ürünlerle uygulanan derinlemesine cilt temizliği ve anti-aging bakımları.', 'Deep skin cleansing and anti-aging treatments applied with luxury products.')
    services_html = services_html.replace('Doğal peeling ürünleri ile ölü derilerden arınan pürüzsüz bir vücut bakımı.', 'A smooth body treatment that purifies dead skin cells using natural peeling products.')
    services_html = services_html.replace('Geleneksel köpük bulutları arasında kaslarınızı gevşeten rahatlatıcı masaj.', 'A relaxing massage that loosens your muscles amidst clouds of traditional foam.')
    services_html = services_html.replace('Mineral bakımından zengin doğal çamur ile toksin atıcı yenileyici vücut sargısı.', 'A detoxifying and renewing body wrap with mineral-rich natural mud.')
    services_html = services_html.replace('Tamamen size özel ayrılmış VIP odalarda ayrıcalıklı spa deneyimi.', 'An exclusive spa experience in VIP rooms reserved entirely for you.')
    
    html = html[:services_start] + services_html + html[services_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Turkish Hammam
html = html.replace('<img src="turkish_hamam_1783703968279.jpg" alt="Turkish Hammam"', '<img src="images/hamam_kurna.jpg" alt="Turkish Hammam"')

# 2. Couple Massage
html = html.replace('<img src="spa_massage_1783703978608.jpg" alt="Couple Massage"', '<img src="images/hamam_cift.jpg" alt="Couple Massage"')

# 3. Foam Massage
html = html.replace('<img src="turkish_hamam_1783703968279.jpg" alt="Foam Massage"', '<img src="images/kopuk_masaji.jpg" alt="Foam Massage"')

# 4. Foot Massage
html = html.replace('<img src="spa_massage_1783703978608.jpg" alt="Foot Massage"', '<img src="images/ayak_masaji.jpg" alt="Foot Massage"')

# 5. Swimming Pool
old_pool = """    <div class="service-card reveal-up delay-2">
      <div class="card-image"><img src="spa_hero_pool_1783703958490.jpg" alt="Spa Rituals" loading="lazy"/><div class="card-overlay"><a href="#contact" class="card-btn">Randevu Al</a></div></div>
      <div class="card-body">
        <h3 class="card-title">Spa Rituals</h3>
        <p class="card-text">Tepeden tırnağa yenilenmenizi sağlayan, çoklu bakımların birleştiği ritüeller.</p>"""

new_pool = """    <div class="service-card reveal-up delay-2">
      <div class="card-image"><img src="images/yuzme_havuzu.jpg" alt="Indoor Pool" loading="lazy"/><div class="card-overlay"><a href="#contact" class="card-btn">Randevu Al</a></div></div>
      <div class="card-body">
        <h3 class="card-title">Kapalı Yüzme Havuzu</h3>
        <p class="card-text">Şubelerimizde bulunan ferah ve ısıtmalı kapalı yüzme havuzlarında rahatlayın.</p>"""

html = html.replace(old_pool, new_pool)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

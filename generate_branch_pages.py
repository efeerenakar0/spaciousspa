import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    header_match = re.search(r'(.*?</header>)', html, re.DOTALL)
    header_part = header_match.group(1) if header_match else ""

    footer_match = re.search(r'(<!-- ====== CONTACT & MAP ====== -->.*)', html, re.DOTALL)
    footer_part = footer_match.group(1) if footer_match else ""

    sections = ['home', 'about', 'services', 'prices', 'branches', 'gallery', 'faq']
    for sec in sections:
        header_part = header_part.replace(f'href="#{sec}"', f'href="index.html#{sec}"')
        footer_part = footer_part.replace(f'href="#{sec}"', f'href="index.html#{sec}"')

    branches = [
        {
            "id": "deluxe", "name": "<span class=\"notranslate\">Deluxe Spacious Spa</span>", "location": "Fethiye Merkez / Muğla", "bg": "spa_reception_1783704904680.jpg",
            "desc": "Fethiye'nin merkezinde, karmaşadan uzak ve bir o kadar ulaşılabilir konumda yer alan Deluxe şubemiz, size en üst düzey spa deneyimini sunmak için özel olarak tasarlandı. Otantik atmosferi, alanında uzman terapistleri ve premium VIP odaları ile ruhunuzu ve bedeninizi şımartın.",
            "features": [
                {"icon": "fa-fire-flame-curved", "title": "Geleneksel Türk Hamamı", "text": "Özel mermer göbek taşı ile otantik arınma."},
                {"icon": "fa-spa", "title": "Uzak Doğu Masajları", "text": "Bali ve Thai terapistlerinden imza masajlar."},
                {"icon": "fa-gem", "title": "VIP Süitler", "text": "Çiftlere özel jakuzili terapi odaları."},
                {"icon": "fa-mug-hot", "title": "Detox Bar", "text": "Masaj sonrası bitki çayı ve taze meyve sunumu."}
            ]
        },
        {
            "id": "alesta", "name": "<span class=\"notranslate\">Alesta Spacious Spa</span>", "location": "Alesta Yacht Hotel, Fethiye", "bg": "alesta_yacht_1783956682857.jpg",
            "desc": "Denizin mavisiyle huzurun buluştuğu nokta. Alesta Yacht Hotel bünyesindeki şubemiz, marinaya karşı rahatlatıcı bir gün geçirmek isteyenler için butik ve lüks bir hizmet sunuyor. Lüks otel konforunda dünya standartlarında bakım ritüellerini keşfedin.",
            "features": [
                {"icon": "fa-water", "title": "Kapalı Yüzme Havuzu", "text": "Sakin ve ısıtmalı havuz alanımız."},
                {"icon": "fa-temperature-high", "title": "Modern Sauna", "text": "Doğal ahşap dokulu rahatlatıcı sauna odası."},
                {"icon": "fa-hot-tub-person", "title": "Buhar Odası", "text": "Geniş ve ferah buhar terapisi alanı."},
                {"icon": "fa-hands", "title": "Klasik Masajlar", "text": "Avrupa ve aromaterapi masaj seçenekleri."}
            ]
        },
        {
            "id": "ramada", "name": "<span class=\"notranslate\">Ramada Spacious Spa</span>", "location": "Ramada by Wyndham, Fethiye", "bg": "ramada_hotel_1783956693354.jpg",
            "desc": "Ramada by Wyndham Fethiye kalitesiyle entegre olan bu geniş spa merkezimiz, büyük gruplar ve kurumsal müşterilerimiz için de idealdir. Kapsamlı fitness ve ıslak alan kullanımıyla tam donanımlı bir sağlıklı yaşam kompleksi.",
            "features": [
                {"icon": "fa-dumbbell", "title": "Fitness Merkezi", "text": "Profesyonel ekipmanlarla donatılmış spor salonu."},
                {"icon": "fa-swimming-pool", "title": "Geniş Havuz Alanı", "text": "Yarı olimpik ölçülerde dinlenme havuzu."},
                {"icon": "fa-shower", "title": "Şok Duşları", "text": "Hamam sonrası canlandırıcı şok duş sistemi."},
                {"icon": "fa-leaf", "title": "Cilt ve Vücut Bakımı", "text": "Premium markalarla uygulanan özel kürler."}
            ]
        },
        {
            "id": "europark", "name": "<span class=\"notranslate\">Euro Park Spacious Spa</span>", "location": "Euro Park Hotel, Bursa", "bg": "europark_bursa_1783956734470.jpg",
            "desc": "Bursa'nın termal geleneğini modern spa anlayışımızla buluşturuyoruz. Euro Park Hotel içerisindeki şubemiz, hem iş seyahatlerinizde stres atmak hem de hafta sonu kaçamaklarında yenilenmek için eşsiz bir atmosfere sahip.",
            "features": [
                {"icon": "fa-fire", "title": "Termal Sular", "text": "Bursa'nın şifalı sularıyla zenginleşen banyolar."},
                {"icon": "fa-house-chimney-medical", "title": "Tuz Odası", "text": "Solunum yollarını rahatlatan Himalaya tuz terapisi."},
                {"icon": "fa-bed", "title": "Dinlenme Lounge", "text": "Sessiz, loş ve huzur dolu dinlenme alanları."},
                {"icon": "fa-hand-sparkles", "title": "Medikal Masaj", "text": "Uzmanlar tarafından uygulanan tedavi destekli masajlar."}
            ]
        },
        {
            "id": "garcia", "name": "<span class=\"notranslate\">Garcia Resort Spa</span>", "location": "Garcia Resort, Ölüdeniz", "bg": "garcia_resort_1783956673577.jpg",
            "desc": "Ölüdeniz'in büyüleyici manzarası eşliğinde doğayla iç içe bir arınma deneyimi. Garcia Resort şubemiz, yeşilin ve mavinin ortasında, tropikal esintili açık hava masaj pavilyonları ve lüks bakım menüsüyle sizi şımartacak.",
            "features": [
                {"icon": "fa-umbrella-beach", "title": "Açık Hava Pavilyonları", "text": "Doğa manzarasına karşı esintili masaj deneyimi."},
                {"icon": "fa-seedling", "title": "Organik Bakımlar", "text": "Tamamen doğal yağlar ve organik ürünler."},
                {"icon": "fa-person-swimming", "title": "Sonsuzluk Havuzu", "text": "Ölüdeniz manzaralı etkileyici dinlenme havuzu."},
                {"icon": "fa-yin-yang", "title": "Asya Terapileri", "text": "Uzak doğu felsefesine dayalı enerji dengeleyici seanslar."}
            ]
        }
    ]

    for b in branches:
        features_html = ""
        for feat in b['features']:
            features_html += f"""
        <div class="feature-item reveal-up" style="background:#fff; border:1px solid var(--border); box-shadow:none;">
            <div class="feature-icon" style="margin: 0 auto 15px;"><i class="fa {feat['icon']}"></i></div>
            <h4 style="font-family:var(--font-heading); color:var(--dark); margin-bottom:10px; font-size:20px;">{feat['title']}</h4>
            <p style="font-size:14px; color:var(--gray);">{feat['text']}</p>
        </div>"""

        branch_html = f"""
{header_part}

<!-- ====== BRANCH HERO ====== -->
<section class="hero" style="min-height: 65vh; background: url('{b['bg']}') center/cover no-repeat; position: relative;">
  <div class="hero-overlay" style="background: rgba(0,0,0,0.5);"></div>
  <div class="hero-content reveal-fade" style="text-align:center; position:relative; z-index:2; padding-top:80px;">
    <div style="display:inline-block; padding:8px 16px; background:var(--accent); color:#fff; border-radius:30px; font-size:13px; font-weight:600; letter-spacing:2px; text-transform:uppercase; margin-bottom:20px;">Lüks SPA Deneyimi</div>
    <h1 class="hero-title" style="font-size: clamp(36px, 6vw, 56px); margin-bottom:15px;">{b['name']}</h1>
    <p class="hero-subtitle" style="font-size:18px; font-weight:400;"><i class="fa fa-map-marker-alt" style="color:var(--accent); margin-right:8px;"></i> {b['location']}</p>
  </div>
</section>

<!-- ====== BRANCH DETAILS & AMENITIES ====== -->
<section class="about" style="padding: 100px 20px; background: var(--cream);">
  <div style="max-width: 1200px; margin: 0 auto;">
    
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:60px; align-items:center; margin-bottom:80px;">
        <div class="reveal-left">
            <p class="section-label" style="text-align:left;">Bizimle Tanışın</p>
            <h2 class="section-title" style="text-align:left; margin-bottom:20px;">{b['name']} Hakkında</h2>
            <div class="divider-leaf" style="justify-content:flex-start;"><span></span><i class="fa fa-leaf"></i><span></span></div>
            <p style="font-size:16px; color:var(--gray); line-height:1.8; margin-bottom:30px;">{b['desc']}</p>
            <a href="#contact" class="btn btn-dark"><i class="fa fa-calendar-check"></i> Hemen Randevu Al</a>
        </div>
        <div class="reveal-right" style="position:relative;">
            <img src="{b['bg']}" alt="{b['name']} Görseli" style="width:100%; border-radius:12px; box-shadow:var(--shadow-md);" />
            <div style="position:absolute; bottom:-30px; left:-30px; background:var(--white); padding:30px; border-radius:12px; box-shadow:var(--shadow-lg);">
                <div style="font-family:var(--font-heading); font-size:48px; color:var(--accent); line-height:1;">5<i class="fa fa-star" style="font-size:24px; vertical-align:middle;"></i></div>
                <div style="font-size:14px; font-weight:600; letter-spacing:1px; color:var(--dark);">Mükemmeliyet</div>
            </div>
        </div>
    </div>

    <!-- Amenities Grid -->
    <div style="text-align:center; margin-bottom:50px;" class="reveal-up">
        <p class="section-label">Şubemize Özel</p>
        <h3 style="font-family:var(--font-heading); font-size:36px; color:var(--dark);">Hizmetler & İmkanlar</h3>
        <div class="divider-leaf"><span></span><i class="fa fa-leaf"></i><span></span></div>
    </div>
    
    <div class="features-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:24px;">
        {features_html}
    </div>

  </div>
</section>

{footer_part}
"""
        with open(f"sube-{b['id']}.html", 'w', encoding='utf-8') as out:
            out.write(branch_html)
            
    print("Created 5 highly professional branch pages successfully!")

if __name__ == '__main__':
    main()

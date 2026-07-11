import os

products = [
    {"id": "kordy_x", "name": "KORDY X", "price": "1,499", "old_price": "1,999", "image": "prod_kordy_x.png", "desc": "A masterpiece of modern nutraceutical science and ancient Ayurvedic wisdom. KORDY X is an effervescent powerhouse formulated to restore core vitality, enhance stamina, and combat daily fatigue instantly."},
    {"id": "ashwagandha", "name": "Ashwagandha Plus", "price": "1,899", "old_price": "2,499", "image": "prod_ashwagandha.png", "desc": "Stress & Vitality Support. A premium formulation designed to combat chronic stress, lower cortisol levels, and restore balance to your mind and body."},
    {"id": "shilajit", "name": "Shilajit Gold", "price": "3,299", "old_price": "4,499", "image": "prod_shilajit.png", "desc": "Himalayan Grade Shuddh Shilajit. Sourced from the highest altitudes, purified to perfection for maximum fulvic acid content and ultimate cellular rejuvenation."},
    {"id": "gokshura", "name": "Gokshura Power", "price": "1,799", "old_price": "2,299", "image": "prod_gokshura.png", "desc": "Male Vitality Support. Harness the power of pure Gokshura extract to naturally support stamina, muscle recovery, and overall physical performance."},
    {"id": "ginseng", "name": "Panax Ginseng", "price": "2,199", "old_price": "2,899", "image": "prod_ginseng.png", "desc": "Adaptogenic Energy Booster. High-potency Panax Ginseng root extract to provide sustained, jitter-free energy and enhance cognitive clarity throughout the day."},
    {"id": "chaste", "name": "Chaste Tree Blend", "price": "1,599", "old_price": "2,099", "image": "prod_chaste.png", "desc": "Hormonal Balance Support. A targeted botanical blend featuring premium Chaste Tree extract to gently support natural hormonal equilibrium and wellness."},
    {"id": "kordy_x_single", "name": "KORDY X (Single)", "price": "299", "old_price": "", "image": "prod_kordy_x.png", "desc": "Single-Tablet Format. Experience the instant vitality of KORDY X in a convenient trial size. Perfect for a quick energy boost on the go."},
    {"id": "joyflex", "name": "JOYFLEX PLUS", "price": "1,899", "old_price": "2,499", "image": "prod_joyflex.png", "desc": "Advanced Joint Relief Formula. A powerful synergistic blend of Ayurvedic herbs specifically chosen to support joint mobility, reduce inflammation, and promote cartilage health."}
]

with open("e:/ecc/product_details.html", "r", encoding="utf-8") as f:
    template = f.read()

for p in products:
    html = template
    
    # Replace Name
    html = html.replace(">KORDY X<", f">{p['name']}<")
    html = html.replace("KORDY X - Premium", f"{p['name']} - Premium")
    html = html.replace('alt="KORDY X"', f'alt="{p['name']}"')
    
    # Replace Price
    html = html.replace("₹1,499", f"₹{p['price']}")
    
    # Replace Old Price or remove it if empty
    if p['old_price']:
        html = html.replace("₹1,999", f"₹{p['old_price']}")
    else:
        # Remove the span with old price and the save badge
        html = html.replace('<span class="text-xl text-charcoal-900/40 line-through mb-1">₹1,999</span>', '')
        html = html.replace('<span class="bg-gold-100 text-gold-600 text-xs font-bold px-2 py-1 rounded-sm uppercase tracking-widest mb-2 border border-gold-200">Save 25%</span>', '')

    # Replace Image
    html = html.replace("prod_kordy_x.png", p['image'])
    
    # Replace Description (Only the first main description under the title)
    original_desc = "A masterpiece of modern nutraceutical science and ancient Ayurvedic wisdom. KORDY X is an effervescent powerhouse formulated to restore core vitality, enhance stamina, and combat daily fatigue instantly."
    html = html.replace(original_desc, p['desc'])
    
    # Output file
    filename = f"product_{p['id']}.html"
    with open(f"e:/ecc/{filename}", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {filename}")


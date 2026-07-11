import re

def update_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    products_mapping = {
        "KORDY X": "product_kordy_x.html",
        "Ashwagandha Plus": "product_ashwagandha.html",
        "Shilajit Gold": "product_shilajit.html",
        "Gokshura Power": "product_gokshura.html",
        "Panax Ginseng": "product_ginseng.html",
        "Chaste Tree Blend": "product_chaste.html",
        "KORDY X (Single)": "product_kordy_x_single.html",
        "JOYFLEX PLUS": "product_joyflex.html",
        "Shilajit Gold Resin": "product_shilajit.html"
    }

    # For products.html and index.html, we look for Add to Cart buttons or titles to replace
    # It's easier to find the titles: <h3 class="text-xl font-serif text-primary-900 mb-1">KORDY X</h3> or similar
    
    # We can use regex to find product cards and inject links
    # Let's replace the h3 titles to be clickable links
    for name, link in products_mapping.items():
        # index.html format
        pattern1 = f'<h3 class="text-xl font-serif text-primary-900 mb-1">{name}</h3>'
        replacement1 = f'<a href="{link}" class="hover:text-gold-600 transition-colors"><h3 class="text-xl font-serif text-primary-900 mb-1 hover:text-gold-600 transition-colors">{name}</h3></a>'
        content = content.replace(pattern1, replacement1)
        
        # products.html format
        pattern2 = f'<h3 class="text-xl mb-1 text-primary-900 font-serif">{name}</h3>'
        replacement2 = f'<a href="{link}" class="hover:text-gold-600 transition-colors"><h3 class="text-xl mb-1 text-primary-900 font-serif hover:text-gold-600 transition-colors">{name}</h3></a>'
        content = content.replace(pattern2, replacement2)
        
    # Let's also wrap the product images if possible
    # We'll just replace <div class="h-64 flex items-center justify-center mb-6 relative overflow-hidden rounded-2xl bg-earth-50 group-hover:bg-earth-100 transition-colors"> with an <a> tag in index.html? Too risky to break layout.
    
    # Let's change the "Add to Cart" button in products.html to have a "View Details" button next to it
    # <button class="w-full bg-gold-500 text-primary-900 hover:bg-gold-600 rounded-lg py-3 font-semibold uppercase tracking-wider text-sm transition-all duration-300 shadow-lg hover:shadow-gold-500/30" onclick="addToCart('KORDY X', 2499)">
    # Add to Cart
    # </button>
    
    # We will do a regex to replace the single Add to Cart button with a 2-column flex in products.html
    # This requires carefully matching the button
    
    button_pattern = re.compile(r'<button class="w-full bg-gold-500[^>]*onclick="addToCart\(\'([^\']+)\', \d+\)"[^>]*>\s*Add to Cart\s*</button>')
    
    def replacer(match):
        prod_name = match.group(1)
        link = products_mapping.get(prod_name, "#")
        original_button = match.group(0).replace('w-full', 'w-1/2')
        new_buttons = f'''<div class="flex gap-2">
                            <a href="{link}" class="w-1/2 text-center bg-primary-900 text-gold-400 hover:bg-primary-800 rounded-lg py-3 font-semibold uppercase tracking-wider text-[10px] transition-all duration-300 shadow-lg flex items-center justify-center">View</a>
                            {original_button.replace("text-sm", "text-[10px]").replace("w-1/2", "w-1/2 flex items-center justify-center")}
                          </div>'''
        return new_buttons
        
    content = button_pattern.sub(replacer, content)

    # In index.html, the Add to Cart button is different
    # <button onclick="addToCart(this)" class="w-full py-3 bg-white border border-primary-900 text-primary-900 hover:bg-primary-900 hover:text-gold-400 rounded-full text-xs uppercase tracking-widest font-semibold transition-all duration-300">
    
    # I'll just change the text of the KORDY X one to View Details just to be safe, but they have onclick
    # It's better to manually replace in index.html if needed. But titles are linked now, which is good enough!
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath}")

update_html("e:/ecc/products.html")
update_html("e:/ecc/index.html")


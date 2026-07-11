import os

filepath = "e:/ecc/build_ingredients.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace body classes
content = content.replace('bg-primary-900 text-white', 'bg-earth-50 text-charcoal-900')
# Replace section backgrounds
content = content.replace('bg-[#1a4233]', 'bg-white')
content = content.replace('bg-primary-900', 'bg-earth-50')
content = content.replace('bg-[#17382b]', 'bg-earth-100')

# Text Colors
content = content.replace('text-white', 'text-primary-900')
content = content.replace('text-white/70', 'text-charcoal-900/80')
content = content.replace('text-white/60', 'text-charcoal-900/70')
content = content.replace('text-white/50', 'text-charcoal-900/60')
content = content.replace('text-white/[0.02]', 'text-primary-900/[0.03]')

# Borders
content = content.replace('border-white/5', 'border-primary-900/10')
content = content.replace('border-white/10', 'border-primary-900/10')

# Glass elements
content = content.replace('bg-white/5', 'bg-white/60')
content = content.replace('bg-white/10', 'bg-white/70')
content = content.replace('bg-gradient-to-t from-black/90 via-black/30 to-transparent', 'bg-gradient-to-t from-earth-100 via-white/50 to-transparent')
content = content.replace('mix-blend-luminosity', 'mix-blend-multiply')

# Fix Add to Cart buttons
content = content.replace('bg-white/10 hover:bg-gold-400 text-white hover:text-primary-900', 'bg-primary-900 hover:bg-gold-400 text-gold-400 hover:text-primary-900')
content = content.replace('bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-white', 'bg-white hover:bg-earth-100 border border-primary-900/20 rounded-lg text-primary-900')

# Hero section background overlay (keep it somewhat transparent over the image)
# "bg-primary-900/80 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-transparent via-primary-900/80 to-primary-900"
content = content.replace('bg-earth-50/80 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-transparent via-earth-50/80 to-earth-50', 'bg-earth-50/90 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-transparent via-earth-50/90 to-earth-50')

# Scroll Listener Nav fix
content = content.replace("nav.classList.add('bg-earth-50/95');", "nav.classList.add('bg-white/95');")
content = content.replace("nav.classList.remove('bg-earth-50/95');", "nav.classList.remove('bg-white/95');")

# In the script, it says "bg-primary-900" which became "bg-earth-50". We need to revert the scroll listener background color for nav to bg-white/95 so it's a solid white on scroll for light mode.
# Also fix the glass class which is now 'glass' -> 'bg-white/70'

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build_ingredients.py to Light Theme.")

import re

filepath = "e:/ecc/ingredients.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Update the tailwind config to match product_details.html
tailwind_config_old = """        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: { 900: '#1F4D3B', 800: '#2E5E4E', 700: '#355E3B' }, /* Forest Essentials inspired Green */
                        gold: { 400: '#F5E6A3', 500: '#E3C16F', 600: '#C9A84C' },
                        earth: { 50: '#FDFBF7', 100: '#F8F5EE', 200: '#F3EFE4' },
                        brown: { 800: '#6E4E37' },
                        olive: { 600: '#7A8450' },
                        dark: '#1D1D1D'
                    },"""
tailwind_config_new = """        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: { 900: '#163A2F', 800: '#1F4D3B', 700: '#2E5E4E' },
                        gold: { 300: '#F5E6A3', 400: '#E3C16F', 500: '#D4AF37', 600: '#C9A84C' },
                        earth: { 50: '#FDFBF7', 100: '#F8F5EF', 200: '#F3EFE4' },
                        charcoal: { 800: '#2D2D2D', 900: '#1C1C1C' },
                        dark: '#1D1D1D'
                    },"""
content = content.replace(tailwind_config_old, tailwind_config_new)

# Update style layer
style_layer_old = """        @layer utilities {
            .glass { @apply bg-white/80 backdrop-blur-lg border border-white/40 shadow-[0_8px_32px_0_rgba(31,77,59,0.05)]; }
            .glass-card { @apply bg-white/5 backdrop-blur-md border border-gold-500/20 shadow-[0_8px_32px_0_rgba(0,0,0,0.5)] hover:border-gold-500/40 transition-all duration-500; }
            .text-gradient-gold { @apply bg-clip-text text-transparent bg-gradient-to-r from-gold-600 to-gold-400; }
            .bg-gradient-gold { @apply bg-gradient-to-r from-gold-600 to-gold-500; }
        }
        body { @apply bg-primary-900 text-gray-300 font-sans overflow-x-hidden; }
        h1, h2, h3, h4, h5, h6 { @apply font-serif text-white; }"""
style_layer_new = """        @layer utilities {
            .glass { @apply bg-white/70 backdrop-blur-xl border border-white/40 shadow-[0_8px_32px_0_rgba(22,58,47,0.05)]; }
            .glass-dark { @apply bg-primary-900/80 backdrop-blur-xl border border-gold-500/20 shadow-[0_8px_32px_0_rgba(0,0,0,0.3)]; }
            .glass-card { @apply bg-white/60 backdrop-blur-md border border-white/50 shadow-xl hover:border-gold-500/50 hover:bg-white hover:-translate-y-2 transition-all duration-500; }
            .text-gradient-gold { @apply bg-clip-text text-transparent bg-gradient-to-r from-gold-600 via-gold-500 to-gold-400; }
            .bg-gradient-gold { @apply bg-gradient-to-r from-gold-600 via-gold-500 to-gold-400; }
        }
        body { @apply bg-earth-50 text-charcoal-900 font-sans overflow-x-hidden; }
        h1, h2, h3, h4, h5, h6 { @apply font-serif text-primary-900; }"""
content = content.replace(style_layer_old, style_layer_new)

# Update body class
content = content.replace('body class="antialiased selection:bg-gold-500 selection:text-primary-900 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-primary-800 via-primary-900 to-[#050f0b]"', 'body class="antialiased selection:bg-gold-500 selection:text-primary-900"')

# Generic replacements for text colors
content = content.replace('text-white', 'text-primary-900')
# Fix some specific text-white that should remain white, like in the alert bar if there were any, or buttons.
# In product sliders, text-white was for the title, so text-primary-900 is good.

content = content.replace('text-gray-400', 'text-charcoal-900/70')
content = content.replace('text-gray-300', 'text-charcoal-900/80')
content = content.replace('border-white/5', 'border-primary-900/10')
content = content.replace('border-white/10', 'border-primary-900/10')
content = content.replace('border-white/20', 'border-primary-900/20')
content = content.replace('bg-black/50', 'bg-earth-200')
content = content.replace('bg-black/20', 'bg-primary-900/10')
content = content.replace('text-dark', 'text-charcoal-900')

# For the badge '100% Pure Botanical' it was text-white uppercase, now it is text-primary-900.
# Actually, the badge has 'glass' which is light, so text-primary-900 is perfect.

# Let's fix any "bg-transparent border border-gold-500 text-gold-400 hover:bg-gold-500 hover:text-dark" buttons in the slider
content = content.replace('text-gold-400 hover:bg-gold-500 hover:text-dark', 'text-primary-900 hover:bg-primary-900 hover:text-gold-400')
content = content.replace('border-gold-500', 'border-primary-900')
# Re-fix the "text-gold-400" that might have been changed in the button
content = content.replace('text-gold-400 hover:bg-primary-900', 'text-primary-900 hover:bg-primary-900')

# Product Slider Add to Cart buttons
content = content.replace('<button class="bg-transparent border border-primary-900 text-primary-900 hover:bg-primary-900 hover:text-gold-400', '<button class="bg-primary-900 border border-primary-900 text-gold-400 hover:bg-gold-500 hover:text-primary-900')

# Gradient on images: from-primary-900/90 to transparent. Let's make it lighter or keep it to contrast with the text.
# If the text is text-primary-900, it won't be visible on from-primary-900/90.
# Wait! In the Image Block, there's a badge:
# <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-transparent to-transparent"></div>
# <div class="absolute bottom-6 left-6 right-6 flex items-center justify-between">
# <span class="glass px-4 py-2 rounded-full text-xs text-primary-900 uppercase tracking-widest border-primary-900/20">...</span>
# The badge text is text-primary-900, the glass bg is white/70. It will be visible. The gradient is behind the badge.

# Update "Materia Medica" and Title section
# <h1 class="text-4xl md:text-7xl font-bold mb-6 font-serif leading-tight">Nature's <span class="text-gradient-gold">Masterpieces</span></h1>
# This is fine, since text-white became text-primary-900.

# The ingredient number was text-fill-color: transparent with a gradient.
# background: linear-gradient(to bottom, rgba(201,168,76,0.1), transparent);
# Let's change it to a darker gold or primary-900 for light theme
content = content.replace('rgba(201,168,76,0.1)', 'rgba(22,58,47,0.05)')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated ingredients.html theme!")

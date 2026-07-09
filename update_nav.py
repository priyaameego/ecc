import os
import re

files = ['about.html', 'products.html', 'ingredients.html', 'contact.html', 'cart.html']
for filename in files:
    filepath = os.path.join('e:/ecc', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update tailwind config and head styles
    head_new = '''    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: { 900: '#1F4D3B', 800: '#2E5E4E', 700: '#355E3B' }, /* Forest Essentials inspired Green */
                        gold: { 400: '#F5E6A3', 500: '#E3C16F', 600: '#C9A84C' },
                        earth: { 50: '#FDFBF7', 100: '#F8F5EE', 200: '#F3EFE4' },
                        brown: { 800: '#6E4E37' },
                        olive: { 600: '#7A8450' },
                        dark: '#1D1D1D'
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        serif: ['Playfair Display', 'serif'],
                    }
                }
            }
        }
    </script>
    <style type="text/tailwindcss">
        @layer utilities {
            .glass { @apply bg-white/80 backdrop-blur-lg border border-white/40 shadow-[0_8px_32px_0_rgba(31,77,59,0.05)]; }
            .glass-card { @apply bg-white/70 backdrop-blur-md border border-white/50 shadow-[0_8px_32px_0_rgba(31,77,59,0.05)] hover:border-gold-500/50 hover:bg-white hover:-translate-y-2 transition-all duration-300; }
            .text-gradient-gold { @apply bg-clip-text text-transparent bg-gradient-to-r from-gold-600 to-gold-500; }
            .bg-gradient-gold { @apply bg-gradient-to-r from-gold-600 to-gold-500; }
        }
        body { @apply bg-earth-100 text-dark font-sans overflow-x-hidden; }
        h1, h2, h3, h4, h5, h6 { @apply font-serif text-primary-900; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @keyframes marquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .animate-marquee {
            animation: marquee 25s linear infinite;
        }
    </style>
</head>'''
    content = re.sub(r'    <script>\s*tailwind\.config = \{.*?</head>', head_new, content, flags=re.DOTALL)
    
    # 3. Add Alert Bar
    alert_bar = '''

    <!-- Alert Bar -->
    <div class="fixed top-0 w-full z-[60] bg-primary-900 text-gold-400 text-xs py-2 px-4 overflow-hidden border-b border-gold-600/30">
        <div class="whitespace-nowrap animate-marquee flex space-x-12 w-max">
            <span>✨ 100% Pure Ayurvedic Formulations</span>
            <span>🌿 Trusted by Thousands</span>
            <span>🚚 Free Premium Shipping on Orders Over ₹999</span>
            <span>🎁 Flat 15% OFF on First Purchase (Code: AYUR15)</span>
            <span>✨ 100% Pure Ayurvedic Formulations</span>
            <span>🌿 Trusted by Thousands</span>
            <span>🚚 Free Premium Shipping on Orders Over ₹999</span>
            <span>🎁 Flat 15% OFF on First Purchase (Code: AYUR15)</span>
        </div>
    </div>'''
    if '<!-- Alert Bar -->' not in content:
        content = content.replace('<body class="antialiased">', '<body class="antialiased">' + alert_bar)

    # 4. Update Nav positioning & styles
    content = content.replace('<nav class="fixed top-0 w-full z-50 glass border-b border-white/10 transition-all duration-300">', '<nav class="fixed top-8 w-full z-50 glass border-b border-white/40 transition-all duration-300">')
    content = content.replace('<a href="index.html" class="font-serif text-2xl font-bold tracking-wider text-gradient-gold">', '<a href="index.html" class="font-serif text-2xl font-bold tracking-wider text-primary-900">')
    
    # 5. Update nav links
    content = content.replace('class="text-white hover:text-gold-400 transition-colors uppercase text-sm tracking-wider"', 'class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium"')
    content = content.replace('class="text-gold-400 transition-colors uppercase text-sm tracking-wider"', 'class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium border-b-2 border-primary-900 pb-1"')
    
    # 6. Cart icon in nav
    content = content.replace('''<a href="cart.html" class="text-white hover:text-gold-400 transition-colors relative">
                        <i class="fas fa-shopping-cart text-xl"></i>
                        <span class="absolute -top-2 -right-2 bg-gradient-gold text-navy-900 text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center">0</span>''', '''<a href="cart.html" class="text-primary-900 hover:text-gold-600 transition-colors relative">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span class="absolute -top-2 -right-2 bg-primary-900 text-gold-400 text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center">0</span>''')
    
    # Mobile cart
    content = content.replace('''<a href="cart.html" class="text-white relative">
                        <i class="fas fa-shopping-cart text-xl"></i>
                        <span class="absolute -top-2 -right-2 bg-gradient-gold text-navy-900 text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center">0</span>''', '''<a href="cart.html" class="text-primary-900 relative">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span class="absolute -top-2 -right-2 bg-primary-900 text-gold-400 text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center">0</span>''')
    
    # Mobile menu btn
    content = content.replace('id="mobile-menu-btn" class="text-white hover:text-gold-400 focus:outline-none"', 'id="mobile-menu-btn" class="text-primary-900 hover:text-gold-600 focus:outline-none"')
    
    # Mobile menu active/inactive
    content = content.replace('class="hidden md:hidden glass border-t border-white/10"', 'class="hidden md:hidden glass border-t border-white/40"')
    content = content.replace('class="block px-3 py-2 text-base font-medium text-white hover:text-gold-400"', 'class="block px-3 py-2 text-base font-medium text-dark hover:text-primary-900"')
    content = content.replace('class="block px-3 py-2 text-base font-medium text-gold-400"', 'class="block px-3 py-2 text-base font-medium text-primary-900 border-l-4 border-primary-900"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")

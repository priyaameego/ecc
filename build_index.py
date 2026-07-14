import os

products = [
    {"id": "kordy_x", "name": "KORDY X", "price": "1,499", "old_price": "1,999", "image": "prod_kordy_x.png", "desc": "Premium Vitality & Stamina Blend", "rating": "4.9", "reviews": "128", "badge": "Bestseller"},
    {"id": "ashwagandha", "name": "Ashwagandha Plus", "price": "899", "old_price": "1,299", "image": "prod_ashwagandha.png", "desc": "Stress Relief & Calmness", "rating": "4.8", "reviews": "95", "badge": "High Absorption"},
    {"id": "shilajit", "name": "Shilajit Gold", "price": "1,899", "old_price": "2,499", "image": "prod_shilajit.png", "desc": "Pure Himalayan Resin", "rating": "5.0", "reviews": "210", "badge": "Premium"},
    {"id": "gokshura", "name": "Gokshura Power", "price": "799", "old_price": "1,099", "image": "prod_gokshura.png", "desc": "Muscle Recovery & Vigor", "rating": "4.7", "reviews": "82", "badge": ""},
    {"id": "ginseng", "name": "Panax Ginseng", "price": "1,199", "old_price": "1,599", "image": "prod_ginseng.png", "desc": "Cognitive Focus & Energy", "rating": "4.9", "reviews": "115", "badge": "New"},
    {"id": "chaste", "name": "Chaste Tree Blend", "price": "949", "old_price": "1,399", "image": "prod_chaste.png", "desc": "Women's Hormonal Balance", "rating": "4.8", "reviews": "90", "badge": ""},
    {"id": "joyflex", "name": "Joyflex Joints", "price": "1,099", "old_price": "1,499", "image": "prod_joyflex.png", "desc": "Joint Mobility & Flexibility", "rating": "4.9", "reviews": "154", "badge": "Clinically Proven"}
]

# Generate products HTML
products_html = ""
for p in products:
    badge_html = f'<div class="absolute top-4 left-4 bg-white px-3 py-1 rounded-full text-[10px] font-bold text-primary-900 uppercase tracking-widest shadow-md z-10">{p["badge"]}</div>' if p["badge"] else ''
    products_html += f"""
                <div class="group" data-aos="fade-up">
                    <div class="relative bg-earth-100 rounded-2xl p-6 mb-6 transition-all duration-500 overflow-hidden group-hover:shadow-[0_20px_40px_rgba(22,58,47,0.08)]">
                        {badge_html}
                        <!-- Wishlist -->
                        <button class="absolute top-4 right-4 w-8 h-8 bg-white/50 backdrop-blur-sm rounded-full flex items-center justify-center text-charcoal-900/40 hover:text-gold-500 hover:bg-white transition-all z-10">
                            <i class="fas fa-heart text-sm"></i>
                        </button>
                        
                        <div class="relative h-64 flex items-center justify-center mb-4">
                            <div class="absolute inset-0 bg-gradient-to-t from-charcoal-900/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-xl"></div>
                            <img src="assets/{p['image']}" alt="{p['name']}" class="h-full object-contain group-hover:scale-105 transition-transform duration-700 relative z-10 filter drop-shadow-[0_15px_15px_rgba(0,0,0,0.15)]">
                        </div>
                        
                        <!-- Quick Actions Overlay -->
                        <div class="absolute bottom-4 left-4 right-4 translate-y-0 opacity-100 md:translate-y-12 md:opacity-0 md:group-hover:translate-y-0 md:group-hover:opacity-100 transition-all duration-300 z-20 flex gap-2">
                            <a href="product_{p['id']}.html" class="flex-1 bg-white text-primary-900 font-semibold text-xs uppercase tracking-widest py-3 rounded-full hover:bg-earth-50 transition-colors shadow-lg flex items-center justify-center">Quick View</a>
                            <a href="cart.html" class="w-12 flex-shrink-0 h-12 bg-primary-900 text-gold-400 rounded-full flex items-center justify-center hover:bg-primary-800 transition-colors shadow-lg"><i class="fas fa-shopping-bag"></i></a>
                        </div>
                    </div>
                    
                    <!-- Details -->
                    <div class="text-center px-2">
                        <div class="flex justify-center items-center gap-1 text-gold-500 text-[10px] mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                            <span class="text-charcoal-900/50 font-sans ml-1">({p['reviews']})</span>
                        </div>
                        <h3 class="font-serif text-xl text-primary-900 mb-1 group-hover:text-gold-600 transition-colors"><a href="product_{p['id']}.html">{p['name']}</a></h3>
                        <p class="text-charcoal-900/60 text-xs font-light mb-3">{p['desc']}</p>
                        <div class="flex justify-center items-center gap-3">
                            <span class="font-medium text-primary-900">₹{p['price']}</span>
                            <span class="text-charcoal-900/40 line-through text-sm">₹{p['old_price']}</span>
                        </div>
                    </div>
                </div>
"""

html_content = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THE HANURAAM WELLNESS | Luxury Ayurvedic Formulations</title>
    <meta name="description" content="Discover world-class luxury Ayurvedic formulations. Where Ancient Wisdom Meets Modern Science.">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: {{ 900: '#163A2F', 800: '#1F4D3B', 700: '#2E5E4E' }},
                        gold: {{ 300: '#F5E6A3', 400: '#E3C16F', 500: '#D4AF37', 600: '#C9A84C' }},
                        earth: {{ 50: '#FDFBF7', 100: '#F8F5EF', 200: '#F3EFE4' }},
                        charcoal: {{ 800: '#2D2D2D', 900: '#1C1C1C' }},
                    }},
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        serif: ['Playfair Display', 'serif'],
                    }},
                    animation: {{
                        'float': 'float 8s ease-in-out infinite',
                        'float-delayed': 'float 8s ease-in-out 4s infinite',
                        'spin-slow': 'spin 20s linear infinite',
                        'scroll': 'scrollDown 2s infinite',
                    }},
                    keyframes: {{
                        float: {{
                            '0%, 100%': {{ transform: 'translateY(0) rotate(0)' }},
                            '50%': {{ transform: 'translateY(-20px) rotate(5deg)' }},
                        }},
                        scrollDown: {{
                            '0%': {{ transform: 'translateY(0)', opacity: 1 }},
                            '100%': {{ transform: 'translateY(15px)', opacity: 0 }},
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style type="text/tailwindcss">
        @layer utilities {{
            .glass {{ @apply bg-white/70 backdrop-blur-xl border border-white/40 shadow-[0_8px_32px_0_rgba(22,58,47,0.05)]; }}
            .glass-dark {{ @apply bg-primary-900/80 backdrop-blur-xl border border-gold-500/20 shadow-[0_8px_32px_0_rgba(0,0,0,0.3)]; }}
            .text-gradient-gold {{ @apply bg-clip-text text-transparent bg-gradient-to-r from-gold-600 via-gold-500 to-gold-400; }}
            .bg-gradient-gold {{ @apply bg-gradient-to-r from-gold-600 via-gold-500 to-gold-400; }}
        }}
        body {{ @apply bg-earth-50 text-charcoal-900 font-sans overflow-x-hidden; }}
        h1, h2, h3, h4, h5, h6 {{ @apply font-serif text-primary-900; }}
        
        ::-webkit-scrollbar {{ width: 8px; }}
        ::-webkit-scrollbar-track {{ background: #F8F5EF; }}
        ::-webkit-scrollbar-thumb {{ background: #D4AF37; border-radius: 4px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #C9A84C; }}
        
        .bg-grain {{
            position: absolute;
            inset: 0;
            background-image: url('data:image/svg+xml,%3Csvg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"%3E%3Cfilter id="noiseFilter"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noiseFilter)"/%3E%3C/svg%3E');
            opacity: 0.04;
            mix-blend-mode: multiply;
            pointer-events: none;
            z-index: 10;
        }}
        
        /* Hide scrollbar for horizontal scrolling */
        .no-scrollbar::-webkit-scrollbar {{ display: none; }}
        .no-scrollbar {{ -ms-overflow-style: none; scrollbar-width: none; }}
        
        @keyframes marquee {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
        .animate-marquee {{ animation: marquee 25s linear infinite; }}
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
</head>
<body class="antialiased selection:bg-gold-500 selection:text-primary-900">

    <!-- Alert Bar -->
    <div class="fixed top-0 w-full z-[60] bg-primary-900 text-gold-500 text-xs py-2 px-4 overflow-hidden border-b border-gold-600/30">
        <div class="whitespace-nowrap animate-marquee flex space-x-12 w-max font-medium tracking-wide">
            <span>✨ 100% Pure Ayurvedic Formulations</span>
            <span>🌿 Trusted by Thousands</span>
            <span>🚚 Free Premium Shipping on Orders Over ₹999</span>
            <span>🎁 Flat 15% OFF on First Purchase (Code: AYUR15)</span>
            <span>✨ 100% Pure Ayurvedic Formulations</span>
            <span>🌿 Trusted by Thousands</span>
            <span>🚚 Free Premium Shipping on Orders Over ₹999</span>
            <span>🎁 Flat 15% OFF on First Purchase (Code: AYUR15)</span>
        </div>
    </div>

    <!-- Navigation -->
    <nav class="fixed top-8 w-full z-50 glass border-b border-white/40 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20 relative">
                <div class="hidden md:flex space-x-8 items-center w-1/3">
                    <a href="index.html" class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium border-b-2 border-primary-900 pb-1">Home</a>
                    <a href="about.html" class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium                    ">About</a>
                    <a href="products.html" class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium">Products</a>
                </div>
                
                <div class="absolute left-1/2 -translate-x-1/2 flex items-center">
                    <a href="index.html" class="flex items-center">
                        <img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-12 object-contain hover:scale-105 transition-transform duration-500">
                    </a>
                </div>
                
                <div class="hidden md:flex space-x-6 lg:space-x-8 items-center justify-end w-1/3">
                    <a href="ingredients.html" class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium">Ingredients</a>
                    <a href="certifications.html" class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium">Certifications</a>
                    <a href="contact.html" class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium">Contact</a>
                    <a href="thankyou.html" class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium">Thank You</a>
                    <a href="cart.html" class="text-primary-900 hover:text-gold-600 transition-colors relative group">
                        <i class="fas fa-shopping-bag text-xl group-hover:scale-110 transition-transform"></i>
                        <span class="cart-counter absolute -top-2 -right-2 bg-primary-900 text-gold-400 text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center border border-gold-500/30">0</span>
                    </a>
                </div>
                
                <div class="md:hidden flex items-center space-x-4 ml-auto">
                    <a href="cart.html" class="text-primary-900 relative">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span class="cart-counter absolute -top-2 -right-2 bg-primary-900 text-gold-400 text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center">0</span>
                    </a>
                    <button id="mobile-menu-btn" class="text-primary-900 hover:text-gold-600 focus:outline-none">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden glass border-t border-white/40">
            <div class="px-4 pt-2 pb-6 space-y-2">
                <a href="index.html" class="block py-2 text-sm uppercase tracking-widest font-medium font-bold text-primary-900 border-b border-primary-900/10">Home</a>
                <a href="about.html" class="block py-2 text-sm uppercase tracking-widest font-medium font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold text-primary-900 border-b border-primary-900/10">About</a>
                <a href="products.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Products</a>
                <a href="ingredients.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Ingredients</a>
                <a href="certifications.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Certifications</a>
                <a href="thankyou.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Thank You</a>
                <a href="contact.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900">Contact</a>
            </div>
        </div>
    </nav>

    <!-- 1. Fullscreen Hero Slider -->
    <header class="relative min-h-screen md:h-screen md:min-h-[700px] flex flex-col justify-center overflow-hidden bg-earth-50 pt-32 pb-16 md:pt-0 md:pb-0 group">
        
        <div id="hero-slider" class="flex w-full h-full transition-transform duration-700 ease-in-out absolute inset-0">
            
            <!-- Slide 1: Original Hero -->
            <div class="w-full h-full flex-shrink-0 flex items-center justify-center relative bg-earth-50">
                <!-- Background Elements -->
                <div class="absolute inset-0 z-0">
                    <div class="absolute inset-0 bg-gradient-radial from-earth-100 to-earth-50"></div>
                    <!-- Decorative circle -->
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] rounded-full border-[1px] border-primary-900/5"></div>
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] rounded-full border-[1px] border-gold-500/10"></div>
                </div>
                <div class="bg-grain"></div>
                
                <!-- Floating Botanicals & Product -->
                <div class="absolute inset-0 z-10 pointer-events-none overflow-hidden">
                    <img src="assets/botanical_ashwagandha.png" alt="Leaf" class="absolute top-1/4 left-10 w-48 opacity-40 animate-float">
                    <img src="assets/botanical_ginseng.png" alt="Leaf" class="absolute bottom-1/4 right-10 w-64 opacity-40 animate-float-delayed">
                </div>
                
                <div class="relative z-20 w-full max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between flex-1 h-full pt-20">
                    <div class="md:w-1/2 text-center md:text-left pt-10 md:pt-0" data-aos="fade-right" data-aos-duration="1500">
                        <span class="text-gold-600 uppercase tracking-[0.3em] text-xs font-bold mb-4 block">Redefining Ayurveda</span>
                        <h1 class="text-5xl md:text-7xl font-serif text-primary-900 mb-6 leading-tight">Elevate Your<br><span class="italic text-charcoal-900">Vitality.</span></h1>
                        <p class="text-lg text-charcoal-900/70 font-light mb-10 max-w-lg mx-auto md:mx-0">
                            Experience the pinnacle of natural wellness. Clinically validated, 100% pure botanical extracts crafted for the modern lifestyle.
                        </p>
                        <div class="flex flex-col sm:flex-row items-center gap-4 justify-center md:justify-start">
                            <a href="products.html" class="w-full sm:w-auto px-8 py-4 bg-primary-900 text-gold-400 font-bold uppercase tracking-widest text-xs rounded-full shadow-[0_10px_30px_rgba(22,58,47,0.3)] hover:shadow-[0_15px_40px_rgba(22,58,47,0.4)] hover:-translate-y-1 transition-all duration-300">Shop Collection</a>
                            <a href="about.html" class="w-full sm:w-auto px-8 py-4 border border-primary-900/30 text-primary-900 font-bold uppercase tracking-widest text-xs rounded-full hover:bg-earth-100 transition-all duration-300">Our Heritage</a>
                        </div>
                    </div>
                    
                    <div class="md:w-1/2 mt-16 md:mt-0 relative flex justify-center" data-aos="zoom-in" data-aos-duration="2000">
                        <!-- Glowing effect behind product -->
                        <div class="absolute inset-0 bg-gold-500/20 rounded-full blur-[100px] w-80 h-80 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"></div>
                        <img src="assets/prod_kordy_x.png" alt="KORDY X" class="w-80 md:w-96 lg:w-[450px] relative z-20 drop-shadow-[0_30px_50px_rgba(0,0,0,0.3)] animate-float">
                        
                        <!-- Product floating badge -->
                        <div class="absolute top-1/4 right-0 md:-right-10 bg-white/80 backdrop-blur-md px-4 py-3 rounded-2xl shadow-xl border border-white z-30 animate-float-delayed flex items-center gap-3">
                            <div class="w-10 h-10 bg-gradient-gold rounded-full flex items-center justify-center text-primary-900"><i class="fas fa-bolt"></i></div>
                            <div>
                                <p class="text-[10px] uppercase tracking-widest text-charcoal-900/50 font-bold">Best Seller</p>
                                <p class="text-sm font-serif text-primary-900">KORDY X</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Slide 2: Promotional Banner -->
            <div class="w-full h-full flex-shrink-0 flex items-center justify-center relative bg-primary-900 overflow-hidden">
                <img src="payday-banner.jpg" alt="Special Offer" class="absolute inset-0 w-full h-full object-cover opacity-60 mix-blend-overlay" onerror="this.src='assets/hero_bg.png'">
                <div class="absolute inset-0 bg-gradient-to-r from-primary-900 via-primary-900/80 to-transparent"></div>
                <div class="relative z-20 w-full max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between flex-1 h-full pt-20">
                    <div class="md:w-1/2 text-center md:text-left">
                        <span class="text-gold-400 uppercase tracking-[0.3em] text-xs font-bold mb-4 block"><i class="fas fa-gift mr-2"></i>Special Promotion</span>
                        <h2 class="text-5xl md:text-7xl font-serif text-white mb-6 leading-tight">Wellness<br><span class="italic text-gold-300">Special Offer.</span></h2>
                        <p class="text-lg text-white/80 font-light mb-10 max-w-lg mx-auto md:mx-0">
                            Invest in your health. Get up to 30% off on all luxury ayurvedic collections. 
                        </p>
                        <a href="products.html" class="px-8 py-4 bg-gold-500 text-primary-900 font-bold uppercase tracking-widest text-xs rounded-full hover:bg-gold-400 transition-all duration-300 inline-block">Shop the Sale</a>
                    </div>
                </div>
            </div>

            <!-- Slide 3: New Arrivals -->
            <div class="w-full h-full flex-shrink-0 flex items-center justify-center relative bg-earth-50 overflow-hidden">
                <img src="assets/hero_bg.png" alt="New Arrivals" class="absolute inset-0 w-full h-full object-cover">
                <div class="relative z-20 w-full max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-center flex-1 h-full pt-20">
                    <div class="text-center">
                        <span class="text-gold-600 uppercase tracking-[0.3em] text-xs font-bold mb-4 block">Just Arrived</span>
                        <h2 class="text-5xl md:text-7xl font-serif text-primary-900 mb-6 leading-tight">Discover<br><span class="italic text-charcoal-900">New Formulations.</span></h2>
                        <a href="products.html" class="px-8 py-4 border border-primary-900 text-primary-900 font-bold uppercase tracking-widest text-xs rounded-full hover:bg-primary-900 hover:text-white transition-all duration-300 inline-block">Explore Now</a>
                    </div>
                </div>
            </div>

            <!-- Slide 4: Best Sellers -->
            <div class="w-full h-full flex-shrink-0 flex items-center justify-center relative bg-earth-100 overflow-hidden">
                <img src="payday-banner.jpg" alt="Best Sellers" class="absolute inset-0 w-full h-full object-cover opacity-20 mix-blend-overlay" onerror="this.src='assets/hero_bg.png'">
                <div class="absolute inset-0 bg-gradient-to-r from-earth-50 via-earth-100/50 to-transparent"></div>
                <div class="relative z-20 w-full max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between flex-1 h-full pt-20">
                    <div class="md:w-1/2 text-center md:text-left">
                        <span class="text-primary-900 uppercase tracking-[0.3em] text-xs font-bold mb-4 block"><i class="fas fa-star text-gold-500 mr-2"></i>Customer Favorites</span>
                        <h2 class="text-5xl md:text-7xl font-serif text-primary-900 mb-6 leading-tight">Our Most<br><span class="italic text-charcoal-900">Loved Products.</span></h2>
                        <a href="products.html" class="px-8 py-4 bg-primary-900 text-gold-400 font-bold uppercase tracking-widest text-xs rounded-full hover:bg-primary-800 transition-all duration-300 inline-block">Shop Best Sellers</a>
                    </div>
                </div>
            </div>

            <!-- Slide 5: Holistic Health -->
            <div class="w-full h-full flex-shrink-0 flex items-center justify-center relative bg-primary-900 overflow-hidden">
                <img src="assets/hero_bg.png" alt="Holistic Health" class="absolute inset-0 w-full h-full object-cover opacity-50 mix-blend-overlay">
                <div class="absolute inset-0 bg-gradient-radial from-primary-900/50 to-primary-900"></div>
                <div class="relative z-20 w-full max-w-7xl mx-auto px-4 flex flex-col items-center justify-center flex-1 h-full pt-20 text-center">
                    <span class="text-gold-400 uppercase tracking-[0.3em] text-xs font-bold mb-4 block">Pure Ingredients</span>
                    <h2 class="text-5xl md:text-7xl font-serif text-white mb-6 leading-tight">Rooted in<br><span class="italic text-gold-300">Nature.</span></h2>
                    <p class="text-lg text-white/80 font-light mb-10 max-w-2xl mx-auto">
                        We source the finest botanical extracts globally to bring you authentic, potent, and safe ayurvedic remedies.
                    </p>
                    <a href="about.html" class="px-8 py-4 bg-gold-500 text-primary-900 font-bold uppercase tracking-widest text-xs rounded-full hover:bg-gold-400 transition-all duration-300 inline-block">Our Philosophy</a>
                </div>
            </div>

        </div>

        <!-- Slider Controls -->
        <button id="prev-slide" class="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/30 backdrop-blur-md flex items-center justify-center text-primary-900 opacity-0 group-hover:opacity-100 transition-all hover:bg-white/70 z-30 shadow-lg border border-white/40">
            <i class="fas fa-chevron-left text-xl"></i>
        </button>
        <button id="next-slide" class="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-white/30 backdrop-blur-md flex items-center justify-center text-primary-900 opacity-0 group-hover:opacity-100 transition-all hover:bg-white/70 z-30 shadow-lg border border-white/40">
            <i class="fas fa-chevron-right text-xl"></i>
        </button>

        <!-- Slider Indicators -->
        <div class="absolute bottom-24 left-1/2 -translate-x-1/2 flex space-x-3 z-30">
            <button class="w-8 h-2.5 rounded-full bg-primary-900 transition-all slider-indicator active shadow-md border border-white/20"></button>
            <button class="w-2.5 h-2.5 rounded-full bg-primary-900/30 transition-all slider-indicator shadow-md border border-white/20"></button>
            <button class="w-2.5 h-2.5 rounded-full bg-primary-900/30 transition-all slider-indicator shadow-md border border-white/20"></button>
            <button class="w-2.5 h-2.5 rounded-full bg-primary-900/30 transition-all slider-indicator shadow-md border border-white/20"></button>
            <button class="w-2.5 h-2.5 rounded-full bg-primary-900/30 transition-all slider-indicator shadow-md border border-white/20"></button>
        </div>

        <!-- Scroll Indicator -->
        <div class="absolute bottom-8 left-1/2 -translate-x-1/2 z-20 flex flex-col items-center cursor-pointer" onclick="window.scrollTo({{top: window.innerHeight, behavior: 'smooth'}})">
            <span class="text-primary-900/50 text-[10px] uppercase tracking-widest mb-2 font-bold bg-white/50 px-2 py-1 rounded-full backdrop-blur-sm">Scroll</span>
            <div class="w-px h-12 bg-primary-900/20 relative overflow-hidden">
                <div class="w-full h-1/2 bg-primary-900 animate-scroll"></div>
            </div>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const slider = document.getElementById('hero-slider');
                const prevBtn = document.getElementById('prev-slide');
                const nextBtn = document.getElementById('next-slide');
                const indicators = document.querySelectorAll('.slider-indicator');
                let currentSlide = 0;
                const totalSlides = 5;
                let slideInterval;

                function updateSlider() {{
                    if(!slider) return;
                    slider.style.transform = `translateX(-${{currentSlide * 100}}%)`;
                    indicators.forEach((ind, index) => {{
                        if (index === currentSlide) {{
                            ind.classList.remove('bg-primary-900/30');
                            ind.classList.add('bg-primary-900');
                            ind.classList.add('w-8');
                            ind.classList.remove('w-2.5');
                        }} else {{
                            ind.classList.add('bg-primary-900/30');
                            ind.classList.remove('bg-primary-900');
                            ind.classList.remove('w-8');
                            ind.classList.add('w-2.5');
                        }}
                    }});
                }}

                function nextSlide() {{
                    currentSlide = (currentSlide + 1) % totalSlides;
                    updateSlider();
                }}

                function prevSlide() {{
                    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
                    updateSlider();
                }}

                function startAutoplay() {{
                    slideInterval = setInterval(nextSlide, 5000);
                }}

                function stopAutoplay() {{
                    clearInterval(slideInterval);
                }}

                if(nextBtn && prevBtn && slider) {{
                    nextBtn.addEventListener('click', () => {{ nextSlide(); stopAutoplay(); startAutoplay(); }});
                    prevBtn.addEventListener('click', () => {{ prevSlide(); stopAutoplay(); startAutoplay(); }});
                    
                    indicators.forEach((ind, index) => {{
                        ind.addEventListener('click', () => {{
                            currentSlide = index;
                            updateSlider();
                            stopAutoplay();
                            startAutoplay();
                        }});
                    }});
                    
                    startAutoplay();
                }}
            }});
        </script>
    </header>



    <!-- 2 & 3. Premium Categories & Shop By Health Goals -->
    <section class="py-24 bg-white relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16" data-aos="fade-up">
                <span class="text-gold-600 uppercase tracking-[0.2em] text-xs font-bold mb-3 block">Targeted Wellness</span>
                <h2 class="text-4xl font-serif text-primary-900 mb-6">Shop By Health Goal</h2>
                <div class="w-16 h-px bg-gold-500 mx-auto"></div>
            </div>
            
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                <!-- Goal 1 -->
                <a href="products.html" class="group block relative rounded-2xl overflow-hidden aspect-square" data-aos="zoom-in" data-aos-delay="0">
                    <img src="assets/cat_vitality.png" alt="Energy" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-4 left-4 right-4 text-center">
                        <h3 class="text-white font-serif text-lg mb-1">Energy & Vigor</h3>
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold opacity-0 group-hover:opacity-100 transition-opacity translate-y-2 group-hover:translate-y-0 duration-300 block">Explore <i class="fas fa-chevron-right ml-1"></i></span>
                    </div>
                </a>
                <!-- Goal 2 -->
                <a href="products.html" class="group block relative rounded-2xl overflow-hidden aspect-square" data-aos="zoom-in" data-aos-delay="100">
                    <img src="assets/cat_immunity.png" alt="Immunity" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-4 left-4 right-4 text-center">
                        <h3 class="text-white font-serif text-lg mb-1">Immunity</h3>
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold opacity-0 group-hover:opacity-100 transition-opacity translate-y-2 group-hover:translate-y-0 duration-300 block">Explore <i class="fas fa-chevron-right ml-1"></i></span>
                    </div>
                </a>
                <!-- Goal 3 -->
                <a href="products.html" class="group block relative rounded-2xl overflow-hidden aspect-square" data-aos="zoom-in" data-aos-delay="200">
                    <img src="assets/cat_mind.png" alt="Stress" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-4 left-4 right-4 text-center">
                        <h3 class="text-white font-serif text-lg mb-1">Stress & Calm</h3>
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold opacity-0 group-hover:opacity-100 transition-opacity translate-y-2 group-hover:translate-y-0 duration-300 block">Explore <i class="fas fa-chevron-right ml-1"></i></span>
                    </div>
                </a>
                <!-- Goal 4 -->
                <a href="products.html" class="group block relative rounded-2xl overflow-hidden aspect-square" data-aos="zoom-in" data-aos-delay="300">
                    <img src="assets/cat_joint.png" alt="Joints" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-4 left-4 right-4 text-center">
                        <h3 class="text-white font-serif text-lg mb-1">Bone & Joint</h3>
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold opacity-0 group-hover:opacity-100 transition-opacity translate-y-2 group-hover:translate-y-0 duration-300 block">Explore <i class="fas fa-chevron-right ml-1"></i></span>
                    </div>
                </a>
                <!-- Goal 5 -->
                <a href="products.html" class="group block relative rounded-2xl overflow-hidden aspect-square" data-aos="zoom-in" data-aos-delay="400">
                    <img src="assets/info_damiyana.jpg" alt="Women's Health" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-4 left-4 right-4 text-center">
                        <h3 class="text-white font-serif text-lg mb-1">Women's Health</h3>
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold opacity-0 group-hover:opacity-100 transition-opacity translate-y-2 group-hover:translate-y-0 duration-300 block">Explore <i class="fas fa-chevron-right ml-1"></i></span>
                    </div>
                </a>
                <!-- Goal 6 -->
                <a href="products.html" class="group block relative rounded-2xl overflow-hidden aspect-square" data-aos="zoom-in" data-aos-delay="500">
                    <img src="assets/info_shilajit.jpg" alt="Men's Health" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-4 left-4 right-4 text-center">
                        <h3 class="text-white font-serif text-lg mb-1">Men's Health</h3>
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold opacity-0 group-hover:opacity-100 transition-opacity translate-y-2 group-hover:translate-y-0 duration-300 block">Explore <i class="fas fa-chevron-right ml-1"></i></span>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <!-- 4. Best Sellers -->
    <section class="py-24 bg-earth-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-end mb-12">
                <div data-aos="fade-right">
                    <h2 class="text-3xl md:text-4xl font-serif text-primary-900 mb-2">Our Masterpieces</h2>
                    <p class="text-charcoal-900/60 font-light">The most loved formulations by our community.</p>
                </div>
                <a href="products.html" class="hidden md:block text-xs uppercase tracking-widest font-bold text-primary-900 hover:text-gold-600 transition-colors border-b border-primary-900 pb-1" data-aos="fade-left">View All Collections</a>
            </div>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-6 gap-y-12">
                {products_html}
            </div>
            
            <div class="mt-12 text-center md:hidden">
                <a href="products.html" class="inline-block px-8 py-4 border border-primary-900 text-primary-900 font-bold uppercase tracking-widest text-xs rounded-full hover:bg-primary-900 hover:text-gold-400 transition-colors">View All Collections</a>
            </div>
        </div>
    </section>

    <!-- 6. Our Heritage (Editorial Layout) -->
    <section class="py-24 bg-charcoal-900 relative overflow-hidden">
        <div class="absolute inset-0 z-0 opacity-50 pointer-events-none">
            <img src="assets/heritage_1.png" alt="Heritage" class="w-full h-full object-cover">
        </div>
        <div class="absolute inset-0 bg-gradient-to-r from-charcoal-900 via-charcoal-900/90 to-transparent z-0"></div>
        <div class="bg-grain"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="w-full md:w-1/2" data-aos="fade-right">
                <span class="text-gold-400 uppercase tracking-[0.3em] text-xs font-bold mb-6 block">The Legacy</span>
                <h2 class="text-4xl md:text-5xl font-serif text-white mb-8 leading-tight">Where Ancient Wisdom<br>Meets <span class="italic text-gold-500">Modern Science</span>.</h2>
                <p class="text-white/70 font-light leading-relaxed mb-6">
                    Rooted in the 5,000-year-old principles of Ayurveda, we don't just create supplements; we craft holistic wellness rituals. 
                </p>
                <p class="text-white/70 font-light leading-relaxed mb-10">
                    By combining classical texts with state-of-the-art supercritical extraction technology, we ensure that every active compound is preserved in its purest, most bioavailable form.
                </p>
                <a href="about.html" class="inline-block border-b border-gold-500 text-gold-400 uppercase tracking-widest text-xs font-bold pb-1 hover:text-white hover:border-white transition-colors">Discover Our Story</a>
            </div>
        </div>
    </section>

    <!-- 7. Key Botanicals -->
    <section class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16" data-aos="fade-up">
                <span class="text-gold-600 uppercase tracking-[0.2em] text-xs font-bold mb-3 block">Materia Medica</span>
                <h2 class="text-4xl font-serif text-primary-900 mb-6">The Power of Nature</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Botanical 1 -->
                <a href="ingredients.html" class="group block relative overflow-hidden rounded-2xl h-80" data-aos="fade-up" data-aos-delay="0">
                    <img src="assets/botanical_ashwagandha.png" alt="Ashwagandha" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-6 left-6 right-6">
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold mb-2 block">Withania somnifera</span>
                        <h3 class="text-white font-serif text-2xl mb-2">Ashwagandha</h3>
                        <p class="text-white/70 text-sm font-light opacity-0 group-hover:opacity-100 transition-opacity duration-300 h-0 group-hover:h-auto overflow-hidden">An adaptogen that manages cortisol levels, reducing stress and enhancing energy.</p>
                    </div>
                </a>
                <!-- Botanical 2 -->
                <a href="ingredients.html" class="group block relative overflow-hidden rounded-2xl h-80" data-aos="fade-up" data-aos-delay="100">
                    <img src="assets/botanical_shilajit.png" alt="Shilajit" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 bg-earth-200">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-6 left-6 right-6">
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold mb-2 block">Asphaltum punjabianum</span>
                        <h3 class="text-white font-serif text-2xl mb-2">Shilajit</h3>
                        <p class="text-white/70 text-sm font-light opacity-0 group-hover:opacity-100 transition-opacity duration-300 h-0 group-hover:h-auto overflow-hidden">Rich in Fulvic Acid, driving essential minerals directly into cells for peak stamina.</p>
                    </div>
                </a>
                <!-- Botanical 3 -->
                <a href="ingredients.html" class="group block relative overflow-hidden rounded-2xl h-80" data-aos="fade-up" data-aos-delay="200">
                    <img src="assets/botanical_gokshura.png" alt="Gokshura" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-6 left-6 right-6">
                        <span class="text-gold-400 text-[10px] uppercase tracking-widest font-bold mb-2 block">Tribulus terrestris</span>
                        <h3 class="text-white font-serif text-2xl mb-2">Gokshura</h3>
                        <p class="text-white/70 text-sm font-light opacity-0 group-hover:opacity-100 transition-opacity duration-300 h-0 group-hover:h-auto overflow-hidden">Supports muscle recovery, vitality, and optimal physical performance.</p>
                    </div>
                </a>
            </div>
            
            <div class="text-center mt-12">
                <a href="ingredients.html" class="inline-block border border-primary-900 text-primary-900 font-bold uppercase tracking-widest text-xs px-8 py-4 rounded-full hover:bg-primary-900 hover:text-gold-400 transition-colors">Explore All Botanicals</a>
            </div>
        </div>
    </section>

    <!-- 10. Customer Reviews -->
    <section class="py-24 bg-earth-100 border-y border-primary-900/5 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row gap-16 items-center">
                <div class="w-full md:w-1/3 text-center md:text-left" data-aos="fade-right">
                    <h2 class="text-3xl md:text-4xl font-serif text-primary-900 mb-4">Real Results. <br>Real Stories.</h2>
                    <div class="flex items-center justify-center md:justify-start gap-2 text-gold-500 text-xl mb-4">
                        <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star-half-alt"></i>
                    </div>
                    <p class="text-charcoal-900/70 font-medium">4.9/5 Average Rating</p>
                    <p class="text-charcoal-900/50 text-sm mb-8">Based on 10,000+ verified reviews</p>
                </div>
                
                <div class="w-full md:w-2/3 flex gap-6 overflow-x-auto no-scrollbar pb-8 snap-x" data-aos="fade-left">
                    <!-- Review 1 -->
                    <div class="min-w-[300px] md:min-w-[350px] bg-white p-8 rounded-2xl shadow-sm snap-center">
                        <div class="flex text-gold-500 text-xs mb-4"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                        <h4 class="font-bold text-primary-900 mb-2">Life-changing energy levels</h4>
                        <p class="text-charcoal-900/70 text-sm italic mb-6">"I've been using KORDY X for 3 months now. The difference in my sustained energy throughout the day is remarkable. No jitters, just clean vitality."</p>
                        <p class="text-xs font-bold uppercase tracking-widest text-primary-900">- Rahul S. <span class="text-green-600 ml-2"><i class="fas fa-check-circle"></i> Verified Buyer</span></p>
                    </div>
                    <!-- Review 2 -->
                    <div class="min-w-[300px] md:min-w-[350px] bg-white p-8 rounded-2xl shadow-sm snap-center">
                        <div class="flex text-gold-500 text-xs mb-4"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                        <h4 class="font-bold text-primary-900 mb-2">Finally found pure Ashwagandha</h4>
                        <p class="text-charcoal-900/70 text-sm italic mb-6">"The sleep quality I get after taking this is unmatched. You can literally feel the purity. The packaging is absolutely premium too."</p>
                        <p class="text-xs font-bold uppercase tracking-widest text-primary-900">- Priya M. <span class="text-green-600 ml-2"><i class="fas fa-check-circle"></i> Verified Buyer</span></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 15. Join The Family (Newsletter) -->
    <section class="py-24 relative overflow-hidden bg-primary-900 text-center">
        <div class="absolute inset-0 z-0">
            <img src="assets/hero_bg.png" alt="Background" class="w-full h-full object-cover opacity-20">
            <div class="absolute inset-0 bg-gradient-to-t from-primary-900 via-transparent to-primary-900"></div>
        </div>
        <div class="bg-grain"></div>
        
        <div class="max-w-3xl mx-auto px-4 relative z-10" data-aos="zoom-in">
            <i class="fas fa-envelope-open-text text-4xl text-gold-400 mb-6 block"></i>
            <h2 class="text-3xl md:text-5xl font-serif text-white mb-6">Join The Insider Circle</h2>
            <p class="text-white/70 mb-10 font-light">
                Subscribe to receive exclusive access to new launches, private sales, and Ayurvedic wisdom directly in your inbox.
            </p>
            <form class="flex flex-col sm:flex-row gap-4 max-w-xl mx-auto">
                <input type="email" placeholder="Enter your email address" class="flex-1 bg-white/10 backdrop-blur-md border border-gold-500/30 rounded-full px-6 py-4 text-white placeholder-white/50 focus:outline-none focus:border-gold-500 transition-colors">
                <button type="button" class="bg-gradient-gold text-primary-900 font-bold uppercase tracking-widest text-xs px-8 py-4 rounded-full hover:shadow-[0_10px_20px_rgba(212,175,55,0.3)] transition-all">Subscribe</button>
            </form>
        </div>
    </section>

    <!-- 16. Premium Footer -->
    <footer class="bg-charcoal-900 text-white/70 pt-20 pb-10 relative z-10 border-t border-gold-500/20">
        <div class="bg-grain"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
                <!-- Brand -->
                <div class="col-span-1 md:col-span-1">
                    <img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-16 mb-6 object-contain bg-white/10 p-2 rounded-lg">
                    <p class="text-sm leading-relaxed mb-6">World-class Ayurvedic formulations crafted for the modern lifestyle. Purity, Potency, and Performance.</p>
                    <div class="flex space-x-4">
                        <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center hover:border-gold-500 hover:text-gold-400 transition-colors"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center hover:border-gold-500 hover:text-gold-400 transition-colors"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center hover:border-gold-500 hover:text-gold-400 transition-colors"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>
                
                <!-- Links -->
                <div>
                    <h4 class="text-white font-serif text-lg mb-6">Explore</h4>
                    <ul class="space-y-3">
                        <li><a href="index.html" class="text-gold-400 text-sm">Home</a></li>
                        <li><a href="products.html" class="hover:text-gold-400 transition-colors text-sm">All Products</a></li>
                        <li><a href="ingredients.html" class="hover:text-gold-400 transition-colors text-sm">Our Ingredients</a></li>
                        <li><a href="about.html" class="hover:text-gold-400 transition-colors text-sm">About Us</a></li>
                    </ul>
                </div>
                
                <!-- Support -->
                <div>
                    <h4 class="text-white font-serif text-lg mb-6">Support</h4>
                    <ul class="space-y-3">
                        <li><a href="contact.html" class="hover:text-gold-400 transition-colors text-sm">Contact Us</a></li>
                        <li><a href="#" class="hover:text-gold-400 transition-colors text-sm">Shipping Policy</a></li>
                        <li><a href="#" class="hover:text-gold-400 transition-colors text-sm">Refund Policy</a></li>
                        <li><a href="#" class="hover:text-gold-400 transition-colors text-sm">FAQs</a></li>
                    </ul>
                </div>
                
                <!-- Payment Badges -->
                <div>
                    <h4 class="text-white font-serif text-lg mb-6">Secure Checkout</h4>
                    <div class="flex flex-wrap gap-2 text-2xl text-white/50">
                        <i class="fab fa-cc-visa hover:text-white transition-colors"></i>
                        <i class="fab fa-cc-mastercard hover:text-white transition-colors"></i>
                        <i class="fab fa-cc-amex hover:text-white transition-colors"></i>
                        <i class="fab fa-cc-paypal hover:text-white transition-colors"></i>
                    </div>
                    <div class="mt-8">
                        <h4 class="text-white font-serif text-lg mb-4">Certifications</h4>
                        <div class="flex gap-2">
                            <span class="px-2 py-1 border border-white/20 rounded text-[10px] uppercase font-bold">GMP</span>
                            <span class="px-2 py-1 border border-white/20 rounded text-[10px] uppercase font-bold">FSSAI</span>
                            <span class="px-2 py-1 border border-white/20 rounded text-[10px] uppercase font-bold">AYUSH</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center">
                <p class="text-xs">&copy; 2026 THE HANURAAM WELLNESS. All rights reserved.</p>
                <div class="flex space-x-4 mt-4 md:mt-0 text-xs">
                    <a href="#" class="hover:text-gold-400 transition-colors">Privacy Policy</a>
                    <a href="#" class="hover:text-gold-400 transition-colors">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        // Initialize Animations
        AOS.init({{
            once: true,
            offset: 50,
            duration: 800,
            easing: 'ease-out-cubic',
        }});
        
        // Mobile Menu Toggle
        document.getElementById('mobile-menu-btn').addEventListener('click', function() {{
            var menu = document.getElementById('mobile-menu');
            if (menu.classList.contains('hidden')) {{
                menu.classList.remove('hidden');
            }} else {{
                menu.classList.add('hidden');
            }}
        }});
    </script>
</body>
</html>"""

with open("e:/ecc/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated index.html successfully!")

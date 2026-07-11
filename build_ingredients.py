import os

ingredients = [
    {
        "id": "ashwagandha",
        "num": "01",
        "name": "ASHWAGANDHA",
        "scientific": "Withania somnifera",
        "image": "assets/botanical_ashwagandha.png",
        "title": "Ashwagandha Root",
        "desc": "Revered as a <span class='italic text-gold-400'>Rasayana</span> (rejuvenator) in Ayurveda for over 3,000 years, Ashwagandha is nature's ultimate adaptogen. It intelligently helps the body manage stress, lowers cortisol levels, and restores foundational vitality.",
        "compounds": "Withanolides (5% standardized)",
        "source": "Roots harvested at peak maturity",
        "benefits": [
            {"icon": "fa-brain", "title": "Stress & Cortisol Regulation", "desc": "Clinically shown to support healthy cortisol levels and promote a calm state of mind."},
            {"icon": "fa-bolt", "title": "Endurance & Vitality", "desc": "Enhances cellular energy production (ATP) for sustained, jitter-free stamina."}
        ],
        "products": [
            {"name": "Ashwagandha Plus", "img": "assets/prod_ashwagandha.png", "desc": "Advanced Stress & Vitality Support", "price": "1,899", "link": "product_ashwagandha.html"}
        ]
    },
    {
        "id": "shilajit",
        "num": "02",
        "name": "SHILAJIT",
        "scientific": "Asphaltum punjabianum",
        "image": "assets/botanical_shilajit.png",
        "title": "Himalayan Shilajit",
        "desc": "Sourced from high-altitude Himalayan rocks between 16,000–18,000 ft, Shilajit is known as the 'Conqueror of Mountains'. It is a potent source of fulvic acid and trace minerals.",
        "compounds": "Fulvic Acid, Humic Acid, 85+ Minerals",
        "source": "High-altitude Himalayan rock exudate",
        "benefits": [
            {"icon": "fa-mountain", "title": "Deep Cellular Vitality", "desc": "Supports normal cellular energy (ATP) production and reduces chronic fatigue."},
            {"icon": "fa-shield-halved", "title": "Powerful Antioxidant", "desc": "Neutralizes free radicals and supports rejuvenation at a cellular level."}
        ],
        "products": [
            {"name": "Shilajit Gold", "img": "assets/prod_shilajit.png", "desc": "Pure Himalayan Shilajit Resin", "price": "3,299", "link": "product_shilajit.html"}
        ]
    },
    {
        "id": "gokshura",
        "num": "03",
        "name": "GOKSHURA",
        "scientific": "Tribulus terrestris",
        "image": "assets/botanical_gokshura.png",
        "title": "Gokshura Extract",
        "desc": "Revered in Ayurveda as a <span class='italic text-gold-400'>Balya</span> (strength promoting) herb, Gokshura naturally supports physical endurance, muscle recovery, and male vitality.",
        "compounds": "Saponins (Protodioscin), Flavonoids",
        "source": "Fruits and aerial parts",
        "benefits": [
            {"icon": "fa-dumbbell", "title": "Physical Endurance", "desc": "Supports physical strength, endurance and muscular performance."},
            {"icon": "fa-mars", "title": "Male Vitality", "desc": "Helps support healthy testosterone levels and hormonal balance naturally."}
        ],
        "products": [
            {"name": "Gokshura Power", "img": "assets/prod_gokshura.png", "desc": "Male Vitality Support", "price": "1,799", "link": "product_gokshura.html"}
        ]
    },
    {
        "id": "ginseng",
        "num": "04",
        "name": "PANAX GINSENG",
        "scientific": "Panax ginseng",
        "image": "assets/botanical_ginseng.png",
        "title": "Panax Ginseng Root",
        "desc": "Revered in Traditional Chinese Medicine for thousands of years as a tonic for vitality, Ginseng helps the body adapt to physical and mental stress.",
        "compounds": "Ginsenosides (Rb1, Rg1, Re, Rd)",
        "source": "Slow-growing root",
        "benefits": [
            {"icon": "fa-battery-full", "title": "Sustained Energy", "desc": "Supports healthy energy, endurance and physical performance without jitters."},
            {"icon": "fa-lightbulb", "title": "Cognitive Clarity", "desc": "Helps support cognitive function, focus and mental clarity."}
        ],
        "products": [
            {"name": "Panax Ginseng", "img": "assets/prod_ginseng.png", "desc": "Adaptogenic Energy Booster", "price": "2,199", "link": "product_ginseng.html"}
        ]
    },
    {
        "id": "chaste",
        "num": "05",
        "name": "CHASTE TREE",
        "scientific": "Vitex agnus-castus",
        "image": "assets/botanical_chaste_tree.png",
        "title": "Chaste Tree Berry",
        "desc": "Used for over 2,500 years in traditional botanical medicine, Chaste Tree gently supports natural hormonal equilibrium and female wellness.",
        "compounds": "Agnuside, Flavonoids",
        "source": "Potent berries of the Mediterranean shrub",
        "benefits": [
            {"icon": "fa-venus", "title": "Hormonal Balance", "desc": "Supports natural hormonal balance through pituitary gland modulation."},
            {"icon": "fa-spa", "title": "Emotional Wellness", "desc": "Promotes emotional balance and stabilizes mood swings."}
        ],
        "products": [
            {"name": "Chaste Tree Blend", "img": "assets/prod_chaste.png", "desc": "Hormonal Balance Support", "price": "1,599", "link": "product_chaste.html"}
        ]
    },
    {
        "id": "kaunch",
        "num": "06",
        "name": "KAUNCH BEEJ",
        "scientific": "Mucuna pruriens",
        "image": "assets/botanical_kaunch_beej.png",
        "title": "Kaunch Beej Extract",
        "desc": "A natural source of L-DOPA, Kaunch Beej is traditionally used in Ayurvedic practices for reproductive wellness, vitality, and nervous system health.",
        "compounds": "L-DOPA, Alkaloids",
        "source": "Seeds of Mucuna pruriens",
        "benefits": [
            {"icon": "fa-child-reaching", "title": "Nervous System Support", "desc": "Helps support nervous system health and overall mood balance."},
            {"icon": "fa-fire", "title": "Vitality & Strength", "desc": "Traditionally used to support natural vitality, stamina and physical performance."}
        ],
        "products": [
            {"name": "KORDY X", "img": "assets/prod_kordy_x.png", "desc": "Effervescent Vitality", "price": "1,499", "link": "product_kordy_x.html"}
        ]
    },
    {
        "id": "piperine",
        "num": "07",
        "name": "KALI MIRCH",
        "scientific": "Piper nigrum",
        "image": "assets/botanical_piperine.png",
        "title": "Piperine (Black Pepper)",
        "desc": "Known as Kali Mirch in Ayurveda, Piperine is nature's ultimate bio-enhancer. It significantly increases the bioavailability and absorption of other nutrients and herbs.",
        "compounds": "Piperine, Essential Oils",
        "source": "Dried fruits (peppercorns)",
        "benefits": [
            {"icon": "fa-arrows-to-circle", "title": "Bioavailability Enhancer", "desc": "Clinically proven to enhance the absorption of vital nutrients and botanical extracts."},
            {"icon": "fa-leaf", "title": "Digestive Support", "desc": "Supports healthy digestion and nutrient assimilation."}
        ],
        "products": [
            {"name": "JOYFLEX PLUS", "img": "assets/prod_joyflex.png", "desc": "Advanced Joint Relief Formula", "price": "1,899", "link": "product_joyflex.html"}
        ]
    }
]

html_head = r'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ingredients | THE HANURAAM WELLNESS</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: { 800: '#2E5E4E', 900: '#1F4D3B' },
                        gold: { 100: '#fcf8f0', 200: '#f5e8c4', 300: '#edd898', 400: '#D4AF37', 500: '#c59d29', 600: '#a37f1e' },
                        earth: { 50: '#F8F5EF', 100: '#EBE5D9', 200: '#D6CDBA', 800: '#5C5441', 900: '#4A4333' },
                        charcoal: { 800: '#2A2A2A', 900: '#1C1C1C' }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        serif: ['Playfair Display', 'serif']
                    }
                }
            }
        }
    </script>
    <style type="text/tailwindcss">
        @layer utilities {
            .glass { @apply bg-white/60 backdrop-blur-xl border border-primary-900/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.3)]; }
            .glass-card { @apply bg-white/60 backdrop-blur-md border border-primary-900/10 hover:border-gold-500/50 transition-colors duration-500; }
            .bg-gradient-gold { @apply bg-gradient-to-r from-gold-300 via-gold-400 to-gold-500; }
            .text-gradient-gold { @apply text-transparent bg-clip-text bg-gradient-to-r from-gold-300 to-gold-500; }
        }
        
        .parallax-bg {
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #163A2F; }
        ::-webkit-scrollbar-thumb { background: #D4AF37; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #c59d29; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
</head>
<body class="antialiased bg-earth-50 text-charcoal-900 selection:bg-gold-500 selection:text-primary-900 overflow-x-hidden">

    <!-- Navigation -->
    <nav class="fixed top-8 w-full z-50 glass border-b border-white/40 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20 relative">
                <div class="hidden md:flex space-x-8 items-center w-1/3">
                    <a href="index.html" class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium">Home</a>
                    <a href="about.html" class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium               ">About</a>
                    <a href="products.html" class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium">Products</a>
                </div>
                
                <div class="absolute left-1/2 -translate-x-1/2 flex items-center">
                    <a href="index.html" class="flex items-center">
                        <img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-12 object-contain hover:scale-105 transition-transform duration-500">
                    </a>
                </div>
                
                <div class="hidden md:flex space-x-6 lg:space-x-8 items-center justify-end w-1/3">
                    <a href="ingredients.html" class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium border-b-2 border-primary-900 pb-1">Ingredients</a>
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
                <a href="index.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Home</a>
                <a href="about.html" class="block py-2 text-sm uppercase tracking-widest font-medium font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold font-bold text-primary-900 border-b border-primary-900/10">About</a>
                <a href="products.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Products</a>
                <a href="ingredients.html" class="block py-2 text-sm uppercase tracking-widest font-medium font-bold text-primary-900 border-b border-primary-900/10">Ingredients</a>
                <a href="certifications.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Certifications</a>
                <a href="thankyou.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Thank You</a>
                <a href="contact.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900">Contact</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden parallax-bg" style="background-image: url('assets/hero_bg.png');">
        <div class="absolute inset-0 bg-earth-50/80 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-transparent via-primary-900/80 to-primary-900 z-0"></div>
        
        <!-- Floating Elements -->
        <img src="assets/botanical_ashwagandha.png" alt="Herb" class="absolute top-1/4 left-10 w-48 md:w-80 opacity-20 rotate-[-15deg] mix-blend-screen blur-[2px]" data-aos="fade-right" data-aos-duration="2000">
        <img src="assets/botanical_shilajit.png" alt="Resin" class="absolute bottom-1/4 right-10 w-48 md:w-80 opacity-20 rotate-[15deg] mix-blend-screen blur-[2px]" data-aos="fade-left" data-aos-duration="2000">
        
        <div class="relative z-10 text-center max-w-4xl mx-auto px-4 pt-20">
            <span class="inline-block py-1 px-4 border border-gold-400/30 rounded-full text-gold-400 text-xs tracking-[0.3em] uppercase mb-8" data-aos="fade-down">Materia Medica</span>
            <h1 class="text-5xl md:text-7xl lg:text-8xl font-serif font-bold mb-6 leading-tight" data-aos="zoom-in" data-aos-delay="100">
                Nature's <br/><span class="text-gradient-gold italic">Masterpieces</span>
            </h1>
            <p class="text-lg md:text-xl text-primary-900/70 font-light leading-relaxed max-w-2xl mx-auto mb-12" data-aos="fade-up" data-aos-delay="200">
                Discover the pure, potent botanical sources and ancient wisdom behind THE HANURAAM WELLNESS formulations. Each ingredient is a luxurious gift from the earth, meticulously sourced and scientifically validated.
            </p>
            <div data-aos="fade-up" data-aos-delay="300">
                <a href="#explore" class="inline-flex flex-col items-center text-gold-400 hover:text-primary-900 transition-colors duration-300 group">
                    <span class="text-xs uppercase tracking-widest mb-4">Explore Botanical Library</span>
                    <i class="fas fa-chevron-down animate-bounce text-xl"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Ingredient Navigation Grid -->
    <section id="explore" class="py-24 bg-earth-50 relative z-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-3xl md:text-4xl font-serif font-bold mb-4">The Botanical <span class="text-gradient-gold italic">Library</span></h2>
                <div class="h-px w-24 bg-gold-500/50 mx-auto"></div>
            </div>
            
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
'''

html_grid = ""
for i, ing in enumerate(ingredients):
    delay = (i % 4) * 100
    html_grid += f'''
                <!-- Card {i+1} -->
                <a href="#ingredient-{ing['id']}" class="group block relative overflow-hidden rounded-xl aspect-[3/4] glass-card" data-aos="fade-up" data-aos-delay="{delay}">
                    <div class="absolute inset-0 bg-gradient-to-t from-earth-100 via-white/50 to-transparent z-10"></div>
                    <img src="{ing['image']}" alt="{ing['name']}" class="absolute inset-0 w-full h-full object-cover object-center group-hover:scale-110 transition-transform duration-700 opacity-60 group-hover:opacity-100 mix-blend-multiply group-hover:mix-blend-normal">
                    <div class="absolute inset-x-0 bottom-0 p-6 z-20 transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                        <p class="text-gold-400 text-[10px] tracking-widest uppercase mb-1 opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100">{ing['scientific']}</p>
                        <h3 class="text-xl font-serif font-bold text-primary-900 group-hover:text-gold-400 transition-colors">{ing['name']}</h3>
                    </div>
                </a>
'''

html_middle = '''
            </div>
            
            <div class="text-center mt-12">
                <p class="text-primary-900/50 text-sm italic font-serif">Featuring over 20+ ethically sourced botanical ingredients.</p>
            </div>
        </div>
    </section>
'''

html_spotlights = ""
for i, ing in enumerate(ingredients):
    # Alternate left/right layout
    is_left = i % 2 == 0
    bg_color = "bg-white" if is_left else "bg-earth-50"
    
    img_block = f'''
                <div class="w-full lg:w-1/2" data-aos="{ 'fade-right' if is_left else 'fade-left' }">
                    <div class="relative rounded-2xl overflow-hidden glass-card p-4 lg:p-8 aspect-square flex items-center justify-center">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-gold-500/10 via-transparent to-transparent"></div>
                        <img src="{ing['image']}" alt="{ing['name']}" class="w-full h-full object-contain filter drop-shadow-[0_20px_30px_rgba(0,0,0,0.5)]">
                    </div>
                </div>
    '''
    
    content_block = f'''
                <div class="w-full lg:w-1/2" data-aos="{ 'fade-left' if is_left else 'fade-right' }">
                    <div class="flex items-center space-x-4 mb-4">
                        <span class="text-gold-400 font-bold text-2xl font-serif">{ing['num']}</span>
                        <div class="h-px w-12 bg-gold-400"></div>
                        <span class="text-xs tracking-[0.2em] uppercase text-primary-900/60 font-semibold">{ing['scientific']}</span>
                    </div>
                    
                    <h2 class="text-4xl md:text-5xl font-serif font-bold mb-6">{ing['title']}</h2>
                    
                    <p class="text-primary-900/70 text-lg font-light leading-relaxed mb-8">
                        {ing['desc']}
                    </p>
                    
                    <div class="grid grid-cols-2 gap-8 mb-10 border-t border-b border-primary-900/10 py-8">
                        <div>
                            <h4 class="text-[10px] text-gold-400 uppercase tracking-widest font-bold mb-2">Active Compounds</h4>
                            <p class="text-sm text-primary-900/80 font-medium">{ing['compounds']}</p>
                        </div>
                        <div>
                            <h4 class="text-[10px] text-gold-400 uppercase tracking-widest font-bold mb-2">Botanical Source</h4>
                            <p class="text-sm text-primary-900/80 font-medium">{ing['source']}</p>
                        </div>
                    </div>
                    
                    <!-- Interactive Benefits -->
                    <h4 class="text-sm text-primary-900 font-bold mb-4 font-serif italic">Key Wellness Benefits</h4>
                    <div class="space-y-4">
                        <div class="flex items-start space-x-4 group cursor-default">
                            <div class="w-10 h-10 rounded-full border border-gold-500/30 flex items-center justify-center flex-shrink-0 group-hover:bg-gold-500/10 transition-colors">
                                <i class="fas {ing['benefits'][0]['icon']} text-gold-400 text-sm"></i>
                            </div>
                            <div>
                                <h5 class="text-primary-900 font-semibold text-sm mb-1 group-hover:text-gold-400 transition-colors">{ing['benefits'][0]['title']}</h5>
                                <p class="text-primary-900/60 text-xs leading-relaxed">{ing['benefits'][0]['desc']}</p>
                            </div>
                        </div>
                        <div class="flex items-start space-x-4 group cursor-default">
                            <div class="w-10 h-10 rounded-full border border-gold-500/30 flex items-center justify-center flex-shrink-0 group-hover:bg-gold-500/10 transition-colors">
                                <i class="fas {ing['benefits'][1]['icon']} text-gold-400 text-sm"></i>
                            </div>
                            <div>
                                <h5 class="text-primary-900 font-semibold text-sm mb-1 group-hover:text-gold-400 transition-colors">{ing['benefits'][1]['title']}</h5>
                                <p class="text-primary-900/60 text-xs leading-relaxed">{ing['benefits'][1]['desc']}</p>
                            </div>
                        </div>
                    </div>
                </div>
    '''

    layout = f'<div class="flex flex-col lg:flex-row items-center gap-16">{img_block}{content_block}</div>' if is_left else f'<div class="flex flex-col lg:flex-row-reverse items-center gap-16">{img_block}{content_block}</div>'

    html_spotlights += f'''
    <!-- Premium Ingredient Spotlight: {ing['name']} -->
    <section id="ingredient-{ing['id']}" class="py-32 relative {bg_color} border-t border-gold-500/10">
        <!-- Giant Watermark -->
        <div class="absolute top-20 left-0 w-full overflow-hidden whitespace-nowrap pointer-events-none select-none">
            <span class="text-[10rem] md:text-[20rem] font-serif font-bold text-primary-900/[0.02] tracking-tighter">{ing['name']}</span>
        </div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            {layout}
        </div>
    </section>
    '''

html_end = r'''
    <!-- Found in Our Products Section -->
    <section class="py-24 bg-earth-100 border-t border-primary-900/10 relative z-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-end mb-12" data-aos="fade-up">
                <div>
                    <h3 class="text-2xl font-serif font-bold text-primary-900 mb-2">Experience the <span class="text-gradient-gold italic">Potency</span></h3>
                    <p class="text-primary-900/60 text-sm">Discover premium formulations featuring our highest grade extracts.</p>
                </div>
                <a href="products.html" class="hidden md:inline-flex text-xs uppercase tracking-widest text-gold-400 hover:text-primary-900 transition-colors items-center">
                    Shop All Products <i class="fas fa-arrow-right ml-2 text-[10px]"></i>
                </a>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Product Card -->
                <div class="glass-card rounded-2xl p-6 group flex flex-col" data-aos="fade-up" data-aos-delay="100">
                    <div class="relative aspect-square mb-6 bg-white/60 rounded-xl overflow-hidden flex items-center justify-center p-8">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-gold-500/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        <img src="assets/prod_ashwagandha.png" alt="Ashwagandha Plus" class="w-full h-full object-contain filter drop-shadow-xl group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <h4 class="text-lg font-bold text-primary-900 mb-1">Ashwagandha Plus</h4>
                    <p class="text-primary-900/50 text-xs mb-4 flex-grow">Stress & Vitality Support</p>
                    <div class="flex items-center justify-between mb-6">
                        <span class="text-gold-400 font-serif font-bold text-xl">₹1,899</span>
                    </div>
                    <div class="flex gap-2 mt-auto">
                        <button onclick="addToCart(this)" class="flex-1 bg-white/70 hover:bg-gold-400 text-primary-900 hover:text-primary-900 transition-colors py-3 rounded-lg text-[10px] font-bold uppercase tracking-widest">
                            Add to Cart
                        </button>
                        <a href="product_ashwagandha.html" class="flex-none w-10 h-10 flex items-center justify-center bg-white/60 hover:bg-white/70 border border-primary-900/10 rounded-lg text-primary-900 transition-colors">
                            <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
                
                <!-- Product Card 2 -->
                <div class="glass-card rounded-2xl p-6 group flex flex-col" data-aos="fade-up" data-aos-delay="200">
                    <div class="relative aspect-square mb-6 bg-white/60 rounded-xl overflow-hidden flex items-center justify-center p-8">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-gold-500/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        <img src="assets/prod_kordy_x.png" alt="KORDY X" class="w-full h-full object-contain filter drop-shadow-xl group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <h4 class="text-lg font-bold text-primary-900 mb-1">KORDY X</h4>
                    <p class="text-primary-900/50 text-xs mb-4 flex-grow">Effervescent Vitality</p>
                    <div class="flex items-center justify-between mb-6">
                        <span class="text-gold-400 font-serif font-bold text-xl">₹1,499</span>
                    </div>
                    <div class="flex gap-2 mt-auto">
                        <button onclick="addToCart(this)" class="flex-1 bg-white/70 hover:bg-gold-400 text-primary-900 hover:text-primary-900 transition-colors py-3 rounded-lg text-[10px] font-bold uppercase tracking-widest">
                            Add to Cart
                        </button>
                        <a href="product_kordy_x.html" class="flex-none w-10 h-10 flex items-center justify-center bg-white/60 hover:bg-white/70 border border-primary-900/10 rounded-lg text-primary-900 transition-colors">
                            <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <!-- Product Card 3 -->
                <div class="glass-card rounded-2xl p-6 group flex flex-col" data-aos="fade-up" data-aos-delay="300">
                    <div class="relative aspect-square mb-6 bg-white/60 rounded-xl overflow-hidden flex items-center justify-center p-8">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-gold-500/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        <img src="assets/prod_shilajit.png" alt="Shilajit Gold" class="w-full h-full object-contain filter drop-shadow-xl group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <h4 class="text-lg font-bold text-primary-900 mb-1">Shilajit Gold</h4>
                    <p class="text-primary-900/50 text-xs mb-4 flex-grow">Pure Himalayan Resin</p>
                    <div class="flex items-center justify-between mb-6">
                        <span class="text-gold-400 font-serif font-bold text-xl">₹3,299</span>
                    </div>
                    <div class="flex gap-2 mt-auto">
                        <button onclick="addToCart(this)" class="flex-1 bg-white/70 hover:bg-gold-400 text-primary-900 hover:text-primary-900 transition-colors py-3 rounded-lg text-[10px] font-bold uppercase tracking-widest">
                            Add to Cart
                        </button>
                        <a href="product_shilajit.html" class="flex-none w-10 h-10 flex items-center justify-center bg-white/60 hover:bg-white/70 border border-primary-900/10 rounded-lg text-primary-900 transition-colors">
                            <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>

                <!-- Product Card 4 -->
                <div class="glass-card rounded-2xl p-6 group flex flex-col" data-aos="fade-up" data-aos-delay="400">
                    <div class="relative aspect-square mb-6 bg-white/60 rounded-xl overflow-hidden flex items-center justify-center p-8">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-gold-500/20 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        <img src="assets/prod_joyflex.png" alt="JOYFLEX PLUS" class="w-full h-full object-contain filter drop-shadow-xl group-hover:scale-105 transition-transform duration-700">
                    </div>
                    <h4 class="text-lg font-bold text-primary-900 mb-1">JOYFLEX PLUS</h4>
                    <p class="text-primary-900/50 text-xs mb-4 flex-grow">Advanced Joint Relief</p>
                    <div class="flex items-center justify-between mb-6">
                        <span class="text-gold-400 font-serif font-bold text-xl">₹1,899</span>
                    </div>
                    <div class="flex gap-2 mt-auto">
                        <button onclick="addToCart(this)" class="flex-1 bg-white/70 hover:bg-gold-400 text-primary-900 hover:text-primary-900 transition-colors py-3 rounded-lg text-[10px] font-bold uppercase tracking-widest">
                            Add to Cart
                        </button>
                        <a href="product_joyflex.html" class="flex-none w-10 h-10 flex items-center justify-center bg-white/60 hover:bg-white/70 border border-primary-900/10 rounded-lg text-primary-900 transition-colors">
                            <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
            </div>
            
            <div class="mt-12 text-center md:hidden">
                <a href="products.html" class="inline-flex text-xs uppercase tracking-widest text-gold-400 hover:text-primary-900 transition-colors items-center border border-gold-400/30 px-6 py-3 rounded-full">
                    Shop All Products
                </a>
            </div>
        </div>
    </section>

    <!-- Science Meets Ayurveda -->
    <section class="py-24 bg-earth-50 relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16" data-aos="fade-up">
                <span class="text-gold-500 tracking-[0.2em] uppercase text-xs mb-4 block font-semibold">The Hanuraam Standard</span>
                <h2 class="text-3xl md:text-5xl font-serif font-bold mb-6 text-primary-900">Science Meets <span class="text-gradient-gold italic">Ayurveda</span></h2>
                <p class="text-primary-900/60 max-w-2xl mx-auto font-light">Every ingredient goes through a rigorous multi-step journey to ensure maximum potency, safety, and purity.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                <!-- Step 1 -->
                <div class="text-center relative" data-aos="fade-up" data-aos-delay="100">
                    <div class="w-20 h-20 mx-auto bg-earth-50 rounded-full border border-gold-500/30 flex items-center justify-center mb-6 relative z-10">
                        <i class="fas fa-seedling text-gold-400 text-2xl"></i>
                    </div>
                    <div class="hidden md:block absolute top-10 left-1/2 w-full h-px bg-gold-500/20 z-0"></div>
                    <h4 class="text-primary-900 font-bold mb-2">Ethical Sourcing</h4>
                    <p class="text-primary-900/50 text-xs leading-relaxed">Harvested at peak potency from traditional geographic origins.</p>
                </div>
                <!-- Step 2 -->
                <div class="text-center relative" data-aos="fade-up" data-aos-delay="200">
                    <div class="w-20 h-20 mx-auto bg-earth-50 rounded-full border border-gold-500/30 flex items-center justify-center mb-6 relative z-10">
                        <i class="fas fa-flask text-gold-400 text-2xl"></i>
                    </div>
                    <div class="hidden md:block absolute top-10 left-1/2 w-full h-px bg-gold-500/20 z-0"></div>
                    <h4 class="text-primary-900 font-bold mb-2">Extraction</h4>
                    <p class="text-primary-900/50 text-xs leading-relaxed">Advanced supercritical fluid extraction preserves delicate active compounds.</p>
                </div>
                <!-- Step 3 -->
                <div class="text-center relative" data-aos="fade-up" data-aos-delay="300">
                    <div class="w-20 h-20 mx-auto bg-earth-50 rounded-full border border-gold-500/30 flex items-center justify-center mb-6 relative z-10">
                        <i class="fas fa-microscope text-gold-400 text-2xl"></i>
                    </div>
                    <div class="hidden md:block absolute top-10 left-1/2 w-full h-px bg-gold-500/20 z-0"></div>
                    <h4 class="text-primary-900 font-bold mb-2">Standardization</h4>
                    <p class="text-primary-900/50 text-xs leading-relaxed">Tested for exact percentages of key bio-actives (e.g. Withanolides).</p>
                </div>
                <!-- Step 4 -->
                <div class="text-center relative" data-aos="fade-up" data-aos-delay="400">
                    <div class="w-20 h-20 mx-auto bg-earth-50 rounded-full border border-gold-500/30 flex items-center justify-center mb-6 relative z-10">
                        <i class="fas fa-check-double text-gold-400 text-2xl"></i>
                    </div>
                    <h4 class="text-primary-900 font-bold mb-2">Purity Testing</h4>
                    <p class="text-primary-900/50 text-xs leading-relaxed">Rigorous heavy metal, microbial, and toxin screening.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-24 bg-white border-t border-gold-500/10 relative z-20">
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12" data-aos="fade-up">
                <h2 class="text-3xl font-serif font-bold text-primary-900 mb-4">Frequently Asked <span class="text-gradient-gold italic">Questions</span></h2>
            </div>
            
            <div class="space-y-4" data-aos="fade-up" data-aos-delay="100">
                <!-- Accordion Item 1 -->
                <div class="glass-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 text-left flex justify-between items-center focus:outline-none" onclick="toggleFaq(this)">
                        <span class="font-bold text-primary-900">Are your ingredients organic?</span>
                        <i class="fas fa-plus text-gold-400 text-sm transition-transform duration-300"></i>
                    </button>
                    <div class="px-6 pb-5 text-primary-900/60 text-sm font-light hidden">
                        We prioritize organic cultivation wherever possible. All our botanical ingredients are ethically wild-harvested or grown without synthetic pesticides, and they undergo strict laboratory testing to ensure zero heavy metals or chemical residue.
                    </div>
                </div>
                <!-- Accordion Item 2 -->
                <div class="glass-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 text-left flex justify-between items-center focus:outline-none" onclick="toggleFaq(this)">
                        <span class="font-bold text-primary-900">What does "Standardized Extract" mean?</span>
                        <i class="fas fa-plus text-gold-400 text-sm transition-transform duration-300"></i>
                    </button>
                    <div class="px-6 pb-5 text-primary-900/60 text-sm font-light hidden">
                        A standardized extract ensures that every batch contains a guaranteed, specific percentage of the herb's active compound (like 5% Withanolides in Ashwagandha). This ensures consistent clinical efficacy in every dose.
                    </div>
                </div>
                <!-- Accordion Item 3 -->
                <div class="glass-card rounded-xl overflow-hidden">
                    <button class="w-full px-6 py-5 text-left flex justify-between items-center focus:outline-none" onclick="toggleFaq(this)">
                        <span class="font-bold text-primary-900">Are they safe for long-term use?</span>
                        <i class="fas fa-plus text-gold-400 text-sm transition-transform duration-300"></i>
                    </button>
                    <div class="px-6 pb-5 text-primary-900/60 text-sm font-light hidden">
                        Most Ayurvedic adaptogens and rasayanas are designed for long-term daily use to build foundational health. However, we always recommend consulting with your healthcare provider if you have specific medical conditions or are pregnant.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Final CTA -->
    <section class="py-32 relative overflow-hidden flex items-center justify-center bg-earth-100">
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-gold-500/20 via-transparent to-transparent z-0"></div>
        <div class="relative z-10 text-center max-w-2xl px-4" data-aos="zoom-in">
            <i class="fas fa-leaf text-4xl text-gold-400 mb-6 block"></i>
            <h2 class="text-4xl md:text-5xl font-serif font-bold text-primary-900 mb-6">Begin Your Wellness Journey</h2>
            <p class="text-primary-900/70 font-light mb-10 text-lg">Experience the transformative power of ancient botanical wisdom, refined for modern living.</p>
            <a href="products.html" class="inline-block px-10 py-4 bg-gradient-gold text-primary-900 font-bold uppercase tracking-widest text-sm rounded-lg shadow-[0_10px_30px_rgba(212,175,55,0.3)] hover:-translate-y-1 hover:shadow-[0_15px_40px_rgba(212,175,55,0.4)] transition-all duration-300">
                Explore Formulations
            </a>
        </div>
    </section>

    <!-- Footer placeholder -->
    <footer>[Footer placeholder - will be synced by apply_footer.py]</footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({ once: true, duration: 1000, offset: 50 });
        
        // FAQ Accordion
        function toggleFaq(btn) {
            const content = btn.nextElementSibling;
            const icon = btn.querySelector('i');
            
            if (content.classList.contains('hidden')) {
                content.classList.remove('hidden');
                icon.classList.remove('fa-plus');
                icon.classList.add('fa-minus', 'rotate-180');
            } else {
                content.classList.add('hidden');
                icon.classList.remove('fa-minus', 'rotate-180');
                icon.classList.add('fa-plus');
            }
        }
        
        // Sticky Nav logic
        window.addEventListener('scroll', function() {
            var nav = document.querySelector('nav');
            if (window.scrollY > 10) {
                nav.classList.add('bg-white/95');
                nav.classList.remove('glass', 'border-primary-900/10');
            } else {
                nav.classList.add('glass', 'border-primary-900/10');
                nav.classList.remove('bg-white/95');
            }
        });

        // Add to Cart Logic
        let cartCount = 0;
        function addToCart(btn) {
            cartCount++;
            document.querySelectorAll('.cart-counter').forEach(el => {
                el.innerText = cartCount;
                el.classList.add('scale-125');
                setTimeout(() => el.classList.remove('scale-125'), 300);
            });
            if (btn && btn.innerHTML) {
                let originalHtml = btn.innerHTML;
                btn.innerHTML = '<i class="fas fa-check mr-2"></i> ADDED';
                setTimeout(() => {
                    btn.innerHTML = originalHtml;
                }, 2000);
            }
        }
    </script>
</body>
</html>'''

with open("e:/ecc/ingredients.html", "w", encoding="utf-8") as f:
    f.write(html_head + html_grid + html_middle + html_spotlights + html_end)

print("Generated full luxury ingredients.html successfully!")

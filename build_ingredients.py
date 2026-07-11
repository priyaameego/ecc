import json

ingredients = [
    {
        "num": "01",
        "name": "ASHWAGANDHA",
        "scientific": "Withania somnifera",
        "image": "assets/botanical_ashwagandha.png",
        "source": "Derived from the root of Withania somnifera, a powerful adaptogenic herb.",
        "compounds": "Naturally rich in Withanolides, its key active compounds.",
        "heritage": "Revered in Ayurveda for centuries as a Rasayana (rejuvenator).",
        "uses": "Traditionally used to help the body manage stress and support overall well-being.",
        "benefits": [
            "Known to support healthy energy levels and mental clarity.",
            "Valued for its role in promoting balance and vitality.",
            "Helps regulate cortisol and mood.",
            "Supports restorative sleep cycles."
        ],
        "products": [
            {"name": "KORDY X", "img": "assets/cat_vitality.png", "price": "₹2,499"}
        ]
    },
    {
        "num": "02",
        "name": "SHILAJIT",
        "scientific": "Asphaltum punjabianum",
        "image": "assets/botanical_shilajit.png",
        "source": "Sourced from high-altitude Himalayan rocks between 16,000–18,000 ft. Purified traditionally.",
        "compounds": "Rich in Fulvic Acid, Humic Acid, and 85+ beneficial trace elements.",
        "heritage": "Described in Ayurveda as the 'Conqueror of Mountains and Destroyer of Weakness'.",
        "uses": "Traditionally used to support strength, stamina, and deep vitality.",
        "benefits": [
            "Naturally contains Fulvic Acid for high mineral absorption.",
            "Helps support normal cellular energy (ATP) production and reduce fatigue.",
            "Supports overall male wellness and natural performance.",
            "Acts as a powerful antioxidant and rejuvenating agent."
        ],
        "products": [
            {"name": "SHILAJIT PRO", "img": "assets/cat_joint.png", "price": "₹1,899"}
        ]
    },
    {
        "num": "03",
        "name": "PANAX GINSENG",
        "scientific": "Panax ginseng",
        "image": "assets/botanical_ginseng.png",
        "source": "Derived from the slow-growing root of Panax ginseng, a premium adaptogenic herb.",
        "compounds": "Rich in Ginsenosides (Rb1, Rg1, Re, Rd) – the active adaptogenic saponins.",
        "heritage": "Revered in Traditional Chinese Medicine for thousands of years as a tonic for vitality.",
        "uses": "Adaptogenic herb known to help the body adapt to physical and mental stress.",
        "benefits": [
            "Supports healthy energy, endurance and physical performance.",
            "Helps support cognitive function, focus and mental clarity.",
            "Traditionally used to promote stamina and overall wellness.",
            "Supports immune system modulation."
        ],
        "products": [
            {"name": "KORDY X", "img": "assets/cat_vitality.png", "price": "₹2,499"}
        ]
    },
    {
        "num": "04",
        "name": "GOKSHURA",
        "scientific": "Tribulus terrestris",
        "image": "assets/botanical_gokshura.png",
        "source": "Derived from the fruits and aerial parts of the Tribulus terrestris plant.",
        "compounds": "Rich in Saponins (Protodioscin), Flavonoids & Alkaloids.",
        "heritage": "Revered in Ayurveda as a Vrishya (aphrodisiac) & Balya (strength promoting) herb.",
        "uses": "Traditionally used in Ayurveda to support male vitality and reproductive wellness.",
        "benefits": [
            "Naturally rich in Protodioscin, a key active saponin.",
            "Helps support healthy testosterone levels and hormonal balance.",
            "Supports physical strength, endurance and muscular performance.",
            "Known to support healthy urinary function."
        ],
        "products": [
            {"name": "KORDY X", "img": "assets/cat_vitality.png", "price": "₹2,499"},
            {"name": "VITALITY PACK", "img": "assets/cat_joint.png", "price": "₹3,999"}
        ]
    },
    {
        "num": "05",
        "name": "DAMIANA",
        "scientific": "Turnera diffusa",
        "image": "assets/botanical_damiana.png",
        "source": "Derived from the leaves and aerial parts of Turnera diffusa, natively found in Central America.",
        "compounds": "Naturally contains Flavonoids, Arbutin, Terpenoids, Tannins and Essential Oils.",
        "heritage": "Traditionally valued in ancient herbal medicine for vitality and overall well-being.",
        "uses": "Helps the body cope with everyday physical and mental stress.",
        "benefits": [
            "Traditionally valued for supporting male reproductive wellness.",
            "Commonly included in botanical vitality formulations.",
            "Acts as a nervine relaxant to support mood.",
            "Supports healthy circulation."
        ],
        "products": [
            {"name": "KORDY X", "img": "assets/cat_vitality.png", "price": "₹2,499"}
        ]
    },
    {
        "num": "06",
        "name": "CHASTE TREE",
        "scientific": "Vitex agnus-castus",
        "image": "assets/botanical_chaste_tree.png",
        "source": "Sourced from the potent berries of the Vitex agnus-castus Mediterranean shrub.",
        "compounds": "Rich in Agnuside, Flavonoids, and Essential Iridoid Glycosides.",
        "heritage": "Used for over 2,500 years in traditional European botanical medicine.",
        "uses": "Supports natural hormonal balance through pituitary gland modulation.",
        "benefits": [
            "Promotes emotional balance and stabilizes mood swings.",
            "Supports healthy endocrine system function.",
            "Valued for its gentle, regulating effect on the body.",
            "Rich in powerful botanical antioxidants."
        ],
        "products": [
            {"name": "WOMEN'S BALANCE", "img": "assets/cat_mind.png", "price": "₹2,199"}
        ]
    },
    {
        "num": "07",
        "name": "KAUNCH BEEJ",
        "scientific": "Mucuna pruriens",
        "image": "assets/botanical_kaunch_beej.png",
        "source": "Derived from the seeds of Mucuna pruriens, traditionally known as Kaunch Beej.",
        "compounds": "Naturally contains L-DOPA, Alkaloids, Flavonoids, Saponins and Tannins.",
        "heritage": "Traditionally used in herbal practices for vitality, strength and overall well-being.",
        "uses": "Traditionally used to support natural vitality and stamina.",
        "benefits": [
            "Helps support nervous system health and mood balance.",
            "Traditionally used in Ayurvedic practices for reproductive wellness.",
            "May help support muscle function and physical performance.",
            "Supports overall well-being and energy levels."
        ],
        "products": [
            {"name": "KORDY X", "img": "assets/cat_vitality.png", "price": "₹2,499"}
        ]
    },
    {
        "num": "08",
        "name": "KALI MIRCH (PIPERINE)",
        "scientific": "Piper nigrum",
        "image": "assets/botanical_piperine.png",
        "source": "Derived from the dried fruits (black peppercorns) of Piper nigrum, commonly known as Kali Mirch.",
        "compounds": "Naturally contains Piperine, Essential Oils, Chavicine, Volatile Oils and Flavonoids.",
        "heritage": "Traditionally used in Ayurveda to enhance absorption, support digestion and overall well-being.",
        "uses": "Enhances the bioavailability and absorption of nutrients and herbs.",
        "benefits": [
            "Supports healthy digestion and nutrient assimilation.",
            "Traditionally used to support respiratory and immune health.",
            "Powerful antioxidant and may help reduce oxidative stress.",
            "Supports overall wellness and vitality."
        ],
        "products": [
            {"name": "IMMUNITY BLEND", "img": "assets/cat_immunity.png", "price": "₹1,299"}
        ]
    },
    {
        "num": "09",
        "name": "CURCUMIN EXTRACT",
        "scientific": "Curcuma longa",
        "image": "assets/botanical_curcumin.png",
        "source": "Derived from the root of Turmeric (Curcuma longa), nature's gold standard for joint health.",
        "compounds": "Naturally rich in Curcuminoids, its key active compounds.",
        "heritage": "Clinically researched botanical with scientifically trusted performance.",
        "uses": "Provides anti-inflammatory support, antioxidant protection, and supports joint mobility.",
        "benefits": [
            "Helps support a healthy inflammatory response.",
            "Promotes joint comfort and flexibility.",
            "Provides powerful antioxidant protection.",
            "Supports cartilage and connective tissue health.",
            "Backed by extensive scientific research."
        ],
        "products": [
            {"name": "JOYFLEX PLUS", "img": "assets/cat_joint.png", "price": "₹1,899"}
        ]
    },
    {
        "num": "10",
        "name": "BOSWELLIA SERRATA EXTRACT",
        "scientific": "Boswellia serrata",
        "image": "assets/botanical_boswellia.png",
        "source": "Derived from Boswellia serrata resin (Indian Frankincense).",
        "compounds": "Main compounds are Boswellic Acids (AKBA & KBA).",
        "heritage": "Used in Ayurveda for centuries as a pure botanical.",
        "uses": "Helps the body handle swelling and inflammation, protecting cells.",
        "benefits": [
            "Comes from the resin of the Boswellia serrata tree.",
            "Contains natural compounds called Boswellic Acids.",
            "Helps the body handle swelling and inflammation.",
            "Protects cells from damage caused by free radicals.",
            "Supports easy movement and flexible joints."
        ],
        "products": [
            {"name": "JOYFLEX PLUS", "img": "assets/cat_joint.png", "price": "₹1,899"}
        ]
    },
    {
        "num": "11",
        "name": "SALIX ALBA BARK EXTRACT",
        "scientific": "Salix alba",
        "image": "assets/botanical_salix_alba.png",
        "source": "Derived from the bark of the Salix alba tree (White Willow).",
        "compounds": "Naturally contains Salicin - a plant-based compound.",
        "heritage": "Traditionally used in herbal practices for comfort and wellness.",
        "uses": "Traditionally used in herbal practices for body comfort.",
        "benefits": [
            "Comes from the bark of the White Willow tree.",
            "Contains Salicin, a natural plant compound.",
            "Traditionally used in herbal practices for body comfort.",
            "Supports the body's natural response to everyday stress and strain.",
            "A well-known botanical used for generations."
        ],
        "products": [
            {"name": "JOYFLEX PLUS", "img": "assets/cat_joint.png", "price": "₹1,899"}
        ]
    }
]

html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ingredients Showcase | THE HANURAAM WELLNESS</title>
    <meta name="description" content="Discover the pure, potent Ayurvedic ingredients we use in our formulations.">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
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
            .glass-card { @apply bg-white/5 backdrop-blur-md border border-gold-500/20 shadow-[0_8px_32px_0_rgba(0,0,0,0.5)] hover:border-gold-500/40 transition-all duration-500; }
            .text-gradient-gold { @apply bg-clip-text text-transparent bg-gradient-to-r from-gold-600 to-gold-400; }
            .bg-gradient-gold { @apply bg-gradient-to-r from-gold-600 to-gold-500; }
        }
        body { @apply bg-primary-900 text-gray-300 font-sans overflow-x-hidden; }
        h1, h2, h3, h4, h5, h6 { @apply font-serif text-white; }
        
        .hide-scrollbar::-webkit-scrollbar { display: none; }
        .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        
        .ingredient-number {
            font-size: 8rem;
            line-height: 1;
            background: linear-gradient(to bottom, rgba(201,168,76,0.1), transparent);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: absolute;
            top: -2rem;
            left: 0rem;
            z-index: 0;
            user-select: none;
            font-family: 'Playfair Display', serif;
            font-weight: 700;
        }
        
        @media (min-width: 768px) {
            .ingredient-number {
                font-size: 14rem;
                top: -4rem;
                left: -2rem;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        @keyframes marquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .animate-marquee {
            animation: marquee 25s linear infinite;
        }
    </style>
</head>
<body class="antialiased selection:bg-gold-500 selection:text-primary-900 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-primary-800 via-primary-900 to-[#050f0b]">

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
    </div>

    <!-- Navigation -->
    <nav class="fixed top-8 w-full z-50 glass border-b border-white/40 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="flex items-center">
                        <img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-12 object-contain">
                    </a>
                </div>
                <div class="hidden md:flex space-x-8 items-center">
                    <a href="index.html" class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium">Home</a>
                    <a href="about.html" class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium">About</a>
                    <a href="products.html" class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium">Products</a>
                    <a href="ingredients.html" class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium border-b-2 border-primary-900 pb-1">Ingredients</a>
                    <a href="certifications.html" class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium">Certifications</a>
                    <a href="contact.html" class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium">Contact</a>
                    <a href="cart.html" class="text-primary-900 hover:text-gold-600 transition-colors relative">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span class="absolute -top-2 -right-2 bg-primary-900 text-gold-400 text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center">1</span>
                    </a>
                </div>
                <div class="md:hidden flex items-center space-x-4">
                    <a href="cart.html" class="text-primary-900 relative">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span class="absolute -top-2 -right-2 bg-primary-900 text-gold-400 text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center">1</span>
                    </a>
                    <button id="mobile-menu-btn" class="text-primary-900 hover:text-gold-600 focus:outline-none">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden glass border-t border-white/40">
            <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                <a href="index.html" class="block px-3 py-2 text-base font-medium text-dark hover:text-primary-900">Home</a>
                <a href="about.html" class="block px-3 py-2 text-base font-medium text-dark hover:text-primary-900">About</a>
                <a href="products.html" class="block px-3 py-2 text-base font-medium text-dark hover:text-primary-900">Products</a>
                <a href="ingredients.html" class="block px-3 py-2 text-base font-medium text-primary-900 border-l-4 border-primary-900">Ingredients</a>
                <a href="certifications.html" class="block px-3 py-2 text-base font-medium text-dark hover:text-primary-900">Certifications</a>
                <a href="contact.html" class="block px-3 py-2 text-base font-medium text-dark hover:text-primary-900">Contact</a>
            </div>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="pt-40 pb-20 relative overflow-hidden">
        <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] opacity-20 z-0"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center" data-aos="fade-up">
            <span class="text-gold-500 tracking-[0.3em] uppercase text-sm mb-4 block font-semibold">Materia Medica</span>
            <h1 class="text-4xl md:text-7xl font-bold mb-6 font-serif leading-tight">Nature's <span class="text-gradient-gold">Masterpieces</span></h1>
            <p class="text-gray-400 max-w-2xl mx-auto text-base md:text-lg font-light leading-relaxed px-4">
                Discover the pure, potent botanical sources and ancient wisdom behind THE HANURAAM WELLNESS formulations. Each ingredient is a luxurious gift from the earth.
            </p>
            <div class="mt-10 w-px h-24 bg-gradient-to-b from-gold-500 to-transparent mx-auto"></div>
        </div>
    </section>

    <!-- Ingredients Sections -->
"""

html_body = ""

for i, ing in enumerate(ingredients):
    is_even = i % 2 == 0
    layout_class = "lg:flex-row" if is_even else "lg:flex-row-reverse"
    
    # Benefits checklist
    benefits_html = ""
    for ben in ing['benefits']:
        benefits_html += f'''
            <li class="flex items-start">
                <i class="fas fa-check-circle text-gold-500 mt-1 mr-3 flex-shrink-0"></i>
                <span class="text-sm text-gray-300 leading-relaxed">{ben}</span>
            </li>
        '''
        
    products_html = ""
    for p in ing["products"]:
        products_html += f'''
                <div class="glass-card rounded-2xl overflow-hidden group">
                    <div class="h-48 bg-white/50 flex items-center justify-center relative border-b border-primary-900/10">
                        <img src="{p.get('img', 'assets/prod_kordy_x.png')}" alt="{p['name']}" class="h-32 w-auto object-contain drop-shadow-xl group-hover:scale-110 transition-transform duration-500">
                    </div>
                    <div class="p-4 bg-white/40">
                        <h3 class="text-lg mb-1 text-primary-900 font-serif hover:text-gold-600 transition-colors">{p['name']}</h3>
                        <p class="text-dark/70 text-xs mb-3">Premium Formulation</p>
                        <div class="flex items-center justify-between mb-4">
                            <span class="text-lg font-bold text-gold-500">{p['price']}</span>
                        </div>
                        <div class="flex gap-2">
                            <button class="w-full flex items-center justify-center bg-gradient-gold text-primary-900 hover:shadow-lg rounded-lg py-2.5 font-semibold uppercase tracking-wider text-[10px] transition-all duration-300 shadow-md" onclick="addToCart('{p['name']}', parseInt('{p['price']}'.replace('₹','').replace(',','')))">Add to Cart</button>
                        </div>
                    </div>
                </div>
        '''

    html_body += f'''
    <section class="py-16 md:py-24 relative border-t border-white/5 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="flex flex-col {layout_class} gap-12 md:gap-16 items-center">
                
                <!-- Image Block -->
                <div class="w-full lg:w-1/2 relative group" data-aos="{"fade-right" if is_even else "fade-left"}">
                    <div class="absolute -inset-4 bg-gradient-gold opacity-0 group-hover:opacity-10 blur-xl rounded-full transition-opacity duration-700"></div>
                    <div class="relative rounded-2xl overflow-hidden shadow-2xl border border-white/10 aspect-[4/5] lg:aspect-square">
                        <img src="{ing['image']}" alt="{ing['name']}" class="absolute inset-0 w-full h-full object-cover group-hover:scale-105 transition-transform duration-1000">
                        <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-transparent to-transparent"></div>
                        <div class="absolute bottom-6 left-6 right-6 flex items-center justify-between">
                            <span class="glass px-4 py-2 rounded-full text-xs text-white uppercase tracking-widest border-white/20"><i class="fas fa-leaf mr-2 text-gold-400"></i>100% Pure Botanical</span>
                        </div>
                    </div>
                </div>
                
                <!-- Content Block -->
                <div class="w-full lg:w-1/2 relative mt-10 lg:mt-0" data-aos="{"fade-left" if is_even else "fade-right"}">
                    <div class="ingredient-number">{ing['num']}</div>
                    <div class="relative z-10 pt-8 lg:pt-0">
                        <h3 class="text-gold-500 tracking-[0.4em] text-xs font-semibold uppercase mb-3">{ing['scientific']}</h3>
                        <h2 class="text-3xl md:text-5xl font-serif text-white mb-8 tracking-wide leading-tight">{ing['name']}</h2>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
                            <div class="glass-card p-5 rounded-xl">
                                <i class="fas fa-seedling text-gold-500 text-xl mb-3"></i>
                                <h4 class="text-white text-sm font-semibold uppercase tracking-wider mb-2">Botanical Source</h4>
                                <p class="text-xs text-gray-400 leading-relaxed">{ing['source']}</p>
                            </div>
                            <div class="glass-card p-5 rounded-xl">
                                <i class="fas fa-flask text-gold-500 text-xl mb-3"></i>
                                <h4 class="text-white text-sm font-semibold uppercase tracking-wider mb-2">Key Compounds</h4>
                                <p class="text-xs text-gray-400 leading-relaxed">{ing['compounds']}</p>
                            </div>
                        </div>
                        
                        <div class="mb-8">
                            <h4 class="text-white font-serif text-xl border-b border-white/10 pb-2 mb-4">Ayurvedic Heritage & Use</h4>
                            <p class="text-gray-400 text-sm leading-relaxed mb-3"><strong class="text-gold-400 font-medium">Heritage:</strong> {ing['heritage']}</p>
                            <p class="text-gray-400 text-sm leading-relaxed"><strong class="text-gold-400 font-medium">Modern Use:</strong> {ing['uses']}</p>
                        </div>
                        
                        <div class="mb-10">
                            <h4 class="text-white font-serif text-xl border-b border-white/10 pb-2 mb-4">Health Benefits</h4>
                            <ul class="space-y-3">
                                {benefits_html}
                            </ul>
                        </div>
                        
                        <!-- Products Slider specific to this ingredient -->
                        <div>
                            <h4 class="text-xs uppercase tracking-widest text-gold-500 font-semibold mb-4">Found In Our Products</h4>
                            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-6">
                                {products_html}
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

html_footer = """
    <!-- Footer -->
    <footer class="bg-primary-900 pt-20 pb-10 border-t-8 border-gold-600">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
                <!-- Brand -->
                <div class="lg:col-span-2">
                    <a href="index.html" class="flex items-center"><img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-12 object-contain"></a>
                    <p class="text-white/80 font-serif italic mb-6 max-w-md text-lg">"Ancient Wisdom. Modern Formulation. Pure Wellness."</p>
                    <p class="text-white/60 text-sm max-w-md leading-relaxed">
                        A premium luxury Ayurvedic wellness brand dedicated to bringing you the purest, most potent herbal formulations inspired by ancient royal traditions and backed by modern science.
                    </p>
                </div>
                <!-- Links -->
                <div>
                    <h4 class="text-gold-400 font-sans text-xs font-semibold uppercase tracking-widest mb-6">Explore</h4>
                    <ul class="space-y-4">
                        <li><a href="about.html" class="text-white/70 hover:text-gold-400 transition-colors text-sm">Our Heritage</a></li>
                        <li><a href="products.html" class="text-white/70 hover:text-gold-400 transition-colors text-sm">Shop Collection</a></li>
                        <li><a href="ingredients.html" class="text-white/70 hover:text-gold-400 transition-colors text-sm">Ayurvedic Ingredients</a></li>
                        <li><a href="certifications.html" class="text-white/70 hover:text-gold-400 transition-colors text-sm">Certifications</a></li>
                        <li><a href="contact.html" class="text-white/70 hover:text-gold-400 transition-colors text-sm">Contact Us</a></li>
                    </ul>
                </div>
                <!-- Contact & Social -->
                <div>
                    <h4 class="text-gold-400 font-sans text-xs font-semibold uppercase tracking-widest mb-6">Connect</h4>
                    <ul class="space-y-4 text-white/70 text-sm mb-8">
                        <li class="flex items-start"><i class="fas fa-map-marker-alt mt-1 mr-3 text-gold-500"></i> New Delhi, India</li>
                        <li class="flex items-center"><i class="fas fa-envelope mr-3 text-gold-500"></i> wellness@hanuraam.com</li>
                        <li class="flex items-center"><i class="fas fa-phone mr-3 text-gold-500"></i> +91 98765 43210</li>
                    </ul>
                    <div class="flex space-x-4">
                        <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-gold-600 hover:border-gold-600 transition-all duration-300"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-gold-600 hover:border-gold-600 transition-all duration-300"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-gold-600 hover:border-gold-600 transition-all duration-300"><i class="fab fa-youtube"></i></a>
                    </div>
                </div>
            </div>
            
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center">
                <p class="text-white/40 text-xs mb-4 md:mb-0">&copy; 2026 THE HANURAAM WELLNESS. All rights reserved.</p>
                <div class="flex space-x-6 text-xs text-white/40">
                    <a href="#" class="hover:text-gold-400 transition-colors">Privacy Policy</a>
                    <a href="#" class="hover:text-gold-400 transition-colors">Terms of Service</a>
                    <a href="#" class="hover:text-gold-400 transition-colors">Shipping & Returns</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({ once: true, duration: 1000, offset: 100 });
        
        document.getElementById('mobile-menu-btn').addEventListener('click', function() {
            var menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden');
        });
        
        window.addEventListener('scroll', function() {
            var nav = document.querySelector('nav');
            if (window.scrollY > 10) {
                nav.classList.add('bg-white/95');
                nav.classList.remove('glass');
            } else {
                nav.classList.add('glass');
                nav.classList.remove('bg-white/95');
            }
        });

        let cartCount = 0;
        function addToCart(product, price) {
            cartCount++;
            document.querySelectorAll('a[href="cart.html"] span.absolute').forEach(el => {
                el.textContent = cartCount;
                el.classList.add('scale-125');
                setTimeout(() => el.classList.remove('scale-125'), 200);
            });
            // Show toast
            const toast = document.createElement('div');
            toast.className = 'fixed bottom-4 right-4 bg-gold-500 border border-gold-600 text-primary-900 font-semibold px-6 py-3 rounded-lg z-[100] shadow-xl transform translate-y-full opacity-0 transition-all duration-300';
            toast.innerHTML = `<i class="fas fa-check-circle text-primary-900 mr-2"></i> Added ${product} to cart`;
            document.body.appendChild(toast);
            
            setTimeout(() => {
                toast.classList.remove('translate-y-full', 'opacity-0');
            }, 100);
            
            setTimeout(() => {
                toast.classList.add('translate-y-full', 'opacity-0');
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }
    </script>
</body>
</html>
"""

full_html = html_head + html_body + html_footer

with open('e:/ecc/ingredients.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Fixed syntax bug and updated premium ingredients page successfully!")

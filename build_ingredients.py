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
                        primary: { 900: '#0f291f', 800: '#1F4D3B', 700: '#2E5E4E' },
                        gold: { 400: '#F5E6A3', 500: '#E3C16F', 600: '#C9A84C' },
                        dark: '#0A0A0A'
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        serif: ['Playfair Display', 'serif'],
                    }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style type="text/tailwindcss">
        @layer utilities {
            .glass { @apply bg-white/5 backdrop-blur-xl border border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.5)]; }
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
</head>
<body class="antialiased selection:bg-gold-500 selection:text-primary-900 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-primary-800 via-primary-900 to-[#050f0b]">

    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 glass border-b border-white/10 transition-all duration-300 bg-primary-900/80">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex-shrink-0 flex items-center">
                    <a href="index.html" class="flex items-center">
                        <img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-12 object-contain">
                    </a>
                </div>
                <div class="hidden md:flex space-x-8 items-center">
                    <a href="index.html" class="text-gray-300 hover:text-gold-400 transition-colors uppercase text-sm tracking-wider font-medium">Home</a>
                    <a href="about.html" class="text-gray-300 hover:text-gold-400 transition-colors uppercase text-sm tracking-wider font-medium">About</a>
                    <a href="products.html" class="text-gray-300 hover:text-gold-400 transition-colors uppercase text-sm tracking-wider font-medium">Products</a>
                    <a href="ingredients.html" class="text-gold-400 border-b-2 border-gold-400 pb-1 uppercase text-sm tracking-wider font-medium">Ingredients</a>
                    <a href="contact.html" class="text-gray-300 hover:text-gold-400 transition-colors uppercase text-sm tracking-wider font-medium">Contact</a>
                    <a href="cart.html" class="text-white hover:text-gold-400 transition-colors relative">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span class="absolute -top-2 -right-2 bg-gold-500 text-primary-900 text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center">1</span>
                    </a>
                </div>
                <div class="md:hidden flex items-center space-x-4">
                    <a href="cart.html" class="text-white relative">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span class="absolute -top-2 -right-2 bg-gold-500 text-primary-900 text-[10px] font-bold rounded-full h-4 w-4 flex items-center justify-center">1</span>
                    </a>
                    <button id="mobile-menu-btn" class="text-white hover:text-gold-400 focus:outline-none">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden glass border-t border-white/10 bg-primary-900/95">
            <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                <a href="index.html" class="block px-3 py-2 text-base font-medium text-gray-300 hover:text-gold-400">Home</a>
                <a href="about.html" class="block px-3 py-2 text-base font-medium text-gray-300 hover:text-gold-400">About</a>
                <a href="products.html" class="block px-3 py-2 text-base font-medium text-gray-300 hover:text-gold-400">Products</a>
                <a href="ingredients.html" class="block px-3 py-2 text-base font-medium text-gold-400 border-l-4 border-gold-400 bg-white/5">Ingredients</a>
                <a href="contact.html" class="block px-3 py-2 text-base font-medium text-gray-300 hover:text-gold-400">Contact</a>
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
        
    # Products slider
    products_html = ""
    for prod in ing['products']:
        products_html += f'''
            <div class="w-64 flex-shrink-0 glass-card rounded-xl p-4 flex flex-col group">
                <div class="w-full h-48 bg-black/50 rounded-lg overflow-hidden mb-4 relative">
                    <img src="{prod['img']}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute inset-0 bg-black/20 group-hover:bg-transparent transition-colors"></div>
                </div>
                <h4 class="text-white font-serif text-lg tracking-wide">{prod['name']}</h4>
                <div class="flex justify-between items-center mt-auto pt-2">
                    <span class="text-gold-400 font-semibold">{prod['price']}</span>
                    <button class="bg-transparent border border-gold-500 text-gold-400 hover:bg-gold-500 hover:text-dark py-1.5 px-3 rounded-lg text-xs uppercase tracking-widest font-semibold transition-colors duration-300 ml-2 whitespace-nowrap" onclick="addToCart('{prod['name']}', parseInt('{prod['price']}'.replace('₹','').replace(',','')))"><i class="fas fa-shopping-bag mr-1"></i> Add to Cart</button>
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
                            <div class="flex overflow-x-auto gap-4 pb-4 hide-scrollbar snap-x snap-mandatory">
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
    <footer class="bg-[#050f0b] pt-16 pb-8 border-t border-white/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
                <div class="col-span-1 md:col-span-2">
                    <a href="index.html" class="mb-4 inline-block">
                        <img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-16 object-contain">
                    </a>
                    <p class="text-gray-400 mb-6 font-serif italic">"Ancient Wisdom. Modern Formulation. Pure Wellness."</p>
                </div>
                <div>
                    <h4 class="text-gold-500 font-sans text-xs font-semibold uppercase tracking-widest mb-6">Explore</h4>
                    <ul class="space-y-3">
                        <li><a href="about.html" class="text-gray-400 hover:text-gold-400 transition-colors text-sm">Our Story</a></li>
                        <li><a href="products.html" class="text-gray-400 hover:text-gold-400 transition-colors text-sm">Shop</a></li>
                        <li><a href="ingredients.html" class="text-gray-400 hover:text-gold-400 transition-colors text-sm">Ingredients</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-gold-500 font-sans text-xs font-semibold uppercase tracking-widest mb-6">Connect</h4>
                    <div class="flex space-x-4">
                        <a href="#" class="w-10 h-10 rounded-full glass flex items-center justify-center text-white hover:text-gold-400 transition-all"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full glass flex items-center justify-center text-white hover:text-gold-400 transition-all"><i class="fab fa-facebook-f"></i></a>
                    </div>
                </div>
            </div>
            <div class="border-t border-white/10 pt-8 text-center text-gray-500 text-sm">
                <p>&copy; 2026 THE HANURAAM WELLNESS. All rights reserved.</p>
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
                nav.classList.add('bg-primary-900/95', 'shadow-lg');
                nav.classList.remove('bg-primary-900/80');
            } else {
                nav.classList.add('bg-primary-900/80');
                nav.classList.remove('bg-primary-900/95', 'shadow-lg');
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

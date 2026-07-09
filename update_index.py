import os

new_body_content = """    <!-- Hero Banner -->
    <style>
        @keyframes kenburns {
            0% { transform: scale(1) translate(0, 0); }
            100% { transform: scale(1.15) translate(-1%, -1%); }
        }
    </style>
    <section class="relative w-full h-[85vh] min-h-[600px] mt-[104px] overflow-hidden bg-black flex items-center justify-center text-center">
        <!-- Background Image with CSS Video Animation (Ken Burns) -->
        <div class="absolute inset-0 bg-[url('assets/hero_bg.png')] bg-cover bg-center opacity-60" style="animation: kenburns 20s ease-in-out infinite alternate"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-black/20 via-black/40 to-black/70"></div>
        
        <div class="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 w-full flex flex-col items-center justify-center space-y-6">
            <h1 class="text-5xl md:text-6xl lg:text-7xl font-serif font-bold text-white leading-tight drop-shadow-2xl">
                Transform Your <br> Health with the Power <br> <span class="italic font-light">of Ayurveda</span>
            </h1>
            
            <p class="text-lg md:text-xl text-white/90 font-light tracking-wide max-w-2xl drop-shadow-md">
                Made with ancient Ayurvedic wisdom and 100% organic ingredients
            </p>

            <div class="pt-8">
                <a href="products.html" class="inline-flex items-center justify-center px-8 py-4 bg-[#4CAF50] text-white font-bold tracking-wide rounded-full text-lg hover:bg-[#45a049] transition-all duration-300 shadow-2xl hover:-translate-y-1">
                    Start Your Wellness Journey
                </a>
            </div>
        </div>
    </section>

    <!-- Premium Categories -->
    <section class="py-24 bg-white relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <span class="text-primary-900 tracking-[0.3em] uppercase text-xs font-semibold mb-2 block">Curated Wellness</span>
                <h2 class="text-4xl md:text-5xl font-serif text-primary-900">Premium Categories</h2>
                <div class="w-24 h-px bg-gold-500 mx-auto mt-6"></div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- Category 1 -->
                <div class="group cursor-pointer relative h-80 rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500">
                    <img src="assets/cat_vitality.png" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Vitality">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-0 left-0 p-8 w-full">
                        <h3 class="text-white font-serif text-2xl mb-2">Vitality & Power</h3>
                        <p class="text-gold-400 text-xs uppercase tracking-widest">Explore Range <i class="fas fa-arrow-right ml-1 opacity-0 group-hover:opacity-100 transition-opacity"></i></p>
                    </div>
                </div>
                <!-- Category 2 -->
                <div class="group cursor-pointer relative h-80 rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500">
                    <img src="assets/cat_immunity.png" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Immunity">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-0 left-0 p-8 w-full">
                        <h3 class="text-white font-serif text-2xl mb-2">Immunity</h3>
                        <p class="text-gold-400 text-xs uppercase tracking-widest">Explore Range <i class="fas fa-arrow-right ml-1 opacity-0 group-hover:opacity-100 transition-opacity"></i></p>
                    </div>
                </div>
                <!-- Category 3 -->
                <div class="group cursor-pointer relative h-80 rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500">
                    <img src="assets/cat_joint.png" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Joint Care">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-0 left-0 p-8 w-full">
                        <h3 class="text-white font-serif text-2xl mb-2">Joint & Muscle</h3>
                        <p class="text-gold-400 text-xs uppercase tracking-widest">Explore Range <i class="fas fa-arrow-right ml-1 opacity-0 group-hover:opacity-100 transition-opacity"></i></p>
                    </div>
                </div>
                <!-- Category 4 -->
                <div class="group cursor-pointer relative h-80 rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-500">
                    <img src="assets/cat_mind.png" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Mind & Balance">
                    <div class="absolute inset-0 bg-gradient-to-t from-primary-900/90 via-primary-900/40 to-transparent"></div>
                    <div class="absolute bottom-0 left-0 p-8 w-full">
                        <h3 class="text-white font-serif text-2xl mb-2">Mind & Balance</h3>
                        <p class="text-gold-400 text-xs uppercase tracking-widest">Explore Range <i class="fas fa-arrow-right ml-1 opacity-0 group-hover:opacity-100 transition-opacity"></i></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Featured Products -->
    <section class="py-24 bg-earth-100 border-t border-primary-900/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-end mb-12">
                <div>
                    <span class="text-gold-600 tracking-[0.2em] uppercase text-xs font-semibold mb-2 block">Our Masterpieces</span>
                    <h2 class="text-4xl font-serif text-primary-900">Featured Products</h2>
                </div>
                <a href="products.html" class="hidden md:inline-flex items-center text-primary-900 hover:text-gold-600 uppercase text-xs tracking-widest font-semibold transition-colors">
                    View All <i class="fas fa-arrow-right ml-2"></i>
                </a>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
                <!-- Product 1 -->
                <div class="glass-card rounded-3xl p-6 relative group bg-white border border-primary-900/10">
                    <div class="absolute top-4 left-4 bg-gold-600 text-white text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-widest z-10">Bestseller</div>
                    <div class="absolute top-4 right-4 text-primary-900/30 hover:text-gold-600 cursor-pointer z-10 transition-colors"><i class="fas fa-heart text-xl"></i></div>
                    
                    <div class="h-64 flex items-center justify-center mb-6 relative overflow-hidden rounded-2xl bg-earth-50 group-hover:bg-earth-100 transition-colors">
                        <div class="w-24 h-40 bg-gradient-to-br from-primary-900 to-primary-800 rounded-xl border border-gold-500/30 shadow-lg flex flex-col items-center justify-center transition-transform duration-500 group-hover:scale-110">
                            <i class="fas fa-leaf text-gold-400 text-3xl mb-2"></i>
                            <span class="text-[10px] text-white tracking-widest uppercase">KORDY X</span>
                        </div>
                    </div>
                    
                    <div class="text-center">
                        <div class="flex justify-center text-gold-500 text-xs mb-2 space-x-1">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                            <span class="text-dark/50 ml-2">(128)</span>
                        </div>
                        <h3 class="text-xl font-serif text-primary-900 mb-1">KORDY X</h3>
                        <p class="text-xs text-dark/60 mb-4">Premium Effervescent Formulation</p>
                        <div class="flex items-center justify-center space-x-3 mb-6">
                            <span class="text-lg font-semibold text-primary-900">₹1,499</span>
                            <span class="text-sm text-dark/40 line-through">₹1,999</span>
                        </div>
                        <button class="w-full py-3 bg-white border border-primary-900 text-primary-900 hover:bg-primary-900 hover:text-gold-400 rounded-full text-xs uppercase tracking-widest font-semibold transition-all duration-300">
                            Add to Cart
                        </button>
                    </div>
                </div>

                <!-- Product 2 -->
                <div class="glass-card rounded-3xl p-6 relative group bg-white border border-primary-900/10">
                    <div class="absolute top-4 right-4 text-primary-900/30 hover:text-gold-600 cursor-pointer z-10 transition-colors"><i class="fas fa-heart text-xl"></i></div>
                    
                    <div class="h-64 flex items-center justify-center mb-6 relative overflow-hidden rounded-2xl bg-earth-50 group-hover:bg-earth-100 transition-colors">
                        <div class="w-24 h-32 bg-gradient-to-br from-brown-800 to-black rounded-xl border border-gold-500/30 shadow-lg flex flex-col items-center justify-center transition-transform duration-500 group-hover:scale-110">
                            <i class="fas fa-pills text-gold-400 text-3xl mb-2"></i>
                            <span class="text-[8px] text-white tracking-widest uppercase text-center">Ashwagandha<br>Plus</span>
                        </div>
                    </div>
                    
                    <div class="text-center">
                        <div class="flex justify-center text-gold-500 text-xs mb-2 space-x-1">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star-half-alt"></i>
                            <span class="text-dark/50 ml-2">(84)</span>
                        </div>
                        <h3 class="text-xl font-serif text-primary-900 mb-1">Ashwagandha Plus</h3>
                        <p class="text-xs text-dark/60 mb-4">Stress Relief & Energy</p>
                        <div class="flex items-center justify-center space-x-3 mb-6">
                            <span class="text-lg font-semibold text-primary-900">₹899</span>
                        </div>
                        <button class="w-full py-3 bg-white border border-primary-900 text-primary-900 hover:bg-primary-900 hover:text-gold-400 rounded-full text-xs uppercase tracking-widest font-semibold transition-all duration-300">
                            Add to Cart
                        </button>
                    </div>
                </div>

                <!-- Product 3 -->
                <div class="glass-card rounded-3xl p-6 relative group bg-white border border-primary-900/10">
                    <div class="absolute top-4 left-4 bg-primary-900 text-gold-400 text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-widest z-10">New</div>
                    <div class="absolute top-4 right-4 text-primary-900/30 hover:text-gold-600 cursor-pointer z-10 transition-colors"><i class="fas fa-heart text-xl"></i></div>
                    
                    <div class="h-64 flex items-center justify-center mb-6 relative overflow-hidden rounded-2xl bg-earth-50 group-hover:bg-earth-100 transition-colors">
                        <div class="w-20 h-28 bg-gradient-to-br from-yellow-900 to-black rounded-full border border-gold-500/30 shadow-lg flex flex-col items-center justify-center transition-transform duration-500 group-hover:scale-110">
                            <i class="fas fa-gem text-gold-400 text-2xl mb-1"></i>
                            <span class="text-[8px] text-white tracking-widest uppercase text-center">Shilajit<br>Gold</span>
                        </div>
                    </div>
                    
                    <div class="text-center">
                        <div class="flex justify-center text-gold-500 text-xs mb-2 space-x-1">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                            <span class="text-dark/50 ml-2">(42)</span>
                        </div>
                        <h3 class="text-xl font-serif text-primary-900 mb-1">Shilajit Gold Resin</h3>
                        <p class="text-xs text-dark/60 mb-4">Pure Himalayan Extract</p>
                        <div class="flex items-center justify-center space-x-3 mb-6">
                            <span class="text-lg font-semibold text-primary-900">₹2,199</span>
                            <span class="text-sm text-dark/40 line-through">₹2,599</span>
                        </div>
                        <button class="w-full py-3 bg-white border border-primary-900 text-primary-900 hover:bg-primary-900 hover:text-gold-400 rounded-full text-xs uppercase tracking-widest font-semibold transition-all duration-300">
                            Add to Cart
                        </button>
                    </div>
                </div>
            </div>
            
            <div class="mt-8 text-center md:hidden">
                <a href="products.html" class="inline-flex items-center text-primary-900 hover:text-gold-600 uppercase text-xs tracking-widest font-semibold transition-colors border-b border-primary-900 pb-1">
                    View All Products <i class="fas fa-arrow-right ml-2"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Why Choose Hanuraam & Heritage -->
    <section class="py-24 relative overflow-hidden bg-primary-900">
        <div class="absolute inset-0 opacity-10 bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] z-0"></div>
        <div class="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-primary-800 to-transparent"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <!-- Image Collage -->
                <div class="relative h-[600px] hidden md:block">
                    <img src="assets/heritage_1.png" class="absolute top-0 left-0 w-2/3 h-2/3 object-cover rounded-t-full border-4 border-gold-600/30 shadow-2xl z-10" alt="Ayurvedic Herbs">
                    <img src="assets/heritage_2.png" class="absolute bottom-0 right-0 w-2/3 h-2/3 object-cover rounded-b-full border-4 border-gold-600/30 shadow-2xl z-20" alt="Ayurvedic Mortar">
                    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-32 h-32 bg-primary-900 border border-gold-500 rounded-full flex items-center justify-center z-30 shadow-2xl">
                        <i class="fas fa-vihara text-5xl text-gold-400"></i>
                    </div>
                </div>

                <!-- Content -->
                <div class="space-y-10 text-white">
                    <div>
                        <span class="text-gold-400 tracking-[0.3em] uppercase text-xs font-semibold mb-4 block">Our Heritage</span>
                        <h2 class="text-5xl font-serif text-white leading-tight mb-6">Where Ancient Wisdom <br><span class="text-gold-400 text-4xl italic">meets</span> Modern Science</h2>
                        <p class="text-white/70 font-light leading-relaxed">
                            Long before modern pharmaceuticals existed, royal families relied on Ayurvedic wisdom to maintain strength and longevity. At THE HANURAAM WELLNESS, we revive this timeless wisdom and combine it with modern nutraceutical research.
                        </p>
                    </div>

                    <div class="space-y-6">
                        <div class="flex items-start">
                            <div class="w-12 h-12 rounded-full border border-gold-500/50 flex items-center justify-center flex-shrink-0 bg-primary-800 text-gold-400">
                                <i class="fas fa-leaf"></i>
                            </div>
                            <div class="ml-5">
                                <h4 class="text-lg font-serif text-white mb-1">100% Pure & Natural</h4>
                                <p class="text-white/60 text-sm font-light">Sourced directly from the purest environments, free from synthetic additives.</p>
                            </div>
                        </div>
                        <div class="flex items-start">
                            <div class="w-12 h-12 rounded-full border border-gold-500/50 flex items-center justify-center flex-shrink-0 bg-primary-800 text-gold-400">
                                <i class="fas fa-microscope"></i>
                            </div>
                            <div class="ml-5">
                                <h4 class="text-lg font-serif text-white mb-1">Clinically Formulated</h4>
                                <p class="text-white/60 text-sm font-light">Standardized extracts combined using modern science for maximum efficacy.</p>
                            </div>
                        </div>
                        <div class="flex items-start">
                            <div class="w-12 h-12 rounded-full border border-gold-500/50 flex items-center justify-center flex-shrink-0 bg-primary-800 text-gold-400">
                                <i class="fas fa-award"></i>
                            </div>
                            <div class="ml-5">
                                <h4 class="text-lg font-serif text-white mb-1">Premium Quality</h4>
                                <p class="text-white/60 text-sm font-light">Manufactured in GMP-certified facilities adhering to global luxury standards.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Market Statistics -->
    <section class="py-16 bg-white border-b border-primary-900/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h3 class="text-center text-primary-900 tracking-[0.2em] text-xs font-bold uppercase mb-10">Why The World Needs Ayurveda Today</h3>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center divide-x divide-primary-900/10">
                <div class="px-4">
                    <h4 class="text-4xl md:text-5xl font-serif text-gold-600 mb-2">320M+</h4>
                    <p class="text-xs text-dark/60 uppercase tracking-widest">Global Vitality Issues</p>
                </div>
                <div class="px-4">
                    <h4 class="text-4xl md:text-5xl font-serif text-gold-600 mb-2">40%</h4>
                    <p class="text-xs text-dark/60 uppercase tracking-widest">Men Face Early Decline</p>
                </div>
                <div class="px-4">
                    <h4 class="text-4xl md:text-5xl font-serif text-gold-600 mb-2">$1.71B</h4>
                    <p class="text-xs text-dark/60 uppercase tracking-widest">Joint Issues Globally</p>
                </div>
                <div class="px-4">
                    <h4 class="text-4xl md:text-5xl font-serif text-gold-600 mb-2">1 in 3</h4>
                    <p class="text-xs text-dark/60 uppercase tracking-widest">Suffer from Stress</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Ingredient Highlights -->
    <section class="py-24 bg-earth-50 relative overflow-hidden">
        <i class="fas fa-leaf absolute -right-20 top-20 text-[200px] text-primary-900/[0.03] rotate-45"></i>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center mb-16">
                <span class="text-gold-600 tracking-[0.2em] uppercase text-xs font-semibold mb-2 block">Nature's Pharmacy</span>
                <h2 class="text-4xl font-serif text-primary-900">Key Botanicals</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                <!-- Botanical 1 -->
                <div class="relative h-64 rounded-2xl overflow-hidden group cursor-pointer shadow-lg">
                    <img src="assets/botanical_ashwagandha.png" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Ashwagandha">
                    <div class="absolute inset-0 bg-primary-900/40 group-hover:bg-primary-900/60 transition-colors"></div>
                    <div class="absolute inset-0 p-6 flex flex-col justify-end text-white">
                        <h3 class="text-xl font-serif mb-1">Ashwagandha</h3>
                        <p class="text-xs opacity-80 mb-3">Withania somnifera</p>
                        <a href="ingredients.html" class="text-[10px] uppercase tracking-widest border-b border-gold-400 w-max pb-1 text-gold-400 opacity-0 group-hover:opacity-100 transition-opacity">Learn More</a>
                    </div>
                </div>
                <!-- Botanical 2 -->
                <div class="relative h-64 rounded-2xl overflow-hidden group cursor-pointer shadow-lg md:mt-8">
                    <img src="assets/botanical_shilajit.png" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Shilajit">
                    <div class="absolute inset-0 bg-primary-900/40 group-hover:bg-primary-900/60 transition-colors"></div>
                    <div class="absolute inset-0 p-6 flex flex-col justify-end text-white">
                        <h3 class="text-xl font-serif mb-1">Shilajit</h3>
                        <p class="text-xs opacity-80 mb-3">Asphaltum punjabianum</p>
                        <a href="ingredients.html" class="text-[10px] uppercase tracking-widest border-b border-gold-400 w-max pb-1 text-gold-400 opacity-0 group-hover:opacity-100 transition-opacity">Learn More</a>
                    </div>
                </div>
                <!-- Botanical 3 -->
                <div class="relative h-64 rounded-2xl overflow-hidden group cursor-pointer shadow-lg">
                    <img src="assets/cat_joint.png" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Panax Ginseng">
                    <div class="absolute inset-0 bg-primary-900/40 group-hover:bg-primary-900/60 transition-colors"></div>
                    <div class="absolute inset-0 p-6 flex flex-col justify-end text-white">
                        <h3 class="text-xl font-serif mb-1">Panax Ginseng</h3>
                        <p class="text-xs opacity-80 mb-3">Panax ginseng</p>
                        <a href="ingredients.html" class="text-[10px] uppercase tracking-widest border-b border-gold-400 w-max pb-1 text-gold-400 opacity-0 group-hover:opacity-100 transition-opacity">Learn More</a>
                    </div>
                </div>
                <!-- Botanical 4 -->
                <div class="relative h-64 rounded-2xl overflow-hidden group cursor-pointer shadow-lg md:mt-8">
                    <img src="assets/botanical_gokshura.png" class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Gokshura">
                    <div class="absolute inset-0 bg-primary-900/40 group-hover:bg-primary-900/60 transition-colors"></div>
                    <div class="absolute inset-0 p-6 flex flex-col justify-end text-white">
                        <h3 class="text-xl font-serif mb-1">Gokshura</h3>
                        <p class="text-xs opacity-80 mb-3">Tribulus terrestris</p>
                        <a href="ingredients.html" class="text-[10px] uppercase tracking-widest border-b border-gold-400 w-max pb-1 text-gold-400 opacity-0 group-hover:opacity-100 transition-opacity">Learn More</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Newsletter -->
    <section class="py-20 bg-earth-200">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <h2 class="text-3xl font-serif text-primary-900 mb-4">Join The Hanuraam Family</h2>
            <p class="text-dark/70 text-sm mb-8">Subscribe to receive wellness tips, exclusive offers, and early access to new Ayurvedic formulations.</p>
            <form class="flex flex-col sm:flex-row max-w-xl mx-auto gap-4">
                <input type="email" placeholder="Your email address" class="flex-1 px-6 py-4 bg-white border border-primary-900/20 focus:outline-none focus:border-gold-500 rounded-sm">
                <button type="submit" class="px-8 py-4 bg-primary-900 text-gold-400 uppercase tracking-widest text-xs font-bold hover:bg-primary-800 transition-colors rounded-sm">Subscribe</button>
            </form>
        </div>
    </section>

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

    <script>
        document.getElementById('mobile-menu-btn').addEventListener('click', function() {
            var menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden');
        });
        
        // Sticky nav background effect
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
    </script>
</body>
</html>"""

with open("e:/ecc/index.html", "r", encoding="utf-8") as f:
    original = f.read()

# We need to replace everything from <!-- Hero Banner --> to the end of the file.
# Note: The original file has `<!-- Hero Banner -->` right after `</nav>`
import re
new_html = re.sub(r'<!-- Hero Banner -->.*', new_body_content, original, flags=re.DOTALL)

with open("e:/ecc/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Updated index.html")



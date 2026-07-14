import re

with open('build_index.py', 'r', encoding='utf-8') as f:
    content = f.read()

hero_start = '    <!-- 1. Fullscreen Hero -->\n    <header class="relative min-h-screen md:h-screen md:min-h-[700px] flex flex-col justify-center overflow-hidden bg-earth-50 pt-32 pb-16 md:pt-0 md:pb-0">'
hero_end = '        <div class="absolute bottom-8 left-1/2 -translate-x-1/2 z-20 flex flex-col items-center cursor-pointer" onclick="window.scrollTo({top: window.innerHeight, behavior: \'smooth\'})">\n            <span class="text-primary-900/50 text-[10px] uppercase tracking-widest mb-2 font-bold">Scroll</span>\n            <div class="w-px h-12 bg-primary-900/20 relative overflow-hidden">\n                <div class="w-full h-1/2 bg-primary-900 animate-scroll"></div>\n            </div>\n        </div>\n    </header>'

replacement = """    <!-- 1. Fullscreen Hero Slider -->
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
                const totalSlides = 2;
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
    </header>"""

start_idx = content.find(hero_start)
end_idx = content.find(hero_end) + len(hero_end)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + replacement + content[end_idx:]
    with open('build_index.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced successfully")
else:
    print(f"Could not find start or end index. Start: {start_idx}, End: {end_idx}")

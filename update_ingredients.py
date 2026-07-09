ingredients_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ingredients | THE HANURAAM WELLNESS</title>
    <meta name="description" content="Discover the pure, potent Ayurvedic ingredients we use in our formulations.">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: { 900: '#1F4D3B', 800: '#2E5E4E', 700: '#355E3B' },
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
        }
        body { @apply bg-earth-100 text-dark font-sans overflow-x-hidden; }
        h1, h2, h3, h4, h5, h6 { @apply font-serif text-primary-900; }
        @keyframes marquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .animate-marquee {
            animation: marquee 25s linear infinite;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="antialiased">

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
                    <a href="index.html" class="font-serif text-2xl font-bold tracking-wider text-primary-900">THE HANURAAM</a>
                </div>
                <div class="hidden md:flex space-x-8 items-center">
                    <a href="index.html" class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium">Home</a>
                    <a href="about.html" class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium">About</a>
                    <a href="products.html" class="text-dark hover:text-gold-600 transition-colors uppercase text-sm tracking-wider font-medium">Products</a>
                    <a href="ingredients.html" class="text-primary-900 hover:text-gold-600 transition-colors relative border-b-2 border-primary-900 pb-1 uppercase text-sm tracking-wider font-medium">Ingredients</a>
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
                <a href="contact.html" class="block px-3 py-2 text-base font-medium text-dark hover:text-primary-900">Contact</a>
            </div>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="pt-32 pb-16 relative bg-earth-200 border-b border-primary-900/10 overflow-hidden">
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-earth-50 via-earth-100 to-earth-200 z-0"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4 font-serif text-primary-900">Materia <span class="text-gold-600">Medica</span></h1>
            <p class="text-dark/70 max-w-2xl mx-auto text-lg font-light">
                Explore the powerful botanical sources and ancient wisdom behind our signature ingredients.
            </p>
        </div>
    </section>

    <!-- Ingredients Infographics -->
    <section class="py-20 relative bg-earth-50">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
            
            <div class="shadow-2xl rounded-2xl overflow-hidden border border-gold-600/20 transform hover:-translate-y-2 transition-all duration-500">
                <img src="assets/info_ashwa.jpg" alt="Ashwagandha Infographic" class="w-full h-auto object-contain bg-black">
            </div>

            <div class="shadow-2xl rounded-2xl overflow-hidden border border-gold-600/20 transform hover:-translate-y-2 transition-all duration-500">
                <img src="assets/info_shilajit.jpg" alt="Shilajit Infographic" class="w-full h-auto object-contain bg-black">
            </div>

            <div class="shadow-2xl rounded-2xl overflow-hidden border border-gold-600/20 transform hover:-translate-y-2 transition-all duration-500">
                <img src="assets/info_ginseng.jpg" alt="Panax Ginseng Infographic" class="w-full h-auto object-contain bg-black">
            </div>

            <div class="shadow-2xl rounded-2xl overflow-hidden border border-gold-600/20 transform hover:-translate-y-2 transition-all duration-500">
                <img src="assets/info_gokshura.png" alt="Gokshura Infographic" class="w-full h-auto object-contain bg-black">
            </div>

            <div class="shadow-2xl rounded-2xl overflow-hidden border border-gold-600/20 transform hover:-translate-y-2 transition-all duration-500">
                <img src="assets/info_damiyana.jpg" alt="Damiyana Infographic" class="w-full h-auto object-contain bg-black">
            </div>

        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-primary-900 pt-10 pb-6 border-t-8 border-gold-600 mt-auto">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center text-white/40 text-xs">
                <p>&copy; 2026 THE HANURAAM WELLNESS. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
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
    </script>
</body>
</html>
"""
with open('e:/ecc/ingredients.html', 'w', encoding='utf-8') as f:
    f.write(ingredients_html)

print("Ingredients page updated successfully!")

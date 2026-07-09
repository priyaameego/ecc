import re

# --- INDEX.HTML ---
with open('e:/ecc/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Make Add to Cart clickable
c = c.replace(
    '<button class="w-full py-3 bg-white border border-primary-900 text-primary-900 hover:bg-primary-900 hover:text-gold-400 rounded-full text-xs uppercase tracking-widest font-semibold transition-all duration-300">\n                            Add to Cart\n                        </button>',
    '<button onclick="addToCart(this)" class="w-full py-3 bg-white border border-primary-900 text-primary-900 hover:bg-primary-900 hover:text-gold-400 rounded-full text-xs uppercase tracking-widest font-semibold transition-all duration-300">\n                            Add to Cart\n                        </button>'
)

# 2. Make Like buttons clickable
c = c.replace(
    '<div class="absolute top-4 right-4 text-primary-900/30 hover:text-gold-600 cursor-pointer z-10 transition-colors"><i class="fas fa-heart text-xl"></i></div>',
    '<div class="absolute top-4 right-4 text-primary-900/30 hover:text-gold-600 cursor-pointer z-10 transition-colors" onclick="toggleLike(this)"><i class="fas fa-heart text-xl transition-transform duration-200"></i></div>'
)

# 3. Add JS for cart and likes
js = '''
    <script>
        let cartCount = 0;
        function addToCart(btn) {
            cartCount++;
            document.querySelectorAll('.fa-shopping-bag + span').forEach(el => {
                el.innerText = cartCount;
                el.classList.add('scale-125');
                setTimeout(() => el.classList.remove('scale-125'), 300);
            });
            let originalText = btn.innerText;
            btn.innerText = 'ADDED TO CART';
            btn.classList.remove('bg-white', 'text-primary-900');
            btn.classList.add('bg-primary-900', 'text-gold-400');
            setTimeout(() => {
                btn.innerText = originalText;
                btn.classList.add('bg-white', 'text-primary-900');
                btn.classList.remove('bg-primary-900', 'text-gold-400');
            }, 2000);
        }
        function toggleLike(btn) {
            btn.classList.toggle('text-red-500');
            btn.classList.toggle('text-primary-900/30');
            let icon = btn.querySelector('i');
            if(icon) {
                icon.classList.add('scale-125');
                setTimeout(() => icon.classList.remove('scale-125'), 200);
            }
        }
    </script>
</body>'''
if 'function addToCart' not in c:
    c = c.replace('</body>', js)

with open('e:/ecc/index.html', 'w', encoding='utf-8') as f:
    f.write(c)


# --- ABOUT.HTML ---
with open('e:/ecc/about.html', 'r', encoding='utf-8') as f:
    ab = f.read()

ab = ab.replace('bg-navy-800', 'bg-black')
ab = ab.replace('from-navy-900', 'from-[#111]')
ab = ab.replace('via-navy-800', 'via-black')
ab = ab.replace('to-navy-700', 'to-black')
ab = ab.replace('bg-navy-900', 'bg-black')
ab = ab.replace('bg-navy-900/90', 'bg-black/90')

# Improve responsiveness and aesthetics of the left side block
old_left_block = '''                <!-- Left Side: Sanskrit & Abstract Imagery -->
                <div class="relative h-full flex flex-col justify-center min-h-[400px]">
                    <div class="absolute -left-20 top-1/2 -translate-y-1/2 w-96 h-96 bg-gold-500/20 blur-[120px] rounded-full pointer-events-none"></div>
                    
                    <div class="glass border border-gold-500/30 p-10 rounded-2xl relative z-10 bg-black/40 shadow-[0_0_50px_rgba(201,168,76,0.15)]">'''

new_left_block = '''                <!-- Left Side: Sanskrit & Abstract Imagery -->
                <div class="relative h-full flex flex-col justify-center min-h-[400px] order-2 md:order-1 mt-10 md:mt-0 rounded-2xl overflow-hidden">
                    <img src="assets/heritage_1.png" class="absolute inset-0 w-full h-full object-cover opacity-30">
                    <div class="absolute inset-0 bg-gradient-to-r from-black via-black/80 to-transparent"></div>
                    <div class="absolute -left-20 top-1/2 -translate-y-1/2 w-96 h-96 bg-gold-500/10 blur-[120px] rounded-full pointer-events-none"></div>
                    
                    <div class="glass border border-gold-500/30 p-6 md:p-10 rounded-2xl relative z-10 bg-black/60 shadow-[0_0_50px_rgba(201,168,76,0.15)] mx-4 md:mx-0">'''

ab = ab.replace(old_left_block, new_left_block)

# Order right side content correctly for mobile
ab = ab.replace('<!-- Right Side: Content -->\n                <div class="relative py-12 md:pl-10">', '<!-- Right Side: Content -->\n                <div class="relative py-12 md:pl-10 order-1 md:order-2">')

with open('e:/ecc/about.html', 'w', encoding='utf-8') as f:
    f.write(ab)

print("Updates complete")

import os
import re

def get_base_html():
    with open('about.html', 'r', encoding='utf-8') as f:
        return f.read()

about_html = get_base_html()

# Extract head and nav
head_match = re.search(r'(<!DOCTYPE html>.*?<nav.*?</nav>)', about_html, re.DOTALL)
if not head_match:
    print("Could not find head/nav")
    exit(1)
    
head_nav = head_match.group(1)

# Extract mobile menu
mobile_menu_match = re.search(r'(<div id="mobile-menu".*?</div>\s*</div>)', about_html, re.DOTALL)
mobile_menu = mobile_menu_match.group(1) if mobile_menu_match else ""

# Extract footer and scripts
footer_match = re.search(r'(<footer.*)', about_html, re.DOTALL)
footer_scripts = footer_match.group(1) if footer_match else ""

# Update Active states in Navigation
# Remove active state from About
head_nav = head_nav.replace('border-b-2 border-primary-900 pb-1', '')
head_nav = head_nav.replace('class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium"', 'class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium"')

# Add active state to Contact
head_nav = head_nav.replace('<a href="contact.html" class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium">Contact</a>',
                            '<a href="contact.html" class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium border-b-2 border-primary-900 pb-1">Contact</a>')

# Mobile menu updates
mobile_menu = mobile_menu.replace('text-primary-900 border-b border-primary-900/10 font-bold', 'text-charcoal-900 border-b border-primary-900/10')
mobile_menu = mobile_menu.replace('<a href="contact.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-charcoal-900 border-b border-primary-900/10">Contact</a>',
                                  '<a href="contact.html" class="block py-2 text-sm uppercase tracking-widest font-medium text-primary-900 border-b border-primary-900/10 font-bold">Contact</a>')

html_content = head_nav + "\n" + mobile_menu + """
    <!-- 1. Hero Section -->
    <section class="relative pt-32 pb-20 overflow-hidden bg-earth-50">
        <div class="absolute inset-0 z-0">
            <img src="assets/botanical_ashwagandha.png" alt="Botanical Background" class="absolute top-10 left-10 w-96 opacity-10 animate-float" style="filter: grayscale(100%) sepia(20%) hue-rotate(70deg);">
            <img src="assets/botanical_shilajit.png" alt="Botanical Background" class="absolute bottom-10 right-10 w-96 opacity-10 animate-float-delayed" style="filter: grayscale(100%) sepia(20%) hue-rotate(70deg);">
        </div>
        <div class="bg-grain"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
            <span class="text-gold-600 font-sans text-xs uppercase tracking-[0.3em] font-bold mb-4 block" data-aos="fade-down">Get In Touch</span>
            <h1 class="text-5xl md:text-7xl font-serif text-primary-900 mb-6" data-aos="fade-up" data-aos-delay="100">Let's Begin Your Wellness Journey</h1>
            <p class="text-charcoal-900/70 max-w-2xl mx-auto text-lg md:text-xl font-light" data-aos="fade-up" data-aos-delay="200">
                Whether you have a question about our Ayurvedic formulations, need guidance on your regimen, or simply want to share your experience, we are here for you.
            </p>
        </div>
    </section>

    <!-- 2. Premium Contact Cards -->
    <section class="py-12 bg-earth-50 relative z-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 -mt-16">
                <!-- Head Office -->
                <div class="glass-card bg-white p-10 rounded-2xl text-center group" data-aos="fade-up" data-aos-delay="100">
                    <div class="w-16 h-16 mx-auto bg-earth-200 rounded-full flex items-center justify-center mb-6 group-hover:bg-gold-500 transition-colors duration-500">
                        <i class="fas fa-map-marker-alt text-2xl text-primary-900 group-hover:text-white transition-colors duration-500"></i>
                    </div>
                    <h3 class="text-xl font-serif text-primary-900 mb-3">Head Office</h3>
                    <p class="text-charcoal-900/70 text-sm leading-relaxed mb-4">
                        The Hanuraam Wellness HQ<br>
                        Level 4, Botanical Towers,<br>
                        New Delhi, India 110001
                    </p>
                </div>
                <!-- Email -->
                <div class="glass-card bg-white p-10 rounded-2xl text-center group" data-aos="fade-up" data-aos-delay="200">
                    <div class="w-16 h-16 mx-auto bg-earth-200 rounded-full flex items-center justify-center mb-6 group-hover:bg-gold-500 transition-colors duration-500">
                        <i class="fas fa-envelope text-2xl text-primary-900 group-hover:text-white transition-colors duration-500"></i>
                    </div>
                    <h3 class="text-xl font-serif text-primary-900 mb-3">Email Us</h3>
                    <p class="text-charcoal-900/70 text-sm leading-relaxed mb-2">For general inquiries:</p>
                    <a href="mailto:hello@hanuraam.com" class="text-primary-900 font-semibold hover:text-gold-600 transition-colors">hello@hanuraam.com</a>
                    <p class="text-charcoal-900/70 text-sm leading-relaxed mt-4 mb-2">For order support:</p>
                    <a href="mailto:support@hanuraam.com" class="text-primary-900 font-semibold hover:text-gold-600 transition-colors">support@hanuraam.com</a>
                </div>
                <!-- Phone -->
                <div class="glass-card bg-white p-10 rounded-2xl text-center group" data-aos="fade-up" data-aos-delay="300">
                    <div class="w-16 h-16 mx-auto bg-earth-200 rounded-full flex items-center justify-center mb-6 group-hover:bg-gold-500 transition-colors duration-500">
                        <i class="fas fa-phone-alt text-2xl text-primary-900 group-hover:text-white transition-colors duration-500"></i>
                    </div>
                    <h3 class="text-xl font-serif text-primary-900 mb-3">Call Us</h3>
                    <p class="text-charcoal-900/70 text-sm leading-relaxed mb-4">
                        Mon-Fri: 9:00 AM - 6:00 PM (IST)<br>
                        Sat: 10:00 AM - 4:00 PM (IST)
                    </p>
                    <a href="tel:+919876543210" class="text-primary-900 font-semibold text-lg hover:text-gold-600 transition-colors">+91 98765 43210</a>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Form & Map Section -->
    <section class="py-24 bg-earth-100 relative border-t border-primary-900/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
                <!-- Interactive Form -->
                <div class="bg-white p-10 md:p-14 rounded-3xl shadow-sm border border-primary-900/5 relative overflow-hidden" data-aos="fade-right">
                    <div class="absolute top-0 right-0 w-32 h-32 bg-earth-200 rounded-full blur-3xl opacity-50 -translate-y-1/2 translate-x-1/2"></div>
                    <h2 class="text-3xl font-serif text-primary-900 mb-2">Send us a message</h2>
                    <p class="text-charcoal-900/60 text-sm mb-10">We aim to respond to all inquiries within 24 hours.</p>
                    
                    <form action="#" method="POST" class="space-y-6" id="contactForm">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="relative group">
                                <input type="text" id="firstName" class="w-full bg-earth-50 border border-primary-900/10 rounded-lg px-4 py-4 text-sm focus:outline-none focus:border-gold-500 focus:ring-1 focus:ring-gold-500 transition-all peer placeholder-transparent" placeholder="First Name" required>
                                <label for="firstName" class="absolute left-4 top-2 text-[10px] uppercase tracking-widest text-primary-900/50 transition-all peer-placeholder-shown:top-4 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-[10px] peer-focus:text-gold-600 font-semibold">First Name</label>
                            </div>
                            <div class="relative group">
                                <input type="text" id="lastName" class="w-full bg-earth-50 border border-primary-900/10 rounded-lg px-4 py-4 text-sm focus:outline-none focus:border-gold-500 focus:ring-1 focus:ring-gold-500 transition-all peer placeholder-transparent" placeholder="Last Name" required>
                                <label for="lastName" class="absolute left-4 top-2 text-[10px] uppercase tracking-widest text-primary-900/50 transition-all peer-placeholder-shown:top-4 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-[10px] peer-focus:text-gold-600 font-semibold">Last Name</label>
                            </div>
                        </div>
                        <div class="relative group">
                            <input type="email" id="email" class="w-full bg-earth-50 border border-primary-900/10 rounded-lg px-4 py-4 text-sm focus:outline-none focus:border-gold-500 focus:ring-1 focus:ring-gold-500 transition-all peer placeholder-transparent" placeholder="Email Address" required>
                            <label for="email" class="absolute left-4 top-2 text-[10px] uppercase tracking-widest text-primary-900/50 transition-all peer-placeholder-shown:top-4 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-[10px] peer-focus:text-gold-600 font-semibold">Email Address</label>
                        </div>
                        <div class="relative group">
                            <select id="subject" class="w-full bg-earth-50 border border-primary-900/10 rounded-lg px-4 py-4 text-sm focus:outline-none focus:border-gold-500 focus:ring-1 focus:ring-gold-500 transition-all appearance-none text-charcoal-900/70" required>
                                <option value="" disabled selected>Select a subject</option>
                                <option value="Order Inquiry">Order Inquiry</option>
                                <option value="Product Advice">Product Advice</option>
                                <option value="Wholesale">Wholesale & Distribution</option>
                                <option value="Other">Other</option>
                            </select>
                            <div class="absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-primary-900/50">
                                <i class="fas fa-chevron-down text-xs"></i>
                            </div>
                        </div>
                        <div class="relative group">
                            <textarea id="message" rows="5" class="w-full bg-earth-50 border border-primary-900/10 rounded-lg px-4 py-4 text-sm focus:outline-none focus:border-gold-500 focus:ring-1 focus:ring-gold-500 transition-all peer placeholder-transparent resize-none" placeholder="Your Message" required></textarea>
                            <label for="message" class="absolute left-4 top-2 text-[10px] uppercase tracking-widest text-primary-900/50 transition-all peer-placeholder-shown:top-4 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-[10px] peer-focus:text-gold-600 font-semibold">Your Message</label>
                        </div>
                        
                        <button type="submit" class="w-full bg-primary-900 text-gold-400 font-bold uppercase tracking-widest text-xs py-5 rounded-lg hover:bg-primary-800 transition-all shadow-[0_10px_20px_rgba(22,58,47,0.15)] flex items-center justify-center group overflow-hidden relative">
                            <span class="relative z-10 flex items-center group-hover:-translate-y-10 transition-transform duration-300">Send Message</span>
                            <span class="absolute z-10 flex items-center translate-y-10 group-hover:translate-y-0 transition-transform duration-300 text-white"><i class="fas fa-paper-plane mr-2"></i> Message Sent</span>
                            <div class="absolute inset-0 bg-gold-600 translate-y-full group-hover:translate-y-0 transition-transform duration-300 z-0"></div>
                        </button>
                    </form>
                </div>
                
                <!-- Map and Support Cards -->
                <div class="space-y-8" data-aos="fade-left">
                    <!-- Map -->
                    <div class="bg-white rounded-3xl overflow-hidden shadow-sm border border-primary-900/5 h-[300px] relative">
                        <!-- Placeholder for a premium map. E.g., a static styling of Google Maps or Mapbox -->
                        <div class="absolute inset-0 bg-earth-200">
                            <!-- Premium styled map image -->
                            <img src="https://images.unsplash.com/photo-1524661135-423995f22d0b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80" alt="Map Location" class="w-full h-full object-cover opacity-80" style="filter: grayscale(80%) contrast(1.2);">
                        </div>
                        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white/90 backdrop-blur-md px-6 py-4 rounded-xl shadow-lg border border-gold-500/20 text-center">
                            <h4 class="font-serif text-primary-900 text-lg mb-1">HQ Location</h4>
                            <p class="text-xs text-charcoal-900/60 uppercase tracking-widest">New Delhi, India</p>
                        </div>
                    </div>
                    
                    <!-- Support Cards -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <a href="mailto:wholesale@hanuraam.com" class="block bg-white p-6 rounded-2xl shadow-sm border border-primary-900/5 hover:border-gold-500/30 hover:shadow-md transition-all group">
                            <i class="fas fa-box-open text-gold-500 text-xl mb-4 group-hover:scale-110 transition-transform"></i>
                            <h4 class="font-bold text-primary-900 mb-1 text-sm">Wholesale</h4>
                            <p class="text-xs text-charcoal-900/60">Partner with our premium brand.</p>
                        </a>
                        <a href="mailto:press@hanuraam.com" class="block bg-white p-6 rounded-2xl shadow-sm border border-primary-900/5 hover:border-gold-500/30 hover:shadow-md transition-all group">
                            <i class="fas fa-newspaper text-gold-500 text-xl mb-4 group-hover:scale-110 transition-transform"></i>
                            <h4 class="font-bold text-primary-900 mb-1 text-sm">Media & Press</h4>
                            <p class="text-xs text-charcoal-900/60">For PR and media inquiries.</p>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. FAQ Section -->
    <section class="py-24 bg-white relative overflow-hidden">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center mb-16" data-aos="fade-up">
                <span class="text-gold-600 font-sans text-xs uppercase tracking-[0.3em] font-bold mb-4 block">Support</span>
                <h2 class="text-3xl md:text-5xl font-serif text-primary-900">Frequently Asked Questions</h2>
            </div>
            
            <div class="space-y-4" data-aos="fade-up" data-aos-delay="100">
                <!-- FAQ 1 -->
                <div class="border border-primary-900/10 rounded-2xl overflow-hidden bg-earth-50/50">
                    <button class="w-full text-left px-8 py-6 flex justify-between items-center focus:outline-none group" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.icon').classList.toggle('rotate-180')">
                        <span class="font-serif text-lg text-primary-900 group-hover:text-gold-600 transition-colors">How long does shipping take?</span>
                        <i class="fas fa-chevron-down text-gold-500 transition-transform duration-300 icon"></i>
                    </button>
                    <div class="px-8 pb-6 hidden text-charcoal-900/70 text-sm leading-relaxed">
                        Domestic orders within India typically arrive within 3-5 business days via our premium courier partners. International shipping takes 7-14 business days depending on the destination. All orders include tracking information.
                    </div>
                </div>
                <!-- FAQ 2 -->
                <div class="border border-primary-900/10 rounded-2xl overflow-hidden bg-earth-50/50">
                    <button class="w-full text-left px-8 py-6 flex justify-between items-center focus:outline-none group" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.icon').classList.toggle('rotate-180')">
                        <span class="font-serif text-lg text-primary-900 group-hover:text-gold-600 transition-colors">Are your products 100% natural?</span>
                        <i class="fas fa-chevron-down text-gold-500 transition-transform duration-300 icon"></i>
                    </button>
                    <div class="px-8 pb-6 hidden text-charcoal-900/70 text-sm leading-relaxed">
                        Yes. We pride ourselves on using only 100% pure, natural botanical extracts. Our formulations contain zero synthetic additives, fillers, or artificial preservatives, ensuring you receive the absolute highest quality Ayurvedic care.
                    </div>
                </div>
                <!-- FAQ 3 -->
                <div class="border border-primary-900/10 rounded-2xl overflow-hidden bg-earth-50/50">
                    <button class="w-full text-left px-8 py-6 flex justify-between items-center focus:outline-none group" onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('.icon').classList.toggle('rotate-180')">
                        <span class="font-serif text-lg text-primary-900 group-hover:text-gold-600 transition-colors">Do you offer international wholesale?</span>
                        <i class="fas fa-chevron-down text-gold-500 transition-transform duration-300 icon"></i>
                    </button>
                    <div class="px-8 pb-6 hidden text-charcoal-900/70 text-sm leading-relaxed">
                        We selectively partner with premium retailers and luxury spas globally. Please reach out to wholesale@hanuraam.com with details about your business to apply for a wholesale account.
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Trust & Certifications (Minimal banner) -->
    <section class="py-12 bg-primary-900 text-white relative overflow-hidden border-y border-gold-500/20">
        <div class="bg-grain"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10">
            <div class="flex flex-wrap justify-center items-center gap-12 md:gap-24 opacity-80">
                <div class="flex flex-col items-center">
                    <i class="fas fa-leaf text-3xl text-gold-400 mb-2"></i>
                    <span class="text-[10px] uppercase tracking-widest font-bold">100% Natural</span>
                </div>
                <div class="flex flex-col items-center">
                    <i class="fas fa-flask text-3xl text-gold-400 mb-2"></i>
                    <span class="text-[10px] uppercase tracking-widest font-bold">Lab Tested</span>
                </div>
                <div class="flex flex-col items-center">
                    <i class="fas fa-certificate text-3xl text-gold-400 mb-2"></i>
                    <span class="text-[10px] uppercase tracking-widest font-bold">GMP Certified</span>
                </div>
                <div class="flex flex-col items-center">
                    <i class="fas fa-vial text-3xl text-gold-400 mb-2"></i>
                    <span class="text-[10px] uppercase tracking-widest font-bold">No Synthetics</span>
                </div>
            </div>
        </div>
    </section>
""" + footer_scripts

with open('e:/ecc/build_contact.py', 'w', encoding='utf-8') as f:
    f.write(f"""
html = r'''{html_content}'''
with open('contact.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html)
""")

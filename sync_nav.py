import os
import re
import glob

def get_base_nav():
    with open('e:/ecc/about.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    nav_match = re.search(r'(<nav.*?</nav>)', html, re.DOTALL)
    mobile_match = re.search(r'(<div id="mobile-menu".*?</div>\s*</div>)', html, re.DOTALL)
    
    if not nav_match or not mobile_match:
        print("Could not find nav in about.html")
        exit(1)
        
    nav = nav_match.group(1)
    mobile = mobile_match.group(1)
    
    # Strip active states from about
    nav = nav.replace('border-b-2 border-primary-900 pb-1', '')
    nav = nav.replace('class="text-primary-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium"', 'class="text-charcoal-900 hover:text-gold-600 transition-colors uppercase text-sm tracking-widest font-medium"')
    
    mobile = mobile.replace('text-primary-900 border-b border-primary-900/10 font-bold', 'text-charcoal-900 border-b border-primary-900/10')
    
    return nav, mobile

base_nav, base_mobile = get_base_nav()

files = glob.glob('e:/ecc/*.html') + glob.glob('e:/ecc/build_*.py')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find existing nav and mobile menu
    if '<nav' not in content:
        continue
        
    # Replace nav block
    new_content = re.sub(r'<nav.*?</nav>', base_nav.replace('\\', '\\\\'), content, flags=re.DOTALL)
    # Replace mobile menu block (if it exists)
    if '<div id="mobile-menu"' in new_content:
        new_content = re.sub(r'<div id="mobile-menu".*?</div>\s*</div>', base_mobile.replace('\\', '\\\\'), new_content, flags=re.DOTALL)
    else:
        # if it wasn't there before but we want to add it, we insert it after </nav>
        new_content = new_content.replace('</nav>', '</nav>\n    ' + base_mobile)
        
    # Set active state
    page_name = os.path.basename(filepath).replace('.html', '').replace('build_', '').replace('.py', '')
    if 'product' in page_name or page_name == 'cart':
        page_name = 'products'
        
    # Determine the link to target
    target_link = f'href="{page_name}.html"'
    
    # Add active class for Desktop Nav
    def repl_desktop(m):
        return m.group(0).replace('text-charcoal-900', 'text-primary-900').replace('font-medium', 'font-medium border-b-2 border-primary-900 pb-1')
        
    # Add active class for Mobile Menu
    def repl_mobile(m):
        return m.group(0).replace('text-charcoal-900', 'text-primary-900').replace('font-medium', 'font-medium font-bold')

    # Apply only to the link with href="{page_name}.html"
    # To differentiate, desktop links have 'tracking-widest', mobile links might have 'block'
    new_content = re.sub(r'<a href="' + page_name + r'\.html"[^>]*class="[^"]*hidden md:flex[^"]*"[^>]*>', repl_desktop, new_content)
    
    # Actually, let's just do a simple replacement for all matching links
    new_content = re.sub(r'<a href="' + page_name + r'\.html"[^>]*>', 
                         lambda m: m.group(0).replace('text-charcoal-900', 'text-primary-900').replace('font-medium', 'font-medium border-b-2 border-primary-900 pb-1') if 'block' not in m.group(0) else m.group(0).replace('text-charcoal-900', 'text-primary-900').replace('font-medium', 'font-medium font-bold'), 
                         new_content)
                         
    # Removed ingredients exception since it's light theme now
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated nav in {filepath}")

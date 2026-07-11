import glob
import re

py_files = glob.glob('e:/ecc/build_*.py')

for filepath in py_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the broken logo line with the fixed one
    broken = '<img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-12 mb-6 brightness-0 invert">'
    fixed = '<img src="assets/logo.png" alt="THE HANURAAM WELLNESS" class="h-16 mb-6 object-contain bg-white/10 p-2 rounded-lg">'
    
    new_content = content.replace(broken, fixed)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed logo in {filepath}")

import os
import re
import glob

# 1. Get the target footer from about.html
with open('e:/ecc/about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

# Extract footer using regex
footer_match = re.search(r'(<footer[^>]*>.*?</footer>)', about_content, re.DOTALL)
if not footer_match:
    print("Could not find footer in about.html")
    exit(1)

target_footer = footer_match.group(1)

# 2. Files to process
html_files = glob.glob('e:/ecc/*.html')
py_files = glob.glob('e:/ecc/build_*.py')

for filepath in html_files + py_files:
    if filepath.endswith('about.html'):
        continue # Already has it
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # In python scripts, the footer might be escaped or indented, but let's try direct replacement
    # Wait, in python scripts, replacing <footer ...> might be tricky because of """ strings or \n.
    # It's better to just do it for html files.
    
    if filepath.endswith('.html'):
        # Replace existing footer
        new_content, count = re.subn(r'<footer[^>]*>.*?</footer>', target_footer.replace('\\', '\\\\'), content, flags=re.DOTALL)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated footer in {filepath}")

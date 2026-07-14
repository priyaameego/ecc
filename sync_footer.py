import os
import re
import glob

def get_base_footer():
    with open('e:/ecc/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    footer_match = re.search(r'(<footer.*?</footer>)', html, re.DOTALL)
        
    if not footer_match:
        print("Could not find footer in index.html")
        exit(1)
        
    return footer_match.group(1)

base_footer = get_base_footer()
base_footer_escaped = base_footer.replace('{', '{{').replace('}', '}}')

files = glob.glob('e:/ecc/*.html') + glob.glob('e:/ecc/build_*.py')

for filepath in files:
    if filepath.endswith('index.html') or filepath.endswith('build_index.py'):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '<footer' not in content:
        continue
        
    is_py = filepath.endswith('.py')
    replacement = base_footer_escaped if is_py else base_footer
        
    new_content = re.sub(r'<footer.*?</footer>', lambda m: replacement, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated footer in {filepath}")


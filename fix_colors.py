import glob
import re

files = glob.glob('e:/ecc/*.html') + glob.glob('e:/ecc/build_*.py')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'charcoal:' not in content and 'colors: {' in content:
        # Add charcoal color
        new_content = re.sub(
            r'colors:\s*\{', 
            "colors: {\n                        charcoal: { 800: '#2D2D2D', 900: '#1C1C1C' },", 
            content
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added charcoal color to {filepath}")
        
    elif 'charcoal:' not in content and '"colors": {' in content: # maybe JSON string?
        pass


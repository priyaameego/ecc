import glob

files = glob.glob('e:/ecc/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if this file has the nav structure
    if '<div class="flex justify-between items-center h-20">' in content and '<div class="flex-shrink-0 flex items-center">' in content:
        content = content.replace('<div class="flex justify-between items-center h-20">', '<div class="flex justify-between items-center h-20 relative">')
        content = content.replace('<div class="flex-shrink-0 flex items-center">', '<div class="absolute left-1/2 -translate-x-1/2 flex items-center">')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath} (pattern not found)")

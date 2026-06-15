import re

with open('c:/LocalFiles/Bali/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove all photo-badge spans
html = re.sub(r'<span class="photo-badge">.*?</span>', '', html, flags=re.DOTALL)

with open('c:/LocalFiles/Bali/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed photo badges.")

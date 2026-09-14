import urllib.request
import os

os.makedirs('icons', exist_ok=True)

icons = {
    'linkedin': ('https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/linkedin.svg', '#0A66C2'),
    'gmail': ('https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/gmail.svg', '#EA4335'),
    'leetcode': ('https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/leetcode.svg', '#FFA116'),
    'github': ('https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg', '#FFFFFF')
}

for name, (url, color) in icons.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg = response.read().decode('utf-8')
            svg = svg.replace('<svg ', f'<svg fill="{color}" ')
            with open(f'icons/{name}.svg', 'w', encoding='utf-8') as f:
                f.write(svg)
        print(f'Downloaded and colored {name}.svg')
    except Exception as e:
        print(f'Error fetching {name}: {e}')

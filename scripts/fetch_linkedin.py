import urllib.request
import os

os.makedirs('icons', exist_ok=True)
url = 'https://unpkg.com/simple-icons@v11.14.0/icons/linkedin.svg'
color = '#0A66C2'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    svg = response.read().decode('utf-8')
    svg = svg.replace('<svg ', f'<svg fill="{color}" ')
    with open('icons/linkedin.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Downloaded linkedin.svg')

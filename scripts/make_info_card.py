import os

def generate_info_card(output_path="info-card.svg", static_mode=False):
    svg_width = 490
    svg_height = 490
    
    card_data = [
        ("USER", "Srujan Satav (sruj08)", "#58a6ff"),
        ("ROLES", "Co-Founder @ Novaryn | Partner @ MindstriX", "#79c0ff"),
        ("EDU", "B.Tech ENTC @ PICT Pune (CGPA: 8.38)", "#d2a8ff"),
        ("WINS", "🏆 4x Hackathon Winner (Pune Agri 15L, TechFiesta #1)", "#ffbd2e"),
        ("LANGS", "Golang, C++, C, Java, Python, Solidity, JS/TS", "#7ee787"),
        ("BACKEND", "Go Microservices, REST APIs, Docker, GCP, Firebase", "#38d430"),
        ("AI / ML", "LLMs, RAG, LangChain, YOLOv8, OpenCV, CNN", "#e3b341"),
        ("WEB3", "Solidity, Smart Contracts, OpenZeppelin, Sepolia", "#f78166"),
        ("STATUS", "🟢 Building Production AI & Blockchain Systems", "#56d364"),
    ]
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg.append('<defs>')
    # 3D gradient borders
    svg.append('  <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#58a6ff" stop-opacity="0.8" />')
    svg.append('    <stop offset="50%" stop-color="#bc8cff" stop-opacity="0.5" />')
    svg.append('    <stop offset="100%" stop-color="#39d353" stop-opacity="0.8" />')
    svg.append('  </linearGradient>')
    svg.append('</defs>')
    
    svg.append('<style>')
    svg.append('  .card-bg { fill: #0d1117; rx: 10px; ry: 10px; stroke: url(#cardBorder); stroke-width: 1.5px; }')
    svg.append('  .header-bg { fill: #161b22; rx: 10px; ry: 10px; }')
    svg.append('  .title { font-family: monospace, Courier; font-size: 11px; font-weight: bold; fill: #8b949e; }')
    svg.append('  .key { font-family: monospace, Courier; font-size: 11.5px; font-weight: bold; fill: #8b949e; }')
    svg.append('  .val { font-family: monospace, Courier; font-size: 11.5px; }')
    svg.append('  .prompt-line { font-family: monospace, Courier; font-size: 12.5px; font-weight: bold; fill: #39d353; }')
    svg.append('  .anim-line { opacity: 1; }')
    svg.append('</style>')
    
    # Outer terminal box
    svg.append(f'<rect width="{svg_width - 4}" height="{svg_height - 4}" x="2" y="2" class="card-bg" />')
    
    # Title bar
    svg.append(f'<path d="M 2 10 A 8 8 0 0 1 10 2 L {svg_width - 10} 2 A 8 8 0 0 1 {svg_width - 2} 10 L {svg_width - 2} 30 L 2 30 Z" class="header-bg" stroke="#30363d" stroke-width="1" />')
    svg.append('<circle cx="16" cy="16" r="4.5" fill="#ff5f56" />')
    svg.append('<circle cx="28" cy="16" r="4.5" fill="#ffbd2e" />')
    svg.append('<circle cx="40" cy="16" r="4.5" fill="#27c93f" />')
    svg.append(f'<text x="{svg_width/2}" y="20" text-anchor="middle" class="title">neofetch --user sruj08</text>')
    
    # Shell prompt title
    start_y = 54
    line_spacing = 32
    
    delay = 0.05
    svg.append(f'<g class="anim-line">')
    svg.append(f'  <text x="20" y="{start_y}" class="prompt-line">sruj08@pict-pune:~$ <tspan fill="#e6edf3">neofetch</tspan></text>')
    svg.append(f'  <line x1="20" y1="{start_y + 10}" x2="{svg_width - 20}" y2="{start_y + 10}" stroke="#30363d" stroke-width="1" />')
    svg.append('</g>')
    
    # Render key-value pairs
    for i, (key, val, color) in enumerate(card_data):
        y_pos = start_y + 36 + i * line_spacing
        delay += 0.1
        
        svg.append(f'<g class="anim-line">')
        svg.append(f'  <text x="22" y="{y_pos}" class="key">{key.lower()}</text>')
        svg.append(f'  <text x="110" y="{y_pos}" class="key" fill="#8b949e">-&gt;</text>')
        svg.append(f'  <text x="132" y="{y_pos}" class="val" fill="{color}">{val}</text>')
        svg.append('</g>')

        
    # Terminal palette blocks at the bottom
    palette_y = start_y + 36 + len(card_data) * line_spacing + 10
    colors = ["#161b22", "#ff5f56", "#27c93f", "#ffbd2e", "#58a6ff", "#bc8cff", "#39d353", "#e6edf3"]
    
    svg.append(f'<g class="anim-line">')
    svg.append(f'  <line x1="20" y1="{palette_y - 12}" x2="{svg_width - 20}" y2="{palette_y - 12}" stroke="#30363d" stroke-width="1" />')
    for idx, c in enumerate(colors):
        x_pos = 22 + idx * 26
        svg.append(f'  <rect x="{x_pos}" y="{palette_y}" width="20" height="14" rx="3" fill="{c}" />')
    svg.append('</g>')
    
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Info Card SVG created at {output_path}")

if __name__ == "__main__":
    generate_info_card("info-card.svg")

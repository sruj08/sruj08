import os

def generate_info_card(output_path="info-card.svg", static_mode=False):
    svg_width = 490
    svg_height = 490
    
    is_static = static_mode or os.environ.get("STATIC") == "1"
    
    card_data = [
        ("USER", "Srujan Satav (sruj08)", "#58a6ff"),
        ("ROLE", "Electronics & Telecom Student @ PICT Pune", "#79c0ff"),
        ("ORG", "@KrishiSahAI", "#d2a8ff"),
        ("LOCATION", "Pune, Maharashtra, India 🇮🇳", "#ffa657"),
        ("LANGUAGES", "Python, C++, C, JavaScript, SQL", "#7ee787"),
        ("DOMAINS", "Embedded Systems, AI/ML, Web Dev, IoT", "#38d430"),
        ("REPOS", "20 Public Repositories on GitHub", "#e3b341"),
        ("TWITTER", "@SatavSruja549", "#1da1f2"),
        ("STATUS", "🟢 Open for Collaborations & Internships", "#56d364"),
    ]
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg.append('<style>')
    svg.append('  @keyframes fadeIn {')
    svg.append('    from { opacity: 0; transform: translateY(8px); }')
    svg.append('    to { opacity: 1; transform: translateY(0); }')
    svg.append('  }')
    svg.append('  .card-bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    svg.append('  .header-bg { fill: #161b22; rx: 8px; ry: 8px; }')
    svg.append('  .title { font-family: monospace; font-size: 11px; font-weight: bold; fill: #8b949e; }')
    svg.append('  .key { font-family: "Fira Code", monospace; font-size: 12px; font-weight: bold; fill: #8b949e; }')
    svg.append('  .val { font-family: "Fira Code", monospace; font-size: 12px; }')
    svg.append('  .prompt-line { font-family: monospace; font-size: 13px; font-weight: bold; fill: #39d353; }')
    svg.append('  .color-block { width: 14px; height: 14px; rx: 3px; display: inline-block; }')
    
    if not is_static:
        svg.append('  .anim-line { opacity: 0; animation: fadeIn 0.4s ease-out forwards; }')
    else:
        svg.append('  .anim-line { opacity: 1; }')
        
    svg.append('</style>')
    
    # Outer terminal box
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="card-bg" />')
    
    # Title bar
    svg.append(f'<path d="M 0 8 A 8 8 0 0 1 8 0 L {svg_width - 8} 0 A 8 8 0 0 1 {svg_width} 8 L {svg_width} 28 L 0 28 Z" class="header-bg" stroke="#30363d" stroke-width="1" />')
    svg.append('<circle cx="15" cy="14" r="4" fill="#ff5f56" />')
    svg.append('<circle cx="27" cy="14" r="4" fill="#ffbd2e" />')
    svg.append('<circle cx="39" cy="14" r="4" fill="#27c93f" />')
    svg.append(f'<text x="{svg_width/2}" y="18" text-anchor="middle" class="title">neofetch --user sruj08</text>')
    
    # Shell prompt title
    start_y = 54
    line_spacing = 32
    
    delay = 0.1
    svg.append(f'<g class="anim-line" style="animation-delay: {delay:.2f}s;">')
    svg.append(f'  <text x="20" y="{start_y}" class="prompt-line">sruj08@pict-pune:~$ <tspan fill="#e6edf3">neofetch</tspan></text>')
    svg.append(f'  <line x1="20" y1="{start_y + 10}" x2="{svg_width - 20}" y2="{start_y + 10}" stroke="#30363d" stroke-width="1" />')
    svg.append('</g>')
    
    # Render key-value pairs
    for i, (key, val, color) in enumerate(card_data):
        y_pos = start_y + 36 + i * line_spacing
        delay += 0.15
        
        svg.append(f'<g class="anim-line" style="animation-delay: {delay:.2f}s;">')
        svg.append(f'  <text x="24" y="{y_pos}" class="key">{key.lower()}</text>')
        svg.append(f'  <text x="120" y="{y_pos}" class="key" fill="#8b949e">-&gt;</text>')
        svg.append(f'  <text x="145" y="{y_pos}" class="val" fill="{color}">{val}</text>')
        svg.append('</g>')
        
    # Terminal palette blocks at the bottom
    palette_y = start_y + 36 + len(card_data) * line_spacing + 10
    colors = ["#161b22", "#ff5f56", "#27c93f", "#ffbd2e", "#58a6ff", "#bc8cff", "#39d353", "#e6edf3"]
    
    delay += 0.2
    svg.append(f'<g class="anim-line" style="animation-delay: {delay:.2f}s;">')
    svg.append(f'  <line x1="20" y1="{palette_y - 12}" x2="{svg_width - 20}" y2="{palette_y - 12}" stroke="#30363d" stroke-width="1" />')
    for idx, c in enumerate(colors):
        x_pos = 24 + idx * 26
        svg.append(f'  <rect x="{x_pos}" y="{palette_y}" width="20" height="14" rx="3" fill="{c}" />')
    svg.append('</g>')
    
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Info Card SVG created at {output_path}")

if __name__ == "__main__":
    generate_info_card("info-card.svg")

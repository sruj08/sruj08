import os

def generate_hackathon_3d_svg(output_path="hackathon-3d-trophies.svg"):
    svg_width = 860
    svg_height = 270
    
    trophies = [
        {
            "title": "Pune Agri Hackathon '26",
            "subtitle": "Govt. of Maharashtra",
            "prize": "INR 15 Lakhs",
            "rank": "🏆 Runner-Up",
            "stats": "Out of 2,000+ Teams Worldwide",
            "detail": "Felicitated by Hon. Chief Minister of Maharashtra",
            "color1": "#f1e05a",
            "color2": "#e3b341"
        },
        {
            "title": "TechFiesta '26 Global",
            "subtitle": "International Hackathon",
            "prize": "INR 3.5L+ Pool",
            "rank": "🥇 1st Rank (Winner)",
            "stats": "Out of 700+ Teams Worldwide",
            "detail": "Executed full architectural pivot in 24 hours",
            "color1": "#38d430",
            "color2": "#26a641"
        },
        {
            "title": "VOIS Innovation Marathon 2.0",
            "subtitle": "Vodafone Intelligent Solutions",
            "prize": "INR 2 Lakhs",
            "rank": "🥇 National Winner",
            "stats": "Out of 630+ Teams Nationwide",
            "detail": "Owned architecture and production deployment",
            "color1": "#58a6ff",
            "color2": "#1f6feb"
        },
        {
            "title": "iQOO Hackathon '26",
            "subtitle": "Phone-First Computing",
            "prize": "INR 50,000",
            "rank": "🥉 2nd Runner-Up",
            "stats": "6,500+ Registrations",
            "detail": "On-device offline spatial memory & path tracker",
            "color1": "#d2a8ff",
            "color2": "#8957e5"
        }
    ]
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    
    # 3D Filters and Gradients
    svg.append('<defs>')
    svg.append('  <filter id="glow3d" x="-20%" y="-20%" width="140%" height="140%">')
    svg.append('    <feGaussianBlur stdDeviation="4" result="blur" />')
    svg.append('    <feComposite in="SourceGraphic" in2="blur" operator="over" />')
    svg.append('  </filter>')
    svg.append('  <filter id="shadow3d" x="-10%" y="-10%" width="120%" height="120%">')
    svg.append('    <feDropShadow dx="0" dy="10" stdDeviation="6" flood-color="#000000" flood-opacity="0.7" />')
    svg.append('  </filter>')
    
    # Card bevel gradients
    svg.append('  <linearGradient id="panelGrad" x1="0%" y1="0%" x2="0%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#161b22" />')
    svg.append('    <stop offset="100%" stop-color="#0d1117" />')
    svg.append('  </linearGradient>')
    
    svg.append('  <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#30363d" />')
    svg.append('    <stop offset="50%" stop-color="#58a6ff" stop-opacity="0.6" />')
    svg.append('    <stop offset="100%" stop-color="#30363d" />')
    svg.append('  </linearGradient>')
    svg.append('</defs>')
    
    svg.append('<style>')
    svg.append('  @keyframes floatUp {')
    svg.append('    0% { transform: translateY(0px); }')
    svg.append('    50% { transform: translateY(-4px); }')
    svg.append('    100% { transform: translateY(0px); }')
    svg.append('  }')
    svg.append('  .bg { fill: #0d1117; rx: 10px; ry: 10px; stroke: #30363d; stroke-width: 1px; }')
    svg.append('  .card-3d { fill: url(#panelGrad); rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1.5px; filter: url(#shadow3d); transition: all 0.3s; }')
    svg.append('  .card-3d:hover { stroke: #58a6ff; }')
    svg.append('  .title-bar { fill: #161b22; rx: 10px; ry: 10px; }')
    svg.append('  .header-title { font-family: monospace; font-size: 11px; font-weight: bold; fill: #8b949e; }')
    svg.append('  .trophy-title { font-family: "Fira Code", monospace; font-size: 13px; font-weight: bold; fill: #e6edf3; }')
    svg.append('  .trophy-sub { font-family: monospace; font-size: 10px; fill: #8b949e; }')
    svg.append('  .trophy-rank { font-family: "Fira Code", monospace; font-size: 12px; font-weight: bold; }')
    svg.append('  .trophy-prize { font-family: "Fira Code", monospace; font-size: 11px; font-weight: bold; fill: #39d353; }')
    svg.append('  .trophy-detail { font-family: system-ui, sans-serif; font-size: 10px; fill: #8b949e; }')
    svg.append('</style>')
    
    # Outer terminal container
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="bg" />')
    
    # Terminal header bar
    svg.append(f'<path d="M 0 8 A 8 8 0 0 1 8 0 L {svg_width - 8} 0 A 8 8 0 0 1 {svg_width} 8 L {svg_width} 28 L 0 28 Z" class="title-bar" stroke="#30363d" stroke-width="1" />')
    svg.append('<circle cx="15" cy="14" r="4" fill="#ff5f56" />')
    svg.append('<circle cx="27" cy="14" r="4" fill="#ffbd2e" />')
    svg.append('<circle cx="39" cy="14" r="4" fill="#27c93f" />')
    svg.append(f'<text x="{svg_width/2}" y="18" text-anchor="middle" class="header-title">sruj08@github ~ $ ./showcase_hackathons.sh --major-wins</text>')
    
    # Render 4 3D Trophy Cards (2x2 grid)
    card_w = 398
    card_h = 100
    start_x = 22
    start_y = 42
    gap_x = 20
    gap_y = 12
    
    for idx, t in enumerate(trophies):
        col = idx % 2
        row = idx // 2
        
        x = start_x + col * (card_w + gap_x)
        y = start_y + row * (card_h + gap_y)
        
        # 3D Card Background
        svg.append(f'<g class="card-group">')
        svg.append(f'  <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" class="card-3d" />')
        
        # Top accent bar with 3D color gradient
        svg.append(f'  <path d="M {x+1} {y+8} A 8 8 0 0 1 {x+9} {y+1} L {x+card_w-9} {y+1} A 8 8 0 0 1 {x+card_w-1} {y+8} L {x+card_w-1} {y+5} L {x+1} {y+5} Z" fill="{t["color1"]}" opacity="0.9" />')
        
        # Rank & Title
        svg.append(f'  <text x="{x + 16}" y="{y + 24}" class="trophy-rank" fill="{t["color1"]}">{t["rank"]}</text>')
        svg.append(f'  <text x="{x + card_w - 16}" y="{y + 24}" text-anchor="end" class="trophy-prize">{t["prize"]}</text>')
        
        svg.append(f'  <text x="{x + 16}" y="{y + 44}" class="trophy-title">{t["title"]}</text>')
        svg.append(f'  <text x="{x + 16}" y="{y + 60}" class="trophy-sub">{t["subtitle"]} • <tspan fill="#e6edf3">{t["stats"]}</tspan></text>')
        
        # Detail line
        svg.append(f'  <line x1="{x + 16}" y1="{y + 70}" x2="{x + card_w - 16}" y2="{y + 70}" stroke="#30363d" stroke-width="1" />')
        svg.append(f'  <text x="{x + 16}" y="{y + 86}" class="trophy-detail">✨ {t["detail"]}</text>')
        svg.append('</g>')
        
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"3D Hackathon Trophies SVG created at {output_path}")

if __name__ == "__main__":
    generate_hackathon_3d_svg("hackathon-3d-trophies.svg")

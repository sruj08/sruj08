import os

def generate_apple_achievements_svg(output_path="apple-achievements.svg"):
    svg_width = 860
    svg_height = 250
    
    achievements = [
        {
            "title": "Pune Agri Hackathon 2026",
            "subtitle": "Govt. of Maharashtra",
            "rank": "🏆 Runner-Up (INR 15 Lakhs)",
            "scope": "2,000+ Teams Worldwide",
            "detail": "Felicitated by Chief Minister of Maharashtra",
            "accent": "#ffd60a"
        },
        {
            "title": "TechFiesta '26 International",
            "subtitle": "Global Agriculture Domain",
            "rank": "🥇 1st Rank (INR 3.5L+ Pool)",
            "scope": "700+ Teams Worldwide",
            "detail": "Executed full 24-hour architectural pivot",
            "accent": "#30d158"
        },
        {
            "title": "VOIS Innovation Marathon 2.0",
            "subtitle": "Vodafone Intelligent Solutions",
            "rank": "🥇 National Winner (INR 2 Lakhs)",
            "scope": "630+ Teams Nationwide",
            "detail": "Architected & deployed live production cloud system",
            "accent": "#2997ff"
        },
        {
            "title": "iQOO Hackathon 2026",
            "subtitle": "Phone-First Computing",
            "rank": "🥉 2nd Runner-Up (INR 50K)",
            "scope": "6,500+ Registrations",
            "detail": "Built on-device spatial memory & offline tracker",
            "accent": "#bf5af2"
        }
    ]
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg.append('<defs>')
    svg.append('  <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#161b22" />')
    svg.append('    <stop offset="100%" stop-color="#0d1117" />')
    svg.append('  </linearGradient>')
    svg.append('</defs>')
    
    svg.append('<style>')
    svg.append('  .outer-card { fill: #0d1117; rx: 16px; ry: 16px; stroke: #30363d; stroke-width: 1.2px; }')
    svg.append('  .inner-card { fill: url(#cardBg); rx: 12px; ry: 12px; stroke: #30363d; stroke-width: 1px; }')
    svg.append('  .section-title { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif; font-size: 15px; font-weight: 700; fill: #f0f6fc; }')
    svg.append('  .item-title { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 13.5px; font-weight: 700; fill: #f0f6fc; }')
    svg.append('  .item-sub { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 11px; fill: #8b949e; }')
    svg.append('  .item-rank { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 12px; font-weight: 700; }')
    svg.append('  .item-detail { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 11px; fill: #8b949e; }')
    svg.append('</style>')
    
    # Base Outer Container
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="outer-card" />')
    
    # Header Title
    svg.append(f'<text x="24" y="32" class="section-title">🏆 Major Hackathon Victories &amp; Honors</text>')
    
    # Render 4 Grid Items (2x2)
    card_w = 398
    card_h = 88
    start_x = 22
    start_y = 48
    gap_x = 20
    gap_y = 12
    
    for idx, item in enumerate(achievements):
        col = idx % 2
        row = idx // 2
        
        x = start_x + col * (card_w + gap_x)
        y = start_y + row * (card_h + gap_y)
        
        svg.append(f'<g>')
        svg.append(f'  <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" class="inner-card" />')
        
        # Left subtle accent pill bar
        svg.append(f'  <rect x="{x + 12}" y="{y + 14}" width="4" height="{card_h - 28}" rx="2" fill="{item["accent"]}" />')
        
        # Title & Rank
        svg.append(f'  <text x="{x + 24}" y="{y + 28}" class="item-title">{item["title"]}</text>')
        svg.append(f'  <text x="{x + card_w - 16}" y="{y + 28}" text-anchor="end" class="item-rank" fill="{item["accent"]}">{item["rank"]}</text>')
        
        # Subtitle & Scope
        svg.append(f'  <text x="{x + 24}" y="{y + 46}" class="item-sub">{item["subtitle"]}  •  <tspan fill="#e6edf3">{item["scope"]}</tspan></text>')
        
        # Detail line
        svg.append(f'  <text x="{x + 24}" y="{y + 66}" class="item-detail">✨ {item["detail"]}</text>')
        svg.append('</g>')
        
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Apple Achievements SVG created at {output_path}")

if __name__ == "__main__":
    generate_apple_achievements_svg("apple-achievements.svg")

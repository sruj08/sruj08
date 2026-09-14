import os

def generate_apple_header_svg(output_path="apple-header.svg"):
    svg_width = 860
    svg_height = 200
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg.append('<defs>')
    # Subtle Apple dark glass gradient
    svg.append('  <linearGradient id="appleBg" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#161b22" />')
    svg.append('    <stop offset="100%" stop-color="#0d1117" />')
    svg.append('  </linearGradient>')
    # Subtle accent gradient
    svg.append('  <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('    <stop offset="0%" stop-color="#2997ff" />')
    svg.append('    <stop offset="50%" stop-color="#a155b9" />')
    svg.append('    <stop offset="100%" stop-color="#30d158" />')
    svg.append('  </linearGradient>')
    svg.append('</defs>')
    
    svg.append('<style>')
    svg.append('  .card { fill: url(#appleBg); rx: 16px; ry: 16px; stroke: #30363d; stroke-width: 1.2px; }')
    svg.append('  .name { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif; font-size: 34px; font-weight: 700; fill: #f0f6fc; letter-spacing: -0.5px; }')
    svg.append('  .subtitle { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, sans-serif; font-size: 15px; font-weight: 500; fill: #2997ff; letter-spacing: -0.2px; }')
    svg.append('  .bio { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, sans-serif; font-size: 13.5px; fill: #8b949e; line-height: 1.5; }')
    svg.append('  .pill-bg { rx: 12px; ry: 12px; fill: #21262d; stroke: #363b42; stroke-width: 1px; }')
    svg.append('  .pill-text { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", monospace; font-size: 11px; font-weight: 600; fill: #e6edf3; }')
    svg.append('</style>')
    
    # Base Apple Card
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="card" />')
    
    # Top subtle multi-color accent line
    svg.append(f'<path d="M 0 16 A 16 16 0 0 1 16 0 L {svg_width - 16} 0 A 16 16 0 0 1 {svg_width} 16 L {svg_width} 4 L 0 4 Z" fill="url(#accentGrad)" opacity="0.95" />')
    
    # Content
    start_x = 36
    
    # Name
    svg.append(f'<text x="{start_x}" y="56" class="name">Srujan Satav</text>')
    
    # Subtitle / Roles
    svg.append(f'<text x="{start_x}" y="82" class="subtitle">Co-Founder @ Novaryn Technologies  •  Partner @ MindstriX  •  PICT Pune \'26</text>')
    
    # Bio description
    svg.append(f'<text x="{start_x}" y="110" class="bio">Building high-performance Go microservices, AI/ML pipelines, and Web3 architecture.</text>')
    
    # Key Metric Apple Badges
    pills = [
        ("🏆 Pune Agri Hackathon 15L Runner-Up", "#ffd60a"),
        ("🥇 TechFiesta '26 Global #1", "#30d158"),
        ("🥇 VOIS 2.0 National Winner", "#2997ff"),
        ("🎓 PICT Pune ENTC (CGPA 8.38)", "#bf5af2")
    ]
    
    pill_x = start_x
    pill_y = 138
    
    for text, color in pills:
        text_len = len(text)
        pill_w = text_len * 7.2 + 22
        
        svg.append(f'<g>')
        svg.append(f'  <rect x="{pill_x}" y="{pill_y}" width="{pill_w}" height="{28}" class="pill-bg" />')
        svg.append(f'  <circle cx="{pill_x + 12}" cy="{pill_y + 14}" r="4" fill="{color}" />')
        svg.append(f'  <text x="{pill_x + 22}" y="{pill_y + 18}" class="pill-text">{text}</text>')
        svg.append(f'</g>')
        
        pill_x += pill_w + 12
        
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Apple Header SVG created at {output_path}")

if __name__ == "__main__":
    generate_apple_header_svg("apple-header.svg")

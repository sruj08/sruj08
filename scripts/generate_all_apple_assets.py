import os
import json

def make_apple_section_header(title, output_path):
    svg_width = 860
    svg_height = 42
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg.append('<defs>')
    svg.append('  <linearGradient id="secGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('    <stop offset="0%" stop-color="#161b22" />')
    svg.append('    <stop offset="100%" stop-color="#0d1117" />')
    svg.append('  </linearGradient>')
    svg.append('</defs>')
    
    svg.append('<style>')
    svg.append('  .bg { fill: url(#secGrad); rx: 10px; ry: 10px; stroke: #30363d; stroke-width: 1px; }')
    svg.append('  .title { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", sans-serif; font-size: 15px; font-weight: 700; fill: #f0f6fc; letter-spacing: -0.2px; }')
    svg.append('  .accent-bar { fill: #2997ff; rx: 2px; ry: 2px; }')
    svg.append('</style>')
    
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="bg" />')
    svg.append(f'<rect x="14" y="11" width="4" height="20" class="accent-bar" />')
    svg.append(f'<text x="28" y="26" class="title">{title}</text>')
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Section Header SVG created at {output_path}")

def make_apple_header_banner(output_path="apple-banner-header.svg"):
    svg_width = 860
    svg_height = 190
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg.append('<defs>')
    svg.append('  <linearGradient id="bannerBg" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#161b22" />')
    svg.append('    <stop offset="100%" stop-color="#0d1117" />')
    svg.append('  </linearGradient>')
    svg.append('  <linearGradient id="topLine" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('    <stop offset="0%" stop-color="#2997ff" />')
    svg.append('    <stop offset="50%" stop-color="#a155b9" />')
    svg.append('    <stop offset="100%" stop-color="#30d158" />')
    svg.append('  </linearGradient>')
    svg.append('</defs>')
    
    svg.append('<style>')
    svg.append('  .card { fill: url(#bannerBg); rx: 16px; ry: 16px; stroke: #30363d; stroke-width: 1.2px; }')
    svg.append('  .name { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif; font-size: 36px; font-weight: 700; fill: #f0f6fc; letter-spacing: -0.6px; }')
    svg.append('  .subtitle { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 15px; font-weight: 500; fill: #2997ff; }')
    svg.append('  .desc { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 13.5px; fill: #8b949e; }')
    svg.append('  .badge-bg { rx: 10px; ry: 10px; fill: #21262d; stroke: #363b42; stroke-width: 1px; }')
    svg.append('  .badge-text { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", monospace; font-size: 11px; font-weight: 600; fill: #e6edf3; }')
    svg.append('</style>')
    
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="card" />')
    svg.append(f'<path d="M 0 16 A 16 16 0 0 1 16 0 L {svg_width - 16} 0 A 16 16 0 0 1 {svg_width} 16 L {svg_width} 4 L 0 4 Z" fill="url(#topLine)" opacity="0.95" />')
    
    start_x = 36
    svg.append(f'<text x="{start_x}" y="56" class="name">Srujan Satav</text>')
    svg.append(f'<text x="{start_x}" y="82" class="subtitle">Co-Founder @ Novaryn Technologies  •  Partner @ MindstriX  •  PICT Pune \'26</text>')
    svg.append(f'<text x="{start_x}" y="108" class="desc">Systems Architect &amp; Forward Deployed Engineer grounded in Go, AI/ML Pipelines &amp; Web3.</text>')
    
    badges = [
        ("🏆 Pune Agri 15L Runner-Up", "#ffd60a"),
        ("🥇 TechFiesta '26 Global #1", "#30d158"),
        ("🥇 VOIS 2.0 National Winner", "#2997ff"),
        ("🎓 PICT Pune ENTC (CGPA 8.38)", "#bf5af2")
    ]
    
    bx = start_x
    by = 132
    for text, col in badges:
        bw = len(text) * 7.2 + 22
        svg.append(f'<g>')
        svg.append(f'  <rect x="{bx}" y="{by}" width="{bw}" height="{26}" class="badge-bg" />')
        svg.append(f'  <circle cx="{bx + 11}" cy="{by + 13}" r="3.5" fill="{col}" />')
        svg.append(f'  <text x="{bx + 20}" y="{by + 17}" class="badge-text">{text}</text>')
        svg.append(f'</g>')
        bx += bw + 10
        
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Header Banner SVG created at {output_path}")

def main():
    make_apple_header_banner("apple-banner-header.svg")
    make_apple_section_header("About Srujan Satav", "apple-section-about.svg")
    make_apple_section_header("Major Competition Victories & Honors", "apple-section-achievements.svg")
    make_apple_section_header("Technical Stack & Engineering Skills", "apple-section-techstack.svg")
    make_apple_section_header("Featured Systems & Production Codebases", "apple-section-projects.svg")
    make_apple_section_header("Industry Experience & Leadership", "apple-section-experience.svg")
    make_apple_section_header("GitHub Activity & Continuous Commit Flow", "apple-section-stats.svg")

if __name__ == "__main__":
    main()

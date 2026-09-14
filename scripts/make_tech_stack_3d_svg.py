import os

def generate_tech_stack_3d_svg(output_path="tech-stack-3d.svg"):
    svg_width = 860
    svg_height = 250
    
    categories = [
        {
            "category": "⚡ Languages & Core",
            "color": "#58a6ff",
            "skills": ["Golang", "C++", "C", "Java", "Python", "Solidity", "JavaScript", "TypeScript"]
        },
        {
            "category": "🚀 Backend, Cloud & Architecture",
            "color": "#38d430",
            "skills": ["Go Microservices", "REST APIs", "ExpressJS", "Firebase", "Docker", "GCP", "System Design", "DSA"]
        },
        {
            "category": "🧠 AI / ML, Computer Vision & RAG",
            "color": "#e3b341",
            "skills": ["LLMs", "RAG Pipeline", "LangChain", "YOLOv8", "OpenCV", "CNN", "Supervised Learning"]
        },
        {
            "category": "🔗 Web3 & Blockchain Development",
            "color": "#d2a8ff",
            "skills": ["Solidity", "Smart Contracts", "ERC-20", "OpenZeppelin", "MetaMask", "Sepolia", "Remix"]
        }
    ]
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    
    # 3D Filters
    svg.append('<defs>')
    svg.append('  <filter id="pillShadow" x="-10%" y="-10%" width="120%" height="120%">')
    svg.append('    <feDropShadow dx="0" dy="3" stdDeviation="2" flood-color="#000000" flood-opacity="0.5" />')
    svg.append('  </filter>')
    svg.append('</defs>')
    
    svg.append('<style>')
    svg.append('  .bg { fill: #0d1117; rx: 10px; ry: 10px; stroke: #30363d; stroke-width: 1px; }')
    svg.append('  .title-bar { fill: #161b22; rx: 10px; ry: 10px; }')
    svg.append('  .header-title { font-family: monospace; font-size: 11px; font-weight: bold; fill: #8b949e; }')
    svg.append('  .cat-title { font-family: "Fira Code", monospace; font-size: 12px; font-weight: bold; }')
    svg.append('  .pill-bg { rx: 12px; ry: 12px; fill: #161b22; stroke: #30363d; stroke-width: 1px; filter: url(#pillShadow); transition: all 0.2s; }')
    svg.append('  .pill-text { font-family: "Fira Code", monospace; font-size: 11px; fill: #c9d1d9; }')
    svg.append('</style>')
    
    # Outer terminal container
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="bg" />')
    
    # Terminal header bar
    svg.append(f'<path d="M 0 8 A 8 8 0 0 1 8 0 L {svg_width - 8} 0 A 8 8 0 0 1 {svg_width} 8 L {svg_width} 28 L 0 28 Z" class="title-bar" stroke="#30363d" stroke-width="1" />')
    svg.append('<circle cx="15" cy="14" r="4" fill="#ff5f56" />')
    svg.append('<circle cx="27" cy="14" r="4" fill="#ffbd2e" />')
    svg.append('<circle cx="39" cy="14" r="4" fill="#27c93f" />')
    svg.append(f'<text x="{svg_width/2}" y="18" text-anchor="middle" class="header-title">sruj08@github ~ $ ./tech_stack.sh --3d-grid</text>')
    
    start_y = 44
    cat_height = 48
    
    for idx, cat in enumerate(categories):
        y = start_y + idx * cat_height
        
        # Category header
        svg.append(f'<text x="20" y="{y + 16}" class="cat-title" fill="{cat["color"]}">{cat["category"]}</text>')
        
        # Skills 3D pills
        curr_x = 220
        for skill in cat["skills"]:
            # Calculate pill width based on text length
            pill_w = len(skill) * 7.5 + 20
            if curr_x + pill_w > svg_width - 20:
                break
                
            svg.append(f'<g class="pill-group">')
            svg.append(f'  <rect x="{curr_x}" y="{y + 2}" width="{pill_w}" height="{22}" class="pill-bg" />')
            svg.append(f'  <text x="{curr_x + pill_w/2}" y="{y + 16}" text-anchor="middle" class="pill-text">{skill}</text>')
            svg.append('</g>')
            
            curr_x += pill_w + 10
            
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"3D Tech Stack SVG created at {output_path}")

if __name__ == "__main__":
    generate_tech_stack_3d_svg("tech-stack-3d.svg")

import os

def generate_apple_tech_stack_svg(output_path="apple-tech-stack.svg"):
    svg_width = 860
    svg_height = 230
    
    categories = [
        {
            "category": "⚡ Languages & Core",
            "accent": "#2997ff",
            "skills": ["Golang", "C++", "C", "Java", "Python", "Solidity", "JavaScript", "TypeScript"]
        },
        {
            "category": "🚀 Backend & Systems",
            "accent": "#30d158",
            "skills": ["Go Microservices", "REST APIs", "ExpressJS", "Firebase", "Docker", "GCP", "System Design", "DSA"]
        },
        {
            "category": "🧠 AI / ML & Vision",
            "accent": "#ffd60a",
            "skills": ["LLMs", "RAG Pipeline", "LangChain", "YOLOv8", "OpenCV", "CNN", "Supervised Learning"]
        },
        {
            "category": "🔗 Web3 & Blockchain",
            "accent": "#bf5af2",
            "skills": ["Solidity", "Smart Contracts", "ERC-20", "OpenZeppelin", "MetaMask", "Sepolia", "Remix"]
        }
    ]
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    
    svg.append('<style>')
    svg.append('  .outer-card { fill: #0d1117; rx: 16px; ry: 16px; stroke: #30363d; stroke-width: 1.2px; }')
    svg.append('  .section-title { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif; font-size: 15px; font-weight: 700; fill: #f0f6fc; }')
    svg.append('  .cat-title { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 12px; font-weight: 600; }')
    svg.append('  .pill-bg { rx: 10px; ry: 10px; fill: #161b22; stroke: #30363d; stroke-width: 1px; }')
    svg.append('  .pill-text { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", monospace; font-size: 11px; fill: #e6edf3; }')
    svg.append('</style>')
    
    # Outer Container
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="outer-card" />')
    
    # Header Title
    svg.append(f'<text x="24" y="32" class="section-title">💻 Technical Stack &amp; Engineering Skills</text>')
    
    start_y = 44
    cat_gap = 43
    
    for idx, cat in enumerate(categories):
        y = start_y + idx * cat_gap
        
        # Category label
        svg.append(f'<text x="24" y="{y + 16}" class="cat-title" fill="{cat["accent"]}">{cat["category"]}</text>')
        
        # Skills pills
        curr_x = 220
        for skill in cat["skills"]:
            pill_w = len(skill) * 7.2 + 20
            if curr_x + pill_w > svg_width - 24:
                break
                
            svg.append(f'<g>')
            svg.append(f'  <rect x="{curr_x}" y="{y + 2}" width="{pill_w}" height="{22}" class="pill-bg" />')
            svg.append(f'  <text x="{curr_x + pill_w/2}" y="{y + 16}" text-anchor="middle" class="pill-text">{skill}</text>')
            svg.append('</g>')
            
            curr_x += pill_w + 10
            
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Apple Tech Stack SVG created at {output_path}")

if __name__ == "__main__":
    generate_apple_tech_stack_svg("apple-tech-stack.svg")

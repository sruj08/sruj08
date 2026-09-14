import os
import xml.etree.ElementTree as ET

BG_COLOR = "#050505" # Tactical Obsidian
BORDER_COLOR = "#1f1f1f" # Hairline Divider
CARD_BG = "transparent" # No bulky cards
HEADER_COLOR = "#FF6B00" # Tactical Orange
TEXT_COLOR = "#f4f5f7" # Signature Off-White
MUTED_TEXT = "#7d8a9e" # Muted Slate-Gray
ICON_BG = "transparent" # No bubbly icons

BRAND_COLORS = {
    "python": "#3776AB",
    "langchain": "#1C3C3C",
    "gemini": "#8E75B2",
    "javascript": "#F7DF1E",
    "typescript": "#3178C6",
    "solidity": "#6B7280",
    "ethereum": "#3C3C3D",
    "go": "#00ADD8",
    "docker": "#2496ED"
}

def extract_path_data(svg_file):
    if not os.path.exists(svg_file):
        return ""
    try:
        tree = ET.parse(svg_file)
        root = tree.getroot()
        paths = []
        for elem in root.iter():
            tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
            if tag in ["path", "rect", "polygon", "circle"]:
                attribs = []
                for k, v in elem.attrib.items():
                    attribs.append(f'{k}="{v}"')
                paths.append(f'<{tag} {" ".join(attribs)} />')
        return "".join(paths)
    except Exception as e:
        print(f"Error parsing {svg_file}: {e}")
        return ""

def generate_apple_hig_tech_card(output_path="tech-stack.svg"):
    width = 1125
    height = 290
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Official Tech Stack">')
    
    svg.append('  <style>')
    svg.append('    .header-title { font-family: "SF Mono", "Consolas", "Courier New", monospace; font-size: 14px; font-weight: bold; fill: #FF6B00; }')
    svg.append('    .tech-title { font-family: "SF Mono", "Consolas", "Courier New", monospace; font-size: 13px; font-weight: bold; fill: #f4f5f7; }')
    svg.append('    .tech-subtitle { font-family: "SF Mono", "Consolas", "Courier New", monospace; font-size: 11px; fill: #7d8a9e; }')
    svg.append('  </style>')
    
    svg.append('  <defs>')
    svg.append('    <filter id="noise" x="0" y="0" width="100%" height="100%">')
    svg.append('      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/>')
    svg.append('      <feColorMatrix type="matrix" values="1 0 0 0 0, 0 1 0 0 0, 0 0 1 0 0, 0 0 0 0.05 0" />')
    svg.append('    </filter>')
    svg.append('  </defs>')
    
    # Outer Background Box & Noise Texture
    svg.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" fill="{BG_COLOR}" stroke="{BORDER_COLOR}"/>')
    svg.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" fill="transparent" filter="url(#noise)" style="pointer-events: none;" />')
    
    # Header Line
    svg.append(f'  <text x="28" y="38" class="header-title">--- sruj08@core-skills ----------------------------------------------------------------───────────</text>')
    
    items = [
        ("python", "Python", "AI / ML &amp; Distributed Systems"),
        ("langchain", "LangChain", "LLM Orchestration &amp; RAG"),
        ("gemini", "GenAI / Gemini", "Agents &amp; Generative AI"),
        ("javascript", "JavaScript", "Fullstack Web &amp; Node.js"),
        ("typescript", "TypeScript", "Type-Safe Architecture"),
        ("solidity", "Solidity", "EVM &amp; Smart Contracts"),
        ("ethereum", "Web3 / Ethereum", "DeFi &amp; Blockchain"),
        ("go", "Golang", "High-Throughput Services"),
        ("docker", "Docker", "DevOps, GCP &amp; Containers")
    ]
    
    cols = 3
    col_width = 352
    row_height = 68
    start_x = 34
    start_y = 60
    
    for idx, (key, title, subtitle) in enumerate(items):
        col = idx % cols
        row = idx // cols
        
        x = start_x + col * col_width
        y = start_y + row * row_height
        
        svg_file = os.path.join("assets/logos", f"{key}.svg")
        path_data = extract_path_data(svg_file)
        brand_color = BRAND_COLORS.get(key, "#00C853")
        
        svg.append(f'  <g>')
        
        # Subtle framing instead of glassmorphism
        svg.append(f'    <rect x="{x}" y="{y}" width="332" height="58" fill="none" stroke="{BORDER_COLOR}" stroke-width="1"/>')
        svg.append(f'    <rect x="{x}" y="{y}" width="3" height="58" fill="{brand_color}" />')
        
        # Embedded Downloaded Official SimpleIcons SVG
        svg.append(f'    <g transform="translate({x + 18}, {y + 17})" fill="{brand_color}">')
        svg.append(f'      <svg width="24" height="24" viewBox="0 0 24 24" fill="{brand_color}">{path_data}</svg>')
        svg.append(f'    </g>')
        
        # Title & Subtitle
        svg.append(f'    <text x="{x + 60}" y="{y + 27}" class="tech-title" xml:space="preserve">{title}</text>')
        svg.append(f'    <text x="{x + 60}" y="{y + 43}" class="tech-subtitle" xml:space="preserve">{subtitle}</text>')
        svg.append('  </g>')
        
    svg.append('</svg>')
    
    content = "\n".join(svg)
    ET.fromstring(content)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Static Minimalist Apple HIG Tech Stack Card VALIDATED & CREATED at {output_path}")

if __name__ == "__main__":
    generate_apple_hig_tech_card()

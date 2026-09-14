import os
import xml.etree.ElementTree as ET

BG_COLOR = "#040404" # Industrial Black
BORDER_COLOR = "#1a1a1a" # Hairline Divider
GRID_COLOR = "#0f0f0f" # CAD Blueprint Grid
CARD_BG = "transparent" # No bulky cards
ACCENT_COLOR = "#FFB000" # Bloomberg Amber
TEXT_COLOR = "#e0e0e0" # Terminal Off-White
MUTED_TEXT = "#666666" # Subdued Data Gray
ICON_BG = "transparent" # No bubbly icons

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
    
    svg.append('  <defs>')
    svg.append('    <filter id="noise" x="0" y="0" width="100%" height="100%">')
    svg.append('      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/>')
    svg.append('      <feColorMatrix type="matrix" values="1 0 0 0 0, 0 1 0 0 0, 0 0 1 0 0, 0 0 0 0.05 0" />')
    svg.append('    </filter>')
    svg.append('  </defs>')
    
    # Outer Background Box & Noise Texture
    svg.append(f'  <rect x="0" y="0" width="{width}" height="{height}" rx="0" fill="{BG_COLOR}" />')
    
    # Render CAD Grid (0.5px offset for sharp rendering)
    svg.append(f'  <g stroke="{GRID_COLOR}" stroke-width="1">')
    for y in range(0, height, 20):
        svg.append(f'    <line x1="0" y1="{y + 0.5}" x2="{width}" y2="{y + 0.5}" />')
    for x in range(0, width, 20):
        svg.append(f'    <line x1="{x + 0.5}" y1="0" x2="{x + 0.5}" y2="{height}" />')
    svg.append('  </g>')
    
    svg.append(f'  <rect x="0" y="0" width="{width}" height="{height}" fill="transparent" filter="url(#noise)" style="pointer-events: none;" />')
    svg.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" fill="none" stroke="{BORDER_COLOR}" />')
    
    # Header Line
    svg.append(f'  <text x="28" y="38" font-family="Fira Code, SF Mono, Consolas, Courier New, monospace" font-size="14px" font-weight="bold" fill="{ACCENT_COLOR}">--- sruj08@core-skills ---------------------------------------------------------------------------</text>')
    
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
        
        svg.append(f'  <g>')
        
        # Subtle framing (0.5 offset)
        svg.append(f'    <rect x="{x + 0.5}" y="{y + 0.5}" width="332" height="58" fill="none" stroke="{BORDER_COLOR}" stroke-width="1"/>')
        svg.append(f'    <rect x="{x}" y="{y}" width="3" height="58" fill="{ACCENT_COLOR}" />')
        
        # Embedded Downloaded Official SimpleIcons SVG - MONOCHROMATIC
        svg.append(f'    <g transform="translate({x + 18}, {y + 17})" fill="{ACCENT_COLOR}">')
        svg.append(f'      <svg width="24" height="24" viewBox="0 0 24 24" fill="{ACCENT_COLOR}">{path_data}</svg>')
        svg.append(f'    </g>')
        
        # Title & Subtitle with dominant-baseline="middle"
        svg.append(f'    <text x="{x + 60}" y="{y + 24}" font-family="Fira Code, SF Mono, Consolas, Courier New, monospace" font-size="13px" font-weight="bold" fill="{TEXT_COLOR}" text-transform="uppercase" dominant-baseline="middle" xml:space="preserve">{title}</text>')
        svg.append(f'    <text x="{x + 60}" y="{y + 40}" font-family="Fira Code, SF Mono, Consolas, Courier New, monospace" font-size="11px" fill="{MUTED_TEXT}" text-transform="uppercase" dominant-baseline="middle" xml:space="preserve">{subtitle}</text>')
        svg.append('  </g>')
        
    svg.append('</svg>')
    
    content = "\n".join(svg)
    ET.fromstring(content)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Static Minimalist Apple HIG Tech Stack Card VALIDATED & CREATED at {output_path}")

if __name__ == "__main__":
    generate_apple_hig_tech_card()

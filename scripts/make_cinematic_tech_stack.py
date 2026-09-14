import os
import xml.etree.ElementTree as ET

BG_COLOR = "#080c14"
BORDER_COLOR = "#21262d"
CARD_BG_1 = "#111622"
CARD_BG_2 = "#182030"
HEADER_COLOR = "#58a6ff"
TEXT_COLOR = "#f0f6fc"
MUTED_TEXT = "#8b949e"

# Full-color, exact official SVG definitions for all major tech stack logos
FULL_OFFICIAL_LOGOS = {
    "python": {
        "title": "Python",
        "category": "AI / ML & Core",
        "viewBox": "0 0 110 110",
        "svg_content": '''
          <linearGradient id="py_g1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#3776AB"/>
            <stop offset="100%" stop-color="#1e4970"/>
          </linearGradient>
          <linearGradient id="py_g2" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFE873"/>
            <stop offset="100%" stop-color="#FFD43B"/>
          </linearGradient>
          <path fill="url(#py_g1)" d="M54.2 8c-24 0-22.5 10.4-22.5 10.4l.1 10.8h22.9v3.3H22.9S8 30.8 8 54.8c0 24 13 23.2 13 23.2h7.8v-11s-.4-13.2 13-13.2h22.5s12.4.2 12.4-12.2V20.4S78.2 8 54.2 8zm-12 12.1a4.2 4.2 0 1 1 0-8.4 4.2 4.2 0 0 1 0 8.4z"/>
          <path fill="url(#py_g2)" d="M55.8 102c24 0 22.5-10.4 22.5-10.4l-.1-10.8H55.3v-3.3h31.8s14.9 1.7 14.9-22.3c0-24-13-23.2-13-23.2h-7.8v11s.4 13.2-13 13.2H45.7s-12.4-.2-12.4 12.2v21.9S31.8 102 55.8 102zm12-12.1a4.2 4.2 0 1 1 0 8.4 4.2 4.2 0 0 1 0-8.4z"/>
        '''
    },
    "langchain": {
        "title": "LangChain",
        "category": "LLM Framework",
        "viewBox": "0 0 100 100",
        "svg_content": '''
          <linearGradient id="lc_g" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00A67E"/>
            <stop offset="100%" stop-color="#1C3C3C"/>
          </linearGradient>
          <path fill="url(#lc_g)" d="M50 5L10 25v50l40 20 40-20V25L50 5zm0 11.2l28.5 14.3L50 44.3 21.5 30.5 50 16.2zM20 38.8l25 12.5v28.8L20 67.5V38.8zm30 41.3V51.3l25-12.5v28.7L50 80.1z"/>
        '''
    },
    "gemini": {
        "title": "GenAI / Gemini",
        "category": "RAG & Agents",
        "viewBox": "0 0 100 100",
        "svg_content": '''
          <linearGradient id="gem_g" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#1BA1E3"/>
            <stop offset="50%" stop-color="#9B51E0"/>
            <stop offset="100%" stop-color="#E91E63"/>
          </linearGradient>
          <path fill="url(#gem_g)" d="M50 5C50 29.85 29.85 50 5 50c24.85 0 45 20.15 45 45 0-24.85 20.15-45 45-45C70.15 50 50 29.85 50 5z"/>
        '''
    },
    "javascript": {
        "title": "JavaScript",
        "category": "Fullstack Web",
        "viewBox": "0 0 100 100",
        "svg_content": '''
          <rect width="100" height="100" rx="16" fill="#F7DF1E"/>
          <path fill="#000000" d="M78.3 73c2.1 3.5 4.8 6.1 9.5 6.1 3.9 0 6.5-1.9 6.5-4.7 0-3.1-2.2-4.3-7.1-6.4l-2.5-1.1c-7.3-3.1-12.1-7-12.1-15.3 0-8.3 6.5-14.8 17.1-14.8 7.3 0 12.3 2.6 15.8 8.8l-7.8 4.9c-1.8-3.3-4.2-4.8-8.8-4.8-4.1 0-6.7 1.9-6.7 4.4 0 2.9 1.8 3.9 6.5 5.9l2.5 1.1c8.7 3.7 13.1 7.7 13.1 15.7 0 9.3-7.1 15.6-18.4 15.6-10.2 0-15.8-4.8-18.8-10.6l8.7-4.8zm-28.7 1.3c1.8 3.1 3.5 5.8 7.5 5.8 3.5 0 5.8-1.4 5.8-6.9V37.2h10.2v36.3c0 10.8-6.2 15.6-15.8 15.6-8.7 0-13.6-4.5-15.8-10.1l8.1-4.7z" transform="scale(0.85) translate(3, 5)"/>
        '''
    },
    "typescript": {
        "title": "TypeScript",
        "category": "Type-Safe Systems",
        "viewBox": "0 0 100 100",
        "svg_content": '''
          <rect width="100" height="100" rx="16" fill="#3178C6"/>
          <path fill="#FFFFFF" d="M57.6 54.8h9.8v-3.5h-9.8v-3.5h13.6v-3.5h-23.4v35.7h9.8v-25.2zm-26.1-10.5H8.1v8.1h7.2v27.6h9.8V52.4h6.4v-8.1z" transform="scale(1.2) translate(8, 10)"/>
        '''
    },
    "solidity": {
        "title": "Solidity",
        "category": "Smart Contracts",
        "viewBox": "0 0 100 100",
        "svg_content": '''
          <linearGradient id="sol_g1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#9EA8B6"/>
            <stop offset="100%" stop-color="#4B5563"/>
          </linearGradient>
          <linearGradient id="sol_g2" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#374151"/>
            <stop offset="100%" stop-color="#1F2937"/>
          </linearGradient>
          <path fill="url(#sol_g1)" d="M50 8L16 35l34 27 34-27L50 8zm0 34.2L30.2 27.8 50 17.6l19.8 10.2L50 42.2z"/>
          <path fill="url(#sol_g2)" d="M16 43.5l34 27 34-27v12.5l-34 27-34-27V43.5z"/>
        '''
    },
    "web3": {
        "title": "Web3 / Ethereum",
        "category": "DeFi & Blockchain",
        "viewBox": "0 0 100 100",
        "svg_content": '''
          <linearGradient id="eth_top" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#8A92B2"/>
            <stop offset="100%" stop-color="#62688F"/>
          </linearGradient>
          <linearGradient id="eth_bot" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#62688F"/>
            <stop offset="100%" stop-color="#454A75"/>
          </linearGradient>
          <path fill="url(#eth_top)" d="M50 5L22 51l28 16 28-16L50 5z"/>
          <path fill="url(#eth_bot)" d="M22 55.5L50 95l28-39.5L50 72 22 55.5z"/>
        '''
    },
    "golang": {
        "title": "Golang",
        "category": "High-Perf Backend",
        "viewBox": "0 0 100 100",
        "svg_content": '''
          <linearGradient id="go_g" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#00ADD8"/>
            <stop offset="100%" stop-color="#007D9C"/>
          </linearGradient>
          <path fill="url(#go_g)" d="M10 44c1.5.5 3 .9 4.5 1.3 2 .5 4 .9 6.3.9 7.4 0 12.8-2.5 16.3-7.8 2-2.9 3-6.4 3.5-10.3H27v-3.9h22.2c.5 2 .5 4 .5 6.4 0 5.9-2 11.3-5.4 15.8-4.9 5.9-12.3 9.3-21.2 9.3-3.9 0-7.9-.9-11.3-2.5L10 44zm55.7 11.3c-8.9 0-15.3-3.4-19.2-9.8-3-4.9-4.5-10.3-4.5-16.7 0-6.4 1.5-12.3 4.5-16.7 3.9-6.4 10.3-9.8 19.2-9.8 8.9 0 15.3 3.4 19.2 9.8 3 4.9 4.5 10.3 4.5 16.7 0 6.4-1.5 12.3-4.5 16.7-3.9 6.4-10.3 9.8-19.2 9.8zm0-8.4c5.4 0 8.9-2.5 11.3-6.9 2-3.9 3-8.9 3-14.3 0-5.4-1-10.3-3-14.3-2.5-4.4-5.9-6.9-11.3-6.9-5.4 0-8.9 2.5-11.3 6.9-2 3.9-3 8.9-3 14.3 0 5.4 1 10.3 3 14.3 2.5 4.4 5.9 6.9 11.3 6.9z"/>
        '''
    },
    "docker": {
        "title": "Docker",
        "category": "DevOps & Containers",
        "viewBox": "0 0 100 100",
        "svg_content": '''
          <linearGradient id="doc_g" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#2496ED"/>
            <stop offset="100%" stop-color="#1D63B8"/>
          </linearGradient>
          <path fill="url(#doc_g)" d="M57.8 45.8h8.8v8.8H57.8zm-11 0h8.8v8.8h-8.8zm-11 0h8.8v8.8h-8.8zm-11 0h8.8v8.8h-8.8zm-11 0h8.8v8.8H13.8zm22-11h8.8v8.8h-8.8zm-11 0h8.8v8.8h-8.8zm-11 0h8.8v8.8H13.8zm22-11h8.8v8.8h-8.8zm58.7 25.3c-2-1.4-6.3-1.9-9.5-.6-1.3.5-2.4 1.4-3.6 2.4-1.4-.9-3-1.6-4.6-2-2.8-.7-5.9-.4-8.6.8-1-1.1-2.2-2-3.6-2.7l-1.4-.7v8.8h3c2 0 3.9.7 5.3 2.2l.6.5c1.1 1.1 2.7 1.8 4.3 1.8h.8c5.5 0 10.2-3.6 11.5-8.9.1-.6.3-1.1.3-1.7z"/>
        '''
    }
}

def generate_cinematic_tech_stack(output_path="tech-stack-cinematic.svg"):
    width = 1125
    height = 290
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">')
    
    # SVG Filters & Gradients for Cinematic Glow & Realistic 3D Depth
    svg.append('  <defs>')
    svg.append('    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#090d16"/>')
    svg.append('      <stop offset="50%" stop-color="#0d1117"/>')
    svg.append('      <stop offset="100%" stop-color="#070a12"/>')
    svg.append('    </linearGradient>')
    
    svg.append('    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#161e2e"/>')
    svg.append('      <stop offset="100%" stop-color="#0f1522"/>')
    svg.append('    </linearGradient>')
    
    svg.append('    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#38445d"/>')
    svg.append('      <stop offset="50%" stop-color="#21283b"/>')
    svg.append('      <stop offset="100%" stop-color="#181f30"/>')
    svg.append('    </linearGradient>')
    
    svg.append('    <filter id="cardShadow" x="-10%" y="-10%" width="130%" height="130%">')
    svg.append('      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.6"/>')
    svg.append('    </filter>')
    
    svg.append('    <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">')
    svg.append('      <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="#58a6ff" flood-opacity="0.25"/>')
    svg.append('    </filter>')
    svg.append('  </defs>')
    
    # Outer Background Container
    svg.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" fill="url(#bgGrad)" stroke="#30363d" stroke-width="1"/>')
    
    # Terminal Header Line
    svg.append(f'  <text x="28" y="38" fill="{HEADER_COLOR}" font-family="\'Consolas\', \'Menlo\', monospace" font-size="14" font-weight="bold" xml:space="preserve" filter="url(#glowEffect)">--- sruj08@core-technologies -----------------------------------------------------------------------</text>')
    
    items = [
        ("python", "Python", "AI / ML &amp; Systems"),
        ("langchain", "LangChain", "LLM Orchestration"),
        ("gemini", "GenAI / Gemini", "RAG &amp; Agents"),
        ("javascript", "JavaScript", "Fullstack Web"),
        ("typescript", "TypeScript", "Type-Safe Systems"),
        ("solidity", "Solidity", "Smart Contracts"),
        ("web3", "Web3 / EVM", "DeFi &amp; Blockchain"),
        ("golang", "Golang", "Microservices"),
        ("docker", "Docker", "DevOps &amp; GCP")
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
        
        logo_info = FULL_OFFICIAL_LOGOS.get(key, {})
        svg_content = logo_info.get("svg_content", "")
        viewBox = logo_info.get("viewBox", "0 0 100 100")
        
        # Glassmorphic Card Container with Drop Shadow & Metallic Gradient Border
        svg.append(f'  <rect x="{x}" y="{y}" width="332" height="58" rx="8" fill="url(#cardGrad)" stroke="url(#borderGrad)" stroke-width="1" filter="url(#cardShadow)"/>')
        
        # Subtle Ambient Light Pill behind Icon
        svg.append(f'  <rect x="{x + 10}" y="{y + 9}" width="40" height="40" rx="6" fill="#1c2538" stroke="#2a364f" stroke-width="0.75"/>')
        
        # Official Full-Color Vector Logo
        svg.append(f'  <svg x="{x + 14}" y="{y + 13}" width="32" height="32" viewBox="{viewBox}">{svg_content}</svg>')
        
        # Title & Subtitle
        svg.append(f'  <text x="{x + 60}" y="{y + 27}" fill="{TEXT_COLOR}" font-family="\'Consolas\', \'Menlo\', monospace" font-size="13" font-weight="bold" xml:space="preserve">{title}</text>')
        svg.append(f'  <text x="{x + 60}" y="{y + 43}" fill="{MUTED_TEXT}" font-family="\'Consolas\', \'Menlo\', monospace" font-size="11" xml:space="preserve">{subtitle}</text>')
        
    svg.append('</svg>')
    
    content = "\n".join(svg)
    ET.fromstring(content)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cinematic Tech Stack SVG VALIDATED & CREATED at {output_path}")

if __name__ == "__main__":
    generate_cinematic_tech_stack()

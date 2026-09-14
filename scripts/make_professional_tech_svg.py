import os
import xml.etree.ElementTree as ET

BG_COLOR = "#0d1117"
BORDER_COLOR = "#30363d"
CARD_BG = "#161b22"
HEADER_COLOR = "#58a6ff"
TEXT_COLOR = "#f0f6fc"
MUTED_TEXT = "#8b949e"

LOGOS = {
    "python": {
        "name": "Python",
        "path": '<path fill="#3776AB" d="M12 2c-5 0-5.5 2.2-5.5 4.2v2.3h5.7v.8H4.3C2.2 9.3 2 11.8 2 14.5c0 2.8.8 4.5 3.8 4.5h2.2v-2.3c0-2.3 2-4.2 4.3-4.2h5.7V10c0-2-1.7-4.2-6-4.2zm-1.8 2a.9.9 0 1 1 0 1.8.9.9 0 0 1 0-1.8zm11.6 8.3h-2.2v2.3c0 2.3-2 4.2-4.3 4.2H9.6v2.5c0 2 1.7 4.2 6 4.2 5 0 5.5-2.2 5.5-4.2v-2.3h-5.7v-.8h7.9c2.1 0 2.3-2.5 2.3-5.2 0-2.8-.8-4.5-3.8-4.5zm-3.5 11.5a.9.9 0 1 1 0-1.8.9.9 0 0 1 0 1.8z"/>'
    },
    "javascript": {
        "name": "JavaScript",
        "path": '<rect width="24" height="24" rx="3" fill="#F7DF1E"/><path fill="#000" d="M18.8 17.5c.5.8 1.1 1.4 2.2 1.4.9 0 1.5-.4 1.5-1.1 0-.7-.5-1-1.6-1.5l-.6-.2c-1.7-.7-2.8-1.6-2.8-3.5 0-1.9 1.5-3.4 3.9-3.4 1.7 0 2.8.6 3.6 2l-1.4 1c-.4-.8-1-1.1-2.1-1.1-1 0-1.5.4-1.5 1 0 .7.4.9 1.5 1.4l.6.2c2 1 3 1.8 3 3.6 0 2.1-1.6 3.6-4.2 3.6-2.3 0-3.6-1.1-4.3-2.4l1.8-1zm-6.6.3c.4.7.8 1.3 1.7 1.3.8 0 1.3-.3 1.3-1.6V9.3h2.3v8.3c0 2.5-1.4 3.6-3.6 3.6-2 0-3.1-1-3.6-2.3l1.9-1.1z"/>'
    },
    "typescript": {
        "name": "TypeScript",
        "path": '<rect width="24" height="24" rx="3" fill="#3178C6"/><path fill="#FFF" d="M13.5 12.8h2.3v-.8h-2.3v-.8h3.2V9.3h-5.5v8.3h2.3v-4.8zm-6.1-3.5H1.9v1.9h1.7V17.6h2.3v-5.9h1.5V9.3z"/>'
    },
    "solidity": {
        "name": "Solidity",
        "path": '<path fill="#6B7280" d="M12 2L4 8.5l8 6.5 8-6.5L12 2zm0 8.2L7.3 6.8 12 4.4l4.7 2.4L12 10.2zM4 10.5l8 6.5 8-6.5v3l-8 6.5-8-6.5v-3z"/>'
    },
    "web3": {
        "name": "Web3 / Ethereum",
        "path": '<path fill="#8A92B2" d="M11.999 0l-6.62 11.022L12 14.937l6.62-3.915L11.999 0zM5.379 12.012l6.62 9.18 6.622-9.18-6.622 3.914-6.62-3.914z"/>'
    },
    "golang": {
        "name": "Golang",
        "path": '<path fill="#00ADD8" d="M1.8 10.5c.3.1.6.2.9.3.4.1.8.2 1.3.2 1.5 0 2.6-.5 3.3-1.6.4-.6.6-1.3.7-2.1H5.4v-.8h4.5c.1.4.1.8.1 1.3 0 1.2-.4 2.3-1.1 3.2-1 1.2-2.5 1.9-4.3 1.9-.8 0-1.6-.2-2.3-.5L1.8 10.5zm11.5 2.3c-1.8 0-3.1-.7-3.9-2-.6-1-.9-2.1-.9-3.4 0-1.3.3-2.5.9-3.4.8-1.3 2.1-2 3.9-2 1.8 0 3.1.7 3.9 2 .6 1 .9 2.1.9 3.4 0 1.3-.3 2.5-.9 3.4-.8 1.3-2.1 2-3.9 2zm0-1.7c1.1 0 1.8-.5 2.3-1.4.4-.8.6-1.8.6-2.9 0-1.1-.2-2.1-.6-2.9-.5-.9-1.2-1.4-2.3-1.4-1.1 0-1.8.5-2.3 1.4-.4.8-.6 1.8-.6 2.9 0 1.1.2 2.1.6 2.9.5.9 1.2 1.4 2.3 1.4z"/>'
    },
    "langchain": {
        "name": "LangChain",
        "path": '<path fill="#1C3C3C" d="M12 2L2 7v10l10 5 10-5V7L12 2zm0 2.2l7.5 3.8-7.5 3.8L4.5 8 12 4.2zm-8 4.8l7.5 3.8v7.5L4 16.5V9zm9.5 11.3v-7.5l7.5-3.8v7.5l-7.5 3.8z"/>'
    },
    "gemini": {
        "name": "GenAI / Gemini",
        "path": '<path fill="#8E75B2" d="M12 2a10 10 0 0 0 10 10 10 10 0 0 0-10 10 10 10 0 0 0-10-10A10 10 0 0 0 12 2z"/>'
    },
    "docker": {
        "name": "Docker",
        "path": '<path fill="#2496ED" d="M13.98 11.08h2.12v2.12h-2.12zm-2.65 0h2.12v2.12h-2.12zm-2.65 0h2.12v2.12h-2.12zm-2.65 0h2.12v2.12H6.03zm-2.65 0h2.12v2.12H3.38zm5.3-2.65h2.12v2.12h-2.12zm-2.65 0h2.12v2.12h-2.12zm-2.65 0h2.12v2.12H3.38zm5.3-2.65h2.12v2.12h-2.12zm14.15 6.09c-.48-.33-1.53-.45-2.28-.15-.3.12-.58.33-.86.58-.33-.21-.71-.38-1.12-.48-.68-.17-1.41-.1-2.07.19-.24-.26-.53-.48-.86-.65l-.33-.16v2.12h.73c.48 0 .93.18 1.28.52l.14.13c.27.27.65.42 1.04.42h.2c1.32 0 2.45-.88 2.76-2.16.03-.13.06-.27.08-.41z"/>'
    }
}

def generate_tech_stack_svg(output_path="tech-stack-professional.svg"):
    width = 1125
    height = 220
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">')
    svg.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" fill="{BG_COLOR}" stroke="{BORDER_COLOR}"/>')
    
    svg.append(f'  <text x="24" y="38" fill="{HEADER_COLOR}" font-family="\'Consolas\', \'Menlo\', monospace" font-size="14" font-weight="bold" xml:space="preserve">--- sruj08@tech-stack ----------------------------------------------------------------───────────</text>')
    
    items = [
        ("python", "Python", "Core &amp; AI/ML"),
        ("langchain", "LangChain", "LLM Orchestration"),
        ("gemini", "GenAI / Gemini", "RAG &amp; Agents"),
        ("javascript", "JavaScript", "Frontend &amp; Fullstack"),
        ("typescript", "TypeScript", "Type-Safe Systems"),
        ("solidity", "Solidity", "Smart Contracts"),
        ("web3", "Web3 / EVM", "DeFi &amp; Blockchain"),
        ("golang", "Golang", "Microservices"),
        ("docker", "Docker", "DevOps &amp; GCP")
    ]
    
    cols = 3
    col_width = 350
    row_height = 50
    start_x = 36
    start_y = 65
    
    for idx, (key, title, subtitle) in enumerate(items):
        col = idx % cols
        row = idx // cols
        
        x = start_x + col * col_width
        y = start_y + row * row_height
        
        logo_info = LOGOS.get(key, {})
        path_data = logo_info.get("path", "")
        
        svg.append(f'  <rect x="{x}" y="{y}" width="330" height="42" rx="6" fill="{CARD_BG}" stroke="{BORDER_COLOR}" stroke-width="0.75"/>')
        svg.append(f'  <g transform="translate({x + 12}, {y + 9})">{path_data}</g>')
        
        svg.append(f'  <text x="{x + 46}" y="{y + 20}" fill="{TEXT_COLOR}" font-family="\'Consolas\', \'Menlo\', monospace" font-size="13" font-weight="bold" xml:space="preserve">{title}</text>')
        svg.append(f'  <text x="{x + 46}" y="{y + 34}" fill="{MUTED_TEXT}" font-family="\'Consolas\', \'Menlo\', monospace" font-size="11" xml:space="preserve">{subtitle}</text>')
        
    svg.append('</svg>')
    
    content = "\n".join(svg)
    ET.fromstring(content)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Professional Tech Stack SVG created at {output_path}")

if __name__ == "__main__":
    generate_tech_stack_svg()

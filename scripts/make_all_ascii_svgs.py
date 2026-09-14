import os
import xml.etree.ElementTree as ET

BG_COLOR = "#0d1117"
BORDER_COLOR = "#30363d"
HEADER_COLOR = "#58a6ff"
TEXT_COLOR = "#c9d1d9"
MUTED_TEXT = "#8b949e"
WHITE_TEXT = "#f0f6fc"

FONT_ATTRS = 'font-family="\'Consolas\', \'Menlo\', \'DejaVu Sans Mono\', monospace" font-size="13" xml:space="preserve"'

def xml_escape(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    out = []
    for char in text:
        if ord(char) > 127:
            out.append(f"&#x{ord(char):x};")
        else:
            out.append(char)
    return "".join(out)

def create_terminal_card(width, height, content_lines, output_path):
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Terminal Card">')
    svg.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" fill="{BG_COLOR}" stroke="{BORDER_COLOR}"/>')
    
    start_y = 34
    line_height = 21
    
    for idx, (text, color, font_weight) in enumerate(content_lines):
        y = start_y + idx * line_height
        weight_attr = ' font-weight="bold"' if font_weight == "bold" else ''
        escaped_text = xml_escape(text)
        svg.append(f'  <text x="24" y="{y}" fill="{color}" {FONT_ATTRS}{weight_attr}>{escaped_text}</text>')
        
    svg.append('</svg>')
    
    content = "\n".join(svg)
    ET.fromstring(content)
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Terminal ASCII SVG VALIDATED & CREATED at {output_path}")

def generate_ascii_about(output_path="ascii-about.svg"):
    lines = [
        ("--- sruj08@about -----------------------------------------------------------------------------------", HEADER_COLOR, "bold"),
        (". Name: ......... Srujan Satav", TEXT_COLOR, "normal"),
        (". Education: .... B.Tech Electronics & Telecommunication Engineering @ PICT Pune '26 (CGPA 8.38)", TEXT_COLOR, "normal"),
        (". Roles: ........ Partner & Systems Architect @ MindstriX", TEXT_COLOR, "normal"),
        (". Location: ..... Pune, Maharashtra, India", TEXT_COLOR, "normal"),
        (". Core Focus: ... Go Microservices, GenAI / LangChain RAG, Web3 & Smart Contracts", TEXT_COLOR, "normal"),
        ("-------------------------------------------------------------------------------------------------", BORDER_COLOR, "normal"),
        (". Philosophy: .. Engineering high-throughput production systems grounded in clean code and speed.", MUTED_TEXT, "normal"),
        (". Competitions: . Felicitated by Chief Minister of Maharashtra for Agri AI Platform (15L Prize)", WHITE_TEXT, "normal"),
        ("                 Global Winner @ TechFiesta '26 International (INR 3.5L+ Pool)", WHITE_TEXT, "normal"),
        ("                 National Winner @ VOIS Innovation Marathon 2.0 (INR 2L Pool)", WHITE_TEXT, "normal"),
        ("                 2nd Runner-Up @ iQOO Hackathon 2026 (INR 50K Prize)", WHITE_TEXT, "normal")
    ]
    create_terminal_card(1125, 290, lines, output_path)

def generate_ascii_achievements(output_path="ascii-achievements.svg"):
    lines = [
        ("--- sruj08@victories -------------------------------------------------------------------------------", HEADER_COLOR, "bold"),
        ("+----------------------------------------+-------------------------------+------------------------+", BORDER_COLOR, "normal"),
        ("| Competition                            | Rank & Prize                  | Scope                  |", HEADER_COLOR, "bold"),
        ("+----------------------------------------+-------------------------------+------------------------+", BORDER_COLOR, "normal"),
        ("| Pune Agri International Hackathon      | [Winner] Runner-Up (INR 15L)  | Govt. of Maharashtra   |", WHITE_TEXT, "normal"),
        ("| TechFiesta '26 International           | [Winner] 1st Rank (INR 3.5L+) | Global (700+ Teams)    |", WHITE_TEXT, "normal"),
        ("| VOIS Innovation Marathon 2.0           | [Winner] National Winner (2L) | National (630+ Teams)  |", WHITE_TEXT, "normal"),
        ("| iQOO Hackathon 2026                    | [Winner] 2nd Runner-Up (50K)  | National (6,500+ Regs) |", WHITE_TEXT, "normal"),
        ("+----------------------------------------+-------------------------------+------------------------+", BORDER_COLOR, "normal"),
        (". Highlights: Presented Agri AI platform to Maharashtra CM, Agriculture & Education Ministers.", MUTED_TEXT, "normal")
    ]
    create_terminal_card(1125, 250, lines, output_path)

def generate_ascii_techstack(output_path="ascii-techstack.svg"):
    lines = [
        ("--- sruj08@skills ----------------------------------------------------------------------------------", HEADER_COLOR, "bold"),
        (". GenAI & AI/ML: . LangChain, GenAI, Python, Gemini API, YOLOv8, OpenCV, PyTorch, TensorFlow", WHITE_TEXT, "bold"),
        (". Web3 & Blockchain Solidity, Web3.js, Smart Contracts, ERC-20, OpenZeppelin, MetaMask, Sepolia", WHITE_TEXT, "bold"),
        (". Languages: ..... JavaScript, TypeScript, Golang, C++, C, Java, Python, Solidity", TEXT_COLOR, "normal"),
        (". Backend & APIs: Go Microservices, REST APIs, FastAPI, ExpressJS, Node.js, Flask", TEXT_COLOR, "normal"),
        (". DevOps & Cloud: Docker, GCP, Firebase, Linux, Git & GitHub Actions, System Design, DSA", MUTED_TEXT, "normal")
    ]
    create_terminal_card(1125, 170, lines, output_path)

def generate_ascii_projects(output_path="ascii-projects.svg"):
    lines = [
        ("--- sruj08@codebases -------------------------------------------------------------------------------", HEADER_COLOR, "bold"),
        ("[01] CHANAKYA        AI-Powered Regulatory Intelligence Platform for SEBI Hackathon", WHITE_TEXT, "bold"),
        ("     Stack:          Go Microservices * GenAI * RAG * Docker", MUTED_TEXT, "normal"),
        ("-------------------------------------------------------------------------------------------------", BORDER_COLOR, "normal"),
        ("[02] Krishi SahAI    Crop Disease & Pest Advisory Platform with Real-Time Vision", WHITE_TEXT, "bold"),
        ("     Stack:          Flask * LangChain * GenAI * YOLOv8 * React", MUTED_TEXT, "normal"),
        ("-------------------------------------------------------------------------------------------------", BORDER_COLOR, "normal"),
        ("[03] eSurvey         AI-Assisted Digital Agricultural Survey & GIS Land Mapping", WHITE_TEXT, "bold"),
        ("     Stack:          REST APIs * Firebase * GIS Mapping * JavaScript", MUTED_TEXT, "normal"),
        ("-------------------------------------------------------------------------------------------------", BORDER_COLOR, "normal"),
        ("[04] KrishiPrabandh  Enterprise Agricultural Governance & Insurance Claim Intelligence", WHITE_TEXT, "bold"),
        ("     Stack:          Solidity * Web3 * Go * GCP * GenAI", MUTED_TEXT, "normal")
    ]
    create_terminal_card(1125, 290, lines, output_path)

def generate_ascii_experience(output_path="ascii-experience.svg"):
    lines = [
        ("--- sruj08@experience ------------------------------------------------------------------------------", HEADER_COLOR, "bold"),
        ("+----------------------------------------------+------------------------+------------------------+", BORDER_COLOR, "normal"),
        ("| Role                                         | Company                | Duration               |", HEADER_COLOR, "bold"),
        ("+----------------------------------------------+------------------------+------------------------+", BORDER_COLOR, "normal"),
        ("| Partner & AI / Web3 Systems Architect        | MindstriX              | Jan 2026 – Present     |", WHITE_TEXT, "normal"),
        ("| Software Engineer Intern                     | MindstriX              | March 2026 – Present   |", WHITE_TEXT, "normal"),
        ("+----------------------------------------------+------------------------+------------------------+", BORDER_COLOR, "normal")
    ]
    create_terminal_card(1125, 190, lines, output_path)

def main():
    generate_ascii_about("ascii-about.svg")
    # generate_ascii_achievements("ascii-achievements.svg")
    generate_ascii_techstack("ascii-techstack.svg")
    generate_ascii_projects("ascii-projects.svg")
    generate_ascii_experience("ascii-experience.svg")

if __name__ == "__main__":
    main()

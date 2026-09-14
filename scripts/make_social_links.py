import os
import xml.etree.ElementTree as ET

SOCIALS = [
    {"id": "linkedin", "label": "LINKEDIN", "icon": "icons/linkedin.svg", "color": "#0A66C2"},
    {"id": "email", "label": "EMAIL", "icon": "icons/gmail.svg", "color": "#EA4335"},
    {"id": "leetcode", "label": "LEETCODE", "icon": "icons/leetcode.svg", "color": "#FFA116"},
    {"id": "github", "label": "GITHUB", "icon": "icons/github.svg", "color": "#FFFFFF"}
]

def extract_paths(filepath):
    if not os.path.exists(filepath):
        return ""
    try:
        tree = ET.parse(filepath)
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
        print(f"Error parsing {filepath}: {e}")
        return ""

def create_badge():
    os.makedirs("assets/socials", exist_ok=True)
    
    char_width = 7.2
    
    for item in SOCIALS:
        label = f"[ {item['label']} ]"
        text_width = len(label) * char_width
        
        icon_w = 16
        icon_h = 16
        gap = 8
        
        total_width = int(icon_w + gap + text_width)
        height = 20
        
        path_data = extract_paths(item["icon"])
        
        color = item.get("color", "#666666")
        
        svg = []
        svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">')
        
        # Icon
        svg.append(f'  <g transform="translate(0, 2)">')
        svg.append(f'    <svg width="{icon_w}" height="{icon_h}" viewBox="0 0 24 24" fill="{color}">')
        svg.append(f'      {path_data}')
        svg.append(f'    </svg>')
        svg.append(f'  </g>')
        
        # Text
        svg.append(f'  <text x="{icon_w + gap}" y="14" font-family="SF Mono, Consolas, Courier New, monospace" font-size="12px" font-weight="bold" fill="{color}">{label}</text>')
        
        svg.append('</svg>')
        
        out_path = f"assets/socials/{item['id']}.svg"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(svg))
        print(f"Generated {out_path}")

if __name__ == "__main__":
    create_badge()

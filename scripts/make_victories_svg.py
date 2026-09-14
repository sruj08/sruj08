import os
import base64
from io import BytesIO
from PIL import Image, ImageOps
import xml.etree.ElementTree as ET

BG_COLOR = "#0a0b0d" # Deep Slate Charcoal
BORDER_COLOR = "#21252e" # Hairline Divider
ACCENT_GREEN = "#00C853" # Matrix Neon Green
ACCENT_ORANGE = "#FF6B00" # Industrial Orange
TEXT_COLOR = "#f4f5f7" # Signature Off-White
MUTED_TEXT = "#7d8a9e" # Muted Slate-Gray
IMAGE_BORDER = "#333948" # Active Highlight

FILES = [
    "assets/victories/pune_agri.png",
    "assets/victories/techfiesta.png",
    "assets/victories/vois.png",
    "assets/victories/iqoo.png"
]

TITLES = [
    "PUNE AGRI INT. HACKATHON",
    "TECHFIESTA '26 INTERNATIONAL",
    "VOIS INNOVATION MARATHON 2.0",
    "iQOO HACKATHON 2026"
]

RANKS = [
    "Runner-Up",
    "1st Rank",
    "National Winner",
    "2nd Runner-Up"
]

PRIZES = [
    "INR 15L",
    "INR 3.5L+",
    "INR 2L",
    "INR 50K"
]

def image_to_base64(filepath, target_size=(320, 230)):
    if not os.path.exists(filepath):
        return ""
    try:
        with Image.open(filepath) as img:
            img = img.convert("RGB")
            # Crop to aspect ratio then resize
            img = ImageOps.fit(img, target_size, method=Image.Resampling.LANCZOS)
            buffered = BytesIO()
            img.save(buffered, format="JPEG", quality=98)
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            return f"data:image/jpeg;base64,{img_str}"
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")
        return ""

def generate_victories_svg(output_path="victories-grid.svg"):
    width = 1125
    height = 420
    
    # We want 4 columns.
    # Margins: 34 left, 34 right
    # Total available width = 1125 - 68 = 1057
    # 4 columns, 3 gaps. Gap = 20
    # 4 * img_w + 3 * 20 = 1057 => 4 * img_w = 997 => img_w = 249.25 (let's say 248)
    # img_h = img_w * (230/320) = 248 * 0.71875 = 178
    
    img_w = 248
    img_h = 178
    gap = 21
    start_x = 34
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="Hackathon Victories">')
    
    # Fonts & Styles
    svg.append('  <style>')
    svg.append('    .header-text { font-family: "SF Mono", "Consolas", "Menlo", monospace; font-size: 14px; font-weight: bold; fill: #FF6B00; }')
    svg.append('    .title-text { font-family: "SF Pro Display", "Inter", sans-serif; font-size: 13px; font-weight: 800; fill: #f4f5f7; letter-spacing: 0.5px; }')
    svg.append('    .rank-text { font-family: "SF Mono", "Consolas", "Menlo", monospace; font-size: 11px; font-weight: bold; fill: #00C853; }')
    svg.append('    .prize-text { font-family: "SF Mono", "Consolas", "Menlo", monospace; font-size: 11px; fill: #7d8a9e; }')
    svg.append('    .meta-text { font-family: "SF Mono", "Consolas", "Menlo", monospace; font-size: 10px; fill: #7d8a9e; letter-spacing: 1px; }')
    svg.append('  </style>')
    
    svg.append('  <defs>')
    for i in range(4):
        x = start_x + i * (img_w + gap)
        svg.append(f'    <clipPath id="clip-{i}"><rect x="{x}" y="120" width="{img_w}" height="{img_h}" rx="8" ry="8" /></clipPath>')
    svg.append('  </defs>')
    
    # Outer Background Box
    svg.append(f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" fill="{BG_COLOR}" stroke="{BORDER_COLOR}"/>')
    
    # Header Line (matching ASCII aesthetic)
    svg.append(f'  <text x="28" y="38" class="header-text">--- sruj08@victories ----------------------------------------------------------------───────────</text>')
    
    # Hero Headline
    svg.append(f'  <text x="34" y="70" font-size="28" font-family="-apple-system, BlinkMacSystemFont, \'Inter\', sans-serif" font-weight="800" fill="#ffffff" letter-spacing="-0.5">BUILT UNDER PRESSURE. PROVEN IN PUBLIC.</text>')
    svg.append(f'  <text x="34" y="90" class="meta-text" fill="{MUTED_TEXT}">GOVT. OF MAHARASHTRA · GLOBAL / NATIONAL SCALE · 6,500+ REGISTRATIONS</text>')
    
    # Architectural Grid System & Crosshairs
    svg.append(f'  <g stroke="{BORDER_COLOR}" stroke-width="1">')
    for i in range(5):
        cx = start_x - (gap//2) + i * (img_w + gap)
        if i == 0: cx = 0
        if i == 4: cx = width
        # Vertical lines (subtle grid)
        # svg.append(f'    <line x1="{cx}" y1="0" x2="{cx}" y2="{height}" stroke-dasharray="4 4" stroke-opacity="0.5"/>')
    svg.append('  </g>')
    
    meta_tags = ["01 / AGR", "02 / TCF", "03 / VIS", "04 / IQO"]
    
    for i in range(4):
        x = start_x + i * (img_w + gap)
        y = 120
        
        # Meta Tag
        svg.append(f'  <text x="{x}" y="{y - 8}" class="meta-text">{meta_tags[i]}</text>')
        
        # Image
        # Generate at 3x resolution for crisp rendering on Retina displays
        b64 = image_to_base64(FILES[i], target_size=(img_w * 3, img_h * 3))
        if b64:
            svg.append(f'  <image href="{b64}" x="{x}" y="{y}" width="{img_w}" height="{img_h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#clip-{i})" />')
        
        # Image Border
        svg.append(f'  <rect x="{x}" y="{y}" width="{img_w}" height="{img_h}" rx="8" ry="8" fill="none" stroke="{IMAGE_BORDER}" stroke-width="1.5" />')
        
        # Transition Divider
        svg.append(f'  <line x1="{x}" y1="{y + img_h + 20}" x2="{x + img_w}" y2="{y + img_h + 20}" stroke="{IMAGE_BORDER}" stroke-width="1" />')
        svg.append(f'  <line x1="{x}" y1="{y + img_h + 20}" x2="{x + 30}" y2="{y + img_h + 20}" stroke="{ACCENT_GREEN}" stroke-width="2" />')
        
        # Title
        svg.append(f'  <text x="{x}" y="{y + img_h + 45}" class="title-text">{TITLES[i]}</text>')
        
        # Rank & Prize
        svg.append(f'  <text x="{x}" y="{y + img_h + 65}"><tspan class="rank-text">{RANKS[i]}</tspan><tspan class="prize-text"> · {PRIZES[i]}</tspan></text>')
        
        # Crosshairs around images
        ch_len = 5
        ch_color = "#4a5368"
        # Top Left
        svg.append(f'  <path d="M {x-ch_len} {y} L {x+ch_len} {y} M {x} {y-ch_len} L {x} {y+ch_len}" stroke="{ch_color}" stroke-width="1"/>')
        # Top Right
        svg.append(f'  <path d="M {x+img_w-ch_len} {y} L {x+img_w+ch_len} {y} M {x+img_w} {y-ch_len} L {x+img_w} {y+ch_len}" stroke="{ch_color}" stroke-width="1"/>')
        # Bottom Left
        svg.append(f'  <path d="M {x-ch_len} {y+img_h} L {x+ch_len} {y+img_h} M {x} {y+img_h-ch_len} L {x} {y+img_h+ch_len}" stroke="{ch_color}" stroke-width="1"/>')
        # Bottom Right
        svg.append(f'  <path d="M {x+img_w-ch_len} {y+img_h} L {x+img_w+ch_len} {y+img_h} M {x+img_w} {y+img_h-ch_len} L {x+img_w} {y+img_h+ch_len}" stroke="{ch_color}" stroke-width="1"/>')

    svg.append('</svg>')
    
    content = "\n".join(svg)
    ET.fromstring(content)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Victories SVG VALIDATED & CREATED at {output_path}")

if __name__ == "__main__":
    generate_victories_svg()

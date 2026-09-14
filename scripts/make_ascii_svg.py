import os
import sys
from PIL import Image

RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)

def image_to_ascii(image_path, width=96, aspect_ratio_correction=0.55):
    img = Image.open(image_path).convert("L")
    w, h = img.size
    height = int(h / w * width * aspect_ratio_correction)
    img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
    
    try:
        pixels = list(img_resized.get_flattened_data())
    except AttributeError:
        pixels = list(img_resized.getdata())
    num_chars = len(RAMP)
    
    lines = []
    for y in range(height):
        line_chars = []
        for x in range(width):
            pixel_val = pixels[y * width + x]
            # Map 0-255 (dark to bright) -> dark pixels map to dense chars, bright to sparse
            char_idx = int((255 - pixel_val) / 255.0 * (num_chars - 1))
            line_chars.append(RAMP[char_idx])
        lines.append("".join(line_chars))
    return lines

def generate_ascii_svg(lines, output_path="sruj08-ascii.svg"):
    width_chars = len(lines[0]) if lines else 96
    num_rows = len(lines)
    
    font_size = 7
    line_height = 8.5
    char_width = 4.2
    
    svg_width = 370
    svg_height = 490
    
    pad_x = 12
    pad_y = 20
    
    # Calculate row animation timing
    total_duration = 3.5  # seconds for full portrait reveal
    row_delay = total_duration / max(num_rows, 1)
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg.append('<style>')
    svg.append('  .bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    svg.append('  .ascii-text { font-family: "Courier New", Courier, monospace; font-size: 7px; fill: #8b949e; white-space: pre; }')
    svg.append('  .cursor { fill: #39d353; }')
    svg.append('  .title-bar { fill: #161b22; rx: 8px; ry: 8px; }')
    svg.append('  .term-dot { rx: 50%; ry: 50%; }')
    svg.append('</style>')
    
    # Background card
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="bg" />')
    
    # Header bar
    svg.append(f'<path d="M 0 8 A 8 8 0 0 1 8 0 L {svg_width - 8} 0 A 8 8 0 0 1 {svg_width} 8 L {svg_width} 28 L 0 28 Z" fill="#161b22" stroke="#30363d" stroke-width="1" />')
    svg.append('<circle cx="15" cy="14" r="4" fill="#ff5f56" />')
    svg.append('<circle cx="27" cy="14" r="4" fill="#ffbd2e" />')
    svg.append('<circle cx="39" cy="14" r="4" fill="#27c93f" />')
    svg.append(f'<text x="{svg_width/2}" y="18" text-anchor="middle" fill="#8b949e" font-family="monospace" font-size="11" font-weight="bold">sruj08@ascii-art ~</text>')
    
    # ClipPaths for row wipes
    svg.append('<defs>')
    full_row_width = width_chars * char_width + 10
    for i in range(num_rows):
        start_time = i * row_delay
        svg.append(f'  <clipPath id="row-clip-{i}">')
        svg.append(f'    <rect x="{pad_x}" y="{pad_y + 20 + i * line_height}" width="0" height="{line_height}">')
        svg.append(f'      <animate attributeName="width" from="0" to="{full_row_width}" begin="{start_time:.2f}s" dur="{row_delay:.2f}s" fill="freeze" calcMode="linear" />')
        svg.append('    </rect>')
        svg.append('  </clipPath>')
    svg.append('</defs>')
    
    # Render ASCII text lines with row clips
    for i, line in enumerate(lines):
        y_pos = pad_y + 26 + i * line_height
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg.append(f'<g clip-path="url(#row-clip-{i})">')
        svg.append(f'  <text x="{pad_x}" y="{y_pos}" class="ascii-text">{escaped_line}</text>')
        svg.append('</g>')
        
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"ASCII SVG created at {output_path}")

def main():
    prepped_img = "data/source-prepped.png"
    if not os.path.exists(prepped_img):
        print(f"{prepped_img} not found, running prep_photo.py...")
        from prep_photo import prep_photo
        prep_photo()
        
    lines = image_to_ascii(prepped_img, width=82, aspect_ratio_correction=0.52)
    generate_ascii_svg(lines, "sruj08-ascii.svg")

if __name__ == "__main__":
    main()

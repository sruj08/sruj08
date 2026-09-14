import os
import json
from datetime import datetime

# Desaturated max green
PALETTE = ["#040404", "#003b14", "#006d25", "#00a238", "#00c853", "#00e55d"]

def render_heatmap_svg(data_path="data/contributions.json", output_svg="contrib-heatmap.svg"):
    if not os.path.exists(data_path):
        from fetch_contributions import fetch_contributions_data
        data = fetch_contributions_data("sruj08", data_path)
    else:
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
    days = data.get("days", [])
    total_contribs = data.get("total_contributions", 0)
    current_streak = data.get("current_streak", 0)
    longest_streak = data.get("longest_streak", 0)
    
    svg_width = 860
    svg_height = 210
    
    box_size = 11
    box_gap = 3
    step = box_size + box_gap
    
    origin_x = 32
    origin_y = 62
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    
    svg.append('  <defs>')
    svg.append('    <filter id="noise" x="0" y="0" width="100%" height="100%">')
    svg.append('      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/>')
    svg.append('      <feColorMatrix type="matrix" values="1 0 0 0 0, 0 1 0 0 0, 0 0 1 0 0, 0 0 0 0.05 0" />')
    svg.append('    </filter>')
    svg.append('  </defs>')
    
    # Outer terminal box
    svg.append(f'<rect x="0.5" y="0.5" width="{svg_width - 1}" height="{svg_height - 1}" fill="#040404" rx="0" ry="0" stroke="#1a1a1a" stroke-width="1px" />')
    
    # Render CAD Grid (0.5px offset)
    svg.append(f'  <g stroke="#0f0f0f" stroke-width="1">')
    for y in range(0, svg_height, 20):
        svg.append(f'    <line x1="0" y1="{y + 0.5}" x2="{svg_width}" y2="{y + 0.5}" />')
    for x in range(0, svg_width, 20):
        svg.append(f'    <line x1="{x + 0.5}" y1="0" x2="{x + 0.5}" y2="{svg_height}" />')
    svg.append('  </g>')
    
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" fill="transparent" filter="url(#noise)" style="pointer-events: none;" rx="0" ry="0" />')
    
    # Header Line
    svg.append(f'<text x="28" y="38" font-family="Fira Code, SF Mono, Consolas, Courier New, monospace" font-size="14px" font-weight="bold" fill="#FFB000">--- sruj08@contributions ----------------------------------------------------------------------</text>')
    
    weeks = [[] for _ in range(53)]
    for idx, d in enumerate(days):
        week_idx = min(idx // 7, 52)
        weeks[week_idx].append(d)
        
    for w_idx, week in enumerate(weeks):
        x_pos = origin_x + w_idx * step
        for d_idx, day_data in enumerate(week):
            y_pos = origin_y + d_idx * step
            level = day_data.get("level", 0)
            level = min(max(level, 0), len(PALETTE) - 1)
            fill_color = PALETTE[level]
            
            svg.append(f'<rect x="{x_pos + 0.5}" y="{y_pos + 0.5}" width="{box_size}" height="{box_size}" fill="{fill_color}" rx="0" ry="0" opacity="1">')
            svg.append(f'  <title>{day_data.get("count", 0)} contributions on {day_data.get("date", "")}</title>')
            svg.append('</rect>')
            
    # Stats footer along bottom left
    footer_y = origin_y + 7 * step + 22
    stats_str = f"⚡ {total_contribs:,} contributions in the last year | Current Streak: {current_streak} days | Best Streak: {longest_streak} days"
    svg.append(f'<text x="{origin_x}" y="{footer_y}" font-family="Fira Code, SF Mono, Consolas, Courier New, monospace" font-size="11px" font-weight="bold" fill="#00c853" text-transform="uppercase">{stats_str}</text>')
    
    # Legend along bottom right
    legend_x = svg_width - 180
    svg.append(f'<text x="{legend_x - 32}" y="{footer_y}" font-family="Fira Code, SF Mono, Consolas, Courier New, monospace" font-size="10px" fill="#666666" text-transform="uppercase">Less</text>')
    for idx, col in enumerate(PALETTE):
        lx = legend_x + idx * (box_size + 3)
        svg.append(f'<rect x="{lx + 0.5}" y="{footer_y - 9 + 0.5}" width="{box_size}" height="{box_size}" rx="0" fill="{col}" />')
    svg.append(f'<text x="{legend_x + len(PALETTE) * (box_size + 3) + 6}" y="{footer_y}" font-family="Fira Code, SF Mono, Consolas, Courier New, monospace" font-size="10px" fill="#666666" text-transform="uppercase">More</text>')
    
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_svg) or ".", exist_ok=True)
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Heatmap SVG rendered at {output_svg}")

if __name__ == "__main__":
    render_heatmap_svg()

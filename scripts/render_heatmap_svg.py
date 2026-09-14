import os
import json
from datetime import datetime

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

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
    svg.append('<style>')
    svg.append('  .bg { fill: #0d1117; rx: 8px; ry: 8px; stroke: #30363d; stroke-width: 1px; }')
    svg.append('  .title-bar { fill: #161b22; rx: 8px; ry: 8px; }')
    svg.append('  .title { font-family: monospace, Courier; font-size: 11px; font-weight: bold; fill: #8b949e; }')
    svg.append('  .day-rect { rx: 2px; ry: 2px; opacity: 1; }')
    svg.append('  .label { font-family: monospace, Courier; font-size: 10px; fill: #7d8590; }')
    svg.append('  .stats { font-family: monospace, Courier; font-size: 11px; font-weight: bold; fill: #39d353; }')
    svg.append('  .legend-text { font-family: monospace, Courier; font-size: 10px; fill: #7d8590; }')
    svg.append('</style>')
    
    # Outer terminal box
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="bg" />')
    
    # Header bar
    svg.append(f'<path d="M 0 8 A 8 8 0 0 1 8 0 L {svg_width - 8} 0 A 8 8 0 0 1 {svg_width} 8 L {svg_width} 28 L 0 28 Z" fill="#161b22" stroke="#30363d" stroke-width="1" />')
    svg.append('<circle cx="15" cy="14" r="4" fill="#ff5f56" />')
    svg.append('<circle cx="27" cy="14" r="4" fill="#ffbd2e" />')
    svg.append('<circle cx="39" cy="14" r="4" fill="#27c93f" />')
    svg.append(f'<text x="{svg_width/2}" y="18" text-anchor="middle" class="title">sruj08@github ~ $ ./contributions.sh</text>')
    
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
            
            svg.append(f'<rect x="{x_pos}" y="{y_pos}" width="{box_size}" height="{box_size}" fill="{fill_color}" class="day-rect">')
            svg.append(f'  <title>{day_data.get("count", 0)} contributions on {day_data.get("date", "")}</title>')
            svg.append('</rect>')
            
    # Stats footer along bottom left
    footer_y = origin_y + 7 * step + 22
    stats_str = f"⚡ {total_contribs:,} contributions in the last year | Current Streak: {current_streak} days | Best Streak: {longest_streak} days"
    svg.append(f'<text x="{origin_x}" y="{footer_y}" class="stats">{stats_str}</text>')
    
    # Legend along bottom right
    legend_x = svg_width - 180
    svg.append(f'<text x="{legend_x - 32}" y="{footer_y}" class="legend-text">Less</text>')
    for idx, col in enumerate(PALETTE):
        lx = legend_x + idx * (box_size + 3)
        svg.append(f'<rect x="{lx}" y="{footer_y - 9}" width="{box_size}" height="{box_size}" rx="2" fill="{col}" />')
    svg.append(f'<text x="{legend_x + len(PALETTE) * (box_size + 3) + 6}" y="{footer_y}" class="legend-text">More</text>')
    
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_svg) or ".", exist_ok=True)
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Heatmap SVG rendered at {output_svg}")

if __name__ == "__main__":
    render_heatmap_svg()

import os
import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def generate_apple_heatmap_svg(data_path="data/contributions.json", output_svg="apple-heatmap.svg"):
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
    svg_height = 200
    
    box_size = 11
    box_gap = 3
    step = box_size + box_gap
    
    origin_x = 32
    origin_y = 52
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg.append('<style>')
    svg.append('  .outer-card { fill: #0d1117; rx: 16px; ry: 16px; stroke: #30363d; stroke-width: 1.2px; }')
    svg.append('  .section-title { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif; font-size: 15px; font-weight: 700; fill: #f0f6fc; }')
    svg.append('  .day-rect { rx: 2.5px; ry: 2.5px; }')
    svg.append('  .stats { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", monospace; font-size: 11px; font-weight: 600; fill: #30d158; }')
    svg.append('  .legend-text { font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif; font-size: 10px; fill: #8b949e; }')
    svg.append('</style>')
    
    # Outer Container
    svg.append(f'<rect width="{svg_width}" height="{svg_height}" class="outer-card" />')
    
    # Section Title
    svg.append(f'<text x="24" y="32" class="section-title">📊 GitHub Contributions &amp; Continuous Commit Activity</text>')
    
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
            
    # Stats footer
    footer_y = origin_y + 7 * step + 22
    stats_str = f"⚡ {total_contribs:,} contributions in the last year  •  Current Streak: {current_streak} days  •  Best Streak: {longest_streak} days"
    svg.append(f'<text x="{origin_x}" y="{footer_y}" class="stats">{stats_str}</text>')
    
    # Legend
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
    print(f"Apple Heatmap SVG created at {output_svg}")

if __name__ == "__main__":
    generate_apple_heatmap_svg()

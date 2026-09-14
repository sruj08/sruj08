import os
import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#3fb950", "#56d364"]

def generate_animated_heatmap_svg(data_path="data/contributions.json", output_svg="contrib-heatmap.svg"):
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
    
    svg_width = 1125
    svg_height = 250
    
    box_size = 13
    box_gap = 4
    step = box_size + box_gap
    
    origin_x = 36
    origin_y = 65
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}" role="img">')
    svg.append(f'  <rect x="0.5" y="0.5" width="{svg_width - 1}" height="{svg_height - 1}" rx="8" fill="#0d1117" stroke="#30363d"/>')
    
    svg.append('<style>')
    svg.append('  @keyframes pulseGlow {')
    svg.append('    0%, 100% { opacity: 0.85; filter: brightness(1); }')
    svg.append('    50% { opacity: 1; filter: brightness(1.35); }')
    svg.append('  }')
    svg.append('  .day-rect { rx: 2.5px; ry: 2.5px; opacity: 1; }')
    svg.append('  .active-day { animation: pulseGlow 3s infinite ease-in-out; }')
    svg.append('  .header-text { font-family: "Consolas", "Menlo", "DejaVu Sans Mono", monospace; font-size: 14px; font-weight: bold; fill: #58a6ff; }')
    svg.append('  .stats-text { font-family: "Consolas", "Menlo", "DejaVu Sans Mono", monospace; font-size: 12px; fill: #3fb950; font-weight: 600; }')
    svg.append('  .legend-text { font-family: "Consolas", "Menlo", "DejaVu Sans Mono", monospace; font-size: 11px; fill: #8b949e; }')
    svg.append('</style>')
    
    # Section Header
    header_str = f"--- sruj08@contributions ---------------------------------------------------------------------------"
    svg.append(f'<text x="24" y="38" class="header-text">{header_str}</text>')
    
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
            
            # Delay based on column and row for a smooth diagonal wave effect
            delay = (w_idx * 0.05 + d_idx * 0.1) % 3.0
            anim_class = " active-day" if level > 0 else ""
            delay_style = f' style="animation-delay: {delay:.2f}s;"' if level > 0 else ''
            
            escaped_date = day_data.get("date", "")
            count = day_data.get("count", 0)
            
            svg.append(f'<rect x="{x_pos}" y="{y_pos}" width="{box_size}" height="{box_size}" fill="{fill_color}" class="day-rect{anim_class}"{delay_style}>')
            svg.append(f'  <title>{count} contributions on {escaped_date}</title>')
            svg.append('</rect>')
            
    # Stats footer
    footer_y = origin_y + 7 * step + 28
    stats_str = f"Total: {total_contribs:,} commits  |  Current Streak: {current_streak} days  |  Longest Streak: {longest_streak} days"
    svg.append(f'<text x="{origin_x}" y="{footer_y}" class="stats-text">{stats_str}</text>')
    
    # Legend
    legend_x = svg_width - 240
    svg.append(f'<text x="{legend_x - 36}" y="{footer_y}" class="legend-text">Less</text>')
    for idx, col in enumerate(PALETTE):
        lx = legend_x + idx * (box_size + 4)
        svg.append(f'<rect x="{lx}" y="{footer_y - 10}" width="{box_size}" height="{box_size}" rx="2" fill="{col}" />')
    svg.append(f'<text x="{legend_x + len(PALETTE) * (box_size + 4) + 8}" y="{footer_y}" class="legend-text">More</text>')
    
    svg.append('</svg>')
    
    os.makedirs(os.path.dirname(output_svg) or ".", exist_ok=True)
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Animated Heatmap SVG created at {output_svg}")

if __name__ == "__main__":
    generate_animated_heatmap_svg()

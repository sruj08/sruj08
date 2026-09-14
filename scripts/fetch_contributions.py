import os
import json
import urllib.request
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

def fetch_contributions_data(username="sruj08", output_json="data/contributions.json"):
    url = f"https://github.com/users/{username}/contributions"
    print(f"Fetching contribution data from {url}...")
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all contribution cells (td or rect in github contribution calendar)
    day_elements = soup.find_all(['td', 'rect'], class_=lambda c: c and 'ContributionCalendar-day' in c)
    
    days = []
    total_contributions = 0
    best_day = {"date": "", "count": 0}
    
    for el in day_elements:
        date_str = el.get('data-date')
        if not date_str:
            continue
            
        # Level or count extraction
        level_attr = el.get('data-level', '0')
        level = int(level_attr) if level_attr.isdigit() else 0
        
        # Extract count from tooltip / text or id
        count = 0
        # Check tooltips or aria-label or data attributes
        tooltip_id = el.get('aria-describedby') or el.get('id')
        if tooltip_id:
            tooltip_el = soup.find(id=tooltip_id)
            if tooltip_el:
                text = tooltip_el.get_text()
                # e.g. "5 contributions on September 12, 2026" or "No contributions on September 13, 2026"
                parts = text.strip().split()
                if parts and parts[0].isdigit():
                    count = int(parts[0])
                    
        # Fallback if tooltip not found but level > 0
        if count == 0 and level > 0:
            count = level * 2
            
        total_contributions += count
        if count > best_day["count"]:
            best_day = {"date": date_str, "count": count}
            
        days.append({
            "date": date_str,
            "count": count,
            "level": level
        })
        
    # Sort days chronologically
    days.sort(key=lambda d: d["date"])
    
    # Calculate streaks
    current_streak = 0
    longest_streak = 0
    temp_streak = 0
    
    today_str = datetime.now().strftime('%Y-%m-%d')
    
    for day in days:
        if day["count"] > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0
            
    # Calculate current active streak ending today or yesterday
    for day in reversed(days):
        if day["count"] > 0:
            current_streak += 1
        else:
            # allow today to be 0 if yesterday was active
            if day["date"] == today_str and current_streak == 0:
                continue
            break
            
    result = {
        "username": username,
        "total_contributions": total_contributions,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "best_day": best_day,
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'),
        "days": days
    }
    
    os.makedirs(os.path.dirname(output_json) or ".", exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        
    print(f"Successfully scraped {len(days)} days ({total_contributions} total contributions) -> {output_json}")
    return result

if __name__ == "__main__":
    fetch_contributions_data("sruj08", "data/contributions.json")

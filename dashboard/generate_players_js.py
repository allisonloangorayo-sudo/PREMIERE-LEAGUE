import csv
import json
import os

base_dir = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\TALLER 2 ALLISON Y DANNA"
players_path = os.path.join(base_dir, "databases", "players.csv")
out_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\ml-dashboard-copy\src\players_data.js"

team_data = {}

with open(players_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            minutes = float(row['minutes'])
            if minutes <= 0: continue
            
            team = row['team'].strip()
            if not team: continue
            
            if team not in team_data:
                team_data[team] = []
                
            first_name = row['first_name'].strip() if row['first_name'] else ""
            last_name = row['second_name'].strip() if row['second_name'] else ""
            name = f"{first_name} {last_name}".strip()
            
            parts = name.split()
            init = ""
            if len(parts) >= 2:
                init = parts[0][0] + parts[-1][0]
            elif len(parts) == 1:
                init = parts[0][0:2].upper()
                
            xg = float(row.get('xG_per90', 0) or 0)
            price = float(row.get('price', 0) or 0)
            
            team_data[team].append({
                "name": name,
                "init": init.upper(),
                "xg": f"{xg:.2f}",
                "price": f"{price}",
                "xg_val": xg
            })
        except ValueError:
            continue

# Sort by xG descending for each team
for t in team_data:
    team_data[t].sort(key=lambda x: x["xg_val"], reverse=True)
    
    # Format styles and clean up
    for i, p in enumerate(team_data[t]):
        if i == 0:
            p['style'] = 'tg-gold'
        elif i == 1:
            p['style'] = 'tg-silver'
        elif i == 2:
            p['style'] = 'tg-bronze'
        else:
            p['style'] = 'tg-regular'
            
        p['isSuper'] = ("Haaland" in p['name'])
        del p['xg_val'] # remove helper key

all_teams = sorted(list(team_data.keys()))

with open(out_path, "w", encoding="utf-8") as f:
    f.write("const allTeams = " + json.dumps(all_teams) + ";\n")
    f.write("const teamPlayersData = " + json.dumps(team_data, indent=4) + ";\n")

print("Generated players_data.js")

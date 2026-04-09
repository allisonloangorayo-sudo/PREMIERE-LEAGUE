import pandas as pd
import json
import math
import os

# Paths
base_dir = r"c:\Users\salai402\Downloads\TALLER 2 ALLISON Y DANNA\TALLER 2 ALLISON Y DANNA"
players_path = os.path.join(base_dir, "databases", "players.csv")
league_path = os.path.join(base_dir, "models", "outputs", "clustering", "league_meta_results.csv")
out_path = r"c:\Users\salai402\Downloads\TALLER 2 ALLISON Y DANNA\ml-dashboard-copy\public\project_data.json"

# Make sure public dir exists
os.makedirs(os.path.dirname(out_path), exist_ok=True)

# 1. Process Teams (League Meta)
df_teams = pd.read_csv(league_path)
df_teams['coef_ia'] = (df_teams['win_prob'] * 100 + df_teams['goal_diff'] * 10 + df_teams['gf'] * 5).round(1)
df_teams = df_teams.sort_values('coef_ia', ascending=False)
top_teams = []
for i, row in df_teams.head(5).iterrows():
    top_teams.append({
        "pos": len(top_teams) + 1,
        "name": row['home_team'],
        "short": row['home_team'][:3].lower(),
        "coef": row['coef_ia'],
        "label": row['meta_label']
    })

# 2. Process Players
df_players = pd.read_csv(players_path)
# filter to relevant forwards/mids with good minutes
df_players = df_players[df_players['minutes'] > 1200]
df_players = df_players.sort_values('xG_per90', ascending=False)

top_players = []
for i, row in df_players.head(3).iterrows():
    top_players.append({
        "name": f"{row['first_name']} {row['second_name']}",
        "club": row['team'],
        "xg_90": float(row['xG_per90']),
        "price": float(row['price']),
        "influence": float(row['influence'])
    })

# 3. Create dummy predictions based on win properties
matches = [
    {"home": top_teams[0]['name'], "away": top_teams[1]['name'], "prob_h": 45, "prob_a": 35},
    {"home": top_teams[2]['name'], "away": top_teams[3]['name'], "prob_h": 60, "prob_a": 20},
    {"home": top_teams[4]['name'], "away": df_teams.iloc[-1]['home_team'], "prob_h": 75, "prob_a": 10},
]

out_data = {
    "ranking": top_teams,
    "mvps": top_players,
    "matches": matches
}

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=4)

print(f"Data successfully exported to {out_path}")

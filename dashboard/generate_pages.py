import pandas as pd
import os

base_dir = r"c:\Users\salai402\Downloads\TALLER 2 ALLISON Y DANNA\TALLER 2 ALLISON Y DANNA"
web_dir = r"c:\Users\salai402\Downloads\TALLER 2 ALLISON Y DANNA\ml-dashboard-copy"
players_path = os.path.join(base_dir, "databases", "players.csv")
league_path = os.path.join(base_dir, "models", "outputs", "clustering", "league_meta_results.csv")

df_teams = pd.read_csv(league_path)
df_teams['coef'] = (df_teams['win_prob'] * 100 + df_teams['goal_diff'] * 10 + df_teams['gf'] * 5).round(1)
df_teams = df_teams.sort_values('coef', ascending=False)
team_probs = dict(zip(df_teams['home_team'], df_teams['win_prob']))

df_players = pd.read_csv(players_path)
df_players = df_players[df_players['minutes'] > 1200].sort_values('xG_per90', ascending=False)

def get_wrapper(title, content):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | ML Predictor</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Outfit:wght@400;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="./src/index.css">
</head>
<body>
    <header class="main-header" style="background: rgba(2,6,23,0.9); height: 80px;">
        <div class="header-container">
            <h1 class="logo">PREMIER PREDICTOR <span class="badge">ML</span></h1>
            <nav class="main-nav"><ul><li><a href="index.html" class="active">← Volver al Dashboard</a></li></ul></nav>
        </div>
    </header>
    <main style="padding-top: 100px; min-height: 100vh; background: #020617; position: relative;">
        <!-- Background Blur -->
        <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: radial-gradient(circle at 10% 20%, rgba(0, 68, 204, 0.4) 0%, transparent 40%), radial-gradient(circle at 90% 80%, rgba(0, 180, 216, 0.3) 0%, transparent 40%); z-index: 0;"></div>
        <div class="container" style="position: relative; z-index: 1;">
            <h2 class="section-title" style="margin-bottom: 2rem;">{title}</h2>
            {content}
        </div>
    </main>
</body>
</html>'''

# --- GENERATE RANKING HTML ---
ranking_rows = ""
for pos, row in enumerate(df_teams.itertuples(), start=1):
    trend = "up" if pos <= 4 else ("down" if pos >= 15 else "equal")
    icon = 'fa-caret-up' if trend == 'up' else ('fa-caret-down' if trend == 'down' else 'fa-equal')
    ranking_rows += f'''
    <tr>
        <td>{pos}</td>
        <td class="club-cell">{row.home_team}</td>
        <td>{row.win_prob*100:.1f}%</td>
        <td><strong>{row.coef:.1f}</strong></td>
        <td>{row.meta_label}</td>
        <td class="trend {trend}"><i class="fa-solid {icon}"></i></td>
    </tr>'''

ranking_content = f'''
<div class="glass-panel" style="width: 100%; padding: 30px;">
    <table class="uefa-table" style="width: 100%;">
        <thead>
            <tr><th>Posición</th><th>Club</th><th>Prob. Victoria (ML)</th><th>Coeficiente Poder</th><th>Clúster/Perfil</th><th>Tendencia</th></tr>
        </thead>
        <tbody>{ranking_rows}</tbody>
    </table>
</div>
'''
with open(os.path.join(web_dir, "ranking.html"), "w", encoding="utf-8") as f:
    f.write(get_wrapper("RANKING COMPLETO DE PODER", ranking_content))

# --- GENERATE JUGADORES HTML ---
player_cards = ""
for _, row in df_players.head(30).iterrows():
    name = f"{row['first_name']} {row['second_name']}"
    initials = "".join([n[0] for n in name.split()[:2]])
    xg = row['xG_per90']
    market = f"£{float(row['price']):.1f}m"
    player_cards += f'''
    <div class="player-item" style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05);">
        <div class="player-avatar" style="width: 50px; height: 50px;">{initials}</div>
        <div class="player-info">
            <span class="player-name">{name}</span>
            <span class="player-club">{row['team']}</span>
        </div>
        <div class="player-stats">
            <span class="stat-badge" style="background:#0044CC; margin-bottom:5px;">xG {xg:.2f}/90</span>
            <span class="market-value">{market}</span>
        </div>
    </div>'''

jugadores_content = f'''
<div class="glass-panel" style="width: 100%; padding: 30px;">
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px;">
        {player_cards}
    </div>
</div>
'''
with open(os.path.join(web_dir, "jugadores.html"), "w", encoding="utf-8") as f:
    f.write(get_wrapper("ANÁLISIS TÉCNICO DE JUGADORES", jugadores_content))

# --- GENERATE CALENDARIO HTML ---
team_styles = {
    'Arsenal': ('#ef0107', '#fff'), 'Bournemouth': ('#b50e12', '#fff'), 'Chelsea': ('#034694', '#fff'), 
    'Man City': ('#6cabdd', '#fff'), 'Man United': ('#da291c', '#fff'), 'Leeds': ('#ffffff', '#000'), 
    'Liverpool': ('#c8102E', '#fff'), 'Fulham': ('#ffffff', '#000'), 'Brentford': ('#e30613', '#fff'), 
    'Everton': ('#003399', '#fff'), 'Burnley': ('#6c1d45', '#fff'), 'Brighton': ('#0057b8', '#fff'),
    'Crystal Palace': ('#1b458f', '#fff'), 'Newcastle': ('#000000', '#fff'), 'Aston Villa': ('#95bfe5', '#000'), 
    'Tottenham': ('#ffffff', '#000'), 'West Ham': ('#7a263a', '#fff'), 'Wolves': ('#fdb913', '#000'), 
    "Nott'm Forest": ('#e53233', '#fff'), 'Sunderland': ('#eb172b', '#fff')
}

matchweeks = {
    "Jornada 32 (11-13 Abril 2026)": [
        ("Arsenal", "Bournemouth", "Sábado, 11 Abril"), ("Chelsea", "Man City", "Domingo, 12 Abril"), 
        ("Man United", "Leeds", "Lunes, 13 Abril"), ("Liverpool", "Fulham", "Sábado, 11 Abril"), 
        ("Brentford", "Everton", "Sábado, 11 Abril"), ("Burnley", "Brighton", "Sábado, 11 Abril"),
        ("Crystal Palace", "Newcastle", "Domingo, 12 Abril"), ("Aston Villa", "Tottenham", "Domingo, 12 Abril"),
        ("West Ham", "Wolves", "Sábado, 11 Abril"), ("Nott'm Forest", "Sunderland", "Domingo, 12 Abril")
    ],
    "Jornada 33 (18-20 Abril 2026)": [
        ("Bournemouth", "Chelsea", "Sábado, 18 Abril"), ("Man City", "Arsenal", "Domingo, 19 Abril"), 
        ("Leeds", "Liverpool", "Lunes, 20 Abril"), ("Fulham", "Brentford", "Sábado, 18 Abril"), 
        ("Everton", "Burnley", "Domingo, 19 Abril"), ("Brighton", "Crystal Palace", "Sábado, 18 Abril"),
        ("Newcastle", "Aston Villa", "Sábado, 18 Abril"), ("Tottenham", "West Ham", "Sábado, 18 Abril"),
        ("Wolves", "Nott'm Forest", "Sábado, 18 Abril"), ("Sunderland", "Man United", "Domingo, 19 Abril")
    ]
}

calendario_content = ""

for mw_title, fixtures in matchweeks.items():
    calendario_content += f"<h3 style='color:#fff; margin-bottom: 20px; font-weight:800; text-transform: uppercase;'>{mw_title}</h3>"
    calendario_content += "<div class='match-grid' style='margin-bottom: 50px;'>"
    
    for (home, away, date) in fixtures:
        ph = team_probs.get(home, 0.4)
        pa = team_probs.get(away, 0.4)
        total = ph + pa
        pct_h = int(round((ph / total) * 100))
        pct_a = int(round((pa / total) * 100))
        win = home if pct_h > pct_a else away
        pct = max(pct_h, pct_a)
        w_class = "winner-home" if win == home else ("draw" if pct_h == pct_a else "winner")
        
        c_home_bg, c_home_fg = team_styles.get(home, ('#333', '#fff'))
        c_away_bg, c_away_fg = team_styles.get(away, ('#333', '#fff'))
        
        tla_h = home[:3].upper()
        if tla_h == "NOT": tla_h = "NFO"
        if tla_h == "CRY": tla_h = "CPA"
        
        tla_a = away[:3].upper()
        if tla_a == "NOT": tla_a = "NFO"
        if tla_a == "CRY": tla_a = "CPA"

        calendario_content += f'''
        <div class="match-card">
            <div class="match-date">{date}</div>
            <div class="match-teams">
                <div class="team">
                    <span class="team-name">{home}</span>
                    <div class="team-logo" style="background:{c_home_bg}; color:{c_home_fg}; border: 1px solid rgba(255,255,255,0.2);">{tla_h}</div>
                </div>
                <div class="match-vs">vs</div>
                <div class="team">
                    <div class="team-logo" style="background:{c_away_bg}; color:{c_away_fg}; border: 1px solid rgba(255,255,255,0.2);">{tla_a}</div>
                    <span class="team-name">{away}</span>
                </div>
            </div>
            <div class="match-prediction">
                <span class="pred-label">Pred. Modelo:</span>
                <span class="pred-value {w_class}">Victoria {win} ({pct}%)</span>
            </div>
        </div>'''
    
    calendario_content += "</div>"

with open(os.path.join(web_dir, "calendario.html"), "w", encoding="utf-8") as f:
    f.write(get_wrapper("CALENDARIO DE JUEGOS Y PRONÓSTICOS", calendario_content))

print("Created pages!")

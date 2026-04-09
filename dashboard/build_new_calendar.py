import pandas as pd
import os
import re

base_dir = r"c:\Users\salai402\Downloads\TALLER 2 ALLISON Y DANNA\TALLER 2 ALLISON Y DANNA"
web_dir = r"c:\Users\salai402\Downloads\TALLER 2 ALLISON Y DANNA\ml-dashboard-copy"
league_path = os.path.join(base_dir, "models", "outputs", "clustering", "league_meta_results.csv")

df_teams = pd.read_csv(league_path)
df_teams['coef'] = (df_teams['win_prob'] * 100 + df_teams['goal_diff'] * 10 + df_teams['gf'] * 5).round(1)
df_teams = df_teams.sort_values('coef', ascending=False)
team_probs = dict(zip(df_teams['home_team'], df_teams['win_prob']))


# --- LOGOS DICTIONARY ---
logo_map = {
    'Arsenal': 359, 'Aston Villa': 362, 'Bournemouth': 349, 'Brentford': 337,
    'Brighton': 331, 'Burnley': 379, 'Chelsea': 363, 'Crystal Palace': 384,
    'Everton': 368, 'Fulham': 370, 'Leeds': 357, 'Liverpool': 364,
    'Man City': 382, 'Man United': 360, 'Newcastle': 361, "Nott'm Forest": 393,
    'Sunderland': 366, 'Tottenham': 367, 'West Ham': 371, 'Wolves': 380
}

def get_logo_html(team_name, is_tiny=False):
    logo_id = logo_map.get(team_name, 359)
    url = f"https://a.espncdn.com/i/teamlogos/soccer/500/{logo_id}.png"
    size = "25px" if is_tiny else "50px"
    if is_tiny:
        return f'<img src="{url}" alt="{team_name}" style="width:{size}; height:{size}; object-fit:contain; vertical-align:middle; filter: drop-shadow(0 0 5px rgba(255,255,255,0.2));">'
    return f'<img src="{url}" alt="{team_name}" style="width:{size}; height:{size}; object-fit:contain; filter: drop-shadow(0 0 8px rgba(255,255,255,0.3));">'


def get_wrapper(title, content, js_script=""):
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
    {js_script}
</body>
</html>'''

# --- GENERATE RE-STYLED RANKING ---
ranking_rows = ""
for pos, row in enumerate(df_teams.itertuples(), start=1):
    trend = "up" if pos <= 4 else ("down" if pos >= 15 else "equal")
    icon = 'fa-caret-up' if trend == 'up' else ('fa-caret-down' if trend == 'down' else 'fa-equal')
    logo = get_logo_html(row.home_team, is_tiny=True)
    ranking_rows += f'''
    <tr>
        <td>{pos}</td>
        <td class="club-cell" style="display:flex; align-items:center; gap:10px;">{logo} {row.home_team}</td>
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

# --- CALENDARIO RE-GNERATOR ---
raw_text = """
vie., 10 de abr.
vie., 10 de abr.
Semana 32
West Ham United FC
Wolverhampton
14:00
sáb., 11 de abr.
sáb., 11 de abr.
Semana 32
Arsenal
AFC Bournemouth
6:30
sáb., 11 de abr.
Semana 32
Brentford
Everton FC
9:00
sáb., 11 de abr.
Semana 32
Burnley
Brighton & Hove Albion FC
9:00
sáb., 11 de abr.
Semana 32
Liverpool FC
FC Fulham
11:30
dom., 12 de abr.
dom., 12 de abr.
Semana 32
Crystal Palace FC
Newcastle United FC
8:00
dom., 12 de abr.
Semana 32
Sunderland AFC
Tottenham
8:00
dom., 12 de abr.
Semana 32
Nottingham
Aston Villa
8:00
dom., 12 de abr.
Semana 32
Chelsea
Manchester City FC
10:30
lun., 13 de abr.
lun., 13 de abr.
Semana 32
Man Utd
Leeds United
14:00
sáb., 18 de abr.
sáb., 18 de abr.
Semana 33
Brentford
FC Fulham
6:30
sáb., 18 de abr.
Semana 33
Newcastle United FC
AFC Bournemouth
9:00
sáb., 18 de abr.
Semana 33
Leeds United
Wolverhampton
9:00
sáb., 18 de abr.
Semana 33
Tottenham
Brighton & Hove Albion FC
11:30
sáb., 18 de abr.
Semana 33
Chelsea
Man Utd
14:00
dom., 19 de abr.
dom., 19 de abr.
Semana 33
Everton FC
Liverpool FC
8:00
dom., 19 de abr.
Semana 33
Aston Villa
Sunderland AFC
8:00
dom., 19 de abr.
Semana 33
Nottingham
Burnley
8:00
dom., 19 de abr.
Semana 33
Manchester City FC
Arsenal
10:30
lun., 20 de abr.
lun., 20 de abr.
Semana 33
Crystal Palace FC
West Ham United FC
14:00
vie., 24 de abr.
vie., 24 de abr.
Semana 34
Sunderland AFC
Nottingham
14:00
sáb., 25 de abr.
sáb., 25 de abr.
Semana 34
FC Fulham
Aston Villa
6:30
sáb., 25 de abr.
Semana 34
AFC Bournemouth
Leeds United
9:00
sáb., 25 de abr.
Semana 34
West Ham United FC
Everton FC
9:00
sáb., 25 de abr.
Semana 34
Liverpool FC
Crystal Palace FC
9:00
sáb., 25 de abr.
Semana 34
Wolverhampton
Tottenham
9:00
sáb., 25 de abr.
Semana 34
Arsenal
Newcastle United FC
11:30
dom., 26 de abr.
dom., 26 de abr.
Semana 34
Burnley
Manchester City FC
8:00
dom., 26 de abr.
Semana 34
Brighton & Hove Albion FC
Chelsea
10:30
lun., 27 de abr.
lun., 27 de abr.
Semana 34
Man Utd
Brentford
14:00
vie., 1 de may.
vie., 1 de may.
Semana 35
Leeds United
Burnley
14:00
sáb., 2 de may.
sáb., 2 de may.
Semana 35
Aston Villa
Tottenham
6:30
sáb., 2 de may.
Semana 35
Newcastle United FC
Brighton & Hove Albion FC
9:00
sáb., 2 de may.
Semana 35
AFC Bournemouth
Crystal Palace FC
9:00
sáb., 2 de may.
Semana 35
Wolverhampton
Sunderland AFC
9:00
sáb., 2 de may.
Semana 35
Brentford
West Ham United FC
9:00
sáb., 2 de may.
Semana 35
Arsenal
FC Fulham
11:30
dom., 3 de may.
dom., 3 de may.
Semana 35
Man Utd
Liverpool FC
9:30
lun., 4 de may.
lun., 4 de may.
Semana 35
Chelsea
Nottingham
9:00
lun., 4 de may.
Semana 35
Everton FC
Manchester City FC
14:00
sáb., 9 de may.
sáb., 9 de may.
Semana 36
Liverpool FC
Chelsea
6:30
sáb., 9 de may.
Semana 36
Sunderland AFC
Man Utd
9:00
sáb., 9 de may.
Semana 36
FC Fulham
AFC Bournemouth
9:00
sáb., 9 de may.
Semana 36
Brighton & Hove Albion FC
Wolverhampton
9:00
sáb., 9 de may.
Semana 36
Burnley
Aston Villa
9:00
sáb., 9 de may.
Semana 36
Crystal Palace FC
Everton FC
9:00
sáb., 9 de may.
Semana 36
Manchester City FC
Brentford
11:30
dom., 10 de may.
dom., 10 de may.
Semana 36
Nottingham
Newcastle United FC
8:00
dom., 10 de may.
Semana 36
West Ham United FC
Arsenal
10:30
lun., 11 de may.
lun., 11 de may.
Semana 36
Tottenham
Leeds United
14:00
dom., 17 de may.
dom., 17 de may.
Semana 37
Newcastle United FC
West Ham United FC
Pendiente de anuncio
dom., 17 de may.
Semana 37
Brentford
Crystal Palace FC
Pendiente de anuncio
dom., 17 de may.
Semana 37
AFC Bournemouth
Manchester City FC
Pendiente de anuncio
dom., 17 de may.
Semana 37
Chelsea
Tottenham
Pendiente de anuncio
dom., 17 de may.
Semana 37
Everton FC
Sunderland AFC
Pendiente de anuncio
dom., 17 de may.
Semana 37
Arsenal
Burnley
Pendiente de anuncio
dom., 17 de may.
Semana 37
Wolverhampton
FC Fulham
Pendiente de anuncio
dom., 17 de may.
Semana 37
Man Utd
Nottingham
Pendiente de anuncio
dom., 17 de may.
Semana 37
Leeds United
Brighton & Hove Albion FC
Pendiente de anuncio
dom., 17 de may.
Semana 37
Aston Villa
Liverpool FC
Pendiente de anuncio
dom., 24 de may.
dom., 24 de may.
Semana 38
Liverpool FC
Brentford
10:00
dom., 24 de may.
Semana 38
Burnley
Wolverhampton
10:00
dom., 24 de may.
Semana 38
Crystal Palace FC
Arsenal
10:00
dom., 24 de may.
Semana 38
West Ham United FC
Leeds United
10:00
dom., 24 de may.
Semana 38
Brighton & Hove Albion FC
Man Utd
10:00
dom., 24 de may.
Semana 38
Nottingham
AFC Bournemouth
10:00
dom., 24 de may.
Semana 38
FC Fulham
Newcastle United FC
10:00
dom., 24 de may.
Semana 38
Tottenham
Everton FC
10:00
dom., 24 de may.
Semana 38
Sunderland AFC
Chelsea
10:00
dom., 24 de may.
Semana 38
Manchester City FC
Aston Villa
10:00
"""
lines = [l.strip() for l in raw_text.split('\n') if l.strip() != '']
weeks_data = {}
name_map = {
    'West Ham United FC': 'West Ham', 'Wolverhampton': 'Wolves', 'Arsenal': 'Arsenal',
    'AFC Bournemouth': 'Bournemouth', 'Brentford': 'Brentford', 'Everton FC': 'Everton',
    'Burnley': 'Burnley', 'Brighton & Hove Albion FC': 'Brighton', 'Liverpool FC': 'Liverpool',
    'FC Fulham': 'Fulham', 'Crystal Palace FC': 'Crystal Palace', 'Newcastle United FC': 'Newcastle',
    'Sunderland AFC': 'Sunderland', 'Tottenham': 'Tottenham', 'Nottingham': "Nott'm Forest",
    'Aston Villa': 'Aston Villa', 'Chelsea': 'Chelsea', 'Manchester City FC': 'Man City',
    'Man Utd': 'Man United', 'Leeds United': 'Leeds'
}

i = 0
while i < len(lines):
    if lines[i].startswith("Semana"):
        week = lines[i]
        date = lines[i-1]
        t1 = name_map.get(lines[i+1], lines[i+1])
        t2 = name_map.get(lines[i+2], lines[i+2])
        time_m = lines[i+3]
        if week not in weeks_data: weeks_data[week] = []
        weeks_data[week].append((t1, t2, f"{date} • {time_m}"))
        i += 4
    else: i += 1

tabs_html = '<div class="week-selector" style="display:flex; gap:10px; flex-wrap:wrap; margin-bottom:30px;">'
content_html = ''
is_first = True

for week, fixtures in weeks_data.items():
    active_class = "active" if is_first else ""
    btn_style = "background: #0044CC; opacity: 1;" if is_first else "background: rgba(255,255,255,0.1); opacity: 0.7;"
    tabs_html += f'<button class="week-tab {active_class}" onclick="showWeek(\'{week.replace(" ","")}\')" style="padding: 10px 20px; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; {btn_style} transition: 0.3s;">{week}</button>'
    
    display_style = "block" if is_first else "none"
    content_html += f"<div id='{week.replace(' ','')}' class='week-content' style='display: {display_style};'>"
    content_html += "<div class='match-grid'>"
    
    for (home, away, d_string) in fixtures:
        ph = team_probs.get(home, 0.4)
        pa = team_probs.get(away, 0.4)
        tot = ph + pa
        pct_h = int(round((ph / tot) * 100))
        pct_a = int(round((pa / tot) * 100))
        win = home if pct_h > pct_a else away
        pct = max(pct_h, pct_a)
        w_class = "winner-home" if win == home else ("draw" if pct_h == pct_a else "winner")
        
        logo_h = get_logo_html(home)
        logo_a = get_logo_html(away)

        content_html += f'''
        <div class="match-card">
            <div class="match-date" style="text-transform: capitalize;">{d_string}</div>
            <div class="match-teams">
                <div class="team" style="display:flex; flex-direction:column; align-items:center;">
                    {logo_h}
                    <span class="team-name" style="margin-top:8px;">{home}</span>
                </div>
                <div class="match-vs">vs</div>
                <div class="team" style="display:flex; flex-direction:column; align-items:center;">
                    {logo_a}
                    <span class="team-name" style="margin-top:8px;">{away}</span>
                </div>
            </div>
            <div class="match-prediction">
                <span class="pred-label">Pred. Modelo:</span>
                <span class="pred-value {w_class}">Victoria {win} ({pct}%)</span>
            </div>
        </div>'''
    
    content_html += "</div></div>"
    is_first = False

tabs_html += '</div>'

js_script = '''
<script>
function showWeek(weekId) {
    document.querySelectorAll('.week-content').forEach(el => el.style.display = 'none');
    document.getElementById(weekId).style.display = 'block';
    document.querySelectorAll('.week-tab').forEach(btn => {
        btn.style.background = 'rgba(255,255,255,0.1)';
        btn.style.opacity = '0.7';
    });
    event.currentTarget.style.background = '#0044CC';
    event.currentTarget.style.opacity = '1';
}
</script>
'''

with open(os.path.join(web_dir, "calendario.html"), "w", encoding="utf-8") as f:
    f.write(get_wrapper("CALENDARIO DE JUEGOS Y PRONÓSTICOS", f'<div class="glass-panel" style="width: 100%; padding: 30px;">{tabs_html}{content_html}</div>', js_script))

print("Regenerated all pages with explicit logos!")

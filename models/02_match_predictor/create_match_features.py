import pandas as pd
import numpy as np
import os

# Configuración
base_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA"
matches_path = os.path.join(base_path, "databases", "matches.csv")
events_path = os.path.join(base_path, "databases", "events.csv")
output_path = os.path.join(base_path, "databases", "matches_enriched.csv")

print("Cargando base de partidos...")
df_matches = pd.read_csv(matches_path)
df_matches['date'] = pd.to_datetime(df_matches['date'], dayfirst=True)
df_matches = df_matches.sort_values(['date', 'time'])

# --- 1. Calcular Medias Móviles (Rolling Averages) por Equipo ---
# El truco es no incluir el partido actual para predecir el actual.
def get_rolling_stats(team_name, date, n_prev=5):
    # Partidos previos donde el equipo fue local
    prev_home = df_matches[(df_matches['home_team'] == team_name) & (df_matches['date'] < date)]
    # Partidos previos donde el equipo fue visitante
    prev_away = df_matches[(df_matches['away_team'] == team_name) & (df_matches['date'] < date)]
    
    prev_matches = pd.concat([prev_home, prev_away]).sort_values('date', ascending=False).head(n_prev)
    
    if len(prev_matches) < 2: # No hay suficiente historia
        return None
    
    stats = {}
    # Goles anotados por el equipo en cuestión
    goals_for = []
    for _, row in prev_matches.iterrows():
        if row['home_team'] == team_name:
            goals_for.append(row['fthg'])
        else:
            goals_for.append(row['ftag'])
    
    stats['avg_goals_for'] = np.mean(goals_for)
    stats['form_points'] = 0 # 3 pts win, 1 pt draw
    for _, row in prev_matches.iterrows():
        if row['ftr'] == 'D':
            stats['form_points'] += 1
        elif (row['home_team'] == team_name and row['ftr'] == 'H') or (row['away_team'] == team_name and row['ftr'] == 'A'):
            stats['form_points'] += 3
            
    # Tiros al arco previos (ofensivo)
    shot_stats = []
    for _, row in prev_matches.iterrows():
        if row['home_team'] == team_name:
            shot_stats.append(row['hst'])
        else:
            shot_stats.append(row['ast'])
    stats['avg_sot_for'] = np.mean(shot_stats)
    
    return stats

print("Generando variables de estado de forma (esto puede tardar un poco)...")
rows = []
for idx, row in df_matches.iterrows():
    h_stats = get_rolling_stats(row['home_team'], row['date'])
    a_stats = get_rolling_stats(row['away_team'], row['date'])
    
    new_row = row.to_dict()
    if h_stats:
        for k, v in h_stats.items(): new_row[f'home_{k}'] = v
    if a_stats:
        for k, v in a_stats.items(): new_row[f'away_{k}'] = v
    rows.append(new_row)

df_enriched = pd.DataFrame(rows)

# --- 2. Factor Árbitro (Home Bias) ---
# Calcular tendencia del árbitro históricamente
ref_stats = df_matches.groupby('referee').agg({
    'ftr': lambda x: (x == 'H').mean()
}).rename(columns={'ftr': 'ref_home_win_rate'}).reset_index()

df_enriched = df_enriched.merge(ref_stats, on='referee', how='left')

# --- 3. Probabilidad Implícita del Mercado ---
# Ya están en la tabla (implied_prob_h/d/a), pero las reforzamos
df_enriched['market_favorite'] = df_enriched[['b365h', 'b365d', 'b365a']].idxmin(axis=1)

# --- 4. Diferenciales (Lo más potente) ---
df_enriched['goals_diff_form'] = df_enriched['home_avg_goals_for'] - df_enriched['away_avg_goals_for']
df_enriched['sot_diff_form'] = df_enriched['home_avg_sot_for'] - df_enriched['away_avg_sot_for']

# Guardar la base enriquecida
df_enriched.dropna(subset=['home_avg_goals_for', 'away_avg_goals_for'], inplace=True)
df_enriched.to_csv(output_path, index=False)
print(f"Base de partidos enriquecida guardada en: {output_path}")
print(f"Total de partidos después de filtrar por historia: {len(df_enriched)}")

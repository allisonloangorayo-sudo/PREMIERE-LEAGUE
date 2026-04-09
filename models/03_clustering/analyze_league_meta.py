import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

# --- PREPARACIÓN ---
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(base_path, "databases", "matches_enriched.csv")
output_dir = os.path.join(base_path, "models", "outputs", "clustering")
os.makedirs(output_dir, exist_ok=True)

# 1. Carga de datos
df = pd.read_csv(data_path)

# 2. Ingeniería de "Meta-Estadísticas" de Equipo
# Queremos ver el balance ataque/defensa
home_meta = df.groupby('home_team').agg({
    'fthg': 'mean',      # Goles favor
    'ftag': 'mean',      # Goles contra
    'hs': 'mean',        # Tiros favor
    'as_': 'mean',       # Tiros contra
    'implied_prob_h': 'mean'
}).rename(columns={'fthg': 'gf', 'ftag': 'ga', 'hs': 'sf', 'as_': 'sa', 'implied_prob_h': 'win_prob'})

away_meta = df.groupby('away_team').agg({
    'ftag': 'mean',
    'fthg': 'mean',
    'as_': 'mean',
    'hs': 'mean',
    'implied_prob_a': 'mean'
}).rename(columns={'ftag': 'gf', 'fthg': 'ga', 'as_': 'sf', 'hs': 'sa', 'implied_prob_a': 'win_prob'})

team_meta = (home_meta + away_meta) / 2
team_meta['goal_diff'] = team_meta['gf'] - team_meta['ga']
team_meta['shot_ratio'] = team_meta['sf'] / (team_meta['sf'] + team_meta['sa'])

# 3. Selección de Features Meta
features = ['gf', 'ga', 'win_prob', 'goal_diff', 'shot_ratio']
X = team_meta[features]

# 4. Clustering (K=4 para identificar el "Meta")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
team_meta['meta_cluster'] = kmeans.fit_predict(X_scaled)

# 5. Interpretación del Meta
meta_profiles = team_meta.groupby('meta_cluster')[features].mean()
print("\n--- Perfiles del Meta de la Liga ---")
print(meta_profiles)

def label_meta(row):
    if row['win_prob'] > 0.45: return "The Elites (Title Contenders)"
    if row['goal_diff'] > 0: return "Solid Competitors (European Race)"
    if row['ga'] > 1.5: return "Chaos/High Risk (Relegation Risk)"
    return "Stable Mid-Table"

team_meta['meta_label'] = team_meta.apply(label_meta, axis=1)

# 6. Visualización del Meta: Ataque vs Defensa
plt.figure(figsize=(12, 8))
# Invertimos GA para que "mejor defensa" esté arriba
sns.scatterplot(data=team_meta, x='gf', y='ga', hue='meta_label', s=200, palette='Set2')
plt.gca().invert_yaxis() # Menos goles en contra es mejor (arriba)

for i, team in enumerate(team_meta.index):
    plt.text(team_meta.gf[i]+0.02, team_meta.ga[i], team, fontsize=10)

plt.title("El 'Meta' de la Premier League 2025-26: Ataque vs Defensa", fontsize=15)
plt.xlabel("Goles a Favor (Promedio)", fontsize=12)
plt.ylabel("Goles en Contra (Promedio - Invertido)", fontsize=12)
plt.legend(title="Segmento Meta", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig(os.path.join(output_dir, "league_meta_map.png"))

# Guardar
team_meta.to_csv(os.path.join(output_dir, "league_meta_results.csv"))
print(f"\nResultados del meta guardados en: {output_dir}")

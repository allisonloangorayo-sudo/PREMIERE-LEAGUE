import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import scipy.cluster.hierarchy as sch
import os

# --- PREPARACIÓN ---
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(base_path, "databases", "matches_enriched.csv")
output_dir = os.path.join(base_path, "models", "outputs", "clustering")
os.makedirs(output_dir, exist_ok=True)

# 1. Carga de datos
df_m = pd.read_csv(data_path)

# Necesitamos agrupar por equipo para sacar estadísticas promedio por equipo
home_stats = df_m.groupby('home_team').agg({
    'fthg': 'mean',
    'hs': 'mean',
    'hst': 'mean',
    'implied_prob_h': 'mean'
}).rename(columns={'fthg': 'goals', 'hs': 'shots', 'hst': 'sot', 'implied_prob_h': 'win_prob'})

away_stats = df_m.groupby('away_team').agg({
    'ftag': 'mean',
    'as_': 'mean',
    'ast': 'mean',
    'implied_prob_a': 'mean'
}).rename(columns={'ftag': 'goals', 'as_': 'shots', 'ast': 'sot', 'implied_prob_a': 'win_prob'})

# Promedio general por equipo
team_stats = (home_stats + away_stats) / 2
team_stats['efficiency'] = team_stats['goals'] / team_stats['sot']
team_stats = team_stats.fillna(0)

# 2. Selección de Variables Tácticas
features = ['goals', 'shots', 'sot', 'win_prob', 'efficiency']
X = team_stats[features]

# 3. Escalado
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Clustering Jerárquico (Dendrograma)
plt.figure(figsize=(12, 7))
dendrogram = sch.dendrogram(sch.linkage(X_scaled, method='ward'), labels=team_stats.index)
plt.title('Dendrograma de Estilos de Juego (Premier League)', fontsize=15)
plt.xlabel('Equipos')
plt.ylabel('Distancia Euclidiana')
plt.xticks(rotation=90)
plt.savefig(os.path.join(output_dir, "team_dendrogram.png"))

# 5. Aplicar Clustering (K=3 para simplificar: Top, Mid, Bottom)
hc = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
team_stats['cluster'] = hc.fit_predict(X_scaled)

# 6. Resultados e Interpretación
print("\n--- Perfiles de Equipos por Cluster ---")
print(team_stats.groupby('cluster')[features].mean())

# Guardar Resultados
team_stats.to_csv(os.path.join(output_dir, "team_segments.csv"))
print(f"\nResultados de equipos guardados en: {output_dir}")

# Scatter plot de interpretación: Tiros a puerta vs Probabilidad de Victoria
plt.figure(figsize=(10, 6))
sns.scatterplot(data=team_stats, x='sot', y='win_prob', hue='cluster', style='cluster', s=150, palette='Set1')

for i, team in enumerate(team_stats.index):
    plt.text(team_stats.sot[i]+0.1, team_stats.win_prob[i], team, fontsize=9)

plt.title("Segmentación Tactica de Equipos: Eficiencia vs Dominio", fontsize=14)
plt.savefig(os.path.join(output_dir, "team_tactical_clusters.png"))

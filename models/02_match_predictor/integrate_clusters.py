import pandas as pd
import os

# --- RUTAS ---
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
matches_path = os.path.join(base_path, "databases", "matches_enriched.csv")
team_clusters_path = os.path.join(base_path, "models", "outputs", "clustering", "team_segments.csv")
player_clusters_path = os.path.join(base_path, "models", "outputs", "clustering", "player_assignments.csv")
output_path = os.path.join(base_path, "databases", "matches_with_clusters.csv")

print("Integrando clusters en los datos de partidos...")

# 1. Cargar Datos
df_matches = pd.read_csv(matches_path)
df_team_clusters = pd.read_csv(team_clusters_path)
df_player_clusters = pd.read_csv(player_clusters_path)

# --- 2. INTEGRAR CLUSTERS DE EQUIPOS ---
# Mapeo de clusters de equipos
team_to_cluster = df_team_clusters.set_index('home_team')['cluster'].to_dict()

df_matches['home_team_cluster'] = df_matches['home_team'].map(team_to_cluster)
df_matches['away_team_cluster'] = df_matches['away_team'].map(team_to_cluster)

# --- 3. INTEGRAR CLUSTERS DE JUGADORES (AGREGADOS) ---
# Queremos saber cuántos "Finishers" u "Orchestrators" tiene cada equipo
# Cluster 0: Finishers
# Cluster 3: Orchestrators
player_counts = df_player_clusters.groupby(['team', 'cluster']).size().unstack(fill_value=0)
player_counts.columns = [f'cluster_{c}_count' for c in player_counts.columns]

# Normalizar nombres de equipos si es necesario (asumimos que coinciden)
# Unir conteos al match
df_matches = df_matches.merge(player_counts.add_prefix('home_'), left_on='home_team', right_index=True, how='left')
df_matches = df_matches.merge(player_counts.add_prefix('away_'), left_on='away_team', right_index=True, how='left')

# Llenar nulos (equipos que quizás no tengan jugadores en ciertos clusters)
df_matches = df_matches.fillna(0)

# --- 4. CREAR VARIABLES DIFERENCIALES ---
# Ejemplo: Diferencia de "Orquestadores" entre Home y Away
df_matches['orchestrator_diff'] = df_matches['home_cluster_3_count'] - df_matches['away_cluster_3_count']
df_matches['finisher_diff'] = df_matches['home_cluster_0_count'] - df_matches['away_cluster_0_count']

# --- 5. GUARDAR ---
df_matches.to_csv(output_path, index=False)
print(f"Dataset enriquecido con clusters guardado en: {output_path}")
print(f"Nuevas columnas añadidas: {len(df_matches.columns) - len(pd.read_csv(matches_path).columns)}")

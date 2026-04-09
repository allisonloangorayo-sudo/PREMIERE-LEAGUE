import pandas as pd
import os

# --- RUTAS ---
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
xg_data_path = os.path.join(base_path, "databases", "xg_master_data.csv")
player_clusters_path = os.path.join(base_path, "models", "outputs", "clustering", "player_assignments.csv")
output_path = os.path.join(base_path, "databases", "xg_with_clusters.csv")

print("Integrando clusters en los datos de xG (Regresión)...")

# 1. Cargar Datos
df_xg = pd.read_csv(xg_data_path)
df_player_clusters = pd.read_csv(player_clusters_path)

# 2. Unir clusters de jugadores
# Usamos 'web_name' en df_player_clusters y comparamos con 'player_name' (limpieza necesaria)
# Nota: En xg_master_data el nombre puede estar en minúsculas.
df_player_clusters['name_key'] = df_player_clusters['web_name'].str.lower()
df_xg['name_key'] = df_xg['player_name'].str.lower()

mapping = df_player_clusters.set_index('name_key')['cluster'].to_dict()
df_xg['player_cluster'] = df_xg['name_key'].map(mapping)

# Llenar nulos (jugadores sin cluster asignado son 'estándar' or 1)
df_xg['player_cluster'] = df_xg['player_cluster'].fillna(1).astype(int)

# 3. Guardar
df_xg.to_csv(output_path, index=False)
print(f"Dataset xG enriquecido guardado en: {output_path}")

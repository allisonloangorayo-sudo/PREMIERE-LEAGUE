import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

# --- CONFIGURACIÓN DE RUTAS ---
# Usamos rutas relativas para mejor portabilidad
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(base_path, "databases", "players.csv")
output_dir = os.path.join(base_path, "models", "outputs", "clustering")
os.makedirs(output_dir, exist_ok=True)

print(f"Buscando datos en: {data_path}")

# 1. Carga de Datos
try:
    df = pd.read_csv(data_path)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {data_path}")
    exit()

# Filtrar jugadores con minutos significativos para evitar ruido de suplentes extremos
# (Uso 450 min como benchmark de ~5 partidos completos)
df_active = df[df['minutes'] > 450].copy()
print(f"Jugadores filtrados para análisis: {len(df_active)}")

# 2. Selección de Variables para el Perfil Táctico
# Estas variables definen qué tipo de impacto tiene el jugador en el campo
features = ['xG_per90', 'xA_per90', 'ict_index', 'creativity', 'threat', 'influence']
X = df_active[features].fillna(0)

# 3. Preprocesamiento (Escalado)
# Crucial para K-Means ya que se basa en distancias euclidianas
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Encontrar K Óptimo (Método del Codo - Opcional)
# Para este taller usaremos K=4 basándonos en la estructura típica de roles en fútbol
k = 4
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df_active['cluster'] = kmeans.fit_predict(X_scaled)

# 5. Reducción de Dimensionalidad (PCA) para Visualización 2D
# K-Means trabaja en 6D (nuestras features), PCA nos permite verlo en 2D sin perder mucha info
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)
df_active['pca1'] = components[:, 0]
df_active['pca2'] = components[:, 1]

# 6. Interpretación de los Resultados (Centroides)
cluster_profiles = df_active.groupby('cluster')[features].mean()
print("\n--- Perfiles Matemáticos de los Clusters ---")
print(cluster_profiles)

def get_cluster_name(cluster_id):
    # Lógica basada en el perfil promedio observado
    profile = cluster_profiles.loc[cluster_id]
    if profile['threat'] > profile['creativity'] * 1.5:
        return "The Finishers (Goal Hunters)"
    elif profile['creativity'] > profile['threat'] * 1.2:
        return "The Orchestrators (Playmakers)"
    elif profile['ict_index'] > 200:
        return "The Elite Multi-taskers"
    else:
        return "The Engine Room (Consistency)"

# 7. Visualización con Interpretación
plt.figure(figsize=(14, 9))
sns.set_style("darkgrid")

# Plot principal
scatter = sns.scatterplot(
    data=df_active, 
    x='pca1', y='pca2', 
    hue='cluster', 
    palette='viridis', 
    s=100, 
    alpha=0.6,
    edgecolor='w'
)

# Anotar jugadores icónicos para dar contexto al usuario
# Haaland (Threat), Odegaard (Creativity), Van Dijk (Influence), etc.
iconic_players = [
    'Haaland', 'M.Salah', 'Palmer', 'B.Fernandes', 'Saka', 
    'Virgil', 'Rice', 'Rodri', 'Odegaard', 'Alexander-Arnold'
]

for name in iconic_players:
    player_data = df_active[df_active['web_name'] == name]
    if not player_data.empty:
        plt.text(
            player_data['pca1'].values[0] + 0.1, 
            player_data['pca2'].values[0] + 0.1, 
            name, 
            fontsize=10, weight='bold', alpha=0.9
        )

plt.title("Segmentación Táctica de Jugadores - Premier League 2025-26", fontsize=16, pad=20)
plt.xlabel("Componente Principal 1 (Impacto Ofensivo/Volumen)", fontsize=12)
plt.ylabel("Componente Principal 2 (Creatividad vs Amenaza)", fontsize=12)
plt.legend(title="Cluster ID", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Guardar
chart_path = os.path.join(output_dir, "player_clusters.png")
plt.savefig(chart_path)
print(f"\nVisualización guardada en: {chart_path}")

# Guardar CSV con asignaciones
output_csv = os.path.join(output_dir, "player_assignments.csv")
df_active[['web_name', 'team', 'position', 'cluster'] + features].to_csv(output_csv, index=False)
print(f"Asignaciones guardadas en: {output_csv}")

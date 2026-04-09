import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

# --- RUTAS ---
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(base_path, "databases", "players.csv")
output_dir = os.path.join(base_path, "models", "outputs", "clustering")
os.makedirs(output_dir, exist_ok=True)

# 1. Carga y Filtro
df = pd.read_csv(data_path)
df_active = df[df['minutes'] > 450].copy()

# 2. Variables de Perfil
features = ['xG_per90', 'xA_per90', 'ict_index', 'creativity', 'threat', 'influence']
X = df_active[features].fillna(0)

# 3. Escalado
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. DBSCAN - Búsqueda de Outliers (Los "Unicornios")
# eps: distancia máxima entre dos muestras para que se consideren vecinas
# min_samples: nro mínimo de muestras en un vecindario para ser núcleo
dbscan = DBSCAN(eps=1.5, min_samples=3) 
df_active['dbscan_cluster'] = dbscan.fit_predict(X_scaled)

# 5. Marcado de Outliers
# En DBSCAN, el label -1 significa "Noise" (Anomalía)
df_active['is_outlier'] = df_active['dbscan_cluster'] == -1
outliers = df_active[df_active['is_outlier']]

print(f"\n--- Análisis de Outliers (DBSCAN) ---")
print(f"Total de jugadores: {len(df_active)}")
print(f"Outliers detectados: {len(outliers)}")
print("\nJugadores 'Unicornio' (Perfiles Únicos):")
print(outliers[['web_name', 'team', 'position', 'ict_index']].sort_values(by='ict_index', ascending=False).head(10))

# 6. Visualización PCA con Foco en Outliers
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df_active['pca1'] = X_pca[:, 0]
df_active['pca2'] = X_pca[:, 1]
outliers = df_active[df_active['is_outlier']]

plt.figure(figsize=(12, 8))
sns.set_style("white")

# Jugadores normales
sns.scatterplot(
    data=df_active[~df_active['is_outlier']], 
    x='pca1', y='pca2', color='lightgrey', alpha=0.5, label='Perfil Estándar'
)

# Outliers
sns.scatterplot(
    data=df_active[df_active['is_outlier']], 
    x='pca1', y='pca2', color='red', s=120, edgecolor='black', label='Outliers (Unicornios)'
)

# Anotar los outliers más importantes
for i, row in outliers.iterrows():
    if row['ict_index'] > 180 or row['web_name'] in ['Haaland', 'M.Salah', 'Palmer']:
        plt.text(row['pca1']+0.1, row['pca2']+0.1, row['web_name'], fontsize=10, weight='bold')

plt.title("Refinamiento de Clusters: Detección de 'Unicornios' con DBSCAN", fontsize=15)
plt.savefig(os.path.join(output_dir, "player_outliers_dbscan.png"))
print(f"\nMapa de outliers guardado en: {output_dir}")

# Guardar lista de outliers para análisis técnico
outliers.to_csv(os.path.join(output_dir, "player_unicorns.csv"), index=False)

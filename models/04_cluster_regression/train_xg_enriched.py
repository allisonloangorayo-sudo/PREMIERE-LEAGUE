import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, precision_score, roc_auc_score, balanced_accuracy_score, log_loss
import os

# --- RUTAS ---
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(base_path, "databases", "xg_with_clusters.csv")
output_dir = os.path.join(base_path, "models", "outputs", "regression")
os.makedirs(output_dir, exist_ok=True)

print("Entrenando Modelo xG (Regresión Probabilística) con Clusters...")
df = pd.read_csv(data_path)

# 1. Ingeniería de Variables (Copiado de original + Clusters)
df['distance'] = np.sqrt((100 - df['x'])**2 + (50 - df['y'])**2)
dy1 = 46.34 - df['y']
dy2 = 53.66 - df['y']
dx = 100 - df['x']
df['visible_angle'] = np.abs(np.arctan2(dy2, dx) - np.arctan2(dy1, dx))

# Parsear Qualifiers (JSON)
def parse_qualifiers(q_str):
    try:
        q_list = json.loads(q_str.replace("'", '"'))
        q_ids = [str(item.get('type', {}).get('value')) for item in q_list]
        return {'is_big_chance': '214' in q_ids, 'is_header': '15' in q_ids, 'is_penalty': '9' in q_ids}
    except:
        return {'is_big_chance': False, 'is_header': False, 'is_penalty': False}

qualifiers_df = df['qualifiers'].apply(parse_qualifiers).apply(pd.Series)
df = pd.concat([df, qualifiers_df], axis=1)

# Variables
features = [
    'distance', 'visible_angle', 'is_big_chance', 'is_header', 'is_penalty',
    'player_cluster', 'ict_index', 'threat'
]

X = df[features].fillna(0)
y = df['is_goal'].astype(int)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Modelo (Random Forest para manejar no-linealidad de clusters)
rf = RandomForestClassifier(n_estimators=150, max_depth=7, class_weight='balanced', random_state=42)
rf.fit(X_train, y_train)

# Predicciones
y_prob = rf.predict_proba(X_test)[:, 1]
y_pred = rf.predict(X_test)

metrics = {
    "Balanced Acc": balanced_accuracy_score(y_test, y_pred),
    "ROC-AUC": roc_auc_score(y_test, y_prob),
    "Log Loss (xG Error)": log_loss(y_test, y_prob),
    "Recall (Goles)": recall_score(y_test, y_pred)
}

print("\n--- NUEVOS RESULTADOS XG CON CLUSTERS ---")
for k, v in metrics.items():
    print(f"{k}: {v:.4f}")

# Importancia específica del player_cluster
importances = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=False)
print("\nImportancia de Variables:")
print(importances)

# Guardar
pd.DataFrame([metrics]).to_csv(os.path.join(output_dir, "xg_final_regression_metrics.csv"), index=False)

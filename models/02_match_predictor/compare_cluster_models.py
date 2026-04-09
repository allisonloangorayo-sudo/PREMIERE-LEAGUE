import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, f1_score
import os

# --- CONFIGURACIÓN ---
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(base_path, "databases", "matches_with_clusters.csv")
output_dir = os.path.join(base_path, "models", "outputs")

print("Cargando datos con variables de clustering...")
df = pd.read_csv(data_path)

# Features originales + Nuevas de Clustering
original_features = [
    'home_avg_goals_for', 'away_avg_goals_for', 
    'home_form_points', 'away_form_points',
    'home_avg_sot_for', 'away_avg_sot_for',
    'goals_diff_form', 'sot_diff_form',
    'ref_home_win_rate',
    'implied_prob_h', 'implied_prob_d', 'implied_prob_a'
]

cluster_features = [
    'home_team_cluster', 'away_team_cluster',
    'orchestrator_diff', 'finisher_diff',
    'home_cluster_0_count', 'home_cluster_3_count',
    'away_cluster_0_count', 'away_cluster_3_count'
]

features = original_features + cluster_features

X = df[features].fillna(0)
le = LabelEncoder()
y = le.fit_transform(df['ftr']) # H=2, D=1, A=0

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Modelos
models = {
    "RF (With Clusters)": RandomForestClassifier(n_estimators=150, max_depth=7, random_state=42),
    "XGBoost (With Clusters)": XGBClassifier(n_estimators=100, learning_rate=0.03, max_depth=4, random_state=42)
}

results = []
for name, model in models.items():
    print(f"Evaluando {name}...")
    cv_acc = cross_val_score(model, scaler.fit_transform(X), y, cv=5).mean()
    
    model.fit(X_train_s, y_train)
    y_pred = model.predict(X_test_s)
    
    acc_test = accuracy_score(y_test, y_pred)
    f1_macro = f1_score(y_test, y_pred, average='macro')
    
    results.append({
        "Modelo": name,
        "CV Accuracy": cv_acc,
        "Test Accuracy": acc_test,
        "F1 Macro": f1_macro
    })

# --- COMPARACIÓN FINAL ---
df_res = pd.DataFrame(results).sort_values(by="CV Accuracy", ascending=False)
print("\n--- RESULTADOS CON VARIABLES DE CLUSTERING ---")
print(df_res.to_string(index=False))

# Visualizar importancia de variables para ver si el clustering sirvió
model_rf = models["RF (With Clusters)"]
importances = pd.Series(model_rf.feature_importances_, index=features).sort_values(ascending=False)

plt.figure(figsize=(10, 8))
importances.head(15).plot(kind='barh', color='skyblue')
plt.title("Top 15 Features (Incluyendo Clusters)")
plt.savefig(os.path.join(output_dir, "feature_importance_clusters.png"))

print(f"\nGráfica de importancia guardada en {output_dir}")

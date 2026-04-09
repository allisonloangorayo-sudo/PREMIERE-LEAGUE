import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

# --- PREPARACIÓN ---
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_path = os.path.join(base_path, "databases", "matches_with_clusters.csv")
output_dir = os.path.join(base_path, "models", "outputs", "regression")
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(data_path)

# Queremos predecir goles de Local y Visitante
# 1. Preparar Variables
features = [
    'home_avg_goals_for', 'away_avg_goals_for', 
    'home_form_points', 'away_form_points',
    'home_avg_sot_for', 'away_avg_sot_for',
    'home_team_cluster', 'away_team_cluster',   # Clusters Equipos
    'orchestrator_diff', 'finisher_diff'       # Clusters Jugadores
]

X = df[features].fillna(0)
y_home = df['fthg']
y_away = df['ftag']

def evaluate_regressor(X, y, title):
    print(f"\n--- Evaluando {title} ---")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        "Linear Regression": LinearRegression(),
        "Ridge": Ridge(),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=100, max_depth=6, random_state=42)
    }
    
    res = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        r2 = r2_score(y_test, preds)
        
        res.append({
            "Algoritmo": name,
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2
        })
    
    df_res = pd.DataFrame(res).sort_values(by="MAE")
    print(df_res.to_string(index=False))
    return df_res

# Comparar con Base (Mediana/Promedio)
def compare_with_baseline(y_test, y_pred):
    baseline_mae = mean_absolute_error(y_test, np.full_like(y_test, y_test.mean()))
    return baseline_mae

# 2. Ejecutar Home Goals
results_h = evaluate_regressor(X, y_home, "Goles de Local (FTHG)")
# 3. Ejecutar Away Goals
results_a = evaluate_regressor(X, y_away, "Goles de Visitante (FTAG)")

# Guardar Resultados
results_h.to_csv(os.path.join(output_dir, "home_goals_regression.csv"), index=False)
results_a.to_csv(os.path.join(output_dir, "away_goals_regression.csv"), index=False)
print(f"\nReportes de regresión guardados en: {output_dir}")

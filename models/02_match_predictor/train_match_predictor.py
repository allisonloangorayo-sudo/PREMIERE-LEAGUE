import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
base_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA"
data_path = os.path.join(base_path, "databases", "matches_enriched.csv")
output_dir = os.path.join(base_path, "models", "outputs")
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(data_path)

# Features para ambos modelos
features = [
    'home_avg_goals_for', 'away_avg_goals_for', 
    'home_form_points', 'away_form_points',
    'home_avg_sot_for', 'away_avg_sot_for',
    'goals_diff_form', 'sot_diff_form',
    'ref_home_win_rate',
    'implied_prob_h', 'implied_prob_d', 'implied_prob_a'
]

X = df[features].fillna(0)

# --- PARTE A: Regresión Lineal (Total de Goles) ---
print("\n--- PARTE A: PREDICCIÓN DE GOLES TOTALES ---")
y_goals = df['total_goals']

X_train_g, X_test_g, y_train_g, y_test_g = train_test_split(X, y_goals, test_size=0.2, random_state=42)

regressor = LinearRegression()
regressor.fit(X_train_g, y_train_g)
y_pred_g = regressor.predict(X_test_g)

print(f"MAE (Goles Totales): {mean_absolute_error(y_test_g, y_pred_g):.4f}")
print(f"R2 Score: {r2_score(y_test_g, y_pred_g):.4f}")

# --- PARTE B: Regresión Logística (Resultado H/D/A) ---
print("\n--- PARTE B: PREDICCIÓN DE RESULTADO (H/D/A) ---")
le = LabelEncoder()
y_res = le.fit_transform(df['ftr']) # H=2, D=1, A=0 (depende del orden alfabético)

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y_res, test_size=0.2, random_state=42, stratify=y_res)

# Escalado
scaler = StandardScaler()
X_train_r_scaled = scaler.fit_transform(X_train_r)
X_test_r_scaled = scaler.transform(X_test_r)

# Logística Multiclase
# lbfgs soporta multiclase de forma nativa
clf = LogisticRegression(solver='lbfgs', max_iter=1000, random_state=42)
clf.fit(X_train_r_scaled, y_train_r)

# Validación Cruzada
cv_scores = cross_val_score(clf, scaler.fit_transform(X), y_res, cv=5)
print(f"Accuracy (Validación Cruzada): {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

y_pred_r = clf.predict(X_test_r_scaled)
print(f"Accuracy en Test final: {accuracy_score(y_test_r, y_pred_r):.4f}")
print("\nReporte de Clasificación:")
print(classification_report(y_test_r, y_pred_r, target_names=le.classes_))

# Benchmark Bet365 (Comparación)
# Seleccionamos el resultado con mayor probabilidad implícita en el test set
df_test = df.loc[X_test_r.index]
b365_preds = df_test[['implied_prob_h', 'implied_prob_d', 'implied_prob_a']].idxmax(axis=1)
# Mapear 'implied_prob_h' -> 'H', etc.
b365_results = b365_preds.map({'implied_prob_h':'H', 'implied_prob_d':'D', 'implied_prob_a':'A'})
b365_accuracy = (b365_results == df_test['ftr']).mean()

print(f"\n--- BENCHMARK COMPARISON ---")
print(f"Accuracy de Bet365 (Market Favorite) en Test: {b365_accuracy:.4f}")
print(f"Accuracy de Nuestro Modelo en Test: {accuracy_score(y_test_r, y_pred_r):.4f}")

# Importancia de Variables en la Clasificación
importance = pd.DataFrame({'feature': features, 'coef': np.mean(np.abs(clf.coef_), axis=0)})
importance = importance.sort_values('coef', ascending=False)
print("\nTop 5 Variables más influyentes (Match Predictor):")
print(importance.head(5))

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, f1_score

# Configuración
base_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA"
data_path = os.path.join(base_path, "databases", "matches_enriched.csv")
output_dir = os.path.join(base_path, "models", "outputs")
os.makedirs(output_dir, exist_ok=True)

print("Cargando base de partidos enriquecida para comparación multimodelo...")
df = pd.read_csv(data_path)

# Features
features = [
    'home_avg_goals_for', 'away_avg_goals_for', 
    'home_form_points', 'away_form_points',
    'home_avg_sot_for', 'away_avg_sot_for',
    'goals_diff_form', 'sot_diff_form',
    'ref_home_win_rate',
    'implied_prob_h', 'implied_prob_d', 'implied_prob_a'
]

X = df[features].fillna(0)
le = LabelEncoder()
y = le.fit_transform(df['ftr']) # H=2, D=1, A=0 (en orden alfabético)

# Split 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Modelos para la competencia
models = {
    "Logistic Regression (Baseline)": LogisticRegression(solver='lbfgs', max_iter=1000, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42),
    "XGBoost": XGBClassifier(n_estimators=50, learning_rate=0.05, max_depth=3, random_state=42)
}

results = []
for name, model in models.items():
    print(f"Evaluando {name}...")
    # Validación Cruzada (Cv=5)
    cv_acc = cross_val_score(model, scaler.fit_transform(X), y, cv=5).mean()
    
    # Entrenamiento y Test
    model.fit(X_train_s, y_train)
    y_pred = model.predict(X_test_s)
    
    acc_test = accuracy_score(y_test, y_pred)
    f1_macro = f1_score(y_test, y_pred, average='macro')
    
    results.append({
        "Modelo": name,
        "CV Accuracy": cv_acc,
        "Test Accuracy": acc_test,
        "F1 Macro (Test)": f1_macro
    })

# --- COMPARACIÓN ---
df_res = pd.DataFrame(results).sort_values(by="CV Accuracy", ascending=False)
print("\n--- COMPARATIVO MATCH PREDICTOR (H/D/A) ---")
print(df_res.to_string(index=False))

# Guardar resultados
df_res.to_csv(os.path.join(output_dir, "model_comparison_match.csv"), index=False)

# Visualización
plt.figure(figsize=(10, 6))
sns.barplot(x="Modelo", y="CV Accuracy", data=df_res, palette="magma")
plt.axhline(0.498, color='red', linestyle='--', label='Bet365 (49.8%)')
plt.ylim(0.4, 0.65)
plt.title("Comparativa Match Predictor: CV Accuracy vs Bet365 Benchmark")
plt.legend()
plt.savefig(os.path.join(output_dir, "comparison_chart_match.png"))

print(f"\nReporte y gráfica guardados en {output_dir}")

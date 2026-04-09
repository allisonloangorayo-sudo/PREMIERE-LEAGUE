import pandas as pd
import numpy as np
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, log_loss, confusion_matrix

# Configuración de rutas
base_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA"
data_path = os.path.join(base_path, "models", "outputs", "xg_master_data.csv")
output_dir = os.path.join(base_path, "models", "outputs")
os.makedirs(output_dir, exist_ok=True)

print("Cargando dataset para comparación de modelos xG...")
df = pd.read_csv(data_path)

# --- INGENIERÍA DE VARIABLES (Consolidada) ---
df['distance'] = np.sqrt((100 - df['x'])**2 + (50 - df['y'])**2)
df['distance_squared'] = df['distance'] ** 2
dy1, dy2, dx = 46.34 - df['y'], 53.66 - df['y'], 100 - df['x']
df['visible_angle'] = np.abs(np.arctan2(dy2, dx) - np.arctan2(dy1, dx))

def parse_qualifiers(q_str):
    try:
        q_list = json.loads(q_str.replace("'", '"'))
        q_ids = [str(item.get('type', {}).get('value')) for item in q_list]
        return {'is_big_chance': '214' in q_ids, 'is_header': '15' in q_ids, 
                'is_penalty': '9' in q_ids, 'is_assisted': '29' in q_ids}
    except: return {'is_big_chance': False, 'is_header': False, 'is_penalty': False, 'is_assisted': False}

df = pd.concat([df, df['qualifiers'].apply(parse_qualifiers).apply(pd.Series)], axis=1)

features = ['distance', 'distance_squared', 'visible_angle', 'is_big_chance', 'is_header', 'is_penalty', 'is_assisted']
for p_var in ['ict_index', 'xG_per90', 'threat']:
    if p_var in df.columns:
        df[p_var] = df[p_var].fillna(df[p_var].median())
        features.append(p_var)

X = df[features].astype(float)
y = df['is_goal'].astype(int)

# Split 70/15/15
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.15, random_state=42, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.1765, random_state=42, stratify=y_temp)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s = scaler.transform(X_val)
X_test_s = scaler.transform(X_test)

# --- ENTRENAMIENTO DE MODELOS ---
models = {
    "Logistic Regression (Baseline)": LogisticRegression(class_weight='balanced', random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=200, class_weight='balanced', max_depth=10, random_state=42),
    "XGBoost": XGBClassifier(scale_pos_weight=(len(y)-sum(y))/sum(y), n_estimators=100, learning_rate=0.05, max_depth=5, random_state=42)
}

results = []
for name, model in models.items():
    print(f"Entrenando {name}...")
    model.fit(X_train_s, y_train)
    
    # Evaluar en Test
    y_prob = model.predict_proba(X_test_s)[:, 1]
    y_pred = (y_prob > 0.5).astype(int)
    
    results.append({
        "Modelo": name,
        "ROC-AUC": roc_auc_score(y_test, y_prob),
        "Recall": recall_score(y_test, y_pred),
        "Accuracy": accuracy_score(y_test, y_pred),
        "Log-Loss": log_loss(y_test, y_prob)
    })

# --- COMPARACIÓN CUANTITATIVA ---
df_res = pd.DataFrame(results).sort_values(by="ROC-AUC", ascending=False)
print("\n--- TABLA COMPARATIVA DE MODELOS xG ---")
print(df_res.to_string(index=False))

# Guardar comparación para el informe
df_res.to_csv(os.path.join(output_dir, "model_comparison_xg.csv"), index=False)

# Visualización comparativa ROC-AUC
plt.figure(figsize=(10, 6))
sns.barplot(x="Modelo", y="ROC-AUC", data=df_res, palette="viridis")
plt.ylim(0.5, 0.85)
plt.title("Comparativa de Desempeño: ROC-AUC por Modelo")
plt.savefig(os.path.join(output_dir, "comparison_chart_xg.png"))

print(f"\nReporte y gráfica guardados en {output_dir}")

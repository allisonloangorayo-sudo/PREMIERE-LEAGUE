import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de rutas
base_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA"
data_path = os.path.join(base_path, "models", "outputs", "xg_master_data.csv")
output_dir = os.path.join(base_path, "models", "outputs")
os.makedirs(output_dir, exist_ok=True)

print("Cargando dataset maestro para xG...")
df = pd.read_csv(data_path)

# --- 1. Ingeniería de Variables Espaciales y Creativas ---
print("Calculando métricas espaciales y nuevas features de ingeniería...")
# Distancia euclidiana al centro del arco (100, 50)
df['distance'] = np.sqrt((100 - df['x'])**2 + (50 - df['y'])**2)
df['distance_squared'] = df['distance'] ** 2

# Ángulo de tiro ajustado (ángulo visible del arco)
# Asumimos que los postes están en y=46.34 y y=53.66 (arco de 7.32m escalado a 100)
# Formula del ángulo entre dos puntos desde un tercer punto
dy1 = 46.34 - df['y']
dy2 = 53.66 - df['y']
dx = 100 - df['x']
angle1 = np.arctan2(dy1, dx)
angle2 = np.arctan2(dy2, dx)
df['visible_angle'] = np.abs(angle2 - angle1)

# Variables de tiempo (Presión del partido)
df['is_last_10_mins'] = (df['minute'] >= 80).astype(int)
df['is_first_10_mins'] = (df['minute'] <= 10).astype(int)

# --- 2. Parseo Ampliado de Qualifiers (JSON) ---
print("Extrayendo variables adicionales de los qualifiers...")
def parse_qualifiers(q_str):
    try:
        q_list = json.loads(q_str.replace("'", '"'))
        q_ids = [str(item.get('type', {}).get('value')) for item in q_list]
        return {
            'is_big_chance': '214' in q_ids,
            'is_header': '15' in q_ids,
            'is_penalty': '9' in q_ids,
            'is_right_foot': '20' in q_ids,
            'is_left_foot': '72' in q_ids,
            'is_assisted': '29' in q_ids,
            'is_regular_play': '22' in q_ids,
            'is_individual_play': '215' in q_ids
        }
    except:
        return {'is_big_chance': False, 'is_header': False, 'is_penalty': False, 
                'is_right_foot': False, 'is_left_foot': False, 'is_assisted': False,
                'is_regular_play': False, 'is_individual_play': False}

qualifiers_df = df['qualifiers'].apply(parse_qualifiers).apply(pd.Series)
df = pd.concat([df, qualifiers_df], axis=1)

# Feature de interacción: Jugador Peligroso en Jugada Asistida
# Si tenemos ict_index, lo imputamos y luego lo combinamos
if 'ict_index' in df.columns:
    df['ict_index'] = df['ict_index'].fillna(df['ict_index'].median())
    df['threat_assisted'] = df['ict_index'] * df['is_assisted'].astype(float)
else:
    df['threat_assisted'] = 0

# --- 3. Preparación de Datos ---
features = [
    'distance', 'distance_squared', 'visible_angle', 
    'is_big_chance', 'is_header', 'is_penalty', 'is_right_foot', 'is_left_foot', 
    'is_assisted', 'is_regular_play', 'is_individual_play',
    'is_last_10_mins', 'is_first_10_mins',
    'threat_assisted'
]

# Incluir variables de jugadores
for player_var in ['ict_index', 'price', 'xG_per90', 'influence', 'creativity', 'threat']:
    if player_var in df.columns:
        features.append(player_var)

print("Limpiando NaNs...")
df['distance'] = df['distance'].fillna(df['distance'].median())
df['distance_squared'] = df['distance_squared'].fillna(df['distance_squared'].median())
df['visible_angle'] = df['visible_angle'].fillna(df['visible_angle'].median())

for col in features:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# Filtrar df para las features y asegurar no nulos
df[features] = df[features].fillna(0)

X = df[features].astype(float)
y = df['is_goal'].astype(int)

# --- Split Train / Validation / Test (70% / 15% / 15%) ---
print("Dividiendo en Train, Validation y Test...")
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.15, random_state=42, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.1765, random_state=42, stratify=y_temp)
# 0.1765 de 85% es approx 15% del total.

print(f"Tamaño Train: {len(X_train)} | Validación: {len(X_val)} | Test: {len(X_test)}")

# Escalado de variables
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# --- 4. Entrenamiento del Modelo (Regresión Logística) ---
print("Entrenando Regresión Logística con peso balanceado...")
model = LogisticRegression(class_weight='balanced', random_state=42, max_iter=2000)
model.fit(X_train_scaled, y_train)

# --- 5. Evaluación en Validación ---
y_val_pred = model.predict(X_val_scaled)
y_val_prob = model.predict_proba(X_val_scaled)[:, 1]

print("\n--- RESULTADOS EN VALIDACIÓN ---")
print(f"Accuracy:  {accuracy_score(y_val, y_val_pred):.4f}")
print(f"Precision: {precision_score(y_val, y_val_pred):.4f}")
print(f"Recall:    {recall_score(y_val, y_val_pred):.4f}")
print(f"F1-Score:  {f1_score(y_val, y_val_pred):.4f}")
print(f"ROC-AUC:   {roc_auc_score(y_val, y_val_prob):.4f}")

# --- 6. Evaluación Final en Test ---
y_test_pred = model.predict(X_test_scaled)
y_test_prob = model.predict_proba(X_test_scaled)[:, 1]

print("\n--- RESULTADOS EN TEST ---")
print(f"Accuracy:  {accuracy_score(y_test, y_test_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_test_pred):.4f}")
print(f"Recall:    {recall_score(y_test, y_test_pred):.4f}")
print(f"F1-Score:  {f1_score(y_test, y_test_pred):.4f}")
print(f"ROC-AUC:   {roc_auc_score(y_test, y_test_prob):.4f}")

# Matriz de confusión Test
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_test_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges')
plt.title('Matriz de Confusión - xG (Set de Test)')
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.savefig(os.path.join(output_dir, 'confusion_matrix_xg_test.png'))

# Curva ROC Test
fpr, tpr, thresholds = roc_curve(y_test, y_test_prob)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc_score(y_test, y_test_prob):.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Falsos Positivos (FPR)')
plt.ylabel('Verdaderos Positivos (TPR)')
plt.title('Curva ROC - xG Model')
plt.legend(loc="lower right")
plt.savefig(os.path.join(output_dir, 'roc_curve_xg_test.png'))

print(f"\nGráficos generados en: {output_dir}")

# Mostrar importancia
coef_df = pd.DataFrame({'feature': features, 'coefficient': model.coef_[0]})
coef_df = coef_df.sort_values(by='coefficient', ascending=False)
print("\nImportancia de Variables (Coeficientes):")
print(coef_df)

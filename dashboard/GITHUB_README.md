# ⚽ Premier League Analytics & Prediction Portal 🏆

Este repositorio contiene el código fuente, el análisis de datos (EDA) y los modelos de Machine Learning desarrollados para el **Taller 2 de ML1** (Universidad Externado de Colombia).

**URL del Dashboard Desplegado:** [https://premier-predictor.vercel.app](https://premier-predictor.vercel.app)

---

## 👥 Integrantes
*   **Allison Loango Rayo** - Código: [Insertar Código]
*   **Danna [Apellido]** - Código: [Insertar Código]

---

## 🏗️ Resumen del Proyecto y Approach
El objetivo principal de este proyecto es superar las predicciones de las casas de apuestas (Bet365) mediante la integración de:
1.  **Modelo xG (Goles Esperados):** Un análisis geométrico y estadístico de cada disparo realizado en la temporada 2024-25.
2.  **Machine Learning No Supervisado (Clustering):** Segmentación de jugadores en roles tácticos (Finishers, Orchestrators, Engines) para enriquecer los modelos predictivos.
3.  **Match Predictor:** Un modelo de Random Forest que utiliza diferenciales de poder y racha de forma para predecir el resultado (H/D/A) de los partidos.

### Key Features:
*   **Cancha 3D Interactiva:** Simulador de probabilidad de gol basado en el modelo xG entrenado.
*   **Identificación de "Unicornios":** Uso de DBSCAN para detectar jugadores que desafían la probabilidad estadística (Haaland, Salah, Palmer).
*   **Internacionalización (i18n):** Dashboard completamente disponible en Español e Inglés.

---

## 📁 Estructura del Repositorio
*   `EDA/`: Scripts de Python (.py) y Notebooks (.ipynb) con el análisis exploratorio detallado de eventos, partidos y jugadores.
*   `models/`: Código de entrenamiento para los modelos xG, Match Predictor y Clustering.
*   `dashboard/`: Código fuente (HTML/CSS/JS) del portal analítico.
*   `databases/`: Datasets procesados utilizados para el entrenamiento.

---

## 🚀 Instrucciones de Ejecución

### Requisitos Previos
*   Python 3.10+
*   Node.js (opcional, para desarrollo del dashboard)

### Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### Ejecución de Notebooks/Scripts
1.  **EDA:** Ejecuta los scripts en la carpeta `EDA/` para generar los análisis visuales.
2.  **Entrenamiento:** Los modelos se encuentran en `models/`. Puedes volver a entrenarlos ejecutando:
    ```bash
    python models/01_xg_model/train_xg_model.py
    ```

### Ejecución del Dashboard Localmente
Simplemente abre el archivo `index.html` en tu navegador o utiliza un servidor local:
```bash
npx serve .
```

---

## 📊 Resultados Principales
*   **Accuracy del Modelo:** 61.8% (Superando el 49.8% de las casas de apuestas).
*   **ROC-AUC xG:** 0.81.
*   **MAE Regresión de Goles:** 0.74.

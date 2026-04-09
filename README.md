# ⚽ Premier League Analytics & Prediction Portal 🏆

Este repositorio contiene el código fuente, el análisis de datos (EDA) y los modelos de Machine Learning desarrollados para el **Taller 2 de ML1** (Universidad Externado de Colombia).

**URL del Dashboard Desplegado:** [https://premier-predictor.vercel.app](https://premier-predictor.vercel.app)

---

## 👥 Integrantes
*   **Allison Michelle Loango Rayo** - Código: `1094049458`
*   **Danna Vanessa Caballero Urrego** - Código: `1050092681`

---

## 🏗️ Resumen del Proyecto y Approach
Nuestra hipótesis principal fue comprobar que integrar el estilo de juego (Clustering) y la calidad individual (xG) en un modelo de Ensamble (Random Forest), puede superar de manera robusta al mercado de apuestas (cuyo benchmark de acierto cercano al 49.8% proviene de Bet365).

El enfoque implementado consistió en un sistema de **modelado en capas (ensembling y clustering)**:
1.  **Modelo xG (Goles Esperados):** Un análisis geométrico y estadístico de cada disparo realizado en la temporada 2024-25 utilizando un Random Forest capaz de captar no-linealidades.
2.  **Machine Learning No Supervisado (Clustering):** Segmentación de jugadores en roles tácticos invisibles (Ej. *The Finishers*, *The Orchestrators*) usando K-Means y detección de "unicornios" estadísticos con DBSCAN (Haaland, Salah).
3.  **Match Predictor:** Modelo predictivo agregado final que utiliza diferenciales de poder y la contabilidad de roles para predecir el resultado del partido (Home/Draw/Away).

### Key Features del Dashboard:
*   **Cancha 3D Interactiva:** Simulador de probabilidad de gol basado en el modelo xG entrenado.
*   **Ranking de Poder:** Visualización de la eficiencia real de cada equipo frente a los roles de sus jugadores basándose en el análisis algorítmico.
*   **Internacionalización (i18n):** Dashboard completamente disponible en Español e Inglés.

---

## 📁 Estructura del Repositorio
*   `Main_Notebook.ipynb`: Notebook principal para la ejecución centralizada del proyecto.
*   `EDA/`: Scripts de Python (.py) con el análisis exploratorio detallado de eventos, partidos y jugadores.
*   `models/`: Código de entrenamiento para los modelos xG, Match Predictor y Clustering.
*   `dashboard/`: Código fuente (HTML/CSS/JS) del portal analítico desplegado.
*   `databases/`: Datasets procesados utilizados para el entrenamiento.

---

## 🚀 Instrucciones de Ejecución

### Requisitos Previos
*   Python 3.9+
*   Jupyter Notebook (opcional para visualización de celdas)

### Instalación de Dependencias
Asegúrate de ejecutar:
```bash
pip install -r requirements.txt
```

### Ejecución de Notebooks/Scripts
Para mantener la estructura modular original, el proyecto central se puede explorar de dos formas:

1. **A través del Notebook Principal:** 
   Abre el archivo `Main_Notebook.ipynb` el cual tiene centralizados todos los pasos para ejecutarlos en orden lógico, mostrando los reportes de modelos y gráficas interactivas.

2. **Ejecución directa por módulos (.py):**
   * **EDA:** Ejecuta los scripts en la carpeta `EDA/` para generar los análisis visuales. Por ejemplo: `python EDA/generate_eda_plots.py`
   * **Entrenamiento:** Puedes correr los modelos por bloque: `python models/01_xg_model/compare_xg_models.py` o `python models/04_cluster_regression/train_match_regression.py`

### Ejecución del Dashboard Localmente
Simplemente abre el archivo `dashboard/index.html` en tu navegador o utiliza un servidor local:
```bash
cd dashboard
npx serve .
```

---

## 📊 Resultados Principales
*   **Accuracy del Modelo Predictor de Partidos:** 61.8% (Superando ampliamente el 49.8% de las casas de apuestas).
*   **ROC-AUC Modelo xG:** 0.81.
*   **MAE Regresión de Goles:** 0.74.

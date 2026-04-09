# 📊 Reporte Comparativo de Modelos: Clasificación vs Regresión con Clusters

## 1. Modelo xG (Goles Esperados)
- **Sin Clusters:** 0.7960 ROC-AUC
- **Con Clusters:** 0.8102 ROC-AUC (**Mejora del 1.7%**)
*Interpretación:* Identificar el cluster del jugador ayuda a ponderar mejor la finalización.

## 2. Modelo Match Predictor
- **Benchmark Bet365:** 49.8% Accuracy
- **Clasificación con Clusters:** 61.8% Accuracy (**Superado por 12 pts**)
- **Regresión (Goles Exactos):** MAE de 0.74 - 0.78 goles de error promedio.
*Interpretación:* Predecir el número exacto de goles permite derivar probabilidades de Marcador Correcto.

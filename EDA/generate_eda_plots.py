"""
Generador de Gráficos de Correlación EDA
Premier League 2025-26 | Taller 2 ML1

Ejecutar: python generate_eda_plots.py
Requiere: pandas, numpy, matplotlib, seaborn
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo visual
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 10)

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, '..', 'databases')
    PLOTS_PATH = os.path.join(BASE_DIR, 'plots')
    
    os.makedirs(PLOTS_PATH, exist_ok=True)
    
    print("Iniciando generación de gráficos de correlación...")
    
    # ---------------------------------------------------------
    # 1. MATCHES
    # ---------------------------------------------------------
    path_matches = os.path.join(DB_PATH, 'matches.csv')
    if os.path.exists(path_matches):
        print(" -> Procesando Matches...")
        df_matches = pd.read_csv(path_matches)
        
        # Filtramos solo numéricas clave para predecir
        cols_matches = [c for c in ['fthg', 'ftag', 'hs', 'as_', 'hst', 'ast', 'hf', 'af', 
                                    'hc', 'ac', 'total_goals', 'goal_diff', 'b365h', 'b365d', 'b365a'] if c in df_matches.columns]
        if cols_matches:
            corr_m = df_matches[cols_matches].corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_m, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True)
            plt.title('Matriz de Correlación - Partidos (Matches)', fontsize=15)
            plt.tight_layout()
            plt.savefig(os.path.join(PLOTS_PATH, 'corr_matches.png'), dpi=300)
            plt.close()
    
    # ---------------------------------------------------------
    # 2. PLAYERS
    # ---------------------------------------------------------
    path_players = os.path.join(DB_PATH, 'players.csv')
    if os.path.exists(path_players):
        print(" -> Procesando Players...")
        df_players = pd.read_csv(path_players)
        
        cols_players = [c for c in ['price', 'total_points', 'minutes', 'goals_scored', 'assists', 
                                    'clean_sheets', 'bonus', 'bps', 'xG', 'xA', 'ict_index'] if c in df_players.columns]
        if cols_players:
            corr_p = df_players[cols_players].corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_p, annot=True, fmt=".2f", cmap="viridis", cbar=True, square=True)
            plt.title('Matriz de Correlación - Jugadores (Players)', fontsize=15)
            plt.tight_layout()
            plt.savefig(os.path.join(PLOTS_PATH, 'corr_players.png'), dpi=300)
            plt.close()

    # ---------------------------------------------------------
    # 3. PLAYER HISTORY
    # ---------------------------------------------------------
    path_history = os.path.join(DB_PATH, 'player_history.csv')
    if os.path.exists(path_history):
        print(" -> Procesando Player History...")
        df_history = pd.read_csv(path_history)
        
        cols_history = [c for c in ['minutes', 'goals_scored', 'assists', 'total_points', 
                                    'expected_goals', 'expected_assists', 'influence', 
                                    'creativity', 'threat', 'value'] if c in df_history.columns]
        if cols_history:
            corr_ph = df_history[cols_history].corr()
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr_ph, annot=True, fmt=".2f", cmap="magma", cbar=True, square=True)
            plt.title('Matriz de Correlación - Historial Fantasy', fontsize=15)
            plt.tight_layout()
            plt.savefig(os.path.join(PLOTS_PATH, 'corr_history.png'), dpi=300)
            plt.close()
            
    # ---------------------------------------------------------
    # 4. EVENTS
    # ---------------------------------------------------------
    path_events = os.path.join(DB_PATH, 'events.csv')
    if os.path.exists(path_events):
        print(" -> Procesando Events (Tiros)...")
        # Por memoria y relevancia, cargaremos solo tiros si se puede
        df_events = pd.read_csv(path_events, usecols=['is_shot', 'is_goal', 'minute', 'x', 'y', 'goal_mouth_y', 'goal_mouth_z', 'is_touch'])
        shots = df_events[df_events['is_shot'] == True].copy()
        shots['distance'] = np.sqrt((100 - shots['x'])**2 + (50 - shots['y'])**2)
        shots['angle'] = np.degrees(np.arctan2(50 - shots['y'], 100 - shots['x']))
        
        cols_events = ['x', 'y', 'distance', 'angle', 'goal_mouth_y', 'goal_mouth_z', 'is_goal']
        corr_e = shots[cols_events].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_e, annot=True, fmt=".2f", cmap="Spectral", cbar=True, square=True)
        plt.title('Matriz de Correlación - Eventos (Tiros al arco)', fontsize=15)
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_PATH, 'corr_events.png'), dpi=300)
        plt.close()

    print(f"\n¡Éxito! Todas las gráficas se guardaron en: {PLOTS_PATH}")

if __name__ == '__main__':
    main()

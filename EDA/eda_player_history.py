"""
EDA - Dataset Player History
Premier League 2025-26 | Taller 2 ML1

Ejecutar: python eda_player_history.py
Requiere: pandas, numpy
"""

import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.float_format', '{:.2f}'.format)

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'databases')
history = pd.read_csv(os.path.join(DB_PATH, 'player_history.csv'))

# =============================================================================
# 1. ESTRUCTURA GENERAL
# =============================================================================
print('=' * 80)
print('1. ESTRUCTURA GENERAL DEL DATASET')
print('=' * 80)
print(f'Registros: {len(history):,}')
print(f'Columnas:  {len(history.columns)}')
print(f'Memoria:   {history.memory_usage(deep=True).sum()/1024/1024:.1f} MB')
print()
print('Tipos de datos:')
print(history.dtypes.to_string())
print()
print('Primeras 3 filas:')
print(history.head(3).to_string())

# =============================================================================
# 2. ANALISIS DE NULOS
# =============================================================================
print('\n' + '=' * 80)
print('2. ANALISIS DE NULOS')
print('=' * 80)
nulls = history.isnull().sum()
null_pct = (nulls / len(history) * 100).round(2)
null_df = pd.DataFrame({
    'nulos': nulls,
    'porcentaje': null_pct,
    'no_nulos': len(history) - nulls
})
null_df = null_df.sort_values('porcentaje', ascending=False)
print(null_df.to_string())

# =============================================================================
# 3. VALORES UNICOS POR VARIABLE CATEGORICA
# =============================================================================
print('\n' + '=' * 80)
print('3. VALORES UNICOS POR VARIABLE CATEGORICA')
print('=' * 80)
cat_cols = history.select_dtypes(include=['object', 'bool']).columns
for c in cat_cols:
    nuniq = history[c].nunique()
    top5 = history[c].value_counts().head(5)
    print(f'\n{c} ({nuniq} unicos):')
    for val, cnt in top5.items():
        print(f'  {val}: {cnt:,} ({cnt/len(history)*100:.1f}%)')

# =============================================================================
# 4. METRICAS DE TENDENCIA CENTRAL Y DISPERSION
# =============================================================================
print('\n' + '=' * 80)
print('4. METRICAS DE TENDENCIA CENTRAL Y DISPERSION')
print('=' * 80)
num_cols = history.select_dtypes(include=[np.number]).columns.tolist()
if 'player_id' in num_cols: num_cols.remove('player_id')
desc = history[num_cols].describe().T
desc['mediana'] = history[num_cols].median()
desc['moda'] = history[num_cols].mode().iloc[0]
desc['rango'] = desc['max'] - desc['min']
desc['CV'] = (desc['std'] / desc['mean'] * 100).replace([np.inf, -np.inf], np.nan)
desc['skew'] = history[num_cols].skew()
desc['kurtosis'] = history[num_cols].kurtosis()
print(desc[['count', 'mean', 'mediana', 'moda', 'std', 'min', '25%', '50%',
            '75%', 'max', 'rango', 'CV', 'skew', 'kurtosis']].to_string())

# =============================================================================
# 5. ANALISIS DE ATIPICOS (IQR)
# =============================================================================
print('\n' + '=' * 80)
print('5. ANALISIS DE ATIPICOS (metodo IQR)')
print('=' * 80)
for col in num_cols:
    data = history[col].dropna()
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = data[(data < lower) | (data > upper)]
    print(f'{col:>14}: Q1={Q1:.1f}, Q3={Q3:.1f}, IQR={IQR:.1f}, '
          f'Limites=[{lower:.1f}, {upper:.1f}], '
          f'Atipicos={len(outliers):,} ({len(outliers)/len(data)*100:.2f}%)')

# =============================================================================
# 6. DISTRIBUCION POR GAMEWEEK
# =============================================================================
print('\n' + '=' * 80)
print('6. DISTRIBUCION DE REGISTROS POR GAMEWEEK')
print('=' * 80)
if 'gameweek' in history.columns:
    et = history['gameweek'].value_counts().sort_index()
    for ev, cnt in et.items():
        pct = cnt / len(history) * 100
        bar = '#' * int(cnt // 15)
        print(f'  GW {ev:>2}: {cnt:>5,} ({pct:5.1f}%) {bar}')
else:
    print('  Columna gameweek no encontrada.')

# =============================================================================
# 7. GOLES Y ASISTENCIAS POR PARTIDO (SOLO MINUTOS > 0)
# =============================================================================
print('\n' + '=' * 80)
print('7. DISTRIBUCION DE GOLES Y ASISTENCIAS (Solo Jugaron)')
print('=' * 80)
if 'minutes' in history.columns:
    hm = history[history['minutes'] > 0]
    print(f"Partidos jugados analizados: {len(hm):,}")
    for col in ['goals_scored', 'assists']:
        if col in hm.columns:
            vc = hm[col].value_counts().sort_index()
            print(f'\n{col.upper()}:')
            for val, cnt in vc.items():
                print(f'  {val} {col}: {cnt:>5} partidos')

# =============================================================================
# 8. PUNTUACIONES MAXIMAS EN UN SOLO JUEGO (TOTAL_POINTS)
# =============================================================================
print('\n' + '=' * 80)
print('8. TOP 10 ACTUACIONES INDIVIDUALES POR PUNTOS (TOTAL_POINTS)')
print('=' * 80)
if 'total_points' in history.columns and 'web_name' in history.columns:
    top10_points = history.sort_values('total_points', ascending=False).head(10)
    print(top10_points[['web_name', 'gameweek', 'opponent', 'minutes', 'total_points', 'goals_scored', 'assists']].to_string(index=False))

# =============================================================================
# 9. CORRELACIONES GENERALES (variables numericas)
# =============================================================================
print('\n' + '=' * 80)
print('9. CORRELACIONES ENTRE VARIABLES NUMERICAS (Resumen)')
print('=' * 80)
corr_cols = [c for c in ['minutes', 'goals_scored', 'assists', 'clean_sheets',
                        'total_points', 'expected_goals', 'expected_assists', 
                        'influence', 'creativity', 'threat', 'value'] if c in history.columns]
if corr_cols:
    corr = history[corr_cols].corr()
    print(corr.to_string())

# =============================================================================
# 10. CORRELACIONES PARA TOTAL_POINTS EN UN MATCH
# =============================================================================
print('\n' + '=' * 80)
print('10. CORRELACIONES RELEVANTES PARA TOTAL_POINTS')
print('=' * 80)
if 'total_points' in history.columns and corr_cols:
    corr_pts = history[corr_cols].corr()['total_points'].sort_values(ascending=False)
    for feat, val in corr_pts.items():
        if feat != 'total_points':
            bar = '+' * int(abs(val) * 40) if val > 0 else '-' * int(abs(val) * 40)
            print(f'  {feat:<20} {val:>7.3f} {bar}')

# =============================================================================
# 11. PARTICIPACIONES: LOCAL VS VISITANTE (RENDIMIENTO)
# =============================================================================
print('\n' + '=' * 80)
print('11. RENDIMIENTO PROMEDIO: LOCAL VS VISITANTE')
print('=' * 80)
if 'was_home' in history.columns:
    perf = history.groupby('was_home')[['total_points', 'goals_scored', 'assists', 'expected_goals']].mean()
    perf.index = ['Visitante (0)', 'Local (1)']
    print(perf.to_string())

# =============================================================================
# 12. TOP ACTUACIONES POR EXPECTED_GOALS (xG)
# =============================================================================
print('\n' + '=' * 80)
print('12. TOP 10 ACTUACIONES POR XG (EXPECTED_GOALS)')
print('=' * 80)
if 'expected_goals' in history.columns and 'web_name' in history.columns:
    top10_xg = history.sort_values('expected_goals', ascending=False).head(10)
    print(top10_xg[['web_name', 'gameweek', 'opponent', 'expected_goals', 'goals_scored', 'total_points']].to_string(index=False))

# =============================================================================
# 13. DISTRIBUCION DE MINUTOS JUGADOS
# =============================================================================
print('\n' + '=' * 80)
print('13. DISTRIBUCION DE MINUTOS JUGADOS EN UN PARTIDO')
print('=' * 80)
if 'minutes' in history.columns:
    no_play = len(history[history['minutes'] == 0])
    subbed = len(history[(history['minutes'] > 0) & (history['minutes'] < 90)])
    full = len(history[history['minutes'] == 90])
    total = len(history)
    print(f"  0 min (Banca/No Jugo) : {no_play:>5} ({no_play/total*100:.1f}%)")
    print(f"  1-89 min (Sustitucion): {subbed:>5} ({subbed/total*100:.1f}%)")
    print(f"  90 min (Partido Compl): {full:>5} ({full/total*100:.1f}%)")

# =============================================================================
# 14. MAYORES TRANSFERENCIAS EN UNA GAMEWEEK
# =============================================================================
print('\n' + '=' * 80)
print('14. TOP MOVIMIENTOS DE TRANSFERENCIAS (IN Y OUT)')
print('=' * 80)
if 'transfers_in' in history.columns and 'web_name' in history.columns:
    print('Mayores Ingresos a Equipos (Transfers In):')
    top_in = history.sort_values('transfers_in', ascending=False).head(5)
    print(top_in[['web_name', 'gameweek', 'transfers_in', 'total_points']].to_string(index=False))
    
    print('\nMayores Salidas de Equipos (Transfers Out):')
    if 'transfers_out' in history.columns:
        top_out = history.sort_values('transfers_out', ascending=False).head(5)
        print(top_out[['web_name', 'gameweek', 'transfers_out', 'total_points']].to_string(index=False))

print('\n' + '=' * 80)
print('EDA PLAYER HISTORY COMPLETADO')
print('=' * 80)

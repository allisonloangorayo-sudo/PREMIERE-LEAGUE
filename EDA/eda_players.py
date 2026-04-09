"""
EDA - Dataset Players
Premier League 2025-26 | Taller 2 ML1

Ejecutar: python eda_players.py
Requiere: pandas, numpy
"""

import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.float_format', '{:.2f}'.format)

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'databases')
players = pd.read_csv(os.path.join(DB_PATH, 'players.csv'))

# =============================================================================
# 1. ESTRUCTURA GENERAL
# =============================================================================
print('=' * 80)
print('1. ESTRUCTURA GENERAL DEL DATASET')
print('=' * 80)
print(f'Registros: {len(players):,}')
print(f'Columnas:  {len(players.columns)}')
print(f'Memoria:   {players.memory_usage(deep=True).sum()/1024/1024:.1f} MB')
print()
print('Tipos de datos:')
print(players.dtypes.to_string())
print()
print('Primeras 3 filas:')
print(players.head(3).to_string())

# =============================================================================
# 2. ANALISIS DE NULOS
# =============================================================================
print('\n' + '=' * 80)
print('2. ANALISIS DE NULOS')
print('=' * 80)
nulls = players.isnull().sum()
null_pct = (nulls / len(players) * 100).round(2)
null_df = pd.DataFrame({
    'nulos': nulls,
    'porcentaje': null_pct,
    'no_nulos': len(players) - nulls
})
null_df = null_df.sort_values('porcentaje', ascending=False)
print(null_df.to_string())

# =============================================================================
# 3. VALORES UNICOS POR VARIABLE CATEGORICA
# =============================================================================
print('\n' + '=' * 80)
print('3. VALORES UNICOS POR VARIABLE CATEGORICA')
print('=' * 80)
cat_cols = players.select_dtypes(include=['object', 'bool']).columns
for c in cat_cols:
    nuniq = players[c].nunique()
    top5 = players[c].value_counts().head(5)
    print(f'\n{c} ({nuniq} unicos):')
    for val, cnt in top5.items():
        print(f'  {val}: {cnt:,} ({cnt/len(players)*100:.1f}%)')

# =============================================================================
# 4. METRICAS DE TENDENCIA CENTRAL Y DISPERSION
# =============================================================================
print('\n' + '=' * 80)
print('4. METRICAS DE TENDENCIA CENTRAL Y DISPERSION')
print('=' * 80)
num_cols = players.select_dtypes(include=[np.number]).columns.tolist()
if 'id' in num_cols: num_cols.remove('id')
desc = players[num_cols].describe().T
desc['mediana'] = players[num_cols].median()
desc['moda'] = players[num_cols].mode().iloc[0]
desc['rango'] = desc['max'] - desc['min']
desc['CV'] = (desc['std'] / desc['mean'] * 100).replace([np.inf, -np.inf], np.nan)
desc['skew'] = players[num_cols].skew()
desc['kurtosis'] = players[num_cols].kurtosis()
print(desc[['count', 'mean', 'mediana', 'moda', 'std', 'min', '25%', '50%',
            '75%', 'max', 'rango', 'CV', 'skew', 'kurtosis']].to_string())

# =============================================================================
# 5. ANALISIS DE ATIPICOS (IQR)
# =============================================================================
print('\n' + '=' * 80)
print('5. ANALISIS DE ATIPICOS (metodo IQR)')
print('=' * 80)
for col in num_cols:
    data = players[col].dropna()
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
# 6. DISTRIBUCION POR POSICION
# =============================================================================
print('\n' + '=' * 80)
print('6. DISTRIBUCION POR POSICION')
print('=' * 80)
if 'position' in players.columns:
    et = players['position'].value_counts()
    for ev, cnt in et.items():
        pct = cnt / len(players) * 100
        bar = '#' * int(pct * 2)
        print(f'  {ev:>25}: {cnt:>7,} ({pct:5.1f}%) {bar}')
else:
    print('  Columna position no encontrada.')

# =============================================================================
# 7. TOP 10 JUGADORES CON MAS TOTAL_POINTS
# =============================================================================
print('\n' + '=' * 80)
print('7. TOP 10 JUGADORES POR TOTAL_POINTS')
print('=' * 80)
if 'total_points' in players.columns and 'web_name' in players.columns:
    top10_points = players.sort_values('total_points', ascending=False).head(10)
    print(top10_points[['web_name', 'team_short', 'position', 'total_points', 'minutes']].to_string(index=False))

# =============================================================================
# 8. TOP 10 JUGADORES MAS CAROS (PRICE)
# =============================================================================
print('\n' + '=' * 80)
print('8. TOP 10 JUGADORES MAS CAROS (PRICE)')
print('=' * 80)
if 'price' in players.columns and 'web_name' in players.columns:
    top10_price = players.sort_values('price', ascending=False).head(10)
    print(top10_price[['web_name', 'team_short', 'position', 'price', 'total_points']].to_string(index=False))

# =============================================================================
# 9. CORRELACIONES GENERALES (variables numericas)
# =============================================================================
print('\n' + '=' * 80)
print('9. CORRELACIONES ENTRE VARIABLES NUMERICAS (Resumen)')
print('=' * 80)
corr_cols = [c for c in ['price', 'total_points', 'minutes', 'goals_scored', 'assists', 'clean_sheets',
                        'bonus', 'bps', 'xG', 'xA', 'ict_index'] if c in players.columns]
if corr_cols:
    corr = players[corr_cols].corr()
    print(corr.to_string())

# =============================================================================
# 10. CORRELACIONES PARA TOTAL_POINTS
# =============================================================================
print('\n' + '=' * 80)
print('10. CORRELACIONES RELEVANTES PARA TOTAL_POINTS')
print('=' * 80)
if 'total_points' in players.columns and corr_cols:
    corr_pts = players[corr_cols].corr()['total_points'].sort_values(ascending=False)
    for feat, val in corr_pts.items():
        if feat != 'total_points':
            bar = '+' * int(abs(val) * 40) if val > 0 else '-' * int(abs(val) * 40)
            print(f'  {feat:<20} {val:>7.3f} {bar}')

# =============================================================================
# 11. JUGADORES POR EQUIPO
# =============================================================================
print('\n' + '=' * 80)
print('11. JUGADORES INSCRITOS POR EQUIPO')
print('=' * 80)
if 'team_short' in players.columns:
    vc = players['team_short'].value_counts()
    for t, cnt in vc.items():
        print(f'  {t:<10}: {cnt:>3} jugadores')

# =============================================================================
# 12. TOP JUGADORES POR xG_per90 (Min 500 minutos jugados)
# =============================================================================
print('\n' + '=' * 80)
print('12. TOP JUGADORES POR xG_per90 (Minimo 500 min)')
print('=' * 80)
if 'xG_per90' in players.columns and 'minutes' in players.columns:
    q_players = players[players['minutes'] >= 500].sort_values('xG_per90', ascending=False).head(10)
    print(q_players[['web_name', 'team_short', 'position', 'xG_per90', 'goals_scored', 'minutes']].to_string(index=False))

# =============================================================================
# 13. JUGADORES MAS POPULARES (SELECTED_BY_PERCENT)
# =============================================================================
print('\n' + '=' * 80)
print('13. TOP 10 JUGADORES MAS SELECCIONADOS POR MANAGERS')
print('=' * 80)
if 'selected_by_percent' in players.columns:
    top_sel = players.sort_values('selected_by_percent', ascending=False).head(10)
    print(top_sel[['web_name', 'team_short', 'selected_by_percent', 'price', 'total_points']].to_string(index=False))

# =============================================================================
# 14. DISTRIBUCION DE ICT INDEX (INFLUENCE, CREATIVITY, THREAT)
# =============================================================================
print('\n' + '=' * 80)
print('14. DISTRIBUCION DE METRICAS ICT (Top 10 Index)')
print('=' * 80)
if 'ict_index' in players.columns:
    top_ict = players.sort_values('ict_index', ascending=False).head(10)
    print(top_ict[['web_name', 'team_short', 'ict_index', 'influence', 'creativity', 'threat']].to_string(index=False))

print('\n' + '=' * 80)
print('EDA PLAYERS COMPLETADO')
print('=' * 80)

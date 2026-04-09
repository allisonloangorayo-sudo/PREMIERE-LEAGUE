"""
EDA - Dataset Matches
Premier League 2025-26 | Taller 2 ML1

Ejecutar: python eda_matches.py
Requiere: pandas, numpy
"""

import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.float_format', '{:.2f}'.format)

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'databases')
matches = pd.read_csv(os.path.join(DB_PATH, 'matches.csv'))

# Converter date
matches['date'] = pd.to_datetime(matches['date'], format='%d/%m/%Y', errors='coerce')

# =============================================================================
# 1. ESTRUCTURA GENERAL
# =============================================================================
print('=' * 80)
print('1. ESTRUCTURA GENERAL DEL DATASET')
print('=' * 80)
print(f'Registros: {len(matches):,}')
print(f'Columnas:  {len(matches.columns)}')
print(f'Memoria:   {matches.memory_usage(deep=True).sum()/1024/1024:.1f} MB')
print()
print('Tipos de datos:')
print(matches.dtypes.to_string())
print()
print('Primeras 3 filas:')
print(matches.head(3).to_string())

# =============================================================================
# 2. ANALISIS DE NULOS
# =============================================================================
print('\n' + '=' * 80)
print('2. ANALISIS DE NULOS')
print('=' * 80)
nulls = matches.isnull().sum()
null_pct = (nulls / len(matches) * 100).round(2)
null_df = pd.DataFrame({
    'nulos': nulls,
    'porcentaje': null_pct,
    'no_nulos': len(matches) - nulls
})
null_df = null_df.sort_values('porcentaje', ascending=False)
print(null_df.to_string())

# =============================================================================
# 3. VALORES UNICOS POR VARIABLE CATEGORICA
# =============================================================================
print('\n' + '=' * 80)
print('3. VALORES UNICOS POR VARIABLE CATEGORICA')
print('=' * 80)
cat_cols = matches.select_dtypes(include=['object', 'bool']).columns
for c in cat_cols:
    nuniq = matches[c].nunique()
    top5 = matches[c].value_counts().head(5)
    print(f'\n{c} ({nuniq} unicos):')
    for val, cnt in top5.items():
        print(f'  {val}: {cnt:,} ({cnt/len(matches)*100:.1f}%)')

# =============================================================================
# 4. METRICAS DE TENDENCIA CENTRAL Y DISPERSION
# =============================================================================
print('\n' + '=' * 80)
print('4. METRICAS DE TENDENCIA CENTRAL Y DISPERSION')
print('=' * 80)
num_cols = matches.select_dtypes(include=[np.number]).columns.tolist()
if 'id' in num_cols: num_cols.remove('id')
desc = matches[num_cols].describe().T
desc['mediana'] = matches[num_cols].median()
desc['moda'] = matches[num_cols].mode().iloc[0]
desc['rango'] = desc['max'] - desc['min']
desc['CV'] = (desc['std'] / desc['mean'] * 100).replace([np.inf, -np.inf], np.nan)
desc['skew'] = matches[num_cols].skew()
desc['kurtosis'] = matches[num_cols].kurtosis()
print(desc[['count', 'mean', 'mediana', 'moda', 'std', 'min', '25%', '50%',
            '75%', 'max', 'rango', 'CV', 'skew', 'kurtosis']].to_string())

# =============================================================================
# 5. ANALISIS DE ATIPICOS (IQR)
# =============================================================================
print('\n' + '=' * 80)
print('5. ANALISIS DE ATIPICOS (metodo IQR)')
print('=' * 80)
for col in num_cols:
    data = matches[col].dropna()
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
# 6. DISTRIBUCION DE RESULTADOS (FTR)
# =============================================================================
print('\n' + '=' * 80)
print('6. DISTRIBUCION DE RESULTADOS (Full Time Result)')
print('=' * 80)
if 'ftr' in matches.columns:
    et = matches['ftr'].value_counts()
    for ev, cnt in et.items():
        pct = cnt / len(matches) * 100
        bar = '#' * int(pct * 2)
        print(f'  {ev:>25}: {cnt:>7,} ({pct:5.1f}%) {bar}')
else:
    print('  Columna ftr no encontrada.')

# =============================================================================
# 7. GOLES TOTALES POR PARTIDO
# =============================================================================
print('\n' + '=' * 80)
print('7. DISTRIBUCION DE GOLES TOTALES EN UN PARTIDO')
print('=' * 80)
if 'total_goals' in matches.columns:
    no_loc = matches['total_goals'].value_counts().sort_index()
    for ev, cnt in no_loc.items():
        pct = cnt / len(matches) * 100
        bar = '#' * int(pct * 2)
        print(f'  {ev} goles: {cnt:>7,} ({pct:5.1f}%) {bar}')

# =============================================================================
# 8. ANALISIS DE EQUIPO LOCAL VS VISITANTE
# =============================================================================
print('\n' + '=' * 80)
print('8. ANALISIS DE EQUIPO LOCAL VS VISITANTE')
print('=' * 80)
print("Promedios:")
metrics = [("Goles", "fthg", "ftag"), ("Tiros", "hs", "as_"), ("Tiros al arco", "hst", "ast"), 
           ("Faltas", "hf", "af"), ("Corners", "hc", "ac"), ("Tarjetas Amarillas", "hy", "ay")]

for label, h_col, a_col in metrics:
    if h_col in matches.columns and a_col in matches.columns:
        h_mean = matches[h_col].mean()
        a_mean = matches[a_col].mean()
        print(f"  {label:<20}: Local {h_mean:.2f} | Visitante {a_mean:.2f}")

# =============================================================================
# 9. CORRELACIONES GENERALES (variables numericas)
# =============================================================================
print('\n' + '=' * 80)
print('9. CORRELACIONES ENTRE VARIABLES NUMERICAS')
print('=' * 80)
corr_cols = [c for c in ['fthg', 'ftag', 'hs', 'as_', 'hst', 'ast', 'hf', 'af', 'hc', 'ac', 'total_goals', 'goal_diff'] if c in matches.columns]
if corr_cols:
    corr = matches[corr_cols].corr()
    print(corr.to_string())

# =============================================================================
# 10. CORRELACIONES PARA RESULTADO LOCAL (FTHG)
# =============================================================================
print('\n' + '=' * 80)
print('10. CORRELACIONES RELEVANTES PARA GOLES LOCAL (fthg)')
print('=' * 80)
if 'fthg' in matches.columns and corr_cols:
    corr_xg = matches[corr_cols].corr()['fthg'].sort_values(ascending=False)
    for feat, val in corr_xg.items():
        if feat != 'fthg':
            bar = '+' * int(abs(val) * 40) if val > 0 else '-' * int(abs(val) * 40)
            print(f'  {feat:<20} {val:>7.3f} {bar}')

# =============================================================================
# 11. PARTIDOS POR ARBITRO
# =============================================================================
print('\n' + '=' * 80)
print('11. ARBITROS CON MAS PARTIDOS')
print('=' * 80)
if 'referee' in matches.columns:
    refs = matches['referee'].value_counts().head(10)
    for r, c in refs.items():
        print(f'  {r:<25}: {c:>3} partidos')

# =============================================================================
# 12. DISTRIBUCION TEMPORAL (POR MES)
# =============================================================================
print('\n' + '=' * 80)
print('12. DISTRIBUCION TEMPORAL POR MES')
print('=' * 80)
if 'date' in matches.columns:
    matches['month'] = matches['date'].dt.to_period('M')
    vc = matches['month'].value_counts().sort_index()
    for m, cnt in vc.items():
        bar = '#' * int(cnt / 5)
        print(f'  {str(m):<10}: {cnt:>3} partidos {bar}')

# =============================================================================
# 13. EQUIPOS - RENDIMIENTO Y ESTADISTICAS
# =============================================================================
print('\n' + '=' * 80)
print('13. EQUIPOS - GOLES Y PUNTOS')
print('=' * 80)
if 'home_team' in matches.columns:
    home_stats = matches.groupby('home_team').agg(home_goals=('fthg','sum'), home_conceded=('ftag','sum'), home_matches=('id','count'))
    away_stats = matches.groupby('away_team').agg(away_goals=('ftag','sum'), away_conceded=('fthg','sum'), away_matches=('id','count'))
    team_stats = home_stats.join(away_stats, how='outer').fillna(0)
    team_stats['total_goals'] = team_stats['home_goals'] + team_stats['away_goals']
    team_stats['total_conceded'] = team_stats['home_conceded'] + team_stats['away_conceded']
    team_stats = team_stats.sort_values('total_goals', ascending=False)
    print(team_stats[['total_goals', 'total_conceded', 'home_goals', 'away_goals']].head(15).to_string())

# =============================================================================
# 14. CUOTAS PROBABILIDAD (BET365)
# =============================================================================
print('\n' + '=' * 80)
print('14. ANALISIS DE CUOTAS Y PROBABILIDADES (Bet365)')
print('=' * 80)
for c in ['implied_prob_h', 'implied_prob_d', 'implied_prob_a']:
    if c in matches.columns:
        desc = matches[c].describe()
        print(f'  {c:<20}: media {desc["mean"]*100:.1f}%, min {desc["min"]*100:.1f}%, max {desc["max"]*100:.1f}%')

print('\n' + '=' * 80)
print('EDA MATCHES COMPLETADO')
print('=' * 80)

"""
EDA - Dataset Events
Premier League 2025-26 | Taller 2 ML1
444,252 eventos de 291 partidos

Ejecutar: python eda_events.py
Requiere: pandas, numpy
"""

import pandas as pd
import numpy as np
import ast
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.float_format', '{:.2f}'.format)

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'databases')
events = pd.read_csv(os.path.join(DB_PATH, 'events.csv'))

# =============================================================================
# 1. ESTRUCTURA GENERAL
# =============================================================================
print('=' * 80)
print('1. ESTRUCTURA GENERAL DEL DATASET')
print('=' * 80)
print(f'Registros: {len(events):,}')
print(f'Columnas:  {len(events.columns)}')
print(f'Memoria:   {events.memory_usage(deep=True).sum()/1024/1024:.1f} MB')
print()
print('Tipos de datos:')
print(events.dtypes.to_string())
print()
print('Primeras 3 filas:')
print(events.head(3).to_string())

# =============================================================================
# 2. ANALISIS DE NULOS
# =============================================================================
print('\n' + '=' * 80)
print('2. ANALISIS DE NULOS')
print('=' * 80)
nulls = events.isnull().sum()
null_pct = (nulls / len(events) * 100).round(2)
null_df = pd.DataFrame({
    'nulos': nulls,
    'porcentaje': null_pct,
    'no_nulos': len(events) - nulls
})
null_df = null_df.sort_values('porcentaje', ascending=False)
print(null_df.to_string())

# =============================================================================
# 3. VALORES UNICOS POR VARIABLE CATEGORICA
# =============================================================================
print('\n' + '=' * 80)
print('3. VALORES UNICOS POR VARIABLE CATEGORICA')
print('=' * 80)
cat_cols = events.select_dtypes(include=['object', 'bool']).columns
for c in cat_cols:
    if c == 'qualifiers':
        print(f'\n{c}: (JSON array - ver seccion 8)')
        continue
    nuniq = events[c].nunique()
    top5 = events[c].value_counts().head(5)
    print(f'\n{c} ({nuniq} unicos):')
    for val, cnt in top5.items():
        print(f'  {val}: {cnt:,} ({cnt/len(events)*100:.1f}%)')

# =============================================================================
# 4. METRICAS DE TENDENCIA CENTRAL Y DISPERSION
# =============================================================================
print('\n' + '=' * 80)
print('4. METRICAS DE TENDENCIA CENTRAL Y DISPERSION')
print('=' * 80)
num_cols = ['minute', 'second', 'x', 'y', 'end_x', 'end_y',
            'goal_mouth_y', 'goal_mouth_z']
desc = events[num_cols].describe().T
desc['mediana'] = events[num_cols].median()
desc['moda'] = events[num_cols].mode().iloc[0]
desc['rango'] = desc['max'] - desc['min']
desc['CV'] = (desc['std'] / desc['mean'] * 100)
desc['skew'] = events[num_cols].skew()
desc['kurtosis'] = events[num_cols].kurtosis()
print(desc[['count', 'mean', 'mediana', 'moda', 'std', 'min', '25%', '50%',
            '75%', 'max', 'rango', 'CV', 'skew', 'kurtosis']].to_string())

# =============================================================================
# 5. ANALISIS DE ATIPICOS (IQR)
# =============================================================================
print('\n' + '=' * 80)
print('5. ANALISIS DE ATIPICOS (metodo IQR)')
print('=' * 80)
for col in num_cols:
    data = events[col].dropna()
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
# 6. DISTRIBUCION DE EVENT_TYPE (39 tipos)
# =============================================================================
print('\n' + '=' * 80)
print('6. DISTRIBUCION POR EVENT_TYPE (39 tipos)')
print('=' * 80)
et = events['event_type'].value_counts()
for ev, cnt in et.items():
    pct = cnt / len(events) * 100
    bar = '#' * int(pct * 2)
    print(f'  {ev:>25}: {cnt:>7,} ({pct:5.1f}%) {bar}')

# =============================================================================
# 7. EVENTOS SIN UBICACION (x=0, y=0)
# =============================================================================
print('\n' + '=' * 80)
print('7. EVENTOS SIN UBICACION (x=0, y=0)')
print('=' * 80)
no_loc = events[(events['x'] == 0) & (events['y'] == 0)]
print(f'Total eventos con x=0 y y=0: {len(no_loc):,} ({len(no_loc)/len(events)*100:.1f}%)')
print('Tipos:')
print(no_loc['event_type'].value_counts().to_string())

# =============================================================================
# 8. ANALISIS DE QUALIFIERS (114 tipos)
# =============================================================================
print('\n' + '=' * 80)
print('8. ANALISIS DE QUALIFIERS (La mina de oro)')
print('=' * 80)
qualifier_types = {}
for q_str in events['qualifiers']:
    try:
        q_list = ast.literal_eval(q_str) if isinstance(q_str, str) else []
        for q in q_list:
            qtype = q.get('type', {}).get('displayName', 'Unknown')
            if qtype not in qualifier_types:
                qualifier_types[qtype] = {'count': 0, 'has_value': 0, 'sample_value': None}
            qualifier_types[qtype]['count'] += 1
            if 'value' in q:
                qualifier_types[qtype]['has_value'] += 1
                if qualifier_types[qtype]['sample_value'] is None:
                    qualifier_types[qtype]['sample_value'] = q['value']
    except:
        pass

sorted_q = sorted(qualifier_types.items(), key=lambda x: x[1]['count'], reverse=True)
print(f'Total qualifier types: {len(sorted_q)}')
print(f'{"Qualifier":<30} {"Frecuencia":>10} {"Con valor":>10} {"Ejemplo":<30}')
print('-' * 85)
for name, info in sorted_q:
    print(f'{name:<30} {info["count"]:>10,} {info["has_value"]:>10,} '
          f'{str(info["sample_value"])[:30]:<30}')

# =============================================================================
# 9. CORRELACIONES GENERALES (variables numericas)
# =============================================================================
print('\n' + '=' * 80)
print('9. CORRELACIONES ENTRE VARIABLES NUMERICAS')
print('=' * 80)
corr_cols = ['minute', 'second', 'x', 'y', 'end_x', 'end_y',
             'goal_mouth_y', 'goal_mouth_z', 'is_touch', 'is_shot', 'is_goal']
corr = events[corr_cols].corr()
print(corr.to_string())

# =============================================================================
# 10. CORRELACIONES PARA xG (solo tiros)
# =============================================================================
print('\n' + '=' * 80)
print('10. CORRELACIONES RELEVANTES PARA xG (solo tiros)')
print('=' * 80)
shots = events[events['is_shot'] == True].copy()
shots['distance'] = np.sqrt((100 - shots['x'])**2 + (50 - shots['y'])**2)
shots['angle'] = np.degrees(np.arctan2(50 - shots['y'], 100 - shots['x']))


def has_qualifier(q_str, name):
    try:
        ql = ast.literal_eval(q_str) if isinstance(q_str, str) else []
        return int(any(q.get('type', {}).get('displayName', '') == name for q in ql))
    except:
        return 0


for q_name in ['BigChance', 'Head', 'RightFoot', 'LeftFoot', 'Penalty',
               'FastBreak', 'FromCorner', 'Volley', 'FirstTouch', 'RegularPlay']:
    shots[f'q_{q_name}'] = shots['qualifiers'].apply(lambda x: has_qualifier(x, q_name))

xg_features = ['distance', 'angle', 'x', 'y', 'is_goal',
               'q_BigChance', 'q_Head', 'q_RightFoot', 'q_LeftFoot',
               'q_Penalty', 'q_FastBreak', 'q_FromCorner', 'q_Volley',
               'q_FirstTouch', 'q_RegularPlay']

corr_xg = shots[xg_features].corr()['is_goal'].sort_values(ascending=False)
print('Correlacion con is_goal (tiros):')
for feat, val in corr_xg.items():
    bar = '+' * int(abs(val) * 40) if val > 0 else '-' * int(abs(val) * 40)
    print(f'  {feat:<20} {val:>7.3f} {bar}')

# =============================================================================
# 11. TIROS POR ZONA DE DISPARO
# =============================================================================
print('\n' + '=' * 80)
print('11. TIROS POR ZONA DE DISPARO')
print('=' * 80)
bins = [
    (0, 66, 'Fuera del final third'),
    (66, 83, 'Final third (fuera area)'),
    (83, 94, 'Penalty area'),
    (94, 100, '6-yard box'),
]
for lo, hi, label in bins:
    zone = shots[(shots['x'] >= lo) & (shots['x'] < hi)]
    goals = zone['is_goal'].sum()
    conv = goals / len(zone) * 100 if len(zone) > 0 else 0
    print(f'  {label:<30}: {len(zone):>5} tiros, {goals:>4} goles, '
          f'conversion {conv:.1f}%')

# =============================================================================
# 12. DISTRIBUCION TEMPORAL
# =============================================================================
print('\n' + '=' * 80)
print('12. DISTRIBUCION TEMPORAL')
print('=' * 80)
print('Por periodo:')
for period in ['FirstHalf', 'SecondHalf']:
    p = events[events['period'] == period]
    print(f'  {period}: {len(p):>7,} eventos ({len(p)/len(events)*100:.1f}%)')

print('\nGoles por intervalo de 15 min:')
goals_df = events[events['is_goal'] == True]
for lo in range(0, 105, 15):
    hi = lo + 15
    g = goals_df[(goals_df['minute'] >= lo) & (goals_df['minute'] < hi)]
    bar = '#' * (len(g) // 2)
    print(f'  {lo:>3}-{hi:<3} min: {len(g):>3} goles {bar}')

# =============================================================================
# 13. EQUIPOS - EVENTOS Y GOLES
# =============================================================================
print('\n' + '=' * 80)
print('13. EQUIPOS - EVENTOS Y GOLES')
print('=' * 80)
team_stats = events.groupby('team_name').agg(
    eventos=('id', 'count'),
    tiros=('is_shot', 'sum'),
    goles=('is_goal', 'sum')
).sort_values('goles', ascending=False)
team_stats['conversion'] = (team_stats['goles'] / team_stats['tiros'] * 100).round(1)
print(team_stats.to_string())

# =============================================================================
# 14. PARTIDOS CUBIERTOS
# =============================================================================
print('\n' + '=' * 80)
print('14. COBERTURA DE PARTIDOS')
print('=' * 80)
print(f'Match IDs: {events["match_id"].min()} a {events["match_id"].max()}')
print(f'Partidos unicos: {events["match_id"].nunique()}')
events_per_match = events.groupby('match_id').size()
print(f'Eventos por partido: min={events_per_match.min()}, '
      f'max={events_per_match.max()}, media={events_per_match.mean():.0f}, '
      f'mediana={events_per_match.median():.0f}')

print('\n' + '=' * 80)
print('EDA EVENTS COMPLETADO')
print('=' * 80)

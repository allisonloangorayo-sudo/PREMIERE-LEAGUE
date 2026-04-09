import csv
import json
import os

# Configuración de rutas
DB_PATH = r'c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\TALLER 2 ALLISON Y DANNA\databases'
OUTPUT_PATH = r'c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\ml-dashboard-copy\src\pitch_data.js'

print("--- Procesando events.csv (Streaming line-by-line) ---")

pitch_data = {}

try:
    with open(os.path.join(DB_PATH, 'events.csv'), 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            team = row['team_name']
            if not team: continue
            
            if team not in pitch_data:
                pitch_data[team] = {
                    'goals': [],
                    'shots': [],
                    'player_pos': {}
                }
            
            x = float(row['x']) if row['x'] else 0
            y = float(row['y']) if row['y'] else 0
            
            # 1. Goles
            if row['is_goal'].lower() == 'true':
                pitch_data[team]['goals'].append([x, y])
            
            # 2. Tiros
            if row['is_shot'].lower() == 'true':
                pitch_data[team]['shots'].append([x, y, row['outcome']])
            
            # 3. Posiciones
            player = row['player_name']
            if player:
                if player not in pitch_data[team]['player_pos']:
                    pitch_data[team]['player_pos'][player] = {'sum_x': 0, 'sum_y': 0, 'count': 0}
                pitch_data[team]['player_pos'][player]['sum_x'] += x
                pitch_data[team]['player_pos'][player]['sum_y'] += y
                pitch_data[team]['player_pos'][player]['count'] += 1

    # Finalizar cálculos y limitar datos
    final_data = {}
    for team, data in pitch_data.items():
        p_positions = []
        # Top 11 jugadores por equipo
        sorted_players = sorted(data['player_pos'].items(), key=lambda x: x[1]['count'], reverse=True)[:11]
        for player, stats in sorted_players:
            p_positions.append({
                'name': player,
                'x': round(stats['sum_x'] / stats['count'], 2),
                'y': round(stats['sum_y'] / stats['count'], 2)
            })
            
        final_data[team] = {
            'goals': data['goals'][:100],  # Limitar para rendimiento SVG
            'shots': data['shots'][:100],
            'player_positions': p_positions
        }

    # Guardar JS
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(f"const PITCH_DATA = {json.dumps(final_data)};")
    
    print(f"--- Éxito: Datos guardados en {OUTPUT_PATH} ---")

except Exception as e:
    print(f"Error procesando CSV: {e}")

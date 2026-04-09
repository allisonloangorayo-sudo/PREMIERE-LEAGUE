import pandas as pd

events_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\databases\events.csv"
players_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\databases\players.csv"
output_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\databases\xg_master_data.csv"

# Leer eventos en fragmentos para filtrar solo los tiros (is_shot == True)
print("Filtrando eventos (is_shot=True)...")
chunks = pd.read_csv(events_path, chunksize=50000)
shots_list = []
for chunk in chunks:
    shots_chunk = chunk[chunk['is_shot'] == True].copy()
    shots_list.append(shots_chunk)

df_shots = pd.concat(shots_list)
print(f"Total de tiros hallados: {len(df_shots)}")

# Leer jugadores
print("Cargando datos de jugadores...")
df_players = pd.read_csv(players_path)

# Crear la columna de nombre completo para el match
df_players['full_name_pl'] = df_players['first_name'] + " " + df_players['second_name']

# Normalización simple de nombres para mejorar el cruce
def normalize_name(name):
    if pd.isna(name): return ""
    # Remover tildes o caracteres especiales básicos si es necesario, 
    # por ahora solo minúsculas y quitar espacios extra
    return str(name).lower().strip()

df_shots['name_clean'] = df_shots['player_name'].apply(normalize_name)
df_players['name_clean'] = df_players['full_name_pl'].apply(normalize_name)

# Seleccionar columnas relevantes de jugadores
player_features = ['name_clean', 'price', 'ict_index', 'xG_per90', 'threat', 'creativity', 'influence']
df_players_sub = df_players[player_features].drop_duplicates(subset='name_clean')

# Unir con los tiros (Merge) por nombre normalizado
print("Fusionando bases de datos por nombre...")
df_master = pd.merge(df_shots, df_players_sub, on='name_clean', how='left')

# Si no hay match por nombre completo, intentarlo con web_name para casos como "Haaland"
web_name_sub = df_players[['web_name', 'price', 'ict_index', 'xG_per90', 'threat', 'creativity', 'influence']].copy()
web_name_sub['name_clean'] = web_name_sub['web_name'].apply(normalize_name)
web_name_sub = web_name_sub.drop_duplicates(subset='name_clean')

# Llenar algunos NaNs usando web_name
df_master = df_master.set_index('name_clean')
web_name_dict = web_name_sub.set_index('name_clean').to_dict('index')

for idx, row in df_master[df_master['price'].isna()].iterrows():
    if idx in web_name_dict:
        for col in ['price', 'ict_index', 'xG_per90', 'threat', 'creativity', 'influence']:
            df_master.at[idx, col] = web_name_dict[idx][col]

df_master = df_master.reset_index()

# Guardar el CSV maestro
df_master.to_csv(output_path, index=False)
print(f"Dataset maestro guardado con {df_master['price'].notna().sum()} matches de jugadores.")

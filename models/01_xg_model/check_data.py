import pandas as pd
import json

events_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\databases\events.csv"
players_path = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\databases\players.csv"

print("--- EVENTS ---")
df_events = pd.read_csv(events_path, nrows=10)
print(df_events.columns.tolist())
print(df_events[['player_id', 'is_shot', 'qualifiers']].head(2))

print("\n--- PLAYERS ---")
df_players = pd.read_csv(players_path, nrows=5)
print(df_players.columns.tolist())
print(df_players[['id', 'price', 'ict_index', 'xG_per90']].head(2))

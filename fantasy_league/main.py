# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:56:53 2024

@author: matte
"""


import pandas as pd
from player import Player
from team import Team
from league import League
import random

df = pd.read_csv("players.csv", sep = ";")

players = {}
for i in range(len(df)):
    player_name = f'player{i}'
    players[player_name] = Player(df.Name[i], df.Skill_level[i])

team1 = Team("Girondins")
team1.__str__()
team2 = Team("TFC")
team2.__str__()
team3 = Team("Sucy-en-Brie")
team3.__str__()
team4 = Team("Lens")
team4.__str__()

# Créer une liste des équipes
teams = [team1, team2, team3, team4]

# Obtenir les clés des joueurs
player_keys = list(players.keys())

# Tirage aléatoire et distribution des joueurs aux équipes
for i in range(3):
    # Tirer aléatoirement un groupe de 3 joueurs et les ajouter à l'équipe correspondante
    draw = random.sample(player_keys, 3)
    for p in draw:
        teams[i].add_player(players[p])
    
    # Supprimer les joueurs déjà tirés de la liste
    player_keys = [player for player in player_keys if player not in draw]

# Ajouter les joueurs restants à la dernière équipe
for p in player_keys:
    teams[3].add_player(players[p])

league = League(teams)
league.play_season()
league.get_results()

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:56:37 2024

@author: matte
"""
from typing import List, Dict
class League:
    teams : List[Team]
    scores: Dict[str, int]

    def __init__(self, teams = []):
        self.teams=teams

        #pour chaque team, on initialise le score à 0
        for t in teams:
            self.scores[t.team_name] = 0

    def simulate_game(self, team_1 : Team, team_2: Team):
        ##on pourrait vérifier que les teams sont bien dans la league

        ##on calcule le skill moyen des joueurs
        skill_1 = 0 
        for i in range(len(team_1.players) - 1):
            skill_1 += team_1.players[i].skill_level
        skill_1 = skill_1/len(team_1.players)

        skill_2 = 0 
        for i in range(len(team_2.players) - 1):
            skill_2 += team_2.players[i].skill_level
        skill_2 = skill_2/len(team_2.players)


        ##on pourrait également ajouter de la randomness

        ##on ajoute des points à la team en fonction du skill moyen 
        if(skill_1 > skill_2):
            self.scores[team_1.team_name] += 3
        elif(skill_1 < skill_2):
            self.scores[team_2.team_name] += 3
        else:
            self.scores[team_1.team_name] += 1
            self.scores[team_2.team_name] += 1

    def play_season(self):
        for i in range(len(self.teams)-1):
            for j in range(i+1,len(self.teams)-1):
                simulate_game(self.teams[i], self.teams[j])

    def get_results(self):
        for i in range(self.teams):
            print(f"The team {i.team_name} has a score of {self.scores[i.team_name]}")
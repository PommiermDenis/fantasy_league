# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:56:07 2024

@author: matte
"""
from typing import List

class Team:
    team_name:str
    players:List[Player]
    
    def __init__(self, team_name, players=[]):
        self.team_name = team_name
        self.players = players
    
    def add_player(self, player:Player):
        self.players.append(player)
        print(f"The player {player} was added to the team {self.team_name}")
    
    def remove_player(self, player:Player):
        if player in self.players:
            self.players.remove(player)
            print(f"The player {player.name} was removed from the team {self.team_name}.")
        else:
            print(f"The player {player} is not in the team {self.team_name}.")
    
    def __str__(self):
        return f"The team {self.team_name} has {', '.join(self.players)}"

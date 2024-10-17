# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 08:56:21 2024

@author: matte
"""

class Player:

    def __init__(self, name, skill_level = 0):
        self.name = name
        self.skill_level = skill_level
    
    def __str__(self):
        return f"The player {self.name} has a skill level of {self.skill_level}"


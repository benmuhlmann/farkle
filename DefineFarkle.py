# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:10:21 2020

@author: benmu
"""
from random import randint
from collections import defaultdict

class Roll:
    def __init__(self, dice):
        self.dice = dice
        self.score = 0
        self.face_dict = defaultdict(int)
        for face in range(1,7):
            self.face_dict[face]
            
    def roll_dice(self):
        for i in range(self.dice):
            self.face_dict[randint(1,6)] += 1
        

        
        
class Turn:
    def __init__(self):
        self.dice = 6
        self.score = 0
        self.turns = 0
        
    
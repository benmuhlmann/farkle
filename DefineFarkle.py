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
        self.reverse_dict = defaultdict(list)
        for face in range(1, 7):
            self.face_dict[face]

    def roll_dice(self):
        for i in range(self.dice):
            die_roll = randint(1, 6)
            self.face_dict[die_roll] += 1
        for key, value in self.face_dict.items():
            self.reverse_dict[value].append(key)

    def six_of_a_kind(self):
        if 6 in self.reverse_dict.keys():
            return(True)
        else:
            return(False)

    def five_of_a_kind(self):
        if 5 in self.reverse_dict.keys():
            return(True)
        else:
            return(False)

    def four_of_a_kind(self):
        if 4 in self.reverse_dict.keys():
            return(True)
        else:
            return(False)
    
    # will create an empty list of triplets if none appeared (defaultdict)
    def num_triplets(self):
        return(len(self.reverse_dict[3]))
        
    def num_pairs(self):
        return(len(self.reverse_dict[2]))

    def one_through_six(self):
        if len(self.reverse_dict[1]) == 6:
            return(True)
        else:
            return(False)
            
    def score_roll(self):
        if self.one_through_six():
            self.score = 1500
            return
        if self.six_of_a_kind():
            self.score = 3000
            return
        if self.five_of_a_kind():
            self.score = 2000
        if self.four_of_a_kind():
            if self.num_pairs == 1:
                self.score = 1500
                return
            else:
                self.score = 1000
        if self.num_triplets() == 2:
            self.score = 2500
            return
        if self.num_triplets() == 1:
            self.score = 100*self.reverse_dict[3][0]
        if self.num_pairs == 3:
            self.score = 1500
            return
        if self.face_dict[1] < 3:
            self.score += 100*self.face_dict[1]
        if self.face_dict[5] < 3:
            self.score += 50*self.face_dict[5]
        return
     
     
class Turn:
    def __init__(self):
        self.dice = 6
        self.score = 0
        self.rolls = 0

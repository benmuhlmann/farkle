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
        self.scoring_dice = 0
        self.farkled = False
        self.face_dict = defaultdict(int)
        self.reverse_dict = defaultdict(list)
        for face in range(1, 7):
            self.face_dict[face]

        self.roll_dice()
        self.score_roll()
        self.farkle_check()

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
        """
        Score a roll. Order of Checks:
        one through six, six of a kind,
        five of a kind, four of a kind with a pair,
        four of a kind, and so on.

        Return and stop the checking process
        if a scenario rules out the possibility
        of further scoring (e.g. four of a kind and a pair)
        """
        if self.one_through_six():
            self.score = 1500
            self.scoring_dice = 6
            return
        if self.six_of_a_kind():
            self.score = 3000
            self.scoring_dice = 6
            return
        if self.five_of_a_kind():
            self.score = 2000
            self.scoring_dice = 5
        if self.four_of_a_kind():
            if self.num_pairs == 1:
                self.score = 1500
                self.scoring_dice = 6
                return
            else:
                self.score = 1000
                self.scoring_dice = 4
        if self.num_triplets() == 2:
            self.score = 2500
            self.scoring_dice = 6
            return
        if self.num_triplets() == 1:
            self.score = 100*self.reverse_dict[3][0]
            self.scoring_dice = 3
        if self.num_pairs == 3:
            self.score = 1500
            self.scoring_dice = 6
            return
        if self.face_dict[1] < 3:
            self.score += 100*self.face_dict[1]
            self.scoring_dice += self.face_dict[1]
        if self.face_dict[5] < 3:
            self.score += 50*self.face_dict[5]
            self.scoring_dice += self.face_dict[5]
        return

    def farkle_check(self):
        if self.scoring_dice == 0:
            self.farkled = True
        return self.farkled


class Turn:
    """
    Executes one turn (several rolls) of a farkle game
    """
    def __init__(self, roll_mode='user'):
        # user mode will ask before rolling
        # sim mode will roll automatically
        self.dice = 6
        self.score = 0
        self.rolls = 1
        self.farkled = False
        self.roll_again = "Yes"

        # initial roll
        roll1 = Roll(self.dice)
        if (roll1.farkled):
            print(roll1.face_dict)
            self.farkle_procedure()
        else:
            self.scoring_roll_procedure(roll1)
            while(not self.farkled):
                if roll_mode == "auto":
                    self.subsequent_roll()
                else:
                    if (input("Roll Again").lower() == "no"):
                        break
                    else:
                        self.subsequent_roll()
    score_string = "Score: {} \nDice Remaining: {}"

    def all_scored_check(self):
        if self.dice == 0:
            self.dice = 6
        pass

    def subsequent_roll(self):
        self.rolls += 1
        this_roll = Roll(self.dice)
        if(this_roll.farkled):
            self.farkle_procedure()
        else:
            self.scoring_roll_procedure(this_roll)

    def farkle_procedure(self):
        print()
        self.dice = 0
        self.farkled = True
        self.score = 0
        print("You Farkled")

    def scoring_roll_procedure(self, roll):
        print(roll.face_dict)
        self.score += roll.score
        self.dice -= roll.scoring_dice
        self.all_scored_check()
        print("Score: {} \nDice Remaining: {}".format(self.score, self.dice))

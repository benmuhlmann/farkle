"""
To-Do list
1. only accept 'y' and 'n' in Turn class when asking to roll again
2. remove roll_dice(), score_roll(), and farkle_check() from Roll's init method.
   This will make testing easier. (Will be able to initialize a roll, modify the
   face_dict or reverse_dict attributes, then separately 'roll' and score
   to assert scores are as expected
3. Add above roll related methods when initializing a roll in the Turn class
"""



# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:10:21 2020

@author: benmu
"""
import numpy.random as rd
from collections import defaultdict

class Roll:
    """
    Executes one farkle roll.

    init parameters:
    dice: number of dice to roll
    score: the resulting score of this roll
    scoring_dice: the number of dice in this roll that scored
    farkled: farkle indicator
    face_dict: keys are faces, 
               values are number of times the 'key' face appears
    reverse_dict: keys are number of times a face appears, 
                  values are faces which appear 'key' times
    """
    
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
        """
        Generates a dice roll and updates
        face_dict and reverse_dict
        """
        dice_roll = rd.randint(1, 7, self.dice)
        for die in dice_roll:
            self.face_dict[die] += 1
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
        if self.num_pairs() == 3:
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
    init parameters:
    roll_mode:
    "user" mode asks a user if they want
    to roll remaining dice, and gives status of turn between rolls

    "auto" mode will suppress turn status print statements
    as well as keep the turns highest score
    (won't reset a turns score to 0 if a farkle occurs
    See implementation.py for examples of using "auto" mode
    to simulate turns
    
    object attributes:
    dice: number of dice remaining to roll
    score: the sum of each Roll's score (or 0 if a farkle occurs)
    rolls: the number of rolls in this turn
    fakled: farkle indicator
    """
    def __init__(self, roll_mode='user'):
        # user mode will ask before rolling
        # sim mode will roll automatically
        self.roll_mode = roll_mode
        self.dice = 6
        self.score = 0
        self.rolls = 1
        self.farkled = False

        # initial roll
        roll1 = Roll(self.dice)
        if (roll1.farkled):
            self.farkle_procedure()
        else:
            self.scoring_roll_procedure(roll1)
            while(not self.farkled):
                if self.roll_mode == "auto":
                    self.subsequent_roll()
                else:
                    # ask user if they want to roll again. Keep asking until they enter "y" or "n"
                    while (True):
                        user_response = input("roll again? y/n ")
                        if user_response.lower() in ["y", "n"]:
                            break
                    # end the turn if the user inputs "n"
                    if user_response.lower() == 'n':
                        break

                    # roll again if the user inputs "y"
                    else:
                        self.subsequent_roll()

    def all_scored_check(self):
        """
        check if all dice score 
        (only checked if farkle doesn't occur)
        """
        if self.dice == 0:
            self.dice = 6
        pass

    def subsequent_roll(self):
        """
        packages the process for 2nd, 3rd rolls etc. 
        into one method.
        increments the Turn's roll counter, 
        creates a new Roll object, 
        checks output of new Roll
        """
        self.rolls += 1
        this_roll = Roll(self.dice)
        if(this_roll.farkled):
            self.farkle_procedure()
        else:
            self.scoring_roll_procedure(this_roll)

    def farkle_procedure(self):
        """
        Put all the post-farkle steps into one method
        """ 
        self.dice = 0
        self.farkled = True
        if self.roll_mode == "user":
            self.score = 0  # don't zero score in auto mode for sim purposes
            print("You Farkled!")  # only print updates in user mode

    def scoring_roll_procedure(self, roll):
        """
        Everything that happens post-non-farkle roll.
        Add Roll's score to Turn's score,
        Subtract Roll's Scoring Dice from Turn's current dice,
        Check if all dice scored 
        """
        # |testing| print(roll.face_dict)
        self.score += roll.score
        self.dice -= roll.scoring_dice
        self.all_scored_check()
        # only print updates in user mode
        if self.roll_mode == "user":
            print(f"Score: {self.score} \nDice Remaining: {self.dice}")




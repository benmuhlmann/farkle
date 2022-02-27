# -*- coding: utf-8 -*-
"""
Test the roll class.
Simulate rolling one 
die n times
and output the 
percentage of farkles
"""
import random
from DefineFarkle import *

random.seed()
num_rolls = 10000
roll_list = []

for roll in range(num_rolls):
    my_turn = Roll(6)
    my_turn.roll_dice()
    my_turn.score_roll()
    my_turn.farkle_check()
    roll_list.append(my_turn.farkled)

# percent of farkles
farkle_percentage = sum(roll_list)/num_rolls
print(f'Percentage of rolls ending in a farkle: {100*farkle_percentage}')

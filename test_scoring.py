from DefineFarkle import Roll
from collections import defaultdict
import pytest

# utility function to make entering dice rolls easier in testing
def reverse_dict(roll_dict):
    reverse_dict = defaultdict(list)
    for key, value in roll_dict.items():
        reverse_dict[value].append(key)
    return reverse_dict

def test_five_of_a_kind():
    input_dice = {1:5
                 ,2:0
                 ,3:0
                 ,4:0
                 ,5:0
                 ,6:1}
    test_roll = Roll(6)
    reverse_dice = reverse_dict(input_dice)
    test_roll.reverse_dict = reverse_dice
    test_roll.score_roll()
    assert test_roll.score == 2000


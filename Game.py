"""
To-Do
1. Add docstrings to class methods
DONE 2. Add a space after asking player name
3. Add more checks for user input
4. Add procedure at end of while loop
(What happens when a player hits the target score?)
5. Add the entire procedure for a player hitting the target score
(Everyone else rolls again)
(Use Player dict)
"""

from DefineFarkle import *
import time


class Game:
    """
    Runs through a game
    1. get player list
    2. loop through player list until one player gets 10k
    """
    def __init__(self, num_players=2, target_score=10000):
        self.num_players = num_players
        self.target_score = target_score
        self.players = list()
        self.scores = dict()
        self.rounds = 0

    def get_player_list(self):
        player_list = list()
        for i in range(1, self.num_players+1):
            name = input(f"What's player {i}'s name? ")
            player_list.append(name)
            self.scores[name] = 0
            self.players.append(name)

    def game_loop(self):
        # keep playing until someone hits max score
        while max(self.scores.values()) < self.target_score:
            # loop through player list
            # print out player list
            # call the turn class
            # add turn's score to player's score total in self.scores
            for player in self.players:
                print(f"\nIt's {player}'s turn")
                print(f"scores: \n {self.scores}\n")
                time.sleep(1)
                print("Rolling...\n")
                time.sleep(1)
                current_turn = Turn()
                self.scores[player] += current_turn.score
                time.sleep(1)


if __name__ == "__main__":
    num_players = input("How many players? ")
    Threshold =  input("What score do you want to play to? ")
    my_game = Game(int(num_players), int(Threshold))
    my_game.get_player_list()
    my_game.game_loop()

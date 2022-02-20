"""
To-Do
1. Add docstrings to class methods
DONE 2. Add a space after asking player name
3. Add more checks for user input
DONE 4. Add procedure at end of while loop
(What happens when a player hits the target score?)
DONE 5. Add the entire procedure for a player hitting the target score
(Everyone else rolls again)
(Use Player dict)
6. Ensure no two players can have the same name
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
        self.current_player = None

    def get_player_list(self):
        """
        Asks the user to input the name of every player.
        Adds each player name to the 'players' attribute (a list)
        Sets each player's score to 0 in the 'scores' attribute (a dict)
        """
        player_list = list()
        for i in range(1, self.num_players+1):
            name = input(f"What's player {i}'s name? ")
            player_list.append(name)
            self.scores[name] = 0
            self.players.append(name)
        self.current_player = self.players[0]

    def score_above_threshold(self):
        """
        When a player's score exceeds the winning threshold, execute the end-of game procedure.
        Every other player has one final turn to beat the top score.
        """
        print(f"\n{self.current_player} scored over {self.target_score}!")
        print(f"Everyone else gets one more turn to beat {self.current_player}'s score.")
        time.sleep(1.5)
        # Get a list of players to loop through.
        # Exclude the current player (who just exceeded the target score)
        players_copy = (self.players).copy()
        players_copy.remove(self.current_player)
        # let every other player have a turn
        for player in players_copy:
            print(f"\nIt's {player}'s turn")
            print(f"scores: \n {self.scores}\n")
            time.sleep(1)
            print("Rolling...\n")
            time.sleep(1)
            current_turn = Turn()
            self.scores[player] += current_turn.score

    def declare_winner(self):
        """
        Check which player has the top score (or players in case of a tie)
        print winning name(s) with a fun statement!
        """
        top_score = max(self.scores.values())
        winners = [name_score_tup[0] for name_score_tup in [item for item in self.scores.items() if item[1] == top_score]]
        if len(winners) > 1:
            winning_names_string = " and ".join(winners)
            print(f"The winners are {winning_names_string}!")
        else:
            print(f"The winner is {winners[0]}!")





    def game_loop(self):
        # keep playing until someone hits max score
        while max(self.scores.values()) < self.target_score:
            # loop through player list
            # print out player list
            # call the turn class
            # add turn's score to player's score total in self.scores
            for player in self.players:
                self.current_player = player
                print(f"\nIt's {player}'s turn")
                print(f"scores: \n {self.scores}\n")
                time.sleep(1)
                print("Rolling...\n")
                time.sleep(1)
                current_turn = Turn()
                self.scores[player] += current_turn.score
                if self.scores[player]  >= self.target_score:
                    time.sleep(1)
                    break
                time.sleep(1)

        self.score_above_threshold()
        self.declare_winner()





if __name__ == "__main__":
    num_players = input("How many players? ")
    Threshold =  input("What score do you want to play to? ")
    my_game = Game(int(num_players), int(Threshold))
    my_game.get_player_list()
    my_game.game_loop()

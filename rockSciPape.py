# Importing random module to give 2nd player random choice
import random

# !/usr/bin/env python3


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""

# List of possible moves
moves = ['rock', 'paper', 'scissors']


# Superclass Player
class Player:
    # Creating a 'score' variable to control the score for each player
    score = 0

    def move(self):
        return 'rock'

    # Implementing learn method
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


# Creating a subclass RandomPlayer of superclass Player
class RandomPlayer(Player):
    # Overriding move method to make a random choice and return the choice
    def move(self):
        move = random.choice(moves)
        return move


# Creating a subclass HumanPlayer of superclass Player
class HumanPlayer(Player):

    # Overriding move method to prompt user to enter their choice
    def move(self):
        # If user enters something wrong repeting the message
        move = input("rock, paper, scissors: ")
        while move not in moves:
            move = input("rock, paper, scissors: ")
        return move


# Creating a subclass ReflectPlayer of superclass Player
class ReflectPlayer(Player):
    # Constarctor that assigns a random move to opponent
    def __init__(self):
        self.their_move = random.choice(moves)

    # Overriding move method and returning opponent's move
    def move(self):
        return self.their_move


# Creating a subclass CyclePlayer of superclass Player
class CyclePlayer(Player):
    # Constaructor that assigns a random move to its move
    def __init__(self):
        self.my_move = random.choice(moves)

    # Overriding move method to cycle moves
    def move(self):
        index_of_move = moves.index(self.my_move) + 1
        if index_of_move >= len(moves):
            index_of_move = 0
        return moves[index_of_move]


# Beats method to check who wins each round
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Superclass game that takes care of game logic
class Game:
    # Constructor to create players
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # Play round method to find a winner of a round
    def play_round(self):

        # Calling move method on a player object to get a move
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        # Checking if player 1 or player 2 wins using beats function
        # If moves are the same print TIE and don't increment score
        # Otherwise print who wins and increment score for that player
        if move1 == move2:
            print("** TIE **")
        elif beats(move1, move2):
            print("** PLAYER ONE WINS **")
            self.p1.score += 1
        else:
            print("** PLAYER TWO WINS **")
            self.p2.score += 1
        # Printing overall score after a round played
        print(f"Score: Player One {self.p1.score},"
              f"Player Two {self.p2.score}")
        # Passing moves of every player to learn method
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # Method to ask users if they wish to play again
    def play_again(self):

        while True:
            # Asking user desire to play again
            question = input("Do you want to play again? "
                             "Type Y or N: ").lower()
            # If user said yes starting game again
            if question == 'y':
                game = Game(HumanPlayer(), random.choice(players))
                game.play_game()
                break
            # If user doesn't want to play again ending game
            elif question == 'n':
                print("Thank you for playing this game. "
                      "Have a wounderful day!")
                break
            # Otherwise if input is incorrect repeating
            else:
                print("Wrong input! Try again!")

    # Method to play game and find a winner
    def play_game(self):

        # Accumulator to control # of rounds
        round = 0
        print("Game start!")
        # Rounds are played until one of users wins 3 rounds
        while True:
            print(f"Round {round}:")
            self.play_round()
            round += 1
            if self.p1.score == 3 or self.p2.score == 3:
                break
        # identifying the winner of the game, printing a message
        if self.p1.score > self.p2.score:
            print("Player One WON!")
        else:
            print("Player Two WON!")
        # Calling play_again to see if user wants to play again
        self.play_again()


# List of different players to choose from
players = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]

if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(players))
    game.play_game()

#!/usr/bin/env python
#
# play-dice.py
# ------------
#
# A simple python program to perform monte-carlo based analysis on a
# simple dice game and present the results in graphical form.

import argparse
import numpy
import os
import random
import time

class DiceGame:
    """
    A class that stores the key parameters for this version of the
    dice game.
    """
    def __init__(self, args):
        self.sides   = args.sides
        self.players = args.players
        self.winning = args.winning

class DiceGameStats:
    """
    A class that stores the key statistics of a single instance of our
    simple dice game.
    """
    def __init__(self, players):
        self.rolls  = numpy.zeros(players, dtype=int)
        self.scores = numpy.zeros(players, dtype=int)

class DiceGameAccumStats:
    """
    A class that stores and processes accumulated stats from a bunch
    of our simple games.
    """
    def __init__(self):
        self.games      = 1
        self.winscores  = numpy.empty((0, 0), dtype=int)
        self.losescores = numpy.empty((0, 0), dtype=int)
        self.winners    = numpy.empty((0, 0), dtype=int)
        self.losers     = numpy.empty((0, 0), dtype=int)

    def add_game(self, diceGameStats):
        self.games += 1
        self.winscores  = numpy.append(self.winscores, numpy.max(diceGameStats.scores))
        self.losescores = numpy.append(self.losescores, numpy.min(diceGameStats.scores))
        self.winners    = numpy.append(self.winners, numpy.argmax(diceGameStats.scores))
        self.losers     = numpy.append(self.losers, numpy.argmin(diceGameStats.scores))

    def histogram(self):
        self.losescores_hist, self.losescores_histbins = numpy.histogram(self.losescores)
        print("Losing (lowest) score historgram after %d games." % self.games)
        print()
        self.ascii_hist(self.losescores,
                        self.losescores_hist,
                        numpy.floor(self.losescores_histbins))

    def print(self):
        print([diceGameStats.rolls, diceGameStats.scores]) #, end='\r')
        print(self.winscores)
        print(self.losescores)
        print(self.winners)
        print(self.losers)        
        print()
        print()

    def ascii_hist(self, x, N, X):
        """
        A GitHub gist taken from:
          https://gist.github.com/joezuntz/2f3bdc2ab0ea59229907?permalink_comment_id=4473720#gistcomment-4473720
        """
        total = 1.0*len(x)
        width = 50
        nmax = N.max()
        for (xi, n) in zip(X,N):
            bar = '#'*int(n*1.0*width/nmax)
            xi = '{0: <8.4g}'.format(xi).ljust(10)
            print('{0}| {1}'.format(xi,bar))

def play(diceGame,diceGameStats):
    """
    Play a single game of our simple dice game.
    """
    winner = False
    while not winner:
        winner = play_round(diceGame, diceGameStats)

def play_round(diceGame,diceGameStats):
    """
    Play a single round of our simple dice game. 
    """
    for i in range(diceGame.players):
        die = random.randrange(1, diceGame.sides+1)
        diceGameStats.scores[i] += die
        diceGameStats.rolls[i]  += 1
        if diceGameStats.scores[i] >= diceGame.winning:
            return True
    return False

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='A Monte-Carlo based simulation of a simple dice game',
        epilog='I hope you enjoy playing this simple game!')

    parser.add_argument('-r', '--rounds', default=-1, type=int,
                        help='Number of round to play (-1 = forever)')
    parser.add_argument('-s', '--sides', default=6, type=int,
                        help='Number of sides on the die')
    parser.add_argument('-p', '--players', default=10, type=int,
                        help='Number of player in the dice game')
    parser.add_argument('-w', '--winning', default=100, type=int,
                        help='The total score required to win the game')
    args = parser.parse_args()

    diceGameAccumStats = DiceGameAccumStats()
    round = 1
    while True:
        try:
            diceGame      = DiceGame(args)
            diceGameStats = DiceGameStats(args.players)
            play(diceGame, diceGameStats)
            diceGameAccumStats.add_game(diceGameStats)
            round+=1
            #diceGameAccumStats.print()
            if ((round % 100) == 0):
                os.system('clear')
                diceGameAccumStats.histogram()
            if (args.rounds > 0) and (round > args.rounds):
                break
        except KeyboardInterrupt:
            break

    print()
    print("Here is the histogram of loser scores (last place).")
    diceGameAccumStats.histogram()

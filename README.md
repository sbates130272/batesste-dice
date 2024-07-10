# A Simple Dice Game

## Introduction

This project pertains to a simple dice game that I have been playing
with in my head for several years. The rules are [discussed
below](#game-rules) and there is a help for command line arguments
build into the executable.

## Game Rules

The game is very simple:

1. The game consists of p players who take it in turns to roll a fair
   die with s sides.
1. The sides of the die are labelled from 1 to s and the player
   records their score on each roll.
1. The order of the players does not vary and the winner is the first
   player with an accumulated total that meets or exceeds the winning
   score, w.

## Installation and Running

You can install the game by installing the Python modules required
(either in a venv or directly). So for example:
```
python -m pip install -r requirements.txt
```
You can then see the help for the game by running:
```
./play-dice.py -h
```

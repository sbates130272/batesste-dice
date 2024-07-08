#!/usr/bin/env python
#
# play-dice.py
# ------------
#
# A simple python program to perform monte-carlo based analysis on a
# simple dice game and present the results in graphical form.

import argparse
import matplotlib

if __name__ == "__main__":

    args = argparse.ArgumentParser(
        description='A Monte-Carlo based simulation of a simple dice game',
        epilog='I hope you enjoy playing this simple game!')

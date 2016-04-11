#!/usr/bin/env python

import numpy as np
from numpy import genfromtxt
import pandas as pd
import mlpy as ml


def main():
    print "Test"

    seasonStats = pd.read_csv('data/RegularSeasonDetailedResults.csv')
    tourneyStats = pd.read_csv('data/TourneyDetailedResults.csv')
    allGames = pd.concat([seasonStats, tourneyStats])

    print allGames

def getSubjectMatrix(games):
    return

def getTargetMatrix(games):
    targets = []
    

def getWinnerVector(game):
    return 

def getLoserVector(game):
    return

if __name__ == "__main__":
    main()

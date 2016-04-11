#!/usr/bin/env python

import numpy as np
import pandas as pd

def main():
    df = pd.read_csv('singleTeamGames.csv')
    teams = df.groupby('ID')
    averages = teams.mean()
    averages.to_csv('teamStats.csv')  

main()


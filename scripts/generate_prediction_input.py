#!usr/bin/env python

import numpy as np
import pandas as pd

def main():
    print 'Begin prediction input generation'

    teamData = pd.read_csv('teamStats.csv').set_index('ID')
    ans = pd.DataFrame()

    with open('../data/SampleSubmission.csv') as f:

        games = f.readlines()

        for game in games:

            if game[0] != 'I':

                year = game[0:4]

                team1 = game[5:9]
                team2 = game[10:14]

                teamOneID = int(year + team1)
                teamTwoID = int(year + team2)

                teamOneSeries = teamData.loc[teamOneID, 'SCORE':]
                teamTwoSeries = teamData.loc[teamTwoID, 'SCORE':]

                series = pd.concat([teamOneSeries, teamTwoSeries],ignore_index='True')
                ans = ans.append(series, ignore_index='True')

    ans.to_csv('predictionInput.csv', index=False)

    print 'End prediction input generation'
main()

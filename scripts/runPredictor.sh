#!/bin/sh

echo "Generating Training Data"
./generate_training_data.sh ../data/RegularSeasonDetailedResults.csv ../data/TourneyDetailedResults.csv

echo "Single Team Format"
./single_team_format.sh ../data/RegularSeasonDetailedResults.csv ../data/TourneyDetailedResults.csv

echo "Generating Team Stats"
python generate_team_stats.py

echo "Generating Prediction Input"
./generate_prediction_input.sh

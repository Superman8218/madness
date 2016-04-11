#!/bin/sh

python generate_prediction_input.py

tail -n +2 predictionInput.csv > temp && mv temp predictionInput.csv

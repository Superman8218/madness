#!/usr/bin/env python

import numpy as np
from numpy import genfromtxt
import pandas as pd
from sklearn import svm
import pickle

def main():
    trainingMatrix = genfromtxt('trainingMatrix.csv', delimiter=',')
    trainingVector = genfromtxt('trainingVector.csv', delimiter=',')
    predictionMatrix = genfromtxt('predictionInput.csv', delimiter=',')

    print 'Begin Training'

    clf = svm.SVC(gamma=0.01, C=100, probability=True)
    clf.fit(trainingMatrix, trainingVector)

    pickle.dump(clf, open('model.p', 'w'))
    
    print 'Finished Training'

main()

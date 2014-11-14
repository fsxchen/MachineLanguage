#/usr/bin/env python
from math import log

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    lableCounts = {}
    for featVec in dataSet:
        currentLable = featVec[-1]
        if currentLable not in lableCounts.keys():
            lableCounts[currentLable] = 0
        lableCounts[currentLable] += 1

    shannonENt = 0.0
    for key in lableCounts:
        prob = float(lableCounts[key])/ numEntries
        shannonENt -= prob * log(prob, 2)
    return shannonENt

def createDataSet():
    dataSet = [[1, 1, 'yes'], 
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'], 
        [0, 1, 'no']]
    lables = ['no surfacing', 'flippers']
    return dataSet, lables

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if axis == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0] - 1)
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSte = splitDataSet(data, i, value)
            prob = len(subDataSte) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSte)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

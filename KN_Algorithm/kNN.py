from numpy import *
import operator

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLableVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFormLine = line.split("\t")
        returnMat[index, :] = listFormLine[0:3]
        classLableVector.append(int(listFormLine[-1]))
        index += 1
    return returnMat, classLableVector

def autoNorm(dataSet):
    minVal = dataSet.min(0)
    maxVal = dataSet.max(0)
    ranges = maxVal - minVal
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVal, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minVal

def classifPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    precentTalt = float(raw_input(\
            "percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat, datingLables = file2matrix("datingTestSet.txt")
    normMat, ranges, minVal = autoNorm(datingDataMat)
    inArr = array([ffMiles, precentTalt, iceCream])
    classifierResult = classify0((inArr-\
        minVal)/ranges, normMat, datingLables, 3)
    print "You will probably like this people: ", \
        resultList[classifierResult-1]

def createDateSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	lables = ['A', 'A', 'B', 'B']
	return group, lables

def classify0(inX, dataSet, lables, k):
    dataSetSize = dataSet.shape[0]   #the shape of the matrix
                                    #+return a tuple of (length, width)

    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    print distances
    sortedDistIndicies = distances.argsort()
    print sortedDistIndicies
    classCount = {}
    for i in range(k):
        voteIlable = lables[sortedDistIndicies[i]]
        classCount[voteIlable] = classCount.get(voteIlable, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(),
        key=operator.itemgetter(1), reverse=True)
    print sortedClassCount[0][0]
    return sortedClassCount[0][0]

g, l = createDateSet()
classify0([0, 0], g, l, 3)

import matplotlib.pyplot as plt
plt.plot([1.0 ,1.0, 0, 0],[1.1, 1.0, 0, 0.1], "ro")
plt.plot([0], [1], "ro")

plt.axis([-1, 2, -1, 2])
plt.ylabel('some numbers')
plt.show()
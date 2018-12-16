import numpy as np
import operator

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    #说明tile里参数列表中元组的第二个参数是控制a重复次数的
    ######说明参数列表的元组第一个是控制行数的 
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet  #计算差值
    #求差值的平方
    sqDiffMat = diffMat**2
    #每行求和
    sqDistances = sqDiffMat.sum(axis=1)
    #开方根
    distances = sqDistances**0.5
    print(distances)
    #排序
    sortedDisIndicies = distances.argsort()
    print(sortedDisIndicies)
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDisIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel , 0) + 1
    sortedClassCount = sorted(classCount.items(),
        key = operator.itemgetter(1),reverse = True)
    print(sortedClassCount)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    numberOfLines = len(arrayOlines)
    returnMat = np.zeros((numberOfLines,3))
    classLableVector = []
    index = 0
    for line in arrayOlines:
        line = line.strip()
        listFromLines = line.split('\t')
        returnMat[index:] =listFromLines[0:3]
        classLableVector.append(int(listFromLines[-1]))
        index+=1
    return returnMat,classLableVector
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m,1))
    normDataSet = normDataSet/np.tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.50      #hold out 10%
    datingDataMat,datingLabels = file2matrix('datingTestSet.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))
    print(errorCount)
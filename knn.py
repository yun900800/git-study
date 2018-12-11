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
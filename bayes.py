import numpy as np
def loadDataSet():
    postingList = [
        ['my','dog','has','flea','problems','help','please'],
        ['maybe','not','take','him','to','dog','park','stupid'],
        ['my','dalmation','is','so','cute','I','love','him'],
        ['stop','posting','stupid','worthless','garbage'],
        ['mr','licks','ate','my','steak','how','to','stop','him'],
        ['quit','buying','worthless','dog','food','stupid']
        ]
    classVec = [0,1,0,1,0,1]
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set()
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabSet, inputSet):
    returnVec = [0]*len(vocabSet)
    for word in inputSet:
        if word in vocabSet:
            returnVec[vocabSet.index(word)] = 1
        else: print('the word %s is not in my Vocabulary!'%word)
    return returnVec

### 输入参数为文档矩阵(将文档处理为词向量的文档矩阵)，和每篇文档对应的类别标签
def trainNB0(trainMatrix, trainCategory):
    #总的文档的数目
    numberOfDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numberOfDocs)
    print(pAbusive)
    p0Num = np.zeros(numWords)
    p1Num = np.zeros(numWords)
    #初始化概率
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numberOfDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])         
    p0Vect = p0Num/p0Denom
    p1Vect = p1Num/p1Denom
    return p0Vect,p1Vect,pAbusive
    

import knn
import trees
import numpy as np

#import dict
import matplotlib
import matplotlib.pyplot as plt

# group,labels = knn.createDataSet()
# result = knn.classify0([0,0],group,labels,3)
# print(result)

# ####returnMat, classLableVector = knn.file2matrix('datingTestSet.txt')
# # print('returnMat',returnMat)
# # print('classLableVector',classLableVector)

# # fig = plt.figure()
# # ax = fig.add_subplot(111)
# # datingDataMat,datingLabels = knn.file2matrix('datingTestSet.txt')
# # #ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
# # ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*np.array(datingLabels), 15.0*np.array(datingLabels))
# # ax.axis([-2,25,-0.2,2.0])
# # plt.xlabel('Percentage of Time Spent Playing Video Games')
# # plt.ylabel('Liters of Ice Cream Consumed Per Week')
# # plt.show()
# knn.datingClassTest()
# # returnVec = knn.img2vector('testDigits/0_13.txt')
# # print(returnVec[0,0:31])
# knn.handwritingClassTest()

myData,label = trees.createDataSet()
# myData[0][-1] ='maybe'
# result= trees.calShannonEnt(myData)
# print('result',result)

# result = trees.splitDataSet(myData,0,1)
# print('result',result)
# result = trees.splitDataSet(myData,0,0)
# print('result',result)

result = trees.chooseBestFeatureToSplit(myData)
print('result',result)
import knn
import numpy as np
#import dict
import matplotlib
import matplotlib.pyplot as plt
import bayes

from hotel import MyClass
from complex import Complex,Test,People,student,sample

group,labels = knn.createDataSet()
result = knn.classify0([0,0],group,labels,3)
print(result)

####returnMat, classLableVector = knn.file2matrix('datingTestSet.txt')
# print('returnMat',returnMat)
# print('classLableVector',classLableVector)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# datingDataMat,datingLabels = knn.file2matrix('datingTestSet.txt')
# #ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*np.array(datingLabels), 15.0*np.array(datingLabels))
# ax.axis([-2,25,-0.2,2.0])
# plt.xlabel('Percentage of Time Spent Playing Video Games')
# plt.ylabel('Liters of Ice Cream Consumed Per Week')
# plt.show()

# knn.datingClassTest()
# returnVec = knn.img2vector('testDigits/0_13.txt')
# print(returnVec[0,0:31])
# knn.handwritingClassTest()

a , b = bayes.loadDataSet()
print(a)

c = bayes.createVocabList(a)
print(c)

d = bayes.setOfWords2Vec(c,a[0])
print(d)
d = bayes.setOfWords2Vec(c,a[3])
print(d)

trainMat = []
for postingDoc in a:
   trainMat.append(bayes.setOfWords2Vec(c,postingDoc)) 
p0Vec, p1Vec, pAbusive = bayes.trainNB0(trainMat,b)
print(p0Vec)
print(p1Vec)
print(pAbusive)

# 实例化类
x = MyClass()
 
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
t = Test()
t.prt()
t.prt1()

# 实例化类
p = People('runoob',10,30)
p.speak()

s = student('ken',10,60,3)
s.speak()

test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法


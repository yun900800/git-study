import knn
group,labels = knn.createDataSet()
result = knn.classify0([0,0],group,labels,3)
print(result)
import knn
import dict
group,labels = knn.createDataSet()
result = knn.classify0([0,0],group,labels,3)
print(result)
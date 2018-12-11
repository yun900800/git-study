import numpy as np
list=[[1,2,3,4,5],[6,7,8,9,10]]
print(type(list))
d = np.array(list)
print(type(d))
print(d.dtype)
print(d.shape)# 返回一个元组(一维为2，二维为3)
print(d.ndim)
print(type(d.shape))

e = np.zeros((3,3))
print(e.dtype)
print(e.shape)# 返回一个元组(一维为2，二维为3)
print(e.ndim)

e = np.ones((2,3))
print(e.dtype)
print(e.shape)# 返回一个元组(一维为2，二维为3)
print(e.ndim)
print(e) 

x = np.array([1,2.6,3],dtype = np.int64)
print(x)
x = np.array([1,2,3],dtype =np.float64)
print(x)

x = np.array([1,2.6,3],dtype =np.float64)
print(x)
y = x.astype(np.int32)
print(y)
z = y.astype(np.float64)
print(z)

x = np.array(['12','2','3'],dtype =np.string_)
print(x)
y = x.astype(np.int32)
print(y)

x = np.array([1,2,3])
y = x * 2
print(x+y)

y = x>2
print(y)

x = np.array([[1,2],[3,4],[5,6]])
print(x[0])
print(x[0][1])
y = x[0,1]
print(y)

x = np.array([[[1, 2], [3,4]], [[5, 6], [7,8]]])
print(x[0])
y = x[0].copy()
print(y[0][0])

x = np.array([1,2,3,4,5])
print(x[1:3])
print(x[:3])
print(x[1:])
print(x[0:4:2])

x = np.array([[1,2],[3,4],[5,6]])
print(x[:2])
print(x[:2,:1])
print(x[:2][0])
x[:2,:1]=0
print(x)


#https://www.jianshu.com/p/83c8ef18a1e8
#创建10行10列的随机数组
x = np.random.rand(10, 10)
print(x)
print(x.dtype)
print(x.shape)# 返回一个元组(一维为10，二维为10)
print(x.ndim)
#创建指定范围内的一个数
x = np.random.uniform(0, 100)
print(x)

# 创建指定范围内的一个整数
x = np.random.randint(0, 100)
print(x)

# 正态生成4行5列的二维数组
arr = np.random.normal(1.75, 0.1, (4, 5))
print(arr)
# 截取第1至2行的第2至3列(从第0行算起)
after_arr = arr[1:3, 2:4]
print(after_arr)

print("reshape函数的使用!")
one_20 = np.ones([20])
print("-->1行20列<--")
print (one_20)

one_4_5 = one_20.reshape([4, 5])
print("-->4行5列<--")
print (one_4_5)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
stus_score = stus_score > 80
print(stus_score)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
stus_score = np.where(stus_score < 80, 0, 90)
print(stus_score)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一列的最大值(0表示列)
print("每一列的最大值为:")
result = np.amax(stus_score, axis=0)
print(result)

print("每一行的最大值为:")
result = np.amax(stus_score, axis=1)
print(result)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的最小值(0表示列)
print("每一列的最小值为:")
result = np.amin(stus_score, axis=0)
print(result)

# 求每一行的最小值(1表示行)
print("每一行的最小值为:")
result = np.amin(stus_score, axis=1)
print(result)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的平均值(0表示列)
print("每一列的平均值:")
result = np.mean(stus_score, axis=0)
print(result)

# 求每一行的平均值(1表示行)
print("每一行的平均值:")
result = np.mean(stus_score, axis=1)
print(result)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一行的方差(0表示列)
print("每一列的方差:")
result = np.std(stus_score, axis=0)
print(result)

# 求每一行的方差(1表示行)
print("每一行的方差:")
result = np.std(stus_score, axis=1)
print(result)


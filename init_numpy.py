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

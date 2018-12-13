import numpy as np 
import pandas as pd
#通过numpy创建Series 
result = pd.Series(np.arange(4,10))
#通过python数组创建Series
print(result)
result = pd.Series([11,12,14],index=['北京','上海','深圳'])
print(result)
#通过字典创建Series
result = pd.Series({'北京':11, '上海':12, '深圳':14})
print(result)

#Series 允许索引重复
result = pd.Series([11,12,14],index=['北京','上海','上海'])
print(result)
print(result['上海'])

data_3_4 = pd.DataFrame(np.arange(10,22).reshape(3,4))
print(data_3_4)
# 打印第一行数据
print(data_3_4[:2])
# 打印第一列数据
print(data_3_4[:][1])
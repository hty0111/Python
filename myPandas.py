import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import string

pd.read_csv('myCsvData.csv')

# 默认键值从0开始 0:1, 1:2, 2:3
t1 = pd.Series([1, 2, 3], dtype=float)
t1.astype(int)
# A:1, B:2, C:3
t2 = pd.Series(np.arange(3), index=list(string.ascii_uppercase[:3]))
# A:10, B:10, C:3
t2.where(t2 > 1, 10)
# 用字典创建，type = object
temp_dict = {"HTY": "play", "ZXA": "study"}
t3 = pd.Series(temp_dict)
print(t3["HTY"])    # 'play'
print(t3[1])        # 'study'
print(t3[1:2])      # zxa:study
print(t3.index)     # Index(['HTY', 'ZXA'], dtype='object')
print(list(t3.index)[:1])   # ['HTY']

# 行索引index，axis=0；列索引column，axis=1
d = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list('XYZ'), columns=list('ABCD'))
temp_dict = {'name': ['HTY', 'ZXA'], 'age': [21, 20], 'tele': [5285, 1877]}
pd.DataFrame(temp_dict)     # 字典的键作为列标column
temp_list = [{'name': 'HTY', 'age': 21}, {'name': 'ZXA', 'age': 20}]
pd.DataFrame(temp_list)     # 效果同上

# loc通过标签取行数据，切片时为闭区间；iloc通过位置取行数据
print(d.loc['X'])           # 取一行，Series
# print(d.iloc[0])
print(d.loc[['X', 'Y']])    # 取两行，Dataframe
print(d.loc['X']['A'])      # 0
# print(d.loc['X'][0])
# print(d.iloc[0][0])

# dataframe属性：shape, dtypes, ndim(维度), index, columns, values
# dataframe方法：head(), tail(), info(), describe(), sort_values(by='age', ascending=True)

pd.date_range(start='20201230', end='20210120', freq='2D')
d = pd.date_range(start='20210111', periods=10, freq='M')
print(d)

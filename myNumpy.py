import numpy as np
import random

t1 = np.array([1, 2, 3])
t2 = np.arange(0, 5, 1)

t3 = np.array(range(0, 5, 1), dtype='float32')  #单精度
t4 = np.array(range(0, 5, 1), dtype='float64')  #双精度(默认)

t5 = np.array([1, 1, 0, 0, 1], dtype='bool')
t6 = t5.astype('int8')                          #改变类型

t7 = np.array([random.random() for i in range(5)])
t8 = np.round(t7, 2)                            #取小数

t9 = np.array([[[1, 2]], [[3, 4]]])
t10 = t9.flatten()                              #降成一维
t11 = t9.reshape(-1)
t12 = t9.reshape((t9.shape[0]*t9.shape[1]*t9.shape[2],))

t13 = t9 - 2                                    #全部数字&对应位数进行计算，有相同维度即可计算
t14 = t13 / 0                                   #nan/-inf/inf

t15 = t13.transpose()                           #转置
t16 = t15.T
t17 = t16.swapaxes(1, 0)

t18 = np.array([[1, 2], [3, 4], [5, 6]])
t19 = t18[:2, 1:]                               #第1行及之前的行，第1列之后的列
t20 = t18[[0, 2]]                               #第1、3行
t21 = t18[[0, 2], [0, 1]]                       #(0, 0)&(2, 1)
t18[[1, 2], :] = t18[[2, 1], :]                 #交换1、2行


t22 = t18.copy()                                #深拷贝
t22[t22 > 5] = 0                                #bool索引
t23 = np.where(t22<3, 2, 4)                     #三元运算符，小于3替换为2，其余替换为4
t24 = t22.clip(3, 5)                            #小于3替换为3，大于5替换为5

np.count_nonzero(t22)                           #非0的个数
np.isnan(t22)                                   #nan的个数
np.sum(t22, axis=1)                             #求和
t22.sum(axis=1)
t22.mean()                                      #平均值
np.median(t22)                                  #中位数
t22.max()                                       #最大值
np.argmax(t22)                                  #最大值的位置
np.ptp(t22)                                     #最大值和最小值的差     
t22.std()                                       #标准差
np.vstack((t22, t23))                           #竖直拼接
np.hstack((t22, t23))                           #水平拼接
np.eye(3)                                       #单位矩阵

np.random.rand()                                #0-1的均匀分布
np.random.randn()                               #标准正态分布
np.random.randint(10, 20, (2, 3))               #10-19的随机整数
np.random.seed(10)                              #设置随机种子

np.linalg.eigvals()                             #特征根
np.linalg.eig()                                 #特征根和特征向量
np.diagonal()                                   #取对角线元素，可设置偏移量
np.linalg.inv()                                 #求逆
np.triu()                                       #低于第k个对角线归零
np.tril()                                       #高于第k个对角线归零

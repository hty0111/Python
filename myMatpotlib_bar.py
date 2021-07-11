import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as mf
import numpy as np
import random

font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold',
        'size'   : '12'}
matplotlib.rc('font', **font)

a = ['战狼2', '速度与激情8', '功夫瑜伽', '西游伏妖篇']
b_1 = [1564, 269, 175, 164]
b_2 = [1348, 234, 298, 95]
b_3 = [1287, 528, 343, 54]

bar_width = 0.2

x_1 = list(range(len(a)))
x_2 = [i + bar_width for i in x_1]
x_3 = [i + bar_width*2 for i in x_1]

plt.bar(a, b_1, width=bar_width)
plt.bar(x_2, b_2, width=bar_width)
plt.bar(x_3, b_3, width=bar_width)

plt.xticks(x_2)
plt.show()

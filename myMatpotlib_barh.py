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
b = [56.01, 26.94, 17.53, 16.49]

plt.barh(a, b, height=0.3)

plt.show()
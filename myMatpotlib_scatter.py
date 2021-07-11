import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as mf
import numpy as np

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23]
x_3 = np.arange(0, 14, dtype=int)
x_10 = np.arange(20, 34, dtype=int)

font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold',
        'size'   : '12'}
matplotlib.rc('font', **font)


plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(x_3, y_3, c='red', edgecolors='none', label='三月')
plt.scatter(x_10, y_10, c=y_10, cmap=plt.cm.Blues, label='十月')

_x = list(x_3) + list(x_10)
_xtick = ['3月{}日'.format(i) for i in x_3]
_xtick += ['10月{}日'.format(i-20) for i in x_10]
plt.xticks(_x, _xtick, rotation=45)

plt.title('三月和十月的气温')
plt.xlabel('时间/t')
plt.ylabel('温度/C')
plt.legend(loc='upper right')
plt.axes().get_xaxis().set_visible(False)       # 隐藏坐标轴
plt.axes().get_yaxis().set_visible(False)
plt.show()

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as mf
import numpy as np
import random

x = range(0, 120)
y_1 = [random.randint(20, 35) for i in range(120)]
y_2 = [random.randint(20, 35) for j in range(120)]

font = {'family' : 'MicroSoft YaHei',
        'weight' : 'bold',
        'size'   : '12'}
matplotlib.rc('font', **font)
# _font = mf.FontProperties(fname='C:\\Windows\\Fonts\\simkai.ttf')
# fontproperties=_font

plt.figure(figsize=(20, 8), dpi=80)                     # 设置大小
plt.plot(x, y_1, label="今天", color='orange', linestyle=':', linewidth='5')
plt.plot(x, y_2, label="明天", color='cyan', linestyle='-.', linewidth='2')

_xtick = ['10点{}'.format(i) for i in range(0, 60)]
_xtick += ['11:{}'.format(i) for i in range(0, 60)]
plt.xticks(list(x)[::3], _xtick[::3], rotation=45)      # x轴刻度
# _xtick_labels = [i/2 for i in range(4, 49)]
# plt.xticks(_xtick_labels[::3])

plt.tick_params(axis='both', labelsize=10)
plt.title('气温变化', fontsize=20)
plt.xlabel('时间/t', fontsize=10)
plt.ylabel('温度/C')

plt.grid(alpha=0.4, linestyle='--')                     # 透明度
plt.legend(loc='upper center')                          # prop=_font
# plt.axis([0, 1, 0, 1])
plt.show()
plt.savefig('myLineFigure.png')                         # 保存图片

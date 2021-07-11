import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as mf
import numpy as np
import random

x = [random.randint(50,150) for i in range(100)]

d = 5
num_bins = (max(x) - min(x)) // d
plt.hist(x, num_bins, density=True)     # 直方图显示频率

plt.xticks(range(min(x), max(x)+d, d))
plt.grid()
plt.show()

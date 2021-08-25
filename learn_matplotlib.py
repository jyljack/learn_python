import calendar

import numpy as np
import matplotlib.pyplot as plt

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

t = np.arange(0., 5., 0.2)
plt.figure(figsize=(10, 6), dpi=80)
plt.subplot(2, 1, 1)  # subplot（numbRow ， numbCol ，plotNum ）
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.axis([0, 6, 0, 20])
plt.title("测试")
plt.xlabel("X 轴")
plt.ylabel("Y 轴")

plt.subplot(2, 1, 2)
x = range(1, 13, 1)
y = range(1, 13, 1)
plt.plot(x, y)
plt.xticks(x, calendar.month_name[1:13], color='blue', rotation=60)

plt.show()

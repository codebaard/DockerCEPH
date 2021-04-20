import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


x_min = 0.0
x_max = 75

mean_10 = 28.8482
std_10 = 16.2705

mean_30 = 31.3261
std_30 = 16.054

mean_60 = 61.727
std_60 = 11.3876

x = np.linspace(x_min, x_max, 100)

y_10 = scipy.stats.norm.pdf(x,mean_10,std_10)
y_30 = scipy.stats.norm.pdf(x,mean_30,std_30)
y_60 = scipy.stats.norm.pdf(x,mean_60,std_60)

fig = plt.figure()
ax = plt.subplot(111)

ax.plot(x, y_10, label='10s', color='blue')
ax.plot(x, y_30, label='30s', color='green')
ax.plot(x, y_60, label='60s', color='coral')

plt.grid()

plt.xlim(x_min,x_max)
plt.ylim(0,0.05)

plt.title('Write Latency',fontsize=10)
ax.legend()

plt.xlabel('Latency [s]')
plt.ylabel('Histogram')

plt.savefig('Write_Latency.png')
plt.show()
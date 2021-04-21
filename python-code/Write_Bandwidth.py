import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


x_min = 0.0
x_max = 10

mean_10 = 1.72206
std_10 = 0.910963

mean_30 = 2.53869
std_30 = 2.13052

mean_60 = 2.3401
std_60 = 1.08597

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
plt.ylim(0,0.6)

plt.title('Bandwidth Write',fontsize=10)
ax.legend()

plt.xlabel('Bandwitdth [MB/s]')
plt.ylabel('p[MB/s]')

plt.savefig("Write_Bandwidth.png")
#plt.show()
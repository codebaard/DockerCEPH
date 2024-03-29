import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

x_min = 0.0
x_max = 450

mean_10 = 424
std_10 = 9.63155

mean_30 = 106
std_30 = 42.7955

mean_60 = 60
std_60 = 18.9901

x = np.linspace(x_min, x_max, 500)

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

plt.title('IOPS Read Random',fontsize=10)
ax.legend()

plt.xlabel('IOPS [1/s]')
plt.ylabel('p[1/s]')

plt.savefig("Read_IOPS_Rand.png")
#plt.show()
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

x_min = 0.0
x_max = 50

mean_10 = 18
std_10 = 0.08

mean_30 = 24
std_30 = 17.6777

mean_60 = 15
std_60 = 11.2694

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

plt.title('Read IOPS Sequential',fontsize=10)
ax.legend()

plt.xlabel('IOPS [1/s]')
plt.ylabel('p[1/s]')

plt.savefig("Read_IOPS_sequential.png")
#plt.show()
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

x_min = 0.0
x_max = 0.5

mean_10 = 0.03655
std_10 = 0.000371

mean_30 = 0.147263
std_30 = 0.017623

mean_60 = 0.260001
std_60 = 0.025047

x = np.linspace(x_min, x_max, 1000)

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
plt.ylim(0,35)

plt.title('Read Latency Random',fontsize=10)
ax.legend()

plt.xlabel('Latency [s]')
plt.ylabel('p[s]')

plt.savefig("Read_Latency_Random.png")
#plt.show()
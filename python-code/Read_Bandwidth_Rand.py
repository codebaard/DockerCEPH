import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


x_min = 0.0
x_max = 1800

mean_10 = 1702.354
std_10 = 10.3859

mean_30 = 424.601
std_30 = 35.4608

mean_60 = 243.565
std_60 = 21.80546

x = np.linspace(x_min, x_max, 500)

## make scatterplot!

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
plt.ylim(0,0.04)

plt.title('Read Bandwidth Random',fontsize=10)
ax.legend()

plt.xlabel('Bandwitdth [MB/s]')
plt.ylabel('p[MB/s]')

plt.savefig("Read_Bandwidth_Rand.png")
#plt.show()
import numpy as np
import matplotlib.pyplot as plt

filename = './single_crystal_test_out.csv'
data = np.genfromtxt(filename, dtype=float, delimiter=',', names=True)

x = data['e_zz']
y = data['stress_zz']
y2 = data['pk2']

#fontname

plt.plot(x,y, marker='o', linestyle='-', color='g')
plt.plot(x,y2, marker='x', color='r')

plt.title('Stress-Strain', fontsize=20)

plt.xlabel('e_zz', fontsize=15)
plt.xticks(np.arange(min(x),max(x),0.0005), fontsize=9)
plt.xlim([0,0.005])

plt.ylabel('stress_zz', fontsize=15)
plt.yticks(np.arange(min(y),170,40), fontsize=11)
plt.ylim([0,170])

plt.legend(["stress_zz","pk2"])

plt.show
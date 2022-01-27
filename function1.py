import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci

xmin = 0
xmax = 1
resolution = 100

x = np.linspace(xmin,xmax,resolution)

y = x**2
y2 = np.sin(2*np.pi*x)
y3 = np.cos(2*np.pi*x)
y4 = x*np.log(x) + (1-x)*np.log(1-x)
y5 = np.exp(-x**2)
y6 = 1/2 + np.tanh((x-0.5)/0.01)/2

y7 = sci.erf(x)

plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.plot(x,y6)
plt.plot(x,y7)

plt.xlabel("x")
plt.ylabel("y")
plt.yticks(np.arange(-2,1.1,0.25))
plt.ylim([-2,1.1])

plt.legend(["y","y2","y3","y4","y5","y6","y7"], loc='lower left')
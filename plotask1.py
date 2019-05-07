import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return np.exp(pow(np.sin(x),3))+pow(x,6)-2*pow(x,4)-pow(x,3)-1
t1 = np.arange(-2, 2, 0.02)

plt.plot(t1, f(t1) , 'b')
plt.grid()
plt.ylabel("f(x)")
plt.show()

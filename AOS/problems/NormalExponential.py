import numpy as np
import matplotlib.pyplot as plt

def pdf(x):
	return 1/(x*np.sqrt(2*np.pi)+1e-5)*np.exp(-(np.log(x)**2))

x = np.linspace(0.0, 10.0, num=10000)
y = pdf(x)

plt.scatter(x,y)
plt.show()
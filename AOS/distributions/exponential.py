# Exponential Distribution
# P(X=x|λ) = λ*exp(-λ*x)

import math
import matplotlib.pyplot as plt

lamb = [0.5,1,1.5]
x = [i/5 for i in range(25)]
color = ['b','g','r','c','m','y','k']

for i in range(len(lamb)):
	prob = []
	for j in range(len(x)):
		prob.append(lamb[i]*math.exp(-lamb[i]*x[j]))

	plt.plot(x,prob,c=color[i],label="λ = {}".format(lamb[i]))

plt.legend()
plt.title("Exponential Distrbution")
plt.show()
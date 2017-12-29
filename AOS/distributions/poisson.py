# Poisson Distribution
# P(X=x|λ) = (λ**x)*exp(-λ)/x!

import math
import matplotlib.pyplot as plt

lamb = [1,4,8]
x = [i+1 for i in range(20)]
color = ['b','g','r','c','m','y','k']

for i in range(len(lamb)):
	prob = []
	for j in range(len(x)):
		prob.append((lamb[i]**x[j])*math.exp(-lamb[i])/math.factorial(x[j]))

	plt.plot(x,prob,c=color[i],label="λ = {}".format(lamb[i]))

plt.legend()
plt.title("Poisson Distrbution")
plt.show()
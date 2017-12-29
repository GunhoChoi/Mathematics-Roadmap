# Normal Distribution
# P(X=x|mu,var) = 1/(var*math.sqrt(2*math.pi))*math.exp(-(x-mu)**2/2*var**2)

import math
import matplotlib.pyplot as plt

mu = [0,0,0,-2]
var = [0.2,1,5,0.5] 
x = [(i-50)/10 for i in range(100)]
color = ['b','g','r','c','m','y','k']

for i in range(len(mu)):
	prob = []
	for j in range(len(x)):
		prob.append(1/(math.sqrt(2*math.pi*var[i]))*math.exp(-math.pow(x[j]-mu[i],2)/(2*var[i])))

	plt.plot(x,prob,c=color[i],label="mu={} var={}".format(mu[i],var[i]))

plt.legend()
plt.title("Normal Distrbution")
plt.show()
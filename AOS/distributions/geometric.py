# geometric distribution
# P(X=x|p)= p(1-p)^(x-1)

import matplotlib.pyplot as plt

p = [0.2,0.3,0.5,0.8]
x = [i+1 for i in range(10)]
color = ['b','g','r','c','m','y','k']

for i in range(len(p)):
	prob = []
	for j in range(len(x)):
		prob.append(p[i]*(1-p[i])**(x[j]-1))

	plt.plot(x,prob,c=color[i],label="p = {}".format(p[i]))

plt.legend()
plt.title("Geometric Distrbution")
plt.show()
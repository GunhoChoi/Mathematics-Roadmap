# Gamma Distribution
# P(X=x|alpha,beta) = (beta[i]**alpha[i])*(x[j]**(alpha[i]-1))*(math.exp(-beta[i]*x[j]))/math.gamma(alpha[i])

import math
import matplotlib.pyplot as plt

alpha = [1,2,3,3]
beta = [1,1,1,0.5] 
x = [(i+1)/10 for i in range(100)]
color = ['b','g','r','c','m','y','k']

for i in range(len(alpha)):
	prob = []
	for j in range(len(x)):
		prob.append((beta[i]**alpha[i])*(x[j]**(alpha[i]-1))*(math.exp(-beta[i]*x[j]))/math.gamma(alpha[i]))

	plt.plot(x,prob,c=color[i],label="alpha={} beta={}".format(alpha[i],beta[i]))

plt.legend()
plt.title("Gamma Distrbution")
plt.show()
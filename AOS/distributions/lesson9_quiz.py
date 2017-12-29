# Gamma Distribution
# P(X=x|alpha,beta) = (beta[i]**alpha[i])*(x[j]**(alpha[i]-1))*(math.exp(-beta[i]*x[j]))/math.gamma(alpha[i])

import math
import matplotlib.pyplot as plt

alpha = [9]
beta = [390] 
x = [(i+1)/10 for i in range(1200)]
color = ['b','g','r','c','m','y','k']

for i in range(len(alpha)):
	prob = []
	for j in range(len(x)):
		prob.append((beta[i]**alpha[i]*alpha[i])/(beta[i]+x[j])**(alpha[i]+1))

	plt.plot(x,prob,c=color[i],label="alpha={} beta={}".format(alpha[i],beta[i]))

plt.legend()
plt.title("Gamma Distrbution")
plt.show()
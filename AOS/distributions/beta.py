# Beta Distribution
# P(X=x|alpha,beta) = math.gamma(alpha+beta)/(math.gamma(alpha)*math.gamma(beta))*x**(alpha-1)*(1-x)**(beta-1)

import math
import matplotlib.pyplot as plt

alpha = [0.5,5,1,2,2]
beta = [0.5,1,3,2,5] 
x = [(i+1.5)/50 for i in range(48)]
color = ['b','g','r','c','m','y','k']

for i in range(len(alpha)):
	prob = []
	for j in range(len(x)):
		#print(alpha[i],beta[i],x[j])
		prob.append(math.gamma(alpha[i]+beta[i])/(math.gamma(alpha[i])*math.gamma(beta[i]))*(x[j]**(alpha[i]-1))*((1-x[j])**(beta[i]-1)))

	plt.plot(x,prob,c=color[i],label="alpha={} beta={}".format(alpha[i],beta[i]))

plt.legend()
plt.title("Beta Distrbution")
plt.show()
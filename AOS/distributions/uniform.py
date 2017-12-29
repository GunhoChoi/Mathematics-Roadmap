# Uniform Distribution
# f(x|a,b) = 1/(b-a)

import math
import matplotlib.pyplot as plt

a = 2
b = 8
color = ['b','g','r','c','m','y','k']

prob = []
for i in range(a,b):
	prob.append(1/(b-a))

plt.plot([x for x in range(a,b)],prob,c=color[0])

plt.title("Uniform Distrbution")
plt.show()
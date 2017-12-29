import math

alpha=3
beta=200

gamma = (beta**alpha)*(x[j]**(alpha-1))*(math.exp(-beta*x[j]))/math.gamma(alpha)

print(gamma)
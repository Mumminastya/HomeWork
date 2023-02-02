import numpy as np
import math as m
import sys

n = 120
p = 0.25
k = 0

w = np.random.randint(0, 4, n)
for i in w:
    if i == 1:
        k +=1
Py = m.pow(p, k)
Cnk = m.factorial(k) / (m.factorial(n) * m.factorial(n-k))
print("{:.2E}".format(Py))
print("{:.2E}".format(Cnk))
print(n, k)
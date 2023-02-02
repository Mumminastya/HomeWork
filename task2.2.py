import matplotlib.pyplot as plt
import numpy as np

r = []
for i in range(0, 10):
    ar = np.random.uniform(0, 10, 10)
    r.append(sum(ar))

plt.hist(r)
plt.xlabel('sum')
plt.ylabel('probability')
plt.title('hist')
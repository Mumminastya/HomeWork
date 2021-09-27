import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
n=1
plt.plot(x, np.cos(n*x), marker = "o")
n=2
plt.plot(x, np.cos(n*x), marker = "x")


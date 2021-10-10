import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
plt.plot(x, 3 * x + 4, marker = "o")
plt.plot(x, x - 1, marker = "x")
plt.plot(x, -2  * x + 9, marker = "o")
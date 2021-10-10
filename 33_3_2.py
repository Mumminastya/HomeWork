import math as m
import matplotlib.pyplot as plt

def convertCoord(p, fi_grad):
    fi = fi_grad * m.pi / 180

    x = p * m.cos(fi)
    y = p * m.sin(fi)
    return [x, y]

r = 10
x = []
y = []
for i in range(0, 360, 1):
    coord = convertCoord(r, i)
    x.append(coord[0])
    y.append(coord[1])

plt.plot(x, y)
import math as m
import matplotlib.pyplot as plt


def convertCoord(p, fi_grad):
    fi = fi_grad * m.pi / 180

    x = p * m.cos(fi)
    y = p * m.sin(fi)
    return [x, y]


fi = 45

x = []
y = []
for i in range(0, 50, 1):
    coord = convertCoord(i, fi)
    x.append(coord[0])
    y.append(coord[1])

plt.plot(x, y)
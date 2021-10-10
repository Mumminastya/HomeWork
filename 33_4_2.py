import math as m
import numpy
import matplotlib.pyplot as plt


def calc(minx, maxx, step, res, max_depth, cur_depth):
    prev_x = 0;
    cur_x = 0;
    for x in numpy.arange(minx, maxx, step):
        z = m.exp(x) + 2 * x - m.pow(x, 3) - 1
        if z < res:
            prev_x = x
        if z >= res:
            cur_x = x
            if (max_depth == cur_depth):
                return [prev_x, cur_x, z]
            else:
                print(prev_x, cur_x, z)
                return calc(prev_x, cur_x, step / 10, res, max_depth, cur_depth + 1)


print(calc(0, 10, 1, 1, 7, 1))
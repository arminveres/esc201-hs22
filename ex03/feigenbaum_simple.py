#!/bin/python3
"""
Draw a Feigenbaum diagram that results from solving the logistic equation.
(Optional: Implement a function that allows you to zoom into the Feigenbaum diagram)
"""

import numpy as np
import matplotlib.pyplot as plt

# Simple Version
# --------------
def LogisticsEqSimple(a, x):
    xinfList = []
    xn = x
    for _ in range(1000):
        xn = a * xn * (1 - xn)
        xinfList.append(xn)
    return xinfList


aListLen = 100
xListLen = 100

aList = np.linspace(0.0, 4, aListLen)
xList = np.linspace(0.0, 1, xListLen)

fig, ax = plt.subplots()

x_0 = 0.5

for i in range(aListLen):
    xinfList = LogisticsEqSimple(aList[i], 0.5)
    # if i > (len(aList) / 2):
        # print(i)
        # plt.scatter(aList[i] * np.ones_like(xinfList[i]), xinfList[i], s=1, c="#000000")
    for j in range(xListLen // 2, xListLen):
        plt.scatter(aList[i] * np.ones_like(xinfList[j]), xinfList[j], s=1, c="#000000")

plt.plot()
plt.savefig("feigenbaum_simple.jpg")
plt.show()

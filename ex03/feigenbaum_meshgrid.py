#!/bin/python3
"""
Draw a Feigenbaum diagram that results from solving the logistic equation.
(Optional: Implement a function that allows you to zoom into the Feigenbaum diagram)
"""

import numpy as np
import matplotlib.pyplot as plt

# Meshgrid version
# ----------------
def LogisticsEqMeshgrid(a: np.ndarray, x: np.ndarray):
    # make 1000 iterations
    for _ in range(1000):
        x = a * x * (1 - x)
    return x


aListLen = 500
xListLen = 500

aList = np.linspace(0.0, 4, aListLen)
xList = np.linspace(0.1, 0.9, xListLen)

A, X = np.meshgrid(aList, xList)

# print(A)
# print(X)

feigenbaum = LogisticsEqMeshgrid(A, X)
# print(feigenbaum)

nplot = xListLen // 2  # do not plot the initial transition

fig, ax = plt.subplots()
# ax.set_xlim(0, 4)
# ax.set_ylim(0, 1)

for i in range(len(aList)):
    ax.scatter(
        aList[i] * np.ones_like(feigenbaum[nplot:, i]),
        feigenbaum[nplot:, i],
        s=1,
        c="#000000",
    )

plt.plot()
plt.savefig("feigenbaum_meshgrid.jpg")
plt.show()

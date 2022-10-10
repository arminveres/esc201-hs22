#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt


def getFractal(use_const: bool, constant=0.0):
    x_res = 500
    y_res = 500
    x_linspace = np.linspace(-2.0, 1.0, x_res)
    y_linspace = np.linspace(-1.5, 1.5, y_res)
    X, Y = np.meshgrid(x_linspace, y_linspace)
    # convert to Grid
    Z = X + Y * 1j
    # Starting Copy
    C = np.copy(Z)
    # keep count for color
    count = np.zeros_like(Z, dtype=int)
    # get max values
    rmax = np.maximum(abs(C), 2)

    k = 0
    while k < 100:
        # initial condition used for the meshgrids
        cond = Z < rmax
        # apply for each value that does not exceed/diverge
        if use_const:
            Z[cond] = Z[cond] ** 2 + constant
        else:
            Z[cond] = Z[cond] ** 2 + C[cond]
        count[cond] += 1
        k += 1
    return C, count


# def drawFractal():
#     return


if __name__ == "__main__":
    fig, ax = plt.subplots()

    C, count = getFractal(True, -0.5)

    # print("done")
    ax.scatter(C.real, C.imag, s=1, c=count)

    # plt.plot()
    plt.show()

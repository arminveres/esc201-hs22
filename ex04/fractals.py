#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt


def getFractal(draw_julia: bool, constant=0.0):
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
        cond = abs(Z) < rmax
        # apply for each value that does not exceed/diverge
        if draw_julia:
            Z[cond] = Z[cond] ** 2 + constant
        else:
            Z[cond] = Z[cond] ** 2 + C[cond]
        count[cond] += 1
        k += 1
    return C, count


if __name__ == "__main__":

    fig, ax = plt.subplots()
    C, count = getFractal(draw_julia=False, constant=0)
    ax.scatter(C.real, C.imag, s=1, c=count)
    plt.plot()
    plt.savefig("mandelbrot.png")

    fig, ax = plt.subplots()
    C, count = getFractal(draw_julia=True, constant=0.5 - 0.5j)
    ax.scatter(C.real, C.imag, s=1, c=count)
    plt.plot()
    plt.savefig("julia0.5.png")

    fig, ax = plt.subplots()
    C, count = getFractal(draw_julia=True, constant=0.8 - 0.8j)
    ax.scatter(C.real, C.imag, s=1, c=count)
    plt.plot()
    plt.savefig("julia0.8.png")


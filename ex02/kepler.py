#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

e = 0.5
a = 1
T = a ** (3 / 2)
n = (2 * np.pi) / T


def getM(t):
    """
    Returns: value M, mean anomaly
    """
    return n * t


def fKepler(E, M):
    return E - e * np.sin(E) - M


def fKeplerPrime(E):
    return 1 - e * np.cos(E)


def newton(f, fPrime, Estart, M):
    # print(M)
    E = Estart
    tol = 0.001
    dx = tol + 1
    while abs(dx) > tol:
        dx = -f(E, M) / fPrime(E)
        Enew = E + dx
        E = Enew
    # print(dx, Enew, E)
    return E


def update(frame):
    M = getM(frame)
    E = newton(fKepler, fKeplerPrime, M, M)
    x = a * np.cos(E) - a * e
    # y = b * np.sin(E)
    assert e <= 1  # e must not be greater than 1 bc. square root
    y = a * np.sqrt(1 - e**2) * np.sin(E)

    xdata.append(x)
    ydata.append(y)
    ln.set_data(xdata, ydata)
    return (ln,)


def init():
    # plt.cla()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    return (ln,)


if __name__ == "__main__":

    fig, ax = plt.subplots()
    xdata, ydata = [], []
    (ln,) = plt.plot([], [], "ro", animated=True)

    ani = FuncAnimation(
        fig,
        update,
        frames=np.linspace(0, T, 50),
        init_func=init,
        blit=True,
        interval=50,
    )

    plt.scatter(0, 0)
    # plt.show()
    ani.save("kepler_equation.mp4", writer="ffmpeg", dpi=250)
    plt.show()

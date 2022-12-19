#!/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

EPSILON = 1e0


def odeHO(p, q):
    """
    Harmonic oscillator
    """
    dpdt = -q
    dqdt = p
    return (dpdt, dqdt)


def odePendulum(p, q):
    """
    Pendulum
    """
    dpdt = -EPSILON * np.sin(q)
    dqdt = p
    return (dpdt, dqdt)


def leapFrog(p0, q0, h, odeSystem):
    q12 = q0 + 0.5 * h * p0  # first drift
    dp, dq = odeSystem(p0, q12)
    p1 = p0 + h * dp  # kick
    q1 = q12 + 0.5 * h * p1  # second drift
    return (p1, q1)


def euler(p, q, h, odeSystem):
    dp, dq = odeSystem(p, q)
    p += h * dp
    q += h * dq
    return (p, q)


def rk2MidPoint(p, q, h, odeSystem):
    dp, dq = odeSystem(p, q)
    q12 = q + 0.5 * h * dq
    k2p, k2q = odeSystem(p + 0.5 * h, q12)
    q += h * k2q
    p += h * k2p
    return p, q


def rk4(p, q, h, odeSystem):
    pass


# optional for function animation
# def update(frame):
#     global p,q
#     #p, q = leapFrog(p, q, h, odeHO)
#     p, q = euler(p, q, h, odeHO)
#     xdata.append(q)
#     ydata.append(p)
#     ln.set_data(xdata, ydata)
#     return ln,

if __name__ == "__main__":
    Fig1, axs = plt.subplots(2, 4, layout='constrained')
    # Fig1.tight_layout(pad=7.0)

    """
    initial conditions
    HO: p=0, q=1, q=2, q=3

    Pendulum: q is angle, range is [-pi,pi]
    For circulation you need an additional momentum p /= 0

    axs[0,0]: phase plot HO using leap frog
    axs[0,1]: phase plot HO using euler or rk2 or rk4
    axs[1,0]: phase plot pendulum using leap frog
    axs[1,1]: phase plot pendulum using euler or rk2 or rk4
    """
    h = 1e-2
    rangelen = 5000
    inits_q = [1, 2, 3, 3.14]

    axs[0, 0].set_title("Leapfrog Harmonic Oscillator")
    for qs in inits_q:
        q = qs
        p = 0
        xdata = []
        ydata = []
        for i in range(rangelen):
            p, q = leapFrog(p, q, h, odeSystem=odeHO)
            xdata.append(q)
            ydata.append(p)
        axs[0, 0].plot(xdata, ydata, "-")

    axs[0, 1].set_title("Euler Harmonic Oscillator")
    for qs in inits_q:
        q = qs
        p = 0
        xdata = []
        ydata = []
        for i in range(rangelen):
            p, q = euler(p, q, h, odeSystem=odeHO)
            xdata.append(q)
            ydata.append(p)
        axs[0, 1].plot(xdata, ydata)

    axs[1, 0].set_title("Leapfrog Pendulum")
    for qs in inits_q:
        q = qs
        xdata = []
        ydata = []
        p = 0
        for i in range(rangelen):
            p, q = leapFrog(p, q, h, odeSystem=odePendulum)
            xdata.append(q)
            ydata.append(p)
        axs[1, 0].plot(xdata, ydata)

    axs[1, 1].set_title("Euler Pendulum")
    for qs in inits_q:
        q = qs
        p = 0
        xdata = []
        ydata = []
        for i in range(rangelen):
            p, q = euler(p, q, h, odeSystem=odePendulum)
            xdata.append(q)
            ydata.append(p)
        axs[1, 1].plot(xdata, ydata)

    axs[0, 2].set_title("Leapfrog Pendulum negative")
    inits_q = [-3, -2, -1]
    for qs in inits_q:
        q = qs
        p = 0
        xdata = []
        ydata = []
        for i in range(rangelen):
            p, q = leapFrog(p, q, h, odeSystem=odePendulum)
            xdata.append(q)
            ydata.append(p)
        axs[0, 2].plot(xdata, ydata)

    axs[1, 2].set_title("Leapfrog Pendulum p!=0, p=1")
    for qs in inits_q:
        q = qs
        p = 1
        xdata = []
        ydata = []
        for i in range(rangelen):
            p, q = leapFrog(p, q, h, odeSystem=odePendulum)
            xdata.append(q)
            ydata.append(p)
        axs[1, 2].plot(xdata, ydata)

    axs[0, 3].set_title("Midpoint Oscillator")
    for qs in inits_q:
        q = qs
        p = 1
        xdata = []
        ydata = []
        for i in range(rangelen):
            p, q = rk2MidPoint(p, q, h, odeSystem=odeHO)
            xdata.append(q)
            ydata.append(p)
        axs[0, 3].plot(xdata, ydata)

    axs[1, 3].set_title("Midpoint Pendulum")
    for qs in inits_q:
        q = qs
        p = 1
        xdata = []
        ydata = []
        for i in range(rangelen):
            p, q = rk2MidPoint(p, q, h, odeSystem=odePendulum)
            xdata.append(q)
            ydata.append(p)
        axs[1, 3].plot(xdata, ydata)

    plt.show()
    Fig1.savefig("leapfrog_subplots.png")

#!/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def odeSolver(t0, y0, dfFunc, h, nSteps, solverStepFunc):
    """This is a general ODE solver that takes the
    derivative df/dt (dfFunc) and the algorithm for one time
    step (solverStepFunc) as function arguments.
    t0 = Initial time
    y0 = Initial function values (array)
    nSteps = Total number of integration steps
    solverStepFunc = Euler Method, Midpoint RK or RK4
    """
    yn = y0
    tn = t0
    tlist = [t0]
    ylist = [y0]
    for n in range(nSteps):
        yn1 = solverStepFunc(tn, yn, h, dfFunc)
        tn1 = tn + h
        tlist.append(tn1)
        ylist.append(yn1)
        tn = tn1
        yn = yn1
    return (np.array(tlist), np.array(ylist))


def eulerStep(tn, yn, h, dfdt):
    yn1 = yn + h * dfdt(tn, yn)
    return yn1


def MidPointRK2Step(tn, yn, h, dfdt):
    y_n1 = yn + h * dfdt(tn + h / 2, yn + (h / 2) * dfdt(tn, yn))
    return y_n1


def RK4Step(tn, yn, h, dfdt):
    pass


def LotkaVolterra(t, y):
    """
    Implements the Lotka Volterra System dm/dt and dfox/dt
    where y=(m,fox), dy/dt=(dm/dt, dfox/dt)
    """
    K_m = 2
    K_mf = 0.02
    K_fm = 0.01
    K_f = 1.06
    m, f = y
    dmdt = K_m * m - K_mf * m * f
    dfoxdt = -K_f * f + K_fm * f * m
    return np.array([dmdt, dfoxdt])


if __name__ == "__main__":

    h = 0.001
    nSteps = 60000
    t0 = 0
    y0 = np.array([100, 15])  # y0[0] = mice, y0[1] = foxes
    init_cond_phase = np.linspace(
        1.0, 100.0, 25
    )  # initial conditions for mice population (prey)

    t, y = odeSolver(t0, y0, LotkaVolterra, h, nSteps, eulerStep)
    plt.figure()
    plt.grid()
    plt.title("Forward Euler method")

    plt.plot(t, y[:, 0], "xb", label="Mice")  # population versus time
    plt.plot(t, y[:, 1], "+r", label="Foxes")  # population versus time

    plt.xlabel("Time t, [days]")
    plt.ylabel("Population")
    plt.legend()
    plt.savefig("euler_pop.png")
    plt.show()

    # phase plot
    plt.figure()
    for mice in init_cond_phase:
        X0 = np.array([mice, 15])
        t, y = odeSolver(t0, X0, LotkaVolterra, h, nSteps, eulerStep)
        plt.plot(y[:, 0], y[:, 1], "-", label="$m_0 =$" + str(X0[0]))
    plt.xlabel("Mice")
    plt.ylabel("Foxes")
    plt.legend()
    plt.title("Mice vs Foxes")
    plt.savefig("euler_phase.png")
    plt.show()

    t, y = odeSolver(t0, y0, LotkaVolterra, h, nSteps, MidPointRK2Step)
    plt.figure()
    plt.grid()
    plt.title("Midpoint Runge-Kutta method")

    plt.plot(t, y[:, 0], "xb", label="Mice")  # population versus time
    plt.plot(t, y[:, 1], "+r", label="Foxes")  # population versus time

    plt.xlabel("Time t, [days]")
    plt.ylabel("Population")
    plt.legend()
    plt.savefig("midpoint_pop.png")
    plt.show()

    # phase plot
    plt.figure()
    for mice in init_cond_phase:
        X0 = np.array([mice, 15])
        t, y = odeSolver(t0, X0, LotkaVolterra, h, nSteps, MidPointRK2Step)
        plt.plot(y[:, 0], y[:, 1], "-", label="$m_0 =$" + str(X0[0]))
    plt.xlabel("Mice")
    plt.ylabel("Foxes")
    plt.legend()
    plt.title("Mice vs Foxes")
    plt.savefig("midpoint_phase.png")
    plt.show()

    # t, y = odeSolver(t0, y0, LotkaVolterra, h, nSteps, RK4Step)
    #
    # plt.plot(t, y[:,0], ..)
    #  ... # phase plot
    #
    # plt.show()

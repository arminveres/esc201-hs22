#!/bin/python3

import numpy as np


def abc_solver(a: float, b: float, eps: float, func):
    """
    params:
            a: lower bound
            b: upper bound
            eps: epsilon error range
            func: function to test for
    """
    # Check whether the inputs can be used: a as lower bound and b as upper bound
    if a > b:
        tmp = a
        a = b
        b = tmp

    while True:
        c: float = (a + b) / 2
        # only recheck bounds if outside epsilon region
        if not abs(a - b) < eps:
            if func(c) > 0:
                b = c
            else:
                a = c
        else:
            return c
        # print(func(c))


def par_q_solver(a: float, b: float, c: float):
    q: float = -0.5 * (b + np.sign(b) * np.sqrt((b * b) - 4 * a * c))
    return (q / a, c / q)


if __name__ == "__main__":
    print("Solving for 'x**x-100 = 0,':")
    print(f"\tabc solver: x = {abc_solver(-100, 100, 1e-6, lambda x : x**x - 100)}")

    print("Solving for '1x^2 + 1x + 0 = 0':")
    print(f"\tabc solver: x = {abc_solver(-5, 5, 1e-6, lambda x: x**2 + x)}")
    print(f"\tq solver: {par_q_solver(1, 1, 0)}")

    print("Solving for '35x^2 + 15x - 10 = 0':")
    print(
        f"\tabc solver: x = {abc_solver(-100, 100, 1e-9, lambda x: 35*(x**2) + 15*x - 10)}"
    )
    print(f"\tq solver: {par_q_solver(35, 15, -10)}")

    print("Solving for '35x^3 + 15x^2 - 10x = 0':")
    print(
        f"\tabc solver: x = {abc_solver(-100, 100, 1e-9, lambda x: 35*(x**3) + 15*(x**2) - 10*x)}"
    )

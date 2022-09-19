import numpy as np


def abc_solver(a: float, b: float, eps: float, func):
    """
    params:
            a: lower bound
            b: upper bound
            eps: epsilon range
            func: function to test for
    """
    # Check whether the inputs can be used: a as lower bound and b as upper bound
    if a > b:
        tmp = a
        a = b
        b = tmp
        if a > 0 and b > 0 or a < 0 and b < 0:
            return

    while True:
        c = (a + b) / 2

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
    print(
        f"x**x-100 = 0, x = {abc_solver(-100, 100, 1/1_000_000, lambda x : x**x - 100)}"
    )
    print(
        f"1x^2 + 1x + 0 = 0, x = {abc_solver(-100, 100, 1/1_000_000, lambda x: x**2 + x)}"
    )
    print(
        f"35x^2 + 15x + 1144 = 0, x = {abc_solver(-100, 100, 1/1_000_000_000, lambda x: 35*(x**2) + 15*x + 1144)}"
    )

    print(par_q_solver(35, 15, 0))

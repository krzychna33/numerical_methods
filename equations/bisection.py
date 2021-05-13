import numpy as np
from sympy import *


def bisection(f, E, a, b, out):
    x0 = (a + b) / 2
    print("x0 = {}".format(x0))

    i = 1
    while np.abs(f(x0)) > E:
        if i > out:
            return None
        if f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0
        x0 = (a + b) / 2
        print("x{} = {}".format(i, x0))
        i+=1

    return x0


if __name__ == "__main__":
    x = Symbol("x")

    p = 1
    q = 2

    E = np.float_power(10, -5)

    # a = 7
    # f_raw = x**2 - a

    # f_raw = x ** 3 + x - 1000

    # f_raw = x* exp(-3*x)

    # f_raw = x ** 3 - sinh(x) + 4 * x**2 + 6*x + 9
    # f_raw = x ** 3 - 5 * x + 3

    f_raw = x ** 2 - 2

    f = lambdify(x, f_raw, "numpy")

    p = bisection(f, E, p, q, 100)
    print(p)

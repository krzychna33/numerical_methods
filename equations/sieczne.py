from sympy import *
import numpy as np
x = Symbol("x")


def sieczne(f_raw, E, p, q):
    f = lambdify(x, f_raw, "numpy")
    fp1_raw = diff(f_raw)
    fp1 = lambdify(x, fp1_raw, "numpy")
    fp2_raw = diff(fp1_raw)
    fp2 = lambdify(x, fp2_raw, "numpy")

    # x0 = None
    # if fp1(p)*fp2(p)>0:
    #     x0 = q
    # else :
    #     x0 = p

    x0 = p
    x1 = q

    print("x0 = {}".format(x0))
    print("E = {}".format(E))
    print("f = {}".format(f_raw))
    print("fp1 = {}".format(fp1_raw))
    print("fp2 = {}".format(fp2_raw))

    i = 1
    while np.abs(f(x0)) > E:
        nx1 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = nx1
        print("x{} = {}".format(i - 1, x0, i, x1))
        i += 1
    return x0


if __name__ == "__main__":
    x = Symbol("x")

    # RANGE
    p = 3
    q = 2

    E = np.float_power(10, -5)

    # a = 7
    # f_raw = x**2 - a

    # f_raw = x ** 3 + x - 1000

    # f_raw = x* exp(-3*x)

    # f_raw = x ** 3 - sinh(x) + 4 * x**2 + 6*x + 9

    f_raw = x ** 4 - 4 ** 3
    sieczne(f_raw, E, p, q)

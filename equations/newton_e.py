from sympy import *
import numpy as np


def newton(f_raw, E, x0):
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

    print("x0 = {}".format(x0))
    print("E = {}".format(E))
    print("f = {}".format(f_raw))
    print("fp1 = {}".format(fp1_raw))
    print("fp2 = {}".format(fp2_raw))

    i = 1
    while np.abs(f(x0)) > E:
        x0 = x0 - (f(x0) / fp1(x0))
        print("x{} = {}".format(i, x0))
        i += 1

    return x0


if __name__ == "__main__":
    x = Symbol("x")

    a = 2
    E = np.float_power(10, -10)
    f_raw = x ** 2 - a
    # f_raw = x**3 - a

    # f_raw = x* exp(-3*x)
    # f_raw = x ** 3 - x -1
    print(newton(f_raw, E, 2))

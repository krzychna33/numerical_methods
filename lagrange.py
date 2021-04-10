from sympy import *
from scipy.interpolate import lagrange


def l1(x_arr, y_arr, x0):
    print('--- LAGRANGE INTERPOLATION ---')
    x = Symbol('x')

    sum = 0
    for i in range(0, len(x_arr)):
        l = 1
        for j in range(0, len(x_arr)):
            if i != j:
                l = l * (x - x_arr[j]) / (x_arr[i] - x_arr[j])
        sum += y_arr[i] * l
    print(sum)
    print(simplify(sum))
    mm = Poly(sum, x)
    print(mm.coeffs())
    f = lambdify(x, sum, "numpy")
    return f(x0)


def l2(x_arr, y_arr, x0):
    print('--- LAGRANGE INTERPOLATION ---')

    sum = 0
    for i in range(0, len(x_arr)):
        l = 1
        for j in range(0, len(x_arr)):
            if i != j:
                l *= (x0 - x_arr[j]) / (x_arr[i] - x_arr[j])
        sum += y_arr[i] * l
    return sum


def l3(x_arr, y_arr, x0):
    print('--- LAGRANGE INTERPOLATION ---')

    return lagrange(x_arr, y_arr)(x0)


if __name__ == "__main__":
    # X = [1, 4, 9]
    # Y = [1, 2, 3]

    X = [1,2,3]
    Y = [6,8,2]

    print(l1(X, Y, 1))
    print(l2(X, Y, 1))
    print(l3(X, Y, 1))

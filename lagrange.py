from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


def l1(x_arr, y_arr, x0):
    x = Symbol('x')

    sum = 0
    for i in range(0, len(x_arr)):
        l = 1
        for j in range(0, len(x_arr)):
            if i != j:
                l = l * (x - x_arr[j]) / (x_arr[i] - x_arr[j])
        sum += y_arr[i] * l
    print(sum)
    f = lambdify(x, sum, "numpy")
    return f(x0)


def l2(x_arr, y_arr, x0):
    sum = 0
    for i in range(0, len(x_arr)):
        l = 1
        for j in range(0, len(x_arr)):
            if i != j:
                # print('(' + str(x0) + '-' + str(x_arr[j]) + ')/(' + str(x_arr[i]) + '-' + str(x_arr[j]) + ")")
                l *= (x0 - x_arr[j]) / (x_arr[i] - x_arr[j])
        sum += y_arr[i] * l
    return sum


def l3(x_arr, y_arr, x0):
    return lagrange(x_arr, y_arr)(x0)


X = [1, 4, 9]
Y = [1, 2, 3]

k = np.arange(1, 16, 0.1)

plt.plot(k, l1([1, 4, 9, 16], [1, 2, 3, 4], k))
plt.plot(k, np.sqrt(k))
# plt.plot(k, l2([1,2,3], [49,64,81], k))
# plt.plot(k, l3(X, [101, 97, 104], k))
plt.show()

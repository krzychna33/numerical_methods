import numpy as np
import matplotlib.pyplot as plt
from newton import newton_interpolation1_raw

k = np.arange(-10, 15, 0.0001)
# poly = np.poly1d((1, -36, 546, -4536, 22449, - 67284, 118124, -109584, 40320))
# print(poly)
# print(poly.r)
#
# plt.plot(k, poly(k), 'r')
# plt.show()

X1 = [0, 1, 2, 3, 4, 5]
Y1 = [0, 1, 2, 3, 4, 5]

X2 = [0, 1, 2, 3, 4, 5]
Y2 = [0, 1, 2.001, 3, 4, 5]

val1 = newton_interpolation1_raw(X1, Y1)(14)
val2 = newton_interpolation1_raw(X2, Y2)(14)

print(val1)
print(val2)

val3 = newton_interpolation1_raw(X1, Y1)(2.5)
val4 = newton_interpolation1_raw(X2, Y2)(2.5)

print(val3)
print(val4)

plt.plot(k, newton_interpolation1_raw(X1, Y1)(k), 'r')
plt.plot(k, newton_interpolation1_raw(X2, Y2)(k), 'g')
plt.plot(k, k, 'b')


plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')


plt.show()
import numpy as np
import matplotlib.pyplot as plt
from newton import newton_interpolation1_raw

k = np.arange(-10, 15, 0.001)
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

print("V1= {}".format(val1))
print("V2= {}".format(val2))

val3 = newton_interpolation1_raw(X1, Y1)(20)
val4 = newton_interpolation1_raw(X2, Y2)(20)

print("V3= {}".format(val3))
print("V4= {}".format(val4))

plt.plot(k, newton_interpolation1_raw(X1, Y1)(k), 'r')
plt.plot(k, newton_interpolation1_raw(X2, Y2)(k), 'g')
plt.plot(k, k, 'b')


plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')


plt.show()
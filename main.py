from newton import newton_interpolation1
from lagrange import l1, l2, l3
import matplotlib.pyplot as plt
import numpy as np

# X2 = [0,2,3,4,6]
# Y2 = [1,3,2,5,7]

X2 = [1,2,3,4]
Y2 = [1,5,14,30]

# X2 = [1,2,3,4]
# Y2 = [5,8,2,9]


print(newton_interpolation1(X2,Y2)(7))
print(l1(X2,Y2)(7))

k = np.arange(X2[0], X2[len(X2)-1], 0.0001)
plt.plot(k, newton_interpolation1(X2,Y2)(k), 'r')
plt.plot(k, l1(X2, Y2)(k), 'g')
plt.plot(k, np.sqrt(k), 'b')
plt.scatter(X2, Y2)
plt.show()
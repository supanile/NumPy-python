import numpy as np

x = np.arange(15)
print("x is\n", x)

x = x.reshape((3, 5))
print("x is\n", x)

y = x.sum(axis=0)
print("sum of y is", y)

z = x.sum(axis=1)
print("sum of y is", z)

x = x.sum()
print("sum of y is", x)

import numpy as np

x = np.array([1,2,3,4,5])
print(x.dtype)

y = np.array([1.1,2.2,3.3,4.4,5.5])
print(y.dtype)

x = np.array([1,2,3,4,5], dtype = np.float32)
print(x.dtype)
print(x)

y = np.array([1.1,2.2,3.3,4.4,5.5], dtype = np.int64)
print(y.dtype)
print(y)

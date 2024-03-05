import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
print("x is\n",x)

y = x.reshape((3,3))
print("y is\n",y)

y = y*10+10
print("ynew is\n",y)
import numpy as np

x = np.array([0,1,2,3,4,5])
print("x is\n",x)

x = x.reshape((2,3))
print("xnew is\n",x)

x = np.zeros((2,3))
print("x is\n",x)

x = np.ones((2,3))
print("x is\n",x)

y = np.empty((3,3))
print("y is\n",y)
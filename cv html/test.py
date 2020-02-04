import numpy as np

def f(u):
    return u[0]**2 + u[1]**2


Grid=np.array([u for u in zip(range(10),range(10))])

print(Grid)


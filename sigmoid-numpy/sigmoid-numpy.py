import numpy as np

def sigmoid(x):
    x = np.asarray(x, dtype=float)
    x = -x
    y = np.exp(x)
    z = 1 + y
    s = 1 / z
    return s
    # Write code here
    pass
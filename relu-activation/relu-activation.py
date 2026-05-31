import numpy as np

def relu(x):
    x = np.asarray(x)
    return np.maximum(0, x) #so getting the largest value between 0 and the number
    pass
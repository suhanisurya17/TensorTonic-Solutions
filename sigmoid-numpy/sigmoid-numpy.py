import numpy as np

def sigmoid(x):
    #steps
    #1. make x negative
    #2. put it to e^-x
    #3. add 1
    #4. put it all over 1
    print(type(x))
    print(x)
    x = np.asarray(x, dtype = float)#.asarray converts a list into an array, parameters: the list, the datatype
    x = -x
    y = np.exp(x)
    z = 1 + y
    a = 1 / z

    return a
    pass
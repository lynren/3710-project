import numpy as np
import math
import random

def genUniformValues(num_to_generate):
    a = 16807
    m = 2**31 - 1
    e = math.e
    x_prev = random.randint(1, 256)
    values = []

    for i in range(num_to_generate+1):
        x = (a*x_prev + e) % m
        if i != 0:
            values.append(x / m)
        x_prev = x

    return values


def genExponentialValues(lmbda, num_to_generate):
    #lmbda = 67
    uniform_values = genUniformValues(num_to_generate)
    return [(-1/lmbda) * np.log(1-u) for u in uniform_values]

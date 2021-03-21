import numpy as np

def genUniformValues():
    a = 16807
    m = 2**31 - 1
    e = 43
    x_prev = 61
    values = []

    for i in range(1, 100):
        x = (a*x_prev + e) % m
        values.append(x / m)
        x_prev = x

    return values


def genExponentialValues():
    lmbda = 67
    uniform_values = genUniformValues()
    return [(-1/lmbda) * np.log(1-u) for u in uniform_values]

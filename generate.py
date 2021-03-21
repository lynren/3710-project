import math
import random
import numpy as np

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
    uniform_values = genUniformValues(num_to_generate)
    return [(-1/lmbda) * np.log(1-u) for u in uniform_values]


def poisson(x):
    return (2**x * math.exp(-2)) / math.factorial(x)


def poissonSum(x):
    sum_ = 0
    res = []
    for i in range(x+1):
        p_i = poisson(i)
        res.append(p_i + sum_)
        sum_ += p_i
    return res


def uniToPoisson(r, p_sums):
    return next(p_val for p_val, p_sum in enumerate(p_sums) if r <= p_sum)


def uniValuesToPoissonValues(uni_values):
    p_sums = poissonSum(22)
    return [uniToPoisson(uni_value, p_sums) for uni_value in uni_values]

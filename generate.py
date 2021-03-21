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


def poisson(x: int, lmbda: float) -> float:
    """Computes poisson value of x"""
    return (lmbda**x * math.exp(-lmbda)) / math.factorial(x)


def poissonSum(x: int, lmbda: float) -> list:
    """Computes Poisson summation

    Parameters
    ----------
    x : int
        The summation upper bound

    Returns
    -------
    list
        a list of sums L such that L[i] = summation_(i=0)^x poisson(i)
    """
    sum_ = 0
    res = []
    for i in range(x+1):
        p_i = poisson(i, lmbda)
        res.append(p_i + sum_)
        sum_ += p_i
    return res


def uniToPoisson(r: float, p_sums: list) -> int:
    return next(p_val for p_val, p_sum in enumerate(p_sums) if r <= p_sum)


def genPoissonValues(num_to_gen, lmbda):
    p_sums = poissonSum(100, lmbda)
    uni_values = genUniformValues(num_to_gen)
    return [uniToPoisson(uni_value, p_sums) for uni_value in uni_values]

def simulate_queue_arrivals(times, mean, target):
    count_target = 0
    poisson_values = genPoissonValues(times, mean)
    for i in poisson_values:
        if i == target:
            count_target = count_target + 1
    print("The simulated probability in "+str(times)+" times is: "+str(count_target/times))


def main():
    times = int(input("Enter number of runs:"))
    print(times)
    mean = int(input("Enter the mean value of arrival : "))
    print(mean)
    target = int(input("Enter the target value : "))
    print(target)
    simulate_queue_arrivals(times, mean, target)

if __name__ == "__main__":
    main()

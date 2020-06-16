import numpy as np


# First case: set a=0 and b=100
def Rosenbrock0(x):
    dx = 2 * x[0] - 400 * x[0] * (x[1] - (x[0] ** 2))
    dy = 200 * (x[1] - (x[0] ** 2))
    return dx, dy


# Second case: set a=1 and b=100
def Rosenbrock1(x):
    dx = (-2 * (1 - x[0]) - 400 * (x[1] - (x[0] ** 2) ** 2))
    dy = 200 * (x[1] - (x[0] ** 2))
    return dx, dy


def main():
    lrate = 0.002
    a = np.array([-.5, .2])
    epoch = 1000
    ai = []
    for i in range(epoch):
        f = ((1 - a[0]) ** 2) + (100 * ((a[1] - a[0] ** 2) ** 2))
        ai.append([a, f])
        fi = np.array(Rosenbrock1(a))
        a = a - np.dot(lrate, fi)

    ai = np.array(ai)
    print(ai[-10:-1])
    print(f'the minimum is: {ai[-1, 1]} at x: {ai[-1, 0]}')


if __name__ == '__main__':
    main()

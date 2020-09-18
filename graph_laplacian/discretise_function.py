import numpy as np


def discretise_function(f, resolution):
    n = resolution

    # np.fromfunction doesn't work when applied to weird functions
    f_disc = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            f_disc[i][j] = f(j/n, i/n)

    return f_disc


if __name__ == '__main__':
    # Evaluate cos(2*pi*x) on 4x4 evenly spaced points on the torus.
    # Result does not depend on y and takes values in the interval [-1, 1].
    f = lambda x, y: np.cos(2*np.pi*x)
    print(discretise_function(f,4))
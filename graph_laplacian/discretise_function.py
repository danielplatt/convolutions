import numpy as np

def discretise_function(f, resolution):
    n = resolution

    # np.fromfunction doesn't work when applied to
    f_disc = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            f_disc[i][j] = f(j/n, i/n)

    return f_disc

    # return np.fromfunction(lambda i, j: f(j/n, i/n), (n, n))
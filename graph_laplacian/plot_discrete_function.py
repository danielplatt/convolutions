import matplotlib.pyplot as plt
import numpy as np


def plot_discrete_function(f):
    assert f.shape[0] == f.shape[1] # square matrix?
    plt.imshow(f)
    plt.colorbar()
    plt.show()

def plot_discrete_function_multiple(functions, rescale_minimum=1):
    plt.figure()
    _, axarr = plt.subplots(1, len(functions))

    for num, f in zip(range(len(functions)), functions):
        if isinstance(f, tuple):
            axarr[num].set_title(f[1])
            f = f[0]
        f_max = max(rescale_minimum, np.max(f))
        f_min = min(rescale_minimum, np.min(f))

        axarr[num].imshow(f, vmin=f_min, vmax=f_max)

    plt.show()

if __name__ == '__main__':
    f = lambda x, y: np.cos(2*np.pi*x)

    resolution = 10
    n = resolution

    f_matrix = np.fromfunction(lambda i, j: f(j/n, i/n), (n, n))

    plot_discrete_function(f_matrix)

    plot_discrete_function_multiple([f_matrix, f_matrix])
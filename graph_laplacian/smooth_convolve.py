import numpy as np


def smooth_convolve(f, g, resolution, period=1):
    n = resolution

    def fg_function(x, y):
        f_matrix = np.fromfunction(lambda i, j: f(j * period / n, i * period / n), (n, n))  # columns=x-coordinate
        g_matrix = np.fromfunction(lambda i, j: g(j * period / n, i * period / n), (n, n))

        g_matrix = np.flip(g_matrix)
        g_matrix = np.roll(g_matrix, int(np.round(x*n)), axis=1)
        g_matrix = np.roll(g_matrix, int(np.round(y*n)), axis=0)

        fg_matrix = f_matrix * g_matrix

        return np.sum(fg_matrix) # should really have a /n**2 here, but somehow gives wrong thing

    return fg_function


if __name__ == '__main__':
    f = lambda x, y: np.cos(2*np.pi*x)
    g = lambda x, y: np.cos(2*np.pi*x)+np.cos(2*2*np.pi*x)
    conv = smooth_convolve(f, g, 80) # =f
    print((conv(0.0, 0.), f(0.0, 0.)))
    print((conv(0.2, 0.2), f(0.2, 0.2)))
    print((conv(0.2, 0.5), f(0.2, 0.5)))
    print((conv(0.5, 0.), f(0.5, 0.)))
    print((conv(0.6, 0.), f(0.6, 0.)))

import numpy as np

from graph_laplacian.discretise_function import discretise_function
from graph_laplacian.graph_convolve import graph_convolve
from graph_laplacian.plot_discrete_function import plot_discrete_function_multiple
from graph_laplacian.smooth_convolve import smooth_convolve


def path1(f, g, n, flavour='fourier_series'):
    f_mat = discretise_function(f, n)
    g_mat = discretise_function(g, n)
    return graph_convolve(f_mat, g_mat, flavour)


def path2(f, g, n, convolution_resolution=100):
    fg = smooth_convolve(f, g, convolution_resolution, period=1)
    disc_fg = discretise_function(fg, n)
    return disc_fg


def get_experiments():
    experiment_pairs = [
        (
            lambda x, y: np.cos(2 * np.pi * x),
            lambda x, y: np.cos(2 * np.pi * x) + np.cos(4 * np.pi * x)
        ),
        (
            lambda x, y: np.cos(2 * np.pi * x),
            lambda x, y: np.cos(2 * np.pi * y)
        ),
        (
            lambda x, y: np.cos(2 * np.pi * x),
            lambda x, y: np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)
        ),
        (
            lambda x, y: np.cos(2 * np.pi * x),
            lambda x, y: 1 + 0 * x
        ),
        (
            lambda x, y: (x - 0.5) ** 2 + (y - 0.5) ** 2,
            lambda x, y: np.cos(4 * np.pi * x) + np.cos(4 * np.pi * y)
        ),
        (
            lambda x, y: (x - 0.5) ** 2 + (y - 0.5) ** 2,
            lambda x, y: x + y
        ),
    ]
    return experiment_pairs


def main(flavour='fourier_series'):
    experiment_pairs = get_experiments()
    n = 10
    for f, g in experiment_pairs:
        path1_conv = path1(f, g, n, flavour)  # can choose 'scipy' instead
        path2_conv = path2(f, g, n, convolution_resolution=40)

        plot_discrete_function_multiple(
            [
                (discretise_function(f, n), 'f'),
                (discretise_function(g, n), 'g'),
                (path1_conv, 'f graph conv g'),
                (path2_conv, 'f smooth conv g')
            ],
            rescale_minimum=0.0001
        )


if __name__ == '__main__':
    main()

import numpy as np
from numpy import linalg as LA
from scipy.sparse import csgraph

from graph_laplacian.adjency_matrices import get_grid_adjaceny_matrix


def get_graph_laplacian_eigenbasis(n, flavour='fourier_series'):
    if flavour == 'fourier_series':
        basis = []
        for k in range(n):
            for l in range(n):
                basis += [discrete_laplacian_eigenfunction(n, k, l)]
        return basis
    elif flavour == 'scipy':
        G = get_grid_adjaceny_matrix(n)
        L = csgraph.laplacian(G, normed=False)
        basis = np.transpose(LA.eig(L)[1].real)
        return basis


def discrete_laplacian_eigenfunction(n, period1, period2):
    f = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            f[i][j] = np.exp(2j*np.pi*(i*period1/n + j*period2/n))
    return f/np.sqrt(np.sum(f*f))


if __name__ == '__main__':
    print('Eigenbasis obtained by generalising fourier series to two dimensions:')
    print(get_graph_laplacian_eigenbasis(2, flavour='fourier_series'))

    print('Eigenbasis computed by scipy:')
    print(get_graph_laplacian_eigenbasis(2, flavour='scipy'))

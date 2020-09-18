import numpy as np
from numpy import linalg as LA
from scipy.sparse import csgraph

from graph_laplacian.graph_laplacian_eigenbasis import get_graph_laplacian_eigenbasis
from graph_laplacian.plot_discrete_function import plot_discrete_function_multiple
from graph_laplacian.adjency_matrices import get_grid_adjaceny_matrix


def graph_convolve(f, g):
    assert f.shape == g.shape # input same size?
    assert f.shape[0] == f.shape[1] # square matrix?
    n = f.shape[0]
    G = get_grid_adjaceny_matrix(n)

    # 1
    # approach one with automatically computed eigenvectors
    # L = csgraph.laplacian(G, normed=False)
    #
    # eigen = LA.eig(L)
    #
    # eigenvalues = eigen[0].real
    #
    # print(np.transpose(eigen[1]))
    # eigenvectors = np.transpose(eigen[1]).real#[:n] # changes almost nothing when cutting off here
    # print('#### %s' % (eigenvalues))

    # 2
    # approach two with user defined eigenvectors
    eigenvectors = get_graph_laplacian_eigenbasis(n)

    proj = {}
    proj['f'] = []
    proj['g'] = []
    proj['f_conv_g'] = []

    f = np.reshape(f, -1)
    g = np.reshape(g, -1)


    for num, v in zip(range(len(eigenvectors)), eigenvectors):
        vec = np.reshape(v, -1)
        proj['f'] += [np.dot(vec, f)]
        proj['g'] += [np.dot(vec, g)]
        proj['f_conv_g'] += [np.dot(vec, f) * np.dot(vec, g)]
        # print(vec)
        # print(np.dot(vec, f) * np.dot(vec, g))

        # if np.abs(np.dot(v, f)) > 1:
        #     print('Plotting %s' % (num))
        #     print('%s * %s = %s' % (np.dot(v, f), np.dot(v, g), np.dot(v, f) * np.dot(v, g)))
        #     plot_discrete_function_multiple([np.reshape(f, (n,n)), np.reshape(g, (n,n)), np.reshape(v, (n,n))], rescale_minimum=0)

    # ev_reshape = [np.reshape(u, (n,n)) for u in eigenvectors[:8]]
    # plot_discrete_function_multiple(ev_reshape, rescale_minimum=0)


    f_conv_g = [p * vec for p, vec in zip(proj['f_conv_g'], eigenvectors)]
    f_conv_g = np.sum(f_conv_g, axis=0)
    f_conv_g = np.real(f_conv_g)
    f_conv_g = np.reshape(f_conv_g, (n, n))

    return f_conv_g




if __name__ == '__main__':
    f = lambda x, y: np.cos(2*np.pi*x)
    # g = lambda x, y: 1/2*np.cos(2*np.pi*x)+1/2*np.cos(2*2*np.pi*x)
    g = lambda x, y: 1+0*x

    resolution = 2
    n = resolution

    f_matrix = np.fromfunction(lambda i, j: f(j/n, i/n), (n, n))
    g_matrix = np.fromfunction(lambda i, j: g(j/n, i/n), (n, n))

    print((f_matrix, g_matrix))
    print('-')

    print(np.sum(np.abs(f_matrix-graph_convolve(f_matrix, g_matrix)))/(n**2))
    # 150: 0.64

    print(np.std(np.abs(f_matrix - graph_convolve(f_matrix, g_matrix)))) # should be 0
    print(np.mean(np.abs(f_matrix - graph_convolve(f_matrix, g_matrix)))) # should be 0

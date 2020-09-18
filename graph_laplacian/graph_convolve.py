import numpy as np

from graph_laplacian.graph_laplacian_eigenbasis import get_graph_laplacian_eigenbasis


def graph_convolve(f, g, flavour='fourier_series'):
    assert f.shape == g.shape # input same size?
    assert f.shape[0] == f.shape[1] # square matrix?
    n = f.shape[0]

    eigenvectors = get_graph_laplacian_eigenbasis(n, flavour)

    proj = {'f': [], 'g': [], 'f_conv_g': []}

    f = np.reshape(f, -1)
    g = np.reshape(g, -1)

    for num, v in zip(range(len(eigenvectors)), eigenvectors):
        vec = np.reshape(v, -1)
        proj['f'] += [np.dot(vec, f)]
        proj['g'] += [np.dot(vec, g)]
        proj['f_conv_g'] += [np.dot(vec, f) * np.dot(vec, g)]

    f_conv_g = [p * vec for p, vec in zip(proj['f_conv_g'], eigenvectors)]
    f_conv_g = np.sum(f_conv_g, axis=0)
    f_conv_g = np.real(f_conv_g)
    f_conv_g = np.reshape(f_conv_g, (n, n))

    return f_conv_g


if __name__ == '__main__':
    f = lambda x, y: x**2 + y**2
    g = lambda x, y: 1+0*x

    n = 2

    f_matrix = np.fromfunction(lambda i, j: f(j/n, i/n), (n, n))
    g_matrix = np.fromfunction(lambda i, j: g(j/n, i/n), (n, n))

    print('Matrix f: \n%s\n' % f_matrix)
    print('Matrix g: \n%s\n' % g_matrix)

    print('Graph convolution with a constant function is constant:')
    print(graph_convolve(f_matrix, g_matrix))

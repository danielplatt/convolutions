import numpy as np

def get_graph_laplacian_eigenbasis(n):
    basis = []
    for k in range(n):
        for l in range(n):
            basis += [discrete_laplacian_eigenfunction(n, k, l)]
    return basis


def discrete_laplacian_eigenfunction(n, period1, period2):
    f = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            f[i][j] = np.exp(2j*np.pi*(i*period1/n + j*period2/n))
            # print(2j*np.pi*(i*period1/n + j*period2/n))
    # print('###### %s, %s' % (f, np.sum(f*f)))
    return f/np.sqrt(np.sum(f*f))

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csgraph
# from scipy.linalg import eig
from numpy import linalg as LA

from graph_laplacian.tests.verify_eigen_properties import verify_eigen_properties

from graph_laplacian.adjency_matrices import get_grid_adjaceny_matrix

GRIDSIZE = 8
n = GRIDSIZE

MAX_PLOT_ROW_LENGTH = 8
plot_row_length = 8

G = get_grid_adjaceny_matrix(n)
# print(G)

L = csgraph.laplacian(G, normed=False)

# computes weird stuff
# eigen = eig(L)
eigen = LA.eigh(L)

eigenvalues = eigen[0]
eigenvectors = eigen[1]

print(eigenvalues)

max_entry = np.amax(eigenvectors)
min_entry = np.min(eigenvectors)

verify_eigen_properties(L, eigenvalues, eigenvectors)

plt.figure()

f, axarr = plt.subplots(2, plot_row_length)

for k in range(plot_row_length):
    axarr[0, k].imshow(np.reshape(eigenvectors[:, k], (n, n)), vmin=min_entry, vmax=max_entry)
    axarr[1, k].imshow(np.reshape(eigenvectors[:, n**2-plot_row_length+k], (n, n)), vmin=min_entry, vmax=max_entry)
    # for i in range(n):
    #     for j in range(n):
    #         axarr[0, k].text(i, j, str(np.round_(np.reshape(eigenvectors[:, k], (n, n))[i,j],1)), va='center', ha='center')
    #         axarr[1, k].text(i, j, str(np.round_(np.reshape(eigenvectors[:, n**2-plot_row_length+k], (n, n))[i,j],1)), va='center', ha='center')

plt.savefig('discrete_eigenfunctions.png', dpi=1000)
plt.show()

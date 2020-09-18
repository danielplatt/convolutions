import numpy as np

def verify_eigen_properties(mat, eval, evec):
    for num in range(len(eval)):
        eigenval = eval[num]
        eigenvec = evec[:, num]
        assert np.array_equal(np.round_(np.dot(mat, eigenvec) - eigenval * eigenvec, 1), np.zeros(eigenvec.shape))

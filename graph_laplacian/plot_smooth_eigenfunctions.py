import numpy as np

GRIDSIZE = 16
n = GRIDSIZE

BASIS_ELEMENT_NUMBER = n * n

def get_sin_eigenfunction(x_period, y_period):
    f = lambda x,y: np.sin(2 * np.pi * (x_period * x + y_period * y))
    return f

def get_cos_eigenfunction(x_period, y_period):
    f = lambda x,y: np.cos(2 * np.pi * (x_period * x + y_period * y))
    return f

eigenvalues = [np.around(0.5 * k) for k in range(BASIS_ELEMENT_NUMBER)]
eigenvectors = []
for k in eigenvalues:
    new_sin_func = np.empty((n, n))
    new_cos_func = np.empty((n, n))
    for row in range(n):
        for col in range(n):
            new_sin_func[row, col] =






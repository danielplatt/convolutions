import numpy as np

def get_grid_adjaceny_matrix(n):
    mat = np.zeros((n*n,n*n))
    for row in range(n):
        for col in range(n):
            vertex_index = n*row + col

            neighbour_index = {}

            neighbour_index['right'] = n * row + (col + 1) % n
            neighbour_index['left'] = n * row + (col - 1) % n
            neighbour_index['up'] = n * ((row - 1) % n) + col
            neighbour_index['down'] = n * ((row + 1) % n) + col

            for dir in neighbour_index:
                mat[vertex_index, neighbour_index[dir]] = 1
                mat[neighbour_index[dir], vertex_index] = 1
    return mat

if __name__ == '__main__':
    print(get_grid_adjaceny_matrix(4))

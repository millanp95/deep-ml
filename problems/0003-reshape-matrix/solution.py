import numpy as np

def reshape_matrix(a, new_shape):
    n, m = len(a), len(a[0])
    size = n*m
    n2, m2 = new_shape
    if n * m != n2 * m2:
        return []
    else:  
        reshaped_matrix = [[0] * m2 for _ in range(n2)]
        for k in range(size):
            #print(f"k={k}, {k//n2, k % m2}), ({k //n}, {k % m}))")
            reshaped_matrix[k // m2][k % m2] = a[k // m][k % m]
        return reshaped_matrix
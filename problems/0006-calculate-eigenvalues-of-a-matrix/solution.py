import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	x = np.array(matrix)
    values, vectors = np.linalg.eig(x)
    return values.round(4).tolist()
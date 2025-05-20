import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	x = np.array(matrix)
    if mode == 'row':
        return np.mean(x, axis=1).tolist()
    else:
        return np.mean(x, axis=0).tolist()
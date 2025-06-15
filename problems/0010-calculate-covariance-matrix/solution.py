import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    m = len(vectors[0])
    X = np.array(vectors).T
    X = X - X.mean(axis=0)
    cov = (X.T @ X)/(m-1)

	return cov.tolist()
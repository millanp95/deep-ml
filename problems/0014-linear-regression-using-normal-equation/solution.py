import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	
	theta = np.linalg.solve(X.T @ X, X.T @ np.array(y).reshape(-1,1))
	return np.round(theta, 4).flatten().tolist()
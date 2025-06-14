import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))
    y = np.reshape(y, (m,1))
    for _ in range(iterations):
        theta -= alpha * X.T @ (X @ theta - y) / m
    theta = np.round(theta, decimals=4)
	return theta
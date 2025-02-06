import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	X = data
	standardized_data = 1/np.std(X, axis=0)*(X-np.mean(X, axis=0))
	normalized_data = (X-np.min(X, axis=0))/(np.max(X, axis=0)-np.min(X, axis=0))
	return standardized_data, normalized_data
import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	mean = np.mean(data, axis=0)
	std = np.std(data, axis=0)
	standardized_data = (data - mean) / std

	_min = np.min(data, axis=0)
	_max = np.max(data, axis=0)
	normalized_data = (data - _min) / (_max - _min)
	return standardized_data, normalized_data
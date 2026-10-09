import numpy as np

def to_categorical(x, n_col=None):
	if not n_col:
		n_col = max(x) + 1
	one_hot = np.zeros((x.shape[0], n_col))
	for i in range(x.shape[0]):
		one_hot[i, x[i]] = 1 
	return one_hot
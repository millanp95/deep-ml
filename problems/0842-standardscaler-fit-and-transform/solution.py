import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    u = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    s = np.array([s if s != 0 else 1 for s in std]) 
    return (X_test - u) / s

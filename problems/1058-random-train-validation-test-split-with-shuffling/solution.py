import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n = data.shape[0]
    idx = np.random.default_rng(seed).permutation(n)

    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)
    return [data[idx[:train_end],:], data[idx[train_end:validation_end],:], data[idx[validation_end:],:]] 
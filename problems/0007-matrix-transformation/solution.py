import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

    if np.linalg.det(A) != 0 and np.linalg.det(S) != 0: 
        return (np.linalg.inv(T) @ A @ S).tolist()
    else:
        #print("One of the matrices is not invertible")
        return -1 
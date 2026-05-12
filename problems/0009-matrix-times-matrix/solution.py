import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    a = np.array(a)
    b = np.array(b)
    a_n, a_m = a.shape
    b_n, b_m = b.shape
    if a_m != b_n: 
        return -1
    else:
	    return a @ b  
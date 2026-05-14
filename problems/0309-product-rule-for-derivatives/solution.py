import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    n = len(f_coeffs) + len(g_coeffs) - 1 
    p = [0] * n 
    for i, x in enumerate(f_coeffs):
        for j, y in enumerate(g_coeffs):
            p[i+j] += x * y
    dp = [float(c*i) for i,c in enumerate(p)][1:]
    if dp: 
        return dp
    else:
        return 0.0
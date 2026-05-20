import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    
    def eval(l, x):
        return sum([c*(x**i) for i, c in enumerate(l)])

    h = h_coeffs[::-1]
    g = g_coeffs[::-1]
    
    h_prime = [c*(i+1) for i, c in enumerate(h[1:])]
    g_prime = [c*(i+1) for i, c in enumerate(g[1:])]

    return (eval(g_prime, x)*eval(h,x) - eval(h_prime, x)*eval(g,x)) / eval(h,x)**2
    
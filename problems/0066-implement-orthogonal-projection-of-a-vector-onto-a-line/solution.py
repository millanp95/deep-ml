
def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    norm = sum([l**2 for l in L])**0.5
    unit = [l/norm for l in L]
    dot = sum([x*l for x,l in zip(v, L)])
    return [dot/norm*u for u in unit]
    

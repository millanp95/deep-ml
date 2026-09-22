from collections import Counter
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    c = Counter(samples)
    N = len(samples)
    p = sorted([(x, c/N) for x, c in c.items()], key=lambda x: x[0])

    return p   
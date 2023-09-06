import random

def ranged_list(a, b, n):
    """
    a - minimum value(inclusive)
    b - maximum value(inclusive)
    n - number of elements

    returns list of int type values <a, b> containing n elements
    """
    return [random.randint(a, b) for _ in range(n)]
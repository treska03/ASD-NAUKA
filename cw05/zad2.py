
def subset_sum(T, x):
    """
    T - list of values
    x - value in seek

    returns boolean (True if n values in a row in T sum up to x)
    """
    n = len(T)
    summ = 0
    i = j = 0
    while summ != x:
        while summ < x:
            if j == n:
                return False
            j +=1
            summ += T[j]
        while summ > x:
            summ -= T[i]
            i +=1
    return True
    
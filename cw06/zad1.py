
def black_forest(T):
    """
    Looking for maximum profit from choping trees.
    We cannot chop two trees in a row.

    Args:
    T - list of profit from trees

    Return:
    returns the maximum profit that fits conditions
    """
    n = len(T)

    DP = [0 for _ in range(n+1)]
    
    for i in range(1, n+1):
        DP[i] = max(DP[i-2] + T[i-1], DP[i-1])
    return DP[-1]


dummy_data = [10, 20, 30, 40, 50, 10, 20, 30]
my = black_forest(dummy_data)
print(my)
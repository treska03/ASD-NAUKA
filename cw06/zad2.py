def top(a1, b1, a2, b2):
    return a2 <= a1 and b1 <= b2

def tetris(T):
    """
    T - list of tuples <a, b> that represent blocks

    return minimum number of blocks to be removed
    """
    n = len(T)
    DP = [1 for _ in range(n)]

    for i in range(n):
        a, b = T[i]
        for j in range(i):
            x, y = T[j]
            if top(a,b,x,y):
                DP[i] = max(DP[i], DP[j] + 1)

    print(DP)    
    return n - max(DP)

dummy_data = [
    [1, 20],
    [2, 19],
    [3, 18],
    [2, 22],
    [1, 15],
    [4, 17]
]
my = tetris(dummy_data)
print(my)
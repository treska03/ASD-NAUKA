from tests import ranged_list

def chess_walk(A):
    n = len(A)
    DP = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]
    DP[1][1] = 0
    for row in range(1, n+1):
        for col in range(1, n+1):
            if row == col == 1:
                continue
            DP[row][col] = min(DP[row-1][col], DP[row][col-1]) + A[row-1][col-1]
    return DP[-1][-1]

T1 = [ranged_list(1, 10, 10) for _ in range(10)]
my = chess_walk(T1)
print(my)
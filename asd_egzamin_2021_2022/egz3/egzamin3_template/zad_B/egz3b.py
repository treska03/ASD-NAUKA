from egz3btesty import runtests

def maze( L ):
    n = len(L)
    up = [float("-inf") for _ in range(n+1)]
    down = [float("-inf") for _ in range(n+1)]
    total = [float("-inf") for _ in range(n)]

    for i in range(n):
        if L[i][0] == "#":
            break
        total[i] = i
    for col in range(1, n):
        ### going down
        for row in range(1, n+1):
            if L[row-1][col] == "#":
                down[row] = float("-inf")
            else:
                down[row] = max(down[row-1], total[row-1]) + 1
        ### going up
        for row in range(n-1, -1, -1):
            if L[row][col] == "#":
                up[row] = float("-inf")
            else:
                up[row] = max(up[row+1], total[row]) + 1
        ### getting total
        for row in range(n):
            total[row] = max(down[row+1], up[row])
            
    return total[-1] if total[-1] != float("-inf") else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )

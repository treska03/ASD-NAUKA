from egz2btesty import runtests

def magic( C ):
    n = len(C)
    DP = [float("-inf") for _ in range(n+1)]
    DP[0] = 0
    for i in range(n):
        curr = C[i]
        chest = curr[0]
        for cost, dest in curr[1:]:
            if chest - cost <= 10 and DP[i] + chest >= cost:
                DP[dest] = max(DP[dest], DP[i] + min(chest - cost, 10))
    
    return DP[-2] if DP[-2] != float('-inf') else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )

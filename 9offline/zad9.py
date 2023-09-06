from zad9testy import runtests

def min_cost( O, C, T, L ):

    D = list(zip(O, C))
    D.sort(key=lambda x: x[0])
    D.append((L, 0))
    n = len(D)
    DP = [[float("inf") for _ in range(n)] for _ in range(2)]
    def rek(i, still_available):
        if DP[still_available][i] != float("inf"):
            return DP[still_available][i]
        if D[i][0] < T:
            DP[0][i] = 0
            DP[1][i] = 0
            return 0
        if still_available and D[i][0] < 2*T:
            DP[i][1] = 0
            return 0
        
        minimum = DP[0][i]
        for j in range(i-1, -1, -1):
            if D[i][0] - D[j][0] > T:
                break
            minimum = min(rek(j, 0) + D[j][1], minimum)
        DP[0][i] = minimum

        minimum = DP[1][i]
        for j in range(i-1, -1, -1):
            if D[i][0] - D[j][0] > T*2:
                break
            if D[i][0] - D[j][0] <= T:
                minimum = min(rek(j, 1) + D[j][1], minimum)
            minimum = min(rek(j, 0) + D[j][1], minimum)
        DP[1][i] = minimum
        
        return DP[still_available][i]
    
    rek(n-1, 1)
    return min(DP[0][-1], DP[1][-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

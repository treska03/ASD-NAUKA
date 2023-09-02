from tests import ranged_list

def longest_common_subset(A, B):
    n = len(A)
    DP = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if j == 0 or i == 0:
                DP[i][j] = 0
            else:
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-1] + int(A[i-1] == B[j-1]), DP[i][j-1])

    return DP[-1][-1]

def lcs(X, Y, m, n):
 
    # Declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

i = 0 
while i < 100:
    T1 = ranged_list(0, 15, 100)
    T2 = ranged_list(0, 15, 100)
    if (longest_common_subset(T1, T2)) != (lcs(T1, T2, 100, 100)):
        print("Nie działa")
    i+=1


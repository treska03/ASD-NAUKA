
def wymiana(K):
    n = len(K)
    #We select our 'z' candidate
    for z in range(n):
        DP = [K[z][i] for i in range(n)]
        

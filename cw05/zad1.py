from tests import ranged_list

def knapsack(P, W, C):
    """
    P - LIST OF PRICES OF ITEMS 
    W - LIST OF WEIGHTS OF ITEMS
    C - WEIGHT CAP OF OUR BACKPACK
    """
    n = len(P)
    DP = [0 for _ in range(C+1)]
    for i in range(n):
        price, weight = P[i], W[i]
        for j in range(C-weight+1):
            DP[j] = max(DP[j], DP[j+weight] + price)
    return max(DP)

def working_algo(val, wt, W):
    n = len(val)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
  
    return K[n][W]



val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

values = ranged_list(1, 1000000, 200000)
weights = ranged_list(1, 25000, 200000)
cap = 1500000
print(knapsack(val, wt, W), working_algo(val, wt, W))
print(knapsack(values, weights, W))
print(working_algo(values, weights, W))
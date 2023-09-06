from tests import ranged_list

def frog(T):
    n = len(T)
    DP = [[float("inf") for _ in range(n+1)] for _ in range(n)]
    DP[0][0] = 0
    for i in range(n): ## starting square
        for j in range(n+1): ## how_much_food
            if DP[i][j] != float("inf"):
                curr_food = T[i] + j
                if curr_food >= n-i:
                    DP[-1][0] = min(DP[-1][0], DP[i][j] + 1)
                else:
                    for k in range(i+1, curr_food + i + 1): ## position of landing
                        food_after = curr_food - (k - i)
                        DP[k][food_after] = min(DP[k][food_after], DP[i][j] + 1)
    return min(DP[-1])



T = ranged_list(1, 40, 1000)
print(frog(T))
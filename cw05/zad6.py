from tests import ranged_list

def coins(T, x):
    DP = [float("inf") for _ in range(x+1)]
    DP[x] = 0
    for k in range(x-1, -1, -1):
        DP[k] = min(DP[j+k] if j+k <= x else float("inf") for j in T) + 1
    return DP[0]

def test(coins, amount):
    if amount == 0 :
        return 0
    if min(coins) > amount:
        return -1
    dp = [-1 for i in range(0, amount + 1)]
    for i in coins:
        if i > len(dp) - 1:
            continue
        dp[i] = 1
        for j in range(i + 1, amount + 1):
            if dp[j - i] == -1:
                continue
            elif dp[j] == -1:
                dp[j] = dp[j - i] + 1
            else:
                dp[j] = min(dp[j], dp[j - i] + 1)
    return dp[amount]

T1 = ranged_list(1, 1000, 13)
target = 792
my = coins(T1, target)
custom = test(T1, target)
print(my, custom, my == custom)
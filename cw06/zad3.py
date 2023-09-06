from tests import ranged_list

def prom(T, L):
    DP = [[0 for _ in range(L+1)] for _ in range(L+1)]
    for U in range(L+1):
        for D in range(L+1):
            
            c = DP[U][D]
            if T[c] + D < L+1:
                DP[U][D+T[c]] = max(DP[U][D+T[c]], c+1)
            if T[c] + U < L+1:
                DP[U+T[c]][D] = max(DP[U+T[c]][D], c+1)
    
    return max(max(row) for row in DP)

def prom_2_way(T, r):
  ### Rozwiązanie konrada 
  dp = [False for _ in range(r+1)]
  dp[0] = True
  
  max_dp = 0
  whl_len = 0
  
  i = 0
  while r + max_dp >= whl_len  and  i < len(T):
    if T[i] > r:
      return "ERROR"
    
    for j in range(r+1):
      
      new_j = j + T[i]
      if dp[j]  and  new_j <= r:
        dp[new_j] = True
        max_dp = max(max_dp, new_j)
        
    whl_len += T[i]
    i+=1
    
  return i - (r + max_dp < whl_len)

def prom3way(T, DP, i, n, l, r):
    if(i == n):
        return n
    if(DP[l][r] != -1):
        return DP[l][r]
    a, b = 0, 0
    if(T[i] > l and T[i] > r):
        DP[l][r] = i+1
        return i+1
    if(T[i] <= l):
        a = prom3way(T, DP, i+1, n, l - T[i], r)
    if(T[i] <= r):
        b = prom3way(T, DP, i+1, n, l, r - T[i])
    DP[l][r] = max(a, b)
    return DP[l][r]

i = 0
while i < 100:
    DP = [[-1 for _ in range(2500+1)] for _ in range(2500+1)]
    cars = ranged_list(1, 200, 1000)
    print("MY START")
    my = prom(cars, 2500)
    print("MY FINISH")
    print("CUSTOM START")
    custom = prom3way(cars, DP, 0, len(cars), 2500, 2500)
    print(my, custom)
    print("CUSTOM FINISH")
    if my != custom:
       print("inaczej niz kuba", i)
    if my != prom_2_way(cars, 2500):
       print("Inaczej niż konrad")
    i+=1
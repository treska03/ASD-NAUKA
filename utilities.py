from bisect import bisect_right
from cw05.tests import ranged_list
import random

def binselect(T, x):
    lo = 0
    hi = len(T)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < T[mid]:
            hi = mid
        else:
            lo = mid + 1
    
    return lo

a, b, n = 1, 1000000000, 50000
T = ranged_list(a, b, n)
x = T[random.randint(0, n-1)]


my = binselect(T, x)
custom = bisect_right(T, x)
print(my, custom, my==custom)


sortet = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(binselect(sortet, 4))
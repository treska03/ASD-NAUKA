from tests import ranged_list
import bisect

def longest_increasing_subset_1(T):
    n = len(T)
    DP = [1 for _ in  range(n)]
    maksimum = 0
    for i in range(1, n):
        DP[i] = max(DP[k] if T[k] < T[i] else 0 for k in range(i)) + 1
        maksimum = max(DP[i], maksimum)

    return maksimum

 
def test(arr):
    n = len(arr)
    lis = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
    return max(lis)


T1 = ranged_list(0, 10000, 2500)
print("Inicialized")
my = longest_increasing_subset_1(T1)
custom = test(T1)
print(my, custom, my == custom)


def longest_growing_subset_2(T):
    n = len(T)
    results = [T[0]]
    for i in range(1, n):
        if T[i] > results[-1]:
            results.append(T[i])
        else:
            j = bisect.bisect_left(results, T[i])
            results[j] = T[i]
    return len(results)

T1 = ranged_list(0, 100000, 1000)
print("Inicialized")
my = longest_growing_subset_2(T1)
custom = test(T1)
print(my, custom, my == custom)
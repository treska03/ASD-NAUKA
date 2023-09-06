from zad3testy import runtests


def lamps( n, L ):

    T = [-1 for _ in range(n)]

    max_nieb = 0
    curr_nieb = 0

    for a, b in L:

        for i in range(a, b+1):
            if T[i] == -1:
                T[i] = 0
            elif T[i] == 0:
                curr_nieb += 1
                T[i] = 1
            else:
                curr_nieb -= 1
                T[i] = -1
        if curr_nieb > max_nieb:
            max_nieb = curr_nieb
    
    return max_nieb

    
runtests( lamps )



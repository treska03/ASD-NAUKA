from zad2testy import runtests

def opt_sum(tab):
    tab.sort()
    suma = 0
    i = len(tab)//2
    j = len(tab)%2
    k = 0
    maxx = 0
    while i-k > 0:
        suma+= tab[i-k-1]
        maxx = max(maxx, abs(suma))
        suma+= tab[i+k]
        maxx = max(maxx, abs(suma))
        k+=1

    return maxx



runtests( opt_sum )

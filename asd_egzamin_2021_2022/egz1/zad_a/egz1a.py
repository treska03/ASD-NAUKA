from egz1atesty import runtests

def snow( S ):
    S.sort(reverse=True)
    suma = 0
    i = 0
    while S[i] - i > 0:
        suma += (S[i] - i)
        i+=1

    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

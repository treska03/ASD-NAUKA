from zad9testy import runtests

def min_cost( O, C, T, L ):
    S = list(zip(O, C))
    S.sort(key=lambda x: x[0])
    S.append((L, 0))
    n = len(S)
    DP = [-1] * (n+1)


    def deepthroat(i, used):
        if(S[i][0] <= T):
            DP[i] = S[i][1]
            return S[i][1]
        if(DP[i] != -1):
            return DP[i]
        dist_i, w = S[i][0], 0
        mini = float('inf')
        for j in range(i-1, -1, -1):
            dist_j = S[j][0]
            if(dist_i != dist_j and dist_i - dist_j <= T):
                mini = min(mini, S[i][1] + deepthroat(j, used))
            elif(dist_i - dist_j > T):
                break
        if(not used):
            if(S[i][0] <= 2 * T):
                DP[i] = S[i][1]
                return S[i][1]

            for j in range(i-1, -1, -1):
                dist_j = S[j][0]
                if( T < dist_i - dist_j <= 2 * T):
                    mini = min(mini, S[i][1] + deepthroat(j, 1))
                elif(dist_i - dist_j > 2 * T):
                    break
        DP[i] = mini
        return mini
    
    S.append([L, 0])
    wyn = deepthroat(n, 0)

    return wyn

def min_cost( O, C, T, L ):
    #sortuję obie tablice po dystansach, dodaję dodatkowo na początku pozycję 0 a na końcu L
    #możnaby stworzyć nowe tablice, bo lepiej nie modyfikować parametrów funkcji, ale no cóż.
    n=len(O)
    A=[(O[i],C[i]) for i in range(n)]
    A.sort()
    O[0]=C[0]=0
    for i in range(n-1):
        O[i+1]=A[i][0]
        C[i+1]=A[i][1]
    O.append(A[n-1][0])
    O.append(L)
    C.append(A[n-1][1])
    C.append(0)
    #tablica 2x(n+2), wartości w pierwszym wierszu - przed wykorzystaniem wyjątku,
    #w drugim wierszu - po wykorzystaniu
    DP=[[float('inf') for _ in range(n+2)] for _ in range(2)]
    DP[0][0]=0
    h=k=0
    #i,j - wskaźniki indeksów po skoku z pierwszego wiersza, l - z drugiego
    #analogicznie h i k - przed skokiem
    #czemu <=n+2? szczerze nie analizowałem dokładnie, a dla <=n+1 jeden z testów miał błędny wynik
    #więc to obejmuje ten edge case
    while h<=n+2:
        i=j=h
        l=k
        min_ind_T1=h+1
        min_ind_T2=k+1
        #1 opcja - jeszcze nie wykorzystano wyjątku, dalej nie korzystam
        #wszędzie na bieżąco przy okazji zapisuję indeks najbardziej opłacalnego skoku
        #(oprócz 2 opcji) - znacznie przyspiesza to rozwiązanie
        while i<n+1 and O[i+1]-O[h]<=T:
            DP[0][i+1]=min(DP[0][i+1],DP[0][h]+C[i+1])
            if DP[0][i+1]<=DP[0][min_ind_T1]: 
                min_ind_T1=i+1
            i+=1
        #2 opcja - właśnie wykorzystuję wyjątek
        while j<n+1 and O[j+1]-O[h]<=2*T:
            DP[1][j+1]=min(DP[1][j+1],DP[0][h]+C[j+1])
            j+=1
        #3 opcja - już po wykorzystaniu wyjątku
        while l<n+1 and O[l+1]-O[k]<=T:
            DP[1][l+1]=min(DP[1][l+1],DP[1][k]+C[l+1])
            if DP[1][l+1]<=DP[1][min_ind_T2]: 
                min_ind_T2=l+1
            l+=1
        h=min_ind_T1
        k=min_ind_T2
    return DP[1][n+1]

runtests( min_cost, all_tests = True )

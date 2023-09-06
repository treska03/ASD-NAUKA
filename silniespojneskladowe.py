

def sss(G):
    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    times = [-1 for _ in range(n)]

    def DFS_visit(G, tab, u, flag):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)
        nonlocal time
        if flag:tab[time] = u
        else:tab.append(u)
        time +=1
    
    for u in range(n):
        if not visited[u]:
            DFS_visit(G, times, u, False)
    
    ### reverse edges:

    T = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            T[v].append(u)
    
    result = []
    for u in times[::-1]:
        result.append()
        DFS_visit(T, result[-1], u, True)
    
    return result
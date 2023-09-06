
def topologic(G):
    n = len(G)
    visited = [False for _ in range(n)]
    results = [-1 for _ in range(n)]
    idx = n - 1

    def DFS_visit(G, s):
        visited[s] = True
        for x in G[s]:
            if not visited[x]:
                DFS_visit(G, x)
        nonlocal idx
        results[idx] = s
        idx -= 1
    
    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)

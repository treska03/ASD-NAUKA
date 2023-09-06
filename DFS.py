
def DFS(G):
    n = len(G)
    time = 1
    visited = [False for _ in range(n)]
    times = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]

    def DFS_visit(G, s):
        nonlocal time
        times[s] = time
        visited[s] = True
        time +=1
        for edge in G[s]:
            if not visited[edge]:
                parent[edge] = s
                DFS_visit(edge)

    for vertex in range(n):
        if not visited[vertex]:
            DFS_visit(vertex)


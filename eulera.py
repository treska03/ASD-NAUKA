
def is_consistent(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(u):
        if not visited[u]:
            visited[u] = True
            for v in G[u]:
                DFS_visit(v)
    
    DFS_visit(0)
    return all(visited)

def has_eulers(G):
    return (is_consistent(G) and all(len(x) % 2 == 0 for x in G))

def get_eulers(G):
    if not has_eulers(G):
        return False
    
    n = len(G)
    result = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    def DFS_visit(G, u):
        if not visited[u]:
            for v in G[u]:
                if not visited[u][v]:
                    visited[u][v] = True
                    visited[v][u] = True
                    DFS_visit(v)
            result.append(u)
    
    DFS_visit(G, 0)
    
    return result
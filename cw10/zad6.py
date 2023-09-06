
def BFS(G, s):
    dist = 0
    max_dist = 0

    def BFS_visit(G, u, parent):
        nonlocal max_dist, dist
        for v, w in G[u]:
            if v != parent:
                dist += w
                if dist > max_dist:
                    max_dist = dist
                BFS_visit(G, v)
                dist -= w
    
    BFS_visit(G, s, s)
    return max_dist

def best_root(G):
    ### We assume G is a list of edges:
    V = len(G) + 1
    d = [0 for _ in range(V)]
    G = [[] for _ in range(V)]
    min_dist = float("inf")
    min_idx = 0
    for u, v, w in G:
        d[u] +=1
        d[v] +=1
        G[u].append((v, w))
        G[v].append((u, w))
    
    for start in range(V):
        curr = BFS(G, start)
        if min_dist > curr:
            min_dist = curr
    
    return min_idx
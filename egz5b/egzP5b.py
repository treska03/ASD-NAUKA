from egzP5btesty import runtests 

def detect_bridges(G):
    n = len(G)
    visited = [False for _ in range(n)]

def find_articulation_points(G):
    n = len(G)
    low    = [0 for _ in range(n)]
    times  = [0 for _ in range(n)]
    is_art = [False for _ in range(n)]
    time   = 0
    
    def dfs(root, u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time
        out_deg = 0
        
        for v in G[u]:
            if v != parent:
                if not times[v]:
                    if dfs(root, v, u) + u == root:
                        out_deg +=1
                    low[u] = min(low[u], low[v])
                    if times[u] <= low[v]:
                        is_art[u] = True
                else:
                    low[u] = min(low[u], times[v])
        
        return out_deg
                
    # Check all possible starting vertices as a graph doesn't have to be consistent
    for u in range(n):
        if not times[u]:
            is_art[u] = dfs(u, u, -1) > 1

    return [u for u in range(n) if is_art[u]]


def koleje ( B ):
    for i in range(len(B)):
        B[i] = min(B[i]), max(B[i])
    B.sort(key= lambda x: (x[0], x[1]))
    V = max(max(B[x][0] for x in range(len(B))), max(B[x][1] for x in range(len(B)))) + 1
    G = [[] for _ in range(V)]
    G[B[0][0]].append(B[0][1])
    G[B[0][1]].append(B[0][0])
    for i in range(1, len(B)):
        if B[i] != B[i-1]:
            u = B[i][0]
            v = B[i][1]
            G[u].append(v)
            G[v].append(u)

    return len(find_articulation_points(G))

runtests ( koleje, all_tests=True )
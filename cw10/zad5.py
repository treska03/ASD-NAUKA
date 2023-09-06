import math

def get_lst_of_edges(G):
    n = len(G)
    T = []
    for x in range(n):
        for y in range(x+1, len(G)):
            if G[x][y] != float("inf"):
                T.append((x, y, G[x][y]))
    return T

class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self

def find(x:Node):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x:Node, y:Node):
    x = find(x)
    y = find(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def connected(x, y):
    return find(x) == find(y)

def Kruskal(G, V, E, s):
    vertexes = [Node(i) for i in range(V)]
    result = []
    counter = 0
    idx = s
    while counter < V - 1 and idx < E:
        u, v, weight = G[idx]
        if not connected(vertexes[u], vertexes[v]):
            result.append(G[idx])
            union(vertexes[u], vertexes[v])
            counter +=1
        idx +=1 
    if idx < E:
        return -1
    if counter == V-1:
        return result

def autostrady(G):
    V = len(G)
    T = [[float("inf)") for _ in range(V)]]
    for i in range(V):
        for j in range(V):
            x = G[i]
            y = G[j]
            T[i][j] = T[j][i] = math.ceil(math.sqrt((x[0]-y[0])**2 + (x[1] - y[1])**2))
    
    lst = get_lst_of_edges(T)
    lst.sort(key=lambda x: x[2])
    E = len(lst)
    minimum = float("inf")
    for s in range(E-V+2):
        res = Kruskal(lst, V, E, s)
        minimum = min(minimum, (res[-1][2] - res[0][2]))

    return minimum
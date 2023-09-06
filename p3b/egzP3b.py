from egzP3btesty import runtests 
from queue import PriorityQueue

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0

def find(x : Node):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x : Node, y : Node):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank +=1

def connected(x : Node, y : Node):
    return find(x) == find(y)

def get_edge_list(G):
    T = []
    for i in range(len(G)):
        for j in G[i]:
            if j[0] > i:
                T.append((i, j[0], j[1]))
    return T

def reverse_edge_lst(T):
    e = []
    for edge in T:
        e.append((edge[0], edge[1], -edge[2]))
    return e

def Kruskal(G, T):
    T.sort(key=lambda x: x[2])
    E = len(T)
    V = len(G)
    vertexes = [Node(i) for i in range(V)]
    result = []
    counter = 0
    for edge in T:
        u, v, weight = edge
        if not connected(vertexes[u], vertexes[v]):
            union(vertexes[u], vertexes[v])
            result.append(edge)
            counter +=1
            if counter == V - 1:
                break

    return result

def lufthansa ( G ):
    n = len(G)
    T = [[] for _ in range(n)]
    edge_lst = get_edge_list(G)
    reversed_lst = reverse_edge_lst(edge_lst)

    summ = 0
    for i in range(n):
        for edge in G[i]:
            summ += edge[1]
            T[i].append((edge[0], -edge[1]))
    result = Kruskal(T, reversed_lst)

    j = 0
    while j < n-1:
        if reversed_lst[j][2] != result[j][2]:
            break
        j+=1
    
    return sum(edge[2] for edge in result) + int(summ/2) + reversed_lst[j][2]

runtests ( lufthansa, all_tests=True )
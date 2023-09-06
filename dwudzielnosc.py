from queue import Queue

def BFS(G, colors):
    n = len(G)
    visited = [False for _ in range(n)]
    my_queue = Queue()
    my_queue.put(0)
    while my_queue.not_empty():
        u = my_queue.get()
        if not visited[u]:
            for v in G[u]:
                if colors[v] == colors[u]:
                    return False
                colors[v] = -colors[u]
                my_queue.put(v)
            visited[u] = True
    
    return True



def is_bipart(G):
    n = len(G)
    colors = [0 for _ in range(n)]
    colors[0] = 1

    def DFS(G, u):
        for v in G[u]:
            if not colors[v]:
                colors[v] = -colors[u]
                return DFS(v)
            elif colors[v] == colors[u]:
                return False
        return True

    for u in range(n):
        if not colors[u]:
            if not BFS(G, colors, u): return False #Should work the same
            if not DFS(G, colors, u): return False #Should work the same
    
    return True
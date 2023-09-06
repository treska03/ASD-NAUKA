from zad1testy import runtests
from queue import PriorityQueue

def djikstra(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0 
    my_queue = PriorityQueue()
    my_queue.put((0, s))
    while my_queue.qsize() > 0:
        _, u = my_queue.get()
        if not visited[u]:
            for i in range(n):
                if G[u][i] and dist[u] + G[u][i] < dist[i]:
                    dist[i] = G[u][i] + dist[u]
                    my_queue.put((dist[i], i))
            visited[u] = True
    return dist[t] if visited[t] else None



def islands(G, A, B):
    return djikstra(G, A, B)
                

runtests( islands ) 

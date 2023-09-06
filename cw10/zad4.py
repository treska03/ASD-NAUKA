
def oazy_zajebane(G, V, O):
    """
    G - graph of connections between cities and oases
    V - number of cities
    O - number of oases
    """

    visited = [False for _ in range(V)]
    parent = [-1 for _ in range(V)]
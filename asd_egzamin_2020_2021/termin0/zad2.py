
class Node:
    def __init__(self) -> None:
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.X = None

def get_list(root, k, T):
    if root:
        root.X = [0 for _ in range(k+1)]
        T.append(root)
        get_list(root.left, k, T)
        get_list(root.right, k, T)

def get_n_max(root, n):
    if not root or n == 0:
        return 0
    if n == 1:
        root.X[n] = max(root.leftval, root.rightval)
        return root.X[n]
    if root.X[n] != 0:
        return root.X[n]
    
    root.X[n] = max(root.X[n], get_n_max(root.left, n-1) + root.leftval, get_n_max(root.right, n-1) + root.rightval)
    for i in range(1, n):
        root.X[n] = max(root.X[n], get_n_max(root.left, n-i-1) + root.leftval + get_n_max(root.right, i-1) + root.rightval)
    return root.X[n]

def valuableTree(root, k):
    T = []
    get_list(root, k, T)
    n = len(T)
    maximum = 0
    for i in range(n):
        maximum = max(get_n_max(T[i], k), maximum)
    return maximum

A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()

A.left = B
A.leftval = 1
A.right = E
A.rightval = 5

B.left = D
B.leftval = 6
B.right = C
B.rightval = 2

C.left = F
C.leftval = 8
C.right = G
C.rightval = 10

print(valuableTree(A, 3))
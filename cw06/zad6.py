
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.best = None

def calc_best(root : Node):
    if not root:
        return 0
    if not root.best :
        best_left = calc_best(root.left)
        best_right = calc_best(root.right)
        root.best = max(best_left+root.value, best_right+root.value, best_left+best_right+root.value)
    return root.best
    
def sciezka_w_drzewie(root):
    calc_best(root)
    
    return root.best

A = Node(5)
B = Node(-7)
C = Node(-10)
D = Node(8)
E = Node(2)
F = Node(1)
G = Node(3)
H = Node(-3)
I = Node(9)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
D.left = H
D.right = I

my = sciezka_w_drzewie(A)
print(my)
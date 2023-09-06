from zad2testy import runtests

class Node:
    def __init__(self) -> None:
        self.edges = []
        self.weights = []
        self.ids= []
        self.subweights = []
        self.suma = 0

def calc_subweights(root : Node, lst : list):
    lst.append(root)
    root.subweights = [(calc_subweights(root.edges[i], lst) + root.weights[i]) for i in range(len(root.edges))]
    root.suma = sum(root.subweights)
    return root.suma

def calc_difference(root : Node, total : int, x : int):
    for i in range(len(root.subweights)):
        subsum = root.edges[i].suma
        curr_diff = abs(total - root.weights[i] - 2*subsum)
        if curr_diff < x[0]:
            x = (curr_diff, root.ids[i])
        x = calc_difference(root.edges[i], total, x)
    return x


def balance(root : Node):
    T = []
    calc_subweights(root, T)
    total = sum(root.subweights)
    min_roznica = (total - root.weights[0], root.ids[0])
    min_roznica = calc_difference(root, total, min_roznica)
    return min_roznica[1]

runtests( balance )



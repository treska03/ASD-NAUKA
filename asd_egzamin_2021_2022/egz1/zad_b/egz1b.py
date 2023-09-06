from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.idx = None       # pole do wykorzystania przez studentow
    self.h = None

def inicialize_lists(root, lst, heights, i, h):
    if root:
      root.idx = i
      root.h = h
      lst.append(root)
      heights.append(h)
      i = inicialize_lists(root.left, lst, heights, i+1, h+1)
      i = inicialize_lists(root.right, lst, heights, i, h+1)
    return i

def make_graph(T, n):
    graph = [[] for _ in range(n)]
    for v in range(n):
        if T[v].left:
            graph[v].append(T[v].left.idx)
            graph[T[v].left.idx].append(T[v].idx)
        if T[v].right:
            graph[v].append(T[v].right.idx)
            graph[T[v].right.idx].append(T[v].idx)

def deepthroat_idk(root, h):
    if not root:
      return (0, 0)
    if root.h == h:
      return (int(root.left is not None) + int(root.right is not None), 1)
    l = deepthroat_idk(root.left, h)
    r = deepthroat_idk(root.right, h)
    if l[1] == 1 or r[1] == 1:
      return (l[0] + r[0], 1)
    else:
      return (1, 0)


def wideentall(root):
    T = []
    heights = []
    inicialize_lists(root, T, heights, 0, 0)
    n = len(T)
    maximum_height = max(heights)
    quantity_on_height = [0 for _ in range(maximum_height+1)]
    for v in range(n):
       quantity_on_height[heights[v]] +=1

    max_on_level = max(quantity_on_height)
    widest_level_idx = 0
    for idx in range(maximum_height, -1, -1):
       if quantity_on_height[idx] == max_on_level:
          widest_level_idx = idx
          break
    
    return deepthroat_idk(root, widest_level_idx)[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )
from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def wybory(T):
    
    def sumuj_wybory(wyb:Node):
      p = wyb.fundusze
      DP = [0 for _ in range(p+1)]
      while wyb:
        for money in range(p-wyb.koszt+1):
            DP[money] = max(DP[money], DP[money+wyb.koszt] + wyb.wyborcy)
        wyb = wyb.next
      return max(DP)

    return sum(sumuj_wybory(wyb) for wyb in T)

runtests(wybory, all_tests = True)
import networkx as nx
from random import random

def instance4():
    lst = []
    for _ in range(25):
        lst.append(nx.diamond_graph())
    
    L = nx.Graph()
    for i in lst:
        L = nx.disjoint_union(L,i)
    
    r = 0
    while(r <= 92):
        L.add_edge(r+3, r+4)
        r+=4
    L.add_edge(0,99)
    
    return L
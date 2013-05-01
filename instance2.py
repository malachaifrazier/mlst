from random import random
import networkx as nx
from random import random
def instance2():
    lst = []
    for i in range(11):
        lst.append(nx.star_graph(8))
    L = nx.Graph()
    for item in lst:
        L = nx.disjoint_union(L,item)

    L.add_node(99)
    L.add_edges_from([(0,99),(9,99),(18,99),(27,99),(36,99),(45,99),(54,99),(63,99),(72,99),(81,99),(90,99)])
    for i in range(1500):
        x = int(random()*100)
        y = int(random()*100)
        L.add_edge(x,y)
    return L
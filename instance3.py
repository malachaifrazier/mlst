import networkx as nx
from random import random

def instance3():
    lst = []
    count = 0
    size = []
    leaves = 0
    while(count < 100):
        x = int(random()*100)%10
        if(count + x + 1 > 100):
            break
        lst.append(nx.star_graph(x))
        count = count + x + 1
        
    r = 100 - 1 - count
    lst.append(nx.star_graph(r-1))
    L = nx.Graph()
    for item in lst:
        leaves += nx.number_of_nodes(item)-1
        size.append(nx.number_of_nodes(item))
        L = nx.disjoint_union(L,item)

    L.add_node(99)
          
    """
    L.add_node(99)
    L.add_edges_from([(0,99),(9,99),(18,99),(27,99),(36,99),(45,99),(54,99),(63,99),(72,99),(81,99),(90,99)])
    """
    for i in range(1500):
        x = int(random()*100)
        y = int(random()*100)
        L.add_edge(x,y)
        
    print("Number of nodes in each star: " + str(size))
    print("Total num of leaves: " + str(leaves))
    return L
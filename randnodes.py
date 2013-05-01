import networkx as nx
from random import random

def randomMap(G):
    """
    takes the nodes in graph G and scatter the labels over 0 to 1000
    """
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    H.add_edges_from(G.edges())
    for n in H.nodes():
        new = n + int(random()*1000)
        while(new in H.nodes()):
            new = n + int(random()*1000)
        H = nx.relabel_nodes(H,{n:new})
    return H
    
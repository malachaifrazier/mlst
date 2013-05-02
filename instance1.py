from random import random
import networkx as nx

def instance1():
    #make a star of 4 24-node stars
    A = nx.star_graph(24)
    B = nx.star_graph(24)
    C = nx.star_graph(24)
    D = nx.star_graph(23)
    T = nx.disjoint_union(A,B)
    T = nx.disjoint_union(T,C)
    T = nx.disjoint_union(T,D)
    T.add_node(99)
    T.add_edges_from([(0,99),(25,99),(50,99),(75,99)])
    
    #randomize the labels of nodes    

    for n in T.nodes():
        new = n + int(random()*10000)
        while(new in T.nodes()):
            new = n + int(random()*10000)
        T = nx.relabel_nodes(T,{n:new})

    # T is optimal solution
    # G is the graph

    G = nx.Graph()
    G.add_nodes_from(T.nodes())
    G.add_edges_from(T.edges())

    # add random edges
    for i in range(1000):
        x = int(random()*15897)%100
        y = int(random()*17691)%100
        G.add_edge(G.nodes()[x],G.nodes()[y])

    return (G,T)
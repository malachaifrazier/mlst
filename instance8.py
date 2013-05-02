import networkx as nx
from random import random
import Mlst

def instance8_1000():
    """
    Returns a 3-element tuple (G,T,leaves) where G is the graph
    T is the optimal solution and leaves is the number of leaves
    in the optimal solution.
    
    The graph is constructed by creating 4 stars with 90 nodes and
    adding 10 random nodes.
    """
    
    #create a star of 4 stars
    starList = []
    
    for _ in range(0,6):
        starList.append(nx.heawood_graph())
    
    T = nx.Graph()
    for star in starList:
        T = nx.disjoint_union(T,star)
        
    T.add_node(84)
    T.add_edges_from([(84,0),(84,14),(84,28),(84,42),(84,56),(84,70)])
    
    #add 10 more nodes with random edges
    T.add_nodes_from(range(85,101))
    for i in range(85,101):
        x = int(random()*5371)%90
        T.add_edge(i,x)
        
    #count the number of leaves
    leaves = list(T.degree(T.nodes()).values()).count(1)
    
    #randomize the label of nodes
    for n in T.nodes():
        new = n + int(random()*2000)
        while(new in T.nodes()):
            new = n + int(random()*2000)
        T = nx.relabel_nodes(T,{n:new})
        
    G = nx.Graph()
    G.add_nodes_from(T.nodes())
    G.add_edges_from(T.edges())

    # add random edges
    for i in range(1000):
        x = int(random()*15897)%100
        y = int(random()*17691)%100
        G.add_edge(G.nodes()[x],G.nodes()[y])
    
    T = one_edge_swap(G)    
    return (G,T)
    
def instance8_2000():
    """
    Returns a 3-element tuple (G,T,leaves) where G is the graph
    T is the optimal solution and leaves is the number of leaves
    in the optimal solution.
    
    The graph is constructed by creating 4 stars with 90 nodes and
    adding 10 random nodes.
    """
    
    #create a star of 4 stars
    starList = []
    
    for _ in range(0,6):
        starList.append(nx.heawood_graph())
    
    T = nx.Graph()
    for star in starList:
        T = nx.disjoint_union(T,star)
        
    T.add_node(84)
    T.add_edges_from([(84,0),(84,14),(84,28),(84,42),(84,56),(84,70)])
    
    #add 10 more nodes with random edges
    T.add_nodes_from(range(85,101))
    for i in range(85,101):
        x = int(random()*5371)%90
        T.add_edge(i,x)
        
    #count the number of leaves
    leaves = list(T.degree(T.nodes()).values()).count(1)
    
    #randomize the label of nodes
    for n in T.nodes():
        new = n + int(random()*2000)
        while(new in T.nodes()):
            new = n + int(random()*2000)
        T = nx.relabel_nodes(T,{n:new})
        
    G = nx.Graph()
    G.add_nodes_from(T.nodes())
    G.add_edges_from(T.edges())

    # add random edges
    while(G.number_of_edges() < 2000):
        x = int(random()*15897)%100
        y = int(random()*17691)%100
        
        G.add_edge(G.nodes()[x],G.nodes()[y])
    T = one_edge_swap(G)
        
    return (G,T)
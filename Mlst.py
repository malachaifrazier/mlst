# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import networkx as nx
import itertools as it

# <codecell>

def setEdgeWeights(G):
    """
    Input: Unweighted networkx undirected graph G
    Output: Weighted networkx undirected graph where weight of edge is max degree of its endpoint vertexes
    """
    for e in G.edges():
        src_deg = G.degree(e[0])
        trg_deg = G.degree(e[1])
        G.edge[e[0]][e[1]]['weight'] = max([src_deg,trg_deg])

# <codecell>

def unityEdgeWeights(G):
    """
    Input: Unweighted networkx undirected graph G
    Output: Weighted networkx undirected graph where weight of edge is one
    """
    for e in G.edges():
        G.edge[e[0]][e[1]]['weight'] = 1

# <codecell>

def degBasedMST(G):
    """
    Input: Unweighted or Weighted networkx undirected graph G (Caution weights will be overwritten)
    Output: MST of G where weight of edge is max degree of its endpoint vertexes
    """
    setEdgeWeights(G)
    T = nx.algorithms.mst.minimum_spanning_tree(G)
    return T

# <codecell>

def unityMST(G):
    """
    Input: Unweighted or Weighted networkx undirected graph G (Caution weights will be overwritten)
    Output: MST of G where all edge weights are one
    """
    T = nx.algorithms.mst.minimum_spanning_tree(G)
    return T

def one_edge_swap(G):
    """ 
    Input: Spanning tree T and original graph G 
    Output: Generate a T one edge swap output
    """
   
    T1 = degBasedMST(G);
    T2 = unityMST(G);

    print "Degree Based MST: " + str(list(T1.degree(T1.nodes()).values()).count(1)) + " Leaves"
    print "Unity MST: " + str(list(T2.degree(T2.nodes()).values()).count(1)) +  " Leaves"

    if list(T1.degree(T1.nodes()).values()).count(1) > list(T2.degree(T2.nodes()).values()).count(1):
        T = T1.copy()
    else: 
        T = T2.copy()

    for e in list(set(G.edges()).difference(set(T.edges()))):
        U = T.copy()
        
        path = nx.shortest_path(T, e[0], e[1])

        for f in zip(path[0:],path[1:]):
            Degrees = list(T.degree(T.nodes()).values())
            
            U.add_edge(e[0],e[1])
            U.remove_edge(f[0],f[1])

            newDegrees = list(U.degree(U.nodes()).values()) 

            if newDegrees.count(1) > Degrees.count(1): 
                T = U.copy()

            U.add_edge(f[0],f[1]);

    print "One Edge Swap: " + str(list(T.degree(T.nodes()).values()).count(1)) + " Leaves"

    return T

def two_edge_swap(G):
    """ 
    Input: Spanning tree T and original graph G 
    Output: Generate a T one edge swap output
    """

    T = degBasedMST(G);

    M = count_iterable(it.combinations(list(set(G.edges()).difference(set(T.edges()))),2))
    print M

    i = 1
    for e1,e2 in it.combinations(list(set(G.edges()).difference(set(T.edges()))),2):
        i += 1

        U = T.copy()
        Degrees = list(T.degree(T.nodes()).values())
        
        path1 = nx.shortest_path(T, e1[0], e1[1])

        for f1 in zip(path1[0:],path1[1:]):
            
            U.add_edge(e1[0],e1[1])
            U.remove_edge(f1[0],f1[1])

            path2 = nx.shortest_path(T, e2[0], e2[1])

            for f2 in zip(path2[0:],path2[1:]):
                    
                U.add_edge(e2[0],e2[1])
                
                if (tuple([f2[0],f2[1]]) in U.edges()):
                    U.remove_edge(f2[0],f2[1])
                
                newDegrees = list(U.degree(U.nodes()).values()) 

                if newDegrees.count(1) > Degrees.count(1):
                    print newDegrees.count(1)
                    print i
                    T = U.copy()
                    Degrees = list(T.degree(T.nodes()).values())

                U.add_edge(f2[0],f2[1]);

            U.add_edge(f1[0],f1[1]);

    return T

def leaves(T):
    return list(T.degree(T.nodes()).values()).count(1)

def count_iterable(i):
    return sum(1 for e in i)


# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import networkx as nx
import itertools as it
import instance1 as in1
import instance7 as in7
import instance8 as in8

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

    # print "Degree Based MST: " + str(list(T1.degree(T1.nodes()).values()).count(1)) + " Leaves"
    # print "Unity MST: " + str(list(T2.degree(T2.nodes()).values()).count(1)) +  " Leaves"

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

    # print "One Edge Swap: " + str(list(T.degree(T.nodes()).values()).count(1)) + " Leaves"

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

def get_three_hardest_instances(k):
	"""
	Runs instance1() k times to generate k networkx graphs
	Returns a tuple of two lists, one containing the 3 "hardest" graph instances
	aka the graphs in which unityMST does the worst and the other
	containing the optimal MLST for those graphs
	"""
	G1_tup = in1.instance1_1000()
	G2_tup = in1.instance1_2000()
	G3_tup = in8.instance8_1000()
	T1 = unityMST(G1_tup[0])
	T2 = unityMST(G2_tup[0])
	T3 = unityMST(G3_tup[0])
	C1 = tuple([G1_tup,leaves(G1_tup[1])-leaves(T1)])
	C2 = tuple([G2_tup,leaves(G2_tup[1])-leaves(T2)])
	C3 = tuple([G3_tup,leaves(G3_tup[1])-leaves(T3)])
	hard_lst = [C1,C2,C3]
	for i in range(k):
		
		curr_graph_tup1 = in1.instance1_1000()
		unity_tree1 = unityMST(curr_graph_tup1[0])
		C4 = tuple([curr_graph_tup1,leaves(curr_graph_tup1[1])-leaves(unity_tree1)])
		
		curr_graph_tup2 = in1.instance1_2000()
		unity_tree2 = unityMST(curr_graph_tup2[0])
		C5 = tuple([curr_graph_tup2,leaves(curr_graph_tup2[1])-leaves(unity_tree2)])
		
		curr_graph_tup3 = in8.instance8_1000()
		unity_tree3 = unityMST(curr_graph_tup3[0])
		C6 = tuple([curr_graph_tup3,leaves(curr_graph_tup3[1])-leaves(unity_tree3)])
		
		
		if C4[1] > C1[1]:
			C1 = C4
			
		if C5[1] > C2[1]:
			C2 = C5
			
		if C6[1] > C3[1]:
			C3 = C6
			
	hard_graphs = [hard_lst[0][0][0],hard_lst[1][0][0],hard_lst[2][0][0]]
	opt_trees = [hard_lst[0][0][1],hard_lst[1][0][1],hard_lst[2][0][1]]
	return hard_graphs,opt_trees

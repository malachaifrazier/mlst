# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import networkx as nx
import UnionFind as uf
import MinimumSpanningTree as mst

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

def deg_based_MST(G):
    """
    Input: Unweighted or Weighted networkx undirected graph G (Caution weights will be overwritten)
    Output: MST of G where weight of edge is max degree of its endpoint vertexes
    """
    setEdgeWeights(G)
    return MinimumSpanningTree(G)

# <codecell>



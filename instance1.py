from random import random
import networkx as nx
A = nx.star_graph(24)
B = nx.star_graph(24)
C = nx.star_graph(24)
D = nx.star_graph(23)
E = nx.disjoint_union(A,B)
E = nx.disjoint_union(E,C)
E = nx.disjoint_union(E,D)
E.add_node(99)
E.add_edges_from([(0,99),(25,99),(50,99),(75,99)])
for i in range(1500):
    x = int(random()*100)
    y = int(random()*100)
    E.add_edge(x,y)

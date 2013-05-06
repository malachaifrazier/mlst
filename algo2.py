import networkx as nx
def algo(G):
    m = G.number_of_edges()
    n = G.number_of_nodes()
    F = nx.Graph()
    for v in G.nodes():
        if G.degree(v) >= 3:
            T = nx.Graph()
            T.add_edges_from(G.edges(v))
            for x in T.neighbors(v):
                count = 0
                p1 = []
                for w in G.neighbors(x):
                    if w not in T.nodes():
                        count += 1
                        y = w
                if count >= 2:
                    """fig 1(b) case"""
                    T.add_edges_from(G.edges(x))

                elif count == 1:
                    """fig 1(a) case"""
                    c = 0
                    l = []
                    for u in G.neighbors(y):
                        if u not in T.nodes():
                            c+=1
                            l.append(u)
                    """neighbors of y not in T >= 2"""
                    if c > 2:
                        """priority 2"""
                        T.add_edges_from(G.edges(y))
                        
                    elif c == 2:
                        """priority 1"""
                        print p1
                        print l
                        p1.append((l[0],l[1]))
                        print p1
                for item in p1:
                    if ((item[0] not in T) and (item[1] not in T)):
                        print item[0]
                        # T.add_edge(item[0])
                        T.add_edge(item[0], item[1])                   
        F.add_edges_from(T.edges())
        G.remove_nodes_from(T.nodes())
    #Connect the trees in F and all vertices not in F to form a spanning tree T.
    #I made this line work but seems like it's not quite efficient.
    S = nx.Graph(G)
    S.remove_edges_from(F.edges())
    for e in S.edges():
        if not nx.has_path(F,e[0],e[1]):
            F.add_edge(e[0],e[1])               
    return F
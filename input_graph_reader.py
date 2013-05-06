import networkx as nx


def get_nx_graphs(input_filename):
    fin = open(input_filename,'r')

    num_graphs = int(fin.readline())

    graph_list = []

    for i in range(num_graphs):
        num_edges = int(fin.readline())
        curr_graph = nx.Graph()
        for j in range(num_edges):
            edge_str = fin.readline()
            edge_nodes_str = edge_str.split(' ')
            edge_nodes = [int(x) for x in edge_nodes_str]
            curr_graph.add_edge(edge_nodes[0], edge_nodes[1])
        graph_list.append(curr_graph)
    return graph_list
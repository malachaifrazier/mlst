import input_graph_reader as igr
import Mlst as mlst
import sys
import out
import networkx as nx

in_file = sys.argv[1]

graph_list = igr.get_nx_graphs(in_file)


f1 = open('hard.all.v3.twoedge.out','w')
f2 = open('error_graphs.out','w')

f1.write(str(len(graph_list))+'\n')
for graph in graph_list:
    try:
        curr_mlst1 = mlst.one_edge_swap(graph)
        curr_mlst = mlst.two_edge_swap(curr_mlst1)
        edge_list = out.convert_edges(curr_mlst.edges())
        for edge_str in edge_list:
            f1.write(edge_str)
    except nx.NetworkXNoPath:
        error_edge_list = out.convert_edges(graph.edges())
        for error_edge_str in error_edge_list:
            f2.write(error_edge_str)
        curr_mlst = mlst.one_edge_swap(graph)
        edge_list = out.convert_edges(curr_mlst.edges())
        for edge_str in edge_list:
            f1.write(edge_str)
f1.close()
f2.close()
import input_graph_reader as igr
import Mlst as mlst
import sys
import out

in_file = sys.argv[1]

graph_list = igr.get_nx_graphs(in_file)

our_mlsts = [mlst.unityMST(graph) for graph in graph_list]

out_stuff = out.convert_graphs(our_mlsts)

f = open('hard.all.v3.unity.out', 'w')
for each in out_stuff:
	f.write(each)
f.close()
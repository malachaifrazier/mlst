import networkx as nx
import out
import sys
import Mlst as mlst
output = mlst.get_three_hardest_instances(int(sys.argv[1]))
hard_instance_graphs = output[0]
hard_instance_mlsts = output[1]
in_stuff = out.convert_graphs(hard_instance_graphs)
out_stuff = out.convert_graphs(hard_instance_mlsts)

f = open('hard.in', 'w')
for each in in_stuff:
	f.write(each)
f.close()

f = open('hard.out', 'w')
for each in out_stuff:
	f.write(each)
f.close()

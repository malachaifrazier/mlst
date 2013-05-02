import networkx as nx
import out
import sys
import Mlst as mlst
output = mlst.get_three_hardest_instances(int(sys.argv[1]))
hard_instance_graphs = output[0]
hard_instance_mlsts = output[1]

G1 = hard_instance_graphs[0]
G2 = hard_instance_graphs[1]
G3 = hard_instance_graphs[2]
T1 = mlst.unityMST(G1)
T2 = mlst.unityMST(G2)
T3 = mlst.unityMST(G3)

print str([mlst.leaves(T1),mlst.leaves(hard_instance_mlsts[0])])
print str([mlst.leaves(T2),mlst.leaves(hard_instance_mlsts[1])])
print str([mlst.leaves(T3),mlst.leaves(hard_instance_mlsts[2])])

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

import networkx as nx
import out
graphList = [] 
#stuff here to populate graphList
outlist = convert_graphs(graphList)

f = open('hard.out', 'w')
for each in outlist:
	f.write(each)
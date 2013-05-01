import networkx as nx
import itertools

def convert_edges(edgeList):
	filez2 = []
	filez2.append(str(len(edgeList)) + "\n")
	for edge in edgeList:
		filez2.append(str(edge[0]) + " " + str(edge[1]) +"\n")
	return filez2

def convert_graphs(graphList):
	filez = []
	filez.append(str(len(graphList)) + "\n")
	for graph in graphList:
		filez.add(convert_edges(graph.edges())
	return list(itertools.chain(*filez))
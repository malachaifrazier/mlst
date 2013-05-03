import networkx as nx

f = open('hard.in', 'r')

graphs = list(f)

original_graphs_copy = graphs[:] # saving just in case

num_graphs = int(graphs[0]) # check to make sure that final_graphs is this len
final_graphs = [] # array of graphs to go through with our MLST algorithm
g = -1 # which graph in final_graphs is having edges added to it

for n in range(1,len(graphs)-1):
	graphs[n] = graphs[n].split(' ')
	for x in range(0, len(graphs[n])):
		graphs[n][x] = int(graphs[n][x]) # after this, everything will be an int
	if len(graph[n]) == 1:
		final_graphs.append(nx.Graph())
		g += 1
	if len(graph[n]) == 2:
		final_graphs[g].add_edge(graph[n][0], graph[n][1])

f.close()

if len(final_graphs) != num_graphs:
	return "ERROR - GRAPH LIST DOES NOT CONTAIN CORRECT AMOUNT OF GRAPHS"
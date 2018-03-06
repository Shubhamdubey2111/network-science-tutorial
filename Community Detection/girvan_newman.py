# Communities formation using Girvan-Newman algorithm

import networkx as nx 

# Which edge to remove from the graph to form two communities ?
# This is done by calculating the betweenness centrality for each edge, and higher the betweenness centrality of an edge, sooner it is removed.
def edge_to_remove(G):
	dict1 = nx.edge_betweenness_centrality(G) # Returns dictionary, with 'edge' as key and 'edge betweenness centrality' as value 
	# Now we have to sort edges according to their betweenness centrality measures.
	list_of_tuples = dict1.items()
	list_of_tuples.sort(key = lambda x: x[1], reverse = True)
	return list_of_tuples[0][0] # Returns an edge (a,b) as a tuple ----> ((a,b))

# Function to implement Girvan-Newman algorithm.
def girvan(G):
	c = list(nx.connected_component_subgraphs(G))
	l = len(c)
	print 'The number of connected components in the graph : ', l

	while (l==1):
		G.remove_edge(*edge_to_remove(G))  # ((a,b)) ----> (a,b). That's why we use *
		c = list(nx.connected_component_subgraphs(G))
		l = len(c)
		print 'The number of connected components in the graph : ', l

	return c

G = nx.karate_club_graph() # Creating Karate Club network using builtin function
c = girvan(G) # Detecting communities in the network
print 'The communities formed are as follows :\n'
for i in c :
	print i.nodes()
	print 'Size of the community : ', i.number_of_nodes()
	print '\n'
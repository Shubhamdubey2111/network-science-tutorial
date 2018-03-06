# Community formation using Brute force method
# Try all the possible divisions and make the two best possible communities.

import networkx as nx
import itertools
import matplotlib.pyplot as plt 

# Function to detect communties and print them
def communities_brute(G):
	nodes = list(G.nodes()) # List of all the nodes in the graph
	n = G.number_of_nodes()

	# Finding all the possible divisions of nodes into two communities :
	first_community = [] # List of lists
	for i in range(1, n/2 + 1):
		comb = [list(x) for x in itertools.combinations(nodes, i)]   # comb is a list of lists
		first_community.extend(comb)

	second_community = [] # List of lists
	for i in range(len(first_community)):
		l = list(set(nodes) - set(first_community[i]))
		second_community.append(l)

	# Deciding which division is the best :
	num_intra_edges1 = [] # List containing no. of intra-community edges in 1st community, for different divisions
	num_intra_edges2 = [] # List containing no. of intra-community edges in 2nd community, for different divisions
	num_inter_edges = []  # List containing no. of inter-community edges, for different divisions
	ratio = [] # Ratio of "number of intra community edges" and "number of inter community edges"

	for i in range(len(first_community)):
		num_intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())

	for i in range(len(second_community)):
		num_intra_edges2.append(G.subgraph(second_community[i]).number_of_edges())

	e = G.number_of_edges() # Total number of edges in the graph
	for i in range(len(first_community)):
		num_inter_edges.append(e - num_intra_edges1[i] - num_intra_edges2[i]) # Inter-edges = Total-edges - (Intra-edges in 1 + Intra-edges in 2)

	# Finding the ratio :
	for i in range(len(first_community)):
		ratio.append(float(num_intra_edges1[i] + num_intra_edges2[i])/num_inter_edges[i])
	max_value = max(ratio)
	max_index = ratio.index(max_value) # To get the value of i corresponding to maximum value of ratio
	
	# Printing two formed communities :
	print first_community[max_index]
	print second_community[max_index]

G = nx.barbell_graph(5,0) # Creating brabell graph 
communities_brute(G) # Detecting and printing the communities in the network
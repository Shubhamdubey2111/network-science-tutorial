# Implementing PageRank using random walks
# Procedure :
# 1. Create/take a directed graph.
# 2. Initially all the nodes have zero points.
# 3. Select a random node and make it the start node.
# 4. Perform random walks on the graph with the goal of visiting each node at least once. 
# 	4.1. When a node is visited, increment its point(s) by one.
# 	4.2. If a node having no outlinks is reached, do teleportation, and resume the random walk.
# 5. Rank the nodes according to their accumulated points. 
# 6. Compare the ranking generated with the inbuilt PageRank algorithm function.

import networkx as nx 
import random
import numpy as np

# Function to add edges to the directed graph
def add_edges(G,p):
	for i in G.nodes():
		for j in G.nodes():
			if i != j :
				r = random.random()
				if r <= p:
					G.add_edge(i,j)
				else:
					continue
	return G

# Function to sort nodes according to their accumulated points
# We will denote "random-walk-point" by "RWP"
def get_nodes_sorted_by_RWP(RWP_list):
	RWP_array = np.array(RWP_list) # Converting list to numpy array
	nodes_sorted_by_RWP = np.argsort(-RWP_array) # The minus sign is used for sorting in descending order
	return nodes_sorted_by_RWP

# Function to perform random walks and increment random-walk-point of visited node by 1 
def random_walk(G):
	nodes = list(G.nodes()) # List of nodes of graph
	RWP = [0 for i in range(G.number_of_nodes())]  # List containing RWP of all nodes which are initially 0
	s_node = random.choice(nodes)  # Choosing starting (source) node at random
	RWP[s_node] += 1
	outlinked_neigh = G.out_edges(s_node)
	c = 0 # Iteration variable
	while (c != 100000):
		if (len(outlinked_neigh) == 0): # Case when the node has no outlink
			focus = random.choice(nodes) # focus is the node currently being visited
		else: 
			random_neigh = random.choice(list(outlinked_neigh)) 
			focus = random_neigh[1]
		RWP[focus] += 1
		outlinked_neigh = G.out_edges(focus)
		c += 1
	return RWP

# Function for main program	
def main():
	G = nx.DiGraph() # Creating a directed graph object
	N = 10 # Number of nodes in the graph
	p = 0.3 # Probability for generating random graph
	G.add_nodes_from([i for i in range(N)]) # Adding nodes to the graph object
	G = add_edges(G,p) # Adding edges to the graph object, making it a random graph

	RWP_list = random_walk(G) # Performing random walks on the graph and getting list of RWP for nodes
	nodes_sorted_by_RWP = get_nodes_sorted_by_RWP(RWP_list) # Ranking (ordering) nodes on the basis of accumulated RWP

	print 'Nodes sorted (ranked) according to the accumulated random-walk-points : ', 
	for i in nodes_sorted_by_RWP:
		print i,

	pr = nx.pagerank(G) # Getting PageRank of nodes, output is a dictionary
	pr_sorted = sorted(pr.items(), key=lambda x:x[1], reverse=True) 
	print '\nNodes sorted (ranked) using the builtin PageRank algo function : ',
	for i in pr_sorted:
		print i[0],

main() # Invoking the main function
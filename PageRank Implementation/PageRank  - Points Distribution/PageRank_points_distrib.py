# PROGRAM : 
#  Implementing PageRank algorithm using points distribution method.
# PSEDOCODE : 
#  1. Create a directed graph with 'n' nodes.
#  2. Assign 100 points to each node.
#  3. Each node distributes its points to its outlinked neighbors.
#  4. Keep distributing points (step 3) until convergence.
#  5. Get nodes' ranking on the basis of points accumulated by each node.
# CORRECTNESS : 
#  To check the correctness of our algo, we will compare our ranking with that of ranks obtained using networkx builtin PageRank func.

import networkx as nx 
import random
import numpy as np 

# Function to add edges between nodes (random graph)
def add_edges(G,p):
	for i in G.nodes():
		for j in G.nodes():
			if i != j:
				r = random.random()
				if r <= p:
					G.add_edge(i,j)
				else:
					continue
	return G

# Function to create & initialize list containing 100 points for each node
def initialize_points(G):
	points = [100 for i in range(G.number_of_nodes())]
	return points

# Function to distribute points of a node to its outlinked neighbors
def distribute_points(G, points):
	previous_points = points
	new_points = [0 for i in range(G.number_of_nodes())]
	for i in G.nodes():
		out = G.out_edges(i)
		if len(out) == 0:
			new_points [i] += previous_points[i]
		else:
			share = float(previous_points[i]/len(out))
			for each in out :
				new_points[each[1]] += share
	return G, new_points

# Function to handle points' sink
def handle_points_sink(G,points):
	for i in range(len(points)):
		points[i] = float(points[i] * 0.8)
		n = G.number_of_nodes()
		total_points = n * 100
		extra_points = float(n*100*0.2/n)
		for i in range(len(points)):
			points[i] += extra_points
	return points

# Function to keep distributing the points until convergence
def keep_distributing_points(G,points):
	previous_points = points
	print 'Enter # to stop' 
	while(1):
		G, new_points = distribute_points(G, previous_points)
		print new_points
		new_points = handle_points_sink(G,new_points)
		char = raw_input()
		if char == '#':
			break
		previous_points = new_points
	return G, new_points

# Function to sort nodes according to their accumulated points
def get_nodes_sorted_by_points(points):
	points_array = np.array(points)  # Converting list to numpy array
	nodes_sorted_by_points = np.argsort(-points_array)   # The minus sign is used for sorting in descending order
	return nodes_sorted_by_points
	
# The main program starts here :-
G = nx.DiGraph() # Creating a directed graph object
N = 10 # N is the number of nodes in the graph object
p = 0.3 # Probability for generating random graph
G.add_nodes_from([i for i in range(N)]) # Adding nodes to the graph object
G = add_edges(G,p) # Adding edges to the graph object 
points = initialize_points(G) # Initializing points of each node to 100
print points # Printing the points possessed by each node initially
G, points = keep_distributing_points(G,points) # Performing iterations of points distributions until convergence
sorted_nodes = get_nodes_sorted_by_points(points) # Ranking (sorting) the nodes on the basis of accumulated points
print 'List of nodes sorted according to their accumulated points : ',
for i in sorted_nodes:
	print i,
pr = nx.pagerank(G)  # Returns dictionary with nodes as key and their PageRank as values.
pr_sorted = sorted(pr.items(), key = lambda x:x[1], reverse=True)  # Sorting the dictionary items according to the values(PageRank)
print '\nList of nodes sorted using PageRank algorithm (inbuilt) -----> ',
for i in pr_sorted: 
	print i[0],
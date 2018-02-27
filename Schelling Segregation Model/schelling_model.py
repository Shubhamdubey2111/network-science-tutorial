# Simulating Schelling Model of Segregation
# Assumptions :
# The colony is a N*N size square grid. Each cell in the grid is a house. 
# There are two kinds of people living in the colony. (E.g. different religions (say))
# Some houses are occupied while some are empty.
# A person is satisfied if s/he has a certain number of neighbors of its own type (threshold value), otherwise not satisfied.
# An unsatisfied person move to a randomly selected empty cell in the grid, in the hope of getting un-dissatisfied (Not satisfied)!

import networkx as nx
import matplotlib.pyplot as plt
import random

N = 10 # Size of the square grid = N*N
G = nx.grid_2d_graph(N,N)

# Forming a rectangular grid by positioning the nodes
pos = dict((p,p) for p in G.nodes())

# Getting labels for the nodes.
labels = dict(((i,j), 10*i+j) for i,j in G.nodes())

# Adding diagonal connections across the nodes
for (u,v) in G.nodes():
	if((u+1 <= N-1) and (v+1 <= N-1)):
		G.add_edge((u,v),(u+1,v+1))
for (u,v) in G.nodes():
	if ((u-1 >= 0) and (v+1 <= N-1)):
		G.add_edge((u,v),(u-1,v+1))

# Populating the grid with two kinds of people, leaving some nodes empty
for n in G.nodes():
	G.node[n]['type'] = random.randint(0,2) 

# Making lists of similar type nodes(people), and empty nodes(no residence)
empty_nodes_list = [n for n,d in G.nodes(data=True) if d['type']==0]
type1_nodes_list = [n for n,d in G.nodes(data=True) if d['type']==1]
type2_nodes_list = [n for n,d in G.nodes(data=True) if d['type']==2]


# Function to color nodes on the basis of occupancy, and drawing the graph
def drawing_graph(G, pos, labels, type1_nodes_list, type2_nodes_list, empty_nodes_list):
	nodes_g = nx.draw_networkx_nodes(G, pos, node_color = 'green', nodelist = type1_nodes_list)
	nodes_r = nx.draw_networkx_nodes(G, pos, node_color = 'red', nodelist = type2_nodes_list)
	nodes_w = nx.draw_networkx_nodes(G, pos, node_color = 'white', nodelist = empty_nodes_list)
	nx.draw_networkx_edges(G, pos)
	nx.draw_networkx_labels(G, pos, labels = labels)

drawing_graph(G, pos, labels, type1_nodes_list, type2_nodes_list, empty_nodes_list)
plt.title('A colony of 100 houses', fontsize=15, color='blue')
plt.show()

# Function for getting the list of boundary nodes
def get_boundary_nodes():
	boundary_nodes_list = []
	for (u,v) in G.nodes():
		if(u==0 or u==N-1 or v==0 or v==N-1):
			boundary_nodes_list.append((u,v))
	return boundary_nodes_list

boundary_nodes_list = get_boundary_nodes()

# Getting the list of internal nodes
internal_nodes_list = list(set(G.nodes()) - set(boundary_nodes_list)) 

# Function to get neighbors of an internal node
def get_neigh_for_internal(u,v):
	return [(u,v-1), (u,v+1), (u-1,v), (u+1,v), (u-1,v+1), (u-1,v-1), (u+1,v-1), (u+1,v+1)]

# Function to get neighbors of a boundary node
def get_neigh_for_boundary(u,v):
	# Corner cases :
	if (u==0 and v==0):
		return [(u+1,v), (u,v+1), (u+1,v+1)]
	elif (u==0 and v==N-1):
		return [(u+1,v), (u,v-1), (u+1,v-1)]
	elif (u==N-1 and v==0):
		return [(u-1,v), (u,v+1), (u-1,v+1)]
	elif (u==N-1 and v==N-1):
		return [(u,v-1), (u-1,v), (u-1,v-1)]
	# Side cases (Non-corner but boundary cases)
	elif (u==0):
		return [(u,v+1), (u,v-1), (u+1,v), (u+1,v+1), (u+1,v-1)]
	elif (v==N-1):
		return [(u-1,v), (u+1,v), (u,v-1), (u-1,v-1), (u+1,v-1)]
	elif (u==N-1):
		return [(u,v-1), (u,v+1), (u-1,v), (u-1,v+1), (u-1,v-1)]
	elif (v==0):
		return [(u-1,v), (u+1,v), (u,v+1), (u+1,v+1), (u-1,v+1)]


# Function to get the list of unsatisfied nodes(people) in the colony
def get_unsatisfied_nodes_list(G, boundary_nodes_list, internal_nodes_list):
	unsatisfied_nodes_list = []
	t = 3  # t is the threshold of each node
	for u,v in G.nodes():
		if G.node[(u,v)]['type'] == 0:
			continue
		else:
			same_count = 0
			#neighbours = []
			if ((u,v) in internal_nodes_list):
				neighbours = get_neigh_for_internal(u,v)
			elif ((u,v) in boundary_nodes_list):
				neighbours = get_neigh_for_boundary(u,v)	
			
			for each in neighbours:
				if (G.node[(u,v)]['type'] == G.node[each]['type']):
					same_count += 1
			if same_count <= t:
				unsatisfied_nodes_list.append((u,v))
	return unsatisfied_nodes_list


# Function to make a node get satisfied
def get_a_node_satisfied(unsatisfied_nodes_list, empty_nodes_list):
	if len(unsatisfied_nodes_list) != 0:
		node_to_satisfy = random.choice(unsatisfied_nodes_list)
		new_position = random.choice(empty_nodes_list)
		
		# Type and label of nodes will be swapped. Simply using the technique x,y = y,x
		G.node[new_position]['type'], G.node[node_to_satisfy]['type'] = G.node[node_to_satisfy]['type'], G.node[new_position]['type']
		labels[new_position], labels[node_to_satisfy] = labels[node_to_satisfy], labels[new_position]
	else:
		pass

# while len(get_unsatisfied_nodes_list(G, boundary_nodes_list, internal_nodes_list))>0:
# The above iterations could run indefinitely, so not used.
for i in range(10000):
	unsatisfied_nodes_list = get_unsatisfied_nodes_list(G, boundary_nodes_list, internal_nodes_list)
	get_a_node_satisfied(unsatisfied_nodes_list, empty_nodes_list)
	empty_nodes_list = [n for n,d in G.nodes(data=True) if d['type']==0]
	type1_nodes_list = [n for n,d in G.nodes(data=True) if d['type']==1]
	type2_nodes_list = [n for n,d in G.nodes(data=True) if d['type']==2]

# Drawing the colony structure after segregation :
drawing_graph(G, pos, labels, type1_nodes_list, type2_nodes_list, empty_nodes_list)
plt.title('Result of simulating Schelling Segregation Model', color='blue')
plt.show()
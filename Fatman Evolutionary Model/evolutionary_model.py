# Implementing the Fatman Evolutionary Model

# Assumptions :
# A city consisting of 100 people with different weights, hence different BMIs
# BMI is a number in the range [15,40]
# In the beginning every person should be a member of exactly one social foci.

import networkx as nx
import matplotlib.pyplot as plt
import random
import math

def create_graph():
	''' Function to create and return a graph object with 100 nodes''' 
	G = nx.Graph()
	G.add_nodes_from(range(1,101))
	return G

def assign_bmi(G):
	'''Function to randomly assign BMI to each person in the network.'''
	for i in G.nodes():
		G.node[i]['type'] = 'person'
	 	G.node[i]['name'] = random.randint(15,40)

def add_foci_nodes():
	'''Function to add social foci nodes to the network'''
	n = G.number_of_nodes()
	i = n+1
	foci_nodes = ['Gym','Eatout','Movie_club','Karate_club','Yoga_club']
	for j in range(0,5):
		G.add_node(i)
		G.node[i]['name'] = foci_nodes[j]
		G.node[i]['type'] = 'foci'
		i=i+1
	return G

def get_foci_nodes():
	'''Function to get the list of social foci nodes.'''
	f_nodes = []
	for i in G.nodes():
		if G.node[i]['type'] == 'foci':
			f_nodes.append(i)
	return f_nodes

def get_person_nodes():
	'''Function to get the list of person nodes.'''
	p_nodes = []
	for i in G.nodes():
		if G.node[i]['type'] == 'person':
			p_nodes.append(i)
	return p_nodes

def add_foci_edges():
	'''Function to randomly assign each person to exactly one social foci.'''
	foci_nodes = get_foci_nodes()
	person_nodes = get_person_nodes()
	for i in person_nodes:
		r = random.choice(foci_nodes)
		G.add_edge(i,r)

def homophily(G):
	person_nodes = get_person_nodes()
	for u in person_nodes:
		for v in person_nodes:
			if u != v:
				diff = abs(G.node[u]['name'] - G.node[v]['name'])
				p_connection = float (1)/(diff+2500)              # 2500 is added to bring down the scale of probability, as we want evolution to be slow.
				r = random.random()
				if r<p_connection:
					G.add_edge(u,v)


# We need to find the number of common neighbours of two nodes. This operation seems like intersection of two sets, right!
def cmn(u,v,G):
	'''This function returns the number of common neighbours for two nodes'''
	nu = set(G.neighbors(u))  # Neighbors of u
	nv = set(G.neighbors(v))  # Neighbors of v
	return len(nu & nv)       # & operator is used to take intersection of two sets

def closure(G):
	array1=[]
	for u in G.nodes():
		for v in G.nodes():
			if u!=v and (G.nodes[u]['type'] == 'person' or G.nodes[v]['type'] == 'person'):
				k = cmn(u,v,G) # k is the number of common nodes for nodes u and v
				p = 1 - math.pow((1-0.01),k)
				temp=[]
				temp.append(u)
				temp.append(v)
				temp.append(p)
				array1.append(temp)
	for i in array1:
		u = i[0]
		v = i[1]
		p = i[2]
		r = random.uniform(0,1)
		if r<p:
			G.add_edge(u,v)

def change_bmi(G):
	f_nodes = get_foci_nodes()
	for i in f_nodes:
		if G.node[i]['name']=='Eatout':
			for j in G.neighbors(i):
				if G.node[j]['name']!=40:
					G.node[j]['name'] = G.node[j]['name']+1
		if G.node[i]['name']=='Gym':
			for j in G.neighbors(i):
				if G.node[j]['name']!=15:
					G.node[j]['name']=G.node[j]['name'] - 1

###################################################################################################################################
def visualize(G):
	''' Function to draw and visualize a graph'''
	labeldict = get_labels(G)
	nodesize = get_size(G) # Array for sizes of different nodes, according to theirt BMI
	color_array = get_colors(G) # Array for color of each node, according to their type attribute.
	nx.draw(G, labels=labeldict, node_size=nodesize, node_color=color_array)
	plt.show()
	
def get_labels(G):
	'''Function to get BMI value for each person in the network.'''
	dict1={}
	for i in G.nodes():
		dict1[i] = G.node[i]['name']
	return dict1

def get_size(G):
	'''Function to create an array containing size of each node proportional to its BMI.'''
	array1=[]
	for i in G.nodes():
		if G.node[i]['type'] == 'person':
			array1.append(G.node[i]['name']*20) # Multiplying BMI by 20 for each node, to scale the node size to bigger.
		else:
			array1.append(3000)  # Size for all foci nodes
	return array1

def get_colors(G):
	'''Function to add different colors to nodes, according to their type attributes.'''
	colors=[]
	for i in G.nodes():
		if G.node[i]['type'] == 'person':
			if G.node[i]['name'] == 15: # Underweight person is depicted as green node
				colors.append('green')
			elif G.node[i]['name'] == 40: # Overweight person is depicted as yellow node
				colors.append('yellow')
			else:
				colors.append('blue') # Person nodes are blue in color
		else:
			colors.append('red') # Foci nodes are red in color
	return colors
##################################################################################################################################

G = create_graph()
assign_bmi(G)
add_foci_nodes()
add_foci_edges()

for t in range(0,10):
	homophily(G) # Running one iteration of homophily
	closure(G)
	change_bmi(G)
	visualize(G)
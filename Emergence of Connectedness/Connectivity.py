import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy


# Returns a graph with n number of nodes in it.
def add_nodes(n):
	G=nx.Graph()
	G.add_nodes_from(range(n))
	return G

# Function to add a random edge to the graph, and returns a graph object
def add_rand_edge(G):
	v1=random.choice(list(G.nodes()))
	v2=random.choice(list(G.nodes()))
	if v1!=v2:
		G.add_edge(v1,v2)
	return G

# Function to keep on adding random edges until graph becomes connected.
def add_till_connected(G):
	while nx.is_connected(G)==0:
		G=add_rand_edge(G)
	return G


# Creates an instance of connected graph, and returns the number of edges required to make the graph of n nodes connected.
def create_instance(n):
	G=add_nodes(n)
	G=add_till_connected(G)
	return G.size()


# Returns the AVERAGE number of edges required to make a graph of n nodes connected. 
# It creates 200 instances of a connected graph and take the average of the no of edges required each time.
def create_avg_instance(n):
	G=add_nodes(n)
	list1=[]
	for i in range(200):
		list1.append(create_instance(n)) 
	return numpy.average(list1)

#Plotting the desired for different number of nodes network to become connected.
def plot_connectivity():
	x=[] #List to contain 'no of nodes'
	y=[] #List to contain no of edges required to make the graph connected having no of nodes corresponding to items in x 
	x1=[] #List to contain values of n 
	y1=[] #List to contain values of n*log(n) corresponding to the values of n in x1
	i=10
	while i<=100:
		print 'Calulating average number of edges for ', i, ' nodes...'
		x.append(i)
		y.append(create_avg_instance(i))
		x1.append(i)
		y1.append(i*float(numpy.log(i)))   # Try it for y1.append(i*(float(numpy.log(i)))/2)
		i=i+10

	plt.title('Emergence of Connectivity', fontsize=15, color='red')
	plt.xlabel('No of Nodes (n)', fontsize=12, color='green')
	plt.ylabel('Min edges required just to make the network connected', fontsize=12, color='green')
	plt.plot(x,y, 'blue') #Plotting the curve corresponding to our synthetic network
	plt.plot(x1,y1,'red') #Plotting the curve of n*log(n)
	plt.show()

plot_connectivity()

# Analysis of Karate club network using networkx library

import networkx as nx 
import matplotlib.pyplot as plt

# Calculating the degree of the network
def deg_of_net(G):
        print 'Is the karate club network graph directed ? : ', nx.is_directed(G)
        all_degrees = []  # List containing degree of each individual nodes
        for i in nx.degree(G):
                all_degrees.append(i[1])
        sum_degrees = 0 # Sum of degree of all nodes
        for i in all_degrees:
                sum_degrees=sum_degrees+i
        print 'Degree of the network is : ', sum_degrees/nx.number_of_nodes(G) 

# Plotting degree distribution curve, and loglog curve for the Karate network
def plot_deg_dist(G):  
	all_degrees = []  # List containing degree of each individual node
	for i in nx.degree(G):
		all_degrees.append(i[1])
	unique_degrees = list(set(all_degrees)) # List containing possible degrees in the network, without repetition.
	freq = []  # List containing the frequency of each degree in the network i.e. how many nodes have a particular degree.
	for i in unique_degrees:
		freq.append(all_degrees.count(i))

	# Plotting the loglog curve, which determines whether the network follows Power Law degree distribution or not :-
	plt.title('Loglog curve : Karate club network', fontsize=15, color='red')
	plt.xlabel('log of degrees in the network', fontsize=12, color='green')
	plt.ylabel('log of node freq for a particular degree', fontsize=12, color='green')
	plt.loglog(unique_degrees,freq, 'bo-')
	plt.show()

	# Plotting the curve of degree distribution in the network :-
	plt.title('Degree Distribution : Karate Club Network', fontsize=15, color='red')
	plt.xlabel('Degrees', fontsize=12, color='green')
	plt.ylabel('No of Nodes', fontsize=12, color='green')
	plt.axis([0,18,0,20])
	plt.plot(unique_degrees,freq, 'bo-')
	plt.show()


G = nx.read_gml('karate.gml', label="id") # Reading the karate network from the datset file
deg_of_net(G) # Invoking the function
plot_deg_dist(G) # Invoking the function


# Computing the density of the network
print '\nThe density of the network is : ', nx.density(G) # nx.density(G) returns an int value


# Computing the diameter of the network :
print '\nThe Diameter of the network is : ', nx.diameter(G), '\n' # nx.diameter(G) returns an int value


# Computing clustering coefficients in the network :-
# nx.clustering(G) outputs a "dictionary" with the clustering coefficient as value for each node as a key.
# nx.average_clustering(G) computes the average clustering coefficient of the network, returns a float value.
clustering_coefficients = []  # A list having tuples as its items, tuple contains node and its clustering coefficient
sum_cc=0 #Sum of all the clustering coefficients in the network
for i in nx.clustering(G).items():
	sum_cc=sum_cc+i[1]
	print 'Clustering coefficient of ', i[0], 'is : ', i[1]
print '\nAverage clustering coefficient of the network : ', (sum_cc/nx.number_of_nodes(G)) 
print '\n(Using builtin func) Average clustering coefficient of the network : ', nx.average_clustering(G) # Computes average clustering coefficient of the network
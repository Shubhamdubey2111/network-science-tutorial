# How many random walks does it take to reach the entire graph i.e., reach all the vertices of the given graph
import networkx as nx 
import matplotlib.pyplot as plt 
import random
import numpy

#Function to calculate the number of random walks required to completely visit (visit each node at least once) a graph of n nodes.
def walk(n,p):
	start = random.randint(0,n-1)
	G = nx.erdos_renyi_graph(n,p)
	S = set([]) 
	v = start
	count = 0
	while (len(S)<n):
		Nbr = list(nx.neighbors(G,v))
		v = random.choice(Nbr)
		S.add(v)
		count += 1
	return count

l = []
for n in range(20,150): # Graph size vary from 20 nodes to 150 nodes
	z = []
	for j in range(10): # Taking 10 instances of random walks for a particular graph. Higher the no. of instances, more accurate is the no of walks required.
		z.append(walk(n,0.3))
	l.append(numpy.average(z)) # Taking the average of 10 instances of random walks on each graph.
	print n, "---->", numpy.average(z)
plt.plot(l)
plt.xlabel('No of nodes in the graph', fontsize=12, color='green')
plt.ylabel('No of random walks required for visiting all nodes', fontsize=12, color='green')
plt.title('Random walks on a graph', fontsize=15, color='red')
plt.show()
# Relationship between PageRank and DegreeRank
# The citation network dataset has been used.
# In degree value on x-axis and PageRank value on y-axis


import networkx as nx 
import matplotlib.pyplot as plt 

def main():
	G = nx.read_edgelist('Cit-HepTh.txt', create_using=nx.DiGraph())

	deg = dict(G.in_degree())  #Returns a dictionay, with key as nodes and indegrees as values.
	pr = nx.pagerank(G)
	pr_values = []
	for i in deg.keys():
		pr_values.append(pr[i])

	plt.plot(deg.values(), pr_values, 'ro', markersize = 3)
	plt.xlabel('Indegree value of the nodes')
	plt.ylabel('PageRank value of the nodes')
	plt.show()
main()
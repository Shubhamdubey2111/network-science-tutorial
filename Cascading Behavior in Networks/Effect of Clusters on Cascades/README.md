# Effect of Cluster Density on Information Cascades
Whenever an idea or innovation is spreading on a network having communities/clusters, then the question arises whether the clusters have an effect on the information cascade i.e., whether the clusters affect the spread of information on the network.  
The answer is __Yes__.  
The density of a cluster(s) plays a significant role in determining whether the information cascade will complete or not.

## Cluster Density
We say that a cluster of density _p_ is a set of nodes such that each node in the set has at least a _p_ fraction of its network neighbors in the set. <sup>[[1]](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch19.pdf)</sup>

## Relationship between Clusters and Cascades
A cascade comes to a stop when it runs into a dense cluster; and furthermore, that a dense cluster is the ___only___ thing which causes a cascade to stop.  
In other words, __"clusters are natural obstacles to cascades"__.

Consider a set of initial adopters of behavior _A_, with a threshold of _q_ for nodes in the remaining network to adopt behavior _A_.
1. If the remaining network contains a cluster of density greater than _1-q_, then the set of initial adopters will not cause a complete cascade.
2. Whenever a set of initial adopters doesn't cause a complete cascade with threshold _q_, the remaining network must contain a cluster of density greater than _1-q_.

---
The program contained in the directory verifies the PART - I of the above claim.  
__Source :__ The above definitions and description have been taken from the book [Networks, Crowds, and Markets — Chapter 19](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch19.pdf)

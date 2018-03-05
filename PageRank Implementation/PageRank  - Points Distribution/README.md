PageRank using Points Distribution 
===================================
In this program, [PageRank](https://en.wikipedia.org/wiki/PageRank) algorithm has been implemented using a method of points distribution.

## Description of the implementation 

Given a [directed graph](https://en.wikipedia.org/wiki/Directed_graph), each node is assigned a fixed equal number of points.  
Every node distributes its points equally to its neighbors connected via an _outgoing link_. For example, if a node has 100 points, and has two outlinks, then each outlinked neighbor gets 50 points. Several iterations of this process are performed.  
After every iteration, the points that each node possesses keep on changing.  
However, after a certain number of iterations, the points accumulated by each node do not change, i.e., we get a convergence.  
If we keep on running more iterations after convergence, nothing will change. This is because, the number of points which a node will distribute to its outlinks will be equal to the number of points it will receive from its inlinks.  
Hence, at the point of convergence, every node will be having fixed number of accumulated points.  
The nodes are then sorted according to the number of points accumulated by them.  
The sorting process will yield the ranking of nodes in the graph. This ranking shows the relative importance of a node in the graph structure.  
This ranking is known as PageRank. At the end, we will compare the ranking done by our algorithm with that of the inbuilt PageRank algorithm in [Networkx](https://en.wikipedia.org/wiki/NetworkX) library.

----
Sometimes, the two rankings will differ. This happens due to either of the following two reasons :

1) __Sink nodes :__  
    A [sink node](http://mathworld.wolfram.com/DigraphSink.html) is a node with zero outlinks but non-zero inlinks.
In that case, such nodes can never distribute their points, but only receive points from their inlinked neighbors.
This leads to these nodes accumulating all the points in the graph, and a points' sink occurs.
We can take care of this condition by making some modifications to the code, as done in the program. (_See the source code_)

2) __Two nodes have the same ranking :__  
    In this case, the difference in ranking doesn't matter, because the two nodes have same importance in the graph structure.

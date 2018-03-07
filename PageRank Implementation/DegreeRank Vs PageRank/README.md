DegreeRank versus PageRank
==========================
The program tests whether there is a correlation between PageRank and DegreeRank of a node i.e., if a node has high indegree then will it have higher pagerank ?

The dataset used is that of [High-energy physics theory citation network](https://snap.stanford.edu/data/cit-HepTh.html).

## Ouput Plot
![Indegree Vs PageRank](https://github.com/Shubhamdubey2111/Network-Science/blob/master/PageRank%20Implementation/DegreeRank%20Vs%20PageRank/Indegree_vs_pagerank.png)

__Following conclusions are drawn from the above plot :__

* There is no correlation between PageRank and IndegreeRank. The distribution
* Some papers though having few citations have high pagerank. These are the papers which have been cited by papers which themselves have very high citations. 
* Some papers though having high number of citations have low pagerank. These are the papers which have been cited by papers which themselves have very few citations.
* Pagerank of a node depends not only on the number of inlinks but on the quality of inlinks.

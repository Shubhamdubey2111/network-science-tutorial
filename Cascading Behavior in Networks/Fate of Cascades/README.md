Fate of the Cascade
===================
# Description
When we take a set of nodes as the initial adopters of a new behavior, then with time the behavior of each node changes depending on the threshold rule.  
Consider the chain reaction of switching to new behavior as __cascade of adoptions__.  
There are two possibilities :
* __Complete Cascade :__  
There is a complete cascade where all the nodes have adopted the same new behavior.
* __Incomplete Cascade :__
  * The cascade runs for a while but stops while there are still some nodes having old behavior.
  * The cascade runs and stops with the initial adopters getting switched to their old behavior, hence all nodes have old behavior.

# Program
Given a network with all nodes initially having behavior _B_, two initial adopters of new behavior _A_, and the value of payoffs associated with two behaviors _A_ and _B_, the program determines the fate of the cascade in the network i.e., whether the cascade will complete or not i.e., sweep over the entire network.

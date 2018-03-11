Modeling Diffusion through a Network
====================================
In an underlying [social network](https://en.wikipedia.org/wiki/Social_network), we will study a situation in which each node has a choice between two possible behaviors, labeled _A_ and _B_. If nodes _v_ and _w_ are linked by an edge then there is an incentive for them to have their behaviors match. This is represented using a game as follows :

# A Networked Coordination Game
* _v_ and _w_ are players, and _A_ and _B_ are the possible strategies.
* The payoffs are defined as follows :
  * If nodes _u_ and _v_ both adopt behavior _A_, they each get a payoff of _a_ > 0;
  * If they both adopt _B_, they each get a payoff of _b_ > 0; and
  * If they adopt opposite behaviors, they each get a payoff of 0.
* Each node is playing a copy of this game with its neighbors, and its payoff is the sum of its payoffs in the games played on each edge.  
Hence _v_'s choice of strategy will be based on the choices made by all of its neighbors, taken together.
Now, suppose that some of _v_'s neighbors adopt _A_, and some adopt _B_; what should _v_ do in order to maximize its payoff ?  
This clearly depends on the relative number of neighbors doing each, and on the relation between the payoff values _a_ and _b_.

## __Decision Rule__ (__Threshold Rule__)
Suppose :
* _d_ is the number of neighbors of _v_.
* _p_ fraction of _v_'s neighbors have behavior _A_, i.e., [_p_ * _d_] neighbors adopt _A_.
* (1-_p_) fraction of _v_'s neighbors have behavior _B_, i.e., [(1-_p_) * _d_] neighbors adopt _B_.

Then :
* If _v_ chooses behavior _A_, then its payoff would be (_p_ * _d_ * _a_)
* If _v_ chooses behavior _B_, then its payoff would be [(1-_p_) * _d_ * _b_].

Now, adopting behavior _A_ would be a better choice, when the following condition is satisfied :  
Payoff associated with choosing _A_ >= Payoff associated with choosing _B_  
=> (_p_ * _d_ * _a_) >= [(1-_p_) * _d_ * _b_]  
Rearranging terms, we get :  
_p_ >= _b_/(_a_+_b_) ___(Threshold rule)___  
Let _q_ = _b_/(_a_+_b_)  
__So, if "at least" _q_ fraction of a node's neighbors follow behavior _A_, then the node will also follow behavior _A_.__

# Modeling the Game in a Social Network
1. A social network is given.
2. Everyone in the network is initially using _B_ as the default behavior.
3. Then, a small set of initial adopters all decide to adopt behavior _A_.  
They have somehow switched due to a belief in _A_'s superiority, rather than by following payoffs — but we will assume that all other nodes continue to evaluate their payoffs using the [coordination game](https://github.com/Shubhamdubey2111/Network-Science/new/master#a-networked-coordination-game).
4. Given the fact that the initial adopters are now using _A_, some of their neighbors may decide to switch to _A_ as well, and then some of their neighbors might, and so forth, in a potentially __cascading fashion__.
5. Time then runs forward in unit steps; in each step, each node uses the [decision rule](https://github.com/Shubhamdubey2111/Network-Science/new/master#decision-rule-threshold-rule) to decide whether to switch from _A_ to _B_.
6. The process stops either when every node has switched to _A_ or when we reach a step where no node wants to switch, at which point things have stabilized on coexistence between _A_ and _B_.

## Following Questions arise 
* When does this result in every node in the entire network eventually switching over to _A_ ?
* When this isn't the result i.e., the behavior _A_ is not able to spread across the entire network, and what causes the spread of _A_ to stop ?

The answers to the above questions depend on the following :
* The structure of the network.
* The initial adopters of bahavior _A_.
* The value of the threshold _q_ that nodes use for deciding whether to switch to _A_.

---
___Source :___ The above example has been taken from the book [Networks, Crowds, and Markets — Chapter 19](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch19.pdf).

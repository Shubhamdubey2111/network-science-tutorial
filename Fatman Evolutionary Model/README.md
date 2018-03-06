Fatman Evolutionary Model
=========================
__Fatman Hypothesis :__  
If a person's friend is obese, then s/he is likely to become obese too.
This hypothesis is a direct result of social contagion.

## What is an Evolutionary Model ?
An evolutionary model is a model that evolves with time.  
A network model is evolutionary if new edges are formed with time and some previous edges get removed from the network.

## Phenomena occuring in the model
The following network phenomena are implemented into the model :
* [Homophily](https://en.wikipedia.org/wiki/Homophily)
* All three [types](http://player.slideplayer.com/26/8547687/data/images/img37.jpg) of [closures](https://en.wikipedia.org/wiki/Closure)
  * [Triadic Closure](https://en.wikipedia.org/wiki/Triadic_closure)
  * Foci Closure
  * Membership closure
* Social Influence

## Description of the model
* There is a city having 100 citizens of different kinds, different in terms of their body weight and hence their [BMI](https://en.wikipedia.org/wiki/Body_mass_index) value.
* The range of BMI values is [15,40].
* A person with BMI = 15 is considered as underweight, and a person with BMI = 40 is considered as obese. 
* We have 5 social foci in the city, viz. Eatout, Gym, Movie Club, Karate club, and Yoga Club.
* People having comparable BMI will become friends with each other. (Homophily)
* People having a common friend will become friends with each other. (Triadic Closure)
* People who are members of the same social foci will become friends with each other. (Foci closure)
* If one of the two friends is a member of a particular social foci, then the other one will also become a member of that social foci. (Membership closure)  

## Assumptions for our model
1. In the beginning of the evolution process, each citizen is a member of exactly one social foci.
2. Only two (Eatout and Gym) out of five social focus will take part in foci closure.
3. Though new edges can form between nodes (as a result of homophily, closures, etc), but none of the edges can be deleted.

## Visualization reference 
* The social foci nodes are red colored.
* The person nodes are blue colored.
* The obese people nodes are yellow colored.
* The underweight people nodes are green colored.
* Size of each person node is directly proportional to its BMI value.

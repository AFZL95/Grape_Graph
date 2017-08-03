# Grape Graph

Grape Graph is an effort to implement Graph algorithms in Python.

## what should this repository consists?

first things first, abstract implementation of graph structure

it's "Graph.py" which implement the graph abstract type and two way of storing data in it:

1. Adjacency Matrix Graph
2. Adjacency Set Graph

then in the Graph class, I wrote a simple Test to check everything is ok or not.

### Advantages and Disadvantages:
Adjacency Matrix is suitable for small and densely connected graphs

Adjacency List is more usefull for large, sparsely connected graphs

### Comparing Graph Representations:

|     :)       | Adjacency Matrix | Adjacency List
| :--- | :---: | :---: |
|Space Required| O(V^2) | O(E+V)   
|Checking if edge is present| O(1) | O(degree V) |
|Iterating over edges       | O(V) | O(degree V) |

### Traversing Graph Structure

When we model a graph for a real world relationship, 

we might visit every node of our graph and perform some kind of processing

on each node. "Depth-First" and "Breadth-First" are two ways of traversing a graph.

![img_1](https://github.com/AFZL95/Grape_Graph/blob/master/img/img_1.png)

so Travesing this tree with Breadth-First approach would be like:

H -> B -> F -> A -> G -> E -> C -> D

and with Depth-First approach we gonna have this sort of traversing:

H -> B -> A -> F -> G -> E -> C -> D

### Comparing Traversal Algorithms

| Traversing a Tree | Traversing a Graph |
| :---             | ---:              |
| one node is designed to be root | Not designed root |
|only one specific path from root to any node | Multiple paths possible between any pair of nodes|
| No Cycles | Cycles possible |
|any node will be visited exactly once | Nodes could be visited multiple times |
| No need to track which nodes already visited | Essential to track which node already visited
|No unconnected nodes possible | Unconnected nodes possible|
| No need to track which nodes already visited | Algorithm can not terminate untill all nodes have been visited |
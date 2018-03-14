# Grape Graph

Grape Graph is an effort to implement Graph algorithms in Python.

![grape_graph logo](https://github.com/AFZL95/Grape_Graph/blob/master/img/gg.jpg)

## What does this repository have?

first things first, abstract implementation of graph structure.

it's "graph.py" which implement the graph abstract type and two way of storing data in it:

1. Adjacency Matrix Graph
2. Adjacency Set Graph

then in the Graph class, I wrote a simple Test to check everything is ok or not.

### Advantages and Disadvantages of those two ways:
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

we might visit every node of our graph and perform some kind of processing,

on each node. "Depth-First" and "Breadth-First" are two ways of traversing a graph.

![img_1](https://github.com/AFZL95/Grape_Graph/blob/master/img/img_1.png)

so traversing this tree with Breadth-First approach would be like:

H -> B -> F -> A -> G -> E -> C -> D

and with Depth-First approach we gonna have this sort of traversing:

H -> B -> A -> F -> G -> E -> C -> D

### Comparing Traversal Algorithms

| Traversing a Tree | Traversing a Graph |
| :---             | ---:              |
| One node is designed to be root | Not designed root |
|Only one specific path from root to any node | Multiple paths possible between any pair of nodes|
| No Cycles | Cycles possible |
|Any node will be visited exactly once | Nodes could be visited multiple times |
| No need to track which nodes already visited | Essential to track which node already visited
|No unconnected nodes possible | Unconnected nodes possible|
| No need to track which nodes already visited | Algorithm can not terminate untill all nodes have been visited |

### Implementing the traversal algorithms

two approach of traversing the graph is implemented.

first the "breadth_first" algorithm and second, "depth_first"

"traversal.py" module is highly documented and there is no need for further comments.

### Implementing path related algorithms

in this section, the most two important algorithms were implemented.

dijkstra and kruskal

### miscellaneous

in the case of implementation of shortest path algorithms and path related algorithms i've used Matteo Dell'Amico's python implementation for priority queue.

which can be found in the algorithms directory.
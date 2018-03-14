# importing "abc" for abstract base class thing
# and have need for numpy for setting up
import abc

import numpy as np


#######################################################################
#
# The base class representation of a Graph with all the interface
# methods
#
#######################################################################

# "Graph" class drives from python abstract base class
class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        # how many vertices does graph have
        # a unique number ranging from 0 to num_vertices
        self.numVertices = numVertices
        # by default we assume presented graph is undirected
        self.directed = directed

    # with this decorator below we indicate that "add_edge" method
    # is an abstract method, which
    # will be implemented later by any class that derives from "Graph"

    # add edge between two vertices
    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        # cuz we do not implement things in abstract method,
        # we pass !
        pass

    # decorator is added as same as "ad_edge"'s decorator
    # get number of adjacent vertices
    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    # get number of edges that connected to vortex "v"
    @abc.abstractmethod
    def get_indegree(self, v):
        pass
    # return the weight of edge between "v1" and "v2"
    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass
    # print out the graph
    @abc.abstractmethod
    def display(self):
        pass


#######################################################################
#
# A single node in a graph represented by an adjacency set. Every node
# has a vertex id
# Each node is associated with a set of adjacent vertices
#
#######################################################################
class Node:
    def __init__(self, vertexId):
        # every node have a unique id starts from zero to num_vertices -1
        self.vertexId = vertexId
        # each node maintain a set of it's adjacent nodes
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            # if we do not consider ring edges !
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        # in a sorted manner !
        return sorted(self.adjacency_set)


#######################################################################
#
# Represents a graph as an adjacency set. A graph is a list of Nodes
# and each Node has a set of adjacent vertices. 
# This graph in this current form cannot be used to represent
# weighted edges only unweighted edges can be represented
#
#######################################################################
class AdjacencySetGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)

        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights >1")

        self.vertex_list[v1].add_edge(v2)
        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


#######################################################################
#
# Represents a graph as an adjacency matrix. A cell in the matrix has
# a value when there exists an edge between the vertex represented by
# the row and column numbers.
# Weighted graphs can hold values > 1 in the matrix cells
# A value of 0 in the cell indicates that there is no edge
#
#######################################################################
class AdjacencyMatrixGraph(Graph):
    # "AdjacencyMatrixGraph" inherits from the "Graph" abstract class
    def __init__(self, numVertices, directed=False):
        # and pass the super class initialization
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        # cuz we wanna create a data structure in the form of matrix,
        # for our graph. we create and assign it as "matrix" variable
        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        # check validation of entities
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            # of course i assume that the default weight of an edge will be one
            # it can overloaded with sub method call absolutely !
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] = weight
        if self.directed == False:
            self.matrix[v2][v1] = weight
        # return a list consist of adjacent vertices

    def get_adjacent_vertices(self, v):
        # check validation
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices
    # return all edges that connected to a node
    def get_indegree(self, v):
        # check vortex validation as usual
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)
        # primitive assignment
        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1

        return indegree

    # return weight of an edge, simple af !
    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]
    # and print out all
    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


#######################################################################

# Test Area
# with an example we can examine how Graph class correctly works,
# with testing the "AdjacencySetGraph" class
# for testing the "AdjacencyMatrixGraph" class,
# simply change the "g" object instantiation

#######################################################################

print("*" * 54)
print("THIS IS THE TEST RESULT OF SOME HYPOTHETICAL EXAMPLE !")
print("*" * 54)

# declaring the example

g = AdjacencySetGraph(4)
# if we wanna instantiate a directed graph we can do this:
# g = AdjacencySetGraph(4, directed = True)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

print("*" * 54)
print("which neighbors does every node have?")
print("*" * 54)

for i in range(4):
    print("{0} is Adjacent to: {1}".format(i, g.get_adjacent_vertices(i)))

print("*" * 54)
print("How many edges connected to every node?")
print("*" * 54)

for i in range(4):
    print("In_degree: ", i, g.get_indegree(i))

print("*" * 54)
print("how much is the weight of every edge in our graph?")
print("*" * 54)

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

# and finally display the node relationships !
# to find out how graph looks
g.display()

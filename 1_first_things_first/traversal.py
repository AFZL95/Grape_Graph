from queue import Queue
from graph import *

#######################################################################

# breadth_first traversal needs a graph and a node for start to traverse
# let's set the starting point in the first node of the graph
# it also works with directed graphs. How? ,
# by instantiating the graph with True directed parameter!

#######################################################################

def breadth_first(graph, start=0):
	# instatiating the queue data structure 
	# and add our graph's first node to it
	queue = Queue()
	queue.put(start)
	# create a variable to keep track all of vertices that visited (e.g traversed)
	# it ensures us to do not visit a node more than once in a traverse
	visited = np.zeros(graph.numVertices)

	while not queue.empty():
		vertex = queue.get()

		# if the node that we just accesed in the queue,
		# has already visited before, then we simply do nothing!
		if visited[vertex] == 1:
			continue
		# print the node that we just visited
		print("Visit: ", vertex)
		# and add it to the list of visited vertices
		# setting visited[i] to one to indicate that,
		# this node has been visited
		visited[vertex] = 1

		# after traversing some node, we need to access all it's neighbors !
		for v in graph.get_adjacent_vertices(vertex):
			# if they are haven't been visited ...
			if visited[v] != 1:
				# so visit them !
				# Sele E Rahem xD
				queue.put(v)


# using a recursive algorithm
def depth_first(graph, visited, current=0):
	# if the node that we just accesed in the queue,
	# has already visited before, then we simply do nothing!
	if visited[current] == 1:
		return
	# setting visited[i] to one to indicate that,
	# this node has been visited
	visited[current] = 1
	# print the node that we just visited
	print("Visit: ", current)
	# after traversing some node, we need to access all it's childs !
	for vertex in graph.get_adjacent_vertices(current):
		depth_first(graph, visited, vertex)	



#######################################################################

# Test Area
# with an example we can examine how breadth_first and
# depth_first traversal works,
# with instantiating the "AdjacencyMatrixGraph" class
# for testing the "depth_first" function,
# simply change the traversal method call !

#######################################################################


g = AdjacencyMatrixGraph(9)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

breadth_first(g, 2)

# testing the depth_first algorithm 
# depth_first needs a visited parameter,
# so we create a empty one!
visited = np.zeros(g.numVertices)
depth_first(g, visited)

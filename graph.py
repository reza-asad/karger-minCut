# Reza Asad
# Basic graph
# Jan 28th, 2016
######################### Algorithms ######################
import random

class graph():
	def __init__(self, data):
		self.graph = data
		self.edge_list = []
		for key, values in self.graph.iteritems():
			for value in values:
				if key < value :
					self.edge_list.append((key,value))
	
	# input: a node that currently does not exits in the 
	# graph.
	def add_node(self, node):
		if node in self.graph:
			print "{} already exists".format(node)
		else:
			self.graph[node] = {}
	
	# input: a pair of nodes from the list of existing
	# nodes.
	def add_edge(self,v,w):
		if v in self.graph and w in self.graph:
			if w in self.graph[v]:
				self.graph[v][w] += 1
				self.graph[w][v] += 1
			else:
				self.graph[v][w] = 1
				self.graph[w][v] = 1
			# update edge_list
			if v < w:
				self.edge_list.append((v,w))
			else:
				self.edge_list.append((w,v))
		else:
			print "At leat one of the nodes in {} does not exist".format((v,w))

	# input: an exisiting node
	def drop_node(self, node):
		if node not in self.graph:
			print "node {} does not exist".format(node)
		else:
			for adjacent_node in self.graph[node]:
				del self.graph[adjacent_node][node]
				if node < adjacent_node:
					self.edge_list = filter(lambda x: x != (node, adjacent_node), self.edge_list)
				else:
					self.edge_list = filter(lambda x: x != (adjacent_node, node), self.edge_list)
			del self.graph[node]

	# input: an existing edge
	def drop_edge(self, edge):
		if edge not in self.edge_list:
			print "edge {} does not exist".format(edge)
		else:
			self.edge_list = filter(lambda x: x != edge, self.edge_list)
			node1 = edge[0]
			node2 = edge[1]
			del self.graph[node1][node2]
			del self.graph[node2][node1]

	def pick_random_edge(self):
		return random.choice(self.edge_list)
######################## Main ###############################
# data 
data = {1:{2:1,3:1}, 2:{1:1,4:2}, 3: {1:1}, 4: {2:2}}
g = graph(data)
g.add_edge(3,2)
g.add_edge(3,2)
g.add_node(9)
#g.drop_node(2)
g.drop_edge((2,3))
print g.edge_list
# Reza Asad
# Basic graph
# Jan 28th, 2016
#########################Algorithms######################
import random

class graph():
	def __init__(self, data):
		self.graph = data
		self.edge_list = []
		for key, values in self.graph.iteritems():
			for value in values:
				if key < value:
					self.edge_list.append({key,value})
	
	# input: a node that currently does not exits in the 
	# graph.
	def add_node(self, node):
		if node in self.graph:
			print "{} already exists".format(node)
		else:
			self.graph[node] = set()
	
	# input: a pair of nodes from the list of existing
	# nodes.
	def add_edge(self,v,w):
		if v in self.graph and w in self.graph:
			self.graph[v].add(w)
			self.graph[w].add(v)
			# update edge_list
			self.edge_list.append({v,w})
		else:
			print "At leat one of the nodes in {} does not exist".format((v,w))

	# input: an exisiting node
	def drop_node(self, node):
		if node not in self.graph:
			print "node {} does not exist".format(node)
		else:
			for adjacent_node in self.graph[node]:
				self.graph[adjacent_node].remove(node)
				self.edge_list.remove({node,adjacent_node})
			del self.graph[node]

	# input: an existing edge
	def drop_edge(self, edge):
		if edge not in self.edge_list:
			print "edge {} does not exist".format(edge)
		else:
			self.edge_list.remove(edge)
			node1 = edge.pop()
			node2 = edge.pop()
			self.graph[node1].remove(node2)
			self.graph[node2].remove(node1)

########################Main###############################
# data 
data = {1:{2,3}, 2:{1,4}, 3: {1}, 4: {2}}
g = graph(data)
g.add_node(9)
g.add_edge(3,9)
g.drop_node(1)
g.add_node(3)
g.drop_edge({3,9})
print g.edge_list
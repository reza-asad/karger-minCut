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
			print 'The node already exists'
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
			print "At leat one of the nodes does not exist"

	# input: an exisiting node
	def drop_node(self, node):
		if node not in self.graph:
			print "The node does not exist"
		else:
			#for n in self.graph[node]:

			del self.graph[node]

########################Main###############################
# data 
data = {1:{2,3}, 2:{1,4}, 3: {1}, 4: {2}}
g = graph(data)
g.add_node(9)
g.add_edge(3,9)
#g.drop_node(9)
print g.edge_list
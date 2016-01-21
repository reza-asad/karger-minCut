# Reza Asad
# Karger Algorithm to find the min cut of a graph
# Jan 28th, 2016
#########################Algorithms######################
class graph():
	def __init__(self, data):
		self.graph = data
	
	# input: a node that currently does not exits in the 
	# graph.
	def add_node(self, node):
		if node in self.graph:
			print 'The node already exists'
		else:
			self.graph[node] = []
	
	# input: a pair of nodes from the list of existing
	# nodes.
	def add_edge(self,v,w):
		if v in self.graph and w in self.graph:
			self.graph[v].append(w)
			self.graph[w].append(v)
		else:
			print "At leat one of the nodes does not exist"

########################Main###############################
# data 
data = {1:[2,3], 2:[1,4], 3:[], 4:[]}
g = graph(data)
g.add_node(9)
g.add_edge(3,9)
print g.graph
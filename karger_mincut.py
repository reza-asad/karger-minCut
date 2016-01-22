# Reza Asad
# Basic graph
# Jan 28th, 2016
######################### Algorithms ######################
import random
from graph import graph

class mincut_problem(graph):
	# This is the edge contraction part of the algorithm
	def contract_edge(self, edge):
		node1 = edge[0]
		node2 = edge[1]
		node1_adjacent = self.graph[node1]
		self.drop_node(node1)
		if node2 in node1_adjacent:
			del node1_adjacent[node2]
		for node in node1_adjacent:
			self.add_edge(node, node2)


	# This computes the minimum cut of a graph
	def compute_mincut(self):
		num_vertices = len(data)
		while num_vertices > 2:
			random_edge = self.pick_random_edge()
			self.contract_edge(random_edge)
			num_vertices -= 1
		return len(self.edge_list)



######################## Main ###############################
# data 
data = {1:{2:1,4:1}, 2:{1:1,4:1, 3:1}, 3: {2:1, 4:1}, 4: {1:1, 2:1, 3:1}}

g = mincut_problem(data)
print g.compute_mincut()
# Reza Asad
# Basic graph
# Jan 28th, 2016
######################### Algorithms ######################
import random
from graph import graph

class mincut_problem(graph):
	# This is the edge contraction part of the algorithm
	def contract_edge(self):
		pass

	# This computes the minimum cut of a graph
	def compute_mincut(self):
		num_vertices = len(data)
		while num_vertices > 2:
			random_edge = self.pick_random_edge()
			self.contract_edge()
			num_vertices -= 1
		return len(self.edge_list)



######################## Main ###############################
# data 
data = {1:{2,3}, 2:{1,4}, 3: {1}, 4: {2}}

g = mincut_problem(data)
print g.compute_mincut()
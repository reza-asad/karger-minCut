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
			node1_adjacent.remove(node2)
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
# Lets run this for some numbe rof trials
num_trials = 20
count = 0
for i in range(num_trials):
	data = {1:{2,4}, 2:{1, 4, 3}, 3: {2, 4}, 4: {1, 2, 3}}
	g = mincut_problem(data)
	if g.compute_mincut() == 2:
		count += 1
print float(count)/num_trials
# Reza Asad
# Basic graph
# Jan 28th, 2016
######################### Algorithms ######################
import random
from graph import graph

class mincut_problem(graph):
	def compute_mincut(self):
		pass


######################## Main ###############################
# data 
data = {1:{2,3}, 2:{1,4}, 3: {1}, 4: {2}}

g = mincut_problem(data)

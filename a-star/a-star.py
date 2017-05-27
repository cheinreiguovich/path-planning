# A* algorithm

import numpy as np

def neighbors(node):
	all_dir = [[1,0],[0,1],[-1,0],[0,-1]]
	result = []
	for dir in all_dir:
		neighbor = [node[0]+dir[0],node[1]+dir[1]]
		if neighbor in all_nodes:
			result.append(neighbor)
	return result

if __name__ == "__main__":
	dim_x, dim_y = 10, 10
	all_nodes = []
	for x in range(dim_x):
		for y in range(dim_y):
			all_nodes.append([x,y])



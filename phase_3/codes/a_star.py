from __future__ import print_function
import os
import cv2
import copy
import time
import numpy as np
import heapq
import matplotlib.pyplot as plt
import pickle

import sys
sys.dont_write_bytecode = True

import actions
import obstacles
import node
import utils
import visualization as viz
import univ


# robot_radius = 1
# wheel_distance = 1

GOAL_REACH_THRESH = 0.3

##
## Gets the A-Star path.
## In this algorithm, the heuristic cost from
## current node to goal node is not considered.
##
## :param      input_map:  The input map
## :type       input_map:  { type_description }
##
def aStar(start_pos, goal_pos, robot_radius, clearance, rpm1, rpm2, starting_theta, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30):

	start_r, start_c = start_pos
	goal_r, goal_c = goal_pos

	start_node = node.Node(current_coords=(start_r, start_c), parent_coords=None, orientation=starting_theta, parent_orientation=None, movement_cost=0, goal_cost=utils.euclideanDistance(start_pos, goal_pos))
	# start_node.printNode()

	# print(start_node.goal_cost)
	goal_node = node.Node(current_coords=(goal_r, goal_c), parent_coords=None, orientation=None, parent_orientation=None, movement_cost=None, goal_cost=0)

	# print(goal_node.goal_cost)

	# Saving a tuple with total cost and the state node
	minheap = [((start_node.movement_cost + start_node.goal_cost), start_node)]
	heapq.heapify(minheap)

	# defining the visited node like this avoids checking if two nodes are duplicate. because there is only 1 position to store the visited information for all the nodes that lie within this area.
	# redefine valRound function to be more general. Right now the duplicate_step and duplicate_theta values are 0.5 and 30
	visited = {}
	visited[(utils.valRound(start_r), utils.valRound(start_c), starting_theta)] = start_node 	# marking the start node as visited

	viz_visited_coords = [start_node]
	# print(visited)

	node_count = 0
	while len(minheap) > 0:
		# print("len(minheap):", len(minheap))
		_, curr_node = heapq.heappop(minheap)
		# print(curr_node.goal_cost)
		# if curr_node.isDuplicate(goal_node):	
		
		# print("curr_node:---")
		# curr_node.printNode()
		# print("----------------------")
		if curr_node.goal_cost < (GOAL_REACH_THRESH):
		# if if(((curr_node.current_coords[0] - ())**2 + (y - (0))**2 - (1+radius+clearance)**2) <= 0) :
			print("Reached Goal!")
			print("Current node:---")
			curr_node.printNode()
			print("Goal node:---")
			goal_node.printNode()

			# backtrack to get the path
			path = actions.backtrack(curr_node, visited)
			# path = None 	# FOR NOW FOR DEBUGGING PURPOSES
			print("path length:", len(path))
			print("viz_nodes", len(viz_visited_coords))
			return (path, viz_visited_coords)

		# for row_step, col_step in movement_steps:
		# for angle in range(-60, 61, theta):
		action_set = [[0,rpm1], [rpm1,0],
				[0,rpm2], [rpm2,0],
				[rpm1,rpm2], [rpm2,rpm1],
				[rpm1,rpm1], [rpm2,rpm2]]
		# action_set = [[rpm1, rpm2]]
		i = 0
		for action in action_set:
			# Action Move
			# print("=========" + str(i) + "========")
			i +=1
			next_node = actions.actionMoveNew(current_node=curr_node, next_action=action, goal_position=goal_node.current_coords)
			if next_node is not None:
				# if hit an obstacle, ignore this movement
				if obstacles.withinObstacleSpace((next_node.current_coords[1], next_node.current_coords[0]), robot_radius, clearance):
					# print("skipping loop .....................................................")
					continue

				# Check if the current node has already been visited.
				# If it has, then see if the current path is better than the previous one
				# based on the total cost = movement cost + goal cost

				node_state = (utils.valRound(next_node.current_coords[0]), utils.valRound(next_node.current_coords[1]), next_node.orientation)
				
				if node_state in visited:
					# if current cost is a better cost
					if (next_node < visited[node_state]):
						visited[node_state].current_coords = next_node.current_coords
						visited[node_state].parent_coords = next_node.parent_coords
						visited[node_state].orientation = next_node.orientation
						visited[node_state].parent_orientation = next_node.parent_orientation
						visited[node_state].movement_cost = next_node.movement_cost
						visited[node_state].goal_cost = next_node.goal_cost

						h_idx = utils.findInHeap(next_node, minheap)
						if (h_idx > -1):
							minheap[h_idx] = ((next_node.movement_cost + next_node.goal_cost), next_node)
				else:
					# visited.append(next_node)
					# print("New node added! count:", node_count)
					# node_count += 1
					visited[node_state] = next_node
					heapq.heappush(minheap, ((next_node.movement_cost + next_node.goal_cost), next_node))

					viz_visited_coords.append(next_node)
			# else:
			# 	print("Oops... Node is None!!")

		heapq.heapify(minheap)
	print("outside while")


def testMain():
	# path, viz_nodes = aStar(start_pos=(5,5), goal_pos=(50,50), robot_radius=0, clearance=0, step_size=5, theta=30, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30)

	goal_pos = (4,4)
	goal_node = node.Node(current_coords=goal_pos, parent_coords=None, orientation=None, parent_orientation=None, movement_cost=None, goal_cost=0)

	start_time = time.clock()
	path, viz_nodes = aStar(start_pos=(-4,-4), goal_pos=goal_pos, robot_radius=0.177, clearance=0.2, rpm1=25, rpm2=30, starting_theta=20, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30)
	
	# np.save("path_25_35_01.npy", path)
	# np.save("viz_nodes_25_35_01.npy", viz_nodes)
	print("Time to run A*:", time.clock() - start_time, "seconds")

	# univ.function(viz_nodes, path, goal_node)
	# univ.plotExplorationNodesAndFinalPath(viz_nodes, path, goal_node)
	univ.plotFinalPath(path_node_vector=path, goal_node=goal_node)


if __name__ == '__main__':
	testMain()
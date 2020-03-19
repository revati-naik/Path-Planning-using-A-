import os
import cv2
import copy
import numpy as np
import heapq

import sys
sys.dont_write_bytecode = True

import actions
import obstacles
import node
import utils


##
## Gets the dijkstra path.
## In this algorithm, the heuristic cost from
## current node to goal node is not considered.
##
## :param      input_map:  The input map
## :type       input_map:  { type_description }
##
def getAStarPath(start_pos, goal_pos, robot_radius, clearance, step_size, theta=30):

	# start_r, start_c = 10, 10
	# goal_r, goal_c = 30,10
	start_r, start_c = start_pos
	goal_r, goal_c = goal_pos

	
	goal_cost = utils.heuristic_cost(start_pos, goal_pos)
	
	# 
	# start_node = node.Node((start_r, start_c), None, 0, goal_cost)
	# goal_node = node.Node((goal_r, goal_c), None, -1, 0)
	start_node = node.Node(current_coords=(start_r, start_c), parent_coords=None, orientation=0, movement_cost=0, goal_cost=utils.heuristic_cost(start_pos, goal_pos))
	goal_node = node.Node(current_coords=(goal_r, goal_c), parent_coords=None, orientation=None, movement_cost=None, goal_cost=0)


	# Saving a tuple with total cost and the state node
	minheap = [((start_node.movement_cost + start_node.goal_cost), start_node)]
	heapq.heapify(minheap)

	# dictionary of all the visited nodes
	visited_nodes = {}
	# visited_nodes[start_node.current_coords] = start_node

	# Adding start node to visited list
	visited_nodes[(round(start_r), round(start_c), 0)] = start_node


	# movement_steps = [[-1, -1],
	# 				  [-1,  0],
	# 				  [-1, +1],
	# 				  [ 0, -1],
	# 				  [ 0, +1],
	# 				  [+1, -1],
	# 				  [+1,  0],
	# 				  [+1, +1]]

	viz_visited_coords = []


	while len(minheap) > 0:
		_, curr_node = heapq.heappop(minheap)

		if curr_node.isDuplicate(goal_node):
			print("Reached Goal!")
			# backtrack to get the path
			print("backtracking")
			path = utils.backtrack(curr_node, visited_nodes)

			return (path, viz_visited_coords)

		for angle in range(0, 360, theta):
			# Action Move
			next_node = actions.actionMove(current_node=curr_node, theta_step=angle, linear_step=step_size, goal_position=goal_node.current_coords)
			
			if next_node is not None:
				# if hit an obstacle, ignore this movement
				# if input_map[next_node.current_coords] != 0:
				# 	continue
				if hittingObstacle(next_node):
					continue

				# Check if the current node has already been visited.
				# If it has, then see if the current path is better than the previous one
				# based on the total cost = movement cost + goal cost
				node_state = (round(next_node.current_coords[0]), round(next_node.current_coords[1]), round(next_node.orientation + angle))
				if node_state in visited_nodes:
					if (next_node.movement_cost + next_node.goal_cost) < (visited[node_state].movement_cost + visited[node_state].goal_cost):
						visited_nodes[node_state].movement_cost = next_node.movement_cost
						visited_nodes[node_state].goal_cost = next_node.goal_cost
						visited_nodes[node_state].parent_coords = next_node.parent_coords
						visited_nodes[node_state].orientation = next_node.orientation

						h_idx = utils.findInHeap(next_node, minheap)
						if (h_idx > -1):
							minheap[h_idx] = ((next_node.movement_cost + next_node.goal_cost), next_node)
				else:
					# visited_nodes.append(next_node)
					visited_nodes[node_state] = next_node
					heapq.heappush(minheap, ((next_node.movement_cost + next_node.goal_cost), next_node))

					viz_visited_coords.append(next_node)
					# if visualize:
					# 	utils.drawOnMap(viz_map, next_node.current_coords, visualize=visualize)

		heapq.heapify(minheap)


# Test AStar
def testMain():
	path = getAStarPath(start_pos=(1,1), goal_pos=(10,10), robot_radius=0, clearance=0, step_size=1, theta=30)


if __name__ == '__main__':
	testMain()
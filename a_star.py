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
def aStar(start_pos, goal_pos, robot_radius, clearance, step_size, theta=30, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30):

	start_r, start_c = start_pos
	goal_r, goal_c = goal_pos

	start_node = node.Node(current_coords=(start_r, start_c), parent_coords=None, orientation=0, parent_orientation=None, movement_cost=0, goal_cost=utils.euclideanDistance(start_pos, goal_pos))
	goal_node = node.Node(current_coords=(goal_r, goal_c), parent_coords=None, orientation=None, parent_orientation=None, movement_cost=None, goal_cost=0)

	# check if the start node lies withing the map and not on obstacles
	if (start_node.current_coords[0] < actions.MIN_COORDS[1]) or (start_node.current_coords[0] >= actions.MAX_COORDS[1]) or (start_node.current_coords[1] < actions.MIN_COORDS[0]) or (start_node.current_coords[1] >= actions.MAX_COORDS[0]) or obstacles.withinObstacleSpace((start_node.current_coords[1], start_node.current_coords[0]), robot_radius, clearance):
		print("ERROR: Invalid start node. It either lies outside the map boundary or within the obstacle region.")
		sys.exit(0)

	# check if the goal node lies withing the map and not on obstacles
	if (goal_node.current_coords[0] < actions.MIN_COORDS[1]) or (goal_node.current_coords[0] >= actions.MAX_COORDS[1]) or (goal_node.current_coords[1] < actions.MIN_COORDS[0]) or (goal_node.current_coords[1] >= actions.MAX_COORDS[0]) or obstacles.withinObstacleSpace((goal_node.current_coords[1], goal_node.current_coords[0]), robot_radius, clearance):
		print("ERROR: Invalid goal node. It either lies outside the map boundary or within the obstacle region.")
		sys.exit(0)

	# check is step size lies between 0 and 10
	if step_size < 1 or step_size > 10:
		print("ERROR: Invalid step_size. It must lie within 1 and 10.")
		sys.exit(0)

	# Saving a tuple with total cost and the state node
	minheap = [((start_node.movement_cost + start_node.goal_cost), start_node)]
	heapq.heapify(minheap)

	# defining the visited node like this avoids checking if two nodes are duplicate. because there is only 1 position to store the visited information for all the nodes that lie within this area.
	visited = {}
	visited[(round(start_r), round(start_c), 0)] = start_node 	# marking the start node as visited

	viz_visited_coords = [start_node]

	
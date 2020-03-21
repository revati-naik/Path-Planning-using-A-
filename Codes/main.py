import os
import cv2
import copy
import numpy as np
import heapq
import time

import sys
sys.dont_write_bytecode = True

import actions
import obstacles
import node
import utils



##
## Computes the path from the starting node to the goal node
##
## :param      start_node:    The start node (Xs,Ys,Theta_s)
## :type       start_node:    A tuple of starting coordinates and orientation
## :param      goal_node:     The goal node (Xs,Ys,Theta_g)
## :type       goal_node:     A tuple of the GOAL coordinates and orientation
## :param      robot_radius:  Radius of the circular robot
## :type       robot_radius:  float
## :param      clearance:     Clearance gap between the robot and the obstacle
## :type       clearance:     float
## :param      step_size:     The atomic linear movement step size
## :type       step_size:     float
## :param      theta:         The atomic angular movement in terms of theta in degrees
## :type       theta:         float
##
def aStar(start_node, goal_node, robot_radius, clearance, step_size, theta=30):
	# # check if the start node lies withing the map and not on obstacles
	# if (start_node.current_coords[0] < actions.MIN_COORDS[1]) or (start_node.current_coords[0] >= actions.MAX_COORDS[1]) or (start_node.current_coords[1] < actions.MIN_COORDS[0]) or (start_node.current_coords[1] >= actions.MAX_COORDS[0]) or hittingObstacle(start_node):
	# 	print("ERROR: Invalid start node. It either lies outside the map boundary or within the obstacle region.")
	# 	sys.exit(0)

	# # check if the goal node lies withing the map and not on obstacles
	# if (goal_node.current_coords[0] < actions.MIN_COORDS[1]) or (goal_node.current_coords[0] >= actions.MAX_COORDS[1]) or (goal_node.current_coords[1] < actions.MIN_COORDS[0]) or (goal_node.current_coords[1] >= actions.MAX_COORDS[0]) or hittingObstacle(goal_node):
	# 	print("ERROR: Invalid goal node. It either lies outside the map boundary or within the obstacle region.")
	# 	sys.exit(0)

	# # check is step size lies between 0 and 10
	# if step_size < 1 or step_size > 10:
	# 	print("ERROR: Invalid step_size. It must lie within 1 and 10.")
	# 	sys.exit(0)


	radius = int(input("Enter the robot radius: "))
	clearance = int(input("Enter the clearance: "))

	input_map = obstacles.getMap(radius=(radius + clearance), visualize=False)
	orign_map = obstacles.getMap(radius=0, visualize=False)

	# User input for the start state
	start_c, start_r = map(int, raw_input("Enter starting coordinates (x y): ").split())
	start_r = input_map.shape[0] - start_r
	if (start_r < 0 or start_c < 0 or start_r >= input_map.shape[0] or start_c >= input_map.shape[1] or obstacles.insideObstacle(start_r, start_c, radius=(radius + clearance))):
		print("ERROR: This start state is invalid for the given robot size and clearance distance. Possible issues can be that the start position lies outside the map region or within the obstacle. Please try a different starting position.")
		return 

	# User input for goal state
	goal_c, goal_r = map(int, raw_input("Enter goal coordinates (x y): ").split())
	goal_r = input_map.shape[0] - goal_r
	if (goal_r < 0 or goal_c < 0 or goal_r >= input_map.shape[0] or goal_c >= input_map.shape[1] or obstacles.insideObstacle(goal_r, goal_c, radius=(radius + clearance))):
		print("ERROR: This goal state is unreachable for the given robot rize and clearance distance. Possible issues can be that the goal position lies outside the map region or within the obstacle. Please try a different goal position.")
		return 


	# write code to find the actual path using a star
	path, viz_nodes = aStar(start_pos=(start_r,start_c), goal_pos=(goal_r,goal_c), robot_radius=radius, clearance=clearance, step_size=5, theta=30, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30)

	# visualize path
	univ.function(viz_nodes, path)



def main():
	pass


if __name__ == '__main__':
	main()

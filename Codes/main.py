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
def main():
	radius = int(input("Enter the robot radius: "))
	clearance = int(input("Enter the clearance: "))

	# User input for the start state
	start_c, start_r = map(int, raw_input("Enter starting coordinates (x y): ").split())

	# User input for goal state
	goal_c, goal_r = map(int, raw_input("Enter goal coordinates (x y): ").split())

	# write code to find the actual path using a star
	path, viz_nodes = aStar(start_pos=(start_r,start_c), goal_pos=(goal_r,goal_c), robot_radius=radius, clearance=clearance, step_size=5, theta=30, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30)

	# visualize path
	univ.function(viz_nodes, path)


if __name__ == '__main__':
	main()

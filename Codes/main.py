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



def main():

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
	start_time = time.clock()
	path, viz_nodes = aStar(start_pos=(start_r,start_c), goal_pos=(goal_r,goal_c), robot_radius=radius, clearance=clearance, step_size=5, theta=30, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30)
	print "Time to run A*:", time.clock() - start_time, "seconds"


if __name__ == '__main__':
	main()

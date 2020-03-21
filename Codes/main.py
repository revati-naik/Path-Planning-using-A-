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
import a_star
import univ


def main():


	# User input for the start state
	start_c, start_r, start_orient = map(float, raw_input("Enter starting coordinates (x y) and orientation: ").split())
	# User input for goal state
	goal_c, goal_r = map(float, raw_input("Enter goal coordinates (x y): ").split())
	

	radius = float(input("Enter the robot radius: "))
	clearance = float(input("Enter the clearance: "))
	step_size = float(input("Enter the robot step_size: "))

	# write code to find the actual path using a star
	start_time = time.clock()
	path, viz_nodes = a_star.aStar(start_pos=(start_r,start_c), goal_pos=(goal_r,goal_c), robot_radius=radius, clearance=clearance, step_size=step_size, theta=30, duplicate_step_thresh=0.5, duplicate_orientation_thresh=30)
	print "Time to run A*:", time.clock() - start_time, "seconds"

	# visualize path
	univ.function(viz_nodes, path)


if __name__ == '__main__':
	main()

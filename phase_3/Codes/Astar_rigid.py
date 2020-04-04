import os
import cv2
import copy
import numpy as np
import heapq
import time
import matplotlib.pyplot as plt

import sys
sys.dont_write_bytecode = True

import a_star
import actions_new 
import obstacles
import node
import utils
import visualization as viz


THETA_BIN_SIZE = 30
GOAL_REACH_THRESH = 0.2 	# units in meters

# Robot radius for TurtleBot3
ROBOT_RADIUS = 0.105	
OBSTACLE_CLEARANCE = 0.2

def main():


	# User input for the start state
	start_c, start_r, theta = map(float, raw_input("Enter starting coordinates (x y) and orientation: ").split())
	start_rc = (start_r, start_c)
	# User input for goal state
	goal_c, goal_r = map(float, raw_input("Enter goal coordinates (x y): ").split())
	goal_rc = (goal_r, goal_c)

	clearance = float(input("Enter the clearance: "))

	# check if the start node lies withing the map and not on obstacles
	if (start_r < actions_new.MIN_COORDS[1]) or (start_r >= actions_new.MAX_COORDS[1]) or (start_c < actions_new.MIN_COORDS[0]) or (start_c >= actions_new.MAX_COORDS[0]) or obstacles.withinObstacleSpace((start_c, start_r), ROBOT_RADIUS, clearance):
		print("ERROR: Invalid start node. It either lies outside the map boundary or within the obstacle region.")
		sys.exit(0)

	# check if the goal node lies withing the map and not on obstacles
	if (goal_r < actions_new.MIN_COORDS[1]) or (goal_r >= actions_new.MAX_COORDS[1]) or (goal_c < actions_new.MIN_COORDS[0]) or (goal_c >= actions_new.MAX_COORDS[0]) or obstacles.withinObstacleSpace((goal_c, goal_r), ROBOT_RADIUS, clearance):
		print("ERROR: Invalid goal node. It either lies outside the map boundary or within the obstacle region.")
		sys.exit(0)


	# write code to find the actual path using a star
	start_time = time.clock()
	path, visited_viz_nodes = a_star.a_star(start_rc=start_rc, goal_rc=goal_rc, orientation=theta, rpm1=10, rpm2=20, clearance=clearance, viz_please=False)
	print "Time to run A*:", time.clock() - start_time, "seconds"
	print("Number of visited nodes:", len(visited_viz_nodes))
	print("Number of nodes in path:", len(path))

	plotter = viz.initPlot(start_rc[::-1], goal_rc[::-1], title="Final Plotting")
	
	plt.ion()
	i = 2
	# i = viz.plotPath(path=visited_viz_nodes, rev=False, pause_time=0.001, plotter=plotter, color="blue", linewidth=1, write_path_prefix=-1, show=False, skip_frames=25)
	i = viz.plotPath(path=path, rev=True, pause_time=0.001, plotter=plotter, color="lime", linewidth=4, write_path_prefix=-1, show=False, skip_frames=1)
	plt.ioff()
	print("Done with plots.")
	plt.show()



if __name__ == '__main__':
	main()

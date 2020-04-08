from __future__ import print_function
import sys
import numpy as np

import node
import utils
import math


# input_map_dummy = np.zeros((200, 300))

# stored in the (x,y) format
MIN_COORDS = (-5, -5)
MAX_COORDS = (5, 5)

UNIT_STEP = 0.1

# rpm1 = 10
# rpm2 = 20



##
## Move from the current coordinates Node to the next valid movement.
## The values of row_step and col_step specify the direction of movement 
## from one of the 8 directions. Use of the row_step and col_step parameters
## takes away the need to specify 8 different functions for all the different movements.
##
## :param      data:           The current coordinates
## :type       data:           Node
## :param      row_step:       The row step
## :type       row_step:       int
## :param      col_step:       The col step
## :type       col_step:       int
## :param      goal_position:  The goal position. Used only for A_star, not for dijkstra.
## :type       goal_position:  (row, col)
##
## :returns:   Node for the new position in case of valid movement, None otherwise
## :rtype:     Node
##
# def actionMove(current_node, theta_step, linear_step, goal_position=None):
def actionMove(current_node, next_action, theta, goal_position):
	
	# 8 connected action set
	# print(current_node.current_coords)
	# sys.exit(0)
	u_r = next_action[0]
	u_l = next_action[1]
	t = 0
	mc = 0
	gc = 0
	dt = 0.1
	r = 0.038
	l = 0.354
	# x = current_node.current_coords[0]
	# dx = current_node.current_coords[0]
	dx = current_node[0]
	dy = current_node[1]
	# y = current_node.current_coords[1]
	# dy = current_node.current_coords[1]
	# dtheta = current_node.orientation
	dtheta = theta
	theta = math.radians(dtheta)
	while t < UNIT_STEP:
		t = t + dt
		x = dx
		y = dy
		dx += (r*(u_r+u_l)*math.cos(theta)/2)*dt
		dy += (r*(u_r+u_l)*math.sin(theta)/2)*dt
		dtheta += ((r/l)*(u_r-u_l))*dt
		mc += utils.euclideanDistance((x,y), (dx,dy))
		# print(mc)

		print("Final node", (dx, dy))
		print("Orientation", math.degrees(dtheta))
	cc = (dx, dy)
	# pc = current_node.current_coords
	# print("cc", cc)
	# print("pc", pc)
	# print("theta", dtheta)
	ori = math.degrees(dtheta)
	# pori = current_node.orientation

	# # cost to reach parent node + latest travel from parent node to current node 
	# mc = current_node.movement_cost + step_size
	# # calculate goal cost between current node to goal node
	gc = utils.euclideanDistance(cc, goal_position)
	# print("gc", gc)
	
	if (cc[0] < MIN_COORDS[0]) or (cc[0] >= MAX_COORDS[0]) or (cc[1] < MIN_COORDS[1]) or (cc[1] >= MAX_COORDS[1]):
		return None 
	 
	# # print("cc",cc)
	# # print("pc",pc)
	# # print("ori",ori)
	# # print("pori", pori)
	# # print("mc", mc)
	# # print("gc", gc)

	# ret_val = node.Node(current_coords=cc, parent_coords=pc, orientation=ori, parent_orientation=pori, movement_cost=mc, goal_cost=gc)
	# print("costs:", ret_val.movement_cost, "+", ret_val.goal_cost, "=", ret_val.movement_cost + ret_val.goal_cost)
	# print(ret_val.goal_cost)
	# print(ret_val.movement_cost)
	# sys.exit()

	# return ret_val









# def actionMove(current_node, next_action, theta, goal_position):
# def actionMoveNew(Xi,Yi,Thetai,UL,UR):
def actionMoveNew(current_node, next_action, goal_position):

	Yi, Xi = current_node.current_coords
	Thetai = current_node.orientation
	mc = current_node.movement_cost
	UL, UR = next_action

	t = 0.0
	r = 0.038
	L = 0.354
	dt = 0.1
	Xn=Xi
	Yn=Yi
	# Thetan = 3.14 * Thetai / 180
	Thetan = math.radians(Thetai)

# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes

	while t < UNIT_STEP:
		t = t + dt
		Xs = Xn
		Ys = Yn
		Xn += r * (UL + UR) * math.cos(Thetan) * dt
		Yn += r * (UL + UR) * math.sin(Thetan) * dt
		Thetan += (r / L) * (UR - UL) * dt
		mc += utils.euclideanDistance((Xs, Ys), (Xn, Yn))
		# plt.plot([Xs, Xn], [Ys, Yn], color="blue")
		# print("Final node", (Xn, Yn))
		# print("Orientation", math.degrees(Thetan))

	# Thetan = 180 * (Thetan) / 3.14
	Thetan = math.degrees(Thetan)

	cc = (Yn, Xn)
	pc = current_node.current_coords
	ori = Thetan
	pori = current_node.orientation
	gc = utils.euclideanDistance(cc, goal_position)

	# print("costs:", mc, "+", gc, "=", mc + gc)
	
	if (cc[0] < MIN_COORDS[0]) or (cc[0] >= MAX_COORDS[0]) or (cc[1] < MIN_COORDS[1]) or (cc[1] >= MAX_COORDS[1]):
		return None 

	ret_val = node.Node(current_coords=cc, parent_coords=pc, orientation=ori, parent_orientation=pori, movement_cost=mc, goal_cost=gc)

	# print("Inside action function..... printing ret_val:", ret_val.printNode())
	return ret_val
	# return Xn, Yn, Thetan




##
## Finds the optimum path from the list of visited nodes 
## by backtracking to the parents of each nodes.
##
## :param      node:           The current node that is the same as the goal node
## :type       node:           Node
## :param      visited_nodes:  The visited nodes dictionary with current coordinates as the key
## :type       visited_nodes:  dictionary
##
## :returns:   List of coordinates that give the path from the start node to end node
## :rtype:     list
##
def backtrack(node, visited_nodes):
	# put the goal node in the path
	path = [node]

	# backtrack all the parent nodes from the list of visited nodes
	temp = visited_nodes[(utils.valRound(node.parent_coords[0]), utils.valRound(node.parent_coords[1]), node.parent_orientation)]

	while temp.parent_coords is not None:
		path.insert(0, temp)
		# print("=====================================BACKTRACKING=============")
		# temp.printNode()
		# print("==================")
		temp = visited_nodes[(utils.valRound(temp.parent_coords[0]), utils.valRound(temp.parent_coords[1]), temp.parent_orientation)]

	# put the start node in the path
	path.insert(0, temp)

	return path


def testMain():
	# start_node = node.Node((1,1), parent_coords=None, movement_cost=0, goal_cost=10)
	# print("--- start_node ---")
	# start_node.printNode()
	
	# new_node = actionMove(current_node=start_node, theta_step=0, linear_step=1)
	# print("--- new_node ---")
	# new_node.printNode()

	# plt.figure("action move check")
	# plotVector.plotVector(start_node.current_coords, directions=[0], steps=[1], vector_colors=["black"])
	# plt.plot(start_node.current_coords[1], start_node.current_coords[0], 'ro')
	# plt.plot(new_node.current_coords[1], new_node.current_coords[0], 'go')
	# plt.show()
	# plt.close()

	# action_set = [[0,rpm1], [rpm1,0],
	# 			[0,rpm2], [rpm2,0],
	# 			[rpm1,rpm2], [rpm2,rpm1],
	# 			[rpm1,rpm1], [rpm2,rpm2]]
	action_set = [[10,20]]
	for action in action_set:
		actionMove((1,1), action, 20, (10,10))

if __name__ == '__main__':
	testMain()

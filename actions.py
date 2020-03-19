import numpy as np

import node
import utils


# input_map_dummy = np.zeros((200, 300))

# stored in the (x,y) format
MIN_COORDS = (0, 0)
MAX_COORDS = (300, 200)
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
def actionMove(current_node, theta_step, linear_step, goal_position=None):
	# move as per the given direction and linear_step
	# check if the new position lies within the defined map 
	# check if the new position is valid and does not collide with an obstacle
	xf = current_node.current_coords[1] + np.array(linear_step * np.cos((current_node.orientation + theta_step) * np.pi/180))
	yf = current_node.current_coords[0] + np.array(linear_step * np.sin((current_node.orientation + theta_step) * np.pi/180))

	if (xf < MIN_COORDS[0]) or (xf >= MAX_COORDS[0]) or (yf < MIN_COORDS[1]) or (yf >= MAX_COORDS[1]):
		return None

	current_coords = (yf, xf)
	parent_coords = current_node.current_coords
	movement_cost = current_node.movement_cost + linear_step
	if goal_position is None:
		goal_cost = None
	else:
		goal_cost = utils.heuristic_cost(current_coords, goal_position)

	ret_val = node.Node(current_coords, parent_coords, orientation, movement_cost, goal_cost)

	return ret_val

# Testing action set
def testMain():
	start_node = node.Node((1,1), parent_coords=None, movement_cost=0, goal_cost=10)
	print("--- start_node ---")
	start_node.printNode()
	
	new_node = actionMove(current_node=start_node, theta_step=0, linear_step=1)
	print("--- new_node ---")
	new_node.printNode()

	plt.figure("action move check")
	plotVector.plotVector(start_node.current_coords, directions=[0], steps=[1], vector_colors=["black"])
	plt.plot(start_node.current_coords[1], start_node.current_coords[0], 'ro')
	plt.plot(new_node.current_coords[1], new_node.current_coords[0], 'go')
	plt.show()
	plt.close()


if __name__ == '__main__':
	testMain()

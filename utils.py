import os
import cv2
import copy
import numpy as np




##
## Used to round off the coordinate value with a threshold of 0.5
## USed to cjeck for duplicate points
##
## :param      x:    Value to be rounded off
## :type       x:    float
##
## :returns:   The rounded value with 0.5 threshold
## :rtype:     float
##
def valRound(x):
	return (int(x) if x < (int(x)+0.5) else int(x)+0.5)


##
## To find the euclidean distance between two coordinates.
## Used in the A_star algorithm
##
## :param      state1:  coordinate 1
## :type       state1:  (row, col)
## :param      state2:  coordinate 2
## :type       state2:  (row, col)
##
## :returns:   euclidean distance between the two coordinates
## :rtype:     float
##
def euclideanDistance(state1, state2):
	return np.sqrt(((state1[0] - state2[0]) ** 2) + ((state1[1] - state2[1]) ** 2))


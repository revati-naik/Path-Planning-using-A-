import os
import cv2
import copy
import numpy as np




##
## Used to round off the coordinate value with a threshold of 0.5
## USed to cjeck for duplicate points
##
## :param      x:    { parameter_description }
## :type       x:    { type_description }
##
## :returns:   { description_of_the_return_value }
## :rtype:     { return_type_description }
##
def valRound(x):
	return (int(x) if x < (int(x)+0.5) else int(x)+0.5)


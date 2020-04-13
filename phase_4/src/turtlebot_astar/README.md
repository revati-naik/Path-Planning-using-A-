# Path-Planning-using-A_Star - TurtleBot-3 
Implementation of path planning using A* Algorithm with the non-holonomic constraints, to find the shortest path between start and endpoint on turtlebot3.
---


## Overview

Agenda of this simple implementation is the demonstration the working of a path planning algorithm on a simulation environment -- in our case, a turtlebot3.

The launch file invokes the gazebo simulation node, the turtlebot3 node, and the publisher to move the turtlebot.

## Dependencies

This package has been tested in a system with following dependencies.
- Ubuntu 18.04 LTS
- ROS-Melodic
- Gazebo version 9.12.0

## Build Instructions
1) Clone the repository:
```
$ source /opt/ros/kinetic/setup.bash
$ git clone https://github.com/revati-naik/Path-Planning-using-A_Star.git
```

3) Build and source the package:
```
$ cd Path-Planning-using-A_Star/phase_4
$ catkin_make
$ source devel/setup.bash
```

## Run Instructions
1) Launch the `turtlebot_astar.launch`
```
$ roslaunch turtlebot_astar turtlebot_astar.launch
```

This file launches the gazebo environment, turtlebot3 simulation robot, and the publisher to move the robot as per the defined path.
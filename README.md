# Path-Planning-using-A_Star
Implement A* Algorithm to find the shortest path between start and endpoint

# ENPM661_Proj3_Phase2
A* implementation for Point and Rigid Robot

The two main files are A_Star_point.py and A_Star_rigid.py

## Installation
```bash
pip install opencv-contrib-python
pip install numpy
```

## Instructions to run A* for a Point Robot
```python
$ git clone https://github.com/revati-naik/Path-Palnning-using-A_Star.git
$ python codes\A_Star_point.py
```
The user will then be prompted to enter the start and goal positions in the cartesian coordinates.
Once the program finishes, the optimal path to the goal is displayed. Consider the example below.

```
Enter starting coordinates (x y): 5 5 
Enter goal coordinates (x y): 295 195
Reached Goal!
Time to run A*: 4.436329 seconds
```

## Instructions to run A* for a Rigid Robot
```python
$ python codes\A_Star_rigid.py
```
The user will then be prompted to enter the radius of the rigid robot, clearance, the start position, and the goal position in the cartesian coordinates. The clearance and radius are adjusted for by increasing the size of the obstacles. Once the program finishes, the optimal path to the goal is displayed. Consider the example below.
```
Enter the robot radius: 10
Enter the clearance: 2
Enter starting coordinates (x y): 5 5
Enter goal coordinates (x y): 295 195
Reached Goal!
Time to run A*: 3.221574 seconds
```

## Execution time for the Algorithm (Point Robot)
Start position: 5, 5  
Goal position: 295 195  
Total time to run A*: 4.436329 seconds


The file `a_star_point_exploration.mp4` shows the animation for the exploration of the search space.

The file `a_star_point_optimal_path.mp4` shows the animation for the chosen optimal path after the exploration using the A* algorithm.

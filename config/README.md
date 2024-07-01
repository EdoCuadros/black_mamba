# Configuration files
<hr>

## joystick

The code configures the ROS nodes *joy_node* and *teleop_node* to handle joystick input for robot teleoperation. The *joy_node* translates these joystick inputs into linear and angular movements for the robot, with adjustable scales and turbo mode. 

This file is then used in the joystick launch file.

## my_controllers

This file is to configure the ROS *controller_manager* and *diff_cont* for the differential drive. 


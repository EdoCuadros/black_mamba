## Launch Files

Launch files for simulations and teleoperation with DS4.

## Launch simulation

This file launches the robot description and gazebo simulation.

Launch gazebo in world.

#TODO: Agregar comando que se usaría para descripción.

The controllers for the differential drive of the platform, which publish to the /cmd_vel topic, are started.


For keyboard control, it is necessary to run the ROS teleoperation package.

` ros2 run teleop_twist_keyboard teleop_twist_keyboard`

#TODO: Agregar remapeo.

Remapping is required because the package normally publishes to the */cmd_vel* topic, but the *ros2_control* controller subscribes to the */cmd_vel_unstamped* topic. (Topic used by DS4).

## Joystick launch

Similarly, this file launches the nodes for controlling the robot with a DS4 controller connected via cable. The control parameters are taken from the *joystick.yaml* file. After executing the robot description, use the following command.

`ros2 run black_mamba joystick.launch.py`



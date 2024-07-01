# Description

This folder contains the *.xacro* files and meshes for the Roomba and the D435 for simulations.

## Main file

The main file **robot.urdf.xacro** includes the different files for the platform description. There are files for the URDF model of the robot and the camera, as well as for the robot's control.

## Robot Description 

The URDF model of the robot is created, using the Create 2 mesh for the base link, and adding sensors.

## Control for Gazebo

An initial control for Gazebo was created that does not use *ros2_control*. It works for teleoperation with a keyboard and a DualShock4 controller.

The wheel joints, their separation, and their diameter are established.


## Controller with ros2_control

Following the initial ROS controller, a controller using ros2_control was implemented. The maximum and minimum values for each wheel's speed are set, and the interfaces are established. This file is related to my_controllers.

## Depth Camera Description


Description of the RealSense D435* camera using ROS controllers. The Intel packages for using the camera with the robot in Gazebo were not found to be functional, so they were not used from that point on.

*The camera model in Gazebo does not align with the direction the image is pointing. I tried to change the pose, but I couldn't synchronize the image with the visual model.

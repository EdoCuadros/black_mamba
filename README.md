# black_mamba
[![foxy][foxy-badge]][foxy]
[![ubuntu20][ubuntu20-badge]][ubuntu20]
This repository contains the code and resources for designing and developing a mobile robotic platform using 
NVIDIA Jetson Nano and iRobot Create 2. The plataform utilizes the iRobot Create 2, the Nvidia Jetson Nano board, and the Intel RealSense D435 depth camera. The ROS packages in this repository include components for h andling the Create, descriptions and drivers, as  well as integrating the Jetson and ROS. Additionally, it inclued connections to Gazebo, descriptions, worlds, and controllers, and solutions for teleoperated robot control using PS4 controllers. 

[![foxy][foxy-badge]][foxy]
[![ubuntu20][ubuntu20-badge]][ubuntu20]
## Contents

- [Requirements](#requirements)
- [Installation](#Instalation)
    - [Custom Xubuntu Image](#custom-xubuntu-image)
    - [ROS Package](#ros-package)
- [Usage](#usage)
- [Components](#usage)
    - [Create](#create-robot)
    - [Description](#description)


## Requirements

- Hardware: 
    - Nvidia Jetson Nano
    - Intel RealSense D435
    - PS4 Controller

- Software:
    - ROS 2 ([Foxy](https://docs.ros.org/en/foxy/Installation.html)), Gazebo, Rviz, etc...
    - [create_robot packages](https://github.com/AutonomyLab/create_robot.git)
    - [ROS Wrapper and SDK for D435](https://github.com/IntelRealSense/realsense-ros.git)
    
## Instalation

### Custom Xubuntu Image

1. Download image from [this Nvidia Forum](https://forums.developer.nvidia.com/t/xubuntu-20-04-focal-fossa-l4t-r32-3-1-custom-image-for-the-jetson-nano/121768) and burn it in an SD card.

2. Regular install the operating system in the Jetson.

I tried to use latest Nano Jetpack and  docker containers (recommended by Nvidia), but i just found it impossible to run. 


### ROS Package
1. Clone this repository
```
git clone https://github.com/EdoCuadros/black_mamba.git
cd black_mamba
```
2. Install dependencies
```
rosdep install --from-paths src --ignore-src -r -y
```
3. Build the workspace
```
colcon build    # Go to your workspace 
source install/setup.bash   
```

## Usage

Look for [.launch files](launch/README.md).

## Components 

### Create Robot

### Description
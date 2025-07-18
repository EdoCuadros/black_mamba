import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config_arg = DeclareLaunchArgument(
        'config',
        default_value=os.path.join(
            get_package_share_directory('black_mamba'),
            'config',
            'default.yaml'
        ),
        description='Path to the config file for create_driver'
    )

    desc_arg = DeclareLaunchArgument(
        'desc',
        default_value='true',
        description='Whether to launch robot description'
    )

    config = LaunchConfiguration('config')
    desc = LaunchConfiguration('desc')

    # Nodo de create_driver
    create_driver_node = Node(
        package='create_driver',
        executable='create_driver',
        name='create_driver',
        output='screen',
        parameters=[config, {'robot_model': 'CREATE_2'}]
    )

    # Nodo del LIDAR
    lidar_node = Node(
        package='rplidar_ros',
        executable='rplidar_composition',
        name='rplidar',
        output='screen',
        parameters=[{
            'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0-port0',
            'frame_id': 'laser_frame',
            'angle_compensate': True,
            'scan_mode': 'Standard'
        }]
    )

    # Incluir descripción del robot solo si desc == true
    bm_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('bm_description'),
                'launch',
                'bm_description.launch.py'  # Suponiendo que es .launch.py
            )
        ),
        launch_arguments={
            'use_ros2_control': 'false',
            'use_sim_time': 'false'
        }.items()
        condition=IfCondition(desc)
    )

    return LaunchDescription([
        config_arg,
        desc_arg,
        create_driver_node,
        lidar_node,
        bm_description_launch
    ])

# Author: Kevin DeMarco

import os
import yaml
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():
    #rviz_config = os.path.join(get_package_share_directory('dingo_description'),
    #                          'rviz', 'dingo.rviz')
    #
    #xacro_path = os.path.join(get_package_share_directory('dingo_description'),
    #                          'urdf', 'dingo-d.urdf.xacro')
    #robot_description = {'robot_description' : Command(['xacro', ' ', xacro_path])}

    joystick_config = os.path.join(
        get_package_share_directory('dingo_control'),
        'config',
        'teleop_diff.yaml'
    )

    return LaunchDescription([
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            parameters=[joystick_config],
        ),
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy_node',
            parameters=[joystick_config],
            output='screen'),
    ])

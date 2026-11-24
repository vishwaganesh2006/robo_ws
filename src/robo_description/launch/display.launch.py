from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():

    pkg_name = 'robo_description'

    xacro_file = os.path.join(
        FindPackageShare(pkg_name).find(pkg_name),
        'urdf',
        'robot.xacro'
    )

    robot_description = Command(['xacro ', xacro_file])

    return LaunchDescription([

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),

        Node(
            package='rviz2',
            executable='rviz2'
        )
    ])
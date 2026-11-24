from launch import LaunchDescription
from launch_ros.actions import Node

from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():

    moveit_config = (
        MoveItConfigsBuilder(
            "robo_arm",
            package_name="robo_moveit_config"
        )
        .trajectory_execution(
            file_path="config/moveit_controllers.yaml"
        )
        .to_moveit_configs()
    )

    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",

        parameters=[

            moveit_config.to_dict(),

            {
                "moveit_manage_controllers": False,

                "trajectory_execution.allowed_execution_duration_scaling": 10.0,

                "trajectory_execution.allowed_goal_duration_margin": 10.0,

                "trajectory_execution.allowed_start_tolerance": 1.0,

                "trajectory_execution.execution_duration_monitoring": False,
            }
        ],
    )

    return LaunchDescription([
        move_group_node
    ])
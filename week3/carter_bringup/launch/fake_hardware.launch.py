import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    package_share = FindPackageShare('carter_bringup')
    use_sim_time = LaunchConfiguration('use_sim_time')
    controllers_file = PathJoinSubstitution(
        [package_share, 'config', 'carter_controllers.yaml'])
    xacro_file = PathJoinSubstitution(
        [package_share, 'urdf', 'carter_base.urdf.xacro'])
    robot_description = Command(['xacro ', xacro_file])

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time', default_value='false',
            description='Use simulation time'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'use_sim_time': use_sim_time,
                'robot_description': robot_description,
            }],
            output='screen',
        ),

        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[controllers_file, {'use_sim_time': use_sim_time}],
            output='screen',
        ),

        TimerAction(
            period=2.0,
            actions=[
                Node(
                    package='controller_manager',
                    executable='spawner',
                    arguments=['joint_state_broadcaster'],
                    output='screen',
                )
            ],
        ),

        TimerAction(
            period=3.0,
            actions=[
                Node(
                    package='controller_manager',
                    executable='spawner',
                    arguments=['diff_drive_controller'],
                    output='screen',
                )
            ],
        ),
    ])

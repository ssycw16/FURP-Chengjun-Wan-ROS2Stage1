from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='carter_bringup',
            executable='cmd_vel_watchdog',
            output='screen',
            parameters=[{'timeout': 0.5}],
        ),
    ])

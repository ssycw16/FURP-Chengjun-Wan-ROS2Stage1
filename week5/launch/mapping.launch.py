import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    params_file = os.path.join(package_dir, 'config', 'slam_toolbox_mapping.yaml')
    use_sim_time = LaunchConfiguration('use_sim_time')
    scan_topic = LaunchConfiguration('scan_topic')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time', default_value='false',
            description='Use simulation time'),
        DeclareLaunchArgument(
            'scan_topic', default_value='/scan',
            description='Laser scan topic'),
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[
                params_file,
                {
                    'use_sim_time': use_sim_time,
                    'scan_topic': scan_topic,
                },
            ],
        ),
    ])

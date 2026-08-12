import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    params_file = os.path.join(package_dir, 'config', 'nav2_params.yaml')
    default_map = os.path.join(
        package_dir, '..', 'week5', 'maps', 'map.yaml')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    nav2_launch_file = os.path.join(
        nav2_bringup_dir, 'launch', 'bringup_launch.py')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time', default_value='false',
            description='Use simulation time'),
        DeclareLaunchArgument(
            'map', default_value=default_map,
            description='Map yaml path'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch_file),
            launch_arguments={
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'map': LaunchConfiguration('map'),
                'params_file': params_file,
                'autostart': 'true',
            }.items(),
        ),
    ])

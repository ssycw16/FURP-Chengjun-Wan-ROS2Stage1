import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    global_ekf = os.path.join(
        package_dir, 'config', 'robot_localization_global.yaml')
    navsat = os.path.join(package_dir, 'config', 'navsat_transform.yaml')
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time', default_value='false',
            description='Use simulation time'),
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_global_node',
            output='screen',
            parameters=[global_ekf, {'use_sim_time': use_sim_time}],
        ),
        Node(
            package='robot_localization',
            executable='navsat_transform_node',
            name='navsat_transform_node',
            output='screen',
            parameters=[navsat, {'use_sim_time': use_sim_time}],
            remappings=[
                ('gps/fix', 'fix'),
                ('imu/data', 'imu'),
                ('odometry/filtered', 'odometry/filtered'),
                ('odometry/gps', 'odometry/gps'),
            ],
        ),
    ])

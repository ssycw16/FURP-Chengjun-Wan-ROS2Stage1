import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    repo_dir = os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))

    week3_launch = os.path.join(
        repo_dir,
        'week3', 'carter_bringup', 'launch',
        'fake_hardware.launch.py')
    week4_launch = os.path.join(
        repo_dir, 'week4', 'launch', 'ekf.launch.py')
    week6_launch = os.path.join(
        repo_dir, 'week6', 'launch', 'navigation.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(week3_launch)),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(week4_launch)),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(week6_launch)),
    ])
